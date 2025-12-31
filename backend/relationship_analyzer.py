import ast
import os
import logging
from collections import defaultdict

def path_to_module(filepath, project_root):
    """Wandelt einen Dateipfad in einen Python-Modulpfad um."""
    try:
        rel_path = os.path.relpath(filepath, project_root)
    except ValueError:
        rel_path = os.path.basename(filepath)

    if rel_path.endswith('.py'):
        rel_path = rel_path[:-3]
    module_path = rel_path.replace(os.path.sep, '.')
    if module_path.endswith('.__init__'):
        return module_path[:-9]
    return module_path

class ProjectAnalyzer:
    
    def __init__(self, project_root):
        self.project_root = os.path.abspath(project_root)
        self.definitions = {}
        self.call_graph = defaultdict(list)
        self.file_asts = {} 
        self.ignore_dirs = {'.git', '.venv', 'venv', '__pycache__', 'node_modules', 'dist', 'build', 'docs'}

    def analyze(self):
        py_files = self._find_py_files()
        
        for filepath in py_files:
            self._collect_definitions(filepath)
            
        for filepath in py_files:
            self._resolve_calls(filepath)
            
        self.file_asts.clear()
        
        return self.call_graph

    def get_raw_relationships(self):

        outgoing = defaultdict(set)
        incoming = defaultdict(set)

        for callee_id, callers_info_list in self.call_graph.items():
            for info in callers_info_list:
                caller_id = info['caller']
                
                if caller_id and callee_id:
                    outgoing[caller_id].add(callee_id)
                    incoming[callee_id].add(caller_id)
        
        return {
            "outgoing": {k: sorted(list(v)) for k, v in outgoing.items()},
            "incoming": {k: sorted(list(v)) for k, v in incoming.items()}
        }

    def _find_py_files(self):
        py_files = []
        for root, dirs, files in os.walk(self.project_root):
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))
        return py_files

    def _collect_definitions(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()
                tree = ast.parse(source, filename=filepath)
                
            self.file_asts[filepath] = tree
            module_path = path_to_module(filepath, self.project_root)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    parent = self._get_parent(tree, node)
                    if isinstance(parent, ast.ClassDef):
                        path_name = f"{module_path}.{parent.name}.{node.name}"
                        def_type = 'method'
                    else:
                        path_name = f"{module_path}.{node.name}"
                        def_type = 'function'
                    self.definitions[path_name] = {'file': filepath, 'line': node.lineno, 'type': def_type}
                elif isinstance(node, ast.ClassDef):
                    path_name = f"{module_path}.{node.name}"
                    self.definitions[path_name] = {'file': filepath, 'line': node.lineno, 'type': 'class'}
        except Exception as e:
            logging.error(f"Error collecting definitions in {filepath}: {e}")
            self.file_asts[filepath] = None

    def _get_parent(self, tree, node):
        for parent in ast.walk(tree):
            for child in ast.iter_child_nodes(parent):
                if child is node:
                    return parent
        return None

    def _resolve_calls(self, filepath):
        tree = self.file_asts.get(filepath)
        if not tree:
            return

        try:
            resolver = CallResolverVisitor(filepath, self.project_root, self.definitions)
            resolver.visit(tree)
            
            for callee_pathname, caller_info_list in resolver.calls.items():
                self.call_graph[callee_pathname].extend(caller_info_list)
        except Exception as e:
            logging.error(f"Error resolving calls in {filepath}: {e}")


class CallResolverVisitor(ast.NodeVisitor):
    def __init__(self, filepath, project_root, definitions):
        self.filepath = filepath
        self.module_path = path_to_module(filepath, project_root)
        self.definitions = definitions
        self.scope = {}
        self.instance_types = {}
        self.current_caller_name = self.module_path
        self.current_class_name = None
        self.calls = defaultdict(list)

    def visit_ClassDef(self, node):
        old_class_name = self.current_class_name
        self.current_class_name = node.name
        self.generic_visit(node)
        self.current_class_name = old_class_name

    def visit_FunctionDef(self, node):
        old_caller = self.current_caller_name
        
        if self.current_class_name:
            full_identifier = f"{self.module_path}.{self.current_class_name}.{node.name}"
        else:
            full_identifier = f"{self.module_path}.{node.name}"
            
        self.current_caller_name = full_identifier
        self.generic_visit(node)
        self.current_caller_name = old_caller

    def visit_Call(self, node):
        callee_pathname = self._resolve_call_qname(node.func)
        if callee_pathname and callee_pathname in self.definitions:
            
            if self.current_caller_name == self.module_path:
                caller_type = 'module'
            elif '.<locals>.' in self.current_caller_name:
                caller_type = 'local_function'
            elif self.current_class_name:
                caller_type = 'method'
            else:
                caller_type = 'function'
            
            caller_info = {
                'file': os.path.basename(self.filepath),
                'line': node.lineno,
                'caller': self.current_caller_name,
                'caller_type': caller_type 
            }
            self.calls[callee_pathname].append(caller_info)
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.scope[alias.asname or alias.name] = alias.name
        self.generic_visit(node)
        
    def visit_ImportFrom(self, node):
        module = node.module or ''
        for alias in node.names:
            name = alias.asname or alias.name
            if node.level > 0:
                base = self.module_path.split('.')
                prefix = '.'.join(base[:-node.level])
                full_module_path = f"{prefix}.{module}" if module else prefix
            else:
                full_module_path = module
            self.scope[name] = f"{full_module_path}.{alias.name}"
        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
            class_name = node.value.func.id
            if class_name in self.scope:
                qualified_class_name = self.scope[class_name]
                if qualified_class_name in self.definitions:
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            self.instance_types[target.id] = qualified_class_name
        self.generic_visit(node)

    def _resolve_call_qname(self, func_node):
        if isinstance(func_node, ast.Name):
            name = func_node.id
            if name in self.scope:
                return self.scope[name]
            local_pathname = f"{self.module_path}.{name}"
            if local_pathname in self.definitions:
                return local_pathname
        elif isinstance(func_node, ast.Attribute) and isinstance(func_node.value, ast.Name):
            var_name = func_node.value.id
            method_name = func_node.attr
            if var_name in self.instance_types:
                class_pathname = self.instance_types[var_name]
                return f"{class_pathname}.{method_name}"
            if var_name in self.scope:
                module_pathname = self.scope[var_name]
                return f"{module_pathname}.{method_name}"
        return None
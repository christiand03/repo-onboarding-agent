import ast
import os
from .getRepo import GitRepository

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

class ASTVisitor(ast.NodeVisitor):
    def __init__(self, source_code: str, file_path: str, project_root: str):
        self.source_code = source_code
        self.file_path = file_path
        self.project_root = project_root
        self.module_path = path_to_module(self.file_path, self.project_root)
        self.schema = {"imports": [], "functions": [], "classes": []}
        self._current_class = None

    def visit_Import(self, node):
        for alias in node.names:
            self.schema["imports"].append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.schema["imports"].append(f"{node.module}.{alias.name}")
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        class_identifier = f"{self.module_path}.{node.name}"
        class_info = {
            "mode": "class_analysis",
            "identifier": class_identifier,
            "name": node.name,
            "docstring": ast.get_docstring(node),
            "source_code": ast.get_source_segment(self.source_code, node),
            "start_line": node.lineno,
            "end_line": node.end_lineno,
            "context": {
                "dependencies": [],
                "instantiated_by": [],
                "method_context": []
            },   
        }
        self.schema["classes"].append(class_info)
        self._current_class = class_info 
        self.generic_visit(node)
        self._current_class = None

    def visit_FunctionDef(self, node):
        if self._current_class:
            method_identifier = f"{self._current_class['identifier']}.{node.name}"
            method_context_info = {
                "identifier": method_identifier,
                "name": node.name,
                "calls": [],
                "called_by": [],
                "args": [arg.arg for arg in node.args.args],
                "docstring": ast.get_docstring(node),
                "start_line": node.lineno,
                "end_line": node.end_lineno,
            }
            self._current_class["context"]["method_context"].append(method_context_info)
        else:
            func_identifier = f"{self.module_path}.{node.name}"
            func_info = {
                "mode": "function_analysis",
                "identifier": func_identifier,
                "name": node.name,
                "args": [arg.arg for arg in node.args.args],
                "docstring": ast.get_docstring(node),
                "source_code": ast.get_source_segment(self.source_code, node),
                "start_line": node.lineno,
                "end_line": node.end_lineno,
                "context": {
                    "calls": [],
                    "called_by": []
                }
            }
            self.schema["functions"].append(func_info)
        self.generic_visit(node)
    
    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)


class ASTAnalyzer:

    def __init__(self):
        pass

    def merge_relationship_data(self, full_schema: dict, raw_relationships: dict) -> dict:

        outgoing_calls = raw_relationships.get("outgoing", {})
        incoming_calls = raw_relationships.get("incoming", {})

        for file_path, file_data in full_schema.get("files", {}).items():
            ast_nodes = file_data.get("ast_nodes", {})
            
            for func in ast_nodes.get("functions", []):
                func_id = func.get("identifier")
                if func_id:
                    func["context"]["calls"] = outgoing_calls.get(func_id, [])
                    func["context"]["called_by"] = incoming_calls.get(func_id, [])

            for cls in ast_nodes.get("classes", []):
                cls_id = cls.get("identifier")
                
                if cls_id:
                    cls["context"]["instantiated_by"] = incoming_calls.get(cls_id, [])

                class_dependencies = set()
                
                for method in cls["context"].get("method_context", []):
                    method_id = method.get("identifier")
                    if method_id:
                        m_calls = outgoing_calls.get(method_id, [])
                        method["calls"] = m_calls
                        method["called_by"] = incoming_calls.get(method_id, [])
                        
                        for callee in m_calls:
                            if cls_id and not callee.startswith(f"{cls_id}."):
                                class_dependencies.add(callee)
                
                cls["context"]["dependencies"] = sorted(list(class_dependencies))
        
        return full_schema

    def analyze_repository(self, files: list, repo: GitRepository) -> dict:
        full_schema = {
            "files": {}
        }

        all_paths = [file_obj.path for file_obj in files]
        if not all_paths:
            return full_schema
        
        project_root = os.path.commonpath(all_paths)
        if os.path.isfile(project_root):
            project_root = os.path.dirname(project_root)

        for file_obj in files:
            if not file_obj.path.endswith('.py'):
                continue
            
            file_content = file_obj.content
            if not file_content.strip():
                continue

            try:
                tree = ast.parse(file_content)
                visitor = ASTVisitor(
                    source_code=file_content, 
                    file_path=file_obj.path, 
                    project_root=project_root
                )
                visitor.visit(tree)
                file_schema_nodes = visitor.schema

                if file_schema_nodes["imports"] or file_schema_nodes["functions"] or file_schema_nodes["classes"]:
                    full_schema["files"][file_obj.path] = {
                        "ast_nodes": file_schema_nodes
                    }

            except (SyntaxError, ValueError) as e:
                print(f"Warnung: Konnte Datei '{file_obj.path}' nicht parsen. Fehler: {e}")

        return full_schema
import ast
import networkx as nx

from callgraph import build_callGraph

class ASTVisitor(ast.NodeVisitor):
    def __init__(self, source_code: str,):
        self.source_code = source_code
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
        class_info = {
            "mode": "class_analysis",
            "identifier": node.name, 
            "methods": [],
            "docstring": ast.get_docstring(node),
            "source_code": ast.get_source_segment(self.source_code, node),
            "start_line": node.lineno,
            "end_line": node.end_lineno,
            "context": {
                "dependencies": [],
                "instantiated_by": [],
            },   
        }
        self.schema["classes"].append(class_info)
        
        self._current_class = class_info 
        self.generic_visit(node)
        self._current_class = None

    def visit_FunctionDef(self, node):
        func_info = {
            "mode": "function_analysis",
            "identifier": node.name,
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
        
        if self._current_class:
            self._current_class["methods"].append(func_info)
        else:
            self.schema["functions"].append(func_info)
            
        self.generic_visit(node)
    
    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)

class ASTAnalyzer:

    def __init__(self):
        pass

    @staticmethod
    def _enrich_schema_with_callgraph(schema: dict, call_graph: nx.DiGraph, filename: str):
        for func in schema["functions"]:
            func_name = f"{filename}::{func['identifier']}"
            if func_name in call_graph:
                func['calls'] = sorted(list(call_graph.successors(func_name)))
                func['called_by'] = sorted(list(call_graph.predecessors(func_name)))

        for cls in schema["classes"]:
            for method in cls["methods"]:
                func_name = f"{filename}::{cls['identifier']}::{method['identifier']}"
                if func_name in call_graph:
                    method['context']['calls'] = sorted(list(call_graph.successors(func_name)))
                    method['context']['called_by'] = sorted(list(call_graph.predecessors(func_name)))

    def analyze_repository(self, files: list) -> dict:
        full_schema = {
            "files": {}
        }

        for file_obj in files:
            if not file_obj.path.endswith('.py'):
                continue
            
            file_content = file_obj.content
            if not file_content.strip():
                continue

            try:
                tree = ast.parse(file_content)
                visitor = ASTVisitor(source_code=file_content)
                visitor.visit(tree)
                file_schema_nodes = visitor.schema

                call_graph = build_callGraph(tree, filename=file_obj.path)

                self._enrich_schema_with_callgraph(
                    file_schema_nodes, 
                    call_graph, 
                    file_obj.path
                )

                if file_schema_nodes["imports"] or file_schema_nodes["functions"] or file_schema_nodes["classes"]:
                    full_schema["files"][file_obj.path] = {
                        "ast_nodes": file_schema_nodes
                    }

            except (SyntaxError, ValueError) as e:
                print(f"Warnung: Konnte Datei '{file_obj.path}' nicht parsen. Fehler: {e}")
        
        # Alle Bibliotheken rausfiltern, die nicht selbst im Projekt geschrieben sind
        all_project_functions = set()
        for file_path, file_data in full_schema["files"].items():
            ast_nodes = file_data["ast_nodes"]

            for func in ast_nodes["functions"]:
                func_name = f"{file_path}::{func['identifier']}"
                all_project_functions.add(func_name)

            for cls in ast_nodes["classes"]:
                for method in cls["methods"]:
                    func_name = f"{file_path}::{cls['identifier']}::{method['identifier']}"
                    all_project_functions.add(func_name)
        
        for file_path, file_data in full_schema["files"].items():
            ast_nodes = file_data["ast_nodes"]

            for func in ast_nodes["functions"]:
                func['context']['calls'] = [call for call in func['context']['calls'] if call in all_project_functions]
                func['context']['called_by'] = [caller for caller in func['context']['called_by'] if caller in all_project_functions]
            

            for cls in ast_nodes["classes"]:
                for method in cls["methods"]:
                    method['context']['calls'] = [call for call in method['context']['calls'] if call in all_project_functions]
                    method['context']['called_by'] = [caller for caller in method['context']['called_by'] if caller in all_project_functions]

        return full_schema
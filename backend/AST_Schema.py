import ast

class ASTVisitor(ast.NodeVisitor):

    def __init__(self, source_code: str):
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
            "end_line": node.end_lineno
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
            "end_line": node.end_lineno
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

                if file_schema_nodes["imports"] or file_schema_nodes["functions"] or file_schema_nodes["classes"]:
                    full_schema["files"][file_obj.path] = {
                        "ast_nodes": file_schema_nodes
                    }

            except (SyntaxError, ValueError) as e:
                print(f"Warnung: Konnte Datei '{file_obj.path}' nicht parsen. Fehler: {e}")
        
        return full_schema         
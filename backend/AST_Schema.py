import ast

class ASTVisitor(ast.NodeVisitor):

    def __init__(self):
        self.schema = {"imports": [], "functions": {}, "classes": {}}
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
        self._current_class = node.name
        self.schema["classes"][node.name] = {
            "methods": {},
            "docstring": ast.get_docstring(node),
        }
        self.generic_visit(node)
        self._current_class = None

    def visit_FunctionDef(self, node):
        info = {"args": [arg.arg for arg in node.args.args], "docstring": ast.get_docstring(node)}
        if self._current_class:
            self.schema["classes"][self._current_class]["methods"][node.name] = info
        else:
            self.schema["functions"][node.name] = info
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
                visitor = ASTVisitor()
                visitor.visit(tree)
        
                file_schema_nodes = visitor.schema

                if file_schema_nodes["imports"] or file_schema_nodes["functions"] or file_schema_nodes["classes"]:
                    full_schema["files"][file_obj.path] = {
                        "ast_nodes": file_schema_nodes
                    }

            except (SyntaxError, ValueError, ast.UnparseError) as e:
                print(f"Warnung: Konnte Datei '{file_obj.path}' nicht parsen. Fehler: {e}")
        
        return full_schema         
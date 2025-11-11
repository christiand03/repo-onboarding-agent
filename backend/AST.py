# AST.py

import ast

class PythonASTVisitor(ast.NodeVisitor):
    def __init__(self):
        # Das bisherige Schema speichert die vollen Knoten für die spätere Code-Extraktion.
        self.schema = {"imports": [], "functions": {}, "classes": {}}
        
        # NEU: Ein separates, JSON-kompatibles Schema für Metadaten.
        self.json_schema = {"imports": [], "functions": {}, "classes": {}}
        
        self._current_class = None

    def _extract_function_info(self, node):
        """Hilfsmethode, um JSON-kompatible Infos aus einem Funktionsknoten zu extrahieren."""
        # 'end_lineno' ist erst ab Python 3.8 verfügbar, daher getattr verwenden.
        return {
            "name": node.name,
            "docstring": ast.get_docstring(node),
            "args": [arg.arg for arg in node.args.args],
            "lineno": node.lineno,
            "end_lineno": getattr(node, 'end_lineno', None),
            # Dekoratoren werden als String repräsentiert
            "decorators": [ast.unparse(d) for d in node.decorator_list],
            # Rückgabetyp-Annotation wird als String repräsentiert
            "returns": ast.unparse(node.returns) if node.returns else None
        }

    def visit_Import(self, node):
        for alias in node.names:
            import_name = alias.name
            self.schema["imports"].append(import_name)
            self.json_schema["imports"].append(import_name) # NEU
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            import_name = f"{node.module}.{alias.name}"
            self.schema["imports"].append(import_name)
            self.json_schema["imports"].append(import_name) # NEU
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self._current_class = node.name
        
        # Bisheriges Schema mit vollem AST-Knoten
        self.schema["classes"][node.name] = {
            "node": node,
            "methods": {}
        }
        
        # NEU: JSON-kompatibles Schema mit Metadaten
        self.json_schema["classes"][node.name] = {
            "name": node.name,
            "docstring": ast.get_docstring(node),
            "lineno": node.lineno,
            "end_lineno": getattr(node, 'end_lineno', None),
            "methods": {}
        }
        
        # Methoden für beide Schemata durchlaufen und hinzufügen
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Bisheriges Schema
                self.schema["classes"][node.name]["methods"][child.name] = child
                # NEU: JSON-Schema
                self.json_schema["classes"][node.name]["methods"][child.name] = self._extract_function_info(child)
        
        self._current_class = None

    def visit_FunctionDef(self, node):
        if self._current_class is None:
            # Bisheriges Schema
            self.schema["functions"][node.name] = node
            # NEU: JSON-Schema
            self.json_schema["functions"][node.name] = self._extract_function_info(node)

    def visit_AsyncFunctionDef(self, node):
        if self._current_class is None:
            # Bisheriges Schema
            self.schema["functions"][node.name] = node
            # NEU: JSON-Schema
            self.json_schema["functions"][node.name] = self._extract_function_info(node)


class ASTAnalyzer:
    """
    Analysiert Python-Dateien eines Repositories und extrahiert eine
    strukturierte Übersicht über deren Klassen, Funktionen und Imports
    basierend auf dem Abstract Syntax Tree (AST).
    """
    
    def __init__(self):
        pass

    def analyze_repository(self, files: list, repo_url: str) -> dict:
        """
        Orchestriert die AST-Analyse für eine ganze Liste von Dateien.

        Args:
            files (list): Eine Liste von Objekten, die mindestens die
                          Attribute `.path` (str) und `.content` (str) haben.
            repo_url (str): Die URL des Repositories für die Metadaten.

        Returns:
            dict: Das vollständige, hierarchische AST-Schema für das Repository.
                  Enthält für jede Datei zwei Repräsentationen: eine mit AST-Knoten
                  und eine JSON-kompatible.
        """
        print("\nStarte AST-Analyse...")
        
        full_schema = {
            "repository_url": repo_url,
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
                visitor = PythonASTVisitor()
                visitor.visit(tree)
                
                # Hole beide Schemata vom Visitor ab
                file_schema_nodes = visitor.schema
                file_schema_json = visitor.json_schema

                # Füge die Datei nur hinzu, wenn mindestens eines der Schemata relevante Infos enthält
                if file_schema_nodes["imports"] or file_schema_nodes["functions"] or file_schema_nodes["classes"]:
                    # NEUE STRUKTUR: Speichere beide Versionen
                    full_schema["files"][file_obj.path] = {
                        "ast_nodes": file_schema_nodes,       # Das ursprüngliche Schema mit den AST-Knoten
                        "json_serializable": file_schema_json # Das neue, JSON-kompatible Schema
                    }

            except (SyntaxError, ValueError, ast.UnparseError) as e:
                # Fehlerbehandlung für ungültigen Python-Code oder Probleme beim Unparsing
                print(f"Warnung: Konnte Datei '{file_obj.path}' nicht parsen. Fehler: {e}")
        
        print("AST-Analyse abgeschlossen.")
        return full_schema
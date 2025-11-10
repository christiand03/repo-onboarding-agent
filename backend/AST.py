# AST.py

import ast

class PythonASTVisitor(ast.NodeVisitor):
    def __init__(self):
        # Das Schema speichert jetzt die vollen Knoten statt nur Dictionaries mit Metadaten.
        # Dies ist entscheidend für die spätere Extraktion des Quellcodes.
        self.schema = {"imports": [], "functions": {}, "classes": {}}
        self._current_class = None

    def visit_Import(self, node):
        # Sammelt 'import module' Anweisungen
        for alias in node.names: self.schema["imports"].append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        # Sammelt 'from module import name' Anweisungen
        for alias in node.names: self.schema["imports"].append(f"{node.module}.{alias.name}")
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        # Beginnt die Verarbeitung einer Klasse
        self._current_class = node.name
        
        # Speichert den gesamten AST-Knoten der Klasse
        self.schema["classes"][node.name] = {
            "node": node,
            "methods": {}
        }
        
        # Durchläuft nur die direkten Kinderknoten, um die Methoden zu finden
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Speichert den gesamten AST-Knoten der Methode innerhalb der Klasse
                self.schema["classes"][node.name]["methods"][child.name] = child
        
        # Wichtig: generic_visit() wird hier absichtlich NICHT aufgerufen.
        # Andernfalls würde visit_FunctionDef für die Methoden erneut getriggert
        # und sie würden fälschlicherweise als globale Funktionen registriert.
        
        # Beendet die Verarbeitung der Klasse
        self._current_class = None

    def visit_FunctionDef(self, node):
        # Verarbeitet nur globale Funktionen.
        # Methoden werden bereits in visit_ClassDef behandelt.
        if self._current_class is None:
            # Speichert den gesamten AST-Knoten der Funktion
            self.schema["functions"][node.name] = node
        
        # Kein generic_visit() nötig, da wir nur die Definition selbst sammeln.

    def visit_AsyncFunctionDef(self, node):
        # Funktioniert identisch zu visit_FunctionDef für asynchrone Funktionen.
        if self._current_class is None:
            self.schema["functions"][node.name] = node


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
        """
        print("\nStarte AST-Analyse...")
        
        full_schema = {
            "repository_url": repo_url,
            "files": {}
        }

        for file_obj in files:
            # Nur Python-Dateien analysieren
            if not file_obj.path.endswith('.py'):
                continue
            
            file_content = file_obj.content
            # Leere Dateien überspringen
            if not file_content.strip():
                continue

            try:
                # Den Quellcode in einen AST umwandeln
                tree = ast.parse(file_content)
                
                # Den Visitor erstellen, der den Baum durchläuft
                visitor = PythonASTVisitor()
                visitor.visit(tree)
                
                # Das gesammelte Schema vom Visitor abholen
                file_schema = visitor.schema

                # Das Schema der Datei nur hinzufügen, wenn es relevante Informationen enthält
                if file_schema["imports"] or file_schema["functions"] or file_schema["classes"]:
                    full_schema["files"][file_obj.path] = file_schema

            except (SyntaxError, ValueError) as e:
                # Fehlerbehandlung für ungültigen Python-Code
                print(f"Warnung: Konnte Datei '{file_obj.path}' nicht parsen. Fehler: {e}")
        
        print("AST-Analyse abgeschlossen.")
        return full_schema
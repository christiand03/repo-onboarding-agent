import ast

class PythonASTVisitor(ast.NodeVisitor):
    def __init__(self):
        self.schema = {"imports": [], "functions": {}, "classes": {}}
        self._current_class = None

    # Besuch von Import-Anweisungen
    def visit_Import(self, node):
        # Besucht alle Alias-Namen der Import-Anweisung
        for alias in node.names: self.schema["imports"].append(alias.name)
        # besucht alle untergeordneten Knoten
        self.generic_visit(node)

    # Besuch von From ... Import ... Anweisungen
    def visit_ImportFrom(self, node):
        for alias in node.names: self.schema["imports"].append(f"{node.module}.{alias.name}")
        self.generic_visit(node)

    # Besuch von Klassendefinitionen
    def visit_ClassDef(self, node):
        # Setzt den aktuellen Klassennamen
        self._current_class = node.name
        # Initialisiert den Eintrag für die Klasse im Schema
        self.schema["classes"][node.name] = {"methods": {}, "docstring": ast.get_docstring(node)}
        # Besucht alle untergeordneten Knoten
        self.generic_visit(node)
        # Setzt den aktuellen Klassennamen zurück
        self._current_class = None

    # Besuch von Funktionsdefinitionen        
    def visit_FunctionDef(self, node):
        # Sammelt Informationen über die Funktion
        info = {"args": [arg.arg for arg in node.args.args], "docstring": ast.get_docstring(node)}
        # Fügt die Funktion entweder zur aktuellen Klasse oder zum globalen Funktionsschema hinzu
        if self._current_class:
            self.schema["classes"][self._current_class]["methods"][node.name] = info
        else:
            self.schema["functions"][node.name] = info
        self.generic_visit(node)

class ASTAnalyzer:
    
    def __init__(self):
        pass

    def analyze_repository(self, files: list, repo_url: str) -> dict:
        """
        Orchestriert die Analyse für eine ganze Liste von Dateien.

        Args:
            files (list): Eine Liste von Objekten, die mindestens die
                          Attribute `.path` (str) und `.content` (str) haben.
                          In unserem Fall sind das RepoFile-Objekte.
            repo_url (str): Die URL des Repositories, wird in die Metadaten
                            des Schemas aufgenommen.

        Returns:
            dict: Das vollständige, hierarchische AST-Schema für das Repository.
        """
        print("\nStarte AST-Analyse...")
        
        # 1. Das leere Gesamtschema initialisieren
        full_schema = {
            "repository_url": repo_url,
            "files": {}
        }

        # 2. Über jede gelieferte Datei iterieren
        for file_obj in files:
            
            # 3. Filtern: Uninteressante Dateien sofort überspringen
            if not file_obj.path.endswith('.py'):
                continue
            
            # 4. Daten abrufen (Lazy Loading wird hier durch den Zugriff auf .content ausgelöst)
            file_content = file_obj.content
            if not file_content.strip(): # Leere Dateien auch überspringen
                continue

            # 5. Die Kern-Analyse für eine einzelne Datei durchführen
            try:
                # 5a. Das Spezialwerkzeug: Code-Text in einen AST-Baum umwandeln
                tree = ast.parse(file_content)
                
                # 5b. Den Assistenten (Visitor) für diese eine Datei erstellen
                visitor = PythonASTVisitor()
                
                # 5c. Den Assistenten auf die Reise durch den Baum schicken
                visitor.visit(tree)
                
                # 5d. Das Ergebnis vom Assistenten abholen
                file_schema = visitor.schema

                # 6. Das Ergebnis der Datei dem Gesamtschema hinzufügen
                #    (Nur wenn auch wirklich etwas gefunden wurde)
                if file_schema["imports"] or file_schema["functions"] or file_schema["classes"]:
                    full_schema["files"][file_obj.path] = file_schema

            except (SyntaxError, ValueError) as e:
                # Falls eine Datei ungültigen Python-Code enthält, stürzt das
                # Programm nicht ab, sondern gibt eine Warnung aus und macht weiter.
                print(f"Warnung: Konnte Datei '{file_obj.path}' nicht parsen. Fehler: {e}")
        
        print("AST-Analyse abgeschlossen.")
        return full_schema


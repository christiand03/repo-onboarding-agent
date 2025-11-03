import json
from getRepo import GitRepository, RepoFile
from AST import ASTAnalyzer, PythonASTVisitor


# --- Beispiel für die neue, saubere Verwendung ---
if __name__ == "__main__":
    repo_url = "https://github.com/christiand03/repo-onboarding-agent"

    try:
        # Schritt 1: Der "Zulieferer" wird beauftragt, die Rohmaterialien zu beschaffen.
        # Der `with`-Block stellt sicher, dass am Ende alles aufgeräumt wird.
        with GitRepository(repo_url) as repository:
            print(f"Repository von {repository.repo_url} erfolgreich geklont.")
            
            # Alle Dateien werden als eine Liste von RepoFile-Objekten geholt.
            all_file_objects = repository.get_all_files()
            print(f"Insgesamt {len(all_file_objects)} Dateien im Repository gefunden.")
            
            # Schritt 2: Der "Spezialist" (Analyzer) wird eingestellt.
            analyzer = ASTAnalyzer()
            
            # Schritt 3: Der Spezialist erhält den Auftrag: Analysiere alle gelieferten Dateien.
            # Er bekommt die Liste der Objekte und die URL für die Metadaten.
            repo_ast_schema = analyzer.analyze_repository(all_file_objects, repository.repo_url)
            
            # Schritt 4: Der Geschäftsführer präsentiert den fertigen Analysebericht.
            print("\n--- Vollständiges AST-Schema des Repositories ---")
            
            # Wir benutzen json.dumps, um das komplexe Dictionary schön formatiert auszugeben.
            # indent=2 sorgt für eine lesbare Einrückung.
            print(json.dumps(repo_ast_schema, indent=2))
                
    except RuntimeError as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
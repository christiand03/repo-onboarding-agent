import ast
import json
import os

from getRepo import GitRepository, RepoFile
from AST import ASTAnalyzer, PythonASTVisitor
from callgraph import build_callGraph

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
            
            # Schritt 4: Callgraphs erstellen
            call_graphs = {}
            for file_object in all_file_objects:
                if not file_object.path.endswith(".py"):
                    continue
                tree = ast.parse(file_object.content)
                filename = os.path.basename(file_object.path)
                call_graphs[file_object.path] = build_callGraph(tree, filename=filename)

            # Schritt 5: Der Geschäftsführer präsentiert den fertigen Analysebericht.
            print("\n--- Vollständiges AST-Schema des Repositories ---")
            
            # Wir benutzen json.dumps, um das komplexe Dictionary schön formatiert auszugeben.
            # indent=2 sorgt für eine lesbare Einrückung.
            print(json.dumps(repo_ast_schema, indent=2))
            
            print("\n--- Call-Graph für jede Datei ---")
            for path, graph in call_graphs.items():
                print(f"{path}: {list(graph.edges())}")
                
    except RuntimeError as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
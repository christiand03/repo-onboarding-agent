import ast
import json
import os

from getRepo import GitRepository, RepoFile
from AST import ASTAnalyzer, PythonASTVisitor
# Die neue Funktion importieren
from callgraph import build_callGraph, graph_to_adj_list

# --- Beispiel für die neue, saubere Verwendung ---
if __name__ == "__main__":
    repo_url = "https://github.com/christiand03/repo-onboarding-agent"

    try:
        with GitRepository(repo_url) as repository:
            print(f"Repository von {repository.repo_url} erfolgreich geklont.")
            
            all_file_objects = repository.get_all_files()
            print(f"Insgesamt {len(all_file_objects)} Dateien im Repository gefunden.")
            
            analyzer = ASTAnalyzer()
            
            repo_ast_schema = analyzer.analyze_repository(all_file_objects, repository.repo_url)
            
            # Schritt 4: Callgraphs erstellen
            call_graphs = {}
            json_call_graphs = {} # --- NEU: Separates Dictionary für die JSON-Ausgabe ---
            for file_object in all_file_objects:
                if not file_object.path.endswith(".py"):
                    continue
                try:
                    tree = ast.parse(file_object.content)
                    filename = os.path.basename(file_object.path)
                    
                    # Den Graphen erstellen und im Dictionary speichern
                    graph = build_callGraph(tree, filename=filename)
                    call_graphs[file_object.path] = graph
                    
                    # --- NEU: Den Graphen zusätzlich in das JSON-Format umwandeln ---
                    json_call_graphs[file_object.path] = graph_to_adj_list(graph)
                except SyntaxError as e:
                    print(f"Warnung: Konnte Datei {file_object.path} nicht parsen. Syntaxfehler: {e}")

            # Schritt 5: Der Geschäftsführer präsentiert die fertigen Analyseberichte.
            print("\n--- Vollständiges AST-Schema des Repositories ---")
            print(json.dumps(repo_ast_schema, indent=2))
            
            # Ausgabe der Call-Graphs (Vorschau)
            print("\n--- Call-Graph für jede Datei (Vorschau der Kanten) ---")
            for path, graph in call_graphs.items():
                print(f"{path}: {list(graph.edges())}")

            # Ausgabe im JSON-Format
            print("\n--- Call-Graphen als JSON ---")
            print(json.dumps(json_call_graphs, indent=2))
                
    except RuntimeError as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
import ast
import json
import os

# Stellen Sie sicher, dass die Klassen und Funktionen aus Ihren anderen Dateien importiert werden.
# Wichtig: RepoFile wird von der print_tree_view-Funktion benötigt.
from getRepo import GitRepository, RepoFile
from AST import ASTAnalyzer #, PythonASTVisitor # Visitor wird intern von Analyzer verwendet
from callgraph import build_callGraph, graph_to_adj_list

# ==============================================================================
# HILFSFUNKTION ZUR ANZEIGE DER TREE VIEW
# Diese Funktion gehört in die main.py, da sie nur zur Darstellung dient
# und nicht Teil der Kernlogik der GitRepository-Klasse ist.
# ==============================================================================
def print_tree_view(node, indent=""):
    """
    Gibt eine von get_file_tree() erstellte verschachtelte Dictionary-Struktur
    als lesbaren Verzeichnisbaum in der Konsole aus.
    """
    # Sortiere die Elemente, sodass Verzeichnisse oben stehen und der Rest alphabetisch.
    items = sorted(node.items(), key=lambda item: (not isinstance(item[1], dict), item[0]))
    
    for i, (name, obj) in enumerate(items):
        is_last = i == len(items) - 1
        prefix = "└── " if is_last else "├── "

        if isinstance(obj, dict):
            # Es ist ein Verzeichnis
            print(f"{indent}{prefix}📁 {name}/")
            child_indent = indent + ("    " if is_last else "│   ")
            print_tree_view(obj, child_indent)
        elif isinstance(obj, RepoFile):
            # Es ist eine Datei
            print(f"{indent}{prefix}📄 {name}")


# ==============================================================================
# MAIN-AUSFÜHRUNG
# ==============================================================================
if __name__ == "__main__":
    #repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    repo_url = "https://github.com/pallets/flask"    

    try:
        with GitRepository(repo_url) as repository:
            print(f"Repository von {repository.repo_url} erfolgreich geklont.")
            
            # ==================================================================
            # NEU: TEST DER get_file_tree() FUNKTION
            # ==================================================================
            print("\n--- Verzeichnisstruktur (Tree View) ---")
            
            # 1. Die neue Funktion aus der GitRepository-Klasse aufrufen
            file_tree_structure = repository.get_file_tree()
            
            # 2. Den erhaltenen Baum mit unserer Hilfsfunktion schön ausgeben
            repo_name = os.path.basename(repo_url.removesuffix('.git'))
            print(f"📁 {repo_name}/")
            print_tree_view(file_tree_structure, indent="  ")
            # ==================================================================


            # --- Der Rest des Skripts läuft wie gewohnt weiter ---
            
            print("\n--- Starte nun die detaillierte Code-Analyse... ---")
            
            all_file_objects = repository.get_all_files()
            print(f"Insgesamt {len(all_file_objects)} Dateien im Repository für die Analyse gefunden.")
            
            analyzer = ASTAnalyzer()
            
            repo_ast_schema = analyzer.analyze_repository(all_file_objects, repository.repo_url)
            
            # Callgraphs erstellen
            call_graphs = {}
            json_call_graphs = {}
            for file_object in all_file_objects:
                if not file_object.path.endswith(".py"):
                    continue
                try:
                    tree = ast.parse(file_object.content)
                    filename = os.path.basename(file_object.path)
                    
                    graph = build_callGraph(tree, filename=filename)
                    call_graphs[file_object.path] = graph
                    
                    json_call_graphs[file_object.path] = graph_to_adj_list(graph)
                except SyntaxError as e:
                    print(f"Warnung: Konnte Datei {file_object.path} nicht parsen. Syntaxfehler: {e}")

            # Ergebnisse der Analyse ausgeben
            print("\n--- Vollständiges AST-Schema des Repositories (JSON) ---")
            # Die Ausgabe kann sehr lang sein, daher ist es oft besser, sie zu überspringen
            # print(json.dumps(repo_ast_schema, indent=2))
            print("AST-Schema wurde erfolgreich generiert (JSON-Ausgabe übersprungen).")
            
            # Ausgabe der Call-Graphs
            print("\n--- Call-Graphen als Adjazenzlisten (JSON) ---")
            #print(json.dumps(json_call_graphs, indent=2))
                
    except RuntimeError as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
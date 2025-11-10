# main.py

import ast
import json
import os

# Stellen Sie sicher, dass die Klassen und Funktionen aus Ihren anderen Dateien importiert werden.
# Wichtig: RepoFile wird von der print_tree_view-Funktion benötigt.
from getRepo import GitRepository, RepoFile
from AST import ASTAnalyzer
from callgraph import build_callGraph, graph_to_adj_list
from basic_info import ProjektInfoExtractor

# ==============================================================================
# HILFSFUNKTIONEN ZUR ANZEIGE
# ==============================================================================
def print_tree_view(node, indent=""):
    """
    Gibt eine von get_file_tree() erstellte verschachtelte Dictionary-Struktur
    als lesbaren Verzeichnisbaum in der Konsole aus.
    """
    items = sorted(node.items(), key=lambda item: (not isinstance(item[1], dict), item[0]))
    
    for i, (name, obj) in enumerate(items):
        is_last = i == len(items) - 1
        prefix = "└── " if is_last else "├── "

        if isinstance(obj, dict):
            print(f"{indent}{prefix}📁 {name}/")
            child_indent = indent + ("    " if is_last else "│   ")
            print_tree_view(obj, child_indent)
        elif isinstance(obj, RepoFile):
            print(f"{indent}{prefix}📄 {name}")

def print_basic_info(info: dict):
    """Gibt die extrahierten Basis-Informationen formatiert aus."""
    print("\n--- Basis-Informationen zum Projekt ---")
    
    # Projektübersicht
    overview = info.get("projekt_uebersicht", {})
    print("\n[ Projektübersicht ]")
    print(f"  Titel:             {overview.get('titel')}")
    print(f"  Beschreibung:      {overview.get('beschreibung')}")
    print(f"  Aktueller Status:  {overview.get('aktueller_status')}")
    print(f"  Key Features:\n{overview.get('key_features')}")
    print(f"\n  Tech Stack:\n{overview.get('tech_stack')}")
    
    # Installation
    installation = info.get("installation", {})
    print("\n[ Installation ]")
    print(f"  Benötigte Dependencies:\n{installation.get('dependencies')}")
    print(f"\n  Setup-Anleitung:\n{installation.get('setup_anleitung')}")
    print(f"\n  Quick Start Guide:\n{installation.get('quick_start_guide')}")
    print("-" * 40)


# ==============================================================================
# MAIN-AUSFÜHRUNG
# ==============================================================================
if __name__ == "__main__":
    #repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    repo_url = "https://github.com/pallets/flask"    

    try:
        with GitRepository(repo_url) as repository:
            print(f"Repository von {repository.repo_url} erfolgreich geklont.")
            
            # Die Dateiliste wird jetzt am Anfang geholt, damit sie für alle Analysen verfügbar ist
            all_file_objects = repository.get_all_files()
            
            # ==================================================================
            # 1. Basis-Informationen extrahieren und ausgeben
            # ==================================================================
            info_extractor = ProjektInfoExtractor()
            basic_project_info = info_extractor.extrahiere_info(all_file_objects, repo_url)
            print_basic_info(basic_project_info)
            # Sie können die Daten auch als JSON haben:
            # print(json.dumps(basic_project_info, indent=2, ensure_ascii=False))


            # ==================================================================
            # 2. Verzeichnisstruktur anzeigen
            # ==================================================================
            print("\n--- Verzeichnisstruktur (Tree View) ---")
            file_tree_structure = repository.get_file_tree()
            repo_name = os.path.basename(repo_url.removesuffix('.git'))
            print(f"📁 {repo_name}/")
            print_tree_view(file_tree_structure, indent="  ")


            # ==================================================================
            # 3. Detaillierte Code-Analyse durchführen
            # ==================================================================
            print("\n--- Starte nun die detaillierte Code-Analyse... ---")
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
            print("AST-Schema wurde erfolgreich generiert (JSON-Ausgabe übersprungen).")
            
            print("\n--- Call-Graphen als Adjazenzlisten (JSON) ---")
            print("Call-Graphen wurden erfolgreich generiert (JSON-Ausgabe übersprungen).")
                
    except RuntimeError as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
import ast
import json
import os
from typing import Tuple, Dict, Any, Optional
from langchain.tools import tool

# --- GEÄNDERTE IMPORTS ---
# Relative Imports für Module im selben "backend"-Paket
from getRepo import GitRepository
from AST import ASTAnalyzer
from callgraph import build_callGraph, graph_to_adj_list
from basic_info import ProjektInfoExtractor
# Dieser Import ist korrekt, WENN das Projekt-Root im Suchpfad ist
from schemas.types import FunctionAnalysis

@tool
def analyze_repository(repo_url: str) -> Tuple[Optional[Dict[str, Any]], Dict[str, Any]]:
    """
    Analysiert ein Git-Repository umfassend.

    Diese Funktion klont das angegebene Repository, extrahiert Basis-Informationen,
    analysiert die Verzeichnisstruktur, führt eine AST-Analyse für Python-Dateien durch
    und erstellt Call-Graphen.

    Args:
        repo_url (str): Die URL des zu analysierenden Git-Repositories.

    Returns:
        Tuple[Optional[Dict[str, Any]], Dict[str, Any]]:
        - Das erste Element ist ein Dictionary mit den Analyseergebnissen ('basic_info', 
          'file_tree', 'ast_schema', 'call_graphs') oder None bei einem Fehler.
        - Das zweite Element ist ein Dictionary, das diese Funktion selbst beschreibt
          und dem `FunctionAnalysis`-Schema entspricht, inklusive eines Fehlerfeldes.
    """
    analysis_results = {}
    
    # Metadaten für die Beschreibung dieser Funktion selbst (für die Pydantic-Validierung)
    meta_function_analysis_data = {
        "identifier": "tool.analyze_repository",
        "description": {
            "overall": "Clones a Git repository, performs a comprehensive analysis (basic info, AST, call graphs), and returns the consolidated results.",
            "parameters": [
                {
                    "name": "repo_url",
                    "type": "str",
                    "description": "The URL of the Git repository to be analyzed."
                }
            ],
            "returns": [
                {
                    "name": "analysis_results",
                    "type": "Tuple[Optional[Dict[str, Any]], Dict[str, Any]]",
                    "description": "A tuple containing the analysis dictionary and a self-descriptive dictionary for validation."
                }
            ],
            "usage_context": {
                "calls": [
                    "GitRepository", "ProjektInfoExtractor.extrahiere_info",
                    "ASTAnalyzer.analyze_repository", "build_callGraph", "graph_to_adj_list"
                ],
                "called_by": ["main_script", "api_endpoint"]
            }
        },
        "error": None
    }

    try:
        with GitRepository(repo_url) as repository:
            print(f"Repository von {repository.repo_url} erfolgreich geklont.")
            
            all_file_objects = repository.get_all_files()
            
            # 1. Basis-Informationen extrahieren
            info_extractor = ProjektInfoExtractor()
            basic_project_info = info_extractor.extrahiere_info(all_file_objects, repo_url)
            analysis_results['basic_info'] = basic_project_info
            
            # 2. Verzeichnisstruktur
            file_tree_structure = repository.get_file_tree()
            # Hinweis: Die Baumstruktur enthält RepoFile-Objekte, die nicht direkt JSON-serialisierbar sind.
            # Für eine reine Datenstruktur müsste man dies umwandeln. Hier behalten wir es für die Logik.
            # Für den Output fügen wir eine vereinfachte Version hinzu.
            repo_name = os.path.basename(repo_url.removesuffix('.git'))
            def simplify_tree(node):
                simple_node = {}
                for name, obj in node.items():
                    if isinstance(obj, dict):
                        simple_node[name] = simplify_tree(obj)
                    else: # Es ist ein RepoFile
                        simple_node[name] = f"File: {obj.path}"
                return simple_node
            analysis_results['file_tree'] = {repo_name: simplify_tree(file_tree_structure)}


            # 3. Detaillierte Code-Analyse (AST)
            analyzer = ASTAnalyzer()
            repo_ast_schema = analyzer.analyze_repository(all_file_objects, repository.repo_url)
            # Hinweis: Das AST-Schema enthält AST-Knoten, die nicht JSON-serialisierbar sind.
            # Für einen reinen Daten-Output wäre eine Konvertierung notwendig.
            analysis_results['ast_schema'] = "AST schema generated (complex object not shown)"


            # 4. Call-Graphen erstellen
            json_call_graphs = {}
            for file_object in all_file_objects:
                if not file_object.path.endswith(".py"):
                    continue
                try:
                    tree = ast.parse(file_object.content)
                    graph = build_callGraph(tree, filename=file_object.path)
                    json_call_graphs[file_object.path] = graph_to_adj_list(graph)
                except SyntaxError as e:
                    print(f"Warnung: Konnte Datei {file_object.path} nicht parsen. Syntaxfehler: {e}")
            analysis_results['call_graphs'] = json_call_graphs

        return analysis_results, meta_function_analysis_data

    except Exception as e:
        print(f"Ein schwerwiegender Fehler ist aufgetreten: {e}")
        meta_function_analysis_data["error"] = f"A critical error occurred: {str(e)}"
        return None, meta_function_analysis_data
    

# main.py

import json
from pydantic import ValidationError

# --- GEÄNDERTE IMPORTS ---
# Absoluter Import vom Projekt-Root aus
from schemas.types import FunctionAnalysis

# ==============================================================================
# MAIN-AUSFÜHRUNG
# ==============================================================================
if __name__ == "__main__":
    repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    #repo_url = "https://github.com/pallets/flask"

    # 1. Rufe die zentrale Analyse-Funktion auf
    analysis_results, validation_output = analyze_repository(repo_url)
    
    # 2. Verarbeite die Ergebnisse
    if analysis_results:
        print("\n\nAnalyse erfolgreich abgeschlossen!")
        print("-" * 40)
        
        # Gib einen Teil der Ergebnisse als Beispiel aus
        print("\n--- Basis-Informationen zum Projekt ---")
        print(json.dumps(analysis_results.get("basic_info"), indent=2, ensure_ascii=False))
        
        print("\n--- Call-Graphen (Auszug) ---")
        # Zeige den Call-Graphen für eine der ersten gefundenen Dateien
        first_file_with_graph = next(iter(analysis_results.get("call_graphs", {})), None)
        if first_file_with_graph:
            print(f"Call-Graph für: {first_file_with_graph}")
            print(json.dumps(analysis_results["call_graphs"][first_file_with_graph], indent=2))
        else:
            print("Keine Call-Graphen generiert.")
        
        print("-" * 40)
    else:
        print("\n\nAnalyse fehlgeschlagen. Details siehe oben.")

    # 3. Validiere den Output gegen das Pydantic-Modell
    print("\n--- Validiere den Output der Analyse-Funktion ---")
    try:
        # Pydantic validiert das Dictionary, das unsere Funktion beschreibt
        function_analysis_instance = FunctionAnalysis.model_validate(validation_output)
        
        print("Validierung erfolgreich!")
        print(f"Identifier: {function_analysis_instance.identifier}")
        print(f"Overall Description: {function_analysis_instance.description.overall}")
        if function_analysis_instance.error:
            print(f"Reported Error: {function_analysis_instance.error}")

    except ValidationError as e:
        print("Validierung fehlgeschlagen!")
        print(e)
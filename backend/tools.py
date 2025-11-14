# tools.py

import ast
import os
from typing import List, Dict, Any, Tuple

# --- IMPORTS ---
# Stelle sicher, dass der Pfad zum 'schemas' Verzeichnis korrekt ist
# Wenn 'tools.py' in 'backend' liegt und 'schemas' im Projekt-Root,
# könnte dieser Import fehlschlagen. Gegebenenfalls anpassen.
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from getRepo import GitRepository
from AST import ASTAnalyzer
from callgraph import build_callGraph, graph_to_adj_list
# Der Import von ProjektInfoExtractor ist für diese Aufgabe nicht mehr nötig.
# from basic_info import ProjektInfoExtractor

# Die Pydantic-Modelle, nach denen wir unsere Ausgabe formatieren
from schemas.types import FunctionAnalysisInput, ClassAnalysisInput, FunctionContextInput, ClassContextInput

def _consolidate_call_graph_data(call_graphs_per_file: Dict[str, Dict[str, List[str]]]) -> Dict[str, Dict[str, List[str]]]:
    """
    PRIVATE: Wandelt die Call-Graph-Daten um, um schnellen Zugriff auf 'calls'
    und 'called_by' für jede Funktion/Methode im gesamten Repository zu ermöglichen.

    Args:
        call_graphs_per_file: Ein Dictionary, bei dem der Schlüssel der Dateipfad und
                              der Wert die Adjazenzliste des Call-Graphen ist.

    Returns:
        Ein Dictionary, bei dem jeder Schlüssel ein eindeutiger Funktions-Identifier ist
        (z.B. 'src/main.py::my_function') und der Wert ein Dictionary mit den Listen
        'calls' und 'called_by' ist.
    """
    # Schritt 1: Erstelle eine globale Liste aller Aufrufe (calls)
    global_calls = {}
    for file_path, adj_list in call_graphs_per_file.items():
        for caller_name, callees in adj_list.items():
            # Erstelle eindeutige Identifier für den Caller
            # Annahme: Methoden sind noch nicht mit Klassennamen qualifiziert
            caller_id = f"{file_path}::{caller_name}"
            global_calls[caller_id] = callees # Wir speichern hier nur die Namen der aufgerufenen Fkt.

    # Schritt 2: Baue das finale Look-up-Dictionary inklusive 'called_by' (Invertierung)
    consolidated_data = {func_id: {"calls": calls, "called_by": []} for func_id, calls in global_calls.items()}

    # Fülle 'called_by', indem du durch alle Aufrufe iterierst
    for caller_id, callees in global_calls.items():
        for callee_name in callees:
            # Finde alle möglichen Identifier für den Callee im gesamten Projekt
            # Dies ist eine Vereinfachung. Eine exakte Auflösung wäre komplexer.
            for potential_callee_id in consolidated_data:
                if potential_callee_id.endswith(f"::{callee_name}"):
                    consolidated_data[potential_callee_id]["called_by"].append(caller_id)

    return consolidated_data


def prepare_llm_inputs_from_repo(repo_url: str) -> Tuple[List[Dict[str, Any]], str]:
    """
    Analysiert ein Git-Repository und bereitet eine Liste von strukturierten
    Eingabedaten für den LLMHelper vor. Jedes Element in der Liste entspricht
    entweder einem FunctionAnalysisInput oder einem ClassAnalysisInput Schema.

    Args:
        repo_url (str): Die URL des zu analysierenden Git-Repositories.

    Returns:
        Eine Liste von Dictionaries, die als "Arbeitspakete" für das LLM dienen.
        Ein String, der den lokalen Pfad zum geklonten Repository angibt.
    """
    llm_input_packages = []
    repo_path = ""

    try:
        with GitRepository(repo_url) as repository:
            repo_path = repository.temp_dir
            print(f"Repository von {repository.repo_url} erfolgreich geklont nach {repo_path}.")
            
            all_file_objects = repository.get_all_files()
            
            # 1. AST-Analyse für das gesamte Repository durchführen
            ast_analyzer = ASTAnalyzer()
            # Diese Analyse enthält jetzt für jede Datei die AST-Knoten und eine JSON-Version
            ast_results = ast_analyzer.analyze_repository(all_file_objects, repository.repo_url)

            # 2. Call-Graphen für das gesamte Repository erstellen
            call_graphs = {}
            for file_obj in all_file_objects:
                if not file_obj.path.endswith(".py"):
                    continue
                try:
                    tree = ast.parse(file_obj.content)
                    graph = build_callGraph(tree, filename=file_obj.path, file_content=file_obj.content)
                    call_graphs[file_obj.path] = graph_to_adj_list(graph)
                except SyntaxError as e:
                    print(f"Warnung: Konnte Call-Graph für {file_obj.path} nicht erstellen. Syntaxfehler: {e}")

            # 3. Call-Graph-Daten für einfachen Zugriff konsolidieren
            # Wir benötigen diese Information, um den 'context' für jede Funktion zu füllen
            call_context_map = _consolidate_call_graph_data(call_graphs)

            # 4. Arbeitspakete für LLM generieren durch Iteration über die AST-Ergebnisse
            for file_path, file_data in ast_results.get("files", {}).items():
                
                ast_nodes = file_data["ast_nodes"]
                file_imports = ast_nodes.get("imports", [])

                # A. Arbeitspakete für einzelne Funktionen erstellen
                for func_name, func_node in ast_nodes.get("functions", {}).items():
                    identifier = f"{file_path}::{func_name}"
                    context_info = call_context_map.get(identifier, {"calls": [], "called_by": []})
                    
                    try:
                        func_input = FunctionAnalysisInput(
                            mode="function_analysis",
                            identifier=identifier,
                            source_code=ast.unparse(func_node), # Wandelt AST-Knoten zurück in Code
                            imports=file_imports,
                            context=FunctionContextInput(
                                calls=context_info["calls"],
                                called_by=context_info["called_by"]
                            )
                        )
                        llm_input_packages.append(func_input.model_dump())
                    except Exception as e:
                        print(f"Fehler beim Erstellen des Pakets für Funktion {identifier}: {e}")

                # B. Arbeitspakete für Klassen erstellen
                for class_name, class_info in ast_nodes.get("classes", {}).items():
                    class_node = class_info["node"]
                    identifier = f"{file_path}::{class_name}"

                    # Sammle die eindeutigen Identifier aller Methoden dieser Klasse
                    method_ids_for_class = [
                        f"{file_path}::{method_name}" for method_name in class_info.get("methods", {})
                    ]

                    method_callers = set()
                    for method_id in method_ids_for_class:
                        # Achtung: Der call_context_map-Identifier muss genau passen.
                        # Im callgraph visitor wird der Klassenkontext noch nicht erfasst,
                        # daher ist ein einfacher f"{file_path}::{method_name}" wahrscheinlich richtig.
                        context_info = call_context_map.get(method_id, {"called_by": []})
                        for caller in context_info["called_by"]:
                            method_callers.add(caller)

                    try:
                        class_input = ClassAnalysisInput(
                            mode="class_analysis",
                            identifier=identifier,
                            source_code=ast.unparse(class_node),
                            imports=file_imports,
                            context=ClassContextInput(
                                dependencies=file_imports,
                                instantiated_by=list(method_callers),
                                methods_analysis=[],
                                method_identifiers=method_ids_for_class  # <-- DIESE ZEILE MUSS EXISTIEREN!
                            )
                        )
                        llm_input_packages.append(class_input.model_dump())
                    except Exception as e:
                        print(f"Fehler beim Erstellen des Pakets für Klasse {identifier}: {e}")

        return llm_input_packages, repo_path

    except Exception as e:
        print(f"Ein schwerwiegender Fehler ist in 'prepare_llm_inputs_from_repo' aufgetreten: {e}")
        return [], ""

# ==============================================================================
# Beispiel-Aufruf zum Testen
# ==============================================================================
if __name__ == "__main__":
    import json
    
    # Eine URL zu einem kleinen, öffentlichen Python-Repository
    # TEST_REPO_URL = "https://github.com/pallets/flask" # Sehr groß!
    TEST_REPO_URL = "https://github.com/christiand03/repo-onboarding-agent" # Mittelgroß
    # TEST_REPO_URL = "https://github.com/tiangolo/fastapi" # Sehr groß!
    
    print(f"Analysiere Test-Repository: {TEST_REPO_URL}")
    
    # Rufe die neue Funktion auf
    llm_jobs, local_path = prepare_llm_inputs_from_repo(TEST_REPO_URL)
    
    if llm_jobs:
        print(f"\n\nAnalyse erfolgreich. {len(llm_jobs)} Arbeitspakete für das LLM erstellt.")
        print(f"Repository befindet sich unter: {local_path}")
        
        # Finde ein Beispiel für eine Funktion und eine Klasse zur Ausgabe
        sample_function = next((job for job in llm_jobs if job['mode'] == 'function_analysis'), None)
        sample_class = next((job for job in llm_jobs if job['mode'] == 'class_analysis'), None)
        
        print("\n--- Beispiel-Arbeitspaket für eine Funktion ---")
        if sample_function:
            print(json.dumps(sample_function, indent=2))
        else:
            print("Keine Funktion gefunden.")
            
        print("\n--- Beispiel-Arbeitspaket für eine Klasse ---")
        if sample_class:
            print(json.dumps(sample_class, indent=2))
        else:
            print("Keine Klasse gefunden.")

    else:
        print("\nAnalyse fehlgeschlagen. Keine Arbeitspakete erstellt.")
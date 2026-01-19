import json
import math
import logging
import os
import re
import time
from datetime import datetime
import matplotlib.pyplot as plt
import sys 
import tiktoken
from typing import Any

from pathlib import Path
from dotenv import load_dotenv

sys.path.append(str(Path(__file__).parent))
from .diagram_generation import (
    generator
)
from .getRepo import GitRepository
from .AST_Schema import ASTAnalyzer
from .MainLLM import MainLLM
from .basic_info import ProjektInfoExtractor
from .HelperLLM import LLMHelper
from .relationship_analyzer import ProjectAnalyzer
from schemas.types import FunctionContextInput, FunctionAnalysisInput, ClassContextInput, ClassAnalysisInput, MethodContextInput

from ptoon import encode, estimate_savings

from .converter import process_repo_notebooks


# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path):
    """Erstellt ein Balkendiagramm für den Token-Vergleich und speichert es."""
    labels = ['JSON', 'TOON']
    values = [json_tokens, toon_tokens]
    colors = ['#ff9999', '#66b3ff']

    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, values, color=colors, width=0.5)

    # Titel und Beschriftungen
    plt.title(f'Token-Vergleich: {savings_percent:.2f}% Einsparung', fontsize=14)
    plt.ylabel('Anzahl Token')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Werte über den Balken anzeigen
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, 
                 f'{int(height):,}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Speichern
    plt.savefig(output_path)
    plt.close()

def calculate_net_time(start_time, end_time, total_items, batch_size, model_name):
    """Berechnet die Dauer abzüglich der Sleep-Zeiten für Rate-Limits."""
    total_duration = end_time - start_time
    
    if not model_name.startswith("gemini-"):
        return total_duration

    if total_items == 0:
        return 0

    num_batches = math.ceil(total_items / batch_size)
    sleep_count = max(0, num_batches - 1)
    total_sleep_time = sleep_count * 61
    
    net_time = total_duration - total_sleep_time
    return max(0, net_time)


def main_workflow(user_input, api_keys: dict, model_names: dict, status_callback=None, check_stop=None):
    
    def update_status(msg):
        # --- NEU: Prüfen ob abgebrochen wurde ---
        if check_stop and check_stop():
            logging.info("Interrupt empfangen. Breche main_workflow ab.")
            raise InterruptedError("Analyse wurde vom User gestoppt.")
        
        if status_callback:
            status_callback(msg)
        logging.info(msg)

    update_status("🔍 Analysiere Input...")
    
    # API Keys & URLs extrahieren
    gemini_api_key = api_keys.get("gemini")
    openai_api_key = api_keys.get("gpt")
    scadsllm_api_key = api_keys.get("scadsllm")
    scadsllm_base_url = api_keys.get("scadsllm_base_url")
    ollama_base_url = api_keys.get("ollama")
    
    # User-eigene Open Source Konfiguration
    user_opensrc_key = api_keys.get("opensrc_key")
    user_opensrc_url = api_keys.get("opensrc_url")

    helper_model = model_names.get("helper", "gemini-2.0-flash-lite")
    main_model = model_names.get("main", "gemini-2.0-pro")

    def get_key_and_url(model_name):
        """Bestimmt pro Modell den richtigen Key und die richtige Base URL."""
        if model_name.startswith("gpt-"):
            return openai_api_key, None
        
        if model_name.startswith("gemini-"):
            # NUR wenn es wirklich mit gemini- anfängt, wird der Gemini Key erzwungen
            if not gemini_api_key:
                raise ValueError(f"Gemini API Key fehlt für Modell {model_name}")
            return gemini_api_key, None
        
        if model_name == "llama3":
            return None, ollama_base_url
        
        # Logik für Open Source / ScadsLLM / Aliasse
        # Falls der User in der UI einen eigenen OS-Key/URL hinterlegt hat, nimm diesen
        if user_opensrc_url:
            return user_opensrc_key, user_opensrc_url
            
        # Sonst Fallback auf System-ScadsLLM
        return scadsllm_api_key, scadsllm_base_url

    # Zuweisung für Helper und Main
    helper_api_key, helper_base_url = get_key_and_url(helper_model)
    main_api_key, main_base_url = get_key_and_url(main_model)    

    # Error Handling für fehlende API Keys
    if not gemini_api_key and "gemini" in helper_model:
        raise ValueError("Gemini API Key was not provided in api_keys dictionary.")

    # URL Extraktion
    repo_url = None
    url_pattern = r"https?://(?:www\.)?github\.com/[^\s]+"
    match = re.search(url_pattern, user_input)

    if match:
        repo_url = match.group(0)
        logging.info(f"Extracted repository URL: {repo_url}")
    else:
        raise ValueError("Could not find a valid URL in the provided input.")
    
    # Repo klonen und Dateien extrahieren
    update_status(f"⬇️ Klone Repository: {repo_url} ...")
    
    repo_files = []
    local_repo_path = "" 

    try: 

        with GitRepository(repo_url) as repo:
            repo_files = repo.get_all_files()
            local_repo_path = repo.temp_dir

            logging.info(f"Total files retrieved: {len(repo_files)}")

    except Exception as e:
        logging.error(f"Error cloning repository: {e}")
        raise 


    # Extrahiere Basic Infos
    update_status("ℹ️ Extrahiere Basis-Informationen...")
    try:
        info_extractor = ProjektInfoExtractor()
        basic_project_info = info_extractor.extrahiere_info(dateien=repo_files, repo_url=repo_url)
        logging.info("Basic project info extracted")
    except Exception as e:
        logging.error(f"Error extracting basic project info: {e}")
        basic_project_info = "Could not extract basic info."

    # Erstelle Repository Dateibaum
    update_status("🌲 Erstelle Repository Dateibaum...")
    try:
        repo_file_tree = repo.get_file_tree()
        logging.info("Repository file tree constructed")
    except Exception as e:
        logging.error(f"Error constructing repository file tree: {e}")
        repo_file_tree = "Could not create file tree."

    # Relationship Analyse durchführen
    update_status("🔗 Analysiere Beziehungen (Calls & Instanziierungen)...")
    try:
        rel_analyzer = ProjectAnalyzer(project_root=local_repo_path)
        rel_analyzer.analyze()
        
        raw_relationships = rel_analyzer.get_raw_relationships()
        
        logging.info("Relationships analyzed.")
    except Exception as e:
        logging.error(f"Error in relationship analyzer: {e}")
        raw_relationships = {"outgoing": {}, "incoming": {}}

    # Erstelle AST Schema
    update_status("🌳 Erstelle Abstract Syntax Tree (AST)...")
    try:        
        ast_analyzer = ASTAnalyzer()   
        ast_schema = ast_analyzer.analyze_repository(files=repo_files, repo=repo)
        logging.info("AST schema created")
    except Exception as e:
        logging.error(f"Error retrieving repository files: {e}")
        raise

    # Anreichern des AST Schemas mit Relationship Daten
    update_status("➕ Reiche AST mit Beziehungsdaten an...")            
    try:   
        ast_schema = ast_analyzer.merge_relationship_data(ast_schema, raw_relationships)
        logging.info("AST schema created and enriched")

    except Exception as e:
        logging.error(f"Error processing repository: {e}")
        raise

    # Vorbereitung der HelperLLM Eingaben
    update_status("⚙️ Bereite Daten für Helper LLM vor...")
    
    helper_llm_function_input = []
    helper_llm_class_input = []

    try:
        for filename, file_data in ast_schema['files'].items():
            ast_nodes = file_data.get('ast_nodes', {})
            imports = ast_nodes.get('imports', [])
            functions = ast_nodes.get('functions', [])
            classes = ast_nodes.get('classes', [])

            for function in functions:
                context = function.get('context', {})
                
                raw_called_by = context.get('called_by', [])
                clean_called_by = [cb for cb in raw_called_by if isinstance(cb, dict)]

                function_context = FunctionContextInput(
                    calls = context.get('calls', []),
                    called_by = clean_called_by 
                )
                
                function_input = FunctionAnalysisInput(
                    mode = function.get('mode', 'function_analysis'),
                    identifier = function.get('identifier'),
                    source_code = function.get('source_code'),
                    imports = imports,
                    context = function_context
                )
                
                helper_llm_function_input.append(function_input)

            for _class in classes:
                context = _class.get('context', {})
                
                method_context_inputs = []
                for method in context.get('method_context', []):
                    
                    raw_method_called_by = method.get('called_by', [])
                    clean_method_called_by = [cb for cb in raw_method_called_by if isinstance(cb, dict)]

                    method_context_inputs.append(
                        MethodContextInput(
                            identifier=method.get('identifier'),
                            calls=method.get('calls', []),
                            called_by=clean_method_called_by, 
                            args=method.get('args', []),
                            docstring=method.get('docstring')
                        )
                    )

                raw_instantiated_by = context.get('instantiated_by', [])
                clean_instantiated_by = [ib for ib in raw_instantiated_by if isinstance(ib, dict)]

                class_context = ClassContextInput(
                    dependencies = context.get('dependencies', []),
                    instantiated_by = clean_instantiated_by, 
                    method_context = method_context_inputs
                )

                class_input = ClassAnalysisInput(
                    mode = _class.get('mode', 'class_analysis'),
                    identifier =_class.get('identifier'),
                    source_code = _class.get('source_code'), 
                    imports = imports, 
                    context = class_context
                )
                
                helper_llm_class_input.append(class_input)

    except Exception as e:
        logging.error(f"Error preparing inputs for Helper LLM: {e}")
        raise
    
    # Initialisiere HelperLLM
    function_prompt_file = 'SystemPrompts/SystemPromptFunctionHelperLLM.txt'
    class_prompt_file = 'SystemPrompts/SystemPromptClassHelperLLM.txt'
    prompt_file_mainllm_toon = "SystemPrompts/SystemPromptMainLLMToon.txt"

    llm_input_estimate = {
        "functions": helper_llm_function_input,
        "classes": helper_llm_class_input,
        "ast_schema": ast_schema,
        "basic_info": basic_project_info,
        "file_tree": repo_file_tree,
        "function_prompt": function_prompt_file,
        "class_prompt": class_prompt_file,
        "main_prompt": prompt_file_mainllm_toon
    }

    if ollama_base_url:
        os.environ["OLLAMA_BASE_URL"] = ollama_base_url

    llm_helper = LLMHelper(
        api_key=helper_api_key, 
        function_prompt_path=function_prompt_file, 
        class_prompt_path=class_prompt_file,
        model_name=helper_model,
        base_url=helper_base_url,
    )
    if gemini_api_key or openai_api_key:
        logging.info("Time estimation for documentation generation...")
        tokens_llm = estimate_total_tokens(llm_input_estimate)
        time_llm = math.ceil(tokens_llm / 550 / 60)
        update_status(f"Die voraussichtliche verbleibende Analyse-Zeit beträgt: {time_llm} Minuten.")
    elif user_opensrc_key:
        logging.info("Time estimation for documentation generation...")
        update_status("Die voraussichtliche verbleibende Analyse-Zeit beträgt: < 5 Minuten.")


    if ollama_base_url:
        os.environ["OLLAMA_BASE_URL"] = ollama_base_url

    # Initialisiere Ergebniscontainer
    analysis_results = {}
    function_analysis_results = []
    class_analysis_results = []

    # Call HelperLLM für Funktionen
    update_status(f"🤖 Helper LLM: Analysiere {len(helper_llm_function_input)} Funktionen ({helper_model})...")

    try:
        net_time_func = 0
        if len(helper_llm_function_input) > 0:

            logging.info("\n--- Generating documentation for Functions ---")
            t_start_func = time.time()    
            function_analysis_results = llm_helper.generate_for_functions(helper_llm_function_input)    
            t_end_func = time.time()
            net_time_func = calculate_net_time(t_start_func, t_end_func, len(helper_llm_function_input), llm_helper.batch_size, helper_model)

        if len(function_analysis_results) != 0:
            for doc in function_analysis_results:
                if doc:
                    logging.info(f"Successfully generated doc for: {doc.identifier}")
                    if "functions" not in analysis_results:
                        analysis_results["functions"] = {}
                    analysis_results["functions"][doc.identifier] = doc.model_dump() 
                else:
                    logging.warning("Failed to generate doc for a function") 
    except Exception as e:
        logging.error(f"Error during Helper LLM function analysis: {e}")
        raise
    

    # Call HelperLLM für Klassen
    try:
        net_time_class = 0
        if len(helper_llm_class_input) > 0:
            # Rate Limit Sleep für Gemini Modelle
            if llm_helper.model_name.startswith("gemini-") & (len(helper_llm_function_input) > 0):
                update_status("💤 Wartezeit eingelegt, um Rate Limits einzuhalten...")
                time.sleep(65)
            
            update_status(f"🤖 Helper LLM: Analysiere {len(helper_llm_class_input)} Klassen ({helper_model})...")
            
            logging.info("\n--- Generating documentation for Classes ---")
            t_start_class = time.time()
            class_analysis_results = llm_helper.generate_for_classes(helper_llm_class_input)
            t_end_class = time.time()
            net_time_class = calculate_net_time(t_start_class, t_end_class, len(helper_llm_class_input), llm_helper.batch_size, helper_model)

        if len(class_analysis_results) != 0:
            for doc in class_analysis_results:
                if doc:
                    logging.info(f"Successfully generated doc for: {doc.identifier}")
                    if "classes" not in analysis_results:
                        analysis_results["classes"] = {}
                    analysis_results["classes"][doc.identifier] = doc.model_dump() 
                else:
                    logging.warning("Failed to generate doc for a class")
    except Exception as e:
        logging.error(f"Error during Helper LLM class analysis: {e}")
        raise

    total_helper_time = net_time_func + net_time_class

    diagrams, class_diagrams, component_diagram = generator.main_diagram_generation(repo_files)
    # MainLLM Input Vorbereitung
    main_llm_input = {
        "basic_info": basic_project_info,
        "file_tree": repo_file_tree,
        "ast_schema": ast_schema,
        "analysis_results": analysis_results,
    }

    # Konvertiere Input in Toon Format
    main_llm_input_toon = encode(main_llm_input)
    # Token Evaluation
    savings_data = None
    try:
        logging.info("--- Evaluierung der Token-Ersparnis ---")
        savings_data = estimate_savings(main_llm_input)
        logging.info(f"JSON Tokens: {savings_data['json_tokens']}")
        logging.info(f"TOON Tokens: {savings_data['toon_tokens']}")
        logging.info(f"Ersparnis:   {savings_data['savings_percent']:.2f}%")
        
    except Exception as e:
        logging.warning(f"Token evaluation could not be performed: {e}")    

    # MainLLM Ausführung
    main_llm = MainLLM(
        api_key=main_api_key, 
        prompt_file_path=prompt_file_mainllm_toon,
        model_name=main_model,
        base_url=main_base_url,
    )

    # RPM Limit Sleep für Gemini Modelle
    if llm_helper.model_name == main_llm.model_name and main_llm.model_name.startswith("gemini-"):
        time.sleep(65)
        update_status("💤 Wartezeit eingelegt, um Rate Limits einzuhalten...")

    # Call MainLLM für finalen Report
    update_status(f"🧠 Main LLM: Generiere finalen Report ({main_model})...")
    try:
        total_main_time = 0
        logging.info("\n--- Generating Final Report ---")
        t_start_main = time.time()
        final_report = main_llm.call_llm(main_llm_input_toon)
        t_end_main = time.time()
        total_main_time = t_end_main - t_start_main
    except Exception as e:
        logging.error(f"Error during Main LLM final report generation: {e}")
        raise
    if final_report:
        enriched_final_report = enrich_report_with_diagrams(final_report, diagrams, component_diagram, class_diagrams)
    
    # --- Speichern der Ergebnisse ---
    output_dir = "result"
    stats_dir = "Statistics" # Neuer Ordner
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(stats_dir, exist_ok=True) # Stelle sicher, dass Statistics Ordner existiert

    total_active_time = total_helper_time + total_main_time
    
    # Dateiname für Report
    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    report_filename = f"report_{timestamp}_Helper_{llm_helper.model_name}_MainLLM_{main_llm.model_name}.md"
    report_filename = report_filename.replace("/", "-")
    report_filepath: str = os.path.join(output_dir, report_filename)
    if final_report:
        with open(report_filepath, "w", encoding="utf-8") as f:
            f.write(enriched_final_report)
        logging.info(f"Final report saved to '{report_filepath}'.")
        
        if savings_data:
            try:
                savings_filename = report_filename.replace("report_", "savings_").replace(".md", ".png")
                savings_filepath = os.path.join(stats_dir, savings_filename)
                
                logging.info(f"Erstelle Token-Chart: {savings_filepath}")
                create_savings_chart(
                    json_tokens=savings_data['json_tokens'], 
                    toon_tokens=savings_data['toon_tokens'], 
                    savings_percent=savings_data['savings_percent'],
                    output_path=savings_filepath
                )
            except Exception as chart_error:
                logging.error(f"Konnte Diagramm nicht erstellen: {chart_error}")

    else:
        final_report = "Error: Report generation failed or returned empty."

    metrics = {
        "helper_time": round(total_helper_time, 2),
        "main_time": round(total_main_time, 2),
        "total_time": round(total_active_time, 2),
        "helper_model": helper_model,
        "main_model": main_model,
        "json_tokens": savings_data['json_tokens'] if savings_data else None,
        "toon_tokens": savings_data['toon_tokens'] if savings_data else None,
        "savings_percent": round(savings_data['savings_percent'], 2) if savings_data else None
    
    }
    if enriched_final_report is not None:
        return {
            "report": enriched_final_report,
            "metrics": metrics
        }
    else:
        return {
            "report": final_report,
            "metrics": metrics
        }
    

def enrich_report_with_diagrams(final_report: str, diagrams: dict, component_diagram: str, class_diagrams: dict) -> str:
    """Fügt Diagramme aus dem `diagrams`-Dictionary in den `final_report` ein."""
    report_lines = final_report.splitlines()
    enriched_report = []

    for line in report_lines:
        enriched_report.append(line)
        if "#### Function:" in line:
            for filename, seq_diagram in diagrams.items():
                    if filename in line:
                        enriched_report.append(f"   **Sequence diagram for {filename}**")
                        enriched_report.append(seq_diagram)
        
        if "## 4. Architecture" in line:
            enriched_report.append(component_diagram)
        
        if "#### Class:" in line:
            for class_name, class_diagram in class_diagrams.items():
                if re.search(rf"\b{re.escape(class_name)}\b", line):
                    enriched_report.append(class_diagram)

    return "\n".join(enriched_report)


def notebook_workflow(input, api_keys, model, status_callback=None, check_stop=None):
    t_start = time.time()
    final_report = "keine Notebooks gefunden"
    
    def update_status(msg):
        # --- NEU: Prüfen ob abgebrochen wurde ---
        if check_stop and check_stop():
            logging.info("Interrupt empfangen. Breche notebook_workflow ab.")
            raise InterruptedError("Analyse wurde vom User gestoppt.")
            
        if status_callback:
            status_callback(msg)
        logging.info(msg)

    # --- API KEY & URL LOGIK (KONSISTENT ZU MAIN_WORKFLOW) ---
    gemini_api_key = api_keys.get("gemini")
    openai_api_key = api_keys.get("gpt")
    scadsllm_api_key = api_keys.get("scadsllm")
    scadsllm_base_url = api_keys.get("scadsllm_base_url")
    ollama_base_url = api_keys.get("ollama")
    
    # User-eigene Open Source Konfiguration aus der UI
    user_opensrc_key = api_keys.get("opensrc_key")
    user_opensrc_url = api_keys.get("opensrc_url")

    input_api_key = None
    base_url = None

    # Präzise Bestimmung des Providers
    if model.startswith("gpt-"):
        input_api_key = openai_api_key
        base_url = None
    elif model.startswith("gemini-"):
        if not gemini_api_key:
            raise ValueError(f"Gemini API Key fehlt für Modell {model}")
        input_api_key = gemini_api_key
        base_url = None
    elif model == "llama3":
        input_api_key = None
        base_url = ollama_base_url
    else:
        # Logik für Open Source / ScadsLLM / Aliasse
        if user_opensrc_url:
            input_api_key = user_opensrc_key
            base_url = user_opensrc_url
        else:
            input_api_key = scadsllm_api_key
            base_url = scadsllm_base_url

    update_status("🔍 Analysiere Input...")

    # URL Extraktion
    repo_url = None
    url_pattern = r"https?://(?:www\.)?github\.com/[^\s]+"
    match = re.search(url_pattern, input)

    if match:
        repo_url = match.group(0)
    else:
        raise ValueError("Keine gültige GitHub-URL im Input gefunden.")
    
    update_status(f"⬇️ Klone Repository: {repo_url} ...")

    try: 
        with GitRepository(repo_url) as repo:
            repo_files = repo.get_all_files()
            
            # Extrahiere Basic Infos (während Repo noch offen ist)
            update_status("ℹ️ Extrahiere Basis-Informationen...")
            info_extractor = ProjektInfoExtractor()
            basic_project_info = info_extractor.extrahiere_info(dateien=repo_files, repo_url=repo_url)
            
            update_status("🔗 Bereite Notebooks vor...")
            # convert to XML/Toon (erfordert repo_files)
            processed_data = process_repo_notebooks(repo_files)
            
    except Exception as e:
        logging.error(f"Error processing repository: {e}")
        raise

    if not processed_data:
        return {
            "report": "In diesem Repository wurden keine Jupyter Notebooks (.ipynb) gefunden.",
            "metrics": {"total_time": round(time.time() - t_start, 2), "main_model": model}
        }

    # Initialisiere LLM
    prompt_file_notebook_llm = "SystemPrompts/SystemPromptNotebookLLM.txt"
    notebook_llm = MainLLM(
        api_key=input_api_key, 
        prompt_file_path=prompt_file_notebook_llm,
        model_name=model,
        base_url=base_url,
    )

    notebook_reports = []
    total_notebooks = len(processed_data)
    
    # Hilfsfunktion für Gemini-Payload (bleibt gleich)
    def gemini_payload(info, path, xml, imgs):
        intro_json = json.dumps({"basic_info": info, "current_notebook_path": path}, indent=2)
        payload = [{"type": "text", "text": f"Context Information:\n{intro_json}\n\nNotebook XML Structure:\n"}]
        pattern = r'(<IMAGE_PLACEHOLDER index="(\d+)" mime="([^"]+)"/>)'
        last_pos = 0
        for m in re.finditer(pattern, xml):
            payload.append({"type": "text", "text": xml[last_pos:m.start()]})
            idx = int(m.group(2))
            mime = m.group(3)
            if idx < len(imgs):
                payload.append({"type": "image_url", "image_url": {"url": f"data:{mime};base64,{imgs[idx]['data']}"}})
            last_pos = m.end()
        payload.append({"type": "text", "text": xml[last_pos:]})
        return payload

    # Sequentielle Verarbeitung
    for index, (nb_path, nb_data) in enumerate(processed_data.items(), 1):
        update_status(f"🧠 Generiere Report ({index}/{total_notebooks}): {os.path.basename(nb_path)}")
        
        llm_payload = gemini_payload(basic_project_info, nb_path, nb_data['xml'], nb_data['images'])

        try:
            single_report = notebook_llm.call_llm(llm_payload)
            if single_report:
                notebook_reports.append(single_report)
            else:
                notebook_reports.append(f"## Analyse für {os.path.basename(nb_path)}\nFehler: Keine Antwort vom Modell.")
        except Exception as e:
            logging.error(f"Fehler bei {nb_path}: {e}")
            notebook_reports.append(f"## Fehler bei {os.path.basename(nb_path)}\n{str(e)}")

    final_report = "\n\n---\n\n".join(notebook_reports)
    
    # Zeitmessung
    total_time = time.time() - t_start
    
    return {
        "report": final_report,
        "metrics": {
            "helper_time": 0,
            "main_time": round(total_time, 2),
            "total_time": round(total_time, 2),
            "helper_model": "None",
            "main_model": model,
            "json_tokens": 0,
            "toon_tokens": 0,
            "savings_percent": 0
        }
    }


def estimate_total_tokens(llm_input_estimate: dict[str, Any]):
    """
    Schätzt die Gesamttoken-Kosten für die komplette LLM-Pipeline.
    
    Args:
        llm_input_estimate: Dictionary mit allen Eingaben für die LLM-Analyse
        
    Returns:
        Dictionary mit detaillierten Token-Schätzungen
    """
    
   
    encoding = tiktoken.get_encoding("cl100k_base")
    
    
    HELPER_PROMPT_TOKENS = 3000  
    MAIN_PROMPT_TOKENS = 3000
    HELPER_OUTPUT_TOKENS = 20000  
    MAIN_OUTPUT_TOKENS = 32500  
    
    functions = llm_input_estimate.get("functions", [])
    num_functions = len(functions)
    
    function_input_tokens = 0
    if num_functions > 0:
        sample_func = functions[0]
        sample_text = json.dumps(sample_func.model_dump() if hasattr(sample_func, 'dict') else sample_func)
        avg_tokens_per_function = len(encoding.encode(sample_text))
        function_input_tokens = avg_tokens_per_function * num_functions
    
    classes = llm_input_estimate.get("classes", [])
    num_classes = len(classes)
    
    class_input_tokens = 0
    if num_classes > 0:
        sample_class = classes[0]
        sample_text = json.dumps(sample_class.model_dump() if hasattr(sample_class, 'dict') else sample_class)
        avg_tokens_per_class = len(encoding.encode(sample_text))
        class_input_tokens = avg_tokens_per_class * num_classes

    ast_schema = llm_input_estimate.get("ast_schema", {})
    ast_tokens = len(encoding.encode(json.dumps(ast_schema, default=str)))

    basic_info = llm_input_estimate.get("basic_info", "")
    basic_info_tokens = len(encoding.encode(str(basic_info)))

    file_tree = llm_input_estimate.get("file_tree", "")
    file_tree_tokens = len(encoding.encode(str(file_tree)))
    
    helper_function_input = HELPER_PROMPT_TOKENS + function_input_tokens + ast_tokens + basic_info_tokens
    helper_class_input = HELPER_PROMPT_TOKENS + class_input_tokens + ast_tokens + basic_info_tokens
    total_helper_input = helper_function_input + helper_class_input
    total_helper_output = HELPER_OUTPUT_TOKENS * 2 
    
    total_helper_tokens = total_helper_input + total_helper_output
    
    main_input_content = (
        basic_info_tokens + 
        file_tree_tokens + 
        ast_tokens + 
        total_helper_output 
    )
    

    total_main_input = MAIN_PROMPT_TOKENS + main_input_content
    total_main_output = MAIN_OUTPUT_TOKENS
    
    total_main_tokens = total_main_input + total_main_output

    return total_helper_tokens + total_main_tokens


if __name__ == "__main__":
    user_input = "https://github.com/christiand03/repo-onboarding-agent"
    #main_workflow(user_input, api_keys={"gemini": os.getenv("GEMINI_API_KEY"), "scadsllm": os.getenv("SCADS_AI_KEY"), "scadsllm_base_url": os.getenv("SCADSLLM_URL")}, model_names={"helper": "alias-code", "main": "alias-ha"})

    #notebook_input = "https://github.com/christiand03/predicting-power-consumption-uni"
    #notebook_input = "https://github.com/christiand03/clustering-and-classification-uni"
    # notebook_input= "https://github.com/Schmarc4/Monarchs"
    # notebook_workflow(notebook_input, api_keys= {"gemini": os.getenv("GEMINI_API_KEY"), "scadsllm": os.getenv("SCADS_AI_KEY"), "scadsllm_base_url": os.getenv("SCADSLLM_URL")}, model= "gemini-2.5-flash")
    main_workflow(user_input=user_input,
                  api_keys={
                      "opensrc_key": os.getenv("SCADS_AI_KEY"), 
                      "opensrc_url": os.getenv("SCADSLLM_URL")
                  },
                  model_names={
                      "helper": "Qwen/Qwen3-Coder-30B-A3B-Instruct",
                      "main": "openai/gpt-oss-120b"
                  }
    )

    notebook_input= "https://github.com/Schmarc4/Monarchs"
   # notebook_workflow(notebook_input, api_keys= {"gemini": os.getenv("GEMINI_API_KEY"), "scadsllm": os.getenv("SCADS_AI_KEY"), "scadsllm_base_url": os.getenv("SCADSLLM_URL")}, model= "gemini-2.5-flash")    
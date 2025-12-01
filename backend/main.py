import logging
import os
import re
import json
import time
import math
from datetime import datetime
import matplotlib.pyplot as plt

from dotenv import load_dotenv

from .getRepo import GitRepository, RepoFile
from .AST_Schema import ASTAnalyzer
from .MainLLM import MainLLM
from .basic_info import ProjektInfoExtractor
from .HelperLLM import LLMHelper
from .relationship_analyzer import ProjectAnalyzer
from schemas.types import FunctionContextInput, FunctionAnalysisInput, ClassContextInput, ClassAnalysisInput, MethodContextInput

from toon_format import encode, count_tokens, estimate_savings, compare_formats

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


def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None):
    
    def update_status(msg):
        if status_callback:
            status_callback(msg)
        logging.info(msg)

    update_status("🔍 Analysiere Input...")
    
    user_input = input
    
    # API Key & Ollama Base URL aus Frontend holen
    gemini_api_key = api_keys.get("gemini")
    openai_api_key = api_keys.get("gpt")
    ollama_base_url = api_keys.get("ollama")

    if model_names["helper"].startswith("gpt-"):
        helper_api_key = openai_api_key
    elif model_names["helper"].startswith("gemini-"):
        helper_api_key = gemini_api_key
    if model_names["main"].startswith("gpt-"):
        api_key = openai_api_key
    elif model_names["main"].startswith("gemini-"):
        api_key = gemini_api_key

    # Standardeinstellungen für Modelle
    helper_model = model_names.get("helper", "gpt-5-mini")
    main_model = model_names.get("main", "gpt-5.1")

    # Error Handling für fehlende API Keys
    if not gemini_api_key and "gemini" in helper_model:
        raise ValueError("Gemini API Key was not provided in api_keys dictionary.")

    # URL Extraktion
    repo_url = None
    url_pattern = r"https?://[^\s]+"
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
            if hasattr(repo, 'local_path'):
                local_repo_path = repo.local_path
            elif hasattr(repo, 'working_dir'):
                local_repo_path = repo.working_dir
            else:
                local_repo_path = os.path.dirname(os.path.commonpath([f.path for f in repo_files]))

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

    # Erstelle Repository Dateibaum
    update_status("🌲 Erstelle Repository Dateibaum...")
    try:
        repo_file_tree = repo.get_file_tree()
        logging.info("Repository file tree constructed")
    except Exception as e:
        logging.error(f"Error constructing repository file tree: {e}")

    # Relationship Analyse durchführen
    update_status("🔗 Analysiere Beziehungen (Calls & Instanziierungen)...")
    try:
        rel_analyzer = ProjectAnalyzer(project_root=local_repo_path)
        relationship_results = rel_analyzer.analyze()
        logging.info(f"Relationships analyzed. Found definitions: {len(relationship_results)}")
    except Exception as e:
        logging.error(f"Error in relationship analyzer: {e}")
        relationship_results = []

    # Erstelle AST Schema
    update_status("🌳 Erstelle Abstract Syntax Tree (AST)...")
    try:        
        ast_analyzer = ASTAnalyzer()   
        ast_schema = ast_analyzer.analyze_repository(files=repo_files)
        logging.info("AST schema created")
    except Exception as e:
        logging.error(f"Error retrieving repository files: {e}")
        raise

    # Anreichern des AST Schemas mit Relationship Daten
    update_status("➕ Reiche AST mit Beziehungsdaten an...")            
    try:   
        ast_schema = ast_analyzer.merge_relationship_data(ast_schema, relationship_results)
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
    
    llm_helper = LLMHelper(
        api_key=helper_api_key, 
        function_prompt_path=function_prompt_file, 
        class_prompt_path=class_prompt_file,
        model_name=helper_model,
        ollama_base_url=ollama_base_url,
    )
    
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
                    logging.warning(f"Failed to generate doc for a function") 
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
                time.sleep(90)
            
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
                    logging.warning(f"Failed to generate doc for a class")
    except Exception as e:
        logging.error(f"Error during Helper LLM class analysis: {e}")
        raise

    total_helper_time = net_time_func + net_time_class

    # MainLLM Input Vorbereitung
    main_llm_input = {
        "basic_info": basic_project_info,
        "file_tree": repo_file_tree,
        "ast_schema": ast_schema,
        "analysis_results": analysis_results
    }

    # Speichern als JSON (Optional)
    main_llm_input_json = json.dumps(main_llm_input, indent=2)
    # with open("output.json", "w", encoding="utf-8") as f:
    #     f.write(main_llm_input_json)
    #     logging.info("JSON-Datei wurde gespeichert.")

    # Konvertiere Input in Toon Format
    main_llm_input_toon = encode(main_llm_input)

    #Speichern in TOON Format (Optional)
    # with open("output.toon", "w", encoding="utf-8") as f:
    #     f.write(main_llm_input_toon)
    #     logging.info("output.toon erfolgreich gespeichert.")
    
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



    prompt_file_mainllm = "SystemPrompts/SystemPromptMainLLM.txt"
    prompt_file_mainllm_toon = "SystemPrompts/SystemPromptMainLLMToon.txt"
    # MainLLM Ausführung
    main_llm = MainLLM(
        api_key=api_key, 
        prompt_file_path=prompt_file_mainllm_toon,
        model_name=main_model,
        ollama_base_url=ollama_base_url,
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

    
    # --- Speichern der Ergebnisse ---
    output_dir = "result"
    stats_dir = "Statistics" # Neuer Ordner
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(stats_dir, exist_ok=True) # Stelle sicher, dass Statistics Ordner existiert

    total_active_time = total_helper_time + total_main_time
    
    # Dateiname für Report
    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    report_filename = f"report_{timestamp}_Helper_{llm_helper.model_name}_MainLLM_{main_llm.model_name}.md"
    report_filepath = os.path.join(output_dir, report_filename)
    
    if final_report:
        with open(report_filepath, "w", encoding="utf-8") as f:
            f.write(final_report)
        logging.info(f"Final report saved to '{report_filepath}'.")
        
        # --- NEU: Speichern des Savings-Diagramms ---
        # Nur wenn wir valide Savings Daten haben
        if savings_data:
            try:
                # Dateiname ableiten: "savings_" statt "report_" und Endung .png
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
        "main_model": main_model
    }

    return {
        "report": final_report,
        "metrics": metrics
    }

if __name__ == "__main__":
    user_input = "https://github.com/christiand03/repo-onboarding-agent"
    main_workflow(user_input, api_keys={"gemini": os.getenv("GEMINI_API_KEY")}, model_names={"helper": "gemini-2.5-flash-lite", "main": "gemini-2.5-pro"})
import json
import math
import logging
import os
import re
import time
import math
from datetime import datetime
import matplotlib.pyplot as plt
import csv


from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

from .getRepo import GitRepository, RepoFile
from .AST_Schema import ASTAnalyzer
from .MainLLM import MainLLM
from .basic_info import ProjektInfoExtractor
from .HelperLLM import LLMHelper
from .relationship_analyzer import ProjectAnalyzer
from schemas.types import FunctionContextInput, FunctionAnalysisInput, ClassContextInput, ClassAnalysisInput, MethodContextInput
from .main import calculate_net_time

from toon_format import encode, count_tokens, estimate_savings, compare_formats


# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

def evaluation(input, api_keys: dict, model_names: dict, status_callback=None):
    
    user_input = input
    
    # API Key & Ollama Base URL aus Frontend holen
    gemini_api_key = api_keys.get("gemini")
    openai_api_key = api_keys.get("gpt")
    scadsllm_api_key = api_keys.get("scadsllm")
    scadsllm_base_url = api_keys.get("scadsllm_base_url")
    ollama_base_url = api_keys.get("ollama")
    base_url = None

    if model_names["helper"].startswith("gpt-"):
        helper_api_key = openai_api_key
    elif model_names["helper"].startswith("gemini-"):
        helper_api_key = gemini_api_key
    elif "/" in model_names["helper"] or model_names["helper"].startswith("alias-") or any(x in model_names["helper"] for x in ["DeepSeek", "Teuken", "Llama", "Qwen", "gpt-oss", "openGPT"]):
        helper_api_key = scadsllm_api_key
        base_url = scadsllm_base_url
    else:
        helper_api_key = None
        base_url = ollama_base_url
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
    url_pattern = r"https?://(?:www\.)?github\.com/[^\s]+"
    match = re.search(url_pattern, user_input)

    if match:
        repo_url = match.group(0)
        logging.info(f"Extracted repository URL: {repo_url}")
    else:
        raise ValueError("Could not find a valid URL in the provided input.")
    
    # Repo klonen und Dateien extrahieren
    
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
    try:
        info_extractor = ProjektInfoExtractor()
        basic_project_info = info_extractor.extrahiere_info(dateien=repo_files, repo_url=repo_url)
        logging.info("Basic project info extracted")
    except Exception as e:
        logging.error(f"Error extracting basic project info: {e}")

    # Erstelle Repository Dateibaum
    try:
        repo_file_tree = repo.get_file_tree()
        logging.info("Repository file tree constructed")
    except Exception as e:
        logging.error(f"Error constructing repository file tree: {e}")

    # Relationship Analyse durchführen
    try:
        rel_analyzer = ProjectAnalyzer(project_root=local_repo_path)
        relationship_results = rel_analyzer.analyze()
        logging.info(f"Relationships analyzed. Found definitions: {len(relationship_results)}")
    except Exception as e:
        logging.error(f"Error in relationship analyzer: {e}")
        relationship_results = []

    # Erstelle AST Schema
    try:        
        ast_analyzer = ASTAnalyzer()   
        ast_schema = ast_analyzer.analyze_repository(files=repo_files, repo=repo)
        logging.info("AST schema created")
    except Exception as e:
        logging.error(f"Error retrieving repository files: {e}")
        raise

    # Anreichern des AST Schemas mit Relationship Daten           
    try:   
        ast_schema = ast_analyzer.merge_relationship_data(ast_schema, relationship_results)
        logging.info("AST schema created and enriched")

    except Exception as e:
        logging.error(f"Error processing repository: {e}")
        raise

    # Vorbereitung der HelperLLM Eingaben
    
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

    function_prompt_file = 'SystemPrompts/SystemPromptFunctionHelperLLM.txt'
    class_prompt_file = 'SystemPrompts/SystemPromptClassHelperLLM.txt'
    
    llm_helper = LLMHelper(
        api_key=helper_api_key, 
        function_prompt_path=function_prompt_file, 
        class_prompt_path=class_prompt_file,
        model_name=helper_model,
        base_url=base_url,
    )
    
    if ollama_base_url:
        os.environ["OLLAMA_BASE_URL"] = ollama_base_url

    # Ergebnis-Container
    analysis_results = {}
    
    # Zeitmessung Variablen
    net_time_func = 0
    gross_time_func = 0
    net_time_class = 0
    gross_time_class = 0

    try:
        if len(helper_llm_function_input) > 0:
            t_start_func = time.time()    
            function_analysis_results = llm_helper.generate_for_functions(helper_llm_function_input)    
            t_end_func = time.time()
            
            gross_time_func = t_end_func - t_start_func
            net_time_func = calculate_net_time(t_start_func, t_end_func, len(helper_llm_function_input), llm_helper.batch_size, helper_model)

        if function_analysis_results:
            for doc in function_analysis_results:
                if doc:
                    if "functions" not in analysis_results:
                        analysis_results["functions"] = {}
                    analysis_results["functions"][doc.identifier] = doc.model_dump() 
    except Exception as e:
        logging.error(f"Error during Helper LLM function analysis: {e}")
        raise

    try:
        if len(helper_llm_class_input) > 0:
            sleep_offset = 0
            # Rate Limit Sleep logic
            if llm_helper.model_name.startswith("gemini-") and (len(helper_llm_function_input) > 0):
                time.sleep(65)
                sleep_offset = 65

            
            t_start_class = time.time()
            class_analysis_results = llm_helper.generate_for_classes(helper_llm_class_input)
            t_end_class = time.time()
            
            gross_time_class = (t_end_class - t_start_class) + sleep_offset
            net_time_class = calculate_net_time(t_start_class, t_end_class, len(helper_llm_class_input), llm_helper.batch_size, helper_model)

        if class_analysis_results:
            for doc in class_analysis_results:
                if doc:
                    if "classes" not in analysis_results:
                        analysis_results["classes"] = {}
                    analysis_results["classes"][doc.identifier] = doc.model_dump() 
    except Exception as e:
        logging.error(f"Error during Helper LLM class analysis: {e}")
        raise


    total_net_time = net_time_func + net_time_class
    total_gross_time = gross_time_func + gross_time_class
    
    # Token Evaluation mit TOON
    json_tokens = 0
    toon_tokens = 0
    savings_percent = 0

    try:
        logging.info("--- Evaluierung der Token-Ersparnis ---")
        savings_data = estimate_savings(analysis_results)
        
        json_tokens = savings_data.get('json_tokens', 0)
        toon_tokens = savings_data.get('toon_tokens', 0)
        savings_percent = savings_data.get('savings_percent', 0)

        logging.info(f"JSON Tokens: {json_tokens}")
        logging.info(f"TOON Tokens: {toon_tokens}")
        logging.info(f"Ersparnis:   {savings_percent:.2f}%")
        
    except Exception as e:
        logging.warning(f"Token evaluation could not be performed: {e}") 

    logging.info(f"Analysis Complete. Net: {total_net_time:.2f}s, Gross: {total_gross_time:.2f}s")

    # Rückgabe an den Runner
    return {
        "results": analysis_results,
        "metrics": {
            "model": helper_model,
            "json_tokens": json_tokens,
            "toon_tokens": toon_tokens,
            "duration_gross": total_gross_time,
            "duration_net": total_net_time
        }
    }




INPUT_REPO_URL = "https://github.com/christiand03/repo-onboarding-agent" 

BASE_EVAL_DIR = "Evaluation"

# API Keys aus .env laden
api_keys = {
    "gemini": os.getenv("GEMINI_API_KEY"),
    "gpt": os.getenv("OPENAI_API_KEY"),
    "ollama": os.getenv("OLLAMA_BASE_URL"),
    "scadsllm": os.getenv("SCADS_AI_KEY"),
    "scadsllm_base_url": os.getenv("SCADSLLM_URL")
}

# Liste der Modelle, die durchlaufen werden sollen
MODELS_TO_TEST = [
    # Gemini
    #"gemini-2.0-flash-lite",
    #"gemini-2.5-flash",
    #"gemini-2.0-flash",
    #"gemini-2.5-flash-lite",

    # #scadsllm Modelle
    # # Aliases
    "alias-reasoning",
    "alias-ha",
    "alias-code",
    
    # # Llama
    "meta-llama/Llama-3.3-70B-Instruct",
    "meta-llama/Llama-3.1-8B-Instruct",
    "meta-llama/Llama-4-Scout-17B-16E-Instruct",
    
    # DeepSeek
    "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct",
    "deepseek-ai/DeepSeek-R1",
    "deepseek-ai/DeepSeek-V3.2-Exp",
    
    # Qwen (Code & Instruct)
    "Qwen/Qwen3-Coder-30B-A3B-Instruct",
    "Qwen/Qwen2-VL-7B-Instruct",
    
    # Andere
    "openGPT-X/Teuken-7B-instruct-research-v0.4",
    "openai/gpt-oss-120b",    

]

def save_stats_to_run_file(metrics, filepath):

    data = []
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.strip():
                    data = json.loads(content)
        except Exception as e:
            logging.error(f"Fehler beim Lesen der aktuellen Stats-Datei: {e}")

    new_entry = {
        "model": metrics["model"],
        "tokens_json": metrics["json_tokens"],
        "tokens_toon": metrics["toon_tokens"],
        "duration_gross_sec": round(metrics["duration_gross"], 2),
        "duration_net_sec": round(metrics["duration_net"], 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(new_entry)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logging.info(f"Statistik aktualisiert: {filepath}")
    except Exception as e:
        logging.error(f"Fehler beim Schreiben der Stats-Datei: {e}")

def run_evaluation():
    run_timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    
    current_run_output_dir = os.path.join(BASE_EVAL_DIR, f"Output-{run_timestamp}")
    
    stats_filename = f"evaluation_stats-{run_timestamp}.json"
    stats_file_path = os.path.join(BASE_EVAL_DIR, stats_filename)

    os.makedirs(current_run_output_dir, exist_ok=True)
    
    logging.info(f"Starte Evaluation.")
    logging.info(f"Output Ordner: {current_run_output_dir}")
    logging.info(f"Stats Datei:   {stats_file_path}")

    for model_name in MODELS_TO_TEST:
        logging.info(f"--------------------------------------------------")
        logging.info(f"Starte Run für Helper-Model: {model_name}")

        current_model_config = {
            "helper": model_name,
            "main": "gpt-5.1" 
        }

        try:
            result_data = evaluation(
                input=INPUT_REPO_URL,
                api_keys=api_keys,
                model_names=current_model_config
            )

            metrics = result_data["metrics"]
            json_content = result_data["results"]


            model_timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            safe_model_name = model_name.replace("/", "-").replace(":", "") 
            
            output_filename = f"{safe_model_name}-{model_timestamp}.json"
            
            output_path = os.path.join(current_run_output_dir, output_filename)

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(json_content, f, indent=4, ensure_ascii=False)
            
            logging.info(f"Output gespeichert in: {output_path}")

            save_stats_to_run_file(metrics, stats_file_path)
            
            time.sleep(2)

        except Exception as e:
            logging.error(f"Fehler bei Modell {model_name}: {e}")
            logging.info("Fahre mit dem nächsten Modell fort...")
            continue

    logging.info(f"Evaluation abgeschlossen. Ergebnisse in {current_run_output_dir}")

if __name__ == "__main__":
    if not api_keys.get("scadsllm"):
        logging.warning("Kein SCADS_AI_KEY gefunden.")
    
    run_evaluation()
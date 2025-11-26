import logging
import os
import re
import json
import time
import math
from datetime import datetime

from dotenv import load_dotenv

from .getRepo import GitRepository, RepoFile
from .AST_Schema import ASTAnalyzer
from .MainLLM import MainLLM
from .basic_info import ProjektInfoExtractor
from .HelperLLM import LLMHelper
from schemas.types import FunctionContextInput, FunctionAnalysisInput, ClassContextInput, ClassAnalysisInput

# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

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


# [CHANGE] Neuer Parameter status_callback
def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None):
    
    # [CHANGE] Helper Funktion für Status Updates im Frontend
    def update_status(msg):
        if status_callback:
            status_callback(msg) # Sendet msg an st.status
        logging.info(msg)

    # 1. Setup & Input
    # [CHANGE] Status Update
    update_status("🔍 Analysiere Input...")
    
    user_input = input
    workflow_start_time = datetime.now()
    
    gemini_api_key = api_keys.get("gemini")
    ollama_base_url = api_keys.get("ollama")

    helper_model = model_names.get("helper", "gemini-2.5-pro")
    main_model = model_names.get("main", "gemini-2.5-pro")

    if not gemini_api_key and "gemini" in helper_model:
        raise ValueError("Gemini API Key was not provided in api_keys dictionary.")

    # 2. URL Extraktion
    repo_url = None
    url_pattern = r"https?://[^\s]+"
    match = re.search(url_pattern, user_input)

    if match:
        repo_url = match.group(0)
        logging.info(f"Extracted repository URL: {repo_url}")
    else:
        raise ValueError("Could not find a valid URL in the provided input.")
    
    # 3. Repo Analyse
    # [CHANGE] Status Update
    update_status(f"⬇️ Klone Repository: {repo_url} ...")
    
    repo_files = []
    try: 
        with GitRepository(repo_url) as repo:
            repo_files = repo.get_all_files()
            logging.info(f"Total files retrieved: {len(repo_files)}")
            
            # Basic Info
            # [CHANGE] Status Update
            update_status("ℹ️ Extrahiere Basis-Informationen...")
            info_extractor = ProjektInfoExtractor()
            basic_project_info = info_extractor.extrahiere_info(dateien=repo_files, repo_url=repo_url)
            
            # File Tree
            repo_file_tree = repo.get_file_tree()
            
            # AST
            # [CHANGE] Status Update
            update_status("🌳 Erstelle Abstract Syntax Tree (AST)...")
            ast_analyzer = ASTAnalyzer()   
            ast_schema = ast_analyzer.analyze_repository(files=repo_files)

    except Exception as e:
        logging.error(f"Error retrieving repository files: {e}")
        raise

    # 4. Datenvorbereitung HelperLLM
    # [CHANGE] Status Update
    update_status("⚙️ Bereite Daten für Helper LLM vor...")
    
    helper_llm_function_input = []
    helper_llm_class_input = []

    for filename, file_data in ast_schema['files'].items():
        ast_nodes = file_data.get('ast_nodes', {})
        imports = ast_nodes.get('imports', [])
        
        for function in ast_nodes.get('functions', []):
            context = function.get('context', {})
            f_input = FunctionAnalysisInput(
                mode=function.get('mode', 'function_analysis'),
                identifier=function.get('identifier'),
                source_code=function.get('source_code'),
                imports=imports,
                context=FunctionContextInput(
                    calls=context.get('calls', []),
                    called_by=context.get('called_by', [])
                )
            )
            helper_llm_function_input.append(f_input)

        for _class in ast_nodes.get('classes', []):
            context = _class.get('context', {})
            c_input = ClassAnalysisInput(
                mode=_class.get('mode', 'class_analysis'),
                identifier=_class.get('identifier'),
                source_code=_class.get('source_code'), 
                imports=imports, 
                context=ClassContextInput(
                    dependencies=context.get('dependencies', []),
                    instantiated_by=context.get('instantiated_by', []),
                    method_context=context.get('method_context', [])
                )
            )
            helper_llm_class_input.append(c_input)
    
    logging.info(f"Functions: {len(helper_llm_function_input)}, Classes: {len(helper_llm_class_input)}")
    
    # 5. HelperLLM Ausführung
    function_prompt_file = 'SystemPrompts/SystemPromptFunctionHelperLLM.txt'
    class_prompt_file = 'SystemPrompts/SystemPromptClassHelperLLM.txt'
    
    llm_helper = LLMHelper(
        api_key=gemini_api_key, 
        function_prompt_path=function_prompt_file, 
        class_prompt_path=class_prompt_file,
        model_name=helper_model,
        ollama_base_url=ollama_base_url,
    )
    
    if ollama_base_url:
        os.environ["OLLAMA_BASE_URL"] = ollama_base_url

    analysis_results = {}

    # --- Functions ---
    if len(helper_llm_function_input) > 0:
        # [CHANGE] Status Update
        update_status(f"🤖 Helper LLM: Analysiere {len(helper_llm_function_input)} Funktionen ({helper_model})...")
    
    t_start_func = time.time()
    function_analysis_results = []
    
    if len(helper_llm_function_input) > 0:
        function_analysis_results = llm_helper.generate_for_functions(helper_llm_function_input)
    
    t_end_func = time.time()
    net_time_func = calculate_net_time(t_start_func, t_end_func, len(helper_llm_function_input), llm_helper.batch_size, helper_model)

    if function_analysis_results:
        analysis_results["functions"] = {}
        for doc in function_analysis_results:
            if doc:
                analysis_results["functions"][doc.identifier] = doc.model_dump()

    # --- Classes ---
    if len(helper_llm_class_input) > 0:
        # [CHANGE] Status Update
        update_status(f"🤖 Helper LLM: Analysiere {len(helper_llm_class_input)} Klassen ({helper_model})...")
        
    t_start_class = time.time()
    class_analysis_results = []
    
    if len(helper_llm_class_input) > 0:
        class_analysis_results = llm_helper.generate_for_classes(helper_llm_class_input)
    
    t_end_class = time.time()
    net_time_class = calculate_net_time(t_start_class, t_end_class, len(helper_llm_class_input), llm_helper.batch_size, helper_model)

    if class_analysis_results:
        analysis_results["classes"] = {}
        for doc in class_analysis_results:
            if doc:
                analysis_results["classes"][doc.identifier] = doc.model_dump()

    total_helper_time = net_time_func + net_time_class

    # 6. MainLLM Input Vorbereitung
    main_llm_input = {
        "basic_info": basic_project_info,
        "file_tree": repo_file_tree,
        "ast_schema": ast_schema,
        "analysis_results": analysis_results
    }
    main_llm_input_json = json.dumps(main_llm_input, indent=2)
    
    # 7. MainLLM Ausführung
    main_llm = MainLLM(
        api_key=gemini_api_key, 
        prompt_file_path="SystemPrompts/SystemPromptMainLLM.txt",
        model_name=main_model,
        ollama_base_url=ollama_base_url,
    )

    # [CHANGE] Status Update
    update_status(f"🧠 Main LLM: Generiere finalen Report ({main_model})...")
    
    # Safety Sleep um RPM Limits zu respecten (nach dem Helper Stress)
    time.sleep(5) 

    t_start_main = time.time()
    final_report = main_llm.call_llm(main_llm_input_json)
    t_end_main = time.time()
    total_main_time = t_end_main - t_start_main
    
    # [CHANGE] Status Update
    update_status("✅ Analyse abgeschlossen!")
    
    # Speichern
    output_dir = "result"
    os.makedirs(output_dir, exist_ok=True)  
    total_active_time = total_helper_time + total_main_time
    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    
    report_filename = f"report_{timestamp}_Helper_{llm_helper.model_name}_MainLLM_{main_llm.model_name}.md"
    report_filepath = os.path.join(output_dir, report_filename)
    
    if final_report:
        with open(report_filepath, "w", encoding="utf-8") as f:
            f.write(final_report)
        logging.info(f"Final report saved to '{report_filepath}'.")
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
    pass
import os
import json
import logging
import time
import re
from datetime import datetime
from dotenv import load_dotenv

from backend.getRepo import GitRepository
from backend.AST_Schema import ASTAnalyzer
from backend.relationship_analyzer import ProjectAnalyzer
from backend.HelperLLM import LLMHelper
from backend.EvaluatorLLM import EvaluatorLLM
from schemas.types import FunctionContextInput, FunctionAnalysisInput, ClassContextInput, ClassAnalysisInput, MethodContextInput

# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

REPO_URL_TO_TEST = "https://github.com/christiand03/repo-onboarding-agent-evaluation"

HELPER_MODELS_TO_TEST = [
    # #Google Gemini
    # "gemini-2.5-flash",
    # "gemini-2.5-flash-lite",

    #SCADS  
    #Aliases
    "alias-reasoning",
    "alias-ha",
    "alias-code",
    
    #Llama
    "meta-llama/Llama-3.3-70B-Instruct",
    "meta-llama/Llama-3.1-8B-Instruct",
    "meta-llama/Llama-4-Scout-17B-16E-Instruct",
    
    # DeepSeek
    "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct",
    "deepseek-ai/DeepSeek-R1",
    "deepseek-ai/DeepSeek-V3.2-Exp",
    
    # Qwen
    "Qwen/Qwen3-Coder-30B-A3B-Instruct",
    "Qwen/Qwen2-VL-7B-Instruct",
    
    # Andere
    "openGPT-X/Teuken-7B-instruct-research-v0.4",
    "openai/gpt-oss-120b", 
]

EVALUATOR_MODEL = "gemini-2.5-flash"

PROMPT_FUNC_HELPER = 'SystemPrompts/SystemPromptFunctionHelperLLM.txt'
PROMPT_CLASS_HELPER = 'SystemPrompts/SystemPromptClassHelperLLM.txt'
PROMPT_EVALUATOR_HELPER = 'SystemPrompts/SystemPromptEvaluatorHelper.txt'


def get_api_keys():
    return {
        "gemini": os.getenv("GEMINI_API_KEY"),
        "gpt": os.getenv("OPENAI_API_KEY"),
        "scadsllm": os.getenv("SCADS_AI_KEY"),
        "scadsllm_base_url": os.getenv("SCADSLLM_URL"),
        "ollama": os.getenv("OLLAMA_BASE_URL")
    }

def get_keys_for_model(model_name, all_keys):
    """Wählt den richtigen Key basierend auf dem Modellnamen."""
    if model_name.startswith("gpt-") and "oss" not in model_name: 
        return all_keys["gpt"], None
    elif model_name.startswith("gemini-"):
        return all_keys["gemini"], None
    elif "/" in model_name or model_name.startswith("alias-") or any(x in model_name for x in ["DeepSeek", "Teuken", "Llama", "Qwen", "gpt-oss"]): 
        return all_keys["scadsllm"], all_keys["scadsllm_base_url"]
    else:
        return "ollama", all_keys["ollama"]

def extract_score_from_eval(eval_text):
    if not eval_text:
        return 0
    match = re.search(r"TOTAL SCORE:.*?(\d+)\s*\/", eval_text, re.IGNORECASE | re.DOTALL)
    if match:
        try:
            return int(match.group(1))
        except ValueError:
            return 0
    return 0

def create_benchmark_dirs():
    """Erstellt die Ordnerstruktur: evaluation/HelperLLM/Benchmark_Datum_Zeit/..."""
    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    base_dir = os.path.join("evaluation", "HelperLLM", f"Benchmark_{timestamp}")
    
    dirs = {
        "base": base_dir,
        "input": os.path.join(base_dir, "Input"),
        "output": os.path.join(base_dir, "Output"),
        "evaluations": os.path.join(base_dir, "Evaluations"),
        "stats_file": os.path.join(base_dir, "benchmark_stats.json")
    }
    
    for d in [dirs["input"], dirs["output"], dirs["evaluations"]]:
        os.makedirs(d, exist_ok=True)
        
    logging.info(f"Benchmark-Verzeichnisse erstellt: {base_dir}")
    return dirs

def prepare_live_input(repo_url):

    logging.info(f"Erstelle Live-Input aus: {repo_url}")
    
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

    logging.info("Analysiere Beziehungen...")
    try:
        rel_analyzer = ProjectAnalyzer(project_root=local_repo_path)
        rel_analyzer.analyze()
        raw_relationships = rel_analyzer.get_raw_relationships()
    except Exception as e:
        logging.error(f"Error in relationship analyzer: {e}")
        raw_relationships = {"outgoing": {}, "incoming": {}}

    logging.info("Erstelle AST...")
    try:        
        ast_analyzer = ASTAnalyzer()   
        ast_schema = ast_analyzer.analyze_repository(files=repo_files, repo=repo)
        ast_schema = ast_analyzer.merge_relationship_data(ast_schema, raw_relationships)
    except Exception as e:
        logging.error(f"Error creating AST: {e}")
        raise

    logging.info("Konvertiere AST in HelperLLM Inputs...")
    
    helper_llm_function_input = []
    helper_llm_class_input = []
    
    raw_input_json = {"functions": [], "classes": []}

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
                raw_input_json["functions"].append(function_input.model_dump())

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
                raw_input_json["classes"].append(class_input.model_dump())

    except Exception as e:
        logging.error(f"Error converting to Input objects: {e}")
        raise

    return helper_llm_function_input, helper_llm_class_input, raw_input_json

def benchmark_loop():
    dirs = create_benchmark_dirs()
    keys = get_api_keys()

    # Input Vorbereitung
    try:
        func_inputs, class_inputs, raw_input_json = prepare_live_input(REPO_URL_TO_TEST)
        
        input_file_path = os.path.join(dirs["input"], "generated_input.json")
        with open(input_file_path, "w", encoding="utf-8") as f:
            json.dump(raw_input_json, f, indent=2)
            
        logging.info(f"Input erfolgreich erstellt: {len(func_inputs)} Funktionen, {len(class_inputs)} Klassen.")
        
        raw_input_str = json.dumps(raw_input_json, indent=2)

    except Exception as e:
        logging.error(f"CRITICAL: Konnte Input nicht erstellen. Abbruch. {e}")
        return

    stats = []

    for model in HELPER_MODELS_TO_TEST:
        logging.info(f"==================================================")
        logging.info(f"Starte Test für HelperLLM: {model}")
        
        safe_model_name = model.replace("/", "_").replace(":", "").replace(".", "-")
        
        helper_api_key, helper_base_url = get_keys_for_model(model, keys)
        eval_api_key, eval_base_url = get_keys_for_model(EVALUATOR_MODEL, keys)
        
        current_stat = {
            "helper_model": model,
            "evaluator_model": EVALUATOR_MODEL,
            "status": "pending",
            "score": 0,
            "duration_gen_sec": 0,
            "duration_eval_sec": 0,
            "items_processed": 0,
            "error_message": None,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            analysis_results = None
            generated_json_str = None
            max_retries = 1
            
            for attempt in range(max_retries + 1):
                try:
                    logging.info(f"Generiere Analyse (Versuch {attempt + 1}/{max_retries + 1})...")
                    
                    llm_helper = LLMHelper(
                        api_key=helper_api_key, 
                        function_prompt_path=PROMPT_FUNC_HELPER, 
                        class_prompt_path=PROMPT_CLASS_HELPER,
                        model_name=model,
                        base_url=helper_base_url
                    )
                    
                    start_gen = time.time()
                    temp_results = {"functions": {}, "classes": {}}
                    
                    if func_inputs:
                        logging.info(f"Analysiere Funktionen mit {model}...")
                        res_funcs = llm_helper.generate_for_functions(func_inputs)
                        for doc in res_funcs:
                            if doc: temp_results["functions"][doc.identifier] = doc.model_dump()

                    if class_inputs:
                        if model.startswith("gemini-"):
                            logging.info("Pause für Rate-Limit (Gemini)...")
                            time.sleep(65)
                        
                        logging.info(f"Analysiere Klassen mit {model}...")
                        res_classes = llm_helper.generate_for_classes(class_inputs)
                        for doc in res_classes:
                            if doc: temp_results["classes"][doc.identifier] = doc.model_dump()
                    
                    if not temp_results["functions"] and not temp_results["classes"]:
                        raise ValueError("Leere Antwort vom LLM (keine Funktionen/Klassen generiert)")

                    current_stat["duration_gen_sec"] = round(time.time() - start_gen, 2)
                    current_stat["items_processed"] = len(temp_results["functions"]) + len(temp_results["classes"])
                    analysis_results = temp_results
                    break
                    
                except Exception as e:
                    logging.warning(f"Fehler HelperLLM '{model}' (Versuch {attempt+1}): {e}")
                    current_stat["error_message"] = str(e)
                    if attempt < max_retries:
                        time.sleep(10)
            
            if not analysis_results:
                current_stat["status"] = "failed"
                if not current_stat["error_message"]:
                    current_stat["error_message"] = "Max retries exceeded / Empty Response"
                logging.error(f"Modell '{model}' fehlgeschlagen. Evaluierung wird übersprungen.")
            
            if current_stat["status"] != "failed":
                generated_json_str = json.dumps(analysis_results, indent=2)
                output_path = os.path.join(dirs["output"], f"output_{safe_model_name}.json")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(generated_json_str)

                logging.info(f"Starte Evaluierung mit {EVALUATOR_MODEL}...")
                
                evaluator = EvaluatorLLM(
                    api_key=eval_api_key,
                    prompt_file_path=PROMPT_EVALUATOR_HELPER,
                    model_name=EVALUATOR_MODEL,
                    base_url=eval_base_url
                )
                
                if EVALUATOR_MODEL.startswith("gemini-"):
                    logging.info("Warte 65s für Evaluator Rate-Limit...")
                    time.sleep(65)

                start_eval = time.time()
                
                eval_report = evaluator.evaluate_helper_analysis(
                    original_source_code_json=raw_input_str,
                    generated_analysis_json=generated_json_str
                )
                
                current_stat["duration_eval_sec"] = round(time.time() - start_eval, 2)
                current_stat["score"] = extract_score_from_eval(eval_report)
                
                current_stat["status"] = "success"
                current_stat["error_message"] = None

                eval_path = os.path.join(dirs["evaluations"], f"eval_{safe_model_name}.md")
                with open(eval_path, "w", encoding="utf-8") as f:
                    f.write(eval_report)
                
                logging.info(f"Evaluierung abgeschlossen. Score: {current_stat['score']}/100")

        except Exception as e:
            logging.error(f"Unerwarteter Absturz bei '{model}': {e}")
            current_stat["status"] = "failed"
            current_stat["error_message"] = f"Crash: {str(e)}"
        
        finally:
            stats.append(current_stat)
            try:
                with open(dirs["stats_file"], "w", encoding="utf-8") as f:
                    json.dump(stats, f, indent=4, ensure_ascii=False)
                logging.info(f"Stats aktualisiert für '{model}' (Status: {current_stat['status']})")
            except Exception as e:
                logging.error(f"FATAL: Konnte Stats-Datei nicht schreiben: {e}")

    logging.info(f"Benchmark vollständig abgeschlossen. Alle Ergebnisse in: {dirs['base']}")

if __name__ == "__main__":
    benchmark_loop()
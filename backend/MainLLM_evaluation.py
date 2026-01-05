import os
import json
import logging
import time
import re
from datetime import datetime
from dotenv import load_dotenv

from .getRepo import GitRepository
from .AST_Schema import ASTAnalyzer
from .MainLLM import MainLLM
from .basic_info import ProjektInfoExtractor
from .HelperLLM import LLMHelper
from .relationship_analyzer import ProjectAnalyzer
from .EvaluatorLLM import EvaluatorLLM
from schemas.types import FunctionContextInput, FunctionAnalysisInput, ClassContextInput, ClassAnalysisInput, MethodContextInput
from toon_format import encode

# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

# --- GLOBALE KONFIGURATION ---
REPO_URL = "https://github.com/christiand03/repo-onboarding-agent"
HELPER_MODEL = "alias-code"
EVALUATOR_MODEL = "gemini-2.5-flash"


MAIN_MODELS_TO_TEST = [

    #Google Gemini
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",

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

def get_api_keys():
    return {
        "gemini": os.getenv("GEMINI_API_KEY"),
        "gpt": os.getenv("OPENAI_API_KEY"),
        "scadsllm": os.getenv("SCADS_AI_KEY"),
        "scadsllm_base_url": os.getenv("SCADSLLM_URL"),
        "ollama": os.getenv("OLLAMA_BASE_URL")
    }

def get_keys_for_model(model_name, all_keys):
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
        return int(match.group(1))
    return 0

def create_benchmark_dirs():
    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    
    base_dir = os.path.join("evaluation", "MainLLM", f"Benchmark_{timestamp}")
    
    dirs = {
        "base": base_dir,
        "input": os.path.join(base_dir, "Input"),
        "reports": os.path.join(base_dir, "Reports"),
        "evaluations": os.path.join(base_dir, "Evaluations"),
        "stats_file": os.path.join(base_dir, "benchmark_stats.json")
    }
    
    for d in [dirs["input"], dirs["reports"], dirs["evaluations"]]:
        os.makedirs(d, exist_ok=True)
        
    logging.info(f"Benchmark-Verzeichnisse erstellt unter: {base_dir}")
    return dirs

def prepare_shared_input(repo_url, api_keys, input_dir):

    logging.info("STARTE VORBEREITUNG...")
    
    # 1. Clone & Basic Extraction
    repo_files = []
    local_path = ""
    repo_instance = None 
    
    try:
        repo_instance = GitRepository(repo_url)
        repo_files = repo_instance.get_all_files()
        local_path = os.path.dirname(os.path.commonpath([f.path for f in repo_files]))
        
        # Basic Info
        info_extractor = ProjektInfoExtractor()
        basic_info = info_extractor.extrahiere_info(repo_files, repo_url)
        
        # File Tree
        file_tree = repo_instance.get_file_tree()
        
        # 2. Analysis
        rel_analyzer = ProjectAnalyzer(local_path)
        rel_results = rel_analyzer.analyze()
        
        ast_analyzer = ASTAnalyzer()
        ast_schema = ast_analyzer.analyze_repository(repo_files, repo_instance)
        ast_schema = ast_analyzer.merge_relationship_data(ast_schema, rel_results)
    finally:
        if repo_instance:
            repo_instance.close()

    logging.info(f"Starte HelperLLM ({HELPER_MODEL}) zur Code-Analyse...")
    
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

    helper_api_key, helper_base_url = get_keys_for_model(HELPER_MODEL, api_keys)
    llm_helper = LLMHelper(
        api_key=helper_api_key, 
        function_prompt_path='SystemPrompts/SystemPromptFunctionHelperLLM.txt',
        class_prompt_path='SystemPrompts/SystemPromptClassHelperLLM.txt',
        model_name=HELPER_MODEL,
        base_url=helper_base_url
    )

    analysis_results = {"functions": {}, "classes": {}}
    
    if helper_llm_function_input:
        result = llm_helper.generate_for_functions(helper_llm_function_input)
        for doc in result:
            if doc: analysis_results["functions"][doc.identifier] = doc.model_dump()
            
    if helper_llm_class_input:
        if HELPER_MODEL.startswith("gemini-") and helper_llm_class_input:
            time.sleep(65)
        result = llm_helper.generate_for_classes(helper_llm_class_input)
        for doc in result:
            if doc: analysis_results["classes"][doc.identifier] = doc.model_dump()

    main_llm_input = {
        "basic_info": basic_info,
        "file_tree": file_tree,
        "ast_schema": ast_schema,
        "analysis_results": analysis_results
    }
    
    input_toon = encode(main_llm_input)

    # Speichern im Input Ordner
    timestamp = datetime.now().strftime("%H-%M-%S")
    input_filename = f"input_data_{timestamp}.toon"
    input_path = os.path.join(input_dir, input_filename)
    
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(input_toon)
    
    logging.info(f"Input gespeichert: {input_path}")
    return input_toon, input_filename

def benchmark_loop():
    dirs = create_benchmark_dirs()
    keys = get_api_keys()
    
    stats = []

    try:
        input_toon, input_filename = prepare_shared_input(REPO_URL, keys, dirs["input"])
    except Exception as e:
        logging.error(f"ABBRUCH: Fehler bei der Input-Erstellung: {e}")
        return

    for model in MAIN_MODELS_TO_TEST:
        logging.info(f"Teste MainLLM: {model}")
        
        safe_model_name = model.replace("/", "_").replace(":", "").replace(".", "-")
        timestamp = datetime.now().strftime("%H-%M-%S")
        
        main_api_key, main_base_url = get_keys_for_model(model, keys)
        eval_api_key, eval_base_url = get_keys_for_model(EVALUATOR_MODEL, keys)
        
        current_stat = {
            "main_model": model,
            "helper_model": HELPER_MODEL,
            "evaluator_model": EVALUATOR_MODEL,
            "status": "pending",
            "error_message": None,
            "score": 0,
            "duration_gen_sec": 0,
            "duration_eval_sec": 0,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "files": {
                "input": input_filename,
                "report": None,
                "evaluation": None
            }
        }

        try:
            report_content = None
            max_retries = 1
            
            for attempt in range(max_retries + 1):
                try:
                    logging.info(f"Generiere Dokumentation (Versuch {attempt + 1}/{max_retries + 1})...")
                    
                    main_llm = MainLLM(
                        api_key=main_api_key,
                        prompt_file_path="SystemPrompts/SystemPromptMainLLMToon.txt",
                        model_name=model,
                        base_url=main_base_url
                    )
                    
                    start_gen = time.time()
                    report_content = main_llm.call_llm(input_toon)
                    current_stat["duration_gen_sec"] = round(time.time() - start_gen, 2)
                    
                    if report_content:
                        break
                    else:
                        raise ValueError("Leere Antwort vom LLM")
                        
                except Exception as e:
                    logging.warning(f"Fehler MainLLM '{model}' (Versuch {attempt+1}): {e}")
                    current_stat["error_message"] = str(e)
                    if attempt < max_retries:
                        time.sleep(10)
            
            if not report_content:
                current_stat["status"] = "failed"
                if not current_stat["error_message"]:
                    current_stat["error_message"] = "Max retries exceeded / Empty Response"
                logging.error(f"Modell '{model}' fehlgeschlagen. Schreibe Fehler in Stats.")
            
            else:
                report_file = f"Report_{safe_model_name}.md"
                current_stat["files"]["report"] = report_file
                
                with open(os.path.join(dirs["reports"], report_file), "w", encoding="utf-8") as f:
                    f.write(report_content)

                if EVALUATOR_MODEL.startswith("gemini-"):
                    logging.info("Warte 65s für Evaluator Rate-Limit...")
                    time.sleep(65)

                evaluator = EvaluatorLLM(
                    api_key=eval_api_key,
                    prompt_file_path="SystemPrompts/SystemPromptEvaluatorLLM.txt",
                    model_name=EVALUATOR_MODEL,
                    base_url=eval_base_url
                )
                
                logging.info(f"Evaluiere...")
                start_eval = time.time()
                eval_result = evaluator.evaluate(report_content, input_toon)
                current_stat["duration_eval_sec"] = round(time.time() - start_eval, 2)
                
                eval_file = f"Eval_{safe_model_name}.md"
                current_stat["files"]["evaluation"] = eval_file
                
                with open(os.path.join(dirs["evaluations"], eval_file), "w", encoding="utf-8") as f:
                    f.write(eval_result)

                current_stat["score"] = extract_score_from_eval(eval_result)
                current_stat["status"] = "success"
                current_stat["error_message"] = None
                
                logging.info(f"Abgeschlossen: Score {current_stat['score']}/100")

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

    logging.info(f"\nBenchmark vollständig abgeschlossen. Ergebnisse in: {dirs['base']}")

if __name__ == "__main__":
    benchmark_loop()
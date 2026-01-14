import json
import math
import logging
import os
import re
import time
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path
from dotenv import load_dotenv

# Interne Imports
from .getRepo import GitRepository
from .AST_Schema import ASTAnalyzer
from .MainLLM import MainLLM
from .basic_info import ProjektInfoExtractor
from .HelperLLM import LLMHelper
from .relationship_analyzer import ProjectAnalyzer
from schemas.types import (
    FunctionContextInput, 
    FunctionAnalysisInput, 
    ClassContextInput, 
    ClassAnalysisInput, 
    MethodContextInput
)
from toon_format import encode, estimate_savings
from .converter import process_repo_notebooks

# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

# --- Hilfsfunktionen ---

def validate_llm_credentials(model_name, api_key, base_url):
    """Führt einen minimalen Test-Call aus, um den Key zu validieren, bevor der Workflow startet."""
    # Wir übergeben einen existierenden Pfad, damit der MainLLM-Konstruktor die Datei lesen kann
    dummy_prompt_path = "SystemPrompts/SystemPromptMainLLM.txt"
    
    try:
        # Falls die Datei nicht existiert, erstellen wir eine temporäre Dummy-Datei
        if not os.path.exists(dummy_prompt_path):
            os.makedirs("SystemPrompts", exist_ok=True)
            with open(dummy_prompt_path, "w") as f:
                f.write("You are a helpful assistant.")

        test_llm = MainLLM(
            api_key=api_key, 
            prompt_file_path=dummy_prompt_path, 
            model_name=model_name, 
            base_url=base_url
        )
        # Ein minimaler Test-Aufruf
        test_llm.call_llm("Ping") 
    except Exception as e:
        raise ValueError(f"Validierung fehlgeschlagen für Modell '{model_name}': {str(e)}")

def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path):
    """Erstellt ein Balkendiagramm für den Token-Vergleich."""
    labels = ['JSON', 'TOON']
    values = [json_tokens, toon_tokens]
    colors = ['#ff9999', '#66b3ff']

    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, values, color=colors, width=0.5)
    plt.title(f'Token-Vergleich: {savings_percent:.2f}% Einsparung', fontsize=14)
    plt.ylabel('Anzahl Token')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, 
                 f'{int(height):,}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.savefig(output_path)
    plt.close()

def calculate_net_time(start_time, end_time, total_items, batch_size, model_name):
    """Berechnet die Dauer abzüglich der Sleep-Zeiten für Rate-Limits (speziell Gemini)."""
    total_duration = end_time - start_time
    if not model_name.startswith("gemini-") or total_items == 0:
        return total_duration
    num_batches = math.ceil(total_items / batch_size)
    sleep_count = max(0, num_batches - 1)
    return max(0, total_duration - (sleep_count * 61))

# --- Haupt-Workflows ---

def main_workflow(user_input, api_keys: dict, model_names: dict, status_callback=None, check_stop=None):
    def update_status(msg):
        if check_stop and check_stop():
            raise InterruptedError("Analyse wurde vom User gestoppt.")
        if status_callback:
            status_callback(msg)
        logging.info(msg)

    # 1. API Keys extrahieren
    gemini_api_key = api_keys.get("gemini")
    openai_api_key = api_keys.get("gpt")
    scadsllm_api_key = api_keys.get("scadsllm")
    scadsllm_base_url = api_keys.get("scadsllm_base_url")
    ollama_base_url = api_keys.get("ollama")
    user_opensrc_key = api_keys.get("opensrc_key")
    user_opensrc_url = api_keys.get("opensrc_url")

    helper_model = model_names.get("helper", "gemini-2.5-flash-lite")
    main_model = model_names.get("main", "gemini-2.5-pro")

    def get_key_and_url(model_name):
        if model_name.startswith("gpt-"):
            if not openai_api_key: raise ValueError(f"OpenAI API Key fehlt für {model_name}.")
            return openai_api_key, None
        if model_name.startswith("gemini-"):
            if not gemini_api_key: raise ValueError(f"Gemini API Key fehlt für {model_name}.")
            return gemini_api_key, None
        if model_name == "llama3":
            if not ollama_base_url: raise ValueError(f"Ollama URL fehlt für {model_name}.")
            return None, ollama_base_url
        if user_opensrc_url:
            return user_opensrc_key, user_opensrc_url
        return scadsllm_api_key, scadsllm_base_url

    # 2. Key-Zuweisung & Pre-flight Check
    helper_api_key, helper_base_url = get_key_and_url(helper_model)
    main_api_key, main_base_url = get_key_and_url(main_model)

    update_status("🔑 Validierung der API-Keys (Pre-flight)...")
    validate_llm_credentials(helper_model, helper_api_key, helper_base_url)
    if helper_model != main_model:
        validate_llm_credentials(main_model, main_api_key, main_base_url)

    # 3. Repository klonen
    url_pattern = r"https?://(?:www\.)?github\.com/[^\s]+"
    match = re.search(url_pattern, user_input)
    if not match: raise ValueError("Keine gültige GitHub-URL gefunden.")
    repo_url = match.group(0)
    
    update_status(f"⬇️ Klone Repository: {repo_url} ...")
    try:
        with GitRepository(repo_url) as repo:
            repo_files = repo.get_all_files()
            local_repo_path = repo.temp_dir

            # 4. Informationen extrahieren
            update_status("ℹ️ Extrahiere Basis-Informationen...")
            info_extractor = ProjektInfoExtractor()
            basic_project_info = info_extractor.extrahiere_info(dateien=repo_files, repo_url=repo_url)

            update_status("🌲 Erstelle Dateibaum & Beziehungen...")
            repo_file_tree = repo.get_file_tree()
            rel_analyzer = ProjectAnalyzer(project_root=local_repo_path)
            rel_analyzer.analyze()
            raw_relationships = rel_analyzer.get_raw_relationships()

            update_status("🌳 AST Analyse...")
            ast_analyzer = ASTAnalyzer()   
            ast_schema = ast_analyzer.analyze_repository(files=repo_files, repo=repo)
            ast_schema = ast_analyzer.merge_relationship_data(ast_schema, raw_relationships)

            # 5. Helper LLM Vorbereitung
            update_status("⚙️ Vorbereitung Helper LLM...")
            helper_llm_function_input = []
            helper_llm_class_input = []

            for filename, file_data in ast_schema['files'].items():
                nodes = file_data.get('ast_nodes', {})
                for fn in nodes.get('functions', []):
                    ctx = fn.get('context', {})
                    helper_llm_function_input.append(FunctionAnalysisInput(
                        mode='function_analysis', identifier=fn.get('identifier'),
                        source_code=fn.get('source_code'), imports=nodes.get('imports', []),
                        context=FunctionContextInput(calls=ctx.get('calls', []), called_by=[cb for cb in ctx.get('called_by', []) if isinstance(cb, dict)])
                    ))
                for cl in nodes.get('classes', []):
                    ctx = cl.get('context', {})
                    helper_llm_class_input.append(ClassAnalysisInput(
                        mode='class_analysis', identifier=cl.get('identifier'),
                        source_code=cl.get('source_code'), imports=nodes.get('imports', []),
                        context=ClassContextInput(
                            dependencies=ctx.get('dependencies', []), instantiated_by=[ib for ib in ctx.get('instantiated_by', []) if isinstance(ib, dict)],
                            method_context=[MethodContextInput(identifier=m.get('identifier'), calls=m.get('calls', []), called_by=[cb for cb in m.get('called_by', []) if isinstance(cb, dict)], args=m.get('args', []), docstring=m.get('docstring')) for m in ctx.get('method_context', [])]
                        )
                    ))

            llm_helper = LLMHelper(api_key=helper_api_key, function_prompt_path='SystemPrompts/SystemPromptFunctionHelperLLM.txt', class_prompt_path='SystemPrompts/SystemPromptClassHelperLLM.txt', model_name=helper_model, base_url=helper_base_url)
            analysis_results = {"functions": {}, "classes": {}}

            # Helper LLM Ausführung
            update_status(f"🤖 Helper LLM: Analysiere {len(helper_llm_function_input)} Funktionen...")
            t_start_h = time.time()
            if helper_llm_function_input:
                res_f = llm_helper.generate_for_functions(helper_llm_function_input)
                for r in res_f: 
                    if r: analysis_results["functions"][r.identifier] = r.model_dump()
            
            if helper_llm_class_input:
                if helper_model.startswith("gemini-"): time.sleep(65)
                update_status(f"🤖 Helper LLM: Analysiere {len(helper_llm_class_input)} Klassen...")
                res_c = llm_helper.generate_for_classes(helper_llm_class_input)
                for r in res_c:
                    if r: analysis_results["classes"][r.identifier] = r.model_dump()
            
            total_helper_time = calculate_net_time(t_start_h, time.time(), len(helper_llm_function_input)+len(helper_llm_class_input), llm_helper.batch_size, helper_model)

            # 6. Main LLM Ausführung
            update_status(f"🧠 Main LLM: Generiere finalen Report ({main_model})...")
            main_llm_input = {"basic_info": basic_project_info, "file_tree": repo_file_tree, "ast_schema": ast_schema, "analysis_results": analysis_results}
            input_toon = encode(main_llm_input)
            savings_data = estimate_savings(main_llm_input)

            main_llm = MainLLM(api_key=main_api_key, prompt_file_path="SystemPrompts/SystemPromptMainLLMToon.txt", model_name=main_model, base_url=main_base_url)
            if helper_model == main_model and main_model.startswith("gemini-"): time.sleep(65)
            
            t_start_m = time.time()
            final_report = main_llm.call_llm(input_toon)
            total_main_time = time.time() - t_start_m

            if not final_report or len(final_report.strip()) < 10:
                raise ValueError("Main-Modell lieferte keine Antwort.")

            # Metriken & Speichern
            metrics = {"helper_time": round(total_helper_time, 2), "main_time": round(total_main_time, 2), "total_time": round(total_helper_time + total_main_time, 2), "helper_model": helper_model, "main_model": main_model, "json_tokens": savings_data['json_tokens'], "toon_tokens": savings_data['toon_tokens'], "savings_percent": round(savings_data['savings_percent'], 2)}
            return {"report": final_report, "metrics": metrics}

    except Exception as e:
        logging.error(f"Error: {e}")
        raise

def notebook_workflow(input, api_keys, model, status_callback=None, check_stop=None):
    t_start = time.time()
    def update_status(msg):
        if check_stop and check_stop(): raise InterruptedError("Abgebrochen.")
        if status_callback: status_callback(msg)
        logging.info(msg)

    # API Key Logik
    gemini_key = api_keys.get("gemini")
    openai_key = api_keys.get("gpt")
    scads_key = api_keys.get("scadsllm")
    scads_url = api_keys.get("scadsllm_base_url")
    ollama_url = api_keys.get("ollama")
    user_os_key = api_keys.get("opensrc_key")
    user_os_url = api_keys.get("opensrc_url")

    if model.startswith("gpt-"): input_api_key, base_url = openai_key, None
    elif model.startswith("gemini-"):
        if not gemini_key: raise ValueError("Gemini Key fehlt.")
        input_api_key, base_url = gemini_key, None
    elif model == "llama3": input_api_key, base_url = None, ollama_url
    else:
        input_api_key = user_os_key if user_os_url else scads_key
        base_url = user_os_url if user_os_url else scads_url

    update_status("🔑 Validierung des API-Keys...")
    validate_llm_credentials(model, input_api_key, base_url)

    update_status("🔍 Klone Repo & bereite Notebooks vor...")
    url_match = re.search(r"https?://(?:www\.)?github\.com/[^\s]+", input)
    if not url_match: raise ValueError("Ungültige URL.")
    repo_url = url_match.group(0)

    try:
        with GitRepository(repo_url) as repo:
            repo_files = repo.get_all_files()
            info_extractor = ProjektInfoExtractor()
            basic_info = info_extractor.extrahiere_info(dateien=repo_files, repo_url=repo_url)
            processed_data = process_repo_notebooks(repo_files)

            if not processed_data:
                return {"report": "Keine Notebooks gefunden.", "metrics": {"total_time": round(time.time()-t_start, 2), "main_model": model}}

            notebook_ll = MainLLM(api_key=input_api_key, prompt_file_path="SystemPrompts/SystemPromptNotebookLLM.txt", model_name=model, base_url=base_url)
            notebook_reports = []

            for idx, (path, data) in enumerate(processed_data.items(), 1):
                update_status(f"🧠 Analysiere Notebook {idx}/{len(processed_data)}: {os.path.basename(path)}")
                
                # Payload Erstellung (Multimodal)
                intro = json.dumps({"basic_info": basic_info, "path": path}, indent=2)
                payload = [{"type": "text", "text": f"Context:\n{intro}\n\nStructure:\n"}]
                last_pos = 0
                for m in re.finditer(r'(<IMAGE_PLACEHOLDER index="(\d+)" mime="([^"]+)"/>)', data['xml']):
                    payload.append({"type": "text", "text": data['xml'][last_pos:m.start()]})
                    i_idx = int(m.group(2))
                    if i_idx < len(data['images']):
                        payload.append({"type": "image_url", "image_url": {"url": f"data:{m.group(3)};base64,{data['images'][i_idx]['data']}"}})
                    last_pos = m.end()
                payload.append({"type": "text", "text": data['xml'][last_pos:]})

                report = notebook_ll.call_llm(payload)
                notebook_reports.append(report if report else f"Fehler bei {os.path.basename(path)}")

            final_report = "\n\n---\n\n".join(notebook_reports)
            return {"report": final_report, "metrics": {"helper_time": 0, "main_time": round(time.time()-t_start, 2), "total_time": round(time.time()-t_start, 2), "helper_model": "None", "main_model": model, "json_tokens": 0, "toon_tokens": 0, "savings_percent": 0}}

    except Exception as e:
        logging.error(f"Error: {e}")
        raise
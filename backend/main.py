import logging
import os
import re
import json
import time
from datetime import datetime

from dotenv import load_dotenv

from backend.getRepo import GitRepository, RepoFile
from backend.AST_Schema import ASTAnalyzer
from backend.MainLLM import MainLLM
from backend.basic_info import ProjektInfoExtractor
from backend.HelperLLM import LLMHelper
from schemas.types import FunctionContextInput, FunctionAnalysisInput, ClassContextInput, ClassAnalysisInput


# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def main_workflow():
    # 1. User gibt Input
    user_input = "Analyze the following Git Repository https://github.com/christiand03/repo-onboarding-agent" # Dummy Data
    # https://github.com/pallets/flask
    # https://github.com/christiand03/repo-onboarding-agent

    # 2. Input ans Backend übergeben

    # 3. URL per Regex extrahieren
    repo_url = None

    url_pattern = r"https?://[^\s]+"
    match = re.search(url_pattern, user_input)

    if match:
        repo_url = match.group(0)
        logging.info(f"Extracted repository URL: {repo_url}")
    else:
        logging.error("No repository URL found in the user input.")
# -------- Hier noch Nachricht an Frontend zurückgeben --------
        raise ValueError("Could not find a valid URL in the provided input.")
    
    ## Eventuell Schritt 4 bis 8 outsourcen in tools.py
    # 4. getRepo ausführen 
    repo_files = []
    try: 
        with GitRepository(repo_url) as repo:
            repo_files = repo.get_all_files()
            logging.info(f"Total files retrieved from repository: {len(repo_files)}")
    except Exception as e:
        logging.error(f"Error retrieving repository files: {e}")
# -------- Hier noch Nachricht an Frontend zurückgeben --------
        raise

    # 5. Basic_Info ausführen
    logging.info("Extracting basic project information...")
    info_extractor = ProjektInfoExtractor()
    basic_project_info = info_extractor.extrahiere_info(dateien=repo_files, repo_url=repo_url)
    logging.info("Basic project information extracted.")
    #print(basic_project_info)

    # 6. File Tree ausführen
    logging.info("Generating file tree...")
    repo_file_tree = repo.get_file_tree()
    logging.info("File tree generated.")
    #print(repo_file_tree)

    # 7. AST ausführen
    logging.info("Starting AST analysis...")
    ast_analyzer = ASTAnalyzer()   
    ast_schema = ast_analyzer.analyze_repository(files=repo_files)
    #print(ast_schema)
    logging.info("AST analysis completed.")

    # 8. Callgraph ausführen 

    # 9. Dependecygraph ausführen 

    # 10. Daten verarbeiten für HelperLLM Input 
    logging.info("Processing data for HelperLLM input...")

    helper_llm_function_input = []
    helper_llm_class_input = []

    for filename, file_data in ast_schema['files'].items():
        ast_nodes = file_data.get('ast_nodes', {})
        imports = ast_nodes.get('imports', [])
        functions = ast_nodes.get('functions', [])
        classes = ast_nodes.get('classes', [])

        for function in functions:
            context = function.get('context', {})
            function_context = FunctionContextInput(
                calls = context.get('calls', []),
                called_by = context.get('called_by', [])
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
            class_context = ClassContextInput(
                dependencies = context.get('dependencies', []),
                instantiated_by = context.get('instantiated_by', []),
                method_context = context.get('method_context', [])
            )

            class_input = ClassAnalysisInput(
                mode = _class.get('mode', 'class_analysis'),
                identifier =_class.get('identifier'),
                source_code = _class.get('source_code'), 
                imports = imports, 
                context = class_context
            )
            
            helper_llm_class_input.append(class_input)
    
    logging.info(f"Total Functions to process: {len(helper_llm_function_input)}")
    logging.info(f"Total Classes to process: {len(helper_llm_class_input)}")
    
    # print("--------------------- Function Input -------------------")
    # if helper_llm_function_input:
    #     print("\n--- Example Function Input ---")
    #     print(helper_llm_function_input[0].model_dump_json(indent=2))
    # print("--------------------- Class Input -------------------")
    # if helper_llm_class_input:
    #     print("\n--- Example Class Input ---")
    #     print(helper_llm_class_input[0].model_dump_json(indent=2))

    # 11. HelperLLM Funktion Batch (Notfalls stückeln wegen RPM Limits) 
    function_prompt_file = 'SystemPrompts/SystemPromptFunctionHelperLLM.txt'
    class_prompt_file = 'SystemPrompts/SystemPromptClassHelperLLM.txt'
    llm_helper = LLMHelper(api_key=GEMINI_API_KEY, function_prompt_path=function_prompt_file, class_prompt_path=class_prompt_file)
    analysis_results = {}

    #raise ("Test End.")

    logging.info("\n--- Generating documentation for Functions ---")
    if len(helper_llm_function_input) != 0:
        function_analysis_results = llm_helper.generate_for_functions(helper_llm_function_input)

    if len(function_analysis_results) != 0:
        for doc in function_analysis_results:
            if doc:
                logging.info(f"Successfully generated doc for: {doc.identifier}")
                if "functions" not in analysis_results:
                    analysis_results["functions"] = {}
                analysis_results["functions"][doc.identifier] = doc.model_dump() 
            else:
                logging.warning(f"Failed to generate doc for a function")

    logging.info("Waiting to respect rate limits before class analysis...")
    time.sleep(61)
    # 12. HelperLLM Class Batch 

    logging.info("\n--- Generating documentation for Classes ---")
    if len(helper_llm_class_input) != 0:
        class_analysis_results = llm_helper.generate_for_classes(helper_llm_class_input)

    if len(class_analysis_results) != 0:
        for doc in class_analysis_results:
            if doc:
                logging.info(f"Successfully generated doc for: {doc.identifier}")
                if "classes" not in analysis_results:
                    analysis_results["classes"] = {}
                analysis_results["classes"][doc.identifier] = doc.model_dump() 
            else:
                logging.warning(f"Failed to generate doc for a class")

    # 13. Final Documentation Dictionary als Input für MainLLM 
    main_llm_input = {}
    
    main_llm_input["basic_info"] = basic_project_info
    main_llm_input["file_tree"] = repo_file_tree
    main_llm_input["ast_schema"] = ast_schema
    main_llm_input["analysis_results"] = analysis_results

    main_llm_input_json = json.dumps(main_llm_input, indent=2)
    
    # model validate muss noch gemacht werden
    
    # 14. final Report generieren (MainLLM)
    main_llm = MainLLM(api_key=GEMINI_API_KEY, prompt_file_path="SystemPrompts\SystemPromptMainLLM.txt")

    logging.info("Starting Synthesis Stage...")
    final_report = main_llm.call_llm(main_llm_input_json)
    logging.info("Synthesis Stage completed.")
    logging.info("Report generated.")
    
    # (15. Documenation an Frontend zurückgeben)

    # Optional: Speichern des finalen Berichts in einer Datei
    logging.info("Saving final report...")
    output_dir = "result"
    os.makedirs(output_dir, exist_ok=True)  

    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    
    report_filename = f"report_{timestamp}.md"
    report_filepath = os.path.join(output_dir, report_filename)
    
    with open(report_filepath, "w", encoding="utf-8") as f:
        f.write(final_report)
    
    logging.info(f"Final report saved to '{report_filepath}'.")


if __name__ == "__main__":
    main_workflow()
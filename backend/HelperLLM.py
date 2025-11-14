# HelperLLM.py

import os
import json
import logging
from typing import List, Dict, Any, Optional
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage
from pydantic import ValidationError

from schemas.types import (
    FunctionAnalysis, 
    ClassAnalysis,
    FunctionAnalysisInput,
    ClassAnalysisInput
)
from tools import prepare_llm_inputs_from_repo

# --- Configuration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class LLMHelper:
    """
    A class to interact with Google Gemini for generating code snippet documentation.
    It centralizes API interaction, error handling, and validates I/O using Pydantic.
    """
    def __init__(self, api_key: str, prompt_file_path: str, model_name: str = "gemini-flash-latest"):
        if not api_key:
            raise ValueError("Gemini API Key must be set.")
        
        try:
            with open(prompt_file_path, 'r', encoding='utf-8') as f:
                self.system_prompt = f.read()
        except FileNotFoundError:
            logging.error(f"System prompt file not found at: {prompt_file_path}")
            raise
        
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            api_key=api_key,
            temperature=0.2, # Leicht reduziert für mehr Konsistenz
        )
        logging.info(f"LLMHelper initialized with model '{model_name}'.")

    def _call_llm_and_parse(self, user_json_payload: str) -> Optional[Dict[str, Any]]:
        """
        PRIVATE: Calls the LLM and parses the response into a generic dictionary.
        It's the central point for raw API communication.
        """
        conversation = [SystemMessage(content=self.system_prompt), HumanMessage(content=user_json_payload)]
        content = ""
        try:
            logging.info("Calling Gemini API...")
            response = self.llm.invoke(conversation)
            content = response.content

            # --- ÄNDERUNG: Robustere Verarbeitung und besseres Logging ---
            # Logge IMMER die rohe Antwort, bevor wir versuchen zu parsen
            logging.debug(f"Raw LLM response received:\n---\n{content}\n---")

            # Fall 1: Die Antwort ist eine Liste (manchmal passiert das)
            if isinstance(content, list):
                if not content:
                    logging.error("LLM returned an empty list.")
                    return None
                # Nimm das erste Element, das wahrscheinlich den Inhalt enthält
                content = content[0] 
                if isinstance(content, dict) and 'text' in content:
                    content = content['text']

            # Fall 2: Die Antwort ist kein String (sollte nicht passieren, aber sicher ist sicher)
            if not isinstance(content, str):
                logging.error(f"LLM response content is not a string, but {type(content)}.")
                return None
            
            # Fall 3: Der String ist leer (Safety-Filter hat wahrscheinlich zugeschlagen)
            if not content.strip():
                logging.error("LLM returned an empty string. Likely blocked by safety filters.")
                return None

            # Bereinige den String von Markdown-Code-Blöcken, falls das LLM sie hinzufügt
            if content.strip().startswith("```json"):
                content = content.strip()[7:-3].strip()
            elif content.strip().startswith("```"):
                 content = content.strip()[3:-3].strip()
            
            logging.info("Parsing JSON response.")
            return json.loads(content)
        
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode LLM response as JSON: {e}")
            # Das Debug-Logging oben hat uns bereits den rohen Inhalt gezeigt.
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred during API call or parsing: {e}")
            return None

    def generate_for_function(self, function_input: FunctionAnalysisInput) -> Optional[FunctionAnalysis]:
        """Generates and validates documentation for a single function."""
        payload_dict = function_input.model_dump()
        json_payload = json.dumps(payload_dict, indent=2)
        
        generic_response = self._call_llm_and_parse(json_payload)
        
        if generic_response is None:
            return None

        try:
            validated_output = FunctionAnalysis.model_validate(generic_response)
            if validated_output.error:
                logging.warning(f"LLM reported an error for '{validated_output.identifier}': {validated_output.error}")
            return validated_output
        except ValidationError as e:
            logging.error(f"LLM output for function '{function_input.identifier}' failed Pydantic validation.")
            logging.error(f"Validation Error details: {e}")
            logging.debug(f"Invalid JSON received: {generic_response}") # Mehr Kontext bei Fehler
            return None

    def generate_for_class(self, class_input: ClassAnalysisInput) -> Optional[ClassAnalysis]:
        """Generates and validates documentation for a class."""
        payload_dict = class_input.model_dump()
        json_payload = json.dumps(payload_dict, indent=2)

        generic_response = self._call_llm_and_parse(json_payload)

        if generic_response is None:
            return None

        try:
            validated_output = ClassAnalysis.model_validate(generic_response)
            if validated_output.error:
                logging.warning(f"LLM reported an error for '{validated_output.identifier}': {validated_output.error}")
            return validated_output
        except ValidationError as e:
            logging.error(f"LLM output for class '{class_input.identifier}' failed Pydantic validation.")
            logging.error(f"Validation Error details: {e}")
            logging.debug(f"Invalid JSON received: {generic_response}") # Mehr Kontext bei Fehler
            return None


# --- Der Orchestrator bleibt unverändert ---

def main_orchestrator():
    """
    Simulates the main agent's loop.
    1. Calls the analysis tools to get structured LLM input packages.
    2. Processes functions first to gather their documentation.
    3. Processes classes using the previously generated method docs.
    4. Aggregates and displays the results.
    """
    REPO_URL = "https://github.com/christiand03/repo-onboarding-agent" 
    
    logging.info(f"--- Starting analysis for repository: {REPO_URL} ---")
    llm_jobs, repo_path = prepare_llm_inputs_from_repo(REPO_URL)

    if not llm_jobs:
        logging.error("Failed to generate LLM jobs from repository analysis. Exiting.")
        return

    logging.info(f"Generated {len(llm_jobs)} total analysis jobs. Local repo at: {repo_path}")

    function_jobs = [job for job in llm_jobs if job.get('mode') == 'function_analysis']
    class_jobs = [job for job in llm_jobs if job.get('mode') == 'class_analysis']
    
    prompt_file = 'SystemPrompts/SystempromptHelperLLM.txt'
    # WICHTIG: Pfad anpassen, falls das Skript von einem anderen Ort ausgeführt wird
    # Dieser relative Pfad geht davon aus, dass du das Skript aus dem Projekt-Root-Verzeichnis startest.
    # Wenn du es direkt aus dem 'backend'-Ordner startest, könnte der Pfad falsch sein.
    # Eine sicherere Variante wäre ein absoluter Pfad oder:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_file = os.path.join(os.path.dirname(script_dir), 'SystemPrompts', 'SystempromptHelperLLM.txt')


    llm_helper = LLMHelper(api_key=GEMINI_API_KEY, prompt_file_path=prompt_file)

    function_analysis_results: Dict[str, FunctionAnalysis] = {}
    class_analysis_results: Dict[str, ClassAnalysis] = {}

    logging.info(f"\n--- Phase 1: Generating documentation for {len(function_jobs)} functions/methods ---")
    for job_dict in function_jobs:
        try:
            function_input = FunctionAnalysisInput.model_validate(job_dict)
            doc = llm_helper.generate_for_function(function_input)
            
            if doc:
                logging.info(f"Successfully generated doc for function: {doc.identifier}")
                function_analysis_results[doc.identifier] = doc
            else:
                logging.warning(f"Failed to generate doc for function: {job_dict['identifier']}")
        except ValidationError as e:
            logging.error(f"Input validation failed for function job {job_dict.get('identifier', 'N/A')}: {e}")

    logging.info(f"\n--- Phase 2: Generating documentation for {len(class_jobs)} classes ---")
    for job_dict in class_jobs:
        try:
            class_input = ClassAnalysisInput.model_validate(job_dict)
            
            method_docs_for_class = []
            for method_id in class_input.context.method_identifiers:
                if method_id in function_analysis_results:
                    method_docs_for_class.append(function_analysis_results[method_id])
            
            class_input.context.methods_analysis = method_docs_for_class
            
            doc = llm_helper.generate_for_class(class_input)

            if doc:
                logging.info(f"Successfully generated doc for class: {doc.identifier}")
                class_analysis_results[doc.identifier] = doc
            else:
                logging.warning(f"Failed to generate doc for class: {job_dict['identifier']}")
        except ValidationError as e:
            logging.error(f"Input validation failed for class job {job_dict.get('identifier', 'N/A')}: {e}")

    final_documentation = {
        "repository_url": REPO_URL,
        "functions": {identifier: doc.model_dump() for identifier, doc in function_analysis_results.items()},
        "classes": {identifier: doc.model_dump() for identifier, doc in class_analysis_results.items()}
    }
    
    logging.info("\n--- Final Generated Documentation (Summary) ---")
    # Konvertiere dicts zu JSON-Strings für schönere Ausgabe
    final_documentation['functions'] = {k: json.loads(v.model_dump_json()) for k, v in function_analysis_results.items()}
    final_documentation['classes'] = {k: json.loads(v.model_dump_json()) for k, v in class_analysis_results.items()}

    print(json.dumps(final_documentation, indent=2))
    
    with open("final_documentation.json", "w", encoding="utf-8") as f:
        json.dump(final_documentation, f, indent=2, ensure_ascii=False)
    logging.info("Full documentation saved to 'final_documentation.json'")


if __name__ == "__main__":
    if not GEMINI_API_KEY:
        print("FATAL: Gemini API Key not found. Please create a .env file with GEMINI_API_KEY='your_key'")
    else:
        main_orchestrator()
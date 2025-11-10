import os
import json
import logging
from typing import List, Dict, Any, Optional, Union

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage, AIMessage
from pydantic import ValidationError

from schemas.types import (
    FunctionAnalysis, 
    ClassAnalysis,
    FunctionAnalysisInput,
    FunctionContextInput,
    ClassAnalysisInput,
    ClassContextInput
)

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
            temperature=0.3, 
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
            logging.info("API call successful. Parsing JSON response.")
            return json.loads(content)
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode LLM response as JSON: {e}")
            logging.debug(f"Raw LLM response: {content}")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred during API call: {e}")
            return None

    def generate_for_function(self, function_input: FunctionAnalysisInput) -> Optional[FunctionAnalysis]:
        """Generates and validates documentation for a single function."""
        # Pydantic's model_dump() creates a dictionary from the model
        payload_dict = function_input.model_dump()
        json_payload = json.dumps(payload_dict, indent=2)
        
        generic_response = self._call_llm_and_parse(json_payload)
        
        if generic_response is None:
            return None

        try:
            # --- Pydantic Output Validation ---
            validated_output = FunctionAnalysis.model_validate(generic_response)
            
            if validated_output.error:
                logging.warning(f"LLM reported an error for '{validated_output.identifier}': {validated_output.error}")

            return validated_output
            
        except ValidationError as e:
            # If the LLM output doesn't match the Pydantic model, this error is raised.
            logging.error(f"LLM output for function '{function_input.identifier}' failed validation.")
            logging.error(f"Validation Error details: {e}")
            return None

    def generate_for_class(self, class_input: ClassAnalysisInput) -> Optional[ClassAnalysis]:
        """Generates and validates documentation for a class."""
        payload_dict = class_input.model_dump()
        json_payload = json.dumps(payload_dict, indent=2)

        generic_response = self._call_llm_and_parse(json_payload)

        if generic_response is None:
            return None

        try:
            # --- Pydantic Output Validation ---
            validated_output = ClassAnalysis.model_validate(generic_response)

            if validated_output.error:
                logging.warning(f"LLM reported an error for '{validated_output.identifier}': {validated_output.error}")
                
            return validated_output

        except ValidationError as e:
            logging.error(f"LLM output for class '{class_input.identifier}' failed validation.")
            logging.error(f"Validation Error details: {e}")
            return None








# --- Main Orchestrator Loop (Example Usage) ---

def main_orchestrator():
    """
    Simulates the main agent's loop.
    1. Defines mock data from repository analysis.
    2. Processes functions first to gather their documentation.
    3. Processes classes using the previously generated method docs.
    4. Aggregates the results.
    """
    # 1. Mock data (this would come from your analysis tools)
    repo_analysis_results: List[Dict[str, Union[FunctionContextInput, ClassContextInput]]] = [
        {"type": "function", "data": FunctionContextInput(identifier="calculate_price", raw_code="def calculate_price(base, tax_rate, discount=0): return (base * (1 + tax_rate)) - discount", dependencies=["math"], called_by=["checkout"], calls_to=[])},
        {"type": "function", "data": FunctionContextInput(identifier="add_item", raw_code="def add_item(self, item, price): self.items[item] = price", dependencies=[], called_by=["main"], calls_to=[])},
        {"type": "function", "data": FunctionContextInput(identifier="get_total", raw_code="def get_total(self): return sum(self.items.values())", dependencies=[], called_by=["checkout"], calls_to=["sum"])},
        {"type": "class", "data": ClassContextInput(identifier="ShoppingCart", raw_code="class ShoppingCart:\n  def __init__(self, user_id): self.user_id = user_id; self.items = {}", dependencies=[], methods=["add_item", "get_total"])},
    ]

    # Initialize the helper
    prompt_file = '../SystemPrompts/SystempromptHelperLLM.txt' 
    llm_helper = LLMHelper(api_key=GEMINI_API_KEY, prompt_file_path=prompt_file)

    # This will be the final JSON containing all documentation
    final_documentation = {}

    # 2. Process all functions/methods first
    logging.info("--- Phase 1: Generating documentation for all functions/methods ---")
    for item in repo_analysis_results:
        if item["type"] == "function_analysis":
            func_context = item["data"]               # possibly needs to be adapted to actual dictionary format
            doc = llm_helper.generate_for_function(func_context)
            
            if doc:
                logging.info(f"Successfully generated doc for function: {doc['identifier']}")
                if "functions" not in final_documentation:
                    final_documentation["functions"] = {}
                final_documentation["functions"][doc['identifier']] = doc
            else:
                logging.warning(f"Failed to generate doc for function: {func_context['identifier']}")

    # 3. Process classes, using method docs as context
    logging.info("\n--- Phase 2: Generating documentation for classes ---")
    for item in repo_analysis_results:
        if item["type"] == "class_classanalysis":
            class_context = item["data"]            # possibly needs to be adapted to actual dictionary format
            
            method_docs_for_class = {}
            for method_name in class_context["methods"]:
                if "functions" in final_documentation and method_name in final_documentation["functions"]:
                    method_docs_for_class[method_name] = final_documentation["functions"][method_name]   # potentially needs to be changed

            doc = llm_helper.generate_for_class(class_context, method_docs_for_class)

            if doc:
                logging.info(f"Successfully generated doc for class: {doc['identifier']}")
                if "classes" not in final_documentation:
                    final_documentation["classes"] = {}
                final_documentation["classes"][doc['identifier']] = doc
            else:
                logging.warning(f"Failed to generate doc for class: {class_context['identifier']}")

    # 4. Display the final aggregated result
    logging.info("\n--- Final Generated Documentation ---")
    print(json.dumps(final_documentation, indent=2))


if __name__ == "__main__":
    if not GEMINI_API_KEY:
        print("FATAL: Gemini API Key not found. Please create a .env file with GEMINI_API_KEY='your_key'")
    else:
        main_orchestrator()
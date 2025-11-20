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
    def __init__(self, api_key: str, function_prompt_path: str, class_prompt_path: str, model_name: str = "gemini-flash-latest"):
        if not api_key:
            raise ValueError("Gemini API Key must be set.")
        
        try:
            with open(function_prompt_path, 'r', encoding='utf-8') as f:
                self.function_system_prompt = f.read()
        except FileNotFoundError:
            logging.error(f"Function system prompt file not found at: {function_prompt_path}")
            raise

        # Handle the second file
        try:
            with open(class_prompt_path, 'r', encoding='utf-8') as f:
                self.class_system_prompt = f.read()
        except FileNotFoundError:
            logging.error(f"Class system prompt file not found at: {class_prompt_path}")
            raise
        
        base_llm = ChatGoogleGenerativeAI(
            model=model_name,
            api_key=api_key,
            temperature=0.3, 
        )

        self.function_llm = base_llm.with_structured_output(FunctionAnalysis)
        self.class_llm = base_llm.with_structured_output(ClassAnalysis)

        self.raw_llm = base_llm

        logging.info(f"LLMHelper initialized with model '{model_name}'.")

    def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]:
        """Generates and validates documentation for a batch of functions."""
        if not function_inputs:
            return []

        # Create a list of JSON payloads from the input models
        json_payloads = [
            json.dumps(function_input.model_dump(), indent=2) 
            for function_input in function_inputs
        ]
       
        conversations = [[SystemMessage(content=self.function_system_prompt), HumanMessage(content=payload)] for payload in json_payloads]
        
        try:
            logging.info(f"Calling Gemini API in batch for {len(conversations)} functions...")
            validated_functions = self.function_llm.batch(conversations)

            logging.info("API batch call and parsing successful.")
            return validated_functions

        except Exception as e:
            logging.error(f"An unexpected error occurred during API batch call or parsing: {e}")
            return [None] * len(conversations)
        
            
    

    def generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]:
        """Generates and validates documentation for a batch of classes."""
        if not class_inputs:
            return []

        # Create a list of JSON payloads from the input models
        json_payloads = [
            json.dumps(class_input.model_dump(), indent=2)
            for class_input in class_inputs
        ]

        conversations = [[SystemMessage(content=self.class_system_prompt), HumanMessage(content=payload)] for payload in json_payloads]

        try:
            logging.info(f"Calling Gemini API in batch for {len(conversations)} classes...")
            validated_classes = self.class_llm.batch(conversations)
            
            logging.info("API batch call and parsing successful.")
            return validated_classes

        except Exception as e:
            logging.error(f"An unexpected error occurred during API batch call or parsing: {e}")
            return [None] * len(conversations)






def main_orchestrator():
    """
    Dummy Data and processing loop for testing the LLMHelper class.
    This version is syntactically correct and logically matches the Pydantic models.
    """
    
    # --- Step 1: Define the pre-computed analysis for each method ---
    
    # Example Input 1: For the 'add_item' function
    add_item_input = FunctionAnalysisInput.model_validate({
        "mode": "function_analysis",
        "identifier": "add_item",
        "source_code": """def add_item(self, item_name: str, quantity: int):
        \"\"\"Adds a specified quantity of an item to the inventory. If the item already exists, its quantity is increased.\"\"\"
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
    
        current_quantity = self.inventory.get(item_name, 0)
        self.inventory[item_name] = current_quantity + quantity
        print(f"Added {quantity} of {item_name}. New total: {self.inventory[item_name]}")""",
        "imports": [],
        "context": {
            "calls": ["self.inventory.get"],
            "called_by": ["process_shipment", "restock_api_endpoint"]
        }
    })

    # Example Input 2: For the 'check_stock' function
    check_stock_input = FunctionAnalysisInput.model_validate({
        "mode": "function_analysis",
        "identifier": "check_stock",
        "source_code": """def check_stock(self, item_name: str) -> int:
        \"\"\"Retrieves the current stock quantity for a given item.\"\"\"
        stock_level = self.inventory.get(item_name, 0)
        return stock_level""",
        "imports": [],
        "context": {
            "calls": ["self.inventory.get"],
            "called_by": ["fulfill_order", "ui_display_handler"]
        }
    })

    # Example Input 3: For the 'generate_report' function
    generate_report_input = FunctionAnalysisInput.model_validate({
        "mode": "function_analysis",
        "identifier": "generate_report",
        "source_code": """def generate_report(self) -> str:
        \"\"\"Generates a timestamped string summary of the current inventory state.\"\"\"
        timestamp = datetime.now()
        report_header = "Inventory Report as of: {ts}\\n".format(ts=timestamp)
        report_lines = [report_header]
        
        for item, quantity in self.inventory.items():
            line = "- {name}: {qty}".format(name=item, qty=quantity)
            report_lines.append(line)
            
        return "\\n".join(report_lines)""",
        "imports": ["from datetime import datetime"],
        "context": {
            "calls": ["datetime.now", "str.format"],
            "called_by": ["daily_cron_job", "admin_dashboard_export"]
        }
    })

    add_item_analysis = FunctionAnalysis.model_validate({
        "mode": "function_analysis",
        "identifier": "add_item",
        "description": {
            "overall": "Adds a specified quantity of an item to the inventory. If the item already exists, its quantity is increased.",
            "parameters": [
                {"name": "self", "type": "InventoryManager", "description": "The instance of the class."},
                {"name": "item_name", "type": "str", "description": "The name or ID of the item to add."},
                {"name": "quantity", "type": "int", "description": "The number of units to add. Must be a positive integer."}
            ],
            "returns": [],
            "usage_context": { "calls": "self.inventory.get", "called_by": "process_shipment and restock_api_endpoint" }
        },
        "error": None
    })

    check_stock_analysis = FunctionAnalysis.model_validate({
        "mode": "function_analysis",
        "identifier": "check_stock",
        "description": {
            "overall": "Retrieves the current stock quantity for a given item.",
            "parameters": [
                {"name": "self", "type": "InventoryManager", "description": "The instance of the class."},
                {"name": "item_name", "type": "str", "description": "The name or ID of the item to check."}
            ],
            "returns": [
                {"name": "stock_level", "type": "int", "description": "The quantity of the item in stock. Returns 0 if the item is not found."}
            ],
            "usage_context": { "calls": "self.inventory.get", "called_by": "fulfill_order and ui_display_handler" }
        },
        "error": None
    })

    generate_report_analysis = FunctionAnalysis.model_validate({
        "mode": "function_analysis",
        "identifier": "generate_report",
        "description": {
            "overall": "Generates a timestamped string summary of the current inventory state.",
            "parameters": [ {"name": "self", "type": "InventoryManager", "description": "The instance of the class."} ],
            "returns": [
                {"name": "report", "type": "str", "description": "A formatted string detailing all items and their quantities."}
            ],
            "usage_context": { "calls": "datetime.now and str.format", "called_by": "daily_cron_job and admin_dashboard_export" }
        },
        "error": None
    })

    class_input = ClassAnalysisInput(
        mode="class_analysis",
        identifier="InventoryManager",
        # NOTE: The indentation of this string is now fixed. It starts at column 0.
        source_code="""class InventoryManager:
    \"\"\"Manages stock levels for products in a warehouse.\"\"\"
    def __init__(self, warehouse_id: str):
        self.warehouse_id = warehouse_id
        self.inventory = {}  # item_name: quantity

    def add_item(self, item_name: str, quantity: int):
        \"\"\"Adds an item to the inventory.\"\"\"
        current_quantity = self.inventory.get(item_name, 0)
        self.inventory[item_name] = current_quantity + quantity

    def check_stock(self, item_name: str) -> int:
        \"\"\"Checks the stock of a specific item.\"\"\"
        return self.inventory.get(item_name, 0)

    def generate_report(self) -> str:
        \"\"\"Generates a summary report of the inventory.\"\"\"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_lines = [f"Inventory Report for {self.warehouse_id} at {timestamp}"]
        if not self.inventory:
            report_lines.append("Inventory is empty.")
        else:
            for item, quantity in self.inventory.items():
                report_lines.append(f"- {item}: {quantity}")
        return "\\n".join(report_lines)
""",
        imports=["from datetime import datetime"],
        context=ClassContextInput(
            dependencies=["datetime"],
            instantiated_by=["main_app_startup", "warehouse_worker_script"],
            methods_analysis=[
                add_item_analysis,
                check_stock_analysis,
                generate_report_analysis
            ]
        )
    )

    
    # The helper methods expect a LIST of inputs, so we wrap our single object in a list.
    input = [add_item_input, check_stock_input, generate_report_input]
    analysis = [add_item_analysis, check_stock_analysis, generate_report_analysis] 

    function_prompt_file = 'SystemPrompts/SystemPromptFunctionHelperLLM.txt'
    class_prompt_file = 'SystemPrompts/SystemPromptClassHelperLLM.txt'
    llm_helper = LLMHelper(api_key=GEMINI_API_KEY, function_prompt_path=function_prompt_file, class_prompt_path=class_prompt_file)

    # This will be the final JSON containing all documentation
    final_documentation = {}

    # The analysis of the methods is already provided in the context.
    logging.info("\n--- Generating documentation for classes ---")
    
    # The `generate_for_classes` method returns a list of results.
    analysis_results = llm_helper.generate_for_functions(input)

    # --- Step 4: Process the results ---
    
    # We loop through the list of results (even though there's only one in this case).
    for doc in analysis_results:
        if doc:
            logging.info(f"Successfully generated doc for: {doc.identifier}")
            if "classes" not in final_documentation:
                final_documentation["classes"] = {}
            # Use .model_dump() to convert the Pydantic object back to a dict for JSON serialization
            final_documentation["classes"][doc.identifier] = doc.model_dump() 
        else:
            logging.warning(f"Failed to generate doc for a class")

    # --- Step 5: Display the final aggregated result ---
    logging.info("\n--- Final Generated Documentation ---")
    print(json.dumps(final_documentation, indent=2))

if __name__ == "__main__":
    if not GEMINI_API_KEY:
        print("FATAL: Gemini API Key not found. Please create a .env file with GEMINI_API_KEY='your_key'")
    else:
        main_orchestrator()
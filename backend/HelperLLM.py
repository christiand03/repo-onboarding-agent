import os
import json
import logging
import time
from typing import List, Optional

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from schemas.types import (
    FunctionAnalysis, 
    ClassAnalysis,
    FunctionAnalysisInput,
    ClassAnalysisInput,
)

# --- Configuration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
SCADS_AI_KEY = os.getenv("SCADS_AI_KEY")
SCADSLLM_URL = os.getenv("SCADSLLM_URL")

class LLMHelper:
    """
    A class to interact with Google Gemini for generating code snippet documentation.
    It centralizes API interaction, error handling, and validates I/O using Pydantic.
    """
    def __init__(self, api_key: str, function_prompt_path: str, class_prompt_path: str, model_name: str = "gemini-2.0-flash-lite", base_url: str = None):
        
        
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
        
        # Batch-Size config
        self.model_name = model_name
        self._configure_batch_settings(model_name)


        if model_name.startswith("gemini-"):
            base_llm = ChatGoogleGenerativeAI(
                model=model_name,
                api_key=api_key,
                temperature=0.3, 
            )
        
        elif model_name.startswith("gpt-") and "openGPT" not in model_name:
            base_llm = ChatOpenAI(
                model=model_name,
                api_key=api_key,
                temperature=0.3,
            )

        elif "/" in model_name or model_name.startswith("alias-") or any(x in model_name for x in ["DeepSeek", "Teuken", "Llama", "Qwen", "gpt-oss", "openGPT"]):
            if not SCADSLLM_URL:
                raise ValueError(f"SCADSLLM_URL environment variable is required for model {model_name}")
            
            logging.info(f"Connecting to Custom API at {SCADSLLM_URL} for model {model_name}")
            
            base_llm = ChatOpenAI(
                model=model_name,
                api_key=api_key,
                base_url=SCADSLLM_URL,
                temperature=0.3,
            )

        else:
            target_url = base_url if base_url else OLLAMA_BASE_URL
            logging.info(f"Using Ollama at {target_url} for model {model_name}")
            base_llm = ChatOllama(
                model=model_name,
                temperature=0.3,
                base_url=target_url,
            )

        self.function_llm = base_llm.with_structured_output(FunctionAnalysis, method="json_schema")
        self.class_llm = base_llm.with_structured_output(ClassAnalysis, method="json_schema")

        self.raw_llm = base_llm

        logging.info(f"LLMHelper initialized with model '{model_name}'. Batch Size: {self.batch_size}")

    def _configure_batch_settings(self, model_name: str):

        if model_name == "gemini-2.0-flash-lite":
            self.batch_size = 30
        
        elif model_name == "gemini-flash-latest":
            self.batch_size = 10

        elif model_name == "gemini-2.5-flash":
            self.batch_size = 10
            
        elif model_name == "gemini-2.5-pro":
            self.batch_size = 2
        
        elif model_name == "gemini-2.0-flash":
            self.batch_size = 15

        elif model_name == "gemini-2.5-flash-lite":
            self.batch_size = 15

        elif model_name == "llama3":
            self.batch_size = 50

        elif model_name == "gpt-5.1":
            self.batch_size = 500

        elif model_name == "gpt-5-mini":
            self.batch_size = 500

        elif "/" in model_name or model_name.startswith("alias-") or any(x in model_name for x in ["DeepSeek", "Teuken", "Llama", "Qwen", "gpt-oss", "openGPT"]):
            self.batch_size = 500
            
        else:
            logging.warning(f"Unknown model '{model_name}', using conservative defaults.")
            self.batch_size = 2

    def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]:
        """Generates and validates documentation for a batch of functions."""

        BATCH_SIZE = self.batch_size
        WAITING_TIME = 62

        if not function_inputs:
            return []

        # Create a list of JSON payloads from the input models
        json_payloads = [
            json.dumps(function_input.model_dump(), indent=2) 
            for function_input in function_inputs
        ]
       
        conversations = [[SystemMessage(content=self.function_system_prompt), HumanMessage(content=payload)] for payload in json_payloads]

        all_validated_functions = []
        total_items = len(conversations)

        for i in range(0, total_items, BATCH_SIZE):

            batch_conversations = conversations[i:i + BATCH_SIZE]

            logging.info(f"Calling LLM {self.model_name} API for Batch {i // BATCH_SIZE + 1} (Items {i+1} to {min(i + BATCH_SIZE, total_items)} of {total_items})...")            
        
            try:
                batch_results = self.function_llm.batch(batch_conversations, config={"max_concurrency": self.batch_size})
                all_validated_functions.extend(batch_results)
                logging.info("Batch call successful.")

            except Exception as e:
                logging.error(f"An error occurred during batch {i // BATCH_SIZE + 1}: {e}")
                all_validated_functions.extend([None] * len(batch_conversations))
            
            if i + BATCH_SIZE < total_items:
                logging.info(f"Waiting {WAITING_TIME} seconds to respect rate limits...")
                time.sleep(WAITING_TIME)

        return all_validated_functions
        
            
    def generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]:
        """Generates and validates documentation for a batch of classes."""
        if not class_inputs:
            return []
        
        BATCH_SIZE = self.batch_size
        WAITING_TIME = 62

        # Create a list of JSON payloads from the input models
        json_payloads = [
            json.dumps(class_input.model_dump(), indent=2)
            for class_input in class_inputs
        ]

        conversations = [[SystemMessage(content=self.class_system_prompt), HumanMessage(content=payload)] for payload in json_payloads]

        all_validated_classes = []
        total_items = len(conversations)

        for i in range(0, total_items, BATCH_SIZE):

            batch_conversations = conversations[i:i + BATCH_SIZE]
            logging.info(f"Calling LLM {self.model_name} API for Batch {i // BATCH_SIZE + 1} (Items {i+1} to {min(i + BATCH_SIZE, total_items)} of {total_items})...")            

            try:
                batch_results = self.class_llm.batch(batch_conversations , config={"max_concurrency": self.batch_size})
                all_validated_classes.extend(batch_results)
                logging.info("Batch call successful.")

            except Exception as e:
                logging.error(f"An error occurred during batch {i // BATCH_SIZE + 1}: {e}")
                # Falls ein Fehler auftritt, füllen wir die Liste mit None auf, um die Reihenfolge zu wahren
                all_validated_classes.extend([None] * len(batch_conversations))

            if i + BATCH_SIZE < total_items:
                logging.info(f"Waiting {WAITING_TIME} seconds to respect rate limits...")
                time.sleep(WAITING_TIME)

        return all_validated_classes

import os
import logging
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, SystemMessage

# --- Configuration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SCADS_AI_KEY = os.getenv("SCADS_AI_KEY")
SCADSLLM_URL = os.getenv("SCADSLLM_URL")

class MainLLM:
    """
    Hauptklasse für die Interaktion mit dem LLM.
    """
    def __init__(self, api_key: str, prompt_file_path: str, model_name: str = "gemini-2.5-pro", base_url: str = None):
        if not api_key:
            if "ollama" not in model_name and not base_url:
                 pass
        
        try:
            with open(prompt_file_path, 'r', encoding='utf-8') as f:
                self.system_prompt = f.read()
        except FileNotFoundError:
            logging.error(f"System prompt file not found at: {prompt_file_path}")
            raise
        
        self.model_name = model_name
        
        CLIENT_CONFIG = {
            "max_retries": 0, 
            "timeout": 1200.0
        }

        if model_name.startswith("gemini-"):
            self.llm = ChatGoogleGenerativeAI(
                model=model_name,
                api_key=api_key,
                temperature=1.0,
                request_timeout=5000.0
            )

        elif model_name.startswith("gpt-") and "oss" not in model_name:
            self.llm = ChatOpenAI(
                model=model_name,
                api_key=api_key,
                temperature=1.0,
                **CLIENT_CONFIG 
            )
        elif "/" in model_name or model_name.startswith("alias-") or any(x in model_name for x in ["DeepSeek", "Teuken", "Llama", "Qwen", "gpt-oss", "openGPT"]):
            if not SCADSLLM_URL:
                raise ValueError(f"SCADSLLM_URL environment variable is required for model {model_name}")
            
            logging.info(f"Connecting to Custom API at {SCADSLLM_URL} for model {model_name}")
            
            self.llm = ChatOpenAI(
                model=model_name,
                api_key=api_key,
                base_url=SCADSLLM_URL,
                temperature=1.0,
                **CLIENT_CONFIG
            )

        else:
            target_url = base_url if base_url else OLLAMA_BASE_URL
            self.llm = ChatOllama(
                model=model_name,
                temperature=1.0,
                base_url=target_url,
            )

        logging.info(f"Main LLM initialized with model '{model_name}'.")
    
    def call_llm(self, user_input: str):
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=user_input)
        ]
        logging.info("Calling LLM with HelperLLM input...")

        try:
            response = self.llm.invoke(messages)
            logging.info("LLM call successful.")
            
            content = response.content
            
            if isinstance(content, list):
                text_parts = []
                for part in content:
                    if isinstance(part, str):
                        text_parts.append(part)
                    elif isinstance(part, dict) and "text" in part:
                        text_parts.append(part["text"])
                return "".join(text_parts)
            
            elif isinstance(content, str):
                return content
                
            else:
                return str(content)
            

        except Exception as e:
            logging.error(f"Error during LLM call: {e}")
            return None 

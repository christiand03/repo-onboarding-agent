import os
import logging
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, SystemMessage

# --- Configuration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

SCADSLLM_URL = os.getenv("SCADSLLM_URL")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")

class EvaluatorLLM:
    """
    Klasse für die Bewertung der generierten Dokumentation gegen den Source-Code-Kontext.
    """
    def __init__(self, api_key: str, prompt_file_path: str, model_name: str = "gpt-4o", base_url: str = None):
        if not api_key:
            pass 
        
        try:
            with open(prompt_file_path, 'r', encoding='utf-8') as f:
                self.system_prompt = f.read()
        except FileNotFoundError:
            logging.error(f"Evaluator system prompt file not found at: {prompt_file_path}")
            raise
        
        self.model_name = model_name

        if model_name.startswith("gemini-"):
            self.llm = ChatGoogleGenerativeAI(
                model=model_name,
                api_key=api_key,
                temperature=0.2, 
            )
        elif model_name.startswith("gpt-") and "openGPT" not in model_name:
            self.llm = ChatOpenAI(
                model=model_name,
                api_key=api_key,
                temperature=0.2,
            )
        elif "/" in model_name or model_name.startswith("alias-") or any(x in model_name for x in ["DeepSeek", "Teuken", "Llama", "Qwen", "gpt-oss", "openGPT"]):
             if not SCADSLLM_URL:
                raise ValueError(f"SCADSLLM_URL environment variable is required for model {model_name}")
             
             logging.info(f"Connecting Evaluator to Custom API at {SCADSLLM_URL}")
             self.llm = ChatOpenAI(
                model=model_name,
                api_key=api_key,
                base_url=SCADSLLM_URL,
                temperature=0.2,
            )
        else:
            target_url = base_url if base_url else OLLAMA_BASE_URL
            self.llm = ChatOllama(
                model=model_name,
                temperature=0.2,
                base_url=target_url,
            )

        logging.info(f"Evaluator LLM initialized with model '{model_name}'.")

    def evaluate(self, generated_documentation: str, source_context_toon: str):
        
        user_input_content = f"""
                I require a forensic audit of the following documentation.
                
                === DATA START ===
                
                *** PART 1: GROUND TRUTH (Structured Context: AST, FileTree, Analysis) ***
                [NOTE: This data represents the absolute truth about the code.]
                {source_context_toon}
                
                *** PART 2: CANDIDATE DOCUMENTATION (Markdown to Evaluate) ***
                {generated_documentation}
                
                === DATA END ===

                COMMAND: 
                Perform the evaluation based on the System Prompt rules. 
                Focus strictly on whether PART 2 accurately reflects the structures defined in PART 1.
                """

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=user_input_content)
        ]
        
        logging.info("Calling Evaluator LLM...")

        try:
            response = self.llm.invoke(messages)
            content = response.content
            
            if len(content) > len(generated_documentation) * 0.8 and "# Project Documentation" in content:
                logging.warning("Evaluator appears to have echoed the input. Marking as failed.")
                return "Error: Evaluator echoed input instead of grading."
                
            logging.info("Evaluation successful.")
            return content
        except Exception as e:
            logging.error(f"Error during Evaluator LLM call: {e}")
            return f"Error: Could not perform evaluation. {e}"
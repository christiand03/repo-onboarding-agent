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
    Klasse für die Bewertung von LLM-Outputs.
    """
    def __init__(self, api_key: str, prompt_file_path: str, model_name: str = "gpt-4o", base_url: str = None):
        if not api_key:
            pass # Error handling handled by caller usually
        
        try:
            with open(prompt_file_path, 'r', encoding='utf-8') as f:
                self.system_prompt = f.read()
        except FileNotFoundError:
            logging.error(f"Evaluator system prompt file not found at: {prompt_file_path}")
            raise
        
        self.model_name = model_name
        
        # Konfiguration der Clients
        if model_name.startswith("gemini-"):
            self.llm = ChatGoogleGenerativeAI(
                model=model_name,
                api_key=api_key,
                temperature=0.0, # Wichtig für Reproduzierbarkeit bei Evaluation
            )
        elif model_name.startswith("gpt-") and "openGPT" not in model_name:
            self.llm = ChatOpenAI(
                model=model_name,
                api_key=api_key,
                temperature=0.0,
            )
        elif "/" in model_name or model_name.startswith("alias-") or any(x in model_name for x in ["DeepSeek", "Teuken", "Llama", "Qwen", "gpt-oss", "openGPT"]):
             if not SCADSLLM_URL:
                raise ValueError(f"SCADSLLM_URL environment variable is required for model {model_name}")
             
             logging.info(f"Connecting Evaluator to Custom API at {SCADSLLM_URL}")
             self.llm = ChatOpenAI(
                model=model_name,
                api_key=api_key,
                base_url=SCADSLLM_URL,
                temperature=0.0,
            )
        else:
            target_url = base_url if base_url else OLLAMA_BASE_URL
            self.llm = ChatOllama(
                model=model_name,
                temperature=0.0,
                base_url=target_url,
            )

        logging.info(f"Evaluator LLM initialized with model '{model_name}'.")

    def evaluate(self, generated_documentation: str, source_context_toon: str):
        """Standard Evaluation für MainLLM (Markdown Reports)"""
        user_input_content = f"""
                I require a forensic audit of the following documentation.
                
                === DATA START ===
                *** PART 1: GROUND TRUTH (Structured Context) ***
                {source_context_toon}
                
                *** PART 2: CANDIDATE DOCUMENTATION (Markdown) ***
                {generated_documentation}
                === DATA END ===

                COMMAND: 
                Perform the evaluation based on the System Prompt rules.
                """
        
        raw_response = self._invoke_llm(user_input_content)

        if isinstance(raw_response, list):
            text_parts = []
            for part in raw_response:
                if isinstance(part, str):
                    text_parts.append(part)
                elif isinstance(part, dict) and "text" in part:
                    text_parts.append(part["text"])
            return "".join(text_parts)

        return str(raw_response) if raw_response is not None else None

    def evaluate_helper_analysis(self, original_source_code_json: str, generated_analysis_json: str):
        """
        Methode für das HelperLLM: Vergleicht Raw-Code (Input) mit generiertem JSON (Output).
        """
        user_input_content = f"""
                I require a forensic audit of the Code-to-JSON transformation.

                === DATA START ===

                *** PART 1: INPUT DATA (Ground Truth) ***
                This JSON defines the strict boundaries for the analysis.
                Pay close attention to the 'context' keys (calls, called_by).
                {original_source_code_json}

                *** PART 2: GENERATED ANALYSIS (Candidate) ***
                {generated_analysis_json}

                === DATA END ===

                COMMAND:
                Compare PART 2 against PART 1 based on the System Prompt rules.
                
                IMPORTANT: 
                When checking 'calls' or 'relationships', TRUST ONLY THE 'context' OBJECT IN PART 1. 
                Do NOT manually parse the source code to find new calls (like 'len', 'st.metric', etc.) if they are not listed in PART 1 context.
                """
        
        raw_response = self._invoke_llm(user_input_content)

        if isinstance(raw_response, list):
            text_parts = []
            for part in raw_response:
                if isinstance(part, str):
                    text_parts.append(part)
                elif isinstance(part, dict) and "text" in part:
                    text_parts.append(part["text"])
            return "".join(text_parts)

        return str(raw_response) if raw_response is not None else None

    def _invoke_llm(self, content: str):
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=content)
        ]
        try:
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            logging.error(f"Error during Evaluator LLM call: {e}")
            return f"Error: Could not perform evaluation. {e}"
import os
import logging
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage
 
class MainLLM:
    """
    Hauptklasse für die Interaktion mit dem LLM.
    """
    def __init__(self, api_key: str, prompt_file_path: str, model_name: str = "gemini-2.5-pro"):
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
            temperature=1.0, 
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
            return response.content
        except Exception as e:
            logging.error(f"Error during LLM call: {e}")
            return None

    def stream_llm(self, user_input: str):
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=user_input)
        ]
        logging.info("Calling LLM with 'stream'...")

        try:
            stream_iterator = self.llm.stream(messages)
            
            for chunk in stream_iterator:
                yield chunk.content
        except Exception as e:
            error_message = f"\n--- Error during LLM stream call: {e} ---"
            logging.error(error_message)
            yield error_message

# Für main.py:

    # logging.info("Starting Synthesis Phase...")
    # # final_report = main_llm.call_llm(processed_json)
    # logging.info("stream LLM for final report...")
    # full_response = ""
    # for token in main_llm.stream_llm(processed_json):
    # # ------ Statt print den Token ans Frontend schicken ------
    #     print(token, end="", flush=True)
    #     full_response += token    
    # final_report = full_response
    # logging.info("streaming complete.")
    # logging.info("final report generated.")
    # logging.info("Synthesis Phase completed.")
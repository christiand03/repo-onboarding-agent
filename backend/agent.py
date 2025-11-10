import os
import logging

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage, AIMessage
from langchain.agents import create_agent
from dotenv import load_dotenv

# --- Configuration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class LLM:
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
            temperature=1, 
        )
        logging.info(f"LLMHelper initialized with model '{model_name}'.")

class Agent:
    def __init__(self, llm: LLM, tools: list, system_prompt: str):
        self.agent = create_agent(
            llm=llm,
            tools=tools,
            system_prompt=system_prompt,
        )
        logging.info("Agent created with provided LLM and tools.")


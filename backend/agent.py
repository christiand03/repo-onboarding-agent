import sys
import os

#für main
import datetime

# Füge das übergeordnete Verzeichnis (das Projekt-Hauptverzeichnis) zum Python-Pfad hinzu
# Dies erlaubt es Python, den 'schemas'-Ordner zu finden
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from typing import List, Any, Dict

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage, SystemMessage

from tools import analyze_repository

# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class LLMClient:
    """
    Kapselt die LLM-Client-Konfiguration und -Initialisierung.
    """
    def __init__(self, api_key: str, model_name: str = "gemini-flash-latest", temperature: float = 1):
        if not api_key:
            raise ValueError("Gemini API Key must be provided.")
        
        self.model_name = model_name
        self.temperature = temperature
        self.api_key = api_key
        
        self.llm = self._create_llm_instance()
        logging.info(f"LLMClient initialized with model '{self.model_name}'.")

    def _create_llm_instance(self):
        """Erstellt die Instanz des LLM-Clients."""
        return ChatGoogleGenerativeAI(
            model=self.model_name,
            api_key=self.api_key,
            temperature=self.temperature,
        )

class RepoAnalysisAgent:
    """
    Kapselt die Logik für den Code-Analyse-Agenten.
    """
    def __init__(self, llm: ChatGoogleGenerativeAI, tools: List[Any], system_prompt_path: str):
        if not llm or not tools:
            raise ValueError("LLM and tools must be provided.")
            
        self.llm = llm
        self.tools = tools
        self.system_prompt = self._load_prompt_from_file(system_prompt_path)
        
        # Die `create_agent`-Funktion erstellt den fertigen, ausführbaren Agenten.
        self.agent_executor = self._create_agent()
        logging.info("RepoAnalysisAgent (using create_agent) fully initialized.")

    def _load_prompt_from_file(self, file_path: str) -> str:
        """Lädt den System-Prompt-Text aus einer Datei."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            logging.error(f"System prompt file not found at: {file_path}")
            raise

    def _create_agent(self) -> Any:
        """
        Erstellt den LangChain Agenten
        """
        # Die Funktion `create_agent` benötigt das Modell, die Tools und optional einen System-Prompt.
        # Sie kümmert sich intern um das Prompt-Templating und die Erstellung des Graphen.
        agent = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=self.system_prompt
        )
        return agent

    def run(self, user_query: str) -> str:
        """
        Führt den Agenten mit einer gegebenen Anfrage aus und gibt die finale,
        saubere Text-Antwort zurück.
        """
        logging.info(f"Agent starting run with query: '{user_query[:50]}...'")
        
        input_payload = {"messages": [{"role": "user", "content": user_query}]}
        response = self.agent_executor.invoke(input_payload)
        
        # Die finale Antwort-Nachricht extrahieren
        final_message = response.get('messages', [None])[-1]

        if isinstance(final_message, AIMessage):
            message_content = final_message.content
            
            # Fall 1: Der Inhalt ist eine Liste von "Teilen" (typisch für Gemini)
            if isinstance(message_content, list) and message_content:
                first_part = message_content[0]
                if isinstance(first_part, dict) and 'text' in first_part:
                    final_output = first_part['text']
                else:
                    # Fallback, falls die Struktur unerwartet ist
                    final_output = str(message_content)
            # Fall 2: Der Inhalt ist bereits ein einfacher String
            elif isinstance(message_content, str):
                final_output = message_content
            # Fall 3: Unerwarteter Inhalt
            else:
                final_output = "Error: AIMessage content was empty or in an unexpected format."
        else:
            logging.warning(f"Could not find an AIMessage in the final response. Full response: {response}")
            final_output = "Error: Could not extract a final AI response from the agent's output."

        logging.info("Agent run finished.")
        return final_output

# --- Hauptausführung ---
if __name__ == '__main__':
    if not GEMINI_API_KEY:
        raise ValueError("FATAL: Gemini API Key not found. Please create a .env file with GEMINI_API_KEY='your_key'")

    # 1. LLM-Client instanziieren
    llm_client = LLMClient(api_key=GEMINI_API_KEY)

    # 2. Liste der verfügbaren Tools
    available_tools = [analyze_repository]
    
    # 3. Den Hauptagenten instanziieren
    script_dir = os.path.dirname(__file__)
    prompt_path = os.path.join(script_dir, '..', 'SystemPrompts', 'SystemPromptMainLLM.txt')
    main_agent = RepoAnalysisAgent(
        llm=llm_client.llm,
        tools=available_tools,
        system_prompt_path=prompt_path
    )

    # 4. Den Agenten ausführen
    repo_to_analyze = "https://github.com/christiand03/repo-onboarding-agent" # Beispiel-URL
    
    task_prompt = (
        f"Please perform a complete analysis of the Git repository located at {repo_to_analyze}. "
        "After the analysis, generate the full technical documentation in Markdown format as your final output."
    )
    
    final_documentation = main_agent.run(task_prompt)
    
    # 5. Ergebnis in eine Datei im 'result'-Ordner speichern
    try:
        # Den Pfad zum 'result'-Ordner erstellen (relativ zum Projekt-Hauptverzeichnis)
        project_root = os.path.dirname(script_dir)
        result_dir = os.path.join(project_root, 'result')

        # Sicherstellen, dass der Ordner existiert; wenn nicht, wird er erstellt.
        os.makedirs(result_dir, exist_ok=True)

        # Einen sauberen Zeitstempel für den Dateinamen erstellen
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"result_{timestamp}.md"
        file_path = os.path.join(result_dir, file_name)

        # Die Dokumentation in die Datei schreiben
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_documentation)

        # Bestätigung für den Benutzer ausgeben
        logging.info("AGENTENLAUF ERFOLGREICH ABGESCHLOSSEN")
        logging.info(f"Dokumentation erfolgreich gespeichert in: {file_path}")

    except Exception as e:
        logging.error(f"Fehler beim Speichern der Ergebnisdatei: {e}")
        # Die Ausgabe trotzdem in der Konsole anzeigen, falls das Speichern fehlschlägt
        logging.error("\n--- FEHLER BEIM SPEICHERN, AUSGABE WIRD HIER ANGEZEIGT ---")
        logging.error(final_documentation)
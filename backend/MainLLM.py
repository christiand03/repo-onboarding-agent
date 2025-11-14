# MainLLM.py

import os
import logging
import sys
import json
from dotenv import load_dotenv
from datetime import datetime
import re

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage

# --- Pfad-Anpassung für Modul-Imports ---
# Dies stellt sicher, dass wir Module aus dem übergeordneten Verzeichnis importieren können
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importiere das Tool, das der Agent ausführen würde
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

class MainLLM:
    """
    Orchestriert den zweistufigen Workflow: Befehlserstellung und Synthese.
    Diese Klasse agiert als Schnittstelle zum "CodeScribe" LLM.
    """
    def __init__(self, api_key: str, system_prompt_path: str):
        """
        Initialisiert den MainLLM-Client.
        
        Args:
            api_key (str): Der API-Schlüssel für den LLM-Dienst.
            system_prompt_path (str): Der Pfad zur System-Prompt-Datei.
        """
        self.llm_client = LLMClient(api_key=api_key)
        try:
            with open(system_prompt_path, 'r', encoding='utf-8') as f:
                self.system_prompt = f.read()
            logging.info("System prompt for MainLLM loaded successfully.")
        except FileNotFoundError:
            logging.error(f"System prompt file not found at: {system_prompt_path}")
            raise

    def process_request(self, input_data: str) -> str:
        """
        Verarbeitet eine Eingabe, indem sie an das LLM gesendet wird.
        Diese Methode extrahiert den Textinhalt aus der potenziell komplexen
        Antwortstruktur des LLM-Clients.
        
        Args:
            input_data (str): Die Benutzereingabe oder die JSON-Daten.
                              
        Returns:
            str: Die reine Textantwort des LLM.
        """
        logging.info("Processing request with MainLLM...")
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=input_data)
        ]
        
        try:
            # Die Antwort von invoke() kann komplex sein (z.B. AIMessage)
            response = self.llm_client.llm.invoke(messages)
            logging.info("Successfully received response from MainLLM.")

            # --- NEUE EXTRAKTIONS-LOGIK ---
            # response.content ist der Ort, wo der Inhalt normalerweise steht.
            # Dieser Inhalt kann ein String oder eine Liste von Dictionaries sein.
            content = response.content
            
            if isinstance(content, list) and content:
                # Wenn es eine Liste ist, gehen wir davon aus, dass sie die
                # [{ 'type': 'text', 'text': '...' }] Struktur hat.
                # Wir nehmen den 'text'-Wert des ersten Elements.
                first_part = content[0]
                if isinstance(first_part, dict) and 'text' in first_part:
                    return first_part['text']

            # Wenn es bereits ein String ist oder die Extraktion fehlschlägt,
            # geben wir es direkt zurück.
            if isinstance(content, str):
                return content

            # Fallback für unerwartete Strukturen
            logging.warning(f"Unexpected response content type: {type(content)}. Converting to string.")
            return str(content)

        except Exception as e:
            logging.error(f"An error occurred while invoking the LLM: {e}")
            return f"Error: Could not process the request. Details: {e}"

def extract_json_from_response(response_text: str) -> str:
    """
    Extrahiert einen JSON-String aus einem Text, der möglicherweise
    in einem Markdown-Codeblock eingeschlossen ist.
    
    Args:
        response_text (str): Die rohe Antwort vom LLM.
        
    Returns:
        str: Der extrahierte, reine JSON-String.
    """
    # Sucht nach einem JSON-Block, der von ```json oder nur ``` umgeben ist.
    # re.DOTALL lässt den Punkt '.' auch Zeilenumbrüche matchen.
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", response_text, re.DOTALL)
    
    if match:
        # Wenn ein Markdown-Block gefunden wird, gib den Inhalt der ersten Gruppe zurück.
        return match.group(1)
    else:
        # Wenn kein Markdown-Block gefunden wird, nehmen wir an, die Antwort ist bereits reines JSON.
        # .strip() entfernt führende/nachfolgende Leerzeichen, was auch helfen kann.
        return response_text.strip()

def main_workflow():
    """
    Simuliert den vollständigen, autonomen Workflow von der Benutzeranfrage bis zum finalen Bericht.
    """
    if not GEMINI_API_KEY:
        logging.fatal("Gemini API Key not found. Please create a .env file with GEMINI_API_KEY='your_key'")
        return

    # --- Initialisierung ---
    # Beachte, dass wir den Pfad anpassen müssen, da das Skript in einem Unterordner läuft
    prompt_file = os.path.join(os.path.dirname(__file__), '..', 'SystemPrompts', 'SystemPromptMainLLM.txt')
    main_llm = MainLLM(api_key=GEMINI_API_KEY, system_prompt_path=prompt_file)

    # =========================================================================
    # === STAGE 1: COMMAND STAGE ==============================================
    # =========================================================================
    print("--- WORKFLOW START ---")
    user_request = "Please analyze the repository at https://github.com/pallets/flask"
    print(f"User Request: '{user_request}'\n")

    logging.info("Executing Command Stage...")
    command_json_str = main_llm.process_request(user_request)
    
    print("--- Command Stage Output (from MainLLM) ---")
    print(command_json_str)
    print("-" * 50)

# Bereinige die LLM-Antwort, um nur das JSON zu erhalten
    clean_json_str = extract_json_from_response(command_json_str)

    try:
        command_data = json.loads(clean_json_str)
        repo_url = command_data.get("repo_url")
        if not repo_url or not isinstance(repo_url, str):
            raise ValueError("Key 'repo_url' not found or is not a string in the command JSON.")
    except (json.JSONDecodeError, ValueError) as e:
        logging.error(f"Failed to parse command from MainLLM: {e}")
        logging.debug(f"Original LLM Response: {command_json_str}")
        logging.debug(f"Cleaned JSON String: {clean_json_str}")
        print("Workflow aborted due to invalid command from MainLLM.")
        return

    # =========================================================================
    # === AGENT SIMULATION ====================================================
    # =========================================================================
    print("\n--- Agent Simulation Stage ---")
    logging.info(f"Agent is now analyzing repository: {repo_url}")
    
    # Der "Agent" führt das Tool aus, das im Befehl angegeben wurde.
    analysis_results, _ = analyze_repository(repo_url) # _ fängt die Metadaten ab
    
    if analysis_results is None:
        logging.error("Repository analysis failed. Aborting workflow.")
        print("Workflow aborted because the analysis tool encountered a critical error.")
        return
        
    logging.info("Agent has completed the analysis.")
    # Die Ergebnisse werden für die nächste Stufe in einen JSON-String umgewandelt.
    analysis_json_for_llm = json.dumps(analysis_results, indent=2)
    
    # Optional: Speichere das Analyseergebnis in einer Datei zur Überprüfung
    with open("analysis_output.json", "w", encoding="utf-8") as f:
        f.write(analysis_json_for_llm)
    print("Agent analysis complete. Results saved to 'analysis_output.json'.")
    print("-" * 50)
    
    # =========================================================================
    # === STAGE 2: SYNTHESIS STAGE ============================================
    # =========================================================================
    print("\n--- Synthesis Stage ---")
    logging.info("Executing Synthesis Stage...")
    
    # Die JSON-Daten des Agenten werden als Eingabe für denselben LLM verwendet.
    # Der System-Prompt weist das LLM an, diese Eingabe anders zu behandeln.
    final_report = main_llm.process_request(analysis_json_for_llm)
    
    print("\n--- Synthesis Stage Output (Final Markdown Report from MainLLM) ---")
    print(final_report)
    print("-" * 50)
    
# --- Speichern des finalen Berichts ---
    # Definiere den Zielordner
    output_dir = "result"
    
    # Erstelle den Ordner, falls er nicht existiert. exist_ok=True verhindert einen Fehler, wenn der Ordner bereits da ist.
    os.makedirs(output_dir, exist_ok=True)
    
    # Generiere den Zeitstempel im Format TT_MM_JJJJ_HH-MM-SS
    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    
    # Erstelle den vollständigen Dateinamen
    report_filename = f"report_{timestamp}.md"
    
    # Kombiniere Pfad und Dateinamen auf eine betriebssystem-sichere Weise
    report_filepath = os.path.join(output_dir, report_filename)
    
    # Speichere die Datei
    with open(report_filepath, "w", encoding="utf-8") as f:
        f.write(final_report)
    
    print(f"\n--- WORKFLOW COMPLETE ---")
    print(f"Final report has been saved to '{report_filepath}'.")


if __name__ == "__main__":
    main_workflow()
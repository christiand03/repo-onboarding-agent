import logging
import os
import re
from datetime import datetime

from dotenv import load_dotenv

from getRepo import GitRepository, RepoFile
from AST import ASTAnalyzer
from MainLLM import MainLLM
from basic_info import ProjektInfoExtractor


# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if __name__ == "__main__":
    # 1. User gibt Input
    user_input = "Analyze the following Git Repository https://github.com/christiand03/repo-onboarding-agent" # Dummy Data
    
    # 2. Input ans Backend übergeben

    # 3. URL per Regex extrahieren
    repo_url = None

    url_pattern = r"https?://[^\s]+"
    match = re.search(url_pattern, user_input)

    if match:
        repo_url = match.group(0)
        logging.info(f"Extracted repository URL: {repo_url}")
    else:
        logging.error("No repository URL found in the user input.")
# -------- Hier noch Nachricht an Frontend zurückgeben --------
        raise ValueError("Could not find a valid URL in the provided input.")
    
    ## Eventuell Schritt 4 bis 8 outsourcen in tools.py
    # 4. getRepo ausführen 
    repo_files = []
    try: 
        with GitRepository(repo_url) as repo:
            repo_files = repo.get_all_files()
            logging.info(f"Total files retrieved from repository: {len(repo_files)}")
    except Exception as e:
        logging.error(f"Error retrieving repository files: {e}")
# -------- Hier noch Nachricht an Frontend zurückgeben --------
        raise

    # 5. Basic_Info ausführen
    logging.info("Extracting basic project information...")
    info_extractor = ProjektInfoExtractor()
    basic_project_info = info_extractor.extrahiere_info(dateien=repo_files, repo_url=repo_url)
    logging.info("Basic project information extracted.")

    # 6. File Tree ausführen
    logging.info("Generating file tree...")
    repo_file_tree = repo.get_file_tree()
    logging.info("File tree generated.")

    # 7. AST ausführen

    # 8. Callgraph ausführen 

    # 9. Dependecygraph ausführen 

    # 10. Daten verarbeiten für HelperLLM Input 

    # 11. HelperLLM Funktion Batch (Notfalls stückeln wegen RPM Limits) 

    # 12. HelperLLM Class Batch 

    # 13. Final Documentation Dictionary als Input für MainLLM 

    processed_json = "{...}"  # Platzhalter für das verarbeitete JSON

    # 14. final Report generieren (MainLLM)
    main_llm = MainLLM(api_key=GEMINI_API_KEY, prompt_file_path="SystemPrompts\SystemPromptMainLLM.txt")

    logging.info("Starting Synthesis Phase...")
    final_report = main_llm.call_llm(processed_json)
    logging.info("final report generated.")
    logging.info("Synthesis Phase completed.")
    
    # (15. Documenation an Frontend zurückgeben)

    # Optional: Speichern des finalen Berichts in einer Datei
    logging.info("Saving final report...")
    output_dir = "result"
    os.makedirs(output_dir, exist_ok=True)  

    timestamp = datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
    
    report_filename = f"report_{timestamp}.md"
    report_filepath = os.path.join(output_dir, report_filename)
    
    with open(report_filepath, "w", encoding="utf-8") as f:
        f.write(final_report)
    
    logging.info(f"Final report saved to '{report_filepath}'.")
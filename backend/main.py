import logging
import os

from dotenv import load_dotenv

from getRepo import GitRepository, RepoFile
from AST import ASTAnalyzer
from MainLLM import MainLLM


# --- Konfiguration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if __name__ == "__main__":
    # 1. User gibt Input
    repo_url = "https://github.com/christiand03/repo-onboarding-agent" # Dummy Data
    # 2. Input ans Backend übergeben

    # 3. URL per Regex extrahieren

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

    # 6. AST ausführen
    logging.info("Starting AST-Analysis...")
    ast_analyzer = ASTAnalyzer()
    ast_data = ast_analyzer.analyze_repository(files=repo_files, repo_url=repo_url)
    logging.info("AST-Analysis ready.")

    # 7. Callgraph ausführen

    # 8. Dependecygraph ausführen

    # 9. Daten verarbeiten für HelperLLM Input

    # 10. HelperLLM Funktion Batch (Notfalls stückeln wegen RPM Limits)

    # 11. HelperLLM Class Batch

    # 12. Final Documentation Dictionary als Input für MainLLM

    processed_json = "{...}"  # Platzhalter für das verarbeitete JSON

    # 13. final Report generieren (MainLLM)
    main_llm = MainLLM(api_key=GEMINI_API_KEY, prompt_file_path="SystemPrompts\SystemPromptMainLLM.txt")

    logging.info("Starting Synthesis Phase...")
    final_report = main_llm.call_llm(processed_json)
    logging.info("final report generated.")
    logging.info("Synthesis Phase completed.")
    # (14. Documenation an Frontend zurückgeben)
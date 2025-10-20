import os
import tempfile
import git

from dotenv import load_dotenv
import google.generativeai as genai

#load .env file
load_dotenv()

# Config Gemini API
# get API-Key from .env file
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    # if Key not found.
    raise ValueError("GOOGLE_API_KEY is not found in .env-file! Please create a .env-file with the key.")
genai.configure(api_key=GEMINI_API_KEY)

def clone_repo_to_temp_dir(repo_url: str):
    """
    Clones a public Git repository to a temporary folder.

    Args:
        repo_url (str): The URL of the Git repository (e.g. from GitHub).

    Returns:
        str: The path to the temporary folder if cloning was successful.
        None: If an error occurred.
    """
    try:
        # create temp directory
        temp_dir_path = tempfile.mkdtemp()
        
        print(f"temp created under: {temp_dir_path}")

        # clone the repo into the temp directory
        git.Repo.clone_from(repo_url, temp_dir_path)

        print("temp clone successful!")
        
        # return temp path.
        return temp_dir_path

    except git.GitCommandError as e:
        # This error occurs when Git itself reports a problem.
        print(f"Error cloning the repository: {e}")
        return None
    except Exception as e:
        # Catches all other unexpected errors.
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    test_repo_url = "https://github.com/christiand03/repo-onboarding-agent" # Beispiel-Repository
    
    # Use the function to clone the repo
    cloned_path = clone_repo_to_temp_dir(test_repo_url)

    if cloned_path:
        print(f"\nThe repository was successfully cloned to '{cloned_path}' ")
    else:
        print("\nCloning the repository failed.")
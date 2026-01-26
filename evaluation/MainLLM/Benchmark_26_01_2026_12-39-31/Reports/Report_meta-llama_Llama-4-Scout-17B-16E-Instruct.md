# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
    - **Description:** The Repo Onboarding Agent is a tool designed to streamline the process of onboarding repositories. It analyzes the repository's structure and codebase to provide insights and documentation.
    - **Key Features:**
      - Repository analysis
      - Code documentation generation
      - Automated setup and quick start guide
    - **Tech Stack:** 
      - Python
      - LangChain
      - Streamlit
      - Git

*   **Repository Structure:**
    ```mermaid
    graph LR
    root --> .env.example
    root --> .gitignore
    root --> SystemPrompts
    root --> analysis_output.json
    root --> backend
    root --> database
    root --> frontend
    root --> notizen
    root --> output.json
    root --> output.toon
    root --> readme.md
    root --> requirements.txt
    root --> result
    root --> schemas
    root --> statistics
    root --> test.json
    ```

## 2. Installation
### Dependencies
The project dependencies are listed in `requirements.txt`. To install them, run:
```bash
pip install -r requirements.txt
```
### Setup Guide
To set up the project, follow these steps:
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Initialize the environment variables.

### Quick Startup
To quickly start the project, run:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The Repo Onboarding Agent can be used to analyze repositories and generate documentation. The primary commands include:
- `streamlit run frontend/frontend.py`: Runs the frontend application.
- `python backend/main.py`: Runs the main workflow for analyzing a repository.

## 4. Architecture
The architecture of the Repo Onboarding Agent consists of the following components:
- **Frontend**: A Streamlit application for user interaction.
- **Backend**: A Python module for analyzing the repository and generating documentation.
- **Database**: A MongoDB database for storing user data and chat exchanges.

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** A class for traversing the Abstract Syntax Tree (AST) of Python source code to extract metadata about imports, classes, and functions.
*   **Instantiation:** The class is instantiated by the `ASTAnalyzer` class.
*   **Dependencies:** The class depends on the `ast` and `os` modules.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with the source code, file path, and project root.
    *   *Parameters:* `source_code`, `file_path`, `project_root`
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code: str, file_path: str, project_root: str)`
        *   *Description:* Initializes the ASTVisitor instance.
        *   *Parameters:*
          - **source_code** (`str`): The raw source code of the file being analyzed.
          - **file_path** (`str`): The absolute path to the Python file being visited.
          - **project_root** (`str`): The root directory of the project, used to determine the module path.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Processes `ast.Import` nodes to extract import statements.
        *   *Parameters:* `node` (`ast.Import`): The AST node representing an import statement.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Processes `ast.ImportFrom` nodes to extract import statements.
        *   *Parameters:* `node` (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Processes `ast.ClassDef` nodes to extract class definitions.
        *   *Parameters:* `node` (`ast.ClassDef`): The AST node representing a class definition.

### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** A class for building a graph of file-level import dependencies.
*   **Instantiation:** The class is instantiated by the `build_file_dependency_graph` function.
*   **Dependencies:** The class depends on the `ast` and `networkx` modules.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph instance.
    *   *Parameters:* `filename`, `repo_root`
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename: str, repo_root)`
        *   *Description:* Initializes the FileDependencyGraph instance.
        *   *Parameters:*
          - **filename** (`str`): The name of the file currently being analyzed for dependencies.
          - **repo_root** (`str`): The root directory of the repository, used for resolving file paths.
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* Resolves relative import statements.
        *   *Parameters:* `node` (`ast.ImportFrom`): The AST ImportFrom node representing the relative import statement.

### File: `backend/HelperLLM.py`
#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** A dummy data and processing loop for testing the LLMHelper class.
*   **Parameters:** None
*   **Returns:** None

### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** A class for interacting with the LLM.
*   **Instantiation:** The class is instantiated by the `main_workflow` function.
*   **Dependencies:** The class depends on the `langchain_google_genai` and `langchain_ollama` modules.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance.
    *   *Parameters:* `api_key`, `prompt_file_path`, `model_name`, `base_url`
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key: str, prompt_file_path: str, model_name: str = "gemini-2.5-pro", base_url: str = None)`
        *   *Description:* Initializes the MainLLM instance.
        *   *Parameters:*
          - **api_key** (`str`): The API key for authenticating with the chosen LLM service.
          - **prompt_file_path** (`str`): The file path to the system prompt used for LLM interactions.
          - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'.
          - **base_url** (`str`): An optional base URL for custom LLM endpoints.

### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str) -> str`
*   **Description:** Encrypts a given string using a `cipher_suite` object.
*   **Parameters:** `text` (`str`): The string value to be encrypted.
*   **Returns:** `encrypted_text` (`str`): The encrypted string.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str) -> str`
*   **Description:** Attempts to decrypt a given text string using a `cipher_suite` object.
*   **Parameters:** `text` (`str`): The string value to be decrypted.
*   **Returns:** `decrypted_or_original_text` (`str`): The decrypted string if successful, or the original string if decryption is not performed or if an error occurs.

---
</end_of_documentation>
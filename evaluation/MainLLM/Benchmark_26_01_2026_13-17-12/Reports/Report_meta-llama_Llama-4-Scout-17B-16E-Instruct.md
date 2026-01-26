# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
    - **Description:** The_REPO_Onboarding_Agent is designed to streamline the onboarding process for new repositories. It appears to be a tool that automates various tasks related to repository setup and management, potentially including code analysis, documentation generation, and integration with services like Streamlit for frontend deployment.
    - **Key Features:**
      - Automated code analysis and documentation generation.
      - Integration with Streamlit for frontend deployment.
      - Support for multiple Large Language Models (LLMs) for generating documentation.
      - Token usage evaluation and savings calculation.
    - **Tech Stack:**
      - Python
      - Streamlit
      - Langchain
      - Google Gemini API
      - Pydantic

*   **Repository Structure:**
    ```mermaid
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
The project dependencies can be installed via pip using the requirements.txt file:
```bash
pip install -r requirements.txt
```
### Setup Guide
The setup guide is not explicitly provided, but it typically involves:
1. Cloning the repository.
2. Installing dependencies using `pip install -r requirements.txt`.
3. Setting up environment variables (e.g., API keys for LLMs).

### Quick Startup
To quickly start the project, follow these minimal commands:
```bash
git clone https://github.com/your-repo/Repo-Onboarding-Agent.git
cd Repo-Onboarding-Agent
pip install -r requirements.txt
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The_REPO_Onboarding_Agent can be used for:
- Automated code analysis and documentation generation.
- Integration with Streamlit for deploying the frontend.
- Evaluating token usage and savings.

Primary commands or use cases include:
- Running the Streamlit frontend: `streamlit run frontend/frontend.py`.
- Generating documentation for a repository.

## 4. Architecture
No Mermaid syntax is provided for the architecture.

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** Extracts and structures metadata about imports, classes, and functions within a given Python source file.
*   **Instantiation:** This class is instantiated during the analysis of a Python file to build its AST schema.
*   **Dependencies:** This class depends on `path_to_module` for resolving module paths.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root.
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
        *   *Parameters:*
          - **node** (`ast.Import`): The AST node representing an import statement.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles `ast.ImportFrom` nodes for 'from ... import ...' statements.
        *   *Parameters:*
          - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Processes `ast.ClassDef` nodes to extract class definitions.
        *   *Parameters:*
          - **node** (`ast.ClassDef`): The AST node representing a class definition.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes `ast.FunctionDef` nodes to extract function or method definitions.
        *   *Parameters:*
          - **node** (`ast.FunctionDef`): The AST node representing a function or method definition.

### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** Extracts import dependencies for a Python file by traversing its AST.
*   **Instantiation:** This class is instantiated during the construction of a file dependency graph.
*   **Dependencies:** This class depends on `get_all_temp_files`, `init_exports_symbol`, and `module_file_exists` for resolving module and symbol existence.

### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** Provides a centralized interface for interacting with LLMs to generate structured documentation.
*   **Instantiation:** This class is instantiated with an API key, function and class prompt paths, and a model name.

### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str) -> str`
*   **Description:** Encrypts a given string using a `cipher_suite` object.
*   **Parameters:**
  - **text** (`str`): The string value to be encrypted.
*   **Returns:**
  - **encrypted_text** (`str`): The encrypted string.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str) -> str`
*   **Description:** Attempts to decrypt a given text string using a `cipher_suite` object.
*   **Parameters:**
  - **text** (`str`): The string value to be decrypted.
*   **Returns:**
  - **decrypted_or_original_text** (`str`): The decrypted string if successful, or the original string if decryption is not performed or if an error occurs.

### File: `frontend/frontend.py`
#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** Displays a single chat exchange within a Streamlit application.
*   **Parameters:**
  - **ex** (`dict`): A dictionary representing a single chat exchange.
  - **current_chat_name** (`str`): The name of the current chat.

---
</end.documentation>
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** The Repo Onboarding Agent is an automated pipeline designed to clone, analyze, and document software repositories. It utilizes Abstract Syntax Trees (AST) and relationship analysis to map out project structures, which are then synthesized by Large Language Models (LLMs) to generate comprehensive technical documentation.
- **Key Features:** 
  - Automated repository cloning and file structure extraction.
  - AST-based analysis of functions, classes, and imports.
  - Relationship and call-graph analysis to determine code dependencies.
  - Multi-LLM support (Gemini, GPT, Ollama) for intelligent documentation synthesis.
  - Token efficiency optimization using the TOON format.
- **Tech Stack:** Python, Streamlit, LangChain, Pydantic, NetworkX, GitPython, MongoDB, and Matplotlib.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root[root] --> backend[backend/<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
    root --> database[database/<br/>db.py]
    root --> frontend[frontend/<br/>frontend.py]
    root --> schemas[schemas/<br/>types.py]
    root --> prompts[SystemPrompts/<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt]
    root --> meta[requirements.txt<br/>readme.md<br/>.env.example]
    ```

## 2. Installation
### Dependencies
The project relies on a variety of libraries for LLM orchestration, GUI rendering, and code analysis.
- **Key Libraries:** `langchain`, `streamlit`, `pydantic`, `networkx`, `GitPython`, `pymongo`, `matplotlib`.
- **Full list:** Note the `requirements.txt` file in the root directory.

To install all dependencies:
```bash
pip install -r requirements.txt
```

### Setup Guide
1.  **Environment Variables:** Copy `.env.example` to `.env`.
2.  **API Keys:** Configure your LLM API keys (e.g., Gemini, OpenAI) and database credentials in the `.env` file or via the frontend settings.
3.  **Database:** Ensure a MongoDB instance is accessible as specified in your configuration.

### Quick Startup
Launch the Streamlit dashboard to start analyzing repositories:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
- **Automated Repository Analysis:** Enter a GitHub URL into the UI to generate a full technical report.
- **Architecture Visualization:** Generate and view Mermaid diagrams representing file dependencies and function call graphs.
- **Efficiency Benchmarking:** Use the internal "Token-Comparison" feature to see how the TOON format reduces LLM context usage compared to standard JSON.
- **Notebook Processing:** Convert Jupyter Notebooks into a structured XML format for LLM analysis.

---

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to a specified project root. If the file is a Python file, it removes the '.py' extension. Subsequently, it replaces path separators with dots to form the module path. Special handling is included for '__init__.py' files.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:** *Analysis data not available for this component.*

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) of Python source code. Its primary purpose is to extract and structure metadata about imports, classes, and functions found within a given source file.
*   **Instantiation:** This class is not explicitly instantiated by any known components within the provided context.
*   **Dependencies:** This class depends on `backend.AST_Schema.path_to_module` for resolving module paths.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor with the source code, file path, and project root. It calculates the module path and sets up an empty schema dictionary.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the Python file being visited.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* Processes `ast.Import` nodes. It iterates through each alias in the import statement and appends it to the schema.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   **Usage:** Called by the `ast.NodeVisitor`'s dispatch mechanism.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* Handles `ast.ImportFrom` nodes. It constructs fully qualified import names by combining the module name with aliases.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   **Usage:** Called by the `ast.NodeVisitor`'s dispatch mechanism.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* Processes `ast.ClassDef` nodes. Constructs a dictionary containing detailed info about the class (docstring, source code, lines).
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   **Usage:** Called by the `ast.NodeVisitor`'s dispatch mechanism.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: ast.FunctionDef)`
        *   *Description:* Processes function definitions, distinguishing between methods within a class and top-level functions.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   **Usage:** Called by the dispatch mechanism and `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef)`
        *   *Description:* Handles asynchronous function definitions by delegating directly to `visit_FunctionDef`.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   **Usage:** Called by the dispatch mechanism.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process source code to build a structured AST schema. It analyzes individual files to extract functions and classes and merges external relationship data (call graphs).
*   **Instantiation:** Not explicitly instantiated in provided context.
*   **Dependencies:** Depends on `backend.AST_Schema.ASTVisitor` for parsing and `os/ast` for logic.
*   **Constructor:**
    *   *Description:* Initializes the ASTAnalyzer class. Performs no explicit setup, creating a stateless instance.
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self: ASTAnalyzer, full_schema: dict, raw_relationships: dict)`
        *   *Description:* Integrates raw relationship data (incoming/outgoing calls) into the full schema.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): The comprehensive schema containing file and node data.
            - **raw_relationships** (`dict`): A dictionary containing raw 'outgoing' and 'incoming' call relationships.
        *   **Returns:**
            - **full_schema** (`dict`): The updated schema.
        *   **Usage:** Not explicitly called in provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self: ASTAnalyzer, files: list, repo: GitRepository)`
        *   *Description:* Processes a list of file objects from a Git repository to construct a full AST schema.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): List of file objects with 'path' and 'content'.
            - **repo** (`GitRepository`): Object representing the Git repository.
        *   **Returns:**
            - **full_schema** (`dict`): A dictionary representing the AST schema of the repository.
        *   **Usage:** Not explicitly called in provided context.

---

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** Constructs a directed graph representing file-level import dependencies within an AST.
*   **Parameters:**
    - **filename** (`str`): The path to the file being analyzed.
    - **tree** (`AST`): The AST of the file.
    - **repo_root** (`str`): The root directory for resolving relative imports.
*   **Returns:**
    - **graph** (`networkx.DiGraph`): A directed graph where nodes are files and edges are dependencies.
*   **Usage:** Called by `build_repository_graph`.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** Constructs a directed graph representing the dependencies between Python files across an entire Git repository.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): Aggregated dependency graph.
*   **Usage:** *Analysis data not available for this component.*

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** Locates all Python files within a specified directory and subdirectories.
*   **Parameters:**
    - **directory** (`str`): Root directory to search.
*   **Returns:**
    - **all_files** (`list[Path]`): List of relative paths to Python files.
*   **Usage:** Called by `FileDependencyGraph._resolve_module_name`.

#### Class: `FileDependencyGraph`
*   **Summary:** Extends `ast.NodeVisitor` to traverse the AST and identify import dependencies, supporting robust resolution of relative imports.
*   **Instantiation:** Instantiated by `build_file_dependency_graph`.
*   **Dependencies:** `get_all_temp_files`.
*   **Constructor:**
    *   *Description:* Initializes the instance with the target filename and repo root.
    *   *Parameters:*
        - **filename** (`str`): File being analyzed.
        - **repo_root** (`str`): Repository root.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(node: ImportFrom)`
        *   *Description:* Resolves relative import statements (e.g., `from .. import x`).
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node for the relative import.
        *   **Returns:**
            - **resolved** (`list[str]`): List of resolved module or symbol names.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* Records imported module names as dependencies.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ImportFrom)`
        *   *Description:* Invoked when an ImportFrom node is encountered; handles both absolute and relative resolution.

---

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** Serves as a dummy data and processing loop for testing the `LLMHelper` class using Pydantic models.
*   **Usage:** *Analysis data not available for this component.*

#### Class: `LLMHelper`
*   **Summary:** Provides a centralized interface for interacting with LLMs (Gemini, OpenAI, Ollama) to generate structured documentation based on Pydantic schemas.
*   **Instantiation:** Instantiated in `main_workflow`.
*   **Constructor:**
    *   *Description:* Sets up API keys, loads prompts, and configures the LLM client and batch settings.
    *   *Parameters:*
        - **api_key** (`str`): Auth key.
        - **function_prompt_path** (`str`): Path to function prompt.
        - **class_prompt_path** (`str`): Path to class prompt.
        - **model_name** (`str`): Name of the model (e.g., "gemini-2.0-flash-lite").
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(model_name: str)`
        *   *Description:* Sets `batch_size` based on the specific model and its rate limits.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* Generates structured documentation for functions in batches.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(class_inputs: List[ClassAnalysisInput])`
        *   *Description:* Generates structured documentation for classes in batches.

---

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** Generates a bar chart comparing JSON vs TOON token counts and saves the image.
*   **Parameters:**
    - **json_tokens** (`int`): Count of tokens in JSON.
    - **toon_tokens** (`int`): Count of tokens in TOON.
    - **savings_percent** (`float`): Percentage saved.
    - **output_path** (`str`): Save location.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable | None)`
*   **Description:** The primary orchestrator. Clones the repo, runs AST/relationship analysis, calls the Helper LLM for snippets, and finally the Main LLM for the report.

---

### File: `database/db.py`

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** Hashes the password and creates a new user document in MongoDB.
*   **Parameters:**
    - **username** (`str`): The unique ID.
    - **name** (`str`): User's full name.
    - **password** (`str`): Plaintext password.
*   **Returns:**
    - **inserted_id** (`Any`): The DB ID of the new user.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** Fetches and decrypts (using Fernet) API keys stored for the user.

---

### File: `schemas/types.py`

#### Class: `FunctionAnalysis`
*   **Summary:** Pydantic model representing the structured JSON output for a single function analysis.
*   **Methods:** *No specific methods defined beyond Pydantic boilerplate.*

#### Class: `ClassAnalysis`
*   **Summary:** Pydantic model representing the structured JSON output for an entire class analysis, including its nested methods.

---

### File: `backend/scads_key_test.py`
*No analysis data available for this file.*

---

### File: `frontend/frontend.py`

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** Renders a single chat exchange (User Q + Assistant A) in Streamlit, including a toolbar for feedback, download, and deletion.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str, should_stream: bool)`
*   **Description:** Processes markdown text to detect and render Mermaid code blocks using `st_mermaid`.

---
# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
      - Could not be determined due to a missing README file and insufficient context.
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** 
      - Information not found

## 2. Installation
### Dependencies
The project requires the following dependencies:
- altair==4.2.2
- annotated-types==0.7.0
- anyio==4.11.0
- attrs==25.4.0
- bcrypt==5.0.0
- blinker==1.9.0
- cachetools==6.2.2
- captcha==0.7.1
- certifi==2025.11.12
- cffi==2.0.0
- charset-normalizer==3.4.4
- click==8.3.1
- colorama==0.4.6
- contourpy==1.3.3
- cryptography==46.0.3
- cycler==0.12.1
- distro==1.9.0
- dns-python==2.8.0
- dotenv==0.9.9
- entrypoints==0.4
- extra-streamlit-components==0.1.81
- filetype==1.2.0
- fonttools==4.61.0
- gidgetb==4.0.12
- GitPython==3.1.45
- google-ai-generative-language==0.9.0
- google-api-core==2.28.1
- google-auth==2.43.0
- googleapis-common-protos==1.72.0
- grpcio==1.76.0
- grpcio-status==1.76.0
- h11==0.16.0
- httpcore==1.0.9
- httpx==0.28.1
- idna==3.11
- Jinja2==3.1.6
- jiter==0.12.0
- jsonpatch==1.33.0
- jsonpointer==3.0.0
- jsonschema==4.25.1
- jsonschema-specifications==2025.9.1
- kiwisolver==1.4.9
- langchain==1.0.8
- langchain-core==1.1.0
- langchain-google-genai==3.1.0
- langchain-ollama==1.0.0
- langchain-openai==1.1.0
- langgraph==1.0.3
- langgraph-checkpoint==3.0.1
- langgraph-prebuilt==1.0.5
- langsmitch==0.4.46
- MarkupSafe==3.0.3
- matplotlib==3.10.7
- numpy==2.3.5
- ollama==0.6.1
- openai==2.8.1
- orjson==3.11.4
- ormsgpack==1.12.0
- packaging==25.0
- pandas==2.3.3
- pillow==12.0.0
- proto-plus==1.26.1
- protobuf==6.33.1
- pyarrow==2.1.0.0
- pyaudio==2.21.0
- pyaasn1==0.6.1
- pycparser==2.23
- pydantic==2.12.4
- pydantic-core==2.41.5
- pydeck==6.0.3
- referencing==0.37.0
- regex==2025.11.3
- requests==2.32.5
- requests-toolbelt==1.0.0
- rpds-py==0.29.0
- rsa==4.9.1
- setuptools==69.0.1
- six==1.17.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.51.0
- streamlit-authenticator==0.4.2
- tenacity==9.1.2
- tiktoken==0.12.0
- toml==0.10.2
- toolz==1.1.0
- toon-format==9c4f0c0c24f2a0b0b3
- tornado==6.5.2
- tqdm==4.67.1
- typing-inspection==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2

### Setup Guide
Information not found

### Quick Startup
Information not found

## 3. Use Cases & Commands
The repository appears to be for a repo onboarding agent. It seems to be designed to streamline the process of onboarding new repositories, possibly by automating tasks such as setting up CI/CD pipelines, creating documentation, or configuring repository settings.

## 4. Architecture
No Mermaid syntax provided.

## 5. Code Analysis

### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** A class used to traverse an Abstract Syntax Tree (AST) generated from Python source code.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root.
    *   *Parameters:* `self`, `source_code`, `file_path`, `project_root`
*   **Methods:**
    *   `__init__`
        *   *Signature:* `def __init__(self, source_code: str, file_path: str, project_root: str)`
        *   *Description:* Initializes the ASTVisitor.
        *   *Parameters:*
          - **source_code** (`str`): The full source code string of the file being analyzed.
          - **file_path** (`str`): The file path of the source code being processed.
          - **project_root** (`str`): The root directory of the project being analyzed.
    *   `visit_Import`
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import nodes in the AST.
        *   *Parameters:* `self`, `node`
    *   `visit_ImportFrom`
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Processes import-from nodes in the AST.
        *   *Parameters:* `self`, `node`
    *   `visit_ClassDef`
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Handles class definition nodes in the AST.
        *   *Parameters:* `self`, `node`
    *   `visit_FunctionDef`
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definition nodes in the AST.
        *   *Parameters:* `self`, `node`
    *   `visit_AsyncFunctionDef`
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definition nodes in the AST.
        *   *Parameters:* `self`, `node`

#### Class: `ASTAnalyzer`
*   **Summary:** A class responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs).
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class.
    *   *Parameters:* `self`
*   **Methods:**
    *   `__init__`
        *   *Signature:* `def __init__(self)`
        *   *Description:* Initializes the ASTAnalyzer.
        *   *Parameters:* 
    *   `_enrich_schema_with_callgraph`
        *   *Signature:* `def _enrich_schema_with_callgraph(self, schema: dict, call_graph: nx.DiGraph, filename: str)`
        *   *Description:* Enriches a given schema with call graph information.
        *   *Parameters:*
          - **schema** (`dict`): A dictionary representing the schema containing functions and classes.
          - **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions and methods.
          - **filename** (`str`): The filename associated with the schema being enriched.
    *   `merge_relationship_data`
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, relationship_data: list) -> dict`
        *   *Description:* Merges relationship data into a full schema.
        *   *Parameters:*
          - **full_schema** (`dict`): A dictionary representing the full schema of the repository.
          - **relationship_data** (`list`): A list of dictionaries containing relationship information for identifiers.
        *   *Returns:* `full_schema`, The updated schema with merged relationship data.
    *   `analyze_repository`
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository) -> dict`
        *   *Description:* Analyzes a repository by processing a list of files.
        *   *Parameters:*
          - **files** (`list`): A list of file objects to be analyzed.
          - **repo** (`GitRepository`): An object representing the Git repository being analyzed.
        *   *Returns:* `full_schema`, A dictionary containing the aggregated schema for all processed files.

### File: `backend/File_Dependency.py`
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph`
*   **Description:** Constructs a directed graph representing file dependencies within a repository.
*   **Parameters:**
    - **filename** (`str`): The name of the file being analyzed for dependencies.
    - **tree** (`AST`): The abstract syntax tree of the file being analyzed.
    - **repo_root** (`str`): The root directory path of the repository being analyzed.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph representing file dependencies.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository) -> nx.DiGraph`
*   **Description:** Constructs a dependency graph for all Python files within a given Git repository.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object containing the files to analyze for dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependency relationships between Python files in the repository.

### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** A class to interact with Google Gemini for generating code snippet documentation.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API credentials and prompt files.
    *   *Parameters:*
      - **api_key** (`str`): API key for accessing the language model service.
      - **function_prompt_path** (`str`): Path to the file containing the system prompt for function documentation generation.
      - **class_prompt_path** (`str`): Path to the file containing the system prompt for class documentation generation.
      - **model_name** (`str`): Name of the language model to use. Defaults to 'gemini-2.0-flash-lite'.
      - **base_url** (`str`): Base URL for custom API endpoints. Optional.
*   **Methods:**
    *   `__init__`
        *   *Signature:* `def __init__(self, api_key: str, function_prompt_path: str, class_prompt_path: str, model_name: str = "gemini-2.0-flash-lite", base_url: str = None)`
        *   *Description:* Initializes the LLMHelper.
        *   *Parameters:*
    *   `_configure_batch_settings`
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing requests based on the specified model name.
        *   *Parameters:* `self`, `model_name`
    *   `generate_for_functions`
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]`
        *   *Description:* Generates and validates documentation for a batch of functions.
        *   *Parameters:* `self`, `function_inputs`
        *   *Returns:* `result`, A list of validated function analysis results or None for failed items.
    *   `generate_for_classes`
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]`
        *   *Description:* Generates and validates documentation for a batch of classes.
        *   *Parameters:* `self`, `class_inputs`
        *   *Returns:* `result`, A list of validated class analysis results or None for failed items.

### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str) -> str`
*   **Description:** Encrypts a given text string using a cipher suite.
*   **Parameters:**
    - **text** (`str`): The text string to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input text.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str) -> str`
*   **Description:** Decrypts a given text using a cipher suite.
*   **Parameters:**
    - **text** (`str`): The encrypted text to be decrypted.
*   **Returns:**
    - **return_value** (`str`): The decrypted text if successful.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** Inserts a new user into the database.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain text password of the user.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** Retrieves all user documents from a MongoDB collection.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** Retrieves a single user document from a MongoDB collection.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** Updates the name field of a user document in a MongoDB collection.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** Updates a user's Gemini API key in the database.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** Updates the Ollama base URL for a specified user in the database.

### File: `frontend/Frontend.py`
#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** Handles the saving of a Gemini API key entered by the user.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** Saves a new Ollama URL entered by the user into the database.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** Loads Chats and Exchanges consistently from the DB.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** Updates the feedback value for a given exchange object.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** Handles the deletion of an exchange from the database.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** Handles the deletion of a chat.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** Extracts a repository name from any URL present in the text.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** Yields each word in the text followed by a space.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream=False)`
*   **Description:** Processes markdown text to identify and render Mermaid diagrams.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** Renders a chat exchange in a Streamlit interface.

---
</end.documentation>
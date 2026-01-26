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
- gitdb==4.0.12
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
- langchain-ollama==1.1.0
- langchain-openai==1.1.0
- langgraph==1.0.3
- langgraph-checkpoint==3.0.1
- langgraph-prebuilt==1.0.5
- langsmitsh==0.4.46
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
- pyarrow==2.1.0
- pyas1==0.6.1
- pyasn1==0.4.2
- pycparser==2.23
- pydantic==2.12.4
- pydantic-core==2.41.5
- pydick==0.9.1
- PyJWT==2.10.1
- pymongo==4.15.4
- pymongocrypt==1.2.6
- pyparsing==3.2.5
- python-dateutil==2.9.0.post0
- python-dotenv==2.9.0
- pytz==2025.2
- PyYAML==6.0.3
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
- streamlit-authenticator==0.2.5
- tenacity==9.1.2
- tiktoken==0.12.0
- toml==0.10.2
- toolz==1.1.0
- toon-format  @  githttps://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b3c5f4b8763c15f4b8f8707f8c9c0de6
- tornado==6.5.2
- tqdm==4.67.1
- typing-inspection==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0

### Setup Guide
Information not found

### Quick Startup
Information not found

## 3. Use Cases & Commands
The repository appears to be for a repo onboarding agent. The primary use case seems to be related to onboarding repositories, possibly for documentation or analysis purposes.

## 4. Architecture

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** A class for traversing the Abstract Syntax Tree (AST) of Python source code to collect information about imports, functions, and classes.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root.
    *   *Parameters:* `self`, `source_code`, `file_path`, `project_root`
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code: str, file_path: str, project_root: str)`
        *   *Description:* Initializes the ASTVisitor.
        *   *Parameters:*
          - **source_code** (`str`): The full source code string of the file being analyzed.
          - **file_path** (`str`): The file path of the source code being processed.
          - **project_root** (`str`): The root directory of the project being analyzed.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import nodes in the AST.
        *   *Parameters:*
          - **node** (`ast.Import`): An AST node representing an import statement.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Processes import-from nodes in the AST.
        *   *Parameters:*
          - **node** (`ast.ImportFrom`): An AST node representing an import-from statement.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Handles class definition nodes in the AST.
        *   *Parameters:*
          - **node** (`ast.ClassDef`): An AST node representing a class definition.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definition nodes in the AST.
        *   *Parameters:*
          - **node** (`ast.FunctionDef`): An AST node representing a function definition.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definition nodes in the AST.
        *   *Parameters:*
          - **node** (`ast.AsyncFunctionDef`): An AST node representing an asynchronous function definition.

#### Class: `ASTAnalyzer`
*   **Summary:** A class responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class.
    *   *Parameters:* `self`
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema: dict, call_graph: nx.DiGraph, filename: str)`
        *   *Description:* Enriches a given schema with call graph information.
        *   *Parameters:*
          - **schema** (`dict`): A dictionary representing the schema containing functions and classes.
          - **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions and methods.
          - **filename** (`str`): The filename associated with the schema being enriched.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, relationship_data: list) -> dict`
        *   *Description:* Merges relationship data into a full schema.
        *   *Parameters:*
          - **full_schema** (`dict`): A dictionary representing the full schema of the repository.
          - **relationship_data** (`list`): A list of dictionaries containing relationship information for identifiers.
        *   *Returns:* `full_schema` (`dict`): The updated schema with merged relationship data.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository) -> dict`
        *   *Description:* Analyzes a repository by processing a list of files.
        *   *Parameters:*
          - **files** (`list`): A list of file objects to be analyzed.
          - **repo** (`GitRepository`): An object representing the Git repository being analyzed.
        *   *Returns:* `full_schema` (`dict`): A dictionary containing the aggregated schema for all processed files.

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
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing requests based on the specified model name.
        *   *Parameters:*
          - **model_name** (`str`): Name of the language model for which to configure batch settings.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]`
        *   *Description:* Processes a batch of function inputs to generate and validate documentation using the configured LLM.
        *   *Parameters:*
          - **function_inputs** (`List[FunctionAnalysisInput]`): A list of function input models containing information needed for documentation generation.
        *   *Returns:* `result` (`List[Optional[FunctionAnalysis]]`): A list of validated function analysis results or None for failed items.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]`
        *   *Description:* Processes a batch of class inputs to generate and validate documentation using the configured LLM.
        *   *Parameters:*
          - **class_inputs** (`List[ClassAnalysisInput]`): A list of class input models containing information needed for documentation generation.
        *   *Returns:* `result` (`List[Optional[ClassAnalysis]]`): A list of validated class analysis results or None for failed items.

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
*   **Returns:**
    - **inserted_id** (`ObjectId`): The unique identifier of the newly inserted user document.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** Retrieves all user documents from a MongoDB collection.
*   **Parameters:** None
*   **Returns:**
    - **result** (`list`): A list containing all user documents retrieved from the 'dbusers' MongoDB collection.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** Retrieves a single user document from a MongoDB collection.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) used to locate and retrieve a specific user document.
*   **Returns:**
    - **result** (`Any`): A single user document retrieved from the MongoDB collection.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** Updates the name field of a user document in a MongoDB collection.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose name needs to be updated.
    - **new_name** (`str`): The new name value to set for the specified user.
*   **Returns:**
    - **result.modified_count** (`int`): The number of documents that were modified as a result of the update operation.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** Updates a user's Gemini API key in the database.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The unencrypted Gemini API key provided by the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were successfully modified in the database.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** Updates the Ollama base URL for a specified user in the database.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose Ollama base URL needs to be updated.
    - **ollama_base_url** (`str`): The new Ollama base URL to be set for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were successfully modified by the update operation.

### File: `frontend/Frontend.py`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** Handles the saving of a Gemini API key entered by the user in a Streamlit frontend application.
*   **Parameters:** None
*   **Returns:** None

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** Saves a new Ollama URL entered by the user into the database.
*   **Parameters:** None
*   **Returns:** None

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** Loads chats and exchanges consistently from the database for a given user.
*   **Parameters:**
    - **username** (`str`): The name of the user for whom the data is to be loaded from the database.
*   **Returns:** None

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** Updates the feedback value for a given exchange object in the database and triggers a re-render of the Streamlit application.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing an exchange object.
    - **val** (`Any`): The new feedback value to be assigned to the exchange object.
*   **Returns:** None

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** Handles the deletion of an exchange from the database and updates the session state.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be removed.
    - **ex** (`dict`): A dictionary representing the exchange to be deleted.
*   **Returns:** None

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** Handles the deletion of a chat by removing it from the database and cleaning up the session state.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** None

---
</end$end.documentation>
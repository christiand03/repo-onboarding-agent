# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
      - aktueller_status: Information not found
      - key_features: Information not found
      - tech_stack: Information not found

## 2. Installation 
### Dependencies
- aiter==4.2.2
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
- gidgethub==4.0.12
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
- langs mith==0.4.46
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
- pyasrn1==0.6.1
- pyasrn1_modules==0.4.2
- pycparser==2.23
- pydantic==2.12.4
- pydantic-core==2.41.5
- pydick==0.9.1
- PyJWT==2.10.1
- pymongo==4.15.4
- pypa rsing==3.2.5
- python-dateutil==2.9.0.post0
- python-dotenv==0.9.9
- pytz==2025.2
- PyYAML==6.0.3
- referencing==0.37.0
- regex==2025.11.3
- requests==2.33.0
- requests-toolbelt==1.0.0
- rpds-py==0.2.0
- rsa==4.9.1
- setuptools==69.0.1
- six==1.16.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.5.1
- streamlit-mermaid==1.1.0
- tenacity==9.1.2
- tiktoken==0.12.0
- toml==0.10.2
- toolz==1.1.0
- toon-format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b37
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
Information not found

## 4. Architecture

## 5. Code Analysis
### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** null
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* null
    *   *Parameters:* 
      - **self** 
      - **source_code** (str): The full source code of the file being analyzed.
      - **file_path** (str): The file path of the source code being analyzed.
      - **project_root** (str): The root directory of the project.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code: str, file_path: str, project_root: str)`
        *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It sets up internal tracking variables such as module path, schema storage, and current class context. The schema is initialized with empty lists for imports, functions, and classes.
        *   *Parameters:* 
          - **self** 
          - **source_code** (str): The full source code of the file being analyzed.
          - **file_path** (str): The file path of the source code being analyzed.
          - **project_root** (str): The root directory of the project.
        *   *Returns:* 
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST by extracting the names of imported modules and appending them to the schema's imports list. It processes each alias in the import statement and adds it to the list before continuing the generic visit.
        *   *Parameters:* 
          - **self** 
          - **node** (ast.Import): The AST node representing an import statement.
        *   *Returns:* 
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST by extracting the full module paths of imported items and appending them to the schema's imports list. It constructs the full qualified name for each imported item and appends it to the list before continuing the generic visit.
        *   *Parameters:* 
          - **self** 
          - **node** (ast.ImportFrom): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* 
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Processes class definitions in the AST by creating a structured representation of the class and adding it to the schema. It assigns a unique identifier based on the module path and class name, extracts docstrings and source code segments, and tracks start and end lines. It also sets the current class context for subsequent function processing.
        *   *Parameters:* 
          - **self** 
          - **node** (ast.ClassDef): The AST node representing a class definition.
        *   *Returns:* 
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Handles function definitions in the AST by either associating them with the current class context or adding them as top-level functions to the schema. It generates identifiers for functions based on their context (either module or class), extracts arguments, docstrings, and source code segments, and tracks line numbers. If the function is within a class, it stores the function information in the class's context.
        *   *Parameters:* 
          - **self** 
          - **node** (ast.FunctionDef): The AST node representing a function definition.
        *   *Returns:* 
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions in the AST by delegating to the visit_FunctionDef method. This allows async functions to be processed in the same way as regular functions, maintaining consistent handling of both sync and async function definitions.
        *   *Parameters:* 
          - **self** 
          - **node** (ast.AsyncFunctionDef): The AST node representing an asynchronous function definition.
        *   *Returns:* 

#### Class: `ASTAnalyzer`
*   **Summary:** null
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any operations.
    *   *Parameters:* 
      - **self** 
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any operations.
        *   *Parameters:* 
          - **self** 
        *   *Returns:* 
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema: dict, call_graph: nx.DiGraph, filename: str)`
        *   *Description:* This static method enriches a given schema with call graph information by updating function and method contexts with details about which functions they call and which functions call them. It iterates over functions and class methods in the schema and updates their context fields based on the provided call graph.
        *   *Parameters:* 
          - **schema** (dict): A dictionary representing the schema of a parsed file, containing functions and classes.
          - **call_graph** (nx.DiGraph): A NetworkX directed graph representing the call relationships between functions.
          - **filename** (str): The path of the file being processed, used to construct unique keys for lookup in the call graph.
        *   *Returns:* 
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, relationship_data: list) -> dict`
        *   *Description:* This method merges relationship data into a full schema by mapping identifiers from relationship data to corresponding entries in the schema. It updates function and class contexts with 'called_by' information and class contexts with 'instantiated_by' information based on the provided relationship data.
        *   *Parameters:* 
          - **self** 
          - **full_schema** (dict): A dictionary representing the full schema of the repository, containing file structures and AST nodes.
          - **relationship_data** (list): A list of dictionaries containing relationship information, including identifiers and called_by lists.
        *   *Returns:* 
          - **full_schema** (dict): The updated full schema with merged relationship data.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository) -> dict`
        *   *Description:* This method analyzes a list of Python files within a Git repository by parsing their ASTs, visiting nodes to extract schema information, and enriching that schema with call graph data. It constructs a full schema of files, functions, and classes, handling potential parsing errors gracefully.
        *   *Parameters:* 
          - **self** 
          - **files** (list): A list of file objects containing paths and content of Python files to be analyzed.
          - **repo** (GitRepository): An object representing the Git repository containing the files to be analyzed.
        *   *Returns:* 
          - **full_schema** (dict): A dictionary representing the full schema of the repository, including parsed AST nodes for each file.

---
### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** null
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up internal attributes to track the current file being processed and the root directory of the repository.
    *   *Parameters:* 
      - **self** 
      - **filename** (str): The name of the file being analyzed for dependencies.
      - **repo_root** (Any): The root directory path of the repository containing the file.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename: str, repo_root)`
        *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up internal attributes to track the current file being processed and the root directory of the repository.
        *   *Parameters:* 
          - **self** 
          - **filename** (str): The name of the file being analyzed for dependencies.
          - **repo_root** (Any): The root directory path of the repository containing the file.
        *   *Returns:* 
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ImportFrom) -> list[str]`
        *   *Description:* Resolves relative import statements by analyzing the import node and determining the actual module or symbol names. It checks for existing module files or symbols exported via __init__.py and raises an ImportError if resolution fails.
        *   *Parameters:* 
          - **self** 
          - **node** (ImportFrom): An AST node representing a relative import statement.
        *   *Returns:* 
          - **resolved** (list[str]): A list of resolved module or symbol names.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None = None)`
        *   *Description:* Processes import statements by adding the imported module names to the dependency mapping for the current file. It ensures that the import dependencies dictionary is initialized for the current file before adding entries.
        *   *Parameters:* 
          - **self** 
          - **node** (Import | ImportFrom): An AST node representing an import statement.
          - **base_name** (str | None): Optional base name of the imported module.
        *   *Returns:* 
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
        *   *Description:* Handles 'from ... import ...' style import statements. It extracts the module name or attempts to resolve relative imports using _resolve_module_name. It adds the resolved modules to the dependency graph.
        *   *Parameters:* 
          - **self** 
          - **node** (ImportFrom): An AST node representing a 'from ... import ...' import statement.
        *   *Returns:* 

---
</details>

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API credentials, prompt file paths, and model configuration. It reads system prompts from specified files, configures batch settings based on the model name, and sets up appropriate LLM clients for function and class documentation generation. The initialization also validates the presence of required API keys and handles different model types by selecting the correct backend client.
    *   *Parameters:* 
      - **api_key** (str): API key for authenticating with the LLM provider.
      - **function_prompt_path** (str): Path to the file containing the system prompt for function documentation.
      - **class_prompt_path** (str): Path to the file containing the system prompt for class documentation.
      - **model_name** (str): Name of the language model to use, which determines the backend and batch size configuration.
      - **base_url** (str): Optional base URL for custom API endpoints, used when connecting to non-standard LLM services.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key: str, function_prompt_path: str, class_prompt_path: str, model_name: str = "gemini-2.0-flash-lite", base_url: str = None)`
        *   *Description:* Initializes the LLMHelper with API credentials, prompt file paths, and model configuration. It reads system prompts from specified files, configures batch settings based on the model name, and sets up appropriate LLM clients for function and class documentation generation. The initialization also validates the presence of required API keys and handles different model types by selecting the correct backend client.
        *   *Parameters:* 
          - **api_key** (str): API key for authenticating with the LLM provider.
          - **function_prompt_path** (str): Path to the file containing the system prompt for function documentation.
          - **class_prompt_path** (str): Path to the file containing the system prompt for class documentation.
          - **model_name** (str): Name of the language model to use, which determines the backend and batch size configuration.
          - **base_url** (str): Optional base URL for custom API endpoints, used when connecting to non-standard LLM services.
        *   *Returns:* 
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing requests based on the specified model name. It assigns different batch sizes depending on the capabilities and limitations of various models, ensuring efficient resource utilization and adherence to rate limits.
        *   *Parameters:* 
          - **self** 
          - **model_name** (str): The name of the language model for which to configure batch settings.
        *   *Returns:* 
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]`
        *   *Description:* Processes a batch of function inputs to generate validated documentation using the configured LLM. It divides the input into manageable batches, sends them to the LLM with appropriate system prompts, and handles errors gracefully by filling failed batches with None values while preserving order. Rate limiting is enforced between batches.
        *   *Parameters:* 
          - **self** 
          - **function_inputs** (List[FunctionAnalysisInput]): A list of function input models containing details about functions to document.
        *   *Returns:* 
          - **result** (List[Optional[FunctionAnalysis]]): A list of validated FunctionAnalysis objects or None for failed entries, maintaining the same order as the input.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]`
        *   *Description:* Processes a batch of class inputs to generate validated documentation using the configured LLM. Similar to generate_for_functions, it batches inputs, sends them to the LLM with appropriate system prompts, and handles errors by filling failed batches with None values while preserving order. Rate limiting is enforced between batches.
        *   *Parameters:* 
          - **self** 
          - **class_inputs** (List[ClassAnalysisInput]): A list of class input models containing details about classes to document.
        *   *Returns:* 
          - **result** (List[Optional[ClassAnalysis]]): A list of validated ClassAnalysis objects or None for failed entries, maintaining the same order as the input.

---
</details>

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading the system prompt from a file, and setting up the appropriate LLM client based on the model name. It supports multiple LLM backends such as Google Generative AI models, custom OpenAI-compatible APIs, and Ollama.
    *   *Parameters:* 
      - **api_key** (str): The API key used for authenticating with the LLM service.
      - **prompt_file_path** (str): The file path to the system prompt used for initializing the LLM.
      - **model_name** (str): The name of the model to use. Defaults to 'gemini-2.5-pro'.
      - **base_url** (str): Optional base URL for connecting to a custom LLM endpoint.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key: str, prompt_file_path: str, model_name: str = "gemini-2.5-pro", base_url: str = None)`
        *   *Description:* Initializes the MainLLM instance by validating the API key, loading the system prompt from a file, and setting up the appropriate LLM client based on the model name. It supports multiple LLM backends such as Google Generative AI models, custom OpenAI-compatible APIs, and Ollama.
        *   *Parameters:* 
          - **api_key** (str): The API key used for authenticating with the LLM service.
          - **prompt_file_path** (str): The file path to the system prompt used for initializing the LLM.
          - **model_name** (str): The name of the model to use. Defaults to 'gemini-2.5-pro'.
          - **base_url** (str): Optional base URL for connecting to a custom LLM endpoint.
        *   *Returns:* 
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* Sends a user input message to the configured LLM and returns the content of the response. It constructs a message sequence including the system prompt and the user input, invokes the LLM, and logs the process. In case of an exception, it logs the error and returns None.
        *   *Parameters:* 
          - **self** 
          - **user_input** (str): The input text provided by the user to be processed by the LLM.
        *   *Returns:* 
          - **response_content** (str): The content of the LLM's response, or None if an error occurs.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* Streams the response from the LLM in chunks as they become available. It constructs a message sequence including the system prompt and the user input, initiates a streaming request to the LLM, and yields each chunk of content. If an exception occurs, it logs the error and yields an error message.
        *   *Parameters:* 
          - **self** 
          - **user_input** (str): The input text provided by the user to be processed by the LLM.
        *   *Returns:* 
          - **chunk_content** (str): Yields content chunks from the LLM's response, or an error message if an exception occurs.

---
</details>

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str) -> str`
*   **Description:** 
    - overall: The function encrypts a given text string using a Fernet cipher suite. It first checks if the input text is empty or if the cipher suite is not initialized, returning the original text in such cases. If both conditions are met, it strips whitespace from the input text, encodes it to bytes, encrypts it, and then decodes the result back to a string.
*   **Parameters:**
    - **text** (str): The text string to be encrypted.
*   **Returns:**
    - **encrypted_text** (str): The encrypted version of the input text as a string.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str) -> str`
*   **Description:** 
    - overall: The function decrypts a given text using a cipher suite, returning the decrypted string if successful. If the input text is empty or the cipher suite is not available, it returns the original text. In case of decryption failure, it also returns the original text. The function handles potential exceptions during decryption gracefully.
*   **Parameters:**
    - **text** (str): The encrypted text to be decrypted.
*   **Returns:**
    - **result** (str): The decrypted text if successful; otherwise, the original input text.

---
</details>

### File: `frontend/Frontend.py`

#### Class: `Frontend`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* 
*   **Methods:**
    *   **`save_gemini_cb`**
        *   *Signature:* `def save_gemini_cb()`
        *   *Description:* Handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key associated with the user's username, clears the input field, and displays a success toast message. The function does not take any parameters and does not return any value.
        *   *Parameters:* 
          - **self** 
        *   *Returns:* 
    *   **`save_ollama_cb`**
        *   *Signature:* `def save_ollama_cb()`
        *   *Description:* Handles the callback for saving an Ollama URL entered by the user in the frontend. It retrieves the URL from the session state, updates the database with the new URL associated with the user's username, and displays a success toast message. The function does not take any parameters and does not return any value.
        *   *Parameters:* 
          - **self** 
        *   *Returns:* 
    *   **`load_data_from_db`**
        *   *Signature:* `def load_data_from_db(username: str)`
        *   *Description:* Lädt Chats und Exchanges konsistent aus der DB.
*   **Usage:** 

---
</details>

</details>
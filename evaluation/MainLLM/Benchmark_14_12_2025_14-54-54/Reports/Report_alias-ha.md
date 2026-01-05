# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
      - aktueller_status: Information not found
      - key_features: Information not found
      - tech_stack: Information not found

## 2. Installation 
### Dependencies
- aira~=4.2.2
- annotated-types~=0.7.0
- anyio~=4.11.0
- attrs~=25.4.0
- bcrypt~=5.0.0
- blinker~=1.9.0
- cachetools~=6.2.2
- captcha~=0.7.1
- certifi~=2025.11.12
- cffi~=2.0.0
- charset-normalizer~=3.4.4
- click~=8.3.1
- colorama~=0.4.6
- contourpy~=1.3.3
- cryptography~=46.0.3
- cycler~=0.12.1
- distro~=1.9.0
- dns-python~=2.8.0
- dotenv~=0.9.9
- entrypoints~=0.4
- extra-streamlit-components~=0.1.81
- filetype~=1.2.0
- fonttools~=4.61.0
- gitdb~=4.0.12
- GitPython~=3.1.45
- google-ai-generative-language~=0.9.0
- google-api-core~=2.28.1
- google-auth~=2.43.0
- googleapis-common-protos~=1.72.0
- grpcio~=1.76.0
- grpcio-status~=1.76.0
- h11~=0.16.0
- httpcore~=1.0.9
- httpx~=0.28.1
- idna~=3.11
- Jinja2~=3.1.6
- jiter~=0.12.0
- jsonpatch~=1.33.0
- jsonpointer~=3.0.0
- jsonschema~=4.25.1
- jsonschema-specifications~=2025.9.1
- kiwisolver~=1.4.9
- langchain~=1.0.8
- langchain-core~=1.1.0
- langchain-google~=3.1.0
- langchain-ollama~=1.0.0
- langchain-openai~=1.1.0
- langgraph~=1.0.3
- langgraph-checkpoint~=3.0.1
- langgraph-prebuilt~=1.0.5
- langsmit~=0.4.46
- MarkupSafe~=3.0.3
- matplotlib~=3.10.7
- numpy~=2.3.5
- ollama~=0.6.1
- openai~=2.8.1
- orjson~=3.11.4
- ormsgpack~=1.1.12.0
- packaging~=2.5.0
- pandas~=2.3.3
- pillow~=12.0.0
- proto-plus~=1.26.1
- protobuf~=6.33.1
- pyarrow~=2.1.0.0
- pyas1~=0.6.1
- pyasn1~=0.4.2
- pycparser~=2.23
- pydantic~=2.12.4
- pydantic-core~=2.41.5
- pydick~=0.9.1
- PyJWT~=2.10.1
- pymongo~=4.15.4
- pymongo[srv]~=4.15.4
- python-dateutil~=2.9.0.post0
- python-dotenv~=1.2.1
- pytz~=2025.2
- url3~=2.5.0
- watchdog~=6.0.0
- xxhash~=3.6.0
- zstandard~=0.25.0

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
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code: str, file_path: str, project_root: str)`
        *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It computes the module path based on the file and project root, initializes an empty schema dictionary to store collected information, and sets up a placeholder for tracking the current class during traversal.
        *   *Parameters:*
          - **source_code** (`str`): The full source code of the file being analyzed.
          - **file_path** (`str`): The absolute or relative path to the file being analyzed.
          - **project_root** (`str`): The root directory of the project to compute module paths.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It iterates over all aliases in the import statement and adds them to the schema before proceeding with generic visitation.
        *   *Parameters:*
          - **node** (`ast.Import`): An AST node representing an import statement.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* "Processes import-from nodes by collecting qualified names of imported items (e.g., module.submodule.Item). It appends these fully qualified names to the schema's imports list and continues traversal with generic_visit."
        *   *Parameters:*
          - **node** (`ast.ImportFrom`): An AST node representing an import-from statement.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* "Handles class definition nodes by creating a structured representation of the class, including its identifier, name, docstring, source code segment, and line numbers. It stores this information in the schema under the 'classes' key and tracks the current class being visited to support nested method processing."
        *   *Parameters:*
          - **node** (`ast.ClassDef`): An AST node representing a class definition.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* "Processes function definitions by determining whether the function belongs to a class or is a top-level function. For class methods, it creates a method context entry within the current class. For top-level functions, it creates a standalone function entry in the schema. It extracts function arguments, docstrings, and source code segments."
        *   *Parameters:*
          - **node** (`ast.FunctionDef`): An AST node representing a function definition.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating to the standard function definition handler. This allows async functions to be treated similarly to regular functions in terms of schema collection.
        *   *Parameters:*
          - **node** (`ast.AsyncFunctionDef`): An AST node representing an async function definition.

---
### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API key, function prompt path, class prompt path, and model name. It reads system prompts from specified files, configures batch size based on the model, and sets up appropriate LLM clients for function and class documentation generation.
    *   *Parameters:*
      - **api_key** (`str`): API key for accessing the language model service.
      - **function_prompt_path** (`str`): File path to the system prompt used for function documentation generation.
      - **class_prompt_path** (`str`): File path to the system prompt used for class documentation generation.
      - **model_name** (`str`): Name of the language model to use, defaults to 'gemini-2.0-flash-lite'.
      - **base_url** (`str`): Base URL for custom API endpoints, optional.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing requests based on the selected language model. Different models have different optimal batch sizes which are determined by their capabilities and limitations.
        *   *Parameters:*
          - **model_name** (`str`): Name of the language model for which to configure batch settings.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]`
        *   *Description:* "Processes a batch of function inputs to generate and validate documentation using the configured language model. It splits inputs into batches, sends them to the LLM, and handles errors by filling missing results with None while maintaining order."
        *   *Parameters:*
          - **function_inputs** (`List[FunctionAnalysisInput]`): A list of function inputs to process for documentation generation.
        *   *Returns:*
          - **result** (`List[Optional[FunctionAnalysis]]`): A list of validated function analysis outputs or None for failed items.

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading a system prompt from a specified file, and configuring the underlying LLM client based on the model name. It supports different LLM backends such as Google Generative AI, custom OpenAI-compatible APIs, and Ollama-based models.
    *   *Parameters:*
      - **api_key** (`str`): The API key used for authenticating with the LLM provider.
      - **prompt_file_path** (`str`): The file path to the system prompt used for initializing the LLM.
      - **model_name** (`str`): The name of the model to use. Determines which backend (Google, OpenAI, Ollama) is selected.
      - **base_url** (`str`): Optional base URL for custom LLM endpoints. Defaults to None.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* "Synchronously invokes the configured LLM with a user input message. It constructs a conversation history using the system prompt and the user input, sends it to the LLM, and returns the content of the response. If an error occurs during the call, it logs the error and returns None."
        *   *Parameters:*
          - **user_input** (`str`): The input text provided by the user to be processed by the LLM.
        *   *Returns:*
          - **response_content** (`str`): The content of the LLM's response, or None if an error occurred.

---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str) -> str`
*   **Description:** The function encrypts a given text string using a Fernet cipher suite. It first checks if the input text is empty or if the cipher suite is not initialized, returning the original text in such cases. If both conditions are met, it proceeds to strip whitespace from the input text, encode it to bytes, encrypt it using the cipher suite, and then decode the result back to a string for return.
*   **Parameters:**
  - **text** (`str`): The text string to be encrypted.
*   **Returns:**
  - **encrypted_text** (`str`): The encrypted version of the input text as a string.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str) -> str`
*   **Description:** The function decrypts a given text using a cipher suite if available; otherwise, it returns the text unchanged. It handles potential decryption errors gracefully by returning the original text in case of exceptions. The function ensures that the input text is stripped of leading/trailing whitespace before attempting decryption.
*   **Parameters:**
  - **text** (`str`): The encrypted text to be decrypted.
*   **Returns:**
  - **result** (`str`): The decrypted text if successful, otherwise the original input text.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** The function inserts a new user into the database by creating a user document with the provided username, name, and password. It hashes the password using a hasher utility before storing the user data. The function then stores the user document in the 'dbusers' collection and returns the ID of the inserted document.
*   **Parameters:**
  - **username** (`str`): The unique identifier for the user, used as the '_id' field in the database.
  - **name** (`str`): The full name of the user to be stored in the database.
  - **password** (`str`): The plain text password of the user, which gets hashed before storage.
*   **Returns:**
  - **inserted_id** (`ObjectId`): The unique identifier of the newly inserted user document in the database.

---
</SystemPrompt>
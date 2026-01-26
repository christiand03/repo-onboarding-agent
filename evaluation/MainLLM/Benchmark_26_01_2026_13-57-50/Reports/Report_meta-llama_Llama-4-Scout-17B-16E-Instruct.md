# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
    - **Description:** The Repo Onboarding Agent is a tool designed to streamline the process of onboarding repositories. It appears to be built with a focus on automation, utilizing technologies such as Streamlit for the frontend, and a complex backend involving various Python libraries and tools for analysis and interaction with Git repositories.
    - **Key Features:**
      - Repository cloning and analysis
      - Automated documentation generation
      - Support for multiple LLM (Large Language Models) providers
      - Integration with databases for storing user and chat data
    - **Tech Stack:**
      - Python as the primary programming language
      - Streamlit for frontend
      - LangChain and LangSmith for LLM interactions
      - Pydantic for data validation
      - GitPython for Git repository interactions

## 2. Installation
### Dependencies
The project depends on a wide range of libraries, including but not limited to:
- altair
- annotated-types
- anyio
- attrs
- bcrypt
- blinker
- cachetools
- captcha
- certifi
- cffi
- charset-normalizer
- click
- colorama
- contourpy
- cryptography
- cycler
- distro
- dnspython
- dotenv
- entrypoints
- extra-streamlit-components
- filetype
- fonttools
- gitdb
- GitPython
- google-ai-generativelanguage
- google-api-core
- google-auth
- googleapis-common-protos
- grpcio
- grpcio-status
- h11
- httpcore
- httpx
- idna
- Jinja2
- jiter
- jsonpatch
- jsonpointer
- jsonschema
- jsonschema-specifications
- kiwisolver
- langchain
- langchain-core
- langchain-google-genai
- langchain-ollama
- langchain-openai
- langgraph
- langgraph-checkpoint
- langgraph-prebuilt
- langgraph-sdk
- langsmith
- MarkupSafe
- matplotlib
- narwhals
- networkx
- numpy
- ollama
- openai
- orjson
- ormsgpack
- packaging
- pandas
- pillow
- proto-plus
- protobuf
- pyarrow
- pyasn1
- pyasn1_modules
- pycparser
- pydantic
- pydantic_core
- pydeck
- PyJWT
- pymongo
- pyparsing
- python-dateutil
- python-dotenv
- pytz
- PyYAML
- referencing
- regex
- requests
- requests-toolbelt
- rpds-py
- rsa
- setuptools
- six
- smmap
- sniffio
- streamlit
- streamlit-authenticator
- streamlit-mermaid
- tenacity
- tiktoken
- toml
- toolz
- toon_format
- tornado
- tqdm
- typing-inspection
- typing_extensions
- tzdata
- urllib3
- watchdog
- xxhash
- zstandard
- nbformat

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

### Setup Guide
The setup guide is not explicitly provided in the given information. However, the general steps would involve cloning the repository, setting up a virtual environment, and installing the dependencies.

### Quick Startup
The quick startup guide is also not provided. However, assuming the project is properly set up, you can likely run the application using Streamlit:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The project seems to be designed for automating repository onboarding processes, which may involve analyzing repositories, generating documentation, and interacting with users through a chat interface.

## 4. Architecture
No specific Mermaid syntax is provided for the architecture.

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** A class used to traverse the Abstract Syntax Tree (AST) of Python source code to extract and structure metadata about imports, classes, and functions.
*   **Instantiation:** The class is instantiated during the analysis of Python files within a repository.
*   **Dependencies:** The class depends on `path_to_module` for resolving module paths.
*   **Constructor:**
    *   **Description:** Initializes the ASTVisitor with source code, file path, and project root to calculate module paths and set up an empty schema.
    *   **Parameters:** `self`, `source_code`, `file_path`, `project_root`
*   **Methods:**
    *   `visit_Import`
        *   **Signature:** `visit_Import(self, node)`
        *   **Description:** Processes import statements to populate the import list in the schema.
        *   **Parameters:** `self`, `node` (ast.Import)
    *   `visit_ImportFrom`
        *   **Signature:** `visit_ImportFrom(self, node)`
        *   **Description:** Handles 'from ... import ...' statements to capture specific imports.
        *   **Parameters:** `self`, `node` (ast.ImportFrom)
    *   `visit_ClassDef`
        *   **Signature:** `visit_ClassDef(self, node)`
        *   **Description:** Extracts class definitions and their docstrings.
        *   **Parameters:** `self`, `node` (ast.ClassDef)
    *   `visit_FunctionDef`
        *   **Signature:** `visit_FunctionDef(self, node)`
        *   **Description:** Processes function definitions, distinguishing between methods and standalone functions.
        *   **Parameters:** `self`, `node` (ast.FunctionDef)

### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** A class for building a graph of file-level import dependencies within a repository.
*   **Instantiation:** Instantiated during dependency analysis.
*   **Dependencies:** Depends on `get_all_temp_files` for file discovery.
*   **Constructor:**
    *   **Description:** Initializes the graph with a filename and repository root.
    *   **Parameters:** `self`, `filename`, `repo_root`
*   **Methods:**
    *   `_resolve_module_name`
        *   **Signature:** `_resolve_module_name(self, node)`
        *   **Description:** Resolves relative import statements.
        *   **Parameters:** `self`, `node` (ImportFrom)
    *   `visit_Import`
        *   **Signature:** `visit_Import(self, node, base_name=None)`
        *   **Description:** Records imported modules.
        *   **Parameters:** `self`, `node`, `base_name`

### File: `backend/HelperLLM.py`
#### Function: `main_orchestrator`
*   **Signature:** `main_orchestrator()`
*   **Description:** A dummy function for testing LLMHelper, demonstrating how to generate documentation for example functions.
*   **Parameters:** None
*   **Returns:** None

#### Class: `LLMHelper`
*   **Summary:** A class for interacting with Google Gemini to generate documentation for code snippets.
*   **Instantiation:** Used in the main workflow for generating documentation.
*   **Dependencies:** Depends on `function_prompt_path` and `class_prompt_path`.
*   **Constructor:**
    *   **Description:** Initializes the LLMHelper with API key, prompt paths, and model name.
    *   **Parameters:** `self`, `api_key`, `function_prompt_path`, `class_prompt_path`, `model_name`, `base_url`
*   **Methods:**
    *   `generate_for_functions`
        *   **Signature:** `generate_for_functions(self, function_inputs)`
        *   **Description:** Generates documentation for functions.
        *   **Parameters:** `self`, `function_inputs`
    *   `generate_for_classes`
        *   **Signature:** `generate_for_classes(self, class_inputs)`
        *   **Description:** Generates documentation for classes.
        *   **Parameters:** `self`, `class_inputs`

### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** A class for interacting with LLMs to generate the final report.
*   **Instantiation:** Used in the main workflow for synthesizing the final documentation report.
*   **Dependencies:** Depends on `prompt_file_path` and `model_name`.
*   **Constructor:**
    *   **Description:** Initializes the MainLLM with API key, prompt file path, and model name.
    *   **Parameters:** `self`, `api_key`, `prompt_file_path`, `model_name`, `base_url`
*   **Methods:**
    *   `call_llm`
        *   **Signature:** `call_llm(self, user_input)`
        *   **Description:** Calls the LLM to generate a response.
        *   **Parameters:** `self`, `user_input`

---
</end_of_documentation>
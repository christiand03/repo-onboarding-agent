# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
    - **Description:** The_REPO_Onboarding_Agent is designed to streamline the onboarding process for new repositories. It appears to be a tool that automates various tasks related to repository setup and management, potentially including code analysis, documentation generation, and integration with services like Streamlit for visualization.
    - **Key Features:**
      - Automated repository onboarding
      - Code analysis and documentation generation
      - Integration with Streamlit for UI visualization
      - Support for multiple LLM (Large Language Models) providers
    - **Tech Stack:**
      - Python
      - Streamlit
      - LangChain
      - Google Gemini API
      - MongoDB

## 2. Installation
### Dependencies
The project depends on a wide range of libraries and tools, including but not limited to:
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

If a `requirements.txt` file is present, you can install the dependencies using:
```bash
pip install -r requirements.txt
```

### Setup Guide
The setup guide is not explicitly provided, but it generally involves cloning the repository, setting up a virtual environment, and installing the dependencies.

### Quick Startup
To quickly start the project, you would typically run:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The_REPO_Onboarding_Agent seems to support various use cases, including:
- Automated code analysis and documentation generation
- Integration with Streamlit for visualizing repository data
- Support for multiple LLM providers for generating documentation and analyzing code

Primary commands or workflows might include:
- Running the Streamlit frontend
- Cloning a repository and analyzing its contents
- Generating documentation for a repository

## 4. Architecture
The architecture of the_REPO_Onboarding_Agent involves several components, including:
- A frontend built with Streamlit for user interaction and visualization
- A backend that handles repository cloning, code analysis, and documentation generation
- Integration with various LLM providers for code analysis and documentation

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** This class is designed to traverse the Abstract Syntax Tree (AST) of Python source code and extract metadata about imports, classes, and functions.
*   **Instantiation:** The class is instantiated with source code, file path, and project root.
*   **Dependencies:** The class depends on the `ast` module for parsing Python code and utilizes various data structures for storing metadata.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root.
    *   *Parameters:* `self`, `source_code`, `file_path`, `project_root`
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code: str, file_path: str, project_root: str)`
        *   *Description:* The constructor initializes the ASTVisitor.
        *   *Parameters:*
          - **source_code** (`str`): The raw source code of the file being analyzed.
          - **file_path** (`str`): The absolute path to the Python file being visited.
          - **project_root** (`str`): The root directory of the project, used to determine the module path.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Processes `ast.Import` nodes to extract import statements.
        *   *Parameters:* `self`, `node`
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles `ast.ImportFrom` nodes for extracting imports from specific modules.
        *   *Parameters:* `self`, `node`
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Processes `ast.ClassDef` nodes to extract class definitions.
        *   *Parameters:* `self`, `node`
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Extracts function definitions and distinguishes between methods and standalone functions.
        *   *Parameters:* `self`, `node`
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating to `visit_FunctionDef`.
        *   *Parameters:* `self`, `node`

### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** This class is used to build a graph representing import dependencies between Python files in a repository.
*   **Instantiation:** The class is instantiated with a filename and a repository root.
*   **Dependencies:** The class depends on `ast` for parsing Python code and `networkx` for creating and manipulating the dependency graph.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and a repository root.
    *   *Parameters:* `self`, `filename`, `repo_root`
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename: str, repo_root)`
        *   *Description:* The constructor initializes the FileDependencyGraph.
        *   *Parameters:*
          - **filename** (`str`): The name of the file being analyzed for dependencies.
          - **repo_root** (`str`): The root directory of the repository, used for resolving file paths.
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* Resolves relative import statements to their actual module names.
        *   *Parameters:* `self`, `node`
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name=None)`
        *   *Description:* Records import statements as dependencies in the graph.
        *   *Parameters:*
          - **node**: The AST node representing an import statement.
          - **base_name** (`str | None`): An optional base name for the module.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles `from ... import ...` statements to update the dependency graph.
        *   *Parameters:* `self`, `node`

### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** This class provides a centralized interface for interacting with various Large Language Models (LLMs) to generate structured documentation for Python functions and classes.
*   **Instantiation:** The class is instantiated with an API key, function and class prompt paths, and optionally a model name and base URL.
*   **Dependencies:** The class supports multiple LLM providers, including Google Gemini, OpenAI, and Ollama.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API key, prompt paths, and model settings.
    *   *Parameters:*
      - **api_key** (`str`): The API key for authenticating with the chosen LLM service.
      - **function_prompt_path** (`str`): The file path to the system prompt used for function analysis.
      - **class_prompt_path** (`str`): The file path to the system prompt used for class analysis.
      - **model_name** (`str`): The name of the LLM model to use.
      - **base_url** (`str`): An optional base URL for custom LLM endpoints.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key: str, function_prompt_path: str, class_prompt_path: str, model_name: str = "gemini-2.0-flash-lite", base_url: str = None)`
        *   *Description:* The constructor initializes the LLMHelper.
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures batch processing settings based on the model name.
        *   *Parameters:* `self`, `model_name`
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]`
        *   *Description:* Generates structured documentation for a batch of functions using the configured LLM.
        *   *Parameters:* `self`, `function_inputs`
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]`
        *   *Description:* Generates structured documentation for a batch of classes using the configured LLM.
        *   *Parameters:* `self`, `class_inputs`

---
</end_of_documentation>
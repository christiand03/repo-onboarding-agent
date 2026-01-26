# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** An automated repository analysis and documentation tool that leverages Large Language Models (LLMs) to generate comprehensive technical insights. It parses Python projects using Abstract Syntax Trees (AST), analyzes internal relationships (calls and instantiations), and creates human-readable documentation.
- **Key Features:** 
  - Automated AST-based code parsing and metadata extraction.
  - Multi-LLM support (Gemini, OpenAI, Ollama) for documentation generation.
  - Internal relationship mapping and call graph visualization.
  - Jupyter Notebook analysis with multimodal support (text and images).
  - Token-efficient data serialization using the TOON format.
- **Tech Stack:** Python, Streamlit, LangChain, Pydantic, NetworkX, MongoDB, GitPython, Matplotlib.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root --> backend_node[backend/<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py<br/>__init__.py]
    root --> database_node[database/<br/>db.py]
    root --> frontend_node[frontend/<br/>frontend.py<br/>__init__.py]
    root --> schemas_node[schemas/<br/>types.py]
    root --> prompts_node[SystemPrompts/<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>...]
    ```

## 2. Installation
### Dependencies
- altair, anyio, attrs, bcrypt, blinker, cachetools, captcha, certifi, cffi, charset-normalizer, click, colorama, contourpy, cryptography, cycler, distro, dnspython, dotenv, entrypoints, extra-streamlit-components, filetype, fonttools, gitdb, GitPython, google-ai-generativelanguage, google-api-core, google-auth, googleapis-common-protos, grpcio, grpcio-status, h11, httpcore, httpx, idna, Jinja2, jiter, jsonpatch, jsonpointer, jsonschema, jsonschema-specifications, kiwisolver, langchain, langchain-core, langchain-google-genai, langchain-ollama, langchain-openai, langgraph, langgraph-checkpoint, langgraph-prebuilt, langgraph-sdk, langsmith, MarkupSafe, matplotlib, narwhals, networkx, numpy, ollama, openai, orjson, ormsgpack, packaging, pandas, pillow, proto-plus, protobuf, pyarrow, pyasn1, pyasn1_modules, pycparser, pydantic, pydantic_core, pydeck, PyJWT, pymongo, pyparsing, python-dateutil, python-dotenv, pytz, PyYAML, referencing, regex, requests, requests-toolbelt, rpds-py, rsa, setuptools, six, smmap, sniffio, streamlit, streamlit-authenticator, streamlit-mermaid, tenacity, tiktoken, toml, toolz, toon_format, tornado, tqdm, typing-inspection, typing_extensions, tzdata, urllib3, watchdog, xxhash, zstandard, nbformat.

pip install -r requirements.txt

### Setup Guide
1. Clone the repository.
2. Create a `.env` file based on `.env.example`.
3. Provide your API keys (e.g., `GEMINI_API_KEY`) and MongoDB credentials.
4. Ensure a local MongoDB instance is running if required by `database/db.py`.

### Quick Startup
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
- **Automated Documentation:** Point the tool at a GitHub URL to generate a full Markdown report of the codebase.
- **Codebase Onboarding:** Quickly understand the structure and dependencies of a new project.
- **Relationship Analysis:** Visualize call graphs and class dependencies to identify bottlenecks or architecture patterns.

**Primary Commands:**
- `streamlit run frontend/frontend.py`: Launches the interactive dashboard.

## 4. Architecture
The system follows a modular architecture:
- **Frontend:** Streamlit-based UI for user interaction and report viewing.
- **Backend:** Orchestrates cloning, AST parsing, relationship analysis, and LLM communication.
- **Database:** MongoDB stores user sessions, API keys, and chat history.
- **Schemas:** Pydantic models define the data contract between Helper LLMs and the Main LLM.

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file system path into a Python module path string. It first attempts to determine the relative path from a specified project root, falling back to the basename if a ValueError occurs. It then removes the '.py' extension if present, replaces system path separators with dots, and finally removes the '.__init__' suffix if the resulting module path represents an initialization file.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file to be converted.
    - **project_root** (`str`): The root directory of the project, used as a base to calculate the relative module path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string, e.g., 'my_package.my_module'.
*   **Usage:** This function calls no other functions.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends ast.NodeVisitor to traverse an Abstract Syntax Tree (AST) of Python source code. Its primary purpose is to extract structured information about imports, functions, and classes defined within a given source file, storing this data in a 'schema' dictionary.
*   **Instantiation:** This class is not explicitly listed as being instantiated by any other components in its context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its context.
*   **Constructor:**
    *   *Description:* The __init__ method initializes an ASTVisitor instance by storing the provided source code, file path, and project root. It calculates the module path using an external utility function and sets up an empty schema dictionary.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file.
        - **file_path** (`str`): The absolute path to the file.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* Processes 'ast.Import' nodes and appends module names to the 'imports' list in the schema.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* Handles 'ast.ImportFrom' nodes, constructing fully qualified import names.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* Processes class definitions, extracting identifiers, docstrings, and source segments.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: ast.FunctionDef)`
        *   *Description:* Handles function definitions, distinguishing between class methods and top-level functions.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef)`
        *   *Description:* Delegates async function processing to `visit_FunctionDef`.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for analyzing Python source code to construct a detailed Abstract Syntax Tree (AST) schema of a repository.
*   **Instantiation:** Not explicitly instantiated in context.
*   **Dependencies:** None listed.
*   **Constructor:**
    *   *Description:* Initializes the ASTAnalyzer class with no initial state.
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(full_schema: dict, raw_relationships: dict)`
        *   *Description:* Integrates raw relationship data (incoming/outgoing calls) into a structured AST schema.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(files: list, repo: GitRepository)`
        *   *Description:* Processes file objects from a repository to build a comprehensive AST schema.

---

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Python file's AST.
*   **Parameters:**
    - **filename** (`str`): The path to the Python file being analyzed.
    - **tree** (`AST`): The AST of the Python file.
    - **repo_root** (`str`): The root directory of the repository.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** Constructs a directed graph representing dependencies between Python files across an entire Git repository.
*   **Parameters:**
    - **repository** (`GitRepository`): The object representing the repository to analyze.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): An aggregated NetworkX directed graph.

#### Class: `FileDependencyGraph`
*   **Summary:** Extends ast.NodeVisitor to construct a graph of import dependencies for a given Python file.
*   **Constructor:**
    *   *Description:* Initializes with filename and repo_root.
    *   *Parameters:*
        - **filename** (`str`): Path to the file.
        - **repo_root** (`str`): Root of the repo.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(node: ImportFrom)`
        *   *Description:* Resolves relative imports by checking for module existence and symbols in `__init__.py`.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* Records dependencies in the `import_dependencies` dictionary.

---

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** Serves as a robust interface for interacting with various LLMs (Gemini, OpenAI, Ollama) to generate structured documentation for code snippets.
*   **Constructor:**
    *   *Description:* Initializes API keys, loads prompts, and configures the LangChain chat model.
    *   *Parameters:*
        - **api_key** (`str`): Auth key.
        - **function_prompt_path** (`str`): Path to function prompt.
        - **class_prompt_path** (`str`): Path to class prompt.
        - **model_name** (`str`): Identifier for the model.
*   **Methods:**
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* Orchestrates the generation and validation of documentation for a batch of functions.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(class_inputs: List[ClassAnalysisInput])`
        *   *Description:* Facilitates generation and validation of documentation for a batch of classes.

---

### File: `backend/main.py`

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** Orchestrates the primary analysis pipeline: cloning, info extraction, AST generation, relationship analysis, and LLM report generation.
*   **Parameters:**
    - **input** (`str`): User input (Repo URL).
    - **api_keys** (`dict`): API keys for LLMs.
    - **model_names** (`dict`): Configured model names.
    - **status_callback** (`Callable`): Optional UI feedback function.
*   **Returns:**
    - **report** (`str`): Final report content.
    - **metrics** (`dict`): Performance data.

---

### File: `database/db.py`

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** Inserts a new user record into the database with hashed passwords and empty API key placeholders.
*   **Parameters:**
    - **username** (`str`): Unique identifier.
    - **name** (`str`): User's full name.
    - **password** (`str`): Plain-text password (hashed before storage).

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** Retrieves and decrypts a user's API keys (Gemini, GPT, etc.) from the database.

---

### File: `schemas/types.py`

#### Class: `FunctionAnalysis`
*   **Summary:** The main model representing the entire JSON schema for a function analysis result.
*   **Constructor:**
    *   *Parameters:*
        - **identifier** (`str`): Unique ID.
        - **description** (`FunctionDescription`): Detailed analysis.
        - **error** (`Optional[str]`): Error details.

#### Class: `ClassAnalysis`
*   **Summary:** The main model for representing a comprehensive analysis of a Python class.
*   **Constructor:**
    *   *Parameters:*
        - **identifier** (`str`): Unique ID.
        - **description** (`ClassDescription`): Analytical components.
        - **error** (`Optional[str]`): Error details.

---
*End of Documentation.*
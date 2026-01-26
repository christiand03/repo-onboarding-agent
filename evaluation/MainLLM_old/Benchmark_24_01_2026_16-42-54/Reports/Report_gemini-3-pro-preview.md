# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** A comprehensive automated documentation tool that analyzes Git repositories. It uses a multi-stage LLM pipeline (Helper and Main LLMs) to generate detailed documentation for classes and functions, visualizes dependency graphs, and presents the results via a Streamlit interface.
- **Key Features:**
  - **Automated Code Analysis:** Parses Python code using AST to extract structure.
  - **Dual-LLM Pipeline:** Uses specialized Helper LLMs for component analysis and a Main LLM for final synthesis.
  - **Visualizations:** Generates call graphs and dependency graphs using NetworkX and Mermaid.
  - **Interactive Frontend:** Streamlit-based UI for users to input URLs and view/manage reports.
  - **Notebook Support:** Converts and analyzes Jupyter Notebooks.
- **Tech Stack:** Python, Streamlit, LangChain, GitPython, NetworkX, MongoDB, Pydantic, Altair, Matplotlib.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root[root] --> backend
    root --> database
    root --> frontend
    root --> notizen
    root --> schemas
    root --> systemprompts[SystemPrompts]
    root --> root_files[.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json]
    backend --> backend_files[AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
    database --> database_files[db.py]
    frontend --> frontend_files[frontend.py]
    frontend --> frontend_streamlit[.streamlit/config.toml]
    notizen --> notizen_files[Report Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md]
    schemas --> schemas_files[types.py]
    systemprompts --> prompt_files[SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptNotebookLLM.txt]
    ```

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
- dnspython==2.8.0
- dotenv==0.9.9
- entrypoints==0.4
- extra-streamlit-components==0.1.81
- filetype==1.2.0
- fonttools==4.61.0
- gitdb==4.0.12
- GitPython==3.1.45
- google-ai-generativelanguage==0.9.0
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
- jsonpatch==1.33
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
- langgraph-sdk==0.2.9
- langsmith==0.4.46
- MarkupSafe==3.0.3
- matplotlib==3.10.7
- narwhals==2.12.0
- networkx==3.6
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
- pyarrow==21.0.0
- pyasn1==0.6.1
- pyasn1_modules==0.4.2
- pycparser==2.23
- pydantic==2.12.4
- pydantic_core==2.41.5
- pydeck==0.9.1
- PyJWT==2.10.1
- pymongo==4.15.4
- pyparsing==3.2.5
- python-dateutil==2.9.0.post0
- python-dotenv==1.2.1
- pytz==2025.2
- PyYAML==6.0.3
- referencing==0.37.0
- regex==2025.11.3
- requests==2.32.5
- requests-toolbelt==1.0.0
- rpds-py==0.29.0
- rsa==4.9.1
- setuptools==75.9.1
- six==1.17.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.51.0
- streamlit-authenticator==0.4.2
- streamlit-mermaid==0.3.0
- tenacity==9.1.2
- tiktoken==0.12.0
- toml==0.10.2
- toolz==1.1.0
- toon_format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c9006de6
- tornado==6.5.2
- tqdm==4.67.1
- typing-inspection==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0
- nbformat

Note: `pip install -r requirements.txt`

### Setup Guide
1.  Clone the repository.
2.  Install dependencies using `pip install -r requirements.txt`.
3.  Set up environment variables in a `.env` file (see `.env.example`).
4.  Ensure MongoDB is running (as indicated by `database/db.py`).

### Quick Startup
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
**Primary Use Cases:**
1.  **Repository Onboarding:** Developers can input a GitHub URL to quickly generate a comprehensive documentation report, allowing them to understand the codebase structure and functionality without reading every file.
2.  **Documentation Generation:** Automated creation of Markdown documentation for existing projects, including class/function references and dependency graphs.
3.  **Code Analysis:** Visualizing project architecture through call graphs and file dependency diagrams to identify coupling and structural issues.
4.  **Notebook Conversion:** Analyzing and converting Jupyter Notebooks into XML/Markdown reports for easier review.

**Primary Commands:**
*   Start the application: `streamlit run frontend/frontend.py`

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends ast.NodeVisitor, providing a mechanism to traverse the Abstract Syntax Tree (AST) of Python source code to extract structured information. It is initialized with the source code, file path, and project root, and constructs a schema dictionary to store details about imports, functions, and classes encountered during traversal. The overridden visit methods systematically populate this schema, creating a machine-readable representation of the code's structural components.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class ASTVisitor depends on the `ast` module for AST traversal and node manipulation, and implicitly on `path_to_module` for path resolution.
*   **Constructor:**
    *   *Description:* The __init__ method initializes an ASTVisitor instance by storing the provided source code, file path, and project root. It calculates the module's full path and sets up an empty schema dictionary to accumulate discovered imports, functions, and classes. It also initializes a _current_class attribute to track the class context during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the file being analyzed.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method is designed to process `ast.Import` nodes, which represent top-level import statements. It iterates through each alias within the import node and appends the name of the imported module or object to the `imports` list within the `self.schema` dictionary. After processing the current node's imports, it calls `self.generic_visit(node)` to ensure continued traversal of the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement (e.g., `import os`).
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls self.generic_visit to continue AST traversal.
            *   *Called By:* This method is called by the ast.NodeVisitor framework when an ast.Import node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method processes `ast.ImportFrom` nodes, which correspond to `from ... import ...` statements. It iterates over the aliases (names) being imported and constructs a fully qualified import string, combining the module name with the imported alias. This fully qualified name is then added to the `imports` list in `self.schema`, and `self.generic_visit(node)` is called to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls self.generic_visit to continue AST traversal.
            *   *Called By:* This method is called by the ast.NodeVisitor framework when an ast.ImportFrom node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method handles `ast.ClassDef` nodes, representing class definitions in the source code. It constructs a unique identifier for the class, extracts its name, docstring, and the source code segment. A `class_info` dictionary is created with these details and appended to the `classes` list in `self.schema`. The `_current_class` attribute is temporarily set to this `class_info` to correctly associate nested methods, then `self.generic_visit(node)` is called for further traversal, and finally `_current_class` is reset.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls ast.get_docstring and ast.get_source_segment to extract class details, and self.generic_visit for AST traversal.
            *   *Called By:* This method is called by the ast.NodeVisitor framework when an ast.ClassDef node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, distinguishing between methods defined within a class and standalone functions. If a `_current_class` is active, it extracts method-specific details (identifier, name, arguments, docstring, line numbers) and appends them to the `method_context` of the current class. Otherwise, it extracts similar details for a standalone function and adds them to the `functions` list in `self.schema`. It then calls `self.generic_visit` to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls ast.get_docstring and ast.get_source_segment to extract function details, and self.generic_visit for AST traversal.
            *   *Called By:* This method is called by the ast.NodeVisitor framework when an ast.FunctionDef node is encountered during AST traversal.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is responsible for handling `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation directly delegates the processing of these nodes to the `visit_FunctionDef` method. This approach ensures that asynchronous functions are analyzed and recorded in the schema in the same manner as regular functions, simplifying the overall logic.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls self.visit_FunctionDef to process the async function node.
            *   *Called By:* This method is called by the ast.NodeVisitor framework when an ast.AsyncFunctionDef node is encountered during AST traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process and analyze Python source code within a repository to build a structured Abstract Syntax Tree (AST) schema. It provides functionalities to parse individual Python files, extract their structural components (imports, functions, classes), and then integrate relationship data such as function calls and class instantiations into this schema. This class serves as a core component for understanding the architectural layout and interdependencies within a Python codebase.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class depends on the 'ast' module for parsing Python code, the 'os' module for path manipulation, 'getRepo.GitRepository' for repository interaction, and 'ASTVisitor' for AST traversal.
*   **Constructor:**
    *   *Description:* The constructor for the ASTAnalyzer class. It takes no specific parameters beyond 'self' and performs no initialization logic, effectively creating an empty instance.
    *   *Parameters:*
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing calls, into a pre-existing full AST schema. It iterates through files, functions, and classes within the schema, updating their respective 'context' fields with call information. For classes, it also identifies and lists external dependencies based on method calls that are not internal to the class, providing a comprehensive view of inter-component relationships.
        *   *Parameters:*
            - **full_schema** (`dict`): The comprehensive AST schema containing file, function, and class definitions to be updated.
            - **raw_relationships** (`dict`): A dictionary containing raw 'outgoing' and 'incoming' call relationships to be merged.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full AST schema with integrated relationship data.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other methods, classes, or functions within its source code, focusing on data manipulation.
            *   *Called By:* This method is not explicitly called by other functions or methods in the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to construct a full AST schema. It filters for Python files, parses their content using the 'ast' module, and then uses an 'ASTVisitor' to extract AST nodes. The extracted schema nodes (imports, functions, classes) are then organized into a 'full_schema' dictionary, handling potential parsing errors and providing a structured representation of the repository's code.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes for analysis.
            - **repo** (`GitRepository`): An object representing the Git repository, though it's not directly used in the provided method body for analysis.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed repository, structured by file paths.
        *   **Usage:**
            *   *Calls:* This method calls 'os.path.commonpath', 'os.path.isfile', 'os.path.dirname', 'ast.parse', 'ASTVisitor' (instantiation), 'visitor.visit', and 'print'.
            *   *Called By:* This method is not explicitly called by other functions or methods in the provided context.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into a Python module path string. It first determines the relative path of the file with respect to a specified project root, handling potential `ValueError` by falling back to the base filename. It then removes the `.py` extension if present, replaces operating system path separators with dots, and specifically truncates the `.__init__` suffix to correctly represent package modules. The function ensures the output is a valid Python module identifier.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file to be converted.
    - **project_root** (`str`): The root directory of the project, used as a base to calculate the relative module path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string, e.g., 'my_package.my_module'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class, inheriting from ast.NodeVisitor, is designed to analyze Python source code files and build a graph of their import dependencies. It traverses the Abstract Syntax Tree (AST) of a given file, identifying both absolute and relative import statements. The class includes sophisticated logic to resolve relative imports to their actual module or symbol names within a specified repository structure, recording these relationships in an internal dictionary.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class depends on `ast` module components such as `NodeVisitor`, `Import`, `ImportFrom`, `Assign`, `Name`, `FunctionDef`, `ClassDef`, `literal_eval`, `parse`, and `walk`. It also relies on `keyword.iskeyword` and `pathlib.Path` for path and keyword checks, and an external function `get_all_temp_files`.
*   **Constructor:**
    *   *Description:* The constructor initializes a new instance of the FileDependencyGraph. It takes the target filename and the repository's root path as arguments, storing them as instance attributes to be used during the dependency analysis process.
    *   *Parameters:*
        - **filename** (`str`): The path or name of the Python file for which dependencies are to be analyzed.
        - **repo_root** (`Any`): The root directory of the repository, used for resolving file paths and imports.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ImportFrom)`
        *   *Description:* This method is responsible for resolving relative import statements, such as 'from .. import name1, name2', into their concrete, existing module or symbol names. It determines the current file's path, navigates up the directory tree based on the import level, and then verifies if the imported names correspond to actual Python files, packages (via __init__.py), or symbols exported by __init__.py files. If no valid resolution is found, it raises an ImportError.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of strings, where each string is a resolved module or symbol name.
        *   **Usage:**
            *   *Calls:* This method calls `get_all_temp_files` to retrieve all files in the repository, utilizes `pathlib.Path` for path manipulation, and employs `ast.parse`, `ast.walk`, `ast.literal_eval`, and `keyword.iskeyword` for AST parsing and symbol resolution. It also internally calls the helper functions `module_file_exists` and `init_exports_symbol`.
            *   *Called By:* This method is called by `visit_ImportFrom` to handle the resolution of relative import statements.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* This method is a visitor handler for `Import` and `ImportFrom` AST nodes. Its primary function is to record the identified module or symbol as a dependency for the current file (`self.filename`) within the `import_dependencies` dictionary. It uses an optional `base_name` if provided, otherwise it defaults to the alias name from the import node.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing either an 'import' or 'from ... import ...' statement.
            - **base_name** (`str | None`): An optional base name for the import, typically used to specify the module part of a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self.generic_visit` to continue the AST traversal.
            *   *Called By:* This method is called by `visit_ImportFrom` and by the `NodeVisitor` framework during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method serves as the AST `NodeVisitor` handler specifically for `ImportFrom` nodes, which represent 'from ... import ...' statements. It first checks if the import is absolute (has a `module_name`); if so, it extracts the last part of the module name and delegates to `visit_Import`. For relative imports (where `module_name` is absent), it attempts to resolve the actual module names using `_resolve_module_name` and then calls `visit_Import` for each resolved base name. It also includes error handling for failed relative import resolutions.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls string `split` for module name parsing, `self.visit_Import` to record dependencies, `self._resolve_module_name` for resolving relative imports, `print` for error messages, and `self.generic_visit` to continue AST traversal.
            *   *Called By:* This method is called by the `NodeVisitor` framework as it traverses the Abstract Syntax Tree.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file dependencies based on a given Abstract Syntax Tree (AST). It initializes a networkx.DiGraph and then uses a FileDependencyGraph visitor to traverse the provided AST, collecting import dependencies. The visitor populates an 'import_dependencies' attribute, which is then iterated over. For each identified caller and its associated callees (dependencies), nodes are added to the graph, and directed edges are created from the caller to each callee. Finally, the populated dependency graph is returned.
*   **Parameters:**
    - **filename** (`str`): The path or name of the file being analyzed for dependencies.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph where nodes represent files or modules and edges represent import dependencies.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a directed graph representing dependencies across an entire Git repository. It first retrieves all files from the provided GitRepository object. It then iterates through each Python file, parses its content into an Abstract Syntax Tree (AST), and builds a file-specific dependency graph using `build_file_dependency_graph`. Finally, it aggregates the nodes and edges from these individual file graphs into a single, comprehensive global directed graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to extract files and build the dependency graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependencies found across all Python files in the repository.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function takes a directory path as a string. It converts this string into an absolute `pathlib.Path` object. The function then recursively searches this root path for all files that have a '.py' extension. For each Python file found, it calculates its path relative to the initial root directory. Finally, it returns a list of these relative `pathlib.Path` objects.
*   **Parameters:**
    - **directory** (`str`): The string path to the root directory from which to recursively search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each path represents a Python file found within the specified directory, relative to the provided root directory.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various large language models (LLMs) to generate structured documentation for Python functions and classes. It abstracts away the complexities of LLM API calls, handles system prompt management, configures model-specific batch processing, and includes error handling and rate limiting. The class leverages Pydantic for input/output validation, ensuring the generated documentation conforms to predefined schemas.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class depends on external libraries for LLM interaction (e.g., `langchain_google_genai`, `langchain_ollama`, `langchain_openai`), message formatting (`langchain.messages`), JSON serialization (`json`), logging (`logging`), time management (`time`), and Pydantic schemas (`schemas.types`).
*   **Constructor:**
    *   *Description:* This constructor initializes the LLMHelper instance by setting up API keys, loading system prompts from specified file paths, and configuring the underlying Language Model (LLM) based on the provided model name. It supports various LLM providers like Gemini, OpenAI, custom APIs, and Ollama, and also configures batch processing settings for optimal performance.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **function_prompt_path** (`str`): The file path to the system prompt used for generating function analysis documentation.
        - **class_prompt_path** (`str`): The file path to the system prompt used for generating class analysis documentation.
        - **model_name** (`str`): The name of the LLM model to be used for generation, defaulting to 'gemini-2.0-flash-lite'.
        - **base_url** (`str`): An optional base URL for custom or Ollama LLM endpoints, if applicable.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* This private method sets the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It assigns specific batch sizes for various Gemini, Llama, and GPT models, as well as for custom or alias models. If the model name is unrecognized, it logs a warning and defaults to a conservative batch size of 2.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods within its body.
            *   *Called By:* This method is called internally by the `__init__` method of the `LLMHelper` class during instance initialization.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* This method generates and validates documentation for a batch of functions using the configured LLM. It takes a list of `FunctionAnalysisInput` objects, converts them into JSON payloads, and then creates conversations with the `function_system_prompt`. The conversations are processed in batches, respecting rate limits with a waiting period between calls. It returns a list of `FunctionAnalysis` objects or `None` for failed items.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing function details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, or `None` for any function where generation or validation failed.
        *   **Usage:**
            *   *Calls:* This method calls `json.dumps` to serialize input models, `SystemMessage` and `HumanMessage` to construct LLM conversations, `self.function_llm.batch` to send requests to the LLM, `logging.info` and `logging.error` for logging, and `time.sleep` for rate limiting.
            *   *Called By:* The input context does not specify any callers for this method.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* This method is responsible for generating and validating documentation for a batch of classes using the configured LLM. It accepts a list of `ClassAnalysisInput` objects, converts them into JSON payloads, and prepares them as conversations with the `class_system_prompt`. The method processes these conversations in batches, incorporating a waiting period to manage API rate limits. It returns a list of `ClassAnalysis` objects, with `None` for any items that failed processing.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing class details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, or `None` for any class where generation or validation failed.
        *   **Usage:**
            *   *Calls:* This method calls `json.dumps` to serialize input models, `SystemMessage` and `HumanMessage` to construct LLM conversations, `self.class_llm.batch` to send requests to the LLM, `logging.info` and `logging.error` for logging, and `time.sleep` for rate limiting.
            *   *Called By:* The input context does not specify any callers for this method.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy data and processing loop for testing the LLMHelper class. It defines several pre-computed `FunctionAnalysisInput` and `FunctionAnalysis` objects, as well as a `ClassAnalysisInput` object. It then instantiates an `LLMHelper` and uses it to process the dummy function inputs, logging the results.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a versatile interface for interacting with various large language models, including Google Gemini, OpenAI-compatible models, and Ollama. It centralizes the configuration and invocation of different LLM providers, dynamically selecting the appropriate client based on the specified model name during initialization. The class handles loading a system prompt from a file and offers both synchronous and asynchronous (streaming) methods for sending user input to the configured LLM and retrieving responses.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** Based on the provided context, this class does not have explicit external dependencies listed.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the MainLLM instance by validating the API key, loading a system prompt from a specified file path, and configuring the appropriate LLM client based on the model_name. It supports gemini-, gpt-, custom API models (like DeepSeek, Llama, Qwen, etc.), and Ollama models, setting up self.llm with the chosen provider.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM provider.
        - **prompt_file_path** (`str`): The file path to the system prompt, which is loaded and used for all LLM interactions.
        - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This determines which LLM client (e.g., ChatGoogleGenerativeAI, ChatOpenAI, ChatOllama) is instantiated.
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, used primarily for Ollama or other OpenAI-compatible APIs if SCADSLLM_URL is not set.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* This method performs a synchronous call to the configured LLM. It constructs a list of messages, including the pre-loaded system prompt and the provided user input, and then invokes the self.llm client. The method logs the call status and returns the content of the LLM's response or None if an error occurs during the invocation.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:*
            - **content** (`str`): The text content of the LLM's response.
            - **None** (`None`): Returns None if an exception occurs during the LLM call.
        *   **Usage:**
            *   *Calls:* Based on the provided context, this method does not explicitly call other methods, classes, or functions from the method_context.
            *   *Called By:* Based on the provided context, this method is not explicitly called by other functions or methods from the method_context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* This method initiates a streaming interaction with the configured LLM, allowing for real-time reception of the LLM's response. It prepares the messages with the system prompt and user input, then calls the stream method of self.llm. The method yields chunks of content as they are received from the LLM, or yields an error message if an exception occurs during the streaming process.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message for which a streaming response is desired.
        *   *Returns:*
            - **chunk.content** (`str`): Yields individual text chunks of the LLM's streaming response.
            - **error_message** (`str`): Yields an error message string if an exception occurs during the streaming call.
        *   **Usage:**
            *   *Calls:* Based on the provided context, this method does not explicitly call other methods, classes, or functions from the method_context.
            *   *Called By:* Based on the provided context, this method is not explicitly called by other functions or methods from the method_context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract comprehensive project information from common project configuration and documentation files. It systematically parses `pyproject.toml`, `requirements.txt`, and `README` files to gather details such as project title, description, features, tech stack, status, installation instructions, and dependencies. The class prioritizes information from structured files like `pyproject.toml` and provides fallbacks, including deriving a title from a repository URL. It consolidates all extracted data into a structured dictionary for easy access.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class depends on the `re` module for regular expression operations, the `os` module for path manipulation, and `tomllib` for parsing TOML files. It also utilizes `typing` for type hints.
*   **Constructor:**
    *   *Description:* The constructor initializes an instance attribute `INFO_NICHT_GEFUNDEN` to the string "Information not found". It also sets up a nested dictionary `self.info` with predefined keys for project overview and installation details, populating all initial values with the `INFO_NICHT_GEFUNDEN` placeholder.
    *   *Parameters:*
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content: str)`
        *   *Description:* This private helper method is designed to remove null bytes (`\x00`) from a given string content. These null bytes often appear due to encoding errors, such as reading a UTF-16 encoded file as UTF-8. The method first checks if the content is empty, returning an empty string if true; otherwise, it performs a string replacement to eliminate all occurrences of null bytes.
        *   *Parameters:*
            - **content** (`str`): The string content to be cleaned of null bytes.
        *   *Returns:*
            - **""** (`str`): The cleaned string with all null bytes removed.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods.
            *   *Called By:* This method is called by `_parse_readme`, `_parse_toml`, and `_parse_requirements`.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This private helper method searches for a specific file within a provided list of file objects, matching against a list of string patterns. It performs a case-insensitive comparison of each file's path with every pattern. The method iterates through the files and patterns, returning the first file object that matches any pattern. If no matching file is found after checking all possibilities, it returns `None`.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of string patterns to match against file names (e.g., 'readme.md').
            - **dateien** (`List[Any]`): A list of file objects, where each object is expected to have a `path` attribute.
        *   *Returns:*
            - **""** (`Optional[Any]`): The first file object that matches a pattern, or `None` if no match is found.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods.
            *   *Called By:* This method is called by `extrahiere_info`.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This private helper method extracts text content located directly under a Markdown level 2 heading (e.g., `## Heading`) within a given string. It dynamically constructs a regular expression pattern based on a list of keywords, enabling case-insensitive matching of the heading. The method captures all content following the matched heading up to the next `##` heading or the end of the string, then returns the stripped content.
        *   *Parameters:*
            - **inhalt** (`str`): The Markdown content string from which to extract a section.
            - **keywords** (`List[str]`): A list of keywords to match against Markdown headings (e.g., 'Features', 'Installation').
        *   *Returns:*
            - **""** (`Optional[str]`): The extracted section content as a string, or `None` if no matching section is found.
        *   **Usage:**
            *   *Calls:* This method calls `re.escape`, `re.compile`, and `re.search` from the `re` module.
            *   *Called By:* This method is called by `_parse_readme`.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This private method parses the content of a README file to extract various project information. It first cleans the content using `_clean_content`. It then attempts to extract the project title from a level 1 Markdown heading, a general description, key features, tech stack, current status, installation instructions, and a quick start guide by calling `_extrahiere_sektion_aus_markdown` with different keyword lists. The extracted information is stored in the instance's `self.info` dictionary, but only if the corresponding field is still set to `INFO_NICHT_GEFUNDEN`.
        *   *Parameters:*
            - **inhalt** (`str`): The string content of the README file to be parsed.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `_clean_content` and `_extrahiere_sektion_aus_markdown` from the same class, and `re.search` from the `re` module.
            *   *Called By:* This method is called by `extrahiere_info`.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This private method parses the content of a `pyproject.toml` file to extract project details. It first cleans the content using `_clean_content`. It checks for the availability of the `tomllib` module and prints a warning if it's not installed. If `tomllib` is available, it attempts to load the TOML content, extracts the project name, description, and dependencies from the `[project]` section, and updates the `self.info` dictionary. It includes error handling for `tomllib.TOMLDecodeError`.
        *   *Parameters:*
            - **inhalt** (`str`): The string content of the `pyproject.toml` file to be parsed.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `_clean_content` from the same class, `tomllib.loads`, and `data.get`.
            *   *Called By:* This method is called by `extrahiere_info`.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This private method parses the content of a `requirements.txt` file to extract project dependencies. It first cleans the content using `_clean_content`. It only populates the `dependencies` field in `self.info` if it has not already been set (e.g., by `_parse_toml`). It splits the content into lines, filters out empty lines and comments, and then stores the remaining lines as a list of dependencies.
        *   *Parameters:*
            - **inhalt** (`str`): The string content of the `requirements.txt` file to be parsed.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `_clean_content` from the same class.
            *   *Called By:* This method is called by `extrahiere_info`.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This public method orchestrates the entire information extraction process from various project files. It first uses `_finde_datei` to locate `README`, `pyproject.toml`, and `requirements.txt` files within a provided list of file objects. It then parses these files in a prioritized order (`pyproject.toml`, `requirements.txt`, then `README`) using their respective parsing methods (`_parse_toml`, `_parse_requirements`, `_parse_readme`). Finally, it formats the extracted dependencies and attempts to derive a project title from the repository URL if no title was found in the files, returning the complete `self.info` dictionary.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file objects, each expected to have a `content` attribute containing the file's text.
            - **repo_url** (`str`): The URL of the repository, used as a fallback to derive a project title.
        *   *Returns:*
            - **""** (`Dict[str, Any]`): A dictionary containing all extracted project information.
        *   **Usage:**
            *   *Calls:* This method calls `_finde_datei`, `_parse_toml`, `_parse_requirements`, `_parse_readme` from the same class, and `os.path.basename`, `repo_url.removesuffix` from the `os` module and string methods.
            *   *Called By:* This method is not explicitly called by any other method within the provided context.

### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an ast.NodeVisitor subclass designed to construct a directed call graph for a given Python source file. It traverses the Abstract Syntax Tree (AST) of a file, identifying function definitions, class definitions, import statements, and function calls. The class maintains internal state to track the current file, class, and function context, enabling it to resolve function and method calls to their fully qualified names. Its primary responsibility is to build a networkx.DiGraph representing the call relationships within the analyzed code, along with auxiliary data structures for name resolution and tracking.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class depends on the `ast` module for parsing Python code and the `networkx` library for graph representation. It also uses `typing.Dict` for type hinting.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph instance by setting up the `filename`, `current_function`, and `current_class` tracking variables. It also initializes several data structures: `local_defs` for local symbol definitions, `graph` as a NetworkX directed graph, `import_mapping` to track import aliases, `function_set` to store unique function names, and `edges` to store call relationships.
    *   *Parameters:*
        - **filename** (`str`): The name of the file being analyzed.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node: ast.AST)`
        *   *Description:* This private helper method recursively traverses an AST node to extract the full dotted name components of a function call. It handles `ast.Call`, `ast.Name`, and `ast.Attribute` nodes, returning a list of strings representing the components. This method effectively deconstructs complex call expressions into their constituent parts, such as ['pkg', 'mod', 'Class', 'method'].
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a call expression or its components.
        *   *Returns:*
            - **name** (`list[str]`): A list of string components forming the full name of the called entity.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods within its own definition.
            *   *Called By:* This method is called by visit_Call.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* This private method takes a list of potential callee name components (e.g., [['module', 'function']]) and attempts to resolve them to their fully qualified names. It first checks `self.local_defs` for local definitions, then `self.import_mapping` for imported modules/functions. If no local or imported resolution is found, it constructs a full name based on the current filename and class context. The method ensures that each callee is resolved to a unique, fully qualified identifier.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains string components of a potential callee's name.
        *   *Returns:*
            - **name** (`list[str]`): A list of fully resolved string names for the callees.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods within its own definition.
            *   *Called By:* This method is called by visit_Call.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None)`
        *   *Description:* This private helper method constructs a fully qualified name for a function or method. It takes a base name and an optional class name. If a class name is provided, the full name includes the filename, class name, and base name, separated by `::`. Otherwise, it includes only the filename and base name. This ensures consistent naming conventions for nodes in the call graph.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`str | None`): The name of the class if the entity is a method, otherwise None.
        *   *Returns:*
            - **name** (`str`): The fully qualified name of the entity.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods within its own definition.
            *   *Called By:* This method is called by visit_FunctionDef.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private method determines the identifier of the currently active caller context. It checks if `self.current_function` is set, returning its value if it is. If `self.current_function` is None, it defaults to a global scope identifier, either using the `filename` if available or a generic '<global-scope>'. This method is crucial for correctly attributing calls to their source.
        *   *Parameters:*
        *   *Returns:*
            - **name** (`str`): The identifier of the current calling context.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods within its own definition.
            *   *Called By:* This method is called by visit_Call.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method is an AST visitor that processes `ast.Import` nodes. It iterates through each alias defined in the import statement, extracting the module's original name and its aliased name (if any). It then populates `self.import_mapping` with these mappings, associating the aliased name with the original module name. Finally, it calls `self.generic_visit` to continue traversing the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls self.generic_visit.
            *   *Called By:* This method is implicitly called by the AST traversal mechanism when an ast.Import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method is an AST visitor that processes `ast.ImportFrom` nodes. It extracts the base module name from which objects are imported. For each alias within the import statement, it maps the aliased name (or original name if no alias) to the resolved module name in `self.import_mapping`. This helps in resolving calls to functions or classes imported from specific modules.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing an 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods within its own definition.
            *   *Called By:* This method is implicitly called by the AST traversal mechanism when an ast.ImportFrom node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is an AST visitor that processes `ast.ClassDef` nodes. It temporarily updates `self.current_class` to the name of the class being visited, allowing nested functions and methods to correctly determine their full names. After visiting the class's body using `self.generic_visit`, it restores `self.current_class` to its previous value, ensuring proper scope management during AST traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls self.generic_visit.
            *   *Called By:* This method is implicitly called by the AST traversal mechanism when an ast.ClassDef node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method is an AST visitor that processes `ast.FunctionDef` nodes. It first saves the current function context and then constructs the full qualified name for the function using `_make_full_name`. This full name is stored in `self.local_defs` for resolution. It then updates `self.current_function` to the newly defined function's full name, adds this function as a node to the `self.graph`, and continues the AST traversal. Finally, it adds the function to `self.function_set` and restores the previous function context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls _make_full_name, self.graph.add_node, and self.generic_visit.
            *   *Called By:* This method is implicitly called by the AST traversal mechanism when an ast.FunctionDef node is encountered. It is also explicitly called by visit_AsyncFunctionDef.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is an AST visitor that processes `ast.AsyncFunctionDef` nodes. It acts as a wrapper, simply delegating the processing of asynchronous function definitions to the `visit_FunctionDef` method. This ensures that both synchronous and asynchronous functions are handled uniformly in terms of call graph construction and name resolution.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls visit_FunctionDef.
            *   *Called By:* This method is implicitly called by the AST traversal mechanism when an ast.AsyncFunctionDef node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method is an AST visitor that processes `ast.Call` nodes, which represent function or method calls. It identifies the current caller using `_current_caller` and then recursively extracts the components of the called entity using `_recursive_call`. These components are then resolved to fully qualified names using `_resolve_all_callee_names`. Finally, it records the call relationship by adding the resolved callees to the `self.edges` dictionary for the current caller.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls _current_caller, _recursive_call, _resolve_all_callee_names, and self.generic_visit.
            *   *Called By:* This method is implicitly called by the AST traversal mechanism when an ast.Call node is encountered.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node: ast.If)`
        *   *Description:* This method is an AST visitor that processes `ast.If` nodes. It specifically handles the common `if __name__ == "__main__":` block by temporarily setting the `current_function` to '<main_block>'. This allows calls within the main execution block to be correctly attributed. For all other `if` statements, it simply delegates to `self.generic_visit` to continue the standard AST traversal.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing an if statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls self.generic_visit.
            *   *Called By:* This method is implicitly called by the AST traversal mechanism when an ast.If node is encountered.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function, `make_safe_dot`, takes a NetworkX directed graph and an output file path. Its primary purpose is to prepare the graph for DOT file generation by replacing complex node names with simple, safe identifiers. It achieves this by creating a copy of the graph, generating a unique 'n<i>' identifier for each original node, and then relabeling the graph with these new identifiers. The original node names are preserved by assigning them as 'label' attributes to the relabeled nodes. Finally, the modified graph is written to the specified output path in DOT format.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The input NetworkX directed graph to be processed and made safe for DOT representation.
    - **out_path** (`str`): The file path where the processed DOT graph will be written.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** This function constructs a filtered call graph for a given Git repository. It first retrieves all files from the repository and identifies all user-defined functions within Python files. Subsequently, it builds a directed graph where nodes represent these identified functions and edges indicate call relationships between them. The resulting graph exclusively includes calls between functions that are considered 'self-written' within the repository.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object containing the source code files to be analyzed.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between user-defined functions found in the repository.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content: str)`
*   **Description:** This function takes a string `content` as input and encloses it within XML CDATA tags. It constructs the CDATA block using an f-string, adding newline characters before and after the provided content. The primary purpose is to escape special characters within the content when embedding it in XML or similar documents, ensuring the content is parsed as character data rather than markup.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped within CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A string containing the input content enclosed within CDATA tags, formatted with newlines.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs: list, image_list: list)`
*   **Description:** This function processes a list of output objects, typically from a notebook execution, to extract their content. It iterates through each output, identifying its type to handle text, images, and errors differently. For image data (PNG or JPEG), it decodes Base64 strings, stores the raw data in a provided mutable list, and inserts an XML-like placeholder into the result. Text content is extracted directly, and error outputs are formatted into a string. The function ultimately compiles and returns a list of these extracted text snippets or image placeholders.
*   **Parameters:**
    - **outputs** (`list`): A list or iterable of output objects, typically from a notebook execution, containing various types of data like text, images, or errors.
    - **image_list** (`list`): A mutable list used to store dictionaries representing extracted image data. Each dictionary contains 'mime_type' and the Base64 'data' string for the image.
*   **Returns:**
    - **extracted_xml_snippets** (`list[str]`): A list of strings, which can be plain text content, formatted error messages, or XML-like placeholders for extracted images.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type: str)`
*   **Description:** This function processes an image based on its MIME type. It checks if the provided `mime_type` exists as a key in an external `data` dictionary. If found, it retrieves the base64 encoded image string, removes any newline characters, and appends a dictionary containing the `mime_type` and cleaned base64 data to an external `image_list`. Finally, it returns a formatted string representing an image placeholder with the assigned index and MIME type. In case of any processing error, it returns an error message string. If the `mime_type` is not found in `data`, the function returns `None`.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed, used as a key to retrieve its base64 data from an external `data` dictionary.
*   **Returns:**
    - **image_placeholder_tag** (`str`): A formatted string representing an image placeholder, containing the image's index and MIME type, if processing is successful.
    - **error_message** (`str`): An error message string if an exception occurs during image processing.
    - **None** (`None`): Returns `None` if the specified `mime_type` is not found in the external `data` dictionary.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content: str)`
*   **Description:** This function converts the raw content of a Jupyter notebook (provided as a string) into a structured XML format. It parses the input using `nbformat`, handling potential `NotJSONError` by returning an error message. The function iterates through markdown and code cells, generating corresponding XML elements. For code cell outputs, it extracts content and images, wrapping them in CDATA where appropriate. Finally, it returns the complete XML string and a list of any extracted images.
*   **Parameters:**
    - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a string in JSON format.
*   **Returns:**
    - **xml_representation** (`str`): A string containing the XML representation of the notebook, or an error message if parsing fails.
    - **extracted_images** (`list[str]`): A list of strings representing base64 encoded images extracted from the notebook outputs.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files: Iterable[object])`
*   **Description:** This function processes a list of repository files to identify and convert Jupyter notebooks. It filters the input `repo_files` to select only those ending with '.ipynb'. For each identified notebook, it logs its path and then invokes `convert_notebook_to_xml` using the notebook's content. The results, comprising XML output and extracted images, are stored in a dictionary keyed by the notebook's file path. This dictionary, containing all processed notebook data, is then returned.
*   **Parameters:**
    - **repo_files** (`Iterable[object]`): An iterable collection of file-like objects from a repository. Each object is expected to have a 'path' attribute (string) and a 'content' attribute.
*   **Returns:**
    - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the paths of the processed notebook files (string) and values are dictionaries containing the 'xml' output (string) and 'images' (Any) generated from each notebook.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, designed for efficient access to its properties. It employs a lazy-loading mechanism for its Git blob object, file content, and size, ensuring that these potentially heavy operations are only performed when explicitly requested. The class provides methods to access file metadata like path and size, retrieve its content, and offers an example analysis method for word counting. It also includes utility methods for string representation and conversion to a dictionary format.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class relies on the `git` library for `git.Tree` and `git.Blob` objects, and the `os` module for path manipulation.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes a `RepoFile` object by storing the file path and the Git `Tree` object from which the file originates. It sets up internal attributes (`_blob`, `_content`, `_size`) to `None` to facilitate lazy loading of the file's data.
    *   *Parameters:*
        - **file_path** (`str`): Der Pfad zur Datei innerhalb des Repositories.
        - **commit_tree** (`git.Tree`): Das Tree-Objekt des Commits, aus dem die Datei stammt.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading for the Git `Blob` object associated with the file. It first checks if the `_blob` attribute is already loaded; if not, it attempts to retrieve the blob from the `_tree` object using the stored file path. If the file is not found within the commit tree, a `FileNotFoundError` is raised.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`git.Blob`): The Git Blob object representing the file content.
        *   **Usage:**
            *   *Calls:* This method accesses internal attributes like `self._tree` and `self.path` to retrieve the blob.
            *   *Called By:* This method is called by the `content` and `size` properties to access the Git blob, and potentially by other external functions.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It checks if the `_content` attribute is already loaded. If not, it accesses the `blob` property to obtain the Git `Blob` object, reads its data stream, and decodes it using UTF-8, ignoring any decoding errors.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`str`): The decoded content of the file as a string.
        *   **Usage:**
            *   *Calls:* This method calls the `blob` property to retrieve the Git blob object, and then `data_stream.read()` and `decode()` on the blob.
            *   *Called By:* This method is called by `analyze_word_count` and `to_dict` (conditionally), and potentially by other external functions.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It first checks if the `_size` attribute is already loaded. If not, it accesses the `blob` property to retrieve the Git `Blob` object and then extracts its `size` attribute, which represents the file's size.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   *Calls:* This method calls the `blob` property to retrieve the Git blob object.
            *   *Called By:* This method is called by `to_dict` and potentially by other external functions.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function, demonstrating how to process the file's content. It calculates the total number of words present in the file's content. This is achieved by accessing the `content` property, splitting the resulting string by whitespace, and then returning the count of elements in the generated list.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`int`): The total number of words in the file content.
        *   **Usage:**
            *   *Calls:* This method calls the `content` property.
            *   *Called By:* This method is not explicitly called by other methods within the class, suggesting it's intended for external use.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This special method provides a developer-friendly string representation of the `RepoFile` object. It constructs a string formatted as `<RepoFile(path='...')>`, which includes the `path` attribute of the instance. This representation is particularly useful for debugging and logging purposes, offering a concise summary of the object.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:**
            *   *Calls:* This method accesses `self.path` to include it in the representation.
            *   *Called By:* This method is implicitly called by Python's `repr()` function or when the object is printed in an interactive environment.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content: bool)`
        *   *Description:* This method converts the `RepoFile` object into a dictionary representation, providing a structured way to export its data. It includes the file's path, its base name (derived using `os.path.basename`), its size (obtained via the `size` property), and its type, which is fixed as 'file'. Optionally, if `include_content` is set to `True`, the method also adds the file's content (retrieved via the `content` property) to the dictionary.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the file's content will be included in the dictionary.
        *   *Returns:*
            - **null** (`dict`): A dictionary representation of the file, optionally including its content.
        *   **Usage:**
            *   *Calls:* This method calls `os.path.basename`, `self.size`, and `self.content` (conditionally).
            *   *Called By:* This method is not explicitly called by other methods within the class, suggesting it's intended for serialization or external data representation.

#### Class: `GitRepository`
*   **Summary:** This class provides a robust mechanism for interacting with Git repositories programmatically. It handles the cloning of a remote repository into a temporary local directory, provides methods to list all files, and can generate a hierarchical tree structure of the repository's contents. It also implements the context manager protocol (__enter__ and __exit__) to ensure that the temporary directory and its cloned contents are automatically cleaned up upon exiting the context, preventing resource leaks.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class relies on `tempfile` for temporary directory management, `git.Repo` and `git.GitCommandError` from the GitPython library for Git operations, and `logging` for informational messages.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes a GitRepository instance by cloning the specified Git repository URL into a newly created temporary directory. It sets up instance attributes such as the repository URL, the path to the temporary directory, the GitPython Repo object, and an empty list to store file objects. During initialization, it also captures the latest commit and its tree, logging the cloning process and handling potential `GitCommandError` by cleaning up and raising a `RuntimeError`.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a comprehensive list of all files present within the cloned Git repository. It achieves this by executing the `git.ls_files()` command to obtain a list of file paths. For each identified path, it instantiates a `RepoFile` object, associating it with the current commit tree, and then compiles these objects into a list, which is stored in `self.files` and subsequently returned.
        *   *Parameters:*
        *   *Returns:*
            - **None** (`list[RepoFile]`): A list of `RepoFile` instances, each representing a file in the repository.
        *   **Usage:**
            *   *Calls:* This method calls `self.repo.git.ls_files()` to list files and `RepoFile` to create file objects.
            *   *Called By:* This method is called by `get_file_tree`.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is responsible for performing cleanup operations by deleting the temporary directory where the Git repository was cloned. It first verifies if `self.temp_dir` is set, indicating an active temporary directory. If so, it prints a message confirming the deletion and then sets `self.temp_dir` to `None` to signify that the directory has been removed.
        *   *Parameters:*
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `print()` to output a message.
            *   *Called By:* This method is called by the `__exit__` method and potentially by the `__init__` method in case of a cloning error.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This special method enables the `GitRepository` class to function as a context manager, allowing its use within a `with` statement. When the `with` block is entered, this method is implicitly invoked and simply returns the current instance of the `GitRepository` itself, making it available for operations within the context.
        *   *Parameters:*
        *   *Returns:*
            - **None** (`GitRepository`): The instance of the `GitRepository` class.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other functions or methods.
            *   *Called By:* This method is implicitly called when the `GitRepository` object is used in a `with` statement.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type: type, exc_val: Exception, exc_tb: traceback)`
        *   *Description:* This special method is an integral part of the context manager protocol, ensuring proper resource management. It is automatically invoked when exiting a `with` statement, regardless of whether an exception occurred within the block. Its primary function is to call the `self.close()` method, guaranteeing that the temporary directory and its contents are cleaned up reliably.
        *   *Parameters:*
            - **exc_type** (`type`): The type of the exception that caused the context to be exited, or `None` if no exception occurred.
            - **exc_val** (`Exception`): The exception instance that caused the context to be exited, or `None`.
            - **exc_tb** (`traceback`): The traceback object associated with the exception, or `None`.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self.close()` to clean up the temporary directory.
            *   *Called By:* This method is implicitly called when exiting a `with` statement where the `GitRepository` object is used.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content: bool)`
        *   *Description:* This method generates a hierarchical tree representation of all files within the repository. It first checks if `self.files` is populated; if not, it calls `get_all_files()` to retrieve them. It then iterates through each `RepoFile` object, parsing its path to construct a nested dictionary structure that accurately reflects the directory hierarchy. Each file is added to its respective directory node using its `to_dict()` method, with an option to include file content.
        *   *Parameters:*
            - **include_content** (`bool`): A boolean flag indicating whether the content of each file should be included in its dictionary representation. Defaults to `False`.
        *   *Returns:*
            - **None** (`dict`): A dictionary representing the hierarchical file tree of the repository, with directories and files nested appropriately.
        *   **Usage:**
            *   *Calls:* This method calls `self.get_all_files()` if `self.files` is empty and `file_obj.to_dict()` for each file.
            *   *Called By:* This method is not explicitly called by other methods within the provided class definition.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart to visually compare two token counts, specifically for JSON and TOON formats, and highlights the percentage of token savings. It initializes the chart with labels, values, and colors, then sets a title that includes the savings percentage, a y-axis label, and a grid. The function also adds the exact token counts as bold text above each bar for clarity. Finally, it saves the generated chart to a specified output path and closes the plot to free up resources.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings to be displayed in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart image will be saved.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep durations from the total elapsed time. It takes start and end timestamps, total items, batch size, and a model name as input. If the model name does not begin with 'gemini-', it returns the direct total duration. For 'gemini-' models, it computes the number of batches and associated sleep time, assuming 61 seconds per sleep interval, then subtracts this from the total duration. The function ensures the returned net time is never negative.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp of the operation.
    - **end_time** (`float`): The ending timestamp of the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed per batch.
    - **model_name** (`str`): The name of the model used, which determines if sleep times are considered.
*   **Returns:**
    - **net_time** (`float`): The calculated net duration, after subtracting estimated sleep times, or the total duration if not a 'gemini-' model. The value is guaranteed to be non-negative.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive analysis pipeline for a given input, typically a GitHub repository URL. It handles the extraction of API keys and model configurations, clones the specified repository, and then proceeds to extract basic project information, construct a file tree, and perform detailed relationship and Abstract Syntax Tree (AST) analysis. The function prepares and dispatches these analyzed components to a Helper LLM for individual function and class documentation generation. Finally, it aggregates all analysis results and passes them to a Main LLM to produce a final, comprehensive report, including token usage metrics and saving the output.
*   **Parameters:**
    - **input** (`str`): The initial user input, expected to contain a GitHub repository URL for analysis.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the helper and main LLM models to be utilized in the workflow.
    - **status_callback** (`callable`): An optional callback function used to provide real-time status updates during the workflow execution.
*   **Returns:**
    - **result** (`dict`): A dictionary containing the 'report' (the final generated report as a string) and 'metrics' (a dictionary of performance statistics and token savings).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions.

#### Function: `update_status`
*   **Signature:** `def update_status(msg: str)`
*   **Description:** This function, `update_status`, is designed to handle and propagate status messages. It takes a message as input and first checks if a `status_callback` function is available. If `status_callback` exists, it is invoked with the provided message, allowing for external status updates. Regardless of the `status_callback`'s presence, the function logs the message at an informational level using the `logging` module.
*   **Parameters:**
    - **msg** (`str`): The status message to be processed and logged.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback: callable | None)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing GitHub repository notebooks using a Large Language Model (LLM). It begins by extracting a GitHub repository URL from the input, cloning the repository, and converting its notebook files into an XML-based structure. It then extracts basic project information and initializes an appropriate LLM client based on the specified model and API keys. The function iteratively processes each notebook, constructing a detailed payload (including text and embedded images) for the LLM, and generates individual reports. Finally, it concatenates all reports into a single markdown file, saves it to a designated output directory, and returns the final report along with performance metrics.
*   **Parameters:**
    - **input** (`str`): The input string, which is expected to contain a GitHub repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama') used for authentication.
    - **model** (`str`): The name of the Large Language Model to be used for processing and generating reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`callable | None`): An optional callback function that can be provided to receive status updates and messages during the workflow execution.
*   **Returns:**
    - **result** (`dict`): A dictionary containing two keys: 'report', which holds the concatenated markdown string of all notebook analyses, and 'metrics', a dictionary of performance timings and model information.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info: dict, nb_path: str, xml_content: str, images: list[dict])`
*   **Description:** This function constructs a multi-part payload suitable for the Gemini API, combining textual context and embedded image data. It begins by serializing basic project information and the current notebook path into a JSON string, which forms the initial text part of the payload. The function then processes an XML content string, using regular expressions to locate and extract image placeholders. For each placeholder, it retrieves the corresponding base64 encoded image data from a provided list and formats it as an image_url part. Any text segments between image placeholders, or remaining text, are added as text parts. The final output is a list of dictionaries, each representing a text or image component of the Gemini payload.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing fundamental project information to be included in the payload's context.
    - **nb_path** (`str`): The file path of the current notebook, used as context in the payload.
    - **xml_content** (`str`): The XML string representing the notebook's structure, potentially containing image placeholders.
    - **images** (`list[dict]`): A list of dictionaries, where each dictionary contains base64 encoded image data and its MIME type, corresponding to the image placeholders.
*   **Returns:**
    - **payload_content** (`list[dict]`): A list of dictionaries, each representing a part of the Gemini API payload, which can be either text or image data.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/relationship_analyzer.py`

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to build a comprehensive call graph and identify relationships between functions, methods, and classes. It achieves this by first discovering all Python files, then parsing them to collect definitions, and finally resolving calls within those files. The class provides methods to initiate the analysis and retrieve the raw outgoing and incoming call relationships, serving as a core component for understanding code structure and dependencies.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class relies on external modules such as `os` for file system operations, `ast` for parsing Python code into Abstract Syntax Trees, `logging` for error reporting, and `collections.defaultdict` for managing graph data structures. It also depends on `path_to_module` and `CallResolverVisitor` which are not defined in the provided source but are implied by their usage.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer with the root directory of the project. It sets up various internal data structures such as dictionaries for definitions, a defaultdict for the call graph, and a dictionary to store ASTs of files. It also defines a set of directories to ignore during file system traversal.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed. This path is converted to an absolute path upon initialization.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project using an internal helper. Subsequently, it iterates through these files twice: once to collect all function, method, and class definitions, and then again to resolve calls made within each file. Finally, it clears temporary ASTs stored in memory and returns the generated call graph.
        *   *Parameters:*
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee pathnames and values are lists of caller information.
        *   **Usage:**
            *   *Calls:* This method calls _find_py_files to locate Python files, _collect_definitions to gather code definitions, and _resolve_calls to establish call relationships.
            *   *Called By:* This method is not explicitly called by any other methods within the provided context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* This method processes the internal call graph to generate structured outgoing and incoming relationship dictionaries. It iterates through the established call graph, extracting caller and callee identifiers for each relationship. It then populates two separate dictionaries, 'outgoing' and 'incoming', with sets of unique relationships, which are finally converted to sorted lists for consistent output.
        *   *Parameters:*
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys: 'outgoing' and 'incoming'. Each key maps to a dictionary where keys are entity identifiers and values are sorted lists of related entity identifiers.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other methods or functions within the provided source code.
            *   *Called By:* This method is not explicitly called by any other methods within the provided context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private helper method is responsible for recursively traversing the project root directory to locate all Python files. It utilizes `os.walk` to navigate the file system, actively pruning directories that are specified in the `self.ignore_dirs` set. The method collects and returns a list of absolute paths to all `.py` files found.
        *   *Parameters:*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found in the project, excluding ignored directories.
        *   **Usage:**
            *   *Calls:* This method calls `os.walk` to traverse the file system and `os.path.join` to construct file paths.
            *   *Called By:* This method is called by the `analyze` method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath: str)`
        *   *Description:* This private method parses a given Python file to identify and collect all function, method, and class definitions. It reads the file's source code, parses it into an Abstract Syntax Tree (AST) using `ast.parse`, and stores the AST for later use. It then walks the AST to find `ast.FunctionDef` and `ast.ClassDef` nodes, constructing a unique pathname for each and storing its file path, line number, and type in `self.definitions`. Error handling is included for file processing issues.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file from which to collect definitions.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `open` to read the file, `ast.parse` to create an AST, `path_to_module` to convert file paths, `ast.walk` to traverse the AST, `_get_parent` to determine parent nodes, and `logging.error` for error reporting.
            *   *Called By:* This method is called by the `analyze` method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree: ast.AST, node: ast.AST)`
        *   *Description:* This private helper method determines the direct parent AST node of a given child node within a larger Abstract Syntax Tree. It iterates through all nodes in the provided `tree` and, for each potential parent, checks if the target `node` is one of its direct children. This is crucial for correctly identifying whether a function definition is a standalone function or a method within a class.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within for the parent node.
            - **node** (`ast.AST`): The child AST node for which the direct parent is to be found.
        *   *Returns:*
            - **parent_node** (`ast.AST | None`): The direct parent AST node of the given child node if found, otherwise `None`.
        *   **Usage:**
            *   *Calls:* This method calls `ast.walk` to traverse the AST and `ast.iter_child_nodes` to inspect children of a node.
            *   *Called By:* This method is called by the `_collect_definitions` method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath: str)`
        *   *Description:* This private method is responsible for resolving function and method calls within a specific Python file. It retrieves the file's pre-parsed AST and then instantiates a `CallResolverVisitor` with the file path, project root, and collected definitions. The visitor traverses the AST to identify calls, and the resolved call information is then extended into the class's main `call_graph` data structure. Error handling is included for issues during call resolution.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self.file_asts.get` to retrieve the AST, `CallResolverVisitor` to instantiate a visitor, `resolver.visit` to perform the AST traversal, `self.call_graph.extend` to update the call graph, and `logging.error` for error reporting.
            *   *Called By:* This method is called by the `analyze` method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor is an `ast.NodeVisitor` subclass designed to traverse a Python Abstract Syntax Tree (AST) to identify and resolve function and method calls within a given source file. It maintains a scope of imported names and tracks the types of instantiated objects to accurately determine the fully qualified names of called entities. The visitor records these call relationships, along with caller context, into an internal dictionary, providing a comprehensive map of inter-function/method dependencies.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class depends on the `ast` module for AST traversal, `os` for path manipulation, and `collections.defaultdict` for storing call information. It also implicitly depends on a `path_to_module` utility function, which is not part of the class but is used in its `__init__`.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with the current file path, the project's root directory, and a dictionary of known definitions. It sets up internal state variables like `module_path`, `scope`, `instance_types`, `current_caller_name`, `current_class_name`, and a `defaultdict` to store call relationships.
    *   *Parameters:*
        - **filepath** (`string`): The path to the Python file being analyzed.
        - **project_root** (`string`): The root directory of the entire project.
        - **definitions** (`dict`): A dictionary containing known definitions (functions, classes, etc.) for lookup.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is part of the `ast.NodeVisitor` pattern, specifically designed to handle `ClassDef` nodes in the Abstract Syntax Tree. It temporarily updates the `current_class_name` attribute to reflect the class being visited, allowing nested functions or methods to correctly identify their parent class. After processing the class's children using `self.generic_visit(node)`, it restores the `current_class_name` to its previous value, ensuring proper scope management during tree traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self.generic_visit` to continue traversing the AST.
            *   *Called By:* This method is called by the `ast.NodeVisitor` framework when a `ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method processes `FunctionDef` nodes in the AST. It constructs a `full_identifier` for the function, considering whether it's a method within a class or a top-level function. It then updates `current_caller_name` to this `full_identifier` to track the current context for any nested calls. After visiting the function's body, it restores the `current_caller_name` to its state before entering the function, maintaining correct call stack context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self.generic_visit` to continue traversing the AST.
            *   *Called By:* This method is called by the `ast.NodeVisitor` framework when a `FunctionDef` node is encountered during AST traversal.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method is responsible for identifying and recording function or method calls within the AST. It first resolves the qualified name of the called entity using `_resolve_call_qname`. If the callee is found within the `definitions`, it determines the type of the caller (module, local function, method, or function) and stores information about the call, including the file, line number, caller's full identifier, and caller type, into the `self.calls` dictionary. Finally, it continues the AST traversal.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self._resolve_call_qname` to determine the qualified name of the called function/method and `self.generic_visit` to continue traversing the AST.
            *   *Called By:* This method is called by the `ast.NodeVisitor` framework when a `Call` node is encountered during AST traversal.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method processes `Import` nodes, which represent `import module` statements. For each imported module, it records the module's name (or its alias) in the `self.scope` dictionary, mapping the local name to its full module path. This `scope` dictionary is crucial for later resolving qualified names of calls. After processing all aliases, it continues the AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self.generic_visit` to continue traversing the AST.
            *   *Called By:* This method is called by the `ast.NodeVisitor` framework when an `Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method handles `ImportFrom` nodes, such as `from module import name`. It determines the full module path for the imported names, accounting for relative imports (`node.level`). It then stores these fully qualified names in the `self.scope` dictionary, mapping the local alias (or original name) to its complete path. This allows for accurate resolution of imported functions or classes. After processing, it continues the AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a `from ... import ...` statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self.generic_visit` to continue traversing the AST.
            *   *Called By:* This method is called by the `ast.NodeVisitor` framework when an `ImportFrom` node is encountered during AST traversal.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node: ast.Assign)`
        *   *Description:* This method processes `Assign` nodes, specifically looking for assignments where a variable is assigned the result of a constructor call (e.g., `x = MyClass()`). It checks if the assigned value is an `ast.Call` whose function is an `ast.Name`, and if that name corresponds to a known class in `self.scope` and `self.definitions`. If so, it records the qualified class name as the type of the assigned variable in `self.instance_types`. This helps resolve method calls on instances later.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
        *   **Usage:**
            *   *Calls:* This method calls `self.generic_visit` to continue traversing the AST.
            *   *Called By:* This method is called by the `ast.NodeVisitor` framework when an `Assign` node is encountered during AST traversal.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node: ast.expr)`
        *   *Description:* This private helper method attempts to resolve the fully qualified name (QName) of a function or method being called. It handles two main cases: direct calls to names (`ast.Name`) and method calls on attributes (`ast.Attribute`). For `ast.Name` calls, it checks `self.scope` for imports or constructs a local pathname. For `ast.Attribute` calls, it tries to resolve the instance type from `self.instance_types` or a module from `self.scope` to build the QName. If a QName cannot be resolved, it returns `None`.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., `ast.Name` or `ast.Attribute`).
        *   *Returns:*
            - **name** (`string | None`): The fully qualified name of the called function/method, or `None` if it cannot be resolved.
        *   **Usage:**
            *   *Calls:* This method does not explicitly call other methods within the class, but it accesses `self.scope`, `self.definitions`, and `self.instance_types`.
            *   *Called By:* This method is called by `self.visit_Call` to determine the qualified name of a function or method being invoked.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into its corresponding Python module path string. It first attempts to determine the path relative to a specified project root. If that fails, it uses the base name of the file. It then removes the '.py' extension if present, replaces file system path separators with dots, and finally adjusts the module path by removing '.__init__' if the path ends with it, to yield the correct module name.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The Python module path string derived from the input filepath.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/scads_key_test.py`
*Analysis data not available for this component.*

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function encrypts a given string using a `cipher_suite` object. It first checks if the input text is empty or if the `cipher_suite` is not initialized; if either condition is true, it returns the original text without encryption. Otherwise, it prepares the text by stripping whitespace and encoding it to bytes, then encrypts it using the `cipher_suite.encrypt` method. Finally, the encrypted bytes are decoded back into a string before being returned.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string, or the original string if encryption was skipped due to empty input or an uninitialized cipher suite.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given string using a global or externally defined `cipher_suite` object. It first checks if the input `text` is empty or if `cipher_suite` is not available, in which case it returns the original text without modification. If decryption is attempted, the text is stripped of whitespace, encoded to bytes, decrypted, and then decoded back into a string. A try-except block handles any exceptions during the decryption process, returning the original text if an error occurs.
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted string, or the original string if decryption is not performed or fails due to an exception.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function is responsible for inserting a new user record into the database. It takes a username, name, and a plain-text password as input. The password is first hashed using `stauth.Hasher.hash` before being stored. It constructs a user document with the provided details, setting the username as the document's `_id`, and initializes API key fields to empty strings. Finally, it inserts this document into the `dbusers` collection and returns the `_id` of the newly inserted document.
*   **Parameters:**
    - **username** (`str`): The unique username to be used as the `_id` for the new user document.
    - **name** (`str`): The full name of the new user.
    - **password** (`str`): The plain-text password for the new user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The `_id` of the newly inserted user document, which corresponds to the provided username.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function, `fetch_all_users`, is designed to retrieve all user records from a database collection. It accesses a global or module-level database object named `dbusers` and invokes its `find()` method to query all documents. The results, which are typically returned as a cursor, are then converted into a standard Python list. This list, containing all user data, is subsequently returned by the function.
*   **Parameters:**
*   **Returns:**
    - **users** (`list[dict]`): A list of dictionaries, where each dictionary represents a user record fetched from the 'dbusers' collection.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** This function, `fetch_user`, is responsible for retrieving a single user document from a database collection named `dbusers`. It queries the collection using the provided `username` as the document's `_id`. The function returns the found user document or `None` if no matching user is located.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched, which is used to match the `_id` field in the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if a match is found, otherwise `None`.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the 'name' field for a specific user in the 'dbusers' collection. It identifies the user by their unique 'username', which is mapped to the '_id' field in the database. The function performs a single update operation, setting the 'name' field to the provided 'new_name'. It then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose name is to be updated. This maps to the '_id' field in the database.
    - **new_name** (`str`): The new name to be assigned to the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. Typically 1 if the user is found and updated, or 0 if not found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database. It takes a username and a new Gemini API key as input. The provided API key is first stripped of whitespace and then encrypted before being stored. The function then updates the corresponding user record in the 'dbusers' collection, setting the 'gemini_api_key' field to the encrypted value. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored, which will be encrypted before saving.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation. Typically 1 if the update was successful, 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** This function updates a user's GPT API key in the database. It first encrypts the provided API key, ensuring any leading or trailing whitespace is removed. The encrypted key is then stored in the 'gpt_api_key' field for the user identified by their username. The function returns the number of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The username of the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be stored for the user. This key will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specific user within a database. It takes a username and a new Ollama base URL as input. The function uses the provided username as the document identifier and sets the 'ollama_base_url' field to the new URL after stripping any leading or trailing whitespace. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be updated.
    - **ollama_base_url** (`str`): The new base URL for Ollama to be associated with the specified user. Leading/trailing whitespace will be removed.
*   **Returns:**
    - **modified_count** (`int`): An integer representing the number of documents that were modified by the update operation. Typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function updates a user's Open Source API key in the database. It takes a username and the new API key as input. The provided API key is first stripped of whitespace and then encrypted before being stored. The function then updates the `opensrc_api_key` field for the specified user in the `dbusers` collection. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API key is to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be encrypted and stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** This function updates the 'opensrc_base_url' field for a specific user in a database. It takes a username and a new opensource base URL as input. The provided URL is first stripped of any leading or trailing whitespace before being used in the update operation. The function then performs a database update operation, targeting the document identified by the username. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose 'opensrc_base_url' is to be updated.
    - **opensrc_base_url** (`str`): The new base URL for opensource projects, which will be stripped of leading/trailing whitespace before being stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation. A value of 1 indicates success, 0 indicates no document was found or changed.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** The `fetch_gemini_key` function is designed to retrieve a user's Gemini API key from a database. It accepts a username as an argument. The function queries a `dbusers` collection to locate a document matching the provided username. It specifically projects the `gemini_api_key` field from the found document. If a user document is successfully found, the function returns the associated Gemini API key; otherwise, it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key associated with the user, or None if the user or the key is not found in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL for a specified user from a database. It queries the `dbusers` collection, searching for a document where the `_id` matches the provided `username`. If a user document is found, it extracts the `ollama_base_url` field. The function returns this URL if available, otherwise it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be fetched from the database.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The base URL for Ollama associated with the specified user, or None if the user is not found in the database or the URL is not set.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** The `fetch_gpt_key` function is designed to retrieve a user's GPT API key from a database. It takes a username as input and queries a `dbusers` collection to find a matching user document. If a user is found, the function extracts the `gpt_api_key` field from that document. It returns the API key if present, or `None` if the user is not found or the key is missing.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which corresponds to the `_id` field in the database.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the provided username, or None if the user is not found or the key does not exist.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** This function is designed to retrieve a user's 'opensrc_api_key' from a database. It takes a username as input and queries the 'dbusers' collection. The function specifically looks for a document where the '_id' matches the provided username and projects only the 'opensrc_api_key' field. If a user document is found, it returns the associated API key; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source API key is to be fetched.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key associated with the given username, or None if the user is not found or the key does not exist.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** This function is designed to retrieve the 'opensrc_base_url' for a specific user from a database. It queries the 'dbusers' collection, using the provided username as the document's '_id'. The query is optimized to return only the 'opensrc_base_url' field. If a matching user document is found, the function extracts and returns the value of this URL. If no user is found with the given username, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose opensrc base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The opensrc base URL associated with the user, or None if the user is not found or the 'opensrc_base_url' field is not present.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is responsible for removing a user record from the `dbusers` collection. It takes a username as input and attempts to delete the document where the `_id` field matches the given username. The function then returns the number of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted from the database, typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys and base URLs for a specified user from a database. It first attempts to find the user by their username. If the user is not found, it returns a tuple of None values. Otherwise, it fetches the Gemini, GPT, and open-source API keys, decrypting them using a 'decrypt_text' utility, and also retrieves the Ollama and open-source base URLs. Finally, it returns all five values.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user is not found or the key is not present.
    - **ollama_plain** (`str | None`): The Ollama base URL, or None if the user is not found or the URL is not present.
    - **gpt_plain** (`str | None`): The decrypted GPT API key, or None if the user is not found or the key is not present.
    - **opensrc_plain** (`str | None`): The decrypted open-source API key, or None if the user is not found or the key is not present.
    - **opensrc_url** (`str | None`): The open-source base URL, or None if the user is not found or the URL is not present.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** This function is responsible for creating a new chat entry within a database. It generates a unique identifier for the chat using the `uuid` module and records the current timestamp. The function then constructs a dictionary containing this unique ID, the provided username, the chat's name, and the creation timestamp. This dictionary is subsequently inserted into the `dbchats` collection, likely a MongoDB collection, and the unique `_id` of the newly inserted document is returned.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (`_id`) of the newly created chat document in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** This function, `fetch_chats_by_user`, is designed to retrieve all chat documents associated with a specific user from a database. It queries a collection, presumably `dbchats`, for entries where the 'username' field matches the provided input. The results are then sorted chronologically by their 'created_at' timestamp in ascending order. Finally, the function returns the collection of matching chat documents as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat documents.
*   **Returns:**
    - **chats** (`list`): A list of chat documents associated with the specified username, sorted by creation date.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function verifies the existence of a specific chat entry within the 'dbchats' collection. It takes a username and a chat name as input, constructs a query, and uses 'dbchats.find_one' to search for a matching document. The function returns 'True' if a matching chat is found, indicating its existence, and 'False' otherwise.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked.
*   **Returns:**
    - **chat_exists** (`bool`): True if a chat matching the provided username and chat name exists in the 'dbchats' collection, False otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and all its associated exchanges (messages) within the database. It first updates a single chat entry in the 'dbchats' collection, changing its name from 'old_name' to 'new_name' for a specific 'username'. Subsequently, it updates all related exchange entries in the 'dbexchanges' collection, ensuring their 'chat_name' also reflects the 'new_name'. The function returns the count of documents modified by the initial chat renaming operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The desired new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified in the 'dbchats' collection by the chat renaming operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str, json_tokens: int, toon_tokens: int, savings_percent: float)`
*   **Description:** This function inserts a new exchange record into a database collection. It first generates a unique identifier using UUID, then constructs a dictionary containing various details such as the question, answer, feedback, user information, performance metrics, and a creation timestamp. Finally, it attempts to insert this structured data into the 'dbexchanges' collection. If the insertion is successful, the function returns the unique ID of the new record; otherwise, it catches any exceptions, prints an error message, and returns None.
*   **Parameters:**
    - **question** (`str`): The question string from the exchange.
    - **answer** (`str`): The answer string provided in the exchange.
    - **feedback** (`str`): The feedback string associated with the exchange.
    - **username** (`str`): The username of the participant in the exchange.
    - **chat_name** (`str`): The name of the chat where the exchange took place.
    - **helper_used** (`str`): Optional. Indicates which helper model was utilized, defaults to an empty string.
    - **main_used** (`str`): Optional. Indicates which main model was utilized, defaults to an empty string.
    - **total_time** (`str`): Optional. The total time taken for the exchange, defaults to an empty string.
    - **helper_time** (`str`): Optional. The time taken by the helper model, defaults to an empty string.
    - **main_time** (`str`): Optional. The time taken by the main model, defaults to an empty string.
    - **json_tokens** (`int`): Optional. The number of JSON tokens used, defaults to 0.
    - **toon_tokens** (`int`): Optional. The number of 'toon' tokens used, defaults to 0.
    - **savings_percent** (`float`): Optional. The percentage of savings achieved, defaults to 0.0.
*   **Returns:**
    - **new_id** (`str | None`): The unique ID of the newly inserted exchange record if successful, or None if an error occurs during insertion.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records associated with a specific username from a database collection named `dbexchanges`. It queries the database using the provided username, sorts the results by their creation timestamp in ascending order, and then returns the collection of matching exchanges as a list. The sorting is explicitly noted as important for display purposes.
*   **Parameters:**
    - **username** (`str`): The username used to filter and retrieve relevant exchange records from the database.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (documents) associated with the specified username, sorted by their creation timestamp.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function is designed to retrieve a list of exchange records from a database collection named `dbexchanges`. It filters these records based on a specific `username` and `chat_name` provided as arguments. The retrieved exchanges are then sorted in ascending order by their `created_at` timestamp before being returned as a list.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchange records.
    - **chat_name** (`str`): The name of the chat used to filter the exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents (dictionaries) that match the specified username and chat name, sorted by their creation timestamp.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function updates the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function uses a database object, likely a MongoDB collection, to perform an update operation. It targets the document matching the provided exchange ID and sets its 'feedback' field to the new value. The function then returns the count of documents that were successfully modified.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange record to be updated.
    - **feedback** (`int`): The integer value representing the feedback to be set for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates a specific exchange record in the database by its unique identifier. It takes an exchange ID and a new feedback message string. The function uses the `dbexchanges.update_one` method to locate the document matching the provided `exchange_id` and then sets its `feedback_message` field to the new value. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange document to be updated in the database.
    - **feedback_message** (`str`): The new feedback message string to be stored for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is responsible for deleting a specific exchange record from the 'dbexchanges' collection. It takes a unique identifier for the exchange as input. The function executes a delete operation based on this ID and reports the number of documents that were removed. It is designed to remove a single document matching the provided ID.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier ('_id') of the exchange record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The count of documents successfully deleted. This will typically be 1 if a matching record was found and deleted, or 0 if no record matched the given ID.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is designed to completely remove a specific chat and all its associated messages (exchanges) from the database. It first deletes all exchange documents linked to the given username and chat name, then proceeds to delete the chat document itself. This two-step process ensures data consistency between frontend and backend representations. The function returns the count of chat documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted by the operation (typically 0 or 1).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list: List[str])`
*   **Description:** The `clean_names` function processes a list of strings, where each string is expected to potentially contain path-like delimiters. It iterates through the provided `model_list` and for each string, it splits the string by the '/' character. The function then extracts the last segment from the resulting split parts. Finally, it returns a new list containing these extracted last segments, effectively 'cleaning' the names by removing any preceding path information.
*   **Parameters:**
    - **model_list** (`List[str]`): A list of strings, where each string may represent a path or a name containing '/' delimiters that need to be removed.
*   **Returns:**
    - **cleaned_names** (`List[str]`): A new list of strings, where each string is the last segment of the corresponding input string after splitting by '/'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list: list, category_name: str)`
*   **Description:** This function filters a given list of models based on a specified category name. It retrieves a set of keywords associated with the category from a global `CATEGORY_KEYWORDS` dictionary. If the category's keywords include "STANDARD", the function returns only those models from the input list that are also present in a `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list` and collects models whose names (case-insensitively) contain any of the retrieved keywords. If no models match the keywords, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The initial list of models to be filtered.
    - **category_name** (`str`): The name of the category used to determine the filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered according to the specified category keywords, or the original `source_list` if no models match the keywords or if the 'STANDARD' category logic is applied.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function is designed to save a new Gemini API key. It retrieves the potential new key from the Streamlit session state. If a new key is present, it updates the Gemini key in the database for the current user, clears the key from the session state, and displays a success toast notification to the user.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function, `save_ollama_cb`, acts as a callback to persist a user-defined Ollama URL. It retrieves the potential new URL from the Streamlit session state, specifically from the key "in_ollama_url". If a valid, non-empty URL is found, it proceeds to update this URL in the database for the current user, whose username is also obtained from the session state. Upon successful update, a confirmation toast message is displayed to the user.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** The load_data_from_db function is designed to load chat and exchange data for a specified user into the Streamlit session state. It first checks if the user's data is already loaded to prevent redundant operations. If not, it initializes the chat structure, then fetches existing chats and exchanges from the database. It organizes these exchanges within their respective chats, handling cases for unassigned exchanges and default feedback values. Finally, it ensures a default chat exists if the user has no chats and sets the active_chat in the session state.
*   **Parameters:**
    - **username** (`str`): The username for whom chat and exchange data should be loaded.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: dict, val: Any)`
*   **Description:** This function processes a change in feedback for a specific exchange record. It updates the 'feedback' key within the provided 'ex' dictionary with the new 'val'. Concurrently, it calls a database utility to persist this feedback change using the '_id' from the 'ex' object. Finally, it triggers a rerun of the Streamlit application, likely to refresh the user interface.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing an exchange or data record, expected to contain 'feedback' and '_id' keys.
    - **val** (`Any`): The new feedback value to be assigned to the exchange record.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: str, ex: dict)`
*   **Description:** This function handles the deletion of a specific chat exchange. It first removes the exchange from the database using its `_id`. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if so, removes the exchange from that chat's list of exchanges. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be deleted.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' key for database deletion and to be present in the session state's exchanges list.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** This function handles the deletion of a specified chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the chat from the Streamlit session state. If other chats exist, the first available chat becomes the active one; otherwise, a new default chat named "Chat 1" is created, inserted into the database via `db.insert_chat`, and set as the active chat. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted or created.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text: str)`
*   **Description:** This function is designed to extract a repository name from a given input text. It first attempts to find a URL within the text using a regular expression. If a URL is identified, it then parses the URL to isolate the path component. From this path, the function extracts the last segment, which is assumed to be the repository name. It also handles cases where the repository name ends with '.git', removing the suffix for a cleaner name. If no URL is found or a repository name cannot be successfully extracted, the function returns None.
*   **Parameters:**
    - **text** (`str`): The input string from which to extract a repository name, potentially containing a URL.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string, or None if no valid repository name could be found within the text.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text: str)`
*   **Description:** This function acts as a generator that streams an input string word by word. It takes a complete text string, splits it into individual words, and then yields each word followed by a space. A small delay of 0.01 seconds is introduced between yielding each word, simulating a gradual text display or streaming effect.
*   **Parameters:**
    - **text** (`str`): The input string to be processed and streamed word by word.
*   **Returns:**
    - **word_with_space** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str, should_stream: bool)`
*   **Description:** This function processes a given markdown string, identifying and specially handling embedded Mermaid diagram blocks. It splits the input text into parts, rendering standard markdown sections using `st.markdown` (with an option to stream via `st.write_stream` if `should_stream` is true). For sections identified as Mermaid diagrams, it attempts to render them using `st_mermaid`. If the Mermaid rendering fails, it displays the Mermaid code as a plain code block using `st.code`.
*   **Parameters:**
    - **markdown_text** (`str`): The input string containing markdown content, potentially with embedded Mermaid diagram blocks.
    - **should_stream** (`bool`): A flag indicating whether non-Mermaid markdown parts should be streamed when rendered. Defaults to `False`.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** This function `render_exchange` is responsible for rendering a single chat exchange (user question and assistant answer) within a Streamlit application. It displays the user's question, then the assistant's answer within a dedicated chat message container. The function includes a toolbar with interactive elements such as feedback buttons (like/dislike), a popover for adding notes, a download button for the answer, and a delete button for the exchange. It also handles error states for the assistant's answer and provides specific UI elements for them. The function relies heavily on Streamlit components for its user interface.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing a single chat exchange, containing keys like 'question', 'answer', 'feedback', 'feedback_message', and '_id'.
    - **current_chat_name** (`str`): The name of the current chat, used for handling exchange deletion.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by other functions in the provided context.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to encapsulate the essential details of a single function parameter. It provides a structured format for defining a parameter's name, its data type, and a concise textual description of its role or purpose. This model is typically used within larger schemas to describe the parameters of a function or method in a standardized way.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly depend on other components beyond its Pydantic BaseModel inheritance.
*   **Constructor:**
    *   *Description:* This class, inheriting from pydantic.BaseModel, implicitly generates a constructor. It initializes an instance with 'name', 'type', and 'description' attributes, which are validated according to their type hints upon instantiation.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The data type of the parameter.
        - **description** (`str`): A textual description of the parameter's purpose.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to standardize the description of a function's return value. It encapsulates three key pieces of information: the name of the return value, its Python type, and a detailed textual description. This class serves as a structured data container for metadata about function outputs, facilitating consistent documentation or programmatic analysis.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the __init__ method is automatically generated. It initializes an instance of ReturnDescription by accepting 'name', 'type', and 'description' as keyword arguments, validating their types according to the schema, and assigning them as instance attributes.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The Python type hint or a string representation of the return value's type.
        - **description** (`str`): A detailed explanation of what the return value represents or its purpose.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about the calling context of a function or method. It provides a structured format to describe what external entities a function calls and by which entities it is called, using two string attributes for this purpose.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class relies on the Pydantic BaseModel for its structure and validation capabilities. It does not explicitly list any other external functional dependencies.
*   **Constructor:**
    *   *Description:* The UsageContext class is initialized by accepting two string arguments, 'calls' and 'called_by'. These parameters are directly assigned to instance attributes, with Pydantic handling the validation and type enforcement during object creation.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions, methods, or classes that this entity calls.
        - **called_by** (`str`): A string describing the functions or methods that call this entity.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to provide a structured, machine-readable representation of a function's detailed analysis. It encapsulates information about the function's high-level purpose, its input parameters, its return values, and its usage context within a larger system. This class serves as a schema for describing functions comprehensively.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The FunctionDescription class is initialized by providing values for its Pydantic fields: 'overall', 'parameters', 'returns', and 'usage_context'. These fields are used to construct a structured description of a function, ensuring all necessary analytical components are present.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the function's purpose and implementation.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each describing a single parameter of the function, including its name, type, and purpose.
        - **returns** (`List[ReturnDescription]`): A list of objects, each describing a return value of the function, including its name, type, and description.
        - **usage_context** (`UsageContext`): An object describing the function's calling context, specifically what other functions or classes it calls and where it is called from.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to represent a comprehensive analysis of a Python function in a structured JSON format. It serves as the top-level schema for capturing a function's identity, its detailed description including purpose and signature, and any potential errors encountered during its analysis. This model ensures a standardized and machine-readable representation of function metadata.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, inheriting from Pydantic's BaseModel, implicitly generates an `__init__` method. This constructor is responsible for initializing instances of FunctionAnalysis by accepting values for `identifier`, `description`, and an optional `error` field, setting them as instance attributes.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifying the function being analyzed.
        - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional string field to capture any error messages or issues encountered during the function's analysis. Defaults to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to structure information about a class's `__init__` method. It serves as a data container, holding a textual summary of the constructor's purpose and a list of its individual parameters. This model is used to provide a standardized, machine-readable description of how a class is initialized within a larger system.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel. Its `__init__` method is implicitly generated by Pydantic, which constructs instances by validating and assigning values to the `description` and `parameters` fields based on their type hints.
    *   *Parameters:*
        - **description** (`str`): A textual summary of the constructor's purpose.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each describing a parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's operational context. It specifically tracks external dependencies and the locations where the class is instantiated. This model serves as a structured data container, ensuring consistent representation of these contextual details for further analysis or documentation generation.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. Initialization is handled implicitly by Pydantic's BaseModel, which constructs instances based on the `dependencies` and `instantiated_by` fields provided as keyword arguments.
    *   *Parameters:*
        - **dependencies** (`str`): A string summarizing the external dependencies of the class.
        - **instantiated_by** (`str`): A string summarizing where the class is instantiated.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The `ClassDescription` class is a Pydantic BaseModel designed to serve as a comprehensive schema for representing the detailed analysis of a Python class. It encapsulates various aspects of a class, including its high-level purpose, the specifics of its constructor, a list of analyses for all its methods, and its broader usage context within a system. This model is crucial for structuring the output of an AI code analysis process.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, `ClassDescription` implicitly generates its `__init__` method based on the defined fields. This constructor is responsible for validating and assigning values to `overall`, `init_method`, `methods`, and `usage_context` upon instantiation, ensuring that the object conforms to the specified schema.
    *   *Parameters:*
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The `ClassAnalysis` class serves as a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds the class's unique identifier, a detailed `ClassDescription` object containing its constructor and method analyses, and an optional field to report any errors encountered during the analysis process. This model provides a structured representation for machine-readable class metadata.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. Pydantic's `BaseModel` handles the initialization of its fields automatically based on the provided arguments, ensuring type validation and assignment for `identifier`, `description`, and `error`.
    *   *Parameters:*
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The `CallInfo` class is a Pydantic BaseModel designed to represent a specific call event within a system, typically used by a relationship analyzer. It encapsulates essential information about a call, including the file, function name, mode (e.g., method, function, module), and line number where the call originated. This structure facilitates consistent data representation for tracking call relationships.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly depend on other components within the provided context, but it inherits from `pydantic.BaseModel` for its data modeling capabilities.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `CallInfo` class implicitly generates an `__init__` method. This constructor allows for the creation of `CallInfo` instances by directly passing keyword arguments corresponding to its defined fields: `file`, `function`, `mode`, and `line`. Pydantic handles validation and assignment of these attributes upon instantiation.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that made the call.
        - **mode** (`str`): The type of the calling entity, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the file where the call event occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to encapsulate structured context information relevant to the analysis of a specific function. It serves as a data container, defining the expected structure for inputs related to function call graphs. The class explicitly defines two fields: 'calls', which is a list of strings representing functions or methods called by the target function, and 'called_by', which is a list of CallInfo objects indicating where the target function itself is invoked.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class does not define an explicit `__init__` method. Initialization is handled implicitly by Pydantic's `BaseModel`, which constructs instances based on the provided `calls` and `called_by` attributes, validating their types according to the defined annotations.
    *   *Parameters:*
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The `FunctionAnalysisInput` class serves as a Pydantic model, defining the structured input required to initiate a function analysis process. It acts as a data transfer object (DTO) that encapsulates all necessary information, such as the operational mode, the function's identifier, its source code, associated import statements, and additional contextual data. This class ensures that all inputs conform to a predefined schema, facilitating reliable data handling for subsequent analysis.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `FunctionAnalysisInput` is implicitly generated by Pydantic's `BaseModel`. It handles the automatic validation and assignment of instance attributes based on the type hints provided in the class definition, ensuring that all required fields are present and correctly typed upon instantiation.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the operational mode, which is fixed to 'function_analysis' for this input schema.
        - **identifier** (`str`): The unique name or identifier of the function targeted for analysis.
        - **source_code** (`str`): The raw source code of the function to be analyzed.
        - **imports** (`List[str]`): A list of import statements relevant to the function's execution context.
        - **context** (`FunctionContextInput`): Additional contextual information pertinent to the function's analysis, structured by `FunctionContextInput`.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to provide a structured representation of contextual information for a method. It encapsulates details such as the method's unique identifier, a list of other functions or methods it calls, where it is called from, its arguments, and its docstring. This model serves as a data schema for collecting and organizing metadata about individual methods, likely for analysis or documentation generation in a larger system.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `MethodContextInput` is implicitly generated by Pydantic. It allows for the creation of instances by accepting keyword arguments that directly correspond to the class's defined fields, ensuring data validation and type enforcement upon instantiation.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where this method is called from.
        - **args** (`List[str]`): A list of argument names accepted by the method.
        - **docstring** (`Optional[str]`): The docstring of the method, if available.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured context information necessary for analyzing a Python class. It serves as a data schema for collecting details such as external dependencies, where the class is instantiated, and specific context for each of its methods. This model provides a standardized format for inputting comprehensive contextual data into an analysis system.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not explicitly declare external functional dependencies within its definition.
*   **Constructor:**
    *   *Description:* The class is initialized by Pydantic's BaseModel constructor, which automatically handles the assignment of its declared fields: 'dependencies', 'instantiated_by', and 'method_context'. These fields are validated upon instantiation according to their type hints.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external functional dependencies of the class.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing context for a specific method within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a data schema, ensuring that all necessary components like the operation mode, class identifier, source code, imports, and contextual information are provided in a validated format for subsequent analysis. This class acts as a contract for the data payload used by the class analysis system.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class ClassAnalysisInput does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class inherits from Pydantic's BaseModel and does not explicitly define an __init__ method. Pydantic automatically generates a constructor that validates and initializes instances based on the type-hinted fields: mode, identifier, source_code, imports, and context.
    *   *Parameters:*
        - **mode** (`Literal['class_analysis']`): Specifies the operation mode, fixed to 'class_analysis'.
        - **identifier** (`str`): The unique name or identifier of the class to be analyzed.
        - **source_code** (`str`): The raw source code of the entire class definition.
        - **imports** (`List[str]`): A list of import statements relevant to the source file.
        - **context** (`ClassContextInput`): Additional contextual information for the class analysis.
*   **Methods:**

---
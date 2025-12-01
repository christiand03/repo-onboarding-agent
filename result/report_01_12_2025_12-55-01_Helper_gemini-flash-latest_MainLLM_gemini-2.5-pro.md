# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated documentation agent designed to analyze Python-based Git repositories. It clones a given repository, performs static code analysis by building an Abstract Syntax Tree (AST) and a call graph, and then leverages Large Language Models (LLMs) to generate detailed, human-readable documentation for each class and function. The final report is presented through an interactive web interface.
- **Key Features:**
  - Clones public Git repositories for analysis.
  - Performs static code analysis using Abstract Syntax Trees (ASTs).
  - Generates call graphs to map function and method relationships.
  - Utilizes LLMs (e.g., Gemini, GPT, Ollama) for intelligent code description generation.
  - Provides an interactive Streamlit-based web frontend for user interaction and report viewing.
- **Tech Stack:** Python, Streamlit, Langchain, NetworkX, GitPython, Pydantic.

*   **Repository Structure:**
    ```mermaid
    graph TD
    subgraph root
        direction LR
        root_files[".env.example<br/>.gitignore<br/>analysis_output.json<br/>readme.md<br/>requirements.txt"]
    end
    root --> SystemPrompts
    subgraph SystemPrompts
        direction LR
        SystemPrompts_files["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt"]
    end
    root --> backend
    subgraph backend
        direction LR
        backend_files["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py"]
    end
    root --> database
    subgraph database
        direction LR
        database_files["db.py"]
    end
    root --> frontend
    subgraph frontend
        direction LR
        frontend_files["Frontend.py<br/>__init__.py"]
    end
    frontend --> gifs
    subgraph gifs
        direction LR
        gifs_files["4j.gif"]
    end
    root --> notizen
    subgraph notizen
        direction LR
        notizen_files["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
    end
    notizen --> grafiken
    subgraph grafiken
        direction LR
        grafiken_files["File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
    end
    grafiken --> Flask-Repo
    subgraph Flask-Repo
        direction LR
        Flask-Repo_files["__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot"]
    end
    grafiken --> Repo-onboarding
    subgraph Repo-onboarding
        direction LR
        Repo-onboarding_files["AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot"]
    end
    root --> result
    subgraph result
        direction LR
        result_files["report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
    end
    root --> schemas
    subgraph schemas
        direction LR
        schemas_files["types.py"]
    end
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
- cryptography==46.0.3
- dnspython==2.8.0
- dotenv==0.9.9
- entrypoints==0.4
- extra-streamlit-components==0.1.81
- filetype==1.2.0
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
- jsonpatch==1.33
- jsonpointer==3.0.0
- jsonschema==4.25.1
- jsonschema-specifications==2025.9.1
- langchain==1.0.8
- langchain-core==1.1.0
- langchain-google-genai==3.1.0
- langchain-ollama==1.0.0
- langgraph==1.0.3
- langgraph-checkpoint==3.0.1
- langgraph-prebuilt==1.0.5
- langgraph-sdk==0.2.9
- langsmith==0.4.46
- MarkupSafe==3.0.3
- narwhals==2.12.0
- networkx==3.6
- numpy==2.3.5
- ollama==0.6.1
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
- python-dateutil==2.9.0.post0
- python-dotenv==1.2.1
- pytz==2025.2
- PyYAML==6.0.3
- referencing==0.37.0
- requests==2.32.5
- requests-toolbelt==1.0.0
- rpds-py==0.29.0
- rsa==4.9.1
- six==1.17.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.51.0
- streamlit-authenticator==0.4.2
- streamlit-mermaid==0.3.0
- tenacity==9.1.2
- toml==0.10.2
- toolz==1.1.0
- toon_format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c90006de6
- tornado==6.5.2
- typing-inspection==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0

Since a `requirements.txt` file is present, you can install all dependencies with a single command:
```bash
pip install -r requirements.txt
```
### Setup Guide
Information not found
### Quick Startup
Information not found

    ## 3. Use Cases & Commands
The primary use case is to provide developers with a comprehensive, auto-generated documentation suite for an existing Python codebase. By simply inputting a Git repository URL into the web interface, a user can receive a detailed breakdown of the project's structure, architecture, and code components, significantly speeding up the onboarding and code comprehension process.

The application is run as a web service. To start the frontend, execute the following command from the project's root directory:
```bash
streamlit run frontend/Frontend.py
```

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added


## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is a specialized implementation of ast.NodeVisitor designed to traverse a Python Abstract Syntax Tree (AST) and generate a structured schema of the file's contents. It collects metadata on imports, standalone functions, and classes, including source code segments, line numbers, and docstrings. It maintains state using self._current_class to correctly associate methods with their parent class during traversal, ensuring a hierarchical representation of the code structure is built in the self.schema attribute.
*   **Instantiation:** This class is instantiated by the analyze_repository function within the AST_Schema.py file, suggesting it is a core component of a larger code analysis pipeline.
*   **Dependencies:** The class relies on the path_to_module function (likely imported or defined elsewhere) to determine the fully qualified module path for identifiers.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with necessary context information, including the raw source code, the file location, and the project root directory. It calculates the module path using an external function (path_to_module) and sets up the internal self.schema dictionary, which will store the extracted metadata (imports, functions, classes), and initializes self._current_class to track context during nested traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the file being analyzed.
        - **project_root** (`str`): The root directory of the entire project, used for calculating relative module paths.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code, file_path, project_root)`
        *   *Description:* The constructor initializes the visitor with necessary context information, including the raw source code, the file location, and the project root directory. It calculates the module path using an external function (path_to_module) and sets up the internal self.schema dictionary, which will store the extracted metadata (imports, functions, classes), and initializes self._current_class to track context during nested traversal.
        *   *Parameters:*
            - **source_code** (`str`): The raw source code of the file being analyzed.
            - **file_path** (`str`): The absolute path to the file being analyzed.
            - **project_root** (`str`): The root directory of the entire project, used for calculating relative module paths.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method handles ast.Import nodes (e.g., `import X, Y`). It iterates through all imported names (aliases) within the node and appends the raw import name to the `imports` list within the internal `self.schema`. Finally, it calls `self.generic_visit(node)` to continue the traversal of any nested nodes, adhering to the standard ast.NodeVisitor pattern.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles ast.ImportFrom nodes (e.g., `from module import name`). It iterates through the imported names and constructs a fully qualified import string by combining the module name with the specific imported name. This qualified name is then appended to the imports list in self.schema. It concludes by calling self.generic_visit(node) to ensure deep traversal continues.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from X import Y' statement.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method processes ast.ClassDef nodes, extracting comprehensive metadata about the defined class. It constructs a unique identifier, gathers information like the class name, docstring, source code segment, and line numbers, and appends this structured information to the classes list in self.schema. Crucially, it sets self._current_class to the newly created class context before calling generic_visit, allowing nested function definitions (methods) to be correctly associated with this class, and then resets the state afterwards.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles standard function definitions (ast.FunctionDef). It determines whether the function is a standalone function or a method nested within a class by checking the state of self._current_class. If it is a method, it extracts basic context and appends this context to the method_context list of the current class. If it is a standalone function, it extracts comprehensive information and appends it to the functions list in self.schema. In both cases, it ensures traversal continues via self.generic_visit(node).
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method handles asynchronous function definitions (ast.AsyncFunctionDef). Its implementation is a simple delegation, calling self.visit_FunctionDef(node) to treat asynchronous functions identically to synchronous functions for the purpose of metadata extraction and schema population.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
            *Analysis data not available for this component.*

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to perform comprehensive static analysis on a collection of Python source code files, typically representing a repository. It orchestrates the process of parsing files into Abstract Syntax Trees (ASTs), extracting structured schema information (functions, classes, imports) using an ASTVisitor, and integrating dynamic context by generating and applying a call graph. Its core function is to iterate over input files, handle path resolution, perform parsing, and aggregate the resulting file schemas into a single, detailed dictionary structure, ensuring that all defined functions and methods are enriched with their respective callers and callees.
*   **Instantiation:** This class is instantiated by the function main_workflow located in main.py.
*   **Dependencies:** The class relies on external modules like ast for parsing, networkx (nx) for graph manipulation, os for path handling, and the custom function build_callGraph for call graph generation.
*   **Constructor:**
    *   *Description:* The constructor is empty and does not initialize any instance attributes, serving only to define the class structure.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* The constructor is empty and does not initialize any instance attributes, serving only to define the class structure.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* This static method integrates call graph information into a pre-existing schema dictionary generated by an AST visitor. It iterates through both standalone functions and class methods defined within the schema. For each function or method, it constructs a unique identifier key using the filename and function/method name. If this key exists in the provided NetworkX directed graph (`call_graph`), it extracts the successors (calls) and predecessors (called by) and updates the corresponding 'calls' and 'called_by' fields within the schema dictionary in place.
        *   *Parameters:*
            - **schema** (`dict`): The schema dictionary containing function and class definitions to be enriched.
            - **call_graph** (`nx.DiGraph`): The NetworkX directed graph representing the call relationships within the file.
            - **filename** (`str`): The name of the file being processed, used for constructing unique keys.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files)`
        *   *Description:* This method is the primary entry point for analyzing a repository, processing a list of file objects to generate a comprehensive AST and call graph schema. It first determines the common project root path for context. It then iterates through each Python file, parses its content into an AST, and uses an ASTVisitor to extract structural schema nodes. Subsequently, it builds a call graph for the file and uses the internal _enrich_schema_with_callgraph method to integrate call context into the schema before aggregating the results into a final dictionary structure.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary containing the structured AST and call graph analysis for all processed files under the key 'files'.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a file system path into a standard Python module path string. It first attempts to calculate the path relative to the provided project root using `os.path.relpath`. If a `ValueError` occurs during this calculation, it defaults to using only the file's basename. The function then strips the trailing '.py' extension if present and replaces all system path separators with dots to form the module path. Finally, it checks if the path represents a package initialization file (ending in '.__init__') and removes that suffix if found, returning the package name.
*   **Parameters:**
    - **filepath** (`string`): The full path to the file that needs to be converted into a module path.
    - **project_root** (`string`): The root directory of the project, used as the base for calculating the relative module path.
*   **Returns:**
    - **module_path** (`string`): The resulting Python module path string (e.g., 'package.subpackage.module').
*   **Usage:**
    *   Calls: `basename`, `endswith`, `relpath`, `replace`
    *   Called by: `__init__` in `AST_Schema.py`

---
### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is an AST NodeVisitor designed to analyze Python source code and construct a map of file-level dependencies based on import statements. It maintains the `import_dependencies` dictionary, which tracks which modules the current file depends on. Its primary responsibility is to correctly handle both standard imports and complex relative imports, utilizing the repository root path to resolve module names and ensure accurate dependency mapping. This class is fundamental for generating a comprehensive file dependency graph for a codebase.
*   **Instantiation:** This class is instantiated by the `build_file_dependency_graph` function within the `File_Dependency.py` module.
*   **Dependencies:** The class relies heavily on the `ast` module for traversal and parsing, `pathlib.Path` for file system operations, and external utilities like `get_all_temp_files` for repository file listing.
*   **Constructor:**
    *   *Description:* The constructor initializes the dependency graph visitor by storing the path of the file currently being analyzed (`filename`) and the root path of the repository (`repo_root`). These attributes are essential for resolving relative imports and locating files within the repository structure during the AST traversal.
    *   *Parameters:*
        - **filename** (`str`): The name or path of the file whose dependencies are currently being analyzed.
        - **repo_root** (`Any`): The root directory path of the source code repository, used for resolving file paths.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename, repo_root)`
        *   *Description:* The constructor initializes the dependency graph visitor by storing the path of the file currently being analyzed (`filename`) and the root path of the repository (`repo_root`). These attributes are essential for resolving relative imports and locating files within the repository structure during the AST traversal.
        *   *Parameters:*
            - **filename** (`str`): The name or path of the file whose dependencies are currently being analyzed.
            - **repo_root** (`Any`): The root directory path of the source code repository, used for resolving file paths.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This private method handles the complex task of resolving relative imports, such as `from .. import name`. It first determines the correct base directory by navigating up the file path based on the import level specified in the AST node. It then checks if the imported names exist either as module files (`.py`) or as symbols explicitly exported by a package's `__init__.py` file (checking `__all__` or definitions). If no matching module or symbol can be found after path resolution, it raises an ImportError.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the relative 'from ... import ...' statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of successfully resolved module or symbol names.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method is the handler for standard `ast.Import` nodes, but is also used internally by `visit_ImportFrom`. It iterates over all imported aliases within the node and records the dependency in the `self.import_dependencies` dictionary, mapping the current file (`self.filename`) to the imported module name (either `alias.name` or the provided `base_name`). After recording, it ensures the AST traversal continues by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing the import statement being visited.
            - **base_name** (`str | None`): An optional base name for the module, typically provided by `visit_ImportFrom` for absolute imports.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `ast.ImportFrom` nodes, handling both absolute and relative imports. For absolute imports (e.g., `from a.b.c import d`), it extracts the base module name 'c' and delegates the dependency recording to `visit_Import`. For relative imports (indicated by a null module name or leading dots), it calls `_resolve_module_name` to determine the actual module paths. If resolution fails, it prints an error; otherwise, it calls `visit_Import` for each resolved module. Finally, it ensures the AST traversal continues via `self.generic_visit(node)`.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            *Analysis data not available for this component.*

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function is responsible for constructing a directed graph that maps out the file-level import dependencies for a specific Python file. It initializes a NetworkX directed graph (nx.DiGraph) and utilizes a custom AST visitor, `FileDependencyGraph`, to traverse the provided Abstract Syntax Tree (AST). The visitor collects import relationships, which are then iterated over. For every dependency found, the function adds the caller and callee files as nodes and establishes a directed edge representing the import relationship in the graph.
*   **Parameters:**
    - **filename** (`str`): The name or path of the file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) object representing the source code of the file.
    - **repo_root** (`str`): The root directory path of the repository, used for resolving file paths and imports.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes are file paths and edges represent import dependencies.
*   **Usage:**
    *   Calls: `DiGraph`, `FileDependencyGraph`, `add_edge`, `add_node`, `add_nodes_from`, `items`, `visit`
    *   Called by: `build_repository_graph` in `File_Dependency.py`

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function analyzes a Git repository to construct a comprehensive directed graph of dependencies between its Python files. It iterates through all files provided by the repository object, filtering specifically for Python source files. For each Python file, it parses the content into an Abstract Syntax Tree (AST) and delegates the dependency extraction to the `build_file_dependency_graph` function. The resulting nodes and edges from these file-specific graphs are then aggregated into a single, repository-wide NetworkX directed graph, which represents the overall call and dependency structure.
*   **Parameters:**
    - **repository** (`GitRepository`): An object representing the Git repository whose files and dependencies are to be analyzed, providing access to file content and the root directory.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependency relationships (nodes and edges) found across all Python files in the repository.
*   **Usage:**
    *   Calls: `DiGraph`, `add_edge`, `add_node`, `basename`, `build_file_dependency_graph`, `endswith`, `get_all_files`, `parse`, `removesuffix`, `str`
    *   Called by: `backend.File_Dependency` in `File_Dependency.py`

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function is designed to locate all Python source files within a specified directory and its subdirectories. It converts the input directory string into an absolute pathlib.Path object using `resolve()`. It then recursively searches for all files matching the pattern `*.py` using `rglob()`. The function returns a list containing the paths of these files, with each path expressed relative to the initial root directory.
*   **Parameters:**
    - **directory** (`str`): The string path of the root directory to search recursively for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of pathlib.Path objects, representing all found Python files relative to the input directory.
*   **Usage:**
    *   Calls: `Path`, `relative_to`, `resolve`, `rglob`
    *   Called by: `_resolve_module_name` in `File_Dependency.py`

#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G)`
*   **Description:** This function converts a NetworkX directed graph (nx.DiGraph), where nodes represent file paths, into a Mermaid graph syntax string. It first groups the file path nodes into folders using a defaultdict. It then generates the Mermaid syntax, defining the overall graph direction as 'TD' (Top Down). Crucially, it maps each folder to a Mermaid subgraph block, placing the corresponding files as nodes within that subgraph, while files in the root directory are placed directly in the main graph. Finally, it iterates over the graph edges to define the dependencies (connections) between the sanitized node IDs.
*   **Parameters:**
    - **G** (`nx.DiGraph`): The NetworkX directed graph representing file dependencies, where nodes are expected to be file paths (e.g., 'folder/file.py').
*   **Returns:**
    - **mermaid_syntax** (`str`): A string containing the complete Mermaid graph definition syntax, including subgraphs for folders and edges representing dependencies.
*   **Usage:**
    *   Calls: `append`, `defaultdict`, `items`, `join`, `replace`, `split`
    *   Called by: `backend.File_Dependency` in `File_Dependency.py`

---
### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as the primary interface for interacting with various Large Language Models (LLMs), such as Google Gemini, OpenAI, and Ollama, specifically for generating structured code documentation. It centralizes API configuration, handles model selection, loads specific system prompts for function and class analysis, and implements batch processing with rate-limiting logic. By utilizing LangChain's structured output feature with Pydantic schemas, it ensures that all generated documentation is reliably formatted as valid JSON.
*   **Instantiation:** This class is instantiated by the `main_orchestrator` function in `HelperLLM.py` and the `main_workflow` function in `main.py`.
*   **Dependencies:** The class relies heavily on LangChain components for LLM interaction, specifically `ChatGoogleGenerativeAI`, `ChatOllama`, and `ChatOpenAI`, along with `HumanMessage` and `SystemMessage`. It also uses standard modules like `json`, `logging`, and `time`, and custom Pydantic schemas (`FunctionAnalysis`, `ClassAnalysis`, etc.) for structured I/O.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by validating the API key, loading the necessary system prompts from file paths, and configuring the underlying language model based on the provided model name. It supports dynamic switching between Gemini, GPT, and Ollama providers. It also calls a private method to set the appropriate batch size and wraps the base LLM with structured output capabilities for both function and class analysis schemas.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service (e.g., Gemini or OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt text used when analyzing functions.
        - **class_prompt_path** (`str`): The file path to the system prompt text used when analyzing classes.
        - **model_name** (`str`): The identifier of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
        - **ollama_base_url** (`str | None`): The base URL for the Ollama service, which is used if an Ollama model is specified.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, function_prompt_path, class_prompt_path, model_name, ollama_base_url)`
        *   *Description:* The constructor initializes the LLMHelper by validating the API key, loading the necessary system prompts from file paths, and configuring the underlying language model based on the provided model name. It supports dynamic switching between Gemini, GPT, and Ollama providers. It also calls a private method to set the appropriate batch size and wraps the base LLM with structured output capabilities for both function and class analysis schemas.
        *   *Parameters:*
            - **api_key** (`str`): The API key required for authenticating with the chosen LLM service (e.g., Gemini or OpenAI).
            - **function_prompt_path** (`str`): The file path to the system prompt text used when analyzing functions.
            - **class_prompt_path** (`str`): The file path to the system prompt text used when analyzing classes.
            - **model_name** (`str`): The identifier of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
            - **ollama_base_url** (`str | None`): The base URL for the Ollama service, which is used if an Ollama model is specified.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private helper method is responsible for setting the optimal batch size for API calls based on the specific LLM model being used. It contains hardcoded batch size limits for various models (Gemini, Llama, GPT) to manage throughput and respect API rate limits effectively. If the provided model name is not recognized, it logs a warning and assigns a conservative default batch size of 2.
        *   *Parameters:*
            - **model_name** (`str`): The identifier of the language model for which the batch size needs to be configured.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method orchestrates the generation and validation of documentation for a batch of functions using the configured LLM. It converts the input models into JSON payloads, constructs the necessary conversation structure using system and human messages, and processes these requests in batches defined by `self.batch_size`. It includes robust error handling to log failures and maintain the input order by inserting `None` for failed items, and it enforces a 61-second pause between batches to comply with rate limits.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing the source code and context required for function analysis.
        *   *Returns:*
            - **all_validated_functions** (`List[Optional[FunctionAnalysis]]`): A list of validated FunctionAnalysis objects returned by the LLM, or None for any request that failed during batch processing.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method manages the batch generation and validation of documentation for classes. It converts `ClassAnalysisInput` objects into JSON payloads and prepares them for the LLM using the class-specific system prompt. It iterates through the inputs in batches, calls the `self.class_llm.batch` method, and handles exceptions by logging errors and padding the results with `None` to preserve order. A mandatory 61-second wait time is implemented between batches to respect external API rate limits.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing the source code and context required for class analysis.
        *   *Returns:*
            - **all_validated_classes** (`List[Optional[ClassAnalysis]]`): A list of validated ClassAnalysis objects returned by the LLM, or None for any request that failed during batch processing.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function acts as a self-contained test harness for the LLMHelper class, demonstrating its workflow using pre-defined mock data. It first constructs several input and output Pydantic models (FunctionAnalysisInput, FunctionAnalysis, ClassAnalysisInput) representing sample code analysis tasks. It then initializes the LLMHelper instance and executes the analysis generation process by calling `generate_for_functions`. Finally, it iterates through the results, logs the success of each analysis, aggregates the structured documentation into a dictionary, and prints the final result as a formatted JSON string.
*   **Parameters:**
    *Analysis data not available for this component.*
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `ClassAnalysisInput`, `ClassContextInput`, `LLMHelper`, `dumps`, `generate_for_functions`, `info`, `model_dump`, `model_validate`, `print`, `warning`
    *   Called by: `backend.HelperLLM` in `HelperLLM.py`

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the primary interface for interacting with various Language Models (LLMs), abstracting away the specifics of different providers like Google Gemini or local Ollama instances. It is responsible for initialization, which includes loading a mandatory system prompt from a file and configuring the appropriate LangChain chat model based on the specified model name and API key. The class provides two main methods for communication: call_llm for synchronous, single-response queries, and stream_llm for real-time, chunked responses, ensuring robust error handling for both modes of interaction.
*   **Instantiation:** This class is instantiated by the main_workflow function located in main.py.
*   **Dependencies:** The class relies on external libraries for its functionality, including logging for operational messages, and several components from LangChain such as ChatGoogleGenerativeAI, ChatOllama, HumanMessage, and SystemMessage to manage model interaction and message formatting.
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by setting up the underlying Language Model (LLM) client based on the provided model_name. It first validates the api_key and loads the system prompt from the specified file path, raising an error if the file is missing. Depending on whether the model is Gemini, GPT (using Google's wrapper), or an Ollama model, it instantiates either ChatGoogleGenerativeAI or ChatOllama with a fixed temperature of 1.0.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for accessing the LLM service (e.g., Gemini). Must be set, otherwise a ValueError is raised.
        - **prompt_file_path** (`str`): The path to the file containing the system prompt that guides the LLM's behavior.
        - **model_name** (`str`): The name of the model to use, defaulting to 'gemini-2.5-pro'. This determines which underlying LLM client (Google or Ollama) is initialized.
        - **ollama_base_url** (`str | None`): The base URL for the Ollama service, used only if an Ollama model is selected. Defaults to None, falling back to a global constant if necessary.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, prompt_file_path, model_name, ollama_base_url)`
        *   *Description:* The constructor initializes the MainLLM instance by setting up the underlying Language Model (LLM) client based on the provided model_name. It first validates the api_key and loads the system prompt from the specified file path, raising an error if the file is missing. Depending on whether the model is Gemini, GPT (using Google's wrapper), or an Ollama model, it instantiates either ChatGoogleGenerativeAI or ChatOllama with a fixed temperature of 1.0.
        *   *Parameters:*
            - **api_key** (`str`): The API key required for accessing the LLM service (e.g., Gemini). Must be set, otherwise a ValueError is raised.
            - **prompt_file_path** (`str`): The path to the file containing the system prompt that guides the LLM's behavior.
            - **model_name** (`str`): The name of the model to use, defaulting to 'gemini-2.5-pro'. This determines which underlying LLM client (Google or Ollama) is initialized.
            - **ollama_base_url** (`str | None`): The base URL for the Ollama service, used only if an Ollama model is selected. Defaults to None, falling back to a global constant if necessary.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method executes a synchronous, single-turn call to the initialized LLM. It constructs the message history using the stored system prompt and the provided user input, wrapping them in SystemMessage and HumanMessage objects, respectively. It then uses the self.llm.invoke() method to get the response. If the call is successful, it returns the text content of the response; otherwise, it logs the error and returns None.
        *   *Parameters:*
            - **user_input** (`str`): The specific input or query provided by the user to be processed by the LLM.
        *   *Returns:*
            - **content** (`str | None`): The text content generated by the LLM in response to the input, or None if an exception occurred during the API call.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method initiates a streaming call to the configured LLM, allowing the response to be processed chunk-by-chunk. Similar to call_llm, it prepares the messages using the system prompt and user input. It utilizes the self.llm.stream() method, which returns an iterator. The method yields the content of each chunk received from the stream. If an error occurs during the streaming process, it logs the error and yields the error message as the final output.
        *   *Parameters:*
            - **user_input** (`str`): The input query provided by the user for the LLM to process in a streaming fashion.
        *   *Returns:*
            - **chunk_content** (`Generator[str]`): A generator that yields text chunks (strings) as they are received from the LLM stream, or an error message string if the stream fails.

---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to systematically gather and structure fundamental metadata about a software project from common project files such as README, pyproject.toml, and requirements.txt. It operates by prioritizing structured file formats (TOML) for core data like title and dependencies, while using the README for descriptive sections like features, tech stack, and installation guides. The class maintains an internal state dictionary, progressively populating it through specialized parsing methods, and finally orchestrates the entire extraction process via the public `extrahiere_info` method to return a comprehensive project summary.
*   **Instantiation:** This class is instantiated by the 'main_workflow' function located in 'main.py'.
*   **Dependencies:** The class relies on the standard Python libraries 're' for regular expression matching and 'os' for path manipulation. It also conditionally uses the 'tomllib' library for parsing TOML files.
*   **Constructor:**
    *   *Description:* The constructor initializes the internal state of the extractor. It defines a constant placeholder string, `self.INFO_NICHT_GEFUNDEN`, used to mark fields where information is missing. It then sets up the core data structure, `self.info`, which is a nested dictionary containing placeholders for project overview (title, description, status, features, tech stack) and installation details (dependencies, setup, quick start guide).
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* The constructor initializes the internal state of the extractor. It defines a constant placeholder string, `self.INFO_NICHT_GEFUNDEN`, used to mark fields where information is missing. It then sets up the core data structure, `self.info`, which is a nested dictionary containing placeholders for project overview (title, description, status, features, tech stack) and installation details (dependencies, setup, quick start guide).
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private utility method searches a provided list of file objects (`dateien`) to find the first file whose path matches any of the given filename patterns. The comparison is performed case-insensitively to ensure flexibility across different operating systems and naming conventions. It iterates through all files and patterns, checking if the file path ends with the pattern after converting both to lowercase. If a match is found, the file object is returned immediately.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of filename patterns (e.g., 'readme.md') to search for.
            - **dateien** (`List[Any]`): A list of file objects, expected to have a 'path' attribute.
        *   *Returns:*
            - **** (`Optional[Any]`): The matching file object whose path corresponds to one of the patterns, or None if no file matches.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This method extracts a specific block of text from a Markdown string by searching for a level 2 heading (`##`) that matches one of the provided keywords. It dynamically constructs a regular expression pattern using the keywords, ensuring they are properly escaped for regex use. The pattern captures all content following the matching heading up until the next level 2 heading or the end of the document. The extracted text is then returned after stripping leading/trailing whitespace.
        *   *Parameters:*
            - **inhalt** (`str`): The entire Markdown text content.
            - **keywords** (`List[str]`): A list of alternative keywords used to identify the target section title (e.g., ['Installation', 'Setup']). The search is case-insensitive.
        *   *Returns:*
            - **** (`Optional[str]`): The extracted text section found under the matching Markdown heading, or None if the section is not found.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This method processes the content of a README file to extract descriptive project information. It first attempts to find the project title using a level 1 Markdown heading and extracts a general description from the text immediately following the title. It then calls `_extrahiere_sektion_aus_markdown` repeatedly with different keyword sets to populate fields like key features, tech stack, status, setup instructions, and quick start guides. Fields are only updated if they still hold the 'Information not found' placeholder, allowing higher-priority sources to override them.
        *   *Parameters:*
            - **inhalt** (`str`): The raw content of the README file.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This method parses the content of a `pyproject.toml` file, treating it as the authoritative source for project metadata. It first checks for the availability of the `tomllib` library and prints a warning if it is missing. If successful, it loads the TOML content and extracts the project name, description, and dependencies from the `[project]` table. The dependencies field is always overwritten if found, reflecting the high priority of TOML data, and includes basic exception handling for decoding errors.
        *   *Parameters:*
            - **inhalt** (`str`): The raw content of the pyproject.toml file.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This method processes the content of a `requirements.txt` file to extract project dependencies, serving as a fallback mechanism. It only updates the dependencies list in `self.info` if that field has not yet been populated by a higher-priority source (like `pyproject.toml`). It parses the file content line by line, filtering out empty lines and comments (lines starting with '#') before storing the resulting list of dependencies.
        *   *Parameters:*
            - **inhalt** (`str`): The raw content of the requirements.txt file.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This is the primary public method that orchestrates the entire information extraction process. It first locates the relevant project files (README, TOML, requirements) using `_finde_datei`. It then calls the parsing methods in a strict priority order: TOML, then requirements, then README. After parsing, it formats the collected dependencies list into a bulleted string if necessary. Finally, it derives the project title from the provided repository URL, overwrites any previously found title, and returns the complete, structured project information dictionary.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file objects (expected to contain path and content) from the repository.
            - **repo_url** (`str`): The URL of the repository, used to derive the final project title.
        *   *Returns:*
            - **** (`Dict[str, Any]`): A dictionary containing all extracted project information, categorized into 'projekt_uebersicht' and 'installation' sections.

---
### File: `backend/callgraph.py`
#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an Abstract Syntax Tree (AST) visitor responsible for analyzing Python source code to construct a directed call graph. It inherits from `ast.NodeVisitor` and overrides specific `visit_*` methods to identify function and class definitions, track the current scope, and capture function calls. It uses helper methods to convert raw function names into fully qualified identifiers (including filename and class context) and handles special cases like asynchronous functions and the `if __name__ == "__main__"` block, ensuring that all call relationships are accurately mapped and stored in internal data structures like a NetworkX graph and an edges dictionary.
*   **Instantiation:** This class is instantiated by the function `build_callGraph` in the file `callgraph.py`.
*   **Dependencies:** This class relies on the `ast` module for AST traversal and `networkx` (aliased as `nx`) for graph construction.
*   **Constructor:**
    *   *Description:* The constructor initializes the AST visitor by storing the `filename` being analyzed and setting up internal state variables like `current_function` and `current_class` to track the current scope during traversal. It initializes a NetworkX directed graph (`self.graph`) and several data structures (`import_mapping`, `function_set`, `edges`) used to store the call graph data collected during the AST traversal.
    *   *Parameters:*
        - **filename** (`str`): The name of the file currently being analyzed, used for creating fully qualified names for functions and classes.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename)`
        *   *Description:* The constructor initializes the AST visitor by storing the `filename` being analyzed and setting up internal state variables like `current_function` and `current_class` to track the current scope during traversal. It initializes a NetworkX directed graph (`self.graph`) and several data structures (`import_mapping`, `function_set`, `edges`) used to store the call graph data collected during the AST traversal.
        *   *Parameters:*
            - **filename** (`str`): The name of the file currently being analyzed, used for creating fully qualified names for functions and classes.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively traverses an AST node representing a function call (`ast.Call`) to extract the name(s) of the function being called. If the node is an `ast.Call`, it recursively calls itself on the `node.func` attribute to drill down to the actual callable object. If the node is an `ast.Name` (simple function name) or `ast.Attribute` (method/attribute access), it extracts the identifier (`node.id` or `node.attr`) and returns it, effectively resolving the raw name of the callee.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing the function call structure to be analyzed.
        *   *Returns:*
            - **all_calls** (`list[str]`): A list containing the raw names of the functions or methods identified as the callee.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private helper method takes a list of raw callee names and converts them into fully qualified names suitable for the call graph. It prepends the `self.filename` to the raw callee name. If the traversal is currently inside a class (`self.current_class` is set), it also includes the class name in the fully qualified path, ensuring that the callee is uniquely identified within the project structure.
        *   *Parameters:*
            - **callee_nodes** (`list[str]`): A list of raw function or method names extracted from the AST.
        *   *Returns:*
            - **resolved_callees** (`list[str]`): A list of fully qualified names (e.g., filename::[class]::function) for the callees.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This private utility method constructs a fully qualified name for a function or class definition. It takes a base name (like a function name) and optionally a class name. It prefixes these names with the `self.filename` to ensure global uniqueness within the analysis context, using `::` as a separator.
        *   *Parameters:*
            - **basename** (`str`): The base name of the entity (e.g., function name).
            - **class_name** (`str | None`): The name of the containing class, if applicable. Defaults to None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name (e.g., filename::[class]::function).
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private method determines the identity of the current scope, which acts as the caller in the call graph. If `self.current_function` is set (meaning the visitor is inside a function definition), that function's full name is returned. Otherwise, it defaults to a global scope identifier, using the filename if available, or '<global-scope>' if the filename is missing.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **caller_name** (`str`): The fully qualified name of the current function or a placeholder for the global scope.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method handles the traversal of an `ast.ClassDef` node. It temporarily saves the current class context, updates `self.current_class` to the name of the new class, and then manually iterates through the class body, calling `self.visit` on each function defined within. This ensures that methods defined inside the class are correctly associated with the class name when their full names are generated. Finally, it restores the previous class context upon exiting the definition.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes standard function definitions (`def`). It first determines the fully qualified name of the function using `_make_full_name`, incorporating the class name if applicable. It then adds this fully qualified name as a node to the NetworkX graph and adds it to the `function_set`. After setting `self.current_function` to establish the current caller context, it calls `self.generic_visit(node)` to traverse the function body, allowing nested calls to be captured, and finally resets `self.current_function` to `None`.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method handles asynchronous function definitions (`async def`). Since the call graph analysis treats synchronous and asynchronous functions identically for the purpose of node creation and call tracking, this method simply delegates its processing entirely to `visit_FunctionDef`.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing the asynchronous function definition.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This is the core method for identifying edges in the call graph. When an `ast.Call` node is encountered, it first identifies the `caller` using `_current_caller`. It then uses `_recursive_call` to extract the raw names of the functions being invoked and `_resolve_all_callee_names` to convert them into fully qualified names. Finally, it records the call relationship by adding the resolved callee names to the set of edges associated with the current caller in `self.edges`. Error handling is included to catch complex or unexpected call structures without crashing the traversal.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing the function or method call.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method specifically targets `if` statements to identify the common Python entry point idiom: `if __name__ == "__main__"`. If this pattern is detected, it temporarily overrides `self.current_function` to the special identifier `<main_block>`. This ensures that any function calls found within the main block are correctly attributed to the `<main_block>` node in the call graph, rather than the global scope of the file. After traversing the block, the original caller context is restored.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing the if statement.
        *   *Returns:*
            *Analysis data not available for this component.*

#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree, filename)`
*   **Description:** This function constructs a directed call graph (networkx.DiGraph) from a given Python Abstract Syntax Tree (AST). It initializes a custom `CallGraph` visitor, which traverses the AST to identify function definitions (nodes) and function/method calls (edges). After the traversal is complete, the function iterates over the collected edges stored in the visitor's internal dictionary. It explicitly adds each identified call relationship as a directed edge between the caller and callee nodes in the graph object before returning the final network structure.
*   **Parameters:**
    - **tree** (`ast.AST`): The Abstract Syntax Tree (AST) of the Python file that is being analyzed.
    - **filename** (`str`): The name of the analyzed file, used for context within the graph construction process (e.g., 'main.py').
*   **Returns:**
    - **graph** (`nx.DiGraph`): The complete directed call graph, where nodes represent functions or scopes and edges represent function or method calls.
*   **Usage:**
    *   Calls: `CallGraph`, `add_edge`, `items`, `visit`
    *   Called by: `analyze_repository` in `AST_Schema.py`, `build_global_callgraph` in `callgraph.py`

#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph)`
*   **Description:** This function converts a NetworkX directed graph (nx.DiGraph), which is typically used to represent a call graph, into a standard Python dictionary format that is easily JSON-serializable. The resulting dictionary serves as an adjacency list. To ensure consistent output, the function iterates over the nodes in sorted order. For each node, it retrieves its successors (callees), sorts them, and adds the pair (caller: [callees]) to the adjacency list, provided the node has at least one successor.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph (call graph) to be converted into an adjacency list format.
*   **Returns:**
    - **adj_list** (`Dict[str, list[str]]`): An adjacency list represented as a dictionary. Keys are caller nodes (strings) and values are lists of callee nodes (strings).
*   **Usage:**
    *   Calls: `list`, `nodes`, `sorted`, `successors`
    *   Called by: *No callers found in the provided context.*

#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(repo)`
*   **Description:** This function is responsible for constructing a comprehensive, global directed call graph for all Python files within a given Git repository. It initializes an empty NetworkX directed graph and iterates through every file provided by the repository object. For each Python file found, it parses the content into an Abstract Syntax Tree (AST), generates a file-specific call graph using the helper function `build_callGraph`, and then merges the nodes and edges from this local graph into the global graph. The function ensures that all nodes (functions/methods) and edges (calls) are correctly aggregated before returning the final structure.
*   **Parameters:**
    - **repo** (`GitRepository`): The repository object containing the files to be analyzed for call relationships.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated function call relationships across all Python files in the repository.
*   **Usage:**
    *   Calls: `DiGraph`, `add_edge`, `add_node`, `basename`, `build_callGraph`, `endswith`, `get_all_files`, `parse`, `removesuffix`, `str`
    *   Called by: `backend.callgraph` in `callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function prepares a NetworkX directed graph for DOT file output by ensuring all node identifiers are safe for graph visualization tools. It first creates a copy of the input graph and generates a mapping where complex original node names are replaced with simple, sequential identifiers (e.g., "n0", "n1"). It then relabels the nodes in the copied graph using this mapping. Crucially, it stores the original, complex node names in the 'label' attribute of the newly named nodes. Finally, the function writes the relabeled graph structure to the specified output file path using the NetworkX DOT writer utility.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph (DiGraph) whose nodes need to be safely relabeled for DOT output.
    - **out_path** (`str`): The file path where the resulting DOT file will be saved.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `copy`, `enumerate`, `items`, `list`, `nodes`, `relabel_nodes`, `write_dot`
    *   Called by: `backend.callgraph` in `callgraph.py`

---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** The RepoFile class serves as a representation of a single file found within a Git repository, designed to abstract access to its content and metadata. It utilizes a lazy loading mechanism, meaning that the underlying Git Blob object, file size, and content are only fetched from the commit tree when they are explicitly accessed via their respective properties. This design optimizes performance by avoiding unnecessary data retrieval until required. The class also provides utility methods for data analysis and structured serialization.
*   **Instantiation:** This class is instantiated by the 'get_all_files' function located in 'getRepo.py'.
*   **Dependencies:** This class functionally depends on the 'git.Tree' object passed during initialization and utilizes the 'os' module for path manipulation.
*   **Constructor:**
    *   *Description:* The constructor initializes the RepoFile object by storing the file path and the Git Tree object associated with the commit. It sets up internal attributes for the blob, content, and size to None, establishing the state required for subsequent lazy loading.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, file_path, commit_tree)`
        *   *Description:* The constructor initializes the RepoFile object by storing the file path and the Git Tree object associated with the commit. It sets up internal attributes for the blob, content, and size to None, establishing the state required for subsequent lazy loading.
        *   *Parameters:*
            - **file_path** (`str`): The path to the file within the repository.
            - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy access to the underlying Git Blob object for the file. If the blob has not been loaded, it attempts to retrieve it from the stored commit tree using the file path. If the file is not found in the tree structure, a FileNotFoundError is raised to indicate the missing resource.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **** (`git.Blob`): The Git Blob object representing the file data.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property implements lazy loading for the file's textual content. Upon first access, it retrieves the Git Blob (if not already loaded), reads its data stream, and decodes it using UTF-8 encoding while ignoring potential errors. The decoded string content is then cached for future access.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **** (`str`): The decoded content of the file as a string.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy access to the size of the file in bytes. If the size has not been cached, it ensures the Git Blob is loaded via the 'blob' property and then retrieves the size attribute from the blob object, caching the result before returning it.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **** (`int`): The size of the file in bytes.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method performs a simple analysis by counting the total number of words present in the file content. It accesses the lazy-loaded 'content' property, splits the resulting string based on whitespace, and returns the length of the resulting list of words.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **** (`int`): The total count of words in the file content.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This magic method provides a clear and useful string representation of the RepoFile object, primarily for debugging and logging purposes. It formats the output to display the class name and the stored file path.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **** (`str`): A string representation of the object, including its file path.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method serializes the file's metadata into a dictionary format. It includes the file path, name (extracted using os.path.basename), size (via the lazy-loaded property), and file type. It accepts an optional boolean flag to include the full file content in the dictionary if required.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the file content is included in the output dictionary. Defaults to False.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing the file's metadata and optionally its content.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class is designed to manage the lifecycle of a remote Git repository. It automatically handles cloning the repository into a temporary directory upon instantiation and ensures cleanup of this directory upon closing, leveraging the Python context manager protocol (__enter__ and __exit__). Its core functionality involves retrieving all files within the repository as specialized RepoFile objects and organizing these files into a hierarchical dictionary structure representing the file tree.
*   **Instantiation:** This class is instantiated within the main_workflow function located in main.py.
*   **Dependencies:** This class does not appear to have external dependencies based on the provided context data, though it internally uses tempfile, logging, and git.Repo.
*   **Constructor:**
    *   *Description:* The constructor initializes the repository by accepting a URL, creating a temporary directory, and attempting to clone the repository using `Repo.clone_from`. If successful, it stores the repository object, the latest commit, and the commit tree for subsequent operations. If cloning fails due to a `GitCommandError`, it ensures the temporary directory is cleaned up via `self.close()` before raising a `RuntimeError`.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, repo_url)`
        *   *Description:* The constructor initializes the repository by accepting a URL, creating a temporary directory, and attempting to clone the repository using `Repo.clone_from`. If successful, it stores the repository object, the latest commit, and the commit tree for subsequent operations. If cloning fails due to a `GitCommandError`, it ensures the temporary directory is cleaned up via `self.close()` before raising a `RuntimeError`.
        *   *Parameters:*
            - **repo_url** (`str`): The URL of the Git repository to be cloned.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves all tracked file paths from the cloned Git repository using the underlying Git command `ls-files`. It then iterates over these paths to instantiate a list of `RepoFile` objects, associating each file with the current commit tree. This list is stored internally in `self.files` and returned to the caller, providing structured access to the repository's contents.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* The `close` method is responsible for cleaning up the resources associated with the cloned repository. It checks if a temporary directory path exists and, if so, prints a message indicating its intended deletion. Although the actual file system deletion is commented out in the source code, the method's purpose is to remove the temporary clone and reset the internal directory reference.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This method implements the entry point for the context manager protocol. When the GitRepository object is used in a `with` statement, this method is executed, returning the instance itself to be used within the context block.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **self** (`GitRepository`): Returns the instance of the GitRepository object.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This method implements the exit point for the context manager protocol. It is automatically called when the `with` block is exited, regardless of whether an exception occurred. Its sole function is to call `self.close()` to ensure the temporary repository files are cleaned up.
        *   *Parameters:*
            - **exc_type** (`type`): The type of exception raised, or None if no exception occurred.
            - **exc_val** (`Exception`): The exception instance, or None.
            - **exc_tb** (`traceback`): The traceback object, or None.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method constructs a nested dictionary structure representing the hierarchical file tree of the repository. If the list of files (`self.files`) has not yet been populated, it first calls `get_all_files()`. It then iterates through the files, splitting their paths to build directories dynamically, and finally appends the file's dictionary representation to the appropriate directory level.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the content of the files is included in the resulting dictionary structure. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree structure of the repository.

---
### File: `backend/main.py`
#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the effective processing time (net time) by subtracting estimated rate-limiting sleep durations from the total elapsed time. It first determines the total duration between the start and end times. If the provided model name does not start with "gemini-", the function assumes no rate limiting and returns the total duration immediately. For Gemini models, it calculates the number of batches based on the total items and batch size, and then subtracts 61 time units for every required sleep interval between batches. The final result is guaranteed to be non-negative.
*   **Parameters:**
    - **start_time** (`Numeric`): The timestamp or numeric value representing the start time of the operation.
    - **end_time** (`Numeric`): The timestamp or numeric value representing the end time of the operation.
    - **total_items** (`int`): The total number of items that were processed.
    - **batch_size** (`int`): The maximum number of items allowed per processing batch.
    - **model_name** (`str`): The name of the model being used, which determines if rate-limit adjustments (specific to 'gemini-' models) are applied.
*   **Returns:**
    - **net_time** (`Numeric`): The calculated net duration of the process, adjusted for estimated sleep times, or 0 if the calculated net time is negative.
*   **Usage:**
    *   Calls: `ceil`, `max`, `startswith`
    *   Called by: `main_workflow` in `main.py`

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** This function serves as the main orchestration workflow for analyzing a software repository. It handles input validation, API key and model selection, repository cloning using GitRepository, and structural analysis via ProjektInfoExtractor and ASTAnalyzer. The core logic involves preparing structured inputs for a Helper LLM (to analyze functions and classes) and a Main LLM (to generate the final report). It manages status updates via a callback, implements rate-limiting sleeps for specific models, executes the LLM calls, saves the final report to disk, and returns the report content along with execution metrics.
*   **Parameters:**
    - **input** (`str`): The user input string, which must contain the repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing necessary API keys (e.g., 'gemini', 'gpt', 'ollama') required for initializing the LLM clients.
    - **model_names** (`dict`): A dictionary specifying the names of the models to be used for the 'helper' and 'main' LLM roles.
    - **status_callback** (`callable|None`): An optional callback function used to provide real-time status updates during the workflow execution.
*   **Returns:**
    - **analysis_output** (`dict`): A dictionary containing the 'report' (the final generated Markdown report string) and 'metrics' (timing and model usage statistics).
*   **Usage:**
    *   Calls: *No calls found in the provided context.*
    *   Called by: `frontend.Frontend` in `Frontend.py`, `backend.main` in `main.py`

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function serves as a centralized mechanism for reporting status updates within the application. It accepts a message string (`msg`) which is used to communicate progress or state changes. The function first checks if a `status_callback` function is defined and truthy; if so, it executes this callback with the provided message. Finally, the function ensures that the status message is recorded using the standard Python `logging.info` facility, providing a persistent record of the workflow's progress.
*   **Parameters:**
    - **msg** (`str`): The status message string containing information about the current state or progress of the workflow.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `info`, `status_callback`
    *   Called by: `main_workflow` in `main.py`

---
### File: `backend/relationship_analyzer.py`
#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is responsible for performing static analysis on a Python project to map out its internal structure and function/method relationships. It achieves this by recursively scanning the project directory for Python files, parsing their Abstract Syntax Trees (ASTs) to collect definitions (classes, functions, methods), and then running a specialized visitor (CallResolverVisitor) over the ASTs to identify and record all cross-module and intra-module calls. The class maintains two key internal states: a dictionary of all definitions and a call graph mapping callees to their callers, which it then formats into a structured, machine-readable output detailing the project's functional dependencies.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py.
*   **Dependencies:** The class does not explicitly list external functional dependencies in the provided context array.
*   **Constructor:**
    *   *Description:* The class is initialized by accepting the root directory of the project to be analyzed. It immediately converts this path to an absolute path and initializes internal state dictionaries: self.definitions for storing metadata about defined entities (functions, classes) and self.call_graph (a defaultdict) for mapping callees to a list of their callers.
    *   *Parameters:*
        - **project_root** (`string`): The path to the root directory of the project being analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, project_root)`
        *   *Description:* The class is initialized by accepting the root directory of the project to be analyzed. It immediately converts this path to an absolute path and initializes internal state dictionaries: self.definitions for storing metadata about defined entities (functions, classes) and self.call_graph (a defaultdict) for mapping callees to a list of their callers.
        *   *Parameters:*
            - **project_root** (`string`): The path to the root directory of the project being analyzed.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This is the main execution method for the analyzer. It orchestrates the entire process by first finding all Python files in the project using _find_py_files. It then iterates through these files twice: once to collect all function, method, and class definitions using _collect_definitions, and a second time to resolve the actual function calls using _resolve_calls. Finally, it returns the structured results generated by calling get_formatted_results.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **output_list** (`list[dict]`): A list of dictionaries containing structured information about defined entities and who calls them.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This utility method recursively traverses the project directory starting from self.project_root. It uses os.walk to iterate through all directories and files within the project structure. It filters the results, collecting and returning a list of absolute paths for all files that end with the .py extension.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of file paths corresponding to all Python files found within the project root.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This method processes a single Python file to identify and record all defined entities (functions, methods, and classes). It reads the file content, parses it into an Abstract Syntax Tree (AST), and walks the tree. It uses AST nodes (FunctionDef, ClassDef) to determine the entity type, constructs a unique path name (e.g., module.Class.method), and stores this definition along with its file path and line number in self.definitions. It handles nested definitions (methods inside classes) by calling _get_parent.
        *   *Parameters:*
            - **filepath** (`str`): The path to the Python file currently being analyzed.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This is a helper method used during AST traversal to find the immediate parent node of a given child node within the AST structure. It iterates through all nodes in the tree using ast.walk and checks the children of each potential parent using ast.iter_child_nodes. This logic is crucial for distinguishing standalone functions from class methods during definition collection.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree being searched.
            - **node** (`ast.AST`): The child node whose parent is being sought.
        *   *Returns:*
            - **parent** (`ast.AST | None`): The parent node of the input node, or None if no parent is found.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This method analyzes a single Python file to identify all function and method calls within it. It reads the file, parses the AST, and then instantiates and runs a CallResolverVisitor (an external class) over the tree using the visit method. The visitor populates a temporary structure with call information. The method then iterates through the visitor's results and updates the instance's self.call_graph by mapping the callee's path name to the list of callers found in the current file.
        *   *Parameters:*
            - **filepath** (`str`): The path to the Python file currently being analyzed.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* This method processes the raw data stored in self.call_graph and self.definitions to produce the final structured output list. It iterates through every callee found in the call graph. If the callee is a defined entity in the project, it formats the definition information (identifier, type, origin file/line) and aggregates all unique callers associated with it. The resulting list of dictionaries provides a comprehensive view of which defined entities are called and by whom.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **output_list** (`list[dict]`): A list of dictionaries, where each dictionary represents a defined entity and includes a sorted list of all unique locations where it is called.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor is an Abstract Syntax Tree (AST) visitor designed to statically analyze Python source code and map function/method calls to their fully qualified names (QNames). It achieves this by maintaining a dynamic scope based on import statements and tracking object instantiation types to resolve method calls on instances. When a call is encountered, the visitor determines the caller's context (module, function, or method) and records the relationship in a centralized dictionary, keyed by the callee's QName. This class is fundamental for building a comprehensive call graph of a project.
*   **Instantiation:** This class is instantiated by the private method _resolve_calls located in relationship_analyzer.py.
*   **Dependencies:** This class relies on the abstract base class ast.NodeVisitor for AST traversal functionality, collections.defaultdict for storing call results, and the os module for path manipulation.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor's state, setting up context variables required for accurate call resolution. It stores the file path, calculates the module path, accepts a dictionary of known project definitions, and initializes internal state tracking dictionaries for scope, instance types, and the final call graph results.
    *   *Parameters:*
        - **filepath** (`string`): The path to the source file currently being analyzed.
        - **project_root** (`string`): The root directory of the project, used in conjunction with filepath to determine the module path.
        - **definitions** (`dict`): A dictionary containing all known qualified names (QNames) defined across the project.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filepath, project_root, definitions)`
        *   *Description:* The constructor initializes the visitor's state, setting up context variables required for accurate call resolution. It stores the file path, calculates the module path, accepts a dictionary of known project definitions, and initializes internal state tracking dictionaries for scope, instance types, and the final call graph results.
        *   *Parameters:*
            - **filepath** (`string`): The path to the source file currently being analyzed.
            - **project_root** (`string`): The root directory of the project, used in conjunction with filepath to determine the module path.
            - **definitions** (`dict`): A dictionary containing all known qualified names (QNames) defined across the project.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method handles the traversal of class definitions. It temporarily updates the visitor's state to track the current class name, which is necessary for correctly identifying methods within that class. After recursively visiting all nodes inside the class definition, it restores the previous class name, ensuring correct scope management during AST traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles the traversal of function definitions, whether they are standalone functions or methods. It saves the current caller name and updates it to the name of the function being visited. This ensures that any calls found inside this function are correctly attributed to it. The previous caller name is restored after the function body has been fully traversed.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This is the primary method for recording call relationships. It first attempts to resolve the callee's qualified name using the internal helper method, _resolve_call_qname. If the callee is successfully resolved and known in the project definitions, the method determines the type of the current caller (module, method, or function). It then stores the caller's context (file, line number, name, and type) in the self.calls dictionary, keyed by the callee's QName.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes standard import statements (e.g., 'import module as alias'). It iterates through the imported names and registers them in the self.scope dictionary. The scope maps the local name or alias to the full module name, which is crucial for resolving qualified names of functions or classes imported directly.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles 'from ... import ...' statements, including complex relative imports. It calculates the full module path for the imported names, correctly handling relative levels based on the current module path. It then registers the imported name and its fully qualified path in the self.scope dictionary, enabling resolution of calls to imported entities.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a from-import statement.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method tracks object instantiation to enable instance method resolution. If an assignment involves a call to a class constructor (e.g., 'x = MyClass()'), it checks if the class name is known in the current scope. If so, it maps the assigned variable's ID (e.g., 'x') to the class's qualified name in self.instance_types. This mapping is later used by _resolve_call_qname to resolve calls like 'x.method()'.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
            *Analysis data not available for this component.*
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method resolves the fully qualified name (QName) of a function or method call based on the current scope and instance tracking. It handles two primary cases: direct calls (ast.Name) by checking local scope and module definitions, and attribute access calls (ast.Attribute, e.g., obj.method) by checking if the object is a tracked instance type or an imported module. If a QName can be successfully determined, it is returned; otherwise, it returns None.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called.
        *   *Returns:*
            - **qname** (`string | None`): The fully qualified name of the called entity, or None if resolution fails.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a file system path into a standard Python module path string. It first calculates the path relative to the provided project root using `os.path.relpath`. It then strips the `.py` extension if present. Directory separators are replaced with dots to form the module structure. Finally, if the path refers to an initialization file (ending in `.__init__`), that suffix is removed to represent the package name itself. The resulting string is a fully qualified module path.
*   **Parameters:**
    - **filepath** (`str`): The full file path to be converted into a module identifier.
    - **project_root** (`str`): The root directory of the project, used as the base for calculating the relative path.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path string (e.g., 'package.submodule').
*   **Usage:**
    *   Calls: `endswith`, `relpath`, `replace`
    *   Called by: `_collect_definitions` in `relationship_analyzer.py`, `__init__` in `relationship_analyzer.py`

---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** This function handles the encryption of a plain text string using an external encryption utility, referred to as the global `cipher_suite` object. It first performs a check: if the input `text` is empty or if the `cipher_suite` is not initialized, it returns the original text unencrypted. If encryption proceeds, the input string is encoded into bytes, encrypted using `cipher_suite.encrypt()`, and the resulting ciphertext bytes are decoded back into a string before being returned.
*   **Parameters:**
    - **text** (`str`): The string content that needs to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted ciphertext string, or the original input string if the text was empty or the cipher suite was unavailable.
*   **Usage:**
    *   Calls: `decode`, `encode`, `encrypt`
    *   Called by: `update_gemini_key` in `db.py`

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** This function attempts to decrypt a given input string using a globally available object named `cipher_suite`. It first performs a guard clause check, returning the original text immediately if the input string is empty or if `cipher_suite` is not initialized. If decryption is attempted, the input string is first encoded to bytes, decrypted using `cipher_suite.decrypt()`, and then decoded back into a string. The function includes robust error handling, catching any general exception during the decryption process and returning the original, unencrypted text to prevent application failure.
*   **Parameters:**
    - **text** (`str`): The string content that is intended to be decrypted.
*   **Returns:**
    - **Decrypted Text or Original Text** (`str`): Returns the successfully decrypted string. If decryption fails due to an exception, the input text is empty, or the cipher suite is unavailable, the original input string is returned.
*   **Usage:**
    *   Calls: `decode`, `decrypt`, `encode`
    *   Called by: `get_decrypted_api_keys` in `db.py`

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function is responsible for creating a new user record and inserting it into the database. It constructs a user dictionary where the provided username serves as the document's primary key (_id). The plain-text password is securely hashed using stauth.hasher.hash before storage. The function then inserts this prepared document into the dbusers collection and returns the unique identifier of the newly created record.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which is used as the document's primary key (_id).
    - **name** (`str`): The user's display name.
    - **password** (`str`): The plain-text password that will be hashed before being stored in the database.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (username) of the newly inserted user document, retrieved from the insertion result.
*   **Usage:**
    *   Calls: `hash`, `insert_one`
    *   Called by: *No callers found in the provided context.*

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function serves as a utility to retrieve all stored user records from the database. It accesses the database collection represented by the variable `dbusers` and executes a comprehensive `find()` operation to select all documents. The resulting iterable cursor is immediately converted into a standard Python list to ensure all data is materialized before being returned to the caller.
*   **Parameters:**
    *Analysis data not available for this component.*
*   **Returns:**
    - **users** (`list`): A list containing all user documents (likely dictionaries) fetched from the underlying database collection referenced by `dbusers`.
*   **Usage:**
    *   Calls: `find`, `list`
    *   Called by: `frontend.Frontend` in `Frontend.py`

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** This function is designed to retrieve a single user record from a database collection, presumably named `dbusers`. It takes a `username` as input and uses it to query the database, specifically matching the value against the document's `_id` field. The function executes a `find_one` operation, returning the resulting user document if found, or `None` otherwise.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) used to locate the user document in the database. This value is used as the query for the document's `_id` field.
*   **Returns:**
    - **user** (`dict | None`): The database document (likely a dictionary or BSON object) representing the fetched user, or `None` if no user matches the provided username.
*   **Usage:**
    *   Calls: `find_one`
    *   Called by: *No callers found in the provided context.*

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function is responsible for securely updating a user's Gemini API key within the database. It first takes the raw API key and encrypts it using the `encrypt_text` utility function. It then executes an `update_one` operation on the `dbusers` collection, targeting the document identified by the provided `username`. The encrypted key is stored in the `gemini_api_key` field. The function returns the count of records that were successfully modified.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose Gemini API key needs to be updated. This is used as the MongoDB document ID (_id).
    - **gemini_api_key** (`str`): The raw, unencrypted Gemini API key provided by the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents (users) that were modified by the database update operation.
*   **Usage:**
    *   Calls: `encrypt_text`, `update_one`
    *   Called by: `frontend.Frontend` in `Frontend.py`

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function updates the Ollama Base URL associated with a specific user in the database. It takes the user's unique identifier (username) and the new URL (ollama_base_url). It executes a MongoDB-style update operation on the `dbusers` collection, setting the `ollama_base_url` field for the matching document. The function returns the count of documents that were successfully modified.
*   **Parameters:**
    - **username** (`str`): The unique identifier (used as the _id) of the user whose record needs updating.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service to be stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the database update operation.
*   **Usage:**
    *   Calls: `update_one`
    *   Called by: `frontend.Frontend` in `Frontend.py`

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** This function is designed to retrieve the Gemini API key for a specific user from a database collection, presumably a MongoDB collection named `dbusers`. It executes a query using the provided `username` as the document's primary identifier (`_id`). The query is optimized to fetch only the `gemini_api_key` field. The function then safely extracts and returns the value of this key using the `.get()` method on the resulting user document.
*   **Parameters:**
    - **username** (`str`): The unique identifier (used as the database document's _id) of the user whose Gemini API key is being retrieved.
*   **Returns:**
    - **gemini_api_key** (`str or None`): The Gemini API key string associated with the user, or None if the key is not present in the user's database record.
*   **Usage:**
    *   Calls: `find_one`, `get`
    *   Called by: *No callers found in the provided context.*

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** This function is designed to retrieve the configured Ollama base URL for a specific user from the database. It accepts the user's identifier, `username`, as input. It queries the `dbusers` collection using `find_one` to locate the user document based on the `_id` matching the username. The query is optimized to project only the necessary `ollama_base_url` field. The function then safely extracts and returns this URL using the dictionary's `get` method, which handles cases where the field might be missing.
*   **Parameters:**
    - **username** (`str`): The unique identifier (ID) of the user whose Ollama base URL is being fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The base URL for the Ollama service associated with the user, or None if the field is not present in the user's database record.
*   **Usage:**
    *   Calls: `find_one`, `get`
    *   Called by: *No callers found in the provided context.*

#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** This function handles the deletion of a single user record from the database. It targets the `dbusers` collection and uses the provided `username` as the unique identifier (`_id`) for the document to be removed. The operation executes a `delete_one` command. The function returns an integer indicating the number of records that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) used to locate and delete the specific user record in the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents (users) successfully deleted by the operation (typically 0 or 1).
*   **Usage:**
    *   Calls: `delete_one`
    *   Called by: *No callers found in the provided context.*

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function retrieves a user document from the database based on the provided username. It first queries the 'dbusers' collection using the username as the document ID. If a user is found, it proceeds to retrieve two specific fields: 'gemini_api_key' and 'ollama_base_url'. The Gemini API key is passed to an external 'decrypt_text' function to obtain its plaintext value. The function returns a tuple containing the decrypted Gemini API key and the Ollama base URL; if the user is not found, it returns a tuple of (None, None).
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user document in the database.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted plaintext Gemini API key, or None if the user was not found.
    - **ollama_plain** (`str | None`): The Ollama base URL retrieved from the user document, or None if the user was not found.
*   **Usage:**
    *   Calls: `decrypt_text`, `find_one`, `get`
    *   Called by: `frontend.Frontend` in `Frontend.py`

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time)`
*   **Description:** This function is responsible for persisting a complete user-system interaction record (an "exchange") into the database collection `dbexchanges`. It gathers various inputs including the question, answer, user feedback, and metadata like usernames and chat names. It constructs a dictionary containing all these fields, automatically adding a `created_at` timestamp using `datetime.now()`. Finally, it executes the database insertion via `dbexchanges.insert_one()` and returns the unique identifier of the newly created record.
*   **Parameters:**
    - **question** (`str`): The text of the question posed by the user.
    - **answer** (`str`): The text of the answer generated by the system.
    - **feedback** (`str`): The textual feedback provided by the user regarding the exchange.
    - **username** (`str`): The identifier of the user initiating the exchange.
    - **chat_name** (`str`): The name or identifier of the chat session where the exchange occurred.
    - **helper_used** (`str`): Optional identifier for the helper model utilized during the exchange. Defaults to an empty string.
    - **main_used** (`str`): Optional identifier for the main model utilized during the exchange. Defaults to an empty string.
    - **total_time** (`str`): Optional string representing the total time elapsed for the exchange process. Defaults to an empty string.
    - **helper_time** (`str`): Optional string representing the time spent by the helper model. Defaults to an empty string.
    - **main_time** (`str`): Optional string representing the time spent by the main model. Defaults to an empty string.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier (e.g., MongoDB ObjectId) assigned by the database to the newly inserted exchange record.
*   **Usage:**
    *   Calls: `insert_one`, `now`
    *   Called by: `frontend.Frontend` in `Frontend.py`

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** This function is responsible for querying a database collection, presumed to be `dbexchanges`, to retrieve all exchange records associated with a specific user. It accepts a username string and uses it as a filter criterion in the database query. The results returned by the database's `find` operation are immediately converted into a standard Python list before being returned to the caller.
*   **Parameters:**
    - **username** (`str`): The username used to query and filter the exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of database documents (exchanges) found for the specified username.
*   **Usage:**
    *   Calls: `find`, `list`
    *   Called by: `load_data_from_db` in `Frontend.py`

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function is responsible for querying a database collection, likely named `dbexchanges`, to retrieve specific exchange records. It filters the records based on two required criteria: the `username` and the `chat_name`. The function executes a database `find` operation using these parameters and converts the resulting cursor or iterable into a standard Python list, which is then returned.
*   **Parameters:**
    - **username** (`str`): The user identifier used as a primary filter criterion for the exchange records.
    - **chat_name** (`str`): The name of the chat used as a secondary filter criterion for the exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of database documents (exchanges) that match both the provided username and chat name.
*   **Usage:**
    *   Calls: `find`, `list`
    *   Called by: *No callers found in the provided context.*

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function is responsible for updating the feedback score associated with a specific exchange record in the database. It takes the unique identifier of the exchange and the new integer feedback value as arguments. The function executes an update_one operation on the 'dbexchanges' collection, setting the 'feedback' field within the matching document. It returns the 'modified_count' property from the update result, indicating how many documents were successfully changed.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier used to locate the specific exchange record to be updated in the database.
    - **feedback** (`int`): The new integer value representing the feedback score to be stored for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were successfully modified by the database update operation (typically 0 or 1).
*   **Usage:**
    *   Calls: `update_one`
    *   Called by: `handle_feedback_change` in `Frontend.py`

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function updates the feedback message associated with a specific exchange record in the database. It uses the provided `exchange_id` to locate the target document within the `dbexchanges` collection. The function executes a MongoDB `update_one` operation, setting the `feedback_message` field to the new string value. It returns the count of documents that were successfully modified.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier used to locate the specific exchange record in the database for updating.
    - **feedback_message** (`str`): The new string value to be stored as the feedback message for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents (0 or 1) that were modified by the database update operation.
*   **Usage:**
    *   Calls: `update_one`
    *   Called by: `render_exchange` in `Frontend.py`

#### Function: `delete_chats_by_user`
*   **Signature:** `def delete_chats_by_user(username, chat_name)`
*   **Description:** This function is designed to delete all database records associated with a specific chat session belonging to a particular user. It constructs a query using the provided username and chat name. The function executes a bulk deletion operation using the `dbexchanges.delete_many` method. It returns the total count of documents that were successfully removed from the collection.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose chat exchanges are targeted for deletion.
    - **chat_name** (`str`): The specific name of the chat session whose exchanges should be removed.
*   **Returns:**
    - **deleted_count** (`int`): The number of database documents (exchanges) that were successfully deleted by the operation.
*   **Usage:**
    *   Calls: `delete_many`
    *   Called by: `handle_delete_chat` in `Frontend.py`

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function handles the deletion of a specific exchange record from the database. It accepts a unique identifier, `exchange_id`, and uses it to construct a query targeting the document's `_id` field within the `dbexchanges` collection. The function executes the `delete_one` operation and returns the count of records that were successfully removed, typically 1 if found and deleted, or 0 otherwise.
*   **Parameters:**
    - **exchange_id** (`str`): The unique string identifier used to locate the specific exchange record to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation, typically 0 or 1.
*   **Usage:**
    *   Calls: `delete_one`
    *   Called by: `handle_delete_exchange` in `Frontend.py`

---
### File: `frontend/Frontend.py`
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** This function is responsible for initializing and populating the Streamlit session state with existing chat data retrieved from the database for a specific user. It first checks if the data has already been loaded using the "data_loaded" flag in `st.session_state`. If not loaded, it fetches chat exchanges using `db.fetch_exchanges_by_user` and organizes them into `st.session_state.chats`, grouping exchanges by their `chat_name`. It also ensures that any missing feedback fields are initialized to `np.nan`. Finally, it sets a default 'Chat 1' if no chats are found, or sets the first loaded chat as the `active_chat` if one is not already defined.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose chat exchanges should be loaded from the database.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `append`, `fetch_exchanges_by_user`, `get`, `keys`, `list`
    *   Called by: `frontend.Frontend` in `Frontend.py`

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function is responsible for updating the user feedback associated with a specific exchange object, managing both the in-memory state and the persistent database record. It accepts the exchange object and the new feedback value. The function first updates the 'feedback' key within the local exchange dictionary. Subsequently, it calls a database utility function, `db.update_exchange_feedback`, to persist this change using the exchange's unique identifier. Finally, it invokes `st.rerun()` to force a full refresh of the Streamlit application, ensuring the UI reflects the state change immediately.
*   **Parameters:**
    - **ex** (`dict`): The exchange object (likely a dictionary) whose feedback is being updated. It must contain the '_id' key for database lookup.
    - **val** (`Any`): The new feedback value to be assigned to the exchange.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `rerun`, `update_exchange_feedback`
    *   Called by: `render_exchange` in `Frontend.py`

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of a specific exchange object, ensuring consistency across both the persistent database and the current application state. It first calls a database utility function, `db.delete_exchange_by_id`, using the exchange's unique identifier (`_id`). Subsequently, it removes the exchange object from the relevant chat's list of exchanges stored in the Streamlit session state. Finally, it forces a complete UI refresh by calling `st.rerun()` to immediately reflect the deletion to the user.
*   **Parameters:**
    - **chat_name** (`str`): The name or identifier of the chat whose exchanges list needs to be updated in the session state.
    - **ex** (`dict`): The exchange object (dictionary) to be deleted. It must contain the '_id' key necessary for database deletion.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `delete_exchange_by_id`, `remove`, `rerun`
    *   Called by: `render_exchange` in `Frontend.py`

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function is responsible for deleting a specific chat session identified by the user and chat name. It performs a two-step deletion process: first removing the chat data from the database via `db.delete_chats_by_user`, and then removing it from the Streamlit session state (`st.session_state.chats`). After deletion, it manages the active chat state. If other chats remain, the first one is selected as active; otherwise, a new default chat named "Chat 1" is created. Finally, it forces a Streamlit rerun to refresh the user interface.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose chat is being deleted.
    - **chat_name** (`str`): The name or key of the chat session that should be deleted.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `delete_chats_by_user`, `keys`, `len`, `list`, `rerun`
    *   Called by: `frontend.Frontend` in `Frontend.py`

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text)`
*   **Description:** This function processes a string of markdown text, specifically designed to identify and render embedded Mermaid diagram blocks. It uses a regular expression to split the input text into alternating segments of standard markdown and Mermaid code, delimited by ````mermaid ... ````. Standard text segments are rendered using `st.markdown`. Mermaid code segments are passed to the `st_mermaid` function for graphical rendering. If the `st_mermaid` rendering fails for any reason, the raw code is displayed using `st.code` with the language set to 'mermaid'.
*   **Parameters:**
    - **markdown_text** (`str`): The input text string, potentially containing standard markdown and embedded Mermaid diagram code blocks.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `code`, `enumerate`, `hash`, `markdown`, `split`, `st_mermaid`, `strip`
    *   Called by: `render_exchange` in `Frontend.py`, `frontend.Frontend` in `Frontend.py`

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function is responsible for rendering a single chat exchange (a user question and an assistant answer) within a Streamlit application. It first displays the user's question using a 'user' chat message. It then renders the assistant's response, which includes a compact toolbar for interaction, followed by the answer content itself. The toolbar provides functionality for positive/negative feedback, writing detailed feedback via a popover, downloading the answer as Markdown, and deleting the exchange. The assistant's answer is displayed within a scrollable container and processed by `render_text_with_mermaid` for enhanced rendering.
*   **Parameters:**
    - **ex** (`dict`): The exchange object containing the user's 'question', the assistant's 'answer', feedback status ('feedback'), and a unique identifier ('_id').
    - **current_chat_name** (`str`): The name of the current chat session, which is required when calling the `handle_delete_exchange` function.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   Calls: `button`, `caption`, `chat_message`, `columns`, `container`, `download_button`, `get`, `handle_delete_exchange`, `handle_feedback_change`, `popover`, `render_text_with_mermaid`, `rerun`, `sleep`, `success`, `text_area`, `update_exchange_feedback_message`, `write`
    *   Called by: `frontend.Frontend` in `Frontend.py`

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** This class serves as a Pydantic data model designed to standardize the representation of a single parameter within a function signature. It inherits from `BaseModel` to enforce strict typing and validation for its three core attributes. The model ensures that every parameter is documented with its name, its type (as a string), and a detailed description of its role, making it a fundamental component for structured documentation generation.
*   **Instantiation:** The input context does not specify where this class is instantiated, but it is typically used internally by documentation or analysis tools to structure function parameter metadata.
*   **Dependencies:** This class depends on `pydantic.BaseModel` to provide data validation and structured attribute definition.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated to accept and validate the three required string fields: name, type, and description. These values are assigned directly as instance attributes upon successful initialization.
    *   *Parameters:*
        - **name** (`str`): The identifier of the function parameter.
        - **type** (`str`): The type annotation or inferred type of the parameter, represented as a string.
        - **description** (`str`): A detailed explanation of the parameter's purpose and usage.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic data model designed to strictly define the structure for documenting the return value of a function or method. It inherits from BaseModel, providing validation and serialization capabilities. It ensures that every return description includes a name, a type string, and a textual description, facilitating consistent data exchange and documentation generation within the system.
*   **Instantiation:** The specific locations where this class is instantiated were not provided in the context.
*   **Dependencies:** This class depends on pydantic.BaseModel to provide data validation and structured data capabilities.
*   **Constructor:**
    *   *Description:* The class is initialized via the Pydantic BaseModel constructor, requiring values for the three defined attributes: name, type, and description. This constructor validates the input types to ensure all fields are strings, establishing a structured format for return value documentation.
    *   *Parameters:*
        - **name** (`str`): The name of the return value, often used for named return types or complex structures.
        - **type** (`str`): The string representation of the data type being returned (e.g., 'List[int]', 'Optional[str]').
        - **description** (`str`): A detailed textual explanation of what the return value represents or contains.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic data model designed to encapsulate and validate the calling context of a function or method. It serves as a structured container for two critical pieces of information: a summary of external functions or methods that the target function calls, and a summary of where the target function is called from within the system. This ensures a standardized format for describing functional dependencies and usage patterns.
*   **Instantiation:** The input context does not specify explicit instantiation points, suggesting it is likely instantiated dynamically within data processing pipelines that analyze function usage.
*   **Dependencies:** This class relies on pydantic.BaseModel for defining its structure and providing data validation capabilities.
*   **Constructor:**
    *   *Description:* The class is initialized via the Pydantic BaseModel constructor, requiring string values for both the 'calls' and 'called_by' fields to define the usage context.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or classes that the target function calls internally.
        - **called_by** (`str`): A string summarizing the functions or methods that call the target function.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic BaseModel designed to hold the complete, structured analysis of a single Python function. It acts as a foundational data schema for documentation generation, ensuring that all critical components of a function
its purpose, parameters, returns, and usage context	are captured in a machine-readable format.
*   **Instantiation:** The instantiation points for this class are not explicitly provided in the context, suggesting it is likely instantiated dynamically within analysis or documentation generation pipelines.
*   **Dependencies:** This class relies on pydantic.BaseModel for its structure and validation, and uses typing.List for defining its collection fields. It also depends on the definitions of ParameterDescription, ReturnDescription, and UsageContext.
*   **Constructor:**
    *   *Description:* The constructor is automatically generated by Pydantic's BaseModel. It initializes the instance attributes based on the provided arguments, ensuring they conform to the specified types (str, List[ParameterDescription], List[ReturnDescription], and UsageContext) and performing validation upon instantiation.
    *   *Parameters:*
        - **overall** (`str`): A high-level, synthesized summary of the function's purpose and implementation.
        - **parameters** (`List[ParameterDescription]`): A list of structured descriptions for all input parameters of the function.
        - **returns** (`List[ReturnDescription]`): A list of structured descriptions for the values returned by the function.
        - **usage_context** (`UsageContext`): An object detailing the function's calling context, including what it calls and where it is called from.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class serves as the primary data model for structuring the analysis of a single Python function or method. It inherits from Pydantic's BaseModel, providing robust data validation and serialization capabilities. This model encapsulates the function's name via the `identifier`, its detailed structural and contextual analysis in the `description` field, and an optional `error` field for reporting issues during the analysis process.
*   **Instantiation:** The instantiation context for this data model is not provided in the current context.
*   **Dependencies:** This class relies on the `BaseModel` from Pydantic for data structure definition and validation, and `Optional` from the `typing` module.
*   **Constructor:**
    *   *Description:* The class is initialized by accepting three primary fields: the function's identifier (string), a detailed description object (FunctionDescription), and an optional string for any analysis errors. As a Pydantic BaseModel, initialization handles validation and assignment of these fields.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): A nested data structure containing the detailed analysis of the function's signature, purpose, and usage context.
        - **error** (`Optional[str]`): An optional field used to store any error messages if the function analysis failed or encountered issues.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic data model designed to structure and validate metadata about the constructor (__init__) of a Python class. It acts as a schema for describing how a class is initialized, requiring a high-level summary of the initialization process and a detailed list of all parameters accepted by the constructor. This model is typically used in systems that analyze or generate documentation for code.
*   **Instantiation:** The instantiation context for this class is not provided in the input.
*   **Dependencies:** This class primarily depends on Pydantic's BaseModel for schema definition and validation, and relies on the `List` type hint and the external `ParameterDescription` schema.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel. It initializes the instance attributes `description` and `parameters` by validating the provided input types against the defined schema, ensuring `description` is a string and `parameters` is a list of `ParameterDescription` objects.
    *   *Parameters:*
        - **description** (`str`): A string summarizing the purpose and behavior of the constructor.
        - **parameters** (`List[ParameterDescription]`): A list of objects detailing each parameter accepted by the constructor, conforming to the ParameterDescription schema.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `ClassContext`
*   **Summary:** This Pydantic BaseModel serves as a data structure (DTO) for capturing the usage context of a Python class. It strictly defines two string fields: dependencies and instantiated_by, ensuring that contextual metadata is consistently structured for downstream processing.
*   **Instantiation:** The instantiation points for this data model are not provided in the current context, but it is typically instantiated when structuring class usage metadata.
*   **Dependencies:** This class relies on the Pydantic BaseModel for its structure and validation capabilities.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated to accept and validate the `dependencies` and `instantiated_by` fields, ensuring they are provided as strings upon initialization.
    *   *Parameters:*
        - **dependencies** (`str`): A string summarizing the external dependencies required by the class being described.
        - **instantiated_by** (`str`): A string summarizing the locations or components responsible for instantiating the class being described.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to serve as the canonical schema for storing a complete, structured analysis of a Python class. It aggregates various components of the analysis, including the overall purpose, the constructor details, a list of detailed method analyses, and contextual information regarding its usage and dependencies within a larger system. This structure is crucial for standardizing the output of code analysis tools.
*   **Instantiation:** This class is typically instantiated internally within the AI analysis pipeline to structure the output data.
*   **Dependencies:** This class does not rely on external dependencies beyond its Pydantic base class and standard Python types for its definition.
*   **Constructor:**
    *   *Description:* The constructor is automatically generated by Pydantic's BaseModel. It initializes the data structure by accepting and validating the required fields: the overall class summary, the constructor description, a list of method analyses, and the class's usage context.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose and role.
        - **init_method** (`ConstructorDescription`): The structured analysis of the class's __init__ method.
        - **methods** (`List[FunctionAnalysis]`): A list containing the structured analysis for every method defined within the class (excluding __init__).
        - **usage_context** (`ClassContext`): Contextual information about where the class is used and what dependencies it relies upon.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis model serves as the root structure for the structured output generated by the AI Code Analyst. It encapsulates all findings related to a single Python class, including its unique identifier, a detailed ClassDescription containing method and constructor analyses, and an optional field for reporting analysis errors. This model ensures the output is standardized and machine-readable for downstream processing.
*   **Instantiation:** This class is typically instantiated by the AI Code Analyst system after successfully analyzing a Python class definition, serving as the final structured output format.
*   **Dependencies:** This class is a Pydantic model, inheriting from BaseModel, and relies on the definition of ClassDescription and Optional for type hinting.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the class constructor is inherited. It initializes the data structure by requiring an identifier string and a ClassDescription object, while the error field is optional and defaults to None.
    *   *Parameters:*
        - **identifier** (`str`): The name or unique ID of the class being analyzed.
        - **description** (`ClassDescription`): A nested object containing the detailed analysis of the class, including methods, constructor, and overall purpose.
        - **error** (`Optional[str]`): An optional field used to report if the analysis of the class failed or encountered a critical issue.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `FunctionContextInput`
*   **Summary:** FunctionContextInput is a Pydantic data model used to structure and validate the usage context of a function within a larger codebase analysis system. It serves as a container for two key pieces of information: a list of entities that the function calls, and a list of entities that call the function, both represented as lists of strings. This structure ensures that function analysis data is consistently formatted for downstream processing.
*   **Instantiation:** This class is instantiated by the `main_workflow` function located in `main.py`.
*   **Dependencies:** This class relies on the Pydantic library for inheriting BaseModel functionality, which provides data validation and structured attribute definition.
*   **Constructor:**
    *   *Description:* This class inherits its constructor from pydantic.BaseModel. It initializes the instance attributes `calls` and `called_by` based on the provided keyword arguments, ensuring they conform to the specified list of strings type hints.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of identifiers (strings) representing other functions, methods, or classes that this function calls.
        - **called_by** (`List[str]`): A list of identifiers (strings) representing other functions or methods that call this function.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The class is a Pydantic model and does not contain any custom methods.
*   **Instantiation:** This class is instantiated by the `main_workflow` function located in `main.py`.
*   **Dependencies:** This class relies on Pydantic's BaseModel for schema validation and standard Python typing utilities like List and Literal to define its structure.
*   **Constructor:**
    *   *Description:* The class is initialized by accepting values for its defined fields: mode, identifier, source_code, imports, and context. As a Pydantic BaseModel, validation and type coercion are handled automatically upon instantiation.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies that the input is intended for a function analysis operation.
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **source_code** (`str`): The raw Python source code of the function.
        - **imports** (`List[str]`): A list of import statements relevant to the function's execution context.
        - **context** (`FunctionContextInput`): Additional contextual metadata required for the analysis process.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `MethodContextInput`
*   **Summary:** MethodContextInput is a Pydantic data model designed to structure and hold contextual information about a single method within a larger class analysis. It captures essential metadata such as the method's name (identifier), its dependencies (calls), its usage points (called_by), its arguments (args), and its documentation (docstring). This model serves as a standardized input structure for processing method-level context.
*   **Instantiation:** This class is instantiated primarily within the main_workflow function located in main.py.
*   **Dependencies:** This class has no external functional dependencies defined in the context, relying only on the imported pydantic.BaseModel for structure.
*   **Constructor:**
    *   *Description:* The class is initialized as a Pydantic BaseModel, accepting values for its five defined fields: identifier, calls, called_by, args, and docstring. Pydantic handles validation and attribute assignment, ensuring the input conforms to the specified types.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method being described.
        - **calls** (`List[str]`): A list of identifiers for other functions, methods, or classes that this method calls.
        - **called_by** (`List[str]`): A list of identifiers for other functions or methods that call this method.
        - **args** (`List[str]`): A list of the parameter names defined in the method's signature.
        - **docstring** (`Optional[str]`): The raw docstring content associated with the method, if one exists.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic data model designed to structure and hold all necessary contextual information required for a comprehensive analysis of a target Python class. It defines three core fields: a list of external dependencies, a list detailing where the class is instantiated, and a list providing specific context for each method within the class. This model ensures standardized data input for subsequent AI processing steps.
*   **Instantiation:** This class is instantiated by the `main_orchestrator` function in `HelperLLM.py` and the `main_workflow` function in `main.py`.
*   **Dependencies:** This class does not appear to rely on any external components listed in the provided context.
*   **Constructor:**
    *   *Description:* The class is initialized using the Pydantic BaseModel constructor, which validates and assigns values to the defined fields: dependencies, instantiated_by, and method_context.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of external dependencies required by the class being analyzed.
        - **instantiated_by** (`List[str]`): A list of locations (files/functions) where the class being analyzed is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list containing detailed context information for each method within the class being analyzed.
*   **Methods:**
    *Analysis data not available for this component.*

#### Class: `ClassAnalysisInput`
*   **Summary:** ClassAnalysisInput is a Pydantic data model that strictly defines the required input structure for initiating a class analysis task within the system. It inherits from BaseModel to provide robust data validation and serialization. The model ensures that all necessary components—the operational mode, the class identifier, the raw source code, associated imports, and contextual information—are present and correctly typed before the analysis process can begin.
*   **Instantiation:** This class is instantiated by the main_orchestrator function in HelperLLM.py and the main_workflow function in main.py, indicating its use as a primary input object for workflow execution.
*   **Dependencies:** This class has no external functional dependencies listed in the provided context, relying primarily on Pydantic for data validation.
*   **Constructor:**
    *   *Description:* The class utilizes the inherited Pydantic BaseModel constructor to initialize its attributes based on the provided keyword arguments, ensuring type validation against the defined fields upon instantiation.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operational mode, which must be the literal string 'class_analysis'.
        - **identifier** (`str`): The fully qualified name of the class being analyzed.
        - **source_code** (`str`): The raw source code string of the entire class definition.
        - **imports** (`List[str]`): A list of import statements found in the source file containing the class.
        - **context** (`ClassContextInput`): A nested object containing additional contextual information required for the analysis, such as dependencies and call graphs.
*   **Methods:**
    *Analysis data not available for this component.*

---
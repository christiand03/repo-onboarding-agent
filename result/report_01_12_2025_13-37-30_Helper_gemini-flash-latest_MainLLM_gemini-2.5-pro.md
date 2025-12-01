# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated code analysis and documentation generation agent. It takes a Git repository URL as input, clones it, and performs a comprehensive static analysis. The analysis includes building an Abstract Syntax Tree (AST), creating file dependency graphs, and constructing call graphs. This structured data is then processed by a series of Large Language Models (LLMs) to generate detailed, human-readable documentation, which is presented through a Streamlit-based web frontend.
- **Key Features:**
  - Automated repository cloning and analysis from a URL.
  - Abstract Syntax Tree (AST), file dependency, and call graph generation.
  - Dual-LLM architecture (Helper/Main) for detailed analysis and report synthesis.
  - Interactive web interface built with Streamlit for user input and results display.
  - Database integration for user management, API key storage, and analysis history.
- **Tech Stack:** LangChain, Streamlit, NetworkX, GitPython, Pydantic, PyMongo, Google Generative AI, Ollama.

*   **Repository Structure:**
    ```mermaid
    graph LR
        subgraph root
            A["/.env.example<br/>.gitignore<br/>analysis_output.json<br/>readme.md<br/>requirements.txt"]
        end
        subgraph SystemPrompts
            B["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt"]
        end
        subgraph backend
            C["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py"]
        end
        subgraph database
            D["db.py"]
        end
        subgraph frontend
            E["Frontend.py<br/>__init__.py"]
            subgraph frontend/gifs
                F["4j.gif"]
            end
            E --> F
        end
        subgraph notizen
            G["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
            subgraph notizen/grafiken
                H["File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
            end
            G --> H
        end
        subgraph result
            I["ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
        end
        subgraph schemas
            J["types.py"]
        end
        root --> A
        root --> B
        root --> C
        root --> D
        root --> E
        root --> G
        root --> I
        root --> J
    ```

## 2. Installation
### Dependencies
To install the required dependencies, run the following command in your terminal:
```bash
pip install -r requirements.txt
```
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
- toon_format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c9006de6
- tornado==6.5.2
- typing-inspection==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0

### Setup Guide
1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd repo-onboarding-agent
    ```
2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment Variables:**
    -   Copy the example environment file: `cp .env.example .env`
    -   Edit the `.env` file to add your API keys (e.g., for Gemini, OpenAI) and any other required credentials like your MongoDB connection string.

### Quick Startup
To run the application, execute the following command from the root directory of the project:
```bash
streamlit run frontend/Frontend.py
```

## 3. Use Cases & Commands
The primary use case of this application is to automatically generate comprehensive technical documentation for a given software repository.

1.  **Start the Application:** Run the Streamlit frontend using the command `streamlit run frontend/Frontend.py`.
2.  **User Authentication:** Log in or register through the web interface. User data is managed via a MongoDB database.
3.  **Configure Settings:** In the user settings panel, provide your API keys for the desired LLMs (e.g., Google Gemini, OpenAI) and the base URL if using a local Ollama instance.
4.  **Analyze a Repository:** Enter the URL of a public Git repository into the main input field.
5.  **Initiate Analysis:** Start the documentation generation process. The application will provide real-time status updates as it clones the repository, performs static code analysis, and invokes the LLMs.
6.  **View and Interact with the Report:** Once complete, the final Markdown report will be displayed in the interface. Users can view the generated documentation, interact with diagrams, provide feedback on the analysis, and download the report.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is a specialized implementation of `ast.NodeVisitor` designed to traverse a Python Abstract Syntax Tree and extract structural metadata about the code. It systematically collects information regarding imports, standalone functions, and class definitions, including their nested methods. The primary goal is to generate a structured schema (`self.schema`) containing identifiers, source code segments, line numbers, and context necessary for deeper code analysis.
*   **Instantiation:** This class is instantiated by the `analyze_repository` function located in `AST_Schema.py`.
*   **Dependencies:** This class depends on the standard Python `ast` module for AST traversal capabilities and relies on a local utility function, `path_to_module`, for resolving file paths.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor by storing essential context information: the raw source code, the file path, and the project root. It calculates the module path using an external utility function and sets up the primary output structure, `self.schema`, which is used to collect imports, functions, and classes during the AST traversal. It also initializes `self._current_class` to track context when processing methods nested within classes.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code string of the file being analyzed.
        - **file_path** (`str`): The absolute path to the file containing the source code.
        - **project_root** (`str`): The root directory of the entire project, used for calculating relative module paths.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method overrides the standard `ast.NodeVisitor` behavior to handle simple import statements (e.g., `import os, sys`). It iterates through all imported names defined in the node and appends the module name to the `imports` list within the class schema. After processing the import names, it calls `generic_visit` to ensure traversal continues down the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing the import statement.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `from ... import ...` statements. It constructs the fully qualified import name by combining the module name (`node.module`) with the imported alias name. This fully qualified name is then appended to the `imports` list in the schema, ensuring accurate tracking of dependencies.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing the import-from statement.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method processes class definitions found in the AST. It calculates a unique `class_identifier` and extracts metadata such as the class name, docstring, source code segment, and line numbers using utility functions from the `ast` module. This information is stored in the `classes` list of the schema. Crucially, it sets `self._current_class` to the newly created class context before calling `generic_visit`, allowing nested methods to be correctly associated with this class.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles standard synchronous function definitions. It first checks if it is currently inside a class by inspecting `self._current_class`. If it is a method, it extracts context information (identifier, arguments, lines) and appends it to the current class's method context list. If it is a standalone function, it creates a full analysis structure (including source code) and appends it to the `functions` list in the schema.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method is designed to handle asynchronous function definitions (using `async def`). It delegates the entire processing logic to `visit_FunctionDef`, ensuring that async functions are analyzed and structured identically to synchronous functions for the purpose of structural analysis.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing the asynchronous function definition.
        *   *Returns:*
            - Analysis data not available for this component.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class serves as the primary engine for generating a structured, comprehensive schema of a code repository. Its main responsibility is to process a collection of source files, parse them into Abstract Syntax Trees (ASTs), extract structural information (functions, classes, imports), and integrate relationship data, such as internal call graphs and external usage context. It orchestrates the file-by-file analysis and provides methods to merge relationship data from various sources into a single, cohesive schema dictionary.
*   **Instantiation:** This class is instantiated by the `main_workflow` function located in `main.py`.
*   **Dependencies:** The class relies on the standard Python `ast` module for parsing, `os` for path handling, and external libraries like `networkx` (nx) for handling graph structures. It also depends on external utilities such as `ASTVisitor` and `build_callGraph` to perform the core AST traversal and call graph generation.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTAnalyzer class but does not set any instance attributes.
    *   *Parameters:*
        - Analysis data not available for this component.
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* This static method is responsible for integrating call graph data into the existing AST schema structure. It iterates through all functions and class methods defined in the schema. By constructing a fully qualified name key (including the filename) and querying the provided NetworkX call graph, it identifies which entities call the current function/method ('called_by') and which entities the current function/method calls ('calls'). These relationship lists are then sorted and stored directly within the schema dictionary.
        *   *Parameters:*
            - **schema** (`dict`): The dictionary containing the AST structure (functions and classes) to be enriched.
            - **call_graph** (`nx.DiGraph`): The NetworkX directed graph representing the function/method call relationships.
            - **filename** (`str`): The path or name of the file, used to create unique identifiers for graph lookup.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
        *   *Description:* This method integrates external relationship data, such as cross-file dependencies, into the existing full schema structure. It first transforms the input `relationship_data` list into a quick lookup dictionary based on identifiers. It then traverses the `full_schema`, locating functions, classes, and class methods by their identifiers. If a match is found in the lookup, it updates the corresponding context fields: 'called_by' for functions and methods, and 'instantiated_by' for classes. The method ensures that the schema is holistically enriched with external usage context before returning the modified schema.
        *   *Parameters:*
            - **full_schema** (`dict`): The repository-wide schema dictionary containing AST nodes for all files.
            - **relationship_data** (`list`): A list of dictionaries containing external relationship information, typically including 'identifier' and 'called_by' fields.
        *   *Returns:*
            - **full_schema** (`dict`): The updated schema dictionary with merged relationship data.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files)`
        *   *Description:* This is the primary method for processing a list of source files and generating a comprehensive AST schema for the repository. It first determines the project root path and initializes the schema structure. It iterates through each file, skipping non-Python or empty files, and attempts to parse the content into an AST. It uses an external `ASTVisitor` to extract structural data and `build_callGraph` to generate call relationships. Finally, it calls `_enrich_schema_with_callgraph` to integrate the relationship data before storing the file's schema in the overall repository schema.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each containing the file path and content for analysis.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the complete structured schema of the analyzed repository.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a file system path (`filepath`) into a standard Python module path string, relative to a specified `project_root`. It first attempts to calculate the relative path using `os.path.relpath`, handling potential `ValueError` by falling back to the base filename. If the resulting relative path ends with the `.py` extension, it is stripped. Finally, all file path separators are replaced with dots to form the module path. A special check is included to remove the trailing `.__init__` segment if the file was an initialization file.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative file system path that needs to be converted into a module path.
    - **project_root** (`str`): The root directory path of the project, used as the reference point for calculating the relative path.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path string (e.g., 'package.module').
*   **Usage:**
    *   **Calls:** This function utilizes operating system path utilities, specifically `relpath` and `basename`, and performs string manipulations using `endswith` and `replace` methods.
    *   **Called by:** This function is called by the `__init__` method within the `AST_Schema.py` file.

---
### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is an Abstract Syntax Tree (AST) NodeVisitor designed to analyze Python source code and construct a graph of file-level import dependencies. It maintains a class-level dictionary, `import_dependencies`, mapping source filenames to sets of modules they import. The class overrides the standard AST visitor methods to capture import statements and includes complex logic to accurately resolve relative imports by checking the filesystem for existing modules and symbols exported via package `__init__.py` files.
*   **Instantiation:** This class is instantiated by the function `build_file_dependency_graph` located in the file `File_Dependency.py`.
*   **Dependencies:** The class relies on the `ast` module for parsing and visiting nodes, the `pathlib.Path` module for path resolution, and external functions like `get_all_temp_files` and `iskeyword` for file system interaction and identifier validation.
*   **Constructor:**
    *   *Description:* The constructor initializes the File Dependency Graph instance by storing the path of the file currently being analyzed and the root path of the repository. These paths are essential for correctly resolving relative imports and locating files within the project structure.
    *   *Parameters:*
        - **filename** (`str`): The name or path of the file currently being analyzed for dependencies.
        - **repo_root** (`Any`): The root directory of the code repository, used as the base path for resolving all imports.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This private method resolves relative imports of the form `from .. import name1, name2` by calculating the correct base directory based on the import level and the current file's location. It performs extensive path resolution using `pathlib.Path` and checks for module existence, including looking inside package `__init__.py` files to see if symbols are explicitly exported via `__all__` or defined as functions, classes, or assignments. If successful, it returns a list of resolved module or symbol names; otherwise, it raises an `ImportError` indicating that nothing could be resolved.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the relative import statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of module or symbol names that were successfully resolved and confirmed to exist.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method records the dependency relationship between the current file (`self.filename`) and the imported module. It is designed to handle standard `import X` statements and also acts as a helper for `visit_ImportFrom`. It adds the resolved module name (either from `base_name` or the import alias) to the `import_dependencies` set associated with the current file, ensuring the dependency is tracked, and then continues AST traversal using `generic_visit`.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing the import statement.
            - **base_name** (`str | None`): An optional, pre-resolved module name, typically provided when handling `ImportFrom` nodes.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `from ... import ...` statements, differentiating between absolute and relative imports. For absolute imports, it extracts the base module name (the last component) and records the dependency via `visit_Import`. For relative imports (where `node.module` is null), it calls `_resolve_module_name` to determine the actual module names, recording each resolved dependency via `visit_Import`. If relative resolution fails, it prints an error message but continues traversal.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            - Analysis data not available for this component.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function is responsible for constructing a NetworkX directed graph (`nx.DiGraph`) that maps the file-level import dependencies for a single source file. It initializes a `FileDependencyGraph` visitor with the file's name and repository root, and then traverses the provided Abstract Syntax Tree (AST) to collect dependencies. It iterates through the collected import dependencies, where each key is a caller file and the values are the files it imports (callees). Finally, it populates the graph by adding nodes for both caller and callee files and directed edges representing the import relationship.
*   **Parameters:**
    - **filename** (`str`): The path or name of the Python file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) object representing the parsed content of the file.
    - **repo_root** (`str`): The root directory of the repository, used for resolving file paths and relative imports.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies.
*   **Usage:**
    *   **Calls:** This function initializes a networkx.DiGraph, instantiates the FileDependencyGraph visitor, calls the visitor's visit method, and uses graph manipulation methods like add_node, add_nodes_from, and add_edge.
    *   **Called by:** This function is called by 'build_repository_graph' within the same module.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function constructs a comprehensive directed dependency graph (nx.DiGraph) for an entire Git repository. It begins by retrieving all files from the provided GitRepository object and initializing a global graph structure. The function iterates through all files, skipping any that are not Python files (.py). For each Python file, it parses the content into an AST and calls a helper function, build_file_dependency_graph, to determine local dependencies. Finally, it merges the nodes and edges from the local file dependency graph into the repository-wide global graph, ensuring all dependencies are captured.
*   **Parameters:**
    - **repository** (`GitRepository`): The object representing the Git repository to be analyzed, used to retrieve file contents and the repository's temporary directory path.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the combined dependency relationships (nodes and edges) found across all analyzed Python files in the repository.
*   **Usage:**
    *   **Calls:** This function utilizes methods like DiGraph, add_edge, and add_node (likely from networkx), along with standard library functions like basename, endswith, str, and removesuffix. Crucially, it calls repository.get_all_files() and the internal dependency analysis function build_file_dependency_graph.
    *   **Called by:** This function is called by the module-level execution logic within backend.File_Dependency.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function is designed to recursively locate all Python source files (`*.py`) within a specified directory. It first converts the input directory string into an absolute `pathlib.Path` object using `resolve()`. It then uses recursive globbing (`rglob`) to find all matching files. Finally, it returns a list of these file paths, ensuring each path is relative to the original root directory.
*   **Parameters:**
    - **directory** (`str`): The string path of the root directory from which to start the recursive search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of pathlib.Path objects, where each path represents a Python file found recursively, relative to the input directory.
*   **Usage:**
    *   **Calls:** This function utilizes path manipulation methods including constructing a Path object, resolving the absolute path, recursively globbing for files ('*.py'), and calculating the relative path of found files.
    *   **Called by:** This function is called by the function or method named _resolve_module_name.

#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G)`
*   **Description:** This function converts a NetworkX directed graph (G), where nodes represent file paths, into a string formatted for a Mermaid flowchart diagram. It processes the nodes to group files into their respective folders using a defaultdict, treating each folder as a potential Mermaid subgraph. The function generates the diagram structure, defining subgraphs for non-root folders and nodes for individual files, ensuring node IDs are safe by replacing path separators ('/') with underscores ('_'). Finally, it iterates over the graph edges to define the dependencies between the file nodes, returning the complete diagram definition as a newline-separated string.
*   **Parameters:**
    - **G** (`nx.DiGraph`): The NetworkX directed graph representing file dependencies. Nodes are expected to be file paths (e.g., 'folder/file.py').
*   **Returns:**
    - **mermaid_diagram** (`str`): A string containing the complete definition of the dependency graph in Mermaid flowchart syntax, including subgraphs for folders.
*   **Usage:**
    *   **Calls:** The function utilizes standard Python list, string, and dictionary methods like 'append', 'items', 'join', 'replace', and 'split', and relies on 'collections.defaultdict' for grouping files by folder.
    *   **Called by:** This function is called by the module-level execution of 'backend.File_Dependency'.

---
### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class acts as the centralized manager for interacting with various Large Language Models (LLMs), such as Gemini, GPT, and Ollama, specifically for generating structured documentation. It handles the initialization of the LLM client, loads specific system prompts for function and class analysis, and dynamically configures batch sizes to optimize throughput while respecting API rate limits. The class utilizes LangChain's structured output feature with Pydantic schemas to guarantee that the generated documentation adheres to a strict JSON format, ensuring reliable data processing in high-volume batch operations.
*   **Instantiation:** This class is instantiated by the `main_orchestrator` function within `HelperLLM.py` and the `main_workflow` function in `main.py`.
*   **Dependencies:** The class relies on LangChain integrations for Google Generative AI, OpenAI, and Ollama, as well as standard Python libraries like `json`, `logging`, and `time`. Crucially, it depends on Pydantic schemas (`FunctionAnalysis`, `ClassAnalysis`, etc.) for defining and enforcing the structure of its inputs and outputs.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper instance by validating the provided API key, loading the function and class system prompts from disk, and setting up the appropriate LLM client (Google, OpenAI, or Ollama) based on the `model_name`. It calls a private method to configure the optimal batch size for the selected model and wraps the base LLM with structured output capabilities using the `FunctionAnalysis` and `ClassAnalysis` Pydantic schemas.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authentication with the chosen LLM service (e.g., Gemini or OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt text used when analyzing functions.
        - **class_prompt_path** (`str`): The file path to the system prompt text used when analyzing classes.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
        - **ollama_base_url** (`str | None`): The base URL for the Ollama service, required if an Ollama model is selected.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private helper method determines and sets the appropriate batch size (`self.batch_size`) based on the provided LLM `model_name`. It contains hardcoded logic to assign optimized batch sizes for various models like different Gemini, Llama, and GPT versions. If the model name is not recognized, it logs a warning and assigns a conservative default batch size of 2.
        *   *Parameters:*
            - **model_name** (`str`): The identifier of the language model currently in use.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method orchestrates the batch generation and validation of documentation for a list of functions. It converts the input Pydantic models into JSON payloads, structures them as LangChain conversations with the function system prompt, and iteratively sends them to the structured LLM in batches defined by `self.batch_size`. It includes robust exception handling to manage API errors and enforces a 61-second waiting period between batches to comply with rate limits, ensuring the return list maintains order even if some items fail.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input models containing the source code and context required for function analysis.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of validated FunctionAnalysis objects, or None for any input that failed during LLM processing or validation.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method manages the batch processing for generating structured documentation for classes. It takes a list of `ClassAnalysisInput` models, serializes them into JSON payloads, and constructs conversations using the class-specific system prompt. It then sends these conversations to the structured LLM (`self.class_llm`) in batches, implementing the same error handling and rate-limiting mechanisms (61-second wait) as the function generation method to ensure reliable and compliant API usage.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input models containing the source code and context required for class analysis.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of validated ClassAnalysis objects, or None for any input that failed during LLM processing or validation.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a main orchestration loop for demonstrating and testing the LLMHelper class's functionality, specifically for analyzing functions and classes. It defines pre-computed dummy inputs and expected analysis outputs for several hypothetical methods (add_item, check_stock, generate_report) using Pydantic models. It initializes the LLMHelper, simulates the analysis process by calling the helper's generation methods, and then aggregates the results into a final documentation dictionary. The primary purpose is to set up and execute a demonstration workflow for the documentation generation system.
*   **Parameters:**
    - Analysis data not available for this component.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** This function calls various methods related to Pydantic model validation and manipulation (model_validate, model_dump), logging (info, warning), JSON serialization (dumps), and core operations of the LLMHelper class, specifically generate_for_functions. It also instantiates ClassAnalysisInput, ClassContextInput, and LLMHelper.
    *   **Called by:** This function is called by the backend.HelperLLM module itself, suggesting it is the main entry point or execution block of that module.

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class acts as the primary interface for interacting with various Large Language Models (LLMs). It handles initialization by validating the API key, loading a system prompt from a specified file path, and dynamically configuring the appropriate LangChain client (either ChatGoogleGenerativeAI for remote models or ChatOllama for local models). The class provides both synchronous (call_llm) and asynchronous/streaming (stream_llm) methods for generating responses based on user input and the loaded system prompt.
*   **Instantiation:** This class is instantiated by the main_workflow function located in main.py.
*   **Dependencies:** This class does not have explicit external dependencies listed in the context, but internally relies heavily on LangChain components for LLM interaction.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLM client and loads the system prompt. It validates that an API key is provided and attempts to read the system prompt from the given file path, raising an error if the file is not found. Based on the model name prefix, it instantiates either ChatGoogleGenerativeAI or ChatOllama, setting the resulting client to the `self.llm` attribute.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for accessing the LLM service.
        - **prompt_file_path** (`str`): The file path to the text file containing the system prompt used for guiding the LLM's behavior.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.5-pro'.
        - **ollama_base_url** (`str | None`): Optional base URL for the Ollama service, used if a local model is selected.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method executes a synchronous, single-turn call to the initialized LLM. It constructs a list of messages, including the stored system prompt and the provided user input, using LangChain message objects. It invokes the underlying LLM client's `invoke` method and returns the text content of the response. The method includes error handling to log failures and return None upon exception.
        *   *Parameters:*
            - **user_input** (`str`): The specific query or input provided by the user to be sent to the LLM.
        *   *Returns:*
            - **content** (`str | None`): The text response content from the LLM, or None if an exception occurred during the API call.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method initiates a streaming call to the LLM, yielding chunks of the response content as they become available. It prepares the input using the system prompt and user input, and utilizes the LLM client's `stream` method. It iterates over the resulting stream iterator and yields the content of each chunk. If an error occurs during the streaming process, it logs the error and yields a descriptive error message string.
        *   *Parameters:*
            - **user_input** (`str`): The query or input string to be processed by the LLM in a streaming fashion.
        *   *Returns:*
            - **chunk.content** (`str`): A generator yielding successive text chunks of the LLM response.

---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to systematically extract fundamental project metadata from various common project files, such as README, pyproject.toml, and requirements.txt. It acts as an orchestration layer, prioritizing data sources (TOML first, then requirements, then README) to build a comprehensive, structured dictionary of project information. The class uses internal utility methods for case-insensitive file searching and Markdown section extraction to populate fields like project title, description, dependencies, and setup instructions.
*   **Instantiation:** This class is instantiated by the `main_workflow` function located in `main.py`.
*   **Dependencies:** The class does not rely on any external dependencies listed in the provided context, although the implementation uses standard libraries like `re`, `os`, and conditionally `tomllib` for file parsing.
*   **Constructor:**
    *   *Description:* The constructor initializes the class by defining the constant placeholder string 'Information not found' (`INFO_NICHT_GEFUNDEN`). It then sets up the primary instance attribute `self.info`, a nested dictionary structure containing placeholders for all expected project details, including project overview (title, description, features) and installation details (dependencies, setup guides).
    *   *Parameters:*
        - Analysis data not available for this component.
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private utility method searches a provided list of file objects for a file whose path matches any of the given patterns. The search is performed case-insensitively to ensure flexibility in matching file names like 'README.md' or 'readme.md'. It iterates through all files and patterns, returning the first file object that satisfies the path matching criteria, or `None` if no suitable file is found.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of filename suffixes or patterns to search for.
            - **dateien** (`List[Any]`): A list of file objects, expected to have a 'path' attribute.
        *   *Returns:*
            - **null** (`Optional[Any]`): The matching file object if found, otherwise None.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This utility method is responsible for extracting the text content located beneath a specific level-two Markdown heading (`##`). It accepts the full Markdown content and a list of alternative keywords for the section title (e.g., 'Installation', 'Setup'). It dynamically constructs a regular expression using these keywords to capture the content block that follows the matching heading, stopping before the next `##` heading or the end of the document.
        *   *Parameters:*
            - **inhalt** (`str`): The entire Markdown text content.
            - **keywords** (`List[str]`): A list of alternative keywords for the section title.
        *   *Returns:*
            - **null** (`Optional[str]`): The extracted text section content, or None if the heading is not found.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This method parses the content of a README file to extract descriptive project information, serving as a fallback source if metadata is missing from configuration files. It uses regular expressions to capture the main project title (level one heading) and the initial description text. It then calls `_extrahiere_sektion_aus_markdown` repeatedly to find and extract structured sections such as Key Features, Tech Stack, Status, Setup instructions, and Quick Start guides, updating the internal `self.info` state.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the README file.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This method parses the content of a `pyproject.toml` file, which is treated as the highest priority source for project metadata. It checks for the availability of the `tomllib` module before attempting to load and decode the TOML content. If successful, it extracts the project name, description, and dependencies from the `[project]` table, explicitly overwriting any existing dependency information. It includes error handling for `TOMLDecodeError`.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the pyproject.toml file.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This method parses the content of a `requirements.txt` file to extract dependencies, acting only as a fallback if dependencies were not already found in the higher-priority `pyproject.toml`. It processes the file content line by line, filtering out comments and empty lines. If dependencies are successfully extracted, the internal `self.info` dependency list is updated.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the requirements.txt file.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This is the main public method that orchestrates the entire information extraction process. It first locates relevant files using `_finde_datei` and then calls the specific parsing methods (`_parse_toml`, `_parse_requirements`, `_parse_readme`) in order of priority to populate the project information. Finally, it performs post-processing steps, including formatting the dependency list into a readable string and setting the final project title based on the repository URL, before returning the complete extracted data structure.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file objects containing paths and contents from the repository.
            - **repo_url** (`str`): The URL of the repository, used to derive the project name.
        *   *Returns:*
            - **null** (`Dict[str, Any]`): A dictionary containing all extracted project information, structured under 'projekt_uebersicht' and 'installation' keys.

---
### File: `backend/callgraph.py`
#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an Abstract Syntax Tree (AST) visitor responsible for constructing a directed call graph for a single Python source file. It traverses the AST to identify function and class definitions, maintaining context (current file, class, and function) to generate fully qualified names for all callable entities. The core functionality involves detecting function calls (`visit_Call`), resolving their targets, and establishing edges in the internal NetworkX directed graph. It also includes specialized handling for scoping methods within classes and isolating calls made within `if __name__ == "__main__"` blocks.
*   **Instantiation:** This class is instantiated by the function `build_callGraph` located in the file `callgraph.py`.
*   **Dependencies:** This class depends on the `ast` module for AST traversal (as it inherits from `ast.NodeVisitor`) and the `networkx` library (aliased as `nx`) for creating and managing the directed graph structure.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor by storing the file name being analyzed and setting up context trackers for the current function and class. It instantiates a NetworkX directed graph (`self.graph`) and initializes internal data structures, including a dictionary for import mapping, a set for defined functions, and a dictionary to store call edges.
    *   *Parameters:*
        - **filename** (`str`): The name of the file currently being processed, used as the prefix for fully qualified function names.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively traverses an AST node representing a function call to extract the raw names of the callable entity. It handles complex call structures by recursively checking the `node.func` attribute until it reaches a simple identifier (`ast.Name`) or an attribute access (`ast.Attribute`). It returns a list of string identifiers found during the traversal.
        *   *Parameters:*
            - **node** (`Any`): The AST node representing the function call structure.
        *   *Returns:*
            - **all_calls** (`list[str]`): A list containing the raw string identifiers (names or attributes) extracted from the call expression.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private method takes a list of raw callee names and resolves them into fully qualified names based on the current context of the AST traversal. It checks if the visitor is currently inside a class (`self.current_class`) and prepends the class name and filename accordingly to ensure unique identification of the callee.
        *   *Parameters:*
            - **callee_nodes** (`list[str]`): A list of raw function or method names extracted from the AST.
        *   *Returns:*
            - **resolved_callees** (`list[str]`): A list of fully qualified string identifiers for the callees (e.g., filename::ClassName::methodName).
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This private utility method constructs a fully qualified name for a function or method. It combines the stored `self.filename`, an optional `class_name`, and the function's `basename` using double colons (`::`) as separators. This ensures that the generated identifier is globally unique within the project context.
        *   *Parameters:*
            - **basename** (`str`): The simple name of the function or method.
            - **class_name** (`str | None`): The name of the class if the function is a method; otherwise, it is None.
        *   *Returns:*
            - **""** (`str`): The fully qualified name string.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private method determines the identifier of the current execution context, which acts as the caller node in the call graph. If the visitor is inside a function (`self.current_function` is set), that function's full name is returned. Otherwise, it returns a global scope identifier, defaulting to `<global-scope>` if the filename is not available.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **""** (`str`): The fully qualified name of the current calling context (function name or global scope identifier).
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method handles the traversal of class definitions (`ast.ClassDef`). It temporarily updates `self.current_class` to the name of the class being visited, allowing methods defined within the class body to be correctly scoped. It then iterates through the class body, recursively visiting each element, and finally restores the previous class context upon completion.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
            - **""** (`None`): This visitor method does not return a value.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes standard function definitions (`ast.FunctionDef`). It calculates the function's fully qualified name using `_make_full_name`, registers this name as a node in the NetworkX graph, and adds it to the set of known functions. It sets `self.current_function` for context tracking and then uses `generic_visit` to recursively traverse the function body to find any nested calls before resetting the context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
            - **""** (`None`): This visitor method does not return a value.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method handles asynchronous function definitions (`ast.AsyncFunctionDef`). It acts as a simple proxy, delegating all processing logic directly to `visit_FunctionDef`. This ensures that both synchronous and asynchronous functions are treated identically for the purpose of call graph construction and node registration.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing the asynchronous function definition.
        *   *Returns:*
            - **""** (`None`): This visitor method does not return a value.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This is the primary method for identifying function calls and establishing edges. It first determines the caller context using `_current_caller`. It extracts raw callee names using `_recursive_call` and resolves them into fully qualified identifiers using `_resolve_all_callee_names`. It then adds the resolved callees to the set of edges originating from the current caller, handling potential errors during complex call processing gracefully by printing a warning.
        *   *Parameters:*
            - **node** (`Any`): The AST node representing the function or method call.
        *   *Returns:*
            - **""** (`None`): This visitor method does not return a value.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method is specialized to detect and handle `if __name__ == "__main__"` blocks. When this specific condition is met, it temporarily overrides `self.current_function` to the special identifier `<main_block>`. This ensures that any global function calls found within this block are correctly attributed to the dedicated `<main_block>` node in the call graph, providing accurate context for entry points.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing the conditional statement.
        *   *Returns:*
            - **""** (`None`): This visitor method does not return a value.

#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree, filename)`
*   **Description:** This function is responsible for constructing a directed call graph (nx.DiGraph) based on a provided Python Abstract Syntax Tree (AST). It achieves this by instantiating a specialized `CallGraph` visitor, which traverses the AST to identify function definitions and their corresponding calls. After the traversal, the function retrieves the underlying graph structure and iterates through the collected edges (caller-callee mappings) stored in the visitor. Finally, it explicitly adds these directed edges to the NetworkX graph object before returning the complete call graph.
*   **Parameters:**
    - **tree** (`ast.AST`): The Abstract Syntax Tree (AST) of the Python file that needs to be analyzed.
    - **filename** (`str`): The name of the file being analyzed (e.g., 'main.py'), used to provide context to the CallGraph visitor.
*   **Returns:**
    - **graph** (`nx.DiGraph`): The complete directed call graph, where nodes represent functions, methods, or scopes, and edges represent function/method calls.
*   **Usage:**
    *   **Calls:** This function initializes a `CallGraph` object, invokes its `visit` method on the AST, and uses the `items` method to iterate over collected edges before calling `add_edge` on the resulting graph.
    *   **Called by:** This function is utilized by `analyze_repository` in `AST_Schema.py` and `build_global_callgraph` in `callgraph.py`.

#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph)`
*   **Description:** This function converts a NetworkX directed graph (nx.DiGraph), typically representing a call graph, into a standard adjacency list format suitable for JSON serialization. It initializes an empty dictionary and iterates over all nodes in the graph, ensuring the iteration order is consistent by sorting the nodes first. For each node, it retrieves its successors (the nodes it calls) and sorts this list of successors. The function only includes nodes in the output dictionary that have at least one successor, mapping the caller node (string) to a list of callee nodes (list of strings).
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The call graph (NetworkX directed graph) to be converted into an adjacency list.
*   **Returns:**
    - **adj_list** (`Dict[str, list[str]]`): An adjacency list dictionary where keys are caller nodes (strings) and values are sorted lists of callee nodes (list of strings), ensuring JSON serializability.
*   **Usage:**
    *   **Calls:** This function calls Python built-in functions like list() and sorted(), and utilizes NetworkX methods such as nodes() and successors() to traverse the graph structure.
    *   **Called by:** This function is not called by any other analyzed function in the current context.

#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(repo)`
*   **Description:** This function constructs a comprehensive, global call graph for a given Git repository. It achieves this by first retrieving all files within the repository and iterating over them. It specifically processes only Python files, parsing their content into an Abstract Syntax Tree (AST) and generating a local call graph using the helper function `build_callGraph`. Finally, it merges the nodes and edges from each local graph into a single NetworkX directed graph (`nx.DiGraph`), which is returned as the representation of the entire project's function call structure.
*   **Parameters:**
    - **repo** (`GitRepository`): The repository object containing the files whose call relationships are to be analyzed.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent functions and edges represent function calls across the entire repository.
*   **Usage:**
    *   **Calls:** This function initializes a NetworkX DiGraph, retrieves all files using `get_all_files`, performs path manipulation using `os.path.basename` and string methods like `removesuffix`, parses file content using `ast.parse`, calls the internal function `build_callGraph`, and manipulates the graph structure using `add_node` and `add_edge`.
    *   **Called by:** This function is called by the `backend.callgraph` module.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function takes a NetworkX directed graph and prepares it for safe serialization into the DOT format, writing the output to a specified file path. It operates by creating a copy of the input graph and generating a mapping to replace potentially unsafe node names with simple, indexed identifiers (e.g., 'n0', 'n1'). The graph is then relabeled using these safe identifiers, while the original node names are preserved by setting them as the 'label' attribute on the new nodes. Finally, the relabeled graph is written to the disk using the NetworkX DOT writing utility.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph object whose structure needs to be saved to a DOT file.
    - **out_path** (`str`): The file path where the resulting DOT file will be written.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** This function calls methods such as `copy`, `list`, `nodes`, `enumerate`, `items`, `relabel_nodes`, and `write_dot` to manipulate the graph structure and perform file output.
    *   **Called by:** This function is called by the `backend.callgraph` module.

---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** The RepoFile class serves as a structured representation of a single file found within a Git repository at a specific commit. Its primary function is to abstract the underlying Git object model and implement a lazy loading mechanism for file data (blob, content, and size). This design ensures that resource-intensive operations, such as reading and decoding file content, are only executed when the data is explicitly accessed via its properties. The class also provides utility methods for serialization and simple content analysis.
*   **Instantiation:** This class is instantiated by the `get_all_files` method located in the `getRepo.py` file.
*   **Dependencies:** This class relies on the Git library for handling `Tree` and `Blob` objects, and the `os` module for path manipulation.
*   **Constructor:**
    *   *Description:* The constructor initializes the RepoFile object by storing the file path and the Git Tree object associated with the commit. It sets up internal attributes (`_blob`, `_content`, `_size`) to None, establishing the state required for lazy loading of file data.
    *   *Parameters:*
        - **file_path** (`str`): The relative path of the file within the Git repository.
        - **commit_tree** (`git.Tree`): The Git Tree object from which the file originates, used to retrieve the file's blob.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property implements the lazy loading mechanism for the Git blob object corresponding to the file. If the blob has not yet been loaded, it attempts to retrieve it from the stored commit tree using the file path. If the file path does not exist within the tree, a FileNotFoundError is raised, ensuring data integrity.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **""** (`git.Blob`): The Git blob object representing the file data.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides the decoded, textual content of the file, utilizing lazy loading. If the content is not yet cached, it accesses the `blob` property, reads the data stream from the blob, and decodes it using UTF-8 encoding while ignoring any potential errors.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **""** (`str`): The decoded content of the file as a string.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property retrieves the size of the file in bytes, also employing the lazy loading pattern. If the size attribute is not yet set, it accesses the `blob` property to ensure the Git object is loaded and then retrieves the size from the blob object, caching the result.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **""** (`int`): The size of the file in bytes.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method performs a simple analysis by counting the total number of words present in the file's content. It relies on accessing the `content` property, which ensures the file content is loaded and decoded, and then splits the string by whitespace to count the resulting tokens.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **""** (`int`): The total count of words found in the file content.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This method provides a concise and informative string representation of the RepoFile object, primarily used for debugging and logging purposes. The representation includes the class name and the stored file path.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **""** (`str`): A string representation of the object, formatted as <RepoFile(path='...')>.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method serializes the file object into a dictionary containing essential metadata such as path, derived name, size, and type. It supports an optional flag, `include_content`, which, if true, adds the full file content to the resulting dictionary, making it suitable for data transfer or storage.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the full file content is included in the resulting dictionary; otherwise, only metadata is included.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing file metadata and optionally the file content.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class is responsible for managing the lifecycle of a remote Git repository. Upon instantiation, it clones the repository into a temporary directory and stores metadata like the latest commit and commit tree. It provides functionality to retrieve all files as structured objects (RepoFile instances) and to generate a hierarchical file tree structure of the repository content. Furthermore, it implements the Python context management protocol, ensuring that the temporary directory and its contents are reliably cleaned up via the `close` method when the object exits a `with` block.
*   **Instantiation:** This class is instantiated by the `main_workflow` function located in `main.py`.
*   **Dependencies:** This class does not explicitly list external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the repository by setting the URL, creating a temporary directory, and attempting to clone the repository using `Repo.clone_from`. If cloning is successful, it stores the repository object, the latest commit, and the commit tree. If a `GitCommandError` occurs during cloning, it calls `self.close()` to clean up the temporary directory before raising a `RuntimeError`.
    *   *Parameters:*
        - **repo_url** (`string`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves all file paths within the cloned repository using the underlying Git command line tool (`ls-files`). It then iterates through these paths and instantiates a `RepoFile` object for each, associating it with the current commit tree. The resulting list of `RepoFile` instances is stored internally in `self.files` and returned to the caller, providing structured access to the repository's contents.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **""** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method handles resource cleanup for the repository. It checks if a temporary directory (`self.temp_dir`) exists, prints a message indicating its deletion, and then sets the reference to `None`. Note that the actual file system deletion using `shutil.rmtree` is commented out in the provided source code.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This method implements the entry point for the context management protocol, allowing the GitRepository object to be used with Python's `with` statement. It simply returns the instance itself.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **""** (`GitRepository`): Returns the instance of the repository object.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This method implements the exit point for the context management protocol. It ensures that the `self.close()` method is called to clean up the temporary directory, regardless of whether an exception occurred within the `with` block.
        *   *Parameters:*
            - **exc_type** (`Type | None`): The type of exception raised, or None if no exception occurred.
            - **exc_val** (`BaseException | None`): The exception value, or None.
            - **exc_tb** (`TracebackType | None`): The traceback object, or None.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method generates a nested dictionary structure representing the file and directory hierarchy of the repository. It first ensures that all files are loaded by calling `get_all_files()` if necessary. It then iterates through the files, splitting their paths to dynamically build a tree structure where directories are represented by nodes with 'children' lists, and files are appended at the appropriate level using their `to_dict` representation.
        *   *Parameters:*
            - **include_content** (`bool`): Flag indicating whether the content of the files should be included in the resulting dictionary structure. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree structure of the repository.

---
### File: `backend/main.py`
#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time by subtracting estimated rate-limit sleep durations from the total elapsed time. It first determines the total duration between start_time and end_time. If the model_name does not start with "gemini-", the function returns the full total_duration without modification. For Gemini models, it calculates the number of batches required using math.ceil and estimates the total_sleep_time based on a fixed sleep duration of 61 units per batch (excluding the first). Finally, it returns the maximum of zero and the resulting net time.
*   **Parameters:**
    - **start_time** (`Numeric`): The starting timestamp of the operation.
    - **end_time** (`Numeric`): The ending timestamp of the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The maximum number of items processed per batch.
    - **model_name** (`str`): The name of the model used. Sleep time subtraction only occurs if the name starts with 'gemini-'.
*   **Returns:**
    - **net_time** (`Numeric`): The calculated net duration of the process, guaranteed to be non-negative, after subtracting estimated rate-limit sleep times.
*   **Usage:**
    *   **Calls:** This function utilizes mathematical operations including `ceil` and `max`, and the string method `startswith` to determine if rate-limit adjustments are necessary.
    *   **Called by:** This function is invoked by the `main_workflow` function in `main.py`.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** This function serves as the primary orchestration engine for a code analysis and documentation generation workflow. It takes user input (expected to contain a repository URL), API keys, and model configuration, and manages the entire process from repository cloning to final report generation. The workflow involves extracting the URL, cloning the repository using GitRepository, performing code analysis (basic info extraction, file tree construction, relationship analysis, and AST generation), preparing structured inputs for a Helper LLM, and finally using a Main LLM to synthesize the analysis results into a comprehensive report. It handles status updates via an optional callback, manages API key selection for different LLMs (GPT, Gemini, Ollama), and includes rate-limiting sleeps for Gemini models.
*   **Parameters:**
    - **input** (`Any`): The primary user input string, which is expected to contain the URL of the repository to be analyzed.
    - **api_keys** (`dict`): A dictionary containing necessary API keys (e.g., 'gemini', 'gpt') and potentially the 'ollama' base URL.
    - **model_names** (`dict`): A dictionary specifying the model identifiers to be used for the 'helper' and 'main' LLM roles.
    - **status_callback** (`Callable | None`): An optional function used to provide real-time status updates back to the caller (e.g., a frontend interface). Defaults to None.
*   **Returns:**
    - **return_dict** (`dict`): A dictionary containing the final generated report and metrics related to the execution time of the LLMs.
    - **report** (`str`): The final documentation report generated by the Main LLM.
    - **metrics** (`dict`): Performance metrics including helper_time, main_time, total_time, helper_model, and main_model.
*   **Usage:**
    *   **Calls:** This function orchestrates the analysis by calling an internal status update function (`update_status`), standard library functions (`logging.info`, `re.search`, `time.sleep`, `json.dumps`, `os.makedirs`, `datetime.now`), and numerous methods from specialized classes. Key external calls include `GitRepository.get_all_files`, `ProjektInfoExtractor.extrahiere_info`, `ProjectAnalyzer.analyze`, `ASTAnalyzer.analyze_repository`, and `ASTAnalyzer.merge_relationship_data`. It utilizes the LLM wrappers via `LLMHelper.generate_for_functions`, `LLMHelper.generate_for_classes`, and `MainLLM.call_llm` to produce the final report.
    *   **Called by:** This function is called by the `frontend.Frontend` module and the main execution module `backend.main`.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function serves as a centralized mechanism for handling status updates within the application. It accepts a message string and performs two primary actions. First, it checks if a callable object named `status_callback` is defined in the current scope. If the callback exists, it is executed with the provided message, likely for real-time reporting or external communication. Second, the function ensures the message is recorded in the system logs at the INFO level using the imported `logging` module.
*   **Parameters:**
    - **msg** (`str`): The status message string to be logged and potentially passed to the status callback function.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** The function calls the `info` method of the `logging` module and conditionally executes the external function `status_callback` if it is defined.
    *   **Called by:** This function is called extensively by the `main_workflow` function.

---
### File: `backend/relationship_analyzer.py`
#### Class: `ProjectAnalyzer`
*   **Summary:** ProjectAnalyzer is a core utility class responsible for performing static analysis on a Python project to build a comprehensive map of definitions and a call graph. It orchestrates the analysis workflow by traversing the project root, identifying Python files, and executing a two-pass process: first collecting all function, method, and class definitions, and second resolving the relationships between callers and callees using AST traversal and a specialized visitor. The class manages internal state for definitions and the call graph, ultimately formatting this relational data into a structured output list.
*   **Instantiation:** This class is instantiated by the function main_workflow located in main.py.
*   **Dependencies:** The class relies on external modules like os for file system operations, ast for parsing Python code, logging for error handling, and collections.defaultdict for building the call graph structure. It also depends on external components like path_to_module and CallResolverVisitor.
*   **Constructor:**
    *   *Description:* The constructor initializes the analyzer by setting the absolute path of the project root and establishing internal data structures. It sets up dictionaries to store definitions, the call graph (using defaultdict), and temporary file ASTs, and defines a set of directories to exclude from analysis.
    *   *Parameters:*
        - **project_root** (`string`): The path to the root directory of the project that needs to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This is the main execution method that orchestrates the entire analysis workflow. It first identifies all relevant Python files using an internal helper method. It then iterates through these files in two distinct passes: collecting definitions in the first pass and resolving function calls in the second pass. After processing, it clears the temporary AST cache and returns the final structured results.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **results** (`list`): A list of dictionaries containing the structured call graph results.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private utility method is responsible for recursively traversing the project directory starting from the configured root path. It uses os.walk to iterate through directories and files, applying filtering to exclude directories listed in self.ignore_dirs. It collects the absolute paths of all files ending with ".py" and returns this list.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths for all Python files found in the project, excluding ignored directories.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This method reads a specified Python file, parses its source code into an Abstract Syntax Tree (AST), and temporarily stores the AST. It then walks the AST to identify all function, method, and class definitions. For each definition, it constructs a fully qualified path name, determines its type, and stores this metadata (file path, line number, type) in the self.definitions dictionary for later use in call resolution. Error handling is included to log parsing failures.
        *   *Parameters:*
            - **filepath** (`string`): The path to the Python file whose definitions are to be collected.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This is a utility method designed to find the direct parent AST node of a given child node within a file's AST. It iterates through all nodes in the tree, checking the children of each potential parent node. If a match is found, the parent node is returned; otherwise, it returns None.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root AST node of the file being analyzed.
            - **node** (`ast.AST`): The child node for which the parent is being sought.
        *   *Returns:*
            - **parent** (`ast.AST or None`): The parent AST node of the input node, or None if no parent is found.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This method handles the second pass of analysis, focusing on identifying function and method calls within a specific file. It retrieves the file's AST and instantiates an external CallResolverVisitor with the necessary context (definitions and project path). The visitor traverses the AST to collect call information, which is then merged into the main self.call_graph structure, mapping callees to their respective callers. Errors during call resolution are logged.
        *   *Parameters:*
            - **filepath** (`string`): The path to the Python file whose function calls need to be resolved.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* This method transforms the raw data stored in self.call_graph and self.definitions into a clean, structured list suitable for final output. It iterates through all entities that were called, retrieves their definition metadata, and aggregates the list of callers. It ensures that caller information is deduplicated and sorted by file and line number before being packaged into a final dictionary format.
        *   *Parameters:*
            - Analysis data not available for this component.
        *   *Returns:*
            - **output_list** (`list[dict]`): A list of dictionaries, where each dictionary represents a defined entity and includes a structured list of all unique locations where it is called.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor is an Abstract Syntax Tree (AST) visitor designed to analyze a Python file and identify all function and method calls, resolving them to their fully qualified names (QNames). It maintains context about the current module, class, and function to accurately determine the caller's identity and type. By processing imports and assignments, it builds a scope map and tracks instance types, which are crucial for resolving method calls on objects. The primary output is a dictionary, `self.calls`, mapping resolved callee QNames to a list of caller contexts.
*   **Instantiation:** This class is instantiated by the `_resolve_calls` function located in `relationship_analyzer.py`.
*   **Dependencies:** The class relies on the standard `ast` module for AST traversal, `os` for path manipulation, `collections.defaultdict` for storing call data, and an external utility `path_to_module` for determining the module path.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with file context, project structure information, and a set of known definitions. It sets up internal state variables, including `self.scope` for import tracking, `self.instance_types` for object type resolution, and `self.calls` (a defaultdict) to store the resulting call graph data.
    *   *Parameters:*
        - **filepath** (`string`): The path to the source file currently being analyzed.
        - **project_root** (`string`): The root directory of the project, used to calculate the module path.
        - **definitions** (`dict`): A collection of known fully qualified names (QNames) in the project, used to validate resolved calls.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method overrides the standard AST visitor behavior to handle class definitions. It implements context management by saving the current class name before traversing the class body and restoring it upon exit. This ensures that methods defined within the class are correctly identified as belonging to that class during call resolution.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles function and method definitions, managing the context of the current caller. It saves the existing caller name, sets the new caller name based on the function definition node, traverses the function body, and then restores the previous caller name. This allows `visit_Call` to accurately identify the function or method making a call.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function or method definition.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This is the core method for identifying and recording function and method calls. It first attempts to resolve the callee's fully qualified name using the private helper `_resolve_call_qname`. If the callee is successfully resolved and is a known definition, the method determines the caller's type ('module', 'method', or 'function') and records the caller's context (file, line, and name) against the callee's QName in the `self.calls` dictionary.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing the function call expression.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes simple import statements (e.g., `import module` or `import module as alias`). It updates the `self.scope` dictionary by mapping the imported name or its alias to the original module name. This scope information is later used by `_resolve_call_qname` to resolve calls to imported modules.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing the import statement.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `from ... import ...` statements, including handling relative imports. It calculates the fully qualified path of the imported module, resolving relative imports based on the current module path and the import level. It then maps the imported name (or alias) to its full QName in `self.scope` for accurate call resolution.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing the import-from statement.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method is responsible for tracking the types of instantiated objects. It checks if an assignment involves a function call (typically a constructor). If the called name is a known class, it records the qualified class name in `self.instance_types`, mapping it to the assigned variable name. This mapping is essential for resolving method calls on instances later in the traversal.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing the assignment statement.
        *   *Returns:*
            - Analysis data not available for this component.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper function attempts to resolve the fully qualified name (QName) of a function or method call based on the AST node representing the function being called. It handles two main scenarios: resolving simple names (local or imported functions) by checking `self.scope`, and resolving attribute access (method calls) by checking `self.instance_types` for instance methods or `self.scope` for module-level functions.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., ast.Name or ast.Attribute).
        *   *Returns:*
            - **qname** (`string | None`): The fully qualified name of the function or method, or None if the name cannot be resolved.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a file system path (`filepath`) into a standard Python module path string, which is dot-separated. It first attempts to calculate the path relative to the provided project root using `os.path.relpath`, falling back to the base filename if a `ValueError` occurs. If the path ends with the `.py` extension, it is removed. Finally, it replaces all operating system path separators with dots and handles the special case where the module path ends in `.__init__`, removing that suffix to correctly represent the package path.
*   **Parameters:**
    - **filepath** (`string`): The file system path (absolute or relative) that needs to be converted into a module path.
    - **project_root** (`string`): The root directory of the project, used as the base reference for calculating the relative module path.
*   **Returns:**
    - **module_path** (`string`): The resulting dot-separated Python module path, adjusted to represent packages correctly if the input was an `__init__.py` file.
*   **Usage:**
    *   **Calls:** This function utilizes path manipulation functions from the 'os' module, specifically 'relpath' and 'basename', and standard string methods like 'endswith' and 'replace'.
    *   **Called by:** This function is utilized by the methods '_collect_definitions' and '__init__' within 'relationship_analyzer.py'.

---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** This function is responsible for encrypting a given plaintext string using a globally available `cipher_suite` object. Before proceeding, it checks if the input `text` is non-empty and if the `cipher_suite` is initialized; if either condition is false, the original text is returned unencrypted. If encryption is performed, the input string is first encoded into bytes, encrypted using the cipher suite's `encrypt` method, and the resulting ciphertext bytes are then decoded back into a string before being returned.
*   **Parameters:**
    - **text** (`str`): The plaintext string that needs to be encrypted.
*   **Returns:**
    - **Encrypted Text** (`str`): The base64-encoded, encrypted version of the input text, or the original text if the input was empty or the cipher suite was not initialized.
*   **Usage:**
    *   **Calls:** This function calls methods to encode the string to bytes, encrypt the bytes using the `cipher_suite`, and decode the resulting ciphertext back into a string.
    *   **Called by:** This function is called by `update_gemini_key`.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** This function attempts to decrypt a given string input using a globally available `cipher_suite` object. It first checks if the input text is empty or if the `cipher_suite` is not initialized; if either is true, it returns the original text immediately. If decryption proceeds, the input string is encoded to bytes, decrypted using the cipher suite, and then decoded back into a string. The entire decryption process is wrapped in a try/except block to ensure that if any exception occurs (e.g., decryption failure or invalid token), the original text is returned safely.
*   **Parameters:**
    - **text** (`str`): The string content that needs to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The successfully decrypted string, or the original input string if decryption failed or was skipped.
*   **Usage:**
    *   **Calls:** This function calls methods for encoding, decrypting using cipher_suite, and decoding the resulting bytes back into a string.
    *   **Called by:** This function is called by `get_decrypted_api_keys`.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function handles the creation and persistence of a new user record in the database. It accepts the user's username, display name, and raw password as input. It constructs a user dictionary, using the username as the primary key (\"_id\") and securely hashing the provided password using an external authentication utility (stauth.hasher.hash). The user document is initialized with empty strings for 'gemini_api_key' and 'ollama_base_url'. The function then inserts this prepared dictionary into the dbusers collection via insert_one and returns the unique ID assigned to the new document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which is stored as the document's _id.
    - **name** (`str`): The display name associated with the user account.
    - **password** (`str`): The raw, unhashed password provided by the user, which is hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The _id of the newly created user document, which corresponds to the provided username.
*   **Usage:**
    *   **Calls:** This function calls a hashing utility (hash) to secure the password and a database method (insert_one) to persist the user data.
    *   **Called by:** This function is not explicitly called by any other functions listed in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is designed to query and retrieve all user records stored in the database. It accesses the `dbusers` collection object and executes the `find()` method, which typically returns all documents in that collection. The resulting iterable of documents, which represent the users, is then converted into a standard Python list. This list of user documents is finally returned to the caller.
*   **Parameters:**
    - Analysis data not available for this component.
*   **Returns:**
    - **users** (`list`): A list containing all user documents (likely dictionaries or BSON documents) retrieved from the database collection `dbusers`.
*   **Usage:**
    *   **Calls:** This function calls the `find` method on the `dbusers` object to query the database and uses the built-in `list` constructor to materialize the results.
    *   **Called by:** This function is called by the `frontend.Frontend` component.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** This function is responsible for querying a database collection to retrieve a single user record based on their username. It uses the input `username` as the primary key (`_id`) for the lookup operation. The function executes a `find_one` operation on the `dbusers` object, which is inferred to be a MongoDB collection instance due to the context imports. It returns the resulting document if a match is found, or typically returns None otherwise.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user record, which is mapped to the _id field in the database query.
*   **Returns:**
    - **user** (`dict or None`): The user document retrieved from the database, or None if no user matching the username is found.
*   **Usage:**
    *   **Calls:** This function relies on calling the `find_one` method, likely belonging to a MongoDB collection object named `dbusers`, to execute the database query.
    *   **Called by:** Based on the provided context, this function is not called by any other known components.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function updates the Gemini API key associated with a specific user in the database. It first ensures the security of the provided API key by encrypting it using the `encrypt_text` utility function. Subsequently, it executes a database update operation on the `dbusers` collection, matching the document by the provided `username` and setting the `gemini_api_key` field to the encrypted value. The function returns an integer indicating the success of the database modification.
*   **Parameters:**
    - **username** (`str`): The unique identifier (user ID) of the user whose API key needs to be updated.
    - **gemini_api_key** (`str`): The new, unencrypted Gemini API key provided by the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the database update operation (typically 1 upon success).
*   **Usage:**
    *   **Calls:** This function calls `encrypt_text` to encrypt the API key and utilizes `dbusers.update_one` to perform the database modification.
    *   **Called by:** This function is used by `frontend.Frontend`.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function updates the stored Ollama Base URL for a specific user in a database collection named `dbusers`. It uses the provided `username` as the unique identifier (`_id`) to locate the correct user document. The function then performs a MongoDB `update_one` operation to set the new `ollama_base_url` value. Finally, it returns the count of documents that were successfully modified by the operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (used as the MongoDB _id) of the user whose configuration is being updated.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service that should be stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were updated by the database operation, typically 1 or 0.
*   **Usage:**
    *   **Calls:** This function calls the `update_one` method, likely belonging to a MongoDB collection object (`dbusers`), to perform the database modification.
    *   **Called by:** This function is utilized by the `frontend.Frontend` function within `Frontend.py`.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** This function is designed to securely retrieve the Gemini API key associated with a specific user from a database collection named `dbusers`. It executes a database query using the provided username as the primary identifier (`_id`). The query is optimized to project only the `gemini_api_key` field, minimizing data transfer. The function then uses the `.get()` method on the resulting user document to safely extract and return the API key.
*   **Parameters:**
    - **username** (`str`): The unique string identifier used to locate the user record in the database.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key string retrieved from the user's database record, or None if the key is not present in the document.
*   **Usage:**
    *   **Calls:** This function calls `find_one` on the `dbusers` object (likely a MongoDB collection) to retrieve a single user record, and then calls the dictionary method `get` on the result to safely access the API key.
    *   **Called by:** This function is not explicitly called by any other functions listed in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** This function is designed to retrieve the configured Ollama base URL for a specific user. It accepts the user's username, which is used as the primary key (`_id`) to query the `dbusers` collection. The query is optimized to only return the `ollama_base_url` field. The function then extracts this URL using the dictionary's `get` method and returns the result.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) used to locate the user's record in the database.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The base URL configured for the Ollama service for the specified user, or None if the user is not found or the field is missing.
*   **Usage:**
    *   **Calls:** This function utilizes `find_one` on the `dbusers` object to query the database and subsequently calls the dictionary method `get` on the returned document.
    *   **Called by:** This function is not currently tracked as being called by any other function in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** This function is designed to remove a single user record from a database collection, likely named 'dbusers'. It accepts a username, which is used as the primary key ('_id') to locate the specific document for deletion. The function executes a `delete_one` operation against the collection. It returns the count of documents that were successfully removed by the operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) corresponding to the '_id' field of the user document intended for deletion.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation, typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls `database/db.py::delete_one` (via the `dbusers` object) to perform the database deletion operation.
    *   **Called by:** This function is not called by any other tracked functions in the current context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function retrieves a user record from the database collection `dbusers` using the provided `username` as the primary key (`_id`). If the user is not found, it immediately returns a tuple of (None, None). If the user exists, it extracts the potentially encrypted `gemini_api_key` and decrypts it using the external function `decrypt_text`. It also retrieves the `ollama_base_url` directly from the user object. Finally, it returns the decrypted Gemini key and the Ollama base URL.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to look up the user in the `dbusers` collection.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user was not found.
    - **ollama_plain** (`str | None`): The Ollama base URL, or None if the user was not found.
*   **Usage:**
    *   **Calls:** This function calls `decrypt_text` to decrypt the API key, and utilizes database methods like `find_one` and dictionary access via `get`.
    *   **Called by:** This function is called by `frontend.Frontend` in `Frontend.py`.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time)`
*   **Description:** This function handles the persistence of a single conversation exchange record into a database collection, likely managed by PyMongo. It accepts core exchange details such as the question, answer, feedback, user identifiers, and various timing metrics. It constructs a complete document, automatically adding a current timestamp via `datetime.now()`, and inserts it into the `dbexchanges` collection. The primary purpose is to log user interactions and performance data.
*   **Parameters:**
    - **question** (`str`): The text of the question or prompt provided by the user.
    - **answer** (`str`): The text of the response generated by the system.
    - **feedback** (`str`): The feedback string provided by the user regarding the answer.
    - **username** (`str`): The identifier of the user who initiated the exchange.
    - **chat_name** (`str`): The name or identifier of the specific chat session.
    - **helper_used** (`str`): Optional field indicating which helper model was utilized. Defaults to an empty string.
    - **main_used** (`str`): Optional field indicating which main model was utilized. Defaults to an empty string.
    - **total_time** (`str`): Optional field recording the total time taken for the exchange. Defaults to an empty string.
    - **helper_time** (`str`): Optional field recording the time taken by the helper model. Defaults to an empty string.
    - **main_time** (`str`): Optional field recording the time taken by the main model. Defaults to an empty string.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier (ID) generated by the database for the newly inserted exchange document.
*   **Usage:**
    *   **Calls:** This function calls `dbexchanges.insert_one` to save the constructed document and `datetime.now()` to set the creation timestamp.
    *   **Called by:** This function is primarily used by the `frontend.Frontend` function.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** This function is designed to retrieve all exchange records associated with a specific user from a database collection named `dbexchanges`. It takes a username as input and uses it to construct a query filter. The function executes a database `find` operation using this filter. Finally, it converts the resulting database cursor into a standard Python list, which is then returned to the caller.
*   **Parameters:**
    - **username** (`str`): The unique identifier or name of the user whose exchange records are to be fetched from the database.
*   **Returns:**
    - **exchanges** (`list`): A list containing all exchange documents found in the database where the 'username' field matches the input argument.
*   **Usage:**
    *   **Calls:** This function calls the database method `dbexchanges.find` to execute the query and the built-in function `list` to materialize the results.
    *   **Called by:** This function is utilized by `load_data_from_db` located in `Frontend.py`.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function is responsible for querying a database collection, likely named 'dbexchanges', to retrieve specific records. It filters the records based on two criteria: the provided username and the chat name. The database query result, which is typically an iterable cursor, is immediately converted into a standard Python list containing the matching exchange records before being returned to the caller.
*   **Parameters:**
    - **username** (`str`): The username used as a primary key or filter criterion in the database query.
    - **chat_name** (`str`): The name of the chat used as a secondary filter criterion in the database query.
*   **Returns:**
    - **exchanges** (`list`): A list containing all database records (exchanges) that match the specified username and chat name.
*   **Usage:**
    *   **Calls:** This function calls a database `find` method (likely on a MongoDB collection object named `dbexchanges`) and the built-in `list` constructor.
    *   **Called by:** This function is not called by any other functions listed in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function is responsible for updating the feedback score associated with a specific exchange record in the database. It takes an exchange identifier and the new integer feedback value as input. It executes a targeted update operation using the dbexchanges collection, setting the 'feedback' field for the document matching the provided exchange_id. The function returns the count of documents that were successfully modified by the operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier used to locate the specific exchange record to be updated in the database.
    - **feedback** (`int`): The new integer value representing the feedback score to be stored for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents (typically 0 or 1) that were modified by the database update operation.
*   **Usage:**
    *   **Calls:** This function calls the database method update_one (likely belonging to a MongoDB collection object named dbexchanges) to execute the update.
    *   **Called by:** This function is utilized by handle_feedback_change in Frontend.py.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function updates the feedback message associated with a specific exchange record in the database. It interacts with the `dbexchanges` collection, which is presumed to be a MongoDB interface. The function locates the target document using the provided `exchange_id` as the document's `_id`. It then uses the MongoDB `$set` operator to update the `feedback_message` field with the new string value. The function returns a count of the documents successfully modified.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier (likely a MongoDB ObjectId or string) used to locate the specific exchange document to be updated.
    - **feedback_message** (`str`): The new string content for the feedback message field.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the database update operation.
*   **Usage:**
    *   **Calls:** This function executes a database update operation by calling the `update_one` method on the `dbexchanges` collection object.
    *   **Called by:** This function is utilized by the `render_exchange` function located in the `Frontend.py` module.

#### Function: `delete_chats_by_user`
*   **Signature:** `def delete_chats_by_user(username, chat_name)`
*   **Description:** This function deletes all database records associated with a specific user and a named chat session. It constructs a query dictionary using the provided username and chat name. The function executes a bulk deletion operation using `dbexchanges.delete_many` based on this criteria. The primary purpose is to clean up chat history for a user. It returns the count of records that were successfully removed.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose chat exchanges are to be deleted.
    - **chat_name** (`str`): The specific name of the chat session whose exchanges are to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The total number of documents (exchanges) that were successfully deleted from the collection, derived from the result object of the delete operation.
*   **Usage:**
    *   **Calls:** This function calls `delete_many` on the `dbexchanges` object, likely a MongoDB collection interface, to execute the deletion query.
    *   **Called by:** This function is called by `handle_delete_chat` located in `Frontend.py`.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function is responsible for removing a single exchange record from the database collection referenced by `dbexchanges`. It takes the unique identifier of the exchange (`exchange_id`) and constructs a query to target that specific document using the `_id` field. The deletion operation is executed by calling `delete_one` on the collection object. Finally, the function returns the number of documents successfully deleted, which is typically 1 upon success or 0 if the document was not found.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier string used to locate and delete the specific exchange record in the database.
*   **Returns:**
    - **deleted_count** (`int`): The total number of documents that were successfully deleted by the operation (0 or 1).
*   **Usage:**
    *   **Calls:** This function performs a database operation by calling the `delete_one` method, which is likely part of a PyMongo collection object named `dbexchanges`.
    *   **Called by:** This function is utilized by `handle_delete_exchange` located in `Frontend.py`.

---
### File: `frontend/Frontend.py`
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** This function is responsible for loading existing chat exchanges from the database and initializing the Streamlit session state for a given user. It first checks if the data has already been loaded using a session state flag to prevent redundant operations. It retrieves all exchanges associated with the provided username via a call to `db.fetch_exchanges_by_user`. The exchanges are then processed, grouped by chat name, and stored in `st.session_state.chats`. Exchanges missing feedback are standardized by setting the feedback value to `np.nan`. Finally, if no chats are loaded, a default 'Chat 1' is created and set as the active chat, and the data loading process is marked complete.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose existing chat exchanges should be fetched and loaded into the session state.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** The function primarily calls `db.fetch_exchanges_by_user` to retrieve user data, and uses standard list and dictionary methods such as `append`, `get`, `keys`, and `list` for data structuring.
    *   **Called by:** This function is called by `frontend.Frontend`.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function handles updating the feedback associated with a specific exchange object. It takes the exchange object (\"ex\") and the new feedback value (\"val\"). The function first updates the local state of the exchange object by setting the 'feedback' key. It then persists this change to the database by calling a dedicated update function using the exchange's identifier ('_id'). Finally, it triggers a full application rerun using st.rerun() to ensure the UI reflects the updated state.
*   **Parameters:**
    - **ex** (`dict`): The exchange object, which is expected to be a dictionary containing the current state and a unique identifier ('_id').
    - **val** (`Any`): The new value for the feedback field.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** This function calls `db.update_exchange_feedback` to persist the data change and `st.rerun` to refresh the application interface.
    *   **Called by:** This function is called by the `render_exchange` function.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of a specific exchange object, removing it from both the persistent database and the current Streamlit session state. It first uses the `_id` of the exchange object to call a database function for permanent deletion. It then removes the exchange object from the list of exchanges associated with the specified chat name within `st.session_state`. Finally, it forces a complete application refresh by calling `st.rerun()` to ensure the UI reflects the deletion immediately.
*   **Parameters:**
    - **chat_name** (`str`): The identifier or name of the chat session containing the exchange to be deleted.
    - **ex** (`dict`): The exchange object (containing the '_id' field) that needs to be deleted from the database and the session state.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** This function calls `db.delete_exchange_by_id` to remove the record from the database, accesses the session state to call the list `remove` method, and finally invokes `st.rerun` to refresh the Streamlit application.
    *   **Called by:** This function is utilized by `render_exchange` in `Frontend.py` at line 146.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function handles the complete deletion of a specified chat session for a given user. It performs two primary deletion actions: first, it removes the chat data from the underlying database using `db.delete_chats_by_user`. Second, it deletes the chat entry from the Streamlit session state (`st.session_state.chats`). After deletion, it manages the active chat state: if other chats exist, the first remaining chat is set as active; otherwise, a new default chat named \"Chat 1\" is created. Finally, the function calls `st.rerun()` to force a refresh of the Streamlit application interface.
*   **Parameters:**
    - **username** (`str`): The identifier of the user who owns the chat being deleted.
    - **chat_name** (`str`): The specific name of the chat session to be removed.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** This function calls `db.delete_chats_by_user` to interact with the database, and uses `len`, `list`, and dictionary methods like `keys` for state management, concluding with `st.rerun` to update the application interface.
    *   **Called by:** This function is called by `frontend.Frontend`.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text)`
*   **Description:** This function processes input markdown text to identify and graphically render embedded Mermaid diagrams. It first checks for empty input and returns if none is provided. It uses regular expressions to split the text based on ```mermaid delimiters, separating regular text from the diagram code. Regular text segments are rendered using st.markdown. Mermaid code segments are passed to st_mermaid for visualization, with a safety fallback to rendering the raw code using st.code if the diagram generation encounters an exception.
*   **Parameters:**
    - **markdown_text** (`str`): The input text string which may contain standard markdown and embedded Mermaid diagram definitions.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** This function utilizes the re.split method to parse the input string, iterates using enumerate, generates unique keys using hash, and relies on Streamlit functions like st.markdown, st_mermaid, and st.code for rendering output.
    *   **Called by:** This function is invoked by render_exchange and is also referenced within the frontend.Frontend module context.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function is responsible for rendering a single chat exchange (user question and assistant answer) within a Streamlit application. It first displays the user's question using a 'user' chat message. It then renders the assistant's response within an 'assistant' chat message, which includes a comprehensive toolbar for interaction. The toolbar allows users to provide positive or negative feedback, write a detailed feedback message (which is saved to the database via `db.update_exchange_feedback_message`), download the response as Markdown, and delete the exchange via `handle_delete_exchange`. Finally, the assistant's answer is displayed in a scrollable container and processed by `render_text_with_mermaid` for content rendering.
*   **Parameters:**
    - **ex** (`dict`): The exchange object containing the chat data, including 'question', 'answer', '_id', and current 'feedback' status.
    - **current_chat_name** (`str`): The identifier of the current chat session, required for handling the deletion of the exchange.
*   **Returns:**
    - Analysis data not available for this component.
*   **Usage:**
    *   **Calls:** This function utilizes numerous Streamlit UI components (e.g., chat_message, columns, button, popover, text_area, download_button, rerun, success), interacts with the database via `db.update_exchange_feedback_message`, and calls internal helper functions like `handle_feedback_change`, `handle_delete_exchange`, and `render_text_with_mermaid` for displaying content.
    *   **Called by:** This function is called by the main rendering logic within the `frontend.Frontend` module.

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic data model designed to strictly define the attributes necessary to describe a single parameter of a function. It acts as a standardized schema for capturing the parameter's name, its type (as a string), and a descriptive explanation of its role. This model is a foundational component used across the system for documenting and analyzing function signatures.
*   **Instantiation:** The instantiation context for this class was not provided in the input data.
*   **Dependencies:** This class relies on Pydantic's BaseModel for defining its structure and enabling automatic data validation.
*   **Constructor:**
    *   *Description:* The class uses the Pydantic-generated constructor to initialize its attributes. It requires three mandatory string arguments: name, type, and description, ensuring that every instance fully describes a function parameter upon creation.
    *   *Parameters:*
        - **name** (`str`): The name of the function parameter.
        - **type** (`str`): The type hint or inferred type of the parameter, represented as a string.
        - **description** (`str`): A detailed textual explanation of the parameter's purpose and usage.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic data model designed to structure information about the return value of a function. It serves as a schema component, ensuring that return descriptions consistently include the name, data type, and a textual explanation of the value being returned. This structure is essential for automated documentation or code analysis systems.
*   **Instantiation:** This class is a schema definition and is instantiated whenever a structured description of a function's return value is required, typically within other schema definitions or data processing logic.
*   **Dependencies:** The class relies on pydantic.BaseModel for its structure, validation, and automatic constructor generation.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor automatically handles validation and initialization of the instance attributes based on the provided keyword arguments: name, type, and description.
    *   *Parameters:*
        - **name** (`str`): The identifier or name of the returned value.
        - **type** (`str`): The data type of the returned value (e.g., \"List[str]\", \"int\").
        - **description** (`str`): A textual explanation of what the returned value represents.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `UsageContext`
*   **Summary:** This class is a Pydantic data model designed to structure and validate information regarding the calling context of a function or method. It strictly defines two string fields, 'calls' and 'called_by', which are intended to hold human-readable summaries detailing the entity's dependencies and where it is utilized within the codebase.
*   **Instantiation:** The instantiation points are not provided in the context, but this class is typically used internally within the system to structure analysis results.
*   **Dependencies:** This class depends on pydantic.BaseModel to provide data validation and structured data capabilities.
*   **Constructor:**
    *   *Description:* As a subclass of Pydantic's BaseModel, the constructor for UsageContext is automatically generated. It initializes and validates the required 'calls' and 'called_by' attributes, ensuring they are provided as strings upon object creation.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the external functions, methods, or classes that this entity calls.
        - **called_by** (`str`): A string summarizing the external functions or methods that call this entity.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic data model designed to store the complete, structured analysis of a single Python function. It acts as a container for documentation generated by an automated analysis process. It strictly defines four key components: the function's general purpose, its input parameters, its return values, and its usage context within the larger codebase.
*   **Instantiation:** The instantiation context for this data structure is not provided in the input context.
*   **Dependencies:** This class does not appear to have external functional dependencies, relying primarily on standard Pydantic functionality for data validation.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the class is initialized by accepting keyword arguments corresponding to its defined fields, ensuring data validation upon instantiation. It sets up the core structure for storing function analysis data.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the function's purpose.
        - **parameters** (`List[ParameterDescription]`): A list of objects describing each input parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of objects describing the function's return values.
        - **usage_context** (`UsageContext`): An object detailing the function's calling context and external calls.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic data model designed to hold the complete, structured analysis of a single Python function or method. It acts as a container, requiring a unique string identifier for the function and a detailed description object (FunctionDescription) which contains the functional breakdown. It also includes an optional field for capturing errors encountered during the function's analysis, ensuring robustness in the documentation generation pipeline.
*   **Instantiation:** The instantiation points for this class were not provided in the input context.
*   **Dependencies:** This class does not explicitly rely on other components within the analyzed system, though it depends on external libraries like Pydantic.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the class uses an implicit constructor to initialize its fields. It requires the function's identifier and its detailed description object, while the error field is optional and defaults to None.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): A nested object containing the detailed analysis of the function, including parameters, returns, and overall summary.
        - **error** (`Optional[str]`): An optional field used to store an error message if the analysis of the function failed or encountered issues.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic data model designed to hold structured metadata about the __init__ method of a Python class. It defines two core fields: a general string summary of the constructor's function and a list of detailed parameter descriptions. This structure is essential for systems that analyze and document class definitions programmatically, ensuring consistency when representing constructor metadata.
*   **Instantiation:** The context does not specify where this class is instantiated.
*   **Dependencies:** This class relies on Pydantic's BaseModel for defining its structure and enforcing data validation.
*   **Constructor:**
    *   *Description:* The constructor is automatically generated by Pydantic's BaseModel. It initializes the instance attributes `description` (a string summarizing the constructor) and `parameters` (a list of parameter descriptions, which must conform to the `ParameterDescription` schema).
    *   *Parameters:*
        - **description** (`str`): A string containing a high-level summary of the constructor's purpose.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each detailing a specific parameter accepted by the constructor.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a simple Pydantic data model designed to encapsulate the usage context of another class within a software system. It inherits from BaseModel and defines two required string fields: one for listing external dependencies and another for specifying where the class is instantiated. This structure ensures that critical contextual information is consistently tracked and validated.
*   **Instantiation:** Based on the provided context, there are no explicit instantiation points listed for this class.
*   **Dependencies:** Based on the provided context, there are no explicit external dependencies listed for this class.
*   **Constructor:**
    *   *Description:* The constructor is automatically generated by Pydantic's BaseModel. It requires two string arguments, `dependencies` and `instantiated_by`, which are used to initialize the corresponding instance attributes.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the class's external dependencies.
        - **instantiated_by** (`str`): A string describing the primary points of instantiation for the class.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic data model designed to encapsulate the comprehensive, structured analysis of a target Python class. It acts as the primary output schema for class analysis, organizing information into four key components: a general summary of the class's role, detailed information about its constructor, a list of structured analyses for each of its methods, and contextual data regarding its usage within a larger system. This model ensures that class documentation is generated from a consistent, machine-readable format.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly rely on external dependencies within the provided context, aside from inheriting from pydantic.BaseModel and using standard Python typing constructs.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is implicitly generated to accept and validate the four required fields: overall summary, constructor description, method analyses list, and usage context.
    *   *Parameters:*
        - **overall** (`str`): The high-level summary of the class's purpose.
        - **init_method** (`ConstructorDescription`): The structured analysis of the class's constructor (__init__).
        - **methods** (`List[FunctionAnalysis]`): A list containing the structured analysis of all methods defined within the class.
        - **usage_context** (`ClassContext`): Contextual information regarding the class's dependencies and instantiation points.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class is a Pydantic BaseModel that defines the root structure for storing a complete, structured analysis of a Python class. It acts as a container for the class's name, the detailed analysis object (ClassDescription), and an optional error message. This model ensures that the output of the class analysis process is standardized and machine-readable.
*   **Instantiation:** The instantiation context for this class is not provided in the input.
*   **Dependencies:** This class has no external functional dependencies listed in the context, relying primarily on Pydantic for structure.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel. It initializes the data structure by requiring the class identifier and the detailed description object, while the error field is optional and defaults to None.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or path of the class being analyzed.
        - **description** (`ClassDescription`): The nested object containing the detailed analysis of the class, including methods and context.
        - **error** (`Optional[str]`): An optional field used to store an error message if the analysis process failed.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a single call event identified during code analysis. It standardizes the metadata required to track relationships, such as where a function was called or a class was instantiated. It stores critical information including the file path, the name of the calling function, the mode of the caller (e.g., 'method'), and the exact line number of the call.
*   **Instantiation:** The context does not specify where this class is instantiated.
*   **Dependencies:** This class appears to have no explicit external functional dependencies listed in the provided context, relying primarily on the Pydantic BaseModel for structure.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel. It initializes the four defined data fields: file, function, mode, and line, ensuring they conform to their specified string and integer types upon instantiation.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call originated.
        - **function** (`str`): The name of the calling function or method (Name des Aufrufers).
        - **mode** (`str`): The type of calling entity (z.B. 'method', 'function', 'module').
        - **line** (`int`): The line number within the file where the call occurred.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic data model designed to structure the contextual information necessary for analyzing a specific function. It defines two primary fields: a list of entities called by the function and a structured list detailing where the function itself is invoked. This structure ensures consistent data validation and typing for function dependency analysis within the system.
*   **Instantiation:** This class is instantiated by the main_workflow function located in the main.py file.
*   **Dependencies:** This class depends on pydantic.BaseModel for its structure and validation capabilities, and relies on List for defining collection types.
*   **Constructor:**
    *   *Description:* The constructor is inherited from pydantic.BaseModel. It initializes the instance by accepting keyword arguments corresponding to the defined fields, `calls` and `called_by`, and performs automatic type validation against the specified type hints.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing the identifiers of functions, methods, or classes that the analyzed function calls.
        - **called_by** (`List[CallInfo]`): A list of structured CallInfo objects providing detailed context about the locations and methods that invoke the analyzed function.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `FunctionAnalysisInput`
*   **Summary:** FunctionAnalysisInput serves as the schema for the data payload required by the system to initiate a function analysis task. Inheriting from Pydantic's BaseModel, it strictly defines the necessary components: the function's identifier, its raw source code, associated imports, and detailed usage context. This structure ensures that all inputs for the analysis pipeline are standardized and validated before processing.
*   **Instantiation:** This class is instantiated within the main_workflow function located in main.py.
*   **Dependencies:** This class has no direct external dependencies listed in the context, but structurally relies on Pydantic's BaseModel for data validation and typing components like Literal and List.
*   **Constructor:**
    *   *Description:* This class is a Pydantic model used to define the structured input required for generating a FunctionAnalysis object. It initializes its state by validating and assigning values to its five defined fields, ensuring the 'mode' is strictly set to \"function_analysis\".
    *   *Parameters:*
        - **mode** (`Literal[\"function_analysis\"]`): Specifies the processing mode, which must be fixed to the literal string 'function_analysis'.
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **source_code** (`str`): The raw source code string of the entire function definition.
        - **imports** (`List[str]`): A list of import statements relevant to the function's execution context.
        - **context** (`FunctionContextInput`): A nested Pydantic model containing additional contextual information, such as function calls and dependencies.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic data model designed to structure and store comprehensive contextual information about a specific method within a code analysis workflow. It acts as a schema for capturing the method's identity, its internal dependencies (calls), its external usage points (called_by), its argument signature, and its associated documentation (docstring). This model ensures that method context data is consistently formatted and validated.
*   **Instantiation:** This class is instantiated within the main_workflow function located in main.py.
*   **Dependencies:** This class has no explicit external functional dependencies beyond its base class, pydantic.BaseModel, and standard Python types.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the class constructor is implicitly generated. It accepts keyword arguments corresponding to its defined attributes: identifier, calls, called_by, args, and docstring. Pydantic handles type validation and assignment during instantiation.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method being analyzed.
        - **calls** (`List[str]`): A list of strings representing the names of functions, methods, or classes that this method calls internally.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects detailing the locations and contexts where this method is invoked by other parts of the codebase.
        - **args** (`List[str]`): A list of strings representing the names of the arguments defined in the method's signature.
        - **docstring** (`Optional[str]`): The documentation string (docstring) associated with the method, which may be null if none exists.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput is a Pydantic data model designed to structure all necessary contextual information required for a comprehensive analysis of a target Python class. It serves as a container for metadata, including external dependencies, locations where the class is instantiated, and detailed usage context for each of its methods. This structure ensures that downstream analysis systems receive a complete and standardized input payload for processing.
*   **Instantiation:** This class is instantiated by the main_orchestrator function in HelperLLM.py and the main_workflow function in main.py.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The class inherits its constructor from pydantic.BaseModel. It initializes the instance attributes based on the provided data for dependencies, instantiation points, and method-specific context lists, enforcing type validation upon creation.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of external dependencies required by the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list detailing where the class being analyzed is instantiated within the codebase.
        - **method_context** (`List[MethodContextInput]`): A list containing context information for each method within the class being analyzed.
*   **Methods:**
    - Analysis data not available for this component.

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel that defines the required schema for input data used to generate a ClassAnalysis object. It acts as a standardized contract for the AI Code Analyst, ensuring all necessary components\r\n—mode, identifier, source code, imports, and context—are provided and correctly typed. This structure facilitates reliable data transfer and validation before the analysis process begins.
*   **Instantiation:** This class is instantiated by the main_orchestrator function in HelperLLM.py and the main_workflow function in main.py.
*   **Dependencies:** This class relies on pydantic.BaseModel for schema definition and validation, and uses standard typing utilities like List and Literal.
*   **Constructor:**
    *   *Description:* The constructor is inherited from pydantic.BaseModel, which handles the validation and assignment of the defined fields. It ensures that the input data conforms to the specified types and constraints upon instantiation.
    *   *Parameters:*
        - **mode** (`Literal[\"class_analysis\"]`): A literal string specifying the operation mode, which must be 'class_analysis'.
        - **identifier** (`str`): The unique identifier or name of the class being analyzed.
        - **source_code** (`str`): The raw source code string of the entire class definition.
        - **imports** (`List[str]`): A list of strings representing the import statements relevant to the source file containing the class.
        - **context** (`ClassContextInput`): A nested data structure providing additional context about dependencies and usage.
*   **Methods:**
    - Analysis data not available for this component.

---
# Project Documentation: repo-onboarding-agent

## 1. Project Overview
- **Description:** This project implements an AI-powered documentation agent that analyzes a given Git repository to automatically generate comprehensive technical documentation. It leverages multiple LLMs (Helper LLMs for detailed code component analysis and a Main LLM for report synthesis) to process repository structure, code dependencies, function, and class details. A Streamlit frontend provides a user interface for interaction.
- **Key Features:**
  - Automated Git Repository Analysis
  - Abstract Syntax Tree (AST) Generation & Enrichment
  - LLM-powered Function and Class Documentation
  - Comprehensive Markdown Report Generation
  - Interactive Streamlit User Interface
- **Tech Stack:** Python, Streamlit, LangChain, Google Generative AI (Gemini), OpenAI, Ollama, Pydantic, GitPython, NetworkX, MongoDB (via PyMongo), Matplotlib.

*   **Repository Structure:**
    ```mermaid
    graph LR
    ProjectRoot["repo-onboarding-agent<br/>.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt"]
    ProjectRoot_SystemPrompts["SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt"]
    ProjectRoot_backend["backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py"]
    ProjectRoot_database["database<br/>db.py"]
    ProjectRoot_frontend["frontend<br/>Frontend.py<br/>__init__.py"]
    ProjectRoot_frontend__streamlit["_streamlit<br/>config.toml"]
    ProjectRoot_frontend_gifs["gifs<br/>4j.gif"]
    ProjectRoot_notizen["notizen<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
    ProjectRoot_notizen_grafiken["grafiken"]
    ProjectRoot_notizen_grafiken_1["1<br/>File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
    ProjectRoot_notizen_grafiken_2["2<br/>FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot"]
    ProjectRoot_notizen_grafiken_Flask_Repo["Flask-Repo<br/>__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot"]
    ProjectRoot_notizen_grafiken_Repo_onboarding["Repo-onboarding<br/>AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot"]
    ProjectRoot_result["result<br/>ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
    ProjectRoot_schemas["schemas<br/>types.py"]
    ProjectRoot_statistics["statistics<br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png"]
    ProjectRoot --> ProjectRoot_SystemPrompts
    ProjectRoot --> ProjectRoot_backend
    ProjectRoot --> ProjectRoot_database
    ProjectRoot --> ProjectRoot_frontend
    ProjectRoot --> ProjectRoot_notizen
    ProjectRoot --> ProjectRoot_result
    ProjectRoot --> ProjectRoot_schemas
    ProjectRoot --> ProjectRoot_statistics
    ProjectRoot_frontend --> ProjectRoot_frontend__streamlit
    ProjectRoot_frontend --> ProjectRoot_frontend_gifs
    ProjectRoot_notizen --> ProjectRoot_notizen_grafiken
    ProjectRoot_notizen_grafiken --> ProjectRoot_notizen_grafiken_1
    ProjectRoot_notizen_grafiken --> ProjectRoot_notizen_grafiken_2
    ProjectRoot_notizen_grafiken --> ProjectRoot_notizen_grafiken_Flask_Repo
    ProjectRoot_notizen_grafiken --> ProjectRoot_notizen_grafiken_Repo_onboarding
    ```

## 2. Installation
### Dependencies
- altair == 4.2.2
- annotated-types == 0.7.0
- anyio == 4.11.0
- attrs == 25.4.0
- bcrypt == 5.0.0
- blinker == 1.9.0
- cachetools == 6.2.2
- captcha == 0.7.1
- certifi == 2025.11.12
- cffi == 2.0.0
- charset-normalizer == 3.4.4
- click == 8.3.1
- colorama == 0.4.6
- contourpy == 1.3.3
- cryptography == 46.0.3
- cycler == 0.12.1
- distro == 1.9.0
- dnspython == 2.8.0
- dotenv == 0.9.9
- entrypoints == 0.4
- extra-streamlit-components == 0.1.81
- filetype == 1.2.0
- fonttools == 4.61.0
- gitdb == 4.0.12
- GitPython == 3.1.45
- google-ai-generativelanguage == 0.9.0
- google-api-core == 2.28.1
- google-auth == 2.43.0
- googleapis-common-protos == 1.72.0
- grpcio == 1.76.0
- grpcio-status == 1.76.0
- h11 == 0.16.0
- httpcore == 1.0.9
- httpx == 0.28.1
- idna == 3.11
- Jinja2 == 3.1.6
- jiter == 0.12.0
- jsonpatch == 1.33
- jsonpointer == 3.0.0
- jsonschema == 4.25.1
- jsonschema-specifications == 2025.9.1
- kiwisolver == 1.4.9
- langchain == 1.0.8
- langchain-core == 1.1.0
- langchain-google-genai == 3.1.0
- langchain-ollama == 1.0.0
- langchain-openai == 1.1.0
- langgraph == 1.0.3
- langgraph-checkpoint == 3.0.1
- langgraph-prebuilt == 1.0.5
- langgraph-sdk == 0.2.9
- langsmit == 0.4.46
- MarkupSafe == 3.0.3
- matplotlib == 3.10.7
- narwhals == 2.12.0
- networkx == 3.6
- numpy == 2.3.5
- ollama == 0.6.1
- openai == 2.8.1
- orjson == 3.11.4
- ormsgpack == 1.12.0
- packaging == 25.0
- pandas == 2.3.3
- pillow == 12.0.0
- proto-plus == 1.26.1
- protobuf == 6.33.1
- pyarrow == 21.0.0
- pyasn1 == 0.6.1
- pyasn1_modules == 0.4.2
- pycparser == 2.23
- pydantic == 2.12.4
- pydantic_core == 2.41.5
- pydeck == 0.9.1
- PyJWT == 2.10.1
- pymongo == 4.15.4
- pyparsing == 3.2.5
- python-dateutil == 2.9.0.post0
- python-dotenv == 1.2.1
- pytz == 2025.2
- PyYAML == 6.0.3
- referencing == 0.37.0
- regex == 2025.11.3
- requests == 2.32.5
- requests-toolbelt == 1.0.0
- rpds-py == 0.29.0
- rsa == 4.9.1
- setuptools == 75.9.1
- six == 1.17.0
- smmap == 5.0.2
- sniffio == 1.3.1
- streamlit == 1.51.0
- streamlit-authenticator == 0.4.2
- streamlit-mermaid == 0.3.0
- tenacity == 9.1.2
- tiktoken == 0.12.0
- toml == 0.10.2
- toolz == 1.1.0
- toon_format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c9006de6
- tornado == 6.5.2
- tqdm == 4.67.1
- typing-inspect == 0.4.2
- typing_extensions == 4.15.0
- tzdata == 2025.2
- urllib3 == 2.5.0
- watchdog == 6.0.0
- xxhash == 3.6.0
- zstandard == 0.25.0
If `requirements.txt` is present, you can install dependencies using: `pip install -r requirements.txt`

### Setup Guide
Information not found

### Quick Startup
Information not found

## 3. Use Cases & Commands
The `repo-onboarding-agent` is primarily designed to facilitate the rapid understanding and documentation of new or existing Git repositories. Its main use case involves generating comprehensive technical reports that detail the project's structure, dependencies, and code components (functions and classes). It's particularly useful for:
*   **Onboarding new developers**: Quickly generate a project overview and detailed code analysis for faster ramp-up.
*   **Project Auditing**: Obtain a high-level and granular view of a codebase's architecture and functionality.
*   **Automated Documentation**: Maintain up-to-date documentation without manual effort.

**Primary Commands/Interactions:**
*   **Input Repository URL**: Provide a GitHub repository URL via the Streamlit frontend.
*   **Configure LLM Settings**: Select Helper and Main LLM models and provide API keys through the UI.
*   **Generate Documentation**: Trigger the analysis and report generation process via the web interface.
*   **Review & Download Report**: View the generated Markdown report and download it for offline access.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis
### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** The function 'path_to_module' converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases such as when the filepath is not within the project root by falling back to the basename of the file. If the resulting path ends with '.__init__', it removes the trailing segment to normalize the module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    - **module_path** (`str`): A normalized Python module path derived from the input file path.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by the '__init__' method in 'AST_Schema.py' at line 31.`.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It collects information about imports, classes, and functions, organizing them into a structured schema. The visitor tracks the current class during traversal to associate methods with their respective classes. It supports both synchronous and asynchronous function definitions.
*   **Instantiation:** This class is instantiated by the 'analyze_repository' function in the 'AST_Schema.py' file at line 182.
*   **Dependencies:** This class depends on the standard library modules 'ast', 'networkx', 'os', and external modules such as 'callgraph.build_filtered_callgraph' and 'getRepo.GitRepository'.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It computes the module path based on the file and project root, initializes an empty schema for collecting imports, functions, and classes, and sets up a variable to track the current class being visited.
    *   *Parameters:*
        - **source_code** (`str`): The full source code of the file being analyzed.
        - **file_path** (`str`): The file path of the source code being analyzed.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It then continues visiting child nodes.
        *   *Parameters:*
            - **node** (`ast.Import`): An AST node representing an import statement.
        *   *Usage:* Calls: `This method does not call any other functions directly.`. Called by: `This method is called by the AST traversal mechanism when encountering an import node.`.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information. It supports merging relationship data and building a comprehensive schema of files, functions, classes, and their interconnections. The class orchestrates the process of AST traversal, schema enrichment, and integration of call graph data to provide structured insights into code relationships.
*   **Instantiation:** This class is instantiated in the evaluation function in HelperLLM_evaluation.py at line 128 and in the main_workflow function in main.py at line 187.
*   **Dependencies:** This class depends on external modules such as ast, networkx, os, callgraph.build_filtered_callgraph, and getRepo.GitRepository.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any initialization actions.
    *   *Parameters:*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema: dict, call_graph: nx.DiGraph, filename: str)`
        *   *Description:* This static method enriches a given schema with call graph information by updating function and method contexts with details about what they call and who calls them. It iterates through functions and class methods in the schema and updates their context fields based on the provided call graph.
        *   *Parameters:*
            - **schema** (`dict`): A dictionary representing the schema of a parsed file, containing functions and classes.
            - **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions and methods.
            - **filename** (`str`): The path of the file being processed, used to construct unique keys for lookup in the call graph.
        *   *Usage:* Calls: `This method does not call any other functions directly.`. Called by: `This method is called by the analyze_repository method within the ASTAnalyzer class.`.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, relationship_data: list)`
        *   *Description:* This method merges relationship data from an external source into the provided schema. It maps identifiers from the relationship data to functions and classes in the schema, updating their context with information about what calls them or who instantiates them.
        *   *Parameters:*
            - **full_schema** (`dict`): A dictionary containing the full schema of the repository, including file structures and AST nodes.
            - **relationship_data** (`list`): A list of dictionaries containing relationship information, such as identifiers and called_by lists.
        *   *Returns:*
            - **full_schema** (`dict`): The updated schema with merged relationship data.
        *   *Usage:* Calls: `This method does not call any other functions directly.`. Called by: `This method is called by the evaluation function in HelperLLM_evaluation.py at line 137 and by the main_workflow function in main.py at line 197.`.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository)`
        *   *Description:* This method performs a complete analysis of a repository by processing a list of files. It parses each Python file's content into an AST, uses an ASTVisitor to extract schema information, enriches this schema with call graph data, and aggregates results into a unified schema structure.
        *   *Parameters:*
            - **files** (`list`): A list of file objects containing file paths and content to be analyzed.
            - **repo** (`GitRepository`): An object representing the Git repository being analyzed.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary containing the aggregated schema of all processed files.
        *   *Usage:* Calls: `This method calls the _enrich_schema_with_callgraph method and attempts to build a filtered callgraph using build_filtered_callgraph.`. Called by: `This method is called by the evaluation function in HelperLLM_evaluation.py at line 129 and by the main_workflow function in main.py at line 188.`.

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes an AST representation of a file and uses a custom visitor to extract import dependencies. These dependencies are then added to a NetworkX DiGraph, where nodes represent files and edges represent import relationships. The resulting graph captures the dependency structure of the given file.
*   **Parameters:**
    - **filename** (`str`): The name of the file being analyzed for dependencies.
    - **tree** (`AST`): The abstract syntax tree of the file, used to traverse and extract import information.
    - **repo_root** (`str`): The root directory of the repository, used to resolve relative paths for imports.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes are files and edges represent import relationships.
*   **Usage:** Calls: `This function does not directly call any other functions defined within the provided source code.`. Called by: `This function is called by the 'build_repository_graph' function in the 'File_Dependency.py' file at line 177.`.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a dependency graph for all Python files within a given Git repository. It iterates through each Python file, parses its content into an abstract syntax tree (AST), and builds a file-level dependency graph. These individual file graphs are then merged into a single global directed graph representing the overall dependencies across the repository. The function ensures that only Python files are processed and correctly handles nodes and edges from each file's dependency graph.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object containing the files to analyze for dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the combined file-level dependencies across the entire repository.
*   **Usage:** Calls: `This function internally uses several AST parsing and graph-building utilities such as ast.parse, build_file_dependency_graph, and networkx.DiGraph operations.`. Called by: `This function is called by the backend.File_Dependency module at line 200.`.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function retrieves all Python files (.py) from a specified directory and its subdirectories, returning them as relative paths from the given directory. It resolves the input directory to an absolute path before performing the search. The function uses pathlib for path manipulation and globbing.
*   **Parameters:**
    - **directory** (`str`): The directory path from which to find all Python files.
*   **Returns:**
    - **all_files** (`list[pathlib.Path]`): A list of Path objects representing all Python files found in the directory and its subdirectories, relative to the input directory.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by _resolve_module_name in File_Dependency.py at line 43.`.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze and resolve file-level import dependencies within a Python project. It extends NodeVisitor to traverse AST nodes representing imports and builds a dependency graph by tracking which files depend on others. The class handles both absolute and relative imports, resolving relative paths based on the repository structure and checking for module existence or symbol exports in __init__.py files.
*   **Instantiation:** This class is instantiated by the function build_file_dependency_graph located in File_Dependency.py at line 156.
*   **Dependencies:** This class does not directly depend on any external libraries beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initialisiert den File Dependency Graphen
Args:
    *   *Parameters:*
        - **filename** (`str`): The name of the file being analyzed for dependencies.
        - **repo_root** (`Any`): The root directory of the repository containing the file.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(node: ImportFrom)`
        *   *Description:* Resolves relative import statements by analyzing the import node and determining the actual module or symbol names. It checks for matching files or symbols in the repository structure, including handling __init__.py exports. The method raises ImportError if no resolution can be made.
        *   *Parameters:*
            - **node** (`ImportFrom`): An AST node representing a relative import statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names.
        *   *Usage:* Calls: `This method internally calls helper functions module_file_exists and init_exports_symbol to check for file existence and symbol exports respectively.`. Called by: `This method is called by visit_ImportFrom when resolving relative imports.`.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* Handles AST nodes representing import statements. It adds the imported module names to the import dependencies dictionary for the current file. Optionally accepts a base_name to override the default module name.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): An AST node representing an import statement.
            - **base_name** (`str | None`): Optional override for the base name of the imported module.
        *   *Usage:* Calls: `This method calls generic_visit to continue traversal of the AST.`. Called by: `This method is called by visit_ImportFrom after processing resolved modules.`.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ImportFrom)`
        *   *Description:* Processes AST nodes representing 'from ... import ...' statements. For absolute imports, it extracts the module base name and delegates to visit_Import. For relative imports, it attempts to resolve them using _resolve_module_name before delegating to visit_Import.
        *   *Parameters:*
            - **node** (`ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Usage:* Calls: `This method calls _resolve_module_name to handle relative imports and visit_Import to record dependencies.`. Called by: `This method is invoked during AST traversal by the parent NodeVisitor class.`.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** The main_orchestrator function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analysis for three example functions ('add_item', 'check_stock', and 'generate_report') and simulates the documentation generation process for these functions using an LLMHelper instance. The function sets up mock inputs and expected outputs, initializes an LLM helper with prompt files, and processes the results to build a final documentation dictionary.
*   **Parameters:**
*   **Returns:**
*   **Usage:** Calls: `This function does not call any other user-defined functions directly; it primarily orchestrates the flow of data and interactions between various components like LLMHelper, FunctionAnalysisInput, and FunctionAnalysis.`. Called by: `Called by backend.HelperLLM (line 419 in HelperLLM.py).`.

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a centralized interface for interacting with various language models, particularly for generating and validating code documentation for functions and classes. It supports multiple LLM backends including Google Gemini, OpenAI, custom APIs, and Ollama, dynamically configuring settings such as batch size based on the selected model. The class handles API interactions, error management, and structured output validation using Pydantic models.
*   **Instantiation:** The LLMHelper class is instantiated by the main_orchestrator function in HelperLLM.py, the evaluation function in HelperLLM_evaluation.py, and the main_workflow function in main.py.
*   **Dependencies:** No external dependencies are explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with configuration parameters including API keys, prompt file paths, and model specifications. It reads system prompts from specified files, configures batch processing sizes according to the model, and sets up appropriate LLM clients based on the model type. The initialization also ensures proper validation of required inputs like the API key and prompt file existence.
    *   *Parameters:*
        - **api_key** (`str`): API key for accessing the language model service.
        - **function_prompt_path** (`str`): File path to the system prompt used for function documentation generation.
        - **class_prompt_path** (`str`): File path to the system prompt used for class documentation generation.
        - **model_name** (`str`): Name of the language model to use. Defaults to 'gemini-2.0-flash-lite'.
        - **base_url** (`str`): Base URL for custom API endpoints. Optional.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing requests based on the specified model name. Different models have different recommended or optimal batch sizes, which are determined by checking the model name against predefined conditions. If the model is unknown, a default conservative batch size is applied.
        *   *Parameters:*
            - **model_name** (`str`): The name of the language model being used.
        *   *Usage:* Calls: `This method does not call any other functions directly.`. Called by: `This method is called during the initialization of the LLMHelper class.`.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* Processes a batch of function inputs to generate validated documentation using the configured LLM. It divides the input into manageable batches, sends each batch to the LLM for processing, and handles errors gracefully by filling failed batches with None values while maintaining order. Rate limiting is respected by introducing delays between batches.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of function input models containing details needed for documentation generation.
        *   *Returns:*
            - **result** (`List[Optional[FunctionAnalysis]]`): A list of validated function analysis results or None for failed items.
        *   *Usage:* Calls: `This method does not explicitly call other functions defined in the class.`. Called by: `Called by evaluation function in HelperLLM_evaluation.py and main_workflow function in main.py.`.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* Processes a batch of class inputs to generate validated documentation using the configured LLM. Similar to generate_for_functions, it batches inputs, sends them to the LLM, and manages errors by inserting None placeholders for failed entries. It also respects rate limits by adding delays between batches.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of class input models containing details needed for documentation generation.
        *   *Returns:*
            - **result** (`List[Optional[ClassAnalysis]]`): A list of validated class analysis results or None for failed items.
        *   *Usage:* Calls: `This method does not explicitly call other functions defined in the class.`. Called by: `Called by evaluation function in HelperLLM_evaluation.py and main_workflow function in main.py.`.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the central interface for interacting with various language learning models (LLMs), supporting multiple providers such as Google Generative AI, OpenAI-compatible APIs, and Ollama. It initializes with an API key, a prompt file path, and optional model and base URL configurations. Based on the specified model name, it selects and configures the appropriate LLM client. The class provides two core functionalities: calling the LLM synchronously with a single response and streaming responses from the LLM in real-time.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py at line 398.
*   **Dependencies:** No external dependencies are explicitly listed.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading a system prompt from a file, and setting up the appropriate LLM client based on the model name. It supports different LLM backends including Google Generative AI, custom OpenAI-compatible APIs, and Ollama.
    *   *Parameters:*
        - **api_key** (`str`): API key used for authenticating with the LLM provider.
        - **prompt_file_path** (`str`): File path to the system prompt used for initializing the LLM.
        - **model_name** (`str`): Name of the model to use. Defaults to 'gemini-2.5-pro'.
        - **base_url** (`str`): Base URL for the LLM endpoint, used when connecting to local or custom LLMs.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* Sends a user input message to the configured LLM and returns a single response. It constructs a message sequence including the system prompt and user input, invokes the LLM, and logs the success or failure of the operation.
        *   *Parameters:*
            - **user_input** (`str`): The input text provided by the user to send to the LLM.
        *   *Returns:*
            - **response_content** (`str`): The content of the LLM's response, or None if an error occurs.
        *   *Usage:* Calls: `This method does not call any other functions directly.`. Called by: `Called by the main_workflow function in main.py at line 417.`.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* Streams responses from the LLM in real-time as chunks become available. It constructs a message sequence including the system prompt and user input, initiates a streaming request to the LLM, and yields each chunk of content as it arrives. In case of errors, it yields an error message instead.
        *   *Parameters:*
            - **user_input** (`str`): The input text provided by the user to send to the LLM.
        *   *Returns:*
            - **chunk_content** (`str`): Yields content chunks from the LLM response or an error message if an exception occurs.
        *   *Usage:* Calls: `This method does not call any other functions directly.`. Called by: `This method is not called by any other functions according to the provided context.`.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract basic project information from common project files such as README.md, pyproject.toml, and requirements.txt. It initializes with a predefined structure for storing extracted information and provides methods to parse different file types based on priority. The class orchestrates the extraction process by identifying relevant files and parsing them according to a set order of precedence, ultimately returning a structured dictionary of project metadata.
*   **Instantiation:** This class is instantiated in HelperLLM_evaluation.py at line 104 and in main.py at line 160.
*   **Dependencies:** This class does not depend on any external modules beyond standard library imports.
*   **Constructor:**
    *   *Description:* Initializes the ProjektInfoExtractor with a default structure for storing project information. It sets up placeholders for various project details including overview and installation sections, and defines a constant for indicating missing information.
    *   *Parameters:*
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This private method searches for a file among a list of files that matches any of the given patterns, ignoring case differences. It iterates through the list of files and checks if the file path ends with one of the specified patterns. If a match is found, it returns the matching file object; otherwise, it returns None.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of file extension patterns to search for.
            - **dateien** (`List[Any]`): A list of file objects to search through.
        *   *Returns:*
            - **result** (`Optional[Any]`): The matched file object or None if no match is found.
        *   *Usage:* Calls: `This method does not call any other methods.`. Called by: `This method is not called by any other methods within the provided context.`.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This private method extracts text content from a markdown document under a specific heading (marked with ##). It uses regular expressions to find the heading and captures all text until the next heading or end of the document. It supports multiple alternative keywords for the heading to make the extraction flexible.
        *   *Parameters:*
            - **inhalt** (`str`): The full markdown text content to parse.
            - **keywords** (`List[str]`): A list of possible keywords for the section heading to extract.
        *   *Returns:*
            - **extracted_text** (`Optional[str]`): The extracted text section or None if no matching heading is found.
        *   *Usage:* Calls: `This method does not call any other methods.`. Called by: `This method is not called by any other methods within the provided context.`.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This private method parses the content of a README file to extract various project details such as title, description, key features, tech stack, current status, setup instructions, and quick start guide. It uses regex patterns to locate these elements and stores them in the internal info structure.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the README file to parse.
        *   *Usage:* Calls: `This method calls _extrahiere_sektion_aus_markdown to extract specific sections from the markdown content.`. Called by: `This method is not called by any other methods within the provided context.`.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project metadata like name and description. It also retrieves dependencies if available. It handles potential errors during TOML parsing and logs warnings if the required library is missing.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the pyproject.toml file to parse.
        *   *Usage:* Calls: `This method does not call any other methods.`. Called by: `This method is not called by any other methods within the provided context.`.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This private method parses the content of a requirements.txt file to extract dependency information. It only populates the dependencies field if it hasn't already been filled by a higher-priority source like pyproject.toml. It filters out comments and empty lines.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the requirements.txt file to parse.
        *   *Usage:* Calls: `This method does not call any other methods.`. Called by: `This method is not called by any other methods within the provided context.`.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This public method orchestrates the entire information extraction process. It identifies relevant files (README, pyproject.toml, requirements.txt) and processes them in a prioritized order. It calls the appropriate parsing methods based on the file type and formats the final output, including setting the project title based on the repository URL.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file objects to extract information from.
            - **repo_url** (`str`): The URL of the repository to derive the project title from.
        *   *Returns:*
            - **info** (`Dict[str, Any]`): A dictionary containing the extracted project information.
        *   *Usage:* Calls: `This method calls _finde_datei to locate relevant files, and _parse_readme, _parse_toml, and _parse_requirements to process the contents of those files.`. Called by: `This method is called by evaluation in HelperLLM_evaluation.py and main_workflow in main.py.`.

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** The function 'make_safe_dot' takes a NetworkX directed graph and a file path as inputs. It creates a copy of the graph and generates a safe node naming scheme by replacing original node names with 'n{i}' format, where 'i' is an index. It then relabels the nodes in the copied graph according to this mapping and assigns the original node labels as attributes to the new nodes. Finally, it writes the modified graph to a DOT file at the specified output path.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph object to be processed and saved.
    - **out_path** (`str`): The file path where the DOT representation of the graph will be written.
*   **Returns:**
*   **Usage:** Calls: `This function does not call any other functions directly; it relies on NetworkX and pydot for graph manipulation and file I/O.`. Called by: `This function is called by 'backend.callgraph' in the file 'callgraph.py' at line 244.`.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** Die Funktion erstellt einen globalen Call-Graphen basierend auf allen Python-Dateien eines Git-Repositories und filtert diesen anschließend auf Funktionen, die vom Benutzer selbst geschrieben wurden. Sie durchläuft alle Dateien, parst deren Inhalt mit dem Abstract Syntax Tree (AST), extrahiert Funktionsaufrufe und baut einen gerichteten Graphen auf, wobei nur Kanten zwischen eigenen Funktionen erhalten bleiben.
*   **Parameters:**
    - **repo** (`GitRepository`): Ein Objekt, das Zugriff auf ein Git-Repository bietet, um alle darin enthaltenen Dateien abzurufen.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): Ein gerichteter Graph (DiGraph) aus dem networkx-Bibliothek, der nur die Aufrufbeziehungen zwischen selbst geschriebenen Funktionen enthält.
*   **Usage:** Calls: `Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes direkt auf.`. Called by: `Diese Funktion wird von zwei anderen Stellen aufgerufen: einmal in der Funktion 'analyze_repository' in der Datei 'AST_Schema.py' und einmal als Modul 'backend.callgraph' in der Datei 'callgraph.py'.`.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is designed to construct a call graph from Python AST nodes, tracking function and method calls within a given file. It maintains information about local definitions, imports, and class contexts to resolve and map function names correctly. The class uses NetworkX to represent the call graph as a directed graph, where nodes represent functions and edges represent calls between them. It handles various AST node types including imports, class definitions, function definitions, and function calls.
*   **Instantiation:** The class is instantiated in the build_filtered_callgraph function in callgraph.py at lines 199 and 206.
*   **Dependencies:** The class depends on the ast module for parsing Python code, networkx for graph representation, and several custom modules such as getRepo.GitRepository and basic_info.ProjektInfoExtractor.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph with a filename and sets up internal data structures to track function definitions, the current function and class context, import mappings, and the call graph itself. It also initializes empty dictionaries and sets for storing local definitions, graph nodes, and edges.
    *   *Parameters:*
        - **filename** (`str`): The name of the file being processed to build the call graph.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This method recursively traverses an AST node to extract the dotted name components of a function or attribute call. It identifies whether the node represents a function call, a name, or an attribute access and builds a list of name components accordingly.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node to traverse for extracting name components.
        *   *Returns:*
            - **result** (`list[str]`): A list of strings representing the dotted name components of the call.
        *   *Usage:* Calls: `No external functions are called by this method.`. Called by: `This method is called by the _resolve_all_callee_names method.`.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* Resolves a list of dotted name components into fully qualified names by checking local definitions, import mappings, and class context. It constructs a list of resolved names based on the precedence of local definitions, import mappings, and default naming conventions.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list of lists containing name components for each callee.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of fully qualified names for the callees.
        *   *Usage:* Calls: `This method calls the _recursive_call method to extract name components.`. Called by: `This method is called by the visit_Call method.`.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None)`
        *   *Description:* Constructs a fully qualified name for a function or method, incorporating the filename, optional class name, and base name. This helps in uniquely identifying functions within the context of a file and potentially within a class.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`Optional[str]`): The name of the class if the function belongs to one.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name constructed from the filename, class name (if provided), and base name.
        *   *Usage:* Calls: `No external functions are called by this method.`. Called by: `This method is called by the visit_FunctionDef method.`.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* Determines the current caller's name, either from the current function context or defaults to the filename or global scope if no function is active. This is used to identify the source of a function call in the call graph.
        *   *Parameters:*
        *   *Returns:*
            - **caller** (`str`): The name of the current caller, derived from the function context or defaulting to the filename or global scope.
        *   *Usage:* Calls: `No external functions are called by this method.`. Called by: `This method is called by the visit_Call method.`.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST by mapping aliases to their actual module names. This allows the class to resolve imported names correctly when building the call graph.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Usage:* Calls: `This method calls the generic_visit method to continue processing child nodes.`. Called by: `This method is invoked by the AST visitor during traversal.`.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements by mapping imported names to their respective modules. This ensures that names imported from other modules are correctly resolved in the call graph.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Usage:* Calls: `This method calls the generic_visit method to continue processing child nodes.`. Called by: `This method is invoked by the AST visitor during traversal.`.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* Processes class definitions in the AST by temporarily setting the current class context. This allows the class to correctly associate functions with their defining classes when constructing the call graph.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Usage:* Calls: `This method calls the generic_visit method to continue processing child nodes.`. Called by: `This method is invoked by the AST visitor during traversal.`.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definitions in the AST by creating a fully qualified name for the function, updating local definitions, and adding the function to the call graph. It also manages the current function context during traversal.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Usage:* Calls: `This method calls the _make_full_name and generic_visit methods to process the function definition.`. Called by: `This method is invoked by the AST visitor during traversal.`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating to the visit_FunctionDef method, ensuring that async functions are processed similarly to regular functions in the call graph.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Usage:* Calls: `This method calls the visit_FunctionDef method to handle the async function.`. Called by: `This method is invoked by the AST visitor during traversal.`.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST by determining the caller, resolving the callee names, and adding edges to the call graph. It tracks which functions call which others to build the call graph structure.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function call.
        *   *Usage:* Calls: `This method calls the _current_caller, _recursive_call, and _resolve_all_callee_names methods to determine and resolve the caller and callee names, and then calls the generic_visit method to continue processing.`. Called by: `This method is invoked by the AST visitor during traversal.`.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* Handles conditional statements in the AST, specifically those related to '__name__ == \"__main__\"', by temporarily changing the current function context to '<main_block>' during traversal of the conditional body. This ensures that main block code is correctly attributed in the call graph.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing a conditional statement.
        *   *Usage:* Calls: `This method calls the generic_visit method to continue processing child nodes.`. Called by: `This method is invoked by the AST visitor during traversal.`.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It implements lazy loading for file metadata such as the blob object, content, and size to optimize performance by only loading data when necessary. The class provides properties to access these lazily-loaded attributes and includes utility methods for word count analysis and serialization to a dictionary format.
*   **Instantiation:** This class is instantiated by the 'get_all_files' function located in 'getRepo.py' at line 111.
*   **Dependencies:** This class depends on standard library modules like 'os' and third-party libraries such as 'git.Repo' and 'git.GitCommandError'.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object with the path to the file and the commit tree from which it originates. It sets up internal attributes for lazy loading including placeholders for the blob, content, and size.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* A property that lazily loads and returns the Git blob object associated with the file. If the blob hasn't been loaded yet, it retrieves it from the commit tree using the stored file path. Raises a FileNotFoundError if the file cannot be found in the commit tree.
        *   *Parameters:*
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   *Usage:* Calls: `This method does not call any other functions.`. Called by: `This method is not called by any other functions according to the provided context.`.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* A property that lazily loads and returns the decoded content of the file. It reads the raw data stream from the blob and decodes it into a UTF-8 string, ignoring encoding errors. If the content has not yet been loaded, it triggers the loading of the blob first.
        *   *Parameters:*
        *   *Returns:*
            - **content** (`str`): The decoded content of the file.
        *   *Usage:* Calls: `This method does not call any other functions.`. Called by: `This method is not called by any other functions according to the provided context.`.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* A property that lazily loads and returns the size of the file in bytes. It accesses the size attribute of the blob object. If the size has not yet been determined, it triggers the loading of the blob first.
        *   *Parameters:*
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   *Usage:* Calls: `This method does not call any other functions.`. Called by: `This method is not called by any other functions according to the provided context.`.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* An example analysis method that counts the number of words in the file's content. It splits the content by whitespace and returns the resulting count.
        *   *Parameters:*
        *   *Returns:*
            - **word_count** (`int`): The total number of words in the file.
        *   *Usage:* Calls: `This method does not call any other functions.`. Called by: `This method is not called by any other functions according to the provided context.`.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* Provides a useful string representation of the RepoFile object, displaying the file path for debugging and logging purposes.
        *   *Parameters:*
        *   *Returns:*
            - **repr_string** (`str`): A string representation of the RepoFile object.
        *   *Usage:* Calls: `This method does not call any other functions.`. Called by: `This method is not called by any other functions according to the provided context.`.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content: bool)`
        *   *Description:* Serializes the RepoFile object into a dictionary format. It includes basic file information such as path, name, size, and type. Optionally, it can also include the full content of the file if requested.
        *   *Parameters:*
            - **include_content** (`bool`): If True, includes the file's content in the returned dictionary.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing file metadata and optionally the content.
        *   *Usage:* Calls: `This method does not call any other functions.`. Called by: `This method is not called by any other functions according to the provided context.`.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory and providing access to its files through RepoFile objects. It supports listing all files, retrieving a hierarchical file tree, and cleaning up the temporary directory upon closing. The class implements context manager protocols (__enter__ and __exit__) to facilitate automatic resource management.
*   **Instantiation:** The GitRepository class is instantiated in the evaluation function in HelperLLM_evaluation.py at line 86 and in the main_workflow function in main.py at line 141.
*   **Dependencies:** This class depends on several modules including tempfile, shutil, git.Repo, git.GitCommandError, logging, and os.
*   **Constructor:**
    *   *Description:* Initializes a GitRepository instance by cloning the specified repository URL into a temporary directory. It sets up necessary attributes such as the repository URL, temporary directory path, and references to the cloned repository and its latest commit. If cloning fails, it raises a RuntimeError after cleaning up resources.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* Retrieves a list of all files in the repository and creates RepoFile objects for each file. These objects are stored in the instance's 'files' attribute and returned.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing the files in the repository.
        *   *Usage:* Calls: `This method does not call any other methods internally.`. Called by: `This method is not called by any other methods according to the provided context.`.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* Deletes the temporary directory used for cloning the repository and cleans up associated resources.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Usage:* Calls: `This method does not call any other methods internally.`. Called by: `This method is not called by any other methods according to the provided context.`.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* Enables the use of the GitRepository instance in a 'with' statement, returning itself for use within the context block.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **""** (`GitRepository`): The GitRepository instance itself.
        *   *Usage:* Calls: `This method does not call any other methods internally.`. Called by: `This method is not called by any other methods according to the provided context.`.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* Cleans up the temporary directory when exiting a 'with' statement context by calling the close() method.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
            - **exc_type** (`Any`): Exception type, if an exception occurred in the with block.
            - **exc_val** (`Any`): Exception value, if an exception occurred in the with block.
            - **exc_tb** (`Any`): Exception traceback, if an exception occurred in the with block.
        *   *Usage:* Calls: `This method does not call any other methods internally.`. Called by: `This method is not called by any other methods according to the provided context.`.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content: bool)`
        *   *Description:* Constructs a hierarchical representation of the repository's file structure. If no files have been retrieved yet, it fetches them first. Then, it builds a nested dictionary structure where directories and files are organized according to their paths.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
            - **include_content** (`bool`): Whether to include file content in the returned dictionary structure.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree.
        *   *Usage:* Calls: `This method does not call any other methods internally.`. Called by: `This method is not called by any other methods according to the provided context.`.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** Die Funktion erstellt ein Balkendiagramm zur Darstellung des Token-Vergleichs zwischen JSON und TOON Format. Sie verwendet matplotlib zur Erstellung des Diagramms und speichert das Ergebnis in einer Datei. Das Diagramm zeigt die Anzahl der Token für beide Formate sowie den prozentualen Einsparungswert. Die Funktion fügt außerdem Werte über die Balken hinzu, um die Tokenzahlen direkt sichtbar zu machen.
*   **Parameters:**
    - **json_tokens** (`int`): Die Anzahl der Token im JSON-Format.
    - **toon_tokens** (`int`): Die Anzahl der Token im TOON-Format.
    - **savings_percent** (`float`): Der prozentuale Unterschied oder die Einsparung zwischen den beiden Formaten.
    - **output_path** (`str`): Der Dateipfad, unter dem das generierte Diagramm gespeichert wird.
*   **Returns:**
*   **Usage:** Calls: `Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.`. Called by: `Die Funktion wird von der Funktion 'main_workflow' in der Datei 'main.py' aufgerufen.`.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items: int, batch_size: int, model_name: str)`
*   **Description:** The function calculates the net time duration by subtracting sleep times related to rate limits from the total time elapsed between a start and end timestamp. It specifically handles cases where the model name starts with 'gemini-' and adjusts the calculation based on the number of batches and item count. If the model is not a Gemini model, it returns the total duration directly. For zero items, it returns zero. Otherwise, it computes the number of batches, determines the sleep count, and subtracts the total sleep time from the overall duration.
*   **Parameters:**
    - **start_time** (`float or datetime`): The starting timestamp of the operation.
    - **end_time** (`float or datetime`): The ending timestamp of the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The size of each batch of items.
    - **model_name** (`str`): The name of the model being used, which affects how sleep time is calculated.
*   **Returns:**
    - **net_time** (`float or int`): The net time after subtracting sleep durations, ensuring it is not negative.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by the evaluation function in HelperLLM_evaluation.py at lines 249 and 275, and by the main_workflow function in main.py at lines 311 and 342.`.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive code analysis pipeline that processes a GitHub repository input. It begins by analyzing the input to extract a repository URL, clones the repository, and then extracts basic project information, file tree, and relationships between code elements. It subsequently generates an Abstract Syntax Tree (AST) schema and enriches it with relationship data. The function prepares inputs for a Helper LLM to analyze individual functions and classes, then calls the Helper LLM to generate documentation for these elements. Finally, it prepares a main input for a Main LLM to produce a final report based on all collected data.
*   **Parameters:**
    - **input** (`Any`): The input provided to the workflow, typically a string containing a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing API keys for various services such as Gemini, OpenAI, and SCADsLLM.
    - **model_names** (`dict`): A dictionary specifying the names of models to be used for helper and main LLM tasks.
    - **status_callback** (`Callable[[str], None] or None`): An optional callback function to report progress updates.
*   **Returns:**
    - **report** (`str`): The final markdown report generated by the Main LLM.
    - **metrics** (`dict`): A dictionary containing timing metrics for helper and main LLM processing.
*   **Usage:** Calls: `This function internally calls several components including GitRepository for cloning repositories, ProjektInfoExtractor for extracting basic project information, ProjectAnalyzer for relationship analysis, ASTAnalyzer for AST schema creation, LLMHelper for function and class analysis, and MainLLM for generating the final report.`. Called by: `This function is called by the frontend.Frontend function in Frontend.py at line 489 and by backend.main in main.py at line 533.`.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The function 'update_status' is designed to handle status updates by invoking an optional callback function if it exists, and then logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages throughout the application.
*   **Parameters:**
    - **msg** (`Any`): The status message to be processed and logged.
*   **Returns:**
*   **Usage:** Calls: `This function does not call any other functions directly; it relies on an external 'status_callback' variable and the 'logging' module.`. Called by: `This function is called multiple times (14 instances) from the 'main_workflow' function in 'main.py', typically at various stages of the workflow to report progress or status changes.`.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases where the filepath is not under the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    - **module_path** (`str`): A dot-separated module path derived from the given file path.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by _collect_definitions and __init__ methods in relationship_analyzer.py.`.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze Python projects by parsing their source code to extract definitions (functions, classes, methods) and resolve inter-module call relationships. It walks through the project directory, ignoring common non-source directories, collects ASTs of Python files, identifies definitions with their locations and types, and builds a call graph that tracks which functions or methods call others. Finally, it formats this information into a structured output listing each definition along with the callers that reference it.
*   **Instantiation:** This class is instantiated by the function 'evaluation' in 'HelperLLM_evaluation.py' at line 119 and by the function 'main_workflow' in 'main.py' at line 177.
*   **Dependencies:** No external dependencies are explicitly listed in the provided context.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including a dictionary for storing definitions, a call graph represented as a defaultdict of lists, a mapping of file paths to their parsed ASTs, and a set of directory names to ignore during traversal.
    *   *Parameters:*
        - **project_root** (`str`): The absolute path to the root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* The main analysis method that orchestrates the process of finding Python files, collecting definitions from those files, resolving call relationships between functions and methods, and finally formatting the collected results into a structured list. It clears the cached ASTs after processing to free memory.
        *   *Parameters:*
        *   *Returns:*
            - **return_value** (`list`): A list of dictionaries containing formatted information about each definition and its callers.
        *   *Usage:* Calls: `This method internally calls \`_find_py_files\`, \`_collect_definitions\` for each file, and \`_resolve_calls\` for each file, followed by \`get_formatted_results\`.`. Called by: `This method is called by the functions 'evaluation' in 'HelperLLM_evaluation.py' at line 120 and 'main_workflow' in 'main.py' at line 178.`.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* Recursively walks through the project root directory and identifies all Python (.py) files, excluding certain directories like .git, venv, etc., as specified in the ignore_dirs attribute.
        *   *Parameters:*
        *   *Returns:*
            - **py_files** (`list`): A list of absolute paths to all Python files found in the project directory.
        *   *Usage:* Calls: `This method does not call any other methods within the class.`. Called by: `This method is called by the 'analyze' method.`.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath: str)`
        *   *Description:* Parses a given Python file's content into an Abstract Syntax Tree (AST), walks the tree to find function and class definitions, and stores metadata about these definitions such as their location, type, and full qualified name in the definitions dictionary.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose definitions need to be collected.
        *   *Usage:* Calls: `This method does not call any other methods within the class.`. Called by: `This method is called by the 'analyze' method.`.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* Given an AST and a node within that AST, this helper method attempts to find the parent node of the given node by walking the AST tree.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the AST being searched.
            - **node** (`ast.AST`): The node for which the parent needs to be found.
        *   *Returns:*
            - **parent** (`ast.AST or None`): The parent node of the given node, or None if not found.
        *   *Usage:* Calls: `This method does not call any other methods within the class.`. Called by: `This method is called by the '_collect_definitions' method.`.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath: str)`
        *   *Description:* Uses a CallResolverVisitor to traverse the AST of a file and identify calls made to other functions or methods. It updates the call_graph with these relationships based on the definitions previously collected.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Usage:* Calls: `This method creates a CallResolverVisitor and calls its visit method, then iterates over the calls collected by the visitor to update the call_graph.`. Called by: `This method is called by the 'analyze' method.`.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* Formats the collected definitions and call relationships into a structured list of dictionaries. Each dictionary represents a definition and includes details such as its identifier, mode (function/class/method), origin file, origin line number, and a list of callers.
        *   *Parameters:*
        *   *Returns:*
            - **output_list** (`list`): A list of dictionaries representing each definition and its associated callers.
        *   *Usage:* Calls: `This method does not call any other methods within the class.`. Called by: `This method is called by the 'analyze' method.`.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to analyze Python code and resolve call relationships between functions and methods. It tracks the current execution context (such as class and function names) and records calls made within the code. It also maintains scope information for imports and handles assignment of instance types. This class is primarily used during static analysis to understand how different parts of a codebase interact.
*   **Instantiation:** This class is instantiated in the function `_resolve_calls` located in the file `relationship_analyzer.py` at line 92.
*   **Dependencies:** This class does not depend on any external modules beyond standard library imports like ast, os, and collections.defaultdict.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with a file path, project root, and definitions dictionary. It sets up internal tracking structures including scope, instance types, and call records.
    *   *Parameters:*
        - **filepath** (`str`): The path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the project being analyzed.
        - **definitions** (`dict`): A dictionary containing known definitions in the project, used to resolve qualified names.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Handles the visitation of class definitions in the AST. It updates the current class name context and recursively visits child nodes before restoring the previous class name.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Usage:* Calls: `This method does not explicitly call any other methods.`. Called by: `This method is called by the AST visitor framework when visiting class definitions.`.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Handles the visitation of function definitions in the AST. It updates the current caller name context to the function name and recursively visits child nodes before restoring the previous caller name.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Usage:* Calls: `This method does not explicitly call any other methods.`. Called by: `This method is called by the AST visitor framework when visiting function definitions.`.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes call expressions in the AST. It resolves the qualified name of the called function and records the call along with metadata such as file, line number, and caller type (module, method, or function).
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function call.
        *   *Usage:* Calls: `This method calls the internal helper method \`_resolve_call_qname\` to resolve the qualified name of the call.`. Called by: `This method is called by the AST visitor framework when visiting call expressions.`.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST. It adds imported names to the current scope mapping, allowing resolution of qualified names later.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Usage:* Calls: `This method does not explicitly call any other methods.`. Called by: `This method is called by the AST visitor framework when visiting import statements.`.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST. It resolves the full module path and maps imported names to their qualified paths in the scope.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Usage:* Calls: `This method does not explicitly call any other methods.`. Called by: `This method is called by the AST visitor framework when visiting 'from ... import ...' statements.`.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* Processes assignment statements in the AST. Specifically, it identifies assignments to instances of classes defined in the project and records the type of the assigned instance.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Usage:* Calls: `This method does not explicitly call any other methods.`. Called by: `This method is called by the AST visitor framework when visiting assignment statements.`.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* Resolves the qualified name of a function call based on the AST node representing the function. It checks the scope for local mappings and constructs qualified names for local and global functions.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function being called.
        *   *Returns:*
            - **qualified_name** (`str or None`): The fully qualified name of the function if resolved, otherwise None.
        *   *Usage:* Calls: `This method does not explicitly call any other methods.`. Called by: `This method is called by the \`visit_Call\` method to resolve the qualified name of a call expression.`.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** The function encrypts a given text string using a Fernet cipher suite. It first checks if the input text is empty or if the cipher suite is not initialized, returning the text as-is in such cases. Otherwise, it encodes the stripped text, encrypts it, and returns the decrypted result as a string.
*   **Parameters:**
    - **text** (`str`): The text string to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input text, returned as a string.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by the update_gemini_key function in the db.py file.`.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** The function decrypts a given text using a cipher suite if both the text and the cipher suite are valid. If either is invalid or an exception occurs during decryption, the original text is returned unchanged. It handles potential errors gracefully by catching all exceptions and returning the input text as a fallback.
*   **Parameters:**
    - **text** (`str`): The encrypted text to be decrypted.
*   **Returns:**
    - **return_value** (`str`): The decrypted text if successful; otherwise, the original input text.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by the function 'get_decrypted_api_keys' in the file 'db.py'.`.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** The function inserts a new user into the database by creating a user document with the provided username, name, and password. The password is hashed before being stored. It also initializes default values for the Gemini API key and Ollama base URL. The function returns the ID of the inserted document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, used as the '_id' field in the database.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain text password of the user, which gets hashed before storage.
*   **Returns:**
    - **inserted_id** (`ObjectId`): The unique identifier of the newly inserted user document in the database.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by the frontend.Frontend class in Frontend.py at line 294.`.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user documents from a MongoDB collection named 'dbusers'. It performs a database query to find all records in the collection and returns them as a list. The function does not take any parameters and directly accesses the global 'dbusers' variable, which is expected to be initialized elsewhere in the codebase.
*   **Parameters:**
*   **Returns:**
    - **result** (`list`): A list containing all user documents retrieved from the 'dbusers' collection in the database.
*   **Usage:** Calls: `The function does not call any other functions directly.`. Called by: `This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 244.`.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The function 'fetch_user' retrieves a user document from a MongoDB collection named 'dbusers' based on the provided username. It uses the 'find_one' method to search for a document where the '_id' field matches the given username. The function does not perform any validation or transformation of the retrieved data before returning it.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) used to locate the specific user document in the database.
*   **Returns:**
    - **result** (`Any`): The user document retrieved from the 'dbusers' collection, or None if no matching document is found.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is not called by any other functions within the provided context.`.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the name field of a user in the database identified by their username. It uses MongoDB's update_one method to modify only the name field, leaving other fields unchanged. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose name needs to be updated.
    - **new_name** (`str`): The new name value to set for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were successfully modified by the update operation.
*   **Usage:** Calls: `The function internally calls the MongoDB update_one method to perform the database update operation.`. Called by: `This function is not called by any other functions according to the provided context.`.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates the Gemini API key for a specified user in the database. It first encrypts the provided API key using a text encryption function, then performs an update operation on the 'dbusers' collection to store the encrypted key under the user's ID. The function returns the count of modified documents, indicating whether the update was successful.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The raw Gemini API key provided by the user, which will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were successfully modified as a result of the update operation. Typically 0 or 1.
*   **Usage:** Calls: `The function internally calls 'encrypt_text' to encrypt the provided API key before storing it.`. Called by: `This function is called by 'save_gemini_cb' in 'Frontend.py' at line 35 and by 'frontend.Frontend' in 'Frontend.py' at line 393.`.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and performs an update operation on the user document in the database. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL needs to be updated.
    - **ollama_base_url** (`str`): The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were successfully modified by the update operation. This should typically be 1 if the user exists and the update was successful.
*   **Usage:** Calls: `This function does not call any other functions directly; it relies on the pymongo library's update_one method.`. Called by: `This function is called by save_ollama_cb in Frontend.py at line 42 and by frontend.Frontend in Frontend.py at line 407.`.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** The function retrieves a Gemini API key associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'gemini_api_key' field. If no matching user is found, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be retrieved.
*   **Returns:**
    - **gemini_api_key** (`Optional[str]`): The Gemini API key associated with the provided username, or None if no such user exists.
*   **Usage:** Calls: `This function internally uses the 'dbusers.find_one' method to query a MongoDB collection.`. Called by: `This function is not called by any other functions according to the provided context.`.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the provided username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be retrieved.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL associated with the user, or None if the user is not found.
*   **Usage:** Calls: `The function internally uses the 'dbusers.find_one' method to query the database.`. Called by: `This function is not called by any other functions according to the provided context.`.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** The function 'delete_user' removes a user document from a MongoDB collection based on the provided username. It uses the 'delete_one' method to target a specific user by their '_id', which is expected to match the given username. The function returns the count of deleted documents, which will be 1 if the user was found and deleted, or 0 if no such user exists.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted from the database, either 1 if the user was found and deleted, or 0 if no matching user was found.
*   **Usage:** Calls: `This function internally calls 'dbusers.delete_one' to perform the deletion operation in the MongoDB collection.`. Called by: `This function is not called by any other functions within the provided context.`.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user is not found, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function and retrieves the 'ollama_base_url' directly. It then returns both the decrypted Gemini API key and the Ollama base URL.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str`): The decrypted Gemini API key for the user, or an empty string if not found.
    - **ollama_plain** (`str`): The Ollama base URL for the user, or an empty string if not found.
*   **Usage:** Calls: `The function internally uses dbusers.find_one() to retrieve user data and decrypt_text() to decrypt the Gemini API key.`. Called by: `This function is called by the frontend.Frontend class in Frontend.py at lines 380 and 479.`.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** The function 'insert_chat' creates a new chat entry in a database with a unique identifier, associated username, chat name, and timestamp. It generates a UUID for the chat entry, sets the creation time to the current moment, and inserts the document into a MongoDB collection named 'dbchats'. The function then returns the ID of the newly inserted document.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat.
    - **chat_name** (`str`): The name of the chat being created.
*   **Returns:**
    - **result.inserted_id** (`str`): The unique identifier of the newly inserted chat document in the database.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by load_data_from_db in Frontend.py at line 81, handle_delete_chat in Frontend.py at line 122, and by the frontend.Frontend module in Frontend.py at line 344.`.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** Die Funktion fetch_chats_by_user ruft alle Chats eines bestimmten Benutzers aus einer MongoDB-Datenbank ab. Sie verwendet den Benutzernamen als Filterkriterium und sortiert die Ergebnisse nach dem Erstellungsdatum in aufsteigender Reihenfolge. Das Ergebnis ist eine Liste der gefundenen Chat-Dokumente.
*   **Parameters:**
    - **username** (`str`): Der Benutzername des Benutzers, dessen Chats abgerufen werden sollen.
*   **Returns:**
    - **chats** (`list`): Eine Liste von Chat-Dokumenten, die dem angegebenen Benutzernamen entsprechen und nach Erstellungsdatum sortiert sind.
*   **Usage:** Calls: `Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.`. Called by: `Die Funktion wird von der Funktion load_data_from_db in der Datei Frontend.py aufgerufen.`.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a query using MongoDB's find_one method to locate the document matching both the username and chat name. If such a document is found, the function returns True; otherwise, it returns False.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat.
    - **chat_name** (`str`): The name of the chat to check for existence.
*   **Returns:**
    - **exists** (`bool`): True if a chat with the specified username and chat name exists in the database, False otherwise.
*   **Usage:** Calls: `The function internally uses the dbchats.find_one method to query the database.`. Called by: `This function is not called by any other functions according to the provided context.`.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and updates all associated exchanges in the database. It first modifies the chat entry in the chats collection, then updates all related exchange records in the exchanges collection. The function returns the number of modified chat entries.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat to be renamed.
    - **new_name** (`str`): The new name to assign to the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat entries that were successfully modified in the database.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by the frontend.Frontend function in Frontend.py at line 462.`.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str="", main_used: str="", total_time: str="", helper_time: str="", main_time: str="")`
*   **Description:** This function inserts a new exchange record into a MongoDB collection. It generates a unique identifier for the exchange, constructs a dictionary with all the provided details including optional fields, and attempts to insert this document into the database. If the insertion is successful, it returns the generated ID; otherwise, it catches any exceptions, prints an error message, and returns None.
*   **Parameters:**
    - **question** (`str`): The question asked in the exchange.
    - **answer** (`str`): The answer provided in response to the question.
    - **feedback** (`str`): Feedback associated with the exchange.
    - **username** (`str`): The username of the user involved in the exchange.
    - **chat_name** (`str`): The name of the chat session.
    - **helper_used** (`str`): Optional field indicating which helper was used.
    - **main_used** (`str`): Optional field indicating which main component was used.
    - **total_time** (`str`): Optional field representing the total time taken for the exchange.
    - **helper_time** (`str`): Optional field representing the time taken by the helper component.
    - **main_time** (`str`): Optional field representing the time taken by the main component.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the inserted exchange record, returned upon successful insertion.
    - **None** (`None`): Returned when an exception occurs during the database insertion process.
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by the frontend.Frontend function in the Frontend.py file.`.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses the pymongo library to query the database and returns the results as a list. The sorting ensures that exchanges are displayed chronologically.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose exchange records are to be fetched.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records associated with the specified username, sorted by creation timestamp in ascending order.
*   **Usage:** Calls: `The function does not call any other functions directly.`. Called by: `This function is called by the load_data_from_db function in the Frontend.py file.`.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched documents as a list.
*   **Parameters:**
    - **username** (`str`): The username associated with the exchanges to be retrieved.
    - **chat_name** (`str`): The name of the chat associated with the exchanges to be retrieved.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order.
*   **Usage:** Calls: `The function does not call any other functions directly.`. Called by: `The function is not called by any other functions according to the provided context.`.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** This function updates the feedback field of a document in the 'dbexchanges' collection within a MongoDB database. It takes an exchange ID and a feedback value, then attempts to update the corresponding document by setting its 'feedback' field to the provided value. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    - **feedback** (`int`): The new feedback value to be set in the document.
*   **Returns:**
    - **result.modified_count** (`int`): The number of documents that were modified as a result of the update operation.
*   **Usage:** Calls: `This function does not call any other functions directly; it relies on the pymongo library's update_one method.`. Called by: `This function is called by the handle_feedback_change function in Frontend.py at line 98.`.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** This function updates the feedback message associated with a specific exchange document in a MongoDB collection. It takes an exchange ID and a new feedback message as inputs, then performs an atomic update operation on the database to set the feedback_message field. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    - **feedback_message** (`str`): The new feedback message to be stored in the exchange document.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were successfully modified by the update operation.
*   **Usage:** Calls: `The function internally calls the 'dbexchanges.update_one' method to perform the database update operation.`. Called by: `This function is called by the 'render_exchange' function in 'Frontend.py' at line 211.`.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a provided exchange ID. It performs a deletion operation and returns the count of deleted documents. The function takes a single string parameter representing the unique identifier of the exchange to be deleted.
*   **Parameters:**
    - **exchange_id** (`str`): A string representing the unique identifier of the exchange document to be deleted.
*   **Returns:**
    - **result.deleted_count** (`int`): The number of documents deleted as a result of the operation. Typically 0 or 1.
*   **Usage:** Calls: `The function does not call any other functions directly.`. Called by: `This function is called by the handle_delete_exchange function in Frontend.py at line 102.`.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** The function deletes a full chat and all associated exchanges from the database. It first removes all exchange records linked to the specified username and chat name, followed by deleting the chat record itself. The function returns the count of deleted chat documents, which indicates whether the operation was successful.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents that were deleted from the database.
*   **Usage:** Calls: `This function does not call any other functions directly; it relies on external database operations.`. Called by: `This function is called by the handle_delete_chat function in Frontend.py at line 110.`.

### File: `frontend/Frontend.py`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key for the current user, clears the input field, and displays a success message to the user. The function does not take any parameters and does not return any value.
*   **Parameters:**
*   **Returns:**
*   **Usage:** Calls: `The function internally uses the 'st.session_state' dictionary to access and manipulate session variables, and calls 'db.update_gemini_key' to update the database with the new key.`. Called by: `This function is not called by any other function within the provided context.`.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function handles the callback for saving an Ollama URL entered by the user in the frontend. It retrieves the URL from the session state, updates the database with the new URL associated with the user's username, and displays a success toast message to the user. The function does not take any parameters and does not return any value.
*   **Parameters:**
*   **Returns:**
*   **Usage:** Calls: `The function internally uses \`st.session_state.get\` to retrieve values from the Streamlit session state and calls \`db.update_ollama_url\` to update the database with the new URL.`. Called by: `This function is not called by any other function within the provided context.`.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** Die Funktion 'load_data_from_db' lädt Chats und Exchanges konsistent aus einer Datenbank für einen bestimmten Benutzer. Sie prüft zunächst, ob der Benutzer bereits geladen wurde, und lädt nur dann neue Daten, wenn dies erforderlich ist. Zunächst werden die Chats aus der Datenbank abgerufen und in den Session-State eingefügt. Anschließend werden die Exchanges geladen und den entsprechenden Chats zugeordnet. Bei Bedarf wird ein Standard-Chat erstellt, um sicherzustellen, dass immer mindestens ein Chat vorhanden ist. Schließlich wird der aktive Chat festgelegt.
*   **Parameters:**
    - **username** (`str`): Der Benutzername des Benutzers, dessen Chats und Exchanges geladen werden sollen.
*   **Returns:**
*   **Usage:** Calls: `Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.`. Called by: `Die Funktion wird von der Methode 'frontend.Frontend' in der Datei 'Frontend.py' auf Zeile 310 aufgerufen.`.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function updates the feedback value for a given exchange object in the database and triggers a re-render of the Streamlit application. It takes an exchange dictionary and a new feedback value, updates the feedback field in the dictionary, saves the updated feedback to the database using the exchange ID, and then refreshes the Streamlit UI.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing an exchange object, expected to contain keys such as 'feedback' and '_id'.
    - **val** (`Any`): The new feedback value to be assigned to the exchange object.
*   **Returns:**
*   **Usage:** Calls: `The function internally calls \`db.update_exchange_feedback\` to update the feedback in the database and \`st.rerun()\` to refresh the Streamlit UI.`. Called by: `This function is called by the \`render_exchange\` method in \`Frontend.py\` at lines 199 and 204.`.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of an exchange from the database and updates the session state accordingly. It first deletes the exchange by its ID from the database, then checks if the exchange exists in the session state for a given chat and removes it if found. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange is to be deleted.
    - **ex** (`dict`): A dictionary representing the exchange to be deleted, expected to contain at least an '_id' key.
*   **Returns:**
*   **Usage:** Calls: `The function does not call any other functions directly; it uses external modules like 'db' and 'st' (Streamlit).`. Called by: `This function is called by the render_exchange function in Frontend.py at lines 228 and 234.`.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** The function handles the deletion of a chat by first removing the chat from the database and then cleaning up the session state. It ensures that the active chat is updated appropriately, either by selecting another existing chat or by creating a new default chat if none remain. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:** Calls: `This function does not call any other functions directly; it relies on external modules like 'db' and 'st.session_state'.`. Called by: `This function is called by the frontend.Frontend class in Frontend.py at line 367.`.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** The function 'extract_repo_name' takes a text input and attempts to extract a repository name from any URL present in the text. It uses regular expressions to find a URL, parses it using urllib.parse.urlparse, extracts the path component, and then derives the repository name from the last segment of the path. If the repository name ends with '.git', it removes the extension before returning the result. If no URL is found or the path is empty, it returns None.
*   **Parameters:**
    - **text** (`str`): A string that may contain a URL from which to extract the repository name.
*   **Returns:**
    - **repo_name** (`str`): The extracted repository name from the URL, with '.git' suffix removed if present, or None if no valid URL is found.
*   **Usage:** Calls: `This function does not call any other functions directly; it relies on imported modules like 're' and 'urllib.parse.urlparse'.`. Called by: `This function is called by the 'frontend.Frontend' class, specifically at line 442 in the file 'Frontend.py'.`.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** The function 'stream_text_generator' takes a string of text as input and yields each word in the text followed by a space, with a small delay between each word. This creates a streaming effect where words are produced one at a time. It uses the 'time.sleep' function to introduce a brief pause between yielding each word.
*   **Parameters:**
    - **text** (`str`): A string containing the text to be streamed word by word.
*   **Returns:**
*   **Usage:** Calls: `This function does not call any other functions directly.`. Called by: `This function is called by 'render_text_with_mermaid' in 'Frontend.py' at line 160.`.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream: bool)`
*   **Description:** This function processes a markdown text string to identify and render Mermaid diagrams embedded within code blocks. It splits the input text based on Mermaid code block delimiters and handles regular markdown content versus Mermaid diagram content differently. For non-Mermaid content, it either streams or displays the text as markdown. For Mermaid content, it attempts to render the diagram using a Mermaid component, falling back to displaying the raw code if rendering fails.
*   **Parameters:**
    - **markdown_text** (`str`): A string containing markdown text that may include Mermaid code blocks enclosed in triple backticks with 'mermaid' language specifier.
    - **should_stream** (`bool`): A boolean flag indicating whether to stream the regular markdown text instead of rendering it directly.
*   **Returns:**
*   **Usage:** Calls: `This function does not call any other user-defined functions directly; it relies on external libraries such as 're', 'st_mermaid', 'st.write_stream', 'st.markdown', and 'st.code'.`. Called by: `This function is called by 'render_exchange' in 'Frontend.py' at line 238 and by 'frontend.Frontend' in 'Frontend.py' at line 524.`.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name: str)`
*   **Description:** The function `render_exchange` renders a chat exchange in a Streamlit interface, displaying a user's question and an assistant's response. It handles both successful responses and error cases, providing interactive elements such as feedback buttons, comment popovers, download options, and delete functionality. The assistant's response is rendered with Mermaid support. It uses various Streamlit components like `chat_message`, `container`, `button`, `popover`, `download_button`, and `error` to build the UI.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing the exchange, containing keys like 'question', 'answer', 'feedback', 'feedback_message', and '_id'.
    - **current_chat_name** (`str`): The name of the current chat, used for handling deletion of exchanges.
*   **Returns:**
*   **Usage:** Calls: `This function internally utilizes several Streamlit and custom helper functions such as \`st.chat_message\`, \`st.container\`, \`st.button\`, \`st.popover\`, \`st.download_button\`, \`st.error\`, \`st.write\`, \`st.caption\`, \`st.text_area\`, \`st.success\`, \`time.sleep\`, and \`st.rerun\`. It also calls external functions like \`handle_feedback_change\`, \`db.update_exchange_feedback_message\`, and \`handle_delete_exchange\`.`. Called by: `This function is called by the \`frontend.Frontend\` class in the \`Frontend.py\` file at line 429.`.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the metadata of a single function parameter. It encapsulates three essential attributes: the parameter's name, its type, and a descriptive explanation. This class ensures consistent structure and data integrity for parameter descriptions within the system.
*   **Instantiation:** This class is not instantiated by any other components as per the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the source file.
*   **Constructor:**
    *   *Description:* The constructor initializes a ParameterDescription instance with three required fields: name, type, and description. These fields are defined as string types and are used to store information about a function parameter.
    *   *Parameters:*
        - **name** (`str`): The name of the function parameter.
        - **type** (`str`): The data type of the function parameter.
        - **description** (`str`): A textual description of the function parameter's purpose or usage.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model designed to represent and validate the description of a function's return value. It encapsulates three key pieces of information: the name of the return value, its type, and a textual description. This class ensures that return value metadata is consistently structured and validated, making it suitable for use in API documentation, code analysis tools, or any system requiring standardized return value specifications.
*   **Instantiation:** This class is not directly instantiated by any other component listed in the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ReturnDescription instance with fields for the return value's name, type, and description. Since this class inherits from pydantic.BaseModel, initialization leverages Pydantic's validation mechanisms to enforce type correctness.
    *   *Parameters:*
        - **name** (`str`): The name of the return value.
        - **type** (`str`): The type of the return value.
        - **description** (`str`): A textual description of the return value.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function. It captures two key pieces of information: the functions or methods that are called by the current function ('calls') and the functions or methods that call the current function ('called_by'). This class serves as a structured way to document and enforce the usage context of functions within a system.
*   **Instantiation:** This class is not instantiated by any other component as per the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes the UsageContext model with two string fields: 'calls' and 'called_by'. These fields are intended to store textual representations of the calling and called functions respectively.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions or methods called by the current function.
        - **called_by** (`str`): A string describing the functions or methods that call the current function.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate detailed metadata about a function, including its overall purpose, parameter descriptions, return value details, and usage context. It serves as a structured representation for documenting function signatures and behaviors, making it easier to analyze and communicate function interfaces.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The constructor initializes the FunctionDescription instance with four required fields: 'overall', 'parameters', 'returns', and 'usage_context'. These fields collectively define the comprehensive description of a function's interface and behavior.
    *   *Parameters:*
        - **overall** (`str`): A string describing the overall purpose and functionality of the function.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing each parameter accepted by the function.
        - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects detailing each return value produced by the function.
        - **usage_context** (`UsageContext`): An object describing the usage context of the function, such as where and how it is called.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class serves as the primary data model for representing the complete JSON schema of a function. It encapsulates essential information about a function including its unique identifier, a detailed description, and an optional error field. This class is designed to provide a standardized structure for documenting function metadata and potential errors, making it suitable for use in API documentation, code analysis tools, or any system requiring structured function representations.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** No external dependencies are explicitly listed for this class.
*   **Constructor:**
    *   *Description:* Initializes a FunctionAnalysis instance with required fields for identifier and description, and an optional error field set to None by default.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the function.
        - **description** (`FunctionDescription`): An object containing detailed information about the function's behavior, parameters, and return values.
        - **error** (`Optional[str]`): An optional string field that can contain error details related to the function, defaulting to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to describe the initialization method (__init__) of a class. It captures two key aspects of a constructor: a textual description of its purpose and a list of parameter descriptions that define its interface. This class serves as a structured representation for documenting constructor details, likely used in automated documentation or introspection systems.
*   **Instantiation:** This class is not instantiated by any other component as indicated by the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the source file.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription instance with a description of the constructor and a list of parameter descriptions. The class inherits from pydantic.BaseModel, enabling validation and serialization capabilities.
    *   *Parameters:*
        - **description** (`str`): A string describing the purpose or behavior of the constructor.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing each parameter accepted by the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
*   **Instantiation:** This class is not instantiated by any other component according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields are intended to store information about the class's external dependencies and the entities that create instances of the class.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class.
        - **instantiated_by** (`str`): A string describing the entities or components that instantiate this class.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information. This structure serves as a standardized way to represent detailed metadata about a class, making it suitable for documentation generation or introspection purposes.
*   **Instantiation:** This class is not instantiated by any other component based on the provided context.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond those imported in the file.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ClassDescription model with specified fields for overall purpose, constructor description, methods analysis, and usage context.
    *   *Parameters:*
        - **overall** (`str`): A string describing the overall purpose of the class being analyzed.
        - **init_method** (`ConstructorDescription`): An instance of ConstructorDescription detailing the initialization process of the class.
        - **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects representing the methods of the class.
        - **usage_context** (`ClassContext`): An instance of ClassContext providing information on how the class is used or depends on other components.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential information about a class including its identifier, a detailed description, and an optional error message. This class is designed to structure and validate class metadata in a standardized format, making it suitable for use in documentation generation systems.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a new instance of the ClassAnalysis class with required fields for the identifier and description, and an optional error field.
    *   *Parameters:*
        - **identifier** (`str`): A string identifier for the class being analyzed.
        - **description** (`ClassDescription`): An instance of ClassDescription providing detailed metadata about the class.
        - **error** (`Optional[str]`): An optional string field to store any error messages related to class analysis.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for logging and analyzing call relationships within the system.
*   **Instantiation:** This class is not instantiated by any other components as per the provided context.
*   **Dependencies:** No external dependencies are explicitly listed for this class.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo instance with file, function, mode, and line attributes to represent a call event.
    *   *Parameters:*
        - **file** (`str`): The file path where the call occurred.
        - **function** (`str`): The name of the function that made the call.
        - **mode** (`str`): The mode of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the file where the call occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to represent structured context for analyzing a function. It encapsulates two key pieces of information: a list of function calls made within the function and a list of CallInfo objects indicating which functions call this one. This model serves as a data structure for tracking and documenting the call relationships and dependencies of functions within a codebase.
*   **Instantiation:** This class is instantiated in the HelperLLM_evaluation.py file within the evaluation function at line 162, and also in main.py within the main_workflow function at line 223.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports list, which includes typing and pydantic components.
*   **Constructor:**
    *   *Description:* The class is initialized with two attributes: 'calls', which is a list of strings representing function names that are called within the function being analyzed, and 'called_by', which is a list of CallInfo objects describing the functions that call this function.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing the names of functions called within the function being analyzed.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects describing the functions that call this function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for analyzing a function, including its mode, identifier, source code, imports, and associated context.
*   **Instantiation:** The class is instantiated by the evaluation function in HelperLLM_evaluation.py at line 167 and by the main_workflow function in main.py at line 228.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput instance with required fields including the mode, identifier, source code, imports list, and context. The mode is constrained to the literal value 'function_analysis', ensuring strict adherence to the intended usage pattern.
    *   *Parameters:*
        - **mode** (`Literal['function_analysis']`): A literal string value that must be 'function_analysis' to indicate the correct mode for this input.
        - **identifier** (`str`): A string identifier for the function being analyzed.
        - **source_code** (`str`): The raw source code of the function to be analyzed.
        - **imports** (`List[str]`): A list of import statements used in the function's source code.
        - **context** (`FunctionContextInput`): An object containing contextual information about the function's environment and usage.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent and exchange method-level metadata, facilitating better understanding and analysis of code structures.
*   **Instantiation:** This class is instantiated in the HelperLLM_evaluation.py at line 187 and in the main_workflow function in main.py at line 248.
*   **Dependencies:** This class does not explicitly depend on any external libraries beyond those imported in the file.
*   **Constructor:**
    *   *Description:* The constructor initializes the MethodContextInput instance with fields representing method metadata. It sets up the identifier, a list of called methods, a list of CallInfo objects for callers, a list of argument names, and an optional docstring.
    *   *Parameters:*
        - **identifier** (`str`): A string identifier for the method.
        - **calls** (`List[str]`): A list of strings representing the identifiers of methods called by this method.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects representing the methods that call this method.
        - **args** (`List[str]`): A list of strings representing the argument names of the method.
        - **docstring** (`Optional[str]`): An optional string containing the docstring of the method.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to structure contextual information about a class being analyzed. It encapsulates three key pieces of information: a list of dependencies, a list of call information for where the class is instantiated, and a list of method contexts for the methods within the class.
*   **Instantiation:** The class is instantiated by the main_orchestrator function in HelperLLM.py at line 369, the evaluation function in HelperLLM_evaluation.py at line 199, and the main_workflow function in main.py at line 260.
*   **Dependencies:** This class does not directly depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The constructor initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are expected to hold lists of strings, CallInfo objects, and MethodContextInput objects respectively.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of string identifiers representing the dependencies of the class.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where and how the class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects describing the context of each method within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class serves as a structured input model for generating a ClassAnalysis object. It encapsulates all necessary information required for analyzing a Python class, including the class's source code, its identifier, associated imports, and contextual metadata.
*   **Instantiation:** The class is instantiated by the main_orchestrator function in HelperLLM.py at line 338, the evaluation function in HelperLLM_evaluation.py at line 205, and the main_workflow function in main.py at line 266.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic components.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysisInput with the required fields: mode, identifier, source_code, imports, and context. The mode is constrained to the literal value 'class_analysis', ensuring strict adherence to the expected input format.
    *   *Parameters:*
        - **mode** (`Literal['class_analysis']`): A literal string value that must be 'class_analysis' to indicate the correct mode for analysis.
        - **identifier** (`str`): A string representing the name of the class being analyzed.
        - **source_code** (`str`): A string containing the complete source code of the class to be analyzed.
        - **imports** (`List[str]`): A list of strings representing the import statements used in the source file.
        - **context** (`ClassContextInput`): An object containing contextual metadata about the class, such as dependencies and instantiation details.
*   **Methods:**
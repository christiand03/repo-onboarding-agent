# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** This project, named "repo-onboarding-agent documentation", appears to be an automated documentation generation pipeline. It integrates multiple LLMs (Helper LLM, Main LLM) with a sophisticated backend for code analysis, including AST parsing, call graph generation, and dependency tracking. A Streamlit-based frontend provides a user interface for interaction, and a database stores user and chat-related information. The primary goal is to generate comprehensive Markdown documentation for Python repositories.
    - **Key Features:** 
      - Automated documentation generation for Python repositories.
      - Integration with multiple Large Language Models (LLMs) for detailed code analysis and report generation.
      - Abstract Syntax Tree (AST) parsing and code structure analysis.
      - Call graph and file dependency analysis to understand code relationships.
      - Interactive Streamlit-based user interface for repository input and documentation display.
    - **Tech Stack:** Python, Streamlit (Frontend), LangChain (LLM Orchestration), Google Gemini API (LLM), Ollama (LLM), OpenAI API (LLM), Pydantic (Data Validation/Schemas), NetworkX (Graph Analysis), GitPython (Git Repository Interaction), PyMongo (NoSQL Database), Matplotlib (Charting/Statistics), python-dotenv (Environment Variables), requests (HTTP Client)

*   **Repository Structure:**
    ```mermaid
    graph LR
        root --> root_.env_example[".env.example"]
        root --> root_.gitignore[".gitignore"]
        root --> root_SystemPrompts["SystemPrompts"]
        root_SystemPrompts --> root_SystemPrompts_files[SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt]
        root --> root_analysis_output_json["analysis_output.json"]
        root --> root_backend["backend"]
        root_backend --> root_backend_files[AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
        root --> root_database["database"]
        root_database --> root_database_files[db.py]
        root --> root_frontend["frontend"]
        root_frontend --> root_frontend_files[Frontend.py<br/>__init__.py]
        root_frontend --> root_frontend__streamlit[".streamlit"]
        root_frontend_root_frontend__streamlit --> root_frontend_root_frontend__streamlit_files[config.toml]
        root_frontend --> root_frontend_gifs["gifs"]
        root_frontend_root_frontend_gifs --> root_frontend_root_frontend_gifs_files[4j.gif]
        root --> root_notizen["notizen"]
        root_notizen --> root_notizen_files[Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md]
        root_notizen --> root_notizen_grafiken["grafiken"]
        root_notizen_root_notizen_grafiken --> root_notizen_root_notizen_grafiken_1["1"]
        root_notizen_root_notizen_grafiken_1 --> root_notizen_root_notizen_grafiken_1_files[File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot]
        root_notizen_root_notizen_grafiken --> root_notizen_root_notizen_grafiken_2["2"]
        root_notizen_root_notizen_grafiken_2 --> root_notizen_root_notizen_grafiken_2_files[FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot]
        root_notizen_root_notizen_grafiken --> root_notizen_root_notizen_grafiken_Flask_Repo["Flask-Repo"]
        root_notizen_root_notizen_grafiken_Flask_Repo --> root_notizen_root_notizen_grafiken_Flask_Repo_files[__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot]
        root_notizen_root_notizen_grafiken --> root_notizen_root_notizen_grafiken_Repo_onboarding["Repo-onboarding"]
        root_notizen_root_notizen_grafiken_Repo_onboarding --> root_notizen_root_notizen_grafiken_Repo_onboarding_files[AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot]
        root --> root_output_json["output.json"]
        root --> root_output_toon["output.toon"]
        root --> root_readme_md["readme.md"]
        root --> root_requirements_txt["requirements.txt"]
        root --> root_result["result"]
        root_result --> root_result_files[ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md]
        root --> root_schemas["schemas"]
        root_schemas --> root_schemas_files[types.py]
        root --> root_statistics["statistics"]
        root_statistics --> root_statistics_files[savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png]
    ```

    ## 2. Installation
    ### Dependencies
    To install the necessary dependencies, it is recommended to use the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

    ### Setup Guide
    1. **Clone the repository:**
       ```bash
       git clone <repository_url>
       cd repo-onboarding-agent
       ```
    2. **Install dependencies:**
       Follow the instructions under the 'Dependencies' section above, typically `pip install -r requirements.txt`.
    3. **Environment Configuration:**
       Create a `.env` file in the project root based on `.env.example` and fill in necessary API keys (e.g., GEMINI_API_KEY, OPENAI_API_KEY) and other configurations.

    ### Quick Startup
    To run the application (assuming all dependencies are installed and environment variables are configured):
    ```bash
    streamlit run frontend/Frontend.py
    ```

    ## 3. Use Cases & Commands
    This agent provides a comprehensive solution for automated code documentation:
    - **Automated Documentation:** Users can input a Git repository URL (e.g., from GitHub), and the system will automatically clone it, analyze its code structure, extract functions and classes, and generate a detailed Markdown-based documentation report using integrated LLMs.
    - **Code Relationship Visualization:** The backend analyzes file dependencies, call graphs, and class instantiation relationships to provide deeper insights into the codebase's architecture.
    - **Interactive UI:** A Streamlit-based frontend allows users to easily input repository details, initiate the documentation process, and view the generated reports in an interactive and user-friendly manner.
    - **Persistent Storage:** User data, API keys, and chat history (interactions with the documentation agent) are stored in a MongoDB database, enabling personalized experiences and retrieval of past reports.

    **Primary Commands/Interactions:**
    - **Launch UI:** `streamlit run frontend/Frontend.py`
    - **Input Repository URL:** Via the Streamlit application's input field.
    - **Generate Documentation:** Triggered by a button in the UI after providing a valid repository URL.
    - **Manage API Keys:** Through dedicated sections in the Streamlit UI to configure access to various LLM providers (Gemini, OpenAI, Ollama, etc.).

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here


## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str):`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases where the filepath is not within the project root by falling back to the basename of the file. If the resulting path ends with '.__init__', it removes the trailing segment to normalize the module path.
*   **Parameters:**
    - **`filepath`** (`str`): The absolute or relative path to a Python file.
    - **`project_root`** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    - **`module_path`** (`str`): A normalized Python module path derived from the input file path.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `__init__` (method) in `AST_Schema.py` at line `31`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It collects information about imports, classes, and functions, organizing them into a structured schema. The visitor maintains context about the current class being processed and builds detailed metadata including source segments, line numbers, and docstrings for each element encountered during traversal.
*   **Instantiation:** This class is instantiated by the analyze_repository function located in AST_Schema.py at line 182.
*   **Dependencies:** This class depends on standard library modules like ast, os, and potentially networkx and callgraph.build_filtered_callgraph which are imported at the top level but not directly used in the class itself.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It sets up internal state variables such as module path derived from the file path and project root, and initializes an empty schema dictionary to store collected information about imports, functions, and classes.
    *   *Parameters:*
        - **`source_code`** (`str`): The full source code string of the file being analyzed.
        - **`file_path`** (`str`): The absolute or relative path to the file being analyzed.
        - **`project_root`** (`str`): The root directory of the project being analyzed.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import):`
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It iterates over all aliases in the import statement and adds their names to the imports section of the schema before continuing the generic visit.
        *   *Parameters:*
            - **`node`** (`ast.Import`): An AST node representing an import statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other functions directly.
  * **Called By:** This method is called automatically by the NodeVisitor base class when encountering an Import node in the AST.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom):`
        *   *Description:* Processes import-from nodes in the AST by collecting qualified names of imported items. For each alias in the import-from statement, it constructs a fully qualified name combining the module and alias, and appends it to the schema's imports list. Then it continues the generic visit to process child nodes.
        *   *Parameters:*
            - **`node`** (`ast.ImportFrom`): An AST node representing an import-from statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other functions directly.
  * **Called By:** This method is called automatically by the NodeVisitor base class when encountering an ImportFrom node in the AST.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef):`
        *   *Description:* Handles class definition nodes in the AST by creating a detailed schema entry for the class. It generates a unique identifier based on the module path and class name, extracts the docstring and source segment, and stores metadata like start and end lines. It also tracks the current class being visited and ensures proper cleanup after processing.
        *   *Parameters:*
            - **`node`** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other functions directly.
  * **Called By:** This method is called automatically by the NodeVisitor base class when encountering a ClassDef node in the AST.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: ast.FunctionDef):`
        *   *Description:* Processes function definition nodes in the AST. If a class is currently being visited, it creates a method context entry under that class. Otherwise, it creates a standalone function entry in the schema. It extracts argument names, docstrings, and source segments, and records line number information for both cases.
        *   *Parameters:*
            - **`node`** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other functions directly.
  * **Called By:** This method is called automatically by the NodeVisitor base class when encountering a FunctionDef node in the AST.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef):`
        *   *Description:* Handles asynchronous function definitions by delegating to the regular visit_FunctionDef method. This allows async functions to be treated similarly to regular functions in terms of schema collection and metadata extraction.
        *   *Parameters:*
            - **`node`** (`ast.AsyncFunctionDef`): An AST node representing an async function definition.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method delegates to visit_FunctionDef to handle the core logic.
  * **Called By:** This method is called automatically by the NodeVisitor base class when encountering an AsyncFunctionDef node in the AST.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information. It supports merging relationship data and building a comprehensive schema of files, classes, functions, and their interdependencies. The class integrates with Git repositories and utilizes networkx-based call graphs to enhance semantic understanding of code relationships.
*   **Instantiation:** This class is instantiated in the evaluation.py file at line 128 and in the main.py file at line 187.
*   **Dependencies:** This class depends on the ast, networkx, os modules, and the build_filtered_callgraph function from the callgraph module.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any initialization actions.
    *   *Parameters:*
        *None*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema: dict, call_graph: networkx.DiGraph, filename: str):`
        *   *Description:* This static method enriches a given schema with call graph information by updating function and method contexts with details about which functions they call and which functions call them. It processes both top-level functions and class methods within the schema, using a provided call graph to populate 'calls' and 'called_by' fields.
        *   *Parameters:*
            - **`schema`** (`dict`): A dictionary representing the schema of parsed AST nodes including functions and classes.
            - **`call_graph`** (`networkx.DiGraph`): A directed graph representing the call relationships between functions and methods.
            - **`filename`** (`str`): The path of the file being processed, used to construct unique identifiers for functions and methods.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other functions directly.
  * **Called By:** This method is called by the analyze_repository method within the ASTAnalyzer class.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, relationship_data: list):`
        *   *Description:* Merges relationship data into a full schema by associating identifiers from relationship data with corresponding entries in the schema. It updates function and class contexts with 'called_by' information and class contexts with 'instantiated_by' information based on a lookup table derived from relationship data.
        *   *Parameters:*
            - **`full_schema`** (`dict`): The complete schema containing file structures and AST node information.
            - **`relationship_data`** (`list`): A list of dictionaries containing relationship metadata such as identifiers and called_by information.
        *   *Returns:*
            - **`full_schema`** (`dict`): The updated schema with merged relationship data.
        *   **Usage:**
  * **Calls:** This method does not call any other functions directly.
  * **Called By:** `evaluation` (function) in `evaluation.py` at line `137`; `main_workflow` (function) in `main.py` at line `197`
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: backend.getRepo.GitRepository):`
        *   *Description:* Analyzes a list of files from a Git repository by parsing their content into ASTs, visiting nodes with an ASTVisitor, and enriching the resulting schema with call graph information. It constructs a full schema of files, functions, and classes while handling potential parsing errors and filtering out non-Python files.
        *   *Parameters:*
            - **`files`** (`list`): A list of file objects containing file paths and content to be analyzed.
            - **`repo`** (`backend.getRepo.GitRepository`): An object representing the Git repository containing the files to be analyzed.
        *   *Returns:*
            - **`full_schema`** (`dict`): A dictionary containing the parsed and enriched schema of the repository files.
        *   **Usage:**
  * **Calls:** This method calls the _enrich_schema_with_callgraph method and uses the build_filtered_callgraph function from the callgraph module.
  * **Called By:** `evaluation` (function) in `evaluation.py` at line `129`; `main_workflow` (function) in `main.py` at line `188`

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: ast.AST, repo_root: str):`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes an AST representation of a file and uses a custom visitor to extract import dependencies. These dependencies are then added as nodes and edges to a NetworkX DiGraph. The resulting graph captures the relationships between files based on their import statements.
*   **Parameters:**
    - **`filename`** (`str`): The name of the file being analyzed for dependencies.
    - **`tree`** (`ast.AST`): The abstract syntax tree representation of the file's source code.
    - **`repo_root`** (`str`): The root directory path of the repository being analyzed.
*   **Returns:**
    - **`graph`** (`networkx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies.
*   **Usage:**
  * **Calls:** The function internally utilizes a FileDependencyGraph visitor to traverse the AST and collect import dependencies.
  * **Called By:** `build_repository_graph` (function) in `File_Dependency.py` at line `177`

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: backend.getRepo.GitRepository):`
*   **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It iterates through all files in the repository, filters for Python files, parses their content into ASTs, and builds individual file dependency graphs. These are then merged into a global dependency graph. The function uses NetworkX to manage the graph structure and relies on helper functions to process individual files.
*   **Parameters:**
    - **`repository`** (`backend.getRepo.GitRepository`): The Git repository object containing the files to analyze for dependencies.
*   **Returns:**
    - **`global_graph`** (`networkx.DiGraph`): A NetworkX directed graph representing the overall dependency structure of all Python files in the repository.
*   **Usage:**
  * **Calls:** This function internally utilizes several AST parsing and graph-building utilities including `parse`, `build_file_dependency_graph`, and various NetworkX functions.
  * **Called By:** This function is called by another function in the same module, specifically at line 200 of File_Dependency.py.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str):`
*   **Description:** This function retrieves all Python files (.py) from a specified directory and its subdirectories, returning them as relative paths from the given directory. It uses pathlib for path manipulation and recursive globbing to find all matching files. The function resolves the input directory to an absolute path before performing the search.
*   **Parameters:**
    - **`directory`** (`str`): The root directory path from which to search for Python files.
*   **Returns:**
    - **`all_files`** (`list[Path]`): A list of Path objects representing the relative paths of all .py files found in the directory and its subdirectories.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `_resolve_module_name` (method) in `File_Dependency.py` at line `43`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze and resolve Python file dependencies, particularly focusing on handling relative imports. It extends NodeVisitor to traverse AST nodes representing import statements and builds a dependency graph by tracking which files import others. The class resolves relative imports by mapping them to actual module or symbol names based on the repository structure and handles both direct and relative import scenarios.
*   **Instantiation:** This class is instantiated by the function 'build_file_dependency_graph' in the file 'File_Dependency.py'.
*   **Dependencies:** This class depends on networkx, os, ast, pathlib, keyword, and other modules related to AST parsing and file system operations.
*   **Constructor:**
    *   *Description:* Initialisiert den File Dependency Graphen

        Args:
    *   *Parameters:*
        - **`filename`** (`str`): The name of the file being analyzed for dependencies.
        - **`repo_root`** (`Any`): The root directory of the repository being analyzed.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ast.ImportFrom):`
        *   *Description:* Resolves relative imports by analyzing the import node and mapping it to actual module or symbol names. It checks for existing module files and symbols exported via __init__.py files, raising an ImportError if resolution fails.
        *   *Parameters:*
            - **`node`** (`ast.ImportFrom`): An AST node representing a relative import statement.
        *   *Returns:*
            - **`resolved`** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:**
  * **Calls:** This method internally calls helper functions 'module_file_exists' and 'init_exports_symbol'.
  * **Called By:** This method is called by 'visit_ImportFrom' when resolving relative imports.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import | ast.ImportFrom, base_name: str | None):`
        *   *Description:* Handles import statements by adding the imported module names to the dependency graph. It tracks which modules are imported by the current file.
        *   *Parameters:*
            - **`node`** (`ast.Import | ast.ImportFrom`): An AST node representing an import statement.
            - **`base_name`** (`str | None`): The base name of the imported module, if available.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method calls generic_visit to continue traversal of the AST.
  * **Called By:** This method is called by 'visit_ImportFrom' and directly during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom):`
        *   *Description:* Processes 'from ... import ...' statements by either extracting the module base name or resolving relative imports. It delegates to '_resolve_module_name' for relative import resolution and updates the dependency graph accordingly.
        *   *Parameters:*
            - **`node`** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method calls '_resolve_module_name' to resolve relative imports and 'visit_Import' to record dependencies.
  * **Called By:** This method is invoked during AST traversal when processing 'from ... import ...' statements.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator():`
*   **Description:** The main_orchestrator function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analyses for three example functions: add_item, check_stock, and generate_report. These analyses are then used to simulate how the LLMHelper would process function inputs and generate documentation. The function also demonstrates the usage of LLMHelper to generate documentation for these functions.
*   **Parameters:**
    *None*
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** This function does not call any other functions directly; it contains embedded examples and mock data.
  * **Called By:** Called by backend.HelperLLM (line 419 in HelperLLM.py)

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a centralized interface for interacting with various Large Language Models (LLMs) such as Google Gemini, OpenAI GPT, custom APIs, and Ollama. It handles API configuration, prompt loading, batching, and structured output validation using Pydantic models. The class supports generating documentation for both functions and classes by processing inputs through configured LLMs and returning validated outputs.
*   **Instantiation:** The LLMHelper class is instantiated by the main_orchestrator function in HelperLLM.py, the evaluation function in evaluation.py, and the main_workflow function in main.py.
*   **Dependencies:** No external dependencies are explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with necessary API credentials, prompt files, and model configurations. It reads system prompts from specified files, sets up the appropriate LLM based on the model name, and configures batch size settings. The initialization also sets up structured output capabilities for function and class analysis using Pydantic models.
    *   *Parameters:*
        - **`api_key`** (`str`): API key for accessing the LLM service.
        - **`function_prompt_path`** (`str`): File path to the system prompt used for function documentation generation.
        - **`class_prompt_path`** (`str`): File path to the system prompt used for class documentation generation.
        - **`model_name`** (`str`): Name of the LLM model to use. Defaults to 'gemini-2.0-flash-lite'.
        - **`base_url`** (`str`): Base URL for custom LLM endpoints. Optional.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str):`
        *   *Description:* Configures the batch size for processing requests based on the specified model name. Different models have different recommended batch sizes to optimize performance and avoid rate limiting issues.
        *   *Parameters:*
            - **`model_name`** (`str`): Name of the LLM model being used.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other functions.
  * **Called By:** This method is called during the initialization of the LLMHelper class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: typing.List[schemas.types.FunctionAnalysisInput]):`
        *   *Description:* Processes a batch of function inputs to generate and validate documentation using the configured LLM. It splits inputs into batches, sends them to the LLM, and handles errors by filling failed batches with None values while maintaining order. Rate limiting is respected by waiting between batches.
        *   *Parameters:*
            - **`function_inputs`** (`List[FunctionAnalysisInput]`): A list of function input models to process.
        *   *Returns:*
            - **`List[Optional[FunctionAnalysis]]`** (`List[Optional[FunctionAnalysis]]`): A list of validated function analysis results or None for failed items.
        *   **Usage:**
  * **Calls:** This method does not explicitly call other functions directly but relies on internal LLM interactions.
  * **Called By:** Called by the evaluation function in evaluation.py and main_workflow function in main.py.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: typing.List[schemas.types.ClassAnalysisInput]):`
        *   *Description:* Processes a batch of class inputs to generate and validate documentation using the configured LLM. Similar to generate_for_functions, it batches inputs, sends them to the LLM, and manages errors by filling failed batches with None values. Rate limiting is respected by waiting between batches.
        *   *Parameters:*
            - **`class_inputs`** (`List[ClassAnalysisInput]`): A list of class input models to process.
        *   *Returns:*
            - **`List[Optional[ClassAnalysis]]`** (`List[Optional[ClassAnalysis]]`): A list of validated class analysis results or None for failed items.
        *   **Usage:**
  * **Calls:** This method does not explicitly call other functions directly but relies on internal LLM interactions.
  * **Called By:** Called by the evaluation function in evaluation.py and main_workflow function in main.py.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the central interface for interacting with various language learning models (LLMs), supporting multiple providers including Google Generative AI, OpenAI-compatible APIs, and Ollama. It initializes with an API key, a prompt file path, and model specifications, dynamically selecting the appropriate LLM client based on the model name. The class provides two core functionalities: synchronous execution via `call_llm` and streaming responses via `stream_llm`, both utilizing a system prompt loaded from a file.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py at line 398.
*   **Dependencies:** No external dependencies listed.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading a system prompt from a specified file, and setting up the appropriate LLM client based on the model name. It supports different LLM backends such as Gemini, GPT, custom APIs, and Ollama, and raises exceptions if required configurations are missing.
    *   *Parameters:*
        - **`api_key`** (`str`): The API key used for authenticating with the LLM provider.
        - **`prompt_file_path`** (`str`): The file path to the system prompt used for initializing the LLM.
        - **`model_name`** (`str`): The name of the model to use, which determines the backend client to instantiate. Defaults to 'gemini-2.5-pro'.
        - **`base_url`** (`str`): Optional base URL for custom API endpoints. Used when the model is not a standard provider.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str):`
        *   *Description:* Executes a synchronous call to the configured LLM with a user input message, using the system prompt and user input to construct a message sequence. It logs the process and handles potential errors during the LLM invocation, returning the content of the response or None if an error occurs.
        *   *Parameters:*
            - **`user_input`** (`str`): The input text provided by the user to be processed by the LLM.
        *   *Returns:*
            - **`response_content`** (`str`): The content of the LLM's response if successful, otherwise None.
        *   **Usage:**
  * **Calls:** No internal method calls detected.
  * **Called By:** `main_workflow` (function) in `main.py` at line `417`
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str):`
        *   *Description:* Initiates a streaming interaction with the configured LLM, yielding chunks of content as they become available. It constructs a message sequence using the system prompt and user input, logs the start of the streaming process, and handles errors by yielding an error message.
        *   *Parameters:*
            - **`user_input`** (`str`): The input text provided by the user to be streamed through the LLM.
        *   *Returns:*
            - **`chunk_content`** (`str`): Yields content chunks from the LLM's streaming response or an error message if an exception occurs.
        *   **Usage:**
  * **Calls:** No internal method calls detected.
  * **Called By:** None

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract basic project information from common project files such as README.md, pyproject.toml, and requirements.txt. It maintains an internal data structure to store extracted information including project overview details like title, description, status, key features, and tech stack, as well as installation-related information such as dependencies, setup instructions, and quick start guides. The class orchestrates the extraction process by identifying relevant files, parsing their contents according to file type, and prioritizing information sources to ensure accurate metadata collection.
*   **Instantiation:** This class is instantiated by the evaluation function in evaluation.py and the main_workflow function in main.py.
*   **Dependencies:** This class does not depend on any external libraries beyond those imported directly in the source code.
*   **Constructor:**
    *   *Description:* Initializes the ProjektInfoExtractor with a predefined data structure to hold project information. It sets up placeholders for various project details under 'projekt_uebersicht' and 'installation' sections, and defines a constant for indicating missing information.
    *   *Parameters:*
        *None*
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: typing.List[str], dateien: typing.List[typing.Any]):`
        *   *Description:* This private method searches for a file among a list of files based on a set of case-insensitive file extension patterns. It iterates through the provided files and checks if any file path ends with one of the specified patterns. If a match is found, it returns the matching file object; otherwise, it returns None.
        *   *Parameters:*
            - **`patterns`** (`List[str]`): A list of file extension patterns to search for.
            - **`dateien`** (`List[Any]`): A list of file objects to search through.
        *   *Returns:*
            - **`result`** (`Optional[Any]`): The matched file object if found, otherwise None.
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: typing.List[str]):`
        *   *Description:* This private method extracts text content from a markdown document that appears under a specific section header (marked by ##). It uses regular expressions to find the section header and captures all text until the next header or end of the document. It supports multiple possible keywords for the section header to increase flexibility in matching different markdown formats.
        *   *Parameters:*
            - **`inhalt`** (`str`): The full markdown text to parse.
            - **`keywords`** (`List[str]`): A list of alternative keywords to match against the section header.
        *   *Returns:*
            - **`extracted_text`** (`Optional[str]`): The extracted text from the section, or None if no matching section is found.
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str):`
        *   *Description:* This private method parses the content of a README file to extract various project details such as title, description, key features, tech stack, status, setup instructions, and quick start guide. It uses regex patterns to locate these elements and stores them in the internal info dictionary. It leverages the _extrahiere_sektion_aus_markdown helper method to extract sections from the markdown content.
        *   *Parameters:*
            - **`inhalt`** (`str`): The content of the README file to parse.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method calls the _extrahiere_sektion_aus_markdown method to extract specific sections from the markdown content.
  * **Called By:** This method is not called by any other methods.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str):`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project metadata such as name, description, and dependencies. It uses the tomllib library to load the TOML content and retrieves project information from the 'project' section. It handles cases where tomllib is not available and catches parsing errors gracefully.
        *   *Parameters:*
            - **`inhalt`** (`str`): The content of the pyproject.toml file to parse.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str):`
        *   *Description:* This private method parses the content of a requirements.txt file to extract dependency information. It filters out comments and empty lines, then stores the resulting list of dependencies in the internal info structure. It only populates dependencies if they haven't already been set by a higher-priority source like pyproject.toml.
        *   *Parameters:*
            - **`inhalt`** (`str`): The content of the requirements.txt file to parse.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: typing.List[typing.Any], repo_url: str):`
        *   *Description:* This public method orchestrates the complete information extraction process from a list of repository files. It identifies relevant files (README, pyproject.toml, requirements.txt) using the _finde_datei helper, processes them in order of priority (pyproject.toml > requirements.txt > README), and formats the final output. It also sets the project title based on the repository URL at the end of processing.
        *   *Parameters:*
            - **`dateien`** (`List[Any]`): A list of file objects to extract information from.
            - **`repo_url`** (`str`): The URL of the repository used to derive the project title.
        *   *Returns:*
            - **`info`** (`Dict[str, Any]`): A dictionary containing the extracted project information organized under 'projekt_uebersicht' and 'installation' keys.
        *   **Usage:**
  * **Calls:** This method calls the _finde_datei, _parse_toml, _parse_requirements, and _parse_readme methods to perform the actual extraction tasks.
  * **Called By:** `evaluation` (function) in `evaluation.py` at line `105`; `main_workflow` (function) in `main.py` at line `161`

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: networkx.DiGraph, out_path: str):`
*   **Description:** The function 'make_safe_dot' takes a NetworkX directed graph and a file path as inputs. It creates a safe version of the graph by relabeling all nodes with unique identifiers prefixed by 'n', ensuring node names are safe for use in graph visualization tools like Graphviz. The original node labels are preserved in the 'label' attribute of the new nodes. Finally, the transformed graph is written to a file in DOT format.
*   **Parameters:**
    - **`graph`** (`networkx.DiGraph`): A NetworkX directed graph object to be processed and saved.
    - **`out_path`** (`str`): The file path where the DOT representation of the graph will be written.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** This function does not call any other user-defined functions directly; it relies on NetworkX and PyDot functionalities.
  * **Called By:** This function is called by the 'backend.callgraph' module at line 244 in the file 'callgraph.py'.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: backend.getRepo.GitRepository):`
*   **Description:** Die Funktion erstellt einen globalen Call-Graphen basierend auf allen Python-Dateien eines Git-Repositories und filtert diesen anschließend, sodass nur Aufrufe zwischen selbst geschriebenen Funktionen erhalten bleiben. Sie durchläuft alle Dateien, parst sie mit dem Abstract Syntax Tree (AST), extrahiert Funktionsaufrufe und baut einen gerichteten Graphen auf. Anschließend werden nur Kanten beibehalten, die sowohl von als auch zu Funktionen führen, die im Repository definiert sind.
*   **Parameters:**
    - **`repo`** (`backend.getRepo.GitRepository`): Ein Objekt, das Zugriff auf ein Git-Repository bietet, um alle darin enthaltenen Dateien abzurufen.
*   **Returns:**
    - **`global_graph`** (`networkx.DiGraph`): Ein gerichteter Graph, der die Aufrufbeziehungen zwischen selbst geschriebenen Funktionen des Repositories darstellt.
*   **Usage:**
  * **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.
  * **Called By:** Diese Funktion wird von 'analyze_repository' in 'AST_Schema.py' und von 'backend.callgraph' in 'callgraph.py' aufgerufen.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is designed to construct a call graph from Python source code by traversing the Abstract Syntax Tree (AST). It tracks function and class definitions, resolves names of called functions, handles imports, and builds a directed graph representing function call relationships. The graph is stored using NetworkX, and the class maintains mappings for local definitions and imports to resolve function names correctly.
*   **Instantiation:** This class is instantiated in the build_filtered_callgraph function located in callgraph.py at lines 199 and 206.
*   **Dependencies:** This class depends on the ast module for parsing Python code, networkx for graph representation, and several custom modules like getRepo.GitRepository and basic_info.ProjektInfoExtractor.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph with a filename and sets up internal data structures including tracking for current function and class, local definitions, a NetworkX directed graph, import mappings, a set of function names, and a dictionary of edges.
    *   *Parameters:*
        - **`filename`** (`str`): The name of the file being processed to build the call graph.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node):`
        *   *Description:* Recursively extracts the dotted name components from an AST node representing a function call. It handles different types of nodes such as ast.Call, ast.Name, and ast.Attribute to build a list of name components.
        *   *Parameters:*
            - **`node`** (`ast.AST`): An AST node representing a function call or attribute access.
        *   *Returns:*
            - **`parts`** (`list[str]`): A list of strings representing the dotted name components.
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]]):`
        *   *Description:* Resolves the names of callees based on their dotted name components. It checks for local definitions first, then import mappings, and finally constructs full names based on the current class or file scope.
        *   *Parameters:*
            - **`callee_nodes`** (`list[list[str]]`): A list of lists containing name components for each callee.
        *   *Returns:*
            - **`resolved`** (`list[str]`): A list of fully resolved callee names.
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None):`
        *   *Description:* Constructs a full name for a function or method by combining the filename, optional class name, and base name. This helps in uniquely identifying functions within the call graph.
        *   *Parameters:*
            - **`basename`** (`str`): The base name of the function or method.
            - **`class_name`** (`Optional[str]`): The name of the class if the function is a method.
        *   *Returns:*
            - **`full_name`** (`str`): The full name constructed from filename, class name, and base name.
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self):`
        *   *Description:* Determines the current caller's name, which can be either the current function or a global scope indicator if no function is active.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`caller`** (`str`): The name of the current caller.
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node):`
        *   *Description:* Handles the AST node for import statements. It maps the imported module names to their actual module names in the import mapping dictionary.
        *   *Parameters:*
            - **`node`** (`ast.Import`): An AST node representing an import statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node):`
        *   *Description:* Handles the AST node for 'from ... import ...' statements. It maps the imported names to their respective modules in the import mapping dictionary.
        *   *Parameters:*
            - **`node`** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef):`
        *   *Description:* Processes AST nodes representing class definitions. It temporarily sets the current class name during traversal and restores it after processing.
        *   *Parameters:*
            - **`node`** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node):`
        *   *Description:* Processes AST nodes representing function definitions. It registers the function in local definitions, adds it to the graph, and manages the current function context during traversal.
        *   *Parameters:*
            - **`node`** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node):`
        *   *Description:* Handles AST nodes representing asynchronous function definitions. It delegates processing to the standard function definition handler.
        *   *Parameters:*
            - **`node`** (`ast.AsyncFunctionDef`): An AST node representing an async function definition.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node):`
        *   *Description:* Processes AST nodes representing function calls. It identifies the caller, resolves the callee names, and records the call relationship in the edges dictionary.
        *   *Parameters:*
            - **`node`** (`ast.Call`): An AST node representing a function call.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node):`
        *   *Description:* Handles AST nodes representing conditional statements. Special handling is applied for conditional blocks related to '__name__ == \"__main__\"', where the current function context is temporarily changed to '<main_block>'.
        *   *Parameters:*
            - **`node`** (`ast.If`): An AST node representing an if statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods.
  * **Called By:** This method is not called by any other methods.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It implements lazy loading for file metadata such as content and size to optimize performance by only loading data when necessary. The class provides properties for accessing the Git blob, content, and size of the file, along with utility methods for word count analysis and converting the file representation to a dictionary format.
*   **Instantiation:** This class is instantiated by the get_all_files method in getRepo.py at line 111.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object with a file path and a commit tree. It sets up internal attributes for lazy loading including placeholders for the blob, content, and size of the file.
    *   *Parameters:*
        - **`file_path`** (`str`): The path to the file within the repository.
        - **`commit_tree`** (`git.Tree`): The tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self):`
        *   *Description:* A property that lazily loads and returns the Git blob object associated with the file. If the blob has not yet been loaded, it attempts to retrieve it from the commit tree using the stored file path. If the file is not found in the tree, a FileNotFoundError is raised.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`blob`** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:**
  * **Calls:** This method does not call any other functions.
  * **Called By:** This method is not called by any other functions according to the provided context.
    *   **`content`**
        *   *Signature:* `def content(self):`
        *   *Description:* A property that lazily loads and returns the decoded content of the file. It reads the data stream from the blob and decodes it into UTF-8 text, ignoring encoding errors. The content is cached after the first access to avoid repeated reads.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`content`** (`str`): The decoded content of the file.
        *   **Usage:**
  * **Calls:** This method does not call any other functions.
  * **Called By:** This method is not called by any other functions according to the provided context.
    *   **`size`**
        *   *Signature:* `def size(self):`
        *   *Description:* A property that lazily loads and returns the size of the file in bytes. It retrieves the size from the blob object and caches it after the first access to avoid repeated computations.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`size`** (`int`): The size of the file in bytes.
        *   **Usage:**
  * **Calls:** This method does not call any other functions.
  * **Called By:** This method is not called by any other functions according to the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self):`
        *   *Description:* An example analysis method that counts the number of words in the file's content. It splits the content on whitespace and returns the length of the resulting list.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`word_count`** (`int`): The total number of words in the file content.
        *   **Usage:**
  * **Calls:** This method does not call any other functions.
  * **Called By:** This method is not called by any other functions according to the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self):`
        *   *Description:* Provides a string representation of the RepoFile object, useful for debugging and logging purposes. It displays the file path of the RepoFile instance.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`repr`** (`str`): A string representation of the RepoFile object.
        *   **Usage:**
  * **Calls:** This method does not call any other functions.
  * **Called By:** This method is not called by any other functions according to the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content=False):`
        *   *Description:* Converts the RepoFile instance into a dictionary representation. It includes basic file information such as path, name, size, and type. Optionally, it can also include the file's content if specified.
        *   *Parameters:*
            - **`include_content`** (`bool`): If True, includes the file's content in the returned dictionary.
        *   *Returns:*
            - **`data`** (`dict`): A dictionary containing file metadata and optionally the content.
        *   **Usage:**
  * **Calls:** This method does not call any other functions.
  * **Called By:** This method is not called by any other functions according to the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory and providing access to its files through RepoFile objects. It supports listing all files, retrieving a hierarchical file tree, and cleaning up the temporary resources upon closing. The class implements the context manager protocol (__enter__ and __exit__) to ensure proper resource management.
*   **Instantiation:** This class is instantiated in the evaluation.py file within the evaluation function at line 86 and in main.py within the main_workflow function at line 141.
*   **Dependencies:** This class depends on external libraries such as 'tempfile', 'shutil', 'git.Repo', 'git.GitCommandError', and 'logging'.
*   **Constructor:**
    *   *Description:* Initializes a GitRepository instance by cloning the specified repository URL into a temporary directory. It sets up necessary attributes like the repository URL, temporary directory path, and references to the cloned repository and its latest commit. If cloning fails, it raises a RuntimeError after cleaning up resources.
    *   *Parameters:*
        - **`repo_url`** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self):`
        *   *Description:* Retrieves a list of all files in the repository and creates RepoFile objects for each file. These objects are stored in the instance's 'files' attribute and returned. The method uses git ls-files to enumerate the files.
        *   *Parameters:*
            - **`self`** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **`files`** (`list[RepoFile]`): A list of RepoFile instances representing the files in the repository.
        *   **Usage:**
  * **Calls:** This method does not call any other methods internally.
  * **Called By:** This method is not called by any other methods according to the provided context.
    *   **`close`**
        *   *Signature:* `def close(self):`
        *   *Description:* Deletes the temporary directory and its contents associated with the repository. It also resets the temp_dir attribute to None to indicate that cleanup has occurred.
        *   *Parameters:*
            - **`self`** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods internally.
  * **Called By:** This method is not called by any other methods according to the provided context.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self):`
        *   *Description:* Enables the use of the GitRepository instance in a 'with' statement, returning itself to allow access to its methods during the context block.
        *   *Parameters:*
            - **`self`** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **`self`** (`GitRepository`): The GitRepository instance itself.
        *   **Usage:**
  * **Calls:** This method does not call any other methods internally.
  * **Called By:** This method is not called by any other methods according to the provided context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb):`
        *   *Description:* Implements the context manager's exit protocol, automatically calling the close() method when exiting a 'with' block to ensure cleanup of temporary resources.
        *   *Parameters:*
            - **`self`** (`GitRepository`): The instance of the GitRepository class.
            - **`exc_type`** (`Any`): Exception type if an exception was raised in the with block.
            - **`exc_val`** (`Any`): Exception value if an exception was raised in the with block.
            - **`exc_tb`** (`Any`): Exception traceback if an exception was raised in the with block.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method calls the close() method internally.
  * **Called By:** This method is not called by any other methods according to the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content=False):`
        *   *Description:* Constructs a hierarchical tree representation of the repository's file structure. If no files have been loaded yet, it calls get_all_files() to load them. Then, it iterates over the files and builds nested dictionaries representing directories and files.
        *   *Parameters:*
            - **`self`** (`GitRepository`): The instance of the GitRepository class.
            - **`include_content`** (`bool`): Flag indicating whether to include file content in the returned dictionary.
        *   *Returns:*
            - **`tree`** (`dict`): A nested dictionary representing the file tree structure.
        *   **Usage:**
  * **Calls:** This method calls the get_all_files() method internally if the files list is empty.
  * **Called By:** This method is not called by any other methods according to the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str):`
*   **Description:** Die Funktion erstellt ein Balkendiagramm zur Darstellung des Token-Vergleichs zwischen JSON und TOON Format. Sie verwendet matplotlib zur Erstellung des Diagramms und speichert das Ergebnis in einer Datei. Das Diagramm zeigt die Anzahl der Tokens für beide Formate sowie den Prozentsatz der Einsparung. Die Funktion nimmt die Token-Anzahlen, den Einsparungsprozentsatz und den Ausgabepfad als Parameter entgegen.
*   **Parameters:**
    - **`json_tokens`** (`int`): Die Anzahl der Tokens im JSON-Format.
    - **`toon_tokens`** (`int`): Die Anzahl der Tokens im TOON-Format.
    - **`savings_percent`** (`float`): Der Prozentsatz der Einsparung zwischen den beiden Formaten.
    - **`output_path`** (`str`): Der Dateipfad, unter dem das generierte Diagramm gespeichert wird.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.
  * **Called By:** Die Funktion wird von der Funktion 'main_workflow' in der Datei 'main.py' aufgerufen.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items: int, batch_size: int, model_name: str):`
*   **Description:** The function calculates the net time duration between a start and end time, adjusted for sleep periods caused by rate limits. It specifically handles cases where the model name starts with 'gemini-', applying additional logic to account for batching and associated sleep times. If the model is not a gemini model, it simply returns the total duration. For zero items, it returns zero. Otherwise, it computes the number of batches, determines the sleep count based on batch size, and subtracts the total sleep time from the overall duration.
*   **Parameters:**
    - **`start_time`** (`float or datetime`): The starting timestamp or time value.
    - **`end_time`** (`float or datetime`): The ending timestamp or time value.
    - **`total_items`** (`int`): The total number of items processed.
    - **`batch_size`** (`int`): The maximum number of items per batch.
    - **`model_name`** (`str`): The name of the model being used, which determines whether rate limit adjustments apply.
*   **Returns:**
    - **`net_time`** (`float or int`): The calculated net time after adjusting for sleep periods due to rate limits.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `evaluation` (function) in `evaluation.py` at line `249`; `evaluation` (function) in `evaluation.py` at line `275`; `main_workflow` (function) in `main.py` at line `311`; `main_workflow` (function) in `main.py` at line `342`

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None):`
*   **Description:** The `main_workflow` function orchestrates a comprehensive code analysis pipeline for a given repository URL. It begins by extracting API keys and model names, determining appropriate API keys and base URLs based on model types. It then clones the repository, extracts basic project information, constructs a file tree, performs relationship analysis, and generates an abstract syntax tree (AST). The function prepares inputs for a helper LLM to analyze functions and classes, then calls the helper LLM to generate documentation for these elements. Subsequently, it prepares inputs for a main LLM to generate a final report, including token usage statistics. Finally, it saves the report and associated metrics.
*   **Parameters:**
    - **`input`** (`Any`): The input containing the repository URL to be analyzed.
    - **`api_keys`** (`dict`): A dictionary containing API keys for various services such as Gemini, OpenAI, and SCADsLLM.
    - **`model_names`** (`dict`): A dictionary specifying the names of helper and main models to be used for analysis.
    - **`status_callback`** (`Callable[[str], None]`): An optional callback function to report the progress of the workflow.
*   **Returns:**
    - **`report`** (`str`): The final markdown report generated by the main LLM.
    - **`metrics`** (`dict`): A dictionary containing timing metrics for helper and main LLM operations.
*   **Usage:**
  * **Calls:** This function internally calls several components including GitRepository for cloning repositories, ProjektInfoExtractor for extracting basic project information, ProjectAnalyzer for relationship analysis, ASTAnalyzer for AST creation, LLMHelper for function and class analysis, and MainLLM for generating the final report.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `489`; `backend.main` (module) in `main.py` at line `533`

#### Function: `update_status`
*   **Signature:** `def update_status(msg):`
*   **Description:** The function 'update_status' is designed to handle status updates by invoking an optional callback function if one is defined, followed by logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages throughout the application.
*   **Parameters:**
    - **`msg`** (`Any`): The status message to be processed and logged.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** This function internally checks for and invokes the 'status_callback' function if it exists, and logs the provided message using 'logging.info'.
  * **Called By:** This function is called multiple times (14 instances) from the 'main_workflow' function in 'main.py', typically at various stages of the workflow execution to report progress or status changes.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root):`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases where the filepath is not within the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure.
*   **Parameters:**
    - **`filepath`** (`str`): The absolute or relative path to a Python file.
    - **`project_root`** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    - **`module_path`** (`str`): A dot-separated module path derived from the given file path.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `_collect_definitions` (method) in `relationship_analyzer.py` at line `60`; `__init__` (method) in `relationship_analyzer.py` at line `134`

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is responsible for analyzing Python project structures by identifying definitions (functions, classes, methods) and tracking their call relationships across files. It walks through the project directory, parses Python files using AST, collects definitions with their metadata, resolves inter-file calls, and formats the results into a structured output showing which functions or methods are called by whom.
*   **Instantiation:** This class is instantiated by the functions `evaluation` in `evaluation.py` at line 119 and `main_workflow` in `main.py` at line 177.
*   **Dependencies:** No external dependencies were explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including storage for definitions, call graphs, and ASTs of parsed files, along with a set of directories to ignore during traversal.
    *   *Parameters:*
        - **`project_root`** (`str`): The absolute path to the root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self):`
        *   *Description:* The main analysis method that orchestrates the process of finding Python files, collecting definitions from those files, resolving call relationships between functions and methods, and finally formatting the collected information into a structured result.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`output_list`** (`list`): A list of dictionaries representing definitions and their callers, formatted with identifiers, types, origins, and call details.
        *   **Usage:**
  * **Calls:** This method internally calls `_find_py_files`, `_collect_definitions`, and `_resolve_calls` for each Python file in the project, and then calls `get_formatted_results` to prepare the final output.
  * **Called By:** `evaluation` (function) in `evaluation.py` at line `120`; `main_workflow` (function) in `main.py` at line `178`
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self):`
        *   *Description:* Traverses the project root directory recursively, ignoring specified directories such as .git and venv, and collects all Python (.py) files into a list.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`py_files`** (`list`): A list of absolute paths to all Python files found in the project directory excluding ignored directories.
        *   **Usage:**
  * **Calls:** This method does not call any other methods directly.
  * **Called By:** This method is called by the `analyze` method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath):`
        *   *Description:* Parses a given Python file using the Abstract Syntax Tree (AST) module to extract function and class definitions. It associates these definitions with their respective modules and stores metadata like file location and definition type.
        *   *Parameters:*
            - **`filepath`** (`str`): The absolute path to the Python file whose definitions need to be collected.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not call any other methods directly.
  * **Called By:** This method is called by the `analyze` method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node):`
        *   *Description:* Given an AST node and a tree, this helper method attempts to find the parent node of the given node by walking the AST.
        *   *Parameters:*
            - **`tree`** (`ast.AST`): The full AST of the file being processed.
            - **`node`** (`ast.AST`): The AST node for which we want to find the parent.
        *   *Returns:*
            - **`parent`** (`ast.AST or None`): The parent AST node of the given node, or None if not found.
        *   **Usage:**
  * **Calls:** This method does not call any other methods directly.
  * **Called By:** This method is called by the `_collect_definitions` method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath):`
        *   *Description:* Processes a Python file's AST to resolve and record call relationships between functions and methods. It uses a CallResolverVisitor to traverse the AST and update the call graph based on discovered calls.
        *   *Parameters:*
            - **`filepath`** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method creates a CallResolverVisitor instance and visits the AST to resolve calls, updating the call_graph accordingly.
  * **Called By:** This method is called by the `analyze` method.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self):`
        *   *Description:* Formats the collected call graph and definition information into a structured list of dictionaries. Each dictionary represents a definition and includes details about where it was defined and who called it.
        *   *Parameters:*
            *None*
        *   *Returns:*
            - **`output_list`** (`list`): A list of dictionaries containing formatted definition and call relationship data.
        *   **Usage:**
  * **Calls:** This method does not call any other methods directly.
  * **Called By:** This method is called by the `analyze` method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to analyze Python code and resolve call relationships between functions and methods. It tracks the current execution context (such as class and function names) and records calls made within the code, associating them with their callers. Additionally, it maintains information about imported modules and class instantiations to aid in resolving qualified names and tracking types.
*   **Instantiation:** This class is instantiated by the `_resolve_calls` function in the `relationship_analyzer.py` file at line 92.
*   **Dependencies:** No external dependencies are specified.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and definitions dictionary. It sets up internal state including scope tracking, instance types, and call recording structures.
    *   *Parameters:*
        - **`filepath`** (`str`): The path to the Python file being analyzed.
        - **`project_root`** (`str`): The root directory of the project, used to compute module paths.
        - **`definitions`** (`dict`): A dictionary mapping qualified names to their definitions for resolution purposes.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node):`
        *   *Description:* Handles the visitation of class definitions in the AST. It updates the current class name context during traversal and restores it after visiting the class body.
        *   *Parameters:*
            - **`node`** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not explicitly call any other functions.
  * **Called By:** This method is invoked by the generic AST visitor when encountering a class definition.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node):`
        *   *Description:* Handles the visitation of function definitions in the AST. It updates the current caller name context to reflect the function being visited and restores it after traversal.
        *   *Parameters:*
            - **`node`** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not explicitly call any other functions.
  * **Called By:** This method is invoked by the generic AST visitor when encountering a function definition.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node):`
        *   *Description:* Processes call expressions in the AST. It resolves the qualified name of the called function and records the call along with caller information if the callee is defined in the provided definitions.
        *   *Parameters:*
            - **`node`** (`ast.Call`): The AST node representing the function call.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method calls the private helper method `_resolve_call_qname` to determine the qualified name of the called function.
  * **Called By:** This method is invoked by the generic AST visitor when encountering a function call expression.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node):`
        *   *Description:* Handles import statements in the AST. It adds imported names to the scope mapping for later resolution of qualified names.
        *   *Parameters:*
            - **`node`** (`ast.Import`): The AST node representing the import statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not explicitly call any other functions.
  * **Called By:** This method is invoked by the generic AST visitor when encountering an import statement.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node):`
        *   *Description:* Handles 'from ... import ...' statements in the AST. It computes the fully qualified module path and maps imported names to their qualified names in the scope.
        *   *Parameters:*
            - **`node`** (`ast.ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not explicitly call any other functions.
  * **Called By:** This method is invoked by the generic AST visitor when encountering a 'from ... import ...' statement.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node):`
        *   *Description:* Handles assignment statements in the AST. Specifically, it identifies assignments to instances of classes defined in the project and records the type of those instances.
        *   *Parameters:*
            - **`node`** (`ast.Assign`): The AST node representing the assignment statement.
        *   *Returns:*
            *None*
        *   **Usage:**
  * **Calls:** This method does not explicitly call any other functions.
  * **Called By:** This method is invoked by the generic AST visitor when encountering an assignment statement.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node):`
        *   *Description:* Resolves the qualified name of a function call based on the AST node representing the function. It handles both direct name references and attribute access (e.g., obj.method).
        *   *Parameters:*
            - **`func_node`** (`ast.expr`): The AST node representing the function being called.
        *   *Returns:*
            - **`qualified_name`** (`str or None`): The resolved qualified name of the function or None if resolution fails.
        *   **Usage:**
  * **Calls:** This method does not explicitly call any other functions.
  * **Called By:** This method is called by the `visit_Call` method to resolve the qualified name of a function call.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str):`
*   **Description:** The function encrypts a given text string using a Fernet cipher suite. It first checks if the input text is empty or if the cipher suite is not available; in such cases, it returns the input text as-is. If both conditions are satisfied, it encodes the stripped text to bytes, encrypts it using the cipher suite, and then decodes the result back to a string for return.
*   **Parameters:**
    - **`text`** (`str`): The text string to be encrypted.
*   **Returns:**
    - **`encrypted_text`** (`str`): The encrypted version of the input text, returned as a string.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** This function is called by the update_gemini_key function in the db.py file.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str):`
*   **Description:** The function decrypts a given text string using a global cipher suite. It first checks if the input text is valid and if the cipher suite is available; if not, it returns the original text. If both are present, it attempts to decrypt the text by encoding it, decrypting it with the cipher suite, and then decoding the result back to a string. In case of any exception during decryption, it gracefully returns the original text.
*   **Parameters:**
    - **`text`** (`str`): The encrypted text string to be decrypted.
*   **Returns:**
    - **`return_value`** (`str`): The decrypted string if successful, otherwise the original input text.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** This function is called by the function 'get_decrypted_api_keys' in the file 'db.py'.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str):`
*   **Description:** This function inserts a new user into a MongoDB collection by creating a user document with the provided username, name, and password. The password is hashed using a hasher utility before being stored. The function also initializes additional fields such as API keys and returns the ID of the inserted document.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier for the user, used as the '_id' field in the database.
    - **`name`** (`str`): The full name of the user.
    - **`password`** (`str`): The plain text password of the user, which gets hashed before storage.
*   **Returns:**
    - **`inserted_id`** (`ObjectId`): The unique identifier assigned by MongoDB to the newly inserted user document.
*   **Usage:**
  * **Calls:** The function internally uses the 'stauth.Hasher.hash' method to hash the password and 'dbusers.insert_one' to store the user document in the database.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `294`

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users():`
*   **Description:** This function retrieves all user documents from a MongoDB collection named 'dbusers'. It performs a database query to find all records in the collection and returns them as a list. The function does not take any parameters and directly accesses the global 'dbusers' variable, which is expected to be initialized elsewhere in the codebase.
*   **Parameters:**
    *None*
*   **Returns:**
    - **`result`** (`list`): A list containing all user documents retrieved from the 'dbusers' collection in the database.
*   **Usage:**
  * **Calls:** The function does not call any other functions directly.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `244`

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str):`
*   **Description:** This function retrieves a user document from a MongoDB collection based on the provided username. It uses the 'find_one' method to query the database with a filter matching the '_id' field to the given username. The function assumes the existence of a global variable 'dbusers' which represents the MongoDB collection.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier (username) used to locate the specific user document in the database.
*   **Returns:**
    - **`result`** (`Any`): The user document retrieved from the database if found; otherwise, None.
*   **Usage:**
  * **Calls:** The function internally calls the 'find_one' method on the 'dbusers' collection object.
  * **Called By:** None

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str):`
*   **Description:** This function updates the name field of a user in the database identified by their username. It uses MongoDB's update_one method to modify only the name field, leaving other fields unchanged. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier of the user whose name needs to be updated.
    - **`new_name`** (`str`): The new name value to set for the specified user.
*   **Returns:**
    - **`result.modified_count`** (`int`): The number of documents that were modified as a result of the update operation.
*   **Usage:**
  * **Calls:** The function internally calls dbusers.update_one to perform the database update operation.
  * **Called By:** None

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str):`
*   **Description:** This function updates a user's Gemini API key in the database after encrypting it. It takes a username and an unencrypted API key as inputs, strips any leading or trailing whitespace from the key, encrypts it using a helper function, and then updates the corresponding document in the 'dbusers' collection with the encrypted key. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **`gemini_api_key`** (`str`): The unencrypted Gemini API key provided by the user, which will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    - **`modified_count`** (`int`): The number of documents that were successfully modified in the database. This should typically be 1 if the operation succeeded.
*   **Usage:**
  * **Calls:** This function internally calls 'encrypt_text' to encrypt the provided API key before storing it.
  * **Called By:** `save_gemini_cb` (function) in `Frontend.py` at line `35`; `frontend.Frontend` (module) in `Frontend.py` at line `393`

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str):`
*   **Description:** This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and performs an update operation on the user document in the database. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier of the user whose Ollama base URL needs to be updated.
    - **`ollama_base_url`** (`str`): The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped.
*   **Returns:**
    - **`modified_count`** (`int`): The number of documents that were successfully modified by the update operation. This should typically be 1 if the user exists and the update was applied.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly; it relies on the pymongo library's update_one method.
  * **Called By:** `save_ollama_cb` (function) in `Frontend.py` at line `42`; `frontend.Frontend` (module) in `Frontend.py` at line `407`

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str):`
*   **Description:** This function retrieves a Gemini API key associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'gemini_api_key' field. If no matching user is found, it returns None.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier for the user whose Gemini API key is to be retrieved.
*   **Returns:**
    - **`gemini_api_key`** (`str or None`): The Gemini API key associated with the user, or None if no such user exists.
*   **Usage:**
  * **Calls:** The function internally uses the 'dbusers.find_one' method to query the database.
  * **Called By:** None

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str):`
*   **Description:** This function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the provided username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier for the user whose Ollama base URL is to be retrieved.
*   **Returns:**
    - **`ollama_base_url`** (`str or None`): The Ollama base URL associated with the user, or None if no such user exists.
*   **Usage:**
  * **Calls:** The function internally calls dbusers.find_one to query the database.
  * **Called By:** None

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str):`
*   **Description:** The function 'delete_user' removes a user document from a MongoDB collection identified by the provided username. It performs a deletion operation using the 'delete_one' method and returns the count of deleted documents. The function assumes the existence of a global 'dbusers' variable that represents a MongoDB collection.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **`deleted_count`** (`int`): The number of documents deleted as a result of the operation, typically 0 or 1.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly; it relies on the 'dbusers.delete_one' method from the MongoDB collection.
  * **Called By:** None

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str):`
*   **Description:** This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user does not exist, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function and retrieves the 'ollama_base_url' directly. It then returns both the decrypted Gemini API key and the Ollama base URL.
*   **Parameters:**
    - **`username`** (`str`): The unique identifier for the user whose API keys are to be retrieved.
*   **Returns:**
    - **`gemini_plain`** (`str`): The decrypted Gemini API key for the user, or an empty string if not found.
    - **`ollama_plain`** (`str`): The Ollama base URL for the user, or an empty string if not found.
*   **Usage:**
  * **Calls:** The function internally uses dbusers.find_one to retrieve user data and decrypt_text to decrypt the Gemini API key.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `380`; `frontend.Frontend` (module) in `Frontend.py` at line `479`

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str):`
*   **Description:** Erstellt einen neuen Chat-Eintrag.
*   **Parameters:**
    - **`username`** (`str`): The username associated with the chat.
    - **`chat_name`** (`str`): The name of the chat to be created.
*   **Returns:**
    - **`result.inserted_id`** (`str`): The unique identifier of the newly inserted chat document in the database.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `load_data_from_db` (function) in `Frontend.py` at line `81`; `handle_delete_chat` (function) in `Frontend.py` at line `122`; `frontend.Frontend` (module) in `Frontend.py` at line `344`

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str):`
*   **Description:** Holt alle definierten Chats eines Users.
*   **Parameters:**
    - **`username`** (`str`): Der Benutzername, für den die Chats abgerufen werden sollen.
*   **Returns:**
    - **`chats`** (`list`): Eine Liste der Chats des angegebenen Benutzers, sortiert nach Erstellungsdatum in aufsteigender Reihenfolge.
*   **Usage:**
  * **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.
  * **Called By:** Die Funktion wird von der Funktion load_data_from_db in der Datei Frontend.py aufgerufen.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str):`
*   **Description:** This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a query using MongoDB's find_one method to locate a document matching both the username and chat name criteria. If such a document is found, the function returns True; otherwise, it returns False.
*   **Parameters:**
    - **`username`** (`str`): The username associated with the chat.
    - **`chat_name`** (`str`): The name of the chat to check for existence.
*   **Returns:**
    - **`exists`** (`bool`): True if a chat with the specified username and chat name exists in the database, False otherwise.
*   **Usage:**
  * **Calls:** The function internally uses the dbchats.find_one method to query the database.
  * **Called By:** None

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str):`
*   **Description:** This function renames a chat and all associated exchanges in a database. It first updates the chat entry in the 'dbchats' collection, then updates all related exchange entries in the 'dbexchanges' collection. The function returns the number of modified chat documents.
*   **Parameters:**
    - **`username`** (`str`): The username associated with the chat to be renamed.
    - **`old_name`** (`str`): The current name of the chat to be renamed.
    - **`new_name`** (`str`): The new name to assign to the chat.
*   **Returns:**
    - **`modified_count`** (`int`): The number of chat documents that were successfully modified during the renaming operation.
*   **Usage:**
  * **Calls:** The function performs database operations using 'dbchats.update_one' and 'dbexchanges.update_many'.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `462`

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str):`
*   **Description:** This function inserts a new exchange record into a MongoDB collection. It generates a unique identifier for the exchange, constructs a dictionary with all the provided details including optional time tracking fields, and attempts to insert this data into the database. If the insertion fails, it catches the exception, prints an error message, and returns None.
*   **Parameters:**
    - **`question`** (`str`): The question asked in the exchange.
    - **`answer`** (`str`): The answer provided in response to the question.
    - **`feedback`** (`str`): Feedback associated with the exchange.
    - **`username`** (`str`): The username of the user involved in the exchange.
    - **`chat_name`** (`str`): The name of the chat session.
    - **`helper_used`** (`str`): Optional field indicating which helper was used.
    - **`main_used`** (`str`): Optional field indicating which main component was used.
    - **`total_time`** (`str`): Optional field for the total time taken for the exchange.
    - **`helper_time`** (`str`): Optional field for the time taken by the helper.
    - **`main_time`** (`str`): Optional field for the time taken by the main component.
*   **Returns:**
    - **`new_id`** (`str`): The unique ID generated for the inserted exchange, or None if insertion failed.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `530`

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str):`
*   **Description:** This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses a database query to find documents matching the username and sorts them by the 'created_at' field. The result is returned as a list of exchange records. The function does not perform any validation or transformation on the retrieved data.
*   **Parameters:**
    - **`username`** (`str`): The username to filter exchange records by.
*   **Returns:**
    - **`exchanges`** (`list`): A list of exchange records retrieved from the database for the specified username, sorted by creation timestamp.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `load_data_from_db` (function) in `Frontend.py` at line `64`

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str):`
*   **Description:** This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched documents as a list.
*   **Parameters:**
    - **`username`** (`str`): The username associated with the exchanges to be retrieved.
    - **`chat_name`** (`str`): The name of the chat associated with the exchanges to be retrieved.
*   **Returns:**
    - **`exchanges`** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order.
*   **Usage:**
  * **Calls:** The function internally uses the 'dbexchanges.find' method to query the database and 'sort' to order the results.
  * **Called By:** None

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int):`
*   **Description:** This function updates the feedback field of a document in the 'dbexchanges' collection within a MongoDB database. It takes an exchange ID and a feedback value, then attempts to update the corresponding document with the new feedback value. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    - **`exchange_id`** (`Any`): The unique identifier of the exchange document to be updated.
    - **`feedback`** (`int`): The new feedback value to be set in the document.
*   **Returns:**
    - **`modified_count`** (`int`): The number of documents that were modified as a result of the update operation.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `handle_feedback_change` (function) in `Frontend.py` at line `98`

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str):`
*   **Description:** This function updates the feedback message associated with a specific exchange document in a MongoDB collection. It takes an exchange ID and a new feedback message as inputs, then performs an atomic update operation on the database to set the feedback_message field. The function returns the count of modified documents, which should typically be 1 if the update was successful.
*   **Parameters:**
    - **`exchange_id`** (`Any`): The unique identifier of the exchange document to be updated.
    - **`feedback_message`** (`str`): The new feedback message to be stored in the exchange document.
*   **Returns:**
    - **`modified_count`** (`int`): The number of documents that were successfully modified by the update operation.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly; it relies on the dbexchanges.update_one method from the pymongo library.
  * **Called By:** `render_exchange` (function) in `Frontend.py` at line `211`

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str):`
*   **Description:** This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a given exchange ID. It performs a delete operation using the 'delete_one' method and returns the count of deleted documents. The function takes a single string parameter representing the exchange ID and uses it to construct a query to locate and remove the corresponding document.
*   **Parameters:**
    - **`exchange_id`** (`str`): A unique identifier for the exchange document to be deleted from the database.
*   **Returns:**
    - **`deleted_count`** (`int`): The number of documents that were deleted as a result of the delete operation. This will typically be 1 if a matching document was found, or 0 if no matching document was found.
*   **Usage:**
  * **Calls:** The function does not call any other functions directly.
  * **Called By:** `handle_delete_exchange` (function) in `Frontend.py` at line `102`

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str):`
*   **Description:** The function deletes all exchanges and the chat entry associated with a given username and chat name from the database. It first removes all exchange records matching the criteria, then deletes the corresponding chat record. The function returns the count of deleted chat entries, which should be 1 if the operation was successful.
*   **Parameters:**
    - **`username`** (`str`): The username associated with the chat to be deleted.
    - **`chat_name`** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **`deleted_count`** (`int`): The number of chat documents deleted from the database.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly; it relies on external database operations via dbexchanges and dbchats.
  * **Called By:** `handle_delete_chat` (function) in `Frontend.py` at line `110`

### File: `frontend/Frontend.py`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb():`
*   **Description:** This function handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key for the current user, clears the input field, and displays a success message to the user. The function does not take any parameters and does not return any value.
*   **Parameters:**
    *None*
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** None

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb():`
*   **Description:** This function is designed to save a new Ollama URL entered by the user in the frontend interface. It retrieves the URL from the Streamlit session state, checks if it's non-empty, and then updates the database with the new URL associated with the current username. Upon successful update, it displays a success message to the user using a toast notification.
*   **Parameters:**
    *None*
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** The function internally uses `st.session_state.get` to retrieve the Ollama URL and `db.update_ollama_url` to persist the URL in the database.
  * **Called By:** None

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str):`
*   **Description:** Die Funktion 'load_data_from_db' lädt Chats und Exchanges konsistent aus einer Datenbank für einen bestimmten Benutzer. Sie prüft zunächst, ob der Benutzer bereits geladen wurde, und lädt nur dann neue Daten, wenn dies erforderlich ist. Anschließend werden Chats und Exchanges aus der Datenbank abgerufen und in den Streamlit-Session-State eingefügt. Bei Bedarf wird ein Standard-Chat erstellt und der aktive Chat festgelegt.
*   **Parameters:**
    - **`username`** (`str`): Der Name des Benutzers, für den die Daten aus der Datenbank geladen werden sollen.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** Die Funktion ruft keine anderen internen Funktionen auf.
  * **Called By:** Die Funktion wird von der Methode 'frontend.Frontend' in der Datei 'Frontend.py' auf Zeile 310 aufgerufen.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val):`
*   **Description:** This function updates the feedback value for a given exchange record in the database and triggers a Streamlit rerun to refresh the UI. It takes an exchange dictionary and a new feedback value, updates the 'feedback' key in the dictionary, saves the updated feedback to the database using the exchange ID, and then reruns the Streamlit app to reflect the changes.
*   **Parameters:**
    - **`ex`** (`dict`): A dictionary representing an exchange record, expected to contain keys like 'feedback' and '_id'.
    - **`val`** (`Any`): The new feedback value to be assigned to the exchange record.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** This function internally calls `db.update_exchange_feedback` to update the feedback in the database and `st.rerun()` to refresh the Streamlit UI.
  * **Called By:** `render_exchange` (function) in `Frontend.py` at line `199`; `render_exchange` (function) in `Frontend.py` at line `204`

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex):`
*   **Description:** This function handles the deletion of an exchange from the database and updates the session state accordingly. It first deletes the exchange from the database using its ID, then checks if the exchange exists in the session state for a given chat and removes it if found. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    - **`chat_name`** (`str`): The name of the chat from which the exchange should be removed.
    - **`ex`** (`dict`): A dictionary representing the exchange to be deleted, expected to contain an '_id' key.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** The function internally calls `db.delete_exchange_by_id` to delete the exchange from the database.
  * **Called By:** `render_exchange` (function) in `Frontend.py` at line `228`; `render_exchange` (function) in `Frontend.py` at line `234`

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name):`
*   **Description:** This function handles the deletion of a chat by first removing the chat from the database and then cleaning up the session state. It ensures that the active chat is updated appropriately after deletion, either by selecting another existing chat or by creating a new default chat if none remain. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    - **`username`** (`str`): The username associated with the chat to be deleted.
    - **`chat_name`** (`str`): The name of the chat to be deleted.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** This function does not call any other functions directly; it relies on external modules like 'db' and 'st.session_state'.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `367`

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text):`
*   **Description:** The function 'extract_repo_name' takes a text input and attempts to extract a repository name from any URL present in the text. It uses regular expressions to find a URL, parses it using urllib.parse.urlparse, extracts the path component, and then derives the repository name from the last segment of the path. If the repository name ends with '.git', it removes the extension. If no URL is found or the path is empty, it returns None.
*   **Parameters:**
    - **`text`** (`str`): A string that may contain a URL from which to extract the repository name.
*   **Returns:**
    - **`repo_name`** (`str`): The extracted repository name from the URL, with '.git' suffix removed if present, or None if no valid URL is found.
*   **Usage:**
  * **Calls:** This function does not call any other functions directly; it relies on imported modules like 're' and 'urllib.parse.urlparse'.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `442`

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text):`
*   **Description:** The function 'stream_text_generator' takes a string of text as input and yields each word from the text followed by a space, with a small delay between each word. It is designed to simulate a streaming effect for text display. The function uses 'time.sleep' to introduce a brief pause between yielding each word.
*   **Parameters:**
    - **`text`** (`str`): A string containing the text to be streamed word by word.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** This function does not call any other functions directly.
  * **Called By:** `render_text_with_mermaid` (function) in `Frontend.py` at line `160`

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream=False):`
*   **Description:** This function processes a markdown text string to identify and render Mermaid diagrams embedded within code blocks. It splits the input text based on Mermaid code block delimiters and handles regular markdown content separately from Mermaid diagrams. For non-Mermaid content, it either streams or displays the content as markdown depending on the streaming flag. For Mermaid diagrams, it attempts to render them using a dedicated Mermaid component, falling back to displaying the raw code if rendering fails.
*   **Parameters:**
    - **`markdown_text`** (`str`): A string containing markdown-formatted text that may include Mermaid diagram code blocks enclosed in triple backticks with 'mermaid' language specifier.
    - **`should_stream`** (`bool`): A boolean flag indicating whether to stream the non-Mermaid markdown content instead of rendering it directly.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** The function does not call any other functions directly; it relies on external libraries like 're', 'st_mermaid', 'st.write_stream', 'st.markdown', and 'st.code'.
  * **Called By:** `render_exchange` (function) in `Frontend.py` at line `238`; `frontend.Frontend` (module) in `Frontend.py` at line `524`

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name):`
*   **Description:** The function `render_exchange` renders a chat exchange in a Streamlit interface, displaying a user's question and an assistant's response. It handles both successful responses and error cases, providing interactive elements such as feedback buttons, comment popovers, download options, and delete functionality. The assistant's response is rendered with Mermaid support. It uses various Streamlit components like `chat_message`, `container`, `button`, `popover`, `download_button`, and `error` to build the UI.
*   **Parameters:**
    - **`ex`** (`dict`): A dictionary representing the exchange, containing keys like 'question', 'answer', 'feedback', 'feedback_message', '_id', etc.
    - **`current_chat_name`** (`str`): The name of the current chat session, used for handling deletion operations.
*   **Returns:**
    *None*
*   **Usage:**
  * **Calls:** This function internally utilizes several Streamlit and custom helper functions such as `st.chat_message`, `st.container`, `st.button`, `st.popover`, `st.download_button`, `st.error`, `st.write`, `st.caption`, `st.text_area`, `st.success`, `time.sleep`, `st.rerun`, `render_text_with_mermaid`, `handle_feedback_change`, and `handle_delete_exchange`. These are used to construct the UI and manage interactions.
  * **Called By:** `frontend.Frontend` (module) in `Frontend.py` at line `429`

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the metadata of a single function parameter. It encapsulates three essential attributes: the parameter's name, its type, and a descriptive explanation. This class ensures data integrity and provides a standardized structure for parameter descriptions, making it suitable for use in API schemas, documentation systems, or any application requiring structured parameter metadata.
*   **Instantiation:** This class is not explicitly instantiated by any other component listed in the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the source file.
*   **Constructor:**
    *   *Description:* The constructor initializes a ParameterDescription instance with three required fields: name, type, and description. These fields are defined as string types and are used to store metadata about a function parameter.
    *   *Parameters:*
        - **`name`** (`str`): The name of the function parameter.
        - **`type`** (`str`): The data type of the function parameter.
        - **`description`** (`str`): A textual description of the function parameter's purpose or usage.
*   **Methods:**
    *None*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to represent and validate the description of a function's return value. It encapsulates three essential properties: the name of the return value, its type, and a textual description. This class ensures data integrity and structure for return value metadata, making it suitable for use in API schemas, documentation systems, or any application requiring standardized return value definitions.
*   **Instantiation:** This class is not instantiated by any other components as indicated by the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* The constructor initializes a ReturnDescription instance with three required fields: name, type, and description. These fields are typical attributes of a return value descriptor and are expected to be provided during instantiation.
    *   *Parameters:*
        - **`name`** (`str`): The name of the return value.
        - **`type`** (`str`): The type of the return value.
        - **`description`** (`str`): A textual description of the return value.
*   **Methods:**
    *None*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function. It encapsulates two string fields: 'calls', which describes the functions or methods that are called by the function in question, and 'called_by', which indicates the function or method that invokes the function in question. This class serves as a structured way to document and enforce the usage context of functions within a system.
*   **Instantiation:** This class is not instantiated by any other components as per the provided context.
*   **Dependencies:** No external dependencies are explicitly listed for this class.
*   **Constructor:**
    *   *Description:* Initializes the UsageContext model with two required string fields: 'calls' and 'called_by'.
    *   *Parameters:*
        - **`calls`** (`str`): A string describing the functions or methods that are called by the function in question.
        - **`called_by`** (`str`): A string indicating the function or method that invokes the function in question.
*   **Methods:**
    *None*

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate detailed metadata about a function, including its overall purpose, parameter descriptions, return value details, and usage context. It serves as a structured representation for documenting function signatures and behaviors, likely used in automated documentation systems or API analysis tools.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The constructor initializes a FunctionDescription instance with four required fields: overall (a string describing the function's purpose), parameters (a list of ParameterDescription objects detailing function arguments), returns (a list of ReturnDescription objects detailing return values), and usage_context (a UsageContext object providing information on how the function is used).
    *   *Parameters:*
        - **`overall`** (`str`): A string describing the overall purpose and functionality of the function.
        - **`parameters`** (`List[ParameterDescription]`): A list of ParameterDescription objects that define each parameter accepted by the function.
        - **`returns`** (`List[ReturnDescription]`): A list of ReturnDescription objects that define each return value produced by the function.
        - **`usage_context`** (`UsageContext`): An object containing contextual information about how the function is used.
*   **Methods:**
    *None*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic model designed to represent the complete JSON schema for a function. It encapsulates essential information about a function including its unique identifier, a detailed description, and an optional error field. This class serves as a structured data container for function metadata, facilitating consistent representation and validation of function-related data within the system.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a FunctionAnalysis instance with required fields for identifier and description, and an optional error field set to None by default.
    *   *Parameters:*
        - **`identifier`** (`str`): A unique string identifier for the function.
        - **`description`** (`schemas.types.FunctionDescription`): An instance of FunctionDescription containing detailed information about the function.
        - **`error`** (`Optional[str]`): An optional string field to store error messages related to the function, defaulting to None.
*   **Methods:**
    *None*

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to describe the initialization method (__init__) of a class. It encapsulates a textual description of the constructor's purpose and a list of parameter descriptions that define its interface.
*   **Instantiation:** This class is not instantiated by any other component as per the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription instance with a description of the constructor and a list of parameter descriptions.
    *   *Parameters:*
        - **`description`** (`str`): A string describing the purpose or behavior of the constructor.
        - **`parameters`** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing each parameter of the constructor.
*   **Methods:**
    *None*

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields are intended to store information about the class's external dependencies and the entities that create instances of the class.
    *   *Parameters:*
        - **`dependencies`** (`str`): A string describing the external dependencies of the class.
        - **`instantiated_by`** (`str`): A string describing the entities or classes that instantiate this class.
*   **Methods:**
    *None*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information. This class serves as a structured representation for documenting and communicating the essential characteristics and behaviors of a class within a codebase.
*   **Instantiation:** This class is not instantiated by any other component within the provided context.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond its base Pydantic model and the types it references.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ClassDescription class with specified attributes for overall purpose, constructor description, methods analysis, and usage context.
    *   *Parameters:*
        - **`overall`** (`str`): A string describing the overall purpose and role of the class being analyzed.
        - **`init_method`** (`schemas.types.ConstructorDescription`): An object containing detailed information about the class's constructor, including its parameters and initialization logic.
        - **`methods`** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each representing a method within the class and its associated metadata.
        - **`usage_context`** (`schemas.types.ClassContext`): An object providing contextual information about how the class is used, such as dependencies and instantiation points.
*   **Methods:**
    *None*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential information about a class including its identifier, a detailed description, and an optional error field. This class is designed to provide a standardized structure for documenting class metadata and associated descriptions, making it suitable for use in documentation systems or schema validation processes.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a new instance of the ClassAnalysis class with the required identifier and description fields, and an optional error field.
    *   *Parameters:*
        - **`identifier`** (`str`): A string identifier for the class being described.
        - **`description`** (`schemas.types.ClassDescription`): An instance of ClassDescription containing detailed information about the class.
        - **`error`** (`Optional[str]`): An optional string field to store any error messages related to the class analysis.
*   **Methods:**
    *None*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for documenting call relationships within the system.
*   **Instantiation:** This class is not instantiated by any other components as per the provided context.
*   **Dependencies:** No external dependencies were identified for this class.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo instance with file, function name, call mode, and line number attributes.
    *   *Parameters:*
        - **`file`** (`str`): The file path where the call occurs.
        - **`function`** (`str`): The name of the function being called.
        - **`mode`** (`str`): The mode of the call, such as 'method', 'function', or 'module'.
        - **`line`** (`int`): The line number in the file where the call occurs.
*   **Methods:**
    *None*

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing functions. It encapsulates two key pieces of information: a list of function names that the analyzed function calls, and a list of CallInfo objects representing functions that call the analyzed function. This model serves as a standardized way to represent function call relationships and dependencies within a codebase.
*   **Instantiation:** This class is instantiated in the evaluation.py file within the evaluation function at line 162, and also in main.py within the main_workflow function at line 223.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes the FunctionContextInput model with two fields: 'calls', which is a list of strings representing function names called by the analyzed function, and 'called_by', which is a list of CallInfo objects representing functions that call the analyzed function.
    *   *Parameters:*
        - **`calls`** (`List[str]`): A list of strings representing the names of functions called by the analyzed function.
        - **`called_by`** (`List[CallInfo]`): A list of CallInfo objects representing functions that call the analyzed function.
*   **Methods:**
    *None*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates all necessary information including the mode of operation, identifier, source code, imports, and contextual data required for function analysis.
*   **Instantiation:** The class is instantiated by the evaluation function in evaluation.py at line 167 and by the main_workflow function in main.py at line 228.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic components.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput class with required fields including the mode, identifier, source code, imports list, and context. The mode is constrained to the literal value 'function_analysis', ensuring strict adherence to the expected operational mode.
    *   *Parameters:*
        - **`mode`** (`Literal['function_analysis']`): A literal string value that must be 'function_analysis' to indicate the operational mode.
        - **`identifier`** (`str`): A string identifier for the function being analyzed.
        - **`source_code`** (`str`): The raw source code of the function to be analyzed.
        - **`imports`** (`List[str]`): A list of import statements used in the function's source code.
        - **`context`** (`schemas.types.FunctionContextInput`): An object containing contextual information about the function's usage and environment.
*   **Methods:**
    *None*

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to represent structured context information for a class's methods. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a data transfer object to facilitate the communication of method-level metadata within a system.
*   **Instantiation:** This class is instantiated in the evaluation.py file within the evaluation function at line 187 and in main.py within the main_workflow function at line 248.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes a MethodContextInput instance with fields for storing method context information including identifier, calls, called_by, args, and docstring.
    *   *Parameters:*
        - **`identifier`** (`str`): A string identifier for the method.
        - **`calls`** (`List[str]`): A list of strings representing the identifiers of methods called by this method.
        - **`called_by`** (`List[CallInfo]`): A list of CallInfo objects representing the methods that call this method.
        - **`args`** (`List[str]`): A list of strings representing the argument names of the method.
        - **`docstring`** (`Optional[str]`): An optional string containing the docstring of the method.
*   **Methods:**
    *None*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to encapsulate structured context information for analyzing a class. It holds three main pieces of data: a list of dependencies, a list of call information for instances where the class is instantiated, and a list of method contexts for each method within the class. This class serves as a data container to facilitate the systematic analysis and documentation of class structures.
*   **Instantiation:** The class is instantiated by the functions main_orchestrator in HelperLLM.py at line 369, evaluation in evaluation.py at line 199, and main_workflow in main.py at line 260.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond those imported in the file.
*   **Constructor:**
    *   *Description:* The constructor for ClassContextInput initializes the instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are expected to hold lists of strings, CallInfo objects, and MethodContextInput objects respectively.
    *   *Parameters:*
        - **`dependencies`** (`List[str]`): A list of string identifiers representing the dependencies of the class.
        - **`instantiated_by`** (`List[CallInfo]`): A list of CallInfo objects indicating where and how the class is instantiated.
        - **`method_context`** (`List[MethodContextInput]`): A list of MethodContextInput objects describing the context for each method within the class.
*   **Methods:**
    *None*

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class serves as a structured input model for generating a ClassAnalysis object. It encapsulates all necessary information required for performing a detailed analysis of a Python class, including the class's source code, its identifier, associated imports, and contextual metadata.
*   **Instantiation:** The class is instantiated by the main_orchestrator function in HelperLLM.py at line 338, the evaluation function in evaluation.py at line 205, and the main_workflow function in main.py at line 266.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports list.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysisInput instance with fields representing the mode of analysis, the class identifier, the source code of the class, a list of import statements, and the contextual information about the class.
    *   *Parameters:*
        - **`mode`** (`Literal["class_analysis"]`): A literal string indicating the mode of analysis, specifically set to "class_analysis".
        - **`identifier`** (`str`): A string identifier for the class being analyzed.
        - **`source_code`** (`str`): The complete source code of the class to be analyzed.
        - **`imports`** (`List[str]`): A list of import statements used within the class's source code.
        - **`context`** (`schemas.types.ClassContextInput`): An object containing contextual metadata about the class, such as dependencies and instantiation details.
*   **Methods:**
    *None*

---
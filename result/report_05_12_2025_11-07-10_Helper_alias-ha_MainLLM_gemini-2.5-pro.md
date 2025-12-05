# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated documentation generation agent. It clones a Git repository, performs static code analysis to build an Abstract Syntax Tree (AST) and a call graph, and then uses a multi-LLM pipeline to analyze the code and synthesize a comprehensive technical report. The process is managed through a Streamlit-based web interface.
- **Key Features:**
  - Git repository cloning and file parsing.
  - Abstract Syntax Tree (AST) and call graph generation.
  - Dual-LLM architecture (Helper/Main) for detailed code analysis and report synthesis.
  - Streamlit frontend for user interaction and report display.
  - Database integration for managing user data and analysis history.
- **Tech Stack:** Python, Streamlit, LangChain, NetworkX, GitPython, Pydantic, Matplotlib. The LLM integrations support Google Gemini, OpenAI GPT models, and local models via Ollama.

*   **Repository Structure:**
    ```mermaid
    graph TD
        root["root"]
        root --> SystemPrompts_dir["SystemPrompts"]
        SystemPrompts_dir --> SystemPrompts_files["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt"]
        root --> backend_dir["backend"]
        backend_dir --> backend_files["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py"]
        root --> database_dir["database"]
        database_dir --> database_files["db.py"]
        root --> frontend_dir["frontend"]
        frontend_dir --> frontend_streamlit_dir[".streamlit"]
        frontend_streamlit_dir --> frontend_streamlit_files["config.toml"]
        frontend_dir --> frontend_files["Frontend.py<br/>__init__.py"]
        frontend_dir --> gifs_dir["gifs"]
        gifs_dir --> gifs_files["4j.gif"]
        root --> notizen_dir["notizen"]
        notizen_dir --> notizen_files["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
        notizen_dir --> grafiken_dir["grafiken"]
        grafiken_dir --> grafiken_1_dir["1"]
        grafiken_1_dir --> grafiken_1_files["File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
        grafiken_dir --> grafiken_2_dir["2"]
        grafiken_2_dir --> grafiken_2_files["FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot"]
        grafiken_dir --> Flask_Repo_dir["Flask-Repo"]
        Flask_Repo_dir --> Flask_Repo_files["__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot"]
        grafiken_dir --> Repo_onboarding_dir["Repo-onboarding"]
        Repo_onboarding_dir --> Repo_onboarding_files["AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot"]
        root --> result_dir["result"]
        result_dir --> result_files["ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
        root --> schemas_dir["schemas"]
        schemas_dir --> schemas_files["types.py"]
        root --> statistics_dir["statistics"]
        statistics_dir --> statistics_files["savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png"]
        root --> root_files[".env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt"]
    ```

## 2. Installation
### Dependencies
To install the required dependencies, run the following command in your terminal:
```bash
pip install -r requirements.txt
```
Key dependencies include:
- `altair`
- `annotated-types`
- `anyio`
- `attrs`
- `bcrypt`
- `blinker`
- `cachetools`
- `captcha`
- `certifi`
- `cffi`
- `charset-normalizer`
- `click`
- `colorama`
- `contourpy`
- `cryptography`
- `cycler`
- `distro`
- `dnspython`
- `dotenv`
- `entrypoints`
- `extra-streamlit-components`
- `filetype`
- `fonttools`
- `gitdb`
- `GitPython`
- `google-ai-generativelanguage`
- `google-api-core`
- `google-auth`
- `googleapis-common-protos`
- `grpcio`
- `grpcio-status`
- `h11`
- `httpcore`
- `httpx`
- `idna`
- `Jinja2`
- `jiter`
- `jsonpatch`
- `jsonpointer`
- `jsonschema`
- `jsonschema-specifications`
- `kiwisolver`
- `langchain`
- `langchain-core`
- `langchain-google-genai`
- `langchain-ollama`
- `langchain-openai`
- `langgraph`
- `langgraph-checkpoint`
- `langgraph-prebuilt`
- `langgraph-sdk`
- `langsmith`
- `MarkupSafe`
- `matplotlib`
- `narwhals`
- `networkx`
- `numpy`
- `ollama`
- `openai`
- `orjson`
- `ormsgpack`
- `packaging`
- `pandas`
- `pillow`
- `proto-plus`
- `protobuf`
- `pyarrow`
- `pyasn1`
- `pyasn1_modules`
- `pycparser`
- `pydantic`
- `pydantic_core`
- `pydeck`
- `PyJWT`
- `pymongo`
- `pyparsing`
- `python-dateutil`
- `python-dotenv`
- `pytz`
- `PyYAML`
- `referencing`
- `regex`
- `requests`
- `requests-toolbelt`
- `rpds-py`
- `rsa`
- `setuptools`
- `six`
- `smmap`
- `sniffio`
- `streamlit`
- `streamlit-authenticator`
- `streamlit-mermaid`
- `tenacity`
- `tiktoken`
- `toml`
- `toolz`
- `toon_format`
- `tornado`
- `tqdm`
- `typing-inspection`
- `typing_extensions`
- `tzdata`
- `urllib3`
- `watchdog`
- `xxhash`
- `zstandard`

### Setup Guide
1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd repo-onboarding-agent
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure environment variables:**
    - Copy the example environment file: `cp .env.example .env`
    - Open the `.env` file and add your API keys (e.g., for Google Gemini, OpenAI) and any other required configuration, such as the MongoDB connection string.
4.  **Run the application:**
    ```bash
    streamlit run frontend/Frontend.py
    ```

### Quick Startup
To quickly get the application running after cloning and installing dependencies, execute the following command:
```bash
streamlit run frontend/Frontend.py
```
The application will open in your default web browser.

## 3. Use Cases & Commands
The primary use case for this application is to automatically generate technical documentation for a software project hosted in a Git repository.

**Workflow:**
1.  Launch the Streamlit web interface.
2.  Register a new user or log in with existing credentials.
3.  Configure API keys for the desired LLMs (e.g., Gemini, OpenAI) and the base URL for local models (Ollama) in the settings panel.
4.  In the main chat interface, enter the URL of the public Git repository you wish to document.
5.  The agent will clone the repository, perform a comprehensive static analysis, and use its LLM pipeline to generate a detailed Markdown report.
6.  The final report will be displayed in the chat interface.

**Primary Command:**
The application is launched using the Streamlit CLI.
```bash
streamlit run frontend/Frontend.py
```

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis
---
### File: `backend/AST_Schema.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** The `path_to_module` function converts a file path into a Python module path. It takes two parameters: `filepath` and `project_root`. The function attempts to calculate the relative path of the file with respect to the project root. If this fails, it falls back to using the file's basename. The function then removes any '.py' extension from the path and replaces directory separators with dots to form the module path. Finally, it checks if the module path ends with '__init__' and removes this suffix if present.
*   **Parameters:**
    - **filepath** (`str`): The path to the file to be converted into a module path.
    - **project_root** (`str`): The root directory of the project.
*   **Returns:**
    - **module_path** (`str`): The converted module path.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by the `__init__` method in the `AST_Schema.py` file at line 31.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is a subclass of ast.NodeVisitor, designed to traverse an Abstract Syntax Tree (AST) and extract relevant information about the code structure. It initializes with source code, file path, and project root, and maintains a schema to store imports, functions, and classes. The class provides methods to visit different types of nodes in the AST, including imports, class definitions, function definitions, and asynchronous function definitions. The primary purpose of this class is to analyze the code structure and populate the schema with the extracted information.
*   **Instantiation:** The class is instantiated by the analyze_repository function in the AST_Schema.py file at line 182.
*   **Dependencies:** The class has no external dependencies.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the ASTVisitor instance with source code, file path, and project root. It sets up the schema to store imports, functions, and classes, and calculates the module path.
    *   *Parameters:*
        - **source_code** (`str`): The source code of the module being analyzed.
        - **file_path** (`str`): The file path of the module being analyzed.
        - **project_root** (`str`): The project root directory.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* The visit_Import method is called when an import statement is encountered in the AST. It extracts the imported names and adds them to the schema.
        *   *Parameters:*
            - **node** (`ast.Import`): The import node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversing the AST.
            *   **Called By:** This method is called by the ast.NodeVisitor when an import statement is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* The visit_ImportFrom method is called when an import from statement is encountered in the AST. It extracts the imported names and adds them to the schema.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The import from node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversing the AST.
            *   **Called By:** This method is called by the ast.NodeVisitor when an import from statement is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* The visit_ClassDef method is called when a class definition is encountered in the AST. It extracts the class information and adds it to the schema.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The class definition node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversing the AST.
            *   **Called By:** This method is called by the ast.NodeVisitor when a class definition is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* The visit_FunctionDef method is called when a function definition is encountered in the AST. It extracts the function information and adds it to the schema.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The function definition node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversing the AST.
            *   **Called By:** This method is called by the ast.NodeVisitor when a function definition is encountered.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* The visit_AsyncFunctionDef method is called when an asynchronous function definition is encountered in the AST. It delegates the visitation to the visit_FunctionDef method.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The asynchronous function definition node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the visit_FunctionDef method to handle the asynchronous function definition.
            *   **Called By:** This method is called by the ast.NodeVisitor when an asynchronous function definition is encountered.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to analyze and process Abstract Syntax Trees (ASTs) of Python files within a repository. It provides methods to enrich schema data with call graph information, merge relationship data, and analyze a repository. The class is instantiated in the main.py file, specifically in the main_workflow function, and is used to process AST data for various files.
*   **Instantiation:** The class is instantiated in the main.py file, specifically in the main_workflow function.
*   **Dependencies:** The class does not have any external dependencies.
*   **Constructor:**
    *   *Description:* The __init__ method is the constructor of the ASTAnalyzer class. It does not take any parameters and does not perform any initialization.
    *   *Parameters:* This method takes no parameters.
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* The _enrich_schema_with_callgraph method enriches the provided schema with call graph information. It iterates over the functions and classes in the schema, and for each one, it checks if the function or method is present in the call graph. If it is, it updates the function or method's context with the call graph information.
        *   *Parameters:*
            - **schema** (`dict`): The schema to be enriched with call graph information.
            - **call_graph** (`nx.DiGraph`): The call graph to be used for enrichment.
            - **filename** (`str`): The filename associated with the schema.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the analyze_repository method.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
        *   *Description:* The merge_relationship_data method merges relationship data into the provided full schema. It iterates over the files in the schema, and for each file, it checks if there are any relationship data to be merged. If there are, it updates the file's AST nodes with the relationship data.
        *   *Parameters:*
            - **full_schema** (`dict`): The full schema to be updated with relationship data.
            - **relationship_data** (`list`): The relationship data to be merged into the schema.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema with merged relationship data.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the main_workflow function in the main.py file.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files, repo)`
        *   *Description:* The analyze_repository method analyzes a repository by processing the ASTs of its Python files. It iterates over the files, parses their ASTs, and enriches the schema with call graph information. The method returns the full schema with the analyzed data.
        *   *Parameters:*
            - **files** (`list`): The list of files to be analyzed.
            - **repo** (`GitRepository`): The repository to be analyzed.
        *   *Returns:*
            - **full_schema** (`dict`): The full schema with the analyzed data.
        *   **Usage:**
            *   **Calls:** This method calls the _enrich_schema_with_callgraph method.
            *   **Called By:** This method is called by the main_workflow function in the main.py file.

---
### File: `backend/File_Dependency.py`
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** The `build_file_dependency_graph` function constructs a directed graph representing the file dependencies within a given file. It utilizes the `networkx` library to create the graph and the `ast` module to parse the file's abstract syntax tree. The function takes in a filename, an abstract syntax tree (AST), and the repository root as parameters. It returns a `networkx.DiGraph` object representing the file dependencies. The function leverages a custom `FileDependencyGraph` visitor to traverse the AST and extract import dependencies, which are then added to the graph. This function is a crucial component in analyzing the dependencies between files within a repository.
*   **Parameters:**
    - **filename** (`str`): The name of the file for which the dependency graph is being constructed.
    - **tree** (`AST`): The abstract syntax tree of the file, which is used to extract import dependencies.
    - **repo_root** (`str`): The root directory of the repository, which is used to resolve file paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph representing the file dependencies within the given file.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by `build_repository_graph` in `File_Dependency.py` at line 177, indicating its role in constructing a broader repository graph.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** The `build_repository_graph` function constructs a directed graph representing the dependencies between Python files in a given Git repository. It iterates over all Python files in the repository, parsing each file's abstract syntax tree (AST) to identify import relationships. These relationships are then added to a global graph, which is returned as a NetworkX DiGraph object. The function utilizes the `parse` function to analyze the AST of each file and the `build_file_dependency_graph` function to construct the dependency graph for each file. The resulting graph provides a visual representation of the dependencies between files in the repository.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository to analyze for file dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the dependencies between Python files in the repository.
*   **Usage:**
    *   **Calls:** This function does not explicitly call any other functions within the provided context.
    *   **Called By:** This function is called by the `backend.File_Dependency` module in the `File_Dependency.py` file at line 233.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** The `get_all_temp_files` function retrieves a list of all Python files within a specified directory and its subdirectories. It utilizes the `pathlib` library to resolve the directory path and then uses a list comprehension to find all files with the `.py` extension. The function returns a list of `Path` objects representing the relative paths of the found files. The purpose of this function appears to be related to file dependency analysis, given its name and the presence of various import statements related to abstract syntax trees (AST) and graph libraries. However, the specific use case is not explicitly defined within the provided code snippet.
*   **Parameters:**
    - **directory** (`str`): The path to the directory in which to search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `Path` objects representing the relative paths of all Python files found within the specified directory and its subdirectories.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls based on the provided source code.
    *   **Called By:** This function is called by the `_resolve_module_name` method in the `File_Dependency.py` file, specifically on line 43, suggesting its role in resolving module dependencies.

#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G)`
*   **Description:** The function nx_to_mermaid_with_folders takes a directed graph G as input and converts it into a Mermaid graph representation. It first maps nodes to their respective folders, then creates subgraphs for each folder and adds nodes to these subgraphs. Finally, it adds edges between nodes based on the original graph's edges. The function returns the Mermaid graph as a string.
*   **Parameters:**
    - **G** (`nx.DiGraph`): A directed graph representing file dependencies
*   **Returns:**
    - **Mermaid graph** (`str`): A string representing the Mermaid graph
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze and resolve file dependencies within a repository. It utilizes the NodeVisitor class from the ast module to traverse the abstract syntax tree of Python files and identify import statements. The class provides methods to resolve relative imports and track dependencies between files.
*   **Instantiation:** The class is instantiated by the build_file_dependency_graph function in the File_Dependency.py file.
*   **Dependencies:** The class has no external dependencies.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the FileDependencyGraph object with a filename and a repository root. It sets the filename and repo_root attributes of the object.
    *   *Parameters:*
        - **filename** (`str`): The name of the file to analyze.
        - **repo_root** (`str`): The root directory of the repository.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* The _resolve_module_name method resolves relative imports of the form `from .. import name1, name2`. It returns a list of existing module or symbol names. If no resolution is possible, it raises an ImportError.
        *   *Parameters:*
            - **node** (`ImportFrom`): The import node to resolve.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:**
            *   **Calls:** This method is called by the visit_ImportFrom method to resolve relative imports.
            *   **Called By:** This method is called by the visit_ImportFrom method.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* The visit_Import method visits an import node and adds the imported module to the import dependencies of the current file.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The import node to visit.
            - **base_name** (`str | None`): The base name of the imported module.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversing the abstract syntax tree.
            *   **Called By:** This method is called by the visit_ImportFrom method.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* The visit_ImportFrom method visits an import from node and resolves the relative import. If the import is relative, it calls the _resolve_module_name method to resolve the import.
        *   *Parameters:*
            - **node** (`ImportFrom`): The import from node to visit.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the _resolve_module_name method to resolve relative imports and the generic_visit method to continue traversing the abstract syntax tree.
            *   **Called By:** This method is not explicitly called by any other method.

---
### File: `backend/HelperLLM.py`
#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** The main_orchestrator function appears to be a test harness for the LLMHelper class, which is used to generate documentation for functions and classes. It defines several example inputs for function analysis, creates FunctionAnalysis objects for these inputs, and then uses the LLMHelper class to generate documentation for these functions. The function also defines a ClassAnalysisInput object for the InventoryManager class and uses the LLMHelper class to generate documentation for this class.
*   **Parameters:** This function takes no parameters.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** No internal function calls are made within this code.
    *   **Called By:** This function is called by the backend.HelperLLM module at line 421.

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class is designed to interact with Google Gemini for generating code snippet documentation. It centralizes API interaction, error handling, and validates I/O using Pydantic. The class is initialized with an API key, function prompt path, class prompt path, and model name. It provides methods to generate and validate documentation for batches of functions and classes.
*   **Instantiation:** This class is instantiated by the main_orchestrator function in HelperLLM.py and the main_workflow function in main.py.
*   **Dependencies:** This class has no external dependencies.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper object with the provided API key, function prompt path, class prompt path, and model name. It sets up the batch size based on the model name and configures the LLM objects for function and class analysis.
    *   *Parameters:*
        - **api_key** (`str`): The API key for Google Gemini.
        - **function_prompt_path** (`str`): The path to the function prompt file.
        - **class_prompt_path** (`str`): The path to the class prompt file.
        - **model_name** (`str`): The name of the model to use (default is 'gemini-2.0-flash-lite').
        - **ollama_base_url** (`str`): The base URL for Ollama (default is None).
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This method configures the batch size based on the model name. It sets the batch size to a specific value depending on the model name.
        *   *Parameters:*
            - **model_name** (`str`): The name of the model to use.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method is called by the constructor to configure the batch size.
            *   **Called By:** The constructor calls this method to configure the batch size.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates and validates documentation for a batch of functions. It takes a list of FunctionAnalysisInput objects as input and returns a list of FunctionAnalysis objects.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of FunctionAnalysisInput objects.
        *   *Returns:*
            - **FunctionAnalysis** (`List[Optional[FunctionAnalysis]]`): A list of FunctionAnalysis objects.
        *   **Usage:**
            *   **Calls:** This method calls the LLM API to generate documentation for the functions.
            *   **Called By:** The main_workflow function in main.py calls this method to generate documentation for functions.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method generates and validates documentation for a batch of classes. It takes a list of ClassAnalysisInput objects as input and returns a list of ClassAnalysis objects.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of ClassAnalysisInput objects.
        *   *Returns:*
            - **ClassAnalysis** (`List[Optional[ClassAnalysis]]`): A list of ClassAnalysis objects.
        *   **Usage:**
            *   **Calls:** This method calls the LLM API to generate documentation for the classes.
            *   **Called By:** The main_workflow function in main.py calls this method to generate documentation for classes.

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class is designed to interact with a Large Language Model (LLM). It provides methods to call the LLM with user input and stream the response. The class is initialized with an API key, a prompt file path, and a model name. It supports different LLM models, including Gemini and Ollama.
*   **Instantiation:** The class is instantiated by the main_workflow function in main.py at line 396.
*   **Dependencies:** The class has no external dependencies.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the MainLLM class with the provided API key, prompt file path, and model name. It checks if the API key is set and raises a ValueError if it is not. It also reads the system prompt from the prompt file path and initializes the LLM model based on the model name.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the LLM model.
        - **prompt_file_path** (`str`): The path to the prompt file.
        - **model_name** (`str`): The name of the LLM model. Defaults to 'gemini-2.5-pro'.
        - **ollama_base_url** (`str`): The base URL for the Ollama model. Defaults to None.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* The call_llm method calls the LLM with the provided user input and returns the response. It creates a list of messages, including the system prompt and the user input, and invokes the LLM model with these messages.
        *   *Parameters:*
            - **user_input** (`str`): The user input to be passed to the LLM.
        *   *Returns:*
            - **response** (`str`): The response from the LLM.
        *   **Usage:**
            *   **Calls:** The method calls the invoke method of the LLM model.
            *   **Called By:** The method is called by the main_workflow function in main.py at line 415.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* The stream_llm method streams the response from the LLM with the provided user input. It creates a list of messages, including the system prompt and the user input, and streams the response from the LLM model.
        *   *Parameters:*
            - **user_input** (`str`): The user input to be passed to the LLM.
        *   *Returns:*
            - **response** (`str`): The response from the LLM.
        *   **Usage:**
            *   **Calls:** The method calls the stream method of the LLM model.
            *   **Called By:** The method is not called by any other function.

---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract basic project information from common project files such as README, pyproject.toml, and requirements.txt. It initializes a structured information object and populates it by parsing the contents of these files in a prioritized manner.
*   **Instantiation:** The class is instantiated by the main_workflow function in main.py at line 152.
*   **Dependencies:** The class does not have any external dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the class with a structured information object containing placeholders for project overview and installation information. It sets up an attribute 'info' with default values for various project metadata.
    *   *Parameters:*
        - **self** (`reference`): Reference to the instance of the class.
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This method searches case-insensitively for a file that matches one of the given patterns within a list of files.
        *   *Parameters:*
            - **self** (`reference`): Reference to the instance of the class.
            - **patterns** (`List[str]`): A list of file patterns to search for.
            - **dateien** (`List[Any]`): A list of files to search within.
        *   *Returns:*
            - **file** (`Optional[Any]`): The first matching file object or None if no match is found.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other method in the provided context.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This method extracts text under a Markdown heading (##) based on given keywords.
        *   *Parameters:*
            - **self** (`reference`): Reference to the instance of the class.
            - **inhalt** (`str`): The entire Markdown text.
            - **keywords** (`List[str]`): A list of alternative keywords for the section title.
        *   *Returns:*
            - **section_text** (`Optional[str]`): The extracted text section or None if not found.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other method in the provided context.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This method parses the content of a README file and extracts relevant project information.
        *   *Parameters:*
            - **self** (`reference`): Reference to the instance of the class.
            - **inhalt** (`str`): The content of the README file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls _extrahiere_sektion_aus_markdown.
            *   **Called By:** This method is not called by any other method in the provided context.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This method parses the content of a pyproject.toml file and extracts project metadata.
        *   *Parameters:*
            - **self** (`reference`): Reference to the instance of the class.
            - **inhalt** (`str`): The content of the pyproject.toml file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other method in the provided context.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This method parses the content of a requirements.txt file and extracts dependencies.
        *   *Parameters:*
            - **self** (`reference`): Reference to the instance of the class.
            - **inhalt** (`str`): The content of the requirements.txt file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other method in the provided context.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This method orchestrates the extraction of information from a list of repository file objects.
        *   *Parameters:*
            - **self** (`reference`): Reference to the instance of the class.
            - **dateien** (`List[Any]`): A list of repository file objects.
            - **repo_url** (`str`): The URL of the repository.
        *   *Returns:*
            - **project_info** (`Dict[str, Any]`): A dictionary containing the extracted project information.
        *   **Usage:**
            *   **Calls:** This method calls _finde_datei, _parse_toml, _parse_requirements, and _parse_readme.
            *   **Called By:** This method is called by main_workflow in main.py.

---
### File: `backend/callgraph.py`
#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** The `make_safe_dot` function generates a safe representation of a directed graph and writes it to a file in DOT format. It takes a `networkx.DiGraph` object and an output file path as input. The function creates a copy of the input graph, relabels its nodes with safe names, and then writes the modified graph to the specified output file. This process ensures that the graph can be safely represented in a DOT file without any potential naming conflicts. The function utilizes the `networkx` library for graph manipulation and the `nx_pydot` module for writing the graph to a DOT file.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The input directed graph to be made safe and written to a file.
    - **out_path** (`str`): The file path where the safe graph will be written in DOT format.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not call any other functions explicitly mentioned in the provided context.
    *   **Called By:** The `make_safe_dot` function is called by the `backend.callgraph` module, specifically in the `callgraph.py` file at line 252.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo)`
*   **Description:** The `build_filtered_callgraph` function constructs a global call graph and filters it to include only self-written functions. It takes a `GitRepository` object as input, iterates over all Python files in the repository, and uses the `ast` module to parse the abstract syntax trees of these files. The function then builds a directed graph using `networkx`, where nodes represent functions and edges represent function calls. The graph is filtered to only include functions that are part of the repository's own codebase.
*   **Parameters:**
    - **repo** (`GitRepository`): A `GitRepository` object representing the repository to analyze.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the filtered call graph of the repository's own functions.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by `analyze_repository` in `AST_Schema.py` and `backend.callgraph` in `callgraph.py`.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is designed to analyze and construct a call graph from a given Python file. It utilizes the abstract syntax tree (AST) to traverse and understand the structure of the code, identifying function definitions, calls, imports, and class definitions.
*   **Instantiation:** The CallGraph class is instantiated by functions build_filtered_callgraph in the file callgraph.py at lines 207 and 214.
*   **Dependencies:** The class depends on external modules such as ast and networkx for its operations.
*   **Constructor:**
    *   *Description:* The constructor of the CallGraph class initializes the object with a filename. It sets up several instance variables to keep track of the current function, current class, local definitions, a graph to represent the call relationships, import mappings, a set of functions, and edges in the graph.
    *   *Parameters:*
        - **filename** (`str`): The name of the file to analyze.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This method recursively processes a node in the AST to extract a list of name components as a dotted string, representing a call's callee in a hierarchical manner.
        *   *Parameters:*
            - **node** (`ast.Call | ast.Name | ast.Attribute`): The node in the AST to process.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This method takes a list of callee nodes (lists of name steps) and resolves their names based on local definitions and import mappings.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list of lists, where each sublist contains name steps.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved callee names.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* Constructs a full name for a given basename and optional class name, prefixing them with the filename.
        *   *Parameters:*
            - **basename** (`str`): The base name to construct the full name from.
            - **class_name** (`str | None`): An optional class name.
        *   *Returns:*
            - **full_name** (`str`): The constructed full name.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* Determines the current caller, which could be the current function or a representation of the global scope if no function is being processed.
        *   *Parameters:* This method takes no parameters.
        *   *Returns:*
            - **caller** (`str`): The identifier of the current caller.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles Import nodes in the AST by updating the import mapping with the names and aliases of imported modules.
        *   *Parameters:*
            - **node** (`ast.Import`): The Import node to process.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Processes ImportFrom nodes by updating the import mapping based on the module and names imported.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The ImportFrom node to process.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Visits ClassDef nodes in the AST, temporarily updating the current class and then reverting it after processing.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The ClassDef node to process.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Handles FunctionDef nodes by setting up local definitions, adding the function to the graph, and updating the current function.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The FunctionDef node to process.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Processes AsyncFunctionDef nodes by delegating to visit_FunctionDef.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AsyncFunctionDef node to process.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Visits Call nodes, resolving callees and updating the edges in the call graph.
        *   *Parameters:*
            - **node** (`ast.Call`): The Call node to process.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* Handles If nodes, specifically checking for a common Python idiom related to __name__ == '__main__'.
        *   *Parameters:*
            - **node** (`ast.If`): The If node to process.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 

---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file in a Git repository. It provides lazy loading of the file content, allowing for efficient handling of large files. The class offers various methods for accessing file properties, such as its path, size, and content.
*   **Instantiation:** The RepoFile class is instantiated by the get_all_files function in the getRepo.py file at line 111.
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* The constructor initializes the RepoFile object with the file path and the commit tree from which the file originates. It sets up the object's attributes for lazy loading of the file's blob, content, and size.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* The blob property lazy-loads the Git blob object associated with the file. If the blob is not already loaded, it attempts to retrieve it from the commit tree. If the file is not found, it raises a FileNotFoundError.
        *   *Parameters:* This method takes no parameters.
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object associated with the file.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* The content property lazy-loads and returns the decoded content of the file. If the content is not already loaded, it reads the data from the blob's data stream and decodes it using UTF-8.
        *   *Parameters:* This method takes no parameters.
        *   *Returns:*
            - **content** (`str`): The decoded content of the file.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* The size property lazy-loads and returns the size of the file in bytes. If the size is not already loaded, it retrieves it from the blob's size attribute.
        *   *Parameters:* This method takes no parameters.
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* The analyze_word_count method provides an example analysis by counting the words in the file's content. It splits the content into words using whitespace as a delimiter and returns the word count.
        *   *Parameters:* This method takes no parameters.
        *   *Returns:*
            - **word_count** (`int`): The number of words in the file's content.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* The to_dict method converts the RepoFile object into a dictionary representation. It includes the file's path, name, size, and type. If include_content is True, it also includes the file's content.
        *   *Parameters:*
            - **include_content** (`bool`): Whether to include the file's content in the dictionary.
        *   *Returns:*
            - **data** (`dict`): The dictionary representation of the RepoFile object.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory and providing RepoFile objects. It handles the cloning process, including error handling, and provides methods to retrieve all files in the repository and to close the temporary directory. The class also supports a context manager interface to ensure the temporary directory is cleaned up after use.
*   **Instantiation:** The class is instantiated by the main_workflow function in the main.py file.
*   **Dependencies:** The class does not have any external dependencies.
*   **Constructor:**
    *   *Description:* The class is initialized with a repository URL, which is used to clone the repository into a temporary directory. The constructor also sets up instance attributes for the repository URL, temporary directory, and the cloned repository object.
    *   *Parameters:*
        - **repo_url** (`string`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a list of all files in the repository as RepoFile objects. It uses the cloned repository object to get the list of files and then creates RepoFile instances for each file.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other methods in the provided context.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method closes the temporary directory and its contents. It is used to clean up after the repository has been cloned and processed.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the __exit__ method when the context manager exits.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method retrieves a tree-like structure representing the files and directories in the repository. It uses the get_all_files method to get the list of files and then constructs a tree structure from the file paths.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
            - **include_content** (`boolean`): A flag indicating whether to include the file content in the tree structure.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the tree structure of the repository.
        *   **Usage:**
            *   **Calls:** This method calls the get_all_files method to retrieve the list of files.
            *   **Called By:** This method is not called by any other methods in the provided context.

---
### File: `backend/main.py`
#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** The `create_savings_chart` function generates a bar chart comparing the number of JSON and TOON tokens, displaying the savings percentage. It utilizes matplotlib for chart creation and saves the chart to a specified output path. The function takes four parameters: `json_tokens`, `toon_tokens`, `savings_percent`, and `output_path`. It calculates the chart's title, labels, and values based on the input parameters. The chart includes a title, labels, and grid lines, with the values displayed above each bar.
*   **Parameters:**
    - **json_tokens** (`int`): The number of JSON tokens.
    - **toon_tokens** (`int`): The number of TOON tokens.
    - **savings_percent** (`float`): The percentage of savings.
    - **output_path** (`str`): The path where the chart will be saved.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not make any internal function calls.
    *   **Called By:** This function is called by the `main_workflow` function in the `main.py` file at line 450.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** The calculate_net_time function calculates the net time taken by a process, excluding sleep times due to rate limits. It takes into account the start and end times of the process, the total number of items, the batch size, and the model name. If the model name does not start with 'gemini-', the function returns the total duration. Otherwise, it calculates the number of batches, the total sleep time, and subtracts this from the total duration to get the net time.
*   **Parameters:**
    - **start_time** (`float`): The start time of the process.
    - **end_time** (`float`): The end time of the process.
    - **total_items** (`int`): The total number of items being processed.
    - **batch_size** (`int`): The size of each batch.
    - **model_name** (`str`): The name of the model being used.
*   **Returns:**
    - **net_time** (`float`): The net time taken by the process, excluding sleep times due to rate limits.
*   **Usage:**
    *   **Calls:** This function does not make any external calls.
    *   **Called By:** This function is called by the main_workflow function in main.py at lines 309 and 340.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** The main_workflow function is responsible for orchestrating the analysis of a given input. It extracts basic project information, constructs a repository file tree, analyzes relationships between functions and classes, and generates documentation using Helper LLM and Main LLM models. The function takes input, api_keys, model_names, and an optional status_callback as parameters. It returns a dictionary containing the final report and metrics.
*   **Parameters:**
    - **input** (`str`): The input to be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various services.
    - **model_names** (`dict`): A dictionary containing model names for Helper LLM and Main LLM.
    - **status_callback** (`callable`): An optional callback function to update the status of the analysis.
*   **Returns:**
    - **report** (`str`): The final report generated by the Main LLM model.
    - **metrics** (`dict`): A dictionary containing metrics such as helper time, main time, and total time.
*   **Usage:**
    *   **Calls:** The main_workflow function does not call any other functions directly.
    *   **Called By:** The main_workflow function is called by the frontend.Frontend function in Frontend.py and the backend.main function in main.py.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The update_status function is designed to update the status by calling the status_callback function if it exists and logging the provided message. It takes a single parameter, msg, which is the message to be logged and potentially passed to the status_callback function. The function does not return any value. It is used within the main_workflow function in main.py at multiple points to update the status and log messages.
*   **Parameters:**
    - **msg** (`str`): The message to be logged and potentially passed to the status_callback function.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not call any other functions explicitly within its body, but it relies on the status_callback function being defined and callable.
    *   **Called By:** The update_status function is called by the main_workflow function in main.py at multiple lines, indicating its role in updating the status and logging messages throughout the main workflow.

---
### File: `backend/relationship_analyzer.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** The `path_to_module` function converts a file path into a Python module path. It takes two parameters: `filepath` and `project_root`. The function attempts to calculate the relative path of the file with respect to the project root. If this fails, it falls back to using the file's basename. The function then removes any '.py' extension from the path, replaces path separators with dots, and removes any '__init__' suffix before returning the resulting module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the file.
    - **project_root** (`str`): The root directory of the project.
*   **Returns:**
    - **module_path** (`str`): The Python module path equivalent to the input file path.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by the `_collect_definitions` method and the `__init__` method in the `relationship_analyzer.py` file.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a project by traversing its directory structure, identifying Python files, and resolving function and method calls within those files. It constructs a call graph and provides detailed information about the definitions and their callers.
*   **Instantiation:** The ProjectAnalyzer class is instantiated by the main_workflow function in main.py at line 169.
*   **Dependencies:** The class does not have any external dependencies listed.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer with a project root path. It sets up instance attributes such as the project root, definitions, call graph, file ASTs, and directories to ignore.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the analysis of the project. It finds all Python files, collects definitions, resolves calls, and returns formatted results.
        *   *Parameters:* This method takes no parameters.
        *   *Returns:*
            - **results** (`list`): A list of dictionaries containing information about definitions and their callers.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** The analyze method is called by the main_workflow function in main.py at line 170.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This method finds all Python files within the project directory structure, excluding ignored directories.
        *   *Parameters:* This method takes no parameters.
        *   *Returns:*
            - **py_files** (`list`): A list of paths to Python files in the project.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This method collects function, method, and class definitions from a given Python file and stores them in the definitions dictionary.
        *   *Parameters:*
            - **filepath** (`str`): The path to the Python file to analyze.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This method finds the parent node of a given node in the AST.
        *   *Parameters:*
            - **tree** (`ast.Tree`): The abstract syntax tree to search.
            - **node** (`ast.Node`): The node whose parent to find.
        *   *Returns:*
            - **parent** (`ast.Node`): The parent node of the given node, or None if not found.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This method resolves function and method calls within a given Python file and updates the call graph.
        *   *Parameters:*
            - **filepath** (`str`): The path to the Python file to analyze.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* This method formats and returns the analysis results, including definitions and their callers.
        *   *Parameters:* This method takes no parameters.
        *   *Returns:*
            - **results** (`list`): A list of dictionaries containing formatted information about definitions and their callers.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is designed to traverse an Abstract Syntax Tree (AST) of Python code and resolve function calls, tracking the call relationships between different parts of the codebase. It initializes with a filepath, project root, and definitions, and uses this information to analyze the AST nodes it visits. The class provides detailed information about where functions are called from and what they are called by.
*   **Instantiation:** The class is instantiated by the _resolve_calls method in relationship_analyzer.py at line 92.
*   **Dependencies:** The class depends on external modules such as ast, os, and collections.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallResolverVisitor with a filepath, project root, and definitions. It sets up the module path, scope, instance types, and other attributes necessary for analyzing the AST.
    *   *Parameters:*
        - **filepath** (`str`): The file path of the code being analyzed.
        - **project_root** (`str`): The root directory of the project.
        - **definitions** (`dict`): A dictionary of definitions used for resolving calls.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method visits a class definition node in the AST. It temporarily updates the current class name, performs a generic visit of the node, and then reverts the current class name.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The class definition node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method visits a function definition node in the AST. It temporarily updates the current caller name, performs a generic visit of the node, and then reverts the current caller name.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The function definition node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method visits a call node in the AST. It resolves the callee's pathname, determines the caller type (module, method, or function), and records the call information.
        *   *Parameters:*
            - **node** (`ast.Call`): The call node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method visits an import node in the AST. It updates the scope with the imported names.
        *   *Parameters:*
            - **node** (`ast.Import`): The import node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method visits an import from node in the AST. It updates the scope with the imported names, handling both absolute and relative imports.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The import from node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method visits an assignment node in the AST. It checks if the assignment involves a call to a class constructor and updates the instance types accordingly.
        *   *Parameters:*
            - **node** (`ast.Assign`): The assignment node being visited.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This method resolves the qualified name of a call node. It handles different types of function nodes, including names and attributes.
        *   *Parameters:*
            - **func_node** (`ast.Node`): The function node being resolved.
        *   *Returns:*
            - **callee_pathname** (`str`): The resolved pathname of the callee.
        *   **Usage:**
            *   **Calls:** 
            *   **Called By:** 

---
### File: `backend/scads_key_test.py`
*Analysis data not available for this component.*
---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** The `encrypt_text` function is designed to encrypt a given text using a cipher suite. It first checks if the input text is empty or if the cipher suite is not available. If either condition is true, it returns the original text. Otherwise, it encrypts the text using the cipher suite, strips any leading or trailing whitespace, encodes the text to bytes, and then decodes the encrypted bytes back to a string. The function returns the encrypted text as a string.
*   **Parameters:**
    - **text** (`str`): The text to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted text.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is called by the `update_gemini_key` function in the `db.py` file at line 71.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** The `decrypt_text` function is designed to decrypt a given text using a cipher suite. It first checks if the input text is empty or if the cipher suite is not available. If either condition is true, it returns the original text. Otherwise, it attempts to decrypt the text using the cipher suite and returns the decrypted text. If an exception occurs during decryption, it catches the exception and returns the original text.
*   **Parameters:**
    - **text** (`str`): The text to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted text if decryption is successful, otherwise the original text.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by `get_decrypted_api_keys` in `db.py` at line 93.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** The `insert_user` function creates a new user document in the database. It takes in three parameters: `username`, `name`, and `password`. The function hashes the provided password using `stauth.Hasher.hash` and constructs a user dictionary with the provided information. It then inserts this user document into the database using `dbusers.insert_one` and returns the inserted ID. The function appears to be part of a user management system, likely used in conjunction with a frontend application. The user document also includes empty fields for a Gemini API key and an Ollama base URL, suggesting potential future integration with these services.
*   **Parameters:**
    - **username** (`str`): The unique username chosen by the user.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The password chosen by the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`ObjectId`): The ID of the newly inserted user document in the database.
*   **Usage:**
    *   **Calls:** This function does not appear to call any other functions directly.
    *   **Called By:** This function is called by the `frontend.Frontend` function in the `Frontend.py` file, specifically on line 294, suggesting it is used to create new user accounts within the application.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** The `fetch_all_users` function retrieves all user documents from a MongoDB database. It utilizes the `pymongo` library to interact with the database. The function returns a list of all user documents found in the database. The implementation is straightforward, relying on the `find` method of the `dbusers` collection to fetch all documents. This function does not perform any data validation or filtering on the retrieved documents. It is called by the `frontend.Frontend` function in the `Frontend.py` file.
*   **Parameters:** This function takes no parameters.
*   **Returns:**
    - **users** (`list`): A list of all user documents retrieved from the database.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is used by the `frontend.Frontend` function in the `Frontend.py` file, specifically on line 244.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** The `fetch_user` function retrieves a user document from a MongoDB database based on the provided `username`. It uses the `find_one` method of the `dbusers` collection to query for a document where the `_id` field matches the `username`. The function returns the found document, or `None` if no matching document exists. This function appears to be part of a larger system that utilizes MongoDB for user data storage. The function's implementation is straightforward, relying on the `pymongo` library for database interactions.
*   **Parameters:**
    - **username** (`str`): The username of the user to fetch from the database.
*   **Returns:**
    - **user_document** (`dict or None`): The user document retrieved from the database, or `None` if no matching document exists.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions in the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username, new_name)`
*   **Description:** The `update_user_name` function updates the name of a user in the database. It takes two parameters: `username` and `new_name`, both of which are strings. The function uses the `update_one` method of the `dbusers` collection to update the `name` field of the user document with the matching `_id` (which is the `username`). The function returns the number of documents modified by the update operation.
*   **Parameters:**
    - **username** (`str`): The username of the user to be updated.
    - **new_name** (`str`): The new name to be assigned to the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** The `update_gemini_key` function updates a user's Gemini API key in the database. It takes two parameters: `username` and `gemini_api_key`. The function first encrypts the provided API key using the `encrypt_text` function, then updates the corresponding user document in the database with the encrypted key. The function returns the number of documents modified by the update operation.
*   **Parameters:**
    - **username** (`str`): The username of the user whose Gemini API key is to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be updated for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation.
*   **Usage:**
    *   **Calls:** This function does not call any other functions explicitly mentioned in the provided context.
    *   **Called By:** This function is called by the `save_gemini_cb` function in `Frontend.py` at line 35 and is also referenced in the `frontend.Frontend` module in `Frontend.py` at line 393.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** The `update_ollama_url` function updates the `ollama_base_url` field in the database for a given `username`. It uses the `dbusers.update_one` method to perform the update and returns the number of documents modified. The function takes two parameters: `username` and `ollama_base_url`, both of which are strings. The `ollama_base_url` is stripped of any leading or trailing whitespace before being updated in the database. This function appears to be part of a larger system that manages user data and ollama base URLs.
*   **Parameters:**
    - **username** (`str`): The username of the user whose ollama base URL is being updated.
    - **ollama_base_url** (`str`): The new ollama base URL to be updated for the given username.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is called by `save_ollama_cb` and `frontend.Frontend` in the `Frontend.py` file.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** The `fetch_gemini_key` function retrieves a Gemini API key associated with a given username from a MongoDB database. It uses the `pymongo` library to connect to the database and query for the user document. If the user is found, it returns the Gemini API key; otherwise, it returns `None`. The function takes a single parameter, `username`, which is expected to be a string. The function does not handle any exceptions that may occur during database operations.
*   **Parameters:**
    - **username** (`str`): The username to retrieve the Gemini API key for.
*   **Returns:**
    - **gemini_api_key** (`str or None`): The Gemini API key associated with the given username, or `None` if the user is not found.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** The `fetch_ollama_url` function retrieves the Ollama base URL associated with a given username from a MongoDB database. It uses the `dbusers` collection and queries for a document with the specified username. If a matching document is found, the function returns the `ollama_base_url` value; otherwise, it returns `None`. This function appears to be part of a larger system that manages user data and authentication. The function's implementation is straightforward, relying on the `find_one` method of the `dbusers` collection to retrieve the relevant data.
*   **Parameters:**
    - **username** (`str`): The username for which to retrieve the Ollama base URL.
*   **Returns:**
    - **ollama_base_url** (`str or None`): The Ollama base URL associated with the given username, or `None` if no matching document is found.
*   **Usage:**
    *   **Calls:** This function does not appear to call any other functions.
    *   **Called By:** This function does not appear to be called by any other functions.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** The `delete_user` function deletes a user from the database based on their username. It utilizes the `dbusers.delete_one` method to remove the user document from the collection. The function returns the number of documents deleted, which should be 1 if the user exists and 0 if the user does not exist. This function appears to be part of a larger database management system, likely using MongoDB as the database. The function's implementation is straightforward, relying on the `delete_one` method to handle the deletion logic.
*   **Parameters:**
    - **username** (`str`): The username of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted from the database, which should be 1 if the user exists and 0 if the user does not exist.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** The `get_decrypted_api_keys` function retrieves a user's decrypted API keys from the database. It takes a `username` as input and uses it to query the `dbusers` collection. If a user with the provided username is found, the function decrypts the `gemini_api_key` and returns it along with the `ollama_base_url`. If no user is found, the function returns `None` for both values. The function relies on the `decrypt_text` function to handle the decryption process.
*   **Parameters:**
    - **username** (`str`): The username of the user whose API keys are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str`): The decrypted Gemini API key.
    - **ollama_plain** (`str`): The Ollama base URL.
*   **Usage:**
    *   **Calls:** This function does not make any explicit calls to other functions within the provided source code.
    *   **Called By:** This function is called by the `frontend.Frontend` function in the `Frontend.py` file, specifically on lines 380 and 479.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username, chat_name)`
*   **Description:** The `insert_chat` function creates a new chat entry in the database. It takes two parameters, `username` and `chat_name`, and generates a unique identifier for the chat using `uuid.uuid4()`. The function then constructs a dictionary representing the chat, including the username, chat name, and creation timestamp. This dictionary is inserted into the database using `dbchats.insert_one()`, and the function returns the inserted ID of the new chat entry.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat.
    - **chat_name** (`str`): The name of the chat.
*   **Returns:**
    - **inserted_id** (`ObjectId`): The ID of the newly inserted chat entry in the database.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by `load_data_from_db`, `handle_delete_chat`, and `frontend.Frontend` in the `Frontend.py` file.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username)`
*   **Description:** The `fetch_chats_by_user` function retrieves all defined chats for a given user. It takes a `username` as input, queries the database using the `dbchats.find` method, and returns a list of chats sorted by creation time in ascending order. The function appears to be part of a larger system that utilizes a MongoDB database, as indicated by the use of `pymongo`. The sorting of chats by creation time suggests that the function is intended to provide a chronological view of a user's chat history. The function does not perform any error handling or validation on the input `username`. The return value is a list of chats, which can be used for further processing or display.
*   **Parameters:**
    - **username** (`str`): The username of the user for whom to retrieve chats.
*   **Returns:**
    - **chats** (`list`): A list of chats associated with the given username, sorted by creation time in ascending order.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is called by the `load_data_from_db` function in the `Frontend.py` file on line 57.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username, chat_name)`
*   **Description:** The `check_chat_exists` function checks if a chat exists in the database for a given username and chat name. It uses the `dbchats` collection to find a document that matches the provided username and chat name. If such a document exists, the function returns `True`; otherwise, it returns `False`. The function takes two parameters: `username` and `chat_name`, both of which are strings. This function appears to be part of a larger system that utilizes a MongoDB database for storing chat data.
*   **Parameters:**
    - **username** (`str`): The username of the user whose chat is being checked.
    - **chat_name** (`str`): The name of the chat being checked.
*   **Returns:**
    - **existence** (`bool`): A boolean indicating whether the chat exists for the given username and chat name.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
*   **Description:** The `rename_chat_fully` function renames a chat and all associated exchanges in the database. It takes three parameters: `username`, `old_name`, and `new_name`. The function first updates the chat entry with the new name, and then updates all messages (exchanges) associated with the chat. The function returns the number of modified documents.
*   **Parameters:**
    - **username** (`str`): The username of the user who owns the chat.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is called by the `frontend.Frontend` function in the `Frontend.py` file at line 462.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time)`
*   **Description:** The `insert_exchange` function is designed to insert a new exchange record into a database. It takes in several parameters, including the question, answer, feedback, username, chat name, and various usage metrics. The function generates a unique identifier for the new record, constructs a dictionary representing the exchange, and attempts to insert this dictionary into the database. If successful, it returns the new identifier; otherwise, it catches any exceptions, prints an error message, and returns `None`. The function relies on the `uuid` library for generating unique identifiers and the `datetime` library for timestamping the creation of the record.
*   **Parameters:**
    - **question** (`str`): The question being asked in the exchange.
    - **answer** (`str`): The answer provided in the exchange.
    - **feedback** (`str`): Feedback related to the exchange.
    - **username** (`str`): The username of the user involved in the exchange.
    - **chat_name** (`str`): The name of the chat where the exchange occurred.
    - **helper_used** (`str`): Optional parameter indicating if a helper was used, defaults to an empty string.
    - **main_used** (`str`): Optional parameter indicating if the main system was used, defaults to an empty string.
    - **total_time** (`str`): Optional parameter for the total time taken for the exchange, defaults to an empty string.
    - **helper_time** (`str`): Optional parameter for the time taken by the helper, defaults to an empty string.
    - **main_time** (`str`): Optional parameter for the time taken by the main system, defaults to an empty string.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly inserted exchange record, or `None` if the insertion fails.
*   **Usage:**
    *   **Calls:** This function does not explicitly call any other functions within its body.
    *   **Called By:** The `insert_exchange` function is called by the `frontend.Frontend` function in the `Frontend.py` file at line 530.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** The `fetch_exchanges_by_user` function retrieves a list of exchanges associated with a given username from the database. It uses the `dbexchanges` collection and filters the results by the `username` field. The function sorts the exchanges in ascending order based on their `created_at` timestamp. The sorted list of exchanges is then returned by the function. This function appears to be part of a larger system that interacts with a MongoDB database using the `pymongo` library. The function's purpose is to fetch data from the database for a specific user, which is then likely used for display or further processing.
*   **Parameters:**
    - **username** (`str`): The username of the user for whom to fetch exchanges.
*   **Returns:**
    - **exchanges** (`list`): A list of exchanges associated with the given username, sorted in ascending order by their `created_at` timestamp.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by the `load_data_from_db` function in the `Frontend.py` file on line 64.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** The `fetch_exchanges_by_chat` function retrieves a list of exchanges from the database that are associated with a specific username and chat name. It uses the `dbexchanges` collection and filters the results based on the provided `username` and `chat_name`. The results are sorted in ascending order by the `created_at` field. The function returns a list of exchanges that match the specified criteria.
*   **Parameters:**
    - **username** (`str`): The username to filter exchanges by.
    - **chat_name** (`str`): The chat name to filter exchanges by.
*   **Returns:**
    - **exchanges** (`list`): A list of exchanges that match the specified username and chat name, sorted in ascending order by creation time.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** The `update_exchange_feedback` function updates the feedback for a given exchange in the database. It takes an `exchange_id` and a `feedback` value as input, and uses the `dbexchanges.update_one` method to update the corresponding document in the database. The function returns the number of documents modified by the update operation. The purpose of this function is to allow for the modification of exchange feedback in the database, which can be useful for tracking user feedback and improving the overall quality of exchanges.
*   **Parameters:**
    - **exchange_id** (`unknown`): The ID of the exchange to update
    - **feedback** (`int`): The new feedback value for the exchange
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is called by the `handle_feedback_change` function in the `Frontend.py` file, specifically on line 98.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** The `update_exchange_feedback_message` function updates the feedback message associated with a specific exchange in the database. It takes two parameters: `exchange_id` and `feedback_message`. The function uses the `dbexchanges.update_one` method to update the feedback message in the database and returns the number of documents modified. This function appears to be part of a larger system that manages exchanges and their associated feedback messages.
*   **Parameters:**
    - **exchange_id** (`object`): The ID of the exchange to update.
    - **feedback_message** (`str`): The new feedback message to associate with the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified in the database.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is called by the `render_exchange` function in the `Frontend.py` file on line 211.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** The `delete_exchange_by_id` function deletes a document from a MongoDB database based on the provided `exchange_id`. It utilizes the `dbexchanges` collection and returns the number of documents deleted. The function is designed to handle deletion operations and provides a count of affected documents as a result.
*   **Parameters:**
    - **exchange_id** (`str`): The ID of the exchange to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted from the database.
*   **Usage:**
    *   **Calls:** This function does not make any explicit calls to other functions within the provided code snippet.
    *   **Called By:** The `delete_exchange_by_id` function is called by the `handle_delete_exchange` function in the `Frontend.py` file at line 102.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username, chat_name)`
*   **Description:** The `delete_full_chat` function deletes a specified chat and all associated exchanges from the database. It ensures consistency between the frontend and backend by removing all related data in two steps: first, it deletes all messages in the chat, and then it removes the chat itself from the chat list. The function takes two parameters, `username` and `chat_name`, and returns the number of chats deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chats deleted.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is called by `handle_delete_chat` in `Frontend.py` at line 110.

---
### File: `frontend/Frontend.py`
#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** The `save_gemini_cb` function is designed to save a Gemini key to the database. It retrieves the new key from the session state, checks if it exists, and if so, updates the Gemini key in the database for the current user. After updating, it clears the session state variable and displays a success toast message. The function appears to be part of a Streamlit application, utilizing session state and toast notifications. It does not take any parameters and does not return any values. The function's purpose is to handle the saving of a Gemini key, likely as part of a user authentication or configuration process.
*   **Parameters:** This function takes no parameters.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not call any other functions explicitly mentioned in the provided context.
    *   **Called By:** This function is not explicitly mentioned as being called by any other functions in the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** The `save_ollama_cb` function is designed to save a new Ollama URL to the database. It retrieves the new URL from the session state and checks if it is not empty. If the URL is valid, it updates the Ollama URL in the database for the current user and displays a success toast message. The function appears to be part of a Streamlit application, utilizing session state and database interactions. It does not take any parameters and does not return any values. The function's purpose is to persist user-specific data in the database.
*   **Parameters:** This function takes no parameters.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions in the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** The `load_data_from_db` function is responsible for loading chat and exchange data from the database for a given username. It checks if the data has already been loaded for the current user and, if not, fetches the defined chats and exchanges from the database. The function then populates the `st.session_state.chats` dictionary with the loaded data and sets the active chat if necessary. If no chats exist for the user, it creates a default chat. The function ensures that the data is loaded consistently and handles legacy support for exchanges that may not have a corresponding chat in the database.
*   **Parameters:**
    - **username** (`str`): The username for which to load the chat and exchange data.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by the `frontend.Frontend` module in the `Frontend.py` file at line 310.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** The `handle_feedback_change` function updates the feedback value for a given exchange in the database and then triggers a re-run of the Streamlit application. It takes two parameters, `ex` and `val`, where `ex` is expected to be a dictionary containing an exchange's data, including its `_id`, and `val` is the new feedback value. The function modifies the `ex` dictionary directly by updating its `feedback` key with the provided `val`. It then calls `db.update_exchange_feedback` to persist this change in the database, using the exchange's `_id` and the new feedback value. Finally, it invokes `st.rerun()` to refresh the application's UI, reflecting the updated feedback.
*   **Parameters:**
    - **ex** (`dict`): A dictionary containing an exchange's data, including its `_id`.
    - **val** (`str`): The new feedback value to be updated for the exchange.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not explicitly call any other functions within its body, but it is called by `render_exchange` in `Frontend.py` on lines 199 and 204, indicating its role in handling user feedback changes within the frontend application.
    *   **Called By:** The `handle_feedback_change` function is utilized within the `render_exchange` function of `Frontend.py` on lines 199 and 204, suggesting its integration in the application's feedback handling mechanism.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** The `handle_delete_exchange` function is responsible for deleting an exchange from the database and updating the session state accordingly. It takes two parameters: `chat_name` and `ex`, where `ex` is expected to be a dictionary containing an `_id` key. The function first deletes the exchange from the database using the `db.delete_exchange_by_id` method. Then, it checks if the `chat_name` exists in the session state and if the exchange is present in the list of exchanges for that chat. If both conditions are met, it removes the exchange from the list. Finally, the function triggers a rerun of the Streamlit application using `st.rerun()`.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange is being deleted.
    - **ex** (`dict`): A dictionary containing information about the exchange to be deleted, including its `_id`.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls beyond the database deletion and Streamlit rerun.
    *   **Called By:** This function is called by the `render_exchange` function in the `Frontend.py` file, specifically on lines 228 and 234.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** The `handle_delete_chat` function is responsible for handling the deletion of a chat. It takes two parameters, `username` and `chat_name`, and performs the following actions: it deletes the full chat from the database using the `db.delete_full_chat` function, cleans up the state by removing the chat from the session state, and then resets the active chat. If all chats are deleted, it creates a new empty chat and sets it as the active chat. Finally, it triggers a rerun of the Streamlit application.
*   **Parameters:**
    - **username** (`str`): The username of the user deleting the chat.
    - **chat_name** (`str`): The name of the chat being deleted.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by the `frontend.Frontend` module in the `Frontend.py` file at line 367.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** The `extract_repo_name` function takes a text input, attempts to find a URL within it, and extracts the repository name from the URL's path. It uses regular expressions to find the URL and the `urlparse` function to parse the URL. If a repository name is found, it is returned; otherwise, the function returns `None`. The function appears to be designed to handle URLs from version control systems, as it removes the '.git' extension from the repository name if present.
*   **Parameters:**
    - **text** (`str`): The input text to search for a URL.
*   **Returns:**
    - **repo_name** (`str`): The extracted repository name, or `None` if no URL or repository name is found.
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is called by the `frontend.Frontend` function in the `Frontend.py` file at line 442.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** The `stream_text_generator` function is a generator that takes a string of text as input and yields each word in the text with a space appended, pausing for 0.01 seconds between each yield. This function appears to be designed for streaming text in a frontend application, possibly for display or rendering purposes. The use of `time.sleep(0.01)` suggests that the function is intended to introduce a delay between the display of each word, potentially for visual effect. The function does not perform any error checking on the input text and assumes that it will always be a string.
*   **Parameters:**
    - **text** (`str`): The input string of text to be streamed.
*   **Returns:**
    - **word** (`str`): Each word in the input text with a space appended, yielded one at a time.
*   **Usage:**
    *   **Calls:** This function does not make any explicit function calls.
    *   **Called By:** This function is called by `render_text_with_mermaid` in `Frontend.py` at line 160, suggesting that it is used to stream text in a mermaid rendering context.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream)`
*   **Description:** The `render_text_with_mermaid` function is designed to render markdown text that may contain mermaid diagrams. It splits the input text into parts based on mermaid code blocks and then renders each part accordingly. If the `should_stream` parameter is True, it uses the `stream_text_generator` function to stream the text; otherwise, it uses the `st.markdown` function to render the text. For mermaid code blocks, it attempts to render them using the `st_mermaid` function and falls back to rendering them as code if an exception occurs.
*   **Parameters:**
    - **markdown_text** (`str`): The markdown text to be rendered, which may contain mermaid diagrams.
    - **should_stream** (`bool`): A flag indicating whether to stream the text or render it directly.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not make any explicit calls to other functions within the provided context.
    *   **Called By:** This function is called by `render_exchange` in `Frontend.py` at line 238 and by the `frontend.Frontend` module in `Frontend.py` at line 524.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** The `render_exchange` function is responsible for rendering an exchange in a chat interface. It takes two parameters: `ex` and `current_chat_name`. The function displays the question and answer in the chat, along with various buttons for feedback, commenting, downloading, and deleting the exchange. If an error occurs, it displays an error message and a button to delete the exchange.
*   **Parameters:**
    - **ex** (`dict`): A dictionary containing information about the exchange, including the question, answer, and feedback.
    - **current_chat_name** (`str`): The name of the current chat.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function does not call any other functions explicitly, but it uses various Streamlit functions to render the chat interface.
    *   **Called By:** This function is called by the `frontend.Frontend` module in the `Frontend.py` file at line 429.

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic model that represents a single parameter of a function. It encapsulates the parameter's name, type, and description, providing a structured way to document and validate function parameters. This class is designed to be instantiated with specific parameter details, allowing for easy access and manipulation of parameter information. The class's primary responsibility is to provide a clear and concise representation of a function's parameters, making it easier to understand and work with the function's interface.
*   **Instantiation:** The ParameterDescription class is not instantiated by any other classes or functions in the provided context.
*   **Dependencies:** The ParameterDescription class has no external dependencies.
*   **Constructor:**
    *   *Description:* The ParameterDescription class is initialized with three parameters: name, type, and description, which are all strings. These parameters are used to set the corresponding instance attributes, allowing for easy access to the parameter's details.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type of the parameter.
        - **description** (`str`): A description of the parameter.
*   **Methods:** This class has no methods.

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model that describes the return value of a function. It has three attributes: name, type, and description, all of which are strings. This class provides a structured way to represent the return value of a function, making it easier to understand and document the function's behavior.
*   **Instantiation:** The ReturnDescription class is not instantiated by any other classes or functions in the provided context.
*   **Dependencies:** The ReturnDescription class has no external dependencies.
*   **Constructor:**
    *   *Description:* The ReturnDescription class is initialized with three parameters: name, type, and description. These parameters are used to set the corresponding attributes of the class.
    *   *Parameters:*
        - **name** (`str`): The name of the return value.
        - **type** (`str`): The type of the return value.
        - **description** (`str`): A description of the return value.
*   **Methods:** This class has no methods.

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model that describes the calling context of a function. It has two attributes: calls and called_by, which represent the functions called by the current function and the functions that call the current function, respectively.
*   **Instantiation:** The UsageContext class is not instantiated by any other classes or functions in the provided context.
*   **Dependencies:** The UsageContext class has no external dependencies.
*   **Constructor:**
    *   *Description:* The UsageContext class is initialized with two parameters: calls and called_by. These parameters are used to set the corresponding attributes of the class.
    *   *Parameters:*
        - **calls** (`str`): A string representing the functions called by the current function.
        - **called_by** (`str`): A string representing the functions that call the current function.
*   **Methods:** This class has no methods.

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to contain the detailed analysis of a function's purpose and signature. It encapsulates key aspects of a function, including its overall description, parameters, return values, and usage context. This class serves as a foundational element in documenting and analyzing functions within a larger system.
*   **Instantiation:** The class is not explicitly instantiated by other components in the provided context.
*   **Dependencies:** The FunctionDescription class does not have external dependencies.
*   **Constructor:**
    *   *Description:* The FunctionDescription class is initialized with attributes that describe a function's purpose and signature. The constructor does not have explicit parameters, but the class attributes are set through the Pydantic model's initialization process.
    *   *Parameters:*
        - **overall** (`str`): A string describing the overall purpose of the function.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing the function's parameters.
        - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects detailing the function's return values.
        - **usage_context** (`UsageContext`): An object describing the usage context of the function.
*   **Methods:** This class has no methods.

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class represents a model for analyzing functions, encapsulating their identifier, description, and potential error messages. It inherits from pydantic's BaseModel, ensuring data validation and serialization capabilities. This class serves as a foundational component in a larger system for documenting and analyzing functions, providing a structured format for representing function metadata.
*   **Instantiation:** The class is not explicitly instantiated by any other components in the provided context.
*   **Dependencies:** The FunctionAnalysis class does not have any external dependencies.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class is initialized with an identifier, a description of type FunctionDescription, and an optional error message. The identifier uniquely represents the function being analyzed, while the description provides detailed information about the function's purpose and behavior. The error field allows for the capture of any errors encountered during analysis.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the function being analyzed.
        - **description** (`FunctionDescription`): A detailed description of the function, including its purpose, parameters, return values, and usage context.
        - **error** (`Optional[str]`): An optional string field to capture any error messages encountered during function analysis.
*   **Methods:** This class has no methods.

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is designed to provide a structured description of a class's constructor method. It encapsulates the description and parameters of the constructor, offering a clear and standardized way to document and analyze class initialization.
*   **Instantiation:** The ConstructorDescription class is not instantiated by any other classes or methods in the provided context.
*   **Dependencies:** The ConstructorDescription class has no external dependencies.
*   **Constructor:**
    *   *Description:* The ConstructorDescription class is initialized with a description and a list of parameters, which are used to describe the constructor method of a class.
    *   *Parameters:*
        - **description** (`str`): A string describing the constructor method.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each describing a parameter of the constructor method.
*   **Methods:** This class has no methods.

#### Class: `ClassContext`
*   **Summary:** The ClassContext class represents the external dependencies and primary points of instantiation for a given class. It has two main attributes: dependencies and instantiated_by, which are used to describe the class's relationships with other components. This class is likely used in a larger system to track and manage class dependencies and instantiation points.
*   **Instantiation:** This class is not instantiated by any other components.
*   **Dependencies:** This class has no external dependencies.
*   **Constructor:**
    *   *Description:* The ClassContext class is initialized with two parameters: dependencies and instantiated_by. These parameters are used to set the corresponding attributes of the class, which are then used to describe the class's external dependencies and primary points of instantiation.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the class's external dependencies.
        - **instantiated_by** (`str`): A string describing the primary points of instantiation for the class.
*   **Methods:** This class has no methods.

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is designed to hold the detailed analysis of a class's purpose, constructor, and methods. It serves as a data structure to organize and represent the findings of a class analysis. The class has attributes for the overall description, the constructor description, a list of method analyses, and the usage context. This class is crucial for documenting and understanding the behavior of other classes.
*   **Instantiation:** The ClassDescription class is not instantiated by any other classes in the provided context.
*   **Dependencies:** The ClassDescription class has no external dependencies.
*   **Constructor:**
    *   *Description:* The ClassDescription class is initialized with four parameters: overall, init_method, methods, and usage_context. The overall parameter is a string describing the class's purpose, the init_method parameter is an object of type ConstructorDescription, the methods parameter is a list of FunctionAnalysis objects, and the usage_context parameter is an object of type ClassContext.
    *   *Parameters:*
        - **overall** (`str`): A string describing the class's overall purpose.
        - **init_method** (`ConstructorDescription`): An object describing the class's constructor.
        - **methods** (`List[FunctionAnalysis]`): A list of objects analyzing the class's methods.
        - **usage_context** (`ClassContext`): An object describing the class's usage context.
*   **Methods:** This class has no methods.

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class represents the main model for the entire JSON schema for a class. It contains an identifier, a description of the class, and an optional error message. The class is designed to provide a structured representation of a class's analysis, including its methods, attributes, and usage context.
*   **Instantiation:** The ClassAnalysis class is not instantiated by any other classes or functions in the provided context.
*   **Dependencies:** The ClassAnalysis class has no external dependencies.
*   **Constructor:**
    *   *Description:* The ClassAnalysis class is initialized with an identifier, a description of the class, and an optional error message.
    *   *Parameters:*
        - **identifier** (`str`): The unique identifier of the class.
        - **description** (`ClassDescription`): The description of the class, including its methods, attributes, and usage context.
        - **error** (`Optional[str]`): An optional error message, defaults to None.
*   **Methods:** This class has no methods.

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer. It is used in 'called_by' and 'instantiated_by' lists to provide information about the caller and the call mode. The class has four attributes: file, function, mode, and line, which provide details about the call event.
*   **Instantiation:** The class is not instantiated by any other class or function in the provided context.
*   **Dependencies:** The class has no external dependencies.
*   **Constructor:**
    *   *Description:* The class is initialized with four parameters: file, function, mode, and line. These parameters are used to set the corresponding attributes of the class.
    *   *Parameters:*
        - **file** (`str`): The file where the call event occurred.
        - **function** (`str`): The name of the function that made the call.
        - **mode** (`str`): The mode of the call, e.g. 'method', 'function', 'module'.
        - **line** (`int`): The line number where the call event occurred.
*   **Methods:** This class has no methods.

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model that represents structured context for analyzing a function. It encapsulates information about the functions a given function calls and the functions that call it. This class is primarily used to provide context for function analysis and is instantiated in the main_workflow function in main.py.
*   **Instantiation:** The FunctionContextInput class is instantiated in the main_workflow function in main.py at line 217.
*   **Dependencies:** The FunctionContextInput class has no external dependencies.
*   **Constructor:**
    *   *Description:* The FunctionContextInput class is initialized with two parameters: calls and called_by. The calls parameter is a list of strings representing the functions called by the analyzed function, while the called_by parameter is a list of CallInfo objects representing the functions that call the analyzed function.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing the functions called by the analyzed function.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects representing the functions that call the analyzed function.
*   **Methods:** This class has no methods.

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic model that represents the required input to generate a FunctionAnalysis object. It encapsulates the necessary information to analyze a function, including the mode, identifier, source code, imports, and context. The class is designed to provide a structured input for function analysis, ensuring that all necessary information is provided in a consistent and reliable manner.
*   **Instantiation:** The FunctionAnalysisInput class is instantiated by the main_workflow function in main.py at line 222.
*   **Dependencies:** The FunctionAnalysisInput class has no external dependencies.
*   **Constructor:**
    *   *Description:* The FunctionAnalysisInput class is initialized with the mode, identifier, source code, imports, and context. The mode is set to 'function_analysis', indicating that this input is for function analysis. The identifier, source code, and imports are used to identify and analyze the function, while the context provides additional information about the function's dependencies and instantiation.
    *   *Parameters:*
        - **mode** (`Literal['function_analysis']`): The mode of analysis, which is set to 'function_analysis'.
        - **identifier** (`str`): The identifier of the function to be analyzed.
        - **source_code** (`str`): The source code of the function to be analyzed.
        - **imports** (`List[str]`): A list of import statements required for the function analysis.
        - **context** (`FunctionContextInput`): The context in which the function is being analyzed, including dependencies and instantiation information.
*   **Methods:** This class has no methods.

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to hold structured context information for a class's methods. It encapsulates details such as the method's identifier, the functions it calls, the functions that call it, its arguments, and an optional docstring. This class plays a crucial role in providing a standardized way to represent method context, facilitating easier analysis, documentation, and potentially, automated processing of method interactions within a larger system.
*   **Instantiation:** The MethodContextInput class is instantiated by the main_workflow function in main.py at line 245.
*   **Dependencies:** The MethodContextInput class does not have any external dependencies listed.
*   **Constructor:**
    *   *Description:* The MethodContextInput class is initialized with several parameters that define the context of a method. These include the method's identifier, calls, called_by, args, and an optional docstring. The initialization sets up the instance attributes that store this contextual information.
    *   *Parameters:*
        - **identifier** (`str`): The unique identifier of the method.
        - **calls** (`List[str]`): A list of functions or methods called by this method.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects representing functions or methods that call this method.
        - **args** (`List[str]`): A list of argument names or types associated with the method.
        - **docstring** (`Optional[str]`): An optional docstring providing additional information about the method.
*   **Methods:** This class has no methods.

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class represents a structured context for analyzing a class. It encapsulates information about the class's dependencies, where it is instantiated, and the context of its methods. This class is primarily used as a data model to organize and provide context for class analysis.
*   **Instantiation:** The ClassContextInput class is instantiated in the main_orchestrator function of HelperLLM.py at line 371 and in the main_workflow function of main.py at line 258.
*   **Dependencies:** The ClassContextInput class has no external dependencies.
*   **Constructor:**
    *   *Description:* The ClassContextInput class is initialized with three parameters: dependencies, instantiated_by, and method_context. The dependencies parameter is a list of strings representing the class's dependencies. The instantiated_by parameter is a list of CallInfo objects, which contain information about where the class is instantiated. The method_context parameter is a list of MethodContextInput objects, which provide context for the class's methods.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing the class's dependencies.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects, which contain information about where the class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, which provide context for the class's methods.
*   **Methods:** This class has no methods.

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic model that represents the required input to generate a ClassAnalysis object. It encapsulates the necessary information to perform a class analysis, including the mode, identifier, source code, imports, and context. The class is primarily used as a data structure to hold the input data for the class analysis process.
*   **Instantiation:** The ClassAnalysisInput class is instantiated by the main_orchestrator function in HelperLLM.py at line 340 and the main_workflow function in main.py at line 264.
*   **Dependencies:** The ClassAnalysisInput class has no external dependencies.
*   **Constructor:**
    *   *Description:* The ClassAnalysisInput class is initialized with the mode, identifier, source code, imports, and context. The mode is set to 'class_analysis', indicating the type of analysis to be performed. The identifier, source code, and imports are used to identify the class and its dependencies. The context provides additional information about the class, such as its dependencies and instantiation locations.
    *   *Parameters:*
        - **mode** (`Literal['class_analysis']`): The mode of analysis, which is set to 'class_analysis'.
        - **identifier** (`str`): The identifier of the class being analyzed.
        - **source_code** (`str`): The source code of the class being analyzed.
        - **imports** (`List[str]`): A list of import statements required by the class.
        - **context** (`ClassContextInput`): The context of the class, including its dependencies and instantiation locations.
*   **Methods:** This class has no methods.

---
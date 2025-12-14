# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview

-   **Description:** This project implements an AI-powered agent designed to automate the generation of comprehensive documentation for software repositories. It performs deep code analysis, extracts architectural and functional insights, and synthesizes these into structured, human-readable reports using various Large Language Models.
-   **Key Features:**
    -   Automated Git Repository Cloning and File Processing.
    -   Deep Code Analysis: Abstract Syntax Tree (AST) generation, Call Graph construction, and dependency mapping.
    -   LLM-Driven Code Documentation: Specialized Helper LLMs analyze individual functions and classes for detailed descriptions, parameters, returns, and usage contexts.
    -   Main LLM Synthesis: A central LLM synthesizes all analyzed data into a cohesive Markdown documentation report.
    -   Interactive Streamlit Frontend: Provides a user-friendly interface for inputting repository URLs, configuring LLM models, viewing generated documentation, and managing chat history.
    -   Secure Database Integration: Manages user authentication, stores API keys (encrypted), and retains chat history and generated exchanges.
-   **Tech Stack:** Python, Streamlit, LangChain, Google Generative AI (Gemini), OpenAI, Ollama, PyMongo, NetworkX, GitPython, Pydantic, AST.

*   **Repository Structure:**
    ```mermaid
    graph LR
        root --> SystemPrompts["SystemPrompts<br/>.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt"]
        root --> backend
        root --> database
        root --> frontend
        root --> notizen
        root --> result
        root --> schemas
        root --> statistics
        SystemPrompts --> SystemPromptClassHelperLLM.txt
        SystemPrompts --> SystemPromptFunctionHelperLLM.txt
        SystemPrompts --> SystemPromptHelperLLM.txt
        SystemPrompts --> SystemPromptMainLLM.txt
        SystemPrompts --> SystemPromptMainLLMToon.txt
        backend --> AST_Schema.py
        backend --> File_Dependency.py
        backend --> HelperLLM.py
        backend --> MainLLM.py
        backend --> __init__.py
        backend --> basic_info.py
        backend --> callgraph.py
        backend --> getRepo.py
        backend --> main.py
        backend --> relationship_analyzer.py
        backend --> scads_key_test.py
        database --> db.py
        frontend --> .streamlit
        frontend --> Frontend.py
        frontend --> __init__.py
        frontend --> gifs
        .streamlit --> config.toml
        gifs --> 4j.gif
        notizen --> grafiken["grafiken<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
        grafiken --> "1"
        grafiken --> "2"
        grafiken --> Flask-Repo
        grafiken --> Repo-onboarding
        "1" --> File_Dependency_Graph_Repo.dot
        "1" --> global_callgraph.png
        "1" --> global_graph.png
        "1" --> global_graph_2.png
        "1" --> repo.dot
        "2" --> FDG_repo.dot
        "2" --> fdg_graph.png
        "2" --> fdg_graph_2.png
        "2" --> filtered_callgraph_flask.png
        "2" --> filtered_callgraph_repo-agent.png
        "2" --> filtered_callgraph_repo-agent_3.png
        "2" --> filtered_repo_callgraph_flask.dot
        "2" --> filtered_repo_callgraph_repo-agent-3.dot
        "2" --> filtered_repo_callgraph_repo-agent.dot
        "2" --> global_callgraph.png
        "2" --> graph_flask.md
        "2" --> repo.dot
        Flask-Repo --> __init__.dot
        Flask-Repo --> __main__.dot
        Flask-Repo --> app.dot
        Flask-Repo --> auth.dot
        Flask-Repo --> blog.dot
        Flask-Repo --> blueprints.dot
        Flask-Repo --> cli.dot
        Flask-Repo --> conf.dot
        Flask-Repo --> config.dot
        Flask-Repo --> conftest.dot
        Flask-Repo --> ctx.dot
        Flask-Repo --> db.dot
        Flask-Repo --> debughelpers.dot
        Flask-Repo --> factory.dot
        Flask-Repo --> flask.dot
        Flask-Repo --> globals.dot
        Flask-Repo --> hello.dot
        Flask-Repo --> helpers.dot
        Flask-Repo --> importerrorapp.dot
        Flask-Repo --> logging.dot
        Flask-Repo --> make_celery.dot
        Flask-Repo --> multiapp.dot
        Flask-Repo --> provider.dot
        Flask-Repo --> scaffold.dot
        Flask-Repo --> sessions.dot
        Flask-Repo --> signals.dot
        Flask-Repo --> tag.dot
        Flask-Repo --> tasks.dot
        Flask-Repo --> templating.dot
        Flask-Repo --> test_appctx.dot
        Flask-Repo --> test_async.dot
        Flask-Repo --> test_auth.dot
        Flask-Repo --> test_basic.dot
        Flask-Repo --> test_blog.dot
        Flask-Repo --> test_blueprints.dot
        Flask-Repo --> test_cli.dot
        Flask-Repo --> test_config.dot
        Flask-Repo --> test_config.png
        Flask-Repo --> test_converters.dot
        Flask-Repo --> test_db.dot
        Flask-Repo --> test_factory.dot
        Flask-Repo --> test_helpers.dot
        Flask-Repo --> test_instance_config.dot
        Flask-Repo --> test_js_example.dot
        Flask-Repo --> test_json.dot
        Flask-Repo --> test_json_tag.dot
        Flask-Repo --> test_logging.dot
        Flask-Repo --> test_regression.dot
        Flask-Repo --> test_reqctx.dot
        Flask-Repo --> test_request.dot
        Flask-Repo --> test_session_interface.dot
        Flask-Repo --> test_signals.dot
        Flask-Repo --> test_subclassing.dot
        Flask-Repo --> test_templating.dot
        Flask-Repo --> test_testing.dot
        Flask-Repo --> test_user_error_handler.dot
        Flask-Repo --> test_views.dot
        Flask-Repo --> testing.dot
        Flask-Repo --> typing.dot
        Flask-Repo --> typing_app_decorators.dot
        Flask-Repo --> typing_error_handler.dot
        Flask-Repo --> typing_route.dot
        Flask-Repo --> views.dot
        Flask-Repo --> wrappers.dot
        Flask-Repo --> wsgi.dot
        Repo-onboarding --> AST.dot
        Repo-onboarding --> Frontend.dot
        Repo-onboarding --> HelperLLM.dot
        Repo-onboarding --> HelperLLM.png
        Repo-onboarding --> MainLLM.dot
        Repo-onboarding --> agent.dot
        Repo-onboarding --> basic_info.dot
        Repo-onboarding --> callgraph.dot
        Repo-onboarding --> getRepo.dot
        Repo-onboarding --> graph_AST.png
        Repo-onboarding --> graph_AST2.png
        Repo-onboarding --> graph_AST3.png
        Repo-onboarding --> main.dot
        Repo-onboarding --> tools.dot
        Repo-onboarding --> types.dot
        result --> ast_schema_01_12_2025_11-49-24.json
        result --> report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result --> report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result --> report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result --> report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md
        result --> report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md
        result --> report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md
        result --> report_14_11_2025_14-52-36.md
        result --> report_14_11_2025_15-21-53.md
        result --> report_14_11_2025_15-26-24.md
        result --> report_21_11_2025_15-43-30.md
        result --> report_21_11_2025_16-06-12.md
        result --> report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md
        result --> report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md
        result --> result_2025-11-11_12-30-53.md
        result --> result_2025-11-11_12-43-51.md
        result --> result_2025-11-11_12-45-37.md
        schemas --> types.py
        statistics --> savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png
        statistics --> savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png
        statistics --> savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png
        statistics --> savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png
        statistics --> savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png
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
- typing-inspect==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0

Alternatively, if `requirements.txt` is available:
`pip install -r requirements.txt`

### Setup Guide
Information not found

### Quick Startup
Information not found

## 3. Use Cases & Commands
The Repo-onboarding Agent provides a streamlined approach to understanding and documenting software repositories, leveraging AI for deeper insights.

**Primary Use Cases:**

1.  **Automated Repository Onboarding:** Quickly generate comprehensive documentation for new or unfamiliar Git repositories. This is invaluable for new team members to rapidly grasp codebase structure, key functionalities, and interdependencies without extensive manual code exploration.
2.  **Codebase Deep Dive:** Developers can analyze specific functions, classes, and modules to understand their purpose, parameters, return values, and how they interact with other components through detailed AI-generated summaries and call graphs.
3.  **LLM-Powered Documentation Generation:** Utilize various Large Language Models (Gemini, OpenAI, Ollama, etc.) to automatically describe code elements, allowing for experimentation with different models to find the best documentation quality.
4.  **Interactive Exploration and Management:** Interact with the system via a user-friendly Streamlit web interface to input repository URLs, configure LLM settings, review generated reports, and manage personal chat history and API keys.

**Primary Commands / Interaction Flow:**

The system is primarily operated through its interactive Streamlit web interface (`frontend/Frontend.py`).

1.  **Launch the Frontend:** Run the Streamlit application to access the user interface.
2.  **Input Repository URL:** Provide the GitHub (or other Git-compatible) repository URL in the designated input field.
3.  **Configure LLMs (Optional):** Select desired Helper and Main LLM models and provide necessary API keys (Gemini, OpenAI, SCADSLLM) or Ollama base URLs within the settings/profile section.
4.  **Initiate Documentation Generation:** Click the "Generate Documentation" button. The system's `main_workflow` (`backend/main.py`) orchestrates the following:
    *   Cloning the repository (`backend/getRepo.py`).
    *   Extracting basic project information (`backend/basic_info.py`).
    *   Analyzing relationships and building AST schemas (`backend/relationship_analyzer.py`, `backend/AST_Schema.py`, `backend/callgraph.py`).
    *   Sending code snippets to the Helper LLM for detailed function/class analysis (`backend/HelperLLM.py`).
    *   Synthesizing all gathered data into a final Markdown report using the Main LLM (`backend/MainLLM.py`).
5.  **Review Report:** The generated Markdown report, including code analysis and architectural insights, is displayed directly in the web interface. Users can save, provide feedback, or delete generated exchanges.

No direct command-line interface (CLI) commands are exposed for end-users, as the system prioritizes a graphical interaction model.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases where the filepath is not within the project root by falling back to the basename of the file. If the resulting path ends with '.__init__', it removes the trailing part to correctly represent the module.
*   **Parameters:**
    -   **filepath** (`str`): The absolute or relative path to a Python file.
    -   **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    -   **module_path** (`str`): A dot-separated module path derived from the given file path.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** `__init__` method in `AST_Schema.py` at line 31.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is a specialized AST (Abstract Syntax Tree) visitor that traverses Python source code to extract structural information such as imports, classes, and functions. It leverages the `ast.NodeVisitor` base class to walk through nodes in the AST and builds a schema representation of the module's structure. The class maintains contextual information about the current class being visited during traversal, enabling it to associate methods with their respective classes. It also tracks source code segments and line numbers for each element.
*   **Instantiation:** The ASTVisitor class is instantiated by the `analyze_repository` function in the file AST_Schema.py at line 182.
*   **Dependencies:** This class depends on the `ast` module for parsing and traversing Python code, and uses `path_to_module` to compute module paths.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It computes the module path based on the file path and project root, initializes an empty schema dictionary to store extracted information, and sets up a placeholder for tracking the currently visited class.
    *   *Parameters:*
        -   **source_code** (`str`): The full source code of the file being analyzed.
        -   **file_path** (`str`): The absolute or relative path to the file being analyzed.
        -   **project_root** (`str`): The root directory of the project to compute module paths.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It iterates over the aliases in the import statement and adds each alias name to the imports list before proceeding with generic visitation.
        *   *Parameters:*
            -   **node** (`ast.Import`): An AST node representing an import statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the AST traversal mechanism when an import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST by extracting the fully qualified names of imported items and appending them to the schema's imports list. It constructs a dotted string combining the module name and the imported item name before adding it to the imports list.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the AST traversal mechanism when an 'import from' node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Processes class definitions in the AST by creating a structured representation of the class including its identifier, name, docstring, source code segment, and line numbers. It appends this information to the schema's classes list and temporarily stores it as the current class for subsequent method processing. After visiting child nodes, it resets the current class reference.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the AST traversal mechanism when a class definition node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definitions in the AST. If a class is currently being visited, it associates the function with that class by creating a method context entry. Otherwise, it treats the function as a top-level function and creates a function info entry in the schema. It extracts argument names, docstrings, and source code segments for both cases.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the AST traversal mechanism when a function definition node is encountered.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating the processing to the standard `visit_FunctionDef` method. This allows async functions to be treated similarly to regular functions in terms of schema extraction.
        *   *Parameters:*
            -   **node** (`ast.AsyncFunctionDef`): An AST node representing an async function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the visit_FunctionDef method to handle the async function.
            *   **Called By:** This method is called by the AST traversal mechanism when an async function definition node is encountered.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information. It merges relationship data into the schema and supports the construction of a comprehensive view of the codebase including functions, classes, and their interdependencies. The class orchestrates the process of AST traversal, schema enrichment, and data consolidation across multiple files.
*   **Instantiation:** This class is instantiated in the evaluation.py file at line 128 and in the main.py file at line 187.
*   **Dependencies:** This class depends on external modules such as ast, networkx, os, callgraph.build_filtered_callgraph, and getRepo.GitRepository.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor does not perform any specific initialization actions.
    *   *Parameters:*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema: dict, call_graph: networkx.DiGraph, filename: str)`
        *   *Description:* This static method enriches a given schema with call graph information by updating function and method contexts with details about which functions they call and which functions call them. It processes both top-level functions and class methods within the schema, using a provided call graph to populate 'calls' and 'called_by' fields.
        *   *Parameters:*
            -   **schema** (`dict`): A dictionary representing the schema of a parsed Python file, containing functions and classes.
            -   **call_graph** (`networkx.DiGraph`): A NetworkX directed graph representing the call relationships between functions.
            -   **filename** (`str`): The path of the file being processed, used to construct unique keys for looking up functions in the call graph.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the analyze_repository method within the ASTAnalyzer class.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, relationship_data: list)`
        *   *Description:* Merges relationship data into a full schema by associating identifiers from the relationship data with corresponding entries in the schema. It updates function and class contexts with 'called_by' information and class instantiation details based on the provided relationship data.
        *   *Parameters:*
            -   **full_schema** (`dict`): The complete schema containing file data and AST nodes to be updated with relationship information.
            -   **relationship_data** (`list`): A list of dictionaries containing relationship information, including identifiers and associated 'called_by' lists.
        *   *Returns:*
            -   **full_schema** (`dict`): The updated schema with merged relationship data.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the evaluate function in evaluation.py at line 137 and by the main_workflow function in main.py at line 197.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: getRepo.GitRepository)`
        *   *Description:* Analyzes a repository by processing a list of files, parsing their content into ASTs, visiting them with an ASTVisitor to extract schema information, and enriching that schema with call graph data. It constructs a full schema representation of the repository including files, functions, and classes with their respective contexts.
        *   *Parameters:*
            -   **files** (`list`): A list of file objects containing file paths and content to be analyzed.
            -   **repo** (`getRepo.GitRepository`): An object representing the Git repository being analyzed.
        *   *Returns:*
            -   **full_schema** (`dict`): A dictionary containing the full schema of the analyzed repository, organized by file paths.
        *   **Usage:**
            *   **Calls:** This method calls the _enrich_schema_with_callgraph method and uses the build_filtered_callgraph function from the callgraph module.
            *   **Called By:** This method is called by the evaluate function in evaluation.py at line 129 and by the main_workflow function in main.py at line 188.

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: ast.AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes an AST representation of a file and uses a custom visitor to extract import dependencies. The resulting graph captures relationships between files and their imported modules.
*   **Parameters:**
    -   **filename** (`str`): The name of the file being analyzed for dependencies.
    -   **tree** (`ast.AST`): The abstract syntax tree representation of the file's source code.
    -   **repo_root** (`str`): The root directory path of the repository being analyzed.
*   **Returns:**
    -   **graph** (`networkx.DiGraph`): A NetworkX directed graph representing the file dependency relationships.
*   **Usage:**
    *   **Calls:** The function internally utilizes a FileDependencyGraph visitor to traverse the AST and collect import dependencies.
    *   **Called By:** This function is called by the 'build_repository_graph' function in the 'File_Dependency.py' file at line 177.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: getRepo.GitRepository)`
*   **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It iterates through all files in the repository, filters for Python files, parses their content into ASTs, and builds individual file dependency graphs. These are then merged into a global graph that captures the overall dependency structure. The resulting graph is returned as a NetworkX DiGraph.
*   **Parameters:**
    -   **repository** (`getRepo.GitRepository`): The GitRepository object containing the files to analyze for dependencies.
*   **Returns:**
    -   **global_graph** (`networkx.DiGraph`): A NetworkX directed graph representing the dependency relationships between Python files in the repository.
*   **Usage:**
    *   **Calls:** This function internally utilizes several AST parsing and graph-building utilities including `parse`, `build_file_dependency_graph`, and NetworkX functions like `DiGraph`, `add_node`, and `add_edge`.
    *   **Called By:** This function is called by the module-level function `backend.File_Dependency` in the file File_Dependency.py at line 200.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function retrieves all Python files (.py) from a specified directory and its subdirectories. It resolves the given directory path to an absolute path, then uses recursive globbing to find all .py files. Each found file is converted to a relative path from the root directory and returned as a list. The function assumes the input directory exists and is accessible.
*   **Parameters:**
    -   **directory** (`str`): The path to the directory from which to search for Python files.
*   **Returns:**
    -   **all_files** (`list[Path]`): A list of pathlib.Path objects representing the relative paths of all Python files found in the directory and its subdirectories.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by _resolve_module_name in File_Dependency.py at line 43.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze and resolve file-level import dependencies within a Python project. It extends NodeVisitor to traverse AST nodes representing imports and builds a dependency graph by tracking which files depend on others. The class handles both absolute and relative imports, resolving relative paths based on the repository structure and checking for module existence or symbol exports in __init__.py files.
*   **Instantiation:** This class is instantiated by the function 'build_file_dependency_graph' in the file 'File_Dependency.py' at line 156.
*   **Dependencies:** This class does not directly depend on any external modules beyond standard library imports and ast-related components.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. This sets up the core state needed for dependency resolution, including storing the file being analyzed and the root directory of the repository.
    *   *Parameters:*
        -   **filename** (`str`): The name of the file for which dependencies are being analyzed.
        -   **repo_root** (`Any`): The root directory path of the repository containing the file.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ast.ImportFrom)`
        *   *Description:* Resolves relative import statements by analyzing the import node and determining the actual module or symbol names that can be imported. It checks for module existence and symbol availability in __init__.py files, raising ImportError if resolution fails. The method uses helper functions to check file existence and symbol exports.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing a relative import statement.
        *   *Returns:*
            -   **resolved** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:**
            *   **Calls:** This method internally calls helper functions 'module_file_exists' and 'init_exports_symbol'.
            *   **Called By:** This method is called by 'visit_ImportFrom' when resolving relative imports.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import | ast.ImportFrom, base_name: str | None = None)`
        *   *Description:* Handles AST nodes representing import statements. It records the import dependencies by adding the import name to the import_dependencies dictionary associated with the current file. This method ensures that all imports are tracked for dependency analysis.
        *   *Parameters:*
            -   **node** (`Import | ImportFrom`): An AST node representing an import statement.
            -   **base_name** (`str | None`): Optional base name for the import, used primarily for handling relative imports.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls generic_visit to continue traversal of the AST.
            *   **Called By:** This method is called by the parent class's visit method during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* Processes AST nodes representing 'from ... import ...' statements. It extracts the module name and delegates to visit_Import for recording dependencies. For relative imports, it attempts to resolve the module names using _resolve_module_name, handling any ImportError gracefully by printing a message.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls _resolve_module_name for relative imports and visit_Import for dependency recording.
            *   **Called By:** This method is called by the parent class's visit method during AST traversal.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analysis for several example functions including 'add_item', 'check_stock', and 'generate_report'. It also constructs inputs for these functions and simulates the generation of documentation via an LLMHelper instance.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    *   **Calls:** No external functions are called directly by this function.
    *   **Called By:** Called by backend.HelperLLM (line 419 in HelperLLM.py)

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a centralized interface for interacting with various language models, including Google Gemini, OpenAI, custom APIs, and Ollama, to generate and validate code documentation for functions and classes. It handles API configuration, batching, and error management while leveraging Pydantic for input/output validation.
*   **Instantiation:** The LLMHelper class is instantiated by the main_orchestrator function in HelperLLM.py, the evaluation function in evaluation.py, and the main_workflow function in main.py.
*   **Dependencies:** No external dependencies are explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API credentials, prompt files, and model configurations. It reads system prompts from specified files, sets up batch size based on the model name, and configures the appropriate LLM client depending on the model type. It also prepares structured output parsers for function and class analysis.
    *   *Parameters:*
        -   **api_key** (`str`): API key for accessing the language model service.
        -   **function_prompt_path** (`str`): Path to the file containing the system prompt for function documentation generation.
        -   **class_prompt_path** (`str`): Path to the file containing the system prompt for class documentation generation.
        -   **model_name** (`str`): Name of the language model to use. Defaults to 'gemini-2.0-flash-lite'.
        -   **base_url** (`str`): Base URL for custom API endpoints. Optional.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing requests based on the specified model name. Different models have different recommended batch sizes to optimize performance and avoid rate limiting.
        *   *Parameters:*
            -   **model_name** (`str`): Name of the language model for which to configure batch settings.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method is called internally by the constructor during initialization.
            *   **Called By:** This method is called by the constructor of the LLMHelper class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: typing.List[schemas.types.FunctionAnalysisInput])`
        *   *Description:* Processes a batch of function inputs to generate validated documentation using the configured LLM. It splits inputs into batches, sends them to the LLM, and handles errors by filling failed items with None values while maintaining order. Rate limiting is respected by waiting between batches.
        *   *Parameters:*
            -   **function_inputs** (`List[FunctionAnalysisInput]`): A list of function input models to document.
        *   *Returns:*
            -   **result** (`List[Optional[FunctionAnalysis]]`): A list of validated function analysis results or None for failed items.
        *   **Usage:**
            *   **Calls:** This method does not directly call other methods within the class.
            *   **Called By:** This method is called by the evaluation function in evaluation.py and the main_workflow function in main.py.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: typing.List[schemas.types.ClassAnalysisInput])`
        *   *Description:* Processes a batch of class inputs to generate validated documentation using the configured LLM. Similar to generate_for_functions, it batches inputs, sends them to the LLM, and manages errors by filling failed items with None values while preserving order. Rate limiting is enforced with delays between batches.
        *   *Parameters:*
            -   **class_inputs** (`List[ClassAnalysisInput]`): A list of class input models to document.
        *   *Returns:*
            -   **result** (`List[Optional[ClassAnalysis]]`): A list of validated class analysis results or None for failed items.
        *   **Usage:**
            *   **Calls:** This method does not directly call other methods within the class.
            *   **Called By:** This method is called by the evaluation function in evaluation.py and the main_workflow function in main.py.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the central interface for interacting with various language learning models (LLMs), including Google Generative AI models, custom OpenAI-compatible APIs, and local Ollama models. It initializes with an API key, a prompt file path, and model specifications, then dynamically selects and configures an appropriate LLM client based on the model name. The class provides two core functionalities: synchronous invocation of the LLM via the call_llm method and streaming responses via the stream_llm method, both using a predefined system prompt and user input.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py at line 398.
*   **Dependencies:** This class depends on external libraries such as langchain_google_genai.ChatGoogleGenerativeAI, langchain_ollama.ChatOllama, langchain_openai.ChatOpenAI, and langchain.messages.HumanMessage and langchain.messages.SystemMessage.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading a system prompt from a file, and configuring an appropriate LLM client based on the specified model name. It supports multiple LLM backends including Google Generative AI, custom OpenAI-compatible endpoints, and local Ollama models.
    *   *Parameters:*
        -   **api_key** (`str`): The API key used for authenticating with the LLM service.
        -   **prompt_file_path** (`str`): The file path to the system prompt that will be loaded and used for LLM interactions.
        -   **model_name** (`str`): The name of the model to use, which determines the backend LLM client to instantiate.
        -   **base_url** (`str`): Optional base URL for connecting to a local Ollama instance or other compatible endpoint.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* Invokes the configured LLM with a user input message, prepending a system prompt to the conversation history. It handles potential exceptions during the LLM call and logs the outcome before returning the content of the response or None in case of failure.
        *   *Parameters:*
            -   **user_input** (`str`): The input text provided by the user to be processed by the LLM.
        *   *Returns:*
            -   **response_content** (`str`): The content of the LLM's response, or None if an error occurred during the call.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods within its own source code.
            *   **Called By:** Called by the main_workflow function in main.py at line 417.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* Streams the response from the configured LLM in chunks for real-time processing. It prepares the conversation history with the system prompt and user input, initiates a streaming request, and yields each chunk of content as it becomes available. In case of an exception, it logs the error and yields an error message.
        *   *Parameters:*
            -   **user_input** (`str`): The input text provided by the user to be processed by the LLM.
        *   *Returns:*
            -   **chunk_content** (`str`): Yields content chunks from the LLM's streaming response, or an error message if an exception occurs.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods within its own source code.
            *   **Called By:** This method is not called by any other function or method according to the provided context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract basic project information from common project files such as README.md, pyproject.toml, and requirements.txt. It initializes a structured dictionary to hold project overview and installation details, and provides methods to parse different file types and extract relevant sections. The class orchestrates the extraction process by prioritizing file types based on their informativeness, starting with pyproject.toml, followed by requirements.txt, and finally README files. It also handles fallback mechanisms and formatting of extracted data.
*   **Instantiation:** This class is instantiated in the evaluation function in evaluation.py at line 104 and in the main_workflow function in main.py at line 160.
*   **Dependencies:** This class does not depend on any external libraries beyond those already imported in the module.
*   **Constructor:**
    *   *Description:* Initializes the ProjektInfoExtractor with a predefined structure for storing project information. It sets up placeholders for various project details like title, description, status, features, tech stack, dependencies, setup instructions, and quick start guides. Additionally, it defines a constant for indicating missing information.
    *   *Parameters:*
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: typing.List[str], dateien: typing.List[typing.Any])`
        *   *Description:* This method searches for a file among a list of files that matches any of the given patterns, ignoring case differences. It iterates through the list of files and checks if the file path ends with one of the specified patterns. If a match is found, it returns the matching file object; otherwise, it returns None.
        *   *Parameters:*
            -   **patterns** (`List[str]`): A list of file extension patterns to search for.
            -   **dateien** (`List[Any]`): A list of file objects to search through.
        *   *Returns:*
            -   **result** (`Optional[Any]`): The first matching file object or None if no match is found.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: typing.List[str])`
        *   *Description:* This method extracts text content from a markdown document under a section header marked by '##'. It uses regular expressions to find the specified keywords and captures the text until the next '##' header or end of the document. It supports case-insensitive matching and handles multiline content.
        *   *Parameters:*
            -   **inhalt** (`str`): The full markdown text to parse.
            -   **keywords** (`List[str]`): A list of alternative keywords to look for as section headers.
        *   *Returns:*
            -   **extracted_text** (`Optional[str]`): The extracted text section or None if no match is found.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* Parses the content of a README file to extract metadata such as title, description, key features, tech stack, current status, setup instructions, and quick start guide. It uses regex patterns to identify these elements and stores them in the internal info structure. It leverages the _extrahiere_sektion_aus_markdown helper to extract sections from the markdown content.
        *   *Parameters:*
            -   **inhalt** (`str`): The content of the README file to parse.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the _extrahiere_sektion_aus_markdown helper method to extract specific sections from the markdown content.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* Parses the content of a pyproject.toml file to extract project metadata such as name, description, and dependencies. It uses the tomllib library to load the TOML content and updates the internal info structure accordingly. If tomllib is not available, it prints a warning message. It also catches TOML parsing errors and reports them.
        *   *Parameters:*
            -   **inhalt** (`str`): The content of the pyproject.toml file to parse.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* Parses the content of a requirements.txt file to extract dependency information. It filters out comments and empty lines, then stores the resulting list of dependencies in the internal info structure only if no dependencies were previously found from other sources.
        *   *Parameters:*
            -   **inhalt** (`str`): The content of the requirements.txt file to parse.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: typing.List[typing.Any], repo_url: str)`
        *   *Description:* Orchestrates the extraction of project information from a list of repository files. It identifies relevant files (README, pyproject.toml, requirements.txt) using the _finde_datei helper, processes them in order of priority (pyproject.toml, requirements.txt, README), and formats the final output. It also sets the project title based on the repository URL after processing all files.
        *   *Parameters:*
            -   **dateien** (`List[Any]`): A list of repository file objects to extract information from.
            -   **repo_url** (`str`): The URL of the repository to derive the project title from.
        *   *Returns:*
            -   **info** (`Dict[str, Any]`): A dictionary containing the extracted project information.
        *   **Usage:**
            *   **Calls:** This method calls the _finde_datei, _parse_toml, _parse_requirements, and _parse_readme helper methods to process different types of files.
            *   **Called By:** This method is called by the evaluation function in evaluation.py and the main_workflow function in main.py.

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: networkx.DiGraph, out_path: str)`
*   **Description:** The function 'make_safe_dot' takes a NetworkX directed graph and a file path as inputs, and generates a DOT file representation of the graph with sanitized node names. It creates a mapping from original node names to safe identifiers, relabels the nodes accordingly, and stores the original labels as node attributes before writing the modified graph to a specified output path.
*   **Parameters:**
    -   **graph** (`networkx.DiGraph`): A NetworkX directed graph object to be processed and written to a DOT file.
    -   **out_path** (`str`): The file path where the DOT representation of the graph will be saved.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on external libraries such as NetworkX and pydot for graph manipulation and file I/O.
    *   **Called By:** This function is called by the 'backend.callgraph' module at line 244 in the file 'callgraph.py'.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: getRepo.GitRepository)`
*   **Description:** Die Funktion erstellt einen globalen Call-Graphen basierend auf allen Python-Dateien eines Git-Repositories und filtert diesen anschließend, sodass nur Aufrufe zwischen selbst geschriebenen Funktionen erhalten bleiben. Sie durchläuft alle Dateien, parst deren Inhalt mit dem Abstract Syntax Tree (AST), extrahiert Funktionsaufrufe und baut einen gerichteten Graphen auf. Anschließend werden nur Kanten beibehalten, die sowohl vom aufrufenden als auch vom aufgerufenen Element zu den eigenen Funktionen gehören.
*   **Parameters:**
    -   **repo** (`getRepo.GitRepository`): Ein Objekt, das Zugriff auf ein Git-Repository bietet und Informationen über alle darin enthaltenen Dateien bereitstellt.
*   **Returns:**
    -   **global_graph** (`networkx.DiGraph`): Ein gerichteter Graph (DiGraph) aus dem networkx-Bibliothek, der nur die Call-Beziehungen zwischen selbst geschriebenen Funktionen enthält.
*   **Usage:**
    *   **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes direkt auf, sondern verwendet externe Klassen und Module wie 'ast', 'networkx' sowie 'CallGraph'.
    *   **Called By:** Diese Funktion wird von zwei anderen Funktionen aufgerufen: 'analyze_repository' in der Datei 'AST_Schema.py' (Zeile 167) und 'backend.callgraph' in der Datei 'callgraph.py' (Zeile 243).

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is a visitor for Python Abstract Syntax Tree (AST) nodes that builds a directed graph representing function call relationships within a Python file. It tracks local definitions, imports, and class contexts to resolve function names and construct edges between callers and callees. The class maintains internal state such as the current function and class being processed, and uses NetworkX to store the resulting call graph.
*   **Instantiation:** This class is instantiated by the build_filtered_callgraph function in the callgraph.py file at lines 199 and 206.
*   **Dependencies:** This class depends on the ast module for parsing Python code, networkx for graph representation, and various utility modules for repository and project information extraction.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph with a filename and sets up internal data structures including dictionaries for local definitions, import mappings, and a NetworkX directed graph. It also initializes tracking variables for the current function and class.
    *   *Parameters:*
        -   **filename** (`str`): The name of the file being analyzed for call graph construction.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* Recursively traverses an AST node to extract the dotted name components of a function or attribute access. It handles different node types like ast.Call, ast.Name, and ast.Attribute to build a list of name parts that represent the full path of a reference.
        *   *Parameters:*
            -   **node** (`ast.AST`): The AST node to traverse for extracting name components.
        *   *Returns:*
            -   **parts** (`list[str]`): A list of strings representing the dotted name components.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the _resolve_all_callee_names method.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: typing.List[typing.List[str]])`
        *   *Description:* Resolves a list of dotted name components into fully qualified names by checking local definitions, import mappings, and constructing appropriate paths based on the current class context. It prioritizes local definitions over imports and constructs names in a standardized format.
        *   *Parameters:*
            -   **callee_nodes** (`list[list[str]]`): A list of lists containing name components for potential callees.
        *   *Returns:*
            -   **resolved** (`list[str]`): A list of fully qualified names for the callees.
        *   **Usage:**
            *   **Calls:** This method calls the _recursive_call method to extract name components.
            *   **Called By:** This method is called by the visit_Call method.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None = None)`
        *   *Description:* Constructs a fully qualified name for a function or method by combining the filename with the base name and optionally a class name, using a double-colon separator for clarity.
        *   *Parameters:*
            -   **basename** (`str`): The base name of the function or method.
            -   **class_name** (`Optional[str]`): The optional class name to include in the fully qualified name.
        *   *Returns:*
            -   **full_name** (`str`): The fully qualified name constructed from the filename, class name, and base name.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the visit_FunctionDef method.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* Determines the current caller's name based on whether a function is currently being visited. If there is no active function, it defaults to either the filename or global scope.
        *   *Parameters:*
        *   *Returns:*
            -   **caller_name** (`str`): The name of the current caller, either the function name or a default scope identifier.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the visit_Call method.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST by mapping aliases to their actual module names and storing them in the import mapping dictionary. This allows for proper resolution of imported names later during call resolution.
        *   *Parameters:*
            -   **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversal.
            *   **Called By:** This method is called by the AST visitor framework.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements by extracting the module name and mapping aliases to their respective modules. It stores these mappings for resolving names in function calls.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversal.
            *   **Called By:** This method is called by the AST visitor framework.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* Processes class definitions in the AST by temporarily setting the current class name, visiting the class body, and then restoring the previous class name. This ensures that function definitions within classes are correctly associated with their parent class.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversal.
            *   **Called By:** This method is called by the AST visitor framework.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definitions in the AST by creating a fully qualified name for the function, adding it to local definitions, and recording it in the graph. It also manages the current function context during traversal.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the _make_full_name method to construct the function name and the generic_visit method to continue traversal.
            *   **Called By:** This method is called by the AST visitor framework.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating to the regular function definition handler. This ensures that async functions are treated similarly to regular functions in terms of call graph construction.
        *   *Parameters:*
            -   **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the visit_FunctionDef method to handle the function definition.
            *   **Called By:** This method is called by the AST visitor framework.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST by identifying the caller, extracting the callee's name components, resolving those names to fully qualified forms, and adding edges to the call graph. It also manages edge storage in a dictionary for later processing.
        *   *Parameters:*
            -   **node** (`ast.Call`): The AST node representing a function call.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the _current_caller method to determine the caller, the _recursive_call method to extract callee components, and the _resolve_all_callee_names method to resolve the names.
            *   **Called By:** This method is called by the AST visitor framework.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* Handles conditional statements in the AST, specifically looking for conditions related to '__name__ == '__main__' to treat the main block specially. It temporarily changes the current function context to '<main_block>' when such a condition is detected.
        *   *Parameters:*
            -   **node** (`ast.If`): The AST node representing an if statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversal.
            *   **Called By:** This method is called by the AST visitor framework.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It implements lazy loading for file metadata such as content and size to optimize performance by only loading data when explicitly accessed. The class provides properties for accessing the Git blob, content, and size of the file, along with utility methods for word count analysis and serialization to a dictionary format.
*   **Instantiation:** This class is instantiated by the get_all_files method located in getRepo.py at line 111.
*   **Dependencies:** This class does not depend on any other classes or modules outside of those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object with a file path and a commit tree. Sets up internal attributes for lazy loading including placeholders for blob, content, and size.
    *   *Parameters:*
        -   **file_path** (`str`): The path to the file within the repository.
        -   **commit_tree** (`git.Tree`): The tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* A property that lazily loads and returns the Git blob object associated with the file. If the blob hasn't been loaded yet, it attempts to retrieve it from the commit tree using the stored file path. Raises a FileNotFoundError if the file cannot be found in the commit tree.
        *   *Parameters:*
        *   *Returns:*
            -   **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions or methods.
            *   **Called By:** This method is not called by any other functions or methods according to the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* A property that lazily loads and returns the decoded content of the file. If the content hasn't been loaded yet, it reads the data stream from the blob and decodes it as UTF-8 text, ignoring encoding errors. Returns the decoded string content.
        *   *Parameters:*
        *   *Returns:*
            -   **content** (`str`): The decoded content of the file.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions or methods.
            *   **Called By:** This method is not called by any other functions or methods according to the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* A property that lazily loads and returns the size of the file in bytes. If the size hasn't been determined yet, it retrieves the size directly from the blob object. Returns the integer size of the file.
        *   *Parameters:*
        *   *Returns:*
            -   **size** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions or methods.
            *   **Called By:** This method is not called by any other functions or methods according to the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* An example analysis method that counts the number of words in the file's content. It leverages the content property to ensure the content is loaded before performing the word count operation using the split() method on the content string.
        *   *Parameters:*
        *   *Returns:*
            -   **word_count** (`int`): The total number of words in the file content.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions or methods.
            *   **Called By:** This method is not called by any other functions or methods according to the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* Provides a useful string representation of the RepoFile object, displaying the file path for debugging and logging purposes.
        *   *Parameters:*
        *   *Returns:*
            -   **repr_string** (`str`): A string representation of the RepoFile object.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions or methods.
            *   **Called By:** This method is not called by any other functions or methods according to the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content=False)`
        *   *Description:* Serializes the RepoFile object into a dictionary format. Includes basic file information like path, name, size, and type. Optionally includes the full content if the include_content flag is set to True.
        *   *Parameters:*
            -   **include_content** (`bool`): Flag indicating whether to include the file content in the returned dictionary.
        *   *Returns:*
            -   **data** (`dict`): A dictionary containing file metadata and optionally the content.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions or methods.
            *   **Called By:** This method is not called by any other functions or methods according to the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory and providing access to its files through RepoFile objects. It supports retrieving all files in the repository, constructing a hierarchical file tree representation, and cleaning up the temporary directory upon closing. The class implements the context manager protocol (__enter__ and __exit__) to ensure proper resource management.
*   **Instantiation:** This class is instantiated in the evaluation.py file within the evaluation function at line 86 and in the main.py file within the main_workflow function at line 141.
*   **Dependencies:** This class depends on the 'tempfile', 'shutil', 'git.Repo', 'git.GitCommandError', 'logging', and 'os' modules.
*   **Constructor:**
    *   *Description:* Initializes a GitRepository instance by cloning the specified repository URL into a temporary directory. It sets up necessary attributes such as the repository URL, temporary directory path, and references to the cloned repository and its latest commit. If cloning fails, it raises a RuntimeError after attempting to clean up.
    *   *Parameters:*
        -   **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* Retrieves a list of all files in the repository and creates RepoFile objects for each file. These objects are stored in the instance's 'files' attribute and returned. The method uses git ls-files to enumerate the files.
        *   *Parameters:*
        *   *Returns:*
            -   **list[RepoFile]** (`list[RepoFile]`): A list of RepoFile instances representing the files in the repository.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods internally.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* Deletes the temporary directory used for the repository clone. It prints a message indicating which directory is being deleted and sets the temp_dir attribute to None.
        *   *Parameters:*
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other methods internally.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* Enables the use of the GitRepository instance as a context manager. It simply returns the instance itself, allowing the 'with' statement to manage the lifecycle of the repository.
        *   *Parameters:*
        *   *Returns:*
            -   **self** (`GitRepository`): The GitRepository instance itself.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods internally.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* Implements the context manager's exit protocol. It calls the close() method to clean up the temporary directory when exiting the 'with' block.
        *   *Parameters:*
            -   **exc_type** (`Any`): Exception type, if an exception occurred during execution.
            -   **exc_val** (`Any`): Exception value, if an exception occurred during execution.
            -   **exc_tb** (`Any`): Exception traceback, if an exception occurred during execution.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the close() method internally.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content=False)`
        *   *Description:* Constructs a hierarchical tree representation of the repository's file structure. If no files have been retrieved yet, it first calls get_all_files(). Then, it iterates over the files and builds a nested dictionary structure reflecting the directory hierarchy. Optionally includes file content in the output.
        *   *Parameters:*
            -   **include_content** (`bool`): If True, includes file content in the resulting tree nodes.
        *   *Returns:*
            -   **tree** (`dict`): A dictionary representing the hierarchical file tree structure.
        *   **Usage:**
            *   **Calls:** This method calls the get_all_files() method internally if the files list is empty.
            *   **Called By:** This method is not called by any other methods according to the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** Die Funktion erstellt ein Balkendiagramm zur Darstellung des Token-Vergleichs zwischen JSON und TOON Format. Sie verwendet matplotlib zur Erstellung des Diagramms und speichert das Ergebnis in einer Datei. Das Diagramm zeigt die Anzahl der Tokens für beide Formate sowie den Prozentsatz der Einsparung. Die Funktion nimmt Parameter für die Token-Anzahl, den Einsparungsprozentsatz und den Ausgabepfad entgegen.
*   **Parameters:**
    -   **json_tokens** (`int`): Die Anzahl der Tokens im JSON-Format.
    -   **toon_tokens** (`int`): Die Anzahl der Tokens im TOON-Format.
    -   **savings_percent** (`float`): Der Prozentsatz der Einsparung zwischen den beiden Formaten.
    -   **output_path** (`str`): Der Dateipfad, unter dem das generierte Diagramm gespeichert wird.
*   **Returns:**
*   **Usage:**
    *   **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.
    *   **Called By:** Die Funktion wird von der Funktion 'main_workflow' in der Datei 'main.py' aufgerufen.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** The function calculates the net time duration between a start and end time, adjusted for sleep periods caused by rate limits. It specifically handles cases where the model name starts with 'gemini-', applying additional logic to account for batching and associated sleep times. If the model is not a gemini model, it simply returns the total duration. For zero items, it returns zero. Otherwise, it computes the number of batches, determines the sleep count based on batch size, and subtracts the total sleep time from the overall duration.
*   **Parameters:**
    -   **start_time** (`float or datetime`): The starting timestamp or time value.
    -   **end_time** (`float or datetime`): The ending timestamp or time value.
    -   **total_items** (`int`): The total number of items processed.
    -   **batch_size** (`int`): The number of items per batch.
    -   **model_name** (`str`): The name of the model being used, which determines whether rate limit adjustments apply.
*   **Returns:**
    -   **net_time** (`float or int`): The calculated net time after subtracting sleep durations, ensuring it is never negative.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the evaluation function in evaluation.py at lines 249 and 275, and by the main_workflow function in main.py at lines 311 and 342.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive code analysis pipeline for a given repository URL. It begins by extracting API keys and model names from input dictionaries, then clones the repository and retrieves all files. It performs various analyses including extracting basic project information, constructing a file tree, analyzing relationships between code elements, and generating an abstract syntax tree (AST). The function prepares inputs for a helper LLM to analyze individual functions and classes, then calls the helper LLM to generate documentation for these elements. Finally, it prepares inputs for a main LLM to produce a final report based on all collected data.
*   **Parameters:**
    -   **input** (`Any`): The input provided to the workflow, typically a string containing a repository URL.
    -   **api_keys** (`dict`): A dictionary containing API keys for different services such as Gemini, OpenAI, and SCADsLLM.
    -   **model_names** (`dict`): A dictionary specifying the names of models to be used for the helper and main LLMs.
    -   **status_callback** (`Callable[[str], None]`): An optional callback function to report progress updates.
*   **Returns:**
    -   **report** (`str`): The final markdown report generated by the main LLM.
    -   **metrics** (`dict`): A dictionary containing timing metrics for helper and main LLM processing.
*   **Usage:**
    *   **Calls:** This function internally calls several components including GitRepository for cloning repositories, ProjektInfoExtractor for extracting basic project info, ProjectAnalyzer for relationship analysis, ASTAnalyzer for AST creation, LLMHelper for function/class analysis, and MainLLM for final report generation.
    *   **Called By:** This function is called by the frontend.Frontend function in Frontend.py at line 489 and by backend.main in main.py at line 533.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The function 'update_status' is designed to handle status updates by invoking an optional callback function if one is defined, followed by logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages within the application.
*   **Parameters:**
    -   **msg** (`Any`): A message to be logged and optionally passed to a status callback function.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on an external 'status_callback' variable and the 'logging' module.
    *   **Called By:** This function is invoked multiple times by the 'main_workflow' function in main.py at various lines including 81, 134, 158, 167, 175, 185, 195, 205, 301, 333, 336, 409, 412, and 430.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases where the filepath is not under the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure.
*   **Parameters:**
    -   **filepath** (`str`): The absolute or relative path to a Python file.
    -   **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    -   **module_path** (`str`): A dot-separated module path derived from the given file path.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by _collect_definitions in relationship_analyzer.py at line 60 and by __init__ in relationship_analyzer.py at line 134.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is responsible for analyzing Python project structures by identifying definitions (functions, classes, methods) and tracking their call relationships across files. It walks through a project directory, parses Python files into ASTs, collects definitions with their metadata, resolves inter-file calls using a custom visitor, and formats the results into a structured output showing which definitions are called by which other definitions.
*   **Instantiation:** This class is instantiated by the functions 'evaluation' in 'evaluation.py' at line 119 and 'main_workflow' in 'main.py' at line 177.
*   **Dependencies:** No external dependencies are explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including storage for definitions, call graphs, and file ASTs, while also defining a set of directories to ignore during traversal.
    *   *Parameters:*
        -   **project_root** (`str`): The root directory path of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* The main analysis method that orchestrates the process of finding Python files, collecting definitions from those files, resolving call relationships, and formatting the final results. It clears the cached ASTs after processing to free memory.
        *   *Parameters:*
        *   *Returns:*
            -   **output_list** (`list`): A list of dictionaries representing the formatted call relationship results.
        *   **Usage:**
            *   **Calls:** This method calls `_find_py_files`, `_collect_definitions` for each file, `_resolve_calls` for each file, and finally `get_formatted_results`.
            *   **Called By:** This method is called by the functions 'evaluation' in 'evaluation.py' at line 120 and 'main_workflow' in 'main.py' at line 178.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* Recursively walks the project root directory to find all Python (.py) files, excluding certain directories like .git, venv, etc., and returns a list of absolute paths to these files.
        *   *Parameters:*
        *   *Returns:*
            -   **py_files** (`list`): A list of absolute file paths ending in .py.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods within the class.
            *   **Called By:** This method is called by the 'analyze' method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* Parses a given Python file into an Abstract Syntax Tree (AST), walks the tree to identify function and class definitions, and stores metadata about these definitions such as file location and line number. Handles errors gracefully by logging them and marking the file's AST as None.
        *   *Parameters:*
            -   **filepath** (`str`): The absolute path to the Python file to analyze.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other methods within the class.
            *   **Called By:** This method is called by the 'analyze' method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* Given an AST node and a tree, this helper method attempts to find the parent node of the specified node by walking the tree and checking child nodes. Returns None if no parent is found.
        *   *Parameters:*
            -   **tree** (`ast.AST`): The AST tree to search in.
            -   **node** (`ast.AST`): The AST node whose parent is to be found.
        *   *Returns:*
            -   **parent** (`ast.AST or None`): The parent AST node of the given node, or None if not found.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods within the class.
            *   **Called By:** This method is called by the '_collect_definitions' method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* Uses a CallResolverVisitor to traverse the AST of a given file and resolve function calls. It updates the global call graph with information about who calls whom. Errors during resolution are logged but do not halt execution.
        *   *Parameters:*
            -   **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the 'CallResolverVisitor' class to visit the AST.
            *   **Called By:** This method is called by the 'analyze' method.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* Formats the collected call graph and definition data into a structured list of dictionaries. Each dictionary represents a definition and includes details such as identifier, mode (function/class/method), origin file, line number, and a list of callers. Duplicate calls are removed before returning.
        *   *Parameters:*
        *   *Returns:*
            -   **output_list** (`list`): A list of dictionaries containing formatted call relationship data.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods within the class.
            *   **Called By:** This method is called by the 'analyze' method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to traverse Python source code and resolve call relationships between functions, methods, and modules. It tracks the current execution context (like class or function scope) and records calls made within the code, associating them with their callers and the files they originate from. It also maintains mappings of imported names and instance types to support accurate call resolution.
*   **Instantiation:** This class is instantiated in the function `_resolve_calls` located in the file relationship_analyzer.py at line 92.
*   **Dependencies:** This class does not depend on any external libraries beyond standard Python modules like ast, os, and collections.defaultdict.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and a dictionary of definitions. It sets up internal tracking structures such as scope, instance types, and call records, and determines the module path based on the file path and project root.
    *   *Parameters:*
        -   **filepath** (`str`): The absolute path to the Python file being analyzed.
        -   **project_root** (`str`): The root directory of the project, used to compute relative module paths.
        -   **definitions** (`dict`): A dictionary mapping qualified names to their definitions, used to validate and resolve calls.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Handles the traversal of class definitions in the AST. It updates the current class name context during traversal and restores the previous class name after visiting the class body.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is called by the generic AST visitor when encountering a class definition node.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Handles the traversal of function definitions in the AST. It updates the current caller name context to the function name during traversal and restores the previous caller name after visiting the function body.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is called by the generic AST visitor when encountering a function definition node.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes call nodes in the AST to determine the qualified name of the called function or method. If the call can be resolved and exists in the definitions, it records the call with metadata about the caller, file, and line number.
        *   *Parameters:*
            -   **node** (`ast.Call`): The AST node representing the function call.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the private helper method `_resolve_call_qname` to resolve the qualified name of the function being called.
            *   **Called By:** This method is called by the generic AST visitor when encountering a call expression node.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST by updating the internal scope mapping to associate aliases with their actual module names.
        *   *Parameters:*
            -   **node** (`ast.Import`): The AST node representing the import statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is called by the generic AST visitor when encountering an import statement node.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST by resolving the full module path and updating the internal scope mapping for imported names.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is called by the generic AST visitor when encountering a 'from ... import ...' statement node.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* Processes assignment statements in the AST to track instances of classes. If an assignment involves a call to a known class, it maps the assigned variable to the qualified class name.
        *   *Parameters:*
            -   **node** (`ast.Assign`): The AST node representing the assignment statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is called by the generic AST visitor when encountering an assignment statement node.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* Resolves the qualified name of a function or method call based on the AST node representing the call. It handles both direct names and attribute access (e.g., obj.method).
        *   *Parameters:*
            -   **func_node** (`ast.expr`): The AST node representing the function or method being called.
        *   *Returns:*
            -   **qualified_name** (`str or None`): The fully qualified name of the function or method, or None if it cannot be resolved.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is called by the `visit_Call` method to resolve the qualified name of a function call.

### File: `backend/scads_key_test.py`
*Analysis data not available for this component.*

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** The function encrypts a given text string using a Fernet cipher suite. It first checks if the input text is empty or if the cipher suite is not available, returning the text as-is in such cases. If both conditions are met, it encodes the stripped text to bytes, encrypts it, and returns the decrypted result as a string.
*   **Parameters:**
    -   **text** (`str`): The text string to be encrypted.
*   **Returns:**
    -   **encrypted_text** (`str`): The encrypted version of the input text, returned as a string.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the update_gemini_key function located in db.py at line 71.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** The function decrypts a given text using a cipher suite, returning the decrypted string if successful. If the input text is empty or the cipher suite is not available, it returns the original text unchanged. In case of decryption failure, it also returns the original text. The function handles potential exceptions during decryption gracefully.
*   **Parameters:**
    -   **text** (`str`): The encrypted text to be decrypted.
*   **Returns:**
    -   **result** (`str`): The decrypted text if successful; otherwise, the original input text.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the function 'get_decrypted_api_keys' in the file 'db.py'.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** The function inserts a new user into the database by creating a user document with the provided username, name, and password. The password is hashed using a hasher utility before being stored. The function also initializes additional fields such as API keys and returns the ID of the inserted document.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user, used as the '_id' field in the database.
    -   **name** (`str`): The full name of the user.
    -   **password** (`str`): The plain text password of the user, which gets hashed before storage.
*   **Returns:**
    -   **inserted_id** (`ObjectId`): The unique identifier generated by the database for the newly inserted user document.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the frontend.Frontend class in the Frontend.py file at line 294.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user documents from a MongoDB collection named 'dbusers'. It performs a database query to find all records in the collection and returns them as a list. The function does not take any parameters and directly accesses the global 'dbusers' variable, which is expected to be initialized elsewhere in the codebase.
*   **Parameters:**
*   **Returns:**
    -   **result** (`list`): A list containing all user documents retrieved from the 'dbusers' collection in the database.
*   **Usage:**
    *   **Calls:** The function does not call any other functions directly.
    *   **Called By:** This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 244.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The function 'fetch_user' retrieves a user document from a MongoDB collection named 'dbusers' based on the provided username. It performs a lookup operation using the username as the search key in the '_id' field of the document. The function assumes that the 'dbusers' collection is already initialized and accessible via a global or module-level variable named 'dbusers'.
*   **Parameters:**
    -   **username** (`str`): The unique identifier (username) used to locate the specific user document in the database.
*   **Returns:**
    -   **result** (`Any`): The user document retrieved from the 'dbusers' collection, or None if no matching document is found.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is not called by any other functions within the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the name field of a user document in a MongoDB collection identified by the username. It uses the MongoDB update_one method to modify only the name field, leaving other fields unchanged. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    -   **username** (`str`): The unique identifier (typically the _id field) of the user whose name needs to be updated.
    -   **new_name** (`str`): The new name value to set for the specified user.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified by the update operation. This should typically be 1 if the user exists and the update was applied.
*   **Usage:**
    *   **Calls:** The function internally calls the MongoDB update_one method to perform the database update operation.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database by first encrypting the provided key and then performing an update operation on the 'dbusers' collection. It takes a username and a raw API key as inputs, strips any leading or trailing whitespace from the key, encrypts it, and stores the encrypted version in the database under the user's document. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    -   **gemini_api_key** (`str`): The raw Gemini API key provided by the user, which will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified in the database. This value is typically 1 if the update succeeded.
*   **Usage:**
    *   **Calls:** This function internally uses the 'encrypt_text' function to encrypt the provided API key before storing it.
    *   **Called By:** This function is called by 'save_gemini_cb' in 'Frontend.py' at line 35 and by 'frontend.Frontend' in 'Frontend.py' at line 393.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and attempts to update the corresponding document in the 'dbusers' collection. The function returns the count of modified documents, which should be 1 if the update was successful or 0 if no matching document was found.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose Ollama base URL needs to be updated.
    -   **ollama_base_url** (`str`): The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified by the update operation. Typically 1 if a matching document was found and updated, or 0 if no matching document was found.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on the pymongo library's update_one method.
    *   **Called By:** This function is called by save_ollama_cb in Frontend.py at line 42 and by frontend.Frontend in Frontend.py at line 407.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** The function retrieves a Gemini API key associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'gemini_api_key' field. If no matching user is found, it returns None.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose Gemini API key is to be retrieved.
*   **Returns:**
    -   **gemini_api_key** (`Optional[str]`): The Gemini API key associated with the user, or None if the user is not found.
*   **Usage:**
    *   **Calls:** This function internally uses the 'dbusers.find_one' method to query the database.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the provided username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None.
*   **Parameters:**
    -   **username** (`str`): The unique identifier (username) used to look up the user in the database.
*   **Returns:**
    -   **ollama_base_url** (`str or None`): The Ollama base URL retrieved from the user's record, or None if no such user exists.
*   **Usage:**
    *   **Calls:** The function internally uses the 'dbusers.find_one' method to query the database.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** The function 'delete_user' removes a user document from a MongoDB collection identified by the provided username. It performs a deletion operation using the 'delete_one' method on the 'dbusers' collection, targeting the document where the '_id' field matches the given username. The function returns the count of deleted documents, which should be 1 if the user was successfully deleted or 0 if no matching user was found.
*   **Parameters:**
    -   **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    -   **deleted_count** (`int`): The number of documents deleted as a result of the operation. Typically 1 if a user was deleted, or 0 if no matching user was found.
*   **Usage:**
    *   **Calls:** This function internally uses the 'delete_one' method on the 'dbusers' collection to perform the deletion operation.
    *   **Called By:** This function is not called by any other functions within the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user is not found, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function, while directly retrieving the 'ollama_base_url' field without decryption. Both decrypted and non-decrypted values are returned as a tuple.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose API keys are to be retrieved.
*   **Returns:**
    -   **gemini_plain** (`str`): The decrypted Gemini API key for the user, or an empty string if not present.
    -   **ollama_plain** (`str`): The Ollama base URL for the user, or an empty string if not present.
*   **Usage:**
    *   **Calls:** The function internally uses dbusers.find_one to retrieve user data from the database.
    *   **Called By:** This function is called by the frontend.Frontend class in Frontend.py at lines 380 and 479.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** The function 'insert_chat' creates a new chat entry in the database with a unique identifier, associated username, chat name, and creation timestamp. It generates a UUID for the chat entry, populates the necessary fields, and inserts the document into the 'dbchats' collection. The function then returns the ID of the inserted document.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat.
    -   **chat_name** (`str`): The name of the chat.
*   **Returns:**
    -   **result.inserted_id** (`str`): The unique identifier of the newly inserted chat document.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by load_data_from_db in Frontend.py at line 81, handle_delete_chat in Frontend.py at line 122, and frontend.Frontend in Frontend.py at line 344.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** Die Funktion fetch_chats_by_user ruft alle Chats eines bestimmten Benutzers aus einer MongoDB-Datenbank ab. Sie verwendet den Benutzernamen als Filterkriterium und sortiert die Ergebnisse nach dem Erstellungsdatum in aufsteigender Reihenfolge. Das Ergebnis ist eine Liste der gefundenen Chat-Dokumente.
*   **Parameters:**
    -   **username** (`str`): Der Benutzername, dessen Chats abgerufen werden sollen.
*   **Returns:**
    -   **chats** (`list`): Eine Liste aller Chat-Dokumente des angegebenen Benutzers, sortiert nach Erstellungsdatum.
*   **Usage:**
    *   **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.
    *   **Called By:** Die Funktion wird von der Funktion load_data_from_db in der Datei Frontend.py aufgerufen.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a query using MongoDB's find_one method to locate a document matching both the username and chat name. If such a document is found, the function returns True; otherwise, it returns False.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat.
    -   **chat_name** (`str`): The name of the chat to check for existence.
*   **Returns:**
    -   **exists** (`bool`): True if a chat with the specified username and chat name exists in the database, False otherwise.
*   **Usage:**
    *   **Calls:** The function internally uses the dbchats.find_one method to query the database.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and updates all associated exchanges in the database. It first updates the chat entry in the chats collection, then updates all related exchange records in the exchanges collection. The function returns the number of modified chat entries.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be renamed.
    -   **old_name** (`str`): The current name of the chat to be renamed.
    -   **new_name** (`str`): The new name to assign to the chat.
*   **Returns:**
    -   **modified_count** (`int`): The number of chat entries that were successfully modified in the database.
*   **Usage:**
    *   **Calls:** The function performs database operations using MongoDB update methods but does not call any other user-defined functions.
    *   **Called By:** This function is called by the frontend.Frontend class in the Frontend.py file at line 462.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str="", main_used: str="", total_time: str="", helper_time: str="", main_time: str="")`
*   **Description:** This function inserts a new exchange record into a MongoDB collection. It generates a unique ID for the exchange, constructs a dictionary with all the provided details including question, answer, feedback, and timestamps, and attempts to insert this data into the database. If the insertion fails, it catches the exception, prints an error message, and returns None. Otherwise, it returns the generated unique ID.
*   **Parameters:**
    -   **question** (`str`): The question asked in the exchange.
    -   **answer** (`str`): The answer provided in response to the question.
    -   **feedback** (`str`): Feedback associated with the exchange.
    -   **username** (`str`): The username of the user involved in the exchange.
    -   **chat_name** (`str`): The name of the chat session.
    -   **helper_used** (`str`): The helper tool used during the exchange (optional).
    -   **main_used** (`str`): The main tool used during the exchange (optional).
    -   **total_time** (`str`): Total time taken for the exchange (optional).
    -   **helper_time** (`str`): Time taken by the helper tool during the exchange (optional).
    -   **main_time** (`str`): Time taken by the main tool during the exchange (optional).
*   **Returns:**
    -   **new_id** (`str`): The unique ID of the inserted exchange record, or None if insertion failed.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the frontend.Frontend class in Frontend.py at line 530.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses a database query to filter documents by the username field and sorts the results chronologically. The function returns the complete list of matching exchange records as retrieved from the database.
*   **Parameters:**
    -   **username** (`str`): The unique identifier of the user whose exchange records are to be fetched.
*   **Returns:**
    -   **exchanges** (`list`): A list of exchange records associated with the specified username, sorted by creation timestamp in ascending order.
*   **Usage:**
    *   **Calls:** The function does not call any other functions directly.
    *   **Called By:** This function is called by the load_data_from_db function in the Frontend.py file.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched documents as a list.
*   **Parameters:**
    -   **username** (`str`): The username associated with the exchanges to be retrieved.
    -   **chat_name** (`str`): The name of the chat associated with the exchanges to be retrieved.
*   **Returns:**
    -   **exchanges** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order.
*   **Usage:**
    *   **Calls:** The function internally calls the 'dbexchanges.find' method to query the database and 'sort' to order the results.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** This function updates the feedback field of a document in the 'dbexchanges' collection within a MongoDB database. It takes an exchange ID and a feedback value, then attempts to update the corresponding document with the new feedback value. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    -   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    -   **feedback** (`int`): The feedback value to be set in the document.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were modified as a result of the update operation.
*   **Usage:**
    *   **Calls:** The function internally uses the 'dbexchanges.update_one' method to perform the database update operation.
    *   **Called By:** This function is called by the 'handle_feedback_change' function in 'Frontend.py' at line 98.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** This function updates the feedback message associated with a specific exchange document in a MongoDB collection. It takes an exchange ID and a new feedback message as inputs, then performs an update operation on the database to set the feedback_message field. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    -   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    -   **feedback_message** (`str`): The new feedback message to be stored in the exchange document.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified by the update operation.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on the external dbexchanges.update_one method.
    *   **Called By:** This function is called by the render_exchange function in Frontend.py at line 211.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a given exchange ID. It performs a deletion operation and returns the count of deleted documents. The function takes a single string parameter representing the unique identifier of the exchange to be deleted.
*   **Parameters:**
    -   **exchange_id** (`str`): A string representing the unique identifier of the exchange document to be deleted from the database.
*   **Returns:**
    -   **deleted_count** (`int`): The number of documents successfully deleted from the database, typically 0 or 1.
*   **Usage:**
    *   **Calls:** The function does not call any other functions directly.
    *   **Called By:** This function is called by the handle_delete_exchange function in the Frontend.py file at line 102.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function deletes a complete chat session along with all associated exchanges from the database. It first removes all exchange records linked to the specified username and chat name, followed by deleting the chat record itself. The function returns the count of deleted chat documents, which indicates whether the operation was successful.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be deleted.
    -   **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    -   **deleted_count** (`int`): The number of chat documents that were deleted from the database.
*   **Usage:**
    *   **Calls:** The function internally uses database operations to delete exchanges and chats.
    *   **Called By:** This function is called by the 'handle_delete_chat' function in 'Frontend.py' at line 110.

### File: `frontend/Frontend.py`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key associated with the user's username, clears the input field, and displays a success message to the user.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    *   **Calls:** The function internally uses streamlit session state operations and calls a database update function.
    *   **Called By:** This function is not called by any other function within the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function handles the callback for saving an Ollama URL entered by the user in a Streamlit frontend. It retrieves the URL from the session state, updates the database with the new URL associated with the username, and displays a success toast message. The function does not take any parameters and does not return any value.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    *   **Calls:** The function internally uses `st.session_state.get()` to retrieve values from the Streamlit session state and calls `db.update_ollama_url()` to update the database.
    *   **Called By:** This function is not called by any other function according to the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** Die Funktion 'load_data_from_db' lädt Chats und Exchanges konsistent aus einer Datenbank für einen bestimmten Benutzer. Sie prüft zunächst, ob der Benutzer bereits geladen wurde, und lädt dann die Chats und zugehörigen Exchanges aus der Datenbank. Bei Bedarf werden auch Standard-Chats erstellt und das aktive Chat-Objekt gesetzt.
*   **Parameters:**
    -   **username** (`str`): Der Name des Benutzers, für den die Daten aus der Datenbank geladen werden sollen.
*   **Returns:**
*   **Usage:**
    *   **Calls:** Die Funktion ruft keine anderen internen Funktionen auf.
    *   **Called By:** Die Funktion wird von 'frontend.Frontend' in der Datei 'Frontend.py' auf Zeile 310 aufgerufen.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function updates the feedback value for a given exchange object in the database and triggers a re-render of the Streamlit application. It takes an exchange dictionary and a new feedback value, assigns the feedback to the exchange, updates the database with the new feedback, and then reruns the Streamlit app to reflect the changes.
*   **Parameters:**
    -   **ex** (`dict`): A dictionary representing an exchange object, expected to contain keys such as 'feedback' and '_id'.
    -   **val** (`Any`): The new feedback value to be assigned to the exchange.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function internally calls `db.update_exchange_feedback` to update the feedback in the database and `st.rerun()` to refresh the Streamlit UI.
    *   **Called By:** This function is called by the `render_exchange` method in `Frontend.py` at lines 199 and 204.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of an exchange from the database and updates the session state accordingly. It first deletes the exchange from the database using its ID, then checks if the exchange exists in the session state for a given chat and removes it if found. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    -   **chat_name** (`str`): The name of the chat from which the exchange is to be deleted.
    -   **ex** (`dict`): A dictionary representing the exchange to be deleted, expected to contain an '_id' key.
*   **Returns:**
*   **Usage:**
    *   **Calls:** The function internally calls `db.delete_exchange_by_id` to delete the exchange from the database and `st.rerun` to refresh the Streamlit UI.
    *   **Called By:** This function is called by the `render_exchange` function in `Frontend.py` at lines 228 and 234.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** The function handles the deletion of a chat by first removing the chat from the database and then cleaning up the session state. It ensures that the active chat is updated appropriately, either by selecting another existing chat or by creating a new default chat if none remain. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be deleted.
    -   **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on external modules like 'db' and 'st.session_state'.
    *   **Called By:** This function is called by the frontend.Frontend class in Frontend.py at line 367.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** The function 'extract_repo_name' takes a text input and attempts to extract a repository name from any URL present in the text. It uses regular expressions to find a URL, parses it using urllib.parse.urlparse, and then extracts the last component of the URL path, removing the '.git' suffix if present. If no valid URL is found or if the URL does not contain a repository name, the function returns None.
*   **Parameters:**
    -   **text** (`str`): A string that may contain a URL from which to extract the repository name.
*   **Returns:**
    -   **repo_name** (`str`): The extracted repository name from the URL, with '.git' suffix removed if present, or None if no valid URL is found.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on imported modules like 're' and 'urllib.parse.urlparse'.
    *   **Called By:** This function is called by the 'frontend.Frontend' class, specifically at line 442 in the file 'Frontend.py'.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** The function 'stream_text_generator' takes a string input and yields each word from the string followed by a space, with a small delay between each yield. It is designed to simulate a streaming effect for text rendering. The function splits the input text into words based on spaces and iterates through them, yielding one word at a time with a short pause.
*   **Parameters:**
    -   **text** (`str`): A string input containing the text to be streamed.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by 'render_text_with_mermaid' in 'Frontend.py' at line 160.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream)`
*   **Description:** This function processes a markdown text string to identify and render Mermaid diagrams embedded within code blocks. It splits the input text by Mermaid code blocks and renders regular markdown content normally while rendering Mermaid diagrams using a specialized component. If a Mermaid diagram fails to render, it falls back to displaying the raw code block. The function supports streaming output for regular markdown content.
*   **Parameters:**
    -   **markdown_text** (`str`): The markdown text that may contain Mermaid code blocks enclosed in triple backticks with 'mermaid' as the language identifier.
    -   **should_stream** (`bool`): A flag indicating whether regular markdown content should be streamed to the frontend instead of rendered all at once.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other user-defined functions directly; it relies on external libraries such as 're', 'st_mermaid', 'st.write_stream', 'st.markdown', and 'st.code'.
    *   **Called By:** This function is called by 'render_exchange' in 'Frontend.py' at line 238 and by 'frontend.Frontend' in 'Frontend.py' at line 524.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function renders a chat exchange in a Streamlit interface, displaying a user's question and an assistant's response. It handles both regular responses and error cases, providing interactive feedback mechanisms such as like/dislike buttons, comment popups, download options, and delete functionality. The UI is structured with a toolbar container for controls and a content area for the response text, including Mermaid rendering.
*   **Parameters:**
    -   **ex** (`dict`): A dictionary representing the exchange, containing keys such as 'question', 'answer', 'feedback', 'feedback_message', '_id', etc.
    -   **current_chat_name** (`str`): The name of the current chat session, used for handling deletion operations.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not directly call any other user-defined functions; it relies on Streamlit components and external functions like 'handle_feedback_change' and 'handle_delete_exchange'.
    *   **Called By:** This function is called by the frontend.Frontend class, specifically at line 429 in Frontend.py.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the metadata of a single function parameter. It encapsulates three core attributes: the parameter's name, its type, and a descriptive explanation. This class serves as a structured data model for documenting function parameters, ensuring consistency and type safety in parameter metadata handling.
*   **Instantiation:** This class is not directly instantiated by any other component as indicated by the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the source file.
*   **Constructor:**
    *   *Description:* The constructor initializes the ParameterDescription instance with three required fields: name, type, and description. These fields are defined as string types and are used to store information about a function parameter.
    *   *Parameters:*
        -   **name** (`str`): The name of the function parameter.
        -   **type** (`str`): The data type of the function parameter.
        -   **description** (`str`): A textual description of the function parameter's purpose or usage.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model designed to represent and validate the description of a function's return value. It encapsulates three essential properties: the name of the return value, its type, and a textual description. This class ensures data integrity and structure for return value metadata, making it suitable for use in API documentation, code analysis tools, or any system requiring standardized return value specifications.
*   **Instantiation:** This class is not instantiated by any other component as per the provided context.
*   **Dependencies:** No external dependencies are explicitly listed for this class.
*   **Constructor:**
    *   *Description:* The constructor initializes a ReturnDescription instance with three required fields: name, type, and description. These fields are typical attributes of a Pydantic model and are used to define the characteristics of a function's return value.
    *   *Parameters:*
        -   **name** (`str`): The name of the return value.
        -   **type** (`str`): The type of the return value.
        -   **description** (`str`): A textual description of the return value.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function. It encapsulates two string fields: 'calls', which describes the functions or methods that are called by the function in question, and 'called_by', which indicates the function or method that invokes the function in question. This class serves as a structured way to document and enforce the usage context of functions within a codebase.
*   **Instantiation:** This class is not instantiated by any other components mentioned in the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a new instance of the UsageContext class with the required 'calls' and 'called_by' string fields.
    *   *Parameters:*
        -   **calls** (`str`): A string describing the functions or methods that are called by the function in question.
        -   **called_by** (`str`): A string indicating the function or method that invokes the function in question.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate detailed information about a function's purpose, parameters, return values, and usage context. It serves as a structured representation for documenting function signatures and behavior, making it suitable for API documentation, code analysis tools, or automated code generation systems.
*   **Instantiation:** This class is not instantiated by any other components as indicated in the context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The constructor initializes the FunctionDescription instance with required fields: overall description, a list of parameter descriptions, a list of return value descriptions, and a usage context object. Since this class inherits from BaseModel, it leverages Pydantic's validation and serialization capabilities.
    *   *Parameters:*
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic model designed to represent the complete JSON schema for a function. It serves as a structured data container that holds essential information about a function, including its identifier, a detailed description, and an optional error field. This class is primarily used for documenting and validating function metadata within a larger system.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules or libraries beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a FunctionAnalysis instance with an identifier, a FunctionDescription object, and an optional error string. The constructor sets up the basic structure required to represent a function's metadata.
    *   *Parameters:*
        -   **identifier** (`str`): A unique string identifier for the function.
        -   **description** (`FunctionDescription`): An object containing detailed information about the function's purpose, parameters, and behavior.
        -   **error** (`Optional[str]`): An optional string field to store any error messages related to the function.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to describe the initialization method (__init__) of a class. It encapsulates a textual description of the constructor's purpose and a list of parameter descriptions that define its inputs.
*   **Instantiation:** This class is not instantiated by any other component as indicated by the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription instance with a description of the constructor and a list of parameter descriptions.
    *   *Parameters:*
        -   **description** (`str`): A textual description of the constructor's purpose.
        -   **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing each parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
*   **Instantiation:** This class is not instantiated by any other components as per the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields are intended to store information about the class's external dependencies and the entities responsible for its instantiation.
    *   *Parameters:*
        -   **dependencies** (`str`): A string describing the external dependencies of the class.
        -   **instantiated_by** (`str`): A string describing the entities or classes that instantiate this class.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class serves as a structured representation for encapsulating detailed information about a class, including its overall purpose, constructor details, individual method analyses, and usage context. It is designed to provide a comprehensive overview of a class's functionality and integration within a system.
*   **Instantiation:** This class is not instantiated by any other components as indicated in the context.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond those imported in the file.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ClassDescription class with specified attributes for overall purpose, constructor description, method analyses, and usage context.
    *   *Parameters:*
        -   **overall** (`str`): A string describing the overall purpose and functionality of the class.
        -   **init_method** (`ConstructorDescription`): An object detailing the constructor's purpose and parameters.
        -   **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects representing the methods of the class.
        -   **usage_context** (`ClassContext`): An object providing context on how the class is used and its dependencies.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential information about a class including its identifier, a detailed description, and an optional error field for capturing any issues during processing.
*   **Instantiation:** This class is not instantiated by any other components based on the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes a new instance of the ClassAnalysis class with required fields for the identifier and description, and an optional error field.
    *   *Parameters:*
        -   **identifier** (`str`): A string identifier for the class being analyzed.
        -   **description** (`ClassDescription`): An instance of ClassDescription providing detailed metadata about the class.
        -   **error** (`Optional[str]`): An optional string field to capture any errors encountered during analysis.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for documenting call relationships within the system.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** No external dependencies were identified for this class.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo instance with fields representing a call event, including the file path, function name, call mode, and line number.
    *   *Parameters:*
        -   **file** (`str`): The file path where the call occurred.
        -   **function** (`str`): The name of the function that made the call.
        -   **mode** (`str`): The mode of the call, such as 'method', 'function', or 'module'.
        -   **line** (`int`): The line number in the file where the call occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to represent structured context for analyzing a function. It encapsulates two key pieces of information: a list of function calls made within the function and a list of CallInfo objects indicating which functions call this one. This class serves as a data transfer object to facilitate function analysis and dependency tracking.
*   **Instantiation:** This class is instantiated in the evaluation.py file within the evaluation function at line 162, and also in main.py within the main_workflow function at line 223.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes the FunctionContextInput with two attributes: 'calls', a list of strings representing function names called within the function, and 'called_by', a list of CallInfo objects representing functions that call this function.
    *   *Parameters:*
        -   **calls** (`List[str]`): A list of strings representing the names of functions called within the analyzed function.
        -   **called_by** (`List[CallInfo]`): A list of CallInfo objects representing the functions that call the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for function analysis, including the mode of operation, identifier, source code, imports, and associated context.
*   **Instantiation:** The class is instantiated by the evaluation function in evaluation.py at line 167 and by the main_workflow function in main.py at line 228.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput instance with required fields including the operational mode, identifier, source code, list of imports, and contextual information.
    *   *Parameters:*
        -   **mode** (`Literal["function_analysis"]`): Specifies the operational mode for the analysis, constrained to the literal value 'function_analysis'.
        -   **identifier** (`str`): A unique identifier for the function being analyzed.
        -   **source_code** (`str`): The complete source code of the function to be analyzed.
        -   **imports** (`List[str]`): A list of import statements used within the function's source code.
        -   **context** (`FunctionContextInput`): An object containing contextual information related to the function analysis.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent method metadata, facilitating better introspection and analysis of code structures.
*   **Instantiation:** The class is instantiated in the evaluation.py file within the evaluation function at line 187 and in main.py within the main_workflow function at line 248.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes the MethodContextInput instance with fields for identifying the method, listing its dependencies, tracking callers, specifying arguments, and storing its docstring.
    *   *Parameters:*
        -   **identifier** (`str`): A string identifier for the method.
        -   **calls** (`List[str]`): A list of strings representing the identifiers of methods called by this method.
        -   **called_by** (`List[CallInfo]`): A list of CallInfo objects indicating which methods call this method.
        -   **args** (`List[str]`): A list of strings representing the argument names of the method.
        -   **docstring** (`Optional[str]`): An optional string containing the docstring of the method.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to encapsulate structured context information for analyzing a class. It holds three main pieces of data: a list of dependencies, a list of call information for instances where the class is instantiated, and a list of method contexts detailing the behavior of methods within the class.
*   **Instantiation:** The class is instantiated by the functions 'main_orchestrator' in HelperLLM.py at line 369, 'evaluation' in evaluation.py at line 199, and 'main_workflow' in main.py at line 260.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond those imported in the file.
*   **Constructor:**
    *   *Description:* The constructor initializes the ClassContextInput object with three attributes: dependencies, instantiated_by, and method_context. These attributes are expected to hold lists of strings, CallInfo objects, and MethodContextInput objects respectively.
    *   *Parameters:*
        -   **dependencies** (`List[str]`): A list of string identifiers representing the dependencies of the class.
        -   **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where and how the class is instantiated.
        -   **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects describing the context and behavior of methods within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class serves as a data structure for encapsulating the necessary inputs required to generate a ClassAnalysis object. It defines the expected fields including the mode of operation, a unique identifier for the class being analyzed, the source code of the class, a list of import statements, and contextual information about how the class is used.
*   **Instantiation:** The class is instantiated by the main_orchestrator function in HelperLLM.py at line 338, the evaluation function in evaluation.py at line 205, and the main_workflow function in main.py at line 266.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysisInput instance with the required fields: mode, identifier, source_code, imports, and context. The mode is constrained to the literal value 'class_analysis', ensuring that only class analysis operations can instantiate this object.
    *   *Parameters:*
        -   **mode** (`Literal['class_analysis']`): A literal string that specifies the mode of operation, which must be 'class_analysis'.
        -   **identifier** (`str`): A string identifier for the class being analyzed.
        -   **source_code** (`str`): The raw source code of the class being analyzed.
        -   **imports** (`List[str]`): A list of import statements from the source file.
        -   **context** (`ClassContextInput`): Contextual information about how the class is used, including dependencies and instantiation points.
*   **Methods:**

---
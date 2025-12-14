# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
-   **Description:** The `repo-onboarding-agent` is an automated documentation pipeline designed to generate comprehensive Markdown reports for GitHub repositories. It clones repositories, extracts structural and semantic information using AST analysis, call graph generation, and relationship detection, then synthesizes this data into human-readable documentation using a multi-LLM approach. It features a Streamlit-based frontend for user interaction and a MongoDB backend for managing user data and conversation history.
-   **Key Features:**
    -   Automated repository cloning and file extraction.
    -   Detailed code analysis (AST, call graphs, dependencies, relationships).
    -   Multi-stage LLM-driven documentation generation for functions and classes.
    -   Interactive Streamlit frontend for user input and report display.
    -   MongoDB integration for user management and chat history persistence.
-   **Tech Stack:** Python, LangChain, Pydantic, Streamlit, GitPython, PyMongo, NetworkX, Matplotlib, Google Gemini API, OpenAI API, Ollama (local LLM integration), TOML.

*   **Repository Structure:**
    ```mermaid
    graph LR
        root --> SystemPrompts[SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt]
        root --> backend[backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
        root --> database[database<br/>db.py]
        root --> frontend[frontend<br/>Frontend.py<br/>__init__.py]
        root --> notizen[notizen<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md]
        root --> result[result<br/>ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md]
        root --> schemas[schemas<br/>types.py]
        root --> statistics[statistics<br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png]
        frontend --> frontend_streamlit[.streamlit<br/>config.toml]
        frontend --> frontend_gifs[gifs<br/>4j.gif]
        notizen --> grafiken[grafiken]
        grafiken --> grafiken_1[1<br/>File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot]
        grafiken --> grafiken_2[2<br/>FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot]
        grafiken --> grafiken_flaskrepo[Flask-Repo<br/>__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot]
        grafiken --> grafiken_repoonboarding[Repo-onboarding<br/>AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot]
        root --> .env.example
        root --> .gitignore
        root --> analysis_output.json
        root --> output.json
        root --> output.toon
        root --> readme.md
        root --> requirements.txt
    ```

    ## 2. Installation
    ### Dependencies
    ```
    - altair == 4.2.2 
    - annotated-types == 0.7.0 
    - anyio == 4.1.1.0 
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
    - langsmith == 0.4.46 
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
    ```
    To install these dependencies, run: `pip install -r requirements.txt`

    ### Setup Guide
    1.  **Clone the Repository:**
        ```bash
        git clone https://github.com/your-repo/repo-onboarding-agent.git
        cd repo-onboarding-agent
        ```
    2.  **Create a Virtual Environment:**
        ```bash
        python -m venv .venv
        source .venv/bin/activate  # On Windows: .venv\Scripts\activate
        ```
    3.  **Install Dependencies:**
        ```bash
        pip install -r requirements.txt
        ```
    4.  **Configure Environment Variables:**
        Copy the `.env.example` file to `.env` and fill in your API keys (e.g., `GEMINI_API_KEY`) and any other necessary URLs (`OLLAMA_BASE_URL`, `SCADSLLM_URL`).
        ```bash
        cp .env.example .env
        # Open .env and add your API keys/URLs
        ```

    ### Quick Startup
    To start the Streamlit frontend, navigate to the project root and run:
    ```bash
    streamlit run frontend/Frontend.py
    ```

    ## 3. Use Cases & Commands
    The `repo-onboarding-agent` is designed to automate and streamline the process of understanding and onboarding to new or unfamiliar Python codebases.

    **Primary Use Cases:**
    *   **Automated Documentation Generation:** Quickly generate comprehensive Markdown documentation for any specified GitHub repository, including high-level overviews and detailed component analyses (functions, classes, methods).
    *   **Codebase Exploration:** Developers can use the generated reports to get a rapid understanding of project structure, key functionalities, inter-component relationships (call graphs, dependencies), and the purpose of individual code elements.
    *   **Onboarding New Team Members:** Provide new team members with automatically generated documentation to reduce the time and effort required to become familiar with a project.
    *   **API/Functionality Reference:** Serve as a quick reference for the usage, parameters, and return values of functions and classes within the repository.
    *   **Quality Assurance:** By highlighting code structure and relationships, it can indirectly aid in identifying potential architectural issues or areas lacking clarity.

    **Primary Commands:**
    The main interaction with the `repo-onboarding-agent` is through its Streamlit web interface:
    *   To launch the application:
        ```bash
        streamlit run frontend/Frontend.py
        ```
    Once the application is running, users can input a GitHub repository URL directly within the UI to initiate the documentation generation process.

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is a specialized AST (Abstract Syntax Tree) visitor that traverses Python source code to extract structural information such as imports, classes, and functions. It leverages the `ast.NodeVisitor` base class to walk through nodes in the AST and builds a schema representation of the code structure. This schema includes metadata like identifiers, docstrings, source segments, and line numbers for each element. The visitor also tracks the current class context when processing function definitions, allowing for hierarchical organization of method information within class contexts.
*   **Instantiation:** This class is instantiated in the 'analyze_repository' function located in 'AST_Schema.py' at line 182.
*   **Dependencies:** This class depends on the standard library modules 'ast', 'networkx', 'os', and external modules 'callgraph.build_filtered_callgraph' and 'getRepo.GitRepository'.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It sets up internal state including module path derived from the file path and project root, and initializes an empty schema dictionary to store extracted information about imports, functions, and classes.
    *   *Parameters:*
        -   **source_code** (`str`): The full source code string of the file being analyzed.
        -   **file_path** (`str`): The absolute or relative path to the Python file being processed.
        -   **project_root** (`str`): The root directory of the project, used to compute module paths.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It iterates over all aliases in the import statement and adds their names to the schema.
        *   *Parameters:*
            -   **node** (`ast.Import`): An AST node representing an import statement.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called by the AST traversal mechanism during the visit process.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* Processes import-from nodes in the AST by collecting qualified names of imported items and appending them to the schema's imports list. Each imported item is formatted as 'module.name' before being added.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing an import-from statement.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called by the AST traversal mechanism during the visit process.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* Handles class definition nodes in the AST by creating a structured representation of the class and adding it to the schema. It computes the fully qualified class identifier based on the module path and class name, extracts documentation and source code segment, and stores metadata like start and end lines. Additionally, it tracks the current class being visited to support nested method processing.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called by the AST traversal mechanism during the visit process.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: ast.FunctionDef)`
        *   *Description:* Processes function definition nodes in the AST. If a class context is active, it creates a method context entry under the current class. Otherwise, it creates a standalone function entry in the schema. In both cases, it captures argument names, docstrings, source segments, and line numbers.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called by the AST traversal mechanism during the visit process.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef)`
        *   *Description:* Handles asynchronous function definition nodes in the AST by delegating the processing to the standard `visit_FunctionDef` method. This allows async functions to be treated similarly to regular functions in terms of schema extraction.
        *   *Parameters:*
            -   **node** (`ast.AsyncFunctionDef`): An AST node representing an async function definition.
        *   *Returns:*
        *   **Usage:** This method delegates to visit_FunctionDef. This method is called by the AST traversal mechanism during the visit process.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information. It supports merging relationship data and building a comprehensive schema of files, functions, classes, and their interconnections. The class integrates with Git repositories and utilizes networkx-based call graphs to enhance semantic understanding of code structures.
*   **Instantiation:** This class is instantiated by the evaluation function in evaluation.py at line 128 and by the main_workflow function in main.py at line 187.
*   **Dependencies:** This class depends on external modules such as ast, networkx, os, callgraph.build_filtered_callgraph, and getRepo.GitRepository.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any specific initialization actions.
    *   *Parameters:*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema: dict, call_graph: networkx.DiGraph, filename: str)`
        *   *Description:* This static method enriches a given schema with call graph data by updating function and method contexts with information about what they call and who calls them. It processes both top-level functions and class methods, mapping them to entries in a provided call graph.
        *   *Parameters:*
            -   **schema** (`dict`): A dictionary representing the schema of a parsed Python file, containing functions and classes.
            -   **call_graph** (`networkx.DiGraph`): A directed graph representing the call relationships between functions and methods.
            -   **filename** (`str`): The path of the file being processed, used to construct unique keys for matching against the call graph.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other functions. This method is called by the analyze_repository method within the ASTAnalyzer class.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, relationship_data: list)`
        *   *Description:* Merges relationship data into a full schema by associating identifiers from the relationship data with corresponding nodes in the schema. Specifically, it updates function and class contexts with 'called_by' information and class contexts with 'instantiated_by' information based on a lookup table derived from the relationship data.
        *   *Parameters:*
            -   **full_schema** (`dict`): A dictionary representing the complete schema of the repository, including files and their AST nodes.
            -   **relationship_data** (`list`): A list of dictionaries containing relationship information, such as identifiers and associated 'called_by' lists.
        *   *Returns:*
            -   **full_schema** (`dict`): The updated schema with merged relationship data.
        *   **Usage:** This method does not explicitly call any other functions. This method is called by the evaluation function in evaluation.py at line 137 and by the main_workflow function in main.py at line 197.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: backend.getRepo.GitRepository)`
        *   *Description:* Analyzes a set of Python files from a Git repository by parsing their ASTs, visiting nodes with an ASTVisitor, and enriching the resulting schema with call graph information. It constructs a full schema of files, functions, and classes while handling potential parsing errors and filtering out non-Python files.
        *   *Parameters:*
            -   **files** (`list`): A list of file objects containing paths and content of Python files to be analyzed.
            -   **repo** (`backend.getRepo.GitRepository`): An object representing the Git repository from which files are analyzed.
        *   *Returns:*
            -   **full_schema** (`dict`): A dictionary representing the full schema of the analyzed repository, including file-level AST node information.
        *   **Usage:** This method calls the build_filtered_callgraph function and the ASTVisitor class, and also calls the _enrich_schema_with_callgraph method. This method is called by the evaluation function in evaluation.py at line 129 and by the main_workflow function in main.py at line 188.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: Any, project_root: Any)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases where the file path is not within the project root by falling back to the basename of the file. If the resulting path ends with '.__init__', it removes the trailing part to correctly represent the module.
*   **Parameters:**
    -   **filepath** (`str`): The absolute or relative path to the Python file.
    -   **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    -   **module_path** (`str`): A dot-separated module path derived from the input file path.
*   **Usage:** This function does not call any other functions directly. This function is called by the __init__ method in AST_Schema.py at line 31.

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze Python file dependencies by traversing AST nodes representing import statements. It resolves both absolute and relative imports, identifies module and symbol existence, and builds a dependency graph mapping files to their imported modules. The class leverages AST parsing and file system checks to determine valid import paths and maintains a dictionary of import dependencies.
*   **Instantiation:** This class is instantiated by the function 'build_file_dependency_graph' in the file 'File_Dependency.py'.
*   **Dependencies:** This class depends on networkx, os, ast, pathlib, keyword, and other utility functions from getRepo.GitRepository and callgraph.make_safe_dot.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up the instance variables to track the current file being analyzed and the root directory of the repository.
    *   *Parameters:*
        -   **filename** (`str`): The name of the file being analyzed for dependencies.
        -   **repo_root** (`Any`): The root directory path of the repository containing the file.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ast.ImportFrom)`
        *   *Description:* Resolves relative import statements by analyzing the import node and determining the actual module or symbol names that can be imported. It handles cases where imports use relative paths like '..' and checks for the existence of modules or symbols in the repository structure. The method raises an ImportError if no valid resolution can be found.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing a relative import statement.
        *   *Returns:*
            -   **resolved** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:** This method internally calls helper functions 'module_file_exists' and 'init_exports_symbol'. This method is called by 'visit_ImportFrom' when resolving relative imports.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import | ast.ImportFrom, base_name: str | None)`
        *   *Description:* Handles AST nodes representing import statements. It adds the imported module names to the import dependencies dictionary associated with the current file. This method ensures that all imports are recorded in the dependency graph.
        *   *Parameters:*
            -   **node** (`ast.Import | ast.ImportFrom`): An AST node representing an import statement.
            -   **base_name** (`str | None`): Optional base name of the imported module.
        *   *Returns:*
        *   **Usage:** This method calls 'generic_visit' to continue traversal of the AST. This method is called by 'visit_ImportFrom' and directly during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* Processes AST nodes representing 'from ... import ...' statements. It extracts the module name and either uses it directly or resolves relative imports by calling '_resolve_module_name'. It records these dependencies in the import dependencies dictionary.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method calls 'visit_Import', '_resolve_module_name', and 'generic_visit'. This method is called during AST traversal when processing 'from ... import ...' statements.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: ast.AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes an AST representation of a file and uses a custom visitor to extract import dependencies. These dependencies are then added to a NetworkX DiGraph, where nodes represent files and edges represent import relationships. The resulting graph captures the dependency structure between files.
*   **Parameters:**
    -   **filename** (`str`): The name of the file being analyzed for dependencies.
    -   **tree** (`ast.AST`): The abstract syntax tree of the file being analyzed.
    -   **repo_root** (`str`): The root directory of the repository being analyzed.
*   **Returns:**
    -   **graph** (`networkx.DiGraph`): A directed graph representing file dependencies, where nodes are files and edges indicate import relationships.
*   **Usage:** The function internally utilizes a FileDependencyGraph visitor to traverse the AST and collect import dependencies. This function is called by the 'build_repository_graph' function in the 'File_Dependency.py' file at line 177.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: backend.getRepo.GitRepository)`
*   **Description:** This function constructs a directed graph representing the dependencies between Python files within a Git repository. It iterates through all files in the repository, filters for Python files, parses their content into ASTs, and builds individual file dependency graphs. These individual graphs are then merged into a single global graph that captures the overall dependency structure. The function uses NetworkX to manage the graph structure and ensures nodes and edges are properly added to represent the relationships.
*   **Parameters:**
    -   **repository** (`backend.getRepo.GitRepository`): The GitRepository object containing the files to analyze for dependencies.
*   **Returns:**
    -   **global_graph** (`networkx.DiGraph`): A NetworkX directed graph representing the dependency relationships between Python files in the repository.
*   **Usage:** This function internally utilizes several AST parsing and graph-building functions including parse(), build_file_dependency_graph(), and various NetworkX methods such as DiGraph(), add_node(), and add_edge(). This function is called by the module backend.File_Dependency at line 200 in File_Dependency.py.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function retrieves all Python files (.py) from a specified directory and its subdirectories. It resolves the given directory path to an absolute path, then uses recursive globbing to find all .py files. Each found file is converted to a relative path with respect to the root directory. The function returns a list of these relative paths as pathlib.Path objects.
*   **Parameters:**
    -   **directory** (`str`): The directory path from which to search for Python files.
*   **Returns:**
    -   **all_files** (`list[pathlib.Path]`): A list of pathlib.Path objects representing the relative paths of all Python files found in the directory and its subdirectories.
*   **Usage:** This function does not call any other functions directly. This function is called by _resolve_module_name in File_Dependency.py at line 43.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a centralized interface for interacting with various language models, including Google Gemini, OpenAI, custom APIs, and Ollama. It handles API configuration, prompt loading, batching logic, and structured output validation using Pydantic models. The class supports generating documentation for both functions and classes by processing inputs in batches while respecting rate limits.
*   **Instantiation:** The LLMHelper class is instantiated in HelperLLM.py at line 387 in the main_orchestrator function, in evaluation.py at line 222 in the evaluation function, and in main.py at line 284 in the main_workflow function.
*   **Dependencies:** No external dependencies were explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API credentials, prompt files, and model configuration. It loads system prompts from specified files, configures batch settings based on the model name, and sets up appropriate language model clients depending on the model type. It also prepares structured output validators for function and class analysis.
    *   *Parameters:*
        -   **api_key** (`str`): API key for accessing the language model service.
        -   **function_prompt_path** (`str`): Path to the file containing the system prompt for function documentation generation.
        -   **class_prompt_path** (`str`): Path to the file containing the system prompt for class documentation generation.
        -   **model_name** (`str`): Name of the language model to use. Defaults to 'gemini-2.0-flash-lite'.
        -   **base_url** (`Optional[str]`): Base URL for custom API endpoints. Optional.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing inputs based on the specified model name. Different models have different recommended or supported batch sizes, which are set accordingly. If the model name is unknown, a default conservative batch size is applied.
        *   *Parameters:*
            -   **model_name** (`str`): The name of the language model being used.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called during initialization of the LLMHelper class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: typing.List[schemas.types.FunctionAnalysisInput])`
        *   *Description:* Processes a batch of function inputs to generate validated documentation using the configured language model. It divides the input into chunks according to the configured batch size, sends each chunk to the LLM, and collects results. In case of errors, it fills the result list with None values to maintain order.
        *   *Parameters:*
            -   **function_inputs** (`List[FunctionAnalysisInput]`): A list of inputs representing functions to document.
        *   *Returns:*
            -   **result** (`List[Optional[FunctionAnalysis]]`): A list of validated function analysis outputs or None for failed items.
        *   **Usage:** This method does not explicitly call other functions within its body. Called by evaluation() in evaluation.py at line 245 and main_workflow() in main.py at line 309.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: typing.List[schemas.types.ClassAnalysisInput])`
        *   *Description:* Processes a batch of class inputs to generate validated documentation using the configured language model. Similar to generate_for_functions, it splits inputs into batches, sends them to the LLM, and collects results. Errors result in None entries to preserve item ordering.
        *   *Parameters:*
            -   **class_inputs** (`List[ClassAnalysisInput]`): A list of inputs representing classes to document.
        *   *Returns:*
            -   **result** (`List[Optional[ClassAnalysis]]`): A list of validated class analysis outputs or None for failed items.
        *   **Usage:** This method does not explicitly call other functions within its body. Called by evaluation() in evaluation.py at line 271 and main_workflow() in main.py at line 340.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analysis for several example functions including 'add_item', 'check_stock', and 'generate_report'. It also constructs a ClassAnalysisInput for an 'InventoryManager' class, which includes these methods. The function simulates the workflow of generating documentation for both functions and classes using an LLMHelper instance.
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function does not call any other user-defined functions directly; it primarily orchestrates the setup and execution of the LLMHelper for documentation generation. This function is called by the backend.HelperLLM module, specifically at line 419 of HelperLLM.py.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the central interface for interacting with various language learning models (LLMs), supporting multiple backends including Google Generative AI, OpenAI-compatible APIs, and Ollama. It initializes with an API key, a system prompt file path, and a model name, dynamically selecting the appropriate LLM client based on the model specification. The class provides two core functionalities: synchronous invocation of the LLM via the 'call_llm' method and streaming responses via the 'stream_llm' method.
*   **Instantiation:** The class is instantiated by the main_workflow function in main.py at line 398.
*   **Dependencies:** This class depends on several LangChain components including ChatGoogleGenerativeAI, ChatOllama, ChatOpenAI, HumanMessage, and SystemMessage, as well as standard libraries like os, logging, and dotenv.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading the system prompt from a specified file, and setting up the appropriate LLM client based on the model name. It supports different LLM backends such as Google Generative AI, custom OpenAI-compatible APIs, and Ollama.
    *   *Parameters:*
        -   **api_key** (`str`): The API key used for authenticating with the LLM service.
        -   **prompt_file_path** (`str`): The file path to the system prompt used for initializing the LLM.
        -   **model_name** (`str`): The name of the model to use, which determines the backend client to instantiate. Defaults to 'gemini-2.5-pro'.
        -   **base_url** (`str`): Optional base URL for custom LLM endpoints. Used when the model is not recognized as a standard Google or Ollama model.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* Invokes the configured LLM synchronously with a user input message, prepending the system prompt to the conversation. It handles potential exceptions during the LLM call and logs both success and failure events.
        *   *Parameters:*
            -   **user_input** (`str`): The input message from the user to be sent to the LLM.
        *   *Returns:*
            -   **response_content** (`str`): The content of the LLM's response if the call is successful, otherwise None.
        *   **Usage:** No internal method calls. Called by the main_workflow function in main.py at line 417.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* Streams the response from the configured LLM in real-time for a given user input message. It yields content chunks as they become available, handling errors gracefully by yielding an error message upon failure.
        *   *Parameters:*
            -   **user_input** (`str`): The input message from the user to be sent to the LLM for streaming.
        *   *Returns:*
            -   **chunk_content** (`str`): Yields content chunks from the LLM's streaming response.
        *   **Usage:** No internal method calls. Not called by any other function or method.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract basic project information from common project files such as README.md, pyproject.toml, and requirements.txt. It maintains an internal dictionary structure to store extracted information under categories like 'projekt_uebersicht' (project overview) and 'installation'. The extraction process prioritizes pyproject.toml for metadata, falls back to requirements.txt for dependencies, and uses README for descriptive content. The class also handles formatting of dependency lists and sets the project title based on the repository URL.
*   **Instantiation:** This class is instantiated in the evaluation function in evaluation.py at line 104 and in the main_workflow function in main.py at line 160.
*   **Dependencies:** No external dependencies are explicitly listed in the provided context.
*   **Constructor:**
    *   *Description:* Initializes the ProjektInfoExtractor with a predefined structure for storing project information. It sets up placeholder values for various fields in 'projekt_uebersicht' and 'installation', including title, description, status, features, tech stack, dependencies, setup instructions, and quick start guides.
    *   *Parameters:*
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: typing.List[str], dateien: typing.List[typing.Any])`
        *   *Description:* This private method searches for a file among a list of files that matches any of the given patterns, ignoring case. It iterates through the list of files and checks if the file path ends with one of the specified patterns. If a match is found, it returns the matching file object; otherwise, it returns None.
        *   *Parameters:*
            -   **patterns** (`List[str]`): A list of file extension patterns to search for.
            -   **dateien** (`List[Any]`): A list of file objects to search through.
        *   *Returns:*
            -   **result** (`Optional[Any]`): The first matching file object or None if no match is found.
        *   **Usage:** This method does not call any other functions. This method is not called by any other methods in the provided context.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: typing.List[str])`
        *   *Description:* This private method extracts text sections from a markdown document that follow a specific heading pattern (##). It uses regular expressions to find the section associated with any of the provided keywords and returns the content between that heading and the next heading or end of the document. This is useful for extracting specific parts of documentation like installation instructions or feature descriptions.
        *   *Parameters:*
            -   **inhalt** (`str`): The full markdown text to parse.
            -   **keywords** (`List[str]`): A list of alternative keywords to look for as headings.
        *   *Returns:*
            -   **extracted_text** (`Optional[str]`): The extracted text section or None if no matching section is found.
        *   **Usage:** This method does not call any other functions. This method is not called by any other methods in the provided context.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This private method parses the content of a README file to extract various pieces of information such as the project title, description, key features, technology stack, current status, setup instructions, and quick start guide. It uses regex patterns to locate these elements and stores them in the internal info dictionary, only updating fields that haven't been previously set.
        *   *Parameters:*
            -   **inhalt** (`str`): The content of the README file to parse.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions. This method is not called by any other methods in the provided context.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project metadata such as name, description, and dependencies. It uses the tomllib library to load the TOML content and updates the internal info dictionary accordingly. If tomllib is not available, it prints a warning message. It also handles potential parsing errors gracefully.
        *   *Parameters:*
            -   **inhalt** (`str`): The content of the pyproject.toml file to parse.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions. This method is not called by any other methods in the provided context.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This private method parses the content of a requirements.txt file to extract dependency information. It filters out comments and empty lines, then stores the resulting list in the internal info dictionary only if dependencies have not already been set from a pyproject.toml file. This ensures that pyproject.toml takes precedence over requirements.txt.
        *   *Parameters:*
            -   **inhalt** (`str`): The content of the requirements.txt file to parse.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions. This method is not called by any other methods in the provided context.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: typing.List[typing.Any], repo_url: str)`
        *   *Description:* This public method orchestrates the extraction of project information from a list of file objects. It finds relevant files (README, pyproject.toml, requirements.txt) using the _finde_datei helper, processes them in order of priority (_parse_toml, _parse_requirements, _parse_readme), formats the dependencies list, and finally sets the project title based on the repository URL. It returns the complete info dictionary after processing.
        *   *Parameters:*
            -   **dateien** (`List[Any]`): A list of file objects to extract information from.
            -   **repo_url** (`str`): The URL of the repository to derive the project title from.
        *   *Returns:*
            -   **info** (`Dict[str, Any]`): A dictionary containing the extracted project information.
        *   **Usage:** This method calls the helper methods _finde_datei, _parse_toml, _parse_requirements, and _parse_readme. This method is called by the evaluation function in evaluation.py and the main_workflow function in main.py.

### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is a specialized AST visitor designed to construct a call graph from Python source code. It traverses the abstract syntax tree of a file, tracking function and class definitions, imports, and function calls to build a directed graph representing the relationships between different callable entities. The class maintains internal state such as current function and class context, local definitions, and import mappings to resolve names correctly within the scope of the visited code.
*   **Instantiation:** This class is instantiated by the build_filtered_callgraph function in callgraph.py at lines 199 and 206.
*   **Dependencies:** This class depends on the ast module for parsing Python code and networkx for graph operations.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph with a filename and sets up internal data structures including dictionaries and sets to track local definitions, the call graph itself, import mappings, and function names. It also initializes tracking variables for the current function and class being processed during AST traversal.
    *   *Parameters:*
        -   **filename** (`str`): The name of the file being analyzed for call graph construction.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node: Any)`
        *   *Description:* Recursively extracts the dotted name components from an AST node representing a function or attribute access. It handles various node types like ast.Call, ast.Name, and ast.Attribute to build a list of name parts that can later be joined into a dotted string representation.
        *   *Parameters:*
            -   **node** (`ast.AST`): An AST node representing a function or attribute access.
        *   *Returns:*
            -   **parts** (`list[str]`): A list of strings representing the dotted name components.
        *   **Usage:** This method does not call any other methods. This method is called by the _resolve_all_callee_names method.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* Resolves a list of dotted name components into fully qualified names based on local definitions, import mappings, and current class context. It checks for local definitions first, then import mappings, and finally constructs a full name using the file path and class/function context.
        *   *Parameters:*
            -   **callee_nodes** (`list[list[str]]`): A list of lists containing name components for potential callees.
        *   *Returns:*
            -   **resolved** (`list[str]`): A list of fully qualified names for the callees.
        *   **Usage:** This method calls the _recursive_call method to extract name components. This method is called by the visit_Call method.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None)`
        *   *Description:* Constructs a fully qualified name for a given base name, optionally including a class name. This is used to create unique identifiers for functions and methods within the context of a file and potentially a class.
        *   *Parameters:*
            -   **basename** (`str`): The base name of the entity (e.g., function or method name).
            -   **class_name** (`Optional[str]`): The optional class name to include in the fully qualified name.
        *   *Returns:*
            -   **full_name** (`str`): A fully qualified name constructed from the filename, class name (if provided), and basename.
        *   **Usage:** This method does not call any other methods. This method is called by the visit_FunctionDef method.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* Determines the current caller's name based on whether a function is currently being visited. If a function is active, it returns the function name; otherwise, it returns a placeholder indicating global scope or the filename.
        *   *Parameters:*
        *   *Returns:*
            -   **caller** (`str`): The name of the current caller or a placeholder if no function is active.
        *   **Usage:** This method does not call any other methods. This method is called by the visit_Call method.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Any)`
        *   *Description:* Handles import statements in the AST by mapping aliases to their actual module names. It updates the import mapping dictionary which is later used to resolve imported names when building the call graph.
        *   *Parameters:*
            -   **node** (`ast.Import`): An AST node representing an import statement.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal. This method is called by the AST traversal mechanism.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: Any)`
        *   *Description:* Handles 'from ... import ...' statements by extracting the module name and mapping aliases to their respective modules. This helps in resolving names that are imported from other modules.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal. This method is called by the AST traversal mechanism.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* Processes class definitions in the AST by temporarily setting the current class context before visiting the class body. After processing, it restores the previous class context to maintain proper scoping during traversal.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal. This method is called by the AST traversal mechanism.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: Any)`
        *   *Description:* Handles function definitions by creating a fully qualified name for the function, updating local definitions, adding the function to the graph, and setting the current function context. It ensures that both direct and class-scoped function names are tracked.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
        *   **Usage:** This method calls _make_full_name to construct the function name and generic_visit to continue traversal. This method is called by the AST traversal mechanism.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: Any)`
        *   *Description:* Handles asynchronous function definitions by delegating to the standard function definition handler. This allows async functions to be treated similarly to regular functions in the call graph.
        *   *Parameters:*
            -   **node** (`ast.AsyncFunctionDef`): An AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** This method calls visit_FunctionDef to handle the function definition. This method is called by the AST traversal mechanism.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: Any)`
        *   *Description:* Processes function calls in the AST by identifying the caller and resolving the callee names. It adds edges to the call graph based on the resolved names, capturing the relationships between callers and callees.
        *   *Parameters:*
            -   **node** (`ast.Call`): An AST node representing a function call.
        *   *Returns:*
        *   **Usage:** This method calls _current_caller to determine the caller and _resolve_all_callee_names to resolve callee names, and generic_visit to continue traversal. This method is called by the AST traversal mechanism.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node: Any)`
        *   *Description:* Handles conditional statements in the AST, specifically looking for conditions related to '__name__ == '__main__' to treat the main block specially. It temporarily changes the current function context to '<main_block>' while processing the condition's body.
        *   *Parameters:*
            -   **node** (`ast.If`): An AST node representing an if statement.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal. This method is called by the AST traversal mechanism.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: networkx.DiGraph, out_path: str)`
*   **Description:** The function 'make_safe_dot' takes a NetworkX directed graph and a file path as inputs. It creates a copy of the graph and generates a safe node naming scheme by replacing original node names with 'n0', 'n1', etc. It then relabels the nodes in the copied graph with these safe names and assigns the original node names as labels to the new nodes. Finally, it writes the modified graph to a DOT file at the specified output path.
*   **Parameters:**
    -   **graph** (`networkx.DiGraph`): A NetworkX directed graph object to be processed and saved as a DOT file.
    -   **out_path** (`str`): The file path where the DOT representation of the graph will be written.
*   **Returns:**
*   **Usage:** This function does not directly call any other functions from the provided source code. This function is called by 'backend.callgraph' in the file 'callgraph.py' at line 244.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: backend.getRepo.GitRepository)`
*   **Description:** Die Funktion erstellt einen globalen Call-Graphen basierend auf allen Python-Dateien eines Git-Repositories und filtert diesen anschließend auf Funktionen, die vom Benutzer selbst geschrieben wurden. Sie durchläuft alle Dateien, parst deren Inhalt mit dem Abstract Syntax Tree (AST), extrahiert Funktionsaufrufe und baut einen gerichteten Graphen auf, wobei nur Kanten zwischen eigenen Funktionen erhalten bleiben.
*   **Parameters:**
    -   **repo** (`backend.getRepo.GitRepository`): Ein Objekt, das Informationen über ein Git-Repository enthält, insbesondere Zugriff auf alle enthaltenen Dateien.
*   **Returns:**
    -   **global_graph** (`networkx.DiGraph`): Ein gerichteter Graph, der die Aufrufbeziehungen zwischen Funktionen darstellt, wobei nur Funktionen berücksichtigt werden, die vom Benutzer geschrieben wurden.
*   **Usage:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes direkt auf. Diese Funktion wird von 'analyze_repository' in der Datei 'AST_Schema.py' auf Zeile 167 und von 'backend.callgraph' in der Datei 'callgraph.py' auf Zeile 243 aufgerufen.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It implements lazy loading for file metadata such as content and size to optimize performance by only loading data when necessary. The class provides properties to access these lazy-loaded attributes and includes utility methods for basic file analysis and serialization.
*   **Instantiation:** This class is instantiated by the get_all_files method in the getRepo.py file.
*   **Dependencies:** This class depends on external modules such as git.Repo, git.GitCommandError, logging, and os.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object with a file path and a commit tree. Sets up internal attributes for lazy loading including blob, content, and size.
    *   *Parameters:*
        -   **file_path** (`str`): The path to the file within the repository.
        -   **commit_tree** (`git.Tree`): The tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* A property that lazily loads and returns the Git Blob object associated with the file. If the blob hasn't been loaded yet, it retrieves it from the commit tree using the stored file path. Raises a FileNotFoundError if the file cannot be found in the commit tree.
        *   *Parameters:*
        *   *Returns:*
            -   **blob** (`git.Blob`): The Git Blob object representing the file.
        *   **Usage:** This method does not call any other functions or methods. This method is not called by any other functions or methods according to the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* A property that lazily loads and returns the decoded content of the file. If the content hasn't been loaded yet, it reads the data stream from the blob and decodes it to UTF-8, ignoring encoding errors. Returns the decoded string content.
        *   *Parameters:*
        *   *Returns:*
            -   **content** (`str`): The decoded content of the file.
        *   **Usage:** This method does not call any other functions or methods. This method is not called by any other functions or methods according to the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* A property that lazily loads and returns the size of the file in bytes. If the size hasn't been determined yet, it retrieves the size from the blob object. Returns the integer size of the file.
        *   *Parameters:*
        *   *Returns:*
            -   **size** (`int`): The size of the file in bytes.
        *   **Usage:** This method does not call any other functions or methods. This method is not called by any other functions or methods according to the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* An example analysis method that counts the number of words in the file's content. It uses the content property to retrieve the file's text and splits it by whitespace to count the words.
        *   *Parameters:*
        *   *Returns:*
            -   **word_count** (`int`): The total number of words in the file's content.
        *   **Usage:** This method does not call any other functions or methods. This method is not called by any other functions or methods according to the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* Provides a useful string representation of the RepoFile object, showing the file path for debugging and logging purposes.
        *   *Parameters:*
        *   *Returns:*
            -   **repr_string** (`str`): A string representation of the RepoFile object including the file path.
        *   **Usage:** This method does not call any other functions or methods. This method is not called by any other functions or methods according to the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content: Any)`
        *   *Description:* Converts the RepoFile object into a dictionary format. Includes basic file information like path, name, size, and type. Optionally includes the file content if specified by the include_content flag.
        *   *Parameters:*
            -   **include_content** (`bool`): Flag indicating whether to include the file content in the returned dictionary.
        *   *Returns:*
            -   **data** (`dict`): A dictionary containing file metadata and optionally the file content.
        *   **Usage:** This method does not call any other functions or methods. This method is not called by any other functions or methods according to the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory and providing functionality to retrieve files and construct a hierarchical file tree. It supports initialization with a repository URL, cloning the repository, listing all files as RepoFile objects, and cleaning up the temporary directory upon closing. The class also implements context manager protocols (__enter__ and __exit__) to facilitate automatic resource management.
*   **Instantiation:** The GitRepository class is instantiated in the evaluation.py file within the evaluation function at line 86, and in main.py within the main_workflow function at line 141.
*   **Dependencies:** This class depends on the 'tempfile', 'shutil', 'git.Repo', 'git.GitCommandError', 'logging', and 'os' modules.
*   **Constructor:**
    *   *Description:* Initializes a GitRepository instance by setting up a temporary directory and cloning the specified Git repository. It also retrieves metadata about the latest commit and its file tree.
    *   *Parameters:*
        -   **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* Retrieves a list of all files in the cloned repository and creates RepoFile objects for each file. These objects are stored in the instance's 'files' attribute and returned.
        *   *Parameters:*
            -   **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            -   **files** (`list[RepoFile]`): A list of RepoFile instances representing the files in the repository.
        *   **Usage:** This method does not call any other methods internally. This method is not called by any other methods according to the provided context.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* Deletes the temporary directory used for cloning the repository and cleans up associated resources.
        *   *Parameters:*
            -   **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
        *   **Usage:** This method does not call any other methods internally. This method is not called by any other methods according to the provided context.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* Enables the use of the GitRepository instance in a 'with' statement, returning the instance itself for use within the context block.
        *   *Parameters:*
            -   **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            -   **""** (`GitRepository`): The GitRepository instance itself.
        *   **Usage:** This method does not call any other methods internally. This method is not called by any other methods according to the provided context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any)`
        *   *Description:* Automatically closes the GitRepository instance when exiting a 'with' statement context, ensuring cleanup of temporary resources.
        *   *Parameters:*
            -   **self** (`GitRepository`): The instance of the GitRepository class.
            -   **exc_type** (`Any`): Exception type if an exception occurred in the context block.
            -   **exc_val** (`Any`): Exception value if an exception occurred in the context block.
            -   **exc_tb** (`Any`): Exception traceback if an exception occurred in the context block.
        *   *Returns:*
        *   **Usage:** This method calls the close() method to clean up resources. This method is not called by any other methods according to the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content: Any)`
        *   *Description:* Constructs a hierarchical representation of the repository's file structure. If no files have been retrieved yet, it first calls get_all_files to populate the internal list of files. Then, it builds a nested dictionary structure representing directories and files.
        *   *Parameters:*
            -   **self** (`GitRepository`): The instance of the GitRepository class.
            -   **include_content** (`bool`): Flag indicating whether to include file content in the returned dictionary structure.
        *   *Returns:*
            -   **tree** (`dict`): A nested dictionary structure representing the file tree of the repository.
        *   **Usage:** This method calls get_all_files if the files list is empty. This method is not called by any other methods according to the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: Any, toon_tokens: Any, savings_percent: Any, output_path: Any)`
*   **Description:** Die Funktion erstellt ein Balkendiagramm zur Visualisierung des Token-Vergleichs zwischen JSON und TOON-Formaten und speichert das Diagramm in einer Datei. Sie verwendet matplotlib zur Erstellung des Diagramms und zeigt die Anzahl der Tokens sowie den Prozentsatz der Einsparung im Titel an. Die Funktion nimmt die Token-Anzahlen für beide Formate, einen Prozentwert für die Einsparung und einen Ausgabepfad entgegen.
*   **Parameters:**
    -   **json_tokens** (`int`): Die Anzahl der Tokens im JSON-Format.
    -   **toon_tokens** (`int`): Die Anzahl der Tokens im TOON-Format.
    -   **savings_percent** (`float`): Der Prozentsatz der Einsparung zwischen den beiden Formaten.
    -   **output_path** (`str`): Der Dateipfad, unter dem das generierte Diagramm gespeichert wird.
*   **Returns:**
*   **Usage:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf. Die Funktion wird von der Funktion 'main_workflow' in der Datei 'main.py' aufgerufen.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: Any, end_time: Any, total_items: Any, batch_size: Any, model_name: Any)`
*   **Description:** The function calculates the net time duration between a start and end time, excluding sleep times that occur due to rate limits when using specific models. It first computes the total duration and then adjusts it based on whether the model name starts with 'gemini-'. If it does, it further adjusts the duration by subtracting the total sleep time caused by batching items according to a given batch size.
*   **Parameters:**
    -   **start_time** (`float or datetime`): The starting timestamp or time value.
    -   **end_time** (`float or datetime`): The ending timestamp or time value.
    -   **total_items** (`int`): The total number of items processed.
    -   **batch_size** (`int`): The number of items per batch.
    -   **model_name** (`str`): The name of the model being used, which determines if rate limit adjustments are applied.
*   **Returns:**
    -   **net_time** (`float or int`): The adjusted time duration after subtracting sleep time, ensuring it is not negative.
*   **Usage:** This function does not call any other functions directly. This function is called by the evaluation function in evaluation.py at lines 249 and 275, and by the main_workflow function in main.py at lines 311 and 342.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: Any, api_keys: dict, model_names: dict, status_callback: Any)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive code analysis and documentation generation process for a given GitHub repository. It begins by extracting API keys and model names, then clones the repository and analyzes its structure. The function proceeds to extract basic project information, construct a file tree, and perform relationship analysis on the codebase. It generates an abstract syntax tree (AST) schema and enriches it with relationship data. Subsequently, it prepares inputs for a helper LLM to analyze functions and classes, and then calls the helper LLM to generate documentation. Finally, it prepares inputs for a main LLM to generate a final report, saves the report and associated statistics, and returns the generated report along with timing metrics.
*   **Parameters:**
    -   **input** (`Any`): The input provided to the workflow, typically a string containing a GitHub repository URL.
    -   **api_keys** (`dict`): A dictionary containing API keys for various services such as Gemini, OpenAI, and SCADsLLM.
    -   **model_names** (`dict`): A dictionary specifying the names of models to be used for the helper and main LLMs.
    -   **status_callback** (`Callable[[str], None] | None`): An optional callback function to report progress updates during execution.
*   **Returns:**
    -   **report** (`str`): The final markdown report generated by the main LLM.
    -   **metrics** (`dict`): A dictionary containing timing metrics for the helper and main LLM processes.
*   **Usage:** This function internally calls several components including GitRepository for cloning repositories, ProjektInfoExtractor for extracting basic project information, ProjectAnalyzer for analyzing relationships, ASTAnalyzer for generating AST schemas, LLMHelper for function and class analysis, and MainLLM for generating the final report. This function is called by the frontend.Frontend function in Frontend.py at line 489 and by backend.main in main.py at line 533.

#### Function: `update_status`
*   **Signature:** `def update_status(msg: Any)`
*   **Description:** The function 'update_status' is designed to handle status updates by invoking an optional callback function if one is defined, followed by logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages throughout the application.
*   **Parameters:**
    -   **msg** (`Any`): A message to be logged and optionally passed to a status callback function.
*   **Returns:**
*   **Usage:** This function internally calls the 'status_callback' function if it is defined, and also logs the message using 'logging.info'. This function is called by 'main_workflow' in 'main.py' at multiple locations across lines 81, 134, 158, 167, 175, 185, 195, 205, 301, 333, 336, 409, 412, and 430.

### File: `backend/relationship_analyzer.py`

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is responsible for analyzing Python project structures by identifying definitions (functions, classes, methods) and tracking their call relationships across files. It walks through the project directory, parses Python files into Abstract Syntax Trees (ASTs), collects definitions with their metadata, and resolves inter-file call relationships. The analyzer filters out common ignored directories like .git, venv, and __pycache__, and provides formatted results showing which definitions are called by which other definitions along with their locations.
*   **Instantiation:** This class is instantiated by the functions 'evaluation' in 'evaluation.py' at line 119 and 'main_workflow' in 'main.py' at line 177.
*   **Dependencies:** This class does not depend on any external libraries beyond standard Python modules (ast, os, logging, collections.defaultdict).
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including a dictionary for storing definitions, a call graph for tracking relationships, and a mapping of file paths to ASTs. It also defines a set of directories to ignore during traversal.
    *   *Parameters:*
        -   **project_root** (`str`): The root directory path of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* The main analysis method that orchestrates the process of finding Python files, collecting definitions from those files, resolving call relationships, and formatting the final output. It clears the cached ASTs after processing and returns the formatted results.
        *   *Parameters:*
        *   *Returns:*
            -   **return_value** (`list`): A list of dictionaries containing information about definitions and their callers.
        *   **Usage:** This method does not explicitly call any other methods defined in the class directly; however, it indirectly invokes several helper methods such as `_find_py_files`, `_collect_definitions`, and `_resolve_calls`. This method is called by the functions 'evaluation' in 'evaluation.py' at line 120 and 'main_workflow' in 'main.py' at line 178.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* Traverses the project root directory recursively to find all Python (.py) files, excluding certain directories specified in the ignore list. It uses os.walk to walk through directories and filters out unwanted ones before collecting file paths.
        *   *Parameters:*
        *   *Returns:*
            -   **py_files** (`list`): A list of absolute paths to Python files found in the project.
        *   **Usage:** This method does not call any other methods defined in the class. This method is called by the 'analyze' method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath: Any)`
        *   *Description:* Parses a given Python file into an AST and extracts definitions such as functions, classes, and methods. It associates these definitions with their respective modules and stores metadata including file location and definition type. Errors during parsing are logged but do not halt execution.
        *   *Parameters:*
            -   **filepath** (`str`): The absolute path to the Python file to analyze.
        *   *Returns:*
        *   **Usage:** This method does not call any other methods defined in the class. This method is called by the 'analyze' method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree: Any, node: Any)`
        *   *Description:* Given an AST node and a tree, this method attempts to find the parent node of the given node by walking the AST. It is used to determine whether a function or method is defined inside a class.
        *   *Parameters:*
            -   **tree** (`ast.AST`): The AST tree to search within.
            -   **node** (`ast.AST`): The AST node whose parent needs to be found.
        *   *Returns:*
            -   **parent** (`ast.AST or None`): The parent AST node of the given node, or None if not found.
        *   **Usage:** This method does not call any other methods defined in the class. This method is called by the '_collect_definitions' method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath: Any)`
        *   *Description:* Resolves inter-file call relationships by visiting the AST of a given file using a CallResolverVisitor. It updates the call graph with information about who calls whom, based on the resolved calls. Errors during resolution are logged.
        *   *Parameters:*
            -   **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   **Usage:** This method calls the 'CallResolverVisitor' class to resolve calls in the AST. This method is called by the 'analyze' method.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* Formats the collected call graph and definition information into a structured list of dictionaries. Each dictionary represents a definition and includes details about its origin, type, and the list of callers. Duplicate entries are removed to ensure uniqueness.
        *   *Parameters:*
        *   *Returns:*
            -   **output_list** (`list`): A list of dictionaries representing definitions and their callers with associated metadata.
        *   **Usage:** This method does not call any other methods defined in the class. This method is called by the 'analyze' method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to analyze Python code and resolve call relationships between functions, methods, and modules. It tracks the current execution context (such as class and function names) while traversing the AST to record which functions are called by which other functions or methods. Additionally, it maintains scope information for imports and handles assignment of instance types to track method calls on objects. This class plays a crucial role in static analysis for mapping call graphs and resolving qualified names.
*   **Instantiation:** This class is instantiated in the function `_resolve_calls` located in the file `relationship_analyzer.py` at line 92.
*   **Dependencies:** No external dependencies are specified in the context.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and a set of definitions. It sets up internal tracking structures such as scope, instance types, and call records, and determines the module path based on the file path and project root.
    *   *Parameters:*
        -   **filepath** (`str`): The absolute path to the Python file being analyzed.
        -   **project_root** (`str`): The root directory of the project, used to compute relative module paths.
        -   **definitions** (`dict`): A dictionary of known definitions (functions, classes, etc.) to resolve qualified names against.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: Any)`
        *   *Description:* Handles the traversal of class definitions in the AST. It updates the current class name during traversal and restores the previous class name after visiting the class body. This ensures proper scoping when analyzing nested classes.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is invoked by the generic AST visitor during traversal of class definitions.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: Any)`
        *   *Description:* Processes function definitions in the AST. It temporarily updates the current caller name to the function name and restores it after processing the function body. This allows accurate tracking of which function is making calls.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is invoked by the generic AST visitor during traversal of function definitions.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: Any)`
        *   *Description:* Analyzes function calls in the AST. It resolves the qualified name of the called function and checks if it exists in the definitions. If so, it records the call along with metadata about the caller, including the file, line number, and caller type (module, method, or function).
        *   *Parameters:*
            -   **node** (`ast.Call`): The AST node representing the function call.
        *   *Returns:*
        *   **Usage:** This method calls the helper method `_resolve_call_qname` to determine the qualified name of the function being called. This method is invoked by the generic AST visitor during traversal of function calls.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Any)`
        *   *Description:* Handles import statements in the AST. It adds imported names to the current scope, mapping aliases to their actual names. This helps in resolving qualified names later during call resolution.
        *   *Parameters:*
            -   **node** (`ast.Import`): The AST node representing the import statement.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is invoked by the generic AST visitor during traversal of import statements.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: Any)`
        *   *Description:* Processes 'from ... import ...' statements in the AST. It correctly resolves the module path for relative imports and maps imported names to their fully qualified paths in the scope. This supports accurate name resolution across modules.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is invoked by the generic AST visitor during traversal of 'from ... import ...' statements.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node: Any)`
        *   *Description:* Handles assignment statements in the AST. Specifically, it looks for assignments where the right-hand side is a call to a class constructor. It maps the assigned variable to the qualified class name, enabling tracking of instance types for method resolution.
        *   *Parameters:*
            -   **node** (`ast.Assign`): The AST node representing the assignment statement.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is invoked by the generic AST visitor during traversal of assignment statements.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node: Any)`
        *   *Description:* Resolves the qualified name of a function call based on the AST node representing the function. It handles both direct function names and attribute access (like obj.method). It checks the current scope and local module path to find the fully qualified name.
        *   *Parameters:*
            -   **func_node** (`ast.AST`): The AST node representing the function being called.
        *   *Returns:*
            -   **qualified_name** (`str or None`): The fully qualified name of the function, or None if it cannot be resolved.
        *   **Usage:** This method is called by the `visit_Call` method to resolve the qualified name of a function call. This method is invoked by the `visit_Call` method during AST traversal.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: Any, project_root: Any)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles cases where the filepath is not under the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure.
*   **Parameters:**
    -   **filepath** (`str`): The absolute or relative path to a Python file.
    -   **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    -   **module_path** (`str`): A dot-separated module path derived from the given file path.
*   **Usage:** This function does not call any other functions directly. This function is called by _collect_definitions and __init__ methods in relationship_analyzer.py.

### File: `backend/scads_key_test.py`

*Analysis data not available for this component.*

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** The function encrypts a given text string using a Fernet cipher suite. It first checks if the input text is empty or if the cipher suite is not available, returning the original text in such cases. If both conditions are met, it strips whitespace from the input text, encodes it to bytes, encrypts it using the cipher suite, and then decodes the result back to a string for return.
*   **Parameters:**
    -   **text** (`str`): The text string to be encrypted.
*   **Returns:**
    -   **encrypted_text** (`str`): The encrypted version of the input text, or the original text if encryption was not performed.
*   **Usage:** This function does not call any other functions directly. This function is called by the update_gemini_key function in the db.py file.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** The function decrypts a given text using a cipher suite if available; otherwise, it returns the original text. It handles potential decryption errors gracefully by returning the original text in case of exceptions. The function ensures that the input text is stripped of leading/trailing whitespace before attempting decryption.
*   **Parameters:**
    -   **text** (`str`): The encrypted text to be decrypted.
*   **Returns:**
    -   **result** (`str`): The decrypted text if successful, otherwise the original input text.
*   **Usage:** This function does not call any other functions directly. This function is called by get_decrypted_api_keys in db.py at line 93.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** The function inserts a new user into the database by creating a user document with the provided username, name, and password. It hashes the password using a hasher utility before storing the user information. The function also initializes additional fields such as API keys and returns the ID of the inserted document.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user, used as the '_id' field in the database.
    -   **name** (`str`): The full name of the user to be stored in the database.
    -   **password** (`str`): The plain text password of the user, which is hashed before storage.
*   **Returns:**
    -   **inserted_id** (`ObjectId`): The unique identifier generated by the database for the newly inserted user document.
*   **Usage:** This function does not call any other functions directly. This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 294.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user documents from a MongoDB collection named 'dbusers'. It performs a database query to find all records in the collection and returns them as a list. The function does not take any parameters and directly accesses the global 'dbusers' variable, which is expected to be initialized elsewhere in the codebase.
*   **Parameters:**
*   **Returns:**
    -   **result** (`list`): A list containing all user documents retrieved from the 'dbusers' collection in the database.
*   **Usage:** The function does not call any other functions directly. This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 244.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** This function retrieves a user document from a MongoDB collection based on the provided username. It uses the 'find_one' method to query the database with a filter matching the '_id' field to the given username. The function assumes the existence of a global variable 'dbusers' that represents a MongoDB collection.
*   **Parameters:**
    -   **username** (`str`): The unique identifier (username) used to locate the specific user document in the database.
*   **Returns:**
    -   **result** (`Any`): The user document retrieved from the database if found; otherwise, None or an empty result depending on the behavior of find_one.
*   **Usage:** The function internally calls the 'find_one' method on the 'dbusers' collection to perform the database lookup. This function is not called by any other functions within the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the name field of a user in the database identified by their username. It uses MongoDB's update_one method to modify only the name field, leaving other fields unchanged. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    -   **username** (`str`): The unique identifier of the user whose name needs to be updated.
    -   **new_name** (`str`): The new name value to set for the specified user.
*   **Returns:**
    -   **result.modified_count** (`int`): The number of documents that were successfully modified by the update operation.
*   **Usage:** The function internally calls the MongoDB update_one method to perform the database update operation. This function is not called by any other functions according to the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database after encrypting it. It takes a username and an unencrypted API key as inputs, strips any leading or trailing whitespace from the key, encrypts it using a helper function, and then updates the corresponding document in the 'dbusers' collection with the encrypted key. The function returns the number of documents modified, which should be 1 if the update was successful.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    -   **gemini_api_key** (`str`): The unencrypted Gemini API key provided by the user, which will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified in the database. This should typically be 1 if the operation succeeds.
*   **Usage:** This function internally calls 'encrypt_text' to encrypt the provided API key before storing it. This function is called by 'save_gemini_cb' in 'Frontend.py' at line 35 and by 'frontend.Frontend' in 'Frontend.py' at line 393.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and performs an update operation on the user document in the database. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    -   **username** (`str`): The unique identifier of the user whose Ollama base URL needs to be updated.
    -   **ollama_base_url** (`str`): The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified by the update operation. This should typically be 1 if the user exists and the update was applied.
*   **Usage:** This function does not call any other functions directly; it relies on the pymongo library's update_one method. This function is called by save_ollama_cb in Frontend.py at line 42 and by frontend.Frontend in Frontend.py at line 407.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** The function retrieves a Gemini API key associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'gemini_api_key' field. If no matching user is found, it returns None.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose Gemini API key is to be retrieved.
*   **Returns:**
    -   **gemini_api_key** (`str or None`): The Gemini API key associated with the user, or None if the user is not found.
*   **Usage:** This function internally uses the 'dbusers.find_one' method to query a MongoDB collection. This function is not called by any other functions according to the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the provided username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose Ollama base URL is to be retrieved.
*   **Returns:**
    -   **ollama_base_url** (`Optional[str]`): The Ollama base URL associated with the user, or None if the user is not found.
*   **Usage:** The function internally calls 'dbusers.find_one' to query the database. This function is not called by any other functions according to the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** The function 'delete_user' removes a user document from a MongoDB collection based on the provided username. It uses the 'delete_one' method to target a specific user by their '_id' field, which corresponds to the username. The function returns the count of deleted documents, which will be 1 if the user was found and deleted, or 0 if no such user existed.
*   **Parameters:**
    -   **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    -   **deleted_count** (`int`): The number of documents deleted from the database, either 1 if the user was found and deleted, or 0 if no matching user was found.
*   **Usage:** This function internally calls 'dbusers.delete_one' to perform the deletion operation in the MongoDB collection. This function is not called by any other functions within the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user does not exist, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function and retrieves the 'ollama_base_url' directly. The function then returns both the decrypted Gemini API key and the Ollama base URL.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose API keys are to be retrieved.
*   **Returns:**
    -   **gemini_plain** (`str`): The decrypted Gemini API key for the user, or an empty string if not found.
    -   **ollama_plain** (`str`): The Ollama base URL for the user, or an empty string if not found.
*   **Usage:** The function internally uses dbusers.find_one to retrieve user data and decrypt_text to decrypt the Gemini API key. This function is called by the frontend.Frontend class in Frontend.py at lines 380 and 479.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** The function 'insert_chat' creates a new chat entry in the database with a unique identifier, associated username, chat name, and timestamp. It generates a UUID for the chat entry, populates the necessary fields, and inserts the document into the 'dbchats' collection. The function then returns the ID of the inserted document.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat.
    -   **chat_name** (`str`): The name of the chat.
*   **Returns:**
    -   **result.inserted_id** (`str`): The unique identifier of the newly inserted chat document.
*   **Usage:** This function does not call any other functions directly. This function is called by load_data_from_db in Frontend.py at line 81, handle_delete_chat in Frontend.py at line 122, and frontend.Frontend in Frontend.py at line 344.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** Die Funktion fetch_chats_by_user ruft alle Chats eines bestimmten Benutzers aus einer MongoDB-Datenbank ab. Sie verwendet den Benutzernamen als Filterkriterium und sortiert die Ergebnisse nach dem Erstellungsdatum in aufsteigender Reihenfolge. Das Ergebnis ist eine Liste der Chat-Dokumente, die dem Benutzer zugeordnet sind.
*   **Parameters:**
    -   **username** (`str`): Der Benutzername, für den die Chats abgerufen werden sollen.
*   **Returns:**
    -   **chats** (`list`): Eine Liste von Chat-Dokumenten, die dem angegebenen Benutzer zugeordnet sind und nach Erstellungsdatum sortiert sind.
*   **Usage:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf. Die Funktion wird von der Funktion load_data_from_db in der Datei Frontend.py aufgerufen.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a lookup in the 'dbchats' collection using a MongoDB query that matches both the username and chat name. The function returns a boolean value indicating the presence or absence of the chat entry.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat.
    -   **chat_name** (`str`): The name of the chat to check for existence.
*   **Returns:**
    -   **exists** (`bool`): True if a chat with the specified username and chat_name exists in the database; False otherwise.
*   **Usage:** The function does not call any other functions directly. The function is not called by any other functions according to the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and updates all associated exchanges in the database. It first updates the chat entry in the chats collection, then updates all related exchange entries in the exchanges collection. The function returns the number of modified chat documents.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be renamed.
    -   **old_name** (`str`): The current name of the chat to be renamed.
    -   **new_name** (`str`): The new name to assign to the chat.
*   **Returns:**
    -   **modified_count** (`int`): The number of chat documents that were successfully modified during the renaming operation.
*   **Usage:** This function does not call any other functions directly; it uses MongoDB operations update_one and update_many. This function is called by the frontend.Frontend class in the Frontend.py file at line 462.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str)`
*   **Description:** This function inserts a new exchange record into a MongoDB collection. It generates a unique ID for the exchange, constructs a dictionary with all the provided details including question, answer, feedback, and timestamps, and attempts to insert this data into the database. If the insertion fails, it catches the exception, prints an error message, and returns None. Otherwise, it returns the generated unique ID.
*   **Parameters:**
    -   **question** (`str`): The question associated with the exchange.
    -   **answer** (`str`): The answer provided in response to the question.
    -   **feedback** (`str`): Feedback related to the exchange.
    -   **username** (`str`): The username of the user involved in the exchange.
    -   **chat_name** (`str`): The name of the chat session.
    -   **helper_used** (`str`): The helper tool used during the exchange (optional).
    -   **main_used** (`str`): The main tool used during the exchange (optional).
    -   **total_time** (`str`): Total time taken for the exchange (optional).
    -   **helper_time** (`str`): Time taken by the helper tool (optional).
    -   **main_time** (`str`): Time taken by the main tool (optional).
*   **Returns:**
    -   **new_id** (`str`): The unique identifier of the inserted exchange record, or None if insertion failed.
*   **Usage:** This function does not call any other functions directly. This function is called by the frontend.Frontend class in Frontend.py at line 530.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses a database query to find documents matching the username and sorts them by the 'created_at' field. The result is returned as a list of exchange records.
*   **Parameters:**
    -   **username** (`str`): The username to filter exchange records by.
*   **Returns:**
    -   **exchanges** (`list`): A list of exchange records retrieved from the database, sorted by creation timestamp.
*   **Usage:** The function does not call any other functions directly. This function is called by the load_data_from_db function in Frontend.py at line 64.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched documents as a list.
*   **Parameters:**
    -   **username** (`str`): The username associated with the exchanges to be retrieved.
    -   **chat_name** (`str`): The name of the chat associated with the exchanges to be retrieved.
*   **Returns:**
    -   **exchanges** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order.
*   **Usage:** The function internally uses the 'dbexchanges.find' method to query the database and 'sort' to order the results. This function is not called by any other functions according to the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function updates the feedback field of a document in the 'dbexchanges' collection within a MongoDB database. It takes an exchange ID and a feedback value, then attempts to update the corresponding document with the new feedback value. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    -   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    -   **feedback** (`int`): The feedback value to be set in the document.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were modified as a result of the update operation.
*   **Usage:** This function does not call any other functions directly. This function is called by the handle_feedback_change function in Frontend.py at line 98.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates the feedback message associated with a specific exchange document in a MongoDB collection. It takes an exchange ID and a new feedback message as inputs, then performs an update operation on the database to set the feedback_message field. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    -   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    -   **feedback_message** (`str`): The new feedback message to be stored in the exchange document.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** The function internally calls the 'dbexchanges.update_one' method to perform the database update operation. This function is called by the 'render_exchange' function in 'Frontend.py' at line 211.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a provided exchange ID. It performs a deletion operation and returns the count of deleted documents. The function takes a single string parameter representing the unique identifier of the exchange to be deleted.
*   **Parameters:**
    -   **exchange_id** (`str`): A string representing the unique identifier of the exchange document to be deleted.
*   **Returns:**
    -   **deleted_count** (`int`): The number of documents that were deleted as a result of the operation.
*   **Usage:** The function does not call any other functions directly. This function is called by the handle_delete_exchange function in the Frontend.py file at line 102.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function deletes a complete chat session along with all associated exchanges from the database. It first removes all exchange records linked to the specified username and chat name, followed by deleting the chat record itself. The function returns the count of deleted chat documents, ensuring consistency between frontend and backend data states.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be deleted.
    -   **chat_name** (`str`): The name of the chat session to be deleted.
*   **Returns:**
    -   **deleted_count** (`int`): The number of chat documents that were successfully deleted from the database.
*   **Usage:** The function internally uses database operations to delete exchanges and chats. This function is called by the 'handle_delete_chat' function in 'Frontend.py' at line 110.

### File: `frontend/Frontend.py`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key associated with the user's username, clears the input field in the session state, and displays a success message to the user. The function does not take any parameters and does not return any value.
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function does not call any other functions directly. This function is not called by any other functions according to the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function handles the callback for saving an Ollama URL entered by the user in the frontend. It retrieves the URL from the session state, updates the database with the new URL associated with the user's username, and displays a success toast message. The function does not take any parameters and does not return any value.
*   **Parameters:**
*   **Returns:**
*   **Usage:** The function internally uses `st.session_state.get` to retrieve values from the Streamlit session state and calls `db.update_ollama_url` to update the database. This function is not called by any other function according to the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** Die Funktion 'load_data_from_db' lädt Chats und Exchanges konsistent aus einer Datenbank für einen bestimmten Benutzer. Sie prüft zunächst, ob der Benutzer bereits geladen wurde, und lädt dann die Chats und zugehörigen Exchanges aus der Datenbank. Bei Bedarf werden auch Standard-Chats erstellt und das aktive Chat-Objekt gesetzt.
*   **Parameters:**
    -   **username** (`str`): Der Name des Benutzers, für den die Daten aus der Datenbank geladen werden sollen.
*   **Returns:**
*   **Usage:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf. Die Funktion wird von der Methode 'frontend.Frontend' in der Datei 'Frontend.py' auf Zeile 310 aufgerufen.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: Any, val: Any)`
*   **Description:** This function updates the feedback value for a given exchange object in the database and triggers a re-render of the Streamlit application. It takes an exchange dictionary and a new feedback value, updates the feedback field in the dictionary, saves the updated feedback to the database using the exchange ID, and then reruns the Streamlit app to reflect the changes.
*   **Parameters:**
    -   **ex** (`dict`): A dictionary representing an exchange object, expected to contain keys like 'feedback' and '_id'.
    -   **val** (`Any`): The new feedback value to be assigned to the exchange object.
*   **Returns:**
*   **Usage:** This function internally calls 'db.update_exchange_feedback' to update the feedback in the database and 'st.rerun()' to refresh the Streamlit UI. This function is called by the 'render_exchange' method in 'Frontend.py' at lines 199 and 204.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: Any, ex: Any)`
*   **Description:** This function handles the deletion of an exchange from the database and updates the session state accordingly. It first deletes the exchange by its ID from the database, then checks if the exchange exists in the session state for a given chat and removes it if found. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    -   **chat_name** (`str`): The name of the chat from which the exchange is to be deleted.
    -   **ex** (`dict`): A dictionary representing the exchange to be deleted, expected to contain an '_id' key.
*   **Returns:**
*   **Usage:** The function internally calls `db.delete_exchange_by_id` to delete the exchange from the database and `st.rerun()` to refresh the Streamlit UI. This function is called by the `render_exchange` function in `Frontend.py` at lines 228 and 234.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: Any, chat_name: Any)`
*   **Description:** This function handles the deletion of a chat by first removing the chat from the database and then cleaning up the session state. It ensures that the active chat is updated appropriately after deletion, either by switching to another existing chat or creating a new default chat if none remain. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be deleted.
    -   **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:** This function does not directly call any other functions defined within the provided source code. This function is called by frontend.Frontend in Frontend.py at line 367.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text: Any)`
*   **Description:** The function 'extract_repo_name' takes a text input and attempts to extract a repository name from any URL present in the text. It uses regular expressions to find a URL, parses it using urllib.parse.urlparse, and then extracts the last segment of the URL path, which typically represents the repository name. If the extracted name ends with '.git', it removes the extension. If no URL is found or the path is empty, the function returns None.
*   **Parameters:**
    -   **text** (`str`): A string that may contain a URL from which to extract the repository name.
*   **Returns:**
    -   **repo_name** (`str`): The extracted repository name from the URL, with '.git' suffix removed if present, or None if no valid URL is found.
*   **Usage:** This function does not call any other functions directly; it relies on imported modules like 're' and 'urllib.parse.urlparse'. This function is called by the 'frontend.Frontend' class, specifically at line 442 in the file 'Frontend.py'.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text: Any)`
*   **Description:** The function 'stream_text_generator' takes a string input and yields each word from the string followed by a space, with a small delay between each yield. It is designed to simulate a streaming effect for text rendering. The function splits the input text into words based on spaces and iterates through them, yielding one word at a time with a short pause.
*   **Parameters:**
    -   **text** (`str`): A string containing the text to be streamed word by word.
*   **Returns:**
*   **Usage:** This function does not call any other functions directly. This function is called by 'render_text_with_mermaid' in 'Frontend.py' at line 160.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: Any, should_stream: Any)`
*   **Description:** This function processes a markdown text string to identify and render Mermaid diagrams embedded within code blocks. It splits the input text by Mermaid code blocks, rendering regular markdown content normally and Mermaid diagrams using a specialized Mermaid renderer. If rendering fails, it falls back to displaying the Mermaid code as a plain code block.
*   **Parameters:**
    -   **markdown_text** (`str`): A string containing markdown text that may include Mermaid diagram code blocks enclosed in triple backticks with 'mermaid' language identifier.
    -   **should_stream** (`bool`): A boolean flag indicating whether to stream the rendered markdown text or render it directly.
*   **Returns:**
*   **Usage:** The function does not call any other functions directly; it relies on external libraries like 're', 'st_mermaid', 'st.write_stream', 'st.markdown', and 'st.code'. This function is called by 'render_exchange' in 'Frontend.py' at line 238 and by 'frontend.Frontend' in 'Frontend.py' at line 524.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: Any, current_chat_name: Any)`
*   **Description:** This function renders a chat exchange in a Streamlit interface, displaying a user's question and an assistant's response. It handles both regular responses and error cases, providing interactive feedback mechanisms such as like/dislike buttons, comment functionality, and download/delete options. The function uses Streamlit components to build a rich UI layout including containers, buttons, popovers, and text areas.
*   **Parameters:**
    -   **ex** (`dict`): A dictionary containing the exchange data, including the question, answer, feedback status, and other metadata.
    -   **current_chat_name** (`str`): The name of the current chat session, used for handling delete operations.
*   **Returns:**
*   **Usage:** This function internally utilizes several Streamlit components such as st.chat_message, st.container, st.button, st.popover, st.text_area, st.download_button, and st.error, along with custom functions like handle_feedback_change, handle_delete_exchange, and render_text_with_mermaid. This function is called by the frontend.Frontend class, specifically from line 429 in Frontend.py.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the metadata of a single function parameter. It encapsulates three essential attributes: the parameter's name, its type, and a descriptive explanation. This class serves as a structured data model for documenting function parameters, ensuring consistency and type safety in parameter definitions.
*   **Instantiation:** This class is not directly instantiated by any other components as per the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* The constructor initializes the ParameterDescription instance with three required fields: name, type, and description. These fields are defined as string types and are used to store information about a function parameter.
    *   *Parameters:*
        -   **name** (`str`): The name of the function parameter.
        -   **type** (`str`): The data type of the function parameter.
        -   **description** (`str`): A textual description of the function parameter's purpose or usage.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to describe the return value of a function. It encapsulates three key pieces of information about a function's return: the name of the return value, its type, and a descriptive explanation. This class serves as a structured way to document and validate function return values, ensuring consistency and clarity in API or function signatures.
*   **Instantiation:** This class is not instantiated by any other components as per the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported.
*   **Constructor:**
    *   *Description:* The class is initialized with three required string fields: 'name', 'type', and 'description'. These fields collectively define the characteristics of a function's return value.
    *   *Parameters:*
        -   **name** (`str`): The name of the return value.
        -   **type** (`str`): The type of the return value.
        -   **description** (`str`): A textual description of the return value.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function. It captures two key pieces of information: the functions or methods that are called by the function in question, and the functions or methods that call the function in question. This class serves as a structured way to document and enforce the usage context of functions within a codebase.
*   **Instantiation:** This class is not instantiated by any other components as indicated by the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes the UsageContext model with two string fields: 'calls' and 'called_by'. These fields are used to store information about the calling context of a function.
    *   *Parameters:*
        -   **calls** (`str`): A string describing the functions or methods that are called by the function.
        -   **called_by** (`str`): A string describing the functions or methods that call the function.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate detailed metadata about a function, including its overall purpose, parameter descriptions, return value details, and usage context. It serves as a structured representation for documenting function signatures and behaviors, likely used in automated documentation systems or API analysis tools.
*   **Instantiation:** This class is not instantiated by any other component according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports list, which include standard typing constructs and pydantic components.
*   **Constructor:**
    *   *Description:* Initializes a FunctionDescription instance with fields for overall function description, a list of parameter descriptions, a list of return value descriptions, and usage context information.
    *   *Parameters:*
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class serves as the primary data model for representing the complete JSON schema of a function. It encapsulates essential information about a function including its unique identifier, a detailed description, and an optional error field for capturing validation issues.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a FunctionAnalysis instance with an identifier, a function description, and an optional error message. The constructor sets up the core attributes required to represent a function's metadata and potential errors.
    *   *Parameters:*
        -   **identifier** (`str`): A unique string identifier for the function.
            **description** (`schemas.types.FunctionDescription`): An object containing detailed information about the function's behavior, parameters, and return values.
            **error** (`Optional[str]`): An optional string field to store any error messages related to the function's validation or processing.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to describe the initialization method (__init__) of a class. It encapsulates a textual description of the constructor's purpose and a list of parameter descriptions that define its interface.
*   **Instantiation:** This class is not instantiated by any other component as indicated by the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription instance with a description of the constructor and a list of parameter descriptions.
    *   *Parameters:*
        -   **description** (`str`): A string describing the purpose or behavior of the constructor.
        -   **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing each parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
*   **Instantiation:** This class is not instantiated by any other component as indicated in the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields store information about the class's external dependencies and the entities responsible for its instantiation.
    *   *Parameters:*
        -   **dependencies** (`str`): A string describing the external dependencies of the class.
        -   **instantiated_by** (`str`): A string describing the entities or components that instantiate the class.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information. This class serves as a structured representation for documenting and communicating the essential characteristics and behaviors of a class within a codebase.
*   **Instantiation:** This class is not instantiated by any other component within the provided context.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond its base Pydantic model and the types it references.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ClassDescription class with specified attributes for overall purpose, constructor description, methods analysis, and usage context.
    *   *Parameters:*
        -   **overall** (`str`): A string describing the overall purpose and role of the class being analyzed.
        -   **init_method** (`schemas.types.ConstructorDescription`): An object detailing the constructor of the class, including its parameters and initialization logic.
        -   **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each representing a method within the class and its associated metadata.
        -   **usage_context** (`schemas.types.ClassContext`): An object providing contextual information about how the class is used, such as dependencies and instantiation points.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential information about a class including its identifier, a detailed description, and an optional error field for capturing any issues during processing.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules or libraries beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysis instance with an identifier string, a ClassDescription object, and an optional error message.
    *   *Parameters:*
        -   **identifier** (`str`): A unique string identifier for the class being analyzed.
        -   **description** (`schemas.types.ClassDescription`): An object containing detailed information about the class's structure and behavior.
        -   **error** (`Optional[str]`): An optional string field to store error messages if any issues occur during analysis.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure to capture metadata related to how functions are invoked within the system.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** No external dependencies were identified for this class.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo instance with fields representing a call event, including the file path, function name, call mode, and line number.
    *   *Parameters:*
        -   **file** (`str`): The file path where the call event occurred.
        -   **function** (`str`): The name of the function that made the call.
        -   **mode** (`str`): The mode of the call, such as 'method', 'function', or 'module'.
        -   **line** (`int`): The line number in the file where the call occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to represent structured context for analyzing a function. It encapsulates two key pieces of information: a list of function calls made within the function and a list of CallInfo objects indicating which functions call this one. This class serves as a data transfer object to facilitate function analysis and dependency tracking.
*   **Instantiation:** The class is instantiated in the evaluation.py file within the evaluation function at line 162, and also in main.py within the main_workflow function at line 223.
*   **Dependencies:** This class does not depend on any external modules beyond its imports.
*   **Constructor:**
    *   *Description:* Initializes the FunctionContextInput with two fields: 'calls', a list of strings representing function names called by the analyzed function, and 'called_by', a list of CallInfo objects representing functions that call the analyzed function.
    *   *Parameters:*
        -   **calls** (`List[str]`): A list of strings representing the names of functions called by the analyzed function.
        -   **called_by** (`List[CallInfo]`): A list of CallInfo objects representing the functions that call the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates all necessary information including the mode of operation, identifier, source code, imports, and contextual data required for function analysis.
*   **Instantiation:** This class is instantiated by the evaluation function in evaluation.py at line 167 and by the main_workflow function in main.py at line 228.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports list.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput instance with required fields including the mode, identifier, source code, imports list, and context object.
    *   *Parameters:*
        -   **mode** (`Literal["function_analysis"]`): A literal string indicating the mode of operation, specifically set to "function_analysis".
        -   **identifier** (`str`): A string identifier for the function being analyzed.
        -   **source_code** (`str`): The raw source code of the function to be analyzed.
        -   **imports** (`List[str]`): A list of import statements used in the function's source code.
        -   **context** (`schemas.types.FunctionContextInput`): An object containing contextual information about the function's environment and usage.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to represent structured context information for a class's methods. It encapsulates essential metadata such as the method's identifier, the list of methods it calls, the list of callers, its arguments, and its docstring. This class serves as a data transfer object to facilitate communication and documentation of method-level context within the application.
*   **Instantiation:** This class is instantiated in the evaluation.py file within the evaluation function at line 187 and in main.py within the main_workflow function at line 248.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes a MethodContextInput instance with fields for identifier, calls, called_by, args, and docstring. The identifier is a string representing the method name, calls is a list of strings indicating methods called by this method, called_by is a list of CallInfo objects showing who calls this method, args is a list of argument names, and docstring is an optional string containing the method's docstring.
    *   *Parameters:*
        -   **identifier** (`str`): A string representing the unique identifier or name of the method.
        -   **calls** (`List[str]`): A list of strings representing the identifiers of methods called by this method.
        -   **called_by** (`List[CallInfo]`): A list of CallInfo objects representing the callers of this method.
        -   **args** (`List[str]`): A list of strings representing the argument names of the method.
        -   **docstring** (`Optional[str]`): An optional string containing the docstring of the method.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to encapsulate structured context information for analyzing a class. It holds three main pieces of data: a list of dependencies, a list of call information for where the class is instantiated, and a list of method context inputs for each method within the class.
*   **Instantiation:** The class is instantiated by the functions main_orchestrator in HelperLLM.py at line 369, evaluation in evaluation.py at line 199, and main_workflow in main.py at line 260.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* The constructor initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are intended to store contextual metadata about a class being analyzed.
    *   *Parameters:*
        -   **dependencies** (`List[str]`): A list of strings representing the dependencies of the class.
        -   **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where the class is instantiated.
        -   **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects describing the context for each method in the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class serves as a data structure for encapsulating the necessary inputs required to generate a ClassAnalysis object. It defines the expected fields including the mode of operation, a unique identifier for the class being analyzed, the source code of the class, a list of import statements, and contextual information about how the class is used.
*   **Instantiation:** The class is instantiated by the main_orchestrator function in HelperLLM.py at line 338, the evaluation function in evaluation.py at line 205, and the main_workflow function in main.py at line 266.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports list.
*   **Constructor:**
    *   *Description:* Initializes a new instance of the ClassAnalysisInput class with the specified parameters. The constructor sets up the required fields for class analysis, including the operational mode, class identifier, source code, imports, and context.
    *   *Parameters:*
        -   **mode** (`Literal["class_analysis"]`): A literal string value that specifies the mode of operation as 'class_analysis'.
        -   **identifier** (`str`): A string identifier for the class being analyzed.
        -   **source_code** (`str`): A string containing the full source code of the class to be analyzed.
        -   **imports** (`List[str]`): A list of strings representing the import statements used in the source file.
        -   **context** (`schemas.types.ClassContextInput`): An object containing contextual information about the class usage and dependencies.
*   **Methods:**

---
# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview

-   **Description:** A repository onboarding agent designed to automate the generation of documentation and analysis for code repositories, leveraging LLMs for code understanding, a Streamlit frontend for user interaction, and a MongoDB backend for data persistence.
-   **Key Features:**
    -   Automated documentation generation for code repositories.
    -   Leverages Large Language Models (LLMs) for deep code analysis.
    -   Interactive Streamlit frontend for user input and display.
    -   MongoDB integration for persistent storage of user data and documentation.
    -   Detailed code analysis of functions, classes, and their relationships.
-   **Tech Stack:** Python, Streamlit, LangChain (Google Generative AI, Ollama, OpenAI), Pydantic, GitPython, NetworkX, PyMongo, Matplotlib, python-dotenv, Streamlit-Mermaid, TOON Format.

*   **Repository Structure:**
    ```mermaid
    graph LR
        node_root_0["root"]
        node__env_example_1[".env.example"]
        node_root_0 --> node__env_example_1
        node__gitignore_2[".gitignore"]
        node_root_0 --> node__gitignore_2
        node_analysis_output_json_3["analysis_output.json"]
        node_root_0 --> node_analysis_output_json_3
        node_output_json_4["output.json"]
        node_root_0 --> node_output_json_4
        node_output_toon_5["output.toon"]
        node_root_0 --> node_output_toon_5
        node_readme_md_6["readme.md"]
        node_root_0 --> node_readme_md_6
        node_requirements_txt_7["requirements.txt"]
        node_root_0 --> node_requirements_txt_7
        node_SystemPrompts_8["SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt"]
        node_root_0 --> node_SystemPrompts_8
        node_backend_9["backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py"]
        node_root_0 --> node_backend_9
        node_database_10["database<br/>db.py"]
        node_root_0 --> node_database_10
        node_frontend_11["frontend<br/>Frontend.py<br/>__init__.py"]
        node_root_0 --> node_frontend_11
        node__streamlit_12[".streamlit<br/>config.toml"]
        node_frontend_11 --> node__streamlit_12
        node_gifs_13["gifs<br/>4j.gif"]
        node_frontend_11 --> node_gifs_13
        node_notizen_14["notizen<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
        node_root_0 --> node_notizen_14
        node_grafiken_15["grafiken"]
        node_notizen_14 --> node_grafiken_15
        node_1_16["1<br/>File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
        node_grafiken_15 --> node_1_16
        node_2_17["2<br/>FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot"]
        node_grafiken_15 --> node_2_17
        node_Flask_Repo_18["Flask-Repo<br/>__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot"]
        node_grafiken_15 --> node_Flask_Repo_18
        node_Repo_onboarding_19["Repo-onboarding<br/>AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot"]
        node_grafiken_15 --> node_Repo_onboarding_19
        node_result_20["result<br/>ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
        node_root_0 --> node_result_20
        node_schemas_21["schemas<br/>types.py"]
        node_root_0 --> node_schemas_21
        node_statistics_22["statistics<br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png"]
        node_root_0 --> node_statistics_22
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
- toon_format@git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c9006de6
- tornado==6.5.2
- tqdm==4.67.1
- typing-inspect==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0
pip install -r requirements.txt

### Setup Guide
Information not found

### Quick Startup
Information not found

## 3. Use Cases & Commands
This repository hosts a sophisticated agent designed to automate the generation of documentation for code repositories. It leverages advanced Large Language Models (LLMs) to analyze code, extract essential information, and synthesize comprehensive reports. The project features a user-friendly Streamlit frontend for interactive input and display, with a MongoDB backend ensuring the persistence of user data, API keys, and generated documentation history. Key functionalities include repository cloning, AST generation, call graph analysis, relationship extraction, and structured output formatting using TOON.

**Use Cases:**
*   **Automated Code Onboarding:** Quickly generate documentation for new or existing repositories to facilitate developer onboarding.
*   **Code Comprehension:** Gain deep insights into project structure, function calls, class hierarchies, and file dependencies without manual analysis.
*   **LLM-Powered Documentation:** Leverage various LLMs (Gemini, OpenAI, Ollama) for intelligent code understanding and report generation.
*   **Interactive Documentation Interface:** Interact with the documentation agent through a Streamlit web application to specify repositories, view analyses, and manage API keys.
*   **Historical Documentation Management:** Store and retrieve previously generated documentation and user interactions in a persistent MongoDB database.

**Primary Commands:**
*   **Install Dependencies:** `pip install -r requirements.txt`
*   **Start the Application:** `streamlit run frontend/Frontend.py`
*   **Environment Setup:** Copy the example environment file: `cp .env.example .env`

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases where the file path is not within the project root by falling back to the basename of the file. If the resulting path ends with '.__init__', it removes the trailing segment to normalize the module path.
*   **Parameters:**
    -   **filepath** (`str`): The absolute or relative path to a Python file.
    -   **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    -   **module_path** (`str`): A normalized Python module path derived from the given file path.
*   **Usage:** This function does not call any other functions directly. This function is called by the __init__ method in AST_Schema.py at line 31.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It collects information about imports, classes, and functions, organizing them into a structured schema. The visitor maintains context for class definitions and their methods, allowing for detailed analysis of modules, including their structure, dependencies, and relationships.
*   **Instantiation:** The class is instantiated in the 'analyze_repository' function located in 'AST_Schema.py' at line 182.
*   **Dependencies:** This class relies on standard library modules such as 'ast', 'networkx', and 'os'. It also uses custom modules like 'callgraph.build_filtered_callgraph' and 'getRepo.GitRepository'.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It sets up internal tracking variables such as module path, schema structure, and current class context.
    *   *Parameters:*
        -   **source_code** (`str`): The full source code string of the file being analyzed.
        -   **file_path** (`str`): The file path of the source code being processed.
        -   **project_root** (`str`): The root directory of the project being analyzed.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It ensures that all imports are recorded for further analysis.
        *   *Parameters:*
            -   **node** (`ast.Import`): An AST node representing an import statement.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called automatically by the AST traversal mechanism when an import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* Processes import-from nodes in the AST by collecting the fully qualified names of imported items and adding them to the schema's imports list. It supports both direct imports and relative imports.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing an import-from statement.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called automatically by the AST traversal mechanism when an import-from node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* Handles class definition nodes in the AST by creating a structured representation of the class, including its identifier, name, docstring, and source code segment. It also tracks the class in the schema and sets the current class context for subsequent method processing.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called automatically by the AST traversal mechanism when a class definition node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: ast.FunctionDef)`
        *   *Description:* Processes function definition nodes in the AST. If a class context is active, it records the function as a method of that class. Otherwise, it treats the function as a top-level function and adds it to the schema accordingly. It captures details like arguments, docstrings, and source segments.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions directly. This method is called automatically by the AST traversal mechanism when a function definition node is encountered.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef)`
        *   *Description:* Handles asynchronous function definition nodes in the AST by delegating to the standard function definition handler. This allows async functions to be treated similarly to regular functions during schema collection.
        *   *Parameters:*
            -   **node** (`ast.AsyncFunctionDef`): An AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** This method delegates to visit_FunctionDef. This method is called automatically by the AST traversal mechanism when an async function definition node is encountered.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information. It merges relationship data into the schema and supports repository-wide analysis by processing multiple files and building a structured representation of functions, classes, and their relationships.
*   **Instantiation:** This class is instantiated in HelperLLM_evaluation.py at line 128, in MainLLM_evaluation.py at line 131, and in main.py at line 187.
*   **Dependencies:** This class depends on external modules such as ast, networkx, os, callgraph.build_filtered_callgraph, and getRepo.GitRepository.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any initialization actions.
    *   *Parameters:*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema: dict, call_graph: networkx.DiGraph, filename: str)`
        *   *Description:* Enriches a given schema with call graph information by adding 'calls' and 'called_by' details for functions and methods based on a provided call graph. It iterates through functions and class methods in the schema and updates their context with successors and predecessors from the call graph.
        *   *Parameters:*
            -   **schema** (`dict`): A dictionary representing the schema containing functions and classes.
            -   **call_graph** (`networkx.DiGraph`): A NetworkX directed graph representing the call relationships between functions and methods.
            -   **filename** (`str`): The filename associated with the schema being enriched.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions. This method is called by the analyze_repository method.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, relationship_data: list)`
        *   *Description:* Merges relationship data into a full schema by updating function and class context with 'called_by' information. It builds a lookup table from the relationship data and applies this information to functions, classes, and methods within the schema.
        *   *Parameters:*
            -   **full_schema** (`dict`): A dictionary representing the full schema of the repository.
            -   **relationship_data** (`list`): A list of dictionaries containing relationship information for identifiers.
        *   *Returns:*
            -   **full_schema** (`dict`): The updated schema with merged relationship data.
        *   **Usage:** This method does not call any other functions. This method is called by the evaluation function in HelperLLM_evaluation.py, the prepare_shared_input function in MainLLM_evaluation.py, and the main_workflow function in main.py.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: getRepo.GitRepository)`
        *   *Description:* Analyzes a repository by processing a list of files, parsing their content into ASTs, and generating a schema for each file. It enriches the schema with call graph information and aggregates results into a full schema structure. Handles errors during parsing and filters out non-Python files.
        *   *Parameters:*
            -   **files** (`list`): A list of file objects to be analyzed.
            -   **repo** (`getRepo.GitRepository`): An object representing the Git repository being analyzed.
        *   *Returns:*
            -   **full_schema** (`dict`): A dictionary containing the aggregated schema for all processed files.
        *   **Usage:** This method does not call any other functions directly but relies on external functions like build_filtered_callgraph and ASTVisitor. This method is called by the evaluation function in HelperLLM_evaluation.py, the prepare_shared_input function in MainLLM_evaluation.py, and the main_workflow function in main.py.

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: ast.AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes a filename, an abstract syntax tree (AST), and a repository root path as inputs. It uses a custom visitor class to traverse the AST and extract import dependencies. These dependencies are then added to a NetworkX DiGraph, where nodes represent files and edges represent dependency relationships.
*   **Parameters:**
    -   **filename** (`str`): The name of the file being analyzed for dependencies.
    -   **tree** (`ast.AST`): The abstract syntax tree of the file being analyzed.
    -   **repo_root** (`str`): The root directory path of the repository being analyzed.
*   **Returns:**
    -   **graph** (`networkx.DiGraph`): A NetworkX directed graph representing file dependencies, where nodes are files and edges indicate import relationships.
*   **Usage:** This function does not directly call any other functions from within its own body; it relies on the FileDependencyGraph visitor class for traversal. This function is called by the 'build_repository_graph' function in the 'File_Dependency.py' file at line 177.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: getRepo.GitRepository)`
*   **Description:** This function constructs a dependency graph for all Python files within a given Git repository. It iterates through each Python file, parses its content into an abstract syntax tree (AST), and builds a file-level dependency graph. These individual graphs are then merged into a single global directed graph representing dependencies across the entire repository. The function ensures that only Python files are processed and properly handles nodes and edges in the resulting graph.
*   **Parameters:**
    -   **repository** (`getRepo.GitRepository`): The Git repository object containing the files to analyze for dependencies.
*   **Returns:**
    -   **global_graph** (`networkx.DiGraph`): A NetworkX directed graph representing the dependency relationships between Python files in the repository.
*   **Usage:** This function internally uses several AST parsing and graph-building utilities such as ast.parse, build_file_dependency_graph, and networkx.DiGraph operations. This function is called by the backend.File_Dependency module at line 200 in File_Dependency.py.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function retrieves all Python files (.py) from a specified directory and its subdirectories, returning them as relative paths from the given directory. It uses pathlib to resolve the directory path and recursively searches for files with the .py extension.
*   **Parameters:**
    -   **directory** (`str`): The path to the directory from which to search for Python files.
*   **Returns:**
    -   **all_files** (`list[pathlib.Path]`): A list of Path objects representing all Python files found in the directory and its subdirectories, relative to the specified directory.
*   **Usage:** This function does not call any other functions directly. This function is called by _resolve_module_name in File_Dependency.py at line 43.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze Python file dependencies by parsing import statements and resolving both absolute and relative imports. It extends NodeVisitor to traverse AST nodes representing import structures, building a dependency graph that maps files to their imported modules. The class handles complex relative imports by resolving module names against the repository structure and checks for symbol existence in package __init__.py files. It maintains a dictionary of import dependencies for each file, which can be used to construct a call graph or visualize module relationships.
*   **Instantiation:** This class is instantiated by the function 'build_file_dependency_graph' in the file 'File_Dependency.py' at line 156.
*   **Dependencies:** This class depends on networkx, os, ast module classes (Assign, AST, ClassDef, FunctionDef, Import, ImportFrom, Name, NodeVisitor, literal_eval, parse, walk), keyword.iskeyword, pathlib.Path, GitRepository, and make_safe_dot.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up the instance variables to track the current file being analyzed and the root directory of the repository for resolving relative paths.
    *   *Parameters:*
        -   **filename** (`str`): The name of the file being analyzed for dependencies.
        -   **repo_root** (`Any`): The root directory path of the repository containing the file.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ast.ImportFrom)`
        *   *Description:* Resolves relative import statements by analyzing the import node and mapping it to actual module or symbol names. It determines the correct base directory based on the import level and checks whether the resolved modules or symbols exist in the repository structure. The method supports both direct module file existence checks and symbol resolution through __init__.py files. It raises ImportError if no valid module or symbol can be resolved.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing a relative import statement.
        *   *Returns:*
            -   **""** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:** This method calls helper functions 'module_file_exists' and 'init_exports_symbol' to check for module existence and symbol availability in __init__.py files respectively. This method is called by 'visit_ImportFrom' when resolving relative imports.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Union[ast.Import, ast.ImportFrom], base_name: Union[str, None])`
        *   *Description:* Handles import statements by adding the imported module names to the dependency tracking dictionary. It ensures that the current file's dependencies are recorded under its filename key in the import_dependencies dictionary. The method supports both regular imports and those with base names derived from more complex import structures.
        *   *Parameters:*
            -   **node** (`Union[ast.Import, ast.ImportFrom]`): An AST node representing an import statement.
            -   **base_name** (`Union[str, None]`): Optional base name for the imported module, used in complex import cases.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal of the AST. This method is called by 'visit_ImportFrom' during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* Processes 'from ... import ...' style import statements by extracting the module name and delegating to visit_Import for handling. For relative imports without explicit module names, it attempts to resolve the module names using _resolve_module_name. If resolution fails, it prints an error message but continues processing.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method calls '_resolve_module_name' to resolve relative imports and 'visit_Import' to record dependencies. This method is called during AST traversal by the parent NodeVisitor class.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** The main_orchestrator function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analysis for several example functions including add_item, check_stock, and generate_report, and simulates the process of generating documentation for these functions using an LLMHelper instance. The function sets up mock inputs and expected outputs for these functions, initializes an LLMHelper with specific prompt files, and processes the results to build a final documentation structure.
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function does not call any other functions directly. This function is called by backend.HelperLLM (line 419 in HelperLLM.py)

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a centralized interface for interacting with various language models, particularly for generating and validating code documentation for functions and classes. It handles configuration of different LLM backends based on model names, manages batching and rate limiting for API calls, and ensures structured output using Pydantic models. The class supports multiple providers including Google Gemini, OpenAI, custom APIs, and Ollama, with appropriate batch size configurations per model.
*   **Instantiation:** This class is instantiated by the main_orchestrator function in HelperLLM.py, the evaluation function in HelperLLM_evaluation.py, the prepare_shared_input function in MainLLM_evaluation.py, and the main_workflow function in main.py.
*   **Dependencies:** This class depends on several external libraries including langchain modules for LLM integration, pydantic models for validation, and standard library modules like json, logging, and time.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API credentials and prompt files. It reads system prompts from specified paths, configures batch settings based on the model name, and sets up appropriate LLM clients for function and class documentation generation. The initialization also validates the presence of required API keys and handles different model types by selecting the correct backend client.
    *   *Parameters:*
        -   **api_key** (`str`): API key for accessing the language model service.
        -   **function_prompt_path** (`str`): Path to the file containing the system prompt for function documentation generation.
        -   **class_prompt_path** (`str`): Path to the file containing the system prompt for class documentation generation.
        -   **model_name** (`str`): Name of the language model to use. Defaults to 'gemini-2.0-flash-lite'.
        -   **base_url** (`str`): Base URL for custom API endpoints. Optional.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing requests based on the specified model name. It assigns different batch sizes depending on the model type, defaulting to a conservative value for unknown models. This method ensures efficient processing while respecting model-specific constraints.
        *   *Parameters:*
            -   **model_name** (`str`): Name of the language model for which to configure batch settings.
        *   *Returns:*
        *   **Usage:** This method does not call any other functions. This method is called during the initialization of the LLMHelper class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[schemas.types.FunctionAnalysisInput])`
        *   *Description:* Processes a batch of function inputs to generate and validate documentation using the configured LLM. It divides inputs into batches according to the configured batch size, sends them to the LLM for processing, and handles errors gracefully by returning None values for failed items. Rate limiting is enforced between batches to comply with API constraints.
        *   *Parameters:*
            -   **function_inputs** (`List[schemas.types.FunctionAnalysisInput]`): A list of function input models containing information needed for documentation generation.
        *   *Returns:*
            -   **result** (`List[Optional[schemas.types.FunctionAnalysis]]`): A list of validated function analysis results or None for failed items.
        *   **Usage:** This method does not directly call other functions from the provided context. This method is called by evaluation, prepare_shared_input, and main_workflow functions.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[schemas.types.ClassAnalysisInput])`
        *   *Description:* Processes a batch of class inputs to generate and validate documentation using the configured LLM. Similar to generate_for_functions, it batches inputs, sends them to the LLM, and handles errors by returning None values for failed items. Rate limiting is applied between batches to respect API constraints.
        *   *Parameters:*
            -   **class_inputs** (`List[schemas.types.ClassAnalysisInput]`): A list of class input models containing information needed for documentation generation.
        *   *Returns:*
            -   **result** (`List[Optional[schemas.types.ClassAnalysis]]`): A list of validated class analysis results or None for failed items.
        *   **Usage:** This method does not directly call other functions from the provided context. This method is called by evaluation, prepare_shared_input, and main_workflow functions.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the central interface for interacting with various Large Language Models (LLMs). It supports multiple LLM providers including Google Generative AI, OpenAI-compatible APIs, and Ollama-based models. The class initializes with configuration parameters such as API keys, prompt file paths, and model specifications, and provides two core methods for interacting with the LLM: one for synchronous calls and another for streaming responses.
*   **Instantiation:** This class is instantiated by the benchmark_loop function in MainLLM_evaluation.py and the main_workflow function in main.py.
*   **Dependencies:** This class depends on several external libraries including langchain_google_genai.ChatGoogleGenerativeAI, langchain_ollama.ChatOllama, langchain_openai.ChatOpenAI, and langchain.messages.HumanMessage and SystemMessage for handling LLM interactions.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading the system prompt from a specified file, and setting up the appropriate LLM client based on the model name. It supports different LLM backends like Google Generative AI, custom OpenAI-compatible endpoints, and Ollama.
    *   *Parameters:*
        -   **api_key** (`str`): The API key used for authenticating with the LLM provider.
        -   **prompt_file_path** (`str`): The file path to the system prompt that will be loaded and used for LLM interactions.
        -   **model_name** (`str`): The name of the model to use. Determines which backend (Google, OpenAI, or Ollama) will be initialized.
        -   **base_url** (`str`): Optional base URL for connecting to a custom LLM endpoint. Defaults to None.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* Synchronously invokes the configured LLM with a user input message and returns the generated response content. It constructs a message sequence including the system prompt and user input, sends it to the LLM, and handles potential exceptions during the call.
        *   *Parameters:*
            -   **user_input** (`str`): The input text provided by the user to be processed by the LLM.
        *   *Returns:*
            -   **response_content** (`str`): The content of the LLM's response if the call is successful; otherwise, returns None in case of an error.
        *   **Usage:** This method does not explicitly call other functions defined in the class. This method is called by the benchmark_loop function in MainLLM_evaluation.py and the main_workflow function in main.py.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* Initiates a streaming interaction with the LLM, yielding chunks of the response content incrementally. It prepares the same message sequence as call_llm but uses the stream method of the LLM client to process and yield results in real-time.
        *   *Parameters:*
            -   **user_input** (`str`): The input text provided by the user to be processed by the LLM.
        *   *Returns:*
            -   **chunk_content** (`str`): Yields content chunks from the LLM's streaming response. In case of an error, yields an error message string.
        *   **Usage:** This method does not explicitly call other functions defined in the class. This method is not called by any other function according to the provided context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract basic project information from common project files such as README.md, pyproject.toml, and requirements.txt. It maintains an internal dictionary structure to store extracted information under categories like 'projekt_uebersicht' (project overview) and 'installation'. The class orchestrates the extraction process by identifying relevant files, parsing their content using helper methods, and prioritizing data sources to ensure metadata accuracy. It supports fallback mechanisms and handles various file formats including Markdown and TOML.
*   **Instantiation:** The class is instantiated in HelperLLM_evaluation.py at line 104, MainLLM_evaluation.py at line 121, and main.py at line 160.
*   **Dependencies:** This class does not depend on any external libraries beyond standard Python modules (re, os, tomllib) and typing annotations.
*   **Constructor:**
    *   *Description:* Initializes the ProjektInfoExtractor with a predefined structure for storing project information. It sets up placeholder values for fields such as title, description, status, features, tech stack, dependencies, setup instructions, and quick start guides. These placeholders are later replaced with actual data during the extraction process.
    *   *Parameters:*
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This private method searches for a file among a list of files based on a set of case-insensitive file extension patterns. It iterates through the provided file list and checks if any file's path ends with one of the specified patterns. If a match is found, it returns the matching file object; otherwise, it returns None.
        *   *Parameters:*
            -   **patterns** (`List[str]`): A list of file extension patterns to search for (e.g., ['readme.md', 'readme.rst']).
            -   **dateien** (`List[Any]`): A list of file objects to search through.
        *   *Returns:*
            -   **result** (`Optional[Any]`): The matched file object if found, otherwise None.
        *   **Usage:** This method does not call any other methods. This method is called by the extrahiere_info method to locate relevant project files such as README, pyproject.toml, and requirements.txt.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This private method extracts text sections from a Markdown document that appear under a specific heading (marked by '##'). It uses regular expressions to find the section associated with given keywords and returns the content between that heading and the next heading or end of the document. This allows for targeted extraction of sections like 'Installation' or 'Features'.
        *   *Parameters:*
            -   **inhalt** (`str`): The full Markdown text content to parse.
            -   **keywords** (`List[str]`): A list of alternative keywords to look for as section headings (e.g., ['Installation', 'Setup']).
        *   *Returns:*
            -   **extracted_text** (`Optional[str]`): The extracted text block under the specified heading, or None if no match is found.
        *   **Usage:** This method does not call any other methods. This method is invoked by _parse_readme to extract specific sections like 'Features', 'Tech Stack', 'Status', 'Installation', and 'Quick Start' from the README file.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This private method parses the content of a README file to extract project metadata such as title, description, key features, tech stack, current status, setup instructions, and quick start guide. It uses regex patterns to identify these elements and stores them in the internal info dictionary. It leverages the _extrahiere_sektion_aus_markdown helper to extract structured sections from the Markdown content.
        *   *Parameters:*
            -   **inhalt** (`str`): The full content of the README file as a string.
        *   *Returns:*
        *   **Usage:** This method calls _extrahiere_sektion_aus_markdown to extract specific sections from the README content. This method is called by extrahiere_info to parse README content when a README file is identified.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project metadata such as name and description. It uses the tomllib library to load the TOML data and updates the internal info dictionary accordingly. It also handles cases where tomllib is not available or when there are parsing errors, providing appropriate warnings.
        *   *Parameters:*
            -   **inhalt** (`str`): The full content of the pyproject.toml file as a string.
        *   *Returns:*
        *   **Usage:** This method does not call any other methods. This method is called by extrahiere_info to parse pyproject.toml content when a TOML file is identified.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This private method parses the content of a requirements.txt file to extract dependency information. It filters out comments and empty lines to form a clean list of dependencies. It only populates the dependencies field if it hasn't already been filled by a higher-priority source like pyproject.toml.
        *   *Parameters:*
            -   **inhalt** (`str`): The full content of the requirements.txt file as a string.
        *   *Returns:*
        *   **Usage:** This method does not call any other methods. This method is called by extrahiere_info to parse requirements.txt content when a requirements.txt file is identified.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This public method orchestrates the entire information extraction process. It identifies relevant project files (README, pyproject.toml, requirements.txt) using _finde_datei, then parses them in order of priority (_parse_toml, _parse_requirements, _parse_readme). It ensures proper formatting of dependencies and finalizes the project title based on the repository URL. The method returns the complete info dictionary populated with extracted data.
        *   *Parameters:*
            -   **dateien** (`List[Any]`): A list of file objects representing files in the repository.
            -   **repo_url** (`str`): The URL of the repository, used to derive the project title.
        *   *Returns:*
            -   **info** (`Dict[str, Any]`): A dictionary containing the extracted project information organized under 'projekt_uebersicht' and 'installation' keys.
        *   **Usage:** This method calls _finde_datei to locate relevant files, and _parse_readme, _parse_toml, and _parse_requirements to parse file contents. This method is called by evaluation in HelperLLM_evaluation.py, prepare_shared_input in MainLLM_evaluation.py, and main_workflow in main.py.

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: networkx.DiGraph, out_path: str)`
*   **Description:** The function 'make_safe_dot' takes a NetworkX directed graph and a file path as inputs. It creates a copy of the graph and generates a safe node naming scheme by prefixing each original node name with 'n' followed by its index. The function then relabels the nodes in the graph according to this safe naming scheme and assigns the original node names as labels to the new nodes. Finally, it writes the modified graph to a DOT file at the specified output path.
*   **Parameters:**
    -   **graph** (`networkx.DiGraph`): A NetworkX directed graph object to be processed and saved.
    -   **out_path** (`str`): The file path where the DOT representation of the graph will be written.
*   **Returns:**
*   **Usage:** This function does not call any other functions directly; it uses NetworkX functions such as 'copy', 'relabel_nodes', and 'write_dot'. This function is called by 'backend.callgraph' in the file 'callgraph.py' at line 244.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: getRepo.GitRepository)`
*   **Description:** Die Funktion erstellt einen globalen Call-Graphen basierend auf allen Python-Dateien eines Git-Repositories und filtert diesen anschließend, sodass nur Aufrufe zwischen selbst geschriebenen Funktionen erhalten bleiben. Sie durchläuft alle Dateien, parst deren Inhalt mit dem Abstract Syntax Tree (AST), extrahiert Funktionsaufrufe und baut einen gerichteten Graphen auf, der nur die relevanten Verbindungen zwischen eigenen Funktionen enthält.
*   **Parameters:**
    -   **repo** (`getRepo.GitRepository`): Ein Objekt, das Zugriff auf alle Dateien des Git-Repositories bietet.
*   **Returns:**
    -   **global_graph** (`networkx.DiGraph`): Ein gerichteter Graph, der die Aufrufbeziehungen zwischen selbst geschriebenen Funktionen darstellt.
*   **Usage:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Quellcodes auf. Diese Funktion wird von 'analyze_repository' in 'AST_Schema.py' und von 'backend.callgraph' in 'callgraph.py' aufgerufen.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is designed to construct a call graph from Python AST nodes, tracking function and method calls within a given file. It uses the Abstract Syntax Tree (AST) visitor pattern to traverse the code and builds a directed graph representing these relationships. The class maintains mappings for local definitions, imports, and function names to resolve and track inter-function dependencies. It supports handling of classes, functions, asynchronous functions, imports, and conditional blocks like main block detection.
*   **Instantiation:** This class is instantiated by the build_filtered_callgraph function in callgraph.py at lines 199 and 206.
*   **Dependencies:** This class depends on the ast module for parsing Python code and networkx for graph operations.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph with a filename and sets up internal data structures including local definitions, a directed graph, import mappings, a function set, and edges for tracking function calls.
    *   *Parameters:*
        -   **filename** (`str`): The name of the file being processed to build the call graph.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node: ast.AST)`
        *   *Description:* Recursively extracts the dotted name components from an AST node representing a function or attribute call. It handles different types of AST nodes such as ast.Call, ast.Name, and ast.Attribute to build a list of name parts.
        *   *Parameters:*
            -   **node** (`ast.AST`): The AST node to extract name components from.
        *   *Returns:*
            -   **parts** (`list[str]`): A list of strings representing the dotted name components.
        *   **Usage:** This method does not call any other methods. This method is called by the _resolve_all_callee_names method.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* Resolves a list of dotted name components into full qualified names by checking local definitions, import mappings, and constructing appropriate names based on current class context. It processes each component list to determine the correct fully qualified name for each callee.
        *   *Parameters:*
            -   **callee_nodes** (`list[list[str]]`): A list of lists containing name components for callees.
        *   *Returns:*
            -   **resolved** (`list[str]`): A list of fully qualified names for the callees.
        *   **Usage:** This method calls the _recursive_call method to extract name components. This method is called by the visit_Call method.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: Union[str, None])`
        *   *Description:* Constructs a fully qualified name for a function or method by combining the filename, optional class name, and base name. This helps in uniquely identifying functions within the context of a file and class hierarchy.
        *   *Parameters:*
            -   **basename** (`str`): The base name of the function or method.
            -   **class_name** (`Union[str, None]`): The name of the class if the function belongs to one.
        *   *Returns:*
            -   **full_name** (`str`): The fully qualified name constructed from the filename, class name, and base name.
        *   **Usage:** This method does not call any other methods. This method is called by the visit_FunctionDef method.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* Determines the current caller's name, either from the current function or defaults to a global scope identifier if no function is active. This is used to label nodes in the call graph.
        *   *Parameters:*
        *   *Returns:*
            -   **caller** (`str`): The name of the current caller.
        *   **Usage:** This method does not call any other methods. This method is called by the visit_Call method.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST by mapping aliases to their actual module names. It updates the import mapping dictionary to resolve imported names later during call resolution.
        *   *Parameters:*
            -   **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal. This method is called by the AST visitor framework.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements by extracting the module name and mapping aliases to their respective modules. It updates the import mapping dictionary accordingly.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal. This method is called by the AST visitor framework.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* Processes class definitions in the AST by temporarily setting the current class name and visiting the class body. After processing, it restores the previous class name to maintain proper scoping.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal. This method is called by the AST visitor framework.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definitions by creating a fully qualified name for the function, updating local definitions, adding the function to the graph, and visiting the function body. It also tracks the function in a set for future reference.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
        *   **Usage:** This method calls _make_full_name and generic_visit to continue traversal. This method is called by the AST visitor framework.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating to the standard function definition handler. This ensures that async functions are treated similarly to regular functions in terms of call graph construction.
        *   *Parameters:*
            -   **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** This method calls visit_FunctionDef to process the function. This method is called by the AST visitor framework.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST by determining the caller, resolving the callee names, and recording the edge in the call graph. It manages the edges dictionary to store function call relationships.
        *   *Parameters:*
            -   **node** (`ast.Call`): The AST node representing a function call.
        *   *Returns:*
        *   **Usage:** This method calls _recursive_call, _resolve_all_callee_names, and _current_caller to process the call. This method is called by the AST visitor framework.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* Handles conditional statements, specifically detecting when the condition checks for '__name__ == '__main__''. In such cases, it temporarily sets the current function to '<main_block>' before visiting the conditional body and then restores the original function name.
        *   *Parameters:*
            -   **node** (`ast.If`): The AST node representing an if statement.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal. This method is called by the AST visitor framework.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It implements lazy loading for file metadata such as content and size to optimize performance by only loading data when necessary. The class provides properties to access these lazily-loaded attributes and includes utility methods for basic file analysis and serialization.
*   **Instantiation:** This class is instantiated by the get_all_files method located in getRepo.py at line 111.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object with a file path and a commit tree. Sets up internal attributes for lazy loading including blob, content, and size.
    *   *Parameters:*
        -   **file_path** (`str`): The path to the file within the repository.
        -   **commit_tree** (`git.Tree`): The tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* A property that lazily loads and returns the Git Blob object associated with the file. If the blob hasn't been loaded yet, it attempts to retrieve it from the commit tree using the stored file path. Raises a FileNotFoundError if the file cannot be found in the commit tree.
        *   *Parameters:*
        *   *Returns:*
            -   **blob** (`git.Blob`): The Git Blob object representing the file.
        *   **Usage:** This method does not call any other functions. This method is not called by any other functions according to the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* A property that lazily loads and returns the decoded UTF-8 content of the file. If the content hasn't been loaded yet, it reads the data stream from the blob and decodes it, ignoring encoding errors. Returns the decoded string representation of the file's content.
        *   *Parameters:*
        *   *Returns:*
            -   **content** (`str`): The decoded content of the file.
        *   **Usage:** This method does not call any other functions. This method is not called by any other functions according to the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* A property that lazily loads and returns the size of the file in bytes. If the size hasn't been determined yet, it retrieves the size directly from the blob object. Returns the integer size of the file.
        *   *Parameters:*
        *   *Returns:*
            -   **size** (`int`): The size of the file in bytes.
        *   **Usage:** This method does not call any other functions. This method is not called by any other functions according to the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* An example analysis method that counts the number of words in the file's content. It splits the content on whitespace and returns the length of the resulting list, effectively counting the words.
        *   *Parameters:*
        *   *Returns:*
            -   **word_count** (`int`): The total number of words in the file's content.
        *   **Usage:** This method does not call any other functions. This method is not called by any other functions according to the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* Provides a useful string representation of the RepoFile object, displaying the file path for debugging and logging purposes.
        *   *Parameters:*
        *   *Returns:*
            -   **repr_string** (`str`): A string representation of the RepoFile object.
        *   **Usage:** This method does not call any other functions. This method is not called by any other functions according to the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content: bool)`
        *   *Description:* Serializes the RepoFile object into a dictionary format. Includes basic file information like path, name, size, and type. Optionally includes the file's content if requested. Uses os.path.basename to extract the filename from the path.
        *   *Parameters:*
            -   **include_content** (`bool`): If True, includes the file's content in the returned dictionary.
        *   *Returns:*
            -   **data** (`dict`): A dictionary containing file metadata and optionally the content.
        *   **Usage:** This method calls os.path.basename to extract the filename from the path. This method is not called by any other functions according to the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory and providing functionality to access files and their hierarchical structure. It supports retrieving all files as RepoFile objects, constructing a file tree representation, and cleaning up the temporary directory upon closing. The class implements context manager protocols (__enter__ and __exit__) to facilitate automatic resource management.
*   **Instantiation:** This class is instantiated by the functions evaluation in HelperLLM_evaluation.py at line 86, prepare_shared_input in MainLLM_evaluation.py at line 116, and main_workflow in main.py at line 141.
*   **Dependencies:** This class depends on several modules including tempfile, shutil, git.Repo, git.GitCommandError, logging, and os.
*   **Constructor:**
    *   *Description:* Initializes a GitRepository instance by cloning the specified repository URL into a temporary directory. It sets up necessary attributes such as the repository URL, temporary directory path, and references to the cloned repository and its latest commit. If cloning fails, it raises a RuntimeError after attempting to clean up resources.
    *   *Parameters:*
        -   **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* Retrieves a list of all files in the repository and creates RepoFile instances for each file. These instances are stored in the internal 'files' attribute and returned. The method uses git ls-files to obtain the file paths and filters out any empty entries.
        *   *Parameters:*
        *   *Returns:*
            -   **list[RepoFile]** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:** This method does not call any other methods internally. This method is called by the function prepare_shared_input in MainLLM_evaluation.py at line 117.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* Deletes the temporary directory and its contents associated with the repository. It also resets the temp_dir attribute to None to indicate that cleanup has occurred.
        *   *Parameters:*
        *   *Returns:*
        *   **Usage:** This method does not call any other methods internally. This method is called by the function prepare_shared_input in MainLLM_evaluation.py at line 136.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* Enables the use of the GitRepository instance in a 'with' statement, returning itself so that it can be used within the context block.
        *   *Parameters:*
        *   *Returns:*
            -   **self** (`GitRepository`): The GitRepository instance itself.
        *   **Usage:** This method does not call any other methods internally. This method is not directly called by any other function according to the provided context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* Implements the context manager protocol's exit behavior by calling the close() method when exiting a 'with' block, ensuring proper cleanup of the temporary directory.
        *   *Parameters:*
            -   **exc_type** (`Any`): Exception type if an exception was raised in the with block.
            -   **exc_val** (`Any`): Exception value if an exception was raised in the with block.
            -   **exc_tb** (`Any`): Exception traceback if an exception was raised in the with block.
        *   *Returns:*
        *   **Usage:** This method does not call any other methods internally. This method is not directly called by any other function according to the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content: bool)`
        *   *Description:* Constructs a hierarchical tree representation of the repository's file structure. If no files have been loaded yet, it retrieves them first. Then, it iterates through each file and builds nested dictionaries reflecting the folder hierarchy, appending each file as a leaf node at the appropriate level.
        *   *Parameters:*
            -   **include_content** (`bool`): Flag indicating whether to include file content in the returned dictionary representation.
        *   *Returns:*
            -   **tree** (`dict`): A dictionary representing the hierarchical file tree structure.
        *   **Usage:** This method does not call any other methods internally. This method is called by the function prepare_shared_input in MainLLM_evaluation.py at line 125.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** Die Funktion erstellt ein Balkendiagramm zur Darstellung des Token-Vergleichs zwischen JSON und TOON Format. Sie verwendet matplotlib zur Erstellung des Diagramms und speichert das Ergebnis in einer Datei. Das Diagramm zeigt die Anzahl der Token für beide Formate sowie den prozentualen Einsparungswert. Die Funktion setzt einen Titel mit dem Einsparungsprozentsatz, fügt eine y-Achsenbeschriftung hinzu und zeigt die Werte über den Balken an.
*   **Parameters:**
    -   **json_tokens** (`int`): Die Anzahl der Token im JSON-Format.
    -   **toon_tokens** (`int`): Die Anzahl der Token im TOON-Format.
    -   **savings_percent** (`float`): Der prozentuale Einsparungswert zwischen den beiden Formaten.
    -   **output_path** (`str`): Der Dateipfad, unter dem das generierte Diagramm gespeichert wird.
*   **Returns:**
*   **Usage:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf. Die Funktion wird von der Funktion 'main_workflow' in der Datei 'main.py' aufgerufen.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items: int, batch_size: int, model_name: str)`
*   **Description:** The function calculates the net time duration between a start and end time, excluding sleep times caused by rate limits. It specifically adjusts the calculation when the model name starts with 'gemini-', applying a correction based on the number of batches and a fixed sleep interval per batch. If the total items count is zero, it returns zero directly. The result is never negative, ensuring a non-negative net time.
*   **Parameters:**
    -   **start_time** (`float or datetime`): The starting timestamp or time value.
    -   **end_time** (`float or datetime`): The ending timestamp or time value.
    -   **total_items** (`int`): The total number of items processed.
    -   **batch_size** (`int`): The size of each processing batch.
    -   **model_name** (`str`): The name of the model being used, which determines whether rate limit adjustments are applied.
*   **Returns:**
    -   **net_time** (`float or int`): The calculated net time after subtracting sleep durations, ensuring a minimum value of zero.
*   **Usage:** This function does not call any other functions internally. This function is called by the evaluation function in HelperLLM_evaluation.py at lines 249 and 275, and by the main_workflow function in main.py at lines 311 and 342.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive code analysis pipeline that processes a GitHub repository input. It begins by extracting API keys and model names, then clones the repository and analyzes its structure. The function performs static analysis on the codebase using various components like AST analyzers, relationship analyzers, and information extractors. It prepares inputs for a helper LLM to analyze functions and classes, and subsequently calls a main LLM to generate a final documentation report. The workflow includes error handling, logging, and performance metrics collection.
*   **Parameters:**
    -   **input** (`Any`): The input containing the repository URL to be analyzed.
    -   **api_keys** (`dict`): A dictionary containing API keys for different services such as Gemini, OpenAI, and SCADsLLM.
    -   **model_names** (`dict`): A dictionary specifying the names of models to be used for helper and main LLMs.
    -   **status_callback** (`Callable[[str], None]`): An optional callback function to report progress updates.
*   **Returns:**
    -   **report** (`str`): The final documentation report generated by the main LLM.
    -   **metrics** (`dict`): Performance metrics including execution times and model names used.
*   **Usage:** This function internally calls several components including GitRepository for cloning repositories, ProjektInfoExtractor for extracting basic project information, ProjectAnalyzer for analyzing relationships, ASTAnalyzer for creating abstract syntax trees, LLMHelper for function and class analysis, and MainLLM for generating the final report. This function is called by both 'frontend.Frontend' in 'Frontend.py' at line 489 and 'backend.main' in 'main.py' at line 533.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The function 'update_status' is designed to handle status updates by invoking an optional callback function if one is defined, followed by logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages throughout the application.
*   **Parameters:**
    -   **msg** (`Any`): The status message to be processed and logged.
*   **Returns:**
*   **Usage:** This function does not call any other functions directly; it relies on an external 'status_callback' variable and the 'logging' module. This function is called multiple times by the 'main_workflow' function in 'main.py', specifically at lines 81, 134, 158, 167, 175, 185, 195, 205, 301, 333, 336, 409, 412, and 430.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles cases where the filepath is not under the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure.
*   **Parameters:**
    -   **filepath** (`str`): The absolute or relative path to a Python file.
    -   **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    -   **module_path** (`str`): A dot-separated module path derived from the given file path.
*   **Usage:** This function does not call any other functions directly. This function is called by _collect_definitions and __init__ methods in relationship_analyzer.py.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is responsible for analyzing Python project structures by identifying definitions (functions, classes, methods) and tracking their interdependencies through call relationships. It recursively scans a given project root directory to find Python files, parses their Abstract Syntax Trees (ASTs) to extract definitions, and resolves function calls between these definitions. The analyzer maintains internal data structures such as a dictionary of definitions and a call graph to store relationships. After processing, it formats and returns the collected information in a structured output.
*   **Instantiation:** This class is instantiated in HelperLLM_evaluation.py, MainLLM_evaluation.py, and main.py.
*   **Dependencies:** This class depends on standard library modules such as ast, os, logging, and collections.defaultdict.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including a dictionary for storing definitions, a defaultdict for maintaining a call graph, and a dictionary for caching ASTs of processed files. Also defines a set of directories to ignore during scanning.
    *   *Parameters:*
        -   **project_root** (`str`): The absolute path to the root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* The main analysis method that orchestrates the process of finding Python files, collecting definitions from those files, resolving call relationships, and formatting the results. It iterates over all Python files in the project, collects definitions and resolves calls for each file, clears cached ASTs after processing, and finally returns formatted results.
        *   *Parameters:*
        *   *Returns:*
            -   **output_list** (`list`): A list of dictionaries containing information about each definition and the callers that reference it.
        *   **Usage:** This method does not explicitly call any other methods defined in the class directly but relies on helper methods like `_find_py_files`, `_collect_definitions`, and `_resolve_calls`. This method is called by functions in HelperLLM_evaluation.py, MainLLM_evaluation.py, and main.py.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* Recursively walks through the project root directory and identifies all Python (.py) files while excluding certain directories such as .git, venv, etc. It returns a list of absolute paths to these Python files.
        *   *Parameters:*
        *   *Returns:*
            -   **py_files** (`list`): A list of absolute file paths to Python source files found in the project.
        *   **Usage:** This method does not call any other methods defined in the class. This method is called by the `analyze` method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath: str)`
        *   *Description:* Parses a given Python file's content into an AST and extracts definitions such as functions, classes, and methods. It associates each definition with metadata like file location and line number. It also handles errors during parsing by logging them and marking the file's AST as None.
        *   *Parameters:*
            -   **filepath** (`str`): The absolute path to the Python file whose definitions need to be collected.
        *   *Returns:*
        *   **Usage:** This method does not call any other methods defined in the class. This method is called by the `analyze` method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* Given an AST node and a tree, this method attempts to find the parent node of the specified node by walking the AST. It is used to determine whether a function or method definition belongs to a class.
        *   *Parameters:*
            -   **tree** (`ast.AST`): The AST tree to search within.
            -   **node** (`ast.AST`): The AST node for which the parent needs to be found.
        *   *Returns:*
            -   **parent** (`ast.AST or None`): The parent AST node of the given node, or None if not found.
        *   **Usage:** This method does not call any other methods defined in the class. This method is called by the `_collect_definitions` method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath: str)`
        *   *Description:* Resolves function calls within a given Python file by using a CallResolverVisitor to traverse the AST and identify calls. It updates the global call graph with the resolved call relationships. Errors during resolution are logged.
        *   *Parameters:*
            -   **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   **Usage:** This method calls the CallResolverVisitor class to resolve calls. This method is called by the `analyze` method.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* Formats the collected definitions and call relationships into a structured list of dictionaries. Each dictionary contains details about a definition and a list of callers that reference it. Duplicate calls are removed, and the result is sorted by file and line number.
        *   *Parameters:*
        *   *Returns:*
            -   **output_list** (`list`): A list of dictionaries representing definitions and their callers, formatted for output.
        *   **Usage:** This method does not call any other methods defined in the class. This method is called by the `analyze` method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to analyze Python code and resolve call relationships between functions and methods. It tracks the current execution context (such as class and function names) and records calls made within the code. Additionally, it maintains scope information for imports and resolves qualified names for function calls. It also tracks instance types to determine the class of objects being instantiated.
*   **Instantiation:** This class is instantiated by the `_resolve_calls` function in the `relationship_analyzer.py` file at line 92.
*   **Dependencies:** No external dependencies are explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and a set of definitions. It sets up internal tracking structures such as scope, instance types, and call records, and determines the module path based on the file path and project root.
    *   *Parameters:*
        -   **filepath** (`str`): The path to the Python file being analyzed.
        -   **project_root** (`str`): The root directory of the project, used to compute relative module paths.
        -   **definitions** (`dict`): A dictionary containing known definitions (functions, classes, etc.) to resolve call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Handles the visiting of class definitions in the AST. It updates the current class name context before traversing the class body and restores the previous class name after traversal.
        *   *Parameters:*
            -   **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Handles the visiting of function definitions in the AST. It updates the current caller name context to the function name before traversing the function body and restores the previous caller name after traversal.
        *   *Parameters:*
            -   **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST. It resolves the qualified name of the called function and records the call if the resolved name exists in the definitions. It also tracks the caller's context (module, method, or function) and stores call metadata including file, line number, and caller information.
        *   *Parameters:*
            -   **node** (`ast.Call`): The AST node representing the function call.
        *   *Returns:*
        *   **Usage:** This method calls the private helper method `_resolve_call_qname` to resolve the qualified name of the function being called. This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST. It adds imported names to the current scope, mapping aliases to their actual names for later resolution.
        *   *Parameters:*
            -   **node** (`ast.Import`): The AST node representing the import statement.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST. It computes the full module path for relative imports and maps imported names to their fully qualified names in the scope.
        *   *Parameters:*
            -   **node** (`ast.ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* Handles assignment statements in the AST. Specifically, it identifies assignments to instances of classes defined in the project and records the class type associated with the assigned variable.
        *   *Parameters:*
            -   **node** (`ast.Assign`): The AST node representing the assignment statement.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call any other methods. This method is called by the generic AST visitor during traversal of the AST.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* A helper method that resolves the qualified name of a function call. It handles both simple names and attribute access (e.g., obj.method). For simple names, it checks the scope and constructs a local qualified name. For attribute access, it uses stored instance types or scope mappings to resolve the full path.
        *   *Parameters:*
            -   **func_node** (`ast.AST`): The AST node representing the function being called.
        *   *Returns:*
            -   **qualified_name** (`str or None`): The fully qualified name of the function, or None if it cannot be resolved.
        *   **Usage:** This method is called by the `visit_Call` method to resolve the qualified name of a function call. This method is called by the `visit_Call` method.

### File: `backend/scads_key_test.py`
*Analysis data not available for this component.*

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** The function encrypts a given text string using a cipher suite, returning the encrypted result as a string. It first checks if the input text is empty or if the cipher suite is not available, in which case it returns the original text unchanged. If both conditions are met, it encodes the stripped text to bytes, encrypts it using the cipher suite, and then decodes the result back to a string.
*   **Parameters:**
    -   **text** (`str`): The text string to be encrypted.
*   **Returns:**
    -   **encrypted_text** (`str`): The encrypted version of the input text, or the original text if encryption was not performed.
*   **Usage:** This function does not call any other functions directly. This function is called by the update_gemini_key function in the db.py file.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** The function decrypts a given text using a cipher suite if available; otherwise, it returns the original text unchanged. It handles potential decryption errors gracefully by returning the original text in case of exceptions. The function performs basic validation to ensure the input text and cipher suite are present before attempting decryption.
*   **Parameters:**
    -   **text** (`str`): The encrypted text to be decrypted.
*   **Returns:**
    -   **return_value** (`str`): The decrypted text if successful, otherwise the original input text.
*   **Usage:** This function does not call any other functions directly. This function is called by get_decrypted_api_keys in db.py at line 93.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** The function inserts a new user into the database by creating a user document with the provided username, name, and password. The password is hashed before being stored. It also initializes additional fields such as API keys and returns the ID of the inserted document.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user, used as the '_id' field in the database.
    -   **name** (`str`): The full name of the user.
    -   **password** (`str`): The plain text password of the user, which gets hashed before storage.
*   **Returns:**
    -   **inserted_id** (`ObjectId`): The unique identifier of the newly inserted user document in the database.
*   **Usage:** This function does not call any other functions directly. This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 294.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user documents from a MongoDB collection named 'dbusers'. It performs a database query using the 'find()' method and returns the results as a list. The function does not accept any parameters and directly accesses a global or module-level variable 'dbusers' which is expected to be a MongoDB collection object.
*   **Parameters:**
*   **Returns:**
    -   **result** (`list`): A list containing all user documents retrieved from the 'dbusers' MongoDB collection.
*   **Usage:** The function does not call any other functions internally. This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 244.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The function fetch_user retrieves a single user document from a MongoDB collection named 'dbusers' based on the provided username. It uses the find_one method to query the database with a filter that matches the '_id' field to the given username. The function assumes the existence of a global or module-level variable 'dbusers' that represents the MongoDB collection. This function serves as a simple data retrieval utility for fetching specific user information.
*   **Parameters:**
    -   **username** (`str`): The unique identifier (username) used to locate and retrieve a specific user document from the MongoDB collection.
*   **Returns:**
    -   **result** (`Any`): A single user document retrieved from the MongoDB collection, or None if no matching document is found.
*   **Usage:** This function internally calls the find_one method on the dbusers collection to perform the database query. This function is not called by any other functions within the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the name field of a user document in a MongoDB collection identified by the username. It uses the MongoDB update_one method to modify only the name field, leaving other fields unchanged. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    -   **username** (`str`): The unique identifier of the user whose name needs to be updated.
    -   **new_name** (`str`): The new name value to set for the specified user.
*   **Returns:**
    -   **result.modified_count** (`int`): The number of documents that were modified as a result of the update operation.
*   **Usage:** The function internally calls the MongoDB update_one method to perform the database update operation. This function is not called by any other functions according to the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database after encrypting it. It takes a username and an unencrypted API key as inputs, strips any leading or trailing whitespace from the key, encrypts it using a helper function, and then updates the corresponding document in the 'dbusers' collection with the encrypted key. The function returns the number of documents modified, which should be 1 if the update was successful.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    -   **gemini_api_key** (`str`): The unencrypted Gemini API key provided by the user, which will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified in the database. This should typically be 1 if the user exists and the update succeeds.
*   **Usage:** This function internally calls 'encrypt_text' to encrypt the provided API key before storing it. This function is called by 'save_gemini_cb' in 'Frontend.py' at line 35 and by 'frontend.Frontend' in 'Frontend.py' at line 393.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and attempts to update the corresponding document in the 'dbusers' collection. The function returns the count of modified documents, which should be 1 if the update was successful or 0 if no matching document was found.
*   **Parameters:**
    -   **username** (`str`): The unique identifier of the user whose Ollama base URL needs to be updated.
    -   **ollama_base_url** (`str`): The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified by the update operation. This will typically be 1 if the user exists, or 0 if no matching user was found.
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
*   **Description:** The function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose Ollama base URL is to be retrieved.
*   **Returns:**
    -   **ollama_base_url** (`str or None`): The Ollama base URL associated with the user, or None if the user is not found.
*   **Usage:** This function does not call any other functions directly; it relies on the pymongo library's find_one method to query the database. This function is not called by any other functions according to the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** The function 'delete_user' removes a user document from a MongoDB collection based on the provided username. It uses the 'delete_one' method to target a specific user by their '_id', which corresponds to the username. The function returns the count of deleted documents, which will be 1 if the user was found and deleted, or 0 if no such user existed.
*   **Parameters:**
    -   **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    -   **deleted_count** (`int`): The number of documents deleted, either 1 if the user was found and removed, or 0 if no matching user was found.
*   **Usage:** This function internally calls 'dbusers.delete_one' to perform the deletion operation in the MongoDB collection. This function is not called by any other functions within the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user does not exist, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function and retrieves the 'ollama_base_url' directly. It then returns both the decrypted Gemini API key and the Ollama base URL.
*   **Parameters:**
    -   **username** (`str`): The unique identifier for the user whose API keys are to be retrieved.
*   **Returns:**
    -   **gemini_plain** (`str`): The decrypted Gemini API key for the user, or an empty string if not found.
    -   **ollama_plain** (`str`): The Ollama base URL for the user, or an empty string if not found.
*   **Usage:** The function internally uses dbusers.find_one to retrieve user data from the database. This function is called by the frontend.Frontend class in Frontend.py at lines 380 and 479.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** The function 'insert_chat' creates a new chat entry in the database with a unique identifier, associated username, chat name, and creation timestamp. It generates a UUID for the chat entry, populates the necessary fields, and inserts the document into the 'dbchats' collection. The function then returns the ID of the inserted document.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat.
    -   **chat_name** (`str`): The name of the chat.
*   **Returns:**
    -   **result.inserted_id** (`str`): The unique identifier of the newly inserted chat document.
*   **Usage:** This function does not call any other functions directly. This function is called by load_data_from_db in Frontend.py at line 81, handle_delete_chat in Frontend.py at line 122, and frontend.Frontend in Frontend.py at line 344.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** Die Funktion fetch_chats_by_user ruft alle Chats eines bestimmten Benutzers aus einer MongoDB-Datenbank ab. Sie verwendet den Benutzernamen als Filterkriterium und sortiert die Ergebnisse nach dem Erstellungsdatum in aufsteigender Reihenfolge. Das Ergebnis ist eine Liste der gefundenen Chat-Dokumente.
*   **Parameters:**
    -   **username** (`str`): Der Benutzername, dessen Chats abgerufen werden sollen.
*   **Returns:**
    -   **chats** (`list`): Eine Liste aller Chat-Dokumente des angegebenen Benutzers, sortiert nach Erstellungsdatum.
*   **Usage:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf. Die Funktion wird von der Funktion load_data_from_db in der Datei Frontend.py aufgerufen.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a query using MongoDB's find_one method to locate a matching document. If a document is found, the function returns True; otherwise, it returns False.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat.
    -   **chat_name** (`str`): The name of the chat to check for existence.
*   **Returns:**
    -   **exists** (`bool`): True if a chat with the specified username and chat name exists, False otherwise.
*   **Usage:** The function internally uses the dbchats.find_one method to query the database. This function is not called by any other functions according to the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and updates all associated exchanges in the database. It first updates the chat entry in the chats collection, then updates all related exchange entries in the exchanges collection. The function returns the number of modified chat documents.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be renamed.
    -   **old_name** (`str`): The current name of the chat to be renamed.
    -   **new_name** (`str`): The new name to assign to the chat.
*   **Returns:**
    -   **modified_count** (`int`): The number of chat documents that were successfully modified.
*   **Usage:** This function does not call any other functions directly. This function is called by the frontend.Frontend function in Frontend.py at line 462.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str = "", main_used: str = "", total_time: str = "", helper_time: str = "", main_time: str = "")`
*   **Description:** This function inserts a new exchange record into a MongoDB collection. It generates a unique ID for the exchange, constructs a dictionary with all the provided details including question, answer, feedback, and metadata, and attempts to insert this record into the database. If the insertion fails, it catches the exception, prints an error message, and returns None. Otherwise, it returns the generated unique ID.
*   **Parameters:**
    -   **question** (`str`): The question associated with the exchange.
    -   **answer** (`str`): The answer provided in response to the question.
    -   **feedback** (`str`): Feedback related to the exchange.
    -   **username** (`str`): The username of the user involved in the exchange.
    -   **chat_name** (`str`): The name of the chat session.
    -   **helper_used** (`str`): The helper component used during the exchange (optional).
    -   **main_used** (`str`): The main component used during the exchange (optional).
    -   **total_time** (`str`): Total time taken for the exchange (optional).
    -   **helper_time** (`str`): Time taken by the helper component (optional).
    -   **main_time** (`str`): Time taken by the main component (optional).
*   **Returns:**
    -   **new_id** (`str`): The unique identifier of the inserted exchange record, or None if insertion failed.
*   **Usage:** The function internally uses the uuid.uuid4() function to generate a unique ID and datetime.now() to set the creation timestamp. This function is called by the frontend.Frontend class in the Frontend.py file at line 530.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses the pymongo library to query the database and returns the results as a list. The sorting ensures that exchanges are displayed chronologically.
*   **Parameters:**
    -   **username** (`str`): The username associated with the exchange records to be fetched.
*   **Returns:**
    -   **exchanges** (`list`): A list of exchange records retrieved from the database, sorted by creation timestamp in ascending order.
*   **Usage:** This function does not call any other functions directly. This function is called by the load_data_from_db function in Frontend.py at line 64.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched documents as a list.
*   **Parameters:**
    -   **username** (`str`): The username associated with the exchanges to be retrieved.
    -   **chat_name** (`str`): The name of the chat associated with the exchanges to be retrieved.
*   **Returns:**
    -   **exchanges** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order.
*   **Usage:** The function does not call any other functions directly. The function is not called by any other functions according to the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** This function updates the feedback field of a document in the 'dbexchanges' collection within a MongoDB database. It takes an exchange ID and a feedback value, then attempts to update the corresponding document with the new feedback value. The function returns the count of modified documents, which should be 1 if the update was successful or 0 if no matching document was found.
*   **Parameters:**
    -   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    -   **feedback** (`int`): The feedback value to be set in the document.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were modified as a result of the update operation.
*   **Usage:** The function internally calls 'dbexchanges.update_one' to perform the database update operation. This function is called by 'handle_feedback_change' in 'Frontend.py'.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** This function updates the feedback message associated with a specific exchange document in a MongoDB collection. It takes an exchange ID and a new feedback message as inputs, then performs an atomic update operation on the database to set the feedback_message field. The function returns the count of modified documents, which should typically be 1 if the update was successful.
*   **Parameters:**
    -   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    -   **feedback_message** (`str`): The new feedback message to be stored in the exchange document.
*   **Returns:**
    -   **modified_count** (`int`): The number of documents that were successfully modified by the update operation.
*   **Usage:** This function does not call any other functions directly; it relies on the external dbexchanges.update_one method. This function is called by the render_exchange function in the Frontend.py file at line 211.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a provided exchange ID. It performs a deletion operation using the 'delete_one' method and returns the count of deleted documents. The function takes a single string parameter representing the unique identifier of the exchange to be deleted.
*   **Parameters:**
    -   **exchange_id** (`str`): A string representing the unique identifier of the exchange document to be deleted from the database.
*   **Returns:**
    -   **deleted_count** (`int`): An integer indicating the number of documents successfully deleted from the database. This will typically be 0 or 1.
*   **Usage:** The function internally calls 'dbexchanges.delete_one' to perform the deletion operation. This function is called by 'handle_delete_exchange' in 'Frontend.py' at line 102.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** The function deletes all exchanges and the chat entry associated with a given username and chat name from the database. It first removes all exchange records matching the criteria, then deletes the corresponding chat record. The function returns the count of deleted chat entries, which should be 1 if the operation was successful.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be deleted.
    -   **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    -   **deleted_count** (`int`): The number of chat documents deleted from the database.
*   **Usage:** This function does not call any other functions directly; it uses database operations from external modules. This function is called by the handle_delete_chat function in the Frontend.py file.

### File: `frontend/Frontend.py`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key for the current user, clears the input field, and displays a success message to the user. The function does not take any parameters and does not return any value.
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function does not call any other functions directly. This function is not called by any other functions according to the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function is designed to save a new Ollama URL entered by the user into the database. It retrieves the URL from the Streamlit session state, checks if it's non-empty, and then updates the database with the new URL associated with the current user. Upon successful update, it displays a success message to the user via a toast notification.
*   **Parameters:**
*   **Returns:**
*   **Usage:** The function internally uses `st.session_state.get` to retrieve the Ollama URL and `db.update_ollama_url` to persist the data. This function is not called by any other function within the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** Die Funktion 'load_data_from_db' lädt Chats und Exchanges konsistent aus einer Datenbank für einen bestimmten Benutzer. Sie prüft zunächst, ob der Benutzer bereits geladen wurde, und lädt nur dann neue Daten, wenn dies erforderlich ist. Zunächst werden Chats aus der Datenbank abgerufen und in den Session-State eingefügt. Anschließend werden Exchanges geladen und den entsprechenden Chats zugeordnet. Bei Bedarf wird ein Standard-Chat erstellt und als aktiv markiert.
*   **Parameters:**
    -   **username** (`str`): Der Name des Benutzers, für den die Daten aus der Datenbank geladen werden sollen.
*   **Returns:**
*   **Usage:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf. Die Funktion wird von der Methode 'frontend.Frontend' in der Datei 'Frontend.py' auf Zeile 310 aufgerufen.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function updates the feedback value for a given exchange object in the database and triggers a re-render of the Streamlit application. It takes an exchange dictionary and a new feedback value, updates the feedback field in the dictionary, saves the updated feedback to the database using the exchange ID, and then refreshes the Streamlit UI.
*   **Parameters:**
    -   **ex** (`dict`): A dictionary representing an exchange object, expected to contain at least '_id' and 'feedback' keys.
    -   **val** (`Any`): The new feedback value to be assigned to the exchange object.
*   **Returns:**
*   **Usage:** This function internally calls 'db.update_exchange_feedback' to update the feedback in the database and 'st.rerun()' to refresh the Streamlit UI. This function is called by the 'render_exchange' function in 'Frontend.py' at lines 199 and 204.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of an exchange from the database and updates the session state accordingly. It first deletes the exchange from the database using its ID, then checks if the exchange exists in the session state for a given chat and removes it if found. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    -   **chat_name** (`str`): The name of the chat from which the exchange should be removed.
    -   **ex** (`dict`): A dictionary representing the exchange to be deleted, expected to contain an '_id' key.
*   **Returns:**
*   **Usage:** This function does not call any other functions directly; it relies on external modules like 'db' and 'st' for database operations and UI updates. This function is called by render_exchange in Frontend.py at lines 228 and 234.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** The function handles the deletion of a chat by first removing the chat from the database and then cleaning up the session state. It ensures that the active chat is updated appropriately, either by switching to another existing chat or creating a new default chat if none remain. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    -   **username** (`str`): The username associated with the chat to be deleted.
    -   **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:** This function does not directly call any other user-defined functions; it relies on external modules like `db` and `st` for database operations and session management. This function is called by the frontend module, specifically from the Frontend class in Frontend.py at line 367.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** The function 'extract_repo_name' takes a text input and attempts to extract a repository name from any URL present in the text. It uses regular expressions to find a URL, parses it using urllib.parse.urlparse, extracts the path component, and then derives the repository name from the last segment of the path. If the repository name ends with '.git', it removes the extension. If no URL is found or the path is empty, it returns None.
*   **Parameters:**
    -   **text** (`str`): A string that may contain a URL from which to extract the repository name.
*   **Returns:**
    -   **repo_name** (`str`): The extracted repository name from the URL, with '.git' suffix removed if present.
    -   **None** (`NoneType`): Returned when no valid URL is found in the input text or when the URL path is empty.
*   **Usage:** This function does not call any other functions directly; it relies on external modules like 're' and 'urllib.parse.urlparse'. This function is called by the 'frontend.Frontend' class, specifically at line 442 in the file 'Frontend.py'.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** The function `stream_text_generator` takes a string of text as input and yields each word in the text followed by a space, with a small delay between each word. This creates a streaming effect where words are produced one at a time. The function uses `time.sleep(0.01)` to introduce a brief pause between yielding each word.
*   **Parameters:**
    -   **text** (`str`): A string containing the text to be streamed word by word.
*   **Returns:**
*   **Usage:** This function does not call any other functions directly. This function is called by the function `render_text_with_mermaid` in the file `Frontend.py` at line 160.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream: bool)`
*   **Description:** This function processes a markdown text string to identify and render Mermaid diagrams embedded within code blocks. It splits the input text based on Mermaid code block delimiters and handles regular markdown content versus Mermaid diagram content differently. For non-Mermaid content, it either streams or displays the text as markdown depending on the streaming flag. For Mermaid content, it attempts to render the diagram using a Mermaid component, falling back to displaying the raw code if rendering fails.
*   **Parameters:**
    -   **markdown_text** (`str`): A string containing markdown-formatted text that may include Mermaid code blocks enclosed in triple backticks with 'mermaid' as the language identifier.
    -   **should_stream** (`bool`): A boolean flag indicating whether to stream the regular markdown text instead of rendering it all at once.
*   **Returns:**
*   **Usage:** The function does not call any other user-defined functions directly; it relies on external libraries such as 're', 'st_mermaid', 'st.write_stream', 'st.markdown', and 'st.code'. This function is called by 'render_exchange' in 'Frontend.py' at line 238 and by 'frontend.Frontend' in 'Frontend.py' at line 524.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name: str)`
*   **Description:** This function renders a chat exchange in a Streamlit interface, displaying a user's question and an assistant's response. It handles both regular responses and error cases, providing interactive feedback mechanisms such as like/dislike buttons, comment popups, download options, and deletion capabilities. The function uses Streamlit components to build a rich UI for each exchange entry.
*   **Parameters:**
    -   **ex** (`dict`): A dictionary containing the exchange data including the question, answer, feedback information, and other metadata.
    -   **current_chat_name** (`str`): The name of the current chat session, used for handling exchange deletions.
*   **Returns:**
*   **Usage:** This function does not directly call any other functions defined within the provided source code. This function is called by the frontend.Frontend class in Frontend.py at line 429.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the metadata of a single function parameter. It encapsulates three essential attributes: the parameter's name, its type, and a descriptive explanation. This class serves as a structured way to define and enforce the shape of parameter descriptions, ensuring consistency and type safety when working with function signatures.
*   **Instantiation:** This class is not directly instantiated by any other components listed in the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* The class is initialized with three required string fields: 'name', 'type', and 'description'. These fields collectively define the essential metadata for describing a function parameter.
    *   *Parameters:*
        -   **name** (`str`): The name of the function parameter.
        -   **type** (`str`): The data type of the function parameter.
        -   **description** (`str`): A human-readable description of the function parameter's purpose or usage.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model designed to represent and validate the description of a function's return value. It encapsulates three essential pieces of information about a return value: its name, type, and a textual description. This class ensures data integrity and structure for return value metadata, making it suitable for use in API documentation, code analysis tools, or any system requiring standardized return value specifications.
*   **Instantiation:** This class is not instantiated by any other components as indicated by the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ReturnDescription instance with a name, type, and description. This constructor leverages Pydantic's BaseModel functionality to enforce type safety and validation for the attributes.
    *   *Parameters:*
        -   **name** (`str`): The name of the return value.
        -   **type** (`str`): The type of the return value.
        -   **description** (`str`): A textual description of the return value.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function, specifically capturing information about what functions are called and by whom. It serves as a structured data container for documenting usage relationships within a codebase.
*   **Instantiation:** This class is not explicitly instantiated by any other components listed in the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the source file.
*   **Constructor:**
    *   *Description:* Initializes a UsageContext instance with two string fields: 'calls' and 'called_by'. These fields are intended to store textual descriptions of the functions being called and the entities that call them, respectively.
    *   *Parameters:*
        -   **calls** (`str`): A string describing the functions or methods that are called within the context.
        -   **called_by** (`str`): A string describing the entity or function that calls the function in question.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate detailed information about a function's purpose, parameters, return values, and usage context. It serves as a structured representation for documenting function signatures and behaviors, making it easier to analyze and communicate function details within a system.
*   **Instantiation:** This class is not instantiated by any other components as indicated in the context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a FunctionDescription instance with fields for overall function description, a list of parameter descriptions, a list of return value descriptions, and usage context information.
    *   *Parameters:*
        -   **overall** (`str`): A string describing the overall purpose and functionality of the function.
        -   **parameters** (`List[schemas.types.ParameterDescription]`): A list of ParameterDescription objects detailing each parameter of the function.
        -   **returns** (`List[schemas.types.ReturnDescription]`): A list of ReturnDescription objects detailing each return value of the function.
        -   **usage_context** (`schemas.types.UsageContext`): An object providing context on how the function is used within the system.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic model designed to represent the complete JSON schema for a function. It serves as a structured data container that holds essential information about a function, including its identifier, a detailed description, and an optional error field. This class is intended to provide a standardized way to encapsulate function metadata and potential errors in a type-safe manner.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The constructor initializes the FunctionAnalysis model with required fields for the function's identifier and description, along with an optional error field that defaults to None.
    *   *Parameters:*
        -   **identifier** (`str`): A string identifier for the function.
        -   **description** (`schemas.types.FunctionDescription`): An instance of FunctionDescription that contains detailed information about the function.
        -   **error** (`Optional[str]`): An optional string field that can hold error messages related to the function.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to represent and validate the description of a class's __init__ method. It encapsulates two key pieces of information: a textual description of the constructor and a list of parameter descriptions that define its inputs. This class serves as a structured way to document and enforce the schema of constructor metadata, making it suitable for use in tools that analyze or generate API documentation, code introspection systems, or automated code generation processes.
*   **Instantiation:** This class is not instantiated by any other component as indicated in the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the source file.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription instance with a description string and a list of ParameterDescription objects.
    *   *Parameters:*
        -   **description** (`str`): A textual description of the __init__ method.
        -   **parameters** (`List[schemas.types.ParameterDescription]`): A list of ParameterDescription objects detailing each parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
*   **Instantiation:** This class is not instantiated by any other component as indicated in the context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the source file.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields are intended to store information about the class's external dependencies and the entities responsible for its instantiation.
    *   *Parameters:*
        -   **dependencies** (`str`): A string describing the external dependencies of the class.
        -   **instantiated_by** (`str`): A string describing the entities or components that instantiate the class.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information. This structure serves as a standardized way to represent detailed metadata and analysis of classes within a codebase.
*   **Instantiation:** This class is not instantiated by any other component mentioned in the provided context.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond those imported in the file.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ClassDescription model with specified attributes for overall purpose, constructor description, methods analysis, and usage context.
    *   *Parameters:*
        -   **overall** (`str`): A string describing the overall purpose and role of the class being analyzed.
        -   **init_method** (`schemas.types.ConstructorDescription`): An instance of ConstructorDescription that contains detailed information about the class's constructor.
        -   **methods** (`List[schemas.types.FunctionAnalysis]`): A list of FunctionAnalysis objects, each representing a method within the class and its associated metadata.
        -   **usage_context** (`schemas.types.ClassContext`): An instance of ClassContext providing information on how the class is used or depends on other components.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential metadata about the class, including its identifier, a detailed description, and an optional error field for capturing any issues during processing. This class is designed to be a structured representation of class information, facilitating consistent serialization and deserialization using Pydantic's validation mechanisms.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysis instance with an identifier string, a ClassDescription object, and an optional error message. The constructor sets up the core attributes required to represent a class's metadata in a standardized format.
    *   *Parameters:*
        -   **identifier** (`str`): A unique string identifier for the class being analyzed.
        -   **description** (`schemas.types.ClassDescription`): An object containing detailed descriptive information about the class.
        -   **error** (`Optional[str]`): An optional string field to store error messages related to class analysis.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for capturing metadata related to code interactions.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** No external dependencies were identified for this class.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo instance with file, function, mode, and line attributes to represent a call event.
    *   *Parameters:*
        -   **file** (`str`): The file path where the call event occurred.
        -   **function** (`str`): The name of the function that made the call.
        -   **mode** (`str`): The mode of the call, such as 'method', 'function', or 'module'.
        -   **line** (`int`): The line number in the file where the call occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing a function. It encapsulates two key pieces of information: a list of function names that the analyzed function calls, and a list of CallInfo objects representing the functions that call the analyzed function. This class serves as a data container to facilitate function analysis and dependency tracking within a codebase.
*   **Instantiation:** This class is instantiated in three different functions across multiple files: 'evaluation' in HelperLLM_evaluation.py at line 162, 'prepare_shared_input' in MainLLM_evaluation.py at line 156, and 'main_workflow' in main.py at line 223.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes the FunctionContextInput instance with two attributes: 'calls', which is a list of strings representing function names called by the analyzed function, and 'called_by', which is a list of CallInfo objects representing functions that call the analyzed function.
    *   *Parameters:*
        -   **calls** (`List[str]`): A list of strings representing the names of functions called by the analyzed function.
        -   **called_by** (`List[schemas.types.CallInfo]`): A list of CallInfo objects representing the functions that call the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for function analysis, including the mode of operation, identifier, source code, imports, and associated context.
*   **Instantiation:** The class is instantiated by functions in HelperLLM_evaluation.py, MainLLM_evaluation.py, and main.py, specifically in the evaluation, prepare_shared_input, and main_workflow functions respectively.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput instance with fields defining the analysis mode, identifier, source code, imports list, and context. It sets up the foundational structure needed for function analysis workflows.
    *   *Parameters:*
        -   **mode** (`Literal["function_analysis"]`): A literal string indicating the mode of operation for the analysis, constrained to the value 'function_analysis'.
        -   **identifier** (`str`): A string identifier for the function being analyzed.
        -   **source_code** (`str`): The raw source code of the function to be analyzed.
        -   **imports** (`List[str]`): A list of import statements used within the function's source code.
        -   **context** (`schemas.types.FunctionContextInput`): An object containing contextual information related to the function analysis.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent and exchange metadata about method usage and dependencies in a structured format.
*   **Instantiation:** The class is instantiated in three different functions across multiple files: HelperLLM_evaluation.py at line 187 in the evaluation function, MainLLM_evaluation.py at line 181 in the prepare_shared_input function, and main.py at line 248 in the main_workflow function.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The class is initialized with a set of predefined attributes including identifier, calls, called_by, args, and docstring. These attributes are typed using Pydantic's type hints and optional types to enforce data integrity.
    *   *Parameters:*
        -   **identifier** (`str`): A string identifier for the method.
        -   **calls** (`List[str]`): A list of strings representing the identifiers of methods called by this method.
        -   **called_by** (`List[schemas.types.CallInfo]`): A list of CallInfo objects representing the methods that call this method.
        -   **args** (`List[str]`): A list of strings representing the argument names of the method.
        -   **docstring** (`Optional[str]`): An optional string containing the docstring of the method.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to structure contextual information about a class being analyzed. It encapsulates three key pieces of information: a list of dependencies, a list of CallInfo objects indicating where the class is instantiated, and a list of MethodContextInput objects detailing the context of each method within the class.
*   **Instantiation:** The class is instantiated by the functions main_orchestrator in HelperLLM.py, evaluation in HelperLLM_evaluation.py, prepare_shared_input in MainLLM_evaluation.py, and main_workflow in main.py.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond its declared imports.
*   **Constructor:**
    *   *Description:* The constructor initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are expected to hold lists of strings, CallInfo objects, and MethodContextInput objects respectively.
    *   *Parameters:*
        -   **dependencies** (`List[str]`): A list of string identifiers representing the dependencies of the class.
        -   **instantiated_by** (`List[schemas.types.CallInfo]`): A list of CallInfo objects describing where and how the class is instantiated.
        -   **method_context** (`List[schemas.types.MethodContextInput]`): A list of MethodContextInput objects providing context for each method within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class serves as a structured input model for generating a ClassAnalysis object. It encapsulates all necessary information required for analyzing a Python class, including its source code, import statements, and contextual metadata such as instantiation details and dependencies.
*   **Instantiation:** The class is instantiated by multiple functions across different files including main_orchestrator in HelperLLM.py, evaluation in HelperLLM_evaluation.py, prepare_shared_input in MainLLM_evaluation.py, and main_workflow in main.py.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic components.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysisInput instance with fields representing the mode of analysis, the identifier of the class being analyzed, the source code of the class, a list of import statements, and contextual information about how the class is used.
    *   *Parameters:*
        -   **mode** (`Literal["class_analysis"]`): A literal string indicating the mode of analysis, specifically set to "class_analysis".
        -   **identifier** (`str`): A string identifier for the class being analyzed.
        -   **source_code** (`str`): The raw source code of the class to be analyzed.
        -   **imports** (`List[str]`): A list of import statements associated with the class.
        -   **context** (`schemas.types.ClassContextInput`): An object containing contextual information about the class, such as dependencies and instantiation points.
*   **Methods:**

---
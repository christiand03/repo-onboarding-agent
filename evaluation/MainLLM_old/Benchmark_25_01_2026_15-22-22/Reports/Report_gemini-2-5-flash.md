# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** The project appears to be an AI-powered "Repo Onboarding Agent" designed to automate the generation of technical documentation for software repositories. It leverages various Large Language Models (LLMs) like Google Gemini, OpenAI, and Ollama to analyze code, extract architectural information, and synthesize comprehensive reports. The agent likely includes capabilities for cloning repositories, parsing Abstract Syntax Trees (ASTs), identifying relationships (calls, instantiations), and integrating with a database for user and chat management, possibly fronted by a Streamlit-based interactive user interface.
- **Key Features:**
  - AI-driven code analysis and documentation generation.
  - Support for multiple Large Language Models (Gemini, OpenAI, Ollama).
  - Automated repository cloning and file processing.
  - Extraction of project metadata, file structure, and code relationships (AST, call graphs).
  - Interactive Streamlit frontend for user interaction and report display.
- **Tech Stack:** Python, Streamlit, LangChain, Google Gemini, OpenAI, Ollama, MongoDB (pymongo), GitPython, NetworkX, Pydantic, TOON format.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root_dir["root<br/>.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json"]
    root_dir --> SystemPrompts["SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt"]
    root_dir --> backend["backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py"]
    root_dir --> database["database<br/>db.py"]
    root_dir --> frontend["frontend<br/>__init__.py<br/>frontend.py"]
    frontend --> frontend_streamlit[".streamlit<br/>config.toml"]
    frontend --> gifs["gifs<br/>4j.gif"]
    root_dir --> notizen["notizen<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
    notizen --> grafiken["grafiken"]
    grafiken --> grafiken_1["1<br/>File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
    grafiken --> grafiken_2["2<br/>FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot"]
    grafiken --> Flask_Repo["Flask-Repo<br/>__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot"]
    grafiken --> Repo_onboarding["Repo-onboarding<br/>AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot"]
    root_dir --> result["result<br/>ast_schema_01_12_2025_11-49-24.json<br/>notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
    root_dir --> schemas["schemas<br/>types.py"]
    root_dir --> statistics["statistics<br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png"]
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
**Note:** A `requirements.txt` file is present. You can install dependencies using: `pip install -r requirements.txt`

### Setup Guide
Information not found

### Quick Startup
Information not found

## 3. Use Cases & Commands
This Repo Onboarding Agent facilitates several key use cases:

*   **Automated Repository Documentation:** Users can provide a GitHub repository URL, and the agent will automatically clone it, analyze the code structure, identify functions, classes, and their relationships, and generate a comprehensive markdown-based documentation report. This report serves as an excellent starting point for new team members onboarding onto a project.
*   **Multi-LLM Powered Analysis:** The agent allows selection from various Large Language Models (Gemini, OpenAI, Ollama, custom SCADSLLM) for performing code analysis, enabling flexibility and potentially leveraging different models' strengths for specific codebases or documentation styles.
*   **Interactive Documentation Exploration:** With its Streamlit frontend, the agent likely provides an interactive environment where users can view generated reports, manage chat sessions, and provide feedback on the AI-generated content, enhancing the documentation process.
*   **API Key Management:** Users can securely store and manage their API keys for different LLM services within the integrated database, ensuring personalized and secure access to AI capabilities.

**Primary Commands/Interactions:**

*   **To Initiate Documentation Generation:** (Inferred from frontend/backend interaction)
    *   Provide a GitHub repository URL via the Streamlit interface.
    *   Select preferred Helper and Main LLM models.
    *   Trigger the analysis, which will clone the repo, analyze code, and generate a report.
*   **To Manage API Keys:**
    *   Access the settings/configuration section in the Streamlit UI.
    *   Input and save API keys for Gemini, GPT, Ollama, and custom SCADSLLMs.
*   **To Navigate Generated Reports:**
    *   Use the Streamlit interface to browse past reports and chat history.
    *   Interact with feedback mechanisms (like/dislike) for generated answers.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into a Python module path string. It first attempts to determine the relative path from a specified project root, falling back to the base filename if a relative path cannot be established. It then removes the '.py' extension if present and replaces directory separators with dots. Finally, it handles '__init__.py' files by removing the '.__init__' suffix to correctly represent the package.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a file that needs to be converted to a module path.
    - **project_root** (`str`): The root directory of the project, used as a reference to calculate the relative path for the module.
*   **Returns:**
    - **module_path** (`str`): The Python module path string derived from the input filepath.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends ast.NodeVisitor to systematically traverse an Abstract Syntax Tree (AST) and extract structured information about imports, functions, and classes from Python source code. It populates an internal schema dictionary with details such as identifiers, docstrings, and source code segments for each encountered element. The visitor manages context, like the current module path and the class being processed, to accurately scope and identify nested elements like methods and functions. This class serves as a foundational component for static code analysis, providing a structured representation of a Python file's contents.
*   **Instantiation:** It is not explicitly known where this class is instantiated within the provided context.
*   **Dependencies:** The ASTVisitor class depends on the 'ast' module for its core functionality, inheriting from ast.NodeVisitor and utilizing functions like ast.get_docstring and ast.get_source_segment. It also implicitly depends on a 'path_to_module' function, which is called during initialization.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor instance with the raw source code, the file's absolute path, and the project's root directory. It calculates the module's relative path and sets up an empty schema dictionary to store parsed imports, functions, and classes. An internal attribute, `_current_class`, is also initialized to `None` to track the class currently being visited during AST traversal.
    *   *Parameters:*
        - **self** (`ASTVisitor`): The instance of the class.
        - **source_code** (`str`): The raw source code of the Python file being analyzed.
        - **file_path** (`str`): The absolute file path to the Python file.
        - **project_root** (`str`): The root directory of the entire project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method is invoked by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered during AST traversal. It iterates through each alias within the import statement, extracting the module name. Each identified module name is then appended to the 'imports' list within the visitor's `schema` dictionary. Finally, it calls `self.generic_visit(node)` to ensure that the traversal continues to any child nodes.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an 'import' statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls self.generic_visit(node).
            *   **Called By:** This method is called by the ast.NodeVisitor framework when an ast.Import node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to 'from ... import ...' statements in Python. It processes each alias within the import statement, constructing a fully qualified name by combining the module name from the node with the alias name. This fully qualified import string is then added to the 'imports' list within the visitor's `schema`. The method concludes by calling `self.generic_visit(node)` to ensure proper traversal of any nested nodes.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls self.generic_visit(node).
            *   **Called By:** This method is called by the ast.NodeVisitor framework when an ast.ImportFrom node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is responsible for processing `ast.ClassDef` nodes, representing class definitions in the source code. It constructs a unique identifier for the class using the module path and class name, then gathers essential information such as the class's name, docstring, and its exact source code segment. This collected data is stored in a `class_info` dictionary, which is then appended to the 'classes' list in the visitor's `schema`. The method temporarily sets `_current_class` to this `class_info` to correctly scope nested methods, performs a generic visit for child nodes, and finally resets `_current_class` to `None`.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls ast.get_docstring(node), ast.get_source_segment(self.source_code, node), and self.generic_visit(node).
            *   **Called By:** This method is called by the ast.NodeVisitor framework when an ast.ClassDef node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, distinguishing between methods defined within a class and standalone functions. If a class is currently being visited (indicated by `_current_class`), it extracts method-specific details like its identifier, name, arguments, docstring, and line numbers, appending this information to the `method_context` of the current class. Otherwise, for standalone functions, it gathers similar details and appends them to the 'functions' list in the visitor's `schema`. The method ensures continued AST traversal by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition (either a standalone function or a class method).
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls ast.get_docstring(node), ast.get_source_segment(self.source_code, node) (for standalone functions), and self.generic_visit(node).
            *   **Called By:** This method is called by the ast.NodeVisitor framework when an ast.FunctionDef node is encountered during AST traversal, and also by visit_AsyncFunctionDef.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is designed to handle `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. To avoid code duplication and ensure consistent processing, it delegates the entire analysis of the asynchronous function directly to the `visit_FunctionDef` method. This approach ensures that both synchronous and asynchronous functions are processed uniformly, collecting their metadata into the visitor's schema.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls self.visit_FunctionDef(node).
            *   **Called By:** This method is called by the ast.NodeVisitor framework when an ast.AsyncFunctionDef node is encountered during AST traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to perform static analysis on a Python codebase, focusing on building an Abstract Syntax Tree (AST) schema and integrating relationship data. It processes a collection of files from a repository, parses their Python content, and extracts structural information like functions, classes, and imports. Furthermore, it enriches this AST schema by merging call graph data, identifying incoming/outgoing calls for functions and methods, and determining class-level dependencies.
*   **Instantiation:** This class is not explicitly instantiated by any known entities in the provided context.
*   **Dependencies:** The class does not explicitly declare any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It currently performs no specific setup or attribute assignments, serving as a placeholder or indicating that the class's state is managed entirely through its methods.
    *   *Parameters:*
        - **self** (`ASTAnalyzer`): The instance of the class.
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates relationship data (incoming and outgoing calls) into a pre-existing AST schema. It iterates through files, functions, and classes within the `full_schema`, populating their respective 'calls', 'called_by', and 'instantiated_by' contexts using information from `raw_relationships`. Additionally, it identifies and lists external dependencies for each class based on its methods' outgoing calls.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): A dictionary representing the complete AST schema of the repository, including files, functions, and classes.
            - **raw_relationships** (`dict`): A dictionary containing raw incoming and outgoing call relationships for various identifiers.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary with integrated relationship data.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other functions or methods.
            *   **Called By:** This method is not explicitly called by any other functions or methods in the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to build a comprehensive AST schema. It filters for Python files, parses their content using the `ast` module, and then uses an `ASTVisitor` to extract structured AST nodes (imports, functions, classes). The extracted schema for each file is then added to a `full_schema` dictionary, handling potential parsing errors.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): A list of file objects, each expected to have `path` and `content` attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though its direct attributes are not accessed in the provided method body.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the entire repository, structured by file paths.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other functions or methods.
            *   **Called By:** This method is not explicitly called by any other functions or methods in the provided context.

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and creates an instance of a `FileDependencyGraph` visitor. The visitor then traverses the provided AST to collect import relationships. Finally, the function populates the graph with nodes for files and edges representing these import dependencies, returning the complete dependency graph.
*   **Parameters:**
    - **filename** (`str`): The path to the file being analyzed for dependencies.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph representing the file import dependencies.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by other functions in the provided context.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a directed graph representing dependencies across an entire Git repository. It iterates through all Python files within the provided repository, parsing each file's content into an Abstract Syntax Tree (AST). For each file, it builds a local dependency graph using a helper function and then integrates the nodes and edges from these local graphs into a single, global NetworkX directed graph. The final graph illustrates the relationships between various components (e.g., functions, classes) found across the repository's Python files.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object representing the code repository to be analyzed for dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent code components (e.g., files, functions, classes) and edges represent dependencies between them across the entire repository.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and converts it into an absolute `Path` object. The function then recursively searches for all files ending with the ".py" extension. Finally, it returns a list of these Python files, with each file's path represented as a `Path` object relative to the initial input directory.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory from which to start searching for Python files.
*   **Returns:**
    - **all_files** (`list[pathlib.Path]`): A list of `pathlib.Path` objects, where each path is relative to the input `directory`, representing all found Python files.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends NodeVisitor to analyze Python source code and build a graph of file-level import dependencies. It processes import statements, resolving both absolute and relative imports to identify which files depend on others. The class maintains a dictionary, `import_dependencies`, to store these relationships, mapping a filename to a set of files it imports.
*   **Instantiation:** This class has no explicitly listed instantiation points in the provided context.
*   **Dependencies:** This class has no explicitly listed external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the FileDependencyGraph instance with the path to the current file being analyzed and the root directory of the repository. These paths are stored as instance attributes to be used during the dependency resolution process.
    *   *Parameters:*
        - **self** (`FileDependencyGraph`): The instance of the class.
        - **filename** (`str`): The path to the Python file currently being analyzed for dependencies.
        - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths and locating files.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ImportFrom)`
        *   *Description:* This method is responsible for resolving relative import statements (e.g., `from .. import name`). It calculates the correct base directory based on the import level and then checks if the imported names correspond to existing module files or symbols exported by `__init__.py` files. It uses two nested helper functions, `module_file_exists` and `init_exports_symbol`, to perform these checks. If no modules or symbols can be resolved, an `ImportError` is raised.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            - **resolved_names** (`list[str]`): A list of resolved module or symbol names that actually exist.
        *   **Usage:**
            *   **Calls:** This method does not make any external calls according to the provided context.
            *   **Called By:** This method is not explicitly called by other methods within the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* This method is part of the AST NodeVisitor pattern and is invoked for `Import` and `ImportFrom` nodes. Its primary function is to record the detected import dependencies. It adds the imported module or symbol name to the `import_dependencies` dictionary, associating it with the current file being analyzed. It then calls `generic_visit` to continue traversing the AST.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`Import | ImportFrom`): The AST node representing an import statement.
            - **base_name** (`str | None`): An optional base name for the import, typically used for `from ... import ...` statements where the module name is explicitly provided.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method does not make any external calls according to the provided context.
            *   **Called By:** This method is not explicitly called by other methods within the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
        *   *Description:* This method is a specialized visitor for `ImportFrom` AST nodes. It distinguishes between absolute and relative imports. For absolute imports (where `node.module` is present), it extracts the last part of the module name and passes it to `visit_Import`. For relative imports (where `node.module` is `None`), it calls `_resolve_module_name` to determine the actual module paths, handling potential `ImportError` exceptions by printing a message. Finally, it ensures the AST traversal continues by calling `generic_visit`.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method does not make any external calls according to the provided context.
            *   **Called By:** This method is not explicitly called by other methods within the provided context.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy orchestrator for testing the LLMHelper class. It defines pre-computed analysis inputs and outputs for several example functions, such as 'add_item', 'check_stock', and 'generate_report'. It also sets up a ClassAnalysisInput for an 'InventoryManager' class, incorporating the pre-computed function analyses. The orchestrator then initializes an LLMHelper instance and simulates the process of generating documentation for these functions. Finally, it aggregates and prints the simulated documentation results.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs) to generate structured documentation for Python functions and classes. It handles the configuration of different LLM providers (Gemini, OpenAI, custom, Ollama), manages system prompts, and implements batch processing with rate limiting. The class ensures that LLM outputs conform to predefined Pydantic schemas for FunctionAnalysis and ClassAnalysis, streamlining the documentation generation workflow.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** The class depends on `logging` for output, `time` for rate limiting, `json` for serialization, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI` for LLM integrations, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage` for conversation construction, and `schemas.types.FunctionAnalysis`, `schemas.types.ClassAnalysis`, `schemas.types.FunctionAnalysisInput`, `schemas.types.ClassAnalysisInput` for structured input/output. It also implicitly depends on `SCADSLLM_URL` and `OLLAMA_BASE_URL` environment variables for certain model types.
*   **Constructor:**
    *   *Description:* This constructor initializes the LLMHelper with the necessary API key, paths to system prompt files for function and class analysis, and optional model configuration. It loads the system prompts from the specified files, configures the appropriate LLM client (Gemini, OpenAI, custom, or Ollama) based on the model name, and sets up structured output parsers. It also calls a private method to configure batch processing settings based on the chosen model.
    *   *Parameters:*
        - **self** (`LLMHelper`): The instance of the class.
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **function_prompt_path** (`str`): The file path to the system prompt used for generating function documentation.
        - **class_prompt_path** (`str`): The file path to the system prompt used for generating class documentation.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
        - **base_url** (`str`): An optional base URL for custom or Ollama LLM endpoints.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* This private method dynamically sets the `batch_size` attribute for the LLMHelper instance based on the provided model name. It contains a series of conditional statements to assign specific batch sizes optimized for different LLM models, including various Gemini, Llama, and GPT versions, as well as custom or alias models. If the model name is not explicitly recognized, it logs a warning and assigns a conservative default batch size.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **model_name** (`str`): The name of the LLM model for which batch processing settings need to be configured.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods or functions within its body, beyond standard Python operations.
            *   **Called By:** This method is called by the `__init__` method of the `LLMHelper` class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* This method generates and validates documentation for a batch of functions using the configured LLM. It takes a list of FunctionAnalysisInput objects, converts them into JSON payloads, and constructs conversations with the `function_system_prompt`. The method then processes these conversations in batches, calling the `function_llm.batch` method, and includes a waiting period between batches to respect API rate limits. Any errors encountered during batch processing result in `None` being added to the results for the corresponding input.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing details of a function for which documentation is to be generated.
        *   *Returns:*
            - **null** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, where each object represents the generated documentation for a function, or `None` if an error occurred during its processing.
        *   **Usage:**
            *   **Calls:** This method calls `json.dumps` for serialization, `SystemMessage` and `HumanMessage` to build LLM conversations, `self.function_llm.batch` to execute batch LLM calls, `logging.info` and `logging.error` for logging, and `time.sleep` for rate limiting.
            *   **Called By:** This method is not explicitly called by other methods within the provided `method_context`.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* This method is responsible for generating and validating documentation for a batch of classes using the configured LLM. It accepts a list of `ClassAnalysisInput` objects, serializes them into JSON payloads, and prepares them as `SystemMessage` and `HumanMessage` conversations using the `class_system_prompt`. The method then iterates through these conversations in batches, invoking `self.class_llm.batch` to obtain LLM responses. It incorporates error handling for batch calls and a `time.sleep` mechanism to manage API rate limits, ultimately returning a list of `ClassAnalysis` objects or `None` for inputs that failed during processing.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing details of a class for which documentation is to be generated.
        *   *Returns:*
            - **null** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, where each object represents the generated documentation for a class, or `None` if an error occurred during its processing.
        *   **Usage:**
            *   **Calls:** This method calls `json.dumps` for serialization, `SystemMessage` and `HumanMessage` to build LLM conversations, `self.class_llm.batch` to execute batch LLM calls, `logging.info` and `logging.error` for logging, and `time.sleep` for rate limiting.
            *   **Called By:** This method is not explicitly called by other methods within the provided `method_context`.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a central interface for interacting with various large language models (LLMs). It abstracts away the specifics of different LLM providers (Gemini, OpenAI, Ollama, or custom APIs) by dynamically configuring the appropriate client based on the model name. The class manages a system prompt loaded from a file and provides methods for both direct (blocking) and streaming interactions with the chosen LLM, ensuring robust error handling for communication.
*   **Instantiation:** This class is not explicitly instantiated by other functions or methods in the provided context.
*   **Dependencies:** The class depends on external libraries such as langchain_google_genai, langchain_ollama, langchain_openai, and langchain.messages for LLM integration, as well as logging for operational insights. It also relies on environment variables like SCADSLLM_URL and OLLAMA_BASE_URL for custom API configurations.
*   **Constructor:**
    *   *Description:* This constructor initializes the MainLLM instance by setting up the system prompt from a specified file and configuring the appropriate LLM client based on the provided model name. It supports various LLM providers like Google Generative AI, OpenAI, and Ollama, handling their respective API keys and base URLs. The method also includes validation for the API key and prompt file path.
    *   *Parameters:*
        - **self** (`MainLLM`): The instance of the class.
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **prompt_file_path** (`str`): The file path to the system prompt that will be used for all LLM interactions.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.5-pro'.
        - **base_url** (`str`): An optional base URL for custom LLM API endpoints, if applicable.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* This method sends a user's input along with the pre-configured system prompt to the initialized LLM for a single, blocking response. It constructs a list of messages, invokes the LLM, logs the process, and returns the content of the LLM's response. The method includes error handling to catch and report exceptions during the LLM call, returning None in case of failure.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the class.
            - **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:*
            - **content** (`str`): The text content of the LLM's response, or None if an error occurred.
        *   **Usage:**
            *   **Calls:** This method calls SystemMessage, HumanMessage, self.llm.invoke, logging.info, and logging.error.
            *   **Called By:** This method is not explicitly called by other functions or methods in the provided context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* This method streams the LLM's response for a given user input, allowing for real-time processing of the output. It constructs messages similar to call_llm but utilizes the stream method of the LLM client, yielding each chunk of content as it becomes available. The method also incorporates error handling for streaming operations, yielding an error message if an exception occurs.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the class.
            - **user_input** (`str`): The user's query or message for which to stream the LLM response.
        *   *Returns:*
            - **chunk.content** (`str`): Yields individual text chunks from the LLM's streaming response.
            - **error_message** (`str`): Yields an error message if an exception occurs during streaming.
        *   **Usage:**
            *   **Calls:** This method calls SystemMessage, HumanMessage, self.llm.stream, logging.info, and logging.error.
            *   **Called By:** This method is not explicitly called by other functions or methods in the provided context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to systematically extract and consolidate essential project information from various common project files and a repository URL. It acts as a central intelligence unit for gathering metadata such as project title, description, features, tech stack, installation instructions, and dependencies. By prioritizing information sources (e.g., pyproject.toml over requirements.txt for dependencies), it ensures a robust and consistent data collection process, ultimately providing a comprehensive overview of a project.
*   **Instantiation:** The class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context, but it internally relies on the 're' module for regular expressions, the 'os' module for path manipulation, and the 'tomllib' module for TOML parsing.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjektInfoExtractor instance by setting a default 'Information not found' string and establishing the self.info dictionary structure. This dictionary serves as a container for all extracted project details, pre-filled with placeholder values to indicate missing information.
    *   *Parameters:* None
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content: str)`
        *   *Description:* This private utility method is responsible for sanitizing string content by removing null bytes (\x00). Null bytes can appear due to encoding errors, such as reading UTF-16 encoded files as UTF-8, and can interfere with text processing. The method ensures that the content is clean before further parsing by replacing all occurrences of null bytes with an empty string.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **content** (`str`): The input string content to be cleaned.
        *   *Returns:*
            - **null** (`str`): The cleaned string content with null bytes removed, or an empty string if the input content was empty.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions or methods, performing only string manipulation.
            *   **Called By:** This method is called by _parse_readme, _parse_toml, and _parse_requirements to preprocess file contents.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This private helper method searches through a list of file objects to find one whose path matches any of the provided patterns. The search is case-insensitive, making it robust to variations in file naming conventions. It iterates through each file and each pattern, returning the first file object that satisfies a match or None if no match is found after checking all possibilities.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **patterns** (`List[str]`): A list of string patterns (e.g., file extensions or names) to match against file paths.
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have a 'path' attribute.
        *   *Returns:*
            - **null** (`Optional[Any]`): The first file object that matches a pattern, or None if no match is found.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions or methods, performing only string and list operations.
            *   **Called By:** This method is called by extrahiere_info to locate specific project files like READMEs, pyproject.toml, and requirements.txt.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This private method extracts content from a Markdown string that appears under a level 2 heading (##). It takes a list of keywords and constructs a regular expression to find any of these keywords in an H2 heading. The method then captures all text following that heading until the next H2 heading or the end of the document, returning the stripped content if a match is found.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The Markdown content string to parse.
            - **keywords** (`List[str]`): A list of keywords to match against Markdown H2 headings.
        *   *Returns:*
            - **null** (`Optional[str]`): The stripped content found under the matched Markdown H2 heading, or None if no matching section is found.
        *   **Usage:**
            *   **Calls:** This method calls re.escape to prepare keywords for regex, re.compile to create a regex pattern, and re.search to find the pattern in the content.
            *   **Called By:** This method is called by _parse_readme to extract specific sections like features, tech stack, status, installation instructions, and quick start guides.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This private method processes the content of a README file to populate various project information fields within the self.info dictionary. It first cleans the content, then attempts to extract the project title from an H1 heading and a general description. Subsequently, it utilizes _extrahiere_sektion_aus_markdown to find and extract specific sections like 'Features', 'Tech Stack', 'Status', 'Installation', and 'Quick Start' based on predefined keywords.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the README file as a string.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls _clean_content to sanitize the input, re.search for title and description extraction, and _extrahiere_sektion_aus_markdown for extracting specific sections.
            *   **Called By:** This method is called by extrahiere_info after a README file has been identified.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project-related metadata. It first cleans the content and then attempts to load it using the tomllib module. If tomllib is not available or a decoding error occurs, it prints a warning. Upon successful parsing, it extracts the project name, description, and dependencies from the '[project]' section and updates the self.info dictionary.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the pyproject.toml file as a string.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls _clean_content for content sanitization, tomllib.loads to parse TOML content, and data.get to safely access dictionary keys.
            *   **Called By:** This method is called by extrahiere_info if a pyproject.toml file is found.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This private method processes the content of a requirements.txt file to extract project dependencies. It first cleans the content. It only populates the dependencies field in self.info if it hasn't already been filled by a pyproject.toml file, ensuring that pyproject.toml takes precedence. It filters out empty lines and comments before storing the dependencies as a list.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the requirements.txt file as a string.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls _clean_content to sanitize the input content.
            *   **Called By:** This method is called by extrahiere_info if a requirements.txt file is found.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This is the main public method of the class, orchestrating the entire information extraction process. It first uses _finde_datei to locate README, pyproject.toml, and requirements.txt files within a provided list of file objects. It then parses these files in a prioritized order (pyproject.toml first, then requirements.txt, then README) to populate the self.info dictionary. Finally, it formats the extracted dependencies and attempts to derive a project title from the repo_url if no title was found in the files, returning the complete information dictionary.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have 'path' and 'content' attributes.
            - **repo_url** (`str`): The URL of the repository, used as a fallback for the project title.
        *   *Returns:*
            - **null** (`Dict[str, Any]`): A dictionary containing all extracted project information.
        *   **Usage:**
            *   **Calls:** This method calls _finde_datei to locate files, _parse_toml, _parse_requirements, and _parse_readme to process file contents. It also uses os.path.basename and string methods like removesuffix to process the repository URL.
            *   **Called By:** This is the primary public method, expected to be called by external components to initiate project information extraction.

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and an output file path, then generates a 'safe' DOT file representation of the graph. It achieves this by creating a copy of the input graph and relabeling its nodes with generic, safe identifiers (e.g., 'n0', 'n1'). The original node names are preserved by assigning them as 'label' attributes to the new safe nodes. Finally, the modified graph, with sanitized node names, is written to the specified output path using the NetworkX pydot drawing utility.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph object to be converted into a safe DOT file format.
    - **out_path** (`str`): The file path where the sanitized DOT graph representation will be saved.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** This function constructs a filtered call graph for a given Git repository. It first iterates through all Python files in the repository to identify and collect all functions defined within the project's own codebase. Subsequently, it re-processes these files to detect function calls. A NetworkX directed graph is then built, where edges are added exclusively between functions that were previously identified as belonging to the project's own code. The final graph represents the internal call structure, focusing only on self-written functions.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object containing the source code files to be analyzed.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions defined within the repository's own Python files.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST visitor designed to construct a directed call graph for a given Python source file. It traverses the Abstract Syntax Tree, identifying function and class definitions, import statements, and function calls. The class maintains context about the current function and class to accurately resolve full names of callers and callees, ultimately building a graph of dependencies between functions and methods.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components in the provided context.
*   **Dependencies:** This class depends on the `ast` module for parsing Python code and the `networkx` library for graph manipulation.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph instance by setting the filename and various internal state variables required for graph construction. These include tracking the current function and class context, local definitions, import mappings, a NetworkX graph object, a set of discovered functions, and a dictionary to store call edges.
    *   *Parameters:*
        - **self** (`CallGraph`): The instance of the class.
        - **filename** (`str`): The path to the Python file being analyzed.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node: ast.AST)`
        *   *Description:* This private helper method recursively extracts the name components from an Abstract Syntax Tree node representing a call, name, or attribute access. It breaks down complex expressions like `obj.method()` or `module.submodule.function` into a list of strings, such as `['module', 'submodule', 'function']`, which are then used for name resolution.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.AST`): The Abstract Syntax Tree node to analyze, typically an `ast.Call`, `ast.Name`, or `ast.Attribute`.
        *   *Returns:*
            - **parts** (`list[str]`): A list of strings representing the dotted name components of the entity being called.
        *   **Usage:**
            *   **Calls:** This method calls itself recursively to process nested AST nodes.
            *   **Called By:** This method is called by `visit_Call` to extract callee name components.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* This private method takes a list of potential callee name components and resolves them into fully qualified names. It prioritizes resolution by first checking local definitions, then import mappings, and finally constructs a full path based on the current filename and class context. This ensures that calls to local functions, imported modules, or methods within the current class are correctly identified.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **callee_nodes** (`list[list[str]]`): A list where each inner list represents the name components of a potential callee, e.g., `[['module', 'function']]`.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of fully qualified names for the resolved callees.
        *   **Usage:**
            *   **Calls:** This method accesses `self.local_defs`, `self.import_mapping`, `self.current_class`, and `self.filename` for name resolution.
            *   **Called By:** This method is called by `visit_Call` to resolve the names of called entities.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None)`
        *   *Description:* This private helper method constructs a fully qualified name for a function or method. It combines the filename, an optional class name, and the base name of the entity to create a unique identifier within the project's scope, following a `filename::ClassName::methodName` or `filename::functionName` format.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **basename** (`str`): The base name of the function or method (e.g., 'my_function').
            - **class_name** (`str | None`): The name of the class if the entity is a method, otherwise `None`.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name of the function or method.
        *   **Usage:**
            *   **Calls:** This method accesses `self.filename` to construct the full name.
            *   **Called By:** This method is called by `visit_FunctionDef` to create unique identifiers for functions and methods.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private helper method determines the identifier of the currently active caller context. It returns the `self.current_function` if set, otherwise it provides a placeholder indicating the global scope within the current filename. This is crucial for correctly attributing calls to their originating context.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
        *   *Returns:*
            - **caller_identifier** (`str`): The identifier of the current function or a placeholder for the global scope.
        *   **Usage:**
            *   **Calls:** This method accesses `self.current_function` and `self.filename` to determine the caller.
            *   **Called By:** This method is called by `visit_Call` to identify the source of a function call.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method is an AST visitor for `ast.Import` nodes. It processes `import module as alias` statements, recording the mapping from the alias (or original module name) to the actual module name in `self.import_mapping`. After processing the import, it delegates to `generic_visit` to continue the AST traversal.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.Import`): The `ast.Import` node representing an `import` statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls `self.generic_visit` to continue the AST traversal.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.Import` node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method is an AST visitor for `ast.ImportFrom` nodes. It handles `from module import name as alias` statements, extracting the module name and mapping the imported name (or its alias) to the module in `self.import_mapping`. This helps in resolving fully qualified names for imported entities.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.ImportFrom`): The `ast.ImportFrom` node representing a `from ... import ...` statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method accesses `self.import_mapping` to store import information.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.ImportFrom` node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is an AST visitor for `ast.ClassDef` nodes. It manages the `self.current_class` context, saving the previous class name before setting the current one to the newly defined class. It then performs a generic visit to process nested elements (like methods) within the class and restores the previous class context upon exiting the class definition.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.ClassDef`): The `ast.ClassDef` node representing a class definition.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls `self.generic_visit` to traverse the class's body.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.ClassDef` node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method is an AST visitor for `ast.FunctionDef` nodes. It captures the definition of a function or method, constructs its full qualified name using `_make_full_name`, and updates `self.local_defs` to map its simple name to the full name. It sets the `self.current_function` context, adds the function as a node to the call graph, performs a generic visit to process its body, and finally restores the previous function context.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.FunctionDef`): The `ast.FunctionDef` node representing a function definition.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls `self._make_full_name` to get the function's full name, `self.graph.add_node` to add it to the graph, and `self.generic_visit` to traverse its body.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.FunctionDef` node is encountered, and explicitly by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is an AST visitor for `ast.AsyncFunctionDef` nodes. It handles asynchronous function definitions by simply delegating the processing to the `visit_FunctionDef` method. This ensures that async functions are treated similarly to regular functions for the purpose of call graph construction, capturing their definition and adding them to the graph.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.AsyncFunctionDef`): The `ast.AsyncFunctionDef` node representing an asynchronous function definition.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls `self.visit_FunctionDef` to process the async function.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.AsyncFunctionDef` node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method is an AST visitor for `ast.Call` nodes, which represent function or method calls. It identifies the caller using `_current_caller`, extracts the callee's name components using `_recursive_call`, and resolves the callee's full name using `_resolve_all_callee_names`. Finally, it records the call as an edge in the `self.edges` dictionary, linking the caller to the resolved callee.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.Call`): The `ast.Call` node representing a function or method call.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls `self._current_caller`, `self._recursive_call`, `self._resolve_all_callee_names`, and `self.generic_visit`.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.Call` node is encountered.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node: ast.If)`
        *   *Description:* This method is an AST visitor for `ast.If` nodes. It includes special handling for the `if __name__ == "__main__"` block, temporarily setting the `self.current_function` to `<main_block>` to correctly attribute calls within this entry point. For all other `if` statements, it simply performs a generic visit to continue traversing the AST.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.If`): The `ast.If` node representing an `if` statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method calls `self.generic_visit` to continue the AST traversal.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.If` node is encountered.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content: str)`
*   **Description:** This function, `wrap_cdata`, is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string that begins with `<![CDATA[`, followed by a newline, the provided content, another newline, and finally `]]>`. This ensures that the content is treated as character data by an XML parser, preventing interpretation of any special characters within it. The primary purpose is to safely embed raw text, potentially containing XML-sensitive characters, into an XML document.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped in CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A string with the provided content wrapped in CDATA tags, including leading and trailing newlines within the CDATA block.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs, image_list)`
*   **Description:** This function processes a list of notebook output objects to extract their content, primarily focusing on text and image data. It iterates through each output, identifying its type (display_data, execute_result, stream, or error). For display_data and execute_result types, it prioritizes extracting image data (PNG then JPEG), converting Base64 encoded images into a structured format and storing them in a provided image_list, while generating XML-like placeholders for the images. If no image is found, it extracts plain text. For stream outputs, it extracts the raw text, and for error outputs, it formats the error name and value. The function accumulates all extracted content, including image placeholders and text, into a list of strings.
*   **Parameters:**
    - **outputs** (`list`): A list of output objects, typically from a notebook cell execution, each containing various data types such as text, images, or error information.
    - **image_list** (`list[dict]`): A mutable list passed by reference, used to store dictionaries of extracted image data (mime_type and Base64 string) and their corresponding metadata. This list is modified in-place.
*   **Returns:**
    - **extracted_content** (`list[str]`): A list of strings, where each string represents either extracted plain text, a formatted error message, or an XML-like placeholder for an image that was processed and added to `image_list`.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type)`
*   **Description:** The process_image function is designed to extract and format base64 encoded image data based on a given MIME type. It first checks for the presence of the mime_type as a key in an external 'data' dictionary. If found, it retrieves the corresponding base64 string, removes any newline characters, and then appends a dictionary containing the mime_type and processed data to an external 'image_list'. Finally, it returns a formatted string representing an image placeholder, including an index derived from the 'image_list' length and the mime_type. In case of any exception during this process, it returns an error message. If the mime_type is not present in 'data', the function returns None.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type string, used as a key to locate the image's base64 data within an external 'data' dictionary.
*   **Returns:**
    - **result** (`str | None`): Returns a formatted string containing an image placeholder if the image data is successfully processed. If an error occurs during processing, it returns an error message string. If the mime_type is not found in the external 'data' dictionary, it returns None.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content)`
*   **Description:** This function converts the content of a Jupyter Notebook, provided as a string, into a custom XML format. It iterates through each cell, processing markdown cells by embedding their source directly and code cells by wrapping their source in CDATA. If code cells have outputs, it extracts and processes them, potentially identifying and collecting images. The function handles parsing errors by returning a specific error message.
*   **Parameters:**
    - **file_content** (`str`): The raw content of a Jupyter Notebook file, expected as a string in JSON format.
*   **Returns:**
    - **xml_output** (`str`): A string containing the converted notebook content in a custom XML format, or an error message if the input cannot be parsed as a notebook.
    - **extracted_images** (`list`): A list of extracted image data or references found within the notebook's output cells.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files)`
*   **Description:** This function processes a list of repository files to identify and convert Jupyter notebooks. It filters the input `repo_files` to find items with a '.ipynb' extension. For each identified notebook, it logs its path and then calls an external utility to convert its content into XML and extract associated images. The function stores the resulting XML and image data in a dictionary, keyed by the notebook's original file path. Finally, it returns this dictionary containing all processed notebook data.
*   **Parameters:**
    - **repo_files** (`List[object]`): An iterable collection of file-like objects, where each object is expected to have a 'path' attribute (string) and a 'content' attribute (string), representing files from a repository.
*   **Returns:**
    - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the paths of the processed notebook files (strings) and values are dictionaries. Each inner dictionary contains two keys: 'xml' (string, representing the converted XML content) and 'images' (representing extracted image data).
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, designed for efficient handling of file data through lazy loading. It provides properties to access the Git blob object, the file's content, and its size only when they are first requested. Additionally, it includes methods for basic analysis, such as word counting, and for converting the file's metadata into a dictionary format.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly declare any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This method initializes a RepoFile object by setting its file path and the Git Tree object from which the file originates. It also initializes internal attributes for the Git blob, file content, and file size to `None`, indicating that these values will be loaded lazily upon first access.
    *   *Parameters:*
        - **self** (`RepoFile`): The instance of the class.
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if the `_blob` attribute is already populated; if not, it attempts to retrieve the blob from the `_tree` using the file's path. If the file is not found in the commit tree, a `FileNotFoundError` is raised.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **null** (`git.Blob`): The Git blob object for the file.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other functions or methods within the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It first checks if the `_content` attribute is already loaded. If not, it accesses the `blob` property to get the Git blob, reads its data stream, and decodes it using UTF-8, ignoring any decoding errors.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **null** (`str`): The decoded content of the file.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other functions or methods within the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the `_size` attribute is already loaded. If not, it accesses the `blob` property to get the Git blob and retrieves its `size` attribute, storing it for future access.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **null** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other functions or methods within the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function, demonstrating how to process the file's content. It retrieves the file's content using the `content` property, splits the string into individual words, and then returns the total count of these words.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **null** (`int`): The total number of words in the file content.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other functions or methods within the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This special method provides a developer-friendly string representation of the RepoFile object. It returns a string that includes the class name and the file's path, which is useful for debugging and logging purposes.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **null** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other functions or methods within the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content: bool)`
        *   *Description:* This method converts the RepoFile object into a dictionary representation, providing structured access to its metadata. It includes the file's path, its base name, its size, and its type. Optionally, if `include_content` is set to `True`, the file's content is also added to the dictionary.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
            - **include_content** (`bool`): A boolean flag indicating whether the file's content should be included in the dictionary.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing the file's metadata and optionally its content.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other functions or methods within the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a comprehensive interface for managing Git repositories. It handles the cloning of a remote repository into a temporary local directory, manages the lifecycle of this directory, and offers methods to access and structure the repository's files. The class also implements the context manager protocol, ensuring proper cleanup of temporary resources upon exiting a 'with' statement.
*   **Instantiation:** The class is not explicitly instantiated by other known components in the provided context.
*   **Dependencies:** The class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes a GitRepository instance by cloning the specified Git repository URL into a newly created temporary directory. It sets up various instance attributes including the repository URL, the path to the temporary directory, the GitPython Repo object, an empty list for `RepoFile` objects, and the latest commit and its tree. Error handling is included to catch and raise `RuntimeError` if the cloning process fails.
    *   *Parameters:*
        - **self** (`GitRepository`): The instance of the class.
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method is responsible for retrieving all file paths present in the cloned Git repository. It utilizes the GitPython library's `ls-files` command to get a list of all tracked files. Each file path is then used to instantiate a `RepoFile` object, which is assumed to be an external class capable of representing a file within the repository context. The method populates the `self.files` attribute with these `RepoFile` instances and returns the complete list.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances, each representing a file within the repository.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods based on the provided context.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* The `close` method is designed for resource cleanup, specifically for deleting the temporary directory where the Git repository was cloned. It first checks if `self.temp_dir` is set to ensure a directory exists to be removed. After printing a message indicating the deletion, it sets `self.temp_dir` to `None`, effectively marking the resource as cleaned up.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods based on the provided context.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This method implements the `__enter__` part of Python's context manager protocol. When a `GitRepository` instance is used in a `with` statement, this method is implicitly called upon entry to the block. Its primary function is to return the instance itself, allowing it to be bound to a variable in the `with` statement for use within the block.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository class itself.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods based on the provided context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This method implements the `__exit__` part of Python's context manager protocol. It is implicitly called when execution leaves the `with` statement block, regardless of whether an exception occurred. Its main purpose is to ensure that the `close()` method is invoked to clean up the temporary repository directory, thereby guaranteeing proper resource management.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
            - **exc_type** (`type`): The type of exception that occurred, or None if no exception.
            - **exc_val** (`Exception`): The exception instance that occurred, or None.
            - **exc_tb** (`traceback`): The traceback object associated with the exception, or None.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods based on the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content: bool)`
        *   *Description:* This method generates a hierarchical dictionary representation of the repository's file structure, mimicking a file system tree. If the `self.files` attribute is not already populated with `RepoFile` objects, it first calls `get_all_files()` to retrieve them. It then iterates through these `RepoFile` objects, splitting their paths to construct a nested dictionary where each node represents either a directory or a file. Files are added to the appropriate directory level, optionally including their content.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
            - **include_content** (`bool`): A boolean flag indicating whether the content of the files should be included in the dictionary representation. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree of the repository, with 'name', 'type', and 'children' keys for directories, and file details for files.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods based on the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart to visually compare the number of JSON tokens against TOON tokens. It takes the token counts and a savings percentage as input, then uses `matplotlib.pyplot` to create the visualization. The chart includes a title indicating the token comparison and savings, labeled axes, and displays the exact token counts above each bar. Finally, the generated chart is saved to a specified output file path and the plot is closed to free up memory.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens for the JSON format.
    - **toon_tokens** (`int`): The number of tokens for the TOON format.
    - **savings_percent** (`float`): The calculated percentage of savings between the two token counts.
    - **output_path** (`str`): The file path where the generated chart image will be saved.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the net operational time between a start and end time, specifically accounting for potential sleep durations due to rate limits when a 'gemini-' model is used. It first determines the total elapsed duration. If the model is not a 'gemini-' type, the total duration is returned directly. For 'gemini-' models, it computes the number of batches, estimates the total sleep time based on a fixed sleep duration per batch, and subtracts this from the total duration. The final net time is guaranteed to be non-negative.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp or time value for the operation.
    - **end_time** (`float`): The ending timestamp or time value for the operation.
    - **total_items** (`int`): The total number of items processed during the operation.
    - **batch_size** (`int`): The number of items processed per batch.
    - **model_name** (`str`): The name of the model being used, which determines if rate-limiting sleep adjustments are applied.
*   **Returns:**
    - **net_time** (`float`): The calculated net duration in seconds, adjusted for rate-limiting sleep times if applicable, or the total duration if no adjustments are made. The value is always non-negative.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive process for analyzing a GitHub repository, generating documentation using Helper LLMs, and compiling a final report with a Main LLM. It handles API key and model selection, clones the specified repository, extracts project information, constructs a file tree, and performs relationship and AST analysis. The function then prepares structured inputs for LLMs, calls them to generate function and class analyses, and finally synthesizes these into a comprehensive report, including token usage metrics and saving the output.
*   **Parameters:**
    - **input** (`str`): The initial user input, expected to contain a GitHub repository URL for analysis.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used in the workflow.
    - **status_callback** (`None`): An optional callback function used to provide real-time status updates during the workflow execution.
*   **Returns:**
    - **result** (`dict`): A dictionary containing the generated 'report' (string) and 'metrics' (dict) related to the workflow's execution and performance.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function, `update_status`, is designed to handle and propagate status messages. It accepts a single message as input. The function first checks if a `status_callback` function is available and, if so, invokes it with the provided message. Regardless of the callback's presence, it logs the message at the info level using the `logging` module. Its main purpose is to ensure status updates are both logged and optionally dispatched to a custom handler.
*   **Parameters:**
    - **msg** (`Any`): The status message to be processed, logged, and potentially passed to a callback.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback)`
*   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks within a Git repository. It clones the repository, extracts basic project information, converts notebooks to an XML-like structure, and then processes each notebook individually using a specified Large Language Model (LLM). The function dynamically selects the appropriate API key and base URL based on the chosen LLM model. Finally, it concatenates the reports generated for each notebook, saves the combined report to a markdown file, and returns the report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): A string containing the URL to a Git repository that will be cloned and analyzed.
    - **api_keys** (`dict`): A dictionary containing various API keys, such as 'gpt', 'gemini', 'scadsllm', and 'ollama', used for authenticating with different LLM services.
    - **model** (`str`): The name of the Large Language Model to be used for generating notebook reports (e.g., 'gpt-4', 'gemini-pro', 'alias-model').
    - **status_callback** (`callable`): An optional callback function that receives status messages during the workflow execution, allowing for real-time updates. Defaults to None.
*   **Returns:**
    - **report_and_metrics** (`dict`): A dictionary containing two keys: 'report', which holds the concatenated markdown string of all generated notebook reports, and 'metrics', which is a dictionary of performance metrics for the workflow execution.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a multimodal payload suitable for the Gemini API, combining textual context with embedded images. It serializes basic project information and the notebook path into an initial JSON string. The function then parses an XML content string, identifying image placeholders using a regular expression. For each placeholder, it extracts the corresponding base64 image data from a provided list and formats it as an image_url entry in the payload. Text segments found between or around these image placeholders are added as text entries, resulting in a structured list of dictionaries ready for a multimodal API request.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary or object containing basic project information to be included in the payload.
    - **nb_path** (`str`): The current notebook's file path, included in the context information.
    - **xml_content** (`str`): An XML string representing the notebook structure, which may contain <IMAGE_PLACEHOLDER/> tags.
    - **images** (`List[dict]`): A list of dictionaries, where each dictionary contains image data (e.g., base64 string) corresponding to image placeholders in `xml_content`.
*   **Returns:**
    - **payload_content** (`List[dict]`): A list of dictionaries, each representing a part of the multimodal Gemini payload, containing either text content or image URLs with base64 encoded data.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into its corresponding Python module path string. It first determines the path relative to the project root, handling cases where the file is not within the root by falling back to the base filename. It then removes the '.py' extension if present and replaces directory separators with dots. Finally, it specifically handles '__init__.py' files by removing the '.__init__' suffix from the module path to represent the package itself.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string (e.g., 'my_package.my_module').
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to build a comprehensive call graph. It identifies all Python files, collects definitions of functions, methods, and classes, and then resolves calls between these entities. The class provides methods to initiate the analysis and retrieve the raw relationships in a structured format, enabling a deep understanding of code dependencies within the project.
*   **Instantiation:** This class is not explicitly instantiated by any other components based on the provided context.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer instance by setting the project's root directory and preparing several internal data structures. It sets up dictionaries for storing definitions, the call graph, and file ASTs, along with a set of directories to be ignored during file system traversal.
    *   *Parameters:*
        - **self** (`ProjectAnalyzer`): The instance of the class.
        - **project_root** (`string`): The absolute path to the root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect function, method, and class definitions. Subsequently, it resolves calls within these files to build a comprehensive call graph. Finally, it clears temporary AST storage and returns the generated call graph.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* This method processes the internal call_graph to generate a structured representation of incoming and outgoing relationships between code entities. It iterates through the call graph, populating two dictionaries: 'outgoing' (what each entity calls) and 'incoming' (what calls each entity). The results are then sorted and returned in a dictionary format.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **relationships_data** (`dict`): A dictionary containing two keys, 'outgoing' and 'incoming', each mapping entity identifiers to sorted lists of related entity identifiers.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private helper method is responsible for recursively traversing the project directory to locate all Python files. It uses os.walk to navigate the file system, explicitly skipping directories specified in self.ignore_dirs. It compiles a list of absolute paths to all discovered Python files.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found within the project root, excluding ignored directories.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath: str)`
        *   *Description:* This private method parses a given Python file to identify and store definitions of functions, methods, and classes. It reads the file, parses it into an Abstract Syntax Tree (AST), and then walks the AST to find FunctionDef and ClassDef nodes. For each definition, it constructs a unique path name and stores its file path, line number, and type in self.definitions. It also stores the AST in self.file_asts. Error handling is included for file processing.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **filepath** (`str`): The absolute path to the Python file being analyzed.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree: ast.AST, node: ast.AST)`
        *   *Description:* This private helper method traverses an Abstract Syntax Tree (AST) to find the parent node of a given child node. It iterates through all nodes in the tree and checks their children to identify if any child matches the provided node. If a match is found, the current parent node is returned. If no parent is found, it returns None.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent_node** (`ast.AST or None`): The parent AST node of the given node, or None if no parent is found.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath: str)`
        *   *Description:* This private method is responsible for resolving function and method calls within a specified Python file. It retrieves the AST for the given filepath from self.file_asts. It then instantiates a CallResolverVisitor with the file context and definitions, and uses it to visit the AST. The resolved calls from the visitor are then extended into the self.call_graph. Error handling is included for the call resolution process.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **filepath** (`str`): The absolute path to the Python file whose calls are to be resolved.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions based on the provided context.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class extends ast.NodeVisitor to perform a detailed analysis of Python Abstract Syntax Trees (ASTs). Its primary function is to identify and resolve all function and method calls within a given source file, mapping them to their fully qualified names. By tracking module paths, class definitions, function scopes, and object instantiations, it builds a comprehensive record of call relationships across the codebase.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with the current file path, the project root, and a dictionary of known definitions. It sets up internal state variables like `module_path`, `scope` for imports, `instance_types` for tracking assigned object types, and `calls` (a defaultdict) to store detected call relationships.
    *   *Parameters:*
        - **self** (`CallResolverVisitor`): The instance of the class.
        - **filepath** (`str`): The path to the source file being analyzed.
        - **project_root** (`str`): The root directory of the project, used for module path resolution.
        - **definitions** (`dict`): A dictionary containing known qualified names of definitions in the project.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is called when an ast.ClassDef node is encountered during AST traversal. It temporarily updates the `current_class_name` attribute to reflect the class being visited, allowing nested methods to correctly form their fully qualified names. After visiting the class's children, it restores the previous class name.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** No specific calls made by this method were identified in the provided context.
            *   **Called By:** No specific callers of this method were identified in the provided context.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method is invoked when an ast.FunctionDef node is visited. It constructs the full qualified identifier for the function or method, considering whether it's nested within a class. It then sets this as the `current_caller_name` for subsequent call resolution within the function's body and restores the previous caller name after processing.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function or method definition.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** No specific calls made by this method were identified in the provided context.
            *   **Called By:** No specific callers of this method were identified in the provided context.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* When an ast.Call node is encountered, this method attempts to resolve the fully qualified name of the called function or method using `_resolve_call_qname`. If a definition is found and recognized, it records the call, including the caller's file, line number, full identifier, and type (module, local function, method, or function), storing this information in the `self.calls` defaultdict.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** No specific calls made by this method were identified in the provided context.
            *   **Called By:** No specific callers of this method were identified in the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method handles ast.Import nodes, which represent `import module_name [as alias]` statements. It iterates through the imported names and their aliases, storing the mapping from the local name (alias or original name) to the module's original name in the `self.scope` dictionary.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** No specific calls made by this method were identified in the provided context.
            *   **Called By:** No specific callers of this method were identified in the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method processes ast.ImportFrom nodes, which correspond to `from module import name [as alias]` statements. It correctly resolves the full module path, accounting for relative imports (`node.level`), and then maps the imported names (or their aliases) to their fully qualified paths in the `self.scope` dictionary.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** No specific calls made by this method were identified in the provided context.
            *   **Called By:** No specific callers of this method were identified in the provided context.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node: ast.Assign)`
        *   *Description:* This method is triggered by ast.Assign nodes, representing assignment statements. It specifically looks for assignments where the right-hand side is a call to a constructor (e.g., `x = MyClass()`). If such an instantiation is found and the class name is resolvable, it records the qualified class name associated with the assigned variable in `self.instance_types`."
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:* None
        *   **Usage:**
            *   **Calls:** No specific calls made by this method were identified in the provided context.
            *   **Called By:** No specific callers of this method were identified in the provided context.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node: ast.expr)`
        *   *Description:* This private helper method attempts to determine the fully qualified name (QName) of a function or method being called. It handles direct name calls (e.g., `func()`), resolving them against the current scope or local module definitions. It also handles attribute calls (e.g., `obj.method()`), using `self.instance_types` to find the class of the object or `self.scope` for module-level attributes.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., ast.Name or ast.Attribute).
        *   *Returns:*
            - **qualified_name** (`str | None`): The fully qualified name of the callee as a string if resolved, otherwise None.
        *   **Usage:**
            *   **Calls:** No specific calls made by this method were identified in the provided context.
            *   **Called By:** No specific callers of this method were identified in the provided context.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function encrypts a given string using a `cipher_suite` object. It first checks if the input text or the `cipher_suite` is empty or null; if either is, it returns the original text without encryption. Otherwise, it prepares the text by stripping leading/trailing whitespace and encoding it to bytes. The byte string is then encrypted, and the resulting encrypted bytes are decoded back into a string before being returned.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input text, or the original text if encryption was skipped due to empty input or missing cipher suite.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given text string using a global `cipher_suite` object. It first checks if the input text or the `cipher_suite` is empty, returning the original text if either condition is true. If both are present, it proceeds to strip whitespace from the text, encode it to bytes, decrypt it using `cipher_suite.decrypt`, and then decode the result back into a string. The function includes error handling, returning the original text in case any exception occurs during the decryption process.
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_or_original_text** (`str`): The decrypted string if successful, or the original string if decryption is not performed (due to empty input or missing cipher_suite) or if an error occurs during decryption.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function creates a new user document with the provided username, name, and a hashed password. It initializes fields for Gemini API key, Ollama base URL, and GPT API key as empty strings. The function then inserts this user document into the `dbusers` collection, which is presumed to be a MongoDB collection. It leverages `stauth.Hasher.hash` to secure the password before storage.
*   **Parameters:**
    - **username** (`str`): The unique username for the new user, which will also serve as the document's `_id`.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before being stored.
*   **Returns:**
    - **inserted_id** (`str`): The `_id` of the newly inserted user document, which corresponds to the provided username.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** The `fetch_all_users` function is responsible for retrieving all user records from a database collection. It executes a `find()` operation on the `dbusers` object, which is expected to be a database collection. The results, typically a cursor of user documents, are then converted into a standard Python list before being returned. This provides a comprehensive list of all stored user data.
*   **Parameters:** None
*   **Returns:**
    - **users** (`list`): A list containing all user documents retrieved from the 'dbusers' collection.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** This function retrieves a single user record from a database collection named `dbusers`. It queries the collection for a document where the `_id` field matches the provided `username`. The function is designed to return the first document that satisfies this criterion.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched, which is used to match the `_id` field in the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if a matching record is found, otherwise `None`.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the 'name' field for a user identified by their 'username' in the 'dbusers' collection. It performs a MongoDB update_one operation, setting the 'name' field to the provided new_name for the document where the '_id' matches the given username. The function returns the count of modified documents. It specifically notes that the '_id' field itself is not changed, only the 'name' attribute.
*   **Parameters:**
    - **username** (`str`): The unique identifier (MongoDB _id) of the user whose name is to be updated.
    - **new_name** (`str`): The new name to be set for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function is responsible for updating a user's Gemini API key within a database. It takes a username and the new API key as input. The provided API key is first stripped of any leading or trailing whitespace and then encrypted. Finally, the function updates the `gemini_api_key` field for the specified user in the `dbusers` collection with the encrypted key.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored for the user, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** This function `update_gpt_key` is designed to securely update a user's GPT API key in the database. It takes a username and a new API key as input. The provided API key is first stripped of any leading/trailing whitespace and then encrypted using an external `encrypt_text` function. Finally, the encrypted key is stored in the `gpt_api_key` field for the specified user in the `dbusers` collection.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose GPT API key needs to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be stored for the user. It will be stripped of whitespace and encrypted before being saved.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. This will typically be 1 if the user was found and the key was updated, or 0 if the user was not found.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specific user in a database. It takes a username and a new Ollama base URL as input. The provided URL is first stripped of any leading or trailing whitespace before being stored. The function then updates the corresponding user's document in the 'dbusers' collection. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be updated.
    - **ollama_base_url** (`str`): The new base URL for Ollama, which will be stripped of whitespace before being saved.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function updates a user's OpenSRC API key within the database. It takes a username and the new API key as input. The provided API key is first stripped of any leading or trailing whitespace, then encrypted before being stored. Finally, the function performs an update operation on the `dbusers` collection, setting the `opensrc_api_key` field for the specified user. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The username of the user whose OpenSRC API key needs to be updated.
    - **opensrc_api_key** (`str`): The new OpenSRC API key to be stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** This function updates the 'opensrc_base_url' for a specific user in a database. It takes a username and a new base URL as input. The function uses the provided username to locate the user's record and then updates their 'opensrc_base_url' field with the new URL, ensuring any leading or trailing whitespace is removed from the URL. It returns the count of modified documents.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose 'opensrc_base_url' is to be updated.
    - **opensrc_base_url** (`str`): The new base URL for the open-source repository, which will have leading/trailing whitespace removed before being stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. Typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** The fetch_gemini_key function retrieves a user's Gemini API key from a database. It takes a username as input to identify the specific user. The function queries a 'dbusers' collection, searching for a document where the '_id' field matches the provided username. If a user document is found, it extracts and returns the 'gemini_api_key' field. If no user is found with the given username, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key associated with the user, or None if the user or key is not found in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions based on the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL associated with a specific user from a database. It queries the `dbusers` collection using the provided username as the `_id`. If a user document is found, it extracts and returns the `ollama_base_url` field. If no user is found, the function returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL associated with the user, or `None` if the user is not found in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** This function is designed to retrieve a user's GPT API key from a database. It accepts a username as an argument and uses it to query a collection named 'dbusers'. The function specifically looks for a document matching the provided username and extracts the 'gpt_api_key' field. If a user document is found, the corresponding API key is returned; otherwise, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched from the database.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the specified username, or None if the user is not found in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** This function, `fetch_opensrc_key`, is designed to retrieve an Open Source API key for a specified user from a database. It queries the `dbusers` collection using the provided username as the document's `_id`. The function projects only the `opensrc_api_key` field. If a user document is found, it extracts the `opensrc_api_key` value; otherwise, it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source API key is to be fetched.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key associated with the user, or None if the user is not found or the key does not exist.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** This function retrieves the 'opensrc_base_url' for a specified user from a database. It queries the 'dbusers' collection using the provided username as the document's '_id'. If a matching user document is found, it extracts the 'opensrc_base_url' field. If no user is found or the field is absent, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose opensrc base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The base URL for opensrc associated with the user, or None if the user is not found or the 'opensrc_base_url' field is not present.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is designed to remove a user record from a database collection. It takes a username as input and uses it to identify the document to be deleted. The function performs a delete operation on the `dbusers` collection, specifically targeting a document where the `_id` field matches the provided username. It then returns the number of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database. This value is used to match the '_id' field in the database.
*   **Returns:**
    - **deleted_count** (`int`): An integer representing the number of documents that were deleted from the collection. A value of 1 indicates successful deletion of the user, while 0 indicates the user was not found or not deleted.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves a user's API keys and base URLs from a database based on a provided username. It queries the `dbusers` collection for a matching user. If no user is found, it returns `None` for all expected values. Otherwise, it decrypts specific API keys (Gemini, GPT, Open Source) and retrieves base URLs (Ollama, Open Source) before returning all five values.
*   **Parameters:**
    - **username** (`str`): The username used to identify and retrieve the user's data from the database.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user is not found or the key is absent.
    - **ollama_plain** (`str | None`): The Ollama base URL, or None if the user is not found or the URL is absent.
    - **gpt_plain** (`str | None`): The decrypted GPT API key, or None if the user is not found or the key is absent.
    - **opensrc_plain** (`str | None`): The decrypted open-source API key, or None if the user is not found or the key is absent.
    - **opensrc_url** (`str | None`): The open-source base URL, or None if the user is not found or the URL is absent.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** This function creates a new chat entry in a database. It generates a unique identifier for the chat using UUID, records the provided username and chat name, and captures the current timestamp for creation. The constructed chat dictionary is then inserted into the 'dbchats' collection. Finally, it returns the unique ID of the newly inserted document.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat entry.
    - **chat_name** (`str`): The name of the chat.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier of the newly created chat entry in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** This function, `fetch_chats_by_user`, is designed to retrieve all chat documents associated with a specific user from a database. It queries the `dbchats` collection, filtering documents where the 'username' field matches the provided input. The results are then sorted in ascending order based on their 'created_at' timestamp. Finally, the function returns the collection of matching chat documents as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat documents.
*   **Returns:**
    - **chats** (`list`): A list of chat documents associated with the specified username, sorted by their creation date.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function, `check_chat_exists`, is designed to verify the existence of a specific chat within a database collection named `dbchats`. It takes a username and a chat name as input. The function queries the `dbchats` collection to find a document that matches both the provided username and chat name. It then returns a boolean value indicating whether such a chat was found.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked for existence.
    - **chat_name** (`str`): The name of the chat to be checked for existence.
*   **Returns:**
    - **exists** (`bool`): True if a chat matching the provided username and chat name is found in the database; False otherwise.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and all its associated exchanges (messages) within the database for a specified user. It first updates the `chat_name` field for a single chat entry in the `dbchats` collection. Subsequently, it updates the `chat_name` field for all related exchange entries in the `dbexchanges` collection. The function returns the count of chat documents that were modified during the initial rename operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat that needs to be changed.
    - **new_name** (`str`): The desired new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat documents modified by the initial rename operation (from dbchats.update_one).
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str, json_tokens: int, toon_tokens: int, savings_percent: float)`
*   **Description:** This function is designed to create and persist a new exchange record into a database. It generates a unique identifier using UUID, constructs a comprehensive dictionary containing the provided question, answer, feedback, user details, chat name, and various optional metrics such as helper/main components used, time taken, token counts, and savings percentage. A timestamp for creation is automatically added. The function attempts to insert this structured record into the `dbexchanges` collection. Upon successful insertion, it returns the unique ID of the new record; otherwise, it catches any exceptions during the database operation and returns `None`.
*   **Parameters:**
    - **question** (`str`): The textual question associated with the exchange.
    - **answer** (`str`): The textual answer generated for the exchange.
    - **feedback** (`str`): The feedback string provided for the exchange.
    - **username** (`str`): The username of the individual involved in the exchange.
    - **chat_name** (`str`): The name of the chat session where the exchange occurred.
    - **helper_used** (`str`): An optional string indicating which helper component was utilized, defaulting to an empty string.
    - **main_used** (`str`): An optional string indicating which main component was utilized, defaulting to an empty string.
    - **total_time** (`str`): An optional string representing the total time taken for the exchange, defaulting to an empty string.
    - **helper_time** (`str`): An optional string representing the time taken by the helper component, defaulting to an empty string.
    - **main_time** (`str`): An optional string representing the time taken by the main component, defaulting to an empty string.
    - **json_tokens** (`int`): An optional integer representing the number of JSON tokens used, defaulting to 0.
    - **toon_tokens** (`int`): An optional integer representing the number of Toon tokens used, defaulting to 0.
    - **savings_percent** (`float`): An optional float representing the percentage of savings, defaulting to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly created exchange record upon successful insertion.
    - **None** (`NoneType`): Returned if an error occurs during the database insertion process.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records associated with a specific username from a database collection named `dbexchanges`. It queries the database using the provided username and sorts the results by their 'created_at' timestamp in ascending order. The function then converts the database cursor into a list and returns these sorted exchange records.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records associated with the specified username, sorted by creation timestamp.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a list of exchange documents from the 'dbexchanges' collection. It filters these exchanges based on a provided username and chat name. The results are then sorted by their 'created_at' timestamp in ascending order before being returned as a list.
*   **Parameters:**
    - **username** (`str`): The username to filter the exchanges by.
    - **chat_name** (`str`): The name of the chat to filter the exchanges by.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents (dictionaries) that match the specified username and chat name, sorted by their creation timestamp.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** This function updates the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value. The function uses `dbexchanges.update_one` to locate the document by its `_id` and sets the 'feedback' field to the provided value. It then returns the count of documents that were successfully modified.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated.
    - **feedback** (`int`): The integer value representing the feedback to be set for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** This function updates an existing exchange record in the database. It takes an exchange identifier and a new feedback message string. The function uses the `dbexchanges` collection to find the document matching the provided `exchange_id` and sets its `feedback_message` field to the new value. It then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated in the database.
    - **feedback_message** (`str`): The new feedback message to be stored for the specified exchange record.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified as a result of the update operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is responsible for deleting a single exchange record from the database. It takes an exchange ID as input and uses it to locate and remove the corresponding document from the 'dbexchanges' collection. The function returns an integer indicating how many documents were successfully deleted.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange record to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted from the collection. Typically 0 if no matching document was found, or 1 if a document was successfully deleted.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is designed to completely delete a specific chat and all its associated message exchanges for a given user. It first removes all messages linked to the chat from the 'dbexchanges' collection using `dbexchanges.delete_many`. Subsequently, it deletes the chat entry itself from the 'dbchats' collection using `dbchats.delete_one`. This two-step process ensures data consistency between the frontend and backend. The function returns the count of chat entries that were deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted from the 'dbchats' collection. This will typically be 0 or 1 for a delete_one operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list)`
*   **Description:** The `clean_names` function processes a list of strings, `model_list`. It iterates through each string, splitting it by the '/' character. For each string, it extracts the last segment after the final '/' and compiles these segments into a new list. This effectively cleans path-like names by returning only the base name.
*   **Parameters:**
    - **model_list** (`list`): A list of strings, where each string is expected to be a path-like identifier that may contain '/' characters.
*   **Returns:**
    - **cleaned_names** (`list[str]`): A new list containing the last segment of each string in the input `model_list` after splitting by '/'.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list, category_name)`
*   **Description:** This function filters a given list of models (`source_list`) based on a specified `category_name`. It retrieves associated keywords from a global `CATEGORY_KEYWORDS` mapping. If the "STANDARD" keyword is present for the category, it returns only those models from `source_list` that are also found in a global `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list` and appends models whose names contain any of the category's keywords (case-insensitive) to a `filtered` list. Finally, it returns the `filtered` list if it contains any items, otherwise it returns the original `source_list`.
*   **Parameters:**
    - **source_list** (`list`): The list of models to be filtered.
    - **category_name** (`str`): The name of the category to use for filtering.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered according to the specified category, or the original source list if no models match the filter criteria.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function, `save_gemini_cb`, is designed to handle the saving of a new Gemini API key. It retrieves the potential new key from the Streamlit session state. If a new key is present, it updates the Gemini key in the database for the current user and then clears the key from the session state. Finally, it displays a success toast notification to the user.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function, `save_ollama_cb`, acts as a callback to process and save a user-provided Ollama URL. It retrieves the URL from the Streamlit session state, specifically from the key 'in_ollama_url'. If a non-empty URL is found, it proceeds to update this URL in the database associated with the current user's username. Upon successful update, it displays a confirmation toast message to the user.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function `load_data_from_db` is responsible for loading chat and exchange data for a specified user from the database and populating the Streamlit session state. It first checks if the user's data is already loaded to prevent redundant operations. If not loaded, it initializes the `chats` dictionary in `st.session_state`, then fetches predefined chats and exchanges from the database. The fetched exchanges are organized into their corresponding chats within the session state, with a fallback for unnamed chats and handling of `feedback` values. Finally, it ensures a default chat exists if none are loaded, inserting "Chat 1" into the database if necessary, and sets an active chat for the user interface.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose chat and exchange data needs to be loaded from the database.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function updates the 'feedback' key of an exchange object (`ex`) with a new value (`val`). It then persists this updated feedback to a database using `db.update_exchange_feedback`, identifying the record by `ex["_id"]`. Finally, it triggers a full re-run of the Streamlit application using `st.rerun()` to reflect the changes in the UI.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing an exchange, expected to contain 'feedback' and '_id' keys.
    - **val** (`Any`): The new feedback value to be assigned.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if the exchange is present within that chat's exchanges list, it removes it from the session state. Finally, it triggers a Streamlit rerun to refresh the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat to which the exchange belongs.
    - **ex** (`dict`): A dictionary representing the exchange to be deleted, expected to contain an '_id' key.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function, `handle_delete_chat`, is designed to remove a specific chat for a given user. It first deletes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the Streamlit session state by removing the chat from `st.session_state.chats`. If other chats remain, the first one is set as the active chat; otherwise, a new default chat named 'Chat 1' is created in both the database and the session state. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** The `extract_repo_name` function processes an input string to identify and extract a repository name. It first uses a regular expression to locate a URL within the provided text. If a URL is found, it parses the URL to isolate the path component. From this path, the function extracts the last segment, which is treated as the repository name, and removes any trailing ".git" suffix. If no URL is found or a repository name cannot be successfully extracted, the function returns None.
*   **Parameters:**
    - **text** (`str`): The input string, which may contain a URL from which a repository name needs to be extracted.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string, or None if no URL is found or a repository name cannot be determined.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** This function acts as a generator that takes a string of text and yields its words sequentially. It splits the input text by spaces and iterates through each word. For every word, it yields the word followed by a space, introducing a small delay of 0.01 seconds between each yield. This creates a streaming effect, delivering the text word by word over time.
*   **Parameters:**
    - **text** (`str`): The input string of text to be processed and streamed word by word.
*   **Returns:**
    - **word_chunk** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream: bool)`
*   **Description:** This function processes a given markdown text, identifying and rendering embedded Mermaid diagrams. It splits the input text into parts based on '```mermaid' delimiters. Non-Mermaid text sections are rendered using `st.markdown` or `st.write_stream` if streaming is enabled. Mermaid code blocks are rendered using `st_mermaid`, with a fallback to `st.code` if an error occurs during Mermaid rendering.
*   **Parameters:**
    - **markdown_text** (`str`): The input text, which may contain markdown and embedded Mermaid diagram definitions.
    - **should_stream** (`bool`): A flag indicating whether non-Mermaid text content should be streamed (True) or rendered directly (False). Defaults to False.
*   **Returns:**
    - **None** (`None`): The function does not explicitly return a value. It performs side effects by rendering content to a Streamlit application. It returns implicitly if 'markdown_text' is empty.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function `render_exchange` is designed to display a single chat exchange, comprising a user's question and an assistant's answer, within a Streamlit application. It renders the user's input and then presents the assistant's response, which includes an interactive toolbar. This toolbar offers functionalities such as providing feedback (like/dislike), adding comments through a popover, downloading the response, and deleting the exchange. The function also manages error states, displaying an error message if the answer indicates an issue and providing a delete option for erroneous exchanges. It leverages various Streamlit components to construct the user interface.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing a single chat exchange. It is expected to contain keys such as 'question', 'answer', 'feedback', '_id', and 'feedback_message' for rendering and interaction.
    - **current_chat_name** (`str`): A string representing the name of the current chat session, primarily used when invoking the `handle_delete_exchange` function.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** This class serves as a Pydantic data model designed to precisely describe a single parameter of a function. It encapsulates the essential attributes of a function parameter, including its name, data type, and a descriptive explanation. By inheriting from BaseModel, it provides robust data validation and serialization capabilities for structured parameter information.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* This class, inheriting from Pydantic's BaseModel, implicitly generates a constructor. It initializes instances with values for 'name', 'type', and 'description', enforcing type validation based on the defined annotations.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The data type of the parameter.
        - **description** (`str`): A brief explanation of the parameter's purpose.
*   **Methods:** None

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model designed to structure information about the return value of a function. It serves as a data container, ensuring that return value descriptions consistently include a name, its type, and a textual explanation. This class facilitates standardized documentation or programmatic representation of function outputs within a larger system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ReturnDescription` is implicitly generated by Pydantic's BaseModel. It initializes an instance of `ReturnDescription` by accepting `name`, `type`, and `description` as keyword arguments, validating them against their respective string types.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The Python type hint or description of the return value's type.
        - **description** (`str`): A detailed explanation of what the return value represents.
*   **Methods:** None

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to standardize the description of how a function or method interacts with other parts of a system. It serves as a data structure to capture both the outgoing calls made by an entity and the incoming calls it receives, providing a clear overview of its operational context.
*   **Instantiation:** The specific points where this `UsageContext` class is instantiated are not provided in the current context.
*   **Dependencies:** This class primarily depends on `pydantic.BaseModel` for its structural definition and validation capabilities. No other explicit functional dependencies are listed in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly defines its constructor to accept `calls` and `called_by` as keyword arguments. It initializes these attributes directly based on the provided values, ensuring they conform to the `str` type and enabling data validation upon instantiation.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or classes that this entity calls.
        - **called_by** (`str`): A string summarizing the functions or methods that call this entity.
*   **Methods:** None

#### Class: `FunctionDescription`
*   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to provide a structured and detailed analysis of a Python function. It serves as a data schema to encapsulate various aspects of a function, including its high-level purpose, the parameters it accepts, the values it returns, and its operational context within a larger system. This class is crucial for standardizing the representation of function metadata, enabling systematic documentation and analysis.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `FunctionDescription` is implicitly generated by Pydantic. It handles the instantiation of a `FunctionDescription` object by validating and assigning values to its defined fields: `overall`, `parameters`, `returns`, and `usage_context`. This ensures that all instances conform to the specified data types and structure.
    *   *Parameters:*
        - **overall** (`str`): A comprehensive summary describing the function's purpose and its high-level implementation details.
        - **parameters** (`List[ParameterDescription]`): A list containing detailed descriptions for each parameter accepted by the function, including their names, types, and individual purposes.
        - **returns** (`List[ReturnDescription]`): A list detailing the values returned by the function, specifying their types and descriptions.
        - **usage_context** (`UsageContext`): An object providing context on how the function interacts with other components, including what it calls and where it is called from.
*   **Methods:** None

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data container for machine-readable function analysis results, including the function's unique identifier, a detailed description of its purpose, parameters, return values, and usage context, along with an optional field for error reporting. This model ensures consistency in how function analysis data is represented.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class, being a Pydantic BaseModel, implicitly initializes its instances through Pydantic's generated constructor. This constructor sets up the `identifier`, `description`, and an optional `error` field based on the provided arguments, ensuring data validation upon instantiation.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): An object containing a detailed analysis of the function's purpose, parameters, return values, and usage context.
        - **error** (`Optional[str]`): An optional field to store an error message if the function analysis encountered issues or failed.
*   **Methods:** None

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to encapsulate structured information about the `__init__` method of another class. It serves as a data schema, providing fields to store a high-level textual description of the constructor's purpose and a detailed list of its individual parameters. This model is crucial for standardizing the representation of constructor metadata within a larger system, enabling consistent processing and documentation of class initialization logic.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor is responsible for initializing instances of ConstructorDescription with a string description of a constructor and a list of ParameterDescription objects, ensuring type validation and data integrity.
    *   *Parameters:*
        - **description** (`str`): A textual summary or explanation of the constructor being described.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing an individual parameter of the constructor.
*   **Methods:** None

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate contextual information about another class. It defines two string attributes, `dependencies` and `instantiated_by`, which are intended to describe the external components a class relies on and the locations where it is instantiated, respectively. This model provides a structured and type-hinted way to store metadata crucial for understanding a class's role and integration within a larger system.
*   **Instantiation:** The provided context does not specify any locations where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for ClassContext is automatically generated. It initializes an instance of ClassContext by accepting keyword arguments corresponding to its defined fields: `dependencies` and `instantiated_by`. Pydantic handles validation and assignment of these values upon instantiation.
    *   *Parameters:*
        - **dependencies** (`str`): A string summarizing the external dependencies of the class being described.
        - **instantiated_by** (`str`): A string summarizing the primary locations or modules where the class being described is instantiated.
*   **Methods:** None

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to structure and store a comprehensive analysis of a Python class. It encapsulates various aspects such as an overall description of the class, details about its constructor, a list of analyses for its methods, and information regarding its usage context. This model serves as a standardized data structure for representing the analytical output of a class.
*   **Instantiation:** The instantiation points for this class are not specified within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not define an explicit `__init__` method. Initialization is handled implicitly by Pydantic's `BaseModel`, which typically involves assigning values to its defined fields upon instantiation.
    *   *Parameters:* None
*   **Methods:** None

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the root data model for representing a complete analysis of a Python class. It is a Pydantic BaseModel designed to structure information such as the class's unique identifier, a detailed ClassDescription object containing its constructor, methods, and usage context, and an optional field for capturing any errors encountered during the analysis process. This model ensures a standardized format for machine-readable class analysis.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly declare external functional dependencies within its provided source code.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly generates an __init__ method. It initializes instances with 'identifier', 'description', and an optional 'error' field, enforcing type validation based on the defined schema.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifying the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its constructor, methods, and usage context.
        - **error** (`Optional[str]`): An optional string to store any error messages encountered during the analysis of the class, defaulting to None.
*   **Methods:** None

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to encapsulate details about a specific call event identified by a relationship analyzer. It acts as a structured data record, storing critical information such as the source file, the name of the calling function, the mode of the caller (e.g., method, function), and the exact line number where the call occurs. This class provides a standardized format for representing call origins within a system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context. It is designed to be instantiated by components that analyze code relationships and identify call events.
*   **Dependencies:** This class primarily depends on pydantic.BaseModel for its data validation and serialization capabilities.
*   **Constructor:**
    *   *Description:* This class, inheriting from Pydantic's BaseModel, does not define an explicit __init__ method. Pydantic automatically generates a constructor that initializes its fields (file, function, mode, line) based on the provided arguments, ensuring data validation and type enforcement.
    *   *Parameters:*
        - **file** (`str`): The path to the source file where the call event occurred.
        - **function** (`str`): The name of the function or method that made the call.
        - **mode** (`str`): The classification of the calling entity, such as 'method', 'function', or 'module'.
        - **line** (`int`): The specific line number within the file where the call event is located.
*   **Methods:** None

#### Class: `FunctionContextInput`
*   **Summary:** The `FunctionContextInput` class is a Pydantic BaseModel designed to provide a structured context for analyzing a function. It encapsulates two primary pieces of information: a list of identifiers for other functions or methods that the analyzed function calls, and a list of `CallInfo` objects detailing where the analyzed function itself is called. This model ensures a standardized format for representing a function's operational context, facilitating consistent data handling and analysis within a larger system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context, relying on Pydantic's BaseModel for its core functionality.
*   **Constructor:**
    *   *Description:* This class does not define an explicit `__init__` method. As a Pydantic `BaseModel`, its initialization is handled automatically by Pydantic, which parses input data to populate the `calls` and `called_by` attributes based on their type hints.
    *   *Parameters:* None
*   **Methods:** None

#### Class: `FunctionAnalysisInput`
*   **Summary:** The `FunctionAnalysisInput` class is a Pydantic BaseModel designed to serve as a structured input for a function analysis process. It encapsulates all necessary data, including the analysis mode, the function's identifier, its source code, relevant import statements, and additional contextual information. This class acts as a data contract, ensuring that all required components for a comprehensive function analysis are provided in a standardized format.
*   **Instantiation:** This class has no explicitly listed instantiation points.
*   **Dependencies:** This class has no explicitly listed external functional dependencies.
*   **Constructor:**
    *   *Description:* This class inherits from `BaseModel` and does not explicitly define an `__init__` method. Pydantic automatically generates a constructor to validate and initialize its fields: `mode`, `identifier`, `source_code`, `imports`, and `context` based on the provided type hints.
    *   *Parameters:* None
*   **Methods:** None

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to provide a structured schema for capturing contextual information about a method. It defines fields such as the method's identifier, a list of other functions or methods it invokes, a list of entities that call this method, its arguments, and an optional docstring. This class serves as a data structure to represent the operational context and inter-method relationships within a larger system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `MethodContextInput` is automatically generated by Pydantic. It initializes an instance by accepting keyword arguments that correspond to its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`. This allows for straightforward creation and validation of method context data.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects detailing where this method is called from.
        - **args** (`List[str]`): A list of string representations of the arguments accepted by the method.
        - **docstring** (`Optional[str]`): An optional string containing the method's docstring.
*   **Methods:** None

#### Class: `ClassContextInput`
*   **Summary:** The `ClassContextInput` class is a Pydantic model designed to structure contextual information relevant for analyzing a Python class. It encapsulates details about the class's external dependencies, where it is instantiated within the codebase, and specific contextual information for its methods. This model serves as a standardized input format for tools or systems that require a comprehensive understanding of a class's operational environment and internal structure.
*   **Instantiation:** The `ClassContextInput` class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any direct functional dependencies within the provided context, but it relies on Pydantic's BaseModel for its core functionality.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ClassContextInput` is implicitly generated by Pydantic's `BaseModel`. It handles the instantiation of a `ClassContextInput` object by accepting keyword arguments corresponding to its defined fields: `dependencies`, `instantiated_by`, and `method_context`. Pydantic automatically performs data validation and type coercion based on the provided type hints during object creation.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings, where each string represents an external dependency of the class being analyzed. These are typically other modules, functions, or classes that the analyzed class relies upon.
        - **instantiated_by** (`List[CallInfo]`): A list of `CallInfo` objects, indicating the locations or contexts where the class being analyzed is instantiated. This helps in understanding the class's usage patterns across the codebase.
        - **method_context** (`List[MethodContextInput]`): A list of `MethodContextInput` objects, each providing specific contextual details for individual methods within the class being analyzed. This includes information about what each method calls and where it is called from.
*   **Methods:** None

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel that defines the structured input required for generating a ClassAnalysis object. It acts as a data transfer object (DTO), encapsulating all necessary information, such as the class identifier, its source code, relevant imports, and additional context, to facilitate a comprehensive analysis of a Python class. This model ensures that all data passed for class analysis conforms to a predefined schema.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The ClassAnalysisInput class does not explicitly define an `__init__` method. As a Pydantic BaseModel, its constructor is implicitly generated by Pydantic, allowing instantiation by providing keyword arguments corresponding to its defined fields: `mode`, `identifier`, `source_code`, `imports`, and `context`.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): A literal string indicating the analysis mode, which must be 'class_analysis' to specify a class analysis request.
        - **identifier** (`str`): The unique name or identifier of the class that is to be analyzed.
        - **source_code** (`str`): The complete raw source code of the entire class definition to be analyzed.
        - **imports** (`List[str]`): A list of import statements from the source file, which may include imports relevant to the class or its methods.
        - **context** (`ClassContextInput`): An object containing additional contextual information for the class analysis, such as dependencies and instantiation points.
*   **Methods:** None
---
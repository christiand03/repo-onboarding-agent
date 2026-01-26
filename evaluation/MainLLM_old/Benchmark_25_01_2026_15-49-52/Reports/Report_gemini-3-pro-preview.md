# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
    - **Description:** The Repo Onboarding Agent is a comprehensive tool designed to facilitate the understanding and documentation of software repositories. It automates the process of cloning a GitHub repository, analyzing its structure (File Trees, AST, Call Graphs), and generating detailed documentation using Large Language Models (LLMs). The system employs a two-stage LLM approach: a "Helper LLM" for granular analysis of functions and classes, and a "Main LLM" for synthesizing final reports. It includes a Streamlit-based frontend for interactive use, allowing users to visualize data, chat with the repository context, and manage generated reports.
    - **Key Features:** 
      - **Automated Code Analysis:** detailed parsing of Python code into ASTs, generating call graphs and dependency maps.
      - **Dual-LLM Pipeline:** orchestrates specialized LLMs (Helper & Main) to generate high-fidelity documentation and architectural insights.
      - **Interactive Frontend:** Streamlit application providing visualization of repo structure, metric dashboards, and a chat interface.
      - **Data Persistence:** uses MongoDB to store user profiles, chat history, and analysis results securely.
      - **Notebook Support:** specialized handling for converting and analyzing Jupyter Notebooks (`.ipynb`) including image extraction.
    - **Tech Stack:** Python, Streamlit, MongoDB, LangChain, GitPython, NetworkX, Pydantic, Matplotlib.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root --> .env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json
    root --> SystemPrompts
    SystemPrompts --> SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt
    root --> backend
    backend --> AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py
    root --> database
    database --> db.py
    root --> frontend
    frontend --> .streamlit
    .streamlit --> config.toml
    frontend --> __init__.py<br/>frontend.py
    frontend --> gifs
    gifs --> 4j.gif
    root --> notizen
    notizen --> Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md
    notizen --> grafiken
    grafiken --> 1
    1 --> File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot
    grafiken --> 2
    2 --> FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot
    grafiken --> Flask-Repo
    Flask-Repo --> __init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot
    grafiken --> Repo-onboarding
    Repo-onboarding --> AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot
    root --> result
    result --> ast_schema_01_12_2025_11-49-24.json<br/>notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md
    root --> schemas
    schemas --> types.py
    root --> statistics
    statistics --> savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png
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

    To install dependencies, run:
    `pip install -r requirements.txt`

    ### Setup Guide
    1.  Clone the repository.
    2.  Install dependencies using the command above.
    3.  Configure your environment variables by copying `.env.example` to `.env` and filling in the required API keys (Gemini, OpenAI, etc.) and database connection strings.

    ### Quick Startup
    Run the frontend application to start the agent:
    `streamlit run frontend/frontend.py`

    ## 3. Use Cases & Commands
    The Repo Onboarding Agent is primarily used for:
    *   **Repository Analysis:** Rapidly understanding a new codebase by providing a GitHub URL. The tool analyzes the structure, dependencies, and code logic.
    *   **Documentation Generation:** Automatically generating detailed documentation for functions and classes within a repository.
    *   **Interactive Onboarding:** Using the chat interface to ask questions about the repository's functionality, architecture, or specific code segments.
    *   **Architecture Visualization:** Visualizing file dependencies and call graphs to understand the system's architecture.

    **Primary Commands:**
    *   `streamlit run frontend/frontend.py`: Launches the main web interface.

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here



## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into a Python module path string. It first attempts to calculate the relative path of the file with respect to a specified project root. If this fails, it falls back to using just the base name of the file. The function then removes the '.py' extension if present and replaces all operating system path separators with dots to form the module path. Finally, it handles '__init__' modules by removing '. __init__' from the end of the module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:**
    - **Calls:** *None*
    - **Called By:** *None*

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` and is designed to traverse the Abstract Syntax Tree (AST) of Python code. Its primary purpose is to extract structured information about imports, functions, and classes within a given source file. It builds a `schema` dictionary that categorizes these elements, including details like identifiers, docstrings, and source code segments. This class acts as a foundational component for static code analysis, enabling the collection of metadata from Python source files.
*   **Instantiation:** *None*
*   **Dependencies:** *None*
*   **Constructor:**
    *   *Description:* The `__init__` method initializes the ASTVisitor with the raw source code, the file's absolute path, and the project's root directory. It calculates the module path based on these inputs and sets up an empty `schema` dictionary to store discovered imports, functions, and classes. It also initializes `_current_class` to `None` to track the class currently being visited during AST traversal.
    *   *Parameters:*
        - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
        - **source_code** (`str`): The raw source code string of the file being visited.
        - **file_path** (`str`): The absolute path to the file being visited.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self: ASTVisitor, node: ast.Import)`
        *   *Description:* This method processes `ast.Import` nodes, which represent module import statements (e.g., `import module`). It iterates through each alias defined in the import statement and appends the module's name to the `imports` list within the `self.schema` dictionary. After processing the current node, it calls `self.generic_visit` to continue the AST traversal to child nodes.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** *None*
            - **Called By:** *None*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self: ASTVisitor, node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent 'from ... import ...' statements. It iterates through the imported names (aliases) and constructs a fully qualified import string (e.g., `node.module.alias.name`), which is then appended to the `imports` list in `self.schema`. Following this, it invokes `self.generic_visit` to ensure continued traversal of the AST.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** *None*
            - **Called By:** *None*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self: ASTVisitor, node: ast.ClassDef)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which define classes in the source code. It constructs a dictionary containing comprehensive information about the class, including its fully qualified identifier, name, docstring, the exact source code segment, and its start and end line numbers. This class information is then appended to the `classes` list within `self.schema`. It temporarily sets `_current_class` to this new class info for nested method processing and resets it after visiting the class's children.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** *None*
            - **Called By:** *None*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self: ASTVisitor, node: ast.FunctionDef)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, handling both standalone functions and methods defined within classes. If a class is currently being visited (indicated by `_current_class` being set), it extracts method-specific information and appends it to the `method_context` of the current class. Otherwise, for standalone functions, it extracts function-specific details and adds them to the `functions` list in `self.schema`. After processing, it calls `self.generic_visit` to continue the AST traversal.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** *None*
            - **Called By:** *None*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self: ASTVisitor, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is specifically designed to handle `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation is straightforward: it delegates the entire processing task to the `visit_FunctionDef` method. This approach ensures that asynchronous functions are analyzed and recorded in the schema in the same manner as regular synchronous functions.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** *None*
            - **Called By:** *None*

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to analyze the Abstract Syntax Trees (ASTs) of Python files within a repository and integrate call relationship data. It provides functionality to parse Python source code, extract structural information about functions, classes, and imports, and then enrich this structural data with details about how different code elements interact through calls and instantiations. Its primary role is to build a comprehensive, interconnected schema of a codebase.
*   **Instantiation:** *None*
*   **Dependencies:** The class depends on the 'ast' module for parsing Python code, the 'os' module for path manipulation, and 'getRepo.GitRepository' for repository interaction, although 'GitRepository' is only used as a type hint in 'analyze_repository's signature.
*   **Constructor:**
    *   *Description:* This constructor initializes an instance of the ASTAnalyzer class. It currently performs no specific setup or attribute assignments, serving as a placeholder for future initialization logic.
    *   *Parameters:* *None*
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self: ASTAnalyzer, full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates call relationship data (incoming and outgoing calls) into a pre-existing full schema of AST nodes. It iterates through functions and classes within the schema, updating their respective 'context' fields with 'calls', 'called_by', and 'instantiated_by' information. For classes, it also identifies and lists external dependencies based on method calls that are not internal to the class, providing a holistic view of inter-component communication.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
            - **full_schema** (`dict`): A dictionary representing the complete AST schema, including files, functions, and classes, to be enriched with relationship data.
            - **raw_relationships** (`dict`): A dictionary containing raw incoming and outgoing call relationships, typically structured by identifier.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary with integrated relationship data for functions, classes, and methods.
        *   **Usage:**
            - **Calls:** This method primarily uses dictionary access methods like 'get' and string methods like 'startswith' to process and update the schema.
            - **Called By:** *None*
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self: ASTAnalyzer, files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to construct a comprehensive AST schema. It filters for Python files, parses their content using the 'ast' module, and then visits the AST tree with an 'ASTVisitor' to extract structured node information. The method aggregates these file-specific schemas into a single 'full_schema' dictionary, handling potential parsing errors gracefully by printing warnings.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
            - **files** (`list`): A list of file objects, where each object is expected to have 'path' and 'content' attributes representing a file in the repository.
            - **repo** (`GitRepository`): An object representing the Git repository, used for context but not directly accessed in the provided method body.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary containing the AST schema for all processed Python files in the repository, structured by file path.
        *   **Usage:**
            - **Calls:** This method calls 'os.path.commonpath', 'os.path.isfile', 'os.path.dirname' for path manipulation, 'ast.parse' to parse Python code, and instantiates and uses 'ASTVisitor' to traverse the AST.
            - **Called By:** *None*

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends NodeVisitor to analyze Python source code and build a graph of file dependencies. It initializes with a specific file and repository root, then traverses the Abstract Syntax Tree (AST) to identify and resolve import statements. The class's primary responsibility is to populate an internal dictionary, `import_dependencies`, which maps each file to the set of modules it imports, handling both absolute and relative import paths.
*   **Instantiation:** *None*
*   **Dependencies:** The class relies on external components such as `ast` module elements (e.g., `NodeVisitor`, `Import`, `ImportFrom`, `parse`, `walk`, `literal_eval`), `keyword.iskeyword`, and `pathlib.Path` for file system interactions.
*   **Constructor:**
    *   *Description:* This constructor initializes the FileDependencyGraph instance by setting the `filename` and `repo_root` attributes. These attributes are crucial for resolving file paths and managing dependencies within the repository during AST traversal.
    *   *Parameters:*
        - **filename** (`str`): The path to the file currently being analyzed for dependencies.
        - **repo_root** (`Any`): The root directory of the repository, used for resolving file paths and imports.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(node: ImportFrom)`
        *   *Description:* This method is responsible for resolving relative import statements, such as `from .. import name1, name2`. It calculates the actual module or symbol names based on the import's `level` and the current file's location within the repository. The method checks for the existence of corresponding module files or symbols exported via `__init__.py` files. If no matching module or symbol can be resolved, it raises an ImportError.
        *   *Parameters:*
            - **node** (`ImportFrom`): An AST node representing the 'from ... import ...' statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of strings, where each string is a resolved module or symbol name.
        *   **Usage:**
            - **Calls:** *None*
            - **Called By:** *None*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* This method processes AST nodes representing `Import` or `ImportFrom` statements. Its purpose is to record the identified import dependencies in the class's `import_dependencies` dictionary. It adds the imported module or symbol name, either directly from the node's alias or from an optionally provided `base_name`, to the set of dependencies for the current `self.filename`. After processing, it calls `self.generic_visit(node)` to continue the AST traversal.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing an import statement.
            - **base_name** (`str | None`): An optional base name for the module, typically used when resolving 'from ... import ...' statements.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** *None*
            - **Called By:** *None*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ImportFrom)`
        *   *Description:* This method specifically handles `ImportFrom` AST nodes, which represent 'from module import name' statements. If the import is absolute (i.e., `node.module` is present), it extracts the last component of the module name and passes it to `visit_Import`. For relative imports (where `node.module` is None), it attempts to resolve the actual module names using the `_resolve_module_name` helper method. Any successfully resolved base names are then passed to `visit_Import` to record the dependency. It also includes basic error handling for failed relative import resolutions and continues the AST traversal with `self.generic_visit(node)`.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** *None*
            - **Called By:** *None*

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a repository. It initializes a NetworkX directed graph and then uses an instance of `FileDependencyGraph` to traverse the Abstract Syntax Tree (AST) of a specified file. The visitor collects all import relationships, which are then used to populate the graph. Each file involved in an import relationship becomes a node, and a directed edge is added from a file to another if it imports that file. The resulting graph illustrates the import structure discovered.
*   **Parameters:**
    - **filename** (`str`): The path to the file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies between them.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** *None*

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** The `build_repository_graph` function constructs a directed graph representing file-level dependencies across a Git repository. It iterates through all Python files, parsing each into an Abstract Syntax Tree. For each file, it generates a local dependency graph using `build_file_dependency_graph`. These individual file graphs are then merged into a single global NetworkX directed graph, which is subsequently returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object representing the code repository to analyze.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated file-level dependencies across the entire repository.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** *None*

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function identifies and returns a list of all Python files within a specified directory and its subdirectories. It first converts the input directory string into an absolute Path object. Then, it recursively searches for all files ending with '.py' within this root path. Finally, it returns these file paths as a list of Path objects, with each path made relative to the initial root directory.
*   **Parameters:**
    - **directory** (`str`): The string path to the root directory from which to start the recursive search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of pathlib.Path objects, where each Path represents a Python file found within the specified directory, with paths relative to the input 'directory'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** *None*

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a robust interface for interacting with various Large Language Models (LLMs), including Google Gemini, OpenAI, Ollama, and custom endpoints, to generate structured documentation for Python functions and classes. It centralizes the logic for loading LLM system prompts, dynamically configuring LLM clients, managing API batch requests, and handling rate limits. The class leverages Pydantic for strict input/output validation, ensuring that the generated documentation adheres to predefined schemas for FunctionAnalysis and ClassAnalysis.
*   **Instantiation:** *None*
*   **Dependencies:** This class depends on external libraries such as `json`, `logging`, `time`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`, and custom Pydantic schemas like `FunctionAnalysis`, `ClassAnalysis`, `FunctionAnalysisInput`, and `ClassAnalysisInput`.
*   **Constructor:**
    *   *Description:* This constructor initializes the LLMHelper, loading system prompts from specified files for function and class analysis. It dynamically configures the appropriate LLM client (Gemini, OpenAI, Ollama, or a custom endpoint) based on the provided model name and API key. It also sets up structured output capabilities for FunctionAnalysis and ClassAnalysis schemas and configures batch processing settings for API calls.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **function_prompt_path** (`str`): The file path to the system prompt text used for guiding the LLM in function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt text used for guiding the LLM in class analysis.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, such as Ollama or other self-hosted models.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* This private method sets the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It assigns specific batch sizes for various Gemini, Llama, and GPT models, as well as custom or aliased models, to optimize API calls and respect rate limits. If an unknown model is encountered, it logs a warning and defaults to a conservative batch size of 2.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch processing settings.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method internally calls `logging.warning` if an unknown model is provided.
            - **Called By:** This method is called by the `__init__` constructor of the `LLMHelper` class during initialization.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* This method processes a list of `FunctionAnalysisInput` objects to generate structured function documentation using the configured LLM. It converts each input into a JSON payload, constructs conversations with a system prompt, and then sends these in batches to the LLM. It handles potential errors during batch processing by extending the results with `None` and includes a waiting period between batches to manage API rate limits effectively.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary data for function analysis.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, or `None` for inputs that failed during processing, maintaining the original order.
        *   **Usage:**
            - **Calls:** This method calls `json.dumps` to serialize input, `model_dump` on input objects, `SystemMessage` and `HumanMessage` for conversation formatting, `self.function_llm.batch` to send requests, `logging.info` for progress, `logging.error` for exceptions, and `time.sleep` for rate limiting.
            - **Called By:** *None*
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* This method is responsible for generating structured class documentation by processing a list of `ClassAnalysisInput` objects. It prepares JSON payloads from the inputs, creates conversations with a class-specific system prompt, and dispatches these conversations to the LLM in batches. The method incorporates error handling for batch calls, filling the result list with `None` for failed items, and implements a delay between batches to comply with API rate limits.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary data for class analysis.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, or `None` for inputs that failed during processing, maintaining the original order.
        *   **Usage:**
            - **Calls:** This method calls `json.dumps` to serialize input, `model_dump` on input objects, `SystemMessage` and `HumanMessage` for conversation formatting, `self.class_llm.batch` to send requests, `logging.info` for progress, `logging.error` for exceptions, and `time.sleep` for rate limiting.
            - **Called By:** *None*

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a test orchestrator for the LLMHelper class, demonstrating its functionality by processing predefined dummy data. It sets up multiple FunctionAnalysisInput and FunctionAnalysis objects, along with a ClassAnalysisInput, to simulate a complete analysis workflow. The function initializes an LLMHelper instance, then calls its `generate_for_functions` method with the prepared inputs. Finally, it logs the results and prints the aggregated documentation in JSON format.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a central interface for interacting with various large language models (LLMs), abstracting away the specifics of different providers. It handles the initialization of LLM clients (Gemini, OpenAI-compatible, Ollama) based on configuration, loads a system prompt, and provides methods for both single-response and streaming interactions. This class enables flexible integration of LLMs into applications, allowing for different models and deployment environments.
*   **Instantiation:** *None*
*   **Dependencies:** The class has no explicit functional dependencies listed in the input context.
*   **Constructor:**
    *   *Description:* This constructor initializes the MainLLM class by setting up the API key, loading a system prompt from a specified file, and configuring the appropriate Language Model (LLM) client based on the `model_name`. It supports various LLM providers like Gemini, OpenAI-compatible APIs (e.g., SCADSLLM), and Ollama, ensuring the correct client is instantiated for subsequent interactions.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service. A ValueError is raised if it's not provided.
        - **prompt_file_path** (`str`): The file path to a text file containing the system prompt that will guide the LLM's behavior. A FileNotFoundError is raised if the file does not exist.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to "gemini-2.5-pro". This parameter determines which LLM client (Gemini, OpenAI, or Ollama) is initialized.
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, particularly relevant for Ollama or other OpenAI-compatible services. If not provided for Ollama, it defaults to OLLAMA_BASE_URL.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* This method sends a user input to the configured LLM and retrieves a single, complete response. It constructs a list of messages including the class's system_prompt and the provided user_input, then uses the self.llm.invoke method to get the LLM's reply. The method includes error handling to log any issues during the LLM call and returns None in case of an exception.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:*
            - **content** (`str`): The textual content of the LLM's response if the call is successful.
            - **None** (`None`): Returns None if an error occurs during the LLM invocation.
        *   **Usage:**
            - **Calls:** This method calls SystemMessage and HumanMessage to format the input, logging.info and logging.error for operational messages, and self.llm.invoke to interact with the underlying LLM.
            - **Called By:** *None*
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* This method provides a streaming interface to the LLM, allowing it to return responses in chunks rather than a single complete message. It constructs the message payload similar to call_llm and then uses self.llm.stream to obtain an iterator. Each chunk's content is yielded, enabling real-time display or processing of the LLM's output. Error handling is included to yield an error message if the streaming process fails.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM for streaming response.
        *   *Returns:*
            - **content** (`str`): Yields chunks of textual content from the LLM's streaming response.
            - **error_message** (`str`): Yields an error message string if an exception occurs during the streaming process.
        *   **Usage:**
            - **Calls:** This method calls SystemMessage and HumanMessage to format the input, logging.info and logging.error for operational messages, and self.llm.stream to interact with the underlying LLM in a streaming fashion.
            - **Called By:** *None*

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract fundamental project information from common project files such as README, pyproject.toml, and requirements.txt. It initializes an internal data structure to store various project details, including an overview, installation steps, key features, and tech stack. The class orchestrates the parsing of these files, prioritizing structured data sources like pyproject.toml over less structured ones like README, and provides a consolidated view of the project's basic information.
*   **Instantiation:** *None*
*   **Dependencies:** This class depends on the 're' module for regular expressions, the 'os' module for path manipulation, the 'tomllib' module for TOML parsing, and 'typing.List', 'typing.Dict', 'typing.Any', 'typing.Optional' for type hinting.
*   **Constructor:**
    *   *Description:* The constructor initializes the instance by setting a constant string for 'information not found' and creating a nested dictionary `self.info`. This dictionary is pre-populated with placeholder values for project overview and installation details, ensuring a consistent structure for extracted information.
    *   *Parameters:* *None*
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content: str)`
        *   *Description:* This method removes null bytes from a given string, which can occur due to encoding errors, particularly when a file encoded in UTF-16 is incorrectly read as UTF-8. It first checks if the input content is empty, returning an empty string if so, otherwise it replaces all occurrences of the null byte character ('\x00') with an empty string.
        *   *Parameters:*
            - **content** (`str`): The string content to be cleaned.
        *   *Returns:*
            - **""** (`str`): The cleaned string with null bytes removed.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods or functions within its source code.
            - **Called By:** This method is called by _parse_readme, _parse_toml, and _parse_requirements.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This method searches for a specific file within a provided list of file objects based on a list of patterns. It iterates through each file and each pattern, performing a case-insensitive comparison of the file's path against the pattern. The method returns the first file object whose path ends with any of the specified patterns, or None if no matching file is found.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of string patterns (e.g., file extensions or names) to match against file paths.
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have a 'path' attribute.
        *   *Returns:*
            - **""** (`Optional[Any]`): The first file object that matches one of the patterns, or None if no match is found.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods or functions within its source code.
            - **Called By:** This method is called by extrahiere_info.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This method extracts text content located directly under a Markdown level 2 heading (##) that matches one of the specified keywords. It dynamically constructs a regular expression pattern using the provided keywords to find the relevant heading. The method then captures all subsequent content until another level 2 heading or the end of the document, returning the stripped text of that section.
        *   *Parameters:*
            - **inhalt** (`str`): The full Markdown content as a string.
            - **keywords** (`List[str]`): A list of keywords to match against the Markdown heading (case-insensitive).
        *   *Returns:*
            - **""** (`Optional[str]`): The extracted section content as a string, or None if no matching section is found.
        *   **Usage:**
            - **Calls:** This method calls re.escape, re.compile, re.IGNORECASE, re.DOTALL, pattern.search, match.group, and strip.
            - **Called By:** This method is called by _parse_readme.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This method parses the content of a README file to extract various project details such as the title, description, key features, tech stack, current status, installation instructions, and a quick start guide. It first cleans the content using `_clean_content` and then uses regular expressions and the `_extrahiere_sektion_aus_markdown` helper to find and extract information from different sections. The extracted data is then used to update the `self.info` dictionary.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the README file.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self._clean_content, re.search, and self._extrahiere_sektion_aus_markdown.
            - **Called By:** This method is called by extrahiere_info.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This method parses the content of a `pyproject.toml` file to extract project-level information like the project name, description, and dependencies. It begins by cleaning the input content using `_clean_content`. If the `tomllib` module is available, it attempts to load the TOML content; otherwise, it prints a warning. Any successfully extracted project data is then used to update the `self.info` dictionary, handling potential `TOMLDecodeError` during parsing.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the pyproject.toml file.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self._clean_content, tomllib.loads, data.get, and print.
            - **Called By:** This method is called by extrahiere_info.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This method parses the content of a `requirements.txt` file to extract project dependencies. It first cleans the input content using `_clean_content`. It then processes each line, filtering out empty lines and comments to identify actual dependency specifications. The extracted dependencies are stored in the `self.info` dictionary, but only if the dependencies have not already been populated from another source, such as a `pyproject.toml` file.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the requirements.txt file.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self._clean_content.
            - **Called By:** This method is called by extrahiere_info.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This method orchestrates the entire process of extracting project information from various files. It first identifies relevant project files (README, pyproject.toml, requirements.txt) using `_finde_datei`. It then parses these files in a specific order of priority: `pyproject.toml` first, then `requirements.txt`, and finally `README.md`. After parsing, it formats the extracted dependencies and, if no project title was found, attempts to derive one from the provided repository URL. The method returns the comprehensive `self.info` dictionary containing all gathered project details.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file-like objects, each containing 'path' and 'content' attributes, representing the project files.
            - **repo_url** (`str`): The URL of the repository, used as a fallback to derive the project title if not found elsewhere.
        *   *Returns:*
            - **""** (`Dict[str, Any]`): A dictionary containing all extracted project information, including overview and installation details.
        *   **Usage:**
            - **Calls:** This method calls self._finde_datei, self._parse_toml, self._parse_requirements, self._parse_readme, os.path.basename, and repo_url.removesuffix.
            - **Called By:** *None*

### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST NodeVisitor designed to construct a directed call graph for a given Python source file. It traverses the Abstract Syntax Tree (AST) of a file, identifying function definitions, class definitions, import statements, and function calls. The class resolves function and method names, handles import aliases, and tracks the current scope (function or class) to accurately map caller-callee relationships, ultimately building a networkx.DiGraph representing the call structure.
*   **Instantiation:** *None*
*   **Dependencies:** This class depends on the `ast` module for parsing Python code into an Abstract Syntax Tree and the `networkx` library for creating and managing the directed graph structure.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph instance with the filename of the source code being analyzed. It sets up various internal state variables, including `current_function` and `current_class` for tracking scope, `local_defs` for local name resolution, `graph` as a networkx.DiGraph to store the call graph, `import_mapping` for resolving imported names, `function_set` to keep track of all defined functions, and `edges` to store raw caller-callee relationships.
    *   *Parameters:*
        - **filename** (`str`): The path to the Python source file being analyzed.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node: ast.AST)`
        *   *Description:* This private helper method recursively extracts the name components from an AST node representing a function call, attribute access, or simple name. It processes `ast.Call`, `ast.Name`, and `ast.Attribute` nodes to build a list of strings that represent the hierarchical path of a callable, such as `['pkg', 'mod', 'Class', 'method']`. This list is then used for resolving the full name of the callee.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node to be recursively processed, typically an ast.Call, ast.Name, or ast.Attribute.
        *   *Returns:*
            - **parts** (`list[str]`): A list of string components representing the dotted name of the callable.
        *   **Usage:**
            - **Calls:** This method calls itself recursively to traverse the AST node structure.
            - **Called By:** This method is called by the `visit_Call` method to extract callee name components.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* This private helper method takes a list of potential callee name components and resolves them into fully qualified names. It first checks against local definitions (`self.local_defs`) and then against the import mapping (`self.import_mapping`). If a name cannot be resolved through these mechanisms, it constructs a full name using the current filename and class context. This ensures that each callee is identified with a unique, fully qualified path.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains string components of a potential callee's name.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of fully qualified string names for the resolved callees.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods within the class.
            - **Called By:** This method is called by the `visit_Call` method to resolve the full names of called functions or methods.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None)`
        *   *Description:* This private helper method constructs a fully qualified name for a given base name, incorporating the filename and an optional class name. If a `class_name` is provided, the format will be `filename::class_name::basename`; otherwise, it will be `filename::basename`. This ensures unique identification of functions and methods within the call graph.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method (e.g., 'my_function').
            - **class_name** (`str | None`): The name of the class if the function is a method, or None if it's a top-level function.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name of the function or method.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods within the class.
            - **Called By:** This method is called by the `visit_FunctionDef` method to create a unique identifier for a defined function or method.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private helper method determines the identifier for the current calling context. It returns the `self.current_function` if a function is currently being visited. If no function context is active, it returns a placeholder string indicating either the filename (if available) or a generic '<global-scope>' to represent calls made at the module level.
        *   *Parameters:* *None*
        *   *Returns:*
            - **caller_identifier** (`str`): A string representing the identifier of the current caller (function name or global scope).
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods within the class.
            - **Called By:** This method is called by the `visit_Call` method to identify the source of a function call.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method is an override from `ast.NodeVisitor` that processes `ast.Import` nodes. It iterates through each alias in the import statement, extracting the original module name and its potential alias. It then populates the `self.import_mapping` dictionary, associating the alias (or original name if no alias) with the module's full name. After processing, it calls `generic_visit` to continue AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement (e.g., `import module as alias`).
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls `self.generic_visit(node)` to ensure continued traversal of the AST.
            - **Called By:** This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when an `ast.Import` node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method is an override from `ast.NodeVisitor` that processes `ast.ImportFrom` nodes. It extracts the module name from which objects are imported and then iterates through the imported names. For each name, it updates `self.import_mapping` to associate the imported name (or its alias) with the module it came from. This helps in resolving fully qualified names for imported functions or classes.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing an `from ... import ...` statement.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods within the class.
            - **Called By:** This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when an `ast.ImportFrom` node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is an override from `ast.NodeVisitor` that processes `ast.ClassDef` nodes. It manages the `self.current_class` context by saving the previous class, setting the current class to the name of the visited class, and then recursively visiting the class's body. After the class body has been visited, it restores the `self.current_class` to its previous value, ensuring correct scope tracking.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls `self.generic_visit(node)` to continue the AST traversal into the class's body.
            - **Called By:** This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when an `ast.ClassDef` node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method is an override from `ast.NodeVisitor` that processes `ast.FunctionDef` nodes. It saves the current function context, constructs a fully qualified name for the new function using `_make_full_name`, and updates `self.local_defs` to map the function's simple name (and class-qualified name if applicable) to its full name. It then sets `self.current_function`, adds the function as a node to the `self.graph`, visits its body, adds the function to `self.function_set`, and finally restores the previous function context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls `self._make_full_name` to generate a unique identifier for the function and `self.generic_visit(node)` to traverse the function's body.
            - **Called By:** This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when an `ast.FunctionDef` node is encountered. It is also explicitly called by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is an override from `ast.NodeVisitor` that processes `ast.AsyncFunctionDef` nodes. It delegates the processing of asynchronous function definitions directly to the `visit_FunctionDef` method. This approach treats async functions similarly to regular functions for the purpose of call graph construction, ensuring they are added to the graph and their calls are tracked.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls `self.visit_FunctionDef(node)` to handle the actual processing of the function definition.
            - **Called By:** This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when an `ast.AsyncFunctionDef` node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method is an override from `ast.NodeVisitor` that processes `ast.Call` nodes. It first identifies the current caller using `_current_caller` and then extracts the callee's name components using `_recursive_call`. These components are then resolved into fully qualified names using `_resolve_all_callee_names`. Finally, it adds the resolved callees as edges from the current caller in the `self.edges` dictionary, effectively mapping the call. It then continues AST traversal with `generic_visit`.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function call.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls `self._current_caller()`, `self._recursive_call(node)`, `self._resolve_all_callee_names([parts])`, and `self.generic_visit(node)`.
            - **Called By:** This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when an `ast.Call` node is encountered.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node: ast.If)`
        *   *Description:* This method is an override from `ast.NodeVisitor` that processes `ast.If` nodes. It specifically checks for the `if __name__ == "__main__":` idiom. If this condition is met, it temporarily sets `self.current_function` to "<main_block>" to correctly attribute calls within this block to the main execution scope. After visiting the `if` block, it restores the previous `current_function`. For other `if` statements, it simply continues the generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing an if statement.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls `self.generic_visit(node)` to continue the AST traversal into the `if` or `else` block.
            - **Called By:** This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when an `ast.If` node is encountered.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and a file path as input. It creates a copy of the input graph and relabels its nodes with simple, safe identifiers (e.g., "n0", "n1") suitable for DOT file format. The original node names are preserved by assigning them as 'label' attributes to the new nodes. Finally, the modified graph is written to the specified output path as a DOT file.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The input NetworkX directed graph to be processed and saved.
    - **out_path** (`str`): The file path where the DOT representation of the graph will be written.
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** This function `build_filtered_callgraph` constructs a directed graph representing function calls within a Git repository. It first identifies all Python files and parses their Abstract Syntax Trees (ASTs) to determine a set of "own functions" using a `CallGraph` visitor. Subsequently, it iterates through these parsed files again, building a call graph that exclusively includes edges between functions identified as "own functions". The final output is a `networkx.DiGraph` where nodes are "own functions" and edges represent calls between them.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which Python files and their contents will be extracted to build the call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent "self-written" functions found in the repository and edges represent calls between these functions.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content: str)`
*   **Description:** The `wrap_cdata` function takes a string `content` as input and encloses it within XML CDATA tags. It constructs an f-string that prepends "<![CDATA[\n" and appends "\n]]>" to the provided content. This utility function is designed to escape arbitrary text for safe inclusion within XML documents, preventing issues with special characters.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped within CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A new string with the input content enclosed by `<![CDATA[\n` and `\n]]>`.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs: list, image_list: list)`
*   **Description:** The `extract_output_content` function processes a list of output objects, typically from a notebook execution, to extract text content and handle embedded images. It iterates through each output, categorizing it by type. For display data or execution results, it attempts to extract and store base64-encoded PNG or JPEG images into a provided `image_list`, returning an XML-like placeholder. If no image is present, it extracts plain text. Stream outputs are appended as raw text, and error outputs are formatted into a string containing the error name and value. The function compiles all extracted content into a list of strings.
*   **Parameters:**
    - **outputs** (`list`): A list of output objects, likely from a notebook execution, which can contain various types of data such as display data, execution results, streams, or errors.
    - **image_list** (`list`): A mutable list that will be populated with dictionaries representing extracted images. Each dictionary contains the 'mime_type' and the base64-encoded 'data' string for an image.
*   **Returns:**
    - **extracted_xml_snippets** (`list[str]`): A list of strings, where each string is either extracted text content, a formatted error message, or an XML-like placeholder for an image that was stored in the `image_list`.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type: str)`
*   **Description:** This function processes image data identified by a given MIME type. It expects to find base64 encoded image data within an external `data` dictionary, using the `mime_type` as a key. Upon retrieval, it cleans the base64 string by removing newline characters and then stores the processed image information (MIME type and data) into an external `image_list`. The function returns a specific placeholder string containing the image's assigned index and its MIME type. If the `mime_type` is not found in `data`, it returns `None`, and any processing errors result in an error message string.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed. This value is used as a key to access base64 encoded image data from an external `data` dictionary.
*   **Returns:**
    - **image_placeholder_string** (`str`): A formatted string representing an image placeholder, including its index and MIME type, returned upon successful processing and storage of the image data.
    - **error_message** (`str`): A string containing an error message if an exception occurs during the processing or decoding of the image data.
    - **no_image_data_found** (`None`): Returns `None` if the specified `mime_type` is not found as a key in the external `data` dictionary.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.
    > **Warning:** The function relies on external variables `data` and `image_list` which are not defined within the function's scope or passed as parameters, making its execution context ambiguous without further information.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content: str)`
*   **Description:** This function converts the content of a Jupyter notebook, provided as a string, into an XML representation. It parses the input using `nbformat.reads` and iterates through each cell. Markdown cells are wrapped in `<CELL type="markdown">` tags, and code cells are wrapped in `<CELL type="code">` tags, with their source code CDATA-wrapped. If a code cell has outputs, these are also processed, extracted, CDATA-wrapped, and appended within `<CELL type="output">` tags. The function handles potential parsing errors by returning an error message.
*   **Parameters:**
    - **file_content** (`str`): The raw string content of a Jupyter notebook file to be converted.
*   **Returns:**
    - **result** (`tuple[str, list]`): A tuple containing two elements: the first is a string representing the XML conversion of the notebook (or an error message if parsing fails), and the second is a list of extracted images from the notebook outputs.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files: List[FileObject])`
*   **Description:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It filters the input list to find files with a '.ipynb' extension. For each identified notebook, it extracts its content and passes it to an external conversion utility. The function then aggregates the XML output and any extracted images into a structured dictionary, keyed by the notebook's file path.
*   **Parameters:**
    - **repo_files** (`List[FileObject]`): An iterable collection of file objects from a repository. Each FileObject is expected to have a 'path' attribute (string) and a 'content' attribute (Any), representing the file's location and raw data, respectively.
*   **Returns:**
    - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the string paths of the processed Jupyter notebooks. Each value is another dictionary containing two keys: 'xml' (string, the XML representation of the notebook) and 'images' (Any, any images extracted during the conversion).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, providing a structured way to access its metadata and content. It implements lazy loading for the Git blob object, file content, and size, optimizing performance by deferring expensive operations until data is actually needed. The class also offers utility methods for basic analysis and serialization into a dictionary format.
*   **Instantiation:** *None*
*   **Dependencies:** This class depends on the `git` library for `git.Tree` and `git.Blob` objects, and the `os` module for path manipulation.
*   **Constructor:**
    *   *Description:* This constructor initializes a RepoFile object by storing the file path and the Git Tree object from which the file originates. It also sets up internal attributes (`_blob`, `_content`, `_size`) to `None`, indicating that these properties will be loaded lazily upon first access.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit, from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if the `_blob` attribute is already set; if not, it attempts to retrieve the blob from the `_tree` using the stored file path. If the file is not found within the commit tree, a `FileNotFoundError` is raised.
        *   *Parameters:* *None*
        *   *Returns:*
            - **null** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:**
            - **Calls:** This method accesses `self._tree` and `self.path` to retrieve the blob.
            - **Called By:** This method is called by the `content` and `size` properties to access the underlying Git blob.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading for the file's content. It first checks if the `_content` attribute is already populated. If not, it accesses the `blob` property, reads its data stream, and decodes it into a UTF-8 string, ignoring any decoding errors.
        *   *Parameters:* *None*
        *   *Returns:*
            - **null** (`str`): The decoded content of the file as a string.
        *   **Usage:**
            - **Calls:** This method calls the `blob` property to get the Git blob object, and then calls `data_stream.read()` and `decode()` on the blob.
            - **Called By:** This method is called by `analyze_word_count` and `to_dict` when `include_content` is true.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading for the file's size in bytes. It checks if the `_size` attribute is already set. If not, it accesses the `blob` property to retrieve the Git blob object and then extracts its `size` attribute.
        *   *Parameters:* *None*
        *   *Returns:*
            - **null** (`int`): The size of the file in bytes.
        *   **Usage:**
            - **Calls:** This method calls the `blob` property to get the Git blob object and accesses its `size` attribute.
            - **Called By:** This method is called by `to_dict`.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function, demonstrating how to process the file's content. It calculates the total number of words in the file by first retrieving the file's content via the `content` property, then splitting the string by whitespace, and finally counting the resulting elements.
        *   *Parameters:* *None*
        *   *Returns:*
            - **null** (`int`): The total number of words in the file content.
        *   **Usage:**
            - **Calls:** This method calls the `content` property to retrieve the file's content and then calls the `split()` and `len()` functions.
            - **Called By:** The input context indicates no explicit callers, suggesting it's an internal utility or exposed for external use.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This special method provides a developer-friendly string representation of the RepoFile object. It returns a string that includes the class name and the file's path, which is useful for debugging and logging purposes.
        *   *Parameters:* *None*
        *   *Returns:*
            - **null** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:**
            - **Calls:** This method accesses `self.path`.
            - **Called By:** This method is implicitly called by Python's `repr()` function or when the object is printed in an interactive session.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content: bool)`
        *   *Description:* This method converts the RepoFile object into a dictionary representation, providing a structured data format. It includes the file's path, its base name, size, and type. Optionally, if `include_content` is set to `True`, the full file content is also added to the dictionary.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether to include the file's content in the dictionary. Defaults to `False`.
        *   *Returns:*
            - **null** (`dict`): A dictionary representation of the file, optionally including its content.
        *   **Usage:**
            - **Calls:** This method calls `os.path.basename`, `self.size` (property), and `self.content` (property).
            - **Called By:** The input context indicates no explicit callers, suggesting it's an exposed method for serialization or data transfer.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with a Git repository. It handles the cloning of a remote repository into a temporary local directory upon instantiation and offers methods to retrieve all files, organize them into a hierarchical tree structure, and ensure proper cleanup of the temporary directory. It also implements the context manager protocol, allowing for safe and automatic resource management.
*   **Instantiation:** *None*
*   **Dependencies:** This class depends on `tempfile` for temporary directory management, `git.Repo` and `git.GitCommandError` from the GitPython library for Git operations, and `logging` for informational messages. It also implicitly depends on a `RepoFile` class for file representation.
*   **Constructor:**
    *   *Description:* The constructor initializes a GitRepository object by cloning the specified remote Git repository into a newly created temporary directory. It sets up instance attributes for the repository URL, the path to the temporary directory, the GitPython Repo object, the latest commit, and its tree, while also handling potential cloning errors.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a list of all file paths present in the cloned Git repository using the underlying Git command `ls-files`. It then iterates through these paths to create and store `RepoFile` objects in the `self.files` attribute, which are then returned. This effectively populates the repository object with a collection of its constituent files.
        *   *Parameters:* *None*
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances, each representing a file within the repository.
        *   **Usage:**
            - **Calls:** This method calls `self.repo.git.ls_files()` to list files and `RepoFile()` to create file objects.
            - **Called By:** This method is called by `get_file_tree` if the `self.files` attribute is empty.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is responsible for cleaning up the resources used by the GitRepository instance. Specifically, it deletes the temporary directory and all its contents where the Git repository was cloned. It checks if `self.temp_dir` is set before attempting to delete it and then nullifies the `self.temp_dir` attribute.
        *   *Parameters:* *None*
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods or functions within the provided context.
            - **Called By:** This method is called by the `__exit__` context manager method.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This special method enables the GitRepository object to be used as a context manager. When the object is entered in a `with` statement, this method is implicitly called and simply returns the instance itself, allowing it to be bound to a variable in the `as` clause.
        *   *Parameters:* *None*
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository class itself.
        *   **Usage:**
            - **Calls:** This method does not call any other methods or functions.
            - **Called By:** This method is implicitly called when the `GitRepository` object is used in a `with` statement.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type: type | None, exc_val: Exception | None, exc_tb: TracebackType | None)`
        *   *Description:* This special method is part of the context manager protocol, ensuring proper resource cleanup when exiting a `with` statement. It calls the `close()` method to delete the temporary repository directory, guaranteeing that resources are released regardless of whether an exception occurred within the `with` block.
        *   *Parameters:*
            - **exc_type** (`type | None`): The type of the exception that caused the context to be exited, or None if no exception occurred.
            - **exc_val** (`Exception | None`): The exception instance that caused the context to be exited, or None.
            - **exc_tb** (`TracebackType | None`): The traceback object associated with the exception, or None.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls `self.close()` to perform cleanup.
            - **Called By:** This method is implicitly called when the `GitRepository` object exits a `with` statement.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content: bool)`
        *   *Description:* This method generates a hierarchical dictionary representation of the repository's file structure, mimicking a file system tree. If the `self.files` attribute is not already populated, it first calls `get_all_files()` to retrieve all repository files. It then iterates through these `RepoFile` objects, parsing their paths to build a nested dictionary where directories and files are represented with their names, types, and child elements. File content can optionally be included in the output.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether the content of the files should be included in the dictionary representation. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree of the repository.
        *   **Usage:**
            - **Calls:** This method calls `self.get_all_files()` if `self.files` is empty, and `file_obj.to_dict()` for each `RepoFile`.
            - **Called By:** This method is not explicitly called by other methods within the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart to visually compare two token counts: JSON tokens and TOON tokens. It calculates and displays a savings percentage in the chart's title. The chart includes labels, colors, a title, y-axis label, and a grid. It also annotates each bar with its corresponding integer value. Finally, the generated chart is saved to a specified output path and the plot is closed.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens for the JSON format.
    - **toon_tokens** (`int`): The number of tokens for the TOON format.
    - **savings_percent** (`float`): The calculated percentage of savings to display in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart will be saved.
*   **Returns:**
    - **None** (`None`): This function does not return any value; it saves a chart to a file as a side effect.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the effective processing time by subtracting estimated rate-limiting sleep durations from the total elapsed time. It first determines the raw duration between a start and end time. If the specified model is not a 'gemini-' model, or if the total number of items is zero, the raw duration or zero is returned, respectively. For 'gemini-' models, it calculates the number of batches, estimates the total sleep time based on a fixed sleep duration per batch (61 units), and then subtracts this from the total duration to yield the net processing time. The final result is ensured to be non-negative.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp or time object for the duration calculation.
    - **end_time** (`float`): The ending timestamp or time object for the duration calculation.
    - **total_items** (`int`): The total number of items processed, used to determine the number of batches.
    - **batch_size** (`int`): The size of each processing batch, used in conjunction with total_items to calculate batches.
    - **model_name** (`str`): The name of the model being used, which determines if rate-limiting sleep times should be considered.
*   **Returns:**
    - **net_time** (`float`): The calculated net processing time, excluding estimated sleep durations, or the total duration if no specific model is used. Returns 0 if total_items is 0.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable | None)`
*   **Description:** The main_workflow function orchestrates a comprehensive analysis pipeline for a given GitHub repository URL. It begins by extracting API keys and model configurations, then clones the specified repository to retrieve its files. The workflow proceeds to extract basic project information, construct a file tree, analyze code relationships, and build an Abstract Syntax Tree (AST) schema, which is subsequently enriched with relationship data. It then prepares inputs for a 'Helper LLM' to analyze individual functions and classes, and finally uses a 'Main LLM' to generate a comprehensive report based on all collected data. The function concludes by saving the final report and associated performance metrics, including token savings, to designated output directories.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL for analysis.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the models to be used by the helper and main LLMs.
    - **status_callback** (`callable | None`): An optional callable function used to provide real-time status updates during the workflow execution. Defaults to None.
*   **Returns:**
    - **result** (`dict`): A dictionary containing the 'report' (the final generated report as a string) and 'metrics' (a dictionary of performance statistics).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_status`
*   **Signature:** `def update_status(msg: str)`
*   **Description:** The `update_status` function processes a given message, `msg`. It first checks if a `status_callback` function is available and, if so, invokes it with the provided message. Subsequently, it logs the message using the `logging.info` facility. This function serves to standardize status updates and ensure they are consistently logged.
*   **Parameters:**
    - **msg** (`str`): The message string to be used for updating the status via a callback and for logging.
*   **Returns:**
    - **None** (`None`): This function does not explicitly return any value; it performs side effects by calling a callback and logging.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback: callable | None)`
*   **Description:** The notebook_workflow function orchestrates the analysis of Jupyter notebooks found within a specified GitHub repository. It begins by extracting a repository URL from the input, cloning the repository, and then processing its contents. The function extracts basic project information and converts any identified notebooks into an XML-like structure, including embedded images. It then iterates through each processed notebook, constructing a payload for an external Large Language Model (LLM) based on the project information, notebook content, and images. The LLM generates a report for each notebook, which are then concatenated into a final comprehensive report. Finally, the function saves this report to a markdown file and returns the report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): The input string, expected to contain a GitHub repository URL from which notebooks will be processed.
    - **api_keys** (`dict`): A dictionary containing API keys for various Large Language Model (LLM) services, such as 'gpt', 'gemini', 'scadsllm', or 'ollama'.
    - **model** (`str`): The name of the LLM model to be used for generating notebook reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`callable | None`): An optional callback function that receives status messages as strings to provide real-time updates during the workflow execution.
*   **Returns:**
    - **analysis_result** (`dict`): A dictionary containing the final concatenated report and execution metrics. The dictionary includes 'report' (str) with the LLM-generated analysis and 'metrics' (dict) with performance data.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info: dict, nb_path: str, xml_content: str, images: list)`
*   **Description:** This function constructs a multi-part payload suitable for the Gemini API, integrating contextual information, notebook structure, and embedded images. It serializes basic project details and the notebook path into an initial text part. The function then parses the provided XML content, identifying image placeholders using a regular expression. For each placeholder, it extracts the corresponding image data from the 'images' list, converts it to a base64 URL, and adds it as an image part to the payload. Any text segments within the XML content, before, between, or after image placeholders, are added as separate text parts. Finally, it returns a list of dictionaries, each representing a text or image component of the Gemini payload.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing basic project information to be included in the payload context.
    - **nb_path** (`str`): The file path of the current notebook, included in the payload context.
    - **xml_content** (`str`): The XML structure of the notebook, which may contain image placeholders to be replaced with actual image data.
    - **images** (`list`): A list of dictionaries, where each dictionary contains image data (e.g., 'data' key with a base64 string) corresponding to the image placeholders.
*   **Returns:**
    - **payload_content** (`list`): A list of dictionaries, each formatted as a content part (either 'text' or 'image_url') for the Gemini API.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into a Python module import path. It first determines the path relative to a specified project root, falling back to the base filename if a relative path cannot be computed. It then removes the '.py' extension if present and replaces system path separators with dots. Finally, it handles '__init__.py' files by removing the '.__init__' suffix to yield the package name.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative file system path to be converted.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform static analysis on a Python project to build a comprehensive call graph. It initializes with a project root and maintains internal data structures to store definitions of classes, functions, and methods, as well as the relationships between them. The class orchestrates the process of finding Python files, parsing their Abstract Syntax Trees (ASTs), collecting all defined entities, and then resolving the calls made between these entities to construct a detailed call graph.
*   **Instantiation:** *None*
*   **Dependencies:** The class depends on the os module for path manipulation and file system traversal, the ast module for parsing Python source code, the logging module for error reporting, and collections.defaultdict for efficient graph construction. It also implicitly depends on external components like path_to_module and CallResolverVisitor.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer instance by setting the project root, initializing data structures for definitions, call graph, and ASTs, and defining a set of directories to ignore during file traversal.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect definitions of functions, methods, and classes. Subsequently, it iterates through the files again to resolve call relationships between these definitions, building a comprehensive call graph. Finally, it clears the cached ASTs and returns the generated call graph.
        *   *Parameters:* *None*
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary-like object representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:**
            - **Calls:** This method calls _find_py_files to locate Python files, _collect_definitions to gather definitions, and _resolve_calls to establish call relationships.
            - **Called By:** This method is not explicitly called by any other method within the provided context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* This method processes the internal call_graph to generate a structured representation of outgoing and incoming relationships. It iterates through the call graph, extracting caller and callee identifiers, and populates two dictionaries: 'outgoing' (showing what each entity calls) and 'incoming' (showing what calls each entity). The results are then sorted and returned as a dictionary.
        *   *Parameters:* *None*
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, 'outgoing' and 'incoming'. Each value is a dictionary mapping entity identifiers to a sorted list of related entity identifiers.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods or functions within the provided context.
            - **Called By:** This method is not explicitly called by any other method within the provided context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private helper method recursively traverses the project_root directory to locate all Python files, excluding directories specified in self.ignore_dirs. It uses os.walk to navigate the file system and filters directories and files based on the .py extension and the ignore list. It returns a list of absolute paths to all identified Python files.
        *   *Parameters:* *None*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to Python files found within the project root, excluding ignored directories.
        *   **Usage:**
            - **Calls:** This method calls os.walk to traverse the file system and os.path.join to construct file paths.
            - **Called By:** This method is called by the analyze method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath: str)`
        *   *Description:* This private method is responsible for parsing a given Python file and collecting all function, method, and class definitions. It reads the file, parses it into an Abstract Syntax Tree (AST), and then walks the AST to identify FunctionDef and ClassDef nodes. For each identified definition, it determines its full qualified path name and type, storing this information in self.definitions. It also caches the AST in self.file_asts. Error handling is included for file reading or AST parsing issues.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file being analyzed.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls open, f.read, ast.parse, path_to_module (an external function), ast.walk, isinstance, _get_parent, and logging.error.
            - **Called By:** This method is called by the analyze method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree: ast.AST, node: ast.AST)`
        *   *Description:* This private helper method attempts to find the direct parent AST node of a given node within a larger tree. It iterates through all nodes in the AST and checks their children to identify if any child matches the target node. This is primarily used to determine if a FunctionDef is nested within a ClassDef to correctly identify it as a method.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent_node** (`ast.AST or None`): The parent AST node if found, otherwise None.
        *   **Usage:**
            - **Calls:** This method calls ast.walk and ast.iter_child_nodes.
            - **Called By:** This method is called by the _collect_definitions method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath: str)`
        *   *Description:* This private method processes a given Python file's AST to identify and resolve function and method calls. It retrieves the cached AST for the filepath and then instantiates a CallResolverVisitor (an external class) to traverse the AST and detect calls. The resolved calls, along with their caller information, are then extended into the self.call_graph. Error handling is included for issues during call resolution.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose calls are to be resolved.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self.file_asts.get, CallResolverVisitor (an external class), resolver.visit, resolver.calls.items, self.call_graph.extend, and logging.error.
            - **Called By:** This method is called by the analyze method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST NodeVisitor designed to traverse Python source code and identify all function and method calls. It resolves the fully qualified names of these calls and records detailed information about their callers, including the file, line number, and caller type. This class is crucial for building a comprehensive map of call relationships within a project, enabling dependency analysis and understanding code flow.
*   **Instantiation:** *None*
*   **Dependencies:** This class depends on the 'ast' module for Abstract Syntax Tree traversal, the 'os' module for path manipulation, and 'collections.defaultdict' for its internal data structures.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallResolverVisitor with essential context for AST traversal and call resolution. It sets up the file path, project root, and a dictionary of known definitions. It also establishes internal state variables such as `scope` for imports, `instance_types` for tracking object types, and `calls` (a defaultdict) to store the identified call relationships.
    *   *Parameters:*
        - **filepath** (`str`): The absolute path to the Python file currently being analyzed.
        - **project_root** (`str`): The root directory of the entire project, used for resolving module paths.
        - **definitions** (`dict`): A dictionary containing all known qualified definitions (functions, classes) within the project, used for validating resolved call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is an AST visitor specifically for `ast.ClassDef` nodes. When a class definition is encountered, it updates the visitor's internal state to reflect the current class name. This ensures that any nested function or method definitions are correctly associated with their containing class. After visiting the class's children, it restores the previous class context.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition being visited.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self.generic_visit to continue the AST traversal for child nodes.
            - **Called By:** This method is called by the ast.NodeVisitor traversal mechanism when a ClassDef node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method is an AST visitor for `ast.FunctionDef` nodes, handling both top-level functions and methods within classes. It constructs a fully qualified identifier for the function, incorporating the module and class name if applicable. This identifier is then set as the `current_caller_name` for the duration of the function's traversal, ensuring that any calls made within this function are correctly attributed to it. The previous caller name is restored upon exiting the function definition.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition being visited.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self.generic_visit to continue the AST traversal for child nodes.
            - **Called By:** This method is called by the ast.NodeVisitor traversal mechanism when a FunctionDef node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method is an AST visitor for `ast.Call` nodes, which represent function or method invocations. It attempts to resolve the fully qualified name of the called entity using the `_resolve_call_qname` helper. If the callee's qualified name is successfully resolved and exists in the known definitions, the method records detailed information about the caller, including its file, line number, identifier, and type (module, local function, method, or function). This caller information is then appended to the `calls` dictionary, keyed by the callee's qualified name.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing the function or method call being visited.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self._resolve_call_qname to determine the qualified name of the called entity and os.path.basename to extract the base filename.
            - **Called By:** This method is called by the ast.NodeVisitor traversal mechanism when a Call node is encountered.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method is an AST visitor for `ast.Import` nodes, which represent `import module` statements. It processes each imported module alias (or its original name if no alias is used) and stores its fully qualified name in the `self.scope` dictionary. This scope is crucial for resolving subsequent calls to imported modules or their attributes. After processing the import, it continues the generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing the import statement being visited.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self.generic_visit to continue the AST traversal for child nodes.
            - **Called By:** This method is called by the ast.NodeVisitor traversal mechanism when an Import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method is an AST visitor for `ast.ImportFrom` nodes, which represent `from module import name` statements. It resolves the full qualified path for each imported name, correctly handling relative imports based on `node.level`. The resolved qualified names are then stored in the `self.scope` dictionary, making them available for subsequent call resolution. It then proceeds with a generic visit of child nodes.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing the 'from ... import ...' statement being visited.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self.generic_visit to continue the AST traversal for child nodes.
            - **Called By:** This method is called by the ast.NodeVisitor traversal mechanism when an ImportFrom node is encountered.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node: ast.Assign)`
        *   *Description:* This method is an AST visitor for `ast.Assign` nodes, focusing on assignments that involve class instantiation. It checks if the assigned value is a call expression where the function being called is a simple name (e.g., `x = MyClass()`). If the called name corresponds to a known class in the `self.scope` and `self.definitions`, it records the qualified class name as the type of the assigned variable in `self.instance_types`. This mapping is essential for resolving method calls on instances later.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing the assignment statement being visited.
        *   *Returns:* *None*
        *   **Usage:**
            - **Calls:** This method calls self.generic_visit to continue the AST traversal for child nodes.
            - **Called By:** This method is called by the ast.NodeVisitor traversal mechanism when an Assign node is encountered.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node: ast.expr)`
        *   *Description:* This private helper method is responsible for resolving the fully qualified name (QName) of a function or method call. It handles two primary scenarios: direct calls to names (e.g., `func()`) by checking `self.scope` and local definitions, and attribute access calls (e.g., `obj.method()`) by looking up the type of the object in `self.instance_types` or checking `self.scope` for module-level attributes. It returns the resolved QName as a string or `None` if the name cannot be resolved.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., ast.Name for direct calls, ast.Attribute for method calls).
        *   *Returns:*
            - **qualified_name** (`str | None`): The fully qualified name of the callable if resolved, otherwise None.
        *   **Usage:**
            - **Calls:** This method does not make explicit calls to other methods or functions within the provided context, but relies on dictionary lookups and type checks.
            - **Called By:** This method is called by the visit_Call method to resolve the target of a function or method invocation.

### File: `backend/scads_key_test.py`

*Analysis data not available for this component.*

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function encrypts a given text string using a `cipher_suite`. It first performs a check: if the input text is empty or the `cipher_suite` is not initialized, it returns the original text without modification. Otherwise, it prepares the text by stripping leading/trailing whitespace and encoding it to bytes, then encrypts it using the `cipher_suite` and decodes the result back into a string.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string if encryption is performed, or the original text if encryption is skipped due to empty input or uninitialized cipher_suite.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given string using an external `cipher_suite` object. It first performs a guard check, returning the original text if the input text is empty or if `cipher_suite` is not initialized. If decryption is attempted, the text is stripped of whitespace, encoded to bytes, decrypted, and then decoded back to a string. In case of any exception during the decryption process, the original text is returned.
*   **Parameters:**
    - **text** (`str`): The string value that needs to be decrypted.
*   **Returns:**
    - **decrypted_string** (`str`): The successfully decrypted string, or the original `text` if decryption is skipped or an error occurs.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function is responsible for creating a new user entry in a database. It takes a username, display name, and a plain-text password as input. The password is first hashed using `stauth.Hasher` for security before being stored. The function constructs a user document, including empty fields for various API keys, and then inserts this document into the `dbusers` collection. Finally, it returns the unique identifier assigned to the newly created user document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user.
    - **name** (`str`): The display name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier of the newly inserted user document.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function, `fetch_all_users`, is responsible for retrieving all user records from a database collection named `dbusers`. It executes a `find()` operation on the collection, which typically returns a cursor. The function then converts this cursor into a Python list, effectively collecting all user documents. The primary purpose is to provide a comprehensive list of all users stored in the database.
*   **Parameters:** *None*
*   **Returns:**
    - **users** (`list`): A list containing all user documents retrieved from the `dbusers` collection. Each item in the list represents a user record, likely as a dictionary or similar document structure.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** This function is designed to retrieve a single user record from a database collection named `dbusers`. It takes a username as input and uses it to query the collection for a document where the `_id` field matches the provided username. The function returns the first document found that satisfies this query.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched, which is used to match the `_id` field in the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if a match is found, otherwise None if no user with the specified username exists.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function is responsible for updating a user's name in a database. It takes the existing username, which is used as the document's `_id`, and a new name to be assigned. It performs an `update_one` operation on the `dbusers` collection, setting the 'name' field to the provided new name. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose name is to be updated, used as the `_id` in the database.
    - **new_name** (`str`): The new name to be assigned to the specified user.
*   **Returns:**
    - **modified_count** (`int`): An integer representing the number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database. It takes a username and the new Gemini API key as input. The API key is first stripped of whitespace and then encrypted before being stored. The function then updates the 'gemini_api_key' field for the specified user in the 'dbusers' collection. It returns the count of documents that were modified by the update operation.
*   **Parameters:**
    - **username** (`str`): The username of the user whose Gemini API key is to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** This function is responsible for updating a user's GPT API key in the database. It first takes the provided API key, strips any leading or trailing whitespace, and then encrypts it. Finally, it updates the document corresponding to the given username in the `dbusers` collection with the newly encrypted key, returning the count of modified documents.
*   **Parameters:**
    - **username** (`str`): The username of the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be encrypted and stored for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as input. The provided URL is first stripped of any leading or trailing whitespace before being stored. The function then performs an update operation on the user's document in the 'dbusers' collection, setting the 'ollama_base_url' field. It returns an integer indicating the number of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama URL is to be updated.
    - **ollama_base_url** (`str`): The new base URL for Ollama, which will be stripped of leading/trailing whitespace before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation (typically 0 or 1).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function is responsible for securely updating a user's open-source API key in the database. It takes a username and the new API key as input. The provided API key is first stripped of leading/trailing whitespace and then encrypted before being stored. Finally, it updates the 'opensrc_api_key' field for the specified user in the 'dbusers' collection and returns the count of modified documents.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API key needs to be updated.
    - **opensrc_api_key** (`str`): The new open-source API key to be encrypted and stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 indicates success if the user exists.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** This function updates the `opensrc_base_url` field for a specific user in a database collection. It takes a username and a new opensource base URL as input. The function locates the user record using the provided username as the `_id` and sets the `opensrc_base_url` field to the new URL after stripping any leading or trailing whitespace. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose `opensrc_base_url` is to be updated.
    - **opensrc_base_url** (`str`): The new base URL for opensource projects, which will be stripped of leading/trailing whitespace before being stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation. A value of 1 typically indicates success, while 0 indicates no document was found or changed.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** This function is designed to retrieve a user's Gemini API key from a database. It takes a username as input and queries a 'dbusers' collection to find a matching user document. The query specifically projects the 'gemini_api_key' field. If a user document is found, the function extracts and returns the associated Gemini API key. If no user is found for the given username, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key associated with the user, or None if the user is not found or the key does not exist in the user document.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL associated with a specific user from a database. It queries the 'dbusers' collection using the provided username as the document's '_id'. If a user document is found, it extracts and returns the 'ollama_base_url' field. If no user is found, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL string if found for the specified user, otherwise None.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** This function retrieves the GPT API key associated with a given username from a database. It queries the `dbusers` collection to find a user document matching the provided `username`. The query specifically projects only the `gpt_api_key` field. If a user is found, it returns the `gpt_api_key`; otherwise, it returns `None`.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the GPT API key.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the username, or `None` if the user is not found or the key does not exist.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** This function is designed to retrieve an 'opensrc_api_key' associated with a specific username from a database. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided username. If a user document is found, the function extracts the 'opensrc_api_key' from it. If no user is found matching the username, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose opensource API key is to be fetched.
*   **Returns:**
    - **opensrc_api_key** (`Optional[str]`): The opensource API key as a string if found, otherwise None.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** The `fetch_opensrc_url` function is designed to retrieve the 'opensrc_base_url' associated with a specific user from a database. It takes a username as input and performs a database query on the `dbusers` collection to locate the corresponding user document. If a user is found, the function extracts and returns the 'opensrc_base_url' field. If no user is found or the field is missing, it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose opensrc base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The opensrc base URL associated with the user, or None if the user is not found or the URL is not set.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is designed to remove a specific user record from the `dbusers` collection in a database. It identifies the user to be deleted using their `username`, which is mapped to the `_id` field in the database. The function executes a `delete_one` operation and returns the count of documents successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user to be deleted, corresponding to the `_id` field in the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation (typically 0 or 1 for `delete_one`).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts various API keys and base URLs associated with a specific username from a database. It first queries the 'dbusers' collection to find the user. If the user is not found, it returns null values for all keys and URLs. Otherwise, it decrypts the Gemini, GPT, and open-source API keys and returns them along with the Ollama and open-source base URLs.
*   **Parameters:**
    - **username** (`str`): The username used to identify the user in the database.
*   **Returns:**
    - **gemini_plain** (`str or None`): The decrypted Gemini API key, or None if the user is not found.
    - **ollama_plain** (`str`): The Ollama base URL, or an empty string if not found in user data, or None if the user is not found.
    - **gpt_plain** (`str or None`): The decrypted GPT API key, or None if the user is not found.
    - **opensrc_plain** (`str or None`): The decrypted open-source API key, or None if the user is not found.
    - **opensrc_url** (`str`): The open-source base URL, or an empty string if not found in user data, or None if the user is not found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** This function creates a new chat entry in a database. It constructs a dictionary containing a unique identifier generated using UUID, the provided username, the chat name, and the current timestamp. This chat dictionary is then inserted into the 'dbchats' collection using `insert_one`. The function returns the unique ID of the newly inserted chat document.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier of the newly inserted chat document.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** This function is designed to retrieve all chat records associated with a specific user from a database. It queries the 'dbchats' collection, filtering documents by the provided username. The retrieved chat records are then sorted chronologically by their 'created_at' timestamp in ascending order. Finally, the function returns these sorted chat records as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat records.
*   **Returns:**
    - **chats** (`list[dict]`): A list of chat records (dictionaries), each representing a chat associated with the specified username, sorted by creation date.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function queries a database collection, `dbchats`, to determine if a chat entry exists based on a provided username and chat name. It performs a lookup for a document matching both criteria and returns a boolean indicating its presence. The function effectively checks for the uniqueness or existence of a specific chat.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to verify its existence.
*   **Returns:**
    - **exists** (`bool`): Returns True if a chat matching the provided username and chat name is found in the database, False otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and all its associated exchanges (messages) within the database. It first updates the chat entry in the `dbchats` collection, changing its name from `old_name` to `new_name` for the specified `username`. Subsequently, it updates all related exchange entries in the `dbexchanges` collection to reflect this new chat name. The function returns the count of documents modified during the initial chat entry update operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The desired new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified in the `dbchats` collection during the chat entry rename operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str, json_tokens: int, toon_tokens: int, savings_percent: float)`
*   **Description:** This function inserts a new chat exchange record into a database collection. It generates a unique identifier for the exchange using UUID, then constructs a dictionary containing the question, answer, feedback, user details, chat name, and various optional metrics such as models used, time taken, and token counts. The record also includes a timestamp for creation. The function attempts to insert this structured data into the 'dbexchanges' collection and returns the new ID upon successful insertion, or None if a database error occurs.
*   **Parameters:**
    - **question** (`str`): The user's question or prompt in the exchange.
    - **answer** (`str`): The generated answer or response for the question.
    - **feedback** (`str`): Feedback provided for the exchange, typically a rating or category.
    - **username** (`str`): The username associated with this chat exchange.
    - **chat_name** (`str`): The name of the chat session to which this exchange belongs.
    - **helper_used** (`str`): Optional: The name of the helper model utilized for this exchange. Defaults to an empty string.
    - **main_used** (`str`): Optional: The name of the main model utilized for this exchange. Defaults to an empty string.
    - **total_time** (`str`): Optional: The total time taken for processing the exchange. Defaults to an empty string.
    - **helper_time** (`str`): Optional: The time taken specifically by the helper model. Defaults to an empty string.
    - **main_time** (`str`): Optional: The time taken specifically by the main model. Defaults to an empty string.
    - **json_tokens** (`int`): Optional: The number of JSON tokens consumed during the exchange. Defaults to 0.
    - **toon_tokens** (`int`): Optional: The number of 'toon' tokens consumed during the exchange. Defaults to 0.
    - **savings_percent** (`float`): Optional: The percentage of savings achieved for this exchange. Defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier (UUID) of the newly inserted exchange record upon successful insertion.
    - **None** (`NoneType`): Indicates that the insertion failed due to a database exception.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves exchange records from a database based on a provided username. It queries the 'dbexchanges' collection, filtering documents by the 'username' field. The results are then sorted in ascending order by the 'created_at' timestamp before being converted into a list and returned. The sorting is explicitly noted as important for display purposes.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchange records in the database.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents (dictionaries) associated with the given username, sorted by their 'created_at' timestamp.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a list of exchange records from a database collection named `dbexchanges`. It filters these records based on a provided username and chat name. The results are then sorted in ascending order by their `created_at` timestamp before being returned as a list.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchange records.
    - **chat_name** (`str`): The name of the chat used to filter the exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (documents) that match the specified username and chat name, sorted by their creation time.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function is designed to update the feedback score for a specific exchange record within a database. It takes an exchange identifier and an integer feedback value as input. The function executes an update operation on the `dbexchanges` collection, targeting a document by its `_id` and setting its `feedback` field to the provided integer value. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated.
    - **feedback** (`int`): The integer feedback value to be set for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates the feedback message associated with a specific exchange record in the database. It takes an exchange identifier and a new feedback message as input. The function uses `dbexchanges.update_one` to locate the document by its `_id` and set the `feedback_message` field. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange record to be updated.
    - **feedback_message** (`str`): The new feedback message to be set for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is responsible for deleting a single exchange record from a MongoDB collection. It accepts a unique identifier, `exchange_id`, and uses it to locate and remove the corresponding document. The operation targets the `_id` field within the `dbexchanges` collection. Upon completion, it reports the number of documents that were successfully deleted.
*   **Parameters:**
    - **exchange_id** (`str`): The unique string identifier of the exchange document to be removed from the database.
*   **Returns:**
    - **deleted_count** (`int`): An integer indicating the number of documents that were deleted. This will typically be 0 or 1 for a delete_one operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is responsible for completely deleting a chat and all its associated messages (exchanges) for a given user. It ensures data consistency by first removing all messages linked to the chat and then deleting the chat entry itself. The function returns the count of chats that were deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted from the database. This is typically 1 if the chat was found and deleted, or 0 if not found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list: list[str])`
*   **Description:** This function processes a list of strings, where each string is expected to represent a path or a URL. It iterates through the provided `model_list` and for each item, it splits the string by the '/' character. The function then extracts the last component of the split string. The primary purpose is to obtain a 'cleaned' or base name from each input string, returning a new list containing these extracted names.
*   **Parameters:**
    - **model_list** (`list[str]`): A list of strings, where each string is expected to be a path or URL containing '/' characters that need to be cleaned.
*   **Returns:**
    - **cleaned_names** (`list[str]`): A new list containing the last component of each input string after splitting by '/', effectively providing a list of base names.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list: list, category_name: str)`
*   **Description:** The `get_filtered_models` function filters a given list of models (`source_list`) based on a specified `category_name`. It retrieves a set of keywords associated with the category from a global `CATEGORY_KEYWORDS` dictionary. If the category's keywords include "STANDARD", the function returns only those models from `source_list` that are also present in `STANDARD_MODELS`. Otherwise, it iterates through the `source_list` and collects models whose names (case-insensitive) contain any of the category's keywords. If any models match the keyword filter, the filtered list is returned; otherwise, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The initial list of models to be filtered.
    - **category_name** (`str`): The name of the category used to determine filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered according to the specified category's keywords. If no models match the keyword filter, the original `source_list` is returned. If the category implies 'STANDARD', only models present in `STANDARD_MODELS` are returned.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function, `save_gemini_cb`, is designed to save a new Gemini API key. It retrieves the potential new key from the Streamlit session state. If a new key is present, it updates the Gemini key in the database using the current username and the new key. After successfully updating, it clears the key from the session state and displays a success notification to the user.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function is designed to save a new Ollama URL. It retrieves the potential new URL from the Streamlit session state. If a URL is present, it updates the Ollama URL in the database for the current user, also retrieved from the session state. Finally, it displays a confirmation toast message to the user.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by other functions in the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function is responsible for loading chat and exchange data from the database into the Streamlit session state. It ensures data consistency by first fetching predefined chats, then associating exchanges with them, and creating a default chat if no chats exist. The function also manages the active chat within the session state and prevents redundant data loading for the same user.
*   **Parameters:**
    - **username** (`str`): The username for which chat and exchange data should be loaded from the database.
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: dict, val: any)`
*   **Description:** This function is designed to handle changes in feedback for an exchange object. It updates the 'feedback' key within the provided exchange dictionary (`ex`) with the new value (`val`). Subsequently, it calls a database utility function, `db.update_exchange_feedback`, to persist this feedback change using the exchange's ID. Finally, it triggers a full re-execution of the Streamlit application using `st.rerun()` to reflect the changes in the UI.
*   **Parameters:**
    - **ex** (`dict`): The exchange object, expected to be a dictionary containing at least a 'feedback' key and an '_id' key.
    - **val** (`any`): The new feedback value to be assigned to the exchange object.
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: str, ex: dict)`
*   **Description:** This function is responsible for deleting a specific exchange from both the database and the application's session state. It first calls `db.delete_exchange_by_id` using the exchange's `_id`. Subsequently, it checks if the associated chat exists in `st.session_state.chats` and, if the exchange is found within that chat's exchanges list, it removes it. Finally, it triggers a full Streamlit rerun to refresh the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be deleted.
    - **ex** (`dict`): The exchange object to be deleted, which is expected to contain an '_id' key for database deletion.
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** This function is responsible for deleting a specified chat for a given user and managing the application's chat state. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it updates the Streamlit session state by removing the chat from `st.session_state.chats`. If other chats exist, the active chat is reset to the first available chat; otherwise, a new default chat named 'Chat 1' is created via `db.insert_chat` and set as the active chat. Finally, it triggers a Streamlit rerun to reflect these changes.
*   **Parameters:**
    - **username** (`str`): The username of the user whose chat is to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text: str)`
*   **Description:** This function aims to extract a repository name from a given input text. It first attempts to find a URL within the text using a regular expression. If a URL is identified, it then parses this URL to isolate its path component. The last segment of the URL path is considered the potential repository name, with any '.git' suffix being removed. The function returns the extracted repository name as a string or None if no URL is found or a repository name cannot be successfully derived.
*   **Parameters:**
    - **text** (`str`): The input string that may contain a URL from which to extract a repository name.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string, or None if no valid URL or repository name could be found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text: str)`
*   **Description:** This function acts as a generator that simulates streaming text by yielding individual words from an input string. It takes a complete string, splits it into words, and then yields each word sequentially, appending a space after it. A small delay is introduced between each word yield to mimic a real-time streaming effect. This is typically used in user interfaces to display text progressively.
*   **Parameters:**
    - **text** (`str`): The input string that needs to be streamed word by word.
*   **Returns:**
    - **word_chunk** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str, should_stream: bool)`
*   **Description:** This function processes a given markdown text, identifying and rendering embedded Mermaid diagrams. It splits the input text into segments of regular markdown and Mermaid code blocks. Regular markdown segments are rendered using `st.markdown` or streamed via `st.write_stream` if `should_stream` is true. Mermaid code blocks are rendered using `st_mermaid`, with a fallback to `st.code` if the Mermaid rendering fails.
*   **Parameters:**
    - **markdown_text** (`str`): The input text, which may contain markdown and embedded Mermaid diagram code blocks.
    - **should_stream** (`bool`): A boolean flag indicating whether non-Mermaid text parts should be streamed using `st.write_stream` or rendered directly with `st.markdown`. Defaults to `False`.
*   **Returns:**
    - **None** (`None`): This function does not explicitly return a value. It performs side effects by rendering content to a Streamlit application. It returns early if `markdown_text` is empty.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** This function `render_exchange` is designed to display a single chat exchange within a Streamlit application. It renders the user's question and the assistant's answer, providing an interactive interface for user feedback and actions. The assistant's response includes a toolbar with buttons for 'like' (helpful), 'dislike' (not helpful), adding a comment via a popover, downloading the response, and deleting the exchange. It also handles error scenarios, displaying an error message and a delete option if the answer indicates an error.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing a single chat exchange. It contains keys such as 'question', 'answer', 'feedback' (integer, 1 for helpful, 0 for not helpful), 'feedback_message' (string), and '_id' (unique identifier).
    - **current_chat_name** (`str`): A string representing the name of the current chat session, used for context in operations like deleting an exchange.
*   **Returns:** *None*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to encapsulate the essential metadata for a single parameter within a function. It provides a structured format to consistently represent a parameter's name, its data type, and a descriptive explanation of its role or purpose. This model is fundamental for systems requiring detailed, standardized descriptions of function signatures.
*   **Instantiation:** *None*
*   **Dependencies:** This class relies on `pydantic.BaseModel` for its core functionality, but does not explicitly list other external functional dependencies.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for ParameterDescription is automatically generated. It initializes an instance of the class by accepting values for `name`, `type`, and `description`, which are then validated according to their type hints.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type annotation or inferred type of the parameter.
        - **description** (`str`): A brief explanation of the parameter's purpose or usage.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to provide a structured representation of a function's return value. It encapsulates three key pieces of information: the name of the return value, its Python type, and a textual description. This model is intended to be used as a component within larger data structures for comprehensive function signature documentation, ensuring consistency and validation of return value details.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for ReturnDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting values for `name`, `type`, and `description`, performing automatic data validation and type coercion based on the defined annotations.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value, if it has one (e.g., for named tuples or specific data fields).
        - **type** (`str`): The Python type hint or a string representation of the return value's type (e.g., 'str', 'int', 'List[str]').
        - **description** (`str`): A detailed textual explanation of what the return value represents, its purpose, or its content.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function is used within a system. It serves as a structured data container for describing the calling context of a function. This class defines two string attributes, 'calls' and 'called_by', to detail the functions or methods that a given function calls, and the entities that call the given function, respectively.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The UsageContext class does not define an explicit `__init__` method. It inherits from `pydantic.BaseModel`, and its initialization is handled by Pydantic based on the `calls` and `called_by` fields, which are expected to be provided as keyword arguments during instantiation.
    *   *Parameters:* *None*
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to provide a structured and detailed analysis of a Python function. It serves as a data schema, encapsulating an overall summary of the function's purpose, a list of its parameters, a list of its return values, and its usage context within a larger system. This class is fundamental for representing function metadata in a standardized format.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, meaning its `__init__` method is automatically generated to validate and assign values to its defined fields. It initializes an instance by taking an overall description string, a list of `ParameterDescription` objects, a list of `ReturnDescription` objects, and a `UsageContext` object, ensuring type correctness and data integrity upon instantiation.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary describing the function's purpose and its implementation details.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each detailing a parameter of the function, including its name, type, and description.
        - **returns** (`List[ReturnDescription]`): A list of objects, each describing a possible return value of the function, including its name, type, and description.
        - **usage_context** (`UsageContext`): An object providing context on what the function calls and where it is called within the system.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** This class serves as a Pydantic model designed to structure the comprehensive analysis of a single Python function. It encapsulates the function's unique identifier, a detailed 'FunctionDescription' object containing its purpose, signature, and usage context, and an optional field for any errors encountered during its analysis. This model is fundamental for standardizing the output of function analysis within a larger system, ensuring a consistent data format for further processing.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly generates an __init__ method. This constructor is responsible for initializing instances of FunctionAnalysis by validating and assigning the 'identifier', 'description', and 'error' fields based on the provided arguments, ensuring data integrity according to the defined types.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): A detailed analysis object containing the function's overall purpose, parameters, return values, and usage context.
        - **error** (`Optional[str]`): An optional string describing any error encountered during the function's analysis. Defaults to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's constructor (`__init__` method). It structures this information into a textual description of the constructor's purpose and a list detailing each of its parameters. This class serves as a data schema for representing constructor details in a standardized, machine-readable format.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The `__init__` method, implicitly generated by Pydantic's BaseModel, initializes an instance of ConstructorDescription. It validates and assigns the provided 'description' string and a list of 'ParameterDescription' objects to the corresponding instance attributes. This ensures that constructor metadata conforms to the defined schema.
    *   *Parameters:*
        - **description** (`str`): A string providing a high-level summary or explanation of the constructor's functionality.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing a specific parameter accepted by the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate and validate contextual information about other classes. It specifically stores two string attributes: 'dependencies', which summarizes external dependencies, and 'instantiated_by', which describes where the class is instantiated. This model provides a structured way to represent a class's integration points and external requirements within a larger system.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly declare external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for ClassContext is implicitly generated by Pydantic's BaseModel. It handles the initialization of instances by accepting `dependencies` and `instantiated_by` as keyword arguments, performing type validation, and assigning these values as instance attributes.
    *   *Parameters:*
        - **dependencies** (`str`): A string summarizing the external dependencies required by the class being described.
        - **instantiated_by** (`str`): A string summarizing the locations or components that instantiate the class being described.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to structure a comprehensive analysis of a Python class. It serves as a data container, holding an overall textual description of the class, detailed information about its constructor, a list of analyses for each of its methods, and contextual information regarding its dependencies and where it is instantiated. This model ensures a standardized format for class analysis outputs.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class inherits from Pydantic's BaseModel, so its constructor is implicitly generated by Pydantic. It initializes the instance attributes `overall`, `init_method`, `methods`, and `usage_context` based on the provided arguments, performing validation according to their type hints.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose and functionality.
        - **init_method** (`ConstructorDescription`): An object containing the description and parameters of the class's constructor.
        - **methods** (`List[FunctionAnalysis]`): A list of detailed analyses for each method within the class.
        - **usage_context** (`ClassContext`): An object providing context about the class's dependencies and instantiation points.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing a comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed ClassDescription object containing its constructor and method analyses, and an optional error field to report issues during the analysis process. This model is designed to provide a structured, machine-readable output for further processing by other AI systems.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, has its constructor implicitly generated. It initializes instances with an `identifier` (string), a `description` (ClassDescription object), and an optional `error` (string or None).
    *   *Parameters:*
        - **identifier** (`str`): The unique name or path of the class being analyzed.
        - **description** (`ClassDescription`): A detailed analysis object containing the class's overall purpose, constructor, and methods.
        - **error** (`Optional[str]`): An optional string indicating an error encountered during analysis, defaulting to None.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event within a system, likely for relationship analysis. It provides a structured format to store details such as the file path, the name of the calling function, the mode of the call (e.g., 'method', 'function'), and the line number where the call occurs. This model serves as a data container to standardize how call events are described and tracked.
*   **Instantiation:** *None*
*   **Dependencies:** This class primarily depends on Pydantic's BaseModel for its data structure and validation capabilities.
*   **Constructor:**
    *   *Description:* The CallInfo class is initialized by providing values for its defined Pydantic fields: 'file', 'function', 'mode', and 'line'. Pydantic automatically handles the constructor logic, including type validation and assignment of these values as instance attributes.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event originated.
        - **function** (`str`): The name of the function or method that performed the call.
        - **mode** (`str`): The classification of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The specific line number within the file where the call event is located.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information for analyzing a specific function. It serves as a data container, holding details about the external functions, methods, or classes that the target function invokes, as well as the locations from which the target function itself is called. This model facilitates a standardized way to represent a function's interaction within a larger codebase, aiding in static analysis or documentation generation.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. Pydantic's BaseModel automatically generates a constructor based on the type-hinted attributes `calls` and `called_by`, allowing instances to be created by passing these values as keyword arguments.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing the identifiers of other functions, methods, or classes that this function calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this function is called from.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a FunctionAnalysis object. It serves as a data contract, ensuring that all necessary components for analyzing a function—such as its mode, identifier, source code, imports, and contextual information—are provided and properly typed. This class acts as a schema for data validation and parsing before a function analysis can proceed.
*   **Instantiation:** *None*
*   **Dependencies:** This class primarily depends on Pydantic's `BaseModel` for its data validation and serialization capabilities, as well as `typing.Literal` and `typing.List` for type hinting its fields. No other explicit functional dependencies are listed in the provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, meaning its `__init__` method is implicitly generated by Pydantic. It initializes instances by validating and assigning values to its defined fields: `mode`, `identifier`, `source_code`, `imports`, and `context`.
    *   *Parameters:* *None*
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to structure and hold contextual information about a specific method within a class. It defines fields such as the method's identifier, a list of entities it calls, a list of entities that call it, its arguments, and its docstring. This model serves as a standardized data structure for method-level analysis.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `MethodContextInput` is implicitly generated by Pydantic. It handles the validation and assignment of values to the class's fields upon instantiation, ensuring type correctness and data integrity for the method's contextual information.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method being described.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls within its implementation.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects (presumably another structured type) indicating the methods or functions that call this method.
        - **args** (`List[str]`): A list of argument names that the method expects in its signature.
        - **docstring** (`Optional[str]`): The docstring content of the method, if one is provided; otherwise, it can be null.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured context information necessary for analyzing a Python class. It serves as a data container, holding lists of external dependencies, points of instantiation, and detailed context for each method within the class. This model facilitates the organized transfer and processing of contextual data for deeper code analysis.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly declare any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The constructor for ClassContextInput is implicitly generated by Pydantic's BaseModel. It initializes the instance attributes 'dependencies', 'instantiated_by', and 'method_context' based on the provided arguments, ensuring type validation and data integrity.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies relevant to the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this class is instantiated within the codebase.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing specific context for an individual method within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic model designed to define the structured input required for generating a ClassAnalysis object. It serves as a data transfer object, ensuring that all necessary information—such as the operation mode, class identifier, source code, relevant imports, and contextual data—is provided in a consistent format for subsequent analysis. This model facilitates robust data validation and parsing for the class analysis pipeline.
*   **Instantiation:** *None*
*   **Dependencies:** This class does not explicitly list any external functional dependencies within its provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. It inherits from pydantic.BaseModel, and its constructor is implicitly generated by Pydantic based on the defined fields, allowing instantiation by providing values for `mode`, `identifier`, `source_code`, `imports`, and `context`.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operation mode, which must be 'class_analysis'.
        - **identifier** (`str`): The unique name or identifier of the class being analyzed.
        - **source_code** (`str`): The raw source code of the entire class definition.
        - **imports** (`List[str]`): A list of import statements relevant to the source file.
        - **context** (`ClassContextInput`): Additional contextual information for the class analysis.
*   **Methods:**

---
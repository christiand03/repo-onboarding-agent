```md
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
    - **Description:** The Repo Onboarding Agent automates the documentation process of GitHub repositories by analyzing the code and providing structured reports.
    - **Key Features:** 
      - Code Analysis
      - Automated Documentation
      - Dependency Graph Generation
    - **Tech Stack:** Python, Langchain, Google Gemini, Streamlit, NetworkX

*   **Repository Structure:**
    ```mermaid
    graph LR
    root --> .env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json
    root --> SystemPrompts<br/>backend<br/>database<br/>frontend<br/>notizen<br/>result<br/>schemas<br/>statistics
    SystemPrompts --> SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt
    backend --> AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py
    database --> db.py
    frontend --> .streamlit<br/>__init__.py<br/>frontend.py<br/>gifs
    .streamlit --> config.toml
    gifs --> 4j.gif
    notizen --> Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md
    grafiken --> 1<br/>2<br/>Flask-Repo<br/>Repo-onboarding
    1 --> File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot
    2 --> FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot
    Flask-Repo --> __init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot
    Repo-onboarding --> AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot
    result --> ast_schema_01_12_2025_11-49-24.json<br/>notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md
    schemas --> types.py
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
pip install -r requirements.txt
    ### Setup Guide
    Information not found
    ### Quick Startup
    Information not found

    ## 3. Use Cases & Commands
    Could not be determined due to a missing README file and insufficient context.

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here



## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: type, project_root: type)`
*   **Description:** This function converts a given file system path into a Python module path string. It first attempts to calculate a relative path from a specified project root. If that fails, it uses the base name of the file. It then removes the '.py' extension if present and replaces system path separators with dots. Finally, it handles '__init__.py' files by removing the '.__init__' suffix to yield the correct package module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:** This function calls no other functions. This function is not explicitly called by any other functions in the provided context.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to systematically traverse the Abstract Syntax Tree (AST) of Python source code. Its core function is to extract and organize structured information about imports, functions, and classes found within a specified source file. It constructs a `schema` dictionary that categorizes these elements, capturing details such as identifiers, docstrings, and source code segments, while using an internal state (`_current_class`) to correctly associate methods with their respective parent classes.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its context. This class is not explicitly listed as being instantiated by any other components in its context.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes an ASTVisitor instance with the raw source code, the file's path, and the project's root directory. It calculates the module's fully qualified path and sets up an empty `schema` dictionary to store parsed imports, functions, and classes. Additionally, it initializes `_current_class` to `None`, which is used to track the class currently being visited during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw Python source code string to be analyzed.
        - **file_path** (`str`): The absolute path to the file containing the source code.
        - **project_root** (`str`): The root directory of the project, used to determine the module path.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: type, alias: type)`
        *   *Description:* This method is designed to process `ast.Import` nodes, which represent standard `import module` statements in Python. It iterates through each alias defined in the import node, extracting the module name. Each identified module name is then appended to the `imports` list within the `self.schema` dictionary. After processing all aliases, it calls `self.generic_visit(node)` to ensure continued traversal of the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* Analysis data not available for this component.
        *   **Usage:** This method calls `self.generic_visit` to continue AST traversal. This method is called by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: type, alias: type)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to `from module import name` statements. It iterates through the aliases within the node, constructing a fully qualified import string (e.g., 'module.name') for each. These constructed strings are then appended to the `imports` list within the `self.schema` dictionary. Following this, `self.generic_visit(node)` is invoked to ensure the AST traversal continues.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* Analysis data not available for this component.
        *   **Usage:** This method calls `self.generic_visit` to continue AST traversal. This method is called by the `ast.NodeVisitor` framework when an `ast.ImportFrom` node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: type, alias: type)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions in the source code. It constructs a `class_info` dictionary containing the class's identifier, name, docstring, its source code segment, and line numbers. This `class_info` is then added to the `classes` list in `self.schema`. To correctly associate nested methods, it temporarily sets `self._current_class` to this `class_info`, performs a generic visit to traverse the class's body, and then resets `self._current_class` to `None`.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* Analysis data not available for this component.
        *   **Usage:** This method calls `ast.get_docstring` to extract the docstring, `ast.get_source_segment` to get the source code, and `self.generic_visit` for AST traversal. This method is called by the `ast.NodeVisitor` framework when an `ast.ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: type, alias: type)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, representing standard function definitions. It first checks if a class is currently being visited by examining `self._current_class`. If a class is active, the function is treated as a method, and its details are appended to the `method_context` of the current class. Otherwise, it's considered a top-level function, and its information is added to the `functions` list in `self.schema`. Finally, `self.generic_visit(node)` is called to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* Analysis data not available for this component.
        *   **Usage:** This method calls `ast.get_docstring` and `ast.get_source_segment` (for top-level functions) to extract information, and `self.generic_visit` for AST traversal. This method is called by the `ast.NodeVisitor` framework when an `ast.FunctionDef` node is encountered during AST traversal.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node: type, alias: type)`
        *   *Description:* This method processes `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation is a simple delegation, calling `self.visit_FunctionDef(node)`. This means that asynchronous functions are handled identically to regular synchronous functions for the purpose of extracting and structuring their information within the schema.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* Analysis data not available for this component.
        *   **Usage:** This method calls `self.visit_FunctionDef` to handle the actual processing. This method is called by the `ast.NodeVisitor` framework when an `ast.AsyncFunctionDef` node is encountered during AST traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process source code within a repository to generate a structured Abstract Syntax Tree (AST) schema and then enrich this schema with inter-entity relationship data. It first parses Python files to extract AST nodes for functions, classes, and imports, and then integrates call and instantiation relationships to provide a holistic view of the codebase's structure and interactions. This class serves as a core component for static code analysis, providing a detailed, interconnected representation of a project's Python code.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** The class has dependencies on the 'ast' module for parsing Python code, the 'os' module for path manipulation, and 'getRepo.GitRepository' for handling repository files. It also depends on an 'ASTVisitor' class, which is instantiated internally.
*   **Constructor:**
    *   *Description:* This constructor initializes an instance of the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute initialization.
    *   *Parameters:* Analysis data not available for this component.
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(full_schema: type, raw_relationships: type)`
        *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing calls, into a structured full schema. It iterates through files, functions, and classes within the schema, populating their respective 'calls', 'called_by', and 'instantiated_by' contexts. For classes, it also identifies and lists external dependencies based on method calls that are not internal to the class.
        *   *Parameters:*
            - **full_schema** (`dict`): The complete AST schema containing file, function, and class definitions.
            - **raw_relationships** (`dict`): A dictionary containing 'outgoing' and 'incoming' call relationships.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary, now enriched with relationship data for functions, classes, and methods.
        *   **Usage:** This method calls no other methods, classes, or functions. This method is not called by any other function or method.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(files: type, repo: type)`
        *   *Description:* This method processes a list of file objects from a Git repository to build a comprehensive AST schema. It filters for Python files, parses their content using the 'ast' module, and then uses an 'ASTVisitor' to extract structured AST nodes. The method constructs a 'full_schema' dictionary, organizing the parsed AST nodes by file path, and handles potential SyntaxError or ValueError exceptions during file parsing.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though it's not explicitly used in the provided snippet beyond its type hint.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the full AST schema of the repository, organized by file path, containing parsed AST nodes for imports, functions, and classes.
        *   **Usage:** This method calls 'os.path.commonpath', 'os.path.isfile', 'os.path.dirname', 'ast.parse', and 'ASTVisitor'. This method is not called by any other function or method.

---
### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: type, tree: type, repo_root: type)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies. It initializes an empty NetworkX directed graph and then uses a `FileDependencyGraph` visitor to traverse the provided Abstract Syntax Tree (AST). The visitor populates a dictionary of import dependencies, which are then used to add nodes and edges to the graph. The resulting graph illustrates which files import other files within the context of a given repository.
*   **Parameters:**
    - **filename** (`str`): The name of the file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed for dependencies.
    - **repo_root** (`str`): The root directory of the repository, used to resolve relative import paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies.
*   **Usage:** This function calls no other functions. This function is not explicitly called by any other functions in the provided context.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: type)`
*   **Description:** This function constructs a directed graph representing file-level dependencies across an entire Git repository. It first retrieves all files from the provided GitRepository object. It then filters for Python files, parses each file's content into an Abstract Syntax Tree, and uses a helper function, build_file_dependency_graph, to determine dependencies within that specific file. Finally, it merges the nodes and edges from these individual file graphs into a single, comprehensive networkx.DiGraph that captures the global repository structure.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object containing the files to be analyzed for dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files or components within files, and edges represent dependencies between them across the repository.
*   **Usage:** This function calls no other functions. This function is not explicitly called by any other functions in the provided context.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: type)`
*   **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and converts it into an absolute `Path` object. The function then recursively searches for all files ending with ".py" within this root path. Finally, it returns a list of these Python file paths, with each path represented as a `Path` object relative to the initial input directory.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory to search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `Path` objects, each representing a Python file found within the specified directory, relative to the root directory.
*   **Usage:** This function calls no other functions. This function is not called by any other functions.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends `NodeVisitor` to analyze Python source files and construct a graph of their import dependencies. It processes both absolute and relative import statements, meticulously resolving relative paths to identify actual module or symbol dependencies. The class maintains an `import_dependencies` dictionary, mapping each analyzed file to a set of modules it imports, thereby providing a structured representation of file-level dependencies within a repository.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** "The class depends on `networkx` for graph operations, `os` for path manipulation, various `ast` modules (`Assign`, `AST`, `ClassDef`, `FunctionDef`, `Import`, `ImportFrom`, `Name`, `NodeVisitor`, `literal_eval`, `parse`, `walk`) for AST traversal and analysis, `keyword.iskeyword` for identifier validation, `pathlib.Path` for robust path handling, `getRepo.GitRepository` for repository context, and `callgraph.make_safe_dot` for visualization."
*   **Constructor:**
    *   *Description:* This constructor initializes a FileDependencyGraph instance by storing the `filename` of the file currently being analyzed and the `repo_root` directory. These attributes are crucial for resolving file paths and managing dependencies within the context of the repository.
    *   *Parameters:*
        - **filename** (`str`): The path to the file whose dependencies are being analyzed.
        - **repo_root** (`str`): The root directory of the repository.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(node: type, alias: type)`
        *   *Description:* This method resolves relative import statements, such as `from .. import name1, name2`, by determining the actual module or symbol names based on the import level and the current file's location within the repository. It leverages nested helper functions to verify the existence of module files or symbols exported via `__init__.py` files. If no valid modules or symbols can be resolved after this process, an `ImportError` is raised.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:** This method calls `get_all_temp_files`, `Path`, `iskeyword`, `module_file_exists`, `init_exports_symbol`, and `print`. It also utilizes `literal_eval`, `parse`, and `walk` from the `ast` module for source code analysis. This method is called by `visit_ImportFrom`.
    *   **`module_file_exists`**
        *   *Signature:* `def module_file_exists(rel_base: type, name: type)`
        *   *Description:* This helper function, nested within `_resolve_module_name`, checks for the existence of a module or package on the filesystem relative to a specified base directory. It verifies if a Python file (`.py`) with the given name exists, or if a directory with that name contains an `__init__.py` file, indicating a valid Python package.
        *   *Parameters:*
            - **rel_base** (`Path`): The relative base directory within the repository to check.
            - **name** (`str`): The name of the module or package to verify.
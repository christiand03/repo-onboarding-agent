```md
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** The project aims to facilitate the onboarding of new repositories by providing automated documentation and analysis. It extracts project information, analyzes code structure, and generates reports using LLMs.
- **Key Features:**
  - Automated project documentation
  - Code structure analysis using AST
  - Relationship analysis (call graph, dependencies)
  - Integration with LLMs for code understanding and report generation
- **Tech Stack:** Python, Langchain, Google Gemini, OpenAI, Ollama, Streamlit, Pydantic, NetworkX

*   **Repository Structure:**
    ```mermaid
    graph LR
        root --> SystemPrompts<br/>.env.example<br/>.gitignore<br/>analysis_output.json<br/>backend<br/>database<br/>frontend<br/>notizen<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>result<br/>schemas<br/>statistics<br/>test.json
        SystemPrompts --> SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt
        backend --> AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py
        database --> db.py
        frontend --> .streamlit<br/>__init__.py<br/>frontend.py<br/>gifs
        .streamlit --> config.toml
        gifs --> 4j.gif
        notizen --> Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md
        grafiken --> "1"<br/>"2"<br/>Flask-Repo<br/>Repo-onboarding
        "1" --> File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot
        "2" --> FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot
        Flask-Repo --> __init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot
        Repo-onboarding --> AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot
        result --> ast_schema_01_12_2025_11-49-24.json<br/>notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md
        schemas --> types.py
        statistics --> savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png
    ```

    ## 2. Installation
    ### Dependencies
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
    ```
    pip install -r requirements.txt
    ### Setup Guide
    Information not found
    ### Quick Startup
    Information not found

    ## 3. Use Cases & Commands
Description: [Could not be determined due to a missing README file and insufficient context.]

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here



## 5. Code Analysis

### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) of Python source code. Its primary purpose is to extract and structure metadata about imports, classes, and functions found within a given source file. It builds a schema containing lists of imports, functions, and classes, providing a programmatic representation of the code's structure.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class depends on `backend.AST_Schema.path_to_module` for resolving module paths.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor with the source code, file path, and project root. It calculates the module path, sets up an empty schema dictionary to store extracted information, and initializes `_current_class` to `None` for tracking the current class context during AST traversal.
    *   *Parameters:*
        - **self** (`ASTVisitor`): The instance of the class.
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the Python file being visited.
        - **project_root** (`str`): The root directory of the project, used to determine the module path.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes `ast.Import` nodes, which represent `import module` statements. It iterates through each alias in the import statement, extracting the module name and appending it to the `self.schema["imports"]` list. After recording the import, it calls `self.generic_visit(node)` to ensure that the AST traversal continues for any child nodes.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* 
        *   **Usage:** Analysis data not available for this component.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to `from module import name` statements. It constructs fully qualified import names by combining the module name (if present) with each alias name, then appends these to `self.schema["imports"]`. This ensures that specific imports from modules are correctly captured. Finally, it invokes `self.generic_visit(node)` to continue the AST traversal.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* 
        *   **Usage:** Analysis data not available for this component.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is responsible for processing `ast.ClassDef` nodes, which represent class definitions. It constructs a dictionary containing detailed information about the class, including its identifier, name, docstring, source code segment, and line numbers. This class information is then added to `self.schema["classes"]`, and the `_current_class` attribute is temporarily set to this class's info to provide context for any nested methods. After visiting child nodes via `self.generic_visit(node)`, `_current_class` is reset to `None`.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* 
        *   **Usage:** Analysis data not available for this component.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, distinguishing between methods defined within a class and top-level functions. If `_current_class` is set, it means the function is a method, and its details (identifier, name, arguments, docstring, line numbers) are appended to the `method_context` of the current class. Otherwise, it's treated as a standalone function, and its details are added to `self.schema["functions"]`. It ensures proper AST traversal by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* 
        *   **Usage:** Analysis data not available for this component.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method handles `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Instead of implementing its own parsing logic, it delegates the processing directly to the `visit_FunctionDef` method. This approach ensures that both synchronous and asynchronous function definitions are handled uniformly, extracting the same structural and metadata information.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* 
        *   **Usage:** Analysis data not available for this component.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process source code, particularly Python files within a Git repository, to build a structured Abstract Syntax Tree (AST) schema. It can analyze individual files to extract functions, classes, and their internal structures using an ASTVisitor. Additionally, it provides functionality to merge external relationship data, such as call graphs, into the generated AST schema, enriching the structural information with dynamic interaction details.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class depends on `backend.AST_Schema.ASTVisitor` for parsing ASTs, `ast` for Python's built-in AST module, and `os` for path manipulation.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments, effectively creating a stateless instance.
    *   *Parameters:*
        - **self** (`ASTAnalyzer`): The instance of the class.
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict) -> dict`
        *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing calls, into a structured full schema. It iterates through files, functions, and classes within the schema, updating their respective context fields with call and called-by information. For classes, it also calculates and stores external dependencies based on method calls.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): The comprehensive schema containing file, function, and class AST nodes.
            - **raw_relationships** (`dict`): A dictionary containing raw 'outgoing' and 'incoming' call relationships.
        *   *Returns:* 
            - **full_schema** (`dict`): The updated 'full_schema' dictionary with integrated relationship data.
        *   **Usage:** Analysis data not available for this component.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository) -> dict`
        *   *Description:* This method processes a list of file objects from a Git repository to construct a full AST schema. It filters for Python files, reads their content, and uses an ASTVisitor to parse the Abstract Syntax Tree, extracting structural information. The method handles potential parsing errors and populates a 'full_schema' dictionary with the AST nodes for each successfully processed file.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though it's not directly used in the provided snippet beyond its type hint.
        *   *Returns:* 
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed repository, structured by file paths.
        *   **Usage:** Analysis data not available for this component.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to a specified project root. If the file is a Python file, it removes the '.py' extension. Subsequently, it replaces path separators with dots to form the module path. Special handling is included for '__init__.py' files, where the '.__init__' suffix is removed to represent the package itself.
*   **Parameters:*
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:*
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:** This function calls no other functions. This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends ast.NodeVisitor to traverse the Abstract Syntax Tree (AST) of a Python file and identify its import dependencies. It is designed to build a dictionary (import_dependencies) mapping the analyzed file to a set of modules it imports. The class handles both absolute and relative import statements, with a dedicated private method _resolve_module_name for robustly resolving relative imports within a given repository context. Its primary purpose is to establish a foundational understanding of file-level import relationships for a larger dependency analysis system.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class depends on `get_all_temp_files` for repository file discovery, and `init_exports_symbol` and `module_file_exists` for resolving module and symbol existence during relative import processing.
*   **Constructor:**
    *   *Description:* The constructor initializes the FileDependencyGraph instance by storing the filename of the file being analyzed and the repo_root directory. These attributes are crucial for resolving relative imports and locating files within the repository.
    *   *Parameters:*
        - **self** (`FileDependencyGraph`): The instance of the class.
        - **filename** (`str`): The name of the file currently being analyzed for dependencies.
        - **repo_root** (`str`): The root directory of the repository, used for resolving file paths.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ImportFrom) -> list[str]`
        *   *Description:* This private method is responsible for resolving relative import statements (e.g., from .. import name). It calculates the correct base directory based on the import level and the current file's location within the repository. It then iterates through the imported names, checking if they correspond to existing module files or symbols exported by __init__.py files. If no matching modules or symbols are found, it raises an ImportError. Nested functions `module_file_exists` and `init_exports_symbol` are defined within this method to assist in verifying file and symbol existence.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`ImportFrom`): The AST ImportFrom node representing the relative import statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names as strings.
        *   **Usage:** Analysis data not available for this component.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None = None)`
        *   *Description:* This method is part of the NodeVisitor pattern and is called for Import and ImportFrom AST nodes. It records the imported module names as dependencies for the current self.filename in the import_dependencies dictionary. If a base_name is provided (typically from visit_ImportFrom), it uses that; otherwise, it uses the alias name from the import node. After processing, it calls self.generic_visit(node) to continue the AST traversal.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`Import | ImportFrom`): The AST node representing an import statement.
            - **base_name** (`str | None`): An optional base name for the module, typically used for from ... import ... statements where the module part is resolved separately.
        *   *Returns:*
        *   **Usage:** Analysis data not available for this component.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
        *   *Description:* This method is invoked by the AST NodeVisitor when an ImportFrom node is encountered. It extracts the module name from the import statement. If it's an absolute import, it takes the last part of the module name and passes it to visit_Import. If it's a relative import (indicated by node.module being None), it attempts to resolve the module name using the _resolve_module_name helper method. Any resolved base names are then passed to visit_Import to record the dependency. Errors during relative import resolution are caught and printed. Finally, it ensures the AST traversal continues with self.generic_visit.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`ImportFrom`): The AST ImportFrom node to be processed.
        *   *Returns:*
        *   **Usage:** Analysis data not available for this component.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and uses a custom `FileDependencyGraph` visitor to traverse the AST and identify import relationships. The visitor populates an internal dictionary of import dependencies. The function then iterates through these identified dependencies, adding nodes for both importing and imported files, and creating directed edges from the importer to the imported files. The resulting graph illustrates which files depend on others based on their import statements.
*   **Parameters:*
    - **filename** (`str`): The path to the file being analyzed for dependencies.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:*
    - **graph** (`networkx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies (from importer to imported).
*   **Usage:** This function calls backend.File_Dependency.FileDependencyGraph. This function is called by no other functions.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository) -> nx.DiGraph`
*   **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses its content to build a file-specific dependency graph using an external helper function. Finally, it aggregates all these individual file graphs into a single global directed graph, which is then returned.
*   **Parameters:*
    - **repository** (`GitRepository`): The Git repository object from which to build the dependency graph.
*   **Returns:*
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependencies between Python files across the entire repository.
*   **Usage:** This function calls backend.File_Dependency.build_file_dependency_graph. This function is not explicitly called by any other functions in the provided context.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str) -> list[Path]`
*   **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and returns a list of `Path` objects. The function first converts the input directory string into an absolute and canonical `Path` object. It then recursively searches for all files ending with ".py" within this root path. Finally, it returns these found file paths as a list, with each path made relative to the initial root directory.
*   **Parameters:*
    - **directory** (`str`): The path to the root directory to search for Python files.
*   **Returns:*
    - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each path represents a Python file found within the specified directory, relative to the root directory.
*   **Usage:** This function calls no other functions. This function is called by no other functions
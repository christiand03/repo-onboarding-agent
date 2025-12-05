# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated code documentation agent. It clones a given Git repository, performs static code analysis by building an Abstract Syntax Tree (AST) and analyzing file dependencies and call graphs. It then leverages multiple Large Language Models (a "Helper" for detailed code analysis and a "Main" LLM for synthesis) to generate comprehensive project documentation. The agent is accessible through a Streamlit-based web frontend.
- **Key Features:**
  - Automated repository cloning and file processing.
  - Static code analysis including AST generation, call graph construction, and dependency mapping.
  - Dual-LLM architecture for detailed code analysis and final report synthesis.
  - Streamlit web interface for user interaction and displaying results.
  - Support for multiple LLM providers (Gemini, OpenAI, Ollama).
- **Tech Stack:** Streamlit, LangChain, NetworkX, GitPython, Pydantic, PyMongo

*   **Repository Structure:**
    ```mermaid
    graph LR
        subgraph root
            direction LR
            root_files["analysis_output.json<br/>.env.example<br/>output.toon<br/>.gitignore<br/>readme.md<br/>requirements.txt<br/>output.json"]
        end

        subgraph SystemPrompts
            direction LR
            SystemPrompts_files["SystemPromptMainLLM.txt<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLMToon.txt"]
        end

        subgraph backend
            direction LR
            backend_files["main.py<br/>__init__.py<br/>AST_Schema.py<br/>basic_info.py<br/>MainLLM.py<br/>relationship_analyzer.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>getRepo.py<br/>callgraph.py"]
        end

        subgraph database
            direction LR
            database_files["db.py"]
        end

        subgraph frontend
            direction LR
            frontend_files["__init__.py<br/>Frontend.py"]
        end

        subgraph frontend/gifs
            direction LR
            frontend_gifs_files["4j.gif"]
        end

        subgraph notizen
            direction LR
            notizen_files["Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>praesentation_notizen.md<br/>technische_notizen.md<br/>paul_notizen.md<br/>notizen.md<br/>Report Agenda.txt"]
        end

        subgraph notizen/grafiken
            direction LR
            notizen_grafiken_files["global_graph.png<br/>repo.dot<br/>File_Dependency_Graph_Repo.dot<br/>global_graph_2.png<br/>global_callgraph.png"]
        end

        subgraph notizen/grafiken/Flask-Repo
            direction LR
            notizen_grafiken_Flask_Repo_files["importerrorapp.dot<br/>hello.dot<br/>wsgi.dot<br/>test_async.dot<br/>__main__.dot<br/>test_factory.dot<br/>conf.dot<br/>test_templating.dot<br/>test_basic.dot<br/>test_views.dot<br/>test_cli.dot<br/>test_helpers.dot<br/>test_json_tag.dot<br/>test_auth.dot<br/>test_user_error_handler.dot<br/>test_blog.dot<br/>blog.dot<br/>test_testing.dot<br/>tasks.dot<br/>scaffold.dot<br/>typing_route.dot<br/>cli.dot<br/>config.dot<br/>test_subclassing.dot<br/>test_signals.dot<br/>conftest.dot<br/>test_regression.dot<br/>test_session_interface.dot<br/>test_request.dot<br/>multiapp.dot<br/>test_appctx.dot<br/>test_json.dot<br/>test_reqctx.dot<br/>test_db.dot<br/>typing_app_decorators.dot<br/>signals.dot<br/>templating.dot<br/>test_instance_config.dot<br/>test_converters.dot<br/>test_config.png<br/>test_config.dot<br/>blueprints.dot<br/>app.dot<br/>__init__.dot<br/>typing.dot<br/>auth.dot<br/>factory.dot<br/>helpers.dot<br/>ctx.dot<br/>wrappers.dot<br/>test_blueprints.dot<br/>test_logging.dot<br/>db.dot<br/>test_js_example.dot<br/>make_celery.dot<br/>typing_error_handler.dot<br/>debughelpers.dot<br/>sessions.dot<br/>logging.dot<br/>globals.dot<br/>tag.dot<br/>provider.dot<br/>views.dot<br/>testing.dot"]
        end

        subgraph notizen/grafiken/Repo-onboarding
            direction LR
            notizen_grafiken_Repo_onboarding_files["tools.dot<br/>main.dot<br/>graph_AST2.png<br/>graph_AST3.png<br/>types.dot<br/>graph_AST.png<br/>AST.dot<br/>agent.dot<br/>Frontend.dot<br/>MainLLM.dot<br/>getRepo.dot<br/>basic_info.dot<br/>HelperLLM.dot<br/>callgraph.dot<br/>HelperLLM.png"]
        end

        subgraph result
            direction LR
            result_files["report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_14_11_2025_15-21-53.md<br/>report_21_11_2025_16-06-12.md<br/>result_2025-11-11_12-45-37.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_14_11_2025_15-26-24.md<br/>result_2025-11-11_12-30-53.md<br/>report_14_11_2025_14-52-36.md<br/>report_21_11_2025_15-43-30.md<br/>result_2025-11-11_12-43-51.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md"]
        end

        subgraph schemas
            direction LR
            schemas_files["types.py"]
        end

        subgraph statistics
            direction LR
            statistics_files["savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png"]
        end

        root --> SystemPrompts
        root --> backend
        root --> database
        root --> frontend
        root --> notizen
        root --> result
        root --> schemas
        root --> statistics
        SystemPrompts --> SystemPrompts_files
        backend --> backend_files
        database --> database_files
        frontend --> frontend_files
        frontend --> frontend/gifs
        frontend/gifs --> frontend_gifs_files
        notizen --> notizen_files
        notizen --> notizen/grafiken
        notizen/grafiken --> notizen_grafiken_files
        notizen/grafiken --> notizen/grafiken/Flask-Repo
        notizen/grafiken/Flask-Repo --> notizen_grafiken_Flask_Repo_files
        notizen/grafiken --> notizen/grafiken/Repo-onboarding
        notizen/grafiken/Repo-onboarding --> notizen_grafiken_Repo_onboarding_files
        result --> result_files
        schemas --> schemas_files
        statistics --> statistics_files
    ```

## 2. Installation
### Dependencies
To install the dependencies, run: `pip install -r requirements.txt`

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

### Setup Guide
1.  Clone the repository to your local machine.
2.  Navigate to the project root directory.
3.  Create a `.env` file by copying the `.env.example` file.
4.  Populate the `.env` file with your required API keys (e.g., for Gemini or OpenAI).
5.  Install all required dependencies by running the command: `pip install -r requirements.txt`.

### Quick Startup
To run the application, execute the following command from the project's root directory:
```bash
streamlit run frontend/Frontend.py
```

## 3. Use Cases & Commands
The primary use case for this application is to automatically generate technical documentation for a public Git repository. The user interacts with a Streamlit web interface where they can:
1.  Provide the URL of the Git repository to be analyzed.
2.  Select the desired "Helper" and "Main" Large Language Models from the available options (e.g., Gemini, GPT, Ollama).
3.  Enter the necessary API keys for the selected models.
4.  Initiate the analysis process.

The application backend then clones the repository, performs static code analysis, and uses the selected LLMs to generate a comprehensive Markdown report, which is displayed in the frontend.

**Primary Command:**
The main command to launch the web interface is:
```bash
streamlit run frontend/Frontend.py
```

## 4. Architecture
The Mermaid syntax to visualize the architecture is not yet available.

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into its corresponding Python module path string. It first attempts to calculate the relative path of the file with respect to the provided project root using `os.path.relpath`. If this fails, it defaults to using only the file's basename. The function then strips the trailing `.py` extension if present. Finally, it replaces OS-specific path separators with dots to form the module structure and handles package initialization files by removing the `.__init__` suffix from the path.
*   **Parameters:**
    - **filepath** (`string`): The absolute or relative file path that needs to be converted into a module path.
    - **project_root** (`string`): The root directory against which the file path is made relative.
*   **Returns:**
    - **module_path** (`string`): The resulting Python module path string (e.g., 'package.module').
*   **Usage:**
    *   **Calls:** This function utilizes operating system path utilities, specifically `os.path.relpath` and `os.path.basename`, and performs string manipulation using `endswith` and `replace` methods.
    *   **Called By:** This function is used by the `__init__` method within the `AST_Schema.py` file.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is a specialized implementation of ast.NodeVisitor designed to traverse a Python Abstract Syntax Tree (AST) and generate a structured schema of the code elements within a file. It initializes context attributes like file path, project root, and module path, and maintains a schema dictionary to collect imports, functions, and classes. The visitor methods selectively extract metadata, source code segments, and context information for each element encountered, ensuring that nested functions are correctly associated with their parent classes. This class serves as the core mechanism for transforming raw Python source code into structured, machine-readable metadata.
*   **Instantiation:** This class is instantiated by the `analyze_repository` function in the file `AST_Schema.py`.
*   **Dependencies:** The class relies on external functions like `path_to_module` (used in initialization) and methods from the standard `ast` module, such as `ast.NodeVisitor`, `ast.get_docstring`, and `ast.get_source_segment`.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with necessary context information, including the raw source code, the file path, and the project root. It calculates the module path using the external function `path_to_module` and sets up the primary data structure (`self.schema`) to store extracted imports, functions, and classes. It also initializes `self._current_class` to track the current class being visited during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the file being analyzed.
        - **project_root** (`str`): The root directory of the entire project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method handles `ast.Import` nodes, which represent standard import statements (e.g., `import os`). It iterates through all imported names (aliases) defined in the node and adds the simple name of the imported module or package to the `imports` list within the main `self.schema` dictionary. Finally, it calls `self.generic_visit(node)` to ensure the AST traversal continues to nested nodes.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing a standard import statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `append` on the internal schema list and `generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` mechanism when an `ast.Import` node is encountered during traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes (e.g., `from module import name`). It iterates through the imported names and constructs a fully qualified import string by combining the module name (`node.module`) with the specific imported name (`alias.name`). This fully qualified string is then appended to the `self.schema["imports"]` list. It ensures traversal continues by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `append` on the internal schema list and `generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` mechanism when an `ast.ImportFrom` node is encountered during traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method processes `ast.ClassDef` nodes, extracting metadata about defined classes. It constructs a unique identifier and creates a detailed dictionary (`class_info`) containing the class name, docstring, source code segment, and line numbers, preparing it for subsequent analysis. This `class_info` is appended to `self.schema["classes"]`. Crucially, it sets `self._current_class` to the newly created class context before calling `self.generic_visit(node)`, allowing nested methods to be correctly associated, and then resets the context afterward.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `append` on the internal schema list, `ast.get_docstring`, `ast.get_source_segment`, and `generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` mechanism when an `ast.ClassDef` node is encountered during traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, distinguishing between methods defined inside a class and standalone functions. If `self._current_class` is set, it extracts method metadata and appends this context information to the `method_context` list of the current class object. If it is a standalone function, it creates a full function analysis dictionary and appends it to `self.schema["functions"]`. This ensures all functions and methods are cataloged correctly based on their scope.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `append` on either the current class's method context list or the main schema's function list, along with `ast.get_docstring`, `ast.get_source_segment`, and `generic_visit`.
            *   **Called By:** This method is called by the `ast.NodeVisitor` mechanism when an `ast.FunctionDef` node is encountered, and it is explicitly called by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method handles `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. It delegates all processing logic directly to `self.visit_FunctionDef(node)`. This ensures that asynchronous functions are treated identically to synchronous functions for the purpose of schema generation and context extraction.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `self.visit_FunctionDef` to process the node.
            *   **Called By:** This method is called by the `ast.NodeVisitor` mechanism when an `ast.AsyncFunctionDef` node is encountered during traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is the primary component responsible for generating a structured, comprehensive schema of a Python repository based on Abstract Syntax Tree (AST) analysis. It iterates through all provided files, parses them, extracts structural data (functions, classes, imports), and builds a file-specific call graph. The class then enriches this schema with the call graph relationships and provides utilities to merge cross-file dependency data, resulting in a complete, machine-readable representation of the repository's structure and relationships.
*   **Instantiation:** This class is instantiated by the main_workflow function located in main.py.
*   **Dependencies:** The class relies on the standard Python ast and os modules, the networkx library for graph operations, and the external function build_callGraph.
*   **Constructor:**
    *   *Description:* The constructor for the ASTAnalyzer is minimal and performs no initialization of instance attributes, serving only to define the class structure.
    *   *Parameters:* *No parameters.*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* This static method updates a file-specific schema dictionary by integrating call graph relationship data. It iterates through all functions and class methods defined in the schema, constructs unique identifiers using the provided filename, and queries the NetworkX call graph to find both the callers (predecessors) and the callees (successors) for each entity. The collected relationship lists are then sorted and stored in the respective 'calls' and 'called_by' context fields within the schema.
        *   *Parameters:*
            - **schema** (`dict`): The file-specific AST schema containing lists of functions and classes to be enriched.
            - **call_graph** (`nx.DiGraph`): The NetworkX directed graph representing function/method call relationships within the file.
            - **filename** (`str`): The path or name of the file being processed, used to create unique identifiers for graph lookup.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls standard Python functions like list and sorted, along with NetworkX graph methods such as predecessors and successors.
            *   **Called By:** This method is not explicitly called by any external functions according to the provided context.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
        *   *Description:* This method integrates external relationship data, such as cross-file dependencies, into the comprehensive repository schema. It first creates a lookup map from the input relationship data, mapping identifiers to their 'called_by' lists. It then traverses the entire 'full_schema', updating the 'called_by' context for functions and methods, and the 'instantiated_by' context for classes, ensuring that cross-file relationships are correctly documented.
        *   *Parameters:*
            - **full_schema** (`dict`): The complete repository schema structure containing data organized by files.
            - **relationship_data** (`list`): A list of external dependency items used to populate the relationship contexts.
        *   *Returns:*
            - **full_schema** (`dict`): The updated repository schema dictionary containing the merged relationship data.
        *   **Usage:**
            *   **Calls:** This method utilizes basic dictionary access methods like get and items.
            *   **Called By:** This method is called by the main_workflow function in main.py.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files)`
        *   *Description:* This method orchestrates the AST analysis process for an entire repository. It initializes the schema structure, determines the project root path, and iterates through the provided list of files. For each Python file, it parses the content into an AST, uses an ASTVisitor to extract structural schema nodes, builds a call graph, and then calls the internal _enrich_schema_with_callgraph method to integrate relationship data. It handles SyntaxErrors during parsing and accumulates the results into a final repository schema.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each containing the file path and content to be analyzed.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the complete AST and relationship schema for the analyzed repository.
        *   **Usage:**
            *   **Calls:** This method calls external components like ASTVisitor and build_callGraph, standard library functions from the os and ast modules (commonpath, dirname, isfile, parse), and the internal method _enrich_schema_with_callgraph.
            *   **Called By:** This method is called by the main_workflow function in main.py.

### File: `backend/File_Dependency.py`
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a NetworkX directed graph (nx.DiGraph) representing the file-level import dependencies found within a single Python file's Abstract Syntax Tree (AST). It initializes a custom visitor, `FileDependencyGraph`, and traverses the provided AST to extract import relationships. The function then iterates through the collected dependencies, adding the source file (caller) and all imported files (callees) as nodes. Finally, it establishes directed edges from the caller to each callee, mapping out which files depend on others, and returns the resulting graph.
*   **Parameters:**
    - **filename** (`str`): The name of the Python file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) object representing the structure of the file.
    - **repo_root** (`str`): The root path of the repository, used for resolving relative file paths during dependency analysis.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph where nodes represent files and edges indicate an import dependency from one file to another.
*   **Usage:**
    *   **Calls:** This function initializes a DiGraph and a FileDependencyGraph visitor, utilizing methods such as visit, items, add_node, add_nodes_from, and add_edge to populate the graph structure.
    *   **Called By:** This function is invoked by build_repository_graph.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function is responsible for building a comprehensive dependency graph for all Python files within a given Git repository. It first retrieves all files and initializes an empty NetworkX Directed Graph (nx.DiGraph). It then iterates through the files, skipping any that are not Python source files. For each Python file, it parses the content into an Abstract Syntax Tree (AST) and delegates the file-level dependency analysis to the `build_file_dependency_graph` function. Finally, it merges the resulting nodes and edges from the file-specific graphs into the main global graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object containing the source code files whose dependencies are to be mapped.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX Directed Graph representing the aggregated file and internal dependencies across the entire repository's Python codebase.
*   **Usage:**
    *   **Calls:** This function relies heavily on the provided repository object to retrieve files and directory information. It uses standard functions like `str`, `os.path.basename`, `removesuffix`, and `endswith` for file path manipulation, `parse` for AST generation, and `build_file_dependency_graph` for file-level analysis. It utilizes NetworkX methods like `DiGraph`, `add_node`, and `add_edge` to construct the final graph structure.
    *   **Called By:** This function is called by the `backend.File_Dependency` module during its initialization phase.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function is designed to recursively locate all Python source files within a specified root directory. It first converts the input directory string into an absolute `pathlib.Path` object using `resolve()`. It then uses recursive globbing (`rglob("*.py")`) to find all files ending in '.py' starting from the root path. For each file found, the function calculates its path relative to the root directory before collecting it into a list, which is then returned.
*   **Parameters:**
    - **directory** (`str`): The string path of the root directory to be searched recursively for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each path is relative to the input directory, representing a Python file found recursively.
*   **Usage:**
    *   **Calls:** This function utilizes methods associated with `pathlib.Path` objects, specifically calling `resolve()` to get the absolute path, `rglob()` for recursive file searching, and `relative_to()` to convert absolute paths to paths relative to the root.
    *   **Called By:** This function is called by `_resolve_module_name` within the `File_Dependency.py` module.

#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G)`
*   **Description:** This function converts a NetworkX directed graph (nx.DiGraph) representing file dependencies into a structured Mermaid flowchart syntax string. It analyzes the file paths stored as nodes in the graph and groups them based on their containing folders using a defaultdict.
It then generates Mermaid code, creating distinct 'subgraph' blocks for each folder to visually organize the files.
Node IDs are sanitized by replacing path separators ('/') with underscores ('_') to ensure valid Mermaid syntax.
Finally, it iterates over the graph edges to define the dependency arrows ('-->') between the sanitized node IDs, returning the complete diagram string.
*   **Parameters:**
    - **G** (`nx.DiGraph`): The NetworkX directed graph where nodes are file paths (e.g., 'folder/file.py') and edges represent dependencies.
*   **Returns:**
    - **mermaid_diagram** (`str`): A string containing the complete Mermaid flowchart definition, including subgraphs for folders, nodes for files, and dependency edges.
*   **Usage:**
    *   **Calls:** This function utilizes standard Python string and list methods such as `append`, `items`, `join`, `replace`, and `split`, and relies on `collections.defaultdict` for grouping nodes by folder.
    *   **Called By:** This function is called by a module-level execution block within `File_Dependency.py`.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is an Abstract Syntax Tree (AST) visitor designed to analyze Python source code and map file-level import dependencies. It inherits from `NodeVisitor` and overrides specific `visit_*` methods to capture import statements. The class maintains a dictionary, `import_dependencies`, mapping the current file to a set of modules it imports. It is specialized in resolving complex relative imports by checking the filesystem structure and package initialization files (`__init__.py`) to accurately determine dependencies.
*   **Instantiation:** This class is instantiated by the function `build_file_dependency_graph` located in `File_Dependency.py`.
*   **Dependencies:** This class does not rely on any external dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the File Dependency Graph instance by storing the path of the file currently being analyzed (`filename`) and the root directory of the repository (`repo_root`). These attributes are essential for resolving relative imports and locating files within the repository structure.
    *   *Parameters:*
        - **filename** (`str`): The name or path of the file currently being processed by the visitor.
        - **repo_root** (`str`): The root directory of the code repository used as the base for resolving relative paths.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This private method is responsible for resolving relative Python imports, such as those using leading dots (e.g., `from .. import name`). It determines the correct base directory by navigating up the file structure based on the import level specified in the AST node. It then iterates through the imported names, checking if they correspond to existing module files or symbols explicitly exported by a package's `__init__.py` file. If no names can be resolved, it raises an `ImportError` detailing the failure.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the relative import statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of successfully resolved module or symbol names.
        *   **Usage:**
            *   **Calls:** This method calls `get_all_temp_files` to find files, uses `Path` and related methods like `resolve` for path manipulation, and utilizes standard Python functions like `len`, `range`, and `sort`, potentially raising an `ImportError`.
            *   **Called By:** This method is not explicitly called by any other function or method listed in the context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method processes standard `import` statements (like `import module`) and serves as a dependency recording helper for `visit_ImportFrom`. It ensures that the current file (`self.filename`) is registered in the `import_dependencies` dictionary. It then adds the imported module name (either derived from `base_name` or the import alias) as a dependency of the current file before continuing the AST traversal via `generic_visit`.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing the import statement.
            - **base_name** (`str | None`): An optional pre-resolved module name, typically provided when called from `visit_ImportFrom`.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the `add` method on a set, uses the `set` constructor, and invokes `generic_visit` for continued AST traversal.
            *   **Called By:** This method is not explicitly called by any other function or method listed in the context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `from ... import ...` statements. If the import is absolute (e.g., `from a.b.c import d`), it extracts the base module name ('c') and delegates dependency recording to `visit_Import`. If the import is relative (e.g., `from . import d`), it attempts to resolve the actual module names using `_resolve_module_name`. If resolution succeeds, it records dependencies for each resolved name via `visit_Import`; otherwise, it prints an error message indicating the failure of relative import resolution.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the `from ... import ...` statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `_resolve_module_name` to handle relative imports, delegates dependency recording to `visit_Import`, uses `split` for module name parsing, prints error messages, and calls `generic_visit`.
            *   **Called By:** This method is not explicitly called by any other function or method listed in the context.

### File: `backend/HelperLLM.py`
#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy orchestrator and testing harness for the LLMHelper class. It defines several mock inputs (FunctionAnalysisInput) and corresponding analysis objects (FunctionAnalysis) for testing purposes, simulating a pipeline run. It initializes the LLMHelper, simulates the documentation generation process by calling generate_for_functions, and then iterates through the results. The primary action is aggregating the successful analyses into a dictionary and printing the final structure using json.dumps.
*   **Parameters:** *No parameters.*
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function calls Pydantic model methods (model_validate, model_dump), logging utilities (info, warning), the LLMHelper constructor, its generate_for_functions method, and json.dumps for serializing the final documentation.
    *   **Called By:** This function is called by the module backend.HelperLLM.

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class is a specialized utility designed to interact with various Large Language Models (LLMs) like Google Gemini, OpenAI's GPT, and Ollama, primarily for generating structured documentation for Python functions and classes. It centralizes API configuration, loads model-specific system prompts, and enforces structured JSON output using Pydantic schemas via LangChain. The class is optimized for high-throughput documentation generation by implementing a batch processing mechanism that automatically configures batch sizes and respects API rate limits using timed delays.
*   **Instantiation:** This class is instantiated by the `main_orchestrator` function in `HelperLLM.py` and the `main_workflow` function in `main.py`.
*   **Dependencies:** The class has no explicitly listed external dependencies in the provided context structure.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by validating the API key, loading the necessary system prompts for function and class analysis from specified file paths, and configuring the underlying LLM client based on the provided model name. It calls an internal method to set the optimal batch size and establishes two structured output chains (`function_llm` and `class_llm`) ready for Pydantic-validated JSON generation.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for accessing the chosen LLM service (e.g., Gemini or OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt template used for function analysis tasks.
        - **class_prompt_path** (`str`): The file path to the system prompt template used for class analysis tasks.
        - **model_name** (`str`): The identifier of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
        - **ollama_base_url** (`str | None`): The base URL for the Ollama service, which is only used if an Ollama model is selected.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private helper method sets the instance attribute `self.batch_size` based on the provided `model_name`. It uses a series of conditional checks to assign specific, optimized batch sizes for known models (e.g., different Gemini versions, Llama3, GPT). This configuration is crucial for managing API usage and respecting rate limits during batch processing. If the model name does not match any predefined setting, it logs a warning and assigns a conservative default batch size of 2.
        *   *Parameters:*
            - **model_name** (`str`): The identifier string of the LLM model being initialized.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the `warning` function from the logging module to report unknown models.
            *   **Called By:** This function is called internally by the `__init__` method during class initialization.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method orchestrates the generation and validation of documentation for a list of functions in batches. It converts the input Pydantic models into JSON payloads and constructs LangChain conversation messages using the function system prompt. It then iterates through the inputs, sending batches to the structured LLM chain (`self.function_llm`) for analysis. To prevent rate limiting, it pauses execution for a defined waiting time between batches, and handles exceptions by inserting `None` placeholders for failed analyses to maintain result order.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing the necessary context and source code for the LLM to analyze functions.
        *   *Returns:*
            - **results** (`List[Optional[FunctionAnalysis]]`): A list of structured function analysis results, where each element is either a validated FunctionAnalysis object or None if the generation failed for that item.
        *   **Usage:**
            *   **Calls:** This method utilizes LangChain components (`HumanMessage`, `SystemMessage`, `batch`), JSON serialization (`dumps`), Pydantic utilities (`model_dump`), logging functions (`error`, `info`), list manipulation (`extend`, `len`, `min`, `range`), and time control (`sleep`).
            *   **Called By:** This function is called by the `main_workflow` function in `main.py`.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method executes the batch processing and documentation generation specifically for classes, following a structure identical to `generate_for_functions`. It takes a list of `ClassAnalysisInput` objects, serializes them to JSON, and prepares them as conversation messages using the class system prompt. The inputs are processed in batches using `self.class_llm`, which is configured for structured output. It includes rate-limiting logic by pausing between batches and ensures result integrity by appending `None` for any failed batch calls.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing the necessary context and source code for the LLM to analyze classes.
        *   *Returns:*
            - **results** (`List[Optional[ClassAnalysis]]`): A list of structured class analysis results, where each element is either a validated ClassAnalysis object or None if the generation failed for that item.
        *   **Usage:**
            *   **Calls:** This method utilizes LangChain components (`HumanMessage`, `SystemMessage`, `batch`), JSON serialization (`dumps`), Pydantic utilities (`model_dump`), logging functions (`error`, `info`), list manipulation (`extend`, `len`, `min`, `range`), and time control (`sleep`).
            *   **Called By:** This function is called by the `main_workflow` function in `main.py`.

### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the primary interface for interacting with various Large Language Models (LLMs), abstracting away the specifics of the underlying provider (Gemini/Google or Ollama). It handles initialization by loading a mandatory system prompt from a file and configuring the appropriate LangChain client based on the desired model name and API key. Its core functionality includes two modes of interaction: synchronous, single-response generation via call_llm, and asynchronous, chunk-by-chunk response generation via stream_llm.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py.
*   **Dependencies:** The class relies on external libraries for LLM interaction, specifically ChatGoogleGenerativeAI and ChatOllama, along with LangChain's HumanMessage and SystemMessage components.
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by setting up the necessary components for interacting with a Language Model. It first validates the api_key and loads the system prompt from the specified file path, raising an error if the file is missing. Based on the model_name prefix (Gemini, GPT, or other), it instantiates either a ChatGoogleGenerativeAI or ChatOllama object, storing the resulting LLM client in self.llm.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for accessing the LLM service (e.g., Gemini). It must be provided or a ValueError is raised.
        - **prompt_file_path** (`str`): The file path to the text file containing the system prompt that will guide the LLM's behavior.
        - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This determines which underlying LLM client (Google or Ollama) is instantiated.
        - **ollama_base_url** (`str`): Optional base URL for the Ollama service, used only if a non-Gemini/GPT model is selected. Defaults to None.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method executes a synchronous, single-turn call to the configured LLM. It constructs the message payload using the pre-loaded self.system_prompt and the provided user_input, wrapping them in SystemMessage and HumanMessage objects, respectively. It then uses the self.llm.invoke method to get a response. If successful, it returns the content of the LLM's response; otherwise, it logs the error and returns None.
        *   *Parameters:*
            - **user_input** (`str`): The message or prompt provided by the user or another component to be sent to the LLM.
        *   *Returns:*
            - **response_content** (`str | None`): The textual content of the LLM's response if the call is successful, or None if an exception occurs during the invocation.
        *   **Usage:**
            *   **Calls:** This method calls the HumanMessage and SystemMessage constructors, the logging functions (error and info), and the LLM client's invoke method.
            *   **Called By:** This method is called by the main_workflow function in main.py.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method initiates a streaming interaction with the configured LLM, allowing the response to be processed chunk by chunk. Similar to call_llm, it prepares the message list using the system prompt and user input. It then calls self.llm.stream which returns an iterator, yielding the content of each chunk received. If an error occurs during the streaming process, it logs the error and yields the error message as the final output.
        *   *Parameters:*
            - **user_input** (`str`): The message or prompt provided by the user to be processed by the streaming LLM.
        *   *Returns:*
            - **stream_chunk** (`Generator[str, None, None]`): A generator that yields chunks of the LLM's response content as they become available, or an error message string if the stream fails.
        *   **Usage:**
            *   **Calls:** This method calls the HumanMessage and SystemMessage constructors, the logging functions (error and info), and the LLM client's stream method.
            *   **Called By:** This method is not explicitly called by any identified function in the provided context.

### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is responsible for systematically extracting and structuring fundamental project metadata from common repository files, such as README, pyproject.toml, and requirements.txt. It employs a priority-based parsing strategy, where structured files like TOML take precedence over descriptive files like Markdown. The class uses several helper methods for file location and content extraction, ultimately compiling all gathered information into a standardized dictionary structure for project overview and installation details.
*   **Instantiation:** This class is instantiated by the `main_workflow` function in the `main.py` file.
*   **Dependencies:** The class depends on the standard library modules `re` and `os`, and optionally relies on the external `tomllib` module for parsing TOML files.
*   **Constructor:**
    *   *Description:* The constructor initializes the instance by defining a constant placeholder string, `INFO_NICHT_GEFUNDEN`, used when information cannot be found. It sets up the core instance attribute, `self.info`, as a nested dictionary structure containing keys for project overview (title, description, status, features, tech stack) and installation details (dependencies, setup guide, quick start), with all values initially set to the placeholder.
    *   *Parameters:* *No parameters.*
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches a provided list of file objects for a file whose path matches any of the specified string patterns. The search is performed case-insensitively to ensure flexibility in file naming conventions. It iterates through all files and patterns, returning the first file object that satisfies the path matching criteria, or returning None if no suitable file is located.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of file name patterns (e.g., 'readme.md', 'pyproject.toml') to search for.
            - **dateien** (`List[Any]`): A list of file objects, expected to have a 'path' attribute.
        *   *Returns:*
            - **** (`Optional[Any]`): The matching file object whose path ends with one of the patterns, or None if no match is found.
        *   **Usage:**
            *   **Calls:** This method calls string manipulation methods like `endswith` and `lower` to perform case-insensitive path matching.
            *   **Called By:** This function is called by `extrahiere_info`.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private method extracts the text content located under a specific Markdown level 2 heading (##). It accepts a list of alternative keywords for the section title and compiles a regular expression to locate the heading case-insensitively. The method captures all content following the matching heading up until the next level 2 heading or the end of the document, returning the extracted text.
        *   *Parameters:*
            - **inhalt** (`str`): The entire Markdown text content, typically from a README file.
            - **keywords** (`List[str]`): A list of alternative keywords that define the section title (e.g., 'Installation', 'Features').
        *   *Returns:*
            - **** (`Optional[str]`): The extracted text section, stripped of leading/trailing whitespace, or None if the section heading is not found.
        *   **Usage:**
            *   **Calls:** This function utilizes the `re` module for compiling and searching regular expressions, and uses string methods like `join`, `escape`, and `strip`.
            *   **Called By:** This function is called by `_parse_readme`.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This method processes the content of a README file to extract descriptive project information. It uses regular expressions to find the project title (level 1 heading) and a fallback description (text immediately following the title). For structured information like features, tech stack, status, and installation guides, it delegates the extraction to `_extrahiere_sektion_aus_markdown`, updating the `self.info` dictionary only if the fields are still set to the default placeholder value.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the README file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `_extrahiere_sektion_aus_markdown` for section parsing and uses `re.search` along with string methods like `group`, `split`, and `strip` for title and description extraction.
            *   **Called By:** This function is called by `extrahiere_info`.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This method parses the content of a `pyproject.toml` file, treating it as the highest priority source for project metadata. It attempts to load the TOML content using `tomllib` and extracts the project `name`, `description`, and `dependencies` from the `[project]` table. If successful, it updates `self.info` with these values, overriding any existing placeholder data. It includes basic error handling for missing `tomllib` or decoding errors.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the pyproject.toml file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method relies on `tomllib.loads` for parsing and uses dictionary methods like `get`. It also uses the built-in `print` function for warnings.
            *   **Called By:** This function is called by `extrahiere_info`.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This method parses the content of a `requirements.txt` file to extract a list of dependencies. It serves as a fallback mechanism, only populating the `dependencies` field in `self.info` if it has not already been set by a higher-priority source like `pyproject.toml`. It processes the file line by line, filtering out comments and empty lines to produce a clean list of dependencies.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the requirements.txt file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method uses string methods such as `splitlines`, `strip`, and `startswith` to process the file content.
            *   **Called By:** This function is called by `extrahiere_info`.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This is the main public method that orchestrates the entire information extraction process. It first locates relevant project files (README, TOML, requirements) using `_finde_datei`. It then calls the respective parsing methods in a strict priority order (TOML > requirements > README). Finally, it formats the dependencies list for display and overwrites the project title using the repository URL to ensure a consistent, derived project name before returning the complete, structured information dictionary.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file objects (e.g., RepoFile) from the repository.
            - **repo_url** (`str`): The URL of the repository, used to derive the final project title.
        *   *Returns:*
            - **** (`Dict[str, Any]`): The fully populated dictionary containing all extracted project overview and installation information.
        *   **Usage:**
            *   **Calls:** This function orchestrates the parsing process by calling `_finde_datei`, `_parse_toml`, `_parse_requirements`, and `_parse_readme`. It also uses `os.path.basename`, `isinstance`, `join`, and `removesuffix` for final data formatting.
            *   **Called By:** This function is called by `main_workflow`.

### File: `backend/callgraph.py`
#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree, filename)`
*   **Description:** This function constructs a directed call graph (nx.DiGraph) from a given Python Abstract Syntax Tree (AST). It initializes a specialized `CallGraph` visitor object and traverses the input AST using the visitor's `visit` method to identify function definitions and calls. After the traversal, it iterates over all collected caller-callee relationships stored in the visitor's `edges` dictionary. It then explicitly adds these relationships as directed edges to the internal graph object before returning the complete networkx directed graph.
*   **Parameters:**
    - **tree** (`ast.AST`): The Abstract Syntax Tree (AST) of the Python file to be analyzed.
    - **filename** (`str`): The name of the analyzed file, used for context within the graph nodes (e.g., 'main.py').
*   **Returns:**
    - **graph** (`nx.DiGraph`): The complete directed call graph, where nodes represent functions or scopes and edges represent function calls.
*   **Usage:**
    *   **Calls:** This function initializes a `CallGraph` visitor, invokes its `visit` method to traverse the AST, accesses the visitor's `edges` dictionary using `items()`, and uses `add_edge` to populate the resulting graph.
    *   **Called By:** This function is utilized by `analyze_repository` in `AST_Schema.py` and by `build_global_callgraph` in `callgraph.py`.

#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph)`
*   **Description:** The function `graph_to_adj_list` converts a `networkx.DiGraph` object, typically representing a call graph, into a standard Python dictionary format suitable for JSON serialization. This dictionary acts as an adjacency list. It iterates through all nodes in the graph in a sorted order to ensure consistent output. For each node, it retrieves and sorts its successors (the functions it calls). The resulting adjacency list maps a calling node (caller) to a list of its called nodes (callees), only including nodes that have at least one successor.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The call graph (networkx.DiGraph) to be converted into an adjacency list.
*   **Returns:**
    - **adj_list** (`Dict[str, list[str]]`): An adjacency list where the key is a calling node (caller) and the value is a list of called nodes (callees).
*   **Usage:**
    *   **Calls:** This function utilizes graph methods such as `nodes()` and `successors()` on the input graph object, and uses the built-in functions `list()` and `sorted()` to ensure consistent ordering of nodes and successors.
    *   **Called By:** This function is not explicitly called by any other function listed in the provided context.

#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(repo)`
*   **Description:** This function constructs a comprehensive, repository-wide call graph by analyzing all Python files within a given Git repository. It first retrieves all files from the repository object. It then iterates through each file, skipping non-Python files, and uses the 'ast' module to parse the file content into an Abstract Syntax Tree (AST). For each AST, it generates a file-specific call graph using 'build_callGraph'. Finally, it aggregates the nodes and edges from these individual graphs into a single NetworkX directed graph (nx.DiGraph), which is returned as the global call graph.
*   **Parameters:**
    - **repo** (`GitRepository`): The repository object providing access to the source files for analysis.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated function call relationships across all Python files in the repository.
*   **Usage:**
    *   **Calls:** This function utilizes 'repository.get_all_files' to retrieve file data, 'os.path.basename' and string methods like 'removesuffix' for file path manipulation, 'ast.parse' for AST generation, and 'build_callGraph' for file-level analysis. It uses NetworkX methods like 'DiGraph', 'add_node', and 'add_edge' to construct the final graph structure.
    *   **Called By:** This function is called by the 'backend.callgraph' module itself (likely at the module level initialization or execution point).

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function prepares a NetworkX directed graph for serialization into the DOT format, ensuring that node identifiers are safe and simple for visualization tools. It operates by creating a copy of the input graph and generating a mapping from the original, potentially complex node names to simple, indexed string identifiers (e.g., "n0", "n1"). The copied graph is then relabeled using these safe identifiers. Crucially, the original node names are preserved by setting them as the `label` attribute for the newly relabeled nodes. Finally, the modified graph is written to the specified output path using the NetworkX DOT writer.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph object to be processed and saved.
    - **out_path** (`str`): The file path where the resulting DOT file will be written.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function utilizes graph methods like `copy`, `nodes`, and `items`, and calls built-in functions such as `list` and `enumerate`, alongside NetworkX functions `relabel_nodes` and `write_dot` for graph manipulation and serialization.
    *   **Called By:** This function is called by the `backend.callgraph` module.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an Abstract Syntax Tree (AST) visitor specialized in constructing a directed call graph for a single Python file. It traverses the AST to identify function and class definitions, maintaining contextual state (current file, class, and function) to generate fully qualified identifiers for all nodes. The core logic resides in the `visit_Call` method, which resolves raw call targets and records caller-callee relationships in the internal `self.edges` structure. It also includes specific visitor methods to handle class definitions, synchronous and asynchronous function definitions, and special handling for `if __name__ == "__main__":` blocks to accurately map the execution flow.
*   **Instantiation:** This class is instantiated by the `build_callGraph` function located in the `callgraph.py` file.
*   **Dependencies:** This class relies on the standard Python `ast` module for AST traversal and the `networkx` library for graph construction.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph visitor by storing the file name being analyzed and setting up contextual state variables (`current_function`, `current_class`) to `None`. It also initializes a NetworkX directed graph (`self.graph`) and several internal data structures (`import_mapping`, `function_set`, `edges`) used to collect and store the call graph data during AST traversal.
    *   *Parameters:*
        - **filename** (`str`): The name of the file currently being analyzed, which is used as a prefix for creating fully qualified function names.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively traverses an AST node representing a function call to extract the raw names of the callable entities. It specifically handles `ast.Call` nodes by recursively calling itself on the function part of the call. When it encounters an `ast.Name` or `ast.Attribute` node, it extracts the identifier (`id` or `attr`) and returns it. This allows the extraction of simple function names or method names from complex call expressions.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node being inspected, typically starting with an ast.Call node.
        *   *Returns:*
            - **all_calls** (`list[str]`): A list containing the raw string identifiers (names or attributes) extracted from the call expression.
        *   **Usage:**
            *   **Calls:** This function calls itself recursively, uses list manipulation methods like `append`, and performs type checking using `isinstance` on AST nodes.
            *   **Called By:** This method is called by `visit_Call` to determine the raw names of the functions being invoked.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private method takes a list of raw callee names and converts them into fully qualified names based on the current context of the visitor. It prepends the `self.filename` to the raw name. If the visitor is currently inside a class (i.e., `self.current_class` is set), the class name is also included in the fully qualified identifier, ensuring unique identification across the project.
        *   *Parameters:*
            - **callee_nodes** (`list[str]`): A list of raw function or method names extracted from the AST.
        *   *Returns:*
            - **resolved_callees** (`list[str]`): A list of fully qualified function names (e.g., filename::ClassName::methodName).
        *   **Usage:**
            *   **Calls:** This function only uses list `append` to construct the list of resolved callee names.
            *   **Called By:** This method is called by `visit_Call` after raw callee names have been extracted.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This private utility function constructs a standardized, fully qualified name for a function or method. It always includes the `self.filename` as the root prefix. If an optional `class_name` is provided, it is inserted between the filename and the function's base name, using double colons (::) as separators to create a unique identifier.
        *   *Parameters:*
            - **basename** (`str`): The simple name of the function or method.
            - **class_name** (`str | None`): The name of the class if the function is a method, or None otherwise.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name string (e.g., file::class::function or file::function).
        *   **Usage:**
            *   **Calls:** This function does not call any other methods or external functions.
            *   **Called By:** This method is called by `visit_FunctionDef` to generate the unique identifier for a function node.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private method determines the identifier of the current execution scope, which serves as the caller node in the call graph. If the visitor is currently inside a function (`self.current_function` is set), that function's fully qualified name is returned. Otherwise, it returns a placeholder string, either based on the filename (`<filename>`) or a generic global scope identifier (`<global-scope>`), depending on whether a filename was provided.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the visitor.
        *   *Returns:*
            - **caller** (`str`): The fully qualified name of the current calling context.
        *   **Usage:**
            *   **Calls:** This function does not call any other methods or external functions.
            *   **Called By:** This method is called by `visit_Call` to identify the source node of a call edge.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This visitor method handles class definitions by updating the visitor's state to reflect the current class scope. It saves the previous class context, sets `self.current_class` to the new class name, and then recursively visits all function definitions within the class body. This ensures that methods defined inside the class are correctly qualified with the class name. After visiting the body, it restores the previous class context.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
            - **** (`None`): This method is a visitor method and does not return a value.
        *   **Usage:**
            *   **Calls:** This method recursively calls the main visitor method `self.visit` for each function within the class body.
            *   **Called By:** This method is implicitly called by the AST traversal mechanism when a class definition is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes standard function definitions by setting the current function context, adding the function as a node to the call graph, and traversing its body. It uses `_make_full_name` to create a unique identifier, incorporating the class name if the function is a method. After adding the node to `self.graph` and the function name to `self.function_set`, it uses `generic_visit` to recursively process the function's contents, ensuring any nested calls are correctly attributed to this function. Finally, it resets `self.current_function` to `None` upon exiting the definition.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
            - **** (`None`): This method is a visitor method and does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `_make_full_name` to construct the function identifier, uses `add_node` to register the function in the graph, and calls `generic_visit` for recursive traversal of the function body. It also uses set `add` to track defined functions.
            *   **Called By:** This method is implicitly called by the AST traversal mechanism and explicitly called by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This visitor method handles asynchronous function definitions (`async def`). For the purpose of call graph construction, it treats asynchronous functions identically to synchronous functions. It achieves this by simply delegating the entire processing logic to the `visit_FunctionDef` method.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing the asynchronous function definition.
        *   *Returns:*
            - **** (`None`): This method is a visitor method and does not return a value.
        *   **Usage:**
            *   **Calls:** This method explicitly calls `visit_FunctionDef` to handle the node processing.
            *   **Called By:** This method is implicitly called by the AST traversal mechanism when an asynchronous function definition is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This is the primary method for recording function calls. It first identifies the current `caller` using `_current_caller`. It then extracts raw callee names using `_recursive_call` and resolves them to fully qualified names using `_resolve_all_callee_names`. If successful, it ensures the caller exists in the `self.edges` dictionary and adds all resolved callee names to the set of functions called by the current caller, thus establishing the call graph edge. It includes robust error handling to prevent crashes during complex call processing, printing a warning instead.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing the function or method call.
        *   *Returns:*
            - **** (`None`): This method is a visitor method and does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `_current_caller`, `_recursive_call`, and `_resolve_all_callee_names` for name resolution, uses `print` for error logging, and calls `generic_visit` to continue traversal. It also uses set `add` operations to record edges.
            *   **Called By:** This method is implicitly called by the AST traversal mechanism when a function call is encountered.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method checks for the specific conditional pattern `if __name__ == "__main__":`. If this entry point is detected, it temporarily overrides `self.current_function` to the special identifier `<main_block>`. This ensures that any global function calls found within this block are correctly attributed to a dedicated main execution node in the call graph. If the condition is not the main block check, it proceeds with a standard generic visit, allowing normal traversal of the conditional statement.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing the conditional statement.
        *   *Returns:*
            - **** (`None`): This method is a visitor method and does not return a value.
        *   **Usage:**
            *   **Calls:** This method uses `isinstance` for type checking on AST nodes and calls `generic_visit` to traverse the body of the conditional statement.
            *   **Called By:** This method is implicitly called by the AST traversal mechanism when an `if` statement is encountered.

### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file found within a specific Git commit tree. It is designed to handle file data efficiently using a lazy loading pattern, ensuring that the file's content, size, and underlying Git Blob object are only fetched from the repository when they are explicitly accessed via properties. This class provides essential file metadata, serialization capabilities via `to_dict`, and methods for content analysis.
*   **Instantiation:** This class is instantiated by the function 'get_all_files' located in 'getRepo.py'.
*   **Dependencies:** The class relies on external dependencies, specifically the 'os' module for path manipulation and implicitly on the 'git' library for handling Tree and Blob objects.
*   **Constructor:**
    *   *Description:* The constructor initializes the RepoFile object by storing the file path and the associated Git commit tree object. It also sets up internal attributes (`_blob`, `_content`, `_size`) to `None` to enable the lazy loading mechanism for file data.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property implements the lazy loading mechanism for the Git Blob object corresponding to the file. If the blob has not yet been loaded, it attempts to retrieve it from the stored commit tree using the file path. If the file path does not exist in the tree, it raises a FileNotFoundError.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **blob** (`git.Blob`): The Git Blob object representing the file data.
        *   **Usage:**
            *   **Calls:** This method calls FileNotFoundError if the file path is not found in the commit tree.
            *   **Called By:** No specific callers were identified in the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy access to the decoded textual content of the file. If the content has not been loaded, it first accesses the `blob` property, reads the data stream from the blob, and decodes it using UTF-8, ignoring any decoding errors.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **content** (`str`): The decoded content of the file.
        *   **Usage:**
            *   **Calls:** This method calls the decode and read methods on the blob's data stream.
            *   **Called By:** No specific callers were identified in the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property implements lazy loading for the size of the file in bytes. If the size has not been calculated, it accesses the `blob` property (ensuring the blob is loaded) and retrieves the size attribute from the Git Blob object.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   **Calls:** No external calls are listed.
            *   **Called By:** No specific callers were identified in the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method performs a simple analysis by counting the total number of words in the file content. It relies on accessing the `content` property, which triggers lazy loading of the file content if necessary, and then splits the string by whitespace to count the resulting tokens.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **word_count** (`int`): The total number of words found in the file content.
        *   **Usage:**
            *   **Calls:** This method calls the built-in len function and the string split method.
            *   **Called By:** No specific callers were identified in the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This magic method provides a developer-friendly string representation of the RepoFile object. The representation is concise and includes the class name and the file path, which is useful for debugging and logging purposes.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **representation** (`str`): A string representation of the object, including its path.
        *   **Usage:**
            *   **Calls:** No external calls are listed.
            *   **Called By:** No specific callers were identified in the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method serializes the file metadata into a dictionary format. It includes the file path, base name, size (using the lazy-loaded property), and a fixed type identifier. It conditionally includes the file content based on the `include_content` flag.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the lazy-loaded file content is included in the dictionary.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing file metadata and optionally its content.
        *   **Usage:**
            *   **Calls:** This method calls os.path.basename to extract the file name.
            *   **Called By:** No specific callers were identified in the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class is responsible for managing the lifecycle of a remote Git repository. Upon instantiation, it clones the repository into a temporary local directory using GitPython. It provides functionality to list all files and structure them into a hierarchical file tree representation. The class implements the context management protocol (`__enter__` and `__exit__`) to ensure that the temporary directory is handled and cleaned up when the object is finished, preventing resource leaks.
*   **Instantiation:** The class is instantiated in `main.py` within the `main_workflow` function.
*   **Dependencies:** The class relies on external modules and functions such as `tempfile.mkdtemp`, `logging`, `git.Repo`, and `git.GitCommandError`.
*   **Constructor:**
    *   *Description:* The constructor initializes the repository by creating a temporary directory and cloning the Git repository specified by `repo_url` into it. It stores the GitPython `Repo` object, the latest commit, and the commit tree for subsequent file operations. It handles cloning errors by cleaning up the temporary directory using `self.close()` and raising a `RuntimeError`.
    *   *Parameters:*
        - **repo_url** (`string`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a list of all file paths present in the repository using GitPython's `ls_files` command. It processes these paths and converts each valid path into a `RepoFile` object, associating it with the stored `commit_tree`. The resulting list of `RepoFile` instances is stored internally in `self.files` and returned to the caller.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list containing instances of `RepoFile`, representing all files in the repository.
        *   **Usage:**
            *   **Calls:** This method calls the `RepoFile` constructor, the Git command `ls_files`, and the string `split` method.
            *   **Called By:** This method is not explicitly called by other methods listed in the input context.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is responsible for cleaning up the resources used by the repository instance. It checks if `self.temp_dir` is set, prints a message indicating the directory deletion, and then sets `self.temp_dir` to `None`. Note that the actual directory deletion using `shutil.rmtree` is commented out in the provided source code.
        *   *Parameters:* *No parameters.*
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the built-in `print` function.
            *   **Called By:** This method is not explicitly called by other methods listed in the input context.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This method implements the entry point for the context management protocol (used with Python's `with` statement). It simply returns the instance of the `GitRepository` itself, allowing it to be bound to a variable in the `with` block.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **self** (`GitRepository`): Returns the instance of the repository object itself.
        *   **Usage:**
            *   **Calls:** This method makes no external calls.
            *   **Called By:** This method is not explicitly called by other methods listed in the input context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This method implements the exit point for the context management protocol. Regardless of whether an exception occurred within the `with` block, it ensures that the cleanup method `self.close()` is executed to handle temporary directory cleanup.
        *   *Parameters:*
            - **exc_type** (`Type | None`): The type of exception raised, or None if no exception occurred.
            - **exc_val** (`BaseException | None`): The exception value, or None.
            - **exc_tb** (`TracebackType | None`): The traceback object, or None.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls the internal `self.close()` method.
            *   **Called By:** This method is not explicitly called by other methods listed in the input context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method constructs a hierarchical dictionary representation of the repository's file structure, treating it as a file tree. It first ensures all files are loaded via `self.get_all_files()`. It then iterates through the files, splitting their paths to traverse and build the nested dictionary structure, creating directory nodes as necessary, and finally appending the file dictionary representation to the correct location in the tree.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the file content is included in the dictionary representation of the files. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A nested dictionary representing the file structure of the repository, starting from a 'root' directory.
        *   **Usage:**
            *   **Calls:** This method calls internal methods like `get_all_files` and `to_dict`, list `append`, string `split`, and the built-in `next` function.
            *   **Called By:** This method is not explicitly called by other methods listed in the input context.

### File: `backend/main.py`
#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart comparing the token counts of two formats, labeled 'JSON' and 'TOON'. It takes the token counts and a calculated savings percentage as input. The chart is configured using `matplotlib.pyplot`, including a title that displays the savings percentage, appropriate axis labels, and a grid. It also annotates the bars by displaying the exact integer token count above each bar. Finally, the generated visualization is saved to the specified output path.
*   **Parameters:**
    - **json_tokens** (`float | int`): The number of tokens counted for the JSON format.
    - **toon_tokens** (`float | int`): The number of tokens counted for the TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings achieved by the TOON format compared to JSON.
    - **output_path** (`str`): The file path where the generated chart image will be saved.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function utilizes `matplotlib.pyplot` methods such as `figure`, `bar`, `title`, `ylabel`, `grid`, `text`, and `savefig` to generate and save the chart, along with bar object methods like `get_height`, `get_width`, and `get_x`. It also uses the built-in `int` function for formatting.
    *   **Called By:** This function is invoked by the `main_workflow` function.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the effective processing time of an operation by subtracting estimated rate-limit sleep times from the total elapsed duration. It first computes the raw duration by finding the difference between the provided start and end times. If the `model_name` does not start with "gemini-", the raw duration is returned immediately. Otherwise, it calculates the number of batches based on `total_items` and `batch_size`. It then estimates the total sleep time by assuming a 61-second delay between each batch (except the first) and subtracts this from the total duration, ensuring the final result is non-negative.
*   **Parameters:**
    - **start_time** (`float`): The timestamp or numerical representation of the operation's start time.
    - **end_time** (`float`): The timestamp or numerical representation of the operation's end time.
    - **total_items** (`int`): The total number of items processed during the duration.
    - **batch_size** (`int`): The maximum number of items processed per batch, used to calculate the number of required sleep intervals.
    - **model_name** (`str`): The name of the model used; if it starts with 'gemini-', sleep time deduction logic is applied.
*   **Returns:**
    - **net_time** (`float`): The calculated duration of the operation in seconds, adjusted for estimated rate-limit sleep time, or the total duration if rate-limit adjustment is not applicable.
*   **Usage:**
    *   **Calls:** This function utilizes the `ceil` function from the math module, the built-in `max` function, and the string method `startswith`.
    *   **Called By:** This function is called by `main_workflow`.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** This function serves as the central orchestration engine for analyzing a code repository. It handles input validation, API key configuration, and model selection for two distinct LLMs (Helper and Main). The workflow involves several steps: extracting the repository URL, cloning the repository, performing static analysis (extracting basic info, generating file tree, relationship analysis, and AST creation), and enriching the AST schema with relationship data. It then utilizes the Helper LLM to analyze individual functions and classes, aggregates these results, and finally passes the comprehensive data to the Main LLM to generate the final project report, saving the output and execution metrics.
*   **Parameters:**
    - **input** (`str`): The raw user input string, which is expected to contain the repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing necessary API keys for different services (e.g., 'gemini', 'gpt') and potentially the 'ollama' base URL.
    - **model_names** (`dict`): A dictionary specifying the model names to be used for the 'helper' LLM and the 'main' LLM.
    - **status_callback** (`callable | None`): An optional function used to relay status updates and progress messages back to the caller, typically a frontend interface. Defaults to None.
*   **Returns:**
    - **analysis_output** (`dict`): A dictionary containing the final generated report under the 'report' key and execution time metrics under the 'metrics' key.
*   **Usage:**
    *   **Calls:** This function calls various utility functions for logging, path manipulation, time tracking, and regular expression matching. Crucially, it orchestrates the analysis by calling constructors and methods from GitRepository, ProjektInfoExtractor, ProjectAnalyzer, and ASTAnalyzer, and manages the LLM workflow by initializing LLMHelper and MainLLM and invoking their generation methods (generate_for_functions, generate_for_classes, call_llm). It also uses json.dumps, encode, and estimate_savings for data formatting and token evaluation, and creates a chart via create_savings_chart.
    *   **Called By:** This function is primarily utilized by the `frontend.Frontend` component and the main execution module `backend.main`.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function serves as a centralized mechanism for reporting status updates within the application. It takes a status message as input and performs two actions: first, it checks for the existence of a global or locally scoped callable named `status_callback`. If `status_callback` is defined, the message is passed to it, typically for updating a user interface or external system. Second, the function ensures that the status message is consistently recorded in the application logs using `logging.info`.
*   **Parameters:**
    - **msg** (`str`): The status message string to be reported to the callback and recorded in the application logs.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function conditionally calls the external `status_callback` function (if it is defined) and utilizes the `logging.info` method to record the status message.
    *   **Called By:** This function is extensively used by the `main_workflow` function in `main.py` to report progress and status updates throughout the main execution flow.

### File: `backend/relationship_analyzer.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a file system path into a standard Python module path string, relative to a specified project root directory. It first attempts to calculate the relative path using os.path.relpath, falling back to the base filename if a ValueError occurs during path calculation. It then strips the '.py' extension if present and replaces system path separators (os.path.sep) with dots to form the module structure. Finally, it handles package initialization files by removing the '.__init__' suffix if the path ends with it, ensuring the result represents the package name itself.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file that needs conversion into a module path.
    - **project_root** (`str`): The root directory of the project used as the base for calculating the relative module path.
*   **Returns:**
    - **module_path** (`str`): The resulting Python module path string (e.g., 'package.module').
*   **Usage:**
    *   **Calls:** This function utilizes path manipulation functions such as relpath and basename from the os.path module, along with string methods like endswith and replace.
    *   **Called By:** This function is called by the methods _collect_definitions and __init__ within the relationship_analyzer.py file.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform static analysis on a Python project to map out the relationships between defined entities (classes, functions, methods). It executes a two-pass analysis: first collecting all definitions and their locations, and second resolving function/method calls across the entire codebase using AST traversal. The class manages internal state, including the definitions dictionary, the raw call graph, and temporary AST representations. Its primary function is to expose the `analyze` method, which executes the full workflow and returns a structured, formatted report detailing who calls whom within the project.
*   **Instantiation:** The class is instantiated by the `main_workflow` function located in `main.py`.
*   **Dependencies:** The class relies on standard Python libraries like `os`, `ast`, and `logging`, as well as the `collections.defaultdict`. It also depends on external components like `path_to_module` and `CallResolverVisitor` to successfully perform its analysis tasks.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer by setting up the project environment and internal data structures. It takes the project root path, converts it to an absolute path, and initializes dictionaries for storing definitions, the call graph (using defaultdict(list)), and Abstract Syntax Trees (ASTs) for processed files. It also defines a set of common directories to ignore during file traversal.
    *   *Parameters:*
        - **project_root** (`str`): The path to the root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This is the main execution method for the analyzer, orchestrating the entire analysis workflow. It first identifies all relevant Python files within the project root using `_find_py_files`. It then iterates over these files twice: once to collect all function and class definitions via `_collect_definitions`, and a second time to resolve the internal function calls and build the call graph using `_resolve_calls`. Finally, it clears the stored ASTs to free memory and returns the structured results generated by `get_formatted_results`.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **results** (`list[dict]`): A list of dictionaries containing the structured call graph results, detailing definitions and who calls them.
        *   **Usage:**
            *   **Calls:** This method calls internal methods such as `_find_py_files`, `_collect_definitions`, `_resolve_calls`, and `get_formatted_results`, and also clears the internal `file_asts` dictionary.
            *   **Called By:** This function is called by the `main_workflow` function in `main.py`.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private method recursively traverses the project directory starting from `self.project_root` to locate all Python files. It utilizes `os.walk` and filters the directories in place to exclude any directories listed in `self.ignore_dirs`, such as version control or virtual environment folders. Files ending with `.py` are collected, their full paths are constructed, and returned as a list.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths pointing to all Python files found in the project, excluding ignored directories.
        *   **Usage:**
            *   **Calls:** This method uses standard library functions like `os.walk`, `os.path.join`, `str.endswith`, and list `append`.
            *   **Called By:** This function is called by the `analyze` method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method is responsible for parsing a given Python file and collecting all defined classes and functions/methods. It reads the file content, parses it into an Abstract Syntax Tree (AST) using `ast.parse`, and stores the AST in `self.file_asts`. It then traverses the AST, identifying `FunctionDef` and `ClassDef` nodes, determines if functions are methods using `_get_parent`, constructs a fully qualified path name, and stores the definition details in `self.definitions`.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file currently being processed.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method interacts with file I/O (`open`, `read`), AST manipulation (`ast.parse`, `ast.walk`, `isinstance`), external utility `path_to_module`, and the internal method `_get_parent`. It also logs errors using `logging.error`.
            *   **Called By:** This function is called by the `analyze` method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This helper method attempts to find the immediate parent node of a given AST node within the provided AST structure. It iterates through all nodes in the tree using `ast.walk` and checks the children of each potential parent using `ast.iter_child_nodes`. If a child matches the target node by identity, the current parent node is returned. This is primarily used to determine if a function definition is nested within a class definition.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root node of the Abstract Syntax Tree being searched.
            - **node** (`ast.AST`): The target node whose parent is being sought.
        *   *Returns:*
            - **parent_node** (`ast.AST | None`): The parent AST node of the input node, or None if no parent is found.
        *   **Usage:**
            *   **Calls:** This method uses AST utility functions `ast.walk` and `ast.iter_child_nodes`.
            *   **Called By:** This function is called by the `_collect_definitions` method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method processes a single file's AST to identify and resolve function and method calls. It retrieves the AST for the given file, instantiates an external `CallResolverVisitor` with necessary context, and traverses the AST using the visitor. The collected call information is then merged into the class's main `self.call_graph` structure, mapping the called entity's path name to a list of callers.
        *   *Parameters:*
            - **filepath** (`str`): The path to the file whose calls are to be resolved.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method instantiates the external class `CallResolverVisitor`, calls its `visit` method, and uses dictionary methods like `get` and `items`, and list method `extend`. It also logs errors using `logging.error`.
            *   **Called By:** This function is called by the `analyze` method.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* This method processes the raw call graph data and the definition data to produce a clean, structured list of results suitable for external consumption. It iterates through every defined entity that is called by another entity. For each entity, it aggregates and deduplicates the list of callers (`called_by`), ensuring each unique caller is listed only once. The final list is sorted by file and line number before being returned.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **output_list** (`list[dict]`): A structured list where each dictionary represents a defined entity and includes a list of all unique locations where it is called.
        *   **Usage:**
            *   **Calls:** This method uses dictionary/list manipulation functions like `items`, `get`, `append`, `values`, and the built-in `sorted` function, along with `os.path.basename`.
            *   **Called By:** This function is called by the `analyze` method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor is an implementation of the standard library's ast.NodeVisitor, specialized for static analysis to map function and method calls to their fully qualified names (QNames) within a single Python file. It traverses the Abstract Syntax Tree (AST), maintaining context about the current module, class, and function being analyzed. The visitor resolves imports and performs basic type inference for instantiated objects to accurately determine the target of every function call. Its primary output is the `self.calls` dictionary, which records all discovered call relationships, including the caller's type and location.
*   **Instantiation:** This class is instantiated by the `_resolve_calls` method located in the `relationship_analyzer.py` file.
*   **Dependencies:** The class relies on the standard library `ast` for inheritance, `os` for file path operations, and `collections.defaultdict` for its internal data structure. It also depends on the external utility function `path_to_module` for initialization.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with necessary file context and external definitions. It calculates the module path, stores the global definitions dictionary, and sets up internal state variables like `scope` (for imports), `instance_types` (for basic type inference), and `calls` (a defaultdict used to store the resolved call relationships).
    *   *Parameters:*
        - **filepath** (`string`): The path to the source file currently being analyzed.
        - **project_root** (`string`): The root directory of the project, used to calculate the module path.
        - **definitions** (`dict`): A dictionary mapping known qualified names to their definitions, used for validating resolved call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method overrides the standard AST visitor behavior for class definitions to manage the current class context. It saves the existing class name and updates the context to the name of the class being visited. After recursively traversing the class body using `generic_visit`, it restores the previous class name, ensuring correct scope tracking for nested structures.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `generic_visit` to continue traversing the AST within the class definition.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` framework when a `ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles function and method definitions by managing the current caller context. It saves the existing `current_caller_name` and updates it to the name of the function being visited. It then recursively visits the function body using `generic_visit`. Finally, it restores the original caller name, allowing the visitor to correctly identify the source of any calls found within the function body.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function or method definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `generic_visit` to recursively traverse the function body.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` framework when a `FunctionDef` node is encountered during AST traversal.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This is the core method for recording function calls. It uses the private helper `_resolve_call_qname` to determine the fully qualified name (QName) of the function being called. If the QName is resolved and exists in the known definitions, it determines the caller's type (module, method, or function) based on the current context. It then compiles detailed caller information and appends it to the `self.calls` dictionary, keyed by the callee's QName, before continuing the AST traversal.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function call.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `_resolve_call_qname` to resolve the target, `basename` to get the file name, `append` to record the call, and `generic_visit` to continue traversal.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` framework when a `Call` node is encountered during AST traversal.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes standard `import` statements (e.g., `import module as alias`). It iterates through all imported names and updates the internal `self.scope` dictionary, mapping the locally used name (alias or original name) to the original module name. This mapping is essential for resolving qualified names later in the analysis. It then continues the AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `generic_visit` to continue traversing the AST.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` framework when an `Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `from ... import ...` statements, including complex relative imports. For relative imports, it calculates the absolute module path based on the current file's module path and the import level. It then maps the locally used name to its fully qualified name in `self.scope`, ensuring accurate resolution of symbols imported from other modules. The traversal continues via `generic_visit`.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method uses string manipulation functions like `split` and `join` and calls `generic_visit` to continue traversal.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` framework when an `ImportFrom` node is encountered during AST traversal.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method performs basic type inference for object instantiation. It specifically checks for assignments where the value is a constructor call (e.g., `x = MyClass()`). If the class name is found in the scope and its qualified name exists in the global definitions, the method maps the assigned variable name to the qualified class name in `self.instance_types`. This mapping allows for resolving method calls on those instances later.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method uses `isinstance` checks for AST node types and calls `generic_visit` to continue traversing the AST.
            *   **Called By:** This method is implicitly called by the `ast.NodeVisitor` framework when an `Assign` node is encountered during AST traversal.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method determines the fully qualified name (QName) of a function or method being called. It handles direct calls by checking the local scope and module path, and attribute calls (e.g., `obj.method`). For attribute calls, it prioritizes resolving based on inferred instance types (`self.instance_types`) or falling back to resolving based on imported module names (`self.scope`). If resolution fails under all checks, it returns None.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being invoked.
        *   *Returns:*
            - **qname** (`string | None`): The fully qualified name of the resolved function or method, or None if resolution fails.
        *   **Usage:**
            *   **Calls:** This method relies on `isinstance` checks for AST node type identification.
            *   **Called By:** This method is called exclusively by `visit_Call` to resolve the target of a function invocation.

### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** This function encrypts a given string using a globally available symmetric encryption object, presumed to be `cipher_suite`. It first performs a guard clause: if the input `text` is empty or if `cipher_suite` is not initialized, the function immediately returns the original text. If encryption is required, the input string is encoded to bytes, passed to the `cipher_suite.encrypt()` method, and the resulting ciphertext bytes are decoded back into a string before being returned. This mechanism ensures that sensitive text data is protected.
*   **Parameters:**
    - **text** (`str`): The string data that needs to be encrypted.
*   **Returns:**
    - **Encrypted text or original text** (`str`): The encrypted string, or the original input string if the input is empty or the global `cipher_suite` object is unavailable.
*   **Usage:**
    *   **Calls:** This function calls `encode` on the input string, the `encrypt` method of the `cipher_suite` object, and finally the `decode` method on the resulting ciphertext bytes.
    *   **Called By:** This function is called by `update_gemini_key`.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** This function attempts to decrypt an input string using a cryptographic object named `cipher_suite`. It first performs a guard clause, returning the original text if the input string is empty or if `cipher_suite` is not defined. If decryption proceeds, the input string is encoded to bytes, passed to `cipher_suite.decrypt()`, and the result is decoded back into a string. The entire decryption process is wrapped in a try-except block to handle potential cryptographic errors, ensuring that the original text is returned safely if decryption fails.
*   **Parameters:**
    - **text** (`str`): The string content that needs to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The successfully decrypted string, or the original input string if decryption fails or if the necessary components are missing.
*   **Usage:**
    *   **Calls:** The function calls `encode` on the input string, `decrypt` on the `cipher_suite` object, and `decode` on the resulting bytes.
    *   **Called By:** This function is called by `get_decrypted_api_keys`.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function handles the creation and insertion of a new user record into a database collection, likely a MongoDB instance represented by `dbusers`. It accepts the user's username, display name, and raw password. The raw password is immediately hashed using `stauth.hasher.hash` for secure storage. The user object is constructed using the `username` as the unique identifier (`_id`) and initializes API key fields to empty strings. Finally, it executes the insertion via `dbusers.insert_one` and returns the ID of the newly inserted document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which is used as the document's primary key (_id).
    - **name** (`str`): The full or display name of the user.
    - **password** (`str`): The raw password string that will be hashed before being stored in the database.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (username) of the newly created user document, returned by the database insertion operation.
*   **Usage:**
    *   **Calls:** This function calls a hashing utility (`hash`) to secure the password and a database method (`insert_one`) to persist the user data.
    *   **Called By:** This function is not called by any other known functions in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is designed to query and retrieve all user records stored in the database collection represented by the `dbusers` object. It executes the `find()` method, which typically returns a cursor or iterable containing all documents matching the query (in this case, all documents). The function then explicitly converts this result into a standard Python list using the `list()` constructor. Finally, the complete list of user records is returned to the caller for processing.
*   **Parameters:** *No parameters.*
*   **Returns:**
    - **users** (`list`): A list containing all user records (documents) retrieved from the database collection.
*   **Usage:**
    *   **Calls:** This function calls the `find` method on the `dbusers` object to initiate the database query, and then uses the built-in `list` constructor to materialize the results.
    *   **Called By:** This function is utilized by the `frontend.Frontend` component, suggesting it is used to populate user data in the application's front end.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** This function is designed to retrieve a single user record from the database based on their username. It executes a query using the `dbusers.find_one` method, mapping the provided `username` string to the database document's primary key, `_id`. The function returns the resulting database document or None if no matching user is found.
*   **Parameters:**
    - **username** (`str`): The unique identifier string used to locate the user record in the database, typically corresponding to the document's _id field.
*   **Returns:**
    - **user** (`dict | None`): The user document (as a dictionary) retrieved from the database, or None if the search query yields no results.
*   **Usage:**
    *   **Calls:** This function calls the `find_one` method, which is used to query the database collection represented by `dbusers` (specifically identified as `database/db.py::find_one`).
    *   **Called By:** This function is not explicitly called by any tracked functions in the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function is responsible for securely updating a user's Gemini API key within the database. It first encrypts the provided raw API key using the helper function `encrypt_text`. It then performs a database update operation using `dbusers.update_one`, targeting the document identified by the provided username and setting the encrypted key. Finally, it returns the count of documents that were successfully modified by the update operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (user ID) of the user whose key needs to be updated.
    - **gemini_api_key** (`str`): The raw, unencrypted Gemini API key provided by the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents (users) whose Gemini API key was successfully updated in the database.
*   **Usage:**
    *   **Calls:** This function calls `encrypt_text` to secure the API key and utilizes `update_one` on the `dbusers` collection for persistence.
    *   **Called By:** This function is called by `frontend.Frontend` located in `Frontend.py`.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function is designed to update the stored Ollama Base URL associated with a specific user in the database. It accepts the user's identifier (`username`) and the new URL string (`ollama_base_url`). It executes a database update operation using the `dbusers` collection, setting the new URL value for the matching user document identified by `_id`. Finally, it returns the count of documents that were successfully modified by the operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (used as the document's _id) of the user whose Ollama URL needs updating.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service to be stored for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database (typically 0 or 1).
*   **Usage:**
    *   **Calls:** This function relies on calling the `update_one` method, likely belonging to a database client object named `dbusers`, to perform the modification.
    *   **Called By:** This function is utilized by the `frontend.Frontend` component.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** The function `fetch_gemini_key` is designed to retrieve a user's stored Gemini API key from the database. It accepts a username string, which is used as the primary identifier (likely the MongoDB `_id`) to query the `dbusers` collection. It executes a `find_one` operation, specifically projecting only the `gemini_api_key` field while excluding the `_id`. The function then safely extracts and returns the value of the `gemini_api_key` using the dictionary `get` method.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user's record in the database.
*   **Returns:**
    - **gemini_api_key** (`str or None`): The Gemini API key string associated with the user, or None if the key field is missing from the user's database record.
*   **Usage:**
    *   **Calls:** This function utilizes `find_one` (likely a MongoDB operation via `dbusers`) to retrieve a single record and subsequently calls the `.get` method on the result.
    *   **Called By:** Based on the provided context, this function is not called by any other functions.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** This function is responsible for retrieving the configured Ollama Base URL for a specific user from the database. It queries the `dbusers` collection using the provided `username` as the document identifier (`_id`). The query is optimized to project only the `ollama_base_url` field. Finally, it safely extracts and returns the value of the `ollama_base_url` field from the resulting document.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) used to locate the user's record in the database.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The base URL for the Ollama service associated with the user, or None if the field is missing from the user's database record.
*   **Usage:**
    *   **Calls:** This function calls a database method named `find_one` to retrieve user data and then uses the dictionary method `get` to safely extract the required URL.
    *   **Called By:** This function is not called by any other functions listed in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** This function handles the deletion of a single user record from the database collection represented by `dbusers`. It takes the user's unique identifier, `username`, and uses it to construct a query targeting the document's `_id` field. The deletion is executed via the `delete_one` method. Finally, the function returns the count of documents that were successfully removed by the operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (used as the MongoDB _id) of the user record to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation. This is typically 1 if the user was found and deleted, or 0 otherwise.
*   **Usage:**
    *   **Calls:** This function executes a database operation by calling `database/db.py::delete_one`.
    *   **Called By:** This function is not referenced by any other function in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function retrieves a user record from the database using the provided username (acting as the document ID). If the user is successfully found, it extracts two specific fields related to API access: the 'gemini_api_key' and the 'ollama_base_url'. The Gemini API key is processed through the `decrypt_text` utility to obtain its plaintext value. The function returns a tuple containing the decrypted Gemini key and the Ollama URL, or a tuple of (None, None) if no user record matches the provided username.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to look up the user record in the database.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted plaintext value of the Gemini API key, or an empty string if the key is missing, or None if the user was not found.
    - **ollama_plain** (`str | None`): The Ollama base URL, or an empty string if the URL is missing, or None if the user was not found.
*   **Usage:**
    *   **Calls:** This function utilizes database methods, specifically `find_one`, to retrieve user data, and calls `decrypt_text` to process the retrieved Gemini API key.
    *   **Called By:** This function is called by the `frontend.Frontend` module/function.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time)`
*   **Description:** This function handles the persistence of a single user-system exchange into a database collection, likely named `dbexchanges`. It constructs a document containing the core exchange details (question, answer, feedback, username, chat name) and various optional metadata fields related to component usage and timing. A creation timestamp is automatically generated using `datetime.now()`. The function executes the insertion operation via `dbexchanges.insert_one` and returns the unique identifier of the newly created database record.
*   **Parameters:**
    - **question** (`str`): The text of the question or prompt provided by the user.
    - **answer** (`str`): The response generated by the system.
    - **feedback** (`str`): The feedback provided by the user regarding the exchange.
    - **username** (`str`): The identifier of the user associated with the exchange.
    - **chat_name** (`str`): The name or identifier of the chat session.
    - **helper_used** (`str`): Optional. Information about the helper component utilized during the exchange. Defaults to an empty string.
    - **main_used** (`str`): Optional. Information about the main component utilized during the exchange. Defaults to an empty string.
    - **total_time** (`str`): Optional. The total time taken for the exchange process. Defaults to an empty string.
    - **helper_time** (`str`): Optional. The time taken specifically by the helper component. Defaults to an empty string.
    - **main_time** (`str`): Optional. The time taken specifically by the main component. Defaults to an empty string.
*   **Returns:**
    - **inserted_id** (`ObjectId`): The unique identifier assigned by the database to the newly inserted document.
*   **Usage:**
    *   **Calls:** This function calls `dbexchanges.insert_one` to persist the data and `datetime.now` to generate a creation timestamp.
    *   **Called By:** This function is called by the `frontend.Frontend` function located within the `Frontend.py` module.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** This function is responsible for querying a database collection, identified as 'dbexchanges', to retrieve all exchange records associated with a specific user. It accepts a username string and uses it as a filter criterion in a database find operation. The results returned by the database query are immediately cast into a standard Python list. This list, containing all matching exchange documents, is then returned to the caller.
*   **Parameters:**
    - **username** (`str`): The string identifier used to filter the database records and fetch exchanges belonging to this specific user.
*   **Returns:**
    - **exchanges** (`list`): A list containing all database documents (exchanges) found where the 'username' field matches the input argument.
*   **Usage:**
    *   **Calls:** This function calls the `find` method on the `dbexchanges` object and uses the built-in `list` constructor to materialize the results.
    *   **Called By:** This function is called by `load_data_from_db`.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function retrieves data exchanges associated with a specific user and chat session from a database collection named dbexchanges. It constructs a query using the provided username and chat_name to filter the records. The results returned by the find operation (likely a database cursor) are immediately converted into a standard Python list before being returned to the caller. The primary goal is to fetch all historical exchanges for a given chat context.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose exchanges are being queried.
    - **chat_name** (`str`): The name or identifier of the specific chat session to filter the exchanges by.
*   **Returns:**
    - **exchanges** (`list`): A list containing all database exchange records matching the provided username and chat name.
*   **Usage:**
    *   **Calls:** This function utilizes database methods, specifically calling `find` on the `dbexchanges` object to execute a query, and then uses the built-in `list` function to convert the resulting cursor into a concrete list.
    *   **Called By:** This function is not explicitly called by any other functions listed in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function updates the 'feedback' field for a specific exchange record in the database. It accepts the unique identifier of the exchange and the new integer feedback value. The function executes a single update operation against the 'dbexchanges' collection, targeting the document matching the provided ID. It returns an integer indicating how many documents were successfully modified.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier used to locate the specific exchange document in the database.
    - **feedback** (`int`): The integer value representing the new feedback to be set for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The count of documents that were modified by the database update operation.
*   **Usage:**
    *   **Calls:** This function calls `database/db.py::update_one` to perform the database modification.
    *   **Called By:** This function is called by `handle_feedback_change` located in `Frontend.py`.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function is responsible for updating the feedback message associated with a specific exchange record in the database. It takes the unique identifier of the exchange and the new feedback message string as arguments. Internally, it utilizes the `dbexchanges.update_one` method, presumably from a MongoDB client, to locate the document using the `exchange_id` and set the new `feedback_message`. The function concludes by returning the count of documents that were successfully modified by the operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier used to locate the specific exchange document in the database collection.
    - **feedback_message** (`str`): The new string value that will replace the existing feedback message for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents (exchanges) that were modified by the update operation.
*   **Usage:**
    *   **Calls:** This function calls the `update_one` method, likely belonging to a MongoDB collection object named `dbexchanges`, to perform the database modification.
    *   **Called By:** This function is called by `render_exchange`.

#### Function: `delete_chats_by_user`
*   **Signature:** `def delete_chats_by_user(username, chat_name)`
*   **Description:** This function is responsible for deleting all chat exchanges associated with a specific user and a named chat session from the database. It constructs a query dictionary based on the provided username and chat name. It executes a `delete_many` operation on the `dbexchanges` collection using this query. The primary purpose is cleanup or removal of historical chat data.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose chat exchanges are targeted for deletion.
    - **chat_name** (`str`): The specific name of the chat session whose exchanges should be removed.
*   **Returns:**
    - **deleted_count** (`int`): The total number of documents (chat exchanges) that were successfully deleted from the database collection.
*   **Usage:**
    *   **Calls:** This function calls the `delete_many` method on the `dbexchanges` object, which is identified as `database/db.py::delete_many` in the context.
    *   **Called By:** This function is called by the `handle_delete_chat` function located in `Frontend.py`.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function is responsible for deleting a single exchange record from the underlying database collection, identified here as dbexchanges. It accepts the unique identifier of the exchange (exchange_id) as input. The deletion is performed by calling delete_one with a query targeting the document where the _id matches the provided ID. The function returns the integer count of documents successfully deleted by the operation.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier (ID) of the exchange record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents successfully deleted by the database operation (typically 1 if successful, 0 otherwise).
*   **Usage:**
    *   **Calls:** This function utilizes the `delete_one` method, likely belonging to a database client object (`dbexchanges`), to execute the deletion command.
    *   **Called By:** This function is invoked by `handle_delete_exchange`.

### File: `frontend/Frontend.py`
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** This function is responsible for initializing and populating the Streamlit session state with chat data retrieved from the database for a given user. It first checks the session state for the 'data_loaded' flag to ensure the loading process only executes once. It retrieves all chat exchanges associated with the provided username using a database utility function. The exchanges are then organized into 'st.session_state.chats', grouped by their 'chat_name', and any missing feedback fields are initialized to 'numpy.nan'. Finally, it ensures that an 'active_chat' is set, defaulting to 'Chat 1' if no existing chats were loaded.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose existing chat data should be loaded from the database.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function primarily interacts with the database via `db.fetch_exchanges_by_user` to retrieve data, and uses standard Python dictionary and list methods such as `get`, `keys`, `list`, and `append` to process and structure the retrieved data within the session state.
    *   **Called By:** This function is invoked by the `frontend.Frontend` component.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function handles the change event for user feedback on an exchange object. It takes the exchange object (`ex`) and the new feedback value (`val`) as input. The function first updates the local state by setting the `"feedback"` key of the `ex` object to the new value. It then ensures persistence by calling `db.update_exchange_feedback` using the exchange's ID and the new value. Finally, it forces a complete rerun of the Streamlit application using `st.rerun()` to reflect the updated state in the UI.
*   **Parameters:**
    - **ex** (`dict`): The exchange object (likely a dictionary) containing the current state and a unique identifier ('_id'). Its 'feedback' field is updated.
    - **val** (`Any`): The new value representing the user's feedback for the exchange.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** The function calls `db.update_exchange_feedback` to persist the feedback change to the database and `st.rerun` to refresh the Streamlit application.
    *   **Called By:** This function is called by `render_exchange`.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function is responsible for deleting a specific data exchange object (`ex`) associated with a given chat session (`chat_name`). It performs a two-step deletion process: first, it calls `db.delete_exchange_by_id` using the exchange's unique identifier (`_id`) to remove the record from the database. Second, it updates the application's state by removing the exchange object from the list stored in `st.session_state.chats[chat_name]["exchanges"]`. The function concludes by invoking `st.rerun()` to force a refresh of the Streamlit application interface.
*   **Parameters:**
    - **chat_name** (`str`): The identifier or name of the chat session whose exchanges list needs modification.
    - **ex** (`dict`): The exchange object to be deleted, which must contain the `_id` key used for database deletion.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function calls `db.delete_exchange_by_id` to remove the exchange from the database, uses the list `remove` method to update the session state, and finally calls `st.rerun` to refresh the frontend.
    *   **Called By:** This function is primarily called by `render_exchange`.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function handles the complete deletion of a specified chat session for a given user. It first executes a database deletion using `db.delete_chats_by_user` to ensure persistence is removed. Subsequently, it deletes the chat entry from the Streamlit session state (`st.session_state.chats`). After deletion, it manages the active chat state: if other chats exist, the first remaining chat becomes active. If no chats remain, a new default chat named 'Chat 1' is created and set as active. The function concludes by forcing a Streamlit rerun to refresh the user interface.
*   **Parameters:**
    - **username** (`str`): The identifier of the user associated with the chat being deleted.
    - **chat_name** (`str`): The unique name of the chat session to be removed.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function calls `delete_chats_by_user` (likely a database operation), and uses standard Python functions like `len`, `list`, and `keys`. It also invokes Streamlit's `rerun` function to update the application state.
    *   **Called By:** This function is called by the `frontend.Frontend` module or class initialization.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text)`
*   **Description:** This function is designed to process a string of markdown text and render it within a Streamlit application, specifically handling embedded Mermaid diagram blocks. It uses regular expressions to split the input text based on the ````mermaid ... ```` delimiters. Standard markdown content is rendered using `st.markdown`. The content identified as Mermaid code is attempted to be rendered graphically using `st_mermaid`, with a fallback mechanism to display the raw code using `st.code` if the graphical rendering fails.
*   **Parameters:**
    - **markdown_text** (`str`): The input text containing standard markdown and potential Mermaid diagram blocks to be rendered.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function utilizes regular expressions (`re.split`) for parsing, standard Python functions (`enumerate`, `hash`, `strip`) for processing, and external libraries (`st.markdown`, `st.code`, `st_mermaid`) for rendering the output.
    *   **Called By:** This function is primarily used by `render_exchange` and is also referenced within the `frontend.Frontend` module context.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function is responsible for rendering a single chat exchange (a question and an answer) within a Streamlit application interface. It first displays the user's question using st.chat_message("user"). The assistant's response is rendered along with a comprehensive toolbar implemented using Streamlit columns. This toolbar allows users to provide positive or negative feedback, write detailed feedback via a popover (which updates the database using db.update_exchange_feedback_message), download the response content, and delete the exchange. Finally, the assistant's answer is displayed in a scrollable container using render_text_with_mermaid.
*   **Parameters:**
    - **ex** (`dict`): The exchange object containing the user's question, the assistant's answer, feedback status, and a unique identifier ('_id').
    - **current_chat_name** (`str`): The identifier of the current chat session, used for context when invoking the exchange deletion handler.
*   **Returns:** This function does not return a value.
*   **Usage:**
    *   **Calls:** This function makes extensive use of Streamlit components (e.g., chat_message, button, popover, download_button, columns, container, write) for UI rendering. It handles user interactions by calling handle_feedback_change, handle_delete_exchange, and updates the database via db.update_exchange_feedback_message. It also uses time.sleep and st.rerun after saving feedback, and renders content using render_text_with_mermaid.
    *   **Called By:** This function is called by a function within the frontend.Frontend module.

### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic data model used to strictly define the metadata for a single parameter within a function or method signature. It serves as a schema for capturing the parameter's identifier, its type annotation (as a string), and a detailed textual description of its purpose. This model ensures that all necessary information about a function parameter is consistently structured for documentation or analysis purposes.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class depends on `pydantic.BaseModel` for its structural definition and validation capabilities.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel, requiring values for `name`, `type`, and `description` to initialize the instance attributes. It validates that these three fields are present and are strings upon instantiation.
    *   *Parameters:*
        - **name** (`str`): The name of the function parameter.
        - **type** (`str`): The string representation of the parameter's type hint.
        - **description** (`str`): A detailed description explaining the purpose and usage of the parameter.
*   **Methods:** *No methods defined.*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel used to structure and validate data describing the return value of a function. It acts as a strict schema, ensuring that any return description object consistently contains the necessary fields: a name, a type string, and a detailed description string. This model is essential for maintaining data integrity in systems that process function metadata, such as documentation generators or code analysis tools.
*   **Instantiation:** The points of instantiation for this class are not specified in the provided context.
*   **Dependencies:** This class depends on pydantic.BaseModel to provide automatic data validation, serialization, and schema generation based on the defined attributes.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor automatically accepts keyword arguments corresponding to the defined fields (`name`, `type`, `description`) to initialize and validate the instance data according to the specified string types.
    *   *Parameters:*
        - **name** (`str`): The identifier or name associated with the return value.
        - **type** (`str`): The data type of the returned value (e.g., 'int', 'List[str]', 'None').
        - **description** (`str`): A detailed explanation of the purpose and content of the returned value.
*   **Methods:** *No methods defined.*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to strictly define the calling context of a function or method. It serves as a data structure to encapsulate information about the entity's relationships within the codebase. It enforces the presence of two string fields, 'calls' and 'called_by', ensuring structured documentation regarding what the entity uses and where it is used.
*   **Instantiation:** The instantiation points for this class are not provided in the context, but it is typically instantiated by components that generate structured analysis data.
*   **Dependencies:** This class depends on pydantic.BaseModel for defining its structure and providing data validation capabilities.
*   **Constructor:**
    *   *Description:* The class uses the inherited Pydantic BaseModel constructor, which automatically handles initialization and validation based on the defined type-hinted fields. It accepts 'calls' and 'called_by' as required keyword arguments.
    *   *Parameters:*
        - **calls** (`str`): A summary string detailing the external functions, methods, or classes that the entity calls or utilizes.
        - **called_by** (`str`): A summary string detailing the locations (functions, methods, or files) that invoke or instantiate this entity.
*   **Methods:** *No methods defined.*

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic data model designed to structure the detailed analysis of a single Python function. It encapsulates all necessary metadata for understanding a function's signature and behavior, including a textual summary of its purpose, lists of input parameters and return values, and contextual usage information regarding its place in the codebase. This model is fundamental for ensuring that function analysis data is standardized and easily machine-readable for documentation or further processing.
*   **Instantiation:** The input context does not specify where this class is instantiated, but as a Pydantic model, it is typically instantiated during data parsing or within automated analysis pipelines that generate function descriptions.
*   **Dependencies:** This class depends on pydantic.BaseModel for its data structure and validation, and relies on external types such as ParameterDescription, ReturnDescription, and UsageContext to define its fields.
*   **Constructor:**
    *   *Description:* The constructor is inherited from pydantic.BaseModel. It initializes the instance by validating and assigning values to the four required fields: overall, parameters, returns, and usage_context.
    *   *Parameters:*
        - **overall** (`str`): A concise, high-level summary describing the function's purpose and implementation.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing the function's input arguments.
        - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects detailing the function's return values.
        - **usage_context** (`UsageContext`): An object containing information about the function's external calls and where it is called within the system.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class serves as the primary data model for structuring the comprehensive analysis of a single Python function or method. It encapsulates the function's name via the `identifier`, holds the detailed behavioral and structural analysis within the `description` field, and provides an optional `error` field for reporting analysis failures. As a Pydantic model, it ensures data integrity and type validation for structured code analysis outputs.
*   **Instantiation:** The input context does not specify where this class is instantiated, suggesting its usage points are currently unknown or external to the provided context.
*   **Dependencies:** This class depends on Pydantic's BaseModel for its structure and validation capabilities, and utilizes typing.Optional for the error field, as well as the custom type FunctionDescription to hold the core analysis data.
*   **Constructor:**
    *   *Description:* The `FunctionAnalysis` model is initialized by providing values for its three core attributes: the function's name (`identifier`), the detailed analysis object (`description`), and an optional error string. Since it inherits from BaseModel, initialization includes Pydantic's validation and type checking processes.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): A nested object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional field used to store an error message if the analysis of the function failed or was incomplete.
*   **Methods:** *No methods defined.*

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic data model used to structure and validate metadata about the `__init__` method of a Python class. It defines two core fields: a textual summary of the constructor's purpose and a list of detailed parameter descriptions. This model is essential for systems that analyze and document object initialization logic, providing a standardized format for constructor analysis results.
*   **Instantiation:** The points where this class is instantiated are currently unknown based on the provided context.
*   **Dependencies:** This class depends on the Pydantic library for its BaseModel functionality and the standard typing module for the List type hint.
*   **Constructor:**
    *   *Description:* The class is initialized via the Pydantic BaseModel constructor, accepting keyword arguments corresponding to its defined fields: `description` (a string summary) and `parameters` (a list of parameter details). Pydantic handles validation and assignment automatically.
    *   *Parameters:*
        - **description** (`str`): A high-level summary describing the function and behavior of the constructor.
        - **parameters** (`List[ParameterDescription]`): A list containing detailed descriptions of each parameter accepted by the constructor.
*   **Methods:** *No methods defined.*

#### Class: `ClassContext`
*   **Summary:** The ClassContext is a Pydantic data model designed to encapsulate the usage context of a target class within a larger system. It strictly defines two required string fields: dependencies, which summarizes external resources or modules the target class relies on, and instantiated_by, which specifies the locations or modules responsible for creating instances of the target class. This model ensures that context information is consistently represented.
*   **Instantiation:** The analysis context provided no explicit locations where this class is instantiated.
*   **Dependencies:** The analysis context provided no explicit external dependencies for this class.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated to accept and validate the dependencies and instantiated_by fields, ensuring both are provided as strings upon instantiation.
    *   *Parameters:*
        - **dependencies** (`str`): A summary of the external dependencies required by the class being analyzed.
        - **instantiated_by** (`str`): A summary of the locations or modules where the class being analyzed is instantiated.
*   **Methods:** *No methods defined.*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to serve as a comprehensive schema for storing the structured analysis of a Python class. It acts as the primary data container, aggregating all necessary information derived from static code analysis. Its fields define the structure for the overall class summary, the constructor details, a list of analyses for all nested methods, and contextual information regarding dependencies and usage.
*   **Instantiation:** The instantiation points for this class were not provided in the context.
*   **Dependencies:** This class does not appear to have explicit external functional dependencies beyond its base class, BaseModel, and the types used for its fields (ConstructorDescription, FunctionAnalysis, ClassContext).
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated to accept and validate the four required fields: overall, init_method, methods, and usage_context. It initializes the data structure that holds the complete analysis of a target class.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose.
        - **init_method** (`ConstructorDescription`): The structured analysis of the class's __init__ method.
        - **methods** (`List[FunctionAnalysis]`): A list containing the structured analysis for every method defined within the class.
        - **usage_context** (`ClassContext`): Contextual information regarding the class's dependencies and instantiation points.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis model serves as the root structure for storing the comprehensive analysis of a single Python class. It is a Pydantic BaseModel designed to encapsulate all findings from the AI Code Analyst. It holds the class's unique name, the detailed structural and behavioral analysis in the nested `description` object, and provides an optional field to report any errors encountered during the analysis process.
*   **Instantiation:** The points of instantiation for this class were not provided in the context.
*   **Dependencies:** This class relies on Pydantic's BaseModel for defining its structure and validation, and uses Python's `typing.Optional` for the error field.
*   **Constructor:**
    *   *Description:* The class is initialized via Pydantic's BaseModel constructor, requiring values for the class identifier and the detailed analysis object. The optional `error` field defaults to `None` if no issues are present.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the class being analyzed.
        - **description** (`ClassDescription`): A nested object containing the detailed structural and behavioral analysis of the class.
        - **error** (`Optional[str]`): An optional field used to store an error message if the analysis process failed or encountered issues.
*   **Methods:** *No methods defined.*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic data model used to structure and validate information regarding a specific call event identified by a relationship analyzer. It serves as a standardized record for tracking where a function or class is called or instantiated, storing critical metadata such as the source file, the name of the caller, the type of the calling entity (mode), and the exact line number of the invocation. This model is essential for building the 'called_by' and 'instantiated_by' lists in the analysis results.
*   **Instantiation:** The specific instantiation points are not provided in the context, but this class is typically instantiated by the relationship analyzer component to record call events.
*   **Dependencies:** This class relies on the Pydantic library, specifically inheriting from BaseModel, to provide automatic data validation and serialization capabilities.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel, allowing instantiation of a CallInfo object by passing keyword arguments corresponding to the defined fields. It performs type validation to ensure that all four required attributes (file, function, mode, and line) conform to their specified string or integer types.
    *   *Parameters:*
        - **file** (`str`): The path to the source file where the call originated.
        - **function** (`str`): The name of the function or method that performed the call.
        - **mode** (`str`): The type of the calling entity, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the source file where the call occurred.
*   **Methods:** *No methods defined.*

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to structure and hold the contextual data required for analyzing a specific function. It encapsulates two primary pieces of information: a list of external entities the function calls, and a list of structured objects detailing the entities that call the function, thereby providing a complete interaction map. This structure ensures that function analysis is performed using standardized, validated input data.
*   **Instantiation:** This class is instantiated by the `main_workflow` function located in `main.py`.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context, relying primarily on standard Python types and Pydantic's BaseModel.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated. It accepts keyword arguments corresponding to the defined fields, allowing for the initialization and validation of the function's call context upon instantiation.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing the names of functions, methods, or classes called by the function being analyzed.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects detailing the functions or methods that call the function being analyzed, providing structured information about the callers.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel that defines the strict input schema required for initiating a function analysis process. It acts as a data transfer object (DTO) ensuring that all necessary components
—such as the function's source code, identifier, and contextual information
—are present and correctly typed. This structure guarantees reliable data input for subsequent AI processing steps.
*   **Instantiation:** This class is instantiated by the main_workflow function located in the main.py file.
*   **Dependencies:** This class relies on pydantic.BaseModel for data validation and structure, and utilizes typing components such as Literal and List.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated to validate and initialize the instance attributes based on the provided data. It ensures that all required fields, including the analysis mode, identifier, source code, imports list, and context object, conform to their specified types.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): A literal string specifying that the input is intended for function analysis.
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **source_code** (`str`): The raw source code string of the function definition.
        - **imports** (`List[str]`): A list of import statements relevant to the function's environment.
        - **context** (`FunctionContextInput`): A nested object containing additional contextual data required for the analysis.
*   **Methods:** *No methods defined.*

#### Class: `MethodContextInput`
*   **Summary:** This class serves as a structured Pydantic model (BaseModel) used to encapsulate contextual information about a specific method within a codebase analysis workflow. It defines the necessary data points — such as the method's unique identifier, its internal function calls, external callers, arguments, and associated docstring — to provide a complete usage context for that method.
*   **Instantiation:** This class is instantiated within the `main_workflow` function located in `main.py` on line 232.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The class is initialized via the Pydantic BaseModel constructor, which accepts and validates values for its defined fields: identifier, calls, called_by, args, and an optional docstring. These fields are assigned as instance attributes upon creation, ensuring data integrity based on the defined types.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method being described.
        - **calls** (`List[str]`): A list of identifiers for other functions, methods, or classes that this method calls internally.
        - **called_by** (`List[CallInfo]`): A list detailing the external locations (CallInfo objects) from which this method is invoked.
        - **args** (`List[str]`): A list of arguments defined in the method's signature.
        - **docstring** (`Optional[str]`): The optional docstring content associated with the method.
*   **Methods:** *No methods defined.*

#### Class: `ClassContextInput`
*   **Summary:** ClassContextInput is a Pydantic data model designed to encapsulate all necessary contextual information required for a comprehensive analysis of a target Python class. It structures data regarding the class's external dependencies, the locations where it is instantiated throughout the codebase, and detailed context for each of its internal methods. This schema serves as a standardized input format for subsequent AI processing steps.
*   **Instantiation:** This class is instantiated within the main_orchestrator function in HelperLLM.py and the main_workflow function in main.py.
*   **Dependencies:** The class does not explicitly rely on other components or external libraries listed in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the class is initialized by providing values for its three defined fields: dependencies, instantiated_by, and method_context. Pydantic handles validation and attribute assignment automatically upon instantiation.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing the external dependencies of the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects detailing the locations where the class being analyzed is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list providing detailed context, such as calls and callers, for each method within the class being analyzed.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput is a Pydantic data model that defines the required schema for the input payload used to request a class analysis. It acts as a strict contract, ensuring that the necessary components, such as the class identifier, its raw source code, associated imports, and detailed context, are provided before the analysis process can begin. Since it inherits from BaseModel, it provides automatic data validation and parsing for the analysis system.
*   **Instantiation:** The class is instantiated by the `main_orchestrator` function in `HelperLLM.py` and the `main_workflow` function in `main.py`, indicating its role in processing input data for the analysis pipeline.
*   **Dependencies:** This class relies on external types like `Literal` and `List` from the `typing` module, `BaseModel` from `pydantic`, and the custom type `ClassContextInput` for defining its fields.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, this class does not define an explicit __init__ method. Initialization is handled automatically by Pydantic, which validates and assigns values to the defined fields upon instantiation.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): A literal string that must be 'class_analysis', serving as a discriminator to identify the type of request being processed.
        - **identifier** (`str`): The fully qualified name of the class that is to be analyzed.
        - **source_code** (`str`): The raw source code string containing the complete definition of the class.
        - **imports** (`List[str]`): A list of strings representing the import statements found in the source file containing the class.
        - **context** (`ClassContextInput`): A nested object providing contextual information, such as dependencies, instantiation points, and method call graphs.
*   **Methods:** *No methods defined.*
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** This project, the 'Repo Onboarding Agent', is an advanced AI-powered system designed to automate the process of generating comprehensive technical documentation for Git repositories. It leverages Large Language Models (LLMs) and various code analysis techniques (AST parsing, dependency tracking, call graph generation) to extract, synthesize, and present crucial information about a codebase, aiding in developer onboarding and project understanding. The system includes a backend for code analysis and LLM orchestration, and a frontend for user interaction and report display.
- **Key Features:**
  - Automated Repository Cloning and File Extraction.
  - Advanced Code Analysis (AST, Dependency, Call Graph).
  - LLM-Powered Function and Class Documentation.
  - Comprehensive Project Report Generation.
  - Interactive Frontend for Documentation Viewing.
- **Tech Stack:** Python, GitPython, Streamlit, LangChain, Google Gemini, OpenAI GPT, Ollama (for LLM interactions), MongoDB (for database), Pydantic (for data validation), NetworkX (for graph analysis), Matplotlib (for charting), nbformat.

*   **Repository Structure:**
    ```mermaid
    graph LR
        N0["root/"]
        N1["SystemPrompts/"]
        N2["backend/"]
        N3["database/"]
        N4["frontend/"]
        N5["notizen/"]
        N6["result/"]
        N7["schemas/"]
        N8["statistics/"]
        N0 --> N1
        N0 --> N2
        N0 --> N3
        N0 --> N4
        N0 --> N5
        N0 --> N6
        N0 --> N7
        N0 --> N8
        N0 --> F9["readme.md<br/>requirements.txt<br/>.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>test.json"]
        N1 --> F10["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt"]
        N2 --> F11["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py"]
        N3 --> F12["db.py"]
        N4 --> N13[".streamlit/"]
        N4 --> N14["gifs/"]
        N4 --> F15["frontend.py<br/>__init__.py"]
        N13 --> F16["config.toml"]
        N14 --> F17["4j.gif"]
        N5 --> N18["grafiken/"]
        N5 --> F19["doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>Report Agenda.txt<br/>technische_notizen.md<br/>Zwischenpraesentation Agenda.txt"]
        N18 --> N20["1/"]
        N18 --> N21["2/"]
        N18 --> N22["Flask-Repo/"]
        N18 --> N23["Repo-onboarding/"]
        N20 --> F24["File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
        N21 --> F25["FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot"]
        N22 --> F26["__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot"]
        N23 --> F27["AST.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>Frontend.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>HelperLLM.dot<br/>HelperLLM.png<br/>main.dot<br/>MainLLM.dot<br/>tools.dot<br/>types.dot"]
        N6 --> F28["ast_schema_01_12_2025_11-49-24.json<br/>notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md<br/>notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
        N7 --> F29["types.py"]
        N8 --> F30["savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png"]
    ```

## 2. Installation
### Dependencies
Dependencies can be installed via `pip install -r requirements.txt`.
### Setup Guide
1.  **Clone the Repository:** Obtain the project source code from its Git repository.
2.  **Environment Setup:** Ensure you have Python 3.x and Git installed on your system.
3.  **Virtual Environment:** It is recommended to create and activate a Python virtual environment to manage dependencies:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate     # On Windows
    ```
4.  **Install Dependencies:** Install all required Python packages using the provided `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
5.  **API Key Configuration:** Create a `.env` file in the project root based on `.env.example`. Populate it with your API keys for the Large Language Models (e.g., `GEMINI_API_KEY`, `OPENAI_API_KEY`) and any custom LLM endpoints (e.g., `OLLAMA_BASE_URL` or `SCADSLLM_URL`).
6.  **Database Setup:** Ensure a MongoDB instance is running and accessible as configured (e.g., `MONGO_URI` in your `.env` file).
### Quick Startup
To launch the interactive frontend application:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The Repo Onboarding Agent facilitates several key use cases for understanding and documenting codebases:

*   **Generate Comprehensive Repository Documentation:** Users can provide a GitHub repository URL, and the agent will perform a deep analysis of the codebase, including Abstract Syntax Tree (AST) generation, dependency tracking, and call graph analysis. It then leverages LLMs to synthesize this information into a detailed Markdown documentation report covering functions, classes, and overall architecture.
*   **Analyze and Document Jupyter Notebooks:** The system can process `.ipynb` files found within a repository, extracting and documenting their code cells, markdown, and execution outputs (including embedded images), generating specific reports for notebook content.
*   **Interactive Documentation Interface:** The Streamlit-based frontend provides an intuitive web interface for users to input repository URLs, select different LLM models for analysis, view generated reports, and manage a history of their documentation generation sessions.
*   **LLM Model Evaluation and Comparison:** The system tracks token usage and calculates savings when converting analysis data from JSON to the TOON format. It also supports integration with various LLM providers (Google Gemini, OpenAI, Ollama), allowing for comparison of their performance in documentation generation.

**Primary Command:**
The main way to interact with the Repo Onboarding Agent is through its Streamlit web interface:
```bash
streamlit run frontend/frontend.py
```

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into its corresponding Python module path string. It first determines the relative path of the file with respect to a specified project root, falling back to the base filename if a relative path cannot be determined. The function then removes the '.py' extension if present and replaces system-specific path separators with dots. Finally, it handles `__init__` modules by removing the `.__init__` suffix to yield the package name.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative module path.
*   **Returns:**
    - **module_path** (`str`): The Python module path string derived from the input filepath.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to systematically traverse the Abstract Syntax Tree (AST) of a given Python source file. Its core function is to extract and structure metadata about imports, functions, and classes found within the code. It builds a comprehensive schema that categorizes these elements, distinguishing between module-level functions and methods nested within classes, and handles both synchronous and asynchronous function definitions uniformly.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class depends on the `ast` module for parsing and traversing Python Abstract Syntax Trees, and it implicitly relies on a `path_to_module` function for resolving module paths.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes an instance of the ASTVisitor, setting up the context for AST traversal. It stores the raw source code, file path, and project root, then calculates the module's fully qualified path. It also initializes an empty `schema` dictionary to accumulate parsed imports, functions, and classes, and sets `_current_class` to `None` to track the current class being visited.
    *   *Parameters:*
        - **source_code** (`str`): The raw string content of the Python source file to be analyzed.
        - **file_path** (`str`): The absolute path to the Python file being processed.
        - **project_root** (`str`): The root directory of the entire project, used for module path resolution.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node)`
        *   *Description:* This method is invoked by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered, representing a simple `import module` statement. It iterates through each alias specified in the import statement and appends the module's name to the `imports` list within the `self.schema` dictionary. After processing the current node's direct information, it calls `self.generic_visit(node)` to ensure that any child nodes (though typically none for simple imports) are also traversed.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement (e.g., `import os`).
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.generic_visit` to continue AST traversal.
        Called By: This method is called by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to `from module import name` statements. It iterates through each alias (imported name) within the node, constructing a fully qualified import string (e.g., `module.name`). This constructed string is then appended to the `imports` list stored in `self.schema`. Following this, `self.generic_visit(node)` is called to ensure that any nested nodes within the import statement are also visited, although typically there are none for this type of node.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.generic_visit` to continue AST traversal.
        Called By: This method is called by the `ast.NodeVisitor` framework when an `ast.ImportFrom` node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions in the source code. It constructs a unique identifier for the class, extracts its name, docstring, and the exact source code segment defining the class. It then creates a `class_info` dictionary containing these details and appends it to the `classes` list within `self.schema`. Crucially, it sets `_current_class` to this `class_info` before calling `self.generic_visit(node)` to ensure that methods defined within this class are correctly associated. Finally, `_current_class` is reset to `None` after the class's children have been visited.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit` to extract information and continue AST traversal.
        Called By: This method is called by the `ast.NodeVisitor` framework when an `ast.ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, which represent function definitions. It intelligently distinguishes between methods defined within a class and standalone functions based on the `_current_class` attribute. If `_current_class` is set, it treats the node as a method, creating `method_context_info` and appending it to the `method_context` list of the `_current_class`. Otherwise, it treats it as a standalone function, creating `func_info` and appending it to the `functions` list in `self.schema`. After processing, it calls `self.generic_visit(node)` to continue traversing the function's body.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit` to extract information and continue AST traversal.
        Called By: This method is called by the `ast.NodeVisitor` framework when an `ast.FunctionDef` node is encountered during AST traversal.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node)`
        *   *Description:* This method processes `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation is straightforward: it simply delegates the processing of the asynchronous function node to the `visit_FunctionDef` method. This design choice indicates that, for the purpose of schema extraction, asynchronous functions are treated identically to regular synchronous functions, unifying the analysis logic for both types of function definitions.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.visit_FunctionDef` to process the node.
        Called By: This method is called by the `ast.NodeVisitor` framework when an `ast.AsyncFunctionDef` node is encountered during AST traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process and analyze Python source code within a repository to generate a structured Abstract Syntax Tree (AST) schema. It provides functionalities to parse individual files, extract their structural components (functions, classes, imports), and then enrich this schema with inter-component relationship data such as calls, called-by, and dependencies. This class serves as a core component for understanding the architectural layout and interaction patterns within a codebase.
*   **Instantiation:** This class is not explicitly instantiated by any other components in the provided context.
*   **Dependencies:** The class depends on the ast module for parsing Python code, the os module for path manipulation, and the GitRepository class for repository context, as well as an ASTVisitor class for detailed AST traversal.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It currently does not perform any specific setup or attribute initialization, acting as a placeholder.
    *   *Parameters:*
        - **self** (`ASTAnalyzer`): The instance of the class.
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, raw_relationships)`
        *   *Description:* This method integrates call relationship data (incoming and outgoing calls) into a pre-existing AST schema. It iterates through files, functions, and classes within the full_schema to enrich their context with calls, called_by, instantiated_by, and dependencies information. Specifically, it populates function call lists, class instantiation lists, and identifies external dependencies for classes based on method calls.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): A dictionary representing the complete AST schema of a repository, including files, functions, and classes.
            - **raw_relationships** (`dict`): A dictionary containing raw incoming and outgoing call relationships, typically parsed from a separate analysis step.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary, now enriched with call and dependency relationship data.
        *   **Usage:** Calls: This method does not explicitly call other methods, classes, or functions within its source code.
        Called By: This method is not explicitly called by any other functions or methods in the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files, repo)`
        *   *Description:* This method analyzes a list of source code files within a given Git repository to build a comprehensive Abstract Syntax Tree (AST) schema. It iterates through Python files, parses their content using the ast module, and then uses an ASTVisitor to extract structural information like imports, functions, and classes. The collected data for each file is then organized into a full_schema dictionary, handling potential parsing errors gracefully.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): A list of file objects, each containing at least a 'path' and 'content' attribute, representing the source files to be analyzed.
            - **repo** (`GitRepository`): An object representing the Git repository, though its specific attributes are not directly used in this method beyond providing context for file paths.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed repository, structured by file paths and containing extracted AST nodes (imports, functions, classes).
        *   **Usage:** Calls: This method calls os.path.commonpath, os.path.isfile, os.path.dirname, ast.parse, ASTVisitor (instantiation), and visitor.visit.
        Called By: This method is not explicitly called by any other functions or methods in the provided context.

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a repository. It initializes a networkx.DiGraph and then utilizes a FileDependencyGraph visitor to process an Abstract Syntax Tree (AST) of a specified file. The visitor extracts import relationships, which are then used to populate the graph. For each identified importing file and its dependencies, nodes are added to the graph, and directed edges are created from the importer to its imported modules. The function ultimately returns this dependency graph.
*   **Parameters:**
    - **filename** (`str`): The path or name of the file being analyzed for dependencies.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`networkx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies (from caller to callee).
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function constructs a directed graph representing the dependencies within a given Git repository. It iterates through all Python files in the repository, parses each file's content into an Abstract Syntax Tree (AST), and then generates a file-specific dependency graph. These individual file graphs are then merged into a single global directed graph, which is returned. The graph nodes represent entities (e.g., functions, classes) and edges represent calls or relationships between them.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object containing the files to be analyzed for dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependencies across all Python files in the repository.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function `get_all_temp_files` is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input, converts it to an absolute `Path` object, and then recursively searches for all files ending with ".py". The function returns a list of these Python file paths, with each path represented relative to the initial root directory.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory from which to recursively find Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `Path` objects, where each path is relative to the input `directory` and points to a Python file.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze Python source code files to build a graph of import dependencies. It extends `ast.NodeVisitor` to traverse the Abstract Syntax Tree (AST) of a given file. Its primary function is to identify both absolute and relative import statements, resolve them to their actual module names, and store these dependencies in an internal dictionary. The class provides methods to handle different types of import nodes and to resolve complex relative imports, making it a crucial component for understanding the structural relationships between files in a Python project.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** The class relies on external modules such as `ast` for AST traversal and node manipulation, `pathlib` for path operations, `keyword` for checking Python keywords, and a custom `get_all_temp_files` function (likely from `getRepo.GitRepository` based on imports).
*   **Constructor:**
    *   *Description:* This constructor initializes a FileDependencyGraph instance by setting the `filename` and `repo_root` attributes. These attributes are crucial for identifying the file being analyzed and for resolving file paths within the repository.
    *   *Parameters:*
        - **filename** (`str`): The name of the file for which dependencies are being analyzed.
        - **repo_root** (`Any`): The root directory of the repository, used for resolving file paths.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This method resolves relative Python imports, such as `from .. import name1, name2`, into actual module or symbol names. It determines the correct base directory based on the import level and then checks for the existence of corresponding files or symbols within `__init__.py` files. The method iterates through the imported names, verifying if they exist as module files or are exported by an `__init__.py` file, and returns a sorted list of resolved names. If no modules or symbols can be resolved, it raises an `ImportError`.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the `from ... import ...` statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:** Calls: This method calls `get_all_temp_files`, `Path`, `Path.stem`, `Path.name`, `Path.parent`, `Path.resolve`, `Path.exists`, `Path.read_text`, `parse`, `walk`, `isinstance`, `literal_eval`, `iskeyword`, `print`. It also defines and calls two nested functions: `module_file_exists` and `init_exports_symbol`.
        Called By: This method is called by `visit_ImportFrom`.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method processes `Import` and `ImportFrom` AST nodes to record file dependencies. It iterates through the aliases specified in the import statement. For each alias, it adds the imported module's base name or the alias's name to the `import_dependencies` set associated with the current `self.filename`. Finally, it calls `self.generic_visit(node)` to continue AST traversal.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing an import statement.
            - **base_name** (`str | None`): An optional base name for the module, used for `from ... import ...` statements where the module name is already resolved.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `set.add` and `self.generic_visit`.
        Called By: This method is called by `visit_ImportFrom`.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ImportFrom` AST nodes, specifically for imports like `from a.b.c import d`. If the import is absolute (e.g., `from a.b.c`), it extracts the last part of the module name (e.g., `c`) and passes it to `visit_Import`. If the import is relative (e.g., `from .. import x`), it uses `_resolve_module_name` to determine the actual module names and then records each resolved dependency via `visit_Import`. It includes error handling for failed relative import resolution.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the `from ... import ...` statement.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `str.split`, `self.visit_Import`, `self._resolve_module_name`, `print`, and `self.generic_visit`.
        Called By: This method is a standard `NodeVisitor` method, implicitly called by the AST traversal mechanism.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a testing orchestrator for the LLMHelper class, defining dummy data for function analysis inputs and their corresponding pre-computed analysis results. It initializes an LLMHelper instance with API keys and prompt paths, then simulates the process of generating documentation for functions using the prepared inputs. Finally, it aggregates and prints the generated documentation.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various large language models (LLMs), such as Google Gemini, OpenAI GPT, or custom/Ollama models, to generate structured documentation. It is designed to process batches of function or class analysis requests, ensuring proper API interaction, error handling, and adherence to rate limits. The class leverages Pydantic for input/output validation and dynamically configures LLM clients with structured output capabilities based on the chosen model, making it a robust tool for automated code documentation.
*   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
*   **Dependencies:** This class does not explicitly list external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by setting up the API key, loading system prompts for function and class analysis from specified file paths, and configuring the underlying language model. It dynamically selects and initializes an LLM client (Gemini, OpenAI, Custom API, or Ollama) based on the `model_name` and optional `base_url` and then wraps it with structured output capabilities for `FunctionAnalysis` and `ClassAnalysis` Pydantic schemas. It also calls a private method to configure batch processing settings.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the chosen language model (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt used for function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt used for class analysis.
        - **model_name** (`str`): The name of the language model to use, defaulting to 'gemini-2.0-flash-lite'. This determines the LLM provider and batch size.
        - **base_url** (`str | None`): An optional base URL for custom or Ollama LLM endpoints.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method configures the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It assigns specific batch sizes for various Gemini, Llama, and GPT models, as well as custom API models, to optimize performance and adhere to potential rate limits. If an unknown model name is encountered, it logs a warning and sets a conservative default batch size of 2.
        *   *Parameters:*
            - **model_name** (`str`): The name of the language model for which to configure batch settings.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `logging.warning` to report unknown model names.
        Called By: This method is called by the `__init__` constructor of the `LLMHelper` class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates and validates documentation for a list of functions by interacting with the configured language model. It takes a list of `FunctionAnalysisInput` objects, converts them into JSON payloads, and then sends these payloads to the `function_llm` in batches. The method includes logic for handling API errors during batch processing, extending the results with `None` for failed items, and implementing a waiting period between batches to respect rate limits.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary data for a function to be analyzed.
        *   *Returns:*
            - **null** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, where each object contains the generated and validated documentation for a function, or `None` if an error occurred during its processing.
        *   **Usage:** Calls: This method calls `json.dumps` to serialize input models, `SystemMessage` and `HumanMessage` to construct LLM conversations, `self.function_llm.batch` to send requests to the LLM, `logging.info` for progress updates, `logging.error` for error reporting, and `time.sleep` to implement rate limiting.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating and validating documentation for a batch of classes using the configured language model. It accepts a list of `ClassAnalysisInput` objects, transforms them into JSON payloads, and dispatches these payloads to the `class_llm` in batches. The method incorporates error handling to manage exceptions during API calls and includes a delay mechanism (`time.sleep`) to comply with LLM API rate limits, ensuring robust and controlled interaction.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary data for a class to be analyzed.
        *   *Returns:*
            - **null** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, where each object contains the generated and validated documentation for a class, or `None` if an error occurred during its processing.
        *   **Usage:** Calls: This method calls `json.dumps` to serialize input models, `SystemMessage` and `HumanMessage` to construct LLM conversations, `self.class_llm.batch` to send requests to the LLM, `logging.info` for progress updates, `logging.error` for error reporting, and `time.sleep` to implement rate limiting.
        Called By: This method is not explicitly called by other functions or methods in the provided context.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a central interface for interacting with various Large Language Models (LLMs). It abstracts away the specifics of different LLM providers (Google Gemini, OpenAI-compatible APIs, Ollama) by dynamically initializing the appropriate client based on the provided model name. The class handles loading a system prompt from a file, validating API keys, and provides methods for both synchronous and streaming interactions with the configured LLM.
*   **Instantiation:** This class is not explicitly instantiated by any known components within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its context.
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by validating the API key, loading a system prompt from a specified file path, and setting up the appropriate LLM client (ChatGoogleGenerativeAI, ChatOpenAI, or ChatOllama) based on the `model_name` and optional `base_url`. It raises a ValueError if the API key is missing or if a required environment variable (SCADSLLM_URL) is not set for custom models, and a FileNotFoundError if the prompt file is not found.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **prompt_file_path** (`str`): The file path to a text file containing the system prompt that will be used for all LLM interactions.
        - **model_name** (`str`): The identifier for the LLM model to be used, defaulting to 'gemini-2.5-pro'. This parameter dictates which underlying LLM client (e.g., Google, OpenAI, Ollama) is instantiated.
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, primarily used for Ollama or other OpenAI-compatible APIs. If not provided and an Ollama model is selected, it defaults to OLLAMA_BASE_URL.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method performs a synchronous call to the initialized LLM with a given user input. It constructs a list of messages including the class's system prompt and the user's message, then invokes the LLM and returns its content. The method includes logging for the call status and handles potential exceptions during the LLM interaction, returning None in case of an error.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:*
            - **content** (`str`): The textual response content from the LLM, or None if an error occurs during the call.
        *   **Usage:** Calls: This method calls SystemMessage and HumanMessage to construct the message payload, then invokes the self.llm object, and uses logging.info and logging.error for operational status.
        Called By: This method is not explicitly called by any other functions or methods within the provided context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method initiates a streaming interaction with the configured LLM, yielding chunks of the response as they become available. It prepares the messages with the system prompt and user input, then calls the LLM's stream method. Each chunk's content is yielded, and comprehensive error handling is included to log and yield an error message if an exception occurs during the streaming process.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message for which a streaming response is desired from the LLM.
        *   *Returns:*
            - **content** (`str`): A generator that yields chunks of the LLM's response content as strings. In case of an error, it yields a descriptive error message string.
        *   **Usage:** Calls: This method calls SystemMessage and HumanMessage to construct the message payload, then initiates a stream from the self.llm object, and uses logging.info and logging.error for operational status.
        Called By: This method is not explicitly called by any other functions or methods within the provided context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to comprehensively extract and consolidate fundamental project information from various common project files and a repository URL. It initializes a structured dictionary to hold project overview and installation details, using placeholder values. Through a series of private parsing methods, it intelligently processes pyproject.toml, requirements.txt, and README files, prioritizing information sources and handling potential encoding issues or missing data. The class provides a single public interface, extrahiere_info, to orchestrate this extraction, making it a central utility for gathering project metadata.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components within the provided context.
*   **Dependencies:** The class relies on external modules such as re for regular expressions, os for path manipulation, and tomllib for parsing TOML files.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjektInfoExtractor instance by setting a constant INFO_NICHT_GEFUNDEN string and an info dictionary. This info dictionary serves as a structured container for extracted project details, pre-filled with the "Information not found" placeholder for all fields.
    *   *Parameters:* *None*
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content)`
        *   *Description:* This private helper method is responsible for sanitizing string content by removing null bytes (\x00). Null bytes can appear due to encoding errors, such as reading a UTF-16 encoded file as UTF-8. The method checks if the content is empty and returns an empty string if so; otherwise, it performs the replacement.
        *   *Parameters:*
            - **content** (`str`): The string content to be cleaned.
        *   *Returns:*
            - **""** (`str`): The content string with all null bytes removed.
        *   **Usage:** Calls: This method does not explicitly call other methods, classes, or functions from the provided imports or within the class itself, beyond basic string operations.
        Called By: This method is called by _parse_readme, _parse_toml, and _parse_requirements.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches a list of file objects for a file whose path matches any of the provided patterns. The search is case-insensitive, comparing the lowercased file path suffix against lowercased patterns. It returns the first matching file object found or None if no match is made.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of string patterns to match against file paths.
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have a path attribute.
        *   *Returns:*
            - **""** (`Optional[Any]`): The first file object that matches one of the patterns, or None if no match is found.
        *   **Usage:** Calls: This method does not explicitly call other methods, classes, or functions from the provided imports or within the class itself, beyond basic string operations.
        Called By: This method is called by extrahiere_info.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private method extracts content from a Markdown string that appears under a level 2 heading (##). It constructs a regular expression pattern using a list of keywords to identify the target heading. The method then captures all text following the matched heading up to the next level 2 heading or the end of the document, returning the stripped content or None if no match is found.
        *   *Parameters:*
            - **inhalt** (`str`): The Markdown content string to parse.
            - **keywords** (`List[str]`): A list of keywords to match against Markdown H2 headings.
        *   *Returns:*
            - **""** (`Optional[str]`): The stripped string content found under the specified Markdown H2 heading, or None.
        *   **Usage:** Calls: This method calls re.compile, re.escape, re.IGNORECASE, and re.DOTALL from the re module.
        Called By: This method is called by _parse_readme.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This private method parses the content of a README file to extract various project details and populate the self.info dictionary. It first cleans the content using _clean_content. It then attempts to find the project title and a fallback description using regular expressions. For other sections like key features, tech stack, status, installation instructions, and quick start guide, it leverages _extrahiere_sektion_aus_markdown with specific keyword lists. Information is only updated if the corresponding field in self.info is still set to INFO_NICHT_GEFUNDEN.
        *   *Parameters:*
            - **inhalt** (`str`): The string content of the README file.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls _clean_content, _extrahiere_sektion_aus_markdown, and re.search.
        Called By: This method is called by extrahiere_info.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project name, description, and dependencies. It first cleans the content using _clean_content. It checks for the availability of the tomllib module and prints a warning if it's not installed. If tomllib is available, it attempts to load the TOML content and extract relevant project data, updating the self.info dictionary. It includes error handling for TOMLDecodeError.
        *   *Parameters:*
            - **inhalt** (`str`): The string content of the pyproject.toml file.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls _clean_content, tomllib.loads, tomllib.TOMLDecodeError, and print.
        Called By: This method is called by extrahiere_info.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This private method parses the content of a requirements.txt file to extract project dependencies. It first cleans the content using _clean_content. It only proceeds to extract dependencies if the dependencies field in self.info is still marked as INFO_NICHT_GEFUNDEN, indicating that dependencies were not already found from a pyproject.toml file. It filters out empty lines and comments before storing the stripped dependency lines.
        *   *Parameters:*
            - **inhalt** (`str`): The string content of the requirements.txt file.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls _clean_content.
        Called By: This method is called by extrahiere_info.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This public method orchestrates the entire process of extracting project information from a given list of file objects and a repository URL. It first uses _finde_datei to locate README, pyproject.toml, and requirements.txt files. It then parses these files in a specific order of priority: pyproject.toml, then requirements.txt, and finally README.md, ensuring that information from higher-priority files (like TOML for dependencies) is not overwritten by lower-priority ones. Finally, it formats the extracted dependencies and attempts to derive a project title from the repository URL if no title was found in the files, returning the complete self.info dictionary.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have path and content attributes.
            - **repo_url** (`str`): The URL of the repository, used as a fallback for the project title.
        *   *Returns:*
            - **""** (`Dict[str, Any]`): A dictionary containing all extracted project information.
        *   **Usage:** Calls: This method calls _finde_datei, _parse_toml, _parse_requirements, _parse_readme, os.path.basename, and str.removesuffix.
        Called By: This method is not called by any other methods within the provided context.

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function, make_safe_dot, processes a NetworkX directed graph to prepare it for DOT file generation. It achieves this by creating a copy of the input graph and relabeling all its nodes with generic, safe identifiers (e.g., 'n0', 'n1', 'n2'). The original node names are preserved by storing them as 'label' attributes on the newly relabeled nodes. Finally, the function writes this modified graph, suitable for DOT visualization, to the specified output file path using nx.drawing.nx_pydot.write_dot.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The input NetworkX directed graph whose nodes need to be made safe for DOT representation.
    - **out_path** (`str`): The file path where the safe DOT representation of the graph will be written.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo)`
*   **Description:** This function builds a call graph for Python files within a given Git repository. It first identifies all 'self-written' functions by parsing the Abstract Syntax Trees (ASTs) of each Python file. Subsequently, it constructs a directed graph using the NetworkX library, where nodes represent these identified functions and edges indicate calls between them, ensuring only calls between 'self-written' functions are included.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which Python files and their contents will be retrieved to build the call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between 'self-written' functions found within the repository.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST NodeVisitor designed to construct a directed call graph for Python source code. It systematically traverses the Abstract Syntax Tree (AST) of a given file, identifying function and class definitions, import statements, and function calls. The class resolves function names, including those originating from imports and within class scopes, to generate fully qualified identifiers. It maintains internal state regarding the current file, class, and function to accurately map call relationships and definitions, ultimately populating a NetworkX graph and an edge dictionary that represent the call structure within the analyzed Python code.
*   **Instantiation:** This class is not explicitly instantiated by other functions or methods in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph instance by setting up essential attributes required for AST traversal and call graph construction. It stores the filename, initializes state trackers for the current function and class, and sets up dictionaries and sets to manage local definitions, import mappings, function identifiers, and the call graph edges. A NetworkX DiGraph is also initialized to store the graph structure.
    *   *Parameters:*
        - **filename** (`str`): The path to the Python source file being analyzed.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private method recursively traverses an Abstract Syntax Tree (AST) node to extract the full dotted name components of a function or attribute call. It specifically handles `ast.Call`, `ast.Name`, and `ast.Attribute` nodes, building a list of name parts from the innermost component outwards. This method is crucial for deconstructing complex call expressions into their constituent identifiers, which are then used for resolution.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a call, name, or attribute to be recursively processed.
        *   *Returns:*
            - **parts** (`list[str]`): A list of string components representing the dotted name of the call target, e.g., ['pkg', 'mod', 'Class', 'method'].
        *   **Usage:** Calls: This method does not explicitly call any other methods or functions.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private method takes a list of potential callee names, each represented as a list of name parts, and resolves them into fully qualified names. It applies a resolution strategy that prioritizes local definitions, then checks the `import_mapping`, and finally constructs a full name based on the current file and class context. This process is essential for converting raw AST-extracted names into canonical identifiers suitable for the call graph.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains string components of a callee's name.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved, fully qualified callee names.
        *   **Usage:** Calls: This method does not explicitly call any other methods or functions.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This private method constructs a fully qualified name for a given base name, incorporating the filename and an optional class name. The resulting string provides a unique identifier for functions or methods within the context of the entire project. This is crucial for distinguishing between global functions and class methods, ensuring unique nodes in the call graph.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method (e.g., 'my_function').
            - **class_name** (`str | None`): The name of the class if the entity is a method, otherwise None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name (e.g., 'filename::ClassName::methodName').
        *   **Usage:** Calls: This method does not explicitly call any other methods or functions.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private method determines the fully qualified name of the currently active function or, if no function is active, indicates the global scope. It checks the `current_function` attribute and falls back to a filename-based identifier or a generic global scope identifier. This method is used to identify the source of a call when processing `ast.Call` nodes, providing the 'from' part of a call graph edge.
        *   *Parameters:* *None*
        *   *Returns:*
            - **caller_name** (`str`): The fully qualified name of the current caller or '<global-scope>'.
        *   **Usage:** Calls: This method does not explicitly call any other methods or functions.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method overrides the `ast.NodeVisitor` method to process `ast.Import` nodes. It iterates through the aliases defined in the import statement, extracting both the original module name and any assigned alias. These mappings are then stored in the `import_mapping` dictionary, which is later used to resolve imported function calls to their canonical module paths. After processing the import, it calls `generic_visit` to continue AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement (e.g., `import os as my_os`).
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.generic_visit` to continue AST traversal.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method overrides the `ast.NodeVisitor` method to process `ast.ImportFrom` nodes. It extracts the base module name from which entities are imported and then maps each imported name (and its alias) to this module in the `import_mapping` dictionary. This is crucial for correctly resolving calls to functions or classes that are imported using `from ... import ...` statements, ensuring their full path is known.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method does not explicitly call any other methods or functions.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method overrides the `ast.NodeVisitor` method to process `ast.ClassDef` nodes. It temporarily updates the `current_class` attribute to the name of the class being visited, which is essential for correctly constructing fully qualified names for methods defined within that class. After traversing the class body, it restores the `current_class` to its previous state, ensuring proper scope management during AST traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.generic_visit` to continue AST traversal.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method overrides the `ast.NodeVisitor` method to process `ast.FunctionDef` nodes. It constructs the fully qualified name of the function using `_make_full_name`, registers this name in `local_defs`, and adds it as a node to the `graph`. It then updates `current_function` to reflect the current scope for any nested calls or definitions. After visiting the function's body, it restores the `current_function` to its previous state and adds the function to the `function_set`."
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self._make_full_name`, `self.graph.add_node`, and `self.generic_visit` to continue AST traversal.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method overrides the `ast.NodeVisitor` method to process `ast.AsyncFunctionDef` nodes. For the purpose of call graph construction, asynchronous function definitions are treated identically to regular function definitions. Therefore, this method simply delegates its processing to the `visit_FunctionDef` method, ensuring consistent handling of both synchronous and asynchronous function declarations.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.visit_FunctionDef` to process the asynchronous function definition.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method overrides the `ast.NodeVisitor` method to process `ast.Call` nodes, which represent function calls in the source code. It first identifies the caller using `_current_caller`, then extracts the callee's name components using `_recursive_call`, and finally resolves the callee's full name using `_resolve_all_callee_names`. If a callee is successfully resolved, an edge is added from the caller to the callee in the `edges` dictionary, effectively building the call graph. The method then continues generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function call.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self._current_caller`, `self._recursive_call`, `self._resolve_all_callee_names`, and `self.generic_visit` to continue AST traversal.
        Called By: This method is not explicitly called by other functions or methods in the provided context.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method overrides the `ast.NodeVisitor` method to handle `ast.If` nodes. It specifically checks for the `if __name__ == "__main__":` block, which typically marks the entry point of a script. When such a block is identified, it temporarily sets the `current_function` to "<main_block>" to correctly attribute any calls made within this primary execution scope. For all other `if` statements, it simply proceeds with the generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing an if statement.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.generic_visit` to continue AST traversal.
        Called By: This method is not explicitly called by other functions or methods in the provided context.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content)`
*   **Description:** The `wrap_cdata` function takes a single string argument, `content`, and encapsulates it within XML CDATA tags. It constructs a new string that starts with "<![CDATA[\n", inserts the provided content, and ends with "\n]]>". This process is typically used to prevent XML parsers from interpreting special characters within the content as markup, ensuring the content is treated as raw character data.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped within CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A new string containing the original content enclosed within CDATA tags.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs, image_list)`
*   **Description:** This function processes a list of output objects, typically from a Jupyter notebook execution, to extract their content. It iterates through each output, handling different types such as display data, execution results, streams, and errors. For image data (PNG or JPEG), it decodes Base64 strings, stores them in a provided list, and inserts an XML-like placeholder into the main output. Textual content and formatted error messages are directly appended to the result list.
*   **Parameters:**
    - **outputs** (`iterable`): An iterable of output objects, likely from a Jupyter notebook, containing various types of data like text, images, or errors.
    - **image_list** (`list[dict[str, str]]`): A list that is modified in-place to store dictionaries representing extracted image data. Each dictionary contains the 'mime_type' and the Base64 'data' string of an image.
*   **Returns:**
    - **extracted_xml_snippets** (`list[str]`): A list of strings, where each string is either plain text extracted from the outputs, an XML-like placeholder for an image, or a formatted error message.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type)`
*   **Description:** This function processes image data based on a given MIME type. It checks for the `mime_type` within an externally accessible `data` dictionary. If the `mime_type` is present, it retrieves a base64 encoded string, sanitizes it by removing newlines, and then stores this image information into an externally managed `image_list`. The function returns a formatted placeholder string upon successful processing, or an error message if decoding fails. If the `mime_type` is not found in `data`, the function returns `None`.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed, used as a key to access image data from an external source.
*   **Returns:**
    - **image_placeholder_string** (`str`): A string formatted as an image placeholder, including the assigned index and MIME type, indicating successful processing and storage of the image data in an external list.
    - **error_message_string** (`str`): An error message string, returned if an exception occurs during the processing or decoding of the image data.
    - **None** (`NoneType`): Indicates that the specified MIME type was not found in the external `data` dictionary, and no image processing occurred.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content)`
*   **Description:** This function takes the raw content of a Jupyter notebook file as a string and converts it into a structured XML representation. It parses the notebook, iterates through its cells, and generates XML elements for markdown and code cells. For code cells, it also processes and includes their outputs, extracting any embedded images. If the input content cannot be parsed as a valid JSON/Notebook, it returns an error message.
*   **Parameters:**
    - **file_content** (`str`): The raw string content of a Jupyter notebook file.
*   **Returns:**
    - **xml_representation** (`str`): A string containing the XML representation of the notebook, or an error message if parsing fails.
    - **extracted_images** (`list`): A list of extracted image data or paths found within the notebook outputs.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files)`
*   **Description:** This function processes a collection of repository files, specifically filtering for Jupyter notebook files. It iterates through each identified notebook, converting its content into an XML representation and extracting any associated images. The function utilizes a helper function, 'convert_notebook_to_xml', for the conversion process. It logs information about the number of notebooks found and the processing status of each. The final output is a dictionary mapping each notebook's path to its generated XML and extracted images.
*   **Parameters:**
    - **repo_files** (`iterable`): An iterable collection of file objects from a repository. Each object is expected to have a 'path' attribute (string) ending with '.ipynb' and a 'content' attribute containing the notebook's data.
*   **Returns:**
    - **results** (`dict`): A dictionary where keys are the paths of the processed Jupyter notebook files (string) and values are dictionaries. Each inner dictionary contains two keys: 'xml' (string, representing the XML conversion of the notebook) and 'images' (list, containing extracted image data or paths).
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, providing a structured way to access its metadata and content. It implements lazy loading for the Git blob object, file content, and size, ensuring that these potentially heavy operations are only performed when explicitly requested. The class offers properties to retrieve file details, its content, and an example analysis function for word counting, along with a utility method to convert its data into a dictionary.
*   **Instantiation:** The class is not explicitly listed as being instantiated by any other components in the provided context.
*   **Dependencies:** The class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object by setting its file path and the Git tree object from which it originates. It also initializes internal attributes `_blob`, `_content`, and `_size` to `None` for lazy loading.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree-object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading of the Git blob object associated with the file. If the `_blob` attribute is `None`, it attempts to retrieve the blob from the `_tree` using the file's path. If the file is not found in the tree, it raises a `FileNotFoundError`.
        *   *Parameters:* *None*
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:** Calls: This method does not explicitly call any other functions or methods.
        Called By: This method is not explicitly called by any other functions or methods in the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading of the file's content. If the `_content` attribute is `None`, it accesses the `blob` property to get the Git blob, reads its data stream, and decodes it using UTF-8 with error ignoring. The decoded content is then stored and returned.
        *   *Parameters:* *None*
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:** Calls: This method does not explicitly call any other functions or methods.
        Called By: This method is not explicitly called by any other functions or methods in the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading of the file's size in bytes. If the `_size` attribute is `None`, it accesses the `blob` property to get the Git blob and retrieves its size. The size is then stored and returned.
        *   *Parameters:* *None*
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:** Calls: This method does not explicitly call any other functions or methods.
        Called By: This method is not explicitly called by any other functions or methods in the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function. It calculates and returns the total number of words in the file's content. It achieves this by accessing the `content` property, splitting the string by whitespace, and then counting the resulting elements.
        *   *Parameters:* *None*
        *   *Returns:*
            - **word_count** (`int`): The total number of words in the file content.
        *   **Usage:** Calls: This method does not explicitly call any other functions or methods.
        Called By: This method is not explicitly called by any other functions or methods in the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This special method provides a developer-friendly string representation of the `RepoFile` object. It returns a string formatted to show the class name and the file's path, making it useful for debugging and logging.
        *   *Parameters:* *None*
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:** Calls: This method does not explicitly call any other functions or methods.
        Called By: This method is not explicitly called by any other functions or methods in the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method converts the `RepoFile` object into a dictionary representation. It includes the file's path, name (basename), size, and type. Optionally, it can also include the file's content if `include_content` is set to `True`.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether to include the file's content in the dictionary. Defaults to `False`.
        *   *Returns:*
            - **file_data** (`dict`): A dictionary containing the file's metadata and optionally its content.
        *   **Usage:** Calls: This method does not explicitly call any other functions or methods.
        Called By: This method is not explicitly called by any other functions or methods in the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with remote Git repositories. It handles the cloning of a specified repository into a temporary local directory, manages the lifecycle of this temporary directory through context management (__enter__ and __exit__), and offers methods to retrieve and structure the repository's files. Its primary purpose is to abstract away the complexities of Git operations and temporary file system management, allowing other components to easily access repository contents.
*   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
*   **Dependencies:** This class depends on `tempfile` for temporary directory creation, `git.Repo` and `git.GitCommandError` from the GitPython library for Git operations, and `logging` for informational messages. It also implicitly depends on a `RepoFile` class, which is not defined in the provided source but is used for file representation.
*   **Constructor:**
    *   *Description:* Initializes the GitRepository object by cloning a remote Git repository into a temporary directory. It sets up instance attributes like `repo_url`, `temp_dir`, `repo` (the GitPython Repo object), `latest_commit`, and `commit_tree`. It handles potential `GitCommandError` during cloning by cleaning up the temporary directory and raising a `RuntimeError`.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It utilizes the `git.ls_files()` command to obtain a list of file paths. For each path, it instantiates a `RepoFile` object, which is then stored in the `self.files` attribute. Finally, the method returns this comprehensive list of `RepoFile` instances.
        *   *Parameters:* *None*
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances, each representing a file in the repository.
        *   **Usage:** Calls: This method calls `self.repo.git.ls_files()` to list files and `RepoFile` to instantiate file objects.
        Called By: This method is not explicitly called by other methods in the provided context.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is responsible for cleaning up resources by deleting the temporary directory where the Git repository was cloned. It first checks if `self.temp_dir` is set, indicating an active temporary directory. If so, it prints a message and then sets `self.temp_dir` to `None`, effectively marking the directory for deletion and preventing further interaction with it. This ensures proper resource release.
        *   *Parameters:* *None*
        *   *Returns:* *None*
        *   **Usage:** Calls: This method does not explicitly call other methods or functions within its body, but it interacts with the file system implicitly by deleting the temporary directory.
        Called By: This method is called by `__init__` in case of a cloning error and by `__exit__` for context management.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This special method allows the `GitRepository` class to be used as a context manager, enabling its use within a `with` statement. When the `with` block is entered, this method is automatically invoked. Its sole purpose is to return the instance of the `GitRepository` itself, making it available as the target of the `as` clause in the `with` statement.
        *   *Parameters:* *None*
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository class, allowing it to be used within a 'with' statement.
        *   **Usage:** Calls: This method does not call any other methods or functions.
        Called By: This method is implicitly called when the `GitRepository` object is used in a `with` statement.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This special method is part of the context manager protocol and is automatically called when exiting a `with` statement, regardless of whether an exception occurred. Its primary responsibility is to ensure that the `close()` method is invoked, thereby cleaning up the temporary repository directory. The parameters `exc_type`, `exc_val`, and `exc_tb` provide information about any exception that might have occurred within the `with` block, though this method does not explicitly handle them.
        *   *Parameters:*
            - **exc_type** (`type | None`): The type of the exception, if one occurred.
            - **exc_val** (`Exception | None`): The exception instance, if one occurred.
            - **exc_tb** (`traceback | None`): The traceback object, if an exception occurred.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.close()` to perform cleanup.
        Called By: This method is implicitly called when exiting a `with` statement that uses a `GitRepository` object.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method constructs a hierarchical tree representation of the files within the repository. It first ensures that all files are loaded by calling `get_all_files()` if the `self.files` attribute is empty. It then iterates through each `RepoFile` object, splitting its path to dynamically build a nested dictionary structure that accurately represents the directories and files. Files are appended at their respective positions in the tree, and their content can optionally be included based on the `include_content` flag.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether the content of the files should be included in the dictionary representation. Defaults to `False`.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the file tree, with 'name', 'type', and 'children' keys for directories, and file-specific data for files.
        *   **Usage:** Calls: This method calls `self.get_all_files()` to populate the file list and `file_obj.to_dict()` to convert `RepoFile` objects into dictionary format.
        Called By: This method is not explicitly called by other methods in the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare the number of JSON tokens against TOON tokens. It calculates and displays a savings percentage in the chart's title. The chart includes labels, colors, a title, y-axis label, and grid lines. Token counts are displayed above each bar, and the final chart is saved to a specified output path before closing the plot.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings to be displayed in the chart title.
    - **output_path** (`str`): The file path where the generated chart image will be saved.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time for an operation, specifically adjusting for simulated rate-limiting sleep durations. It first determines the total duration between a start and end time. If the `model_name` does not begin with 'gemini-', the total duration is returned without adjustment. For 'gemini-' models, it calculates the number of batches based on `total_items` and `batch_size`, then estimates total sleep time (61 seconds per batch, excluding the first). This estimated sleep time is subtracted from the total duration to yield the net time, ensuring the result is not negative.
*   **Parameters:**
    - **start_time** (`float`): The numeric start timestamp of the operation, typically in seconds.
    - **end_time** (`float`): The numeric end timestamp of the operation, typically in seconds.
    - **total_items** (`int`): The total number of items processed during the operation.
    - **batch_size** (`int`): The maximum number of items processed in a single batch.
    - **model_name** (`str`): The name of the model used for processing, which determines if rate-limiting sleep adjustments are applied.
*   **Returns:**
    - **net_time** (`float`): The calculated net duration of the operation in seconds. This duration is adjusted by subtracting simulated rate-limiting sleep times if the model is 'gemini-', otherwise it is the total duration. Returns 0 if total items are 0 or if the calculated net time is negative.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing a GitHub repository and generating a detailed report using multiple Large Language Models (LLMs). It begins by extracting API keys and model configurations based on the provided input. It then clones a specified GitHub repository, extracts basic project information, constructs a file tree, and performs a relationship analysis to understand calls and instantiations within the codebase. An Abstract Syntax Tree (AST) schema is generated and enriched with the relationship data. The function prepares structured inputs for a Helper LLM, which analyzes individual functions and classes, and then for a Main LLM, which synthesizes the collected information into a final report. Finally, it saves the generated report and associated token savings metrics, including a chart.
*   **Parameters:**
    - **input** (`str`): The initial user input, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs ('scadsllm_base_url', 'ollama').
    - **model_names** (`dict`): A dictionary specifying the names of the helper and main LLM models to be used (e.g., 'helper', 'main').
    - **status_callback** (`callable`): An optional callback function used to provide status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM, detailing the repository analysis.
    - **metrics** (`dict`): A dictionary containing performance metrics such as helper LLM time, main LLM time, total active time, model names, and token savings data.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function, `update_status`, is designed to process and log a given message. It first checks if a `status_callback` function is available and, if so, invokes it with the provided message. Subsequently, it logs the message at the INFO level using the `logging` module. The primary purpose is to provide a mechanism for both external status updates and internal logging.
*   **Parameters:**
    - **msg** (`Any`): The message string or object to be processed and logged.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback)`
*   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks within a Git repository using a Large Language Model (LLM). It begins by extracting a repository URL from the input, then clones the repository. It processes the notebooks, extracts basic project information, and initializes an LLM based on the specified model and API keys. The function then iterates through each identified notebook, constructs a payload (including text and base64-encoded images) for the LLM, and generates a report for each. Finally, it concatenates all individual reports into a single markdown file, saves it to a timestamped file in a 'result' directory, and returns the final report along with performance metrics.
*   **Parameters:**
    - **input** (`str`): The input string, expected to contain a URL to a Git repository.
    - **api_keys** (`dict`): A dictionary containing API keys for various LLM providers (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
    - **model** (`str`): The name of the LLM model to be used for analysis (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`callable | None`): An optional callback function to provide real-time status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final concatenated markdown report generated by the LLM for all processed notebooks.
    - **metrics** (`dict`): A dictionary containing performance metrics such as 'helper_time', 'main_time', 'total_time', 'helper_model', 'main_model', 'json_tokens', 'toon_tokens', and 'savings_percent'.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a payload suitable for the Gemini API, combining textual context with embedded images. It takes basic project information, the notebook path, XML content representing the notebook structure, and image data. It first serializes basic information into a JSON string. Then, it parses the provided XML content, identifying image placeholders using a regular expression. For each placeholder, it extracts the corresponding base64-encoded image data from the `images` list and inserts it into the payload alongside the surrounding text segments. The function returns a list of dictionaries, where each dictionary represents either a text block or an image URL, structured for a multi-modal model input.
*   **Parameters:**
    - **basic_info** (`object`): A dictionary or object containing basic project information to be included in the payload context.
    - **nb_path** (`str`): The file path of the current notebook, included in the payload context.
    - **xml_content** (`str`): The XML string representing the structure and content of the notebook, potentially containing image placeholders.
    - **images** (`list`): A list of dictionaries, where each dictionary contains image data, typically with a 'data' key holding a base64 string and a 'mime' key for the MIME type.
*   **Returns:**
    - **payload_content** (`list`): A list of dictionaries, each representing a content part for a multi-modal model. Each dictionary has a 'type' key ('text' or 'image_url') and corresponding content.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file system path into a Python module path string. It first attempts to calculate the relative path from a specified project root. If that fails, it uses the base name of the file. It then removes the '.py' extension if present, replaces path separators with dots, and finally adjusts for '__init__.py' files by removing the '.__init__' suffix to represent their parent package.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to build a comprehensive call graph. It identifies all Python files, collects definitions of functions, methods, and classes, and then resolves calls between these entities. The class provides methods to initiate the analysis and retrieve the raw relationships in a structured format, facilitating understanding of code dependencies and interactions within a project.
*   **Instantiation:** No explicit instantiations are provided in the input context.
*   **Dependencies:** The class depends on `os` for file system operations, `ast` for parsing Python code, `logging` for error reporting, and `collections.defaultdict` for managing graph data structures. It also implicitly depends on `path_to_module` and `CallResolverVisitor` which are not defined in the provided source but are used.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer instance by setting the project's root directory. It sets up internal data structures such as dictionaries for storing definitions and file ASTs, a defaultdict for the call graph, and a predefined set of directories to ignore during file system traversal.
    *   *Parameters:*
        - **project_root** (`str`): The absolute path to the root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect function, method, and class definitions. Subsequently, it iterates again to resolve calls made within these files, populating the internal call graph. Finally, it clears the stored file ASTs to free up memory and returns the generated call graph.
        *   *Parameters:* *None*
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:** Calls: This method calls `_find_py_files` to locate Python files, `_collect_definitions` to gather entity definitions, and `_resolve_calls` to build the call graph.
        Called By: No explicit callers are provided for this method in the input context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* This method processes the internal `call_graph` to generate a structured representation of outgoing and incoming relationships between code entities. It iterates through the call graph, extracting caller and callee identifiers, and populates two defaultdicts: one for outgoing calls (what an entity calls) and one for incoming calls (what calls an entity). The final output is a dictionary containing sorted lists of these relationships.
        *   *Parameters:* *None*
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, 'outgoing' and 'incoming', each mapping to a dictionary where keys are entity identifiers and values are sorted lists of related entity identifiers.
        *   **Usage:** Calls: No explicit calls are made to other methods or functions within this method.
        Called By: No explicit callers are provided for this method in the input context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private helper method is responsible for recursively traversing the project directory to locate all Python files. It uses `os.walk` to navigate the file system, explicitly skipping directories specified in `self.ignore_dirs`. For each file found, it checks if it ends with `.py` and, if so, adds its absolute path to a list of Python files.
        *   *Parameters:* *None*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found within the project root, excluding ignored directories.
        *   **Usage:** Calls: This method calls `os.walk` to traverse directories and `os.path.join` to construct file paths.
        Called By: This method is called by `analyze`.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method reads the source code of a given Python file, parses it into an Abstract Syntax Tree (AST), and then walks the AST to identify function, method, and class definitions. It stores the AST in `self.file_asts` and populates `self.definitions` with information about each discovered entity, including its file path, line number, and type (function, method, or class). Error handling is included for file reading or parsing issues.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file being analyzed for definitions.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `open` to read file content, `ast.parse` to create an AST, `path_to_module` to convert a file path to a module path, `ast.walk` to traverse the AST, `isinstance` for type checking, `_get_parent` to find a node's parent, and `logging.error` for error reporting.
        Called By: This method is called by `analyze`.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This private helper method traverses an Abstract Syntax Tree (AST) to find the immediate parent node of a given child node. It iterates through all nodes in the tree and then checks their direct children to identify if any child matches the provided node. If a match is found, the parent node is returned. If no parent is found (e.g., for the root node), it returns `None`.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent** (`ast.AST or None`): The parent AST node of the given `node`, or `None` if no parent is found.
        *   **Usage:** Calls: This method calls `ast.walk` to iterate through nodes and `ast.iter_child_nodes` to get children of a node.
        Called By: This method is called by `_collect_definitions`.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method takes a file path, retrieves its AST from `self.file_asts`, and then uses a `CallResolverVisitor` to identify all function, method, and class calls within that file. It then extends the `self.call_graph` with the resolved call information, mapping callees to a list of callers. It includes error handling for issues during call resolution.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose calls are to be resolved.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls `self.file_asts.get` to retrieve an AST, instantiates `CallResolverVisitor`, calls `resolver.visit` to process the AST, accesses `resolver.calls.items` to get resolved calls, and `logging.error` for error reporting.
        Called By: This method is called by `analyze`.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an ast.NodeVisitor subclass designed to traverse a Python Abstract Syntax Tree (AST) and identify all function and method calls within a given source file. It meticulously tracks the current module, class, and function scope to accurately resolve the fully qualified names of both callers and callees. The visitor maintains a scope for imports and instance_types for assigned objects, enabling it to resolve calls to imported functions, module-level functions, class methods, and methods on instantiated objects. Its primary output is a defaultdict (self.calls) that maps each resolved callee's qualified name to a list of detailed caller information, effectively building a call graph for the analyzed code.
*   **Instantiation:** The specific instantiation points for this class are not provided in the current context.
*   **Dependencies:** The class depends on ast for AST traversal, os for path manipulation, and collections.defaultdict for storing call relationships. It also implicitly relies on a path_to_module utility function, which is not part of the class but is used in its constructor.
*   **Constructor:**
    *   *Description:* This constructor initializes the CallResolverVisitor instance with essential path information and a dictionary of known definitions. It sets up internal state variables such as filepath, module_path, definitions, scope, instance_types, current_caller_name, current_class_name, and calls (a defaultdict to store call relationships). These attributes are crucial for tracking the current context during AST traversal and accumulating call data.
    *   *Parameters:*
        - **filepath** (`str`): The path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the project, used to derive the module path.
        - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) for resolution.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is part of the ast.NodeVisitor pattern and is invoked when a class definition (ast.ClassDef) is encountered. It temporarily updates self.current_class_name to the name of the current class being visited. After recursively visiting the nodes within the class definition, it restores the current_class_name to its previous value, ensuring correct scope management during traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls self.generic_visit to continue the AST traversal.
        Called By: This method is implicitly called by the ast.NodeVisitor framework when a ClassDef node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles ast.FunctionDef nodes, which represent function or method definitions. It constructs a full_identifier for the function, incorporating the module path and class name if applicable. This identifier is then set as self.current_caller_name to track the context of subsequent calls within this function. After visiting the function's body, it restores the current_caller_name to its previous state.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls self.generic_visit to continue the AST traversal.
        Called By: This method is implicitly called by the ast.NodeVisitor framework when a FunctionDef node is encountered during AST traversal.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method processes ast.Call nodes, which represent function or method calls. It attempts to resolve the qualified name of the called entity using _resolve_call_qname. If the callee is successfully resolved and exists in the definitions, it records the call by appending caller information (file, line number, caller identifier, and caller type) to a defaultdict keyed by the callee's qualified name. This mechanism is central to building the call graph.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing the function or method call.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls self._resolve_call_qname to determine the qualified name of the called function or method, and self.generic_visit for continued AST traversal.
        Called By: This method is implicitly called by the ast.NodeVisitor framework when a Call node is encountered during AST traversal.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method handles ast.Import nodes, which represent import module [as alias] statements. It iterates through the imported names and their aliases, storing them in self.scope. The scope dictionary maps the local name (alias or original name) to the fully qualified module name, which is crucial for resolving subsequent calls to imported modules or functions.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing the import statement.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls self.generic_visit to continue the AST traversal.
        Called By: This method is implicitly called by the ast.NodeVisitor framework when an Import node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes ast.ImportFrom nodes, which represent from module import name [as alias] statements. It determines the full module path, considering relative imports (node.level). For each imported name, it constructs its fully qualified path and stores it in self.scope, mapping the local name (alias or original name) to this qualified path. This allows for accurate resolution of imported functions or classes.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing the from ... import ... statement.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls self.generic_visit to continue the AST traversal.
        Called By: This method is implicitly called by the ast.NodeVisitor framework when an ImportFrom node is encountered during AST traversal.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method handles ast.Assign nodes, specifically looking for assignments where the right-hand side is a call to a class constructor (e.g., x = MyClass()). If such an assignment is found and the class name can be resolved via self.scope and exists in self.definitions, it records the type of the assigned variable in self.instance_types. This helps in resolving method calls on instances later (e.g., x.method()).
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing the assignment statement.
        *   *Returns:* *None*
        *   **Usage:** Calls: This method calls self.generic_visit to continue the AST traversal.
        Called By: This method is implicitly called by the ast.NodeVisitor framework when an Assign node is encountered during AST traversal.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method attempts to determine the fully qualified name (qname) of a function or method being called, given its AST node (func_node). It handles two main cases: direct name calls (ast.Name) and attribute calls on an object (ast.Attribute). For ast.Name, it checks self.scope and then local module definitions. For ast.Attribute, it tries to resolve the instance type from self.instance_types or the module from self.scope to construct the qualified method name.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., ast.Name or ast.Attribute).
        *   *Returns:*
            - **qualified_name** (`str | None`): The fully qualified name of the callable if resolved, otherwise None.
        *   **Usage:** Calls: This method does not explicitly call other methods within the class, but it accesses self.scope, self.definitions, and self.instance_types.
        Called By: This method is called by self.visit_Call to resolve the qualified name of the callee.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** This function encrypts a provided string using a pre-configured `cipher_suite` object. It first performs a guard clause, returning the original text if the input text is empty or if the `cipher_suite` is not initialized. If encryption proceeds, the text is stripped of leading/trailing whitespace, encoded to UTF-8 bytes, encrypted, and then decoded back into a string. The function ensures that only valid text is processed for encryption.
*   **Parameters:**
    - **text** (`str`): The string to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string, or the original string if encryption is skipped due to empty input or uninitialized cipher_suite.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** This function attempts to decrypt a given string using a global or externally defined 'cipher_suite' object. It first checks if the input text or the cipher_suite itself is empty or falsy, returning the original text immediately in such cases. If both are valid, it proceeds to strip whitespace from the text, encode it to bytes, decrypt it using 'cipher_suite.decrypt', and then decode the result back into a string. In the event of any exception during the decryption process, the function gracefully falls back to returning the original, unencrypted text.
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted string, or the original string if decryption is not performed or an error occurs during the process.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function is responsible for inserting a new user record into the database. It takes a username, name, and plain-text password as input. It constructs a user dictionary, hashes the provided password using `stauth.Hasher.hash`, and initializes API key fields as empty strings. Finally, it uses `dbusers.insert_one` to store the user and returns the unique identifier of the newly inserted document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which will be used as the document's '_id'.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The '_id' of the newly inserted user document, which corresponds to the provided username.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is designed to retrieve all user records from a database collection named `dbusers`. It executes a `find()` operation on this collection, which typically fetches all documents. The results are then cast into a Python list before being returned.
*   **Parameters:** *None*
*   **Returns:**
    - **users** (`list`): A list containing all user documents retrieved from the `dbusers` collection.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** The `fetch_user` function is designed to retrieve a single user document from a database collection, presumably named `dbusers`. It takes a username as input and uses it to query the database for a document where the `_id` field matches the provided username. The function returns the first matching document found or `None` if no user with that username exists.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be retrieved from the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if found, otherwise `None`.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username, new_name)`
*   **Description:** This function updates the 'name' field for a specific user in the 'dbusers' collection. It identifies the user by their '_id', which is expected to be the username. The function sets the 'name' field to the provided new name. It returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose name is to be updated. This is used to match the '_id' field in the database.
    - **new_name** (`str`): The new name to set for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function updates a user's Gemini API key in a database. It takes a username and the new Gemini API key as input. The API key is first stripped of whitespace and then encrypted using an external `encrypt_text` utility. Finally, it updates the `gemini_api_key` field for the specified user in the `dbusers` collection. The function returns the count of modified documents.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose Gemini API key is to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored for the user, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified in the database by the update operation. Typically 0 or 1.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username, gpt_api_key)`
*   **Description:** This function updates a user's GPT API key in the database. It first encrypts the provided API key, ensuring any leading or trailing whitespace is removed. Then, it uses the username to locate the corresponding user document in the `dbusers` collection and sets the `gpt_api_key` field to the newly encrypted value. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The username of the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be encrypted and stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function updates the 'ollama_base_url' for a specific user within a database. It takes a username and a new Ollama base URL as input. The function uses `dbusers.update_one` to locate the user by their username (acting as the document's `_id`) and sets the 'ollama_base_url' field to the provided URL, after stripping any leading or trailing whitespace. It returns an integer representing the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama URL needs to be updated. This is used as the `_id` for the database document.
    - **ollama_base_url** (`str`): The new base URL for Ollama to be associated with the specified user. This value is stripped of whitespace before being stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 indicates successful modification of the user's URL, 0 if no document matched or no change was made.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username, opensrc_api_key)`
*   **Description:** This function updates a user's Open Source API key in the database. It takes a username and the new API key as input. The provided API key is first stripped of whitespace and then encrypted before being stored. The function then updates the 'opensrc_api_key' field for the specified user in the 'dbusers' collection. It returns the count of documents that were modified by this update operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source API key is to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be stored, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username, opensrc_base_url)`
*   **Description:** This function updates a user's 'opensrc_base_url' in the database. It takes a username and a new URL as input. The function performs an 'update_one' operation on the 'dbusers' collection, identifying the user by their username (which serves as the '_id'). The provided 'opensrc_base_url' is stripped of leading/trailing whitespace before being stored. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose opensrc URL is to be updated. This is used as the document's '_id'.
    - **opensrc_base_url** (`str`): The new base URL for opensrc to be associated with the user. This string will have leading/trailing whitespace removed before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. Typically 0 or 1.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** This function retrieves a user's Gemini API key from a database. It queries the 'dbusers' collection using the provided username as the document ID. If a user document is found, it extracts and returns the 'gemini_api_key' field. If no user is found, or the key is not present, it returns None.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the Gemini API key.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key associated with the username, or None if the user or key is not found.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** This function retrieves the Ollama base URL for a specified user from a database. It queries the 'dbusers' collection, using the provided username as the document's identifier. The function specifically fetches only the 'ollama_base_url' field. If a user document is found, it returns the value of 'ollama_base_url'; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL associated with the username, or None if the user is not found in the database.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username)`
*   **Description:** This function is designed to retrieve a user's GPT API key from a database. It takes a username as input and queries a 'dbusers' collection to find a matching user document. If a user is found, the function extracts the 'gpt_api_key' field from the document. The function returns the API key as a string if it exists, otherwise it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the user, or None if the user or key is not found.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username)`
*   **Description:** This function retrieves the 'opensrc_api_key' for a specified username from a database. It queries the 'dbusers' collection, looking for a document that matches the provided username. The function is designed to specifically fetch only the 'opensrc_api_key' field. If a user is found and has an 'opensrc_api_key', that key is returned; otherwise, the function returns None.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the opensrc API key.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The opensrc API key associated with the username, or None if the user is not found or the key does not exist.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username)`
*   **Description:** This function retrieves the 'opensrc_base_url' for a specified user from a database collection. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided 'username'. If a user document is found, the function extracts and returns the value of the 'opensrc_base_url' field. If no user matching the 'username' is found in the collection, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The Open Source base URL associated with the user, or None if the user is not found in the database.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** This function is designed to remove a user record from a database collection. It takes a username as input, which is used as the unique identifier to locate the specific user document. The function executes a delete operation on the `dbusers` collection, targeting the document where the `_id` field matches the provided username. It then returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation, typically 0 or 1.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function retrieves and decrypts various API keys and base URLs associated with a given username from a database. It first queries for a user document using the provided username. If no user is found, the function returns a tuple of five None values. Otherwise, it extracts specific API keys (Gemini, GPT, open-source) and base URLs (Ollama, open-source), decrypting the keys as needed, and returns them as plain text strings.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user is not found.
    - **ollama_plain** (`str | None`): The Ollama base URL, or None if the user is not found.
    - **gpt_plain** (`str | None`): The decrypted GPT API key, or None if the user is not found.
    - **opensrc_plain** (`str | None`): The decrypted open-source API key, or None if the user is not found.
    - **opensrc_url** (`str | None`): The open-source base URL, or None if the user is not found.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username, chat_name)`
*   **Description:** This function creates a new chat entry in a database. It generates a unique identifier for the chat using UUID, records the provided username and chat name, and captures the current timestamp. The constructed chat dictionary is then inserted into the 'dbchats' collection. The function returns the unique ID of the newly inserted chat document.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (MongoDB _id) of the newly created chat entry.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username)`
*   **Description:** This function retrieves all chat records associated with a specific user from a database collection. It queries the `dbchats` collection for documents where the 'username' field matches the input `username`. The results are then sorted in ascending order based on their 'created_at' timestamp. Finally, the function returns these sorted chat records as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat records.
*   **Returns:**
    - **chats** (`list`): A list of chat documents associated with the specified username, sorted by creation date.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username, chat_name)`
*   **Description:** This function checks for the existence of a chat entry within the 'dbchats' collection. It queries the collection using a provided username and chat name. The function returns a boolean indicating whether a matching chat record was found.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked.
*   **Returns:**
    - **exists** (`bool`): True if a chat matching the provided username and chat name exists in the database, False otherwise.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
*   **Description:** This function renames a chat and all its associated exchanges within the database. It first updates the main chat entry in the 'dbchats' collection, changing the 'chat_name' from 'old_name' to 'new_name' for a specific 'username'. Subsequently, it updates all related message entries (exchanges) in the 'dbexchanges' collection, ensuring their 'chat_name' also reflects the 'new_name'. The function returns the count of documents modified during the initial chat entry rename operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The new desired name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified in the 'dbchats' collection during the chat entry rename operation.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time, json_tokens, toon_tokens, savings_percent)`
*   **Description:** This function `insert_exchange` is responsible for creating and storing a new exchange record in a database. It generates a unique identifier using `uuid.uuid4()` and constructs a dictionary containing various details such as the question, answer, feedback, user information, and performance metrics. A `created_at` timestamp is added using `datetime.now()`. The function then attempts to insert this record into the `dbexchanges` collection. If the insertion is successful, it returns the newly generated ID; otherwise, it catches any exceptions, prints an error message, and returns `None`.
*   **Parameters:**
    - **question** (`str`): The user's question in the exchange.
    - **answer** (`str`): The generated answer for the question.
    - **feedback** (`str`): The feedback provided for the exchange.
    - **username** (`str`): The username associated with the exchange.
    - **chat_name** (`str`): The name of the chat where the exchange occurred.
    - **helper_used** (`str`): An optional string indicating which helper model was used. Defaults to an empty string.
    - **main_used** (`str`): An optional string indicating which main model was used. Defaults to an empty string.
    - **total_time** (`str`): An optional string representing the total time taken for the exchange. Defaults to an empty string.
    - **helper_time** (`str`): An optional string representing the time taken by the helper model. Defaults to an empty string.
    - **main_time** (`str`): An optional string representing the time taken by the main model. Defaults to an empty string.
    - **json_tokens** (`int`): An optional integer representing the number of JSON tokens used. Defaults to 0.
    - **toon_tokens** (`int`): An optional integer representing the number of 'toon' tokens used. Defaults to 0.
    - **savings_percent** (`float`): An optional float representing the percentage of savings. Defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly inserted exchange record if the insertion is successful.
    - **None** (`NoneType`): Returned if an exception occurs during the database insertion process.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** This function retrieves all exchange records associated with a specific username from the `dbexchanges` collection. It queries the database using the provided username, sorts the results by their creation timestamp in ascending order, and then returns the collected exchanges as a list. The sorting is explicitly noted as important for display purposes.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records associated with the specified username, sorted by their 'created_at' timestamp in ascending order.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function retrieves a list of exchange documents from a database collection, `dbexchanges`. It filters these documents based on a specified username and chat name. The results are then sorted in ascending order by their `created_at` timestamp and returned as a list.
*   **Parameters:**
    - **username** (`str`): The username to filter the exchanges by.
    - **chat_name** (`str`): The name of the chat to filter the exchanges by.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents (likely dictionaries) that match the provided username and chat name, sorted by their creation time.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function updates the 'feedback' field for a specific exchange record in a database collection. It accepts an exchange identifier and an integer feedback value. The function performs an update operation on a single document matching the provided ID, setting its 'feedback' attribute. It then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange record to be updated in the database.
    - **feedback** (`int`): The integer value representing the feedback to be set for the exchange record.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 0 or 1.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function updates a specific exchange record in the database. It takes an exchange ID and a new feedback message, then uses the `dbexchanges` collection to find the document by its `_id` and set the `feedback_message` field. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange document to be updated.
    - **feedback_message** (`str`): The new feedback message to be set for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is called by no other functions.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function is designed to delete a single exchange record from the 'dbexchanges' collection based on a provided unique identifier. It takes an 'exchange_id' as input, which is used to locate the specific document. The function then executes a delete operation and returns the count of documents that were successfully removed, typically 0 or 1.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier string for the exchange document to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation. This will typically be 1 if a document matching the ID was found and deleted, or 0 if no matching document was found.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username, chat_name)`
*   **Description:** The `delete_full_chat` function is designed to completely remove a specific chat and all its associated message exchanges from the database. It operates in two main steps: first, it deletes all exchanges linked to the given username and chat name using `dbexchanges.delete_many`. Second, it removes the chat entry itself from the `dbchats` collection using `dbchats.delete_one`. This ensures data consistency by eradicating all related records. The function returns the count of chat documents successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted from the database. This is typically 1 if the chat was found and deleted, or 0 if it did not exist.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list)`
*   **Description:** This function processes a list of strings, likely representing paths or identifiers. For each string in the input list, it splits the string by the '/' character and extracts the last segment. The function then returns a new list containing these extracted base names, effectively cleaning them by removing any preceding path information.
*   **Parameters:**
    - **model_list** (`list[str]`): A list of strings, where each string may contain path-like separators (e.g., '/').
*   **Returns:**
    - **cleaned_names** (`list[str]`): A new list where each element is the last segment of the corresponding input string after splitting by '/'.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list, category_name)`
*   **Description:** This function filters a given list of models (`source_list`) based on a specified `category_name`. It retrieves a list of keywords associated with the `category_name` from an external `CATEGORY_KEYWORDS` mapping. If the "STANDARD" keyword is present for the category, the function returns only those models from the `source_list` that are also found in an external `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list` and includes models in the filtered output if their lowercase name contains any of the retrieved category keywords. If no models match the keywords, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The list of models (strings) to be filtered.
    - **category_name** (`str`): The name of the category used to determine filtering keywords.
*   **Returns:**
    - **filtered_models** (`list[str]`): A list of strings representing the models filtered according to the specified category, or the original list if no matches are found.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function, `save_gemini_cb`, is designed to save a new Gemini API key provided by the user. It retrieves the potential new key from `st.session_state` under the key "in_gemini_key". If a non-empty key is found, it updates the user's Gemini key in the database via `db.update_gemini_key`. After successfully updating, it clears the temporary key from `st.session_state` and displays a success notification to the user using `st.toast`.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function, `save_ollama_cb`, serves as a callback to store a user-specified Ollama URL. It retrieves the potential new URL from Streamlit's session state, using the key "in_ollama_url". If a non-empty URL is found, the function proceeds to update this URL in the database. The `db.update_ollama_url` function is invoked with the current username, also obtained from session state, and the new URL. Finally, a success message is displayed to the user via `st.toast` to confirm that the Ollama URL has been saved.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** This function is responsible for loading chat and exchange data from a database into the Streamlit session state for a given user. It first checks if the data for the current user has already been loaded to prevent redundant operations. It initializes the session state's chat dictionary, then fetches predefined chats from the database and populates the session state. Subsequently, it fetches exchanges and assigns them to their respective chats, handling cases where a chat might not yet exist for an exchange. Finally, it ensures a default chat exists if none were loaded and sets the active chat in the session state.
*   **Parameters:**
    - **username** (`str`): The username for whom chat and exchange data should be loaded.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function processes changes to feedback for an exchange object. It updates the 'feedback' key within the provided exchange dictionary and then persists this change to a database using the exchange's ID. Finally, it triggers a UI refresh to reflect the updated state.
*   **Parameters:**
    - **ex** (`dict`): The exchange object, expected to be a dictionary containing 'feedback' and '_id' keys.
    - **val** (`Any`): The new feedback value to be assigned.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function is responsible for deleting a specific exchange from the database and updating the application's session state accordingly. It first calls a database function to remove the exchange by its ID. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if so, removes the exchange from that chat's list of exchanges. Finally, it triggers a Streamlit rerun to refresh the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat to which the exchange belongs.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' key for database lookup.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function handles the deletion of a specified chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it updates the Streamlit session state by removing the deleted chat from `st.session_state.chats`. If other chats exist, the active chat is set to the first available chat. If no chats remain after deletion, a new default chat named 'Chat 1' is created, inserted into the database via `db.insert_chat`, and set as the active chat. Finally, it triggers a Streamlit rerun to reflect these changes.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** This function extracts a repository name from a given text string. It first attempts to find a URL within the text using a regular expression. If a URL is found, it parses the URL to isolate the path component. The last segment of the path is then considered the repository name. It handles cases where the repository name ends with '.git' by removing the suffix. If no URL is found or no valid repository name can be extracted, the function returns None.
*   **Parameters:**
    - **text** (`str`): The input string that may contain a URL from which to extract a repository name.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string, or None if no URL is found or no repository name can be determined.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** This function acts as a generator that takes a string of text and yields its words one by one. It splits the input text by spaces and then iterates through each word. After yielding a word followed by a space, it introduces a small delay of 0.01 seconds. This creates a streaming effect, typically used for displaying text incrementally.
*   **Parameters:**
    - **text** (`str`): The input string of text to be streamed word by word.
*   **Returns:**
    - **word** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream)`
*   **Description:** This function processes a given markdown string, identifying and rendering embedded Mermaid diagrams. It splits the input text into regular markdown and Mermaid code blocks using a regular expression. Regular markdown sections are rendered using `st.markdown` or streamed via `st.write_stream` if `should_stream` is true. Mermaid diagram blocks are attempted to be rendered with `st_mermaid`, falling back to `st.code` if an error occurs during rendering. The function handles cases where the input markdown text is empty by returning early.
*   **Parameters:**
    - **markdown_text** (`str`): The input markdown string that may contain embedded Mermaid diagrams.
    - **should_stream** (`bool`): A flag indicating whether regular markdown parts should be streamed using `st.write_stream` or rendered directly with `st.markdown`. Defaults to `False`.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not called by any other functions.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** The render_exchange function is responsible for displaying a single chat exchange, comprising a user's question and an assistant's answer, within a Streamlit application. It first renders the user's question, followed by the assistant's response. The assistant's message area includes an interactive toolbar featuring feedback buttons (like/dislike), a popover for adding comments, a download button for the answer content, and a delete button for the entire exchange. The function also handles the display of error messages if the assistant's answer indicates a problem, providing a specific delete option for such error states. It leverages Streamlit components for UI rendering and interacts with external functions for managing feedback, updating database records, and deleting exchanges.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing a single chat exchange, expected to contain keys such as 'question', 'answer', '_id', 'feedback', and 'feedback_message' for rendering and interaction.
    - **current_chat_name** (`str`): The name of the current chat session, used to provide context when handling actions like deleting an exchange.
*   **Returns:** *None*
*   **Usage:** Calls: This function calls no other functions.
        Called By: This function is not explicitly called by any other functions in the provided context.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to encapsulate the essential details of a single function parameter. It serves as a structured data model for representing a parameter's name, its type, and a descriptive explanation of its role or purpose within a function's signature. This class is fundamental for generating comprehensive documentation or for systems that require a structured understanding of function interfaces.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the context.
*   **Dependencies:** This class explicitly depends on pydantic.BaseModel for its foundational structure and validation capabilities.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is automatically generated, allowing instances to be created by providing values for its defined fields: name, type, and description.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type annotation or inferred type of the parameter.
        - **description** (`str`): A brief explanation of the parameter's purpose or role.
*   **Methods:** *None*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to structure and validate information about the return value of a function. It encapsulates three essential string attributes: 'name', 'type', and 'description', providing a standardized format for describing function outputs. This class serves as a clear and concise data container for return value metadata within a larger system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an __init__ method. This constructor initializes an instance of ReturnDescription by accepting 'name', 'type', and 'description' as keyword arguments, validating their types, and assigning them as instance attributes.
    *   *Parameters:*
        - **name** (`str`): The name of the return value, often a descriptive label.
        - **type** (`str`): The Python type hint or a string description of the return value's data type.
        - **description** (`str`): A detailed explanation of what the return value represents or its purpose.
*   **Methods:** *None*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts with other parts of a system. It defines two string attributes, 'calls' and 'called_by', to summarize the outbound and inbound relationships, respectively. This class serves as a structured data container for contextual usage information.
*   **Instantiation:** The specific instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for UsageContext is implicitly generated by Pydantic's BaseModel. It initializes an instance by validating and assigning values to the 'calls' and 'called_by' attributes based on the provided arguments.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or classes that this entity calls.
        - **called_by** (`str`): A string summarizing the functions or methods that call this entity.
*   **Methods:** *None*

#### Class: `FunctionDescription`
*   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured schema for representing a function's purpose, its input parameters, its return values, and its contextual usage within a larger system. This class ensures that function analysis data adheres to a predefined format, facilitating consistent data exchange and processing.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `FunctionDescription` is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by validating and assigning values to its fields: `overall`, `parameters`, `returns`, and `usage_context`. Pydantic handles type checking and data validation automatically during instantiation.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary describing the function's purpose and its implementation details.
        - **parameters** (`List[ParameterDescription]`): A list containing detailed descriptions of each parameter the function accepts.
        - **returns** (`List[ReturnDescription]`): A list containing detailed descriptions of the values the function returns.
        - **usage_context** (`UsageContext`): An object providing context about where the function is called and what other functions or methods it calls.
*   **Methods:** *None*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data container, holding the function's unique identifier, a detailed description object (FunctionDescription), and an optional error message. This model is crucial for standardizing the representation of function analysis within a larger system, ensuring consistent data exchange regarding a function's purpose, signature, and contextual usage.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is automatically generated, allowing instances to be created by passing keyword arguments that correspond to its defined fields: identifier, description, and error. This enables straightforward instantiation and validation of the analysis data.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the function being analyzed.
        - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional string that provides details about any errors encountered during the function's analysis. Defaults to None if no error occurred.
*   **Methods:** *None*

#### Class: `ConstructorDescription`
*   **Summary:** The `ConstructorDescription` class is a Pydantic BaseModel designed to encapsulate metadata about a class's `__init__` method. It provides a structured way to store a textual description of the constructor's purpose and a list of its individual parameters, each described by a `ParameterDescription` object. This schema is crucial for systems that need to programmatically analyze, document, or generate code based on constructor signatures.
*   **Instantiation:** This class is not explicitly listed as being instantiated by any other components.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ConstructorDescription` is implicitly generated by Pydantic's BaseModel. It initializes an instance of this class by validating and assigning the provided `description` string and a list of `ParameterDescription` objects to the corresponding instance attributes.
    *   *Parameters:*
        - **description** (`str`): A string providing a high-level overview of the constructor's purpose and behavior.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing a specific parameter accepted by the constructor.
*   **Methods:** *None*

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a class's operational context. It specifically stores information regarding the class's external dependencies and the locations or entities responsible for its instantiation. This model serves as a structured way to describe how a class interacts with its environment and where it fits into a larger system.
*   **Instantiation:** Based on the provided context, there are no specific points of instantiation listed for this class.
*   **Dependencies:** Based on the provided context, there are no specific external dependencies listed for this class.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an __init__ method. It initializes an instance of ClassContext by accepting values for `dependencies` and `instantiated_by`, which are then stored as attributes.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of a class.
        - **instantiated_by** (`str`): A string describing where the class is primarily instantiated.
*   **Methods:** *None*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It serves as a structured data container, holding an overall summary of the class, a detailed description of its constructor, a list of analyses for each of its methods, and information regarding its usage context within a larger system. This model facilitates the programmatic representation and exchange of class analysis data.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any direct external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class does not define an explicit `__init__` method. It inherits from `pydantic.BaseModel`, and its constructor is implicitly generated by Pydantic, accepting keyword arguments corresponding to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`.
    *   *Parameters:* *None*
*   **Methods:** *None*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the main Pydantic model for structuring the comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed description object containing its constructor and method analyses, and an optional field for reporting any errors during the analysis process. This class is designed to provide a standardized, machine-readable format for class analysis outputs.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, has its constructor implicitly generated by Pydantic. It initializes instances with an identifier string, a ClassDescription object, and an optional error string, ensuring all required analysis components are present or accounted for.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the class being analyzed, typically its fully qualified name.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
        - **error** (`Optional[str]`): An optional string to store any error messages encountered during the class analysis, defaulting to None if no errors occurred.
*   **Methods:** *None*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event within a system, typically used by a relationship analyzer. It encapsulates key details about a call, such as the file path, the name of the calling function, the mode of the call (e.g., 'method', 'function'), and the line number where the call occurs. This class serves as a structured data container for tracking and analyzing inter-component relationships, specifically for 'called_by' and 'instantiated_by' contexts.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components within the analyzed context.
*   **Dependencies:** This class does not explicitly depend on other components within the analyzed context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the CallInfo class's initialization is handled implicitly by Pydantic. Instances are created by passing keyword arguments that correspond to the defined fields (file, function, mode, line). Pydantic automatically validates the types and assigns the values to the instance attributes upon object creation.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that performed the call.
        - **mode** (`str`): The type of call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the file where the call event occurred.
*   **Methods:** *None*

#### Class: `FunctionContextInput`
*   **Summary:** The `FunctionContextInput` class is a Pydantic BaseModel designed to provide a structured container for context related to the analysis of a function. It serves as a data transfer object (DTO) to encapsulate information about what a function calls and by whom it is called. This class is fundamental for organizing and passing around structured data within a larger system that performs code analysis.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, inheriting from Pydantic's BaseModel, implicitly defines its constructor. It initializes instances by validating and assigning values to its `calls` and `called_by` attributes based on the keyword arguments provided during instantiation. Pydantic handles the type checking and data conversion automatically.
    *   *Parameters:* *None*
*   **Methods:** *None*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a FunctionAnalysis object. It serves as a data transfer object, ensuring that all necessary components for function analysis, such as the function's mode, identifier, source code, imports, and contextual information, are provided in a consistent format. This class facilitates the reliable parsing and validation of input data before further processing.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. Pydantic's BaseModel handles the initialization of its fields based on the provided data, validating them against the defined types and constraints.
    *   *Parameters:* *None*
*   **Methods:** *None*

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic BaseModel designed to provide a structured representation of a method's contextual information. It defines a schema for capturing key details such as the method's identifier, the functions or methods it calls, where it is called from, its arguments, and its docstring. This class acts as a data model to standardize the input for method analysis within a larger system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The __init__ method for MethodContextInput is implicitly generated by Pydantic's BaseModel. It handles the validation and assignment of the class's defined fields: identifier, calls, called_by, args, and docstring, ensuring that instances conform to the specified types and structure upon creation.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects detailing where this method is invoked.
        - **args** (`List[str]`): A list of argument names that the method accepts.
        - **docstring** (`Optional[str]`): The docstring content of the method, if available.
*   **Methods:** *None*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information relevant to the analysis of a Python class. It serves as a data container, holding lists of external dependencies, locations where the class is instantiated, and detailed context for each method within the class. This model facilitates the organization and transfer of comprehensive class analysis data.
*   **Instantiation:** This class is not explicitly instantiated by any known components in the provided context.
*   **Dependencies:** This class does not explicitly declare external functional dependencies within its own definition.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the __init__ method for ClassContextInput is automatically generated. It initializes an instance by validating and assigning the provided values for 'dependencies', 'instantiated_by', and 'method_context' to the corresponding attributes, ensuring type correctness based on the defined schema.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies relevant to the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects, each detailing a location where the class being analyzed is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, providing specific contextual information for each method within the class being analyzed.
*   **Methods:** *None*

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a data contract, ensuring that all necessary information—such as the class identifier, its source code, relevant imports, and contextual details—is provided in a consistent format for further processing. This model ensures the integrity and completeness of data before initiating a class analysis.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class inherits from Pydantic's BaseModel and does not define an explicit `__init__` method. Pydantic automatically generates a constructor that initializes the instance attributes based on the type hints provided for each field, performing validation during instantiation.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operational mode, which is fixed to 'class_analysis' for this input type.
        - **identifier** (`str`): The unique name or identifier of the class that is to be analyzed.
        - **source_code** (`str`): The raw source code string of the entire class definition to be analyzed.
        - **imports** (`List[str]`): A list of import statements from the source file where the class is defined, which may include imports not directly used by the class itself.
        - **context** (`ClassContextInput`): An object containing additional contextual information relevant to the class, such as its dependencies and where it is instantiated.
*   **Methods:** *None*

---
# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated software documentation agent. It analyzes a given Git repository by cloning it, parsing the source code to build an Abstract Syntax Tree (AST), and identifying key components like classes, functions, and their relationships. Leveraging Large Language Models (LLMs) in a multi-agent architecture (Helper and Main LLMs), it generates detailed, human-readable descriptions for each code component. The final output is a comprehensive technical documentation report, accessible through an interactive Streamlit-based web frontend.
- **Key Features:**
  - Automated Git repository cloning and file analysis.
  - Abstract Syntax Tree (AST) generation for Python code.
  - LLM-powered analysis for generating code summaries, parameter descriptions, and usage contexts.
  - Analysis of code relationships, including function calls and dependencies.
  - Interactive Streamlit web interface for user input and report visualization.
- **Tech Stack:** streamlit, langchain, networkx, gitpython, pydantic, google-generativeai, ollama.

*   **Repository Structure:**
    ```mermaid
    graph TD
        root["repo-onboarding-agent"]
        root --> f0[".env.example"]
        root --> f1[".gitignore"]
        root --> f2["analysis_output.json"]
        root --> f3["readme.md"]
        root --> f4["requirements.txt"]
        root --> d0["SystemPrompts"]
        d0 --> d0_files["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt"]
        root --> d1["backend"]
        d1 --> d1_files["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py"]
        root --> d2["database"]
        d2 --> d2_files["db.py"]
        root --> d3["frontend"]
        d3 --> f5["Frontend.py"]
        d3 --> f6["__init__.py"]
        d3 --> d4["gifs"]
        d4 --> d4_files["4j.gif"]
        root --> d5["notizen"]
        d5 --> f7["Report Agenda.txt"]
        d5 --> f8["Zwischenpraesentation Agenda.txt"]
        d5 --> f9["doc_bestandteile.md"]
        d5 --> f10["notizen.md"]
        d5 --> f11["paul_notizen.md"]
        d5 --> f12["praesentation_notizen.md"]
        d5 --> f13["technische_notizen.md"]
        d5 --> d6["grafiken"]
        d6 --> f14["File_Dependency_Graph_Repo.dot"]
        d6 --> f15["global_callgraph.png"]
        d6 --> f16["global_graph.png"]
        d6 --> f17["global_graph_2.png"]
        d6 --> f18["repo.dot"]
        d6 --> d7["Flask-Repo"]
        d7 --> d7_files["__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot"]
        d6 --> d8["Repo-onboarding"]
        d8 --> d8_files["AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot"]
        root --> d9["result"]
        d9 --> d9_files["report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
        root --> d10["schemas"]
        d10 --> d10_files["types.py"]
    ```

## 2. Installation
### Dependencies
As this repository contains a `requirements.txt` file, you can install all necessary dependencies with the following command:
```bash
pip install -r requirements.txt
```
Key dependencies include:
- altair==4.2.2
- langchain==1.0.8
- langchain-core==1.1.0
- langchain-google-genai==3.1.0
- langchain-ollama==1.0.0
- networkx==3.6
- numpy==2.3.5
- pandas==2.3.3
- pydantic==2.12.4
- streamlit==1.51.0
- streamlit-authenticator==0.4.2

### Setup Guide
1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd repo-onboarding-agent
    ```
2.  **Create a Virtual Environment:**
    It is highly recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install Dependencies:**
    Install all required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment Variables:**
    Copy the example environment file and fill in your API keys.
    ```bash
    cp .env.example .env
    ```
    Now, edit the `.env` file with your preferred text editor to add your API keys (e.g., for Gemini).

### Quick Startup
To run the application, execute the following command from the root directory of the project:
```bash
streamlit run frontend/Frontend.py
```
This will start the Streamlit web server and open the application in your default web browser.

## 3. Use Cases & Commands
The primary use case of this application is to generate comprehensive technical documentation for a software repository automatically.

**Workflow:**
1.  Launch the application using the Quick Startup command.
2.  In the web interface, provide the full URL to a public Git repository.
3.  Select the desired LLM models for the "Helper" and "Main" analysis tasks.
4.  Provide the necessary API keys for the selected models.
5.  Initiate the analysis. The application will clone the repository, analyze the code structure, and use LLMs to generate documentation.
6.  The final, formatted Markdown report will be displayed in the interface.

**Primary Command:**
The application is controlled via its web interface. The only command-line instruction needed is to start the server:
```bash
streamlit run frontend/Frontend.py
```

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a file system path into a standard Python module path string. It first attempts to calculate the path relative to the provided project root using `os.path.relpath`. If this fails due to a `ValueError`, it falls back to using only the base name of the file. The function then strips the `.py` extension and replaces system path separators with dots to form the module path. Finally, it handles package initialization files by removing the `.__init__` suffix if present, ensuring a clean module identifier is returned.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative file system path that needs to be converted into a module path.
    - **project_root** (`str`): The root directory of the project, used as the base for calculating the relative module path.
*   **Returns:**
    - **module_path** (`str`): The resulting Python module path string (e.g., 'package.subpackage.module').
*   **Usage:**
    *   **Calls:** This function utilizes path manipulation utilities such as `os.path.relpath` and `os.path.basename`, along with string methods like `endswith` and `replace` to process the file path.
    *   **Called By:** This function is called by the `__init__` method within `AST_Schema.py`.

#### Class: `ASTVisitor`
*Analysis data not available for this component.*
#### Class: `ASTAnalyzer`
*Analysis data not available for this component.*
---
### File: `backend/File_Dependency.py`
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a NetworkX directed graph representing the file-level import dependencies for a single Python file. It initializes a nx.DiGraph and uses the FileDependencyGraph AST visitor to analyze the provided Abstract Syntax Tree (tree). The visitor collects dependencies by mapping the current file (caller) to the modules it imports (callees). It then iterates through these collected dependencies, adding nodes for both callers and callees, and creating directed edges from the caller to each callee in the graph before returning the final dependency graph.
*   **Parameters:**
    - **filename** (`str`): The path or name of the file currently being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file's source code, which is traversed to find import statements.
    - **repo_root** (`str`): The root directory of the repository, used by the visitor to resolve relative imports and paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files/modules and edges represent import dependencies.
*   **Usage:**
    *   **Calls:** This function initializes a NetworkX directed graph (DiGraph), creates and utilizes a FileDependencyGraph visitor to process the AST via visit, and then iterates over the collected dependencies using items to populate the graph via add_node, add_nodes_from, and add_edge.
    *   **Called By:** This function is called by build_repository_graph.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function is responsible for constructing a comprehensive directed dependency graph (nx.DiGraph) covering all Python files within a given Git repository. It iterates through every file retrieved from the repository object, filtering only for files ending in '.py'. For each Python file, it parses the content into an Abstract Syntax Tree (AST) and delegates the dependency extraction to the `build_file_dependency_graph` function. Finally, it merges the nodes and edges from the resulting file-level graphs into a single repository-wide `global_graph`, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The repository object containing methods to access file contents and the temporary directory path.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependencies between entities (functions, classes, modules) across all Python files in the repository.
*   **Usage:**
    *   **Calls:** This function calls methods on the provided `repository` object (like `get_all_files`), uses string manipulation methods (`endswith`, `removesuffix`), utilizes standard library functions (`os.path.basename`, `str`, `parse`), and relies on `build_file_dependency_graph` to process individual files. It also uses NetworkX methods (`DiGraph`, `add_node`, `add_edge`) to construct the graph.
    *   **Called By:** This function is called by the module-level execution logic within `File_Dependency.py`.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function scans a specified directory recursively to find all Python source files (`*.py`). It first converts the input directory string into an absolute, resolved `pathlib.Path` object. It then uses recursive globbing (`rglob`) to locate all matching files. Finally, it returns a list of these file paths, ensuring each path is relative to the initial root directory provided.
*   **Parameters:**
    - **directory** (`str`): The path string representing the root directory to be searched.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of pathlib.Path objects, each representing a Python file found, with paths relative to the input directory.
*   **Usage:**
    *   **Calls:** The function calls methods associated with `pathlib.Path` objects, specifically `Path` constructor, `resolve`, `rglob`, and `relative_to`.
    *   **Called By:** This function is called by `_resolve_module_name`.

#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G: nx.DiGraph)`
*   **Description:** This function converts a NetworkX Directed Graph (G) representing file dependencies into a Mermaid diagram syntax string. It first organizes the file nodes into folders using a defaultdict, treating path components before the last segment as the folder name. It then generates the Mermaid syntax, creating 'subgraph' blocks for each folder to visually group related files. Files residing in the root directory are handled outside of any subgraph. Finally, it iterates through the graph's edges, translating them into dependency arrows ('-->') between the corresponding file nodes, ensuring all node IDs are sanitized by replacing path separators.
*   **Parameters:**
    - **G** (`nx.DiGraph`): The NetworkX Directed Graph where nodes are file paths (strings) and edges represent dependencies between files.
*   **Returns:**
    - **mermaid_diagram** (`str`): A newline-separated string containing the complete Mermaid diagram definition, structured with subgraphs for folders and dependency arrows.
*   **Usage:**
    *   **Calls:** This function calls methods for list manipulation (append), dictionary iteration (items), string manipulation (join, replace, split), and utilizes the collections.defaultdict class for grouping files by folder.
    *   **Called By:** This function is called by the module-level execution context within File_Dependency.py.

#### Class: `FileDependencyGraph`
*Analysis data not available for this component.*
---
### File: `backend/HelperLLM.py`
#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function acts as a main orchestration and testing loop for the LLMHelper class within the backend system. It initializes several Pydantic models with dummy data representing function analysis inputs and pre-computed outputs for testing purposes. It instantiates the LLMHelper using configuration paths and an API key. The function then simulates the documentation generation process by calling the helper's `generate_for_functions` method with a list of these dummy inputs. Finally, it processes the results, logs the status of each analyzed item, aggregates them into a `final_documentation` dictionary, and prints the final structure as a formatted JSON string.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function calls Pydantic validation methods (`model_validate`, `model_dump`), logging utilities (`info`, `warning`), JSON serialization (`dumps`), and the core documentation generation method (`generate_for_functions`) of the LLMHelper class.
    *   **Called By:** This function is called by the module `backend.HelperLLM`.

#### Class: `LLMHelper`
*Analysis data not available for this component.*
---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*Analysis data not available for this component.*
---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*Analysis data not available for this component.*
---
### File: `backend/callgraph.py`
#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree: ast.AST, filename: str)`
*   **Description:** This function constructs a directed Call Graph (nx.DiGraph) from a given Python Abstract Syntax Tree (AST). It initializes a specialized `CallGraph` visitor with the file name and executes the visitor across the entire AST. The visitor identifies functions, methods, and scopes as nodes, and function calls as potential edges. After the AST traversal is complete, the function iterates through the collected caller-callee relationships stored in the visitor's internal edge dictionary. Finally, it explicitly adds these edges to the graph object and returns the fully populated Call Graph.
*   **Parameters:**
    - **tree** (`ast.AST`): The Abstract Syntax Tree of the Python file being analyzed.
    - **filename** (`str`): The name of the analyzed file, such as 'main.py' or 'src/utils.py'.
*   **Returns:**
    - **graph** (`nx.DiGraph`): The complete directed Call Graph, where nodes represent functions/scopes and edges represent function calls.
*   **Usage:**
    *   **Calls:** The function initializes an instance of `CallGraph`, calls its `visit` method on the AST, and iterates over the `items` of the visitor's `edges` dictionary. It then uses the `add_edge` method to populate the graph structure.
    *   **Called By:** This function is called by `analyze_repository` in `AST_Schema.py` and by `build_global_callgraph` in `callgraph.py`.

#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph: nx.DiGraph)`
*   **Description:** This function converts a `networkx.DiGraph` object, typically representing a call graph, into a standard Python dictionary format suitable for JSON serialization (an adjacency list). It ensures the output is consistent by iterating over the nodes in sorted order. For each node, it retrieves its successors (callees) and sorts them before storing the mapping. Only nodes that have outgoing edges (i.e., nodes that call other functions) are included in the resulting adjacency list.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The directed call graph object to be converted into an adjacency list.
*   **Returns:**
    - **adj_list** (`Dict[str, list[str]]`): An adjacency list where the keys are the calling nodes (callers) and the values are sorted lists of the called nodes (callees).
*   **Usage:**
    *   **Calls:** This function utilizes standard Python functions like `list` and `sorted`, and methods from the `networkx.DiGraph` object, specifically `nodes` and `successors`.
    *   **Called By:** This function is not explicitly called by any other function in the provided context.

#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(repo: GitRepository)`
*   **Description:** This function is responsible for constructing a comprehensive, global directed call graph for all Python files within a given Git repository. It initializes an empty NetworkX directed graph and iterates through every file retrieved from the repository. For each Python file, it parses the content into an Abstract Syntax Tree (AST) and delegates the creation of a file-specific call graph to the `build_callGraph` function. The nodes and edges from these local graphs are then systematically merged into the global graph, ensuring all call relationships are captured across the entire codebase. The function returns the resulting aggregated call graph.
*   **Parameters:**
    - **repo** (`GitRepository`): The repository object providing access to the files and content necessary for analysis.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated function-level call relationships across all analyzed Python files.
*   **Usage:**
    *   **Calls:** The function retrieves all repository files using `repository.get_all_files()`. It uses `os.path.basename` and string methods (`endswith`, `removesuffix`, `str`) for path manipulation, and `ast.parse` to generate the AST. It relies on `build_callGraph` to process individual files and uses NetworkX methods (`DiGraph`, `add_node`, `add_edge`) to construct the final graph.
    *   **Called By:** This function is called by the `backend.callgraph` module.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and a file path, and writes the graph structure to a DOT file. Its primary purpose is to ensure that all node identifiers in the resulting DOT file are safe and simple, typically by replacing complex original names (like fully qualified function paths) with sequential identifiers (e.g., 'n0', 'n1'). It first creates a copy of the graph and generates a mapping from original node names to these safe names. It then relabels the nodes in the copied graph using this mapping, storing the original name as a 'label' attribute on the new nodes. Finally, it uses `nx.drawing.nx_pydot.write_dot` to output the relabeled graph to the specified file path.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph whose nodes need to be relabeled for safe DOT output.
    - **out_path** (`str`): The file path where the resulting DOT file will be written.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function utilizes NetworkX methods including `copy`, `nodes`, `relabel_nodes`, and `write_dot`, alongside built-in Python functions like `enumerate`, `list`, and dictionary `items`.
    *   **Called By:** This function is called by the `backend.callgraph` module at line 263.

#### Class: `CallGraph`
*Analysis data not available for this component.*
---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*Analysis data not available for this component.*
#### Class: `GitRepository`
*Analysis data not available for this component.*
---
### File: `backend/main.py`
#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: , end_time: , total_items: , batch_size: , model_name: )`
*   **Description:** This function calculates the effective processing time by subtracting estimated rate-limiting sleep durations from the total elapsed time. It first computes the total duration as the difference between the start and end times. If the provided model name does not start with "gemini-", the full duration is returned immediately. Otherwise, it calculates the number of batches required for processing and estimates the total sleep time, assuming a 61-second sleep between each batch (except the last one). The final net time is the total duration minus the total sleep time, ensuring the result is non-negative.
*   **Parameters:**
    - **start_time** (`float | datetime`): The starting timestamp or numerical time value of the process.
    - **end_time** (`float | datetime`): The ending timestamp or numerical time value of the process.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The maximum number of items processed per batch.
    - **model_name** (`str`): The name of the model used, which determines if rate-limiting sleep logic should be applied (e.g., 'gemini-').
*   **Returns:**
    - **net_time** (`float`): The calculated net duration of the process, excluding estimated rate-limit sleep times, capped at zero.
*   **Usage:**
    *   **Calls:** This function utilizes mathematical operations including `math.ceil` (aliased as `ceil`) and `max`, and the string method `startswith` to check the model type.
    *   **Called By:** This function is called by the `main_workflow` function in `main.py` at lines 244 and 275.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: , api_keys: dict, model_names: dict, status_callback: )`
*   **Description:** This function serves as the primary orchestration point for analyzing a code repository. It begins by parsing API keys and model configurations, validating the input to ensure it contains a repository URL, and checking for necessary API keys. It then clones the repository using GitRepository, extracts project metadata using ProjektInfoExtractor, and generates a detailed Abstract Syntax Tree (AST) schema via ASTAnalyzer. The function structures this data into inputs for a Helper LLM, which performs detailed analysis on individual functions and classes. Finally, it aggregates all intermediate results and passes them to a Main LLM to generate a comprehensive final report, handling status updates, logging, and rate limit delays throughout the process. The function returns the final report content and execution time metrics.
*   **Parameters:**
    - **input** (`any`): The primary user input string, which is expected to contain the repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various services, such as 'gemini', 'gpt', and 'ollama'.
    - **model_names** (`dict`): A dictionary specifying the names of the models to be used for the 'helper' and 'main' LLM roles.
    - **status_callback** (`function/callable`): An optional callback function used to provide real-time status updates and logging messages to the caller. Defaults to None.
*   **Returns:**
    - **return value** (`dict`): A dictionary containing the final generated report under the key 'report' and execution metrics under the key 'metrics'.
*   **Usage:**
    *   **Calls:** This function utilizes standard library functions like logging, re.search, json.dumps, time.time, time.sleep, os.makedirs, and os.path.join. It relies heavily on external classes and methods for core functionality, including GitRepository for cloning, ProjektInfoExtractor for metadata extraction, ASTAnalyzer for code structure analysis, and LLMHelper and MainLLM for orchestrating the AI analysis and final report generation.
    *   **Called By:** This function is called by frontend.Frontend and backend.main.

#### Function: `update_status`
*   **Signature:** `def update_status(msg: )`
*   **Description:** This utility function standardizes status reporting by handling both logging and external callback execution. It accepts a message and first checks if a callable named `status_callback` is defined and truthy. If the callback exists, the message is passed to it, presumably for real-time status updates to a user interface. Regardless of the callback's presence, the function ensures the message is logged at the INFO level using the standard Python `logging` module.
*   **Parameters:**
    - **msg** (`Any`): The status message (typically a string) to be processed, logged, and potentially passed to the status callback.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function calls `logging.info` (aliased as `backend/main.py::info`) to record the status message and conditionally invokes the `status_callback` function if it is available.
    *   **Called By:** This function is exclusively called by the `main_workflow` function within `main.py` at various stages of the workflow execution.

---
### File: `backend/relationship_analyzer.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: , project_root: )`
*   **Description:** This function converts a file system path into a standardized Python module path string. It first determines the path relative to the provided project root using `os.path.relpath`. It then removes the `.py` extension if present, and replaces all operating system path separators with dots (`.`). Finally, if the resulting module path ends with `.__init__`, that suffix is removed, ensuring that package initialization files are represented by the package name alone. This process is essential for mapping file locations to importable module names.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative file path that needs to be converted into a module path.
    - **project_root** (`str`): The root directory of the project, used as the base to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The resulting Python module path string (e.g., 'package.module').
*   **Usage:**
    *   **Calls:** This function calls `os.path.relpath` to calculate the relative path, and uses string methods like `endswith` and `replace` for path manipulation.
    *   **Called By:** This function is utilized by the methods `_collect_definitions` and `__init__` within the `relationship_analyzer.py` file.

#### Class: `ProjectAnalyzer`
*Analysis data not available for this component.*
#### Class: `CallResolverVisitor`
*Analysis data not available for this component.*
---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function encrypts a given string using a globally available cipher_suite object. It first performs a guard clause, returning the original text if the input string is empty or if the cipher_suite object is not initialized. If encryption is performed, the input string is encoded to bytes, encrypted using the cipher suite's encrypt method, and the resulting ciphertext bytes are decoded back into a string before being returned.
*   **Parameters:**
    - **text** (`str`): The string content intended for encryption.
*   **Returns:**
    - **Encrypted string** (`str`): The encrypted version of the input text, or the original text if the input was empty or the cipher_suite was unavailable.
*   **Usage:**
    *   **Calls:** This function utilizes string manipulation methods (encode, decode) and calls the encrypt method on the cipher_suite object.
    *   **Called By:** This function is called by update_gemini_key.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given string using an external `cipher_suite` object. It first performs a guard clause, returning the original text if the input string is empty or if the `cipher_suite` is not initialized. If decryption proceeds, the input string is encoded to bytes, passed to `cipher_suite.decrypt()`, and the resulting bytes are decoded back into a string. The function includes robust error handling, catching any exception during the decryption process and safely returning the original, unencrypted text as a fallback.
*   **Parameters:**
    - **text** (`str`): The string value intended for decryption.
*   **Returns:**
    - **Decrypted text** (`str`): The successfully decrypted string, or the original input string if decryption fails or is skipped due to missing prerequisites.
*   **Usage:**
    *   **Calls:** This function calls methods for encoding the input string, performing the decryption operation via `cipher_suite.decrypt`, and decoding the result back into a string.
    *   **Called By:** This function is called by `get_decrypted_api_keys` located in `db.py`.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function handles the insertion of a new user record into the database collection `dbusers`. It accepts a username, name, and plaintext password. The password is first hashed using an external authentication utility (`stauth.hasher.hash`) for security. A user dictionary is constructed where the username serves as the document's primary key (`_id`), and fields for API keys are initialized as empty strings. The function then executes the insertion via `dbusers.insert_one` and returns the unique ID of the newly created document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which is stored as the document's _id.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plaintext password that will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (_id) of the document inserted into the database, which corresponds to the provided username.
*   **Usage:**
    *   **Calls:** This function calls a hashing utility (hash) to secure the password and a database method (insert_one) to persist the user data.
    *   **Called By:** This function is not called by any other functions listed in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is designed to retrieve all available user records from the underlying database system. It executes the `find()` method on the `dbusers` collection object, which initiates a query to fetch all documents. The resulting cursor or iterable is then explicitly cast into a standard Python list using the `list()` constructor. Finally, the complete list of user documents is returned to the calling context.
*   **Parameters:**
*   **Returns:**
    - **users** (`list`): A list of all user documents or records retrieved from the 'dbusers' collection.
*   **Usage:**
    *   **Calls:** This function internally calls the `find` method on the `dbusers` object and uses the built-in Python `list` constructor to process the results.
    *   **Called By:** This function is called by the `frontend.Frontend` function located in Frontend.py.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** This function serves to retrieve a single user record from a database collection, likely a MongoDB collection named 'dbusers'. It accepts a username string, which is used as the primary key ('_id') for the lookup. It executes a `find_one` query against the collection. The function returns the resulting user document if found, or None otherwise.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user record in the database.
*   **Returns:**
    - **user** (`dict | None`): The user document (as a dictionary) retrieved from the database, or None if no user matches the provided username.
*   **Usage:**
    *   **Calls:** This function internally calls the `find_one` method, likely belonging to a MongoDB client object (`dbusers`), to execute the database query.
    *   **Called By:** This function is not called by any other functions listed in the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function is responsible for securely updating a user's Gemini API key within the database. It accepts the user's identifier (username) and the new API key as input. Before persistence, the raw API key is encrypted using the `encrypt_text` helper function. The function then executes a database update operation on the `dbusers` collection, setting the encrypted key for the specified user ID. It returns the count of documents that were successfully modified by the update operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose key is being updated.
    - **gemini_api_key** (`str`): The raw, unencrypted Gemini API key provided by the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the database update operation (typically 1 if successful).
*   **Usage:**
    *   **Calls:** This function calls `encrypt_text` to encrypt the API key and utilizes `dbusers.update_one` (likely a wrapper for a database update operation) to persist the changes.
    *   **Called By:** This function is called by `frontend.Frontend`.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function is responsible for updating the Ollama Base URL associated with a specific user in the database. It takes the user's identifier (username) and the new URL as input. It executes a database update operation, targeting the document where the `_id` matches the provided username and setting the `ollama_base_url` field. The function then returns the count of documents that were successfully modified.
*   **Parameters:**
    - **username** (`str`): The unique identifier (used as the document's _id) of the user whose record needs updating.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service to be stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the database update operation.
*   **Usage:**
    *   **Calls:** The function calls the `update_one` method, likely belonging to a MongoDB collection object (`dbusers`), to perform the database modification.
    *   **Called By:** This function is called by `frontend.Frontend` within the file `Frontend.py`.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** This function is designed to retrieve the Gemini API key associated with a specific user from a database. It queries a collection named `dbusers` using the provided `username` as the document's primary identifier (`_id`). The query uses projection to efficiently fetch only the `gemini_api_key` field while excluding the `_id`. The function returns the retrieved API key, utilizing the dictionary's safe `.get()` method to handle cases where the key might be missing.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user's record in the database.
*   **Returns:**
    - **gemini_api_key** (`str or None`): The Gemini API key associated with the user, or None if the user document is not found or the key field is absent.
*   **Usage:**
    *   **Calls:** This function calls `find_one` (likely a database query method on `dbusers`) to retrieve a single user document, and then calls the dictionary method `get` to safely extract the API key.
    *   **Called By:** This function is not called by any other functions listed in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function is responsible for retrieving the configured Ollama base URL for a specific user. It queries the `dbusers` collection, using the provided username as the document identifier (`_id`). The query is projected to return only the `ollama_base_url` field, minimizing data transfer. The function then extracts this URL using the dictionary's safe `get` method, returning the URL string.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose Ollama base URL needs to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The base URL for the Ollama service associated with the user, or None if the field is not present in the user's database record.
*   **Usage:**
    *   **Calls:** The function utilizes `find_one` on the `dbusers` object to retrieve a specific user record and subsequently calls the dictionary `get` method to safely access the 'ollama_base_url' field.
    *   **Called By:** This function is not explicitly called by any other function listed in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is responsible for removing a specific user record from the database collection referenced by `dbusers`. It accepts a `username` string, which is used as the unique identifier (`_id`) for the deletion query. The function executes a single deletion operation using `delete_one` on the collection. Finally, it returns the `deleted_count` attribute from the result object, indicating how many records were successfully removed (expected to be 0 or 1).
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The count of documents successfully deleted by the operation (typically 0 or 1).
*   **Usage:**
    *   **Calls:** This function calls `delete_one`, likely a method on a database collection object (`dbusers`), to perform the deletion operation.
    *   **Called By:** This function is currently not referenced by any other analyzed functions in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves a user record from the `dbusers` collection using the provided username as the document ID. It first checks if the user exists; if not, it immediately returns a tuple of two None values. If the user is found, it extracts the `gemini_api_key` and passes it to the `decrypt_text` function to obtain the plaintext key. It also extracts the `ollama_base_url` directly. Finally, it returns the decrypted Gemini key and the Ollama URL.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to look up the user record in the database.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key string, or None if the user was not found.
    - **ollama_plain** (`str | None`): The Ollama base URL string, or None if the user was not found.
*   **Usage:**
    *   **Calls:** This function utilizes `dbusers.find_one` to query the database, `user.get` to safely retrieve dictionary values, and `decrypt_text` to process the encrypted API key.
    *   **Called By:** This function is primarily used by the `frontend.Frontend` module in `Frontend.py`.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str)`
*   **Description:** This function handles the persistence of a single user exchange record into a database collection, presumably MongoDB based on the context of `insert_one`. It accepts various parameters detailing the conversation (question, answer, feedback, user, chat name) and optional timing/component usage metrics. It constructs a dictionary object, adds a dynamic `created_at` timestamp using `datetime.now()`, and inserts the complete record. The function returns the unique identifier generated by the database for the new document.
*   **Parameters:**
    - **question** (`str`): The text of the question or prompt provided by the user.
    - **answer** (`str`): The text of the answer or response generated by the system.
    - **feedback** (`str`): The feedback string associated with the exchange.
    - **username** (`str`): The identifier of the user who participated in the exchange.
    - **chat_name** (`str`): The name or identifier of the chat session.
    - **helper_used** (`str`): Optional string indicating which helper component was utilized (defaults to an empty string).
    - **main_used** (`str`): Optional string indicating which main component was utilized (defaults to an empty string).
    - **total_time** (`str`): Optional string representing the total time taken for the exchange process (defaults to an empty string).
    - **helper_time** (`str`): Optional string representing the time spent by the helper component (defaults to an empty string).
    - **main_time** (`str`): Optional string representing the time spent by the main component (defaults to an empty string).
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier assigned by the database to the newly inserted exchange record.
*   **Usage:**
    *   **Calls:** This function utilizes `dbexchanges.insert_one` to store the data and `datetime.now` to generate a creation timestamp.
    *   **Called By:** This function is invoked by the `frontend.Frontend` function located within the `Frontend.py` module.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records associated with a specific user from a database collection, likely a MongoDB collection named `dbexchanges`. It accepts a username string as input and executes a find operation using that username as the query filter. The results of the database query are then converted into a standard Python list before being returned to the caller.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to filter the exchange records in the database.
*   **Returns:**
    - **exchanges** (`list`): A list containing all database exchange records found for the specified username.
*   **Usage:**
    *   **Calls:** This function calls `dbexchanges.find` to execute a database query and uses the built-in `list` constructor to convert the resulting cursor into a list.
    *   **Called By:** This function is called by `load_data_from_db` in the `Frontend.py` file.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function is responsible for querying and retrieving specific exchange records from a database collection, likely named 'dbexchanges'. It filters the records based on a combination of the provided username and a specific chat name. The function executes a database 'find' operation using these criteria and converts the resulting iterable cursor into a standard Python list before returning the data.
*   **Parameters:**
    - **username** (`str`): The user identifier used to filter the database exchanges.
    - **chat_name** (`str`): The name of the chat used to filter the database exchanges.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents matching the provided username and chat name criteria.
*   **Usage:**
    *   **Calls:** This function queries the database using `dbexchanges.find` and converts the result into a list using the built-in `list` function.
    *   **Called By:** This function is not called by any other function listed in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: , feedback: int)`
*   **Description:** This function is responsible for updating the feedback score associated with a specific exchange record in the database. It takes the unique exchange identifier and the new integer feedback value as input. It executes a MongoDB update operation using `dbexchanges.update_one`, querying by `_id` and setting the `feedback` field. The function returns the count of documents that were successfully modified by the database operation.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier (likely a MongoDB ObjectId) used to locate the specific exchange record to be updated.
    - **feedback** (`int`): The integer value representing the new feedback score to be stored for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were updated by the MongoDB update operation.
*   **Usage:**
    *   **Calls:** The function calls `database/db.py::update_one` to execute the database modification.
    *   **Called By:** This function is called by `handle_feedback_change` located in `Frontend.py`.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: , feedback_message: str)`
*   **Description:** This function is responsible for updating the feedback message field within a specific exchange document stored in the database collection `dbexchanges`. It takes the unique identifier of the exchange and the new feedback message string. The update is performed using a MongoDB `$set` operation, targeting the document by its `_id`. The function returns the count of documents that were successfully modified.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier (likely a MongoDB ObjectId or string) used to locate the specific exchange record.
    - **feedback_message** (`str`): The new string content to be stored in the 'feedback_message' field of the exchange document.
*   **Returns:**
    - **modified_count** (`int`): The count of documents modified by the database update operation, typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls `dbexchanges.update_one` to execute the database modification.
    *   **Called By:** This function is utilized by `Frontend.py::render_exchange`.

#### Function: `delete_chats_by_user`
*   **Signature:** `def delete_chats_by_user(username: str, chat_name: str)`
*   **Description:** This function is responsible for deleting all chat exchanges associated with a specific user and a named chat session from the `dbexchanges` collection. It constructs a query based on the provided `username` and `chat_name`. It executes a bulk deletion using the `delete_many` method on the collection object. The primary purpose is to clean up data when a user decides to remove a chat history. The function returns the total count of documents that were removed.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose chat exchanges are to be deleted.
    - **chat_name** (`str`): The specific name of the chat session whose exchanges should be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The count of documents (chat exchanges) that were successfully deleted by the database operation.
*   **Usage:**
    *   **Calls:** This function calls database/db.py::delete_many to execute the deletion query against the database collection.
    *   **Called By:** This function is called by handle_delete_chat.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is designed to delete a specific exchange record from the database based on its unique identifier. It accepts the exchange ID as a string input. The function executes a `delete_one` operation on the `dbexchanges` collection, using the provided ID to filter the MongoDB primary key `_id`. It returns the result of the deletion operation, specifically the count of documents removed.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier (ID) of the exchange record that should be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were successfully deleted by the operation. This value is typically 1 if the exchange was found and deleted, or 0 otherwise.
*   **Usage:**
    *   **Calls:** The function calls the `delete_one` method, likely belonging to a PyMongo collection object named `dbexchanges`, to execute the database deletion.
    *   **Called By:** This function is utilized by `handle_delete_exchange` located in `Frontend.py`.

---
### File: `frontend/Frontend.py`
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function initializes the Streamlit session state by loading existing chat exchanges from the database for a specified user. The loading process is idempotent, executing only if the "data_loaded" flag is not present in `st.session_state`. It retrieves exchanges using `db.fetch_exchanges_by_user`, organizes them into chat dictionaries, and ensures that any missing feedback fields are standardized to `np.nan`. Finally, it sets up the initial `active_chat` state, defaulting to 'Chat 1' if no existing chats are found.
*   **Parameters:**
    - **username** (`str`): The username used to query and fetch the relevant chat exchanges from the database.
*   **Returns:**
*   **Usage:**
    *   **Calls:** The function calls `db.fetch_exchanges_by_user` to retrieve user-specific chat data, and uses standard list and dictionary methods like `append`, `get`, `keys`, and `list`.
    *   **Called By:** This function is called by `frontend.Frontend`.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: , val: )`
*   **Description:** This function handles the change event for user feedback, updating the feedback value in both the local state and the persistent database. It takes an exchange object (`ex`) and the new feedback value (`val`). It first modifies the `feedback` key within the provided exchange object. It then calls a database utility function to ensure the change is persisted. Finally, it forces a complete application rerun using `st.rerun()` to update the user interface and reflect the new state.
*   **Parameters:**
    - **ex** (`dict`): The exchange object or state dictionary containing the current exchange data, including the '_id' and 'feedback' fields.
    - **val** (`Any`): The new feedback value to be assigned to the exchange.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function calls `db.update_exchange_feedback` to persist the data change and then invokes `st.rerun` to force a UI refresh.
    *   **Called By:** This function is primarily utilized by the `render_exchange` function.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: , ex: )`
*   **Description:** This function is responsible for deleting a specific 'exchange' record both from the persistent database and the active Streamlit session state. It first extracts the unique identifier (`_id`) from the exchange object (`ex`) and uses it to call a database deletion function. After successful database removal, it removes the entire exchange object from the list of exchanges associated with the provided `chat_name` within `st.session_state`. Finally, it triggers a Streamlit rerun to ensure the user interface reflects the deletion immediately.
*   **Parameters:**
    - **chat_name** (`str`): The identifier of the chat whose exchanges list in the session state needs to be updated.
    - **ex** (`dict`): The exchange object to be deleted. It must contain the '_id' key required for database deletion.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function calls `delete_exchange_by_id` (likely from the `db` module) to remove the record from the database, uses a list's `remove` method to update the session state, and finally calls `rerun` (from the `st` module) to refresh the Streamlit application.
    *   **Called By:** This function is called by `render_exchange`.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: , chat_name: )`
*   **Description:** This function handles the complete deletion of a specified chat session for a given user. It performs two main deletion operations: first, it calls a database utility to remove the chat data permanently using `db.delete_chats_by_user`. Second, it removes the chat entry from the application's session state (`st.session_state.chats`). After deletion, the function manages the active chat state: if other chats exist, the first remaining chat is set as active; otherwise, a new default chat named 'Chat 1' is created. Finally, it forces a Streamlit rerun to update the user interface.
*   **Parameters:**
    - **username** (`str`): The identifier of the user whose chat is being deleted.
    - **chat_name** (`str`): The unique name of the chat session to be deleted.
*   **Returns:**
    - **None** (`None`): The function performs side effects (database deletion, state modification, and UI rerun) and does not return an explicit value.
*   **Usage:**
    *   **Calls:** This function calls `delete_chats_by_user` (likely a database operation), standard list and dictionary methods like `keys`, `len`, and `list`, and the Streamlit function `rerun` to refresh the application state.
    *   **Called By:** This function is called by the `frontend.Frontend` component or module initialization logic.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: )`
*   **Description:** This function processes a string of markdown text, specifically designed to identify and render embedded Mermaid diagram blocks. It uses regular expressions (`re.split`) to separate the input text into alternating segments of standard markdown and Mermaid code, delimited by ````mermaid ... ```. Standard text segments are rendered using `st.markdown`. For the Mermaid code segments, it attempts graphical rendering via `st_mermaid`. If the graphical rendering fails due to an exception, the function falls back to displaying the raw Mermaid code using `st.code` for debugging or viewing.
*   **Parameters:**
    - **markdown_text** (`str`): The input string containing markdown content, potentially including embedded Mermaid diagram blocks.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function utilizes regular expression splitting (`re.split`), iteration (`enumerate`), hashing (`hash`), string manipulation (`strip`), and Streamlit rendering functions (`st.markdown`, `st.code`, and `st_mermaid`).
    *   **Called By:** This function is called by `render_exchange` and is referenced within the `frontend.Frontend` module context.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: , current_chat_name: )`
*   **Description:** This function is responsible for rendering a single chat exchange (user question and assistant answer) within a Streamlit interface. It first displays the user's question. The assistant's response is rendered along with a comprehensive toolbar featuring feedback buttons (upvote/downvote), a popover for writing detailed feedback, a download button for the answer content, and a button to delete the message. User interactions trigger calls to helper functions like `handle_feedback_change` and `handle_delete_exchange`, and database updates via `db.update_exchange_feedback_message`. The assistant's answer is displayed in a scrollable container using `render_text_with_mermaid`.
*   **Parameters:**
    - **ex** (`dict`): The exchange object containing the chat data, including 'question', 'answer', '_id', and current 'feedback' status.
    - **current_chat_name** (`str`): The identifier of the current chat session, required for handling the deletion of the exchange.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function utilizes numerous Streamlit UI components (e.g., chat_message, columns, button, popover, download_button, text_area, success, rerun) to construct the interface. It also calls helper functions `handle_feedback_change`, `handle_delete_exchange`, and `render_text_with_mermaid`, and interacts with the database via `db.update_exchange_feedback_message`.
    *   **Called By:** This function is called by a function or method within `frontend.Frontend`.

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic data model designed to strictly define the structure for describing a single parameter within a function or method signature. It enforces that every parameter description must include its name, its inferred type, and a textual description of its purpose. This model is essential for generating structured metadata about function interfaces in a machine-readable format and serves as a foundational component for larger schema definitions.
*   **Instantiation:** The instantiation points for this class were not provided in the input context.
*   **Dependencies:** This class depends on pydantic.BaseModel for its structural definition and validation capabilities.
*   **Constructor:**
    *   *Description:* The ParameterDescription class inherits its constructor from pydantic.BaseModel. Initialization requires providing values for the three mandatory string fields: name, type, and description, which define the characteristics of a function parameter.
    *   *Parameters:*
        - **name** (`str`): The name of the function parameter.
        - **type** (`str`): The inferred type of the parameter (e.g., 'int', 'List[str]').
        - **description** (`str`): A detailed explanation of the parameter's purpose and expected value.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to strictly define the structure for documenting the return value of a function. It acts as a schema, ensuring that any description of a function's output includes its name, type, and a detailed textual explanation. This model is typically used within larger schema definitions for function analysis or documentation generation.
*   **Instantiation:** The instantiation points for this class are currently unknown.
*   **Dependencies:** This class relies on pydantic.BaseModel for data validation and structured definition.
*   **Constructor:**
    *   *Description:* The class is initialized via the Pydantic BaseModel constructor, which accepts and validates the required fields: name, type, and description. These inputs are assigned as immutable instance attributes upon creation.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The string representation of the data type of the return value.
        - **description** (`str`): A detailed explanation of what the return value represents.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a simple Pydantic data model designed to structure information regarding the calling context of a function or method. It inherits from `BaseModel` to enforce type checking and validation for its two required string fields. This model is essential for providing a structured, human-readable summary of a function's interactions within the larger codebase, detailing both its dependencies and its callers.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** The class relies on the `BaseModel` from the Pydantic library for data validation and structured attribute definition.
*   **Constructor:**
    *   *Description:* The constructor is automatically generated by Pydantic's BaseModel. It initializes the instance by accepting and validating the required string values for `calls` and `called_by` to describe the function's usage context.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions, methods, or classes that the subject function calls.
        - **called_by** (`str`): A string describing the functions or methods that call the subject function.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to hold a complete, structured analysis of a single Python function. It acts as a data schema, encapsulating the function's synthesized purpose, its detailed signature (parameters and returns), and its contextual usage within the larger system. This model is fundamental for generating machine-readable documentation and analysis reports.
*   **Instantiation:** The instantiation points for this data structure are not provided in the current context, but it is typically instantiated when structuring the results of a function analysis.
*   **Dependencies:** This class depends on Pydantic's BaseModel for data validation and structure, and utilizes typing.List for defining collections of nested schema objects.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel. It initializes the FunctionDescription instance by validating and assigning values to its four core fields, which collectively describe a function's analysis.
    *   *Parameters:*
        - **overall** (`str`): The synthesized purpose and high-level implementation summary of the function.
        - **parameters** (`List[ParameterDescription]`): A list of structured descriptions for each input parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of structured descriptions for the values returned by the function.
        - **usage_context** (`UsageContext`): An object detailing the external dependencies and calling context of the function.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class serves as the primary data structure for storing the complete, structured analysis of a single Python function or method. It is a Pydantic model designed to enforce a strict schema, ensuring that every analysis includes the function's unique identifier, a detailed description object, and an optional field for capturing any analysis errors. This model is foundational for generating machine-readable documentation components.
*   **Instantiation:** This class is instantiated by components responsible for parsing and analyzing source code, typically within the documentation generation pipeline.
*   **Dependencies:** This class depends heavily on Pydantic's BaseModel for data validation and structure, and it requires the FunctionDescription type for its nested content.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated to validate and initialize the defined fields. It ensures that the required identifier and description are present and correctly typed, while optionally accepting an error string.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): A nested object containing the detailed analysis of the function's purpose, signature, and usage context.
        - **error** (`Optional[str]`): An optional field used to store an error message if the analysis of the function failed or was incomplete. Defaults to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** This class is a Pydantic data model designed to structure the analysis of a Python class's constructor (__init__ method). It serves as a container for a high-level textual summary of the constructor's behavior via the 'description' field, and a structured list of all its input arguments via the 'parameters' field, which are expected to be instances of 'ParameterDescription'. This model is crucial for generating structured documentation about class initialization within a larger analysis system.
*   **Instantiation:** The context does not specify where this class is instantiated.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated to handle data validation and assignment for its defined fields. It initializes the object with a textual summary of the constructor and a list of its parameters.
    *   *Parameters:*
        - **description** (`str`): The textual summary describing the purpose and behavior of the __init__ method being analyzed.
        - **parameters** (`List[ParameterDescription]`): A list containing structured details for every parameter accepted by the __init__ method.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** This class is a Pydantic BaseModel designed to encapsulate the usage context of a software component, specifically a Python class. It acts as a simple data structure (schema) defining two required string fields: dependencies and instantiated_by. This structure is typically used within a larger analysis framework to provide metadata about a class's integration points.
*   **Instantiation:** The context provided did not list any locations where this class is instantiated.
*   **Dependencies:** The context provided did not list any external dependencies for this class.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is implicitly generated to initialize the instance attributes `dependencies` and `instantiated_by`. It validates that the provided values for these fields are strings upon instantiation.
    *   *Parameters:*
        - **dependencies** (`str`): The external dependencies of the class, typically summarized in a human-readable string.
        - **instantiated_by** (`str`): A summary of the locations or modules where the class is instantiated.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** This Pydantic model serves as the primary data structure for storing the detailed analysis of a Python class. It encapsulates all necessary components, including a high-level summary of the class's role, the constructor details, a list of analyzed methods, and contextual information about its usage and dependencies. This structure is essential for standardizing the output of the code analysis process.
*   **Instantiation:** The class is not explicitly instantiated in the provided context, but it is typically created by components responsible for code analysis and documentation generation to structure their output.
*   **Dependencies:** This model depends on Pydantic's BaseModel for data validation and structure, and relies on external type definitions like ConstructorDescription, FunctionAnalysis, and ClassContext to define its schema.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor initializes the instance by validating and assigning the four required fields: overall, init_method, methods, and usage_context, ensuring they conform to their specified types.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose and primary responsibilities.
        - **init_method** (`ConstructorDescription`): The structured analysis of the class's __init__ method, including parameters and initialization logic.
        - **methods** (`List[FunctionAnalysis]`): A list containing the structured analysis of all methods defined within the class.
        - **usage_context** (`ClassContext`): Contextual information regarding the class's external dependencies and primary points of instantiation.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the root data structure for representing a complete, structured analysis of a Python class. Defined as a Pydantic BaseModel, it enforces a strict schema for the output of the code analysis process. It encapsulates the class's unique identifier, a detailed analysis object (ClassDescription), and an optional field for reporting any errors encountered during the analysis.
*   **Instantiation:** The context for where this class is instantiated is not provided in the input.
*   **Dependencies:** This class inherits from Pydantic's BaseModel for data validation and structure enforcement, and relies on the definition of the ClassDescription type.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the class is initialized by accepting values for its defined fields: identifier, description, and an optional error string. Pydantic handles the validation and assignment of these attributes automatically upon instantiation.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or path of the analyzed class.
        - **description** (`ClassDescription`): A complex object containing the synthesized analysis of the class, including its constructor and methods.
        - **error** (`Optional[str]`): An optional string used to report any errors encountered during the class analysis process. Defaults to None.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic BaseModel used to structure and validate context information related to a specific function being analyzed. It acts as a simple data container, defining two core attributes: a list of entities that the function calls, and a list of entities that call the function. This structure is crucial for tracking dependencies and usage patterns within a larger code analysis system.
*   **Instantiation:** This class is instantiated by the `main_workflow` function located in `main.py`.
*   **Dependencies:** This class has no explicit external dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor is implicitly handled by Pydantic's BaseModel, which initializes the instance attributes `calls` and `called_by` based on the provided dictionary or keyword arguments, ensuring they conform to the specified list of strings type.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing the identifiers of functions, methods, or classes that the analyzed function calls.
        - **called_by** (`List[str]`): A list of strings representing the identifiers of functions or methods that call the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic data model that strictly defines the required structure for input payloads used to initiate a function analysis task. It encapsulates all necessary components, including the function's identifier, its raw source code, associated imports, and detailed contextual information, ensuring that the input payload is correctly formatted and validated before processing by the analysis pipeline. This model serves as a contract for data exchange within the system.
*   **Instantiation:** This class is instantiated within the main_workflow function in main.py, likely when preparing data for a function analysis task.
*   **Dependencies:** This class does not appear to have external functional dependencies based on the provided context, relying primarily on standard Python types and Pydantic for structure.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the class uses Pydantic's default constructor. It initializes its attributes by accepting keyword arguments corresponding to the defined fields, enforcing strict type validation upon instantiation.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): A literal string specifying the operational mode, which must be 'function_analysis'.
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **source_code** (`str`): The raw source code string of the entire function definition.
        - **imports** (`List[str]`): A list of import statements relevant to the function's scope.
        - **context** (`FunctionContextInput`): A nested Pydantic object containing contextual information about the function, such as its dependencies and usage patterns.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic data model used to structure and validate contextual information about a specific method within a codebase. It acts as a schema for capturing essential metadata, including the method's unique identifier, the list of functions or classes it calls (dependencies), the list of entities that call it (usage points), its arguments, and its associated docstring. This structure is crucial for providing machine-readable context during automated code analysis.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class relies on pydantic.BaseModel for its structural definition and data validation capabilities.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel. It initializes the data model by accepting values for its five defined fields, ensuring they conform to the specified types (strings and lists of strings).
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method being described.
        - **calls** (`List[str]`): A list of other functions, methods, or classes that this method calls.
        - **called_by** (`List[str]`): A list of functions or methods that invoke this method.
        - **args** (`List[str]`): A list of argument names accepted by the method.
        - **docstring** (`Optional[str]`): The documentation string associated with the method, which may be optional or null.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput model is a Pydantic data structure designed to hold all necessary contextual information for analyzing a specific Python class. It organizes data related to the class's external dependencies, where it is instantiated throughout the codebase, and detailed usage context for each of its internal methods. This model ensures that the input provided to the class analysis system is standardized and validated.
*   **Instantiation:** This class is instantiated within the main_orchestrator function in HelperLLM.py and the main_workflow function in main.py.
*   **Dependencies:** This data structure relies on the pydantic.BaseModel for its core functionality and uses standard Python types like List for its fields.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated. It accepts keyword arguments corresponding to the defined fields and validates their types, ensuring that the input context for class analysis adheres to the expected structure (lists of strings and a list of MethodContextInput objects).
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of external dependencies (e.g., imported modules or classes) that the class being analyzed relies upon.
        - **instantiated_by** (`List[str]`): A list detailing the locations (files and functions) where the class being analyzed is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list containing detailed usage context, including calls and callers, for every method within the class being analyzed.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput schema defines the mandatory structure for data payloads submitted to the AI Code Analyst system when requesting a class analysis. As a Pydantic BaseModel, it ensures strict validation of the input, requiring fields such as the class identifier, its raw source code, associated imports, and a nested context object. This model serves as the primary contract for initiating the structured analysis workflow.
*   **Instantiation:** The class is instantiated within the main_orchestrator function in HelperLLM.py and the main_workflow function in main.py, suggesting it is used early in the processing pipeline to validate incoming data.
*   **Dependencies:** The input context did not list any specific external functional dependencies for this class, though it relies on Pydantic's BaseModel for its structure.
*   **Constructor:**
    *   *Description:* Since ClassAnalysisInput inherits from Pydantic's BaseModel, its constructor is automatically generated. It initializes the instance attributes based on the provided keyword arguments, enforcing the specified types and the literal value for the 'mode' field.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operational mode, strictly limited to the literal string 'class_analysis'.
        - **identifier** (`str`): The fully qualified name of the class being analyzed.
        - **source_code** (`str`): The raw source code string of the entire class definition.
        - **imports** (`List[str]`): A list of import statements found in the source file.
        - **context** (`ClassContextInput`): A nested schema containing contextual information about dependencies and usage patterns.
*   **Methods:**

---
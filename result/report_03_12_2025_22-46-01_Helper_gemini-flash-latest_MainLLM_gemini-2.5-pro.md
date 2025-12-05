# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated documentation generation agent. It clones a given Git repository, performs static code analysis by building an Abstract Syntax Tree (AST) and call graphs, and then leverages Large Language Models (LLMs) to analyze and describe the functionality of classes, methods, and functions. The final output is a comprehensive technical documentation report presented through a Streamlit-based web interface.
- **Key Features:**
  - Automated cloning of public Git repositories.
  - Static code analysis including Abstract Syntax Tree (AST) generation and dependency graphing.
  - Dual-LLM architecture (Helper and Main LLMs) for detailed code analysis.
  - Generation of human-readable Markdown documentation.
  - Interactive web frontend built with Streamlit for user interaction and displaying results.
- **Tech Stack:** Python, Streamlit, LangChain, NetworkX, GitPython, Pydantic, Matplotlib.

*   **Repository Structure:**
    ```mermaid
    graph LR
        subgraph root
            A["<b>/</b><br/>.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt"]
        end
        subgraph SystemPrompts
            B["<b>SystemPrompts</b><br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt"]
        end
        subgraph backend
            C["<b>backend</b><br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py"]
        end
        subgraph database
            D["<b>database</b><br/>db.py"]
        end
        subgraph frontend
            E["<b>frontend</b><br/>Frontend.py<br/>__init__.py"]
        end
        subgraph gifs
            F["<b>gifs</b><br/>4j.gif"]
        end
        subgraph notizen
            G["<b>notizen</b><br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
        end
        subgraph grafiken
            H["<b>grafiken</b><br/>File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
        end
        subgraph result
            I["<b>result</b><br/>... (17 files)"]
        end
        subgraph schemas
            J["<b>schemas</b><br/>types.py"]
        end
        subgraph statistics
            K["<b>statistics</b><br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png"]
        end
    
        root --> B
        root --> C
        root --> D
        root --> E
        E --> F
        root --> G
        G --> H
        root --> I
        root --> J
        root --> K
    ```

    ## 2. Installation
    ### Dependencies
    As this repository contains a `requirements.txt` file, you can install all dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
    The key dependencies are:
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
    [Information not found]
    ### Quick Startup
    [Information not found]

    ## 3. Use Cases & Commands
    The primary use case of this project is to automate the generation of technical documentation for a software repository. A user provides a Git repository URL through the web interface, and the agent performs a complete analysis and produces a detailed Markdown report.

    The main command to run the application is:
    ```bash
    streamlit run frontend/Frontend.py
    ```
    This command starts the Streamlit web server and opens the user interface in a web browser, from which the analysis process can be initiated.

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here



## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given filesystem path (`filepath`) into a standard Python module path string. It first attempts to calculate the path relative to the provided `project_root` using `os.path.relpath`, handling potential `ValueError` exceptions by falling back to just the file's base name. If the relative path ends with the `.py` extension, it is removed. Finally, all operating system path separators are replaced with dots (`.`), and if the resulting module path ends in `.__init__`, that suffix is stripped to yield the package name.
*   **Parameters:**
    - **filepath** (`str`): The path to the file that needs to be converted into a module path.
    - **project_root** (`str`): The root directory of the project, used as the base for calculating the relative module path.
*   **Returns:**
    - **module_path** (`str`): The resulting Python module path string, with separators replaced by dots and file extensions removed.
*   **Usage:**
    *   **Calls:** `basename`, `endswith`, `relpath`, `replace`
    *   **Called By:** *This function is not called by any other functions listed in the context.*

#### Class: `ASTVisitor`
*Analysis data not available for this component.*
#### Class: `ASTAnalyzer`
*Analysis data not available for this component.*
---
### File: `backend/File_Dependency.py`
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a NetworkX directed graph representing the file-level import dependencies for a given source file. It initializes a FileDependencyGraph visitor, which traverses the provided Abstract Syntax Tree (AST) to collect import relationships based on the file and repository root. It then iterates through the collected dependencies stored in the visitor's results. Finally, it adds the calling file and its imported files as nodes, creating directed edges from the caller to the callees, and returns the resulting dependency graph.
*   **Parameters:**
    - **filename** (`str`): The path or name of the file currently being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) representation of the source code of the file.
    - **repo_root** (`str`): The root directory path of the repository, used for resolving relative imports.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes are file paths and edges represent import dependencies.
*   **Usage:**
    *   **Calls:** `DiGraph`, `FileDependencyGraph`, `add_edge`, `add_node`, `add_nodes_from`, `items`, `visit`
    *   **Called By:** `build_repository_graph`

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function is responsible for constructing a comprehensive, directed dependency graph (call graph) spanning all Python files within a given Git repository. It initializes a global NetworkX directed graph and iterates through every file retrieved from the repository. For each Python file, it parses the content into an Abstract Syntax Tree (AST) and delegates the file-specific dependency analysis to the helper function `build_file_dependency_graph`. Finally, it merges the nodes and edges from the individual file graphs into the single global graph before returning the result.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object containing the source code files to be analyzed for dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependency relationships (nodes and edges) across all Python files in the repository.
*   **Usage:**
    *   **Calls:** `DiGraph`, `add_edge`, `add_node`, `basename`, `build_file_dependency_graph`, `endswith`, `get_all_files`, `parse`, `removesuffix`, `str`
    *   **Called By:** `<main_block>`

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function is designed to recursively locate all Python source files (`*.py`) within a specified starting directory. It first converts the input directory string into an absolute, resolved `pathlib.Path` object to establish the search root. It then uses the `rglob` method to find all matching files in the directory tree. The function compiles these file paths into a list, ensuring each path is represented relative to the original root directory before returning the final list.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory where the recursive search for Python files should begin.
*   **Returns:**
    - **all_files** (`list[Path]`): A list containing pathlib.Path objects, where each object represents a Python file (*.py) found recursively within the directory, relative to the root directory.
*   **Usage:**
    *   **Calls:** `Path`, `relative_to`, `resolve`, `rglob`
    *   **Called By:** *This function is not called by any other functions listed in the provided context.*

#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G)`
*   **Description:** This function converts a NetworkX Directed Graph (G), which models file dependencies, into a structured Mermaid diagram string. It organizes the nodes (file paths) into folders, using `collections.defaultdict` to map directories to lists of files. The function generates Mermaid `subgraph` blocks for each folder to visually group related files. Finally, it iterates over the graph edges to define the dependency arrows between the file nodes, ensuring all file path separators ('/') are replaced with underscores ('_') to create valid Mermaid IDs.
*   **Parameters:**
    - **G** (`nx.DiGraph`): The NetworkX Directed Graph where nodes represent file paths and edges represent dependencies or calls.
*   **Returns:**
    - **mermaid_diagram** (`str`): A string containing the complete Mermaid diagram definition, structured with 'graph TD' and 'subgraph' elements.
*   **Usage:**
    *   **Calls:** `append`, `defaultdict`, `items`, `join`, `replace`, `split`
    *   **Called By:** `<main_block>`

#### Class: `FileDependencyGraph`
*Analysis data not available for this component.*
---
### File: `backend/HelperLLM.py`
#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a test orchestrator and driver for the LLMHelper class, simulating a documentation generation workflow. It defines several hardcoded test cases for function analysis (e.g., 'add_item', 'check_stock') and class analysis using Pydantic models like FunctionAnalysisInput and FunctionAnalysis. It initializes the LLMHelper with necessary configurations and then executes the analysis process by calling `llm_helper.generate_for_functions`. Finally, it processes the results, logs the outcome, aggregates the structured data into a `final_documentation` dictionary, and prints the complete result serialized as JSON.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `ClassAnalysisInput`, `ClassContextInput`, `LLMHelper`, `dumps`, `generate_for_functions`, `info`, `model_dump`, `model_validate`, `print`, `warning`
    *   **Called By:** `<main_block>`

#### Class: `LLMHelper`
*   **Summary:** A class to interact with Google Gemini for generating code snippet documentation.
It centralizes API interaction, error handling, and validates I/O using Pydantic.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* *Analysis data not available for this component.*
    *   *Parameters:* *Analysis data not available for this component.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, function_prompt_path, class_prompt_path, model_name, ollama_base_url)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:* *Analysis data not available for this component.*
        *   *Returns:* *Analysis data not available for this component.*
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:* *Analysis data not available for this component.*
        *   *Returns:* *Analysis data not available for this component.*
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* Generates and validates documentation for a batch of functions.
        *   *Parameters:* *Analysis data not available for this component.*
        *   *Returns:* *Analysis data not available for this component.*
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* Generates and validates documentation for a batch of classes.
        *   *Parameters:* *Analysis data not available for this component.*
        *   *Returns:* *Analysis data not available for this component.*
---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** Hauptklasse für die Interaktion mit dem LLM.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* *Analysis data not available for this component.*
    *   *Parameters:* *Analysis data not available for this component.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, prompt_file_path, model_name, ollama_base_url)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:* *Analysis data not available for this component.*
        *   *Returns:* *Analysis data not available for this component.*
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:* *Analysis data not available for this component.*
        *   *Returns:* *Analysis data not available for this component.*
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:* *Analysis data not available for this component.*
        *   *Returns:* *Analysis data not available for this component.*
---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*Analysis data not available for this component.*
---
### File: `backend/callgraph.py`
#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree, filename)`
*   **Description:** This function constructs a call graph for a given Python file represented by its Abstract Syntax Tree (AST). It initializes a specialized visitor, `CallGraph`, using the provided filename, and then executes the visitor's `visit` method to traverse the AST and collect call information. After traversal, the function retrieves the underlying NetworkX directed graph object from the visitor. It then iterates through all collected edges stored in the visitor's `edges` dictionary and explicitly adds these caller-callee relationships to the graph structure using `graph.add_edge`. Finally, the complete NetworkX directed graph, representing the function and method calls within the analyzed file, is returned.
*   **Parameters:**
    - **tree** (`ast.AST`): The Abstract Syntax Tree (AST) of the Python file to be analyzed.
    - **filename** (`str`): The name of the analyzed file, such as "main.py" or "src/utils.py".
*   **Returns:**
    - **graph** (`nx.DiGraph`): The complete directed call graph, where nodes are functions/scopes and edges represent calls.
*   **Usage:**
    *   **Calls:** `CallGraph`, `add_edge`, `items`, `visit`
    *   **Called By:** `build_global_callgraph`

#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph)`
*   **Description:** This function converts a `networkx.DiGraph` object, typically used to represent a call graph, into a standard Python dictionary format suitable for JSON serialization, known as an adjacency list. The process ensures consistent output by iterating over all graph nodes in sorted order. For each node, it retrieves its successors (callees) using the graph's methods, sorts the list of successors, and then populates the resulting dictionary. The dictionary maps the calling node (key) to its list of called nodes (value), only including entries for nodes that have outgoing edges.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): Der zu konvertierende Call-Graph. (The call graph to be converted.)
*   **Returns:**
    - **adj_list** (`Dict[str, list[str]]`): Eine Adjazenzliste, bei der jeder Schlüssel ein aufrufender Knoten (caller) und der Wert eine Liste der aufgerufenen Knoten (callees) ist. (An adjacency list where each key is a calling node (caller) and the value is a list of the called nodes (callees).)
*   **Usage:**
    *   **Calls:** `list`, `nodes`, `sorted`, `successors`
    *   **Called By:** *This function is not explicitly called by any other functions listed in the provided context.*

#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(repo)`
*   **Description:** The function constructs a comprehensive global call graph for a given Git repository. It iterates over all files provided by the repository object, filtering specifically for Python files. For each Python file, it parses the content into an AST and generates a local call graph using the 'build_callGraph' utility. Finally, it merges the nodes and edges from all these local graphs into a single NetworkX directed graph (nx.DiGraph), which is then returned as the global call structure.
*   **Parameters:**
    - **repo** (`GitRepository`): The repository object containing the files to be analyzed for constructing the global call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated function-to-function call structure across all Python files in the repository.
*   **Usage:**
    *   **Calls:** `DiGraph`, `add_edge`, `add_node`, `basename`, `build_callGraph`, `endswith`, `get_all_files`, `parse`, `removesuffix`, `str`
    *   **Called By:** `<main_block>`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function prepares a NetworkX directed graph for serialization into a DOT file by ensuring all node identifiers are safe strings. It first creates a copy of the input graph. It then iterates through all nodes, generating simple, sequential string identifiers (like 'n0', 'n1') and mapping them to the original node names. The graph is relabeled using these safe identifiers. Crucially, the original, potentially complex node names are stored as the 'label' attribute on the new nodes, preserving the necessary information before the graph is written to the specified output path using nx.drawing.nx_pydot.write_dot.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph object to be processed and written to a DOT file.
    - **out_path** (`str`): The file path where the sanitized DOT graph representation will be saved.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `copy`, `enumerate`, `items`, `list`, `nodes`, `relabel_nodes`, `write_dot`
    *   **Called By:** `<main_block>`

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
#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart comparing two token counts, specifically for 'JSON' and 'TOON' formats. It takes the token counts, a calculated savings percentage, and a file path as input. The function uses `matplotlib.pyplot` to create the visualization, setting a title that includes the savings percentage, labeling the axes, and adding a grid for readability. It iterates over the bars to display the exact integer token count above each bar. Finally, the generated chart is saved to the specified `output_path` and the plot figure is closed.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings, displayed in the chart title formatted to two decimal places.
    - **output_path** (`str`): The file path where the generated chart image should be saved.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `bar`, `close`, `figure`, `get_height`, `get_width`, `get_x`, `grid`, `int`, `savefig`, `text`, `title`, `ylabel`
    *   **Called By:** `<backend/main.py>`

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** The function calculates the effective processing time (net time) by subtracting estimated rate-limiting sleep durations from the total elapsed time. It first determines the total duration between start_time and end_time. If the model_name does not start with 'gemini-', the full duration is returned without adjustment. For models requiring rate-limit handling, it calculates the number of batches based on total_items and batch_size, assuming a 61-unit sleep penalty for every batch transition except the first. Finally, it subtracts the total estimated sleep time from the total duration, ensuring the result is never negative.
*   **Parameters:**
    - **start_time** (`numeric`): The time recording started, used to calculate total duration.
    - **end_time** (`numeric`): The time recording ended, used to calculate total duration.
    - **total_items** (`int`): The total number of items processed, used to determine the number of batches.
    - **batch_size** (`int`): The maximum number of items processed per batch, used in batch calculation.
    - **model_name** (`str`): The name of the model used; if it starts with 'gemini-', sleep time adjustments are applied.
*   **Returns:**
    - **net_time** (`numeric`): The calculated net processing time (duration minus estimated sleep time), guaranteed to be non-negative.
*   **Usage:**
    *   **Calls:** `ceil`, `max`, `startswith`
    *   **Called By:** `<backend/main.py>`

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** This function orchestrates a comprehensive documentation generation pipeline. It initializes by extracting API keys and model configurations, validating the input to find a repository URL, and then cloning the specified repository using GitRepository. It proceeds to perform extensive static analysis, including extracting basic project information, generating a file tree, performing relationship analysis, and constructing an Abstract Syntax Tree (AST) schema. The function prepares structured inputs for a Helper LLM to analyze individual functions and classes, executes these analyses, and finally aggregates all results. The aggregated data is converted into a compressed TOON format and passed to the Main LLM for generating the final report, which is then saved along with execution metrics and an optional token savings chart.
*   **Parameters:**
    - **input** (`str`): The raw user input string, which is expected to contain a valid repository URL that will be cloned and analyzed.
    - **api_keys** (`dict`): A dictionary containing necessary API keys for LLM services (e.g., 'gemini', 'gpt') and potentially the 'ollama' base URL.
    - **model_names** (`dict`): A dictionary specifying the names of the models to be used for the 'helper' and 'main' LLM tasks.
    - **status_callback** (`callable | None`): An optional function used to relay status messages and progress updates back to the caller or a user interface. Defaults to None.
*   **Returns:**
    - **result_dict** (`dict`): A dictionary containing the final generated report string under the 'report' key and execution metrics under the 'metrics' key.
*   **Usage:**
    *   **Calls:** *Analysis data not available for this component.*
    *   **Called By:** `<main_block>`

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This utility function handles the reporting and logging of status updates within the application. It accepts a message and first checks if a callable object named 'status_callback' is available in the current scope. If the callback exists, it is executed with the provided message, allowing for external status reporting (e.g., to a UI or API). Finally, the function ensures the status message is recorded in the application logs using the standard logging mechanism at the INFO level.
*   **Parameters:**
    - **msg** (`str`): The status message string to be reported and logged.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `info`, `status_callback`
    *   **Called By:** `<backend/main.py>`

---
### File: `backend/relationship_analyzer.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given filesystem path (`filepath`) into a standard Python module path string. It first attempts to calculate the path relative to the provided `project_root` using `os.path.relpath`, handling potential `ValueError` exceptions by falling back to just the file's base name. If the relative path ends with the `.py` extension, it is removed. Finally, all operating system path separators are replaced with dots (`.`), and if the resulting module path ends in `.__init__`, that suffix is stripped to yield the package name.
*   **Parameters:**
    - **filepath** (`str`): The path to the file that needs to be converted into a module path.
    - **project_root** (`str`): The root directory of the project, used as the base for calculating the relative module path.
*   **Returns:**
    - **module_path** (`str`): The resulting Python module path string, with separators replaced by dots and file extensions removed.
*   **Usage:**
    *   **Calls:** `basename`, `endswith`, `relpath`, `replace`
    *   **Called By:** *This function is not called by any other functions listed in the context.*

#### Class: `ProjectAnalyzer`
*Analysis data not available for this component.*
#### Class: `CallResolverVisitor`
*Analysis data not available for this component.*
---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** This function handles the encryption of a given text string using a module-level encryption object, likely a Fernet cipher suite. It first performs a guard clause check: if the input 'text' is empty or if the 'cipher_suite' object is not defined, the function immediately returns the original, unencrypted text. If both conditions are met, the input string is encoded into bytes, encrypted using the 'cipher_suite', and the resulting encrypted bytes are decoded back into a string before being returned.
*   **Parameters:**
    - **text** (`str`): The string content that needs to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string, or the original string if the input was empty or the cipher suite was unavailable.
*   **Usage:**
    *   **Calls:** `decode`, `encode`, `encrypt`
    *   **Called By:** `update_gemini_key`

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** This function attempts to decrypt an input string using a globally accessible `cipher_suite` object, likely an instance of Fernet or a similar cryptographic tool. It first performs a guard clause, returning the original text if the input string is empty or if the `cipher_suite` object is not initialized. If decryption proceeds, the input string is encoded to bytes, decrypted by the cipher suite, and then decoded back into a string. The function includes robust error handling, catching any exceptions during the decryption process and returning the original, unencrypted text if the operation fails.
*   **Parameters:**
    - **text** (`str`): The string content that needs to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The successfully decrypted string, or the original input string if the input was empty, the cipher was unavailable, or decryption failed due to an exception.
*   **Usage:**
    *   **Calls:** `decode`, `decrypt`, `encode`
    *   **Called By:** `get_decrypted_api_keys`

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function handles the creation and persistence of a new user record in the database, presumably a MongoDB collection accessed via the global object `dbusers`. It accepts the user's username, full name, and plain text password. Before insertion, the function hashes the provided password using `stauth.hasher.hash`. The resulting user dictionary, which includes the username as the primary key (`_id`) and placeholder empty strings for API keys, is then inserted into the database. The function returns the unique identifier of the newly created document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which is used as the document's primary key (_id).
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain text password provided by the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (_id) of the newly inserted user document, which corresponds to the provided username.
*   **Usage:**
    *   **Calls:** `hash`, `insert_one`
    *   **Called By:** *This function is currently not referenced by any other analyzed functions in the system context.*

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is designed to retrieve all user records stored within the database. It accesses a database object, implied to be a collection named 'dbusers', and executes a `find()` operation without any filtering criteria. The result of this operation, which is typically a database cursor, is immediately converted into a standard Python list using the `list()` constructor. The function then returns this complete list of user objects.
*   **Parameters:** *None*
*   **Returns:**
    - **users** (`list`): A list containing all user records (documents) fetched from the database collection.
*   **Usage:**
    *   **Calls:** `find`, `list`
    *   **Called By:** *This function is not explicitly called by any other functions listed in the provided context.*

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** This function is responsible for retrieving a single user record from a database collection, inferred to be a MongoDB collection named `dbusers`. It accepts a `username` string which is used as the primary key for the lookup. The function executes a database query using the `find_one` method, searching for a document where the `_id` field matches the provided username. It returns the resulting user document if found, or potentially None otherwise.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user record, which is mapped to the _id field in the database query.
*   **Returns:**
    - **user** (`dict | None`): The dictionary representing the user document found in the database, or None if no user matches the provided username.
*   **Usage:**
    *   **Calls:** `find_one`
    *   **Called By:** *This function is not called by any other function listed in the provided context.*

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function updates the Gemini API key associated with a specific user in the database. It first ensures the security of the provided plain text API key by encrypting it using the `encrypt_text` utility. Subsequently, it performs a database update operation using `dbusers.update_one`, targeting the user identified by the `username` (mapped to the `_id` field). The function concludes by returning the count of documents that were successfully modified by the database operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user record in the database.
    - **gemini_api_key** (`str`): The new plain text Gemini API key provided by the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the database update operation.
*   **Usage:**
    *   **Calls:** `encrypt_text`, `update_one`
    *   **Called By:** *This function is not explicitly called by any other function listed in the provided context.*

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function is designed to update the Ollama Base URL associated with a specific user in the database. It takes the user's identifier and the new URL string as input. The function executes an update_one operation on the dbusers collection, setting the "ollama_base_url" field for the document matching the provided username (used as the MongoDB _id). Finally, it returns the count of documents successfully modified by the operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (used as the MongoDB _id) of the user whose URL needs updating.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service to be stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the database update operation (typically 0 or 1).
*   **Usage:**
    *   **Calls:** `update_one`
    *   **Called By:** *Based on the provided context, this function is not called by any other known functions.*

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** This function retrieves the Gemini API key associated with a specific user from a database collection named `dbusers`. It takes the user's identifier as input and performs a database lookup using the `find_one` method. The query is optimized to only return the `gemini_api_key` field. The function then safely extracts and returns this key using the dictionary's `.get()` method.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user's record in the database.
*   **Returns:**
    - **gemini_api_key** (`str or None`): The retrieved Gemini API key for the specified user, or None if the key is not present in the user's record.
*   **Usage:**
    *   **Calls:** `find_one`, `get`
    *   **Called By:** *This function is not called by any other analyzed functions in the provided context.*

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** This function is designed to retrieve the base URL for the Ollama service configured for a specific user. It accepts a 'username' string, which is used as the primary key to query the 'dbusers' database collection. The query is optimized to project only the 'ollama_base_url' field from the matching user document. The function then safely extracts and returns the value of this field using the dictionary's 'get' method.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to locate the user's record in the database.
*   **Returns:**
    - **ollama_base_url** (`str or None`): The base URL for the Ollama service associated with the user, or None if the field is not present in the database record.
*   **Usage:**
    *   **Calls:** `find_one`, `get`
    *   **Called By:** *This function is not called by any other functions listed in the provided context.*

#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** This function handles the deletion of a specific user record from a database collection, assumed to be a MongoDB collection named `dbusers`. It takes the user's username as input and uses it to construct a query targeting the `_id` field for deletion. The operation uses the `delete_one` method to ensure only a single matching record is removed. The function concludes by returning the count of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation, typically 1 if the user was found and deleted, or 0 otherwise.
*   **Usage:**
    *   **Calls:** `delete_one`
    *   **Called By:** *This function is not explicitly called by any other functions listed in the provided context.*

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function is responsible for fetching and decrypting API keys associated with a specific user. It queries the database (via an assumed global or imported object `dbusers`) using the provided username as the unique identifier. If no user record is found, the function immediately returns a tuple of two None values. If the user exists, it retrieves the potentially encrypted 'gemini_api_key' and decrypts it using the external `decrypt_text` function. It also retrieves the 'ollama_base_url' directly from the user object. The function returns both the decrypted Gemini key and the Ollama base URL.
*   **Parameters:**
    - **username** (`str`): The unique identifier used to look up the user in the database (mapped to the `_id` field).
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key string, or None if the user was not found.
    - **ollama_plain** (`str | None`): The Ollama base URL string, or None if the user was not found.
*   **Usage:**
    *   **Calls:** `decrypt_text`, `find_one`, `get`
    *   **Called By:** *This function is currently not referenced by any other functions in the provided context.*

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time)`
*   **Description:** This function is designed to insert a new exchange record into a database collection, likely named 'dbexchanges'. It accepts several mandatory parameters defining the core interaction (question, answer, feedback, user, and chat context) and several optional parameters related to model usage and timing. It constructs a dictionary containing all provided data along with a dynamically generated creation timestamp using `datetime.now()`. Finally, it executes the insertion operation and returns the unique identifier assigned by the database to the new record.
*   **Parameters:**
    - **question** (`str`): The text content of the question posed in the exchange.
    - **answer** (`str`): The text content of the answer generated for the question.
    - **feedback** (`str`): The feedback provided for the exchange (e.g., a rating or category).
    - **username** (`str`): The identifier of the user associated with this exchange.
    - **chat_name** (`str`): The name or identifier of the chat session where the exchange occurred.
    - **helper_used** (`str`): Optional. Specifies which helper model or component was used. Defaults to an empty string.
    - **main_used** (`str`): Optional. Specifies which main model or component was used. Defaults to an empty string.
    - **total_time** (`str`): Optional. The total time recorded for processing the exchange. Defaults to an empty string.
    - **helper_time** (`str`): Optional. The time recorded for the helper component's execution. Defaults to an empty string.
    - **main_time** (`str`): Optional. The time recorded for the main component's execution. Defaults to an empty string.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier (e.g., MongoDB ObjectId) assigned by the database to the newly created exchange record.
*   **Usage:**
    *   **Calls:** `insert_one`, `now`
    *   **Called By:** *This function is not called by any known functions in the provided context.*

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** This function is designed to query and retrieve all exchange records linked to a specific user identifier. It takes the username as input and uses it to filter documents within the 'dbexchanges' collection or database object. The database query is executed using the 'find' method, searching for documents where the "username" field matches the input. Finally, the cursor or iterable result is explicitly cast into a list before being returned.
*   **Parameters:**
    - **username** (`str`): The unique identifier string used to filter the exchange records in the database.
*   **Returns:**
    - **exchanges** (`list`): A list containing all exchange records (documents) retrieved from the database for the specified user.
*   **Usage:**
    *   **Calls:** `find`, `list`
    *   **Called By:** *This function is currently not referenced by any other functions in the provided context.*

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function is designed to retrieve conversation exchanges stored in a database. It takes a specific username and a chat name as input parameters. It constructs a query dictionary using these identifiers and executes a search against the `dbexchanges` collection using the `find` method. The results, which are typically returned as a cursor or iterable, are then explicitly converted into a standard Python list before being returned to the caller.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose exchanges are being fetched.
    - **chat_name** (`str`): The name or identifier of the specific chat session to filter exchanges by.
*   **Returns:**
    - **exchanges** (`list`): A list of database documents (exchanges) matching the provided username and chat name.
*   **Usage:**
    *   **Calls:** `find`, `list`
    *   **Called By:** *This function is not called by any other functions listed in the provided context.*

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function is designed to update the feedback score associated with a specific exchange record in a database. It accepts an identifier for the exchange and the new integer feedback value. The function executes a database update operation using `dbexchanges.update_one`, targeting the document whose `_id` matches the input `exchange_id` and setting its `feedback` field. It returns the count of documents that were successfully modified by the operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier used to locate the specific exchange record in the database.
    - **feedback** (`int`): The new integer value to be set as the feedback score for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation (typically 0 or 1).
*   **Usage:**
    *   **Calls:** `update_one`
    *   **Called By:** *This function is not called by any other functions listed in the provided context.*

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function updates the feedback message associated with a specific exchange record in the database. It accepts the unique identifier of the exchange and the new feedback message string. The function executes a database update operation, specifically calling `dbexchanges.update_one` to locate the document by its `_id` and set the `feedback_message` field. It returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier (likely a MongoDB ObjectId or string) used to locate the specific exchange document to be updated.
    - **feedback_message** (`str`): The new string content to be stored in the 'feedback_message' field of the exchange document.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation (typically 0 or 1).
*   **Usage:**
    *   **Calls:** `update_one`
    *   **Called By:** *This function is not called by any other function in the provided context.*

#### Function: `delete_chats_by_user`
*   **Signature:** `def delete_chats_by_user(username, chat_name)`
*   **Description:** This function is responsible for deleting all chat exchanges associated with a specific user and a specific chat name from the database. It constructs a query using the provided username and chat_name and executes a bulk deletion operation via dbexchanges.delete_many. The function returns the total number of documents that were successfully removed from the collection.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose chat exchanges should be deleted.
    - **chat_name** (`str`): The name of the specific chat thread from which exchanges should be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The total number of documents (chat exchanges) that were successfully deleted from the database collection.
*   **Usage:**
    *   **Calls:** `delete_many`
    *   **Called By:** *This function is not reported to be called by any other functions in the provided context.*

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function is designed to remove a single database record corresponding to a specific exchange. It accepts the unique identifier of the exchange (`exchange_id`) as input. The function executes a deletion operation using the `dbexchanges.delete_one` method, targeting the document where the `_id` field matches the provided ID. The function returns an integer representing the total number of documents successfully deleted by the operation, typically 0 or 1.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier (ID) of the exchange record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents successfully deleted by the operation (typically 0 or 1).
*   **Usage:**
    *   **Calls:** `delete_one`
    *   **Called By:** *This function is currently not referenced or called by any other analyzed functions in the provided context.*

---
### File: `frontend/Frontend.py`
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** This function initializes the Streamlit session state (`st.session_state`) by loading existing chat data associated with a specific user from the database. It first checks if the data has already been loaded (`"data_loaded"` flag) to prevent redundant database calls. If not loaded, it fetches exchanges using `db.fetch_exchanges_by_user(username)`, structures them into a dictionary grouped by chat name, and handles missing feedback values by setting them to `np.nan`. Finally, it ensures that at least one chat ("Chat 1") exists in the session state and sets the `active_chat` pointer, concluding by setting the `data_loaded` flag to `True`.
*   **Parameters:**
    - **username** (`str`): The user identifier used to fetch specific chat exchanges from the database.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `append`, `fetch_exchanges_by_user`, `get`, `keys`, `list`
    *   **Called By:** `<frontend/Frontend.py>`

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function handles the process of updating user feedback associated with a specific exchange object. It takes the exchange object (`ex`) and the new feedback value (`val`) as input. The function first updates the local state by setting the 'feedback' key of the exchange object. It then ensures persistence by calling a database utility, `db.update_exchange_feedback`, using the exchange's ID and the new value. Finally, it forces a complete application refresh by calling `st.rerun()`, likely within a Streamlit context.
*   **Parameters:**
    - **ex** (`dict`): The exchange object (likely a dictionary representing state or a database record) which contains the '_id' and 'feedback' keys to be updated.
    - **val** (`Any`): The new feedback value to be assigned to the exchange object and persisted in the database.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `rerun`, `update_exchange_feedback`
    *   **Called By:** `render_exchange`

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of a specific exchange object from both the persistent storage (database) and the application's current state (Streamlit session state). It first calls a database utility to delete the exchange using its unique identifier (`_id`). Subsequently, it removes the exchange object from the list of exchanges associated with the specified chat name in `st.session_state`. Finally, it forces a Streamlit rerun to ensure the user interface immediately reflects the deletion.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat whose exchanges list is being modified in the session state.
    - **ex** (`dict`): The exchange object to be deleted. It must contain the '_id' key, which is used for database deletion.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `delete_exchange_by_id`, `remove`, `rerun`
    *   **Called By:** `render_exchange`

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function handles the complete deletion of a chat identified by the provided username and chat name. It first executes a database deletion command via `db.delete_chats_by_user` and subsequently removes the chat entry from the Streamlit session state dictionary. Following the deletion, it manages the application's active chat state. If other chats are present, the first available chat key is selected as the new active chat. If the chat list becomes empty, a new default chat named "Chat 1" is initialized and set as active, ensuring the application always maintains a current context. The function concludes by forcing a Streamlit rerun to refresh the user interface.
*   **Parameters:**
    - **username** (`str`): The identifier of the user associated with the chat being deleted.
    - **chat_name** (`str`): The specific name or key of the chat to be removed from the database and session state.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `delete_chats_by_user`, `keys`, `len`, `list`, `rerun`
    *   **Called By:** *This function appears to be called from within the main Streamlit frontend file.*

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text)`
*   **Description:** This function processes a string of markdown text to identify and render embedded Mermaid diagram code blocks separately from standard text content. It uses a regular expression (`re.split`) to segment the input based on the ````mermaid ... ```` delimiters. The function iterates through the resulting parts, rendering standard text using `st.markdown` for even-indexed segments. For odd-indexed segments containing Mermaid code, it attempts graphical rendering via `st_mermaid`, generating a unique key based on the content and index. If the graphical rendering fails, the raw code is displayed using `st.code` instead. The function returns immediately if the input markdown text is empty.
*   **Parameters:**
    - **markdown_text** (`str`): The input text containing standard markdown content potentially interspersed with ````mermaid` code blocks.
*   **Returns:**
    - **None** (`None`): The function performs side effects (rendering content to a Streamlit interface) and does not return a meaningful value.
*   **Usage:**
    *   **Calls:** `code`, `enumerate`, `hash`, `markdown`, `split`, `st_mermaid`, `strip`
    *   **Called By:** `<frontend/Frontend.py>`, `render_exchange`

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function is responsible for rendering a single message exchange (user question and assistant answer) within a Streamlit chat interface. It first displays the user's question using `st.chat_message`. The assistant's response is rendered along with a comprehensive toolbar providing interactive features. The toolbar includes buttons for positive/negative feedback (calling `handle_feedback_change`), a popover for writing detailed feedback messages (which updates the database via `db.update_exchange_feedback_message` and triggers `st.rerun`), a download button for the answer content, and a button to delete the exchange (calling `handle_delete_exchange`). Finally, the assistant's answer is displayed in a scrollable container and processed by `render_text_with_mermaid`.
*   **Parameters:**
    - **ex** (`dict | object`): The exchange object containing the user's question, the assistant's answer, unique ID ('_id'), and current feedback status ('feedback', 'feedback_message').
    - **current_chat_name** (`str`): The name of the current chat session, required as context when calling the exchange deletion handler.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `button`, `caption`, `chat_message`, `columns`, `container`, `download_button`, `get`, `handle_delete_exchange`, `handle_feedback_change`, `popover`, `render_text_with_mermaid`, `rerun`, `sleep`, `success`, `text_area`, `update_exchange_feedback_message`, `write`
    *   **Called By:** *This function is utilized by other components within the `frontend/Frontend.py` module, likely as part of the main chat history rendering loop.*

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to strictly define the metadata for a single parameter within a function or method signature. It enforces the presence of three core attributes: the parameter's name, its data type, and a descriptive explanation of its purpose. This model is typically used within larger schemas to structure and validate documentation or analysis data.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class depends on `pydantic.BaseModel` for structured data validation and serialization capabilities.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated to accept and validate the three required fields: `name`, `type`, and `description`. All fields must be provided as strings upon instantiation, ensuring the parameter metadata is complete and correctly typed.
    *   *Parameters:*
        - **name** (`str`): The identifier or name of the function parameter.
        - **type** (`str`): The data type of the parameter, often inferred or explicitly typed.
        - **description** (`str`): A detailed explanation of the parameter's role and expected value.
*   **Methods:** *No methods defined.*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to strictly define the metadata associated with a function's return value. It acts as a schema for documenting the output, ensuring that the name, data type, and descriptive text are consistently captured. This structure is typically used within automated documentation or analysis pipelines to standardize function signature descriptions.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the context, but it is likely used within schema generation or documentation systems that require structured data definitions.
*   **Dependencies:** This class relies on the Pydantic library for its base functionality as it inherits from BaseModel.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is implicitly generated, requiring values for `name`, `type`, and `description` to initialize the data object. These attributes define the structure of the function's return value documentation.
    *   *Parameters:*
        - **name** (`str`): The identifier or name of the returned value.
        - **type** (`str`): The data type of the returned value (e.g., 'str', 'int', 'List[str]').
        - **description** (`str`): A detailed explanation of what the returned value represents.
*   **Methods:** *No methods defined.*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic data model used to structure and describe the calling context of a function or method. It serves as a container for two required string fields: one summarizing the external entities the function calls, and another summarizing where the function itself is called from. This model is typically nested within a larger analysis structure to provide context for code interactions.
*   **Instantiation:** The instantiation context for this class is not specified in the provided input.
*   **Dependencies:** This class relies on the BaseModel from the Pydantic library to enforce data structure and validation.
*   **Constructor:**
    *   *Description:* The class uses the Pydantic BaseModel constructor to initialize its two required string attributes, calls and called_by, ensuring data validation upon instantiation.
    *   *Parameters:*
        - **calls** (`str`): A human-readable summary describing the functions, methods, or classes that the analyzed entity invokes.
        - **called_by** (`str`): A human-readable summary describing the locations (functions, methods, or files) where the analyzed entity is utilized.
*   **Methods:** *No methods defined.*

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a structured data model, likely implemented using Pydantic's BaseModel, designed to hold a comprehensive analysis of a single Python function. It serves as a schema for documenting a function's behavior, signature, and usage context. This structure is essential for systems that automatically generate documentation or perform static analysis, ensuring all key aspects of a function are captured in a standardized format.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not appear to rely on external dependencies listed in the context, though it uses Pydantic's BaseModel internally.
*   **Constructor:**
    *   *Description:* This class, inheriting from Pydantic's BaseModel, is initialized by providing values for its four defined fields: a string summary of the function's purpose, a list of parameter descriptions, a list of return descriptions, and a usage context object. Pydantic handles the validation and assignment of these attributes upon instantiation.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the function's purpose and implementation.
        - **parameters** (`List[ParameterDescription]`): A list detailing the function's input arguments, including name, type, and description for each.
        - **returns** (`List[ReturnDescription]`): A list detailing the function's return values, including type and description.
        - **usage_context** (`UsageContext`): An object describing the calling context of the function, detailing what it calls and where it is called from.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic model designed to hold the complete structured analysis of a single Python function or method. It acts as the top-level container, ensuring that the function's name, its detailed behavioral description (via a nested `FunctionDescription` object), and any associated analysis errors are captured in a standardized format. This model is crucial for representing the output of the code analysis process.
*   **Instantiation:** The points of instantiation for this class are not specified in the provided context.
*   **Dependencies:** The class relies on the Pydantic BaseModel for data validation and structure definition.
*   **Constructor:**
    *   *Description:* The constructor is automatically generated by Pydantic based on the defined fields. It initializes the instance by requiring the function's identifier and its detailed description object, while allowing the error field to be optionally omitted.
    *   *Parameters:*
        - **identifier** (`str`): The unique name of the function being analyzed.
        - **description** (`FunctionDescription`): A nested object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional field used to store any error messages encountered during the analysis of the function.
*   **Methods:** *No methods defined.*

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic data model designed to encapsulate the analysis of a class's constructor (__init__ method). It is a structural component used within a larger system for code analysis and documentation generation. It strictly defines two fields: a string summary of the initialization process and a list of structured parameter descriptions, ensuring validated and standardized data representation for constructor metadata.
*   **Instantiation:** No specific instantiation points were provided in the context.
*   **Dependencies:** The class relies on Pydantic's BaseModel for its structure and validation capabilities, and it uses List for type hinting.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel. It initializes the instance attributes based on the provided keyword arguments, enforcing type validation for the constructor's textual summary (str) and the list of parameter descriptions (List[ParameterDescription]).
    *   *Parameters:*
        - **description** (`str`): A high-level textual summary detailing how the class is initialized.
        - **parameters** (`List[ParameterDescription]`): A list containing structured descriptions for every parameter accepted by the constructor.
*   **Methods:** *No methods defined.*

#### Class: `ClassContext`
*   **Summary:** ClassContext is a Pydantic data model derived from BaseModel. Its sole purpose is to structure and validate contextual metadata related to a Python class, specifically tracking its external dependencies and the points in the codebase where it is instantiated. It serves as a simple, typed container for usage context information, ensuring that dependency and instantiation details are provided as strings.
*   **Instantiation:** The provided context does not specify any locations where this class is instantiated.
*   **Dependencies:** This class does not appear to have explicit external dependencies listed in the provided context, though it relies on pydantic.BaseModel.
*   **Constructor:**
    *   *Description:* This class inherits from pydantic.BaseModel and uses Pydantic's implicit constructor. It is initialized by providing values for the `dependencies` and `instantiated_by` string fields, which define the class's external context.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class being analyzed.
        - **instantiated_by** (`str`): A string describing where the class being analyzed is primarily instantiated within the codebase.
*   **Methods:** *No methods defined.*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to structure the comprehensive analysis of a Python class. It acts as a data container for documentation generation, organizing the analysis into four key components: a high-level summary of the class's purpose, a detailed description of its constructor, a list of analyses for all its methods, and contextual information regarding its usage and dependencies.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class inherits from Pydantic's BaseModel, which is its primary structural dependency. No other functional dependencies are explicitly listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor is implicitly generated by Pydantic's BaseModel. It initializes the instance attributes based on the provided type hints, ensuring data validation and structure for the class analysis components: overall summary, constructor details, method analyses list, and usage context.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose and role.
        - **init_method** (`ConstructorDescription`): The structured analysis of the class's __init__ method.
        - **methods** (`List[FunctionAnalysis]`): A list containing the detailed analysis of every method defined within the class.
        - **usage_context** (`ClassContext`): Contextual information describing where the class is instantiated and its external dependencies.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the root structure for the structured output generated by the AI Code Analyst. It is a Pydantic model designed to encapsulate the complete analysis of a Python class, including its unique identifier, a detailed structural description (ClassDescription), and an optional field for reporting analysis errors. This structure ensures that the analysis output is standardized and machine-readable for downstream processing.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly rely on external dependencies listed in the context, but it inherits functionality from Pydantic's BaseModel and uses typing.Optional.
*   **Constructor:**
    *   *Description:* As a Pydantic model, ClassAnalysis is initialized by accepting keyword arguments corresponding to its fields. It requires an identifier string and a ClassDescription object, while the error field is optional and defaults to None.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifying the class being analyzed.
        - **description** (`ClassDescription`): A nested object containing the detailed analysis of the class, including methods and constructor.
        - **error** (`Optional[str]`): An optional field used to report any errors encountered during the analysis process. Defaults to None.
*   **Methods:** *No methods defined.*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class serves as a structured data model, inheriting from pydantic.BaseModel, designed to represent a single event of a function or class instantiation call within a relationship analyzer system. It encapsulates essential metadata about the call, including the source file, the name of the calling entity, the type of entity (mode), and the specific line number where the event occurred. This model is crucial for tracking dependencies and usage context across the codebase, particularly in 'called_by' and 'instantiated_by' lists.
*   **Instantiation:** The input context does not specify where the CallInfo class is instantiated.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the input context, but it relies on Pydantic for its core data modeling functionality.
*   **Constructor:**
    *   *Description:* The CallInfo class uses Pydantic's BaseModel to automatically generate a constructor. It initializes the instance attributes (file, function, mode, line) by accepting them as keyword arguments during instantiation, enforcing type validation based on the class annotations.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call occurred.
        - **function** (`str`): The name of the function or method performing the call.
        - **mode** (`str`): The type of calling entity (e.g., 'method', 'function', 'module').
        - **line** (`int`): The line number within the file where the call was made.
*   **Methods:** *No methods defined.*

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic data model used to structure and standardize the contextual information required for analyzing a specific function or method. It primarily serves as a container for two lists: one detailing the entities that the function calls, and another detailing the entities that call the function, using the external CallInfo structure. This model ensures consistent data handling for dependency mapping within a larger analysis system.
*   **Instantiation:** The instantiation context for this class is not provided in the input.
*   **Dependencies:** This class relies on the Pydantic BaseModel for data validation and structure, and utilizes the List type from the typing module. It also depends on the external type CallInfo.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is implicitly generated. It initializes the data structure by accepting keyword arguments corresponding to the defined type-annotated fields, ensuring that the input data conforms to the specified types (List[str] for calls and List[CallInfo] for called_by).
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing the names of functions, methods, or classes that the analyzed function calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects detailing the external functions or methods that call the analyzed function.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel defining the strict data structure required to initiate a function analysis task. It serves as a schema validator for incoming requests, ensuring that the necessary components
Gthe operational mode, function identifier, raw source code, associated imports, and contextual data
Gare all present and correctly typed before analysis proceeds.
*   **Instantiation:** The input context does not specify where this class is instantiated, suggesting it is likely used by API consumers or internal data processing pipelines to validate input payloads.
*   **Dependencies:** This class relies on Pydantic's BaseModel for data validation and structure, and uses typing utilities like Literal and List.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the class uses an implicit constructor to initialize its attributes based on the defined type-hinted fields. It requires five specific fields to be provided upon instantiation.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the operational mode, which is fixed to 'function_analysis' for this input type.
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **source_code** (`str`): The raw source code string of the function definition.
        - **imports** (`List[str]`): A list of import statements relevant to the function's execution context.
        - **context** (`FunctionContextInput`): Additional contextual data required for the analysis, structured by the FunctionContextInput schema.
*   **Methods:** *No methods defined.*

#### Class: `MethodContextInput`
*   **Summary:** MethodContextInput is a Pydantic data model used to encapsulate structured contextual information about a specific method. It defines fields necessary for deep analysis, including the method's unique identifier, a list of functions it calls, a list of entities that call it, its argument list, and its associated docstring. This model ensures consistency when passing method context data throughout the system.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class relies on external dependencies like Pydantic's BaseModel for data validation and structure, and standard Python typing utilities.
*   **Constructor:**
    *   *Description:* The constructor is automatically generated by Pydantic's BaseModel, requiring initialization values for all defined fields: identifier, calls, called_by, args, and docstring.
    *   *Parameters:*
        - **identifier** (`str`): The unique name of the method being described.
        - **calls** (`List[str]`): A list of identifiers for functions or methods called by this method.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects detailing where this method is invoked.
        - **args** (`List[str]`): A list of argument names accepted by the method.
        - **docstring** (`Optional[str]`): The documentation string associated with the method, which may be null.
*   **Methods:** *No methods defined.*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic data model used to structure all necessary contextual information required for analyzing a Python class. It serves as a container for metadata, including external dependencies, instantiation points, and method-specific context, ensuring a standardized input format for analysis systems.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not appear to rely on any specific external dependencies beyond Pydantic for its core functionality.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is implicitly generated, accepting keyword arguments corresponding to the defined fields. It initializes the structured context fields necessary for class analysis.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies relevant to the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list detailing the locations or contexts where the class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list providing structured context and analysis data for each method within the class.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput is a Pydantic data model that strictly defines the required structure for input data used to generate a ClassAnalysis object. It acts as a schema validator, ensuring that the raw data provided to the AI Code Analyst contains all necessary components, including the analysis mode, class identifier, source code, imports list, and contextual information, before the analysis pipeline proceeds.
*   **Instantiation:** There are no specific instantiation points listed in the provided context, suggesting it is likely instantiated by the main pipeline entry point that processes raw data for analysis.
*   **Dependencies:** This class relies on Pydantic's BaseModel for data validation and structure, and uses standard Python typing components like Literal and List.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the constructor is automatically generated. It initializes the instance attributes by validating and assigning the input data against the defined type hints and constraints, ensuring strict adherence to the required input schema.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): A literal string indicating the type of analysis being requested, which must be 'class_analysis'.
        - **identifier** (`str`): The name of the class that is being analyzed.
        - **source_code** (`str`): The raw source code string of the entire class definition.
        - **imports** (`List[str]`): A list of import statements found in the source file context.
        - **context** (`ClassContextInput`): A nested object containing contextual information, such as dependencies and usage context for the class and its methods.
*   **Methods:** *No methods defined.*

---
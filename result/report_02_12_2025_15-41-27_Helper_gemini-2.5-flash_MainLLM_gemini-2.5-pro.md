# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated documentation pipeline designed to analyze Git repositories. It clones a given repository, performs static code analysis using Abstract Syntax Trees (ASTs), and generates call graphs and file dependency structures. The collected data is then processed by a series of Large Language Models (a "Helper LLM" for detailed analysis and a "Main LLM" for final synthesis) to produce a comprehensive technical documentation report. The system includes a web-based frontend built with Streamlit for user interaction.
- **Key Features:**
  - Clones remote Git repositories for local analysis.
  - Performs static code analysis using Abstract Syntax Trees (ASTs).
  - Generates call graphs and file dependency diagrams to visualize code structure.
  - Utilizes a multi-LLM architecture for detailed code summarization and final report generation.
  - Features a Streamlit-based web interface for user input and interaction.
- **Tech Stack:** LangChain, Streamlit, NetworkX, Pydantic, PyMongo, Google Gemini, OpenAI GPT, Ollama.

*   **Repository Structure:**
    ```mermaid
    graph LR;
        subgraph root;
            direction LR;
            id1[".env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt"];
        end

        subgraph SystemPrompts;
            direction LR;
            id2["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt"];
        end

        subgraph backend;
            direction LR;
            id3["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py"];
        end

        subgraph database;
            direction LR;
            id4["db.py"];
        end

        subgraph frontend;
            direction LR;
            id5["Frontend.py<br/>__init__.py<br/>gifs/4j.gif"];
        end

        subgraph notizen;
            direction LR;
            id6["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken/...<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"];
        end
        
        subgraph result;
            direction LR;
            id7["report_...md<br/>..."];
        end

        subgraph schemas;
            direction LR;
            id8["types.py"];
        end
        
        subgraph statistics;
            direction LR;
            id9["savings_...png"];
        end

        root --> id1;
        root --> SystemPrompts;
        root --> backend;
        root --> database;
        root --> frontend;
        root --> notizen;
        root --> result;
        root --> schemas;
        root --> statistics;
    ```

    ## 2. Installation
    ### Dependencies
    To install the required dependencies, run the following command:
    ```bash
    pip install -r requirements.txt
    ```
    Key dependencies include:
    - altair
    - langchain
    - langgraph
    - streamlit
    - streamlit-authenticator
    - networkx
    - pymongo
    - GitPython
    - toon_format
    - pydantic
    - openai
    - ollama
    - google-generativeai

    ### Setup Guide
    [Could not be determined due to a missing README file and insufficient context.]
    ### Quick Startup
    [Could not be determined due to a missing README file and insufficient context.]

    ## 3. Use Cases & Commands
    The primary use case for this project is to automatically generate technical documentation for a software repository. The user interacts with the system through a web interface.

    **Primary Use Case:**
    1.  Launch the web application.
    2.  Provide the URL of a public Git repository.
    3.  Input the necessary API keys for the selected Large Language Models (e.g., Gemini, OpenAI).
    4.  Initiate the analysis process.
    5.  The application will clone the repository, perform static analysis, use LLMs to interpret the code, and generate a comprehensive Markdown report.

    **Primary Command:**
    To run the application, execute the following command from the project's root directory:
    ```bash
    streamlit run frontend/Frontend.py
    ```

    ## 4. Architecture
    *Architecture diagrams are not yet available for this project.*



## 5. Code Analysis
### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) of Python source code. Its primary purpose is to extract structured information about imports, classes, and functions within a given Python file. It builds a `schema` dictionary that categorizes these elements, including details like identifiers, docstrings, and source code segments. The visitor correctly distinguishes between top-level functions and methods nested within classes, providing a comprehensive representation of the code's structure.
*   **Instantiation:** This class is instantiated by the `analyze_repository` function in `AST_Schema.py`.
*   **Dependencies:** This class depends on the `ast` module for AST traversal and `path_to_module` for resolving module paths.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTVisitor with the raw source code, the file's absolute path, and the project's root directory. It calculates the module path based on these inputs and sets up an empty schema dictionary to store parsed imports, functions, and classes. It also initializes an internal `_current_class` attribute to `None` for tracking the current class being visited during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being visited.
        - **file_path** (`str`): The absolute path to the file being visited.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes `ast.Import` nodes, which represent top-level import statements (e.g., `import module`). It iterates through each alias defined in the import statement and appends the module's name to the `imports` list within the `self.schema` dictionary. After processing the current node, it calls `self.generic_visit` to ensure that traversal continues to any child nodes.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent `from ... import ...` statements. It iterates through the aliases within the import statement, constructs a fully qualified import string (e.g., `node.module.alias.name`), and appends it to the `imports` list in `self.schema`. Following this, it invokes `self.generic_visit` to ensure proper traversal of any nested AST nodes.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions in the source code. It constructs a unique identifier for the class, extracts its name, docstring, and the source code segment. This information is then compiled into a `class_info` dictionary and appended to the `classes` list within `self.schema`. It temporarily sets `self._current_class` to this `class_info` to correctly associate nested methods, calls `generic_visit` to traverse the class's body, and then resets `_current_class` to `None`.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, representing both top-level functions and methods within classes. It checks if `_current_class` is set to determine if the function is a method; if so, it appends method-specific context to the current class's `method_context`. Otherwise, it treats it as a top-level function, extracting its details and appending them to the `functions` list in `self.schema`. Finally, it calls `self.generic_visit` to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method processes `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. It acts as a simple proxy, delegating the actual processing of the asynchronous function node directly to the `visit_FunctionDef` method. This ensures that asynchronous functions are handled consistently with regular functions for the purpose of schema generation.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
            *This method does not return a value.*

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to perform static analysis on a Python code repository. Its primary function is to parse Python files, extract Abstract Syntax Tree (AST) nodes, build call graphs, and then consolidate this information into a structured schema. It also provides functionality to merge external relationship data, such as "called by" or "instantiated by" information, into the generated schema, thereby providing a holistic view of code structure and interdependencies.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py at line 166.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments upon instantiation.
    *   *Parameters:*
        *This method has no parameters.*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* This static method enriches an existing schema dictionary with call graph information. It iterates through functions and classes within the schema, using a NetworkX directed graph (`call_graph`) to find successors (calls) and predecessors (called by) for each function or method. The method updates the `context` field of functions and `method_context` of classes with sorted lists of calls and callers.
        *   *Parameters:*
            - **schema** (`dict`): The schema dictionary containing function and class definitions to be enriched.
            - **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships.
            - **filename** (`str`): The name of the file being processed, used to construct unique identifiers for functions/methods in the call graph.
        *   *Returns:*
            *This method does not return a value.*
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
        *   *Description:* This method takes a `full_schema` and a list of `relationship_data` and merges the "called by" and "instantiated by" information into the `full_schema`. It first creates a lookup dictionary from the `relationship_data` for efficient access. Then, it iterates through files, functions, and classes within the `full_schema` to update their respective `context` fields with the relevant relationship data.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): The complete schema dictionary to be updated.
            - **relationship_data** (`list`): A list of dictionaries, each containing an 'identifier' and 'called_by' (or similar relationship) information.
        *   *Returns:*
            - **full_schema** (`dict`): The updated `full_schema` dictionary with merged relationship data.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files)`
        *   *Description:* This method analyzes a list of file objects representing a code repository to build a comprehensive AST-based schema. It initializes an empty schema, determines the project root, and then iterates through each Python file. For each file, it parses the content into an AST, uses an `ASTVisitor` to extract schema nodes, builds a call graph, and then enriches the schema with call graph data using `_enrich_schema_with_callgraph`. Files that cannot be parsed or are empty are skipped, and parsing errors are caught and printed as warnings.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): A list of file objects, each expected to have `path` and `content` attributes.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the full AST schema of the analyzed repository, organized by file path.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into a Python module path string. It first attempts to calculate a relative path from a specified project root, falling back to just the basename if a ValueError occurs. It then removes the '.py' extension if present and replaces file path separators with dots. Finally, it handles '__init__' modules by removing the '.__init__' suffix to yield the package name.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The Python module path string derived from the input filepath.
*   **Usage:**
    *   **Calls:** `basename`, `endswith`, `relpath`, `replace`
    *   **Called By:** `AST_Schema.py::__init__`

---
### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is an AST NodeVisitor designed to analyze Python source code files and build a dictionary of file-level import dependencies. It traverses the Abstract Syntax Tree of a given Python file, specifically looking for 'import' and 'from ... import ...' statements. It handles both absolute and relative imports, using a sophisticated mechanism to resolve relative imports by checking file system existence and '__init__.py' exports. The class maintains an 'import_dependencies' dictionary, mapping the analyzed filename to a set of its direct module dependencies.
*   **Instantiation:** This class is instantiated by the 'build_file_dependency_graph' function, located in 'File_Dependency.py' at line 159.
*   **Dependencies:** This class relies on external modules such as networkx, os, ast components (Assign, AST, ClassDef, FunctionDef, Import, ImportFrom, Name, NodeVisitor, literal_eval, parse, walk), keyword (iskeyword), pathlib (Path), getRepo.GitRepository, and collections (defaultdict).
*   **Constructor:**
    *   *Description:* This constructor initializes the FileDependencyGraph instance with the filename of the file being analyzed and the repository's root directory. It stores these as instance attributes, `self.filename` and `self.repo_root`, which are essential for the subsequent dependency analysis and path resolution processes.
    *   *Parameters:*
        - **filename** (`str`): The path to the file currently being analyzed for dependencies.
        - **repo_root** (`Any`): The root directory of the repository, used for resolving relative paths and locating files.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This private method is responsible for resolving relative import statements, such as 'from .. import name'. It calculates the base directory for the import based on the current file's path and the specified import level. The method then checks for the actual existence of imported modules or symbols by searching for corresponding '.py' files or '__init__.py' files that export the symbol, utilizing internal helper functions like 'module_file_exists' and 'init_exports_symbol'. If no modules or symbols can be successfully resolved, an ImportError is raised to indicate the failure.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names that correspond to the relative import.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method, part of the AST NodeVisitor pattern, is invoked when an 'Import' or 'ImportFrom' AST node is encountered. Its primary function is to record file-level dependencies by adding the imported module's base name to the 'import_dependencies' dictionary. The dictionary uses the current 'self.filename' as the key and stores dependencies in a set to prevent duplicates. After processing the import, it calls 'generic_visit' to ensure continued traversal of the AST.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing the import statement.
            - **base_name** (`str | None`): An optional base name for the module, typically provided when the module name is already resolved from an 'ImportFrom' statement.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method, also part of the NodeVisitor pattern, specifically handles 'ImportFrom' AST nodes. It first attempts to extract an explicit module name (e.g., 'from a.b.c import d'), taking the last part ('c') and passing it to 'visit_Import'. If no explicit module name is present, indicating a relative import (e.g., 'from .. import x'), it invokes the '_resolve_module_name' helper to determine the actual module paths. Upon successful resolution, it then calls 'visit_Import' for each identified base name. Any failures during relative import resolution are caught and printed as an error. Finally, it calls 'generic_visit' to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            *This method does not return a value.*

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It initializes a `networkx.DiGraph` and uses a `FileDependencyGraph` visitor to traverse the provided Abstract Syntax Tree (AST) of a given file. The visitor collects import dependencies, which are then used to populate the graph with nodes (files) and edges (dependencies). The resulting graph illustrates which files import from others.
*   **Parameters:**
    - **filename** (`str`): The name of the file for which to build the dependency graph.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed for dependencies.
    - **repo_root** (`str`): The root directory path of the repository, used for resolving file paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies between them.
*   **Usage:**
    *   **Calls:** `DiGraph`, `FileDependencyGraph`, `add_edge`, `add_node`, `add_nodes_from`, `items`, `visit`
    *   **Called By:** `File_Dependency.py::build_repository_graph`

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a global directed graph representing file-level dependencies across all Python files within a given Git repository. It iterates through each Python file, parses its content into an Abstract Syntax Tree (AST), and then uses a helper function to build a dependency graph for that individual file. The nodes and edges from each file's graph are subsequently merged into a single, comprehensive global graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to extract and analyze Python files.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent Python files (or entities within them) and edges represent dependencies between them across the entire repository.
*   **Usage:**
    *   **Calls:** `DiGraph`, `add_edge`, `add_node`, `basename`, `build_file_dependency_graph`, `endswith`, `get_all_files`, `parse`, `removesuffix`, `str`
    *   **Called By:** `File_Dependency.py::backend.File_Dependency`

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function takes a directory path as input and recursively searches for all Python files within that directory and its subdirectories. It converts the input directory to an absolute path and then collects all files ending with '.py'. The paths of the found files are then made relative to the initial root directory before being returned.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory from which to start scanning for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of Path objects, where each path represents a Python file found within the specified directory, relative to the input 'directory'.
*   **Usage:**
    *   **Calls:** `Path`, `relative_to`, `resolve`, `rglob`
    *   **Called By:** `File_Dependency.py::_resolve_module_name`

#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G: nx.DiGraph)`
*   **Description:** This function converts a NetworkX directed graph, where nodes represent file paths, into a Mermaid diagram string. It processes the graph to identify folder structures, creating Mermaid subgraphs for each folder. Files within these folders are represented as nodes inside their respective subgraphs, while files in the root directory are represented as top-level nodes. Finally, the function iterates through the graph's edges to add directed dependency arrows between the corresponding file nodes in the Mermaid syntax.
*   **Parameters:**
    - **G** (`nx.DiGraph`): The NetworkX directed graph where nodes are expected to be strings representing file paths (e.g., 'folder/subfolder/file.py') and edges represent dependencies between these files.
*   **Returns:**
    - **mermaid_diagram_string** (`str`): A string containing the complete Mermaid diagram syntax, including 'graph TD' declaration, subgraphs for folders, file nodes, and directed edges representing dependencies.
*   **Usage:**
    *   **Calls:** `append`, `defaultdict`, `items`, `join`, `replace`, `split`
    *   **Called By:** `File_Dependency.py::backend.File_Dependency`

---
### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs) like Google Gemini, OpenAI GPT, or Ollama, specifically for generating structured documentation for Python functions and classes. It manages API keys, loads specific system prompts for different analysis types, and configures LLM clients with Pydantic-based structured output. The class is designed to handle batch processing of requests, incorporating rate limiting and error handling to ensure efficient and reliable documentation generation.
*   **Instantiation:** This class is instantiated by the `main_orchestrator` function in `HelperLLM.py` and the `main_workflow` function in `main.py`.
*   **Dependencies:** This class does not explicitly list external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper instance by setting up the API key, loading system prompts from specified file paths, and configuring the underlying LLM model (Gemini, OpenAI, or Ollama) based on the `model_name`. It also sets up structured output parsers for function and class analysis using Pydantic schemas and configures batch processing settings.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the chosen LLM service (Gemini, OpenAI).
        - **function_prompt_path** (`str`): Path to the file containing the system prompt for function analysis.
        - **class_prompt_path** (`str`): Path to the file containing the system prompt for class analysis.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
        - **ollama_base_url** (`str | None`): The base URL for Ollama if an Ollama model is used (default: `None`).
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method dynamically sets the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It assigns specific batch sizes for various Gemini, Llama, and GPT models to optimize API calls and respect rate limits. If an unknown model name is provided, it defaults to a conservative batch size of 2 and logs a warning.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
            *This method does not return a value.*
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method takes a list of `FunctionAnalysisInput` objects, converts them into JSON payloads, and then constructs conversations for the LLM. It processes these conversations in batches, calling the `function_llm` to generate and validate function documentation. The method includes error handling for batch calls and implements a waiting period between batches to manage API rate limits, returning a list of `FunctionAnalysis` objects or `None` for failed items.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing data for function analysis.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, where each object represents the validated documentation for a function, or `None` if an error occurred during processing.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating and validating documentation for a collection of classes. It takes a list of `ClassAnalysisInput` objects, converts them into JSON format, and then prepares them as LLM conversations with a system prompt. The method processes these conversations in batches, invoking the `class_llm` to obtain structured `ClassAnalysis` outputs. It includes robust error handling for API calls and incorporates a delay between batches to comply with rate limits, returning a list of `ClassAnalysis` objects or `None` for any failed entries.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing data for class analysis.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, where each object represents the validated documentation for a class, or `None` if an error occurred during processing.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a self-contained test and demonstration of the LLMHelper class's functionality. It defines dummy data for function analysis inputs and pre-computed analysis results, then simulates the process of generating documentation for these functions using the LLMHelper. The function initializes the helper, processes the mock inputs, and prints the final aggregated documentation to the console.
*   **Parameters:**
    *This method has no parameters.*
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `ClassAnalysisInput`, `ClassContextInput`, `LLMHelper`, `dumps`, `generate_for_functions`, `info`, `model_dump`, `model_validate`, `print`, `warning`
    *   **Called By:** `HelperLLM.py::backend.HelperLLM`

---
### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class provides a unified interface for interacting with various Large Language Models (LLMs), including Google Gemini, OpenAI GPT (via Google Generative AI), and Ollama. It manages the initialization of the specific LLM client based on the provided model name and handles the loading of a system prompt from a file. The class offers methods for both direct, synchronous LLM calls and streaming responses, abstracting the underlying LLM provider for consistent interaction.
*   **Instantiation:** This class is instantiated by the `main_workflow` function in `main.py`.
*   **Dependencies:** The class depends on `logging` for output, `langchain_google_genai.ChatGoogleGenerativeAI` for Google-based LLMs, `langchain_ollama.ChatOllama` for Ollama-based LLMs, and `langchain.messages.HumanMessage` and `langchain.messages.SystemMessage` for constructing LLM prompts.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes the MainLLM instance by configuring the chosen Large Language Model (LLM) client and loading the system prompt. It validates the provided API key, reads the system prompt from a specified file path, and sets up either a `ChatGoogleGenerativeAI` or `ChatOllama` instance based on the `model_name` parameter. If the prompt file is not found, it raises an error.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service, such as Gemini or OpenAI.
        - **prompt_file_path** (`str`): The file path to the text file containing the system-level instructions or context for the LLM.
        - **model_name** (`str`): The identifier for the specific LLM model to be used (e.g., 'gemini-2.5-pro', 'gpt-4', 'llama2'). Defaults to 'gemini-2.5-pro'.
        - **ollama_base_url** (`str`): The base URL for the Ollama server if an Ollama model is selected. Can be `None` to use a default.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* The `call_llm` method sends a user's input to the configured Large Language Model (LLM) and retrieves a single, complete response. It constructs a list of messages, including the class's system prompt and the provided user input, then invokes the LLM. The method includes logging for the call process and error handling to catch exceptions, returning the LLM's content or `None` on failure.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be processed by the LLM.
        *   *Returns:*
            - **content** (`str | None`): The textual content of the LLM's response, or `None` if an error occurred during the call.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* The `stream_llm` method provides a streaming interface to the configured Large Language Model (LLM), yielding chunks of the response as they become available. It prepares the input messages, including the system prompt and user input, and then uses the LLM's streaming capability. The method logs the streaming process and includes error handling to yield an error message if an exception occurs during the stream.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message for which a streaming response is desired from the LLM.
        *   *Returns:*
            - **chunk.content** (`str`): Yields individual content chunks from the LLM's streaming response.
            - **error_message** (`str`): Yields an error message string if an exception occurs during the LLM stream call.

---
### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The `ProjektInfoExtractor` class is designed to systematically extract fundamental project information from common project files such as README, pyproject.toml, and requirements.txt. It acts as an orchestrator, prioritizing information sources to build a comprehensive overview of a project, including its title, description, features, tech stack, status, and installation details. The class maintains an internal dictionary to store and update this extracted information.
*   **Instantiation:** This class is instantiated by the `main_workflow` function in `main.py`.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the `ProjektInfoExtractor` instance by setting a default placeholder string, `INFO_NICHT_GEFUNDEN`, for missing information. It also sets up the `self.info` dictionary with a predefined structure for project overview and installation details, populating all fields with this placeholder string.
    *   *Parameters:*
        *This method has no parameters.*
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches through a provided list of file objects to find one whose path ends with any of the specified patterns. The search is case-insensitive for both the file path and the patterns. It iterates through each file and pattern, returning the first matching file object found.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of string patterns (e.g., file extensions or names) to match against file paths.
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have a `path` attribute.
        *   *Returns:*
            - **None** (`Optional[Any]`): The first file object from `dateien` whose path matches any of the `patterns` (case-insensitively), or `None` if no match is found.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private helper method extracts a specific text section from a Markdown string. It identifies sections by looking for level 2 headings (##) that match any of the provided keywords (case-insensitively). It then captures all content following that heading until the next level 2 heading or the end of the document.
        *   *Parameters:*
            - **inhalt** (`str`): The complete Markdown text content.
            - **keywords** (`List[str]`): A list of alternative keywords that could serve as the section title (e.g., 'Installation', 'Setup').
        *   *Returns:*
            - **None** (`Optional[str]`): The extracted text content under the matched Markdown heading, with leading/trailing whitespace removed, or `None` if no matching section is found.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This private method parses the content of a README file to populate various project information fields within the `self.info` dictionary. It first attempts to extract the project title from a level 1 heading (`#`). It then extracts a general description and uses `_extrahiere_sektion_aus_markdown` to find and populate fields like 'Key Features', 'Tech Stack', 'Current Status', 'Setup Instructions', and 'Quick Start Guide' based on predefined keywords. Information is only updated if it's currently marked as 'Information not found'.
        *   *Parameters:*
            - **inhalt** (`str`): The full content of the README file.
        *   *Returns:*
            *This method does not return a value.*
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This private method parses the content of a `pyproject.toml` file. It attempts to load the TOML content using `tomllib` and then extracts the project `name`, `description`, and `dependencies` from the `[project]` table. It prioritizes TOML data, overwriting existing `self.info` values if found. It includes a warning if `tomllib` is not available or if there's a parsing error.
        *   *Parameters:*
            - **inhalt** (`str`): The full content of the `pyproject.toml` file.
        *   *Returns:*
            *This method does not return a value.*
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This private method parses the content of a `requirements.txt` file. It extracts non-empty, non-comment lines as project dependencies. This method only updates the `dependencies` field in `self.info` if it has not already been populated by a higher-priority source (like `pyproject.toml`), ensuring that TOML data takes precedence.
        *   *Parameters:*
            - **inhalt** (`str`): The full content of the `requirements.txt` file.
        *   *Returns:*
            *This method does not return a value.*
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This is the main public method that orchestrates the extraction of project information. It first identifies relevant project files (README, pyproject.toml, requirements.txt) using `_finde_datei`. It then parses these files in a specific order of priority: `pyproject.toml` first for core metadata, then `requirements.txt` for dependencies (as a fallback), and finally `README` for descriptive texts. After parsing, it formats the dependencies list into a single string and derives a default project title from the `repo_url` if not already set.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of `RepoFile` objects (or similar) containing file paths and content.
            - **repo_url** (`str`): The URL of the repository, used to derive a default project title.
        *   *Returns:*
            - **info** (`Dict[str, Any]`): A dictionary containing all extracted project information, including overview details and installation instructions.

---
### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST NodeVisitor designed to construct a directed call graph for Python source code. It traverses the Abstract Syntax Tree (AST) of a given file, identifying function and method definitions, and recording calls between them. The class manages the current scope (filename, class, function) to create fully qualified names for nodes in the graph, ultimately building a NetworkX DiGraph representing the call relationships.
*   **Instantiation:** This class is instantiated by the `build_callGraph` function in `callgraph.py` at line 165.
*   **Dependencies:** This class relies on the `ast` module for its base functionality as an AST visitor and `networkx` for constructing the directed graph. It also uses standard Python data structures like `dict` and `set`.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph visitor with the filename being analyzed. It sets up internal state variables to track the current function and class context during AST traversal. It also initializes a NetworkX directed graph, a dictionary for import mappings, a set for function names, and a dictionary to store edges (caller-callee relationships).
    *   *Parameters:*
        - **filename** (`str`): The name of the file currently being analyzed by the AST visitor.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively extracts the base names of called functions or methods from an AST node. It handles `ast.Call` nodes by recursing on the `func` attribute, `ast.Name` nodes by extracting the `id`, and `ast.Attribute` nodes by extracting the `attr`. The method aims to get to the innermost callable name, returning a list of potential callee names.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a call, name, or attribute from which to extract callee names.
        *   *Returns:*
            - **all_calls** (`list[str]`): A list of strings, where each string is a raw (unresolved) name of a function or method being called.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private helper method takes a list of raw callee names and resolves them into fully qualified names. It prefixes each raw callee with the `filename` and, if applicable, the `current_class` to create a unique identifier for the callee within the project's context. This ensures that calls are accurately mapped in the call graph.
        *   *Parameters:*
            - **callee_nodes** (`list[str]`): A list of raw (unresolved) callee names extracted from an AST node.
        *   *Returns:*
            - **resolved_callees** (`list[str]`): A list of fully qualified callee names, including filename and class context.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This private helper method constructs a fully qualified name for a function or method. It combines the `filename`, an optional `class_name`, and the `basename` of the function/method using a '::' separator. This standardized naming convention helps in creating unique identifiers for nodes in the call graph.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method (e.g., 'my_function').
            - **class_name** (`str | None`): The name of the class if the function is a method, otherwise None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name (e.g., 'filename::ClassName::methodName' or 'filename::functionName').
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self, )`
        *   *Description:* This private helper method determines the identifier for the current calling context. If `self.current_function` is set, it returns that value, indicating a function or method is the caller. Otherwise, it returns a placeholder string, either '<filename>' if a filename is available or '<global-scope>' if not, to represent calls made from the global scope.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **caller_identifier** (`str`): The fully qualified name of the current function/method or a global scope placeholder.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method, part of the AST visitor pattern, processes `ast.ClassDef` nodes. It temporarily updates `self.current_class` to the name of the class being visited, allowing nested function definitions to correctly form their fully qualified names. After traversing all functions within the class body, it restores the previous `self.current_class` value to maintain correct scope.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, representing regular function definitions. It constructs the fully qualified name for the function using `_make_full_name`, adds this name as a node to the NetworkX graph, and then uses `generic_visit` to traverse the function's body. Finally, it adds the function's full name to `function_set` and resets `self.current_function`.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method handles `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. It delegates its processing directly to `visit_FunctionDef`. This approach ensures that asynchronous functions are treated identically to regular functions for the purpose of call graph construction, simplifying the logic.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method processes `ast.Call` nodes, which represent function or method invocations. It identifies the `caller` using `_current_caller` and extracts `raw_callees` using `_recursive_call`. These raw names are then resolved into fully qualified names via `_resolve_all_callee_names`. Finally, it adds edges to the `self.edges` dictionary, linking the caller to each resolved callee, and includes error handling for unexpected issues during call processing.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method processes `ast.If` nodes, specifically looking for the `if __name__ == "__main__"` block. When such a block is identified, it temporarily sets `self.current_function` to '<main_block>'. This ensures that any function calls made directly within this main execution block are correctly attributed to a special '<main_block>' node in the call graph, providing clear context for global-level execution.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing an 'if' statement.
        *   *Returns:*
            *This method does not return a value.*

#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree: ast.AST, filename: str)`
*   **Description:** This function constructs a call graph from a given Python Abstract Syntax Tree (AST). It utilizes a `CallGraph` visitor to traverse the AST and identify function and method calls. The resulting graph is a directed graph (networkx.DiGraph) where nodes represent functions, methods, and the global scope, and edges signify calls between these entities. After visiting the AST, it iterates through the collected edges and adds them to the graph before returning the complete call graph.
*   **Parameters:**
    - **tree** (`ast.AST`): Der AST der zu analysierenden Python-Datei.
    - **filename** (`str`): Der Name der analysierten Datei, z. B. `"main.py"` oder `"src/utils.py"`.
*   **Returns:**
    - **graph** (`nx.DiGraph`): Der vollständige Call-Graph.
*   **Usage:**
    *   **Calls:** `CallGraph`, `add_edge`, `items`, `visit`
    *   **Called By:** `AST_Schema.py::analyze_repository`, `callgraph.py::build_global_callgraph`

#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph: nx.DiGraph)`
*   **Description:** This function converts a networkx.DiGraph object, representing a call graph, into a JSON-serializable adjacency list. It iterates through all nodes in the graph, ensuring a consistent output by sorting them. For each node, it retrieves its direct successors (callees), sorts them, and then adds an entry to the adjacency list if the node has any successors. The resulting dictionary maps each caller node to a list of its called nodes.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The directed graph (networkx.DiGraph) that needs to be converted into an adjacency list.
*   **Returns:**
    - **adj_list** (`Dict[str, list[str]]`): An adjacency list represented as a dictionary, where keys are caller nodes (strings) and values are lists of callee nodes (strings). This list is designed to be JSON-serializable.
*   **Usage:**
    *   **Calls:** `list`, `nodes`, `sorted`, `successors`
    *   **Called By:** *Not called by any function in the provided context.*

#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(repo: GitRepository)`
*   **Description:** This function aims to construct a global call graph for a given Git repository. It iterates through all files within the repository, filtering for Python files. For each Python file, it parses the content into an Abstract Syntax Tree (AST) and builds a file-specific call graph. These individual file call graphs are then merged into a single `networkx.DiGraph` object, which represents the aggregated call relationships across the entire repository.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which to extract files and build the call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the global call graph of the repository, where nodes are functions/methods and edges indicate call relationships.
*   **Usage:**
    *   **Calls:** `DiGraph`, `add_edge`, `add_node`, `basename`, `build_callGraph`, `endswith`, `get_all_files`, `parse`, `removesuffix`, `str`
    *   **Called By:** `callgraph.py::backend.callgraph`
> **Warning:** The variable 'repository' used in 'repository.get_all_files()' is not defined within the function's scope or as an explicit import. It appears to be an undeclared variable or a typo for the 'repo' parameter.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and a file path, then generates a DOT file representation of the graph. It first creates a copy of the input graph. To ensure compatibility with the DOT format, it relabels all nodes with safe, sequential identifiers (e.g., "n0", "n1"). The original node names are preserved by assigning them as a 'label' attribute to the newly relabeled nodes. Finally, the modified graph is written to the specified output path as a DOT file.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The input directed graph whose node names may contain characters incompatible with the DOT file format.
    - **out_path** (`str`): The file path where the DOT representation of the graph will be saved.
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `copy`, `enumerate`, `items`, `list`, `nodes`, `relabel_nodes`, `write_dot`
    *   **Called By:** `callgraph.py::backend.callgraph`

---
### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, designed for efficient access to file metadata and content through lazy loading. It encapsulates the file's path and its associated Git tree, providing properties to retrieve the Git blob, its decoded content, and its size only when they are first accessed. The class also offers utility methods for basic content analysis and for converting its data into a dictionary format.
*   **Instantiation:** This class is instantiated by the get_all_files method in getRepo.py.
*   **Dependencies:** This class does not explicitly depend on other components in the provided context.
*   **Constructor:**
    *   *Description:* The __init__ method initializes a RepoFile object by setting its path and storing the commit_tree. It also sets up internal attributes _blob, _content, and _size to None, indicating that these will be loaded lazily upon their first access.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Git Tree object from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self, )`
        *   *Description:* This property implements lazy loading for the Git blob object corresponding to the file. It checks if _blob is already populated; if not, it attempts to retrieve the blob from the stored _tree using the file's path. If the file is not found, it raises a FileNotFoundError.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
    *   **`content`**
        *   *Signature:* `def content(self, )`
        *   *Description:* This property provides the decoded content of the file, employing a lazy loading mechanism. It first checks if the _content attribute is already set. If not, it accesses the blob property to get the Git blob, reads its data stream, and decodes it using UTF-8, ignoring any decoding errors.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
    *   **`size`**
        *   *Signature:* `def size(self, )`
        *   *Description:* This property provides the size of the file in bytes, utilizing lazy loading. It checks if the _size attribute is already populated. If not, it retrieves the size attribute directly from the Git blob object associated with the file.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self, )`
        *   *Description:* This method serves as an example analysis, calculating the total number of words within the file's content. It achieves this by accessing the content property, splitting the resulting string by whitespace, and then counting the number of elements in the generated list.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **word_count** (`int`): The total number of words in the file content.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self, )`
        *   *Description:* This special method defines the official string representation of the RepoFile object. It returns a formatted string that includes the class name and the file's path, which is useful for debugging and logging.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, including its path.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method serializes the RepoFile object into a dictionary format, providing structured metadata about the file. It includes the file's full path, its base name, its size, and a fixed type "file". An optional include_content parameter allows for the file's actual content to be added to the dictionary.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the file's content will be included in the dictionary.
        *   *Returns:*
            - **file_data** (`dict`): A dictionary containing file metadata and optionally its content.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a comprehensive interface for managing Git repositories. It handles the entire lifecycle from cloning a remote repository into a temporary local directory to providing structured access to its contents. The class allows users to retrieve all files, organize them into a hierarchical tree structure, and ensures proper cleanup of temporary resources through its context manager implementation. This makes it ideal for tasks requiring programmatic interaction with Git repository data.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py.
*   **Dependencies:** This class depends on tempfile for creating temporary directories, shutil (though commented out for actual deletion) for directory operations, git.Repo and git.GitCommandError for Git interactions, and logging for informational messages. It also implicitly depends on RepoFile for file representation.
*   **Constructor:**
    *   *Description:* This constructor initializes a GitRepository instance by cloning a specified remote Git repository into a temporary local directory. It sets up essential attributes such as the repository URL, the path to the temporary directory, and the `git.Repo` object. It also captures the latest commit and its tree, handling potential `GitCommandError` during cloning by cleaning up and raising a `RuntimeError`.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self, )`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It utilizes the `git.ls_files()` command to obtain raw file paths from the repository. Subsequently, it iterates through these paths, creating a `RepoFile` object for each file. These `RepoFile` instances, which encapsulate file-specific information, are then stored internally within the class and returned as a list.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
    *   **`close`**
        *   *Signature:* `def close(self, )`
        *   *Description:* This method is responsible for cleaning up resources associated with the GitRepository instance. It prints a message indicating the deletion of the temporary directory where the repository was cloned. Following this, it sets the `self.temp_dir` attribute to `None`. The commented-out `shutil.rmtree` line suggests that the actual directory deletion might be handled externally or is currently disabled, but the intent is to remove the temporary clone.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            *This method does not return a value.*
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self, )`
        *   *Description:* This special method enables the GitRepository class to function as a context manager. When an instance of GitRepository is used in a `with` statement, this method is automatically invoked. Its sole purpose is to return the instance of the object itself, allowing the `with` block to operate on the repository object.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository class itself.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This special method is part of the context manager protocol and is automatically called when exiting a `with` statement block. Its primary function is to ensure that the temporary repository directory is properly cleaned up, regardless of whether an exception occurred within the `with` block. It achieves this by invoking the `close` method of the GitRepository instance.
        *   *Parameters:*
            - **exc_type** (`type`): The type of exception that occurred, or None if no exception.
            - **exc_val** (`Exception`): The exception instance, or None.
            - **exc_tb** (`TracebackType`): The traceback object, or None.
        *   *Returns:*
            *This method does not return a value.*
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method generates a hierarchical tree representation of all files within the repository. It first checks if the files have already been retrieved; if not, it calls `get_all_files()` to populate the file list. It then iterates through each `RepoFile` object, splitting its path to construct a nested dictionary structure that accurately mirrors the repository's directory hierarchy. Each file is appended to its corresponding directory within this tree, with an option to include its content.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether the content of each file should be included in its dictionary representation. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the file tree, with 'name', 'type', and 'children' keys.

---
### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart to visually compare two token counts: JSON tokens and TOON tokens. It calculates and displays a savings percentage in the chart's title. The chart includes labels, a y-axis grid, and numerical values displayed above each bar for clarity. Finally, the generated chart is saved to a specified output file path and the plot is closed.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens in JSON format.
    - **toon_tokens** (`int`): The number of tokens in TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings, displayed in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart will be saved.
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `bar`, `close`, `figure`, `get_height`, `get_width`, `get_x`, `grid`, `int`, `savefig`, `text`, `title`, `ylabel`
    *   **Called By:** `main.py::main_workflow`

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the effective duration of an operation by subtracting estimated sleep times, which are introduced due to rate-limiting for specific models. It first determines the total elapsed time between a start and end timestamp. If the model used is not a 'gemini-' model or if no items were processed, it returns the total duration or zero, respectively. Otherwise, it calculates the number of batches, estimates the total sleep time based on a fixed duration per batch, and then subtracts this from the total duration to yield the net time, ensuring the result is not negative.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp of the operation, typically a float representing seconds since the epoch.
    - **end_time** (`float`): The ending timestamp of the operation, typically a float representing seconds since the epoch.
    - **total_items** (`int`): The total number of items processed during the operation.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model used, which determines if rate-limit sleep times are factored into the calculation.
*   **Returns:**
    - **net_time** (`float`): The calculated net duration of the operation in seconds, after accounting for estimated rate-limit sleep times, or the total duration if no sleep times are applicable.
*   **Usage:**
    *   **Calls:** `ceil`, `max`, `startswith`
    *   **Called By:** `main.py::main_workflow`

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: Callable | None)`
*   **Description:** The main_workflow function orchestrates a comprehensive analysis of a Git repository. It initializes by processing input, extracting API keys, and setting up model configurations for Helper and Main LLMs. The function then extracts a repository URL, clones the repository, and performs various analyses including basic project information extraction, file tree construction, relationship analysis, and Abstract Syntax Tree (AST) schema generation. It prepares and dispatches tasks to a Helper LLM for detailed function and class analysis, then aggregates these results. Finally, it uses a Main LLM to generate a comprehensive report, saves the report, and provides token usage statistics and performance metrics.
*   **Parameters:**
    - **input** (`str`): The user input, which is expected to contain a repository URL for analysis.
    - **api_keys** (`dict`): A dictionary containing API keys for various language model services (e.g., Gemini, OpenAI, Ollama).
    - **model_names** (`dict`): A dictionary specifying the names of the helper and main language models to be utilized in the workflow.
    - **status_callback** (`Callable | None`): An optional callback function used to provide real-time status updates during the workflow execution.
*   **Returns:**
    - **result_summary** (`dict`): A dictionary containing the 'report' (the final generated report as a string) and 'metrics' (a dictionary of performance statistics for the LLM operations).
*   **Usage:**
    *   **Calls:** *Not specified in context.*
    *   **Called By:** `Frontend.py::frontend.Frontend`, `main.py::backend.main`

#### Function: `update_status`
*   **Signature:** `def update_status(msg: str)`
*   **Description:** This function serves to update a status by processing a given message. It first checks if a `status_callback` function is available and, if so, invokes it with the provided message. Subsequently, it logs the same message at the INFO level using the `logging` module. This ensures that status updates are both propagated to a potential callback mechanism and recorded in the application's logs.
*   **Parameters:**
    - **msg** (`str`): The message string containing the status update to be processed and logged.
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `info`, `status_callback`
    *   **Called By:** `main.py::main_workflow`

---
### File: `backend/relationship_analyzer.py`

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform a comprehensive static analysis of a Python project to build a call graph and identify definitions. It initializes with a project root, then systematically finds all Python files, parses their Abstract Syntax Trees (ASTs) to collect definitions of classes, functions, and methods, and subsequently resolves calls between these entities. The class provides a structured output detailing each defined entity and the locations from which it is called, making it a core component for understanding code relationships within a project.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py.
*   **Dependencies:** The class depends on ast for parsing Python code, os for file system operations, logging for error reporting, and collections.defaultdict for managing the call graph.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer instance by setting the project root, initializing data structures like 'definitions', 'call_graph', and 'file_asts', and defining a set of directories to ignore during analysis.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self, )`
        *   *Description:* This method orchestrates the entire project analysis workflow. It first identifies all Python files, then iterates through them to collect definitions of functions, methods, and classes. Subsequently, it resolves calls between these definitions, clears intermediate ASTs, and finally returns the structured analysis results.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **output_list** (`list`): A list of dictionaries, where each dictionary represents a defined entity (function, method, or class) and lists the entities that call it.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self, )`
        *   *Description:* This private helper method recursively traverses the 'project_root' directory to locate all Python files, while explicitly excluding directories specified in 'self.ignore_dirs'. It constructs a list of absolute paths for these Python files.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found within the project root, excluding ignored directories.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method reads a given Python file, parses its source code into an Abstract Syntax Tree (AST), and then walks the AST to identify and record definitions of functions, methods, and classes. It stores these definitions in 'self.definitions' with their file path, line number, and type, and also caches the AST in 'self.file_asts'. Error handling is included for file processing and AST parsing.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file being analyzed.
        *   *Returns:*
            *This method does not return a value.*
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This private helper method traverses an AST to find the direct parent node of a given child node. It iterates through all nodes in the tree and checks their children to identify if any child matches the provided 'node'.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent** (`ast.AST or None`): The direct parent AST node of the given 'node', or None if no parent is found (e.g., if 'node' is the root of the 'tree').
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method takes a Python file's path, retrieves its AST, and then uses a CallResolverVisitor to identify all function and method calls within that file. It populates the 'self.call_graph' by extending the list of callers for each identified callee. Errors during call resolution are logged.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose calls are to be resolved.
        *   *Returns:*
            *This method does not return a value.*
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self, )`
        *   *Description:* This method processes the collected definitions and the call graph to generate a structured list of results. For each defined entity, it creates a dictionary containing its identifier, type, origin file, line number, and a sorted list of unique callers.
        *   *Parameters:*
            *This method has no parameters.*
        *   *Returns:*
            - **output_list** (`list[dict]`): A list of dictionaries, where each dictionary describes a defined entity (function, method, or class) and includes a sorted list of unique callers, their files, functions, types, and line numbers.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor is an AST NodeVisitor designed to traverse the Abstract Syntax Tree of a Python file to identify and resolve all function and method calls. It maintains a scope of imports and tracks instantiated object types to accurately determine the fully qualified name of each called entity. The visitor collects detailed information about each call, including the caller's file, line number, name, and type (module, function, or method), storing this data for further analysis.
*   **Instantiation:** This class is instantiated by the _resolve_calls method in the relationship_analyzer.py file at line 92.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the context.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor's state, setting up paths, definitions, and internal tracking mechanisms. It stores the file path, calculates the module path, and takes a dictionary of known definitions. It also initializes a scope for imports, a dictionary for instance types, and sets the initial caller and class names, along with a defaultdict to store identified calls.
    *   *Parameters:*
        - **filepath** (`str`): The path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the project, used to determine module paths.
        - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) within the project, mapped by their fully qualified names.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is invoked when the AST visitor encounters a class definition (`ast.ClassDef`). It temporarily updates the `current_class_name` attribute to reflect the class being visited, allowing nested methods to correctly identify their enclosing class. After processing the class's children, it restores the previous `current_class_name` to maintain correct scope.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method is called when the AST visitor encounters a function definition (`ast.FunctionDef`). It temporarily updates the `current_caller_name` attribute to the name of the function being visited. This ensures that any calls made within this function are correctly attributed to it. After visiting the function's body, it restores the `current_caller_name` to its previous value.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method processes `ast.Call` nodes to identify and record function or method invocations. It first resolves the fully qualified name of the called entity using `_resolve_call_qname`. If the resolved name is a known definition, it constructs a dictionary of caller information, including file, line number, caller name, and caller type (module, method, or function), and appends this information to the `self.calls` dictionary, keyed by the callee's qualified name.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method handles `ast.Import` nodes, which represent `import module_name` statements. It iterates through the imported names (and their aliases) and populates the `self.scope` dictionary. The scope maps the local name (alias or original name) to the imported module's name, facilitating the resolution of fully qualified names for subsequent calls.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `ast.ImportFrom` nodes, which represent `from module import name` statements. It constructs the full module path, correctly handling relative imports based on the current file's module path and the import level. It then populates `self.scope` by mapping the imported name (or its alias) to its fully qualified path, enabling accurate resolution of imported entities.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
            *This method does not return a value.*
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method processes `ast.Assign` nodes to identify and track the types of instantiated objects. Specifically, it looks for assignments where the assigned value is a function call (e.g., `x = MyClass()`). If the called function's name corresponds to a known class in the `self.scope` and `self.definitions`, it records the qualified class name against the target variable's ID in `self.instance_types`. This helps resolve method calls on these instances later.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
            *This method does not return a value.*
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method is responsible for resolving the fully qualified name (QName) of a function or method call. It handles two main cases: direct calls to names (`ast.Name`) and method calls on attributes (`ast.Attribute`). For `ast.Name` nodes, it checks `self.scope` (for imports) or constructs a local module path. For `ast.Attribute` nodes, it uses `self.instance_types` (for object methods) or `self.scope` (for module-level attributes) to determine the full path. If a QName cannot be resolved, it returns None.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called, typically an ast.Name or ast.Attribute.
        *   *Returns:*
            - **callee_qname** (`str | None`): The fully qualified name of the called function or method, or None if it cannot be resolved.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into its corresponding Python module path. It first determines the file's relative path to the specified project root, handling potential `ValueError` by using the file's basename. It then removes the '.py' extension and replaces operating system path separators with dots. Finally, it adjusts the module path by removing '.__init__' if it represents an initialization file within a package.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The Python module path derived from the given filepath.
*   **Usage:**
    *   **Calls:** `basename`, `endswith`, `relpath`, `replace`
    *   **Called By:** `relationship_analyzer.py::_collect_definitions`, `relationship_analyzer.py::__init__`

---
### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function is designed to encrypt a given text string. It first checks if the input text or the `cipher_suite` object is empty; if either is, it returns the original text without encryption. Otherwise, it encodes the text into bytes, encrypts these bytes using the `cipher_suite`, and then decodes the resulting encrypted bytes back into a string before returning it.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input text, or the original text if encryption conditions are not met.
*   **Usage:**
    *   **Calls:** `decode`, `encode`, `encrypt`
    *   **Called By:** `db.py::update_gemini_key`

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given text string using a `cipher_suite` object. It first checks if the input text is empty or if the `cipher_suite` is not initialized; if either condition is true, it returns the original text without modification. Otherwise, it encodes the text to bytes, attempts decryption, and then decodes the result back to a string. If any error occurs during the decryption process, the function gracefully falls back to returning the original, unencrypted text.
*   **Parameters:**
    - **text** (`str`): The string to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted string if successful, or the original string if decryption is skipped or fails due to an exception.
*   **Usage:**
    *   **Calls:** `decode`, `decrypt`, `encode`
    *   **Called By:** `db.py::get_decrypted_api_keys`

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function is responsible for inserting a new user's information into a database. It takes a username, name, and a plain-text password, then hashes the password before creating a user dictionary. The user dictionary also includes placeholders for Gemini API key and Ollama base URL. Finally, it inserts this user dictionary into the 'dbusers' collection and returns the unique identifier of the newly created user document.
*   **Parameters:**
    - **username** (`str`): The unique username for the new user.
    - **name** (`str`): The full name of the new user.
    - **password** (`str`): The plain-text password for the new user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier of the newly inserted user document in the database.
*   **Usage:**
    *   **Calls:** `hash`, `insert_one`
    *   **Called By:** *Not called by any function in the provided context.*

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is responsible for retrieving all user records from a database. It interacts with a database collection, identified as 'dbusers', by invoking its 'find()' method to query all available documents. The iterable result obtained from the database query is then explicitly converted into a standard Python list. Finally, this list, containing all the fetched user documents, is returned by the function.
*   **Parameters:**
    *This method has no parameters.*
*   **Returns:**
    - **users** (`list`): A list containing all user documents fetched from the database.
*   **Usage:**
    *   **Calls:** `find`, `list`
    *   **Called By:** `Frontend.py::frontend.Frontend`

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** This function retrieves a single user record from a database collection, presumably named `dbusers`. It queries the collection using the provided `username` as the document's `_id` field. The primary purpose is to fetch user data based on their unique username. The function returns the user object found by the query.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched, which is used as the `_id` in the database query.
*   **Returns:**
    - **user** (`dict`): The user object (typically a dictionary) if a matching user is found, otherwise `None`.
*   **Usage:**
    *   **Calls:** `find_one`
    *   **Called By:** *Not called by any function in the provided context.*

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database. It first encrypts the provided `gemini_api_key` using an `encrypt_text` utility. Subsequently, it performs an update operation on the `dbusers` collection, locating the user by their `username` and setting their `gemini_api_key` field to the newly encrypted value. The function then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be encrypted and stored for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 1 if the key was successfully updated for the user, or 0 if the user was not found.
*   **Usage:**
    *   **Calls:** `encrypt_text`, `update_one`
    *   **Called By:** `Frontend.py::frontend.Frontend`

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama Base URL for a specified user in the database. It takes the username and the new Ollama base URL as input. The function utilizes a database collection, likely `dbusers`, to locate the user by their username (acting as the `_id`) and then sets the `ollama_base_url` field to the new provided value. It returns an integer indicating the number of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama Base URL is to be updated.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service to be associated with the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 1 if the user exists and the URL was updated, or 0 otherwise.
*   **Usage:**
    *   **Calls:** `update_one`
    *   **Called By:** `Frontend.py::frontend.Frontend`

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** This function is designed to retrieve the Gemini API key associated with a specific user from a database. It queries the `dbusers` collection, searching for a document where the `_id` matches the provided username. The function then extracts and returns the `gemini_api_key` field from the found user document. If the user or the key is not found, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`Optional[str]`): The Gemini API key for the specified user, or None if the user or key is not found.
*   **Usage:**
    *   **Calls:** `find_one`, `get`
    *   **Called By:** *Not called by any function in the provided context.*

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function is designed to retrieve the Ollama Base URL for a specific user from a database. It queries a 'dbusers' collection, using the provided username as the document's identifier. The function specifically fetches only the 'ollama_base_url' field and returns its value. If the user or the URL is not found, it will return None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Ollama Base URL needs to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama Base URL associated with the user, or None if the user or the URL is not found in the database.
*   **Usage:**
    *   **Calls:** `find_one`, `get`
    *   **Called By:** *Not called by any function in the provided context.*

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is designed to remove a user record from a database collection. It takes a username as input, which is used as the unique identifier (`_id`) to locate the specific user document. The function then executes a delete operation on the database and reports the number of documents that were successfully removed.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents (users) that were successfully deleted from the database. A value of 1 indicates successful deletion of the specified user, while 0 indicates the user was not found.
*   **Usage:**
    *   **Calls:** `delete_one`
    *   **Called By:** *Not called by any function in the provided context.*

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves a user's API keys from the database based on the provided username. It first attempts to find a user record matching the username. If a user is found, it decrypts the 'gemini_api_key' using a helper function and retrieves the 'ollama_base_url'. The decrypted Gemini key and the Ollama URL are then returned. If no user is found, the function returns two None values.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys are to be retrieved and decrypted.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key if found, otherwise None.
    - **ollama_plain** (`str | None`): The Ollama base URL if found, otherwise None.
*   **Usage:**
    *   **Calls:** `decrypt_text`, `find_one`, `get`
    *   **Called By:** `Frontend.py::frontend.Frontend`

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str)`
*   **Description:** This function is responsible for inserting a new exchange record into a database collection named `dbexchanges`. It constructs a dictionary containing various details such as the question, answer, feedback, chat name, username, and timestamps for helper and main component usage. A `created_at` timestamp is automatically generated using `datetime.now()`. Finally, it performs the insertion using `dbexchanges.insert_one()` and returns the unique identifier of the newly created document.
*   **Parameters:**
    - **question** (`str`): The question string associated with the exchange.
    - **answer** (`str`): The answer string provided for the exchange.
    - **feedback** (`str`): The feedback string related to the exchange.
    - **username** (`str`): The username of the individual involved in the exchange.
    - **chat_name** (`str`): The name of the chat session where the exchange occurred.
    - **helper_used** (`str`): Optional. Specifies which helper component was utilized, defaulting to an empty string.
    - **main_used** (`str`): Optional. Specifies which main component was utilized, defaulting to an empty string.
    - **total_time** (`str`): Optional. The total duration of the exchange process, defaulting to an empty string.
    - **helper_time** (`str`): Optional. The time spent by the helper component, defaulting to an empty string.
    - **main_time** (`str`): Optional. The time spent by the main component, defaulting to an empty string.
*   **Returns:**
    - **inserted_id** (`ObjectId`): The unique identifier assigned by the database to the newly inserted exchange document.
*   **Usage:**
    *   **Calls:** `insert_one`, `now`
    *   **Called By:** `Frontend.py::frontend.Frontend`

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function is designed to retrieve all exchange records associated with a specific user from a database collection named `dbexchanges`. It takes a username as input, performs a database query to find all documents matching that username, and then converts the query results into a list before returning them. This allows for fetching all historical or current exchanges for a given user.
*   **Parameters:**
    - **username** (`str`): The username used to query the database for associated exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (documents) found for the specified username.
*   **Usage:**
    *   **Calls:** `find`, `list`
    *   **Called By:** `Frontend.py::load_data_from_db`

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a list of chat exchanges from a database. It queries the 'dbexchanges' collection using a provided username and chat name as filters. The results of the database query are then converted into a Python list and returned.
*   **Parameters:**
    - **username** (`str`): The username to filter the chat exchanges by.
    - **chat_name** (`str`): The name of the chat to filter the exchanges by.
*   **Returns:**
    - **exchanges** (`list`): A list of chat exchange documents matching the provided username and chat name.
*   **Usage:**
    *   **Calls:** `find`, `list`
    *   **Called By:** *Not called by any function in the provided context.*

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** This function is responsible for updating the feedback value associated with a specific exchange record in the database. It takes an exchange identifier and an integer feedback value as input. The function uses a database client, `dbexchanges`, to perform an `update_one` operation, setting the 'feedback' field for the document matching the provided `exchange_id`. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    - **feedback** (`int`): The integer feedback value to set for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    *   **Calls:** `update_one`
    *   **Called By:** `Frontend.py::handle_feedback_change`

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** This function is responsible for updating the feedback message associated with a specific exchange record in a database. It takes an exchange identifier and the new feedback message as input. The function utilizes a database collection, likely `dbexchanges`, to locate the document matching the provided ID and then updates its 'feedback_message' field. It returns an integer indicating the number of documents that were successfully modified.
*   **Parameters:**
    - **exchange_id** (`object`): The unique identifier of the exchange record to be updated. Its specific type depends on the database's ID format (e.g., ObjectId, string).
    - **feedback_message** (`str`): The new string value to set as the feedback message for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. This will typically be 0 or 1.
*   **Usage:**
    *   **Calls:** `update_one`
    *   **Called By:** `Frontend.py::render_exchange`

#### Function: `delete_chats_by_user`
*   **Signature:** `def delete_chats_by_user(username: str, chat_name: str)`
*   **Description:** The `delete_chats_by_user` function is responsible for removing chat exchanges from a database. It takes a specific username and chat name as input to identify the records to be deleted. The function executes a bulk delete operation on the `dbexchanges` collection, targeting all documents that match the provided criteria. Upon completion, it returns the total number of documents that were successfully removed from the database.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat exchanges to be deleted.
    - **chat_name** (`str`): The name of the chat whose exchanges are to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat exchanges successfully deleted from the database.
*   **Usage:**
    *   **Calls:** `delete_many`
    *   **Called By:** `Frontend.py::handle_delete_chat`

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is designed to remove a specific exchange record from a database collection. It accepts an `exchange_id` as a string to uniquely identify the record for deletion. The function interacts with the `dbexchanges` collection, invoking its `delete_one` method to remove the matching document. It then returns an integer indicating the number of documents that were successfully deleted.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted (typically 0 or 1 for a delete_one operation).
*   **Usage:**
    *   **Calls:** `delete_one`
    *   **Called By:** `Frontend.py::handle_delete_exchange`

---
### File: `frontend/Frontend.py`

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function is designed to load existing chat data from a database into the Streamlit session state for a specific user. It ensures that the data loading process occurs only once per session by checking a 'data_loaded' flag. The function fetches chat exchanges associated with the provided username and organizes them into a dictionary structure within `st.session_state.chats`. It handles cases where chat names might be missing or feedback values are null, defaulting them appropriately. Finally, it initializes a default chat ('Chat 1') if no chats are found and sets an active chat for the user interface.
*   **Parameters:**
    - **username** (`str`): The username for which to retrieve and load chat data from the database.
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `append`, `fetch_exchanges_by_user`, `get`, `keys`, `list`
    *   **Called By:** `Frontend.py::frontend.Frontend`

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function updates the feedback for a given exchange object both in the application's state and in the database. It takes an exchange object and a new feedback value as input. The function first modifies the 'feedback' key of the provided exchange object with the new value. It then calls a database utility function to persist this change. Finally, it triggers a Streamlit rerun to refresh the user interface, reflecting the updated feedback.
*   **Parameters:**
    - **ex** (`dict`): The exchange object, expected to be a dictionary-like structure containing an '_id' and a 'feedback' key.
    - **val** (`Any`): The new feedback value to be set for the exchange.
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `rerun`, `update_exchange_feedback`
    *   **Called By:** `Frontend.py::render_exchange`

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function is responsible for deleting a specific exchange entry. It performs a two-step deletion process, first removing the exchange from the database and then from the application's session state. After these operations, it triggers a Streamlit rerun to ensure the user interface reflects the changes. This ensures data consistency across both persistent storage and the active UI state.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat associated with the exchange to be deleted.
    - **ex** (`dict`): The exchange object to be deleted, which is expected to contain an '_id' key for database lookup.
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `delete_exchange_by_id`, `remove`, `rerun`
    *   **Called By:** `Frontend.py::render_exchange`

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function is responsible for deleting a specified chat for a given user. It first removes the chat from the database using `db.delete_chats_by_user` and then from the Streamlit session state. After deletion, it updates the active chat: if other chats exist, the first available chat becomes active; otherwise, a new default chat named "Chat 1" is created and set as active. Finally, it triggers a Streamlit rerun to reflect these changes in the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `delete_chats_by_user`, `keys`, `len`, `list`, `rerun`
    *   **Called By:** `Frontend.py::frontend.Frontend`

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str)`
*   **Description:** This function processes a given Markdown text, identifying and extracting Mermaid diagram code blocks. It uses regular expressions to split the text into parts, rendering plain text sections using Streamlit's markdown functionality. For Mermaid code blocks, it attempts to render them graphically using `streamlit_mermaid`. If the graphical rendering fails, the Mermaid code block is displayed as plain text within a Streamlit code block.
*   **Parameters:**
    - **markdown_text** (`str`): The input text, potentially containing Mermaid diagram blocks, to be rendered.
*   **Returns:**
    - **None** (`None`): The function does not return any value; it performs side effects by rendering content directly to a Streamlit application.
*   **Usage:**
    *   **Calls:** `code`, `enumerate`, `hash`, `markdown`, `split`, `st_mermaid`, `strip`
    *   **Called By:** `Frontend.py::render_exchange`, `Frontend.py::frontend.Frontend`

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function is responsible for rendering a single chat exchange within a Streamlit application. It displays both the user's question and the assistant's answer. A toolbar is provided with interactive elements allowing users to give positive or negative feedback, write a detailed feedback message, download the assistant's response as a Markdown file, or delete the entire exchange. The assistant's answer is presented in a scrollable container, potentially supporting Mermaid diagrams.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing a chat exchange, containing keys like 'question', 'answer', '_id', 'feedback', and 'feedback_message'.
    - **current_chat_name** (`str`): The name of the current chat, used for operations like deleting an exchange.
*   **Returns:**
    *This method does not return a value.*
*   **Usage:**
    *   **Calls:** `button`, `caption`, `chat_message`, `columns`, `container`, `download_button`, `get`, `handle_delete_exchange`, `handle_feedback_change`, `popover`, `render_text_with_mermaid`, `rerun`, `sleep`, `success`, `text_area`, `update_exchange_feedback_message`, `write`
    *   **Called By:** `Frontend.py::frontend.Frontend`

---
### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to encapsulate the details of a single function parameter. It defines three core attributes: name (the parameter's identifier), type (its data type), and description (a textual explanation of its role). This class serves as a structured data container for parameter metadata, facilitating consistent representation and validation.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The ParameterDescription class is initialized by providing values for its `name`, `type`, and `description` fields. As a Pydantic BaseModel, it automatically handles validation and assignment of these attributes upon instantiation.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type hint or inferred type of the parameter.
        - **description** (`str`): A brief explanation of the parameter's purpose.
*   **Methods:**
    *This class has no methods.*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to encapsulate the details of a function's return value. It provides a structured format for describing what a function returns, including its name, data type, and a textual description. This model is intended to standardize the representation of return types for documentation or automated analysis purposes.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
*   **Constructor:**
    *   *Description:* The constructor for ReturnDescription is automatically generated by Pydantic's BaseModel. It initializes an instance of ReturnDescription by accepting keyword arguments corresponding to its defined fields: 'name', 'type', and 'description'. These arguments are used to set the respective attributes of the object.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The data type of the return value, represented as a string.
        - **description** (`str`): A detailed textual explanation of the return value's purpose or content.
*   **Methods:**
    *This class has no methods.*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about the calling context of a software entity, typically a function or method. It provides a structured representation for understanding an entity's interactions within a larger system, specifically detailing what it calls and where it is called from. This class serves as a data model for contextual metadata.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an __init__ method that initializes its fields `calls` and `called_by`. It sets up the instance by validating and assigning these string values, ensuring they conform to the defined types.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions or methods this entity calls.
        - **called_by** (`str`): A string summarizing where this entity is used or called from.
*   **Methods:**
    *This class has no methods.*

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic BaseModel designed to provide a structured and detailed analysis of a Python function. It serves as a data schema to encapsulate various aspects of a function, including its high-level purpose, its input parameters, its return values, and its usage context within a larger system. This model ensures consistency and validation for function metadata.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates its constructor. It initializes instances by validating and assigning values to its defined fields: 'overall', 'parameters', 'returns', and 'usage_context'.
    *   *Parameters:*
        - **overall** (`str`): A comprehensive summary describing the function's purpose and its high-level implementation details.
        - **parameters** (`List[ParameterDescription]`): A list containing detailed descriptions for each parameter accepted by the function.
        - **returns** (`List[ReturnDescription]`): A list containing detailed descriptions of the values or types that the function returns.
        - **usage_context** (`UsageContext`): An object providing context about where the function is called and what other functions or methods it calls.
*   **Methods:**
    *This class has no methods.*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to represent a complete analysis of a Python function. It serves as a structured container for the function's unique identifier, a detailed description object, and an optional error message. This model is crucial for standardizing the output of automated function analysis, ensuring consistency in how function metadata and potential issues are captured.
*   **Instantiation:** The specific points where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly generates a constructor that initializes its fields based on the type hints provided. It accepts values for 'identifier', 'description', and 'error', with 'error' being optional and defaulting to None.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the function being analyzed.
        - **description** (`FunctionDescription`): An object containing a detailed breakdown of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the function's analysis. Defaults to None.
*   **Methods:**
    *This class has no methods.*

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to structure information about a Python class's __init__ method. It serves as a data schema, ensuring that any description of a constructor includes a textual summary and a detailed list of its parameters. This model facilitates standardized representation of constructor metadata within a larger system.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class defines the structure for describing a class's `__init__` method. As a Pydantic BaseModel, its constructor is automatically generated, accepting values for `description` and `parameters` to initialize an instance.
    *   *Parameters:*
        - **description** (`str`): A string summary of the `__init__` method's purpose and behavior.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing a parameter of the constructor.
*   **Methods:**
    *This class has no methods.*

#### Class: `ClassContext`
*   **Summary:** The `ClassContext` is a Pydantic `BaseModel` designed to describe the contextual usage of a class within a larger system. It provides a structured format to specify a class's external dependencies and the locations or components responsible for its instantiation. This model serves as a metadata container, offering insights into how a class integrates and operates within its environment.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ClassContext` is implicitly generated by Pydantic's `BaseModel`. It initializes an instance of `ClassContext` by accepting `dependencies` and `instantiated_by` as string arguments, performing validation against their defined types to ensure data integrity.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class.
        - **instantiated_by** (`str`): A string indicating where the class is instantiated.
*   **Methods:**
    *This class has no methods.*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to encapsulate a holistic analysis of another Python class. It serves as a structured data container, holding information about the target class's high-level purpose, its constructor's details, a list of analyses for all its methods, and its external usage context. This model standardizes the representation of class analysis, facilitating automated documentation or further processing.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for this Pydantic BaseModel is implicitly generated. It initializes an instance of `ClassDescription` by validating and assigning values to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose.
        - **init_method** (`ConstructorDescription`): Details about the class's constructor, including its description and parameters.
        - **methods** (`List[FunctionAnalysis]`): A list of analyses for each method within the class, providing detailed insights into their functionality, parameters, and return values.
        - **usage_context** (`ClassContext`): Information regarding the class's external dependencies and the locations where it is instantiated.
*   **Methods:**
    *This class has no methods.*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the root Pydantic model for structuring a comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed description object containing its constructor and methods, and an optional field for error reporting. This model is fundamental for representing structured data about a class's structure and behavior in a machine-readable format.
*   **Instantiation:** The specific points where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The ClassAnalysis class, being a Pydantic BaseModel, has its constructor implicitly generated by Pydantic. This allows for direct instantiation by providing values for its defined fields: `identifier`, `description`, and the optional `error` field.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
        - **error** (`Optional[str]`): An optional field to store an error message if the class analysis failed during processing.
*   **Methods:**
    *This class has no methods.*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event within a system, such as from a relationship analyzer. It encapsulates key details about a function call, including the file where the call occurs, the name of the calling function, the mode of the call (e.g., 'method', 'function'), and the line number. This structure is intended for use in tracking relationships, particularly in 'called_by' and 'instantiated_by' lists.
*   **Instantiation:** The instantiation points for this class are not specified within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the analyzed context.
*   **Constructor:**
    *   *Description:* The CallInfo class, being a Pydantic BaseModel, does not explicitly define an __init__ method. Instead, Pydantic automatically generates a constructor that handles the validation and assignment of its declared fields: `file`, `function`, `mode`, and `line`. Instances are created by passing keyword arguments corresponding to these fields, which are then validated against their specified types.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that is making the call.
        - **mode** (`str`): The type or mode of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the file where the call event is located.
*   **Methods:**
    *This class has no methods.*

#### Class: `FunctionContextInput`
*   **Summary:** This class serves as a Pydantic BaseModel for structuring the contextual information required to analyze a function. It encapsulates details about other functions, methods, or classes that the target function calls, as well as the locations from which the target function itself is invoked. This structured approach facilitates consistent data handling for function analysis within a larger system.
*   **Instantiation:** This class is instantiated by the `main_workflow` function in `main.py` at line 204.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly defines its constructor to accept and validate the 'calls' and 'called_by' fields. It initializes an instance of FunctionContextInput by assigning these values, ensuring they conform to their specified types.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing the names of functions, methods, or classes that this function calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this function is called from.
*   **Methods:**
    *This class has no methods.*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to serve as a structured input schema for initiating a function analysis. It encapsulates all necessary data, including the function's identifier, its raw source code, relevant import statements, and additional contextual information. This class ensures that all required components are present and correctly typed, facilitating robust data validation and organization before the function analysis workflow commences.
*   **Instantiation:** This class is instantiated by the `main_workflow` function in `main.py` on line 209.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within its definition.
*   **Constructor:**
    *   *Description:* The constructor for FunctionAnalysisInput is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting values for its defined fields: mode, identifier, source_code, imports, and context. This setup ensures that all required input data for a function analysis is validated upon object creation.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, which is fixed to 'function_analysis' for this input type.
        - **identifier** (`str`): The unique name or identifier of the function that is to be analyzed.
        - **source_code** (`str`): The raw source code string of the entire function definition.
        - **imports** (`List[str]`): A list of strings, each representing an import statement relevant to the function's execution context.
        - **context** (`FunctionContextInput`): An object containing additional contextual information pertinent to the function analysis, such as call graphs or dependencies.
*   **Methods:**
    *This class has no methods.*

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to structure and validate contextual information pertaining to a specific method. It serves as a data schema for capturing details such as the method's unique identifier, its internal calls to other functions or methods, external callers, its arguments, and its docstring. This model ensures that method context data conforms to a predefined structure, facilitating consistent data handling and analysis within a larger system.
*   **Instantiation:** This class is instantiated by the `main_workflow` function in `main.py` at line 232.
*   **Dependencies:** This class does not explicitly declare external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `MethodContextInput` is implicitly generated by Pydantic's BaseModel. It handles the instantiation and validation of the class attributes based on the provided type hints, ensuring that all input data conforms to the defined schema upon object creation.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method being described.
        - **calls** (`List[str]`): A list of string identifiers representing other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects detailing where this method is invoked from within the codebase.
        - **args** (`List[str]`): A list of strings representing the names of the arguments accepted by this method.
        - **docstring** (`Optional[str]`): The docstring content of the method, if one is present; otherwise, it can be null.
*   **Methods:**
    *This class has no methods.*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate comprehensive contextual information necessary for the analysis of a Python class. It serves as a structured input for an AI system, providing details about the class's external dependencies, its instantiation points within the codebase, and specific contextual data for each of its methods. This model ensures that all relevant background information is available for a holistic class analysis.
*   **Instantiation:** This class is instantiated by the `main_orchestrator` function in `HelperLLM.py` at line 350 and the `main_workflow` function in `main.py` at line 245.
*   **Dependencies:** This class does not explicitly list any direct external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. Pydantic's BaseModel automatically generates a constructor based on the type-hinted fields, allowing instances to be created by passing keyword arguments corresponding to `dependencies`, `instantiated_by`, and `method_context`.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of external dependencies relevant to the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where the class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects providing context for each method within the class.
*   **Methods:**
    *This class has no methods.*

#### Class: `ClassAnalysisInput`
*   **Summary:** This class serves as a Pydantic BaseModel, defining the structured input required for generating a ClassAnalysis object. It encapsulates all necessary data points, including the operational mode, the identifier of the class to be analyzed, its complete source code, a list of relevant import statements, and additional contextual information. Its primary purpose is to ensure that all prerequisites for a class analysis task are provided in a validated and consistent format.
*   **Instantiation:** This class is instantiated by the `main_orchestrator` function in `HelperLLM.py` and the `main_workflow` function in `main.py`.
*   **Dependencies:** This class does not explicitly list any direct functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for ClassAnalysisInput is automatically generated. It handles the validation and assignment of the class's defined fields: `mode`, `identifier`, `source_code`, `imports`, and `context`, ensuring that instances are created with valid data types and values.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operational mode, which is fixed to 'class_analysis' for this input type, indicating the intent to perform a class analysis.
        - **identifier** (`str`): The unique name or identifier of the Python class that is the subject of the analysis.
        - **source_code** (`str`): The complete raw source code string of the entire class definition to be analyzed.
        - **imports** (`List[str]`): A list of strings, where each string represents an import statement relevant to the provided source code.
        - **context** (`ClassContextInput`): An object containing additional contextual information pertinent to the class analysis, such as dependencies and instantiation points.
*   **Methods:**
    *This class has no methods.*

---
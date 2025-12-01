# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated documentation agent designed to analyze Git repositories. It clones a given repository, performs static analysis by building an Abstract Syntax Tree (AST), and leverages Large Language Models (LLMs) to generate comprehensive code documentation. The system features a backend for code processing and LLM orchestration, and a web-based frontend built with Streamlit for user interaction and storing and displaying results.
- **Key Features:**
  - Automated Git Repository Cloning and Analysis
  - Abstract Syntax Tree (AST) Generation for Code Structure Mapping
  - LLM-driven Generation of Code Summaries and Documentation
  - Relationship Analysis for Calls and Instantiations
  - Interactive Web Frontend built with Streamlit
- **Tech Stack:** LangChain, Streamlit, Pydantic, NetworkX, GitPython, PyMongo, Google Generative AI

*   **Repository Structure:**
    ```mermaid
    graph LR
        subgraph root
            direction LR
            A[".env.example<br/>.gitignore<br/>analysis_output.json<br/>readme.md<br/>requirements.txt"]
            B(SystemPrompts)
            C(backend)
            D(database)
            E(frontend)
            F(notizen)
            G(result)
            H(schemas)
        end

        B --> B_Files["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt"]
        C --> C_Files["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py"]
        D --> D_Files["db.py"]
        E --> E_Files["Frontend.py<br/>__init__.py<br/>gifs"]
        F --> F_Files["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
        G --> G_Files["ast_schema_... .json<br/>report_... .md<br/>result_... .md"]
        H --> H_Files["types.py"]
    ```

## 2. Installation
### Dependencies
As this repository contains a `requirements.txt` file, dependencies can be installed by running:
`pip install -r requirements.txt`

Key dependencies include:
- altair==4.2.2
- langchain==1.0.8
- langgraph==1.0.3
- streamlit==1.51.0
- streamlit-authenticator==0.4.2
- google-ai-generativelanguage==0.9.0
- GitPython==3.1.45
- networkx==3.6
- pydantic==2.12.4
- pymongo==4.15.4
- python-dotenv==1.2.1

### Setup Guide
1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd repo-onboarding-agent
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment:**
    -   Copy the `.env.example` file to a new file named `.env`.
    -   Open the `.env` file and add your necessary API keys (e.g., `GEMINI_API_KEY`, `MONGO_DB_URL`).
4.  **Run the Application:**
    -   Start the Streamlit frontend.

### Quick Startup
```bash
streamlit run frontend/Frontend.py
```

## 3. Use Cases & Commands
The primary use case of this agent is to automate the generation of technical documentation for a software project hosted on Git.

**Workflow:**
1.  Launch the Streamlit web application using the command `streamlit run frontend/Frontend.py`.
2.  Log in or register a new user.
3.  Navigate to the settings page to input necessary API keys (e.g., Gemini) and select the desired LLM models for analysis.
4.  In the main chat interface, provide the URL of a public Git repository.
5.  The agent will clone the repository, perform a comprehensive analysis of the codebase, and generate a detailed Markdown documentation file.
6.  The final report is displayed in the interface and can be downloaded. Previous analyses are stored and can be reviewed.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added.

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It specifically focuses on extracting information about imports, classes, and functions within the code. The visitor pattern is employed to systematically visit different node types in the AST, accumulating details into a structured schema. This schema is intended to represent the components of a Python project, including their identifiers, source code segments, and call relationships, facilitating further analysis or documentation generation.
*   **Instantiation:** `AST_Schema.py`, in function `analyze_repository` (Line: 175)
*   **Dependencies:** This class relies on the `ast` module for parsing Python code into an Abstract Syntax Tree and the `path_to_module` function (presumably defined elsewhere) to convert file paths into module paths. It also utilizes `ast.get_docstring` and `ast.get_source_segment` for extracting specific code details.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with the source code, file path, and project root directory. It sets up instance variables to store this information and derives the module path. It also initializes an empty schema dictionary to store extracted information about imports, functions, and classes, and sets an internal variable `_current_class` to None.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the file being analyzed.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code: str, file_path: str, project_root: str)`
        *   *Description:* Initializes the ASTVisitor with the source code, file path, and project root directory. It sets up instance variables to store this information and derives the module path. It also initializes an empty schema dictionary to store extracted information about imports, functions, and classes, and sets an internal variable `_current_class` to None.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **source_code** (`str`): The raw source code of the file being analyzed.
            - **file_path** (`str`): The absolute path to the file being analyzed.
            - **project_root** (`str`): The root directory of the project.
        *   *Returns:* None
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method visits an `ast.Import` node in the AST. It iterates through the imported module aliases and appends their names to the 'imports' list within the class's schema. After processing the import statement, it calls `generic_visit` to continue the traversal down the AST.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* None
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent imports from a specific module (e.g., `from os import path`). It iterates through the imported names, constructing a fully qualified name (module.name) and appending it to the 'imports' list in the schema. It then calls `generic_visit` to ensure further traversal of the AST.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* None
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is responsible for visiting `ast.ClassDef` nodes, representing class definitions in the source code. It constructs a unique identifier for the class, including its module path. It then gathers information such as the class name, docstring, source code segment, start and end line numbers, and initializes a context dictionary for dependencies and method calls. This class information is appended to the 'classes' list in the schema. It also sets an internal `_current_class` attribute to store the information of the class currently being visited, and finally calls `generic_visit` to process nested nodes within the class definition before resetting `_current_class`.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* None
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, which represent function or method definitions. If the visitor is currently inside a class (`_current_class` is set), it treats the definition as a method, constructs a method identifier, and stores method-specific information (name, arguments, docstring, source code, line numbers) within the `method_context` of the current class in the schema. If not inside a class, it's treated as a standalone function, and its information is added to the 'functions' list in the schema. In both cases, it calls `generic_visit` to process any nested nodes within the function definition.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.FunctionDef`): The AST node representing a function or method definition.
        *   *Returns:* None
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method is an alias for `visit_FunctionDef`. It ensures that asynchronous function definitions (`async def`) are also processed correctly by delegating the visit operation to the `visit_FunctionDef` method. This allows the visitor to handle both regular and asynchronous function definitions uniformly.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* None

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process a collection of Python files, parse their Abstract Syntax Trees (ASTs), and build a comprehensive schema representing the code structure, including functions, classes, and their relationships. It enriches this schema with call graph information and merges relationship data to provide a detailed repository analysis.
*   **Instantiation:** `main.py`, in function `main_workflow` (Line: 166)
*   **Dependencies:** This class depends on the 'ast' module for parsing Python code, 'networkx' for graph manipulation (specifically for call graphs), 'os' for path operations, and a custom 'callgraph.build_callGraph' function. It also relies on an 'ASTVisitor' class for traversing the AST.
*   **Constructor:**
    *   *Description:* Initializes the ASTAnalyzer. Currently, the constructor does not perform any specific setup or attribute initialization, as indicated by the 'pass' statement.
    *   *Parameters:* None
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* Initializes the ASTAnalyzer. Currently, the constructor does not perform any specific setup or attribute initialization, as indicated by the 'pass' statement.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
        *   *Returns:* None
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* This static method takes a schema dictionary and a NetworkX call graph, along with a filename, to enrich the schema with call graph information. It iterates through functions and methods within the schema, identifying their corresponding nodes in the call graph. For each identified function or method, it adds 'calls' and 'called_by' attributes to its context, populated with sorted lists of successors and predecessors from the call graph, respectively. This provides a detailed view of inter-function and inter-method call relationships within the context of a specific file.
        *   *Parameters:*
            - **schema** (`dict`): The schema dictionary to be enriched with call graph data.
            - **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call graph of the code.
            - **filename** (`str`): The name of the file for which the call graph and schema are being processed.
        *   *Returns:* None
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
        *   *Description:* This method merges relationship data, such as 'called_by' and 'instantiated_by' information, into a full schema. It first creates a lookup dictionary from the provided relationship data. Then, it iterates through the files and their corresponding AST nodes within the full schema. For each function, class, and method, it checks if its identifier exists in the relationship lookup and updates the schema with the relevant relationship information. This method is crucial for consolidating call and instantiation relationships across different parts of the analyzed code.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
            - **full_schema** (`dict`): The complete schema dictionary that will be updated with relationship data.
            - **relationship_data** (`list`): A list of dictionaries, where each dictionary contains relationship information like 'identifier' and 'called_by'.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary with merged relationship data.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files)`
        *   *Description:* This method orchestrates the analysis of an entire repository by processing a list of files. It initializes an empty schema and determines the project root directory. For each Python file, it parses the file content into an AST, creates an ASTVisitor to extract schema information, and builds a call graph. It then uses the _enrich_schema_with_callgraph method to add call graph details to the file's schema. Finally, it aggregates the processed file schemas into a comprehensive 'full_schema' dictionary, handling potential parsing errors gracefully. This method is the primary entry point for analyzing a collection of code files.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
            - **files** (`list`): A list of file objects, where each object contains file path and content.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary containing the aggregated schema information for all processed files in the repository.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into a Python module path relative to a specified project root. It handles potential errors during relative path calculation and normalizes the path by replacing directory separators with dots. It also specifically handles the case of `__init__.py` files to correctly represent package modules.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the file.
    - **project_root** (`str`): The root directory of the Python project.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path.
*   **Usage:**
    - **Calls:** This function calls `os.path.relpath` to get the relative path, `os.path.basename` if `relpath` fails, and uses string methods like `endswith` and `replace` for path manipulation.
    - **Called By:** This function is called by the `__init__` method within the `AST_Schema.py` file.

---
### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze Python source code and build a graph representing file dependencies based on import statements. It traverses the Abstract Syntax Tree (AST) of a given file to identify direct and relative imports, resolving them to determine the relationships between different modules and files within a repository. The class stores these dependencies in a dictionary, mapping each file to a set of its imported modules or symbols.
*   **Instantiation:** `File_Dependency.py`, in function `build_file_dependency_graph` (Line: 159)
*   **Dependencies:** This class relies on several modules for its functionality, including `ast` for parsing Python code, `keyword` for checking Python keywords, `pathlib` for path manipulation, and potentially other modules like `getRepo.GitRepository` and `collections.defaultdict` for repository and data structure operations. It also uses `ast.literal_eval` and `ast.parse` for code analysis.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with the filename to be analyzed and the root directory of the repository. This sets up the context for resolving imports within the specified file and repository.
    *   *Parameters:*
        - **filename** (`str`): The name of the file for which the dependency graph is being built.
        - **repo_root** (`str`): The root path of the repository containing the file.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename, repo_root)`
        *   *Description:* Initializes the FileDependencyGraph with the filename to be analyzed and the root directory of the repository. This sets up the context for resolving imports within the specified file and repository.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the FileDependencyGraph class.
            - **filename** (`str`): The name of the file for which the dependency graph is being built.
            - **repo_root** (`str`): The root path of the repository containing the file.
        *   *Returns:* None
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This method is responsible for resolving relative import statements (e.g., `from .. import name`) within a Python file. It determines the actual module or symbol name based on the current file's location within the repository and the specified import level. The method searches for corresponding Python files or `__init__.py` files in the calculated base directory and checks if the imported symbol is exported. It raises an `ImportError` if the import cannot be resolved or if the import level is invalid for the file's location.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the FileDependencyGraph class.
            - **node** (`ImportFrom`): The AST node representing the import statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A sorted list of resolved module or symbol names.
    *   **`module_file_exists`**
        *   *Signature:* `def module_file_exists(rel_base, name)`
        *   *Description:* A helper method to check if a Python module file or a package's `__init__.py` file exists at a given relative base path with a specified name. It constructs the potential file paths and returns `True` if either the `.py` file or the package directory with `__init__.py` exists, `False` otherwise.
        *   *Parameters:*
            - **rel_base** (`Path`): The relative base path within the repository.
            - **name** (`str`): The name of the module or package to check for.
        *   *Returns:*
            - **bool** (`bool`): True if the module file or package exists, False otherwise.
    *   **`init_exports_symbol`**
        *   *Signature:* `def init_exports_symbol(rel_base, symbol)`
        *   *Description:* This method checks if a given symbol is exported by an `__init__.py` file within a specified relative base path. It reads the `__init__.py` file, parses its content, and looks for the symbol either in the `__all__` list or as a defined function, class, or assignment. It returns `True` if the symbol is found and exported, and `False` otherwise, including cases where `__init__.py` does not exist or parsing fails.
        *   *Parameters:*
            - **rel_base** (`Path`): The relative base path to the directory containing the `__init__.py` file.
            - **symbol** (`str`): The name of the symbol (function, class, variable) to check for.
        *   *Returns:*
            - **bool** (`bool`): True if the symbol is exported by the `__init__.py` file, False otherwise.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method is called when an `ast.Import` or `ast.ImportFrom` node is encountered during AST traversal. It processes the imported names and adds them to the `import_dependencies` dictionary, mapping the current filename to a set of imported module names. If a `base_name` is provided (typically from `visit_ImportFrom`), it's added; otherwise, the direct alias name is used. It ensures that the `import_dependencies` dictionary is initialized for the current filename and then calls `generic_visit` to continue traversal.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the FileDependencyGraph class.
            - **node** (`Import | ImportFrom`): The AST node representing the import statement.
            - **base_name** (`str | None`): An optional base name to add to the dependencies, often used for resolving specific parts of an import.
        *   *Returns:* None
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent imports like `from module import name`. It first extracts the module name. If the module name is directly available, it uses the last part of the module name as the `base_name` and calls `visit_Import`. If the import is relative (module name is `None`), it calls `_resolve_module_name` to determine the actual module(s) and then calls `visit_Import` for each resolved name. Any `ImportError` during relative import resolution is caught and printed.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the FileDependencyGraph class.
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:* None

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes a filename, an Abstract Syntax Tree (AST) of the file, and the repository root as input. The function initializes a NetworkX directed graph and uses a custom visitor, `FileDependencyGraph`, to traverse the AST and identify import dependencies. It then populates the graph by adding nodes for each file and edges representing the import relationships. Finally, it returns the constructed graph.
*   **Parameters:**
    - **filename** (`str`): The name of the file for which the dependency graph is being built.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) representing the structure of the input file.
    - **repo_root** (`str`): The absolute path to the root directory of the repository.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies.
*   **Usage:**
    - **Calls:** This function initializes a NetworkX DiGraph, instantiates and uses a FileDependencyGraph visitor to process the AST, and then adds nodes and edges to the graph based on the identified import dependencies.
    - **Called By:** This function is called by the `build_repository_graph` function in the `File_Dependency.py` file.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a directed graph representing the dependencies between Python files within a Git repository. It iterates through all Python files, parses their content to build individual file dependency graphs, and then merges these into a single global graph. The function focuses on file-level dependencies, adding nodes for files and edges for calls between them. It filters out non-Python files and processes only files ending with '.py'.
*   **Parameters:**
    - **repository** (`GitRepository`): An object representing the Git repository to analyze, providing methods to access files and repository information.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent dependencies between them.
*   **Usage:**
    - **Calls:** This function calls methods such as `get_all_files`, `basename`, `endswith`, `removesuffix`, `parse`, `build_file_dependency_graph`, `add_node`, and `add_edge` to process files and construct the dependency graph.
    - **Called By:** This function is called by the `backend.File_Dependency` class constructor.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function identifies and returns all Python files within a specified directory and its subdirectories. It resolves the root path of the given directory and then uses a recursive glob pattern to find all files ending with the '.py' extension. The function returns a list of these files, represented as paths relative to the resolved root directory.
*   **Parameters:**
    - **directory** (`str`): The path to the directory to search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of Path objects, where each Path represents a Python file found within the directory, relative to the root path.
*   **Usage:**
    - **Calls:** This function calls Path, relative_to, resolve, and rglob methods, likely from the pathlib module, to manipulate and search for files within a directory structure.
    - **Called By:** This function is called by the _resolve_module_name method in File_Dependency.py.

#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G: nx.DiGraph)`
*   **Description:** This function takes a NetworkX directed graph (G) representing file dependencies and converts it into a Mermaid.js graph definition string. It organizes nodes into subgraphs based on their folder structure, creating a visual representation of how files within folders relate to each other. The function iterates through the graph's nodes to map files to their respective folders, then constructs Mermaid syntax for subgraphs and individual files. Finally, it adds edges to represent the dependencies between files, outputting a single string that can be rendered by Mermaid.
*   **Parameters:**
    - **G** (`nx.DiGraph`): A NetworkX directed graph where nodes represent file paths and edges represent dependencies between them.
*   **Returns:**
    - **mermaid_string** (`str`): A string formatted for Mermaid.js, representing the graph with files organized into folders as subgraphs.
*   **Usage:**
    - **Calls:** This function calls methods like append, defaultdict, items, join, replace, and split to process the graph data and construct the Mermaid string.
    - **Called By:** This function is called from the backend.File_Dependency module, specifically at line 238.

---
### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class is designed to interact with various Large Language Models (LLMs) for generating documentation. It centralizes the configuration of LLM parameters, prompt management, and batch processing for both function and class documentation generation. The class supports different LLM providers like Google Generative AI, OpenAI, and Ollama, and handles API key management, prompt file loading, and model-specific batch size configurations. It ensures structured output by using Pydantic models for validation and includes error handling for API calls and file operations.
*   **Instantiation:** `HelperLLM.py`, in function `main_orchestrator` (Line: 365), `main.py`, in function `main_workflow` (Line: 263)
*   **Dependencies:** This class depends on various LLM provider libraries (Google Generative AI, Ollama, OpenAI), Pydantic for data validation, and standard Python libraries for file handling, logging, and time management. It also relies on custom schema types like `FunctionAnalysis`, `ClassAnalysis`, `FunctionAnalysisInput`, and `ClassAnalysisInput`.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with necessary API credentials, prompt file paths, and LLM configuration. It loads system prompts for function and class documentation, configures batch settings based on the model name, and sets up specific LLM clients (e.g., ChatGoogleGenerativeAI, ChatOpenAI, ChatOllama) with structured output capabilities for `FunctionAnalysis` and `ClassAnalysis`. It also initializes a raw LLM client for general use.
    *   *Parameters:*
        - **api_key** (`str`): The API key for authenticating with the LLM service. Raises ValueError if not provided.
        - **function_prompt_path** (`str`): The file path to the system prompt used for function documentation generation. Raises FileNotFoundError if the file is not found.
        - **class_prompt_path** (`str`): The file path to the system prompt used for class documentation generation. Raises FileNotFoundError if the file is not found.
        - **model_name** (`str`): The name of the LLM model to use. Defaults to 'gemini-2.0-flash-lite'.
        - **ollama_base_url** (`str`): The base URL for Ollama if using an Ollama model. Defaults to a predefined OLLAMA_BASE_URL if not provided.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, function_prompt_path, class_prompt_path, model_name, ollama_base_url)`
        *   *Description:* Initializes the LLMHelper with necessary API credentials, prompt file paths, and LLM configuration. It loads system prompts for function and class documentation, configures batch settings based on the model name, and sets up specific LLM clients (e.g., ChatGoogleGenerativeAI, ChatOpenAI, ChatOllama) with structured output capabilities for `FunctionAnalysis` and `ClassAnalysis`. It also initializes a raw LLM client for general use.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the LLMHelper class.
            - **api_key** (`str`): The API key for authenticating with the LLM service. Raises ValueError if not provided.
            - **function_prompt_path** (`str`): The file path to the system prompt used for function documentation generation. Raises FileNotFoundError if the file is not found.
            - **class_prompt_path** (`str`): The file path to the system prompt used for class documentation generation. Raises FileNotFoundError if the file is not found.
            - **model_name** (`str`): The name of the LLM model to use. Defaults to 'gemini-2.0-flash-lite'.
            - **ollama_base_url** (`str`): The base URL for Ollama if using an Ollama model. Defaults to a predefined OLLAMA_BASE_URL if not provided.
        *   *Returns:* None
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* Configures the batch size for LLM API calls based on the specified model name. It defines different batch sizes for various Gemini and OpenAI models, and a default conservative batch size for unknown models. It logs a warning if an unknown model is encountered.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the LLMHelper class.
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:* None
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* Generates and validates documentation for a batch of function inputs using the configured LLM. It serializes the input data, constructs conversation prompts with system messages, and sends them to the LLM in batches. The method handles potential API errors by logging them and returning None for failed batches, while respecting rate limits by introducing a delay between batches. It returns a list of validated `FunctionAnalysis` objects or None for failed items.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the LLMHelper class.
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of FunctionAnalysisInput objects, each containing the necessary information to generate documentation for a function.
        *   *Returns:*
            - **all_validated_functions** (`List[Optional[FunctionAnalysis]]`): A list containing the generated and validated FunctionAnalysis objects for each input, or None if an error occurred during processing for a specific item.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* Generates and validates documentation for a batch of class inputs using the configured LLM. Similar to `generate_for_functions`, it serializes class input data, creates conversation prompts, and processes them in batches. It includes error handling for API calls and rate limit management with delays between batches. The method returns a list of validated `ClassAnalysis` objects or None for any items that failed processing.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the LLMHelper class.
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of ClassAnalysisInput objects, each containing the necessary information to generate documentation for a class.
        *   *Returns:*
            - **all_validated_classes** (`List[Optional[ClassAnalysis]]`): A list containing the generated and validated ClassAnalysis objects for each input, or None if an error occurred during processing for a specific item.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a testing orchestrator for the LLMHelper class, simulating the process of generating documentation for Python classes and their methods. It defines dummy input data for several functions ('add_item', 'check_stock', 'generate_report') and their corresponding pre-computed analyses. It then constructs a `ClassAnalysisInput` object for an 'InventoryManager' class, including the analyses of its methods. Finally, it utilizes an `LLMHelper` instance to generate documentation for these classes and prints the aggregated results in JSON format.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls backend.HelperLLM.py::ClassAnalysisInput, backend.HelperLLM.py::ClassContextInput, backend.HelperLLM.py::LLMHelper, backend.HelperLLM.py::dumps, backend.HelperLLM.py::generate_for_functions, backend.HelperLLM.py::info, backend.HelperLLM.py::model_dump, backend.HelperLLM.py::model_validate, backend.HelperLLM.py::print, and backend.HelperLLM.py::warning.
    - **Called By:** This function is called by backend.HelperLLM.

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the primary interface for interacting with Large Language Models (LLMs). It handles the initialization of different LLM providers (Google Generative AI or Ollama) based on the provided model name and configuration. The class is responsible for loading a system prompt from a file and then provides methods to either get a direct response from the LLM or stream the response in chunks. It manages API keys and base URLs, ensuring proper connection to the chosen LLM service.
*   **Instantiation:** `main.py`, in function `main_workflow` (Line: 377)
*   **Dependencies:** This class relies on external libraries for LLM interactions, specifically 'langchain_google_genai' for Google's models and 'langchain_ollama' for Ollama models. It also uses 'langchain.messages' for message formatting and 'logging' for output.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM class by setting up the LLM client. It validates the provided API key, loads the system prompt from a specified file, and configures the LLM client based on the model name. It supports models starting with 'gemini-' or 'gpt-' using ChatGoogleGenerativeAI, and other models using ChatOllama, with configurable base URLs. Error handling is included for file not found exceptions during prompt loading.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the LLM service (e.g., Google Generative AI).
        - **prompt_file_path** (`str`): The file path to the system prompt that will be used for all LLM interactions.
        - **model_name** (`str`): The name of the LLM model to use. Defaults to 'gemini-2.5-pro'.
        - **ollama_base_url** (`str`): The base URL for the Ollama service if using Ollama models. Defaults to a predefined OLLAMA_BASE_URL if not provided.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, prompt_file_path, model_name, ollama_base_url)`
        *   *Description:* Initializes the MainLLM class by setting up the LLM client. It validates the provided API key, loads the system prompt from a specified file, and configures the LLM client based on the model name. It supports models starting with 'gemini-' or 'gpt-' using ChatGoogleGenerativeAI, and other models using ChatOllama, with configurable base URLs. Error handling is included for file not found exceptions during prompt loading.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the MainLLM class.
            - **api_key** (`str`): The API key required for authenticating with the LLM service (e.g., Google Generative AI).
            - **prompt_file_path** (`str`): The file path to the system prompt that will be used for all LLM interactions.
            - **model_name** (`str`): The name of the LLM model to use. Defaults to 'gemini-2.5-pro'.
            - **ollama_base_url** (`str`): The base URL for the Ollama service if using Ollama models. Defaults to a predefined OLLAMA_BASE_URL if not provided.
        *   *Returns:* None
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method sends a user's input to the configured LLM and returns the complete response content. It constructs a list of messages including the system prompt and the user's input, then invokes the LLM client. If the LLM call is successful, it returns the content of the response. In case of any exceptions during the LLM invocation, it logs the error and returns None.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the MainLLM class.
            - **user_input** (`str`): The input string provided by the user to be processed by the LLM.
        *   *Returns:*
            - **response.content** (`str`): The text content generated by the LLM in response to the user input, or None if an error occurred.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method enables streaming of LLM responses, yielding content in chunks as it becomes available. It prepares messages similar to `call_llm` and then uses the LLM client's stream method to obtain an iterator. It iterates through the stream, yielding each chunk of content. If an error occurs during the streaming process, it logs the error and yields an error message.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the MainLLM class.
            - **user_input** (`str`): The input string provided by the user to be processed by the LLM for streaming.
        *   *Returns:*
            - **chunk.content** (`str`): Yields chunks of text content as they are generated by the LLM, or an error message if an exception occurs.

---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract fundamental project information from common project files such as README, pyproject.toml, and requirements.txt. It initializes a structured dictionary to hold project overview and installation details, populating it by parsing these files in a prioritized order. The class aims to provide a consolidated view of project metadata, including title, description, key features, tech stack, installation instructions, and dependencies.
*   **Instantiation:** `main.py`, in function `main_workflow` (Line: 139)
*   **Dependencies:** This class utilizes standard Python libraries such as `re` for regular expressions, `os` for operating system path operations, and `tomllib` for parsing TOML files. It also relies on type hinting modules like `typing.List`, `typing.Dict`, and `typing.Optional`.
*   **Constructor:**
    *   *Description:* Initializes the ProjektInfoExtractor with a default structure for project information and defines a constant for indicating missing information. The `self.info` attribute is a dictionary pre-populated with nested dictionaries for 'projekt_uebersicht' (project overview) and 'installation', each containing placeholders for various details.
    *   *Parameters:*
        - **self** (`ProjektInfoExtractor`): The instance of the class.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* Initializes the ProjektInfoExtractor with a default structure for project information and defines a constant for indicating missing information. The `self.info` attribute is a dictionary pre-populated with nested dictionaries for 'projekt_uebersicht' (project overview) and 'installation', each containing placeholders for various details.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
        *   *Returns:* None
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches through a list of file objects to find a file whose path matches one of the provided patterns. The search is case-insensitive, meaning it will find 'README.md' if the pattern is 'readme.md'. It iterates through each file and each pattern, returning the first file that matches a pattern.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **patterns** (`List[str]`): A list of file name patterns to search for (e.g., ['readme.md', 'pyproject.toml']).
            - **dateien** (`List[Any]`): A list of file objects, where each object is expected to have a 'path' attribute.
        *   *Returns:*
            - **Optional[Any]** (`Optional[Any]`): The first matching file object found, or None if no file matches any of the patterns.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private helper method extracts a specific section of text from a Markdown content string. It uses regular expressions to find a section that starts with a Markdown heading (##) followed by one of the provided keywords. It captures all text following the heading until the next heading or the end of the file, returning the stripped content.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The entire Markdown content as a string.
            - **keywords** (`List[str]`): A list of alternative keywords that can be used as section titles (e.g., ['Installation', 'Setup']).
        *   *Returns:*
            - **Optional[str]** (`Optional[str]`): The extracted text content of the section, stripped of leading/trailing whitespace, or None if the section is not found.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This private method parses the content of a README file to extract various project details. It attempts to find the project title from the first line, a description from the text following the title, key features, tech stack, current status, installation instructions, and quick start guide by calling the `_extrahiere_sektion_aus_markdown` helper method for specific sections. It updates the `self.info` dictionary with the extracted information.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the README file as a string.
        *   *Returns:* None
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This private method parses the content of a `pyproject.toml` file using the `tomllib` library. It attempts to extract the project name, description, and dependencies from the `[project]` section of the TOML data. If the `tomllib` library is not available, it prints a warning. It handles potential `TOMLDecodeError` exceptions during parsing.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the pyproject.toml file as a string.
        *   *Returns:* None
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This private method parses the content of a `requirements.txt` file to extract a list of dependencies. It splits the content into lines, strips whitespace from each line, and filters out empty lines and lines starting with a '#'. This method only populates the dependencies if they haven't already been found and set by `_parse_toml`, acting as a fallback.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the requirements.txt file as a string.
        *   *Returns:* None
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This is the main public method of the class that orchestrates the extraction of project information. It first identifies relevant project files (README, pyproject.toml, requirements.txt) using `_finde_datei`. Then, it parses these files in a specific order of priority: `pyproject.toml` first for metadata, followed by `requirements.txt` as a fallback for dependencies, and finally `README` for descriptive content. After parsing, it formats the dependencies and sets the project title based on the repository URL. The method returns the populated `self.info` dictionary.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **dateien** (`List[Any]`): A list of file objects representing the files in the repository.
            - **repo_url** (`str`): The URL of the repository, used to derive the project title.
        *   *Returns:*
            - **Dict[str, Any]** (`Dict[str, Any]`): A dictionary containing the extracted project information, structured into 'projekt_uebersicht' and 'installation' sections.

---
### File: `backend/callgraph.py`
#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST visitor designed to traverse Python code, identify function and method calls, and construct a directed graph representing these relationships. It processes different definition types like classes, functions, and asynchronous functions, and specifically handles call sites and conditional blocks like `if __name__ == '__main__'` to accurately map call chains within a given file. The class maintains internal state for the current file, class, and function being visited, along with data structures to store import mappings, function sets, and the call graph edges.
*   **Instantiation:** `callgraph.py`, in function `build_callGraph` (Line: 165)
*   **Dependencies:** This class relies on the `ast` module for parsing Python code into an Abstract Syntax Tree and `networkx` for graph manipulation. It also uses typing hints like `Dict` and `str`.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph visitor. It sets up attributes to track the current filename, function, and class being processed. It also initializes data structures for the graph itself, including a dictionary for import mappings, a set for all encountered functions, and a dictionary to store the call graph edges, mapping callers to sets of callees.
    *   *Parameters:*
        - **self** (`CallGraph`): The instance of the CallGraph class.
        - **filename** (`str`): The name of the file being analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename)`
        *   *Description:* Initializes the CallGraph visitor. It sets up attributes to track the current filename, function, and class being processed. It also initializes data structures for the graph itself, including a dictionary for import mappings, a set for all encountered functions, and a dictionary to store the call graph edges, mapping callers to sets of callees.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **filename** (`str`): The name of the file being analyzed.
        *   *Returns:* None
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* Recursively traverses an AST node to extract function call names. It handles different node types like `ast.Call`, `ast.Name`, and `ast.Attribute`. For `ast.Call`, it continues recursion on the function part. For `ast.Name` and `ast.Attribute`, it extracts the identifier or attribute name, respectively. It returns a list of extracted names, which are potential callees.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.AST`): The AST node to process.
        *   *Returns:*
            - **all_calls** (`list[str]`): A list of strings representing the extracted callee names.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* Resolves raw callee names into fully qualified names based on the current file and class context. If no class is currently being visited, it prefixes the callee name with the filename. If a class is active, it prefixes with both the filename and the class name. This ensures that callees are uniquely identified within the context of the analysis.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **callee_nodes** (`list[str]`): A list of raw callee names to resolve.
        *   *Returns:*
            - **resolved_callees** (`list[str]`): A list of fully qualified callee names.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* Constructs a fully qualified name for a function or method. It takes a base name and an optional class name. If a class name is provided, it formats the name as 'filename::className::basename'. Otherwise, it formats it as 'filename::basename'. This ensures consistent naming for nodes in the call graph.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`str | None`): The name of the class, if the function is a method. Defaults to None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* Determines the current caller string for the call graph. If `self.current_function` is set, it returns that value. Otherwise, it returns a string representing the filename if available, or '<global-scope>' if the filename is also not available. This helps in identifying the context from which a call is made.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
        *   *Returns:*
            - **caller** (`str`): The string representing the current caller.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Visits an `ast.ClassDef` node, which represents a class definition. It temporarily sets `self.current_class` to the name of the class being visited, then iterates through the nodes in the class body, recursively visiting each one. After processing the class body, it restores the previous `self.current_class` value to maintain the correct context.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:* None
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Visits an `ast.FunctionDef` node, representing a standard function definition. It determines the fully qualified name of the function using `_make_full_name`, adds the function as a node to the graph, and then recursively visits the function's body using `generic_visit`. Finally, it adds the function to a set of all functions and resets `self.current_function` to `None`.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:* None
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Visits an `ast.AsyncFunctionDef` node, which represents an asynchronous function definition (defined with `async def`). This method simply delegates the visit operation to `visit_FunctionDef`, as the logic for handling asynchronous functions is identical to that of regular functions in terms of call graph construction.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing the asynchronous function definition.
        *   *Returns:* None
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Visits an `ast.Call` node, representing a function or method call. It determines the current caller, extracts raw callee names using `_recursive_call`, resolves them into fully qualified names using `_resolve_all_callee_names`, and then adds the corresponding edge to the call graph stored in `self.edges`. It includes error handling to gracefully manage unexpected issues during call processing.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.Call`): The AST node representing the function call.
        *   *Returns:* None
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* Visits an `ast.If` node, specifically checking for the common `if __name__ == "__main__"` construct. If this condition is met, it temporarily sets the `self.current_function` to a special marker '<main_block>' to distinguish calls made within this block. It then recursively visits the nodes within the `if` block and restores the original `self.current_function` afterwards. Otherwise, it simply proceeds with a generic visit.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.If`): The AST node representing the if statement.
        *   *Returns:* None

#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree: ast.AST, filename: str)`
*   **Description:** This function constructs a call graph from a Python Abstract Syntax Tree (AST). The resulting graph is a directed graph (networkx.DiGraph) where nodes represent functions, methods, and scopes (global or main block), and edges represent function or method calls between them. It initializes a `CallGraph` visitor, traverses the AST to populate the visitor's data, and then adds edges to the graph based on the collected caller-callee relationships. Finally, it returns the complete call graph.
*   **Parameters:**
    - **tree** (`ast.AST`): The Abstract Syntax Tree of the Python file to be analyzed.
    - **filename** (`str`): The name of the analyzed file, used for context within the call graph.
*   **Returns:**
    - **graph** (`nx.DiGraph`): The complete directed call graph representing function and method calls within the analyzed Python code.
*   **Usage:**
    - **Calls:** This function utilizes a `CallGraph` visitor, calls its `visit` method, accesses its `edges` and `graph` attributes, and uses the `add_edge` method to build the graph.
    - **Called By:** This function is called by `analyze_repository` in `AST_Schema.py` and `build_global_callgraph` in `callgraph.py`.

#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph: nx.DiGraph)`
*   **Description:** This function converts a directed graph (nx.DiGraph) from the networkx library into an adjacency list format, which is suitable for JSON serialization. It iterates through each node in the graph, retrieves its successors (functions it calls), and stores this information in a dictionary. The keys of the dictionary represent the calling nodes (callers), and the values are lists of the called nodes (callees). The function ensures a consistent output by sorting both the nodes and their successors before adding them to the adjacency list. Only nodes that actually call other functions are included in the final output.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The directed graph representing the call graph to be converted.
*   **Returns:**
    - **adj_list** (`Dict[str, list[str]]`): An adjacency list where keys are caller nodes (strings) and values are lists of callee nodes (strings).
*   **Usage:**
    - **Calls:** This function calls internal list operations, graph node and successor retrieval methods, and sorting functions.
    - **Called By:** This function is not called by any other function within the provided context.

#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(repo: GitRepository)`
*   **Description:** This function constructs a global call graph for a given Git repository. It iterates through all Python files in the repository, parses their Abstract Syntax Trees (ASTs), and builds a call graph for each file. These individual file call graphs are then merged into a single, comprehensive global call graph. The function uses the `networkx` library to represent the graph structure, where nodes represent functions or methods and edges represent calls between them. It handles file filtering to process only Python files and extracts filenames for context within the graph.
*   **Parameters:**
    - **repo** (`GitRepository`): An object representing the Git repository to analyze, providing access to its files.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the global call graph of the repository, where nodes are functions/methods and edges indicate calls.
*   **Usage:**
    - **Calls:** This function calls methods for file system operations (like `endswith`, `basename`, `removesuffix`), AST parsing (`ast.parse`), building individual call graphs (`build_callGraph`), and graph manipulation (`nx.DiGraph`, `add_node`, `add_edge`). It also utilizes repository methods to retrieve all files (`get_all_files`).
    - **Called By:** This function is called from the `backend.callgraph` module at line 262.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and an output path as input. It creates a safe representation of the graph by relabeling its nodes to be simple sequential identifiers (e.g., 'n0', 'n1'). This is likely done to avoid issues with special characters or complex names in the DOT format. The original node names are preserved as labels in the relabeled graph. Finally, it writes the modified graph to a DOT file at the specified output path.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The input directed graph to be processed.
    - **out_path** (`str`): The file path where the DOT representation of the graph will be saved.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls methods for copying graphs, iterating through nodes, relabeling nodes, and writing the graph to a DOT file.
    - **Called By:** This function is called from the `backend.callgraph` module.

---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It is designed for lazy loading of file content and metadata, meaning that attributes like the file's blob object, content, and size are only fetched when they are first accessed. This class provides methods to access file properties, analyze its content (like word count), and represent the file as a dictionary.
*   **Instantiation:** `getRepo.py`, in function `get_all_files` (Line: 111)
*   **Dependencies:** This class depends on the 'git' library for interacting with Git repositories and the 'os' module for path manipulations.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object by storing the file path and the commit tree it belongs to. It also sets up internal attributes for lazy loading of the blob, content, and size, initializing them to None.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, file_path, commit_tree)`
        *   *Description:* Initializes a RepoFile object by storing the file path and the commit tree it belongs to. It also sets up internal attributes for lazy loading of the blob, content, and size, initializing them to None.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the RepoFile class.
            - **file_path** (`str`): The path to the file within the repository.
            - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
        *   *Returns:* None
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property lazily loads and returns the Git blob object for the file. If the blob has not been loaded yet, it attempts to retrieve it from the associated commit tree using the file's path. If the file is not found in the tree, it raises a FileNotFoundError.
        *   *Parameters:* None
        *   *Returns:*
            - **self._blob** (`git.Blob`): The Git blob object representing the file.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property lazily loads, decodes, and returns the content of the file. It first accesses the file's blob object (which itself might be lazily loaded) and then reads its data stream. The content is decoded from bytes to a UTF-8 string, with errors ignored during decoding.
        *   *Parameters:* None
        *   *Returns:*
            - **self._content** (`str`): The decoded content of the file as a string.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property lazily loads and returns the size of the file in bytes. It retrieves the size directly from the file's blob object, which is loaded on demand if it hasn't been already.
        *   *Parameters:* None
        *   *Returns:*
            - **self._size** (`int`): The size of the file in bytes.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method performs a simple analysis on the file's content by counting the number of words. It accesses the file's content (which is lazily loaded) and then splits the content into words based on whitespace, returning the total count.
        *   *Parameters:* None
        *   *Returns:*
            - **word_count** (`int`): The total number of words found in the file's content.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* Provides a developer-friendly string representation of the RepoFile object. It includes the file's path, making it easy to identify the object when debugging or inspecting.
        *   *Parameters:* None
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, e.g., "<RepoFile(path='...')>".
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* Converts the RepoFile object into a dictionary representation. By default, it includes the file's path, name, size, and type. Optionally, if 'include_content' is set to True, it also includes the file's content in the dictionary.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the RepoFile class.
            - **include_content** (`bool`): A flag to determine if the file's content should be included in the dictionary.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing file metadata and optionally its content.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class is designed to manage a Git repository by cloning it into a temporary directory. It provides methods to access files within the repository, retrieve them as RepoFile objects, and construct a hierarchical file tree. The class also handles cleanup by deleting the temporary directory upon completion, making it suitable for use in contexts where temporary access to a repository is needed.
*   **Instantiation:** `main.py`, in function `main_workflow` (Line: 120)
*   **Dependencies:** This class depends on external libraries such as `tempfile` for temporary directory creation, `shutil` for file operations (though commented out in `close`), `git.Repo` and `git.GitCommandError` for Git repository interactions, and `logging` for information output. It also relies on a `RepoFile` class which is not defined in the provided source code.
*   **Constructor:**
    *   *Description:* Initializes the GitRepository by storing the repository URL, creating a temporary directory, and cloning the repository into it. It attempts to clone the repository using the provided URL and logs the process. If cloning fails, it cleans up and raises a RuntimeError. It also initializes attributes for files and the latest commit information.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, repo_url)`
        *   *Description:* Initializes the GitRepository by storing the repository URL, creating a temporary directory, and cloning the repository into it. It attempts to clone the repository using the provided URL and logs the process. If cloning fails, it cleans up and raises a RuntimeError. It also initializes attributes for files and the latest commit information.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
            - **repo_url** (`str`): The URL of the Git repository to be cloned.
        *   *Returns:* None
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* Retrieves all files from the cloned Git repository and returns them as a list of RepoFile objects. It uses the Git command `ls-files` to get a list of file paths, then iterates through these paths to create RepoFile instances, associating each with the commit tree. This method populates the `self.files` attribute.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list containing RepoFile objects, each representing a file in the repository.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* Cleans up by deleting the temporary directory that was created for the Git repository. It checks if `self.temp_dir` is set before attempting to remove the directory and its contents, and then sets `self.temp_dir` to None to indicate that cleanup has occurred. A message is printed to the console indicating the directory being deleted.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:* None
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* Implements the context management protocol, returning the instance of the GitRepository itself. This allows the class to be used with the `with` statement, ensuring that resources are properly managed.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **self** (`GitRepository`): The current instance of the GitRepository.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* Implements the context management protocol's exit behavior. It ensures that the `close` method is called to clean up the temporary directory, regardless of whether an exception occurred within the `with` block. It receives exception details as arguments but does not explicitly handle them, allowing exceptions to propagate.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
            - **exc_type** (`type`): The type of the exception raised in the `with` block, if any.
            - **exc_val** (`Exception`): The exception instance raised in the `with` block, if any.
            - **exc_tb** (`traceback`): The traceback object associated with the exception, if any.
        *   *Returns:* None
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* Constructs and returns a hierarchical tree structure representing the files and directories within the repository. If no files have been loaded, it first calls `get_all_files`. It then iterates through the file paths, building the directory structure and adding each file (optionally including its content) as a dictionary to the appropriate level in the tree. The root of the tree is always named 'root'.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
            - **include_content** (`bool`): A boolean flag indicating whether to include the content of each file in the returned tree structure. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical structure of the repository's files and directories.

---
### File: `backend/main.py`
#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: Any, end_time: Any, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the net time spent on a task, excluding time spent sleeping due to rate limits. It takes the start and end times, total items processed, batch size, and model name as input. If the model name does not start with 'gemini-', the total duration is returned directly. For 'gemini-' models, it calculates the number of batches, the total sleep time based on the number of batches, and subtracts this sleep time from the total duration. The function ensures that the returned net time is not negative.
*   **Parameters:**
    - **start_time** (`Any`): The timestamp when the task started.
    - **end_time** (`Any`): The timestamp when the task ended.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model being used.
*   **Returns:**
    - **net_time** (`Any`): The calculated net time, excluding sleep durations, or the total duration if the model is not 'gemini-' based. Returns 0 if total_items is 0 for 'gemini-' models. The returned value is guaranteed to be non-negative.
*   **Usage:**
    - **Calls:** This function calls math.ceil to determine the number of batches, math.max to ensure sleep count is non-negative and net time is non-negative, and the string method startswith to check the model name.
    - **Called By:** This function is called by the main_workflow function in main.py on lines 290 and 321.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: Any, api_keys: dict, model_names: dict, status_callback: Callable)`
*   **Description:** The main_workflow function orchestrates a complex process of analyzing a software repository to generate documentation. It begins by extracting a repository URL from user input and cloning the repository. It then proceeds to extract basic project information, construct a file tree, and perform relationship analysis (calls and instantiations) using specialized tools. The core of the workflow involves generating an Abstract Syntax Tree (AST) schema and enriching it with the relationship data. Finally, it prepares inputs for two Language Models (LLMs): a Helper LLM for analyzing individual functions and classes, and a Main LLM for generating a final report based on the combined analysis. The function handles API key management, model selection, and includes status callbacks for user feedback throughout the process. It also incorporates error handling and timing metrics for both LLM calls.
*   **Parameters:**
    - **input** (`Any`): The raw user input, expected to contain a repository URL.
    - **api_keys** (`dict`): A dictionary containing API keys for different services (e.g., 'gemini', 'gpt', 'ollama').
    - **model_names** (`dict`): A dictionary specifying the names of the models to be used for helper and main LLM tasks.
    - **status_callback** (`Callable`): An optional callback function to provide status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final generated documentation report as a string.
    - **metrics** (`dict`): A dictionary containing performance metrics, including helper LLM time, main LLM time, total active time, and the models used.
*   **Usage:**
    - **Calls:** *Analysis data not available for this component.*
    - **Called By:** This function is called by the Frontend.py script and the main.py module, indicating it serves as a central orchestrator for backend processing.

#### Function: `update_status`
*   **Signature:** `def update_status(msg: Any)`
*   **Description:** This function is designed to report status updates. It first checks if a callback function named 'status_callback' is defined and, if so, it invokes this callback with the provided message. Subsequently, it logs the message using the 'logging.info' function. This dual approach allows for both custom handling of status messages via the callback and standard logging for monitoring purposes.
*   **Parameters:**
    - **msg** (`Any`): The status message to be reported and logged.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls the 'logging.info' function and conditionally calls a 'status_callback' function.
    - **Called By:** This function is called multiple times within the 'main_workflow' function in 'main.py'.

---
### File: `backend/relationship_analyzer.py`
#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to parse a Python project, identify its code definitions (functions, classes, methods), and build a call graph to understand relationships between these elements. It traverses the project's file system, parses Python files using the AST module, and stores information about definitions and calls. Finally, it formats these findings into a structured list representing the call graph.
*   **Instantiation:** `main.py`, in function `main_workflow` (Line: 156)
*   **Dependencies:** This class relies on standard Python libraries such as `ast` for parsing code, `os` for file system operations, `logging` for error reporting, and `collections.defaultdict` for managing the call graph. It also implicitly depends on external components like `path_to_module` and `CallResolverVisitor` which are not defined within the provided source code.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer with the root directory of the project. It sets up instance attributes to store project root, definitions, call graph, file ASTs, and a set of directories to ignore during file traversal. The project root path is normalized to an absolute path.
    *   *Parameters:*
        - **project_root** (`string`): The absolute path to the root directory of the project to be analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, project_root)`
        *   *Description:* The constructor initializes the ProjectAnalyzer with the root directory of the project. It sets up instance attributes to store project root, definitions, call graph, file ASTs, and a set of directories to ignore during file traversal. The project root path is normalized to an absolute path.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
            - **project_root** (`string`): The absolute path to the root directory of the project to be analyzed.
        *   *Returns:* None
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This is the main method to initiate the project analysis. It first finds all Python files within the project, then iterates through them to collect all code definitions (functions, classes, methods) and subsequently resolves the call relationships between them. After processing, it clears the stored ASTs to free up memory and returns the formatted results of the analysis.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
        *   *Returns:*
            - **output_list** (`list`): A list of dictionaries, where each dictionary represents a definition and details the functions or methods that call it.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private method recursively walks through the project directory starting from `self.project_root`. It identifies all Python files (`.py`) while excluding specified directories like `.git`, `venv`, `__pycache__`, etc. The method returns a list of absolute paths to all found Python files.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
        *   *Returns:*
            - **py_files** (`list`): A list of strings, where each string is the absolute path to a Python file found in the project.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method parses a given Python file to extract code definitions such as functions, classes, and methods. It reads the source code, uses the `ast` module to build an Abstract Syntax Tree (AST), and then walks the tree to identify definition nodes. For each definition, it records its type, file path, line number, and constructs a unique path name. It stores the AST for later use and handles potential file reading or parsing errors by logging them.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
            - **filepath** (`string`): The path to the Python file to be parsed.
        *   *Returns:* None
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This private helper method traverses the AST of a given tree to find the direct parent node of a specified child node. It iterates through all nodes in the tree and checks their child nodes to locate the target node, returning its parent. If the node is not found or has no parent within the tree, it returns None.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
            - **tree** (`ast.AST`): The Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node whose parent is to be found.
        *   *Returns:*
            - **parent** (`ast.AST | None`): The parent node of the given node, or None if no parent is found.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method analyzes the AST of a given Python file to identify function and method calls. It instantiates a `CallResolverVisitor` (presumably a custom visitor class) which traverses the AST and records call information. The collected call data, mapping callees to their callers, is then merged into the class's main `call_graph` attribute. Errors during the resolution process are logged.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
            - **filepath** (`string`): The path to the Python file whose calls are to be resolved.
        *   *Returns:* None
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* This method formats the collected call graph data into a user-friendly list of dictionaries. It iterates through the `self.call_graph`, and for each callee, it retrieves its definition information. It then processes the list of callers for that callee, ensuring uniqueness of call sites (file, line, caller) and structures the output to include the callee's identifier, mode, origin file and line, and a list of callers with their respective file, function, mode, and line number. Definitions not found in `self.definitions` are skipped.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
        *   *Returns:*
            - **output_list** (`list`): A list of dictionaries, where each dictionary details a definition and the functions/methods that call it.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is designed to traverse an Abstract Syntax Tree (AST) of Python code to identify and resolve function and method calls. It maintains scope information, tracks imported modules and aliases, and records the types of instantiated classes to accurately determine the fully qualified names of called functions or methods. This allows for the construction of a call graph, mapping where specific definitions are invoked from within the codebase.
*   **Instantiation:** `relationship_analyzer.py`, in function `_resolve_calls` (Line: 92)
*   **Dependencies:** This class utilizes the 'ast' module for parsing Python code into an Abstract Syntax Tree, the 'os' module for path manipulations (specifically os.path.basename), and 'collections.defaultdict' for efficiently storing call information. It also relies on an external function `path_to_module` for converting file paths to module paths.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and a dictionary of known definitions. It sets up internal state to track the current scope, instance types, caller information, and a defaultdict to store call relationships.
    *   *Parameters:*
        - **filepath** (`str`): The absolute path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the project, used for resolving module paths.
        - **definitions** (`dict`): A dictionary containing known definitions within the project, mapping qualified names to their details.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filepath, project_root, definitions)`
        *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and a dictionary of known definitions. It sets up internal state to track the current scope, instance types, caller information, and a defaultdict to store call relationships.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the CallResolverVisitor class.
            - **filepath** (`str`): The absolute path to the Python file being analyzed.
            - **project_root** (`str`): The root directory of the project, used for resolving module paths.
            - **definitions** (`dict`): A dictionary containing known definitions within the project, mapping qualified names to their details.
        *   *Returns:* None
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Visits a class definition node in the AST. It temporarily stores the current class name, updates the `current_class_name` to the newly encountered class, recursively visits child nodes within the class definition, and then restores the previous class name upon exiting the class scope.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* None
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Visits a function definition node in the AST. It temporarily stores the current caller name, updates `current_caller_name` to the name of the function being defined, recursively visits any nodes within the function body, and then restores the previous caller name.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* None
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Visits a call expression node in the AST. It attempts to resolve the fully qualified name of the called function or method using `_resolve_call_qname`. If the resolved name exists in the project's definitions, it records the call information, including the caller's file, line number, name, and type (module, method, or function), and appends it to the `calls` dictionary. It then continues the traversal.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:* None
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Visits an import statement node. It iterates through the imported aliases, updating the `scope` dictionary with the mapping from the imported name (or its alias) to its module path. It then continues the AST traversal.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* None
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Visits an import-from statement node. It processes each imported name, determining its full module path based on the current module's path and the import level. It then stores this mapping in the `scope` dictionary and continues the AST traversal.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.ImportFrom`): The AST node representing an import-from statement.
        *   *Returns:* None
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* Visits an assignment statement node. If the assignment involves calling a class constructor (e.g., `variable = ClassName(...)`), it identifies the class name, resolves its qualified name using the `scope`, and if the class is defined within the project, it records the mapping from the variable name to the qualified class name in the `instance_types` dictionary. It then continues the AST traversal.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:* None
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* A helper method to resolve the fully qualified name (QName) of a called function or method from its AST node. It handles cases where the call is a direct name (function or module) or an attribute access (method call on an object or module attribute). It uses the `scope` and `instance_types` dictionaries to perform the resolution. Returns `None` if the QName cannot be resolved.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., ast.Name or ast.Attribute).
        *   *Returns:*
            - **qualified_name** (`str | None`): The fully qualified name of the function or method, or None if it cannot be resolved.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into a Python module path. It first calculates the relative path of the file with respect to a project root. If the file is a Python file (ends with '.py'), the extension is removed. The path separators are then replaced with dots to form a module path. Special handling is included for '__init__.py' files, where the trailing '__init__' is removed from the module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the file.
    - **project_root** (`str`): The root directory of the project from which the relative path is calculated.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path derived from the filepath.
*   **Usage:**
    - **Calls:** This function utilizes os.path.relpath, os.path.basename, str.endswith, and str.replace to manipulate file paths and convert them into module paths.
    - **Called By:** This function is called by '_collect_definitions' and '__init__' within the 'relationship_analyzer.py' file.

---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function encrypts a given string using a pre-defined cipher suite. It first checks if the input text is empty or if the cipher suite is not initialized. If either condition is true, it returns the original text without encryption. Otherwise, it encodes the input text into bytes, encrypts these bytes using the cipher suite, and then decodes the resulting encrypted bytes back into a string before returning it.
*   **Parameters:**
    - **text** (`str`): The string to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string, or the original string if encryption could not be performed.
*   **Usage:**
    - **Calls:** This function calls the encode and decode methods on the input string, and the encrypt method on the cipher_suite object.
    - **Called By:** This function is called by the update_gemini_key function in db.py.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function decrypts a given string using a cipher suite. It first checks if the input text or the cipher suite is invalid; if so, it returns the original text. Otherwise, it attempts to decrypt the text by encoding it, decrypting it, and then decoding the result. If any exception occurs during the decryption process, the original text is returned.
*   **Parameters:**
    - **text** (`str`): The encrypted text string to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted string, or the original string if decryption fails or is not possible.
*   **Usage:**
    - **Calls:** This function calls encode, decrypt, and decode methods, likely related to cryptographic operations.
    - **Called By:** This function is called by the get_decrypted_api_keys function in db.py.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function inserts a new user record into a database collection named 'dbusers'. It takes a username, name, and password as input. The password is hashed using a provided hashing function before being stored along with other user details like API keys and base URLs. The function returns the unique identifier of the newly inserted user record.
*   **Parameters:**
    - **username** (`str`): The unique username for the new user.
    - **name** (`str`): The full name of the new user.
    - **password** (`str`): The plain text password for the new user, which will be hashed.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier of the newly inserted user document in the database.
*   **Usage:**
    - **Calls:** This function calls a hashing function (likely from 'stauth.hasher') to hash the password and 'dbusers.insert_one' to insert the user document into the database.
    - **Called By:** This function is not called by any other functions within the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user records from a database collection named 'dbusers'. It queries the collection and converts the result into a list. The function is designed to fetch all available user data without any filtering or specific selection criteria.
*   **Parameters:** None
*   **Returns:**
    - **users** (`list`): A list containing all user documents fetched from the database.
*   **Usage:**
    - **Calls:** This function calls the 'find' method on the 'dbusers' object and the 'list' constructor.
    - **Called By:** This function is called by the 'frontend.Frontend' constructor in the 'Frontend.py' file.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** This function retrieves a single user record from the database based on their username. It queries the `dbusers` collection using the provided username as the document's `_id`. The function then returns the found user document or None if no user matches the given username.
*   **Parameters:**
    - **username** (`str`): The username of the user to fetch from the database.
*   **Returns:**
    - **user** (`Any`): The user document found in the database, or None if the user does not exist.
*   **Usage:**
    - **Calls:** This function calls `database/db.py::find_one` to perform the database query.
    - **Called By:** This function is not called by any other functions within the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates the Gemini API key for a given user in the database. It first encrypts the provided API key using a helper function `encrypt_text`. Then, it uses the `update_one` method to find the user by their username and set the encrypted API key in the database. The function returns the count of modified documents, indicating whether the update was successful.
*   **Parameters:**
    - **username** (`str`): The username of the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be set for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database. Typically 1 if the update was successful, 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls `encrypt_text` to encrypt the API key and `update_one` to modify the database record.
    - **Called By:** This function is called by the `frontend.Frontend` class in `Frontend.py`.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama Base URL for a specific user in the database. It takes the username and the new Ollama base URL as input. The function then uses the `dbusers.update_one` method to find the user document by their username and set the `ollama_base_url` field to the provided value. Finally, it returns the count of modified documents, which should ideally be 1 if the update was successful.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama URL needs to be updated.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service to be associated with the user.
*   **Returns:**
    - **modified_count** (`int`): An integer representing the number of documents that were modified in the database. This is expected to be 1 if the update was successful for the specified user.
*   **Usage:**
    - **Calls:** This function calls the `database/db.py::update_one` method to perform the database update operation.
    - **Called By:** This function is called by the `frontend.Frontend` constructor in the `Frontend.py` file.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** This function retrieves the Gemini API key associated with a given username from the database. It queries the database for a specific user's record and extracts the 'gemini_api_key' field. If the key is found, it is returned; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The username of the user whose Gemini API key needs to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key for the specified user, or None if not found.
*   **Usage:**
    - **Calls:** This function calls `dbusers.find_one` to query the database and `user.get` to safely retrieve the API key from the result.
    - **Called By:** This function is not called by any other function within the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama Base URL associated with a specific username from a database. It queries the database for a user document based on the provided username and extracts the 'ollama_base_url' field. If the user or the URL is not found, it returns None.
*   **Parameters:**
    - **username** (`str`): The username to look up in the database.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama Base URL for the specified user, or None if not found.
*   **Usage:**
    - **Calls:** This function calls `dbusers.find_one` to retrieve user data and then uses the `.get()` method on the result to safely access the 'ollama_base_url'.
    - **Called By:** This function is not called by any other functions within the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function deletes a user from the database based on their username. It interacts with a database collection named 'dbusers' to perform the deletion. The function returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted from the database. This is expected to be 1 if the user existed and was deleted, or 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls the `delete_one` method on the `dbusers` object.
    - **Called By:** This function is not called by any other function within the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys for a given username from the database. It first fetches the user's record using the provided username. If the user is not found, it returns None for both API keys. Otherwise, it decrypts the 'gemini_api_key' and retrieves the 'ollama_base_url' from the user's record, returning both decrypted values.
*   **Parameters:**
    - **username** (`str`): The username of the user whose API keys are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user is not found or the key is missing.
    - **ollama_plain** (`str`): The Ollama base URL, or an empty string if the user is not found or the URL is missing.
*   **Usage:**
    - **Calls:** This function calls `database/db.py::decrypt_text` to decrypt the Gemini API key, `database/db.py::find_one` to retrieve the user record, and `database/db.py::get` to access user data.
    - **Called By:** This function is called by the `frontend.Frontend` class in `Frontend.py` at lines 233 and 295.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str)`
*   **Description:** This function inserts a new conversation exchange into a database. It takes various parameters related to a user's question, the AI's answer, feedback, user details, chat information, and performance metrics. The function constructs a dictionary containing all this information, including a timestamp of when the exchange was created, and then uses `dbexchanges.insert_one` to add this record to the database. Finally, it returns the unique identifier of the newly inserted record.
*   **Parameters:**
    - **question** (`str`): The user's question.
    - **answer** (`str`): The AI's answer to the question.
    - **feedback** (`str`): User feedback on the answer.
    - **username** (`str`): The username of the user.
    - **chat_name** (`str`): The name of the chat session.
    - **helper_used** (`str`): Information about whether a helper was used (optional, defaults to empty string).
    - **main_used** (`str`): Information about whether the main model was used (optional, defaults to empty string).
    - **total_time** (`str`): Total processing time (optional, defaults to empty string).
    - **helper_time** (`str`): Processing time for the helper model (optional, defaults to empty string).
    - **main_time** (`str`): Processing time for the main model (optional, defaults to empty string).
*   **Returns:**
    - **result.inserted_id** (`Any`): The unique identifier of the newly inserted exchange record.
*   **Usage:**
    - **Calls:** This function calls `dbexchanges.insert_one` to insert a document and `datetime.now` to get the current timestamp.
    - **Called By:** This function is called by `Frontend.Frontend` in `Frontend.py`.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves exchange records associated with a specific username from a database. It queries a collection named 'dbexchanges' for documents matching the provided username and returns the results as a list. The function is designed to fetch user-specific transaction or exchange data.
*   **Parameters:**
    - **username** (`str`): The username to filter exchange records by.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents found for the specified username.
*   **Usage:**
    - **Calls:** This function calls the `find` method on `dbexchanges` and converts the result to a list.
    - **Called By:** This function is called by `load_data_from_db` in `Frontend.py`.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a list of exchanges associated with a specific user and chat name from a database. It queries the database for documents matching the provided username and chat name, then converts the result into a list. The function is designed to fetch historical chat data.
*   **Parameters:**
    - **username** (`str`): The username of the user whose exchanges are to be fetched.
    - **chat_name** (`str`): The name of the chat for which exchanges are to be fetched.
*   **Returns:**
    - **exchanges** (`list`): A list of dictionaries, where each dictionary represents an exchange document from the database.
*   **Usage:**
    - **Calls:** This function calls the `find` method on `dbexchanges` and converts the result to a list.
    - **Called By:** This function is not called by any other function within the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function updates the feedback associated with a specific exchange in the database. It takes an exchange ID and an integer feedback value as input. The function then uses the `update_one` method to modify the 'feedback' field for the matching exchange document. Finally, it returns the count of documents that were modified.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange to be updated.
    - **feedback** (`int`): The new feedback value to be set for the exchange. This should be an integer.
*   **Returns:**
    - **modified_count** (`int`): An integer representing the number of documents that were successfully modified in the database. Typically, this will be 1 if the update was successful, or 0 if no document matched the provided exchange_id.
*   **Usage:**
    - **Calls:** This function calls the `update_one` method, presumably from a database collection object named `dbexchanges`, to perform the update operation.
    - **Called By:** This function is called by the `handle_feedback_change` function in the `Frontend.py` file.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates the feedback message associated with a specific exchange in the database. It takes an exchange ID and a feedback message string as input. The function then uses the `dbexchanges.update_one` method to find the exchange by its ID and set the `feedback_message` field to the provided value. Finally, it returns the count of documents that were modified.
*   **Parameters:**
    - **exchange_id** (`any`): The unique identifier of the exchange to be updated.
    - **feedback_message** (`str`): The new feedback message to be associated with the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database. This is typically 1 if the update was successful, or 0 if the exchange was not found or the message was unchanged.
*   **Usage:**
    - **Calls:** This function calls the `database/db.py::update_one` method to perform the database update.
    - **Called By:** This function is called by the `render_exchange` function in the `Frontend.py` file.

#### Function: `delete_chats_by_user`
*   **Signature:** `def delete_chats_by_user(username: str, chat_name: str)`
*   **Description:** This function deletes all exchanges associated with a specific user and chat name from the database. It utilizes a helper function `dbexchanges.delete_many` to perform the deletion operation. The function then returns the count of deleted documents.
*   **Parameters:**
    - **username** (`str`): The username of the user whose chats are to be deleted.
    - **chat_name** (`str`): The name of the chat from which exchanges should be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted from the database.
*   **Usage:**
    - **Calls:** This function calls the `database/db.py::delete_many` function to remove records from the database.
    - **Called By:** This function is invoked by the `handle_delete_chat` function in `Frontend.py`.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function deletes a specific exchange record from the database using its unique identifier. It interacts with a database collection named 'dbexchanges' to perform the deletion operation. The function returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted from the database. This is typically 1 if the exchange was found and deleted, and 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls the 'delete_one' method on the 'dbexchanges' collection to remove a single document matching the provided exchange ID.
    - **Called By:** This function is called by the 'handle_delete_exchange' function in the 'Frontend.py' file.

---
### File: `frontend/Frontend.py`
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function loads existing chat data from a database into the Streamlit session state. It initializes the session state for chats if 'data_loaded' is not already set. The function fetches exchanges for a given username from the database, organizing them by chat name. If a chat name does not exist, it is created. It also handles missing feedback data by setting it to NaN. Finally, it ensures that there is at least one chat available and sets the active chat, marking the data as loaded in the session state.
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat data.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls methods such as append, fetch_exchanges_by_user, get, keys, and list.
    - **Called By:** This function is called by the frontend.Frontend constructor in Frontend.py.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: dict, val: any)`
*   **Description:** This function updates the feedback associated with an exchange in the application's state and database. It takes an exchange dictionary and a new feedback value as input. The function first modifies the 'feedback' key within the provided exchange dictionary to the new value. Subsequently, it calls a database update function to persist this change, using the exchange's ID and the new feedback value. Finally, it triggers a rerun of the Streamlit application to reflect the updated state.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing the exchange, expected to contain at least '_id' and 'feedback' keys.
    - **val** (`any`): The new feedback value to be assigned to the exchange.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls the `rerun` function from the frontend and the `update_exchange_feedback` function from the database module.
    - **Called By:** This function is called by the `render_exchange` function in `Frontend.py` on lines 117 and 122.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: str, ex: dict)`
*   **Description:** This function deletes an exchange from both the database and the application's state. It first removes the exchange from the database using its ID and then removes it from the session state's chat data. Finally, it triggers a rerun of the application to reflect the changes.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which to delete the exchange.
    - **ex** (`dict`): A dictionary representing the exchange to be deleted, containing at least an '_id' key.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls `delete_exchange_by_id` to remove data from the database, `remove` to modify the session state, and `rerun` to refresh the application.
    - **Called By:** This function is called by the `render_exchange` function in `Frontend.py`.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** This function deletes a specified chat for a given username. It first removes the chat data from the database using `db.delete_chats_by_user`. Then, it removes the chat from the session state. Finally, it updates the `active_chat` session state to either the first remaining chat or a default new chat if no chats are left, and then reruns the application to reflect these changes.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls `db.delete_chats_by_user` to remove chat data from the database, and interacts with `st.session_state` to manage chat data and the active chat. It also calls `st.rerun()` to refresh the application state.
    - **Called By:** This function is called from within the `frontend.Frontend` class, specifically at line 219 in `Frontend.py`.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str)`
*   **Description:** This function takes a markdown text string as input and renders it, specifically handling blocks marked for Mermaid diagram visualization. It splits the input text based on ` ```mermaid ` delimiters. For regular text parts, it uses `st.markdown` for rendering. For the content within ` ```mermaid ` blocks, it attempts to render them as Mermaid diagrams using `st_mermaid`. If `st_mermaid` fails, it falls back to displaying the content as a code block with the language set to 'mermaid'. The function returns early if the input text is empty.
*   **Parameters:**
    - **markdown_text** (`str`): The input markdown text which may contain Mermaid diagram blocks.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls `re.split` to divide the text, `enumerate` to iterate through the parts, `hash` to create unique keys, `st.markdown` to render regular text, `st_mermaid` to render Mermaid diagrams, and `st.code` as a fallback for Mermaid rendering. It also uses `part.strip()` to remove leading/trailing whitespace.
    - **Called By:** This function is called by `render_exchange` in Frontend.py and also within the module `frontend.Frontend` at line 333.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** This function, `render_exchange`, is responsible for displaying a chat exchange within a Streamlit frontend. It takes an exchange object (`ex`) and the current chat name (`current_chat_name`) as input. The function first displays the user's question and then renders the assistant's answer within a chat message context. It includes a toolbar with buttons for positive/negative feedback, writing feedback messages, downloading the answer as a Markdown file, and deleting the exchange. The answer content is displayed in a scrollable container, with Mermaid diagrams rendered if present.
*   **Parameters:**
    - **ex** (`dict`): A dictionary containing the chat exchange data, including 'question', 'answer', 'feedback', 'feedback_message', and '_id'.
    - **current_chat_name** (`str`): The name of the current chat session.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls various Streamlit components such as `st.chat_message`, `st.columns`, `st.button`, `st.popover`, `st.text_area`, `st.download_button`, `st.caption`, `st.container`, and `st.write`. It also calls helper functions like `handle_feedback_change`, `handle_delete_exchange`, `db.update_exchange_feedback_message`, `time.sleep`, `st.success`, `st.rerun`, and `render_text_with_mermaid`.
    - **Called By:** This function is called from the `frontend.Frontend` class, specifically from a method likely responsible for rendering the main chat interface.

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic model used to define the structure for describing a single parameter within a function or method. It captures the parameter's name, its data type, and a textual explanation of its purpose.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not have any external dependencies beyond Pydantic's BaseModel.
*   **Constructor:**
    *   *Description:* Initializes a ParameterDescription object with the name, type, and description of a function parameter. This model inherits from Pydantic's BaseModel, ensuring data validation.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The data type of the parameter.
        - **description** (`str`): A textual explanation of the parameter's purpose.
*   **Methods:** *No methods defined.*

#### Class: `ReturnDescription`
*   **Summary:** This class, ReturnDescription, is a Pydantic model designed to structure information about a function's return value. It captures the name, type, and a textual description of what the function returns.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class depends on the BaseModel from the pydantic library for its structure and validation.
*   **Constructor:**
    *   *Description:* Initializes the ReturnDescription model with the name, type, and description of a function's return value. These attributes are directly assigned from the provided arguments.
    *   *Parameters:*
        - **name** (`str`): The name of the return value, if applicable.
        - **type** (`str`): The data type of the return value.
        - **description** (`str`): A textual explanation of the return value.
*   **Methods:** *No methods defined.*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model used to describe the calling context of a function. It specifically captures information about which other functions or methods a given function calls, and which functions or methods call it.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class depends on pydantic.BaseModel for its structure and validation.
*   **Constructor:**
    *   *Description:* Initializes the UsageContext model with information about the functions called and the functions that call this one. It inherits from Pydantic's BaseModel for data validation.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions or methods called by this function.
        - **called_by** (`str`): A string describing the functions or methods that call this function.
*   **Methods:** *No methods defined.*

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a function. It details the function's overall purpose, its parameters, its return values, and its usage context within a larger system. This structure is intended for machine readability and facilitates the systematic documentation of code.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class depends on Pydantic's BaseModel for its structure and validation. It also relies on other defined types such as ParameterDescription, ReturnDescription, and UsageContext, which are assumed to be defined elsewhere.
*   **Constructor:**
    *   *Description:* Initializes a FunctionDescription object. As this is a Pydantic model, initialization is handled by Pydantic's BaseModel, which validates and assigns the provided attributes. The attributes directly correspond to the components of a function's analysis: overall description, parameter details, return value details, and usage context.
    *   *Parameters:*
        - **overall** (`str`): A string providing an overall summary of the function's purpose and behavior.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing a parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects, each detailing a return value of the function.
        - **usage_context** (`UsageContext`): A UsageContext object that describes how and where the function is called and what other functions it calls.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic model designed to represent the structured analysis of a Python function. It serves as a primary data structure within a documentation generation system, encapsulating all relevant details about a function's signature, behavior, and usage context. This model is intended for machine readability, facilitating further processing by other AI components.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class has no external dependencies beyond Pydantic's BaseModel and typing.Optional.
*   **Constructor:**
    *   *Description:* Initializes a FunctionAnalysis object. It takes the function's identifier, a detailed description object, and an optional error string as input. This constructor is used to create structured representations of function analyses, typically generated by an AI code analyst.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): A complex object containing the detailed analysis of the function, including its overall purpose, parameters, return values, and usage context.
        - **error** (`Optional[str]`): An optional field to store any error messages encountered during the analysis of the function. If no errors occurred, this will be None.
*   **Methods:** *No methods defined.*

#### Class: `ConstructorDescription`
*   **Summary:** This class, ConstructorDescription, is designed to encapsulate the details of a class's initialization method (__init__). It inherits from Pydantic's BaseModel, ensuring data validation for its fields. The class is intended to hold a textual description of the constructor and a list of its parameters, each described by a ParameterDescription object.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class has no external dependencies beyond Pydantic's BaseModel and typing.List.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription object. It takes a textual description of the constructor and a list of ParameterDescription objects, which detail each parameter of the constructor.
    *   *Parameters:*
        - **description** (`str`): A string providing a textual summary of the __init__ method's purpose and behavior.
        - **parameters** (`List[ParameterDescription]`): A list where each element is a ParameterDescription object, detailing a parameter of the __init__ method.
*   **Methods:** *No methods defined.*

#### Class: `ClassContext`
*   **Summary:** The ClassContext model is a Pydantic BaseModel used to describe a class's external dependencies and its primary points of instantiation. It serves as a structured way to document how a class interacts with other parts of a system and where it is typically created.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not appear to have any external dependencies defined within its scope.
*   **Constructor:**
    *   *Description:* Initializes the ClassContext model with details about the class's dependencies and instantiation points. It directly assigns the provided values to the corresponding attributes.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class.
        - **instantiated_by** (`str`): A string describing where the class is typically instantiated.
*   **Methods:** *No methods defined.*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It structures information about the class's overall purpose, its initialization method, a detailed breakdown of its individual methods, and its usage context including dependencies and instantiation points.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class relies on other Pydantic models (BaseModel) and typing constructs (List) for its structure and definition.
*   **Constructor:**
    *   *Description:* Initializes a ClassDescription object. It takes arguments that directly map to the attributes of the class, allowing for the structured representation of a class's analysis.
    *   *Parameters:*
        - **overall** (`str`): A string describing the overall purpose and responsibilities of the class.
        - **init_method** (`ConstructorDescription`): An object detailing the constructor's behavior, including its description and parameters.
        - **methods** (`List[FunctionAnalysis]`): A list of objects, where each object represents the analysis of a specific method within the class.
        - **usage_context** (`ClassContext`): An object detailing the class's external dependencies and where it is instantiated.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis model represents the overall structure for analyzing a Python class. It encapsulates the class's identifier, a detailed description of its components (constructor, methods, and overall purpose), and an optional error field for reporting analysis issues. This model is designed to be a comprehensive data structure for documenting and understanding Python classes.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class has no external dependencies explicitly listed in its context.
*   **Constructor:**
    *   *Description:* Initializes a ClassAnalysis object. It takes the class identifier, a ClassDescription object containing the analysis details, and an optional error string. The error defaults to None, indicating successful analysis.
    *   *Parameters:*
        - **identifier** (`str`): The name of the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, methods, and usage context.
        - **error** (`Optional[str]`): An optional string that holds an error message if the analysis failed; otherwise, it is None.
*   **Methods:** *No methods defined.*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic model used to represent detailed information about a specific call event, typically originating from a relationship analyzer. It serves to structure data for lists like 'called_by' and 'instantiated_by', providing context about the caller, the function or method being called, and the location of the call.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** This class does not appear to have any external dependencies beyond Pydantic's BaseModel.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo object with details about a call event. It takes the file path, function name, call mode, and line number as arguments, storing them as instance attributes.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call occurred.
        - **function** (`str`): The name of the function or method that made the call.
        - **mode** (`str`): The type of call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the file where the call occurred.
*   **Methods:** *No methods defined.*

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing a function. It specifically captures the functions or methods that a given function calls and the functions or methods that call it. This is useful for understanding call graphs and dependencies within a codebase.
*   **Instantiation:** `main.py`, in function `main_workflow` (Line: 202)
*   **Dependencies:** This class depends on Pydantic's BaseModel for its structure and validation, and it uses List from typing. It also references a CallInfo type which is assumed to be defined elsewhere.
*   **Constructor:**
    *   *Description:* Initializes the FunctionContextInput model with lists of calls and called_by information. This constructor is automatically generated by Pydantic based on the class attributes.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings, where each string represents a function or method called by the function being analyzed.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, where each object represents a function or method that calls the function being analyzed.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic model designed to encapsulate all the necessary information required for analyzing a Python function. It serves as a structured input for a function analysis process, ensuring all relevant data like the function's identifier, source code, import statements, and contextual information are provided in a standardized format.
*   **Instantiation:** `main.py`, in function `main_workflow` (Line: 207)
*   **Dependencies:** This class does not specify any external dependencies beyond Pydantic's BaseModel and typing modules.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput model with the necessary components for function analysis. It takes the mode, identifier, source code, a list of import statements, and a FunctionContextInput object as arguments, validating them according to Pydantic's BaseModel rules.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, which must be 'function_analysis' for this input type.
        - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
        - **source_code** (`str`): The raw source code of the function.
        - **imports** (`List[str]`): A list of import statements relevant to the source code file where the function is defined.
        - **context** (`FunctionContextInput`): An object containing contextual information about the function, such as its dependencies and call relationships.
*   **Methods:** *No methods defined.*

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to structure contextual information about a class's methods. It captures details such as the method's identifier, lists of other methods or functions it calls and is called by, its arguments, and an optional docstring. This class serves as a data container for method-specific metadata within a larger system, likely for documentation generation or code analysis.
*   **Instantiation:** `main.py`, in function `main_workflow` (Line: 227)
*   **Dependencies:** This class depends on `pydantic.BaseModel` for its structure and validation, and `typing.List` and `typing.Optional` for type hinting. It also relies on a `CallInfo` type, which is not defined in the provided source code but is used for the `called_by` attribute.
*   **Constructor:**
    *   *Description:* Initializes a MethodContextInput object, which is a Pydantic model. It takes the method's identifier, a list of calls it makes, a list of call information for methods that call it, a list of its arguments, and an optional docstring as input. These attributes are validated and stored as instance attributes.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method.
        - **calls** (`List[str]`): A list of strings, where each string represents a method or function that this method calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, where each object details a caller of this method.
        - **args** (`List[str]`): A list of strings representing the arguments accepted by the method.
        - **docstring** (`Optional[str]`): An optional string containing the docstring of the method.
*   **Methods:** *No methods defined.*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput model is a Pydantic BaseModel designed to structure the contextual information required for analyzing a Python class. It encapsulates details about the class's dependencies, where it is instantiated, and the context of its individual methods. This model serves as a data container for facilitating comprehensive class analysis within a larger system.
*   **Instantiation:** `HelperLLM.py`, in function `main_orchestrator` (Line: 347), `main.py`, in function `main_workflow` (Line: 239)
*   **Dependencies:** This class does not explicitly list any external dependencies within its definition.
*   **Constructor:**
    *   *Description:* Initializes the ClassContextInput model with lists of dependencies, instantiation information, and method contexts. This constructor sets up the data structure for holding all relevant information needed for a thorough class analysis.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies of the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects detailing where instances of the class are created.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing context for a specific method within the class.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic model designed to structure the input required for a class analysis process. It defines the necessary fields for mode, identifier, source code, imports, and a nested context object, ensuring that the input data adheres to a specific schema for analysis.
*   **Instantiation:** `HelperLLM.py`, in function `main_orchestrator` (Line: 316), `main.py`, in function `main_workflow` (Line: 245)
*   **Dependencies:** This class does not have any explicit external code dependencies listed in its context.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysisInput model with all the required fields for class analysis. It sets up the structure for the analysis mode, the identifier of the class to be analyzed, its source code, a list of relevant imports, and a context object containing additional information like dependencies and instantiation points.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the analysis mode, which must be 'class_analysis' for this input type.
        - **identifier** (`str`): The name or identifier of the class that is intended for analysis.
        - **source_code** (`str`): The raw source code of the class definition to be analyzed.
        - **imports** (`List[str]`): A list of import statements relevant to the source code, which may include unused imports.
        - **context** (`ClassContextInput`): A nested object containing contextual information for the analysis, such as dependencies and instantiation details.
*   **Methods:** *No methods defined.*

---
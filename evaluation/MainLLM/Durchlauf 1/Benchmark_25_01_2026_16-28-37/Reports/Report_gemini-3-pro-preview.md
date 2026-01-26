# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** A comprehensive tool designed to automate the process of understanding and documenting software repositories. It utilizes Large Language Models (LLMs) to analyze code structures (AST), generate documentation, and visualize dependencies, all accessible through an interactive Streamlit frontend.
- **Key Features:**
  - Automated Code Documentation using LLMs (Gemini, OpenAI, Ollama).
  - Repository Structure & AST Analysis.
  - Dependency & Call Graph Visualization.
  - Interactive Streamlit Dashboard for user interaction.
  - Jupyter Notebook Analysis & Conversion to XML.
- **Tech Stack:** Python, Streamlit, MongoDB, LangChain, GitPython, NetworkX, Pydantic.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root[root] --> root_files[.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json]
    root --> SystemPrompts
    SystemPrompts --> SystemPrompts_files[SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt]
    root --> backend
    backend --> backend_files[AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
    root --> database
    database --> database_files[db.py]
    root --> frontend
    frontend --> frontend_files[.streamlit<br/>__init__.py<br/>frontend.py<br/>gifs]
    root --> notizen
    notizen --> notizen_files[Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md]
    root --> result
    result --> result_files[ast_schema...json<br/>notebook_report...md<br/>report...md<br/>savings...png]
    root --> schemas
    schemas --> schemas_files[types.py]
    root --> statistics
    statistics --> statistics_files[savings...png]
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

*Note: You can install these using `pip install -r requirements.txt`*

### Setup Guide
1.  **Clone the Repository**: Clone this repository to your local machine.
2.  **Environment Setup**: Create a `.env` file based on `.env.example`. This will likely require API keys for services like Gemini, OpenAI, or Ollama, and database connection strings.
3.  **Database**: Ensure a MongoDB instance is running, as the project utilizes `pymongo`.
4.  **Install Dependencies**: Run `pip install -r requirements.txt`.

### Quick Startup
Run the Streamlit frontend to launch the application:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
Based on the analysis of the code and file structure, the primary use cases are:

*   **Repository Onboarding & Analysis**: Users can input a GitHub repository URL into the frontend. The system clones the repo, analyzes its structure (AST), and generates a comprehensive report, including project overview, installation guides, and code analysis.
*   **Documentation Generation**: The system uses Helper LLMs to generate docstrings and descriptions for classes and functions that lack them, effectively automated documentation.
*   **Notebook Conversion**: Jupyter Notebooks (`.ipynb`) within a repository can be processed and converted into XML/Markdown reports.
*   **Visualization**: Users can view generated Call Graphs and File Dependency Graphs to understand the architecture of the analyzed project.

**Primary Command:**
`streamlit run frontend/frontend.py`

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) of Python code. Its primary purpose is to extract structured information about imports, functions, and classes within a given source file and organize it into a `schema` dictionary. It meticulously identifies and records details such as identifiers, names, docstrings, and source code segments for each discovered element, distinguishing between top-level functions and methods nested within classes. This class serves as a foundational component for static code analysis, providing a structured representation of a Python module's contents.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** `backend.AST_Schema.path_to_module`
*   **Constructor:**
    *   *Description:* The `__init__` method initializes an `ASTVisitor` instance, setting up essential attributes like the source code, file path, and project root. It calculates the module path using an external utility function and initializes an empty `schema` dictionary to store discovered imports, functions, and classes. It also sets `_current_class` to `None` to track the current class being visited during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the entire file being visited.
        - **file_path** (`str`): The absolute path to the Python file currently being analyzed.
        - **project_root** (`str`): The root directory of the entire project, used for calculating relative module paths.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* This method is part of the `ast.NodeVisitor` pattern, specifically designed to handle `ast.Import` nodes. It iterates through the imported modules (aliases) within the node and appends their names to the `imports` list within the `self.schema` dictionary. This captures top-level import statements like `import module_name`. After processing the current node, it calls `self.generic_visit(node)` to ensure that the visitor continues traversing the children of the import node, if any.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an `import` statement.
        *   *Returns:* []
        *   **Usage:** Calls: `This method does not explicitly call other methods, classes, or functions within its source code, besides `self.generic_visit(node)` which is part of the AST visitor pattern.`; Called by: `This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when it encounters an `ast.Import` node.`
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* Similar to `visit_Import`, this method handles `ast.ImportFrom` nodes, which represent `from ... import ...` statements. It iterates through the aliases (names) imported from a specific module and constructs a fully qualified import string (e.g., `module.name`). This constructed string is then appended to the `imports` list in `self.schema`. Finally, `self.generic_visit(node)` is called to continue the AST traversal, ensuring all child nodes are also visited.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a `from ... import ...` statement.
        *   *Returns:* []
        *   **Usage:** Calls: `This method does not explicitly call other methods, classes, or functions within its source code, besides `self.generic_visit(node)` which is part of the AST visitor pattern.`; Called by: `This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when it encounters an `ast.ImportFrom` node.`
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions. It constructs a unique `class_identifier` by combining the module path and the class name, and gathers various pieces of information about the class, including its name, docstring, and source code segment. This information is then stored in a `class_info` dictionary, which is appended to the `classes` list within `self.schema`. The `_current_class` attribute is temporarily set to the `class_info` to allow nested methods to associate themselves with this class, and it is reset to `None` after visiting the class's children.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `ast.get_docstring` to extract the class's docstring and `ast.get_source_segment` to get its source code. It also calls `self.generic_visit(node)` for AST traversal.`; Called by: `This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when it encounters an `ast.ClassDef` node.`
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: ast.FunctionDef)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, representing function definitions. It distinguishes between methods defined within a class and standalone functions. If `_current_class` is set, it means the function is a method of the current class, and its details (identifier, name, arguments, docstring, lines) are appended to the `method_context` of that class within `self.schema`. Otherwise, it's a standalone function, and its details are appended to the `functions` list in `self.schema`. The method then calls `self.generic_visit(node)` to continue traversal.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `ast.get_docstring` to extract the function's docstring and `ast.get_source_segment` to get its source code. It also calls `self.generic_visit(node)` for AST traversal.`; Called by: `This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when it encounters an `ast.FunctionDef` node.`
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef)`
        *   *Description:* This method is designed to handle `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation simply delegates to the `visit_FunctionDef` method, treating asynchronous functions identically to regular functions for the purpose of schema generation. This indicates that the visitor aims to capture the structural information of async functions without special handling for their asynchronous nature, ensuring consistent processing.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* []
        *   **Usage:** Calls: `This method explicitly calls `self.visit_FunctionDef` to process the asynchronous function node.`; Called by: `This method is implicitly called by the `ast.NodeVisitor`'s traversal mechanism when it encounters an `ast.AsyncFunctionDef` node.`

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process and analyze the Abstract Syntax Trees (ASTs) of Python code within a repository. Its primary function is to construct a detailed schema of a codebase, identifying functions, classes, and their interdependencies. It can also merge external relationship data, such as call graphs, into this schema to provide a holistic view of the code's structure and interactions.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** `backend.AST_Schema.ASTVisitor`
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond `self` and performs no internal state setup or attribute initialization.
    *   *Parameters:* []
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self: ASTAnalyzer, full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing call information, into a pre-existing full schema of AST nodes. It iterates through files, functions, and classes within the schema to enrich their context with call and instantiation data. For functions, it assigns `calls` and `called_by` lists. For classes, it assigns `instantiated_by` and then processes each method within the class to determine its `calls` and `called_by` relationships, also identifying external class dependencies.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
            - **full_schema** (`dict`): A dictionary representing the complete AST schema, including files, functions, and classes.
            - **raw_relationships** (`dict`): A dictionary containing raw incoming and outgoing call relationships.
        *   *Returns:*
            - **full_schema** (`dict`): The modified `full_schema` dictionary, now enriched with relationship data.
        *   **Usage:** Calls: `This method does not explicitly call other methods, classes, or functions within its source code.`; Called by: `backend.main.main_workflow`
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self: ASTAnalyzer, files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to build a comprehensive AST schema. It first determines the project root from the file paths. Then, it iterates through each Python file, parses its content into an AST, and uses an `ASTVisitor` to extract structured AST node information. The extracted data, including imports, functions, and classes, is then added to a `full_schema` dictionary, mapping file paths to their respective AST nodes.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
            - **files** (`list`): A list of file objects, each containing a `path` and `content` attribute.
            - **repo** (`GitRepository`): An object representing the Git repository, though it's not directly used in the provided method body beyond its type hint.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary containing the structured AST schema for all processed Python files in the repository.
        *   **Usage:** Calls: `This method calls `os.path.commonpath`, `os.path.isfile`, `os.path.dirname`, `ast.parse`, and instantiates `ASTVisitor`.`; Called by: `backend.main.main_workflow`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into a Python module path string. It first attempts to determine the relative path of the `filepath` to the `project_root`, falling back to the base filename if a `ValueError` occurs. It then removes the '.py' extension if present and replaces file system path separators with dots. Finally, it specifically handles `__init__.py` files by removing the '.__init__' suffix from the resulting module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The Python module path string derived from the input filepath.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `backend.AST_Schema.ASTVisitor.__init__`

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is an AST NodeVisitor designed to analyze Python source code files and build a graph of their import dependencies. It traverses the Abstract Syntax Tree of a given file, specifically looking for 'import' and 'from ... import' statements. It handles both absolute and relative imports, resolving the latter by inspecting the file system. The class maintains a dictionary, 'import_dependencies', to store the mapping from the analyzed file to the set of modules it imports.
*   **Instantiation:** `backend.File_Dependency.build_file_dependency_graph`
*   **Dependencies:** `backend.File_Dependency.get_all_temp_files`, `backend.File_Dependency.init_exports_symbol`, `backend.File_Dependency.module_file_exists`
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph instance by storing the 'filename' of the file being analyzed and the 'repo_root' directory. These attributes are crucial for resolving file paths and dependencies.
    *   *Parameters:*
        - **filename** (`str`): The path to the file currently being analyzed.
        - **repo_root** (`Any`): The root directory of the repository.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(node: ImportFrom)`
        *   *Description:* This method resolves relative import statements (e.g., 'from .. import name'). It determines the actual module or symbol names that are being imported by navigating the file system relative to the current file and the repository root. It checks for both module files ('.py') and symbols exported via '__init__.py' files. If no modules or symbols can be resolved, it raises an ImportError.
        *   *Parameters:*
            - **node** (`ImportFrom`): An AST ImportFrom node representing the import statement to resolve.
        *   *Returns:*
            - **null** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:** Calls: `This method calls `get_all_temp_files`, `init_exports_symbol`, and `module_file_exists`.`; Called by: `This method is not explicitly called by other functions or methods in the provided context.`
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* This method processes 'Import' and 'ImportFrom' AST nodes to record import dependencies. It adds the imported module or symbol name to the 'import_dependencies' dictionary, mapping the current 'filename' to a set of its dependencies. If 'base_name' is provided, it uses that; otherwise, it uses the alias name from the node.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): An AST node representing either an Import or ImportFrom statement.
            - **base_name** (`str | None`): An optional base name for the module, used primarily for 'from ... import ...' statements where the module part is explicitly resolved.
        *   *Returns:* []
        *   **Usage:** Calls: `This method does not explicitly call any other functions or methods.`; Called by: `This method is not explicitly called by other functions or methods in the provided context.`
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ImportFrom)`
        *   *Description:* This method specifically handles 'ImportFrom' AST nodes. It first attempts to extract the module name directly from the node. If it's a direct import (e.g., 'from a.b.c import d'), it extracts the last part ('c') and passes it to 'visit_Import'. If it's a relative import (no direct module name), it calls '_resolve_module_name' to determine the actual modules/symbols and then processes each resolved name via 'visit_Import'. It includes error handling for failed relative import resolutions.
        *   *Parameters:*
            - **node** (`ImportFrom`): An AST ImportFrom node.
        *   *Returns:* []
        *   **Usage:** Calls: `This method does not explicitly call any other functions or methods.`; Called by: `This method is not explicitly called by other functions or methods in the provided context.`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Abstract Syntax Tree (AST). It initializes an empty NetworkX directed graph. It then utilizes a FileDependencyGraph visitor to traverse the provided AST, collecting import relationships. Finally, it populates the graph with nodes for callers and callees, adding directed edges to represent the import dependencies, and returns the completed graph.
*   **Parameters:**
    - **filename** (`str`): The name of the file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed for dependencies.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies.
*   **Usage:** Calls: `This function calls backend.File_Dependency.FileDependencyGraph.`; Called by: `backend.File_Dependency.build_repository_graph`

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a directed graph representing the dependencies within a given Git repository. It iterates through all Python files in the repository, parsing each file's content into an Abstract Syntax Tree (AST). For each Python file, it builds a file-specific dependency graph and then merges its nodes and edges into a global directed graph. The final global graph captures the relationships between various components across the entire repository.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to extract file dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependencies found across all Python files in the repository.
*   **Usage:** Calls: `This function calls backend.File_Dependency.build_file_dependency_graph.`; Called by: `backend.File_Dependency`

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a string representing a directory path as input. The function first resolves the provided directory path to an absolute path using `pathlib.Path`. It then recursively searches this root path for all files ending with the '.py' extension. Finally, it returns a list of these Python file paths, with each path being relative to the initial root directory provided.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory from which to start searching for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each object represents a Python file found within the specified directory, relative to the input `directory`.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `backend.File_Dependency.FileDependencyGraph._resolve_module_name`

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a robust and centralized interface for interacting with various Large Language Models (LLMs) to generate structured documentation for Python functions and classes. It handles the complexities of LLM API integration, including dynamic model selection, API key management, loading of specific system prompts, efficient batch processing, and adherence to API rate limits. By enforcing Pydantic schemas for both input and output, it ensures the reliability and consistency of the generated documentation, making it an essential component for automated code analysis and documentation systems.
*   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper instance by setting up the API key, loading system prompts from specified file paths for function and class analysis, configuring batch settings based on the model name, and initializing various LLM clients (Google Gemini, OpenAI, custom, or Ollama) with structured output capabilities for FunctionAnalysis and ClassAnalysis schemas. It also sets up a raw LLM client for unstructured interactions.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt template specifically designed for guiding the LLM in function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt template specifically designed for guiding the LLM in class analysis.
        - **model_name** (`str`): The name of the LLM model to be used for generating documentation, defaulting to 'gemini-2.0-flash-lite'.
        - **base_url** (`str | None`): An optional base URL for custom LLM endpoints, such as Ollama or other OpenAI-compatible APIs.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(model_name: str)`
        *   *Description:* This private method dynamically configures the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It employs a series of conditional checks to assign specific batch sizes tailored for various LLM models, including different Gemini versions, Llama, GPT, and custom or aliased models. The method aims to optimize API interaction by grouping requests efficiently, and it logs a warning if an unknown model is encountered, defaulting to a conservative batch size.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which the batch processing settings need to be configured.
        *   *Returns:* []
        *   **Usage:** Calls: `This method does not explicitly call other methods or functions within its source code, besides standard Python operations like string comparisons and assignments.`; Called by: `This method is called by the `__init__` method of the `LLMHelper` class during instance initialization.`
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* This method is designed to generate and validate documentation for a batch of Python functions using the configured LLM. It takes a list of `FunctionAnalysisInput` objects, converts each into a JSON payload, and constructs a list of conversations, each paired with the function-specific system prompt. The method then processes these conversations in batches, making asynchronous calls to the `function_llm` and extending the results with validated `FunctionAnalysis` objects. It includes robust error handling for individual batch calls and incorporates a waiting period between batches to adhere to API rate limits.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary details of a function for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, representing the generated and validated documentation for the input functions. If an error occurs during processing, `None` is returned for that specific function's entry.
        *   **Usage:** Calls: `This method calls `json.dumps` to serialize input models, `model_dump` on `function_input` objects, `SystemMessage` and `HumanMessage` to construct conversations, `logging.info` and `logging.error` for logging, `self.function_llm.batch` to make asynchronous LLM calls, and `time.sleep` for rate limiting.`; Called by: `The input context does not specify any explicit callers for this method.`
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(class_inputs: List[ClassAnalysisInput])`
        *   *Description:* This method is responsible for generating and validating documentation for a batch of Python classes using the configured LLM. It accepts a list of `ClassAnalysisInput` objects, transforms each into a JSON payload, and prepares a list of conversations, each paired with the class-specific system prompt. The method then iteratively sends these conversations to the `class_llm` in batches, handling potential exceptions during API calls and ensuring that the order of results is maintained by appending `None` for failed items. It also incorporates a delay between batches to comply with API rate limits and optimize resource usage.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary details of a class for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, representing the generated and validated documentation for the input classes. If an error occurs during processing, `None` is returned for that specific class's entry.
        *   **Usage:** Calls: `This method calls `json.dumps` to serialize input models, `model_dump` on `class_input` objects, `SystemMessage` and `HumanMessage` to construct conversations, `logging.info` and `logging.error` for logging, `self.class_llm.batch` to make asynchronous LLM calls, and `time.sleep` for rate limiting.`; Called by: `The input context does not specify any explicit callers for this method.`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a testing orchestrator for the LLMHelper class. It defines several pre-computed `FunctionAnalysisInput` and `FunctionAnalysis` objects, along with a `ClassAnalysisInput` object, to simulate various analysis scenarios. It then instantiates an `LLMHelper` and calls its `generate_for_functions` method with the prepared input. The function processes the results and prints the final aggregated documentation, demonstrating the expected workflow for generating documentation.
*   **Parameters:** []
*   **Returns:** []
*   **Usage:** Calls: `This function calls backend.HelperLLM.LLMHelper, schemas.types.ClassAnalysisInput, and schemas.types.ClassContextInput.`; Called by: `This function calls no other functions.`

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a central interface for interacting with various Large Language Models (LLMs). It handles the initialization of different LLM clients based on the specified model name, loads a system prompt from a file, and provides methods for both synchronous and asynchronous (streaming) communication with the chosen LLM. This class abstracts the underlying LLM provider, allowing for flexible integration with Gemini, OpenAI-compatible APIs, or Ollama.
*   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by setting up the system prompt and configuring the appropriate LLM client. It validates the API key, reads the system prompt from the provided file path, and dynamically instantiates either a ChatGoogleGenerativeAI, ChatOpenAI, or ChatOllama client based on the `model_name` and `base_url` parameters. It also includes error handling for missing API keys or prompt files.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service (e.g., Gemini or OpenAI).
        - **prompt_file_path** (`str`): The file path to a text file containing the system prompt that will be used for all LLM interactions.
        - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This determines which LLM client (Gemini, OpenAI, or Ollama) will be initialized.
        - **base_url** (`str`): An optional base URL for custom LLM API endpoints, primarily used for Ollama or other self-hosted models. Defaults to None.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(user_input: str)`
        *   *Description:* This method performs a synchronous call to the initialized LLM with a given user input. It constructs a list of messages including the system prompt and the user's query, then invokes the LLM to get a response. The method handles potential exceptions during the LLM call, logging any errors and returning None in case of failure. If successful, it returns the content of the LLM's response.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:*
            - **response_content** (`str`): The textual content of the LLM's response.
            - **None** (`None`): Returns None if an error occurs during the LLM call.
        *   **Usage:** Calls: `This method calls SystemMessage, HumanMessage to construct the message payload, self.llm.invoke to send the request to the LLM, and logging.info and logging.error for operational logging.`; Called by: `This method is not explicitly called by other methods in the provided context.`
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(user_input: str)`
        *   *Description:* This method initiates a streaming call to the configured LLM, yielding chunks of the response content as they become available. It prepares the messages with the system prompt and user input, then iterates through the stream provided by the LLM client. Each chunk's content is yielded, allowing for real-time processing of the LLM's output. Error handling is included to catch exceptions during the streaming process and yield an error message.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message for which a streaming response is desired.
        *   *Returns:*
            - **chunk_content** (`str`): A generator that yields individual string chunks of the LLM's response content.
            - **error_message** (`str`): Yields an error message string if an exception occurs during the streaming call.
        *   **Usage:** Calls: `This method calls SystemMessage, HumanMessage to construct the message payload, self.llm.stream to initiate the streaming request, and logging.info and logging.error for operational logging.`; Called by: `This method is not explicitly called by other methods in the provided context.`

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to automatically gather and structure essential project information from common project files such as README.md, pyproject.toml, and requirements.txt. It provides a consolidated view of a project's overview, installation instructions, and dependencies. The class prioritizes structured data from `pyproject.toml` over less structured `README` content and offers fallback mechanisms to derive information like the project title from the repository URL, ultimately returning a comprehensive dictionary of project details.
*   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* The constructor initializes the class by setting a constant `INFO_NICHT_GEFUNDEN` to indicate missing information. It also sets up a nested dictionary `self.info` with predefined keys for project overview and installation details, populating all values with the `INFO_NICHT_GEFUNDEN` placeholder.
    *   *Parameters:* []
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(content: str)`
        *   *Description:* This private helper method processes a given string content to ensure it is free from null bytes. Null bytes (`\x00`) can often appear due to encoding errors, such as reading a UTF-16 encoded file as UTF-8. The method checks if the content is not empty and then replaces all occurrences of the null byte with an empty string, returning the cleaned result.
        *   *Parameters:*
            - **content** (`str`): The string content to be cleaned.
        *   *Returns:*
            - **""** (`str`): The cleaned string content with all null bytes removed.
        *   **Usage:** Calls: `This method does not explicitly call other functions or methods but uses string manipulation methods.`; Called by: `This method is called by _parse_readme, _parse_toml, and _parse_requirements.`
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(patterns: List[str], dateien: List[Any])`
        *   *Description:* This private method searches through a provided list of file-like objects to find one that matches any of the specified filename patterns. It performs a case-insensitive comparison by converting both the file's path and the patterns to lowercase. The method iterates through each file and each pattern, returning the first file object that satisfies any of the patterns, or `None` if no match is found after checking all possibilities.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of filename patterns (e.g., 'readme.md') to search for.
            - **dateien** (`List[Any]`): A list of file-like objects, where each object is expected to have a 'path' attribute.
        *   *Returns:*
            - **""** (`Optional[Any]`): The first file object found that matches one of the patterns, or None if no match is present.
        *   **Usage:** Calls: `This method does not explicitly call other functions or methods but uses string manipulation methods.`; Called by: `This method is called by extrahiere_info.`
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(inhalt: str, keywords: List[str])`
        *   *Description:* This private method extracts text content located directly under a Markdown level 2 heading (##) within a given string. It takes a list of keywords and constructs a regular expression pattern to match any heading containing these keywords, ignoring case. The method then captures all content following that heading until the next level 2 heading or the end of the document, returning the stripped content or `None` if no matching section is found.
        *   *Parameters:*
            - **inhalt** (`str`): The Markdown content string from which to extract a section.
            - **keywords** (`List[str]`): A list of keywords to match against Markdown level 2 headings.
        *   *Returns:*
            - **""** (`Optional[str]`): The extracted section content as a string, or None if no matching section is found.
        *   **Usage:** Calls: `This method calls re.escape, re.compile, and re.search.`; Called by: `This method is called by _parse_readme.`
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(inhalt: str)`
        *   *Description:* This private method parses the content of a README file to extract various project information. It first cleans the content using `_clean_content`. It then uses regular expressions to find the project title and a fallback description. Subsequently, it utilizes `_extrahiere_sektion_aus_markdown` to locate and extract specific sections like key features, tech stack, current status, installation instructions, and quick start guides, updating the `self.info` dictionary with the gathered details.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the README file as a string.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls _clean_content, re.search, and _extrahiere_sektion_aus_markdown.`; Called by: `This method is called by extrahiere_info.`
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(inhalt: str)`
        *   *Description:* This private method parses the content of a `pyproject.toml` file to extract project metadata. It begins by cleaning the input content using `_clean_content`. It then attempts to load the TOML content using `tomllib.loads`. If successful, it extracts the project name, description, and dependencies from the `[project]` section of the TOML data and updates the `self.info` dictionary. The method includes checks for `tomllib` availability and handles `TOMLDecodeError` during parsing.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the pyproject.toml file as a string.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls _clean_content, tomllib.loads, and data.get.`; Called by: `This method is called by extrahiere_info.`
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(inhalt: str)`
        *   *Description:* This private method parses the content of a `requirements.txt` file to extract project dependencies. It first cleans the input content using `_clean_content`. The method then proceeds to extract dependencies only if they have not already been populated from a `pyproject.toml` file, ensuring prioritization. It processes each line, filtering out comments and empty lines, and stores the valid dependency strings in the `self.info` dictionary.
        *   *Parameters:*
            - **inhalt** (`str`): The content of the requirements.txt file as a string.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls _clean_content.`; Called by: `This method is called by extrahiere_info.`
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(dateien: List[Any], repo_url: str)`
        *   *Description:* This public method orchestrates the entire information extraction process from various project files. It first identifies relevant files like README, pyproject.toml, and requirements.txt using `_finde_datei`. It then parses these files in a prioritized order (TOML, then requirements, then README) to populate the `self.info` dictionary. Finally, it formats the extracted dependencies and derives a project title from the repository URL if no title was found elsewhere, returning the complete project information dictionary.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have 'path' and 'content' attributes.
            - **repo_url** (`str`): The URL of the repository, used as a fallback to derive the project title.
        *   *Returns:*
            - **""** (`Dict[str, Any]`): A dictionary containing all extracted project information.
        *   **Usage:** Calls: `This method calls _finde_datei, _parse_toml, _parse_requirements, _parse_readme, os.path.basename, str.removesuffix, isinstance, and str.join.`; Called by: `This method is not explicitly called by other methods in the provided context, suggesting it is a primary entry point for external usage.`

### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an Abstract Syntax Tree (AST) visitor designed to construct a directed call graph for a given Python source file. It traverses the AST, identifying function definitions, class definitions, import statements, and function calls. The class maintains context about the current file, class, and function to accurately resolve full names for functions and methods, ultimately mapping callers to callees.
*   **Instantiation:** `backend.callgraph.build_filtered_callgraph`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph instance by setting up various internal state variables. It stores the filename being analyzed, initializes placeholders for the current function and class context, and sets up dictionaries and sets to store local definitions, the NetworkX directed graph, import mappings, a set of all functions found, and a dictionary to hold call edges.
    *   *Parameters:*
        - **filename** (`str`): The path or identifier of the source file being analyzed.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(node: ast.AST)`
        *   *Description:* This private helper method recursively traverses an AST node to extract its components, typically used for call expressions or attribute access. It aims to break down a complex expression like `obj.method()` or `pkg.mod.func()` into a list of its name parts, such as `['obj', 'method']` or `['pkg', 'mod', 'func']`. The recursion continues until a simple name or attribute is found, building the list of components in reverse order.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a call, name, or attribute expression.
        *   *Returns:*
            - **parts** (`list[str]`): A list of string components representing the dotted name of the call or attribute.
        *   **Usage:** Calls: `This method recursively calls itself to process nested AST nodes.`; Called by: `This method is called by `visit_Call` to extract the components of a called function or method.`
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(callee_nodes: list[list[str]])`
        *   *Description:* This private method takes a list of potential callee name components and resolves them into fully qualified names. It first checks against locally defined names within the current scope, then consults the import mapping to resolve imported modules or functions. If neither applies, it constructs a full name based on the current filename and class context. This ensures that each callee is identified with a unique, unambiguous name within the project.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains string components of a potential callee's name.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of fully qualified string names for the resolved callees.
        *   **Usage:** Calls: `This method accesses `self.local_defs`, `self.import_mapping`, and `self.current_class` to resolve names.`; Called by: `This method is called by `visit_Call` to determine the full names of called functions or methods.`
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(basename: str, class_name: str | None)`
        *   *Description:* This private helper method constructs a fully qualified name for a given base name, optionally including a class name. It prepends the `self.filename` to the base name, and if a `class_name` is provided, it also includes the class name in the format `filename::ClassName::BaseName`. This ensures consistent naming conventions for functions and methods within the call graph.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method (e.g., 'my_function').
            - **class_name** (`str | None`): The name of the class if the function is a method, otherwise None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name (e.g., 'file.py::ClassName::method_name').
        *   **Usage:** Calls: `This method does not make any explicit calls to other methods or functions.`; Called by: `This method is called by `visit_FunctionDef` to create the full name for a defined function or method.`
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self: CallGraph)`
        *   *Description:* This private helper method determines the identifier of the current caller context. If `self.current_function` is set, it returns that value, indicating a function or method is currently being processed. Otherwise, it defaults to a generic identifier representing the file's global scope, using `self.filename` if available, or `<global-scope>` as a fallback.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
        *   *Returns:*
            - **caller_identifier** (`str`): A string representing the current caller's full name or scope.
        *   **Usage:** Calls: `This method does not make any explicit calls to other methods or functions.`; Called by: `This method is called by `visit_Call` to identify the source of a function call.`
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* This method is an AST visitor for `ast.Import` nodes. It processes import statements like `import module as alias` or `import module`. For each imported module, it updates the `self.import_mapping` dictionary, associating the alias (or original name if no alias) with the module's actual name. After processing the import, it calls `self.generic_visit` to continue traversing the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `self.generic_visit` to continue AST traversal.`; Called by: `This method is implicitly called by the AST visitor mechanism when an `ast.Import` node is encountered.`
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* This method is an AST visitor for `ast.ImportFrom` nodes. It processes import statements like `from package import name as alias` or `from package import name`. It extracts the module name and for each imported name, it updates the `self.import_mapping` dictionary. It maps the alias (or original name) to the module name from which it was imported, or directly to the name if the module is not specified. After processing, it calls `self.generic_visit` to continue AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing an 'from ... import ...' statement.
        *   *Returns:* []
        *   **Usage:** Calls: `This method does not make any explicit calls to other methods or functions.`; Called by: `This method is implicitly called by the AST visitor mechanism when an `ast.ImportFrom` node is encountered.`
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* This method is an AST visitor for `ast.ClassDef` nodes. It manages the `self.current_class` context during AST traversal. Before visiting the class's body, it saves the previous `current_class` and sets `self.current_class` to the name of the newly encountered class. After traversing the class's children using `self.generic_visit`, it restores the `self.current_class` to its previous value, ensuring correct scope management.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `self.generic_visit` to continue AST traversal within the class definition.`; Called by: `This method is implicitly called by the AST visitor mechanism when an `ast.ClassDef` node is encountered.`
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: ast.FunctionDef)`
        *   *Description:* This method is an AST visitor for `ast.FunctionDef` nodes, handling both regular and async function definitions. It records the full name of the function, considering its class context if applicable, and updates `self.local_defs` to map the function's simple name and potentially class-qualified name to its full name. It sets `self.current_function` to the new full name, adds the function as a node to the `self.graph`, and then traverses its body. Finally, it adds the function to `self.function_set` and restores the previous `self.current_function` context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `self._make_full_name` to construct the function's full name, `self.graph.add_node` to add it to the graph, and `self.generic_visit` to traverse its body.`; Called by: `This method is implicitly called by the AST visitor mechanism when an `ast.FunctionDef` node is encountered, and explicitly by `visit_AsyncFunctionDef`.`
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef)`
        *   *Description:* This method is an AST visitor for `ast.AsyncFunctionDef` nodes. It acts as a wrapper, simply delegating the processing of asynchronous function definitions to the `visit_FunctionDef` method. This allows both synchronous and asynchronous functions to be handled by the same core logic for call graph construction, ensuring consistency in how function nodes are added and contextual information is managed.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `self.visit_FunctionDef` to process the asynchronous function definition.`; Called by: `This method is implicitly called by the AST visitor mechanism when an `ast.AsyncFunctionDef` node is encountered.`
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(node: ast.Call)`
        *   *Description:* This method is an AST visitor for `ast.Call` nodes, which represent function or method calls. It first identifies the `caller` using `_current_caller()`, then extracts the components of the `callee` using `_recursive_call()`. These components are then resolved into fully qualified names using `_resolve_all_callee_names()`. Finally, it records the call relationship by adding the resolved callees to the `self.edges` dictionary under the `caller`'s entry. After processing the call, it continues AST traversal with `self.generic_visit`.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `self._current_caller`, `self._recursive_call`, `self._resolve_all_callee_names`, and `self.generic_visit`.`; Called by: `This method is implicitly called by the AST visitor mechanism when an `ast.Call` node is encountered.`
    *   **`visit_If`**
        *   *Signature:* `def visit_If(node: ast.If)`
        *   *Description:* This method is an AST visitor for `ast.If` nodes. It includes special handling for the common `if __name__ == "__main__"` block. If such a block is detected, it temporarily sets `self.current_function` to `"<main_block>"` before traversing the `if` block's contents. This allows calls within the main execution block to be attributed to a distinct 'main' scope. For all other `if` statements, it simply continues the generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing an 'if' statement.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `self.generic_visit` to continue AST traversal.`; Called by: `This method is implicitly called by the AST visitor mechanism when an `ast.If` node is encountered.`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and a file path as input. It creates a copy of the input graph and relabels its nodes with safe, sequential identifiers (e.g., "n0", "n1"). The original node names are preserved by adding them as a 'label' attribute to the relabeled nodes. Finally, the function writes this modified graph to a DOT file at the specified output path, making it suitable for visualization tools that might have issues with complex node names.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The directed graph to be processed and written to a DOT file.
    - **out_path** (`str`): The file path where the DOT graph will be saved.
*   **Returns:** []
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** This function constructs a filtered call graph for a given Git repository. It first identifies all user-defined functions across all Python files within the repository by parsing their Abstract Syntax Trees (ASTs). Subsequently, it builds a directed graph where nodes represent these identified 'own' functions and edges represent call relationships exclusively between these self-written functions. The final output is a NetworkX directed graph representing the internal call structure.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which to extract and analyze Python files.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions defined within the repository's Python files.
*   **Usage:** Calls: `This function calls backend.callgraph.CallGraph.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content: str)`
*   **Description:** The `wrap_cdata` function takes a string `content` as input and encapsulates it within XML CDATA tags. It constructs a new string that begins with "<![CDATA[\n", inserts the provided content, and concludes with "\n]]>". This process ensures that the content is treated as character data by an XML parser, preventing interpretation of any special characters within it.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped inside CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A new string containing the original content enclosed within CDATA tags, with newlines for formatting.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs: list, image_list: list)`
*   **Description:** The `extract_output_content` function processes a collection of output objects, typically originating from notebook execution, to consolidate their content into a list of strings. It intelligently handles different output types: `display_data` and `execute_result` are inspected for image data (PNG or JPEG), which is Base64 decoded and stored in a provided `image_list`, with an XML placeholder returned. If no image is present, `text/plain` content is extracted. `stream` outputs have their raw text appended, and `error` outputs are formatted as error messages. The function returns a list containing these extracted text snippets and image placeholders.
*   **Parameters:**
    - **outputs** (`list`): An iterable of output objects, each potentially containing text, image data, or error information, typically from a notebook execution context.
    - **image_list** (`list`): A mutable list that will be populated with dictionaries, where each dictionary represents an extracted image with its MIME type and Base64 encoded data.
*   **Returns:**
    - **extracted_xml_snippets** (`list[str]`): A list of strings, where each string is either extracted plain text, an XML placeholder referencing an image in `image_list`, or a formatted error message.
*   **Usage:** Calls: `This function calls backend.converter.process_image.`; Called by: `This function is called by no other functions.`

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type: str)`
*   **Description:** This function processes an image based on its MIME type. It attempts to retrieve the base64 encoded image data from an external 'data' object using the provided MIME type. If found, it cleans the base64 string by removing newline characters and then stores the image data along with its MIME type into an external 'image_list'. A formatted placeholder string is returned upon successful processing. If the MIME type is not found in 'data', the function returns None. Any exceptions during the image decoding process result in an error message string being returned.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed, used as a key to locate its base64 encoded data.
*   **Returns:**
    - **result** (`str | None`): A formatted string representing an image placeholder if processing is successful, an error message string if an exception occurs, or None if the MIME type is not found in the 'data' object.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content: str)`
*   **Description:** This function takes the raw content of a Jupyter notebook file as a string and converts it into an XML representation. It parses the notebook, iterates through its cells, and processes markdown and code cells separately. For code cells, it also extracts and processes their outputs, potentially identifying and collecting embedded images. The function returns the generated XML string and a list of any extracted images.
*   **Parameters:**
    - **file_content** (`str`): The content of a Jupyter notebook file as a string, expected to be in JSON format.
*   **Returns:**
    - **xml_output** (`str`): A string containing the XML representation of the notebook content. If the input file content cannot be parsed as a notebook, an error message string is returned.
    - **extracted_images** (`list`): A list of extracted image data (e.g., base64 encoded strings) found within the notebook's code cell outputs. This list is empty if no images are found or if an error occurs during parsing.
*   **Usage:** Calls: `This function calls backend.converter.extract_output_content and backend.converter.wrap_cdata.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files: List[Any])`
*   **Description:** This function processes a given list of repository files to identify and convert Jupyter notebooks. It filters the input to select only files with the '.ipynb' extension. For each identified notebook, it invokes an external utility to transform the notebook's content into XML and extract any associated images. The function then aggregates these conversion results, storing the XML output and images for each notebook, keyed by its original file path. Finally, it returns a dictionary containing all processed notebook data.
*   **Parameters:**
    - **repo_files** (`List[Any]`): An iterable collection of file-like objects. Each object is expected to have a 'path' attribute (string representing the file path) and a 'content' attribute (string representing the file's content).
*   **Returns:**
    - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are notebook file paths (string) and values are dictionaries. Each inner dictionary contains 'xml' (string, the converted XML content) and 'images' (list of any, representing extracted image data or paths).
*   **Usage:** Calls: `This function calls backend.converter.convert_notebook_to_xml.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, providing a structured and lazy-loaded interface to its metadata and content. It encapsulates the file's path and its associated Git tree, deferring the loading of the Git blob, file content, and size until they are explicitly accessed. This design optimizes performance by only fetching data when necessary. The class offers properties to retrieve the Git blob, the decoded file content, and its size, along with utility methods for basic content analysis and serialization into a dictionary format.
*   **Instantiation:** `backend.getRepo.GitRepository.get_all_files`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* The __init__ method initializes a RepoFile object by storing the file path and the Git Tree object from which the file originates. It also sets up internal attributes for the Git blob, file content, and size to None, enabling lazy loading for these properties.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree-object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob()`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if the internal _blob attribute is already loaded; if not, it attempts to retrieve the blob from the stored Git tree using the file's path. If the file cannot be found within the commit tree, a FileNotFoundError is raised, ensuring robust error handling for missing files.
        *   *Parameters:* []
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:** Calls: `This method implicitly calls self._tree[self.path] to access the Git tree object and retrieve the blob.`; Called by: `This method is called by the 'content' and 'size' properties to access the file's Git blob.`
    *   **`content`**
        *   *Signature:* `def content()`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It first ensures that the 'blob' property is loaded to access the Git blob object. Then, it reads the data stream from the blob, decodes it using UTF-8 encoding while ignoring any decoding errors, and stores the result. The decoded string content is then returned for further use.
        *   *Parameters:* []
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:** Calls: `This method calls the 'self.blob' property to get the Git blob and then uses 'data_stream.read().decode()' to get the content.`; Called by: `This method is called by 'analyze_word_count' and 'to_dict' (conditionally) to access the file's content.`
    *   **`size`**
        *   *Signature:* `def size()`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the internal _size attribute is already loaded; if not, it accesses the 'blob' property to ensure the Git blob object is available. Once the blob is loaded, it retrieves its 'size' attribute, which represents the file's size. The calculated file size is then returned.
        *   *Parameters:* []
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:** Calls: `This method calls the 'self.blob' property to get the Git blob and then accesses its 'size' attribute.`; Called by: `This method is called by 'to_dict' to include the file size in the dictionary representation.`
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count()`
        *   *Description:* This method serves as an example analysis function, demonstrating how to process the file's content. It calculates the total number of words present in the file's content. This is achieved by first accessing the 'content' property to retrieve the file's text, then splitting the content string by whitespace to create a list of words, and finally returning the count of words in that list.
        *   *Parameters:* []
        *   *Returns:*
            - **word_count** (`int`): The total number of words found in the file content.
        *   **Usage:** Calls: `This method calls the 'self.content' property to retrieve the file's content.`; Called by: `This method is not explicitly called by other methods within the class, suggesting it's an external utility or example.`
    *   **`__repr__`**
        *   *Signature:* `def __repr__()`
        *   *Description:* This special method provides a developer-friendly string representation of the RepoFile object. It constructs a concise string that includes the class name and the 'path' attribute of the file. This representation is particularly useful for debugging and logging, as it allows for easy identification of the object when it is printed or inspected.
        *   *Parameters:* []
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, showing its path.
        *   **Usage:** Calls: `This method accesses the 'self.path' attribute.`; Called by: `This method is implicitly called by Python's 'repr()' function or when the object is printed in an interactive console.`
    *   **`to_dict`**
        *   *Signature:* `def to_dict(include_content: bool)`
        *   *Description:* This method converts the RepoFile object into a dictionary representation, providing a structured way to export its data. It includes essential metadata such as the file's path, its base name (extracted using os.path.basename), its size, and a 'type' field set to 'file'. Optionally, if the 'include_content' flag is set to True, the method also adds the file's decoded content to the dictionary.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether to include the file's content in the dictionary. Defaults to False.
        *   *Returns:*
            - **file_data** (`dict`): A dictionary containing metadata about the file, optionally including its content.
        *   **Usage:** Calls: `This method accesses 'self.path', 'self.size', 'os.path.basename', and conditionally 'self.content'.`; Called by: `This method is not explicitly called by other methods within the class, suggesting it's intended for external serialization or data export.`

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a comprehensive interface for managing a Git repository. It handles the cloning of a remote repository into a temporary local directory, offers methods to retrieve all files as structured RepoFile objects, and can generate a hierarchical file tree representation. It also implements the context manager protocol, ensuring proper cleanup of the temporary directory upon exiting a 'with' block.
*   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
*   **Dependencies:** `backend.getRepo.RepoFile`
*   **Constructor:**
    *   *Description:* The constructor initializes a GitRepository object by cloning a specified remote Git repository into a temporary local directory. It sets up essential instance attributes like the repository URL, the temporary directory path, and the git.Repo object. It also captures the latest commit and its tree, gracefully handling potential GitCommandError during the cloning process by cleaning up and raising a RuntimeError.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files()`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It utilizes the underlying Git command to list file paths, then iterates through these paths to instantiate RepoFile objects for each file. These RepoFile instances are stored internally and then returned as a list, providing a structured representation of the repository's contents.
        *   *Parameters:* []
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:** Calls: `This method calls the RepoFile constructor to create new file objects.`; Called by: `This method is not explicitly called by other methods in the provided context.`
    *   **`close`**
        *   *Signature:* `def close()`
        *   *Description:* This method is responsible for cleaning up resources by deleting the temporary directory where the Git repository was cloned. It checks if the temporary directory path is set before attempting to remove it. After deletion, it sets the `temp_dir` attribute to `None` to indicate that the directory has been cleaned up.
        *   *Parameters:* []
        *   *Returns:* []
        *   **Usage:** Calls: `This method does not explicitly call other methods or functions within the provided source.`; Called by: `This method is called by the `__exit__` method of the class.`
    *   **`__enter__`**
        *   *Signature:* `def __enter__()`
        *   *Description:* This special method enables the GitRepository object to function as a context manager, allowing its use with Python's `with` statement. When the `with` block is entered, this method is implicitly called and returns the instance of the object itself, making it available for operations within the context.
        *   *Parameters:* []
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository object.
        *   **Usage:** Calls: `This method does not explicitly call other methods or functions.`; Called by: `This method is implicitly called when the GitRepository object is used in a `with` statement.`
    *   **`__exit__`**
        *   *Signature:* `def __exit__(exc_type: type or None, exc_val: Exception or None, exc_tb: traceback or None)`
        *   *Description:* This special method is part of the context manager protocol, ensuring proper resource management. It is implicitly called when exiting a `with` statement, regardless of whether an exception occurred. Its primary role is to invoke the `close()` method, guaranteeing that the temporary repository directory and its contents are cleaned up.
        *   *Parameters:*
            - **exc_type** (`type or None`): The type of the exception raised, if any.
            - **exc_val** (`Exception or None`): The exception instance raised, if any.
            - **exc_tb** (`traceback or None`): The traceback object, if an exception was raised.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls the `close()` method of the class.`; Called by: `This method is implicitly called when exiting a `with` statement where the GitRepository object is used as a context manager.`
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(include_content: bool)`
        *   *Description:* This method constructs and returns a hierarchical tree representation of the files within the repository. If the list of files (`self.files`) is not yet populated, it first calls `get_all_files()` to retrieve them. It then iterates through each RepoFile object, splitting its path to build a nested dictionary structure that accurately reflects the directory and file hierarchy. Files are added to their respective directory levels, with an option to include their content.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the content of each file will be included in its dictionary representation. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the file tree, with 'name', 'type', and 'children' keys.
        *   **Usage:** Calls: `This method calls `self.get_all_files()` and `file_obj.to_dict()`.`; Called by: `This method is not explicitly called by other methods in the provided context.`

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart to visually compare the number of JSON tokens against TOON tokens. It takes the token counts, a calculated savings percentage, and an output file path as input. The chart displays two bars, one for JSON and one for TOON tokens, with their respective values shown above each bar. The title of the chart includes the savings percentage, and the y-axis is labeled 'Anzahl Token'. Finally, the function saves the generated chart to the specified output path and closes the plot to free up resources.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings, used in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart image will be saved.
*   **Returns:** []
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `backend.main.main_workflow`

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the effective processing time, referred to as "net time," by accounting for potential sleep durations introduced by rate-limiting mechanisms, specifically for "gemini-" models. It first determines the total elapsed time between a given start_time and end_time. If the model_name is not a "gemini-" model, or if total_items is zero, the function returns the total duration or zero, respectively. For "gemini-" models, it calculates the number of batches based on total_items and batch_size, then estimates the total sleep time (61 seconds per batch, excluding the first). Finally, it subtracts this estimated total_sleep_time from the total_duration, ensuring the returned net_time is not negative.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp of the operation.
    - **end_time** (`float`): The ending timestamp of the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed per batch.
    - **model_name** (`str`): The name of the model being used, which influences rate-limit calculations.
*   **Returns:**
    - **net_time** (`float`): The calculated net processing time in seconds, after subtracting estimated sleep times, or the total duration if no sleep times are applicable.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `backend.main.main_workflow`

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing a GitHub repository. It begins by extracting API keys and model configurations, then proceeds to clone the specified repository. The workflow involves extracting basic project information, constructing a file tree, performing relationship analysis, and building an Abstract Syntax Tree (AST). The AST is subsequently enriched with relationship data, and inputs are prepared for a Helper LLM to analyze individual functions and classes. Finally, a Main LLM generates a comprehensive report based on the collected data, which is then saved along with performance metrics and token savings analysis.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL for analysis.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., "gemini", "gpt", "scadsllm") and base URLs required for LLM interactions and other services.
    - **model_names** (`dict`): A dictionary specifying the names of the "helper" and "main" LLM models to be utilized in the analysis workflow.
    - **status_callback** (`callable`): An optional callable function that receives status messages, allowing for real-time updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): A string containing the final, comprehensive report generated by the Main LLM based on the repository analysis.
    - **metrics** (`dict`): A dictionary providing performance statistics, including execution times for helper and main LLMs, model names used, and token savings data.
*   **Usage:** Calls: `This function calls backend.AST_Schema.ASTAnalyzer, backend.AST_Schema.ASTAnalyzer.analyze_repository, backend.AST_Schema.ASTAnalyzer.merge_relationship_data, backend.HelperLLM.LLMHelper, backend.HelperLLM.LLMHelper.generate_for_classes, backend.HelperLLM.LLMHelper.generate_for_functions, backend.MainLLM.MainLLM, backend.MainLLM.MainLLM.call_llm, backend.basic_info.ProjektInfoExtractor, backend.basic_info.ProjektInfoExtractor.extrahiere_info, backend.getRepo.GitRepository, backend.main.calculate_net_time, backend.main.create_savings_chart, backend.main.update_status, backend.relationship_analyzer.ProjectAnalyzer, backend.relationship_analyzer.ProjectAnalyzer.analyze, backend.relationship_analyzer.ProjectAnalyzer.get_raw_relationships, schemas.types.ClassAnalysisInput, schemas.types.ClassContextInput, schemas.types.FunctionAnalysisInput, schemas.types.FunctionContextInput, and schemas.types.MethodContextInput.`; Called by: `This function is called by no other functions.`

#### Function: `update_status`
*   **Signature:** `def update_status(msg: str)`
*   **Description:** This function, `update_status`, is designed to report a given message to a status callback mechanism and log it. It accepts a message string as input. If a `status_callback` function is available in its scope, it invokes that callback with the provided message. Regardless of the callback's presence, the message is always logged at the INFO level using the `logging` module. The function does not return any explicit value.
*   **Parameters:**
    - **msg** (`str`): The message string to be reported and logged.
*   **Returns:** []
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `backend.main.main_workflow,backend.main.notebook_workflow`

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback: callable or None)`
*   **Description:** The notebook_workflow function orchestrates the end-to-end process of analyzing Jupyter notebooks found within a specified Git repository. It begins by extracting a GitHub URL from the input, cloning the repository, and converting its notebooks into an XML-based intermediate format. The function then extracts basic project information and initializes an appropriate Large Language Model (LLM) based on the provided model name and API keys. It iteratively processes each notebook, constructing a detailed payload (including text and embedded images) for the LLM to generate individual reports. Finally, all reports are concatenated, saved to a markdown file, and the function returns the combined report along with performance metrics.
*   **Parameters:**
    - **input** (`str`): The primary input string, which is expected to contain a valid GitHub repository URL.
    - **api_keys** (`dict`): A dictionary mapping LLM provider identifiers (e.g., "gpt", "gemini", "scadsllm", "ollama") to their respective API keys.
    - **model** (`str`): The identifier for the specific Large Language Model to be used for analysis, such as "gpt-4" or "gemini-pro".
    - **status_callback** (`callable or None`): An optional function that, if provided, will be called with status messages throughout the workflow execution for real-time updates.
*   **Returns:**
    - **report** (`str`): The comprehensive markdown report generated by the LLM, aggregating the analysis of all processed notebooks.
    - **metrics** (`dict`): A dictionary containing various performance metrics related to the workflow's execution, including total_time and the main_model used.
*   **Usage:** Calls: `This function calls backend.MainLLM.MainLLM, backend.MainLLM.MainLLM.call_llm, backend.basic_info.ProjektInfoExtractor, backend.basic_info.ProjektInfoExtractor.extrahiere_info, backend.converter.process_repo_notebooks, backend.getRepo.GitRepository, backend.main.gemini_payload, and backend.main.update_status.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `update_status`
*   **Signature:** `def update_status(msg: str)`
*   **Description:** *Analysis data not available for this component.*
*   **Parameters:**
    - **msg** (`str`): *Analysis data not available.*
*   **Returns:** []
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `backend.main.main_workflow,backend.main.notebook_workflow`

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info: dict, nb_path: str, xml_content: str, images: List[Dict])`
*   **Description:** This function constructs a multi-modal payload suitable for APIs like Google Gemini. It takes basic information, a notebook path, XML-like content with image placeholders, and a list of image data. It first serializes basic context information into a JSON string. Then, it parses the provided XML content, extracting text segments and replacing image placeholders with base64-encoded image URLs from the images list. The final output is a list of dictionaries, interleaving text and image data, ready for API consumption.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing general information about the project or context, which is serialized into a JSON string for the payload.
    - **nb_path** (`str`): The file path of the current notebook, included as part of the context information in the payload.
    - **xml_content** (`str`): A string representing the notebook's structure in an XML-like format, potentially containing <IMAGE_PLACEHOLDER/> tags.
    - **images** (`List[Dict]`): A list of dictionaries, where each dictionary contains image data, specifically a 'data' key holding a base64-encoded image string.
*   **Returns:**
    - **payload_content** (`List[Dict[str, Any]]`): A list of dictionaries, each representing a segment of the multi-modal payload. These segments can be either text ({"type": "text", "text": "..."}) or base64-encoded image URLs ({"type": "image_url", "image_url": {"url": "data:mime;base64,..."}}).
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

### File: `backend/relationship_analyzer.py`

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform static analysis on a Python project to build a comprehensive call graph. It identifies all Python files, collects definitions of classes, functions, and methods, and then resolves the relationships between these entities by tracking where they are called. The class provides methods to initiate the analysis, retrieve the raw call graph, and present the relationships in an organized incoming/outgoing format.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** `backend.relationship_analyzer.CallResolverVisitor`, `backend.relationship_analyzer.path_to_module`
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer instance by setting the project's root directory, and initializing internal data structures such as definitions, call_graph, and file_asts. It also defines a set of directories to ignore during file traversal to optimize the analysis process.
    *   *Parameters:*
        - **project_root** (`str`): The absolute path to the root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze()`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect definitions of functions, methods, and classes. Subsequently, it resolves the call relationships within these files. Finally, it clears the cached ASTs and returns the populated call graph.
        *   *Parameters:* []
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:** Calls: `This method calls _find_py_files, _collect_definitions, and _resolve_calls.`; Called by: `This method is not explicitly called by any other method in the provided context.`
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships()`
        *   *Description:* This method processes the internal call_graph to generate structured outgoing and incoming relationship dictionaries. It iterates through the call graph, extracting caller and callee identifiers, and populates two defaultdict(set) objects for outgoing and incoming calls. The sets are then converted to sorted lists for the final output.
        *   *Parameters:* []
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys: "outgoing" (a dictionary mapping caller IDs to sorted lists of callee IDs) and "incoming" (a dictionary mapping callee IDs to sorted lists of caller IDs).
        *   **Usage:** Calls: `This method does not explicitly call other methods or functions within the provided context.`; Called by: `This method is not explicitly called by any other method in the provided context.`
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files()`
        *   *Description:* This private helper method is responsible for traversing the project directory and identifying all Python files, while respecting the ignore_dirs list. It uses os.walk to recursively explore the directory structure, filtering out specified directories and collecting paths to files ending with ".py".
        *   *Parameters:* []
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found in the project, excluding ignored directories.
        *   **Usage:** Calls: `This method calls os.walk and os.path.join.`; Called by: `This method is called by analyze.`
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(filepath: str)`
        *   *Description:* This private method parses a given Python file to identify and store definitions of functions, methods, and classes. It reads the file, parses its Abstract Syntax Tree (AST), and then walks the AST to find FunctionDef and ClassDef nodes. For each definition, it constructs a unique path name and stores its file path, line number, and type in the self.definitions dictionary. It also caches the AST in self.file_asts. Error handling is included for file processing.
        *   *Parameters:*
            - **filepath** (`str`): The path to the Python file to be analyzed for definitions.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls path_to_module, _get_parent, ast.parse, ast.walk, ast.FunctionDef, ast.ClassDef, and logging.error.`; Called by: `This method is called by analyze.`
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(tree: ast.AST, node: ast.AST)`
        *   *Description:* This private utility method traverses an Abstract Syntax Tree (AST) to find the immediate parent node of a given child node. It iterates through all nodes in the tree and checks their children to identify if any child matches the provided node. If a match is found, the parent node is returned.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent** (`ast.AST or None`): The parent AST node if found, otherwise None.
        *   **Usage:** Calls: `This method calls ast.walk and ast.iter_child_nodes.`; Called by: `This method is called by _collect_definitions.`
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(filepath: str)`
        *   *Description:* This private method is responsible for identifying and resolving function and method calls within a specific Python file. It retrieves the cached AST for the given filepath. It then instantiates a CallResolverVisitor with the file's context and uses it to visit the AST, collecting call information. Finally, it extends the class's call_graph with the resolved calls from the visitor. Error handling is included for call resolution.
        *   *Parameters:*
            - **filepath** (`str`): The path to the Python file whose calls need to be resolved.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls CallResolverVisitor, resolver.visit, and logging.error.`; Called by: `This method is called by analyze.`

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST NodeVisitor designed to traverse a Python Abstract Syntax Tree to identify and resolve function and method calls. It records the fully qualified name of each called entity and contextual information about the caller, such as its file, line number, and type (module, function, or method). This class is crucial for building a comprehensive understanding of call relationships within a codebase.
*   **Instantiation:** `backend.relationship_analyzer.ProjectAnalyzer._resolve_calls`
*   **Dependencies:** `backend.relationship_analyzer.path_to_module`
*   **Constructor:**
    *   *Description:* The constructor initializes the CallResolverVisitor with the current file path, the project's root directory, and a dictionary of known definitions. It sets up internal state variables including `module_path`, `scope` for imports, `instance_types` for tracking object types, and `calls` as a defaultdict to store the detected call relationships.
    *   *Parameters:*
        - **filepath** (`str`): The absolute path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the entire project, used for calculating module paths.
        - **definitions** (`dict`): A dictionary containing known fully qualified names of functions, classes, and methods within the project.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* This method is invoked when the AST visitor encounters a class definition. It updates the `current_class_name` attribute to reflect the class currently being processed, which is essential for correctly forming fully qualified names of methods defined within that class. After processing the class's children nodes, it restores the previous `current_class_name` to maintain correct scope.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:* []
        *   **Usage:** Calls: `This method implicitly uses `self.generic_visit` to continue the AST traversal for child nodes.`; Called by: `This method is called by the `ast.NodeVisitor`'s traversal mechanism when a `ClassDef` node is encountered.`
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node: ast.FunctionDef)`
        *   *Description:* This method is called when the AST visitor encounters a function definition (either a top-level function or a method). It constructs the full qualified identifier for the function, considering if it's nested within a class. It then updates `current_caller_name` to this identifier, ensuring that any calls made within this function are correctly attributed. The previous `current_caller_name` is restored after processing the function's body.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:* []
        *   **Usage:** Calls: `This method implicitly uses `self.generic_visit` to continue the AST traversal for child nodes.`; Called by: `This method is called by the `ast.NodeVisitor`'s traversal mechanism when a `FunctionDef` node is encountered.`
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(node: ast.Call)`
        *   *Description:* This method is triggered upon encountering a function or method call in the AST. It attempts to resolve the fully qualified name of the called entity using the `_resolve_call_qname` helper. If the callee's qualified name is successfully resolved and exists in the known definitions, the call is recorded in `self.calls`, along with details about the caller such as its file, line number, full identifier, and type (e.g., 'method', 'function').
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing the function or method call.
        *   *Returns:* []
        *   **Usage:** Calls: `This method calls `self._resolve_call_qname` to determine the qualified name of the function being called and uses `os.path.basename` to extract the base filename.`; Called by: `This method is called by the `ast.NodeVisitor`'s traversal mechanism when a `Call` node is encountered.`
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* This method processes `import` statements in the AST. For each imported module or alias, it stores a mapping in `self.scope` from the local name (or alias) to its original module name. This scope information is later used to resolve the fully qualified names of calls to imported modules or functions.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* []
        *   **Usage:** Calls: `This method implicitly uses `self.generic_visit` to continue the AST traversal for child nodes.`; Called by: `This method is called by the `ast.NodeVisitor`'s traversal mechanism when an `Import` node is encountered.`
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* This method handles `from ... import ...` statements. It determines the full module path for each imported name, correctly handling relative imports based on `node.level`. The mapping from the imported name (or its alias) to its fully qualified path is then stored in `self.scope`, which is crucial for resolving calls to specific functions or classes imported from other modules.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* []
        *   **Usage:** Calls: `This method implicitly uses `self.generic_visit` to continue the AST traversal for child nodes.`; Called by: `This method is called by the `ast.NodeVisitor`'s traversal mechanism when an `ImportFrom` node is encountered.`
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(node: ast.Assign)`
        *   *Description:* This method processes assignment statements, specifically looking for instances where a variable is assigned the result of a class constructor call (e.g., `my_object = MyClass()`). If such a pattern is detected and the class is a known definition, it records the fully qualified class name as the type of the assigned variable in `self.instance_types`. This information is vital for resolving method calls on these instantiated objects.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:* []
        *   **Usage:** Calls: `This method implicitly uses `self.generic_visit` to continue the AST traversal for child nodes.`; Called by: `This method is called by the `ast.NodeVisitor`'s traversal mechanism when an `Assign` node is encountered.`
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(func_node: ast.expr)`
        *   *Description:* This private helper method is responsible for resolving the fully qualified name (QName) of a function or method call from its AST node. It handles two primary scenarios: direct name calls (e.g., `func()`) by checking `self.scope` and local definitions, and attribute calls (e.g., `obj.method()`) by first determining the type of the object (`obj`) using `self.instance_types` or `self.scope` to construct the full path.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called, which can be an `ast.Name` or `ast.Attribute`.
        *   *Returns:*
            - **name** (`str | None`): The fully qualified name of the callable if successfully resolved, otherwise None.
        *   **Usage:** Calls: `This method does not explicitly call other functions or methods within its source code.`; Called by: `This method is called by `visit_Call` to determine the qualified name of the function or method being invoked.`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into a Python module path string. It first attempts to determine the path relative to a specified project root, falling back to the base filename if a ValueError occurs. It then removes the '.py' file extension if present and replaces system path separators with dots. Finally, it adjusts the module path by removing the '.__init__' suffix if it corresponds to an `__init__.py` file.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used as a reference to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string, e.g., 'my_package.my_module'.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

### File: `backend/scads_key_test.py`

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function encrypts a given string using a `cipher_suite` object. It first checks if the input `text` is empty or if the `cipher_suite` is not initialized; if either condition is true, it returns the original text without encryption. Otherwise, it prepares the text by stripping whitespace and encoding it into bytes. The prepared text is then encrypted using the `cipher_suite.encrypt()` method, and the resulting encrypted bytes are decoded back into a string before being returned. This process ensures that sensitive text data can be securely processed.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input text, or the original text if encryption conditions are not met.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is called by no other functions.`

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given string using a `cipher_suite` object. It first performs a guard clause, returning the original text if the input `text` is empty or if `cipher_suite` is not initialized. If decryption is attempted, the text is stripped of whitespace, encoded to bytes, decrypted using `cipher_suite.decrypt`, and then decoded back to a string. A try-except block handles potential decryption errors, returning the original text in case of any failure during the decryption process.
*   **Parameters:**
    - **text** (`str`): The string value that needs to be decrypted.
*   **Returns:**
    - **decrypted_string** (`str`): The decrypted string if successful, or the original input string if decryption is skipped or an error occurs during the process.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function is responsible for creating a new user entry in the database. It takes a username, display name, and a plain-text password as input. The password is first hashed using `stauth.Hasher.hash` for security before being stored. A user document is constructed, including default empty strings for Gemini, Ollama, and GPT API keys. This document is then inserted into the `dbusers` collection.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user.
    - **name** (`str`): The display name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier of the newly inserted user document, typically a MongoDB ObjectId.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is called by no other functions.`

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function, `fetch_all_users`, is designed to retrieve all user documents from a database collection named `dbusers`. It executes a `find()` operation on the `dbusers` collection, which typically returns a cursor. This cursor is then immediately converted into a standard Python list, containing all the fetched user documents, before being returned by the function.
*   **Parameters:** []
*   **Returns:**
    - **users** (`list`): A list of all user documents retrieved from the 'dbusers' collection.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The `fetch_user` function is designed to retrieve a single user document from a database collection named `dbusers`. It takes a `username` as input and uses it to query the collection based on the `_id` field. The function then returns the first document that matches the provided username, or `None` if no such user is found.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched, which corresponds to the `_id` field in the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user's document if found, otherwise `None`.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the 'name' field for a specific user in the 'dbusers' collection. It identifies the user document by its '_id' field, which is expected to match the provided 'username'. The function then sets the 'name' field of that user's document to the 'new_name'. It returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose name is to be updated. This value is used to match the '_id' field in the database.
    - **new_name** (`str`): The new name to be assigned to the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. Returns 0 if no document matched the username or if the name was already the new_name.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function is responsible for updating a user's Gemini API key within the database. It takes the username and the new API key as input. The provided API key is first processed by removing any leading or trailing whitespace, then it is encrypted using a dedicated encryption function. Finally, the encrypted key is stored in the 'gemini_api_key' field for the specified user in the 'dbusers' collection.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 0 or 1.
*   **Usage:** Calls: `This function calls database.db.encrypt_text.`; Called by: `This function is called by no other functions.`

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** This function is responsible for updating a user's GPT API key within the database. It takes a username and a new API key as input. The provided API key is first stripped of any leading/trailing whitespace and then encrypted using a helper function. Finally, the encrypted key is stored in the database for the specified user, identified by their username.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be stored for the user. It will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents (users) that were modified by the update operation. This will typically be 0 or 1.
*   **Usage:** Calls: `This function calls database.db.encrypt_text.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specific user in a database. It takes a username and a new Ollama base URL as input. The function locates the user document using the provided username as the document's `_id` and then updates the `ollama_base_url` field, stripping any leading or trailing whitespace from the new URL. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL needs to be updated. This is used as the `_id` in the database query.
    - **ollama_base_url** (`str`): The new base URL for Ollama to be associated with the user. This string will have leading/trailing whitespace removed before being stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database as a result of the update operation. A value of 1 indicates success if the user existed and the URL was different, 0 if the user existed but the URL was the same, or if the user did not exist.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function updates a user's Open Source API key within a database. It accepts a username and the new API key as input. The provided API key is first processed by stripping any leading or trailing whitespace, and then it is encrypted using a dedicated encryption function. Finally, the function performs an update operation on the `dbusers` collection, identifying the target user by their username and setting the `opensrc_api_key` field to the newly encrypted value. The operation returns the count of documents that were successfully modified.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source API key needs to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be stored for the specified user. This key will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 0 or 1.
*   **Usage:** Calls: `This function calls database.db.encrypt_text.`; Called by: `This function is not called by any other functions.`

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** This function updates the 'opensrc_base_url' for a specific user in a database. It takes a username and a new Open Source base URL as input. The provided URL is first stripped of any leading or trailing whitespace. The function then performs an update operation on the 'dbusers' collection, setting the 'opensrc_base_url' field for the document matching the given username. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source base URL needs to be updated.
    - **opensrc_base_url** (`str`): The new Open Source base URL to be set for the user, which will be stripped of whitespace.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** This function retrieves the Gemini API key for a specified user from a database. It queries a 'dbusers' collection, searching for a document where the '_id' field matches the provided 'username'. If a user document is found, the function extracts the 'gemini_api_key' field from it. The function returns the Gemini API key as a string if it exists, otherwise it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key associated with the user, or None if the user is not found or the key does not exist in the user's document.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is called by no other functions.`

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function is designed to retrieve the Ollama base URL for a specific user from a database. It takes a username as input and queries a 'dbusers' collection. The function specifically looks for the 'ollama_base_url' field within the user's document. If a user document is found and contains the URL, it is returned; otherwise, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The base URL for the Ollama service associated with the user, or None if the user or the URL is not found in the database.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** This function is designed to retrieve a GPT API key for a specified user from a database. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided username. If a user is found, it extracts and returns the 'gpt_api_key' field. If the user is not found or the key is missing, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str or None`): The GPT API key associated with the given username, or None if the user or key is not found.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** This function retrieves an Open Source API key for a specified user from a database. It queries the 'dbusers' collection using the provided username as the document's '_id'. If a matching user document is found, the function extracts and returns the 'opensrc_api_key' field. If no user document is found, or if the 'opensrc_api_key' field is absent, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source API key is to be fetched.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key associated with the user, or None if the user is not found or the key does not exist.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** This function retrieves the 'opensrc_base_url' for a specific user from a database. It queries the 'dbusers' collection using the provided username as the document's identifier. The function specifically projects only the 'opensrc_base_url' field. If a user is found, it returns the associated URL; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The username (which serves as the document's '_id') for which to fetch the Open Source base URL.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The Open Source base URL associated with the username, or None if the user is not found in the database.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is designed to remove a specific user record from a database collection. It accepts a username, which is then used as the unique identifier (`_id`) to locate and delete a single document within the `dbusers` collection. The function returns an integer indicating the number of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation. For `delete_one`, this will typically be 0 or 1.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts various API keys and URLs associated with a specific user from a database. It queries the 'dbusers' collection using the provided username as the document's identifier. If no user is found, the function returns None for all expected values. Otherwise, it extracts and decrypts API keys for Gemini, GPT, and open-source services, and retrieves base URLs for Ollama and open-source services, returning all these processed values.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, an empty string if not found in the user document, or None if the user is not found.
    - **ollama_plain** (`str | None`): The Ollama base URL, an empty string if not found in the user document, or None if the user is not found.
    - **gpt_plain** (`str | None`): The decrypted GPT API key, an empty string if not found in the user document, or None if the user is not found.
    - **opensrc_plain** (`str | None`): The decrypted open-source API key, an empty string if not found in the user document, or None if the user is not found.
    - **opensrc_url** (`str | None`): The open-source base URL, an empty string if not found in the user document, or None if the user is not found.
*   **Usage:** Calls: `This function calls database.db.decrypt_text.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** This function creates a new chat entry in a database. It generates a unique identifier using UUID, records the provided username and chat name, and timestamps the creation. The constructed chat object is then inserted into the 'dbchats' collection, and the unique ID of the newly inserted document is returned.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (UUID) of the newly created chat entry in the database.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** This function retrieves all chat entries associated with a specific username from the `dbchats` collection. It queries the database using the provided username and then sorts the results by the `created_at` field in ascending order. The function converts the database cursor into a list of chat documents before returning them.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the associated chat documents.
*   **Returns:**
    - **chats** (`list`): A list of chat documents (dictionaries or objects) belonging to the specified user, sorted by their creation timestamp.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks for the existence of a specific chat within a database collection named `dbchats`. It takes a username and a chat name as input. The function queries the `dbchats` collection to find a document that matches both the provided username and chat name. It returns a boolean indicating whether such a chat exists.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked for existence.
*   **Returns:**
    - **chat_exists** (`bool`): True if a chat matching the given username and chat name is found; False otherwise.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and all its associated exchanges within a database. It first updates a single chat entry in the `dbchats` collection, changing its `chat_name` from `old_name` to `new_name`. Subsequently, it updates multiple exchange entries in the `dbexchanges` collection to reflect the new chat name for all exchanges linked to the original chat. The function returns the count of modified chat entries from the initial chat renaming operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The desired new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat documents modified by the `dbchats.update_one` operation.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str, json_tokens: int, toon_tokens: int, savings_percent: float)`
*   **Description:** This function inserts a new exchange record into a database collection. It generates a unique identifier for the new record using UUID, constructs a dictionary containing various details about the exchange including question, answer, feedback, user information, usage metrics, and a creation timestamp. The function attempts to insert this record into the 'dbexchanges' collection. If the insertion is successful, it returns the newly generated ID; otherwise, it catches any exceptions, prints an error message, and returns None.
*   **Parameters:**
    - **question** (`str`): The question string of the exchange.
    - **answer** (`str`): The answer string of the exchange.
    - **feedback** (`str`): The feedback string for the exchange.
    - **username** (`str`): The username associated with the exchange.
    - **chat_name** (`str`): The name of the chat where the exchange occurred.
    - **helper_used** (`str`): Indicates which helper model was used, defaults to an empty string.
    - **main_used** (`str`): Indicates which main model was used, defaults to an empty string.
    - **total_time** (`str`): The total time taken for the exchange, defaults to an empty string.
    - **helper_time** (`str`): The time taken by the helper model, defaults to an empty string.
    - **main_time** (`str`): The time taken by the main model, defaults to an empty string.
    - **json_tokens** (`int`): The number of JSON tokens used, defaults to 0.
    - **toon_tokens** (`int`): The number of 'toon' tokens used, defaults to 0.
    - **savings_percent** (`float`): The percentage of savings achieved, defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly inserted exchange record if successful.
    - **None** (`NoneType`): Returns None if an error occurs during the database insertion.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records associated with a specific user from a database. It queries the 'dbexchanges' collection using the provided username as a filter. The results are then sorted in ascending order based on their 'created_at' timestamp, which is noted as important for display purposes. Finally, the function converts these sorted exchange records into a list and returns them.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch exchange records.
*   **Returns:**
    - **exchanges** (`list[dict]`): A list of exchange records (dictionaries), sorted by 'created_at' in ascending order.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** The `fetch_exchanges_by_chat` function is designed to retrieve a list of conversation exchanges from a database. It queries a collection named `dbexchanges`, filtering records by a specific username and chat name. The matching exchanges are then sorted chronologically based on their `created_at` timestamp in ascending order. The function returns these retrieved exchanges as a Python list.
*   **Parameters:**
    - **username** (`str`): The username associated with the exchanges to be fetched.
    - **chat_name** (`str`): The name of the chat associated with the exchanges to be fetched.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation time.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function is responsible for updating the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function uses the `dbexchanges.update_one` method to locate the document by its `_id` and then sets the 'feedback' field to the provided integer. Finally, it returns the count of documents that were modified by the operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated.
    - **feedback** (`int`): The integer feedback value to set for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 0 or 1.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates a specific exchange record in a database collection. It accepts an `exchange_id` and a `feedback_message` string. The function locates the document in the `dbexchanges` collection using the provided `exchange_id`. It then sets the `feedback_message` field of that document to the new message. The function returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange document to be updated. This typically corresponds to the `_id` field in MongoDB.
    - **feedback_message** (`str`): The new feedback message to be stored for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. This will typically be 0 or 1.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not called by any other functions.`

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function, `delete_exchange_by_id`, is designed to remove a specific exchange record from a database collection. It takes a unique `exchange_id` as input and uses it to locate and delete a single document where the `_id` field matches. The function then returns an integer indicating the number of documents that were successfully deleted, typically 0 or 1.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange document to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted (0 or 1) as a result of the operation.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is called by no other functions.`

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is designed to completely remove a specific chat and all its associated message exchanges from the database. It first deletes all messages (exchanges) linked to the given username and chat name using a `dbexchanges.delete_many` operation. Following this, it removes the chat entry itself from the `dbchats` collection via a `dbchats.delete_one` call. This two-step process ensures data consistency by clearing all related data for the specified chat.
*   **Parameters:**
    - **username** (`str`): The identifier of the user who owns the chat to be deleted.
    - **chat_name** (`str`): The specific name of the chat to be removed from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents successfully deleted from the 'dbchats' collection. This value is typically 1 if the chat was found and deleted, or 0 if no matching chat was found.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list: List[str])`
*   **Description:** This function takes a list of strings, presumably representing paths or URLs. For each string in the input list, it splits the string by the '/' character and extracts the last segment. The function then returns a new list containing these extracted last segments, effectively 'cleaning' the names by removing path prefixes.
*   **Parameters:**
    - **model_list** (`List[str]`): A list of strings, where each string is expected to contain path-like segments separated by '/'. For example, a list of file paths or URLs.
*   **Returns:**
    - **cleaned_names** (`List[str]`): A new list of strings, where each string is the last segment obtained by splitting the corresponding input string by '/'.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is called by no other functions.`

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list: list, category_name: str)`
*   **Description:** The `get_filtered_models` function filters a provided list of models, `source_list`, based on a specified `category_name`. It retrieves associated keywords from a global `CATEGORY_KEYWORDS` mapping. If the category is designated as "STANDARD", the function returns only those models from `source_list` that are also present in a `STANDARD_MODELS` list. For other categories, it iterates through the `source_list` and includes models whose names (case-insensitive) contain any of the category's keywords. If no models match the keywords, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The initial list of models to be filtered.
    - **category_name** (`str`): The name of the category used to determine filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered according to the specified category, or the original `source_list` if no matches are found or specific filtering criteria are met (e.g., "STANDARD" category).
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is called by no other functions.`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function serves as a callback to save a user's Gemini API key. It retrieves a potential new key from the Streamlit session state. If a valid new key is found, it proceeds to update the user's Gemini key in the database. After a successful update, the function clears the key from the session state and displays a success notification to the user.
*   **Parameters:** []
*   **Returns:** []
*   **Usage:** Calls: `This function calls database.db.update_gemini_key.`; Called by: `This function is called by no other functions.`

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function, `save_ollama_cb`, serves as a callback to handle the saving of an Ollama URL. It first attempts to retrieve a new Ollama URL from the Streamlit session state, using the key "in_ollama_url". If a non-empty URL is successfully retrieved, the function proceeds to update this URL in the database. It utilizes `db.update_ollama_url` to store the `new_url` associated with the current user's username, also obtained from the session state. Upon successful database update, a confirmation toast message is displayed to the user.
*   **Parameters:** []
*   **Returns:** []
*   **Usage:** Calls: `This function calls database.db.update_ollama_url.`; Called by: `This function is not called by any other functions.`

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function, `load_data_from_db`, is designed to load chat data and associated exchanges from the database into the Streamlit session state for a specified user. It first checks if the data for the given username is already loaded to avoid redundant operations. The function retrieves predefined chats, then fetches individual exchanges and organizes them under their respective chat names within the session state. It also includes logic to create a default chat if no chats are found and ensures an active chat is set for the user's session.
*   **Parameters:**
    - **username** (`str`): The username for whom chats and exchanges should be loaded from the database.
*   **Returns:** []
*   **Usage:** Calls: `This function calls database.db.fetch_chats_by_user, database.db.fetch_exchanges_by_user, and database.db.insert_chat.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: dict, val: Any)`
*   **Description:** This function `handle_feedback_change` processes a change in feedback for an exchange object. It updates the 'feedback' key within the provided `ex` dictionary-like object with the new `val`. Concurrently, it calls a database utility function, `db.update_exchange_feedback`, to persist this feedback change using the `_id` from the `ex` object. Finally, it triggers a re-execution of the Streamlit application to reflect the changes in the user interface.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing an exchange or data record, expected to contain 'feedback' and '_id' keys.
    - **val** (`Any`): The new feedback value to be assigned to the exchange object.
*   **Returns:** []
*   **Usage:** Calls: `This function calls database.db.update_exchange_feedback.`; Called by: `This function is called by no other functions.`

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: str, ex: dict)`
*   **Description:** This function handles the deletion of a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if the exchange is present within that chat's exchanges list, it removes it from the session state. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat to which the exchange belongs, used to locate it in the session state.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' key for database deletion and to be an item in the chat's 'exchanges' list.
*   **Returns:** []
*   **Usage:** Calls: `This function calls database.db.delete_exchange_by_id.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** This function handles the deletion of a specific chat for a given user. It first calls the database to remove the chat entirely. Subsequently, it cleans up the Streamlit session state by removing the chat from the `st.session_state.chats` dictionary. If the deleted chat was the active one, or if no chats remain, it reconfigures the `st.session_state.active_chat`. If all chats are deleted, a new default chat named "Chat 1" is created in the database and session state. Finally, it triggers a Streamlit rerun to refresh the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** []
*   **Usage:** Calls: `This function calls database.db.delete_full_chat and database.db.insert_chat.`; Called by: `This function is called by no other functions.`

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text: str)`
*   **Description:** This function extracts a repository name from an input text string. It first attempts to find a URL within the text using a regular expression. If a URL is identified, it is parsed to isolate the path component. The function then processes this path, taking the last segment as the potential repository name and removing a '.git' suffix if present. It returns the extracted repository name as a string or None if no URL is found or a repository name cannot be determined from the path.
*   **Parameters:**
    - **text** (`str`): The input string that may contain a URL from which to extract a repository name.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string, or None if no URL is found or a repository name cannot be determined.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text: str)`
*   **Description:** This function acts as a generator that takes a string of text and yields its words sequentially, each followed by a space. It simulates a streaming effect by introducing a small delay after yielding each word. The primary purpose is to process text into a word-by-word output stream, often used for displaying text gradually.
*   **Parameters:**
    - **text** (`str`): The input string of text to be processed and streamed word by word.
*   **Returns:**
    - **word_with_space** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:** Calls: `This function calls no other functions.`; Called by: `This function is not explicitly called by any other functions in the provided context.`

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str, should_stream: bool)`
*   **Description:** This function processes a given markdown text, identifying and rendering embedded Mermaid diagrams. It splits the input text into parts based on '```mermaid' delimiters. Non-Mermaid text sections are rendered as standard markdown, optionally streamed if 'should_stream' is true. Mermaid code blocks are attempted to be rendered using 'st_mermaid', with a fallback to displaying the raw code block if rendering fails. The function handles empty input text by returning early.
*   **Parameters:**
    - **markdown_text** (`str`): The input text, which may contain embedded Mermaid diagrams within '```mermaid' blocks.
    - **should_stream** (`bool`): A boolean flag indicating whether non-Mermaid text parts should be streamed using 'st.write_stream' or rendered directly with 'st.markdown'. Defaults to False.
*   **Returns:** []
*   **Usage:** Calls: `This function calls frontend.frontend.stream_text_generator.`; Called by: `This function is called by no other functions.`

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** This function is responsible for rendering a single chat exchange within a Streamlit application. It displays the user's question and the assistant's answer. The function includes a dynamic toolbar for the assistant's message, offering feedback mechanisms (like/dislike), a comment popover, download functionality, and the option to delete the message. It also handles displaying error states for the assistant's response and renders the answer content, potentially with Mermaid diagrams.
*   **Parameters:**
    - **ex** (`dict`): A dictionary containing the exchange data, including the user's 'question', the assistant's 'answer', 'feedback' status, 'feedback_message', and a unique identifier '_id'.
    - **current_chat_name** (`str`): The name of the current chat session, used for contextual operations such as deleting an exchange.
*   **Returns:** []
*   **Usage:** Calls: `This function calls database.db.update_exchange_feedback_message, frontend.frontend.handle_delete_exchange, frontend.frontend.handle_feedback_change, and frontend.frontend.render_text_with_mermaid.`; Called by: `This function is called by no other functions.`

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The `ParameterDescription` class is a Pydantic BaseModel designed to provide a structured representation for a single parameter of a function. It encapsulates essential information about a parameter, including its name, its inferred data type, and a descriptive explanation of its purpose or usage. This model serves as a standardized data structure for documenting function parameters, facilitating automated schema generation or API documentation.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, does not explicitly define an `__init__` method. Pydantic automatically generates a constructor that accepts keyword arguments corresponding to the defined fields (`name`, `type`, `description`) for instantiation and validation.
    *   *Parameters:* []
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The `ReturnDescription` class is a Pydantic BaseModel designed to provide a structured schema for describing the return value of a function. It encapsulates three essential pieces of information: the name of the return value, its data type, and a textual description. This class ensures type validation and consistency for function return metadata, making it suitable for use in API specifications or documentation generation.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** `pydantic.BaseModel`
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is implicitly generated to validate and assign values to the `name`, `type`, and `description` fields upon instantiation. It ensures that any object created from this class conforms to the defined schema and types.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The data type of the return value (e.g., 'str', 'int', 'List[str]').
        - **description** (`str`): A textual explanation of what the return value represents or its purpose.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about the calling context of a function or method. It serves as a structured data container, holding two string attributes: 'calls', which describes what the entity calls, and 'called_by', which describes what calls the entity. This class provides a standardized way to represent and exchange usage context data within a larger system.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, has an implicitly generated constructor. It initializes an instance by accepting values for 'calls' and 'called_by', which are then stored as instance attributes.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions, methods, or external entities that this context's subject calls.
        - **called_by** (`str`): A string describing the functions, methods, or external entities that call this context's subject.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic BaseModel designed to provide a structured and comprehensive analysis of a Python function. It serves as a data container for various attributes that describe a function, including its overarching purpose, its input parameters, its return values, and its usage context within a larger codebase. This model facilitates the standardized representation and validation of function metadata.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. It initializes instances by validating and assigning values to its defined fields: `overall`, `parameters`, `returns`, and `usage_context`. These fields are essential for capturing the complete description of a function.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary describing the function's primary purpose and behavior.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing an input parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects, each detailing a possible return value of the function.
        - **usage_context** (`UsageContext`): An object providing context about where the function is called and what other entities it calls.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to structure and validate the comprehensive analysis of a Python function. It serves as the primary data model for representing a function's identifier, its detailed description (including purpose, parameters, returns, and usage context), and any potential errors encountered during its analysis. This class is crucial for standardizing the output of automated code analysis tools.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, does not have an explicitly defined `__init__` method. Pydantic automatically generates a constructor that accepts keyword arguments corresponding to the class fields (`identifier`, `description`, `error`) for instantiation and validation.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the function being analyzed.
        - **description** (`FunctionDescription`): An object containing the detailed analysis of the function, including its overall purpose, parameters, return values, and usage context.
        - **error** (`Optional[str]`): An optional string field to capture any error messages or issues encountered during the function's analysis. Defaults to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to provide a structured representation of a class's `__init__` method. It encapsulates a textual summary of the constructor's purpose and behavior, along with a list of detailed descriptions for each of its parameters. This model is fundamental for systems that require programmatic analysis, documentation, or generation of information about class constructors.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for ConstructorDescription is implicitly generated. It accepts 'description' as a string and 'parameters' as a list of ParameterDescription objects. These arguments are used to initialize the corresponding attributes of the instance, ensuring type validation according to the Pydantic schema.
    *   *Parameters:*
        - **description** (`str`): A string providing a high-level summary of the constructor's functionality.
        - **parameters** (`List[ParameterDescription]`): A list containing detailed descriptions for each parameter accepted by the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate information about a class's contextual usage. It specifically tracks external dependencies and the locations where the class is instantiated. This model provides a structured way to represent metadata crucial for understanding a class's role and integration within a larger system.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* The `__init__` method for this Pydantic BaseModel is implicitly generated, allowing instantiation by providing values for `dependencies` and `instantiated_by` as keyword arguments. Pydantic handles validation and assignment of these attributes upon object creation.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class, typically a summary of other modules, functions, or classes it relies upon.
        - **instantiated_by** (`str`): A string describing the primary locations or components within the system where this class is instantiated.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of another Python class. It serves as a structured data container for various aspects of a class, including its high-level purpose, details of its constructor, a list of analyses for its individual methods, and its broader usage context within a system. This model is crucial for standardizing the representation of class analysis results.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* The ClassDescription class is a Pydantic BaseModel, which means its constructor is implicitly generated by Pydantic. It initializes instances by accepting values for its defined fields: overall, init_method, methods, and usage_context.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose.
        - **init_method** (`ConstructorDescription`): Details about the class's constructor, including its description and parameters.
        - **methods** (`List[FunctionAnalysis]`): A list of analyses for each method within the class, providing detailed information about their purpose, parameters, and return values.
        - **usage_context** (`ClassContext`): Contextual information regarding the class's external dependencies and where it is instantiated.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the root Pydantic model for structuring the comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed ClassDescription object containing insights into its constructor and methods, and an optional field for reporting any analysis errors. This model is fundamental for generating structured, machine-readable reports about analyzed Python classes.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. As a pydantic.BaseModel, its constructor is implicitly generated by Pydantic, which handles the validation and assignment of its fields: identifier, description, and error.
    *   *Parameters:*
        - **identifier** (`str`): The unique string identifier for the class being analyzed.
        - **description** (`ClassDescription`): A comprehensive object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
        - **error** (`Optional[str]`): An optional string that provides an error message if the class analysis failed, otherwise it is None.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event within a system, likely for relationship analysis. It provides a structured data model to store information about where a call originates, including the file path, the name of the calling function, the type of call (e.g., method, function), and the line number. This model is intended to be used in lists that track 'called_by' and 'instantiated_by' relationships.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the CallInfo class automatically generates its `__init__` method. This constructor allows for the direct instantiation of CallInfo objects by providing values for its defined fields: file, function, mode, and line. Pydantic handles validation and assignment of these attributes upon object creation.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that performed the call.
        - **mode** (`str`): The type of call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the file where the call event occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to provide a structured context for analyzing a function. It encapsulates information about the functions or methods that a specific function calls and the functions or methods that called it. This model is used to standardize the input data required for a comprehensive function analysis.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class does not define an explicit `__init__` method. As a Pydantic `BaseModel`, it automatically handles the initialization of its fields `calls` and `called_by` based on the provided arguments during instantiation.
    *   *Parameters:* []
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a FunctionAnalysis object. It serves as a data validation and serialization schema, ensuring that all necessary components for analyzing a function, such as its source code, identifier, and contextual information, are present and correctly typed. This class acts as a contract for the data payload used in the function analysis process.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. It inherits from Pydantic's `BaseModel`, and its initialization is handled implicitly by Pydantic, which validates and assigns values to its fields based on the provided arguments. The class fields are `mode`, `identifier`, `source_code`, `imports`, and `context`.
    *   *Parameters:* []
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to provide a structured schema for representing the contextual information of a class method. It encapsulates key details such as the method's unique identifier, a list of other functions or methods it calls, a list of locations from which it is called, its arguments, and its docstring. This model serves as a data transfer object or a validation schema for method-level context within a larger system, ensuring consistency and type safety for method analysis data.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* The `__init__` method for `MethodContextInput` is implicitly generated by Pydantic's BaseModel. It allows for the creation of instances by accepting values for its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`. Pydantic handles the validation of these input values against their specified types and assigns them as instance attributes upon object initialization.
    *   *Parameters:*
        - **identifier** (`str`): A unique string that identifies the method.
        - **calls** (`List[str]`): A list of strings, each representing another method, class, or function that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects, indicating where this method is called from within the codebase.
        - **args** (`List[str]`): A list of strings, each representing an argument taken by this method.
        - **docstring** (`Optional[str]`): An optional string containing the method's docstring, if available.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput is a Pydantic BaseModel designed to structure the contextual information necessary for analyzing a Python class. It serves as a data container, holding lists of external dependencies, locations where the class is instantiated, and detailed context for each of the class's methods. This model ensures that all relevant contextual data is organized and validated for subsequent analytical processes.
*   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, meaning its initialization is handled automatically by Pydantic. Instances are created by passing keyword arguments for `dependencies`, `instantiated_by`, and `method_context`, which Pydantic then validates and assigns as instance attributes.
    *   *Parameters:* []
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic model designed to define the structured input required for generating a ClassAnalysis object. It serves as a data validation and parsing schema, ensuring that all necessary components for analyzing a Python class, such as its source code, identifier, and contextual information, are provided in a consistent format. This class facilitates the reliable exchange of class analysis requests within a larger system.
*   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
*   **Dependencies:** *Analysis data not available for this component.*
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. It inherits from pydantic.BaseModel, and its initialization is handled implicitly by Pydantic based on the declared fields, which include 'mode', 'identifier', 'source_code', 'imports', and 'context'.
    *   *Parameters:* []
*   **Methods:**

---
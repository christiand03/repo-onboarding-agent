# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** This project is an automated documentation pipeline designed to onboard developers to a new codebase. It takes a Git repository URL as input, clones it, and performs a multi-layered static analysis. The system uses a dual-LLM architecture: "Helper LLMs" analyze individual code components (functions and classes) in parallel, and a "Main LLM" synthesizes these granular analyses into a cohesive, human-readable Markdown report. The entire process is orchestrated through a Streamlit-based web frontend, providing a user-friendly interface for generating and viewing the documentation.
- **Key Features:**
  - **Automated Repository Analysis:** Clones and analyzes public Git repositories directly from a URL.
  - **Dual-LLM Pipeline:** Utilizes specialized Helper LLMs for detailed code analysis and a Main LLM for high-level synthesis, enabling scalability and depth.
  - **Comprehensive Static Analysis:** Builds an Abstract Syntax Tree (AST), constructs file dependency graphs, and analyzes call relationships between functions and classes.
  - **Jupyter Notebook Support:** Capable of parsing and analyzing `.ipynb` notebook files, including their markdown, code, and output cells.
  - **Web-Based Interface:** A Streamlit frontend allows for easy interaction, API key management, model selection, and viewing of generated reports.
- **Tech Stack:**
  - **Backend:** Python, LangChain, GitPython, Pydantic, NetworkX, TOON Format
  - **Frontend:** Streamlit, Streamlit Authenticator
  - **LLM Integration:** Google Gemini, OpenAI Models, Ollama, Custom API endpoints
  - **Database:** MongoDB (via pymongo)

*   **Repository Structure:**
    ```mermaid
    graph LR
        root["/ (root)"]
        
        root --> root_files["
            .env.example<br/>
            .gitignore<br/>
            analysis_output.json<br/>
            output.json<br/>
            output.toon<br/>
            readme.md<br/>
            requirements.txt<br/>
            test.json
        "]

        root --> SystemPrompts
        SystemPrompts["SystemPrompts/"] --> SystemPrompts_files["
            SystemPromptClassHelperLLM.txt<br/>
            SystemPromptFunctionHelperLLM.txt<br/>
            SystemPromptHelperLLM.txt<br/>
            SystemPromptMainLLM.txt<br/>
            SystemPromptMainLLMToon.txt<br/>
            SystemPromptNotebookLLM.txt
        "]

        root --> backend
        backend["backend/"] --> backend_files["
            AST_Schema.py<br/>
            File_Dependency.py<br/>
            HelperLLM.py<br/>
            MainLLM.py<br/>
            __init__.py<br/>
            basic_info.py<br/>
            callgraph.py<br/>
            converter.py<br/>
            getRepo.py<br/>
            main.py<br/>
            relationship_analyzer.py<br/>
            scads_key_test.py
        "]

        root --> database
        database["database/"] --> database_files["
            db.py
        "]

        root --> frontend
        frontend["frontend/"] --> frontend_files["
            __init__.py<br/>
            frontend.py
        "]
        frontend --> frontend_streamlit[".streamlit/"]
        frontend_streamlit --> frontend_streamlit_files["config.toml"]
        frontend --> frontend_gifs["gifs/"]
        frontend_gifs --> frontend_gifs_files["4j.gif"]

        root --> notizen
        notizen["notizen/"] --> notizen_files["
            Report Agenda.txt<br/>
            Zwischenpraesentation Agenda.txt<br/>
            doc_bestandteile.md<br/>
            notizen.md<br/>
            paul_notizen.md<br/>
            praesentation_notizen.md<br/>
            technische_notizen.md
        "]

        root --> result
        result["result/"] --> result_files["... (28 files)"]

        root --> schemas
        schemas["schemas/"] --> schemas_files["
            types.py
        "]

        root --> statistics
        statistics["statistics/"] --> statistics_files["... (5 files)"]
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

Since a `requirements.txt` file is present, you can install all dependencies with a single command:
```bash
pip install -r requirements.txt
```

### Setup Guide
1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment Variables:**
    - Copy the example environment file: `cp .env.example .env`
    - Edit the `.env` file and add your API keys for services like Gemini, OpenAI, and your MongoDB connection string.

### Quick Startup
To run the application, start the Streamlit frontend:
```bash
streamlit run frontend/frontend.py
```
Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## 3. Use Cases & Commands
The primary use case for this agent is to accelerate the onboarding process for developers joining a new project. By providing the repository's Git URL, a developer can receive a detailed, structured, and easy-to-navigate documentation report within minutes.

**Primary Workflow:**
1.  **Launch the Application:** Run the main command `streamlit run frontend/frontend.py`.
2.  **Authenticate:** Log in through the Streamlit interface. The system uses a MongoDB backend for user management.
3.  **Configure Models & API Keys:** In the settings panel, select the desired Helper and Main LLM models and ensure the corresponding API keys are saved.
4.  **Submit Repository URL:** In the main chat interface, enter the full `https://github.com/...` URL of the repository you wish to analyze.
5.  **Generate Report:** The backend will start the analysis pipeline, providing real-time status updates in the UI.
6.  **Review Documentation:** Once complete, the final Markdown report is displayed in the chat window, ready for review, download, or feedback.

The system is designed to be fully interactive through its web UI, abstracting away the complex backend commands.

## 4. Architecture
*Architecture visualization is not available in this version.*

## 5. Code Analysis
### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into a Python module path. It first determines the relative path of the file with respect to the project's root directory, handling potential `ValueError` by falling back to the base filename. It then removes the '.py' extension if present and replaces path separators with dots. Finally, it specifically handles and removes the '.__init__' suffix to yield the canonical module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) of Python source code. Its primary purpose is to extract structured information about imports, functions, and classes within a given Python file. It builds a `schema` dictionary that categorizes these elements, including details like identifiers, docstrings, and source code segments. The visitor distinguishes between top-level functions and methods nested within classes, associating methods with their parent class.
*   **Instantiation:** The class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** The ASTVisitor class depends on the `ast` module for AST traversal and node manipulation, and implicitly relies on a `path_to_module` function for resolving module paths.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes the ASTVisitor instance by storing the provided source code, file path, and project root. It calculates the module path using an external helper function and sets up an empty schema dictionary to store discovered imports, functions, and classes. It also initializes an internal `_current_class` attribute to `None` for tracking the current class being visited.
    *   *Parameters:*
        - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
        - **source_code** (`str`): The raw source code string of the file being analyzed.
        - **file_path** (`str`): The absolute path to the file containing the source code.
        - **project_root** (`str`): The root directory of the project, used for module path calculation.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: ASTVisitor, source_code: str, file_path: str, project_root: str)`
        *   *Description:* The `__init__` method initializes the ASTVisitor instance by storing the provided source code, file path, and project root. It calculates the module path using an external helper function and sets up an empty schema dictionary to store discovered imports, functions, and classes. It also initializes an internal `_current_class` attribute to `None` for tracking the current class being visited.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **source_code** (`str`): The raw source code string of the file being analyzed.
            - **file_path** (`str`): The absolute path to the file containing the source code.
            - **project_root** (`str`): The root directory of the project, used for module path calculation.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self: ASTVisitor, node: ast.Import)`
        *   *Description:* This method is part of the `ast.NodeVisitor` pattern, specifically designed to handle `ast.Import` nodes. It iterates through each alias in the import node and appends the module name to the `imports` list within the `self.schema` dictionary. After processing the current node, it calls `self.generic_visit(node)` to continue traversing its children.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an import statement (e.g., `import os`).
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue AST traversal.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self: ASTVisitor, node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent `from ... import ...` statements. It iterates through the aliases in the node and constructs a fully qualified import string (e.g., `module.name`) which is then appended to the `imports` list in `self.schema`. It ensures that the traversal continues to child nodes by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a `from ... import ...` statement.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue AST traversal.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when an `ast.ImportFrom` node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self: ASTVisitor, node: ast.ClassDef)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions. It constructs a unique identifier for the class, extracts its name, docstring, and source code segment, along with its start and end line numbers. This information is then stored in a `class_info` dictionary, which is appended to the `classes` list within `self.schema`. The `_current_class` attribute is temporarily set to this `class_info` to allow nested methods to associate themselves with the parent class, and then reset to `None` after visiting children.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit`.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when an `ast.ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self: ASTVisitor, node: ast.FunctionDef)`
        *   *Description:* This method handles `ast.FunctionDef` nodes for both regular functions and methods. It checks if a `_current_class` is being visited. If so, it creates `method_context_info` for the method, including its identifier, name, arguments, docstring, and line numbers, appending it to the `method_context` of the `_current_class`. Otherwise, it treats it as a standalone function, creating `func_info` and appending it to `self.schema["functions"]`. It then calls `self.generic_visit(node)` to continue traversal.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit`.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when an `ast.FunctionDef` node is encountered during AST traversal, and is also called by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self: ASTVisitor, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is designed to handle `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation simply delegates the processing to the `visit_FunctionDef` method, treating async functions similarly to regular functions for the purpose of schema extraction.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.visit_FunctionDef`.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when an `ast.AsyncFunctionDef` node is encountered during AST traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process and analyze Python source code within a repository to construct a structured Abstract Syntax Tree (AST) schema. It provides functionality to parse individual Python files, extract their structural components (imports, functions, classes), and then integrate relationship data, such as function calls and class instantiations, into this schema. This class acts as a central component for generating a comprehensive, interconnected view of a codebase's structure and dependencies.
*   **Instantiation:** This class is not explicitly instantiated by any other components in the provided context.
*   **Dependencies:** This class does not have any external functional dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* This constructor initializes an instance of the ASTAnalyzer class. It currently performs no specific setup or attribute assignments, serving as a placeholder.
    *   *Parameters:* None
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: ASTAnalyzer, )`
        *   *Description:* This constructor initializes an instance of the ASTAnalyzer class. It currently performs no specific setup or attribute assignments, serving as a placeholder.
        *   *Parameters:* None
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self: ASTAnalyzer, full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates call relationship data (incoming and outgoing calls) into a pre-existing full schema of AST nodes. It iterates through files, functions, and classes within the schema, updating their respective 'context' fields with call information. For functions, it populates 'calls' and 'called_by' lists. For classes, it populates 'instantiated_by' and also calculates 'dependencies' by identifying calls made by class methods to entities outside the class itself.
        *   *Parameters:*
            - **full_schema** (`dict`): The comprehensive AST schema containing file, function, and class definitions.
            - **raw_relationships** (`dict`): A dictionary containing raw incoming and outgoing call relationships.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full_schema dictionary with integrated relationship data.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call any other functions or methods according to the provided context.
            - *Called By:* This method is not explicitly called by any other functions or methods according to the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self: ASTAnalyzer, files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to build a comprehensive AST schema. It filters for Python files, reads their content, and uses an ASTVisitor to parse the Abstract Syntax Tree, extracting information about imports, functions, and classes. It handles potential SyntaxError or ValueError during parsing and constructs a full_schema dictionary representing the repository's AST structure.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though not directly used in the provided snippet.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary containing the AST schema for all processed Python files in the repository.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call any other functions or methods according to the provided context.
            - *Called By:* This method is not explicitly called by any other functions or methods according to the provided context.

---
### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing the file-level import dependencies within a given Python file. It initializes a NetworkX directed graph and uses a `FileDependencyGraph` visitor to traverse the provided Abstract Syntax Tree (AST). The visitor populates a dictionary of import dependencies, which are then translated into nodes and edges in the NetworkX graph. The resulting graph illustrates which files import other files.
*   **Parameters:**
    - **filename** (`str`): The name of the file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed for dependencies.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It iterates through all Python files, parses each file's content into an Abstract Syntax Tree (AST), and then uses a helper function to build a dependency graph for that individual file. Finally, it aggregates all these file-level graphs into a single, global NetworkX directed graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to extract Python files and analyze their dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependencies between all Python files found in the repository.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and converts it into an absolute `pathlib.Path` object. The function then recursively searches for all files ending with ".py" within this root path. For each discovered Python file, it calculates its path relative to the initial root directory. Finally, it returns a list of these relative `pathlib.Path` objects.
*   **Parameters:**
    - **directory** (`str`): The string path to the root directory from which to start the recursive search for Python files.
*   **Returns:**
    - **all_files** (`list[pathlib.Path]`): A list of `pathlib.Path` objects, where each object represents a Python file found within the specified directory or its subdirectories, with paths relative to the input `directory`.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends NodeVisitor to analyze Python source code files and build a graph of their import dependencies. It identifies both direct and relative imports, resolving relative paths to concrete module names within a given repository structure. The class maintains a dictionary, import_dependencies, to store which files import which modules. Its primary role is to systematically traverse the Abstract Syntax Tree (AST) of a Python file and extract all import relationships, making it a core component for understanding code structure and inter-file dependencies.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** The class relies on ast module components like NodeVisitor, Import, ImportFrom, Assign, Name, FunctionDef, ClassDef, literal_eval, parse, walk, as well as keyword.iskeyword and pathlib.Path for file system interactions. It also uses get_all_temp_files (presumably an external utility) for file discovery.
*   **Constructor:**
    *   *Description:* This constructor initializes the FileDependencyGraph instance by setting the filename and repo_root attributes. These attributes are crucial for identifying the file being analyzed and the base directory for resolving file paths.
    *   *Parameters:*
        - **filename** (`str`): The name of the file for which dependencies are being analyzed.
        - **repo_root** (`str`): The root directory of the repository, used for resolving file paths.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: FileDependencyGraph, filename: str, repo_root: str)`
        *   *Description:* This constructor initializes the FileDependencyGraph instance by setting the filename and repo_root attributes. These attributes are crucial for identifying the file being analyzed and the base directory for resolving file paths.
        *   *Parameters:*
            - **filename** (`str`): The name of the file for which dependencies are being analyzed.
            - **repo_root** (`str`): The root directory of the repository, used for resolving file paths.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self: FileDependencyGraph, node: ImportFrom)`
        *   *Description:* This method is responsible for resolving relative import statements (e.g., from .. import name). It determines the actual module or symbol names that are being imported by navigating the file system relative to the current file and repository root. It checks for both module files (.py) and symbols exported via __init__.py files. If no valid module or symbol can be resolved, it raises an ImportError.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST ImportFrom node representing the relative import statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:** 
            - *Calls:* This method calls get_all_temp_files to get all files in the repository, Path for path manipulation, iskeyword to check if a name is a Python keyword, module_file_exists to check for module files, init_exports_symbol to check for symbols exported by __init__.py files, parse to parse __init__.py content, walk to traverse AST nodes, and literal_eval to evaluate __all__ lists.
            - *Called By:* This method is called by visit_ImportFrom when handling relative imports.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self: FileDependencyGraph, node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* This method processes Import and ImportFrom AST nodes to record import dependencies. It iterates through the aliases in the import statement and adds them to the import_dependencies dictionary, mapping the current filename to a set of imported module names. It can optionally take a base_name to explicitly specify the dependency. After processing, it calls self.generic_visit(node) to continue AST traversal.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing an import statement (either Import or ImportFrom).
            - **base_name** (`str | None`): An optional base name to use for the dependency, typically used for from ... import ... statements where the module name is already resolved.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls self.generic_visit to continue the AST traversal.
            - *Called By:* This method is called by visit_ImportFrom after resolving module names.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self: FileDependencyGraph, node: ImportFrom)`
        *   *Description:* This method is an AST visitor specifically for ImportFrom nodes. It extracts the module name from the import statement. If it's a direct import (e.g., from a.b.c import d), it takes the last part of the module name (c) as the dependency. If it's a relative import (e.g., from .. import name), it uses the _resolve_module_name helper to determine the actual module names. It then delegates to visit_Import to record these dependencies. Error handling for failed relative import resolution is included.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST ImportFrom node to be visited and processed.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls self.visit_Import to record dependencies, self._resolve_module_name to resolve relative imports, and self.generic_visit to continue the AST traversal.
            - *Called By:* This method is implicitly called by the NodeVisitor framework when traversing an AST that contains ImportFrom nodes.

---
### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** The main_orchestrator function serves as a testing and demonstration loop for the LLMHelper class. It defines and validates dummy data representing pre-computed analyses for several Python functions, such as 'add_item', 'check_stock', and 'generate_report', using Pydantic models like FunctionAnalysisInput and FunctionAnalysis. The function then instantiates an LLMHelper object, simulating the process of generating documentation for these functions. Finally, it aggregates the results into a dictionary and prints the final generated documentation in JSON format.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs), such as Google Gemini, OpenAI, and Ollama, to generate structured documentation for Python functions and classes. It handles LLM initialization, loads specific system prompts for different analysis types, and manages batch processing with rate limiting. The class ensures that LLM outputs conform to predefined Pydantic schemas (FunctionAnalysis, ClassAnalysis), facilitating robust data validation and integration into a larger documentation generation system.
*   **Instantiation:** The class does not have any explicit instantiation points listed in the provided context.
*   **Dependencies:** The class does not have any explicit external dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* This constructor initializes the LLMHelper class by setting up the API key, loading system prompts from specified file paths for function and class analysis, and configuring the underlying Language Model (LLM) based on the model_name. It supports various LLM providers like Google Gemini, OpenAI, custom APIs via SCADSLLM_URL, or Ollama, and then wraps them with structured output capabilities for FunctionAnalysis and ClassAnalysis Pydantic schemas. It also calls _configure_batch_settings to set an appropriate batch size for API calls.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **function_prompt_path** (`str`): The file path to the system prompt used for function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt used for class analysis.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
        - **base_url** (`str | None`): An optional base URL for custom or Ollama LLM endpoints.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: LLMHelper, api_key: str, function_prompt_path: str, class_prompt_path: str, model_name: str, base_url: str)`
        *   *Description:* This constructor initializes the LLMHelper class by setting up the API key, loading system prompts from specified file paths for function and class analysis, and configuring the underlying Language Model (LLM) based on the model_name. It supports various LLM providers like Google Gemini, OpenAI, custom APIs via SCADSLLM_URL, or Ollama, and then wraps them with structured output capabilities for FunctionAnalysis and ClassAnalysis Pydantic schemas. It also calls _configure_batch_settings to set an appropriate batch size for API calls.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the LLMHelper.
            - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
            - **function_prompt_path** (`str`): The file path to the system prompt used for function analysis.
            - **class_prompt_path** (`str`): The file path to the system prompt used for class analysis.
            - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
            - **base_url** (`str | None`): An optional base URL for custom or Ollama LLM endpoints.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self: LLMHelper, model_name: str)`
        *   *Description:* This private method sets the batch_size attribute of the LLMHelper instance based on the provided model_name. It uses a series of conditional statements to assign specific batch sizes optimized for different LLM models, such as various Gemini, Llama, and GPT versions. For unknown models or custom API models, it assigns a default or a large batch size, logging a warning for unconfigured models. The purpose is to optimize API call efficiency and respect rate limits for different LLM providers.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method uses logging.warning to report unknown models.
            - *Called By:* This method is called by the __init__ method of the LLMHelper class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self: LLMHelper, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* This method takes a list of FunctionAnalysisInput objects, converts them into JSON payloads, and then uses the configured function_llm to generate structured documentation for each function in batches. It iterates through the inputs, sending BATCH_SIZE conversations to the LLM concurrently, and includes a waiting period between batches to respect API rate limits. Error handling is implemented to catch exceptions during API calls, appending None for failed items to maintain order. The method ultimately returns a list of FunctionAnalysis objects or None for failed generations.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary data for generating documentation for a single function.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of FunctionAnalysis objects, where each object represents the structured documentation for a function, or None if the generation failed for that specific function.
        *   **Usage:** 
            - *Calls:* This method calls json.dumps, len, logging.info, logging.error, time.sleep, and self.function_llm.batch.
            - *Called By:* The input context does not specify any explicit callers for this method.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self: LLMHelper, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* This method is designed to generate structured documentation for a batch of classes. It takes a list of ClassAnalysisInput objects, converts them into JSON, and then processes them in batches using the class_llm configured for structured output. Similar to generate_for_functions, it manages API calls with a defined BATCH_SIZE and WAITING_TIME to handle rate limits, logs progress and errors, and returns a list of ClassAnalysis objects or None for any failed generations.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary data for generating documentation for a single class.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of ClassAnalysis objects, where each object represents the structured documentation for a class, or None if the generation failed for that specific class.
        *   **Usage:** 
            - *Calls:* This method calls json.dumps, len, logging.info, logging.error, time.sleep, and self.class_llm.batch.
            - *Called By:* The input context does not specify any explicit callers for this method.

---
### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a central interface for interacting with various Large Language Models (LLMs), abstracting away the specifics of different providers like Google Generative AI, OpenAI-compatible APIs, and Ollama. It handles the initialization of the appropriate LLM client based on configuration, loads a system prompt from a file, and provides methods for both single-shot and streaming interactions with the chosen model. This class is crucial for integrating diverse LLM capabilities into an application, offering flexibility in model choice and interaction patterns.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** The class depends on external libraries for LLM interaction, specifically langchain_google_genai.ChatGoogleGenerativeAI, langchain_ollama.ChatOllama, langchain_openai.ChatOpenAI, langchain.messages.HumanMessage, langchain.messages.SystemMessage, and the logging module.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the MainLLM class by setting up the API key, loading a system prompt from a specified file path, and configuring the appropriate LangChain LLM client based on the provided model name. It supports Google Generative AI (Gemini/GPT), custom OpenAI-compatible APIs (via SCADSLLM_URL), and Ollama models (via OLLAMA_BASE_URL or a provided base_url). It raises a ValueError if the API key is missing or if a required environment variable for custom models is not set, and a FileNotFoundError if the prompt file cannot be found.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **prompt_file_path** (`str`): The file path to a text file containing the system prompt for the LLM.
        - **model_name** (`str`): The name of the LLM model to be used (e.g., 'gemini-2.5-pro', 'gpt-4', 'llama2'). Defaults to 'gemini-2.5-pro'.
        - **base_url** (`str`): An optional base URL for custom LLM API endpoints, used if model_name does not match predefined patterns. Defaults to None.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: MainLLM, api_key: str, prompt_file_path: str, model_name: str, base_url: str)`
        *   *Description:* The __init__ method initializes the MainLLM class by setting up the API key, loading a system prompt from a specified file path, and configuring the appropriate LangChain LLM client based on the provided model name. It supports Google Generative AI (Gemini/GPT), custom OpenAI-compatible APIs (via SCADSLLM_URL), and Ollama models (via OLLAMA_BASE_URL or a provided base_url). It raises a ValueError if the API key is missing or if a required environment variable for custom models is not set, and a FileNotFoundError if the prompt file cannot be found.
        *   *Parameters:*
            - **self** (`MainLLM`): The MainLLM instance.
            - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
            - **prompt_file_path** (`str`): The file path to a text file containing the system prompt for the LLM.
            - **model_name** (`str`): The name of the LLM model to be used (e.g., 'gemini-2.5-pro', 'gpt-4', 'llama2'). Defaults to 'gemini-2.5-pro'.
            - **base_url** (`str`): An optional base URL for custom LLM API endpoints, used if model_name does not match predefined patterns. Defaults to None.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self: MainLLM, user_input: str)`
        *   *Description:* This method sends a user input to the configured LLM for a single, non-streaming response. It constructs a list of messages, including the pre-loaded system prompt and the user's query, and then invokes the LLM. The method logs the call status and returns the content of the LLM's response. In case of an error during the LLM call, it logs the exception and returns None.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:*
            - **content** (`str`): The textual content of the LLM's response.
            - **None** (`None`): Returns None if an error occurs during the LLM call.
        *   **Usage:** 
            - *Calls:* This method calls SystemMessage, HumanMessage, self.llm.invoke, logging.info, and logging.error.
            - *Called By:* This method is not explicitly called by other methods within the provided context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self: MainLLM, user_input: str)`
        *   *Description:* This method interacts with the configured LLM to stream its response back to the caller, yielding each chunk of content as it becomes available. It prepares the system and human messages, then initiates a streaming call to the LLM. This allows for real-time processing of the LLM's output. If an exception occurs during the streaming process, it logs the error and yields an error message string.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM for streaming.
        *   *Returns:*
            - **chunk.content** (`str`): Yields individual content chunks from the LLM's streaming response.
            - **error_message** (`str`): Yields an error message string if an exception occurs during the streaming call.
        *   **Usage:** 
            - *Calls:* This method calls SystemMessage, HumanMessage, self.llm.stream, logging.info, and logging.error.
            - *Called By:* This method is not explicitly called by other methods within the provided context.

---
### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract comprehensive project information from common project files such as README, pyproject.toml, and requirements.txt. It consolidates this information into a structured dictionary, providing details on project overview, key features, tech stack, status, installation instructions, and dependencies. The class prioritizes information sources, with pyproject.toml taking precedence for core metadata, followed by requirements.txt for dependencies, and README for broader descriptive content.
*   **Instantiation:** This class is not explicitly instantiated by any other component in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjektInfoExtractor instance by setting a default placeholder string, 'Information not found'. It then creates an internal dictionary, `self.info`, which is pre-populated with this placeholder for various project details, including project overview (title, description, status, features, tech stack) and installation information (dependencies, setup guide, quick start guide).
    *   *Parameters:* None
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: ProjektInfoExtractor, )`
        *   *Description:* The constructor initializes the ProjektInfoExtractor instance by setting a default placeholder string, 'Information not found'. It then creates an internal dictionary, `self.info`, which is pre-populated with this placeholder for various project details, including project overview (title, description, status, features, tech stack) and installation information (dependencies, setup guide, quick start guide).
        *   *Parameters:* None
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self: ProjektInfoExtractor, content: str)`
        *   *Description:* This private helper method is responsible for sanitizing input string content by removing null bytes (`\x00`). Null bytes can inadvertently appear in text due to encoding mismatches, such as reading a UTF-16 encoded file as UTF-8. The method ensures that the content is clean and safe for further processing, returning an empty string if the input content is empty.
        *   *Parameters:*
            - **content** (`str`): The string content that needs to be cleaned of null bytes.
        *   *Returns:*
            - **cleaned_content** (`str`): The input string with all null bytes removed.
        *   **Usage:** 
            - *Calls:* This method does not make any external calls.
            - *Called By:* This method is called by _parse_readme, _parse_toml, and _parse_requirements.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self: ProjektInfoExtractor, patterns: List[str], dateien: List[Any])`
        *   *Description:* This private helper method searches through a provided list of file objects to find one whose path matches any of the specified patterns. The search is performed case-insensitively to accommodate varied file naming conventions. It iterates through each file and then through each pattern, returning the first file object that satisfies any of the pattern matches.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of string patterns (e.g., file names or extensions) to match against file paths.
            - **dateien** (`List[Any]`): A list of file-like objects, where each object is expected to have a 'path' attribute.
        *   *Returns:*
            - **matching_file** (`Optional[Any]`): The first file object found that matches any of the given patterns, or None if no match is found.
        *   **Usage:** 
            - *Calls:* This method does not make any external calls.
            - *Called By:* This method is called by extrahiere_info.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self: ProjektInfoExtractor, inhalt: str, keywords: List[str])`
        *   *Description:* This private method is designed to extract text content that appears directly under a Markdown level 2 heading (e.g., '## Section Title') matching one of the specified keywords. It constructs a regular expression dynamically from the provided keywords to locate the heading. The method then captures all subsequent text until another level 2 heading or the end of the document is encountered, performing a case-insensitive and multi-line search.
        *   *Parameters:*
            - **inhalt** (`str`): The Markdown content string from which to extract a section.
            - **keywords** (`List[str]`): A list of keywords to match against the Markdown heading titles.
        *   *Returns:*
            - **extracted_section** (`Optional[str]`): The extracted text content of the section, or None if no matching section is found.
        *   **Usage:** 
            - *Calls:* This method calls re.escape, re.compile, and re.search.
            - *Called By:* This method is called by _parse_readme.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self: ProjektInfoExtractor, inhalt: str)`
        *   *Description:* This private method processes the content of a README file to extract various project details and update the internal `self.info` dictionary. It begins by cleaning the input content to remove any null bytes. The method then uses regular expressions to identify the project title (from a level 1 heading) and a general description. For specific sections like 'Key Features', 'Tech Stack', 'Status', 'Installation', and 'Quick Start', it utilizes the `_extrahiere_sektion_aus_markdown` helper method with predefined keyword lists.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the README file to be parsed.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls self._clean_content, re.search, and self._extrahiere_sektion_aus_markdown.
            - *Called By:* This method is called by extrahiere_info.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self: ProjektInfoExtractor, inhalt: str)`
        *   *Description:* This private method parses the content of a `pyproject.toml` file to extract project metadata. It first cleans the input content. Before parsing, it checks if the `tomllib` module is available, issuing a warning and returning if it is not. If `tomllib` is present, it attempts to load the TOML data and then extracts the project's 'name', 'description', and 'dependencies' from the `[project]` table, updating the `self.info` dictionary. Error handling is included for `tomllib.TOMLDecodeError` during parsing.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the pyproject.toml file to be parsed.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls self._clean_content, tomllib.loads, and data.get.
            - *Called By:* This method is called by extrahiere_info.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self: ProjektInfoExtractor, inhalt: str)`
        *   *Description:* This private method parses the content of a `requirements.txt` file to identify and extract project dependencies. It first cleans the input content to ensure data integrity. The method only populates the 'dependencies' field in the `self.info` dictionary if this information has not already been found from a higher-priority source, such as a `pyproject.toml` file. It processes the file line by line, filtering out empty lines and comments, and then stores the valid dependency strings.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the requirements.txt file to be parsed.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls self._clean_content.
            - *Called By:* This method is called by extrahiere_info.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self: ProjektInfoExtractor, dateien: List[Any], repo_url: str)`
        *   *Description:* This public method orchestrates the entire process of extracting project information from various file sources. It first identifies relevant project files (README, pyproject.toml, requirements.txt) from a given list of `dateien` using the `_finde_datei` helper. It then proceeds to parse these files in a prioritized order: `pyproject.toml` for core metadata, `requirements.txt` for dependencies (if not already found), and `README` for broader descriptive content. Finally, it formats the extracted dependencies and, if a project title is still missing, attempts to derive one from the provided repository URL.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have 'path' and 'content' attributes, representing project files.
            - **repo_url** (`str`): The URL of the repository, used as a fallback to derive the project title if no other source provides it.
        *   *Returns:*
            - **project_info** (`Dict[str, Any]`): A dictionary containing all extracted and consolidated project information.
        *   **Usage:** 
            - *Calls:* This method calls self._finde_datei, self._parse_toml, self._parse_requirements, self._parse_readme, os.path.basename, and repo_url.removesuffix.
            - *Called By:* This method is not explicitly called by any other method in the provided context.

---
### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and an output file path, then generates a DOT file with 'safe' node names. It creates a copy of the input graph and renames all nodes to generic identifiers (e.g., 'n0', 'n1') to prevent issues with special characters in the DOT format. The original node names are preserved by assigning them as 'label' attributes to the newly named nodes. Finally, the modified graph is written to the specified output path in DOT format.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph object to be processed and converted into a DOT file.
    - **out_path** (`str`): The file path where the DOT representation of the graph will be saved.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** This function constructs a directed call graph for a given Git repository. It first identifies all user-defined functions across all Python files within the repository by parsing their Abstract Syntax Trees (ASTs). Subsequently, it iterates through these files again to identify call relationships between functions. The final graph, represented as a networkx.DiGraph, includes only those edges where both the calling and called functions are part of the identified user-defined functions, effectively filtering out external or library calls.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which to extract Python files and build the call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the call relationships between user-defined functions within the repository, filtered to include only self-written functions.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST (Abstract Syntax Tree) visitor designed to construct a call graph for a given Python source file. It traverses the AST, identifying function definitions, class definitions, import statements, and function calls. By maintaining context such as the current function and class, and resolving names through local definitions and import mappings, it builds a directed graph representing the 'caller calls callee' relationships within the code. This class is fundamental for static analysis to understand the flow of execution and dependencies between different parts of a codebase.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its context, but it relies on the `ast` module for parsing Python code and `networkx` for graph manipulation.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes a new CallGraph instance. It sets up various internal state variables and data structures crucial for building the call graph, including the filename being analyzed, the current function and class context, dictionaries for local definitions and import mappings, a NetworkX directed graph to store the call relationships, a set for tracking all identified functions, and a dictionary to store edges (caller-callee relationships).
    *   *Parameters:*
        - **filename** (`str`): The path or name of the source file being analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: CallGraph, filename: str)`
        *   *Description:* The `__init__` method initializes a new CallGraph instance. It sets up various internal state variables and data structures crucial for building the call graph, including the filename being analyzed, the current function and class context, dictionaries for local definitions and import mappings, a NetworkX directed graph to store the call relationships, a set for tracking all identified functions, and a dictionary to store edges (caller-callee relationships).
        *   *Parameters:*
            - **filename** (`str`): The path or name of the source file being analyzed.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self: CallGraph, node: ast.AST)`
        *   *Description:* This private helper method recursively traverses an Abstract Syntax Tree (AST) node to extract the full dotted name components of a function or method call. It specifically handles `ast.Call`, `ast.Name`, and `ast.Attribute` nodes to reconstruct the hierarchical name of the called entity. The method returns a list of strings, where each string is a component of the name, such as `['pkg', 'mod', 'Class', 'method']`, providing a structured representation of the call target.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a call, name, or attribute access.
        *   *Returns:*
            - **parts** (`list[str]`): A list of string components forming the full name of the called entity.
        *   **Usage:** 
            - *Calls:* This method calls itself recursively to traverse the AST node structure.
            - *Called By:* This method is called by `visit_Call`.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self: CallGraph, callee_nodes: list[list[str]])`
        *   *Description:* This private method takes a list of potential callee name components and resolves them to their fully qualified names within the context of the current file. It prioritizes resolution by checking `self.local_defs` for local function or class definitions, then `self.import_mapping` for imported modules or functions. If neither yields a direct match, it constructs a full name using the `filename` and `current_class`. This comprehensive resolution ensures accurate identification of call targets regardless of their origin or scope.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list where each inner list represents the name components of a potential callee.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of fully resolved, qualified names for the callees.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other methods but accesses instance attributes like `self.local_defs`, `self.import_mapping`, `self.current_class`, and `self.filename` for name resolution.
            - *Called By:* This method is called by `visit_Call`.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self: CallGraph, basename: str, class_name: str | None)`
        *   *Description:* This private utility method constructs a fully qualified name for a function or method based on its base name and an optional class name. It prepends the `filename` and, if provided, the `class_name` to the given `basename`. This standardization is essential for creating unique and consistent identifiers for all callable entities within the call graph, ensuring proper tracking and referencing.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`str | None`): The name of the class if the entity is a method; otherwise, it is None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name of the function or method.
        *   **Usage:** 
            - *Calls:* This method does not call any other methods.
            - *Called By:* This method is called by `visit_FunctionDef`.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self: CallGraph, )`
        *   *Description:* This private method determines the identifier of the currently active caller within the AST traversal context. If `self.current_function` is set, it returns that value, indicating a call from within a specific function. Otherwise, it constructs a default identifier based on the `filename` (e.g., `<filename>`) or `<global-scope>` if no filename is available, signifying a call originating from the global scope of the module.
        *   *Parameters:* None
        *   *Returns:*
            - **caller_identifier** (`str`): The identifier of the current caller, either a function's full name or a scope indicator.
        *   **Usage:** 
            - *Calls:* This method does not call any other methods.
            - *Called By:* This method is called by `visit_Call`.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self: CallGraph, node: ast.Import)`
        *   *Description:* This method, part of the `ast.NodeVisitor` pattern, processes `ast.Import` nodes, which represent `import module_name [as alias]` statements. It iterates through the imported modules and their aliases, populating `self.import_mapping` to track how modules are referenced within the code. This mapping is crucial for correctly resolving fully qualified names of imported functions or classes later during call graph construction. After processing the import, it calls `generic_visit` to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an `import` statement.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal.
            - *Called By:* This method is invoked by the AST traversal mechanism when an `ast.Import` node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self: CallGraph, node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent `from module import name [as alias]` statements. It extracts the module name and the specific names imported, along with any aliases. It updates `self.import_mapping` to correctly link the imported names to their originating module or specific imported object, facilitating the accurate resolution of call targets. After processing the import, it calls `generic_visit` to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a `from ... import ...` statement.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal.
            - *Called By:* This method is invoked by the AST traversal mechanism when an `ast.ImportFrom` node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self: CallGraph, node: ast.ClassDef)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which define classes. It manages the `self.current_class` attribute to keep track of the class context during AST traversal. Before visiting the class's body, it saves the previous class context and sets `self.current_class` to the current class's name. After the visit, it restores the previous class context. This ensures that methods defined within a class are correctly associated with that class for proper name resolution.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal into the class body.
            - *Called By:* This method is invoked by the AST traversal mechanism when an `ast.ClassDef` node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self: CallGraph, node: ast.FunctionDef)`
        *   *Description:* This method processes `ast.FunctionDef` nodes for regular function definitions. It constructs the full qualified name of the function using `_make_full_name`, registers this name in `self.local_defs` for local resolution, and adds it as a node to the `self.graph`. It manages `self.current_function` to maintain the current function context during traversal, ensuring that calls made within this function are correctly attributed. Finally, it adds the function to `self.function_set` and calls `generic_visit` to traverse the function's body.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self._make_full_name`, `self.graph.add_node`, and `self.generic_visit`.
            - *Called By:* This method is invoked by the AST traversal mechanism when an `ast.FunctionDef` node is encountered, and also by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self: CallGraph, node: ast.AsyncFunctionDef)`
        *   *Description:* This method processes `ast.AsyncFunctionDef` nodes, which define asynchronous functions. It delegates the actual processing of these nodes to `visit_FunctionDef`. This approach treats asynchronous functions similarly to regular functions for the primary purpose of call graph construction, ensuring that both synchronous and asynchronous callable entities are correctly identified, named, and added to the call graph without redundant logic.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.visit_FunctionDef`.
            - *Called By:* This method is invoked by the AST traversal mechanism when an `ast.AsyncFunctionDef` node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self: CallGraph, node: ast.Call)`
        *   *Description:* This method is invoked for every `ast.Call` node, representing a function or method call within the source code. It first identifies the `caller` using `_current_caller`, then extracts the `callee` name components using `_recursive_call`, and finally resolves these components to fully qualified names using `_resolve_all_callee_names`. The resolved callees are then added as edges from the `caller` in the `self.edges` dictionary, effectively building the call graph relationships. After processing the call, it continues the AST traversal with `generic_visit`.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self._current_caller`, `self._recursive_call`, `self._resolve_all_callee_names`, and `self.generic_visit`.
            - *Called By:* This method is invoked by the AST traversal mechanism when an `ast.Call` node is encountered.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self: CallGraph, node: ast.If)`
        *   *Description:* This method processes `ast.If` nodes, handling conditional statements. It includes special logic to identify and manage the `if __name__ == "__main__":` block, which typically serves as a module's entry point. When this specific condition is met, it temporarily sets `self.current_function` to `<main_block>` to correctly attribute any calls made within this block. For all other `if` statements, it simply continues the generic AST traversal, ensuring all code paths are visited.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing an `if` statement.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal.
            - *Called By:* This method is invoked by the AST traversal mechanism when an `ast.If` node is encountered.

---
### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content: str)`
*   **Description:** The `wrap_cdata` function takes a string `content` as input and encapsulates it within XML CDATA tags. It constructs an f-string that includes the literal `<![CDATA[` and `]]>` delimiters, with the provided content inserted between them, also adding newline characters before and after the content. This operation is designed to ensure that the enclosed content is treated as character data by an XML parser, preventing interpretation of special characters as markup.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped within CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A new string containing the original content enclosed within CDATA tags.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs: list, image_list: list)`
*   **Description:** This function processes a list of output objects, typically from a notebook execution, to extract their content. It iterates through each output, identifying its type to determine how to handle its data. For display or execution results, it prioritizes image data (PNG then JPEG), decoding Base64 strings and storing their metadata in a provided `image_list`, replacing them with XML-like placeholders. If no image is found, it extracts plain text. Stream outputs have their text directly appended, while error outputs are formatted into a string containing the error name and value. The function aggregates all extracted content into a list of strings.
*   **Parameters:**
    - **outputs** (`list`): A list of output objects, likely from a notebook execution, each containing different types of data such as display data, execution results, streams, or errors.
    - **image_list** (`list`): A mutable list that will be populated with dictionaries containing metadata for extracted images, including their MIME type and Base64 data, as they are processed.
*   **Returns:**
    - **extracted_xml_snippets** (`list[str]`): A list of strings, where each string represents extracted text content, an XML-like placeholder for an image, or a formatted error message from the processed outputs.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type: str)`
*   **Description:** This function processes an image identified by its MIME type. It expects the image data to be present in a `data` object (from an outer scope) as a base64 encoded string. The function cleans the base64 string by removing newline characters, stores the processed image data along with its MIME type in an `image_list` (also from an outer scope), and returns a formatted placeholder string. If an error occurs during processing, it returns an error message string. If the specified MIME type is not found in the `data` object, it returns `None`.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed, used as a key to retrieve data from the external `data` object.
*   **Returns:**
    - **image_placeholder_or_error** (`str`): A formatted string representing an image placeholder if successful, or an error message string if an exception occurs during processing.
    - **none_if_not_found** (`None`): Returns None if the specified mime_type is not found in the external `data` object.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content: str)`
*   **Description:** This function takes the raw content of a Jupyter notebook as a string and converts it into an XML representation. It processes each cell, categorizing them as markdown or code. Markdown cell content is directly embedded, while code cell source is wrapped in CDATA. If code cells have outputs, these are also processed, potentially extracting images, and then wrapped in CDATA within an output cell tag. The function handles parsing errors by returning a specific error message.
*   **Parameters:**
    - **file_content** (`str`): The raw string content of a Jupyter notebook file, expected to be in JSON format.
*   **Returns:**
    - **xml_output** (`str`): A string containing the concatenated XML representation of the notebook cells, or an error message if parsing fails.
    - **extracted_images** (`list`): A list of extracted image data (e.g., base64 encoded strings) found within the notebook outputs.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files: list)`
*   **Description:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It filters the input `repo_files` to select only those ending with '.ipynb'. For each identified notebook, it logs its path and then invokes an external conversion utility, `convert_notebook_to_xml`, to transform the notebook's content into XML and extract any embedded images. The function then compiles these conversion results, mapping each notebook's path to its generated XML and images. Finally, it returns a dictionary containing all the processed XML outputs and extracted images.
*   **Parameters:**
    - **repo_files** (`List[Any]`): An iterable collection of file-like objects, where each object is expected to have a 'path' attribute (string) for file identification and a 'content' attribute (string or bytes) representing the file's data.
*   **Returns:**
    - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the paths (string) of the processed notebook files. Each value is another dictionary containing 'xml' (string, the converted XML content) and 'images' (list, extracted image data) for that notebook.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, designed for efficient and lazy access to its metadata and content. It initializes with a file path and a Git tree object, then provides properties to lazily load the Git blob, the decoded file content, and its size. The class also includes utility methods for basic content analysis, string representation, and serialization into a dictionary format.
*   **Instantiation:** This class is not explicitly instantiated by other components based on the provided context.
*   **Dependencies:** This class does not have explicit external dependencies based on the provided context.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object by storing the file's path and the Git Tree object from which it originates. It sets up internal attributes for the Git blob, content, and size to None, indicating they are to be lazy-loaded upon first access.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: RepoFile, file_path: str, commit_tree: git.Tree)`
        *   *Description:* Initializes a RepoFile object by storing the file's path and the Git Tree object from which it originates. It sets up internal attributes for the Git blob, content, and size to None, indicating they are to be lazy-loaded upon first access.
        *   *Parameters:*
            - **self** (`RepoFile`): The RepoFile instance.
            - **file_path** (`str`): The path to the file within the repository.
            - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`blob`**
        *   *Signature:* `def blob(self: RepoFile, )`
        *   *Description:* This property provides lazy loading for the Git blob object corresponding to the file. It checks if the internal `_blob` attribute is already loaded; if not, it attempts to retrieve the blob from the `_tree` using the stored `path`. If the file is not found within the commit tree, it raises a `FileNotFoundError`.
        *   *Parameters:* None
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`content`**
        *   *Signature:* `def content(self: RepoFile, )`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It checks if the internal `_content` attribute is already loaded; if not, it accesses the `blob` property to obtain the Git blob, reads its data stream, and decodes it using UTF-8 with error handling set to 'ignore'.
        *   *Parameters:* None
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`size`**
        *   *Signature:* `def size(self: RepoFile, )`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the internal `_size` attribute is already loaded; if not, it accesses the `blob` property to obtain the Git blob and retrieves its `size` attribute, which represents the file's size.
        *   *Parameters:* None
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self: RepoFile, )`
        *   *Description:* This method serves as an example analysis function, calculating the total number of words in the file's content. It retrieves the file's content via the `content` property, splits the string by whitespace, and returns the count of the resulting words.
        *   *Parameters:* None
        *   *Returns:*
            - **word_count** (`int`): The total number of words in the file content.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self: RepoFile, )`
        *   *Description:* This special method provides a developer-friendly string representation of the RepoFile object. It returns a string that includes the object type and the file's path, which is useful for debugging and logging purposes.
        *   *Parameters:* None
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self: RepoFile, include_content: bool)`
        *   *Description:* This method serializes the RepoFile object into a dictionary format, providing structured metadata about the file. It includes the file's path, its base name, size, and type. Optionally, the file's content can be included in the dictionary if the `include_content` parameter is set to True.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether the file's content should be included in the returned dictionary. Defaults to False.
        *   *Returns:*
            - **file_data** (`dict`): A dictionary containing metadata about the file, optionally including its content.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with Git repositories programmatically. It handles the cloning of a remote repository into a temporary local directory, offers methods to retrieve all files as RepoFile objects, and can generate a hierarchical tree structure of the repository's contents. It also implements the context manager protocol for automatic cleanup of the temporary directory, ensuring resources are properly released.
*   **Instantiation:** This class is not explicitly instantiated by any known components in the provided context.
*   **Dependencies:** The class depends on `tempfile` for temporary directory management, `git.Repo` and `git.GitCommandError` from the GitPython library for Git operations, and `logging` for informational messages.
*   **Constructor:**
    *   *Description:* The constructor initializes a GitRepository object by cloning the specified Git repository URL into a newly created temporary directory. It sets up instance attributes for the repository URL, the temporary directory path, the GitPython Repo object, the latest commit, and the commit tree. It includes error handling for cloning failures, ensuring the temporary directory is cleaned up if an error occurs.
    *   *Parameters:*
        - **repo_url** (`string`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: GitRepository, repo_url: str)`
        *   *Description:* The constructor initializes a GitRepository object by cloning the specified Git repository URL into a newly created temporary directory. It sets up instance attributes for the repository URL, the temporary directory path, the GitPython Repo object, the latest commit, and the commit tree. It includes error handling for cloning failures, ensuring the temporary directory is cleaned up if an error occurs.
        *   *Parameters:*
            - **repo_url** (`string`): The URL of the Git repository to be cloned.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self: GitRepository, )`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It utilizes the GitPython library's `git.ls_files()` command to obtain a list of file paths. For each path, it instantiates a `RepoFile` object and stores these objects in the `self.files` attribute, making them available for further processing.
        *   *Parameters:* None
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances, each representing a file within the repository.
        *   **Usage:** 
            - *Calls:* This method calls `self.repo.git.ls_files()` to list files and `RepoFile` to create file objects.
            - *Called By:* This method is called by `get_file_tree` if `self.files` is empty.
    *   **`close`**
        *   *Signature:* `def close(self: GitRepository, )`
        *   *Description:* This method is responsible for cleaning up resources by deleting the temporary directory where the Git repository was cloned. It prints a message indicating the deletion and then sets the `self.temp_dir` attribute to `None` to mark the directory as removed.
        *   *Parameters:* None
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other methods or functions, but it interacts with the file system implicitly by deleting the temporary directory.
            - *Called By:* This method is called by the `__init__` method in case of a cloning error and by the `__exit__` context manager method.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self: GitRepository, )`
        *   *Description:* This special method enables the GitRepository object to function as a context manager. When the object is used in a `with` statement, this method is implicitly called and simply returns the instance itself, allowing access to its methods and attributes within the context.
        *   *Parameters:* None
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository object itself.
        *   **Usage:** 
            - *Calls:* This method does not call any other methods or functions.
            - *Called By:* This method is implicitly called when the `GitRepository` object is used in a `with` statement.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self: GitRepository, exc_type: type, exc_val: Exception, exc_tb: traceback)`
        *   *Description:* This special method is part of the context manager protocol and is implicitly called when exiting a `with` statement. Its primary purpose is to ensure that the `close()` method is invoked to clean up the temporary directory, guaranteeing proper resource release regardless of whether an exception occurred within the `with` block.
        *   *Parameters:*
            - **exc_type** (`type`): The type of exception raised, or None if no exception occurred.
            - **exc_val** (`Exception`): The exception instance raised, or None.
            - **exc_tb** (`traceback`): The traceback object, or None.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls the `self.close()` method to perform cleanup.
            - *Called By:* This method is implicitly called when exiting a `with` statement where the `GitRepository` object is used.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self: GitRepository, include_content: bool)`
        *   *Description:* This method constructs a hierarchical dictionary representation of the repository's file structure, mimicking a file system tree. It first ensures that all files are loaded into `self.files` by calling `get_all_files()` if they haven't been already. It then iterates through the `RepoFile` objects, parsing their paths to build nested dictionaries that represent directories, and appends file dictionaries at their respective hierarchical levels.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether the content of each file should be included in its dictionary representation. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree of the repository.
        *   **Usage:** 
            - *Calls:* This method calls `self.get_all_files()` to ensure files are loaded and `file_obj.to_dict()` to get a dictionary representation of each file.
            - *Called By:* The input context does not specify any callers for this method.

---
### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart to visually compare the token counts between JSON and TOON formats. It takes the token counts for both formats, a calculated savings percentage, and an output file path as input. The chart displays two bars, one for JSON and one for TOON, with their respective token counts labeled above them. The chart is titled with the token comparison and the savings percentage, then saved to the specified path and closed.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings, used in the chart's title.
    - **output_path** (`str`): The file path where the generated chart image will be saved.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the net processing time for an operation, specifically accounting for and subtracting estimated sleep times introduced by rate limits for 'gemini-' models. It first determines the total duration between a start and end time. If the model is not a 'gemini-' variant, the total duration is returned directly. For 'gemini-' models, it calculates the number of batches, estimates the total sleep time based on 61 seconds per sleep interval, and then subtracts this from the total duration, ensuring the result is non-negative.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp of the operation, typically in seconds.
    - **end_time** (`float`): The ending timestamp of the operation, typically in seconds.
    - **total_items** (`int`): The total number of items processed during the operation.
    - **batch_size** (`int`): The number of items processed per batch.
    - **model_name** (`str`): The name of the model used, which determines if rate limit sleep times are considered.
*   **Returns:**
    - **net_time** (`float`): The calculated net processing time in seconds, excluding estimated sleep times for rate limits, or the total duration if the model is not 'gemini-'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable | None)`
*   **Description:** The main_workflow function orchestrates a comprehensive analysis of a GitHub repository, generating a detailed report. It begins by extracting API keys and configuring LLM models based on provided names. It then clones a specified GitHub repository, extracts basic project information, constructs a file tree, and performs a relationship analysis to identify calls and instantiations. An Abstract Syntax Tree (AST) schema is created and enriched with the relationship data. The function prepares inputs for a 'Helper LLM' to analyze individual functions and classes within the repository, then invokes the 'Helper LLM' to perform these analyses. Finally, it prepares the aggregated data for a 'Main LLM', evaluates token savings, and calls the 'Main LLM' to generate a final, comprehensive report, which is then saved along with token usage metrics.
*   **Parameters:**
    - **input** (`str`): The initial user input, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used.
    - **status_callback** (`callable | None`): An optional callback function used to provide status updates during the workflow execution.
*   **Returns:**
    - **result** (`dict`): A dictionary containing the 'report' (the final generated report as a string) and 'metrics' (a dictionary of performance and token usage statistics).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by other functions in the provided context.

#### Function: `update_status`
*   **Signature:** `def update_status(msg: Any)`
*   **Description:** This function, `update_status`, is designed to process and display a given message. It first checks if a `status_callback` function is available and, if so, invokes it with the provided message. Regardless of the callback's presence, it logs the message at an informational level using the `logging` module. The primary goal is to provide both a programmatic update mechanism and a persistent log entry for status messages.
*   **Parameters:**
    - **msg** (`Any`): The message string or object to be used for status updates and logging.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback: callable | None)`
*   **Description:** The `notebook_workflow` function orchestrates the analysis of Jupyter notebooks from a specified GitHub repository. It begins by extracting the repository URL from the input, cloning the repository, and then processing its notebook files into an XML-like structure. The function dynamically selects an appropriate LLM based on the model name and API keys provided. It then iterates through each processed notebook, generating a detailed report for each using the selected LLM, and finally concatenates all individual reports into a single markdown document. The final report is saved to a timestamped file, and the function returns the combined report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): The input string, expected to contain a GitHub repository URL from which notebooks will be processed.
    - **api_keys** (`dict`): A dictionary containing API keys for various LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama') used for authentication.
    - **model** (`str`): The name of the LLM model to be used for notebook analysis (e.g., 'gpt-4', 'gemini-pro', 'Llama-2').
    - **status_callback** (`callable | None`): An optional callback function that receives status messages during the workflow execution, allowing for real-time updates.
*   **Returns:**
    - **report** (`str`): The concatenated markdown report generated by the LLM for all processed notebooks in the repository.
    - **metrics** (`dict`): A dictionary containing execution metrics such as helper_time, main_time, total_time, helper_model, main_model, json_tokens, toon_tokens, and savings_percent.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info: dict, nb_path: str, xml_content: str, images: list[dict])`
*   **Description:** This function constructs a multi-part payload suitable for the Gemini API, combining textual context with embedded images. It begins by serializing basic project information and the notebook path into an initial JSON text block. The function then iterates through an XML content string, identifying image placeholders using a regular expression. For each placeholder, it extracts the image data from a provided list, converts it into a base64 data URL, and intersperses it with the surrounding text segments from the XML. The final output is a list of dictionaries, where each dictionary represents either a text part or an image URL part of the complete Gemini payload.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing basic project information to be included in the payload's initial context.
    - **nb_path** (`str`): The file path of the current notebook, also included in the initial context.
    - **xml_content** (`str`): An XML string representing the notebook structure, which may contain image placeholders to be replaced with actual image data.
    - **images** (`list[dict]`): A list of dictionaries, where each dictionary is expected to contain 'data' (base64 encoded image string) and potentially 'mime_type' for images referenced in the XML content.
*   **Returns:**
    - **payload_content** (`list[dict]`): A list of dictionaries, each representing a part of the Gemini API payload. These parts can be of type 'text' or 'image_url'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into a Python module path string. It first determines the relative path of the file with respect to a specified project root. If the file is not within the project root, it defaults to using the file's basename. The function then removes the '.py' extension and replaces directory separators with dots to form a module path. Finally, it handles '__init__.py' files by removing the '.__init__' suffix to represent the package itself.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform a comprehensive static analysis of a Python project to build a call graph. It identifies all Python files, collects definitions of classes, functions, and methods, and then resolves the relationships between these entities by detecting calls. The class provides methods to initiate the analysis, retrieve the raw call graph, and present processed incoming and outgoing relationships.
*   **Instantiation:** This class is not explicitly instantiated by other components based on the provided context.
*   **Dependencies:** This class does not explicitly depend on other components based on the provided context.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the ProjectAnalyzer instance by setting the project root, converting it to an absolute path, and preparing internal data structures. It establishes empty dictionaries for definitions and file_asts, a defaultdict for the call_graph, and a set of directories to ignore during file traversal.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: ProjectAnalyzer, project_root: str)`
        *   *Description:* The __init__ method initializes the ProjectAnalyzer instance by setting the project root, converting it to an absolute path, and preparing internal data structures. It establishes empty dictionaries for definitions and file_asts, a defaultdict for the call_graph, and a set of directories to ignore during file traversal.
        *   *Parameters:*
            - **project_root** (`str`): The root directory of the project to be analyzed.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`analyze`**
        *   *Signature:* `def analyze(self: ProjectAnalyzer, )`
        *   *Description:* This method orchestrates the entire project analysis workflow. It first identifies all Python files within the project, then iterates through them to collect class, function, and method definitions. Subsequently, it performs a second pass to resolve calls between these identified entities, populating the call_graph. Finally, it clears the stored file ASTs to free up memory and returns the completed call graph.
        *   *Parameters:* None
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self: ProjectAnalyzer, )`
        *   *Description:* This method processes the internal call_graph to generate a structured representation of outgoing and incoming relationships. It iterates through the call_graph to build two defaultdicts, one for outgoing calls and one for incoming calls. The final output is a dictionary containing these relationships, with the values sorted and converted to lists for consistent formatting.
        *   *Parameters:* None
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing 'outgoing' and 'incoming' relationship maps, where each map links an entity identifier to a sorted list of related entity identifiers.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self: ProjectAnalyzer, )`
        *   *Description:* This private helper method is responsible for recursively scanning the project_root directory to locate all Python source files. It utilizes os.walk to traverse the directory tree, filtering out directories specified in self.ignore_dirs to optimize the search and avoid irrelevant paths. The method collects and returns a list of absolute paths to all identified Python files.
        *   *Parameters:* None
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found within the project, excluding ignored directories.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self: ProjectAnalyzer, filepath: str)`
        *   *Description:* This private method processes a given Python filepath to extract and store definitions of classes, functions, and methods. It reads the file, parses its content into an Abstract Syntax Tree (AST), and then traverses the AST to identify definition nodes. For each definition, it constructs a unique path name and records its file, line number, and type in self.definitions, also storing the AST in self.file_asts for later use. Error handling is included for file processing.
        *   *Parameters:*
            - **filepath** (`str`): The path to the Python file from which to collect definitions.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self: ProjectAnalyzer, tree: ast.AST, node: ast.AST)`
        *   *Description:* This private utility method searches for the direct parent node of a specified node within a given Abstract Syntax Tree (tree). It performs a full traversal of the tree and for each potential parent, it checks if the target node is one of its children. If a parent is found, it is returned; otherwise, None is returned.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root AST node to search within.
            - **node** (`ast.AST`): The child AST node whose parent is to be found.
        *   *Returns:*
            - **parent_node** (`ast.AST | None`): The parent AST node if found, or None if the node has no parent within the provided tree.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self: ProjectAnalyzer, filepath: str)`
        *   *Description:* This private method is responsible for identifying and resolving function and method calls within a specific Python filepath. It retrieves the pre-parsed AST for the file and then employs an external CallResolverVisitor to traverse the AST and detect calls. The resolved call information, including caller and callee details, is then integrated into the class's self.call_graph structure. Error handling is included for the call resolution process.
        *   *Parameters:*
            - **filepath** (`str`): The path to the Python file for which to resolve calls.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other functions or methods based on the provided context.
            - *Called By:* This method is not explicitly called by other functions or methods based on the provided context.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST visitor designed to identify and resolve all function and method calls within a given Python source file. It extends `ast.NodeVisitor` to traverse the Abstract Syntax Tree, maintaining context such as the current module, class, and function. The visitor tracks imported names and the types of instantiated objects to accurately determine the fully qualified names of called entities. Its main output is a collection of identified calls, each linked to detailed information about its caller.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** The class depends on `ast` for AST traversal, `os` for path manipulation, and `collections.defaultdict` for data storage. It also relies on an external `path_to_module` utility.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallResolverVisitor with the necessary context for analyzing a Python file. It sets up attributes to store the file path, module path, a dictionary of known project definitions, a local scope for names, and a mapping for instance types. It also initializes variables to track the current class and caller name during AST traversal, and a `defaultdict` to accumulate discovered calls.
    *   *Parameters:*
        - **filepath** (`str`): The absolute path to the Python source file being analyzed.
        - **project_root** (`str`): The root directory of the project, used to derive the module path from the file path.
        - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) within the project, used to validate resolved call targets.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: CallResolverVisitor, filepath: str, project_root: str, definitions: dict)`
        *   *Description:* The constructor initializes the CallResolverVisitor with the necessary context for analyzing a Python file. It sets up attributes to store the file path, module path, a dictionary of known project definitions, a local scope for names, and a mapping for instance types. It also initializes variables to track the current class and caller name during AST traversal, and a `defaultdict` to accumulate discovered calls.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python source file being analyzed.
            - **project_root** (`str`): The root directory of the project, used to derive the module path from the file path.
            - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) within the project, used to validate resolved call targets.
        *   *Returns:* None
        *   **Usage:** This method is the constructor for the class.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self: CallResolverVisitor, node: ast.ClassDef)`
        *   *Description:* This method is invoked by the AST visitor framework when an `ast.ClassDef` node is encountered. Its primary role is to manage the `current_class_name` context. It updates this attribute to the name of the class currently being visited, allowing methods defined within it to be correctly identified. After processing the class's body and its children, it restores the `current_class_name` to its previous value, ensuring proper scope handling for nested structures.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal into the class's body.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when a class definition node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self: CallResolverVisitor, node: ast.FunctionDef)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, which represent function or method definitions. It constructs a fully qualified identifier for the function, considering whether it is a top-level function or a method within a class. This identifier is then set as `self.current_caller_name` to correctly attribute any calls made within this function. After traversing the function's body, it reverts `self.current_caller_name` to its previous state to maintain correct context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function or method definition.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal into the function's body.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when a function definition node is encountered during AST traversal.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self: CallResolverVisitor, node: ast.Call)`
        *   *Description:* This method processes `ast.Call` nodes, which represent function or method invocations. It attempts to resolve the fully qualified name of the called entity using the `_resolve_call_qname` helper. If the callee's pathname is successfully resolved and exists in the project's definitions, the method records detailed information about the call, including the caller's file, line number, full identifier, and type (e.g., 'method', 'function'). This call information is then appended to the `self.calls` dictionary, indexed by the callee's pathname.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self._resolve_call_qname` to determine the qualified name of the called function and `self.generic_visit` to continue AST traversal.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when a call expression node is encountered during AST traversal.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self: CallResolverVisitor, node: ast.Import)`
        *   *Description:* This method handles `ast.Import` nodes, which correspond to `import module` statements. It iterates through each alias defined in the import statement. For each alias, it stores the local name (either the `asname` or the original `name`) and its corresponding module name in the `self.scope` dictionary. This mapping is crucial for later resolving qualified names of imported modules and their members.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when an import statement node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self: CallResolverVisitor, node: ast.ImportFrom)`
        *   *Description:* This method processes `ast.ImportFrom` nodes, which represent `from module import name` statements. It determines the full module path, correctly handling relative imports by adjusting based on `node.level` and the current `module_path`. For each imported name, it constructs its fully qualified path and stores it in the `self.scope` dictionary, mapping the local alias or name to its global identifier. This enables accurate resolution of imported functions, classes, or variables.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when a 'from ... import ...' statement node is encountered during AST traversal.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self: CallResolverVisitor, node: ast.Assign)`
        *   *Description:* This method handles `ast.Assign` nodes, specifically focusing on assignments where the right-hand side is a call to a class constructor (e.g., `instance = MyClass()`). If such an instantiation is detected and the class name can be resolved through `self.scope` and `self.definitions`, it records the qualified class name as the type for the assigned variable. This information is stored in `self.instance_types`, which is vital for resolving method calls on these instances later in the analysis.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:* None
        *   **Usage:** 
            - *Calls:* This method calls `self.generic_visit` to continue the AST traversal.
            - *Called By:* This method is called by the `ast.NodeVisitor` framework when an assignment statement node is encountered during AST traversal.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self: CallResolverVisitor, func_node: ast.expr)`
        *   *Description:* This private helper method is responsible for resolving the fully qualified name (QName) of a function or method represented by an AST `func_node`. It handles two main scenarios: direct calls to names (`ast.Name`) and method calls on attributes (`ast.Attribute`). For `ast.Name`, it checks `self.scope` for imported names and then local module-level definitions. For `ast.Attribute`, it attempts to determine the class type of the instance variable from `self.instance_types` or the module from `self.scope` to construct the qualified method name. If the QName cannot be resolved, it returns `None`.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the callable expression (e.g., `ast.Name` for a function, `ast.Attribute` for a method).
        *   *Returns:*
            - **qname** (`str | None`): The fully qualified name of the called function or method, or `None` if it cannot be resolved.
        *   **Usage:** 
            - *Calls:* This method does not explicitly call other methods from the input `method_context`.
            - *Called By:* This method is called by `CallResolverVisitor.visit_Call` to determine the qualified name of a function being invoked.

---
### File: `backend/scads_key_test.py`

*No classes or standalone functions were found in this file.*
---
### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function `encrypt_text` is responsible for encrypting a given string using a `cipher_suite` object. It first performs a conditional check: if the input `text` is empty or if the `cipher_suite` is not available, it returns the original text without any encryption. Otherwise, the function processes the input `text` by removing leading and trailing whitespace and then encoding it into bytes. These bytes are subsequently encrypted using the `cipher_suite`'s `encrypt` method, and the resulting encrypted bytes are decoded back into a string before being returned.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted. If this string is empty, it will be returned unencrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input string, or the original string if encryption conditions are not met.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given string using an external `cipher_suite` object. It first performs a guard clause, returning the original text if the input `text` is empty or if `cipher_suite` is not defined. If decryption proceeds, the input string is stripped of whitespace, encoded to bytes, decrypted, and then decoded back into a string. The function includes error handling, returning the original text if any exception occurs during the decryption process.
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_text_or_original** (`str`): The decrypted string if successful, or the original input string if decryption fails or conditions for decryption are not met.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function is designed to insert a new user's information into a database. It takes a username, the user's name, and a plain-text password as input. The provided password is first hashed using `stauth.Hasher.hash` for secure storage. A user document is then constructed, including the hashed password and default empty strings for various API keys. Finally, this document is inserted into the `dbusers` collection, and the unique identifier of the newly created user document is returned.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (`_id`) of the newly inserted user document.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** The `fetch_all_users` function is designed to retrieve all user records from a database collection named `dbusers`. It invokes the `find()` method on the `dbusers` object, which typically returns a cursor containing all documents. This cursor is then immediately converted into a standard Python list, effectively fetching and returning all available user data.
*   **Parameters:** None
*   **Returns:**
    - **users** (`list`): A list containing all user documents (likely dictionaries) retrieved from the 'dbusers' collection.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The `fetch_user` function is designed to retrieve a single user record from a database collection named `dbusers`. It takes a username as input and uses it to query the `_id` field within the collection. The function returns the first document that matches the provided username, or `None` if no such user is found.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be fetched from the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if found, or `None` if no user matches the provided username.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the name of an existing user within the `dbusers` collection. It identifies the target user by matching the provided `username` with the document's `_id` field. The function then sets the `name` field of the identified user's document to the `new_name`. It returns an integer representing the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user, which corresponds to the `_id` field in the database, whose name is to be updated.
    - **new_name** (`str`): The new name to be assigned to the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database. It takes a username and the new Gemini API key as input. The provided API key is first stripped of whitespace and then encrypted before being stored. The function then performs an update operation on the database, setting the 'gemini_api_key' field for the specified user with the encrypted value. It returns the count of modified documents.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The raw Gemini API key provided by the user, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** This function updates a user's GPT API key in the database. It first encrypts the provided `gpt_api_key` after stripping any leading or trailing whitespace. Then, it uses the `dbusers` collection to find a document matching the given `username` and sets its `gpt_api_key` field to the newly encrypted value. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The username of the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be encrypted and stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specific user in a database. It takes a username and a new Ollama base URL as input. The function locates the user document by their username and updates the 'ollama_base_url' field with the provided URL, ensuring any leading or trailing whitespace is removed. It then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama URL is to be updated.
    - **ollama_base_url** (`str`): The new Ollama base URL to set for the user. Leading and trailing whitespace will be removed before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function updates a user's Open Source API key in the database. It first encrypts the provided API key, ensuring any leading or trailing whitespace is removed. Then, it uses the `dbusers` collection to find the user by their username and sets their `opensrc_api_key` field to the newly encrypted value. The function returns the number of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The username of the user whose Open Source API key is to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be stored, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 1 if the user exists and the key was updated, or 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** This function is responsible for updating a user's 'opensrc_base_url' in a database. It takes a username and a new opensrc base URL as input. The function performs an update operation on the 'dbusers' collection, locating the user by their '_id' which corresponds to the provided username. It then sets the 'opensrc_base_url' field to the new URL, ensuring any leading or trailing whitespace is removed. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose opensrc URL needs to be updated.
    - **opensrc_base_url** (`str`): The new base URL for opensrc to be associated with the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions in the provided context.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** This function is designed to retrieve a user's Gemini API key from a database. It queries a collection, presumably `dbusers`, using the provided `username` as the document's `_id`. If a matching user document is found, it extracts the `gemini_api_key` field. The function returns this key if present, or `None` if the user is not found or the key does not exist.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key associated with the user, or None if the user is not found or the key is not present in the user's document.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL for a specific user from a database. It queries the 'dbusers' collection using the provided username as the document's ID. If a user document is found, it extracts and returns the 'ollama_base_url' field. If no user is found, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL associated with the user, or None if the user is not found in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** The `fetch_gpt_key` function is responsible for retrieving a user's GPT API key from a database. It takes a username as input and queries the `dbusers` collection to locate the corresponding user document. If a user is found, the function extracts the 'gpt_api_key' field from the document. It returns this key if present, otherwise it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the user, or None if the user is not found or the key does not exist.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** This function is designed to retrieve a user's 'opensrc_api_key' from a database based on their username. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided username. The query is optimized to return only the 'opensrc_api_key' and exclude the '_id' field. If a user document is found, it attempts to extract and return the 'opensrc_api_key'; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the opensrc API key.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The opensrc API key associated with the username, or None if the user or key is not found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** The `fetch_opensrc_url` function is designed to retrieve a user's opensource base URL from a database. It queries the `dbusers` collection using the provided username as the document's `_id`. The function specifically projects the `opensrc_base_url` field. If a user document is found, it extracts and returns the value of `opensrc_base_url`; otherwise, it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose opensource base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The opensource base URL associated with the user, or `None` if the user is not found or the URL is not set.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** The `delete_user` function is designed to remove a specific user record from a database collection. It accepts a username, which is used as the primary key (`_id`) to locate and delete the corresponding document within the `dbusers` collection. The function returns an integer indicating the number of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation (typically 1 if a user was found and deleted, or 0 if no matching user was found).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves a user's API keys and URLs from a database based on the provided username. It queries the `dbusers` collection for a matching user. If a user is found, it decrypts the Gemini, GPT, and open-source API keys using a `decrypt_text` function and retrieves the Ollama and open-source base URLs directly. If no user is found, it returns a tuple of `None` values. Otherwise, it returns a tuple containing all the processed keys and URLs.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_api_key** (`Union[str, None]`): The decrypted Gemini API key, or None if the user is not found or the key is not present.
    - **ollama_base_url** (`Union[str, None]`): The Ollama base URL, or None if the user is not found or the URL is not present.
    - **gpt_api_key** (`Union[str, None]`): The decrypted GPT API key, or None if the user is not found or the key is not present.
    - **opensrc_api_key** (`Union[str, None]`): The decrypted open-source API key, or None if the user is not found or the key is not present.
    - **opensrc_base_url** (`Union[str, None]`): The open-source base URL, or None if the user is not found or the URL is not present.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** This function creates a new chat entry in a database. It constructs a dictionary containing a unique identifier generated by `uuid.uuid4()`, the provided username, the chat name, and the current timestamp using `datetime.now()`. This chat document is then inserted into the `dbchats` collection. The function returns the unique ID of the newly inserted chat.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (ID) of the newly created chat entry.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** This function retrieves all chat records associated with a specific user from a database collection named `dbchats`. It filters the chats by the provided username and then sorts the results by their creation timestamp in ascending order. The function converts the database cursor into a list of chat documents before returning them.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the associated chat records.
*   **Returns:**
    - **chats** (`list`): A list of chat documents belonging to the specified user, sorted by their creation date.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function determines if a chat entry exists in the 'dbchats' collection based on a provided username and chat name. It queries the database for a document that matches both criteria. The function returns a boolean indicating the presence or absence of such a chat.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked for existence.
*   **Returns:**
    - **chat_exists** (`bool`): True if a chat matching the specified username and chat name is found, False otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and all its associated exchanges within a database. It first updates a single chat entry in the `dbchats` collection, changing its `chat_name` from the `old_name` to the `new_name` for a specific `username`. Subsequently, it updates all related exchange entries in the `dbexchanges` collection, similarly updating their `chat_name` fields. The function returns the count of modified chat entries from the initial chat renaming operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The new desired name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat documents modified in the `dbchats` collection during the rename operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str, json_tokens: int, toon_tokens: int, savings_percent: float)`
*   **Description:** This function is responsible for inserting a new exchange record into a database collection. It generates a unique identifier for the exchange using UUID, then constructs a dictionary containing the provided question, answer, feedback, user details, and various metrics such as helper/main model usage, time, and token counts. A timestamp for creation is also added. The function attempts to insert this record into the `dbexchanges` collection. If the insertion is successful, it returns the generated unique ID; otherwise, it catches any exceptions, prints an error message, and returns `None`.
*   **Parameters:**
    - **question** (`str`): The user's question in the exchange.
    - **answer** (`str`): The generated answer for the question.
    - **feedback** (`str`): User feedback provided for the exchange.
    - **username** (`str`): The username associated with this exchange.
    - **chat_name** (`str`): The name of the chat session where the exchange occurred.
    - **helper_used** (`str`): Indicates which helper model was used, if any. Defaults to an empty string.
    - **main_used** (`str`): Indicates which main model was used, if any. Defaults to an empty string.
    - **total_time** (`str`): The total time taken for the exchange. Defaults to an empty string.
    - **helper_time** (`str`): The time taken by the helper model. Defaults to an empty string.
    - **main_time** (`str`): The time taken by the main model. Defaults to an empty string.
    - **json_tokens** (`int`): The number of JSON tokens used in the exchange. Defaults to 0.
    - **toon_tokens** (`int`): The number of 'toon' tokens used in the exchange. Defaults to 0.
    - **savings_percent** (`float`): The percentage of savings achieved for this exchange. Defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly inserted exchange record upon successful insertion.
    - **None** (`NoneType`): Returns None if an exception occurs during the database insertion process.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records associated with a specific username from a database collection named `dbexchanges`. It queries the collection using the provided username and sorts the results by their 'created_at' timestamp in ascending order. The function then converts the database cursor into a list of these exchange records, which is subsequently returned.
*   **Parameters:**
    - **username** (`str`): The username used to filter and retrieve specific exchange records from the database.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (documents) found for the given username, sorted by their creation timestamp.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function, `fetch_exchanges_by_chat`, is designed to retrieve a collection of exchange records from a database. It queries the `dbexchanges` collection, filtering documents based on a specific username and chat name. The matching records are then sorted by their creation timestamp in ascending order. Finally, the function returns these sorted exchange records as a list.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchange records.
    - **chat_name** (`str`): The name of the chat used to filter the exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents that match the provided username and chat name, sorted by their 'created_at' field.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function is responsible for updating the feedback status of a specific exchange record within a database. It accepts an exchange identifier and an integer feedback value. The function uses a database update operation to locate the record by its ID and then modifies its 'feedback' field to the new provided value. It returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange record to be updated in the database.
    - **feedback** (`int`): The integer value representing the new feedback to be set for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 typically indicates a successful update, while 0 suggests no matching document was found or no changes were made.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates an existing exchange record in the database. It specifically targets a document identified by `exchange_id` and sets its `feedback_message` field to the provided string value. The function then returns the number of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange document to be updated. Its type is inferred from its usage as a query key.
    - **feedback_message** (`str`): The new feedback message string to be stored for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 1 if successful, or 0 if no matching document was found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is designed to remove a specific exchange record from a database collection named `dbexchanges`. It takes a unique identifier for the exchange as input. The function executes a deletion operation targeting the document with the matching `_id`. Upon completion, it returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **exchange_id** (`str`): The unique string identifier of the exchange record to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted from the collection, typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is designed to completely remove a specific chat and all its associated message exchanges from the database. It operates by first deleting all message exchanges that belong to the given username and chat name from the 'dbexchanges' collection. Following this, it deletes the chat entry itself from the 'dbchats' collection. The primary purpose is to ensure data consistency between the frontend and backend by removing all related data for a chat. The function returns the count of chat documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted from the 'dbchats' collection. This will typically be 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

---
### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list: list[str])`
*   **Description:** This function takes a list of strings, presumably model identifiers or paths, as input. It iterates through each string in the provided list. For every string, it splits the string by the '/' character and extracts the last element from the resulting list. The function then returns a new list containing these extracted last elements, effectively cleaning the names by removing any preceding path components.
*   **Parameters:**
    - **model_list** (`list[str]`): A list of strings, where each string is expected to be a path-like identifier for a model.
*   **Returns:**
    - **cleaned_names** (`list[str]`): A new list containing the cleaned names, where each name is the last component of the original string after splitting by '/'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list: list, category_name: str)`
*   **Description:** This function filters a given list of models (`source_list`) based on a specified `category_name`. It retrieves filtering keywords from a global `CATEGORY_KEYWORDS` mapping. If the category's keywords include "STANDARD", it returns only those models from the `source_list` that are also present in `STANDARD_MODELS`. Otherwise, it iterates through the `source_list` and includes models whose names (case-insensitive) contain any of the retrieved keywords. If no models match the keywords, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The initial list of models to be filtered.
    - **category_name** (`str`): The name of the category used to determine the filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered according to the specified category, or the original list if no filters apply or no models match.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function is designed to save a new Gemini API key. It retrieves the key from the Streamlit session state, validates its presence, and then updates the key in the database associated with the current user. After a successful update, it clears the key from the session state and displays a confirmation toast message to the user.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function, `save_ollama_cb`, acts as a callback to persist a user-defined Ollama URL. It retrieves the `in_ollama_url` value from Streamlit's session state. If a valid URL is found, it proceeds to update this URL in the database using the `db.update_ollama_url` method, associating it with the currently logged-in user's username, also retrieved from session state. Upon successful update, a confirmation toast message is displayed to the user. This function primarily handles the logic for saving user preferences related to Ollama service endpoints.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function, `load_data_from_db`, is responsible for loading chat and exchange data for a specified user from the database into the Streamlit session state. It first checks if the data for the given username is already loaded to prevent redundant operations. If not loaded, it initializes the `chats` dictionary in `st.session_state`, then fetches predefined chats and their names from the database to establish the chat structure. Subsequently, it retrieves all exchanges for the user, categorizes them under their respective chats, and handles cases where chat names might be missing or new, while also normalizing feedback values. Finally, it ensures a default chat exists if none were loaded and sets an active chat in the session state.
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat and exchange data from the database.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: dict, val: Any)`
*   **Description:** This function is designed to handle changes in feedback for an 'exchange' object within a Streamlit application. It updates the 'feedback' key of the provided 'ex' object with the new 'val'. Subsequently, it calls the 'db.update_exchange_feedback' function to persist this change to the database, using the '_id' from the 'ex' object. Finally, it triggers a full rerun of the Streamlit application to reflect the updated state in the UI.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing an 'exchange', expected to contain '_id' and 'feedback' keys.
    - **val** (`Any`): The new feedback value to be assigned to the 'feedback' key of the 'ex' object and updated in the database.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: str, ex: dict)`
*   **Description:** This function is responsible for deleting a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if the exchange is found within that chat's exchanges list, it removes it from the session state. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be removed in the session state.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' field for database deletion.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** This function handles the deletion of a specified chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the chat from the Streamlit session state. If the deleted chat was the active one, or if no chats remain, it updates the `active_chat` session state. If all chats are deleted, a new default chat named "Chat 1" is created and set as active. Finally, it triggers a Streamlit rerun.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted or created.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text: str)`
*   **Description:** This function is designed to extract a repository name from a given text string. It first attempts to locate a URL within the input text using a regular expression. If a URL is successfully matched, the function proceeds to parse this URL to isolate its path component. The path is then processed by stripping leading/trailing slashes, and the last segment is considered the potential repository name. Finally, it checks if the extracted name ends with ".git" and removes the suffix if present, returning the cleaned name or None if no URL or valid path is found.
*   **Parameters:**
    - **text** (`str`): The input string, which may contain a URL from which to extract a repository name.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted and cleaned repository name as a string if a valid URL and path are found, otherwise None.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text: str)`
*   **Description:** This function acts as a generator that takes a string of text and yields its words sequentially, each followed by a space. It introduces a small delay of 0.01 seconds between yielding each word, simulating a streaming effect. The function achieves this by splitting the input text by spaces and iterating over the resulting words.
*   **Parameters:**
    - **text** (`str`): The input string of text to be processed and streamed word by word.
*   **Returns:**
    - **word_with_space** (`str`): A single word from the input text, followed by a space, yielded one at a time.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str, should_stream: bool)`
*   **Description:** This function processes a given markdown string, identifying and rendering both standard markdown content and embedded Mermaid diagrams. It splits the input text based on ````mermaid ... ```` delimiters. Standard markdown sections are rendered using `st.markdown` or streamed via `st.write_stream` if `should_stream` is true. Mermaid diagram blocks are rendered using `st_mermaid`, with a fallback to `st.code` if the `st_mermaid` rendering fails.
*   **Parameters:**
    - **markdown_text** (`str`): The input string that may contain markdown and embedded Mermaid diagram syntax.
    - **should_stream** (`bool`): A boolean flag indicating whether non-Mermaid markdown content should be rendered using `st.write_stream` for a streaming effect or `st.markdown` for static rendering.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** The render_exchange function is responsible for displaying a single chat exchange, consisting of a user question and an assistant's answer, within a Streamlit application. It first renders the user's question and then presents the assistant's response within a dedicated message container. This container includes an interactive toolbar with functionalities such as feedback (like/dislike), adding a comment via a popover, downloading the answer as Markdown, and deleting the exchange. The function also handles error states in the assistant's answer, displaying an error message and providing a delete option. It leverages various Streamlit components to create this interactive user interface.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing a single chat exchange. It is expected to contain keys such as 'question', 'answer', 'feedback', 'feedback_message', and '_id', which are used to populate the UI, manage feedback, and identify the exchange for operations like deletion or updates.
    - **current_chat_name** (`str`): A string representing the name of the current chat session. This parameter is utilized when invoking the handle_delete_exchange function to correctly identify and remove an exchange from the specified chat.
*   **Returns:** None
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** This class serves as a Pydantic model to structure the description of a single function parameter. It defines three essential string fields: 'name', 'type', and 'description', providing a standardized way to represent parameter metadata. This model is likely used within larger schemas to detail the parameters of various functions or methods, ensuring consistent data representation.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The class inherits from pydantic.BaseModel and does not define an explicit __init__ method. Pydantic automatically generates a constructor that initializes instances with values for 'name', 'type', and 'description' based on the type hints provided in the class definition.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type of the parameter.
        - **description** (`str`): A description of the parameter's purpose.
*   **Methods:** *No methods defined.*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to standardize the representation of a function's return value. It serves as a data structure to hold metadata about a return, including its identifier, Python type, and a descriptive explanation. This class facilitates consistent documentation and programmatic handling of function outputs within a larger system.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance of `ReturnDescription` by accepting `name`, `type`, and `description` as keyword arguments, validating their types, and assigning them as instance attributes.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The Python type hint of the return value.
        - **description** (`str`): A detailed explanation of what the return value represents.
*   **Methods:** *No methods defined.*

#### Class: `UsageContext`
*   **Summary:** The `UsageContext` class is a Pydantic BaseModel designed to encapsulate and describe the calling context of a function or method. It provides a structured way to store information about what a function calls (`calls`) and where it is called from (`called_by`), both represented as descriptive strings. This class acts as a data container for contextual interaction details within a larger system.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The `__init__` method for `UsageContext` is implicitly generated by Pydantic's `BaseModel`. It handles the instantiation of a `UsageContext` object by validating and assigning the `calls` and `called_by` string attributes based on the arguments provided during object creation.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or external components that this context (e.g., a function) invokes.
        - **called_by** (`str`): A string summarizing the functions, methods, or external components that invoke this context (e.g., a function).
*   **Methods:** *No methods defined.*

#### Class: `FunctionDescription`
*   **Summary:** This class serves as a structured data model for representing a comprehensive analysis of a function. It aggregates key information such as the function's high-level purpose, its input parameters, its expected return values, and where it is utilized within a larger system. As a Pydantic BaseModel, it provides data validation and serialization capabilities for this structured function description.
*   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. It initializes instances by validating and assigning values to its defined fields: `overall`, `parameters`, `returns`, and `usage_context`.
    *   *Parameters:*
        - **overall** (`str`): A string describing the function's overall purpose and high-level implementation.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each detailing a parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of objects, each describing a return value of the function.
        - **usage_context** (`UsageContext`): An object providing context about where the function is called and what it calls.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to represent the structured JSON schema for the comprehensive analysis of a single Python function. It encapsulates the function's unique identifier, a detailed description object (presumably another Pydantic model named FunctionDescription), and an optional field to report any errors encountered during the analysis process. This model is crucial for standardizing the output format of function analysis results within the larger system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class inherits from Pydantic's BaseModel, meaning its initialization is handled automatically by Pydantic based on the defined fields. It does not contain an explicit `__init__` method; instead, instances are created by passing keyword arguments corresponding to its fields.
    *   *Parameters:* None
*   **Methods:** *No methods defined.*

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to encapsulate the details of a Python class's __init__ method. It provides a structured format to store a textual summary of the constructor's behavior and a list of ParameterDescription objects, each detailing an individual parameter of the constructor. This class serves as a schema for representing constructor information in a machine-readable way.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly defines its constructor to accept `description` and `parameters` as arguments. It initializes these attributes directly from the provided values, ensuring type validation according to the Pydantic schema.
    *   *Parameters:*
        - **description** (`str`): A string providing a summary or explanation of the constructor's purpose and behavior.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing a specific parameter accepted by the constructor.
*   **Methods:** *No methods defined.*

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's operational context. It specifically stores information regarding the class's external dependencies and the locations where it is instantiated. This model provides a structured way to represent these contextual details, facilitating data validation and consistent data handling within a larger system.
*   **Instantiation:** The provided context does not specify explicit locations where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the __init__ method for ClassContext is implicitly generated. It accepts 'dependencies' and 'instantiated_by' as keyword arguments, validates their types, and assigns them as instance attributes. This constructor ensures that instances of ClassContext are properly initialized with the required contextual information.
    *   *Parameters:*
        - **dependencies** (`str`): A string summarizing the external dependencies that the class relies upon.
        - **instantiated_by** (`str`): A string summarizing the primary locations or modules where the class is instantiated.
*   **Methods:** *No methods defined.*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of another Python class. It structures information about a class's high-level purpose, its constructor details, a list of its individual methods with their own analyses, and its broader usage context within a system. This model serves as a standardized data structure for representing class analysis.
*   **Instantiation:** There are no explicit instantiation points listed for this class within the provided context.
*   **Dependencies:** There are no explicit external dependencies listed for this class within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, does not have an explicit `__init__` method. Its initialization is handled implicitly by Pydantic, which expects keyword arguments corresponding to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose.
        - **init_method** (`ConstructorDescription`): Details about the class's constructor.
        - **methods** (`List[FunctionAnalysis]`): A list of detailed analyses for each method within the class.
        - **usage_context** (`ClassContext`): Contextual information regarding the class's dependencies and instantiation.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the root Pydantic model for structuring the output of a class analysis. It encapsulates the class's identifier, a comprehensive ClassDescription object detailing its components, and an optional error field for reporting analysis failures. This model ensures a standardized and machine-readable format for class analysis results, facilitating further processing by other AI systems.
*   **Instantiation:** This class is not explicitly instantiated by other known components in the provided context.
*   **Dependencies:** This class depends on 'BaseModel' from 'pydantic' for its core functionality and 'Optional' from 'typing' for type hinting.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, has an implicitly generated constructor. It initializes an instance of ClassAnalysis by accepting keyword arguments for its fields: 'identifier', 'description', and an optional 'error' string. These values are then validated against their respective types as defined in the model.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the class being analyzed.
        - **description** (`ClassDescription`): A detailed analysis object containing the overall class description, constructor details, and method analyses.
        - **error** (`Optional[str]`): An optional string containing an error message if the class analysis failed, otherwise None.
*   **Methods:** *No methods defined.*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event within a system, likely for relationship analysis. It serves as a structured data container for tracking where functions or classes are called or instantiated. The class defines fields such as the file path, the name of the calling function, the mode of the call (e.g., 'method', 'function', 'module'), and the line number where the call occurs. This structure facilitates consistent data representation for call tracing.
*   **Instantiation:** The instantiation points for this class are not specified within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the analyzed context.
*   **Constructor:**
    *   *Description:* The CallInfo class leverages Pydantic's BaseModel for its structure, meaning its initialization is implicitly handled by Pydantic. When an instance is created, Pydantic validates and assigns values to the declared fields based on the provided keyword arguments.
    *   *Parameters:* None
*   **Methods:** *No methods defined.*

#### Class: `FunctionContextInput`
*   **Summary:** This class serves as a structured data container, built with Pydantic, to encapsulate the contextual information required for analyzing a Python function. It specifically tracks the outbound dependencies (what the function calls) and inbound dependencies (what calls the function), providing a holistic view of its interactions within a larger codebase. This model is crucial for understanding a function's role and its integration points.
*   **Instantiation:** The provided context does not specify any explicit locations where this class is instantiated. It is likely instantiated programmatically when gathering context for function analysis.
*   **Dependencies:** This class primarily depends on Pydantic's `BaseModel` for its data validation and serialization capabilities. No other explicit external functional dependencies are listed in the provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, meaning its initialization is handled automatically by Pydantic. Instances are created by providing values for its `calls` and `called_by` fields, which Pydantic validates against their defined types.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of identifiers (strings) representing other functions, methods, or classes that the function being analyzed calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects, each detailing a specific location or context from which the function being analyzed is called.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a FunctionAnalysis object. It serves as a data transfer object (DTO) that encapsulates all necessary information, such as the function's source code, its identifier, relevant imports, and additional contextual data. This class ensures that all inputs for function analysis adhere to a consistent and validated schema, facilitating reliable processing by downstream systems.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. It inherits from `pydantic.BaseModel`, which automatically generates a constructor based on the declared fields. The constructor will accept keyword arguments corresponding to the `mode`, `identifier`, `source_code`, `imports`, and `context` fields to initialize an instance.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, fixed to 'function_analysis' to indicate a function analysis request.
        - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
        - **source_code** (`str`): The raw source code of the entire function definition.
        - **imports** (`List[str]`): A list of import statements from the source file, providing context for the function.
        - **context** (`FunctionContextInput`): Additional contextual information required for the function analysis, such as calls made by or to the function.
*   **Methods:** *No methods defined.*

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to structure and validate contextual information about a Python method. It serves as a data schema for representing various aspects of a method's interaction within a larger system, including its unique identifier, the functions it calls, where it is called from, its arguments, and its docstring. This class is crucial for systems that need to analyze, document, or process method-level metadata in a standardized format.
*   **Instantiation:** The specific instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `MethodContextInput` is automatically generated. It accepts keyword arguments corresponding to the defined fields, allowing for the creation of instances with validated method context data. This constructor ensures that all required fields are present and correctly typed upon instantiation.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method being described.
        - **calls** (`List[str]`): A list of string identifiers for other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects, each describing a specific location or entity that calls this method.
        - **args** (`List[str]`): A list of string representations of the arguments defined in the method's signature.
        - **docstring** (`Optional[str]`): An optional string containing the docstring associated with the method, if available.
*   **Methods:** *No methods defined.*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information relevant for analyzing a Python class. It serves as a data container, defining fields for external dependencies, instantiation points, and detailed context for each of the class's methods. This model ensures that class analysis is performed with a comprehensive understanding of its operational environment and internal structure.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for ClassContextInput is implicitly generated by Pydantic's BaseModel. It handles the validation and assignment of the `dependencies`, `instantiated_by`, and `method_context` fields based on the provided input, ensuring that the object adheres to the defined schema.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external functional dependencies of the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where the class being analyzed is instantiated within the codebase.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing specific contextual details for a method within the class being analyzed.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for performing a class analysis. It serves as a data schema, ensuring that all necessary components like the operation mode, class identifier, its source code, relevant import statements, and additional contextual information are present and correctly typed before analysis proceeds. This class acts as a robust validator and container for the initial data payload.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The ClassAnalysisInput class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is implicitly generated, allowing instantiation by providing values for its defined fields: mode, identifier, source_code, imports, and context. Pydantic handles validation and assignment of these attributes upon object creation.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operation mode, which must be 'class_analysis' to indicate the type of analysis being requested.
        - **identifier** (`str`): The unique name or identifier of the class that is to be analyzed.
        - **source_code** (`str`): The complete raw source code of the entire class definition to be analyzed.
        - **imports** (`List[str]`): A list of import statements from the source file, which may include imports relevant to the class or its methods.
        - **context** (`ClassContextInput`): An object containing additional contextual information pertinent to the class analysis, such as dependencies or instantiation points.
*   **Methods:** *No methods defined.*
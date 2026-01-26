# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** This project is an automated code documentation agent designed to analyze and document GitHub repositories. It features a backend that clones a given repository, performs a deep static analysis by building an Abstract Syntax Tree (AST) and a call graph, and then leverages a multi-LLM architecture for code explanation. A Helper LLM analyzes individual code components (functions and classes), and a Main LLM synthesizes this information into a comprehensive, human-readable report. The system includes a user-friendly web interface built with Streamlit for inputting repository URLs and viewing the final documentation.
- **Key Features:**
  - Automated cloning and analysis of public GitHub repositories.
  - Abstract Syntax Tree (AST) and call graph generation for deep code structure understanding.
  - A dual-LLM architecture (Helper/Main) for detailed, component-level analysis and cohesive report synthesis.
  - Support for analyzing both Python source code and Jupyter Notebooks.
  - A Streamlit-based web interface for user interaction, configuration, and results display.
- **Tech Stack:** Streamlit, LangChain, GitPython, Pydantic, NetworkX, Matplotlib, TOON Format.

*   **Repository Structure:**
    ```mermaid
    graph LR
        subgraph root
            A(".env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json")
        end
        root --> B(SystemPrompts)
        subgraph SystemPrompts
            B1("SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt")
        end
        root --> C(backend)
        subgraph backend
            C1("AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py")
        end
        root --> D(database)
        subgraph database
            D1("db.py")
        end
        root --> E(frontend)
        subgraph frontend
            E1("__init__.py<br/>frontend.py")
        end
        E --> F(.streamlit)
        subgraph .streamlit
            F1("config.toml")
        end
        E --> G(gifs)
        subgraph gifs
            G1("4j.gif")
        end
        root --> H(notizen)
        subgraph notizen
            H1("Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md")
        end
        H --> I(grafiken)
        root --> J(result)
        root --> K(schemas)
        subgraph schemas
            K1("types.py")
        end
        root --> L(statistics)
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
- googleapis-common-protos==1.72.1
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

This project contains a `requirements.txt` file. You can install all dependencies using pip:
`pip install -r requirements.txt`
### Setup Guide
1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
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
4.  **Set Up Environment Variables:**
    - Copy the `.env.example` file to a new file named `.env`.
    - Open the `.env` file and add your necessary API keys and configuration values (e.g., for Gemini, OpenAI, MongoDB).
### Quick Startup
To run the application, execute the following command from the root directory:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The primary use case of this application is to automatically generate technical documentation for a software project hosted on GitHub.

**Primary Workflow:**
1.  Launch the Streamlit web application.
2.  Log in or register to access the main interface.
3.  Configure API keys for the desired Large Language Models (LLMs) in the settings panel.
4.  Enter the URL of a public GitHub repository into the input field.
5.  Select the Helper and Main LLM models to be used for the analysis.
6.  Initiate the analysis. The backend will clone the repository, analyze its structure and code, and generate a comprehensive report.
7.  View the generated report directly in the web interface. The report is also saved locally for future reference.

**Secondary Workflow (Notebook Analysis):**
- The application also supports a dedicated workflow for analyzing Jupyter Notebooks (`.ipynb`) within a repository, capable of processing both text, code, and embedded images.

**Primary Command:**
The application is launched via the Streamlit command-line interface.
```bash
streamlit run frontend/frontend.py
```

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here



## 5. Code Analysis
### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` and is designed to traverse an Abstract Syntax Tree (AST) of a Python source file. Its primary purpose is to extract structured information about imports, functions, and classes defined within the visited source code. It builds a `schema` dictionary that categorizes these elements, including details like identifiers, names, docstrings, and source code segments, facilitating a comprehensive analysis of the code's structure.
*   **Instantiation:** This class is not explicitly instantiated by other known components within the provided context.
*   **Dependencies:** The class depends on the `ast` module for AST traversal and node manipulation, and `path_to_module` for resolving module paths.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor with the raw source code, the file's absolute path, and the project's root directory. It calculates the module's qualified path and sets up an empty dictionary (`self.schema`) to store extracted imports, functions, and classes. It also initializes `_current_class` to `None` for tracking the context of nested definitions.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being visited.
        - **file_path** (`str`): The absolute path to the file being visited.
        - **project_root** (`str`): The root directory of the project, used to determine the module path.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code, file_path, project_root)`
        *   *Description:* The constructor initializes the ASTVisitor with the raw source code, the file's absolute path, and the project's root directory. It calculates the module's qualified path and sets up an empty dictionary (`self.schema`) to store extracted imports, functions, and classes. It also initializes `_current_class` to `None` for tracking the context of nested definitions.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **source_code** (`str`): The raw source code of the file being visited.
            - **file_path** (`str`): The absolute path to the file being visited.
            - **project_root** (`str`): The root directory of the project, used to determine the module path.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes `ast.Import` nodes, which represent `import module` statements. It iterates through each imported alias and appends the module name to the `imports` list within the `self.schema` dictionary. After processing the current node, it calls `self.generic_visit(node)` to ensure continued traversal of its children.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `self.generic_visit`
            *   **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `ast.ImportFrom` nodes, which represent `from module import name` statements. It iterates through each alias in the import statement and appends the fully qualified import name (e.g., `module.alias`) to the `imports` list within `self.schema`. It then calls `self.generic_visit(node)` to continue traversing the AST.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `self.generic_visit`
            *   **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ImportFrom` node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method processes `ast.ClassDef` nodes, representing class definitions. It constructs a dictionary containing detailed information about the class, including its identifier, name, docstring, source code segment, and line numbers. This class information is then appended to the `classes` list in `self.schema`. It temporarily sets `_current_class` to the newly created class info to correctly associate nested function definitions (methods) with their parent class. After visiting children, `_current_class` is reset.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `ast.get_docstring`, `ast.get_source_segment`, `self.generic_visit`
            *   **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, representing function or method definitions. It first checks if a class is currently being visited (indicated by `_current_class`). If so, it creates method-specific information and appends it to the `method_context` of the current class. Otherwise, it creates function-specific information and appends it to the `functions` list in `self.schema`. It extracts details like identifier, name, arguments, docstring, and line numbers. Finally, it calls `self.generic_visit` to continue AST traversal.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function or method definition.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `ast.get_docstring`, `ast.get_source_segment`, `self.generic_visit`
            *   **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.FunctionDef` node is encountered during AST traversal.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method processes `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. It delegates the processing of these nodes directly to the `visit_FunctionDef` method, treating them similarly to regular function definitions for the purpose of schema generation and data extraction.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `self.visit_FunctionDef`
            *   **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.AsyncFunctionDef` node is encountered during AST traversal.
#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process and analyze the Abstract Syntax Tree (AST) of a Python codebase within a Git repository. It provides functionality to parse individual Python files, extract their structural components (imports, functions, classes), and then integrate relationship data (like calls and dependencies) into the generated schema. This class serves as a core component for building a comprehensive, interconnected representation of a project's code structure.
*   **Instantiation:** This class is not explicitly instantiated by any other component within the provided context.
*   **Dependencies:** This class depends on the 'ast' module for parsing Python source code, the 'os' module for path manipulation, and 'getRepo.GitRepository' for repository interaction, as well as an 'ASTVisitor' class which is instantiated internally.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments, effectively creating a stateless instance.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, )`
        *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments, effectively creating a stateless instance.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, raw_relationships)`
        *   *Description:* This method integrates raw relationship data, such as incoming and outgoing calls, into a comprehensive AST schema. It iterates through files, functions, and classes within the 'full_schema' to enrich their context. For functions, it populates 'calls' and 'called_by' lists. For classes, it adds 'instantiated_by' information and calculates external 'dependencies' based on method calls that are not internal to the class. The method modifies the 'full_schema' in place and then returns the updated schema.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): A dictionary representing the complete Abstract Syntax Tree (AST) schema of a codebase, structured by files, functions, and classes.
            - **raw_relationships** (`dict`): A dictionary containing raw relationship data, typically with "outgoing" and "incoming" keys mapping identifiers to lists of related entities.
        *   *Returns:*
            - **full_schema** (`dict`): The modified 'full_schema' dictionary, now enriched with relationship data for functions and classes.
        *   **Usage:**
            *   **Calls:** dictionary methods like 'get', 'items', and 'add'
            *   **Called By:** This method is not explicitly called by any other function or method within the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files, repo)`
        *   *Description:* This method analyzes a list of file objects from a Git repository to construct a full AST schema. It first determines the common project root from all file paths. It then iterates through each Python file, parses its content into an AST, and uses an ASTVisitor to extract schema nodes (imports, functions, classes). The extracted schema for each file is then added to a 'full_schema' dictionary, which is returned upon completion. Error handling is included for parsing failures.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An instance of a GitRepository, though it's not directly used in the provided method body.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the aggregated AST schema for all processed Python files in the repository.
        *   **Usage:**
            *   **Calls:** `os.path.commonpath`, `os.path.isfile`, `os.path.dirname`, `ast.parse`, `ASTVisitor` (instantiation), `ASTVisitor.visit`, `print`
            *   **Called By:** This method is not explicitly called by any other function or method within the provided context.
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a file system path into a Python module import path. It first determines the relative path of the given `filepath` to the `project_root`. If a `ValueError` occurs during this process, it defaults to using only the base name of the file. It then removes the `.py` extension and replaces all operating system path separators with dots. Finally, it removes the `.__init__` suffix if the resulting module path represents an `__init__.py` file.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The Python module path derived from the filepath.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends the AST NodeVisitor to build a graph of import dependencies within Python files. It traverses the Abstract Syntax Tree of a given file, identifying both standard and 'from ... import ...' statements. Its core functionality involves resolving relative imports to their canonical forms and recording these relationships in an internal dictionary, providing a structured understanding of how files depend on each other within a repository.
*   **Instantiation:** The class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** The class depends on the 'ast' module for its core functionality as a NodeVisitor, specifically using 'Assign', 'ClassDef', 'FunctionDef', 'Import', 'ImportFrom', 'Name', 'NodeVisitor', 'literal_eval', 'parse', and 'walk'. It also relies on 'keyword.iskeyword' and 'pathlib.Path' for path manipulation and keyword checking, and an external 'get_all_temp_files' function.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph instance by setting the target filename and the repository root directory. These values are stored as instance attributes for use during the AST traversal and dependency resolution process.
    *   *Parameters:*
        - **filename** (`str`): The path to the Python file whose dependencies are to be analyzed.
        - **repo_root** (`Any`): The root directory of the repository, used for resolving file paths and relative imports.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename, repo_root)`
        *   *Description:* Initializes the FileDependencyGraph instance by setting the target filename and the repository root directory. These values are stored as instance attributes for use during the AST traversal and dependency resolution process.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **filename** (`str`): The path to the Python file whose dependencies are to be analyzed.
            - **repo_root** (`Any`): The root directory of the repository, used for resolving file paths and relative imports.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This private method is responsible for resolving relative import statements, such as 'from .. import name1, name2'. It calculates the correct module path based on the import level and the current file's location within the repository. It verifies the existence of the target module file or symbol (including those exported via '__init__.py') and returns a list of successfully resolved names. An ImportError is raised if no valid modules or symbols can be found.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of actual module or symbol names that the relative import resolves to.
        *   **Usage:**
            *   **Calls:** `get_all_temp_files`, `Path`, `Path.stem`, `Path.name`, `Path.resolve`, `Path.exists`, `Path.read_text`, `parse`, `walk`, `literal_eval`, `iskeyword`. It also defines and utilizes two nested helper functions, 'module_file_exists' and 'init_exports_symbol'.
            *   **Called By:** `visit_ImportFrom`
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method is part of the AST NodeVisitor pattern, designed to process 'Import' and 'ImportFrom' nodes. It iterates through the aliases within the import statement and records each imported module or symbol name as a dependency for the current file in the 'import_dependencies' dictionary. It then calls 'generic_visit' to ensure continued traversal of the AST.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`Import | ImportFrom`): The AST node representing either an 'import' or 'from ... import ...' statement.
            - **base_name** (`str | None`): An optional base name for the module, typically used when a specific module part has already been resolved (e.g., from a 'from ... import ...' statement).
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `self.generic_visit`
            *   **Called By:** `visit_ImportFrom` and implicitly by the AST NodeVisitor when encountering 'Import' nodes.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method, also part of the AST NodeVisitor, specifically handles 'ImportFrom' nodes. If the import is an absolute import (e.g., 'from a.b.c import d'), it extracts the base module name ('c') and passes it to 'visit_Import'. For relative imports (e.g., 'from .. import name'), it delegates the resolution to '_resolve_module_name'. Upon successful resolution, it records each resolved base name as a dependency via 'visit_Import', and includes error handling for failed relative import resolutions.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `str.split`, `self.visit_Import`, `self._resolve_module_name`, `print`, `self.generic_visit`
            *   **Called By:** This method is implicitly called by the AST NodeVisitor when traversing an 'ImportFrom' node.
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given repository. It initializes a NetworkX directed graph and then employs a `FileDependencyGraph` visitor to traverse the Abstract Syntax Tree (AST) of a specified file. The visitor collects all import dependencies, which are subsequently used to populate the graph. For each identified caller file and its imported callees, nodes are added to the graph, and directed edges are created to illustrate these relationships. The function ultimately returns the fully constructed NetworkX DiGraph.
*   **Parameters:**
    - **filename** (`str`): The path to the file whose dependencies are to be analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) object representing the source code of the file.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges indicate import dependencies from one file to another.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a directed graph representing the dependencies within a given Git repository. It iterates through all Python files in the repository, parses each file into an Abstract Syntax Tree (AST), and then uses a helper function, `build_file_dependency_graph`, to create a dependency graph for that individual file. Finally, it merges all these file-level graphs into a single global directed graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object containing the files to be analyzed for dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependencies across all Python files in the repository.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function identifies all Python files within a specified directory and its subdirectories. It takes a directory path as input, resolves it to an absolute path, and then recursively searches for all files ending with '.py'. The function returns a list of these Python files, with each file's path expressed relative to the initial root directory.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory from which to begin the search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of pathlib.Path objects, where each object represents a Python file found within the specified directory, with its path relative to the root directory.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs), specifically for generating structured documentation for Python functions and classes. It handles the configuration of different LLM providers (Gemini, OpenAI, Ollama, custom APIs), manages API keys, loads system prompts, and implements batch processing with rate limiting. The class ensures that LLM outputs conform to predefined Pydantic schemas (FunctionAnalysis and ClassAnalysis), facilitating reliable and structured data generation.
*   **Instantiation:** The class is not explicitly instantiated by any other components within the provided context.
*   **Dependencies:** The class depends on `os`, `json`, `logging`, `time`, components from the `typing` module, `dotenv.load_dotenv`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, components from `langchain.messages`, `pydantic.ValidationError`, and custom schemas like `schemas.types.FunctionAnalysis`, `schemas.types.ClassAnalysis`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, `schemas.types.ClassAnalysisInput`, `schemas.types.ClassContextInput`.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by validating the API key, loading system prompts from specified file paths, and configuring the underlying language model based on the `model_name`. It sets up different LLM clients (Google Gemini, OpenAI, Ollama, or custom) and wraps them with structured output capabilities for `FunctionAnalysis` and `ClassAnalysis` Pydantic schemas. It also calls `_configure_batch_settings` to set an appropriate batch size for API calls.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the chosen LLM service (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): File path to the system prompt for function analysis.
        - **class_prompt_path** (`str`): File path to the system prompt for class analysis.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
        - **base_url** (`str | None`): Optional base URL for custom LLM endpoints like Ollama or SCADSLLM.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, function_prompt_path, class_prompt_path, model_name, base_url)`
        *   *Description:* The constructor initializes the LLMHelper by validating the API key, loading system prompts from specified file paths, and configuring the underlying language model based on the `model_name`. It sets up different LLM clients (Google Gemini, OpenAI, Ollama, or custom) and wraps them with structured output capabilities for `FunctionAnalysis` and `ClassAnalysis` Pydantic schemas. It also calls `_configure_batch_settings` to set an appropriate batch size for API calls.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **api_key** (`str`): The API key for the chosen LLM service (e.g., Gemini, OpenAI).
            - **function_prompt_path** (`str`): File path to the system prompt for function analysis.
            - **class_prompt_path** (`str`): File path to the system prompt for class analysis.
            - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
            - **base_url** (`str | None`): Optional base URL for custom LLM endpoints like Ollama or SCADSLLM.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method sets the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It defines specific batch sizes for various Gemini, Llama, and GPT models, as well as a general batch size for custom or unknown models. The purpose is to optimize API call efficiency and respect rate limits by adjusting the number of concurrent requests. If an unknown model is encountered, it logs a warning and uses a conservative default batch size.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods or functions within its source code.
            *   **Called By:** `__init__`
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates and validates documentation for a list of `FunctionAnalysisInput` objects using the configured LLM. It processes inputs in batches, converting each input into a JSON payload and constructing a conversation with the `function_system_prompt`. The method then calls the `function_llm` (which is configured for structured output of `FunctionAnalysis`) in batches, handling potential errors by extending the result list with `None` for failed items. It includes a waiting period between batches to adhere to API rate limits.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing function details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, where each object represents the generated and validated documentation for a function, or `None` if an error occurred during generation for that specific function.
        *   **Usage:**
            *   **Calls:** `json.dumps`, `len`, `min`, `logging.info`, `logging.error`, `self.function_llm.batch`, `time.sleep`
            *   **Called By:** This method is not explicitly called by other methods within the provided `method_context`.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating and validating documentation for a list of `ClassAnalysisInput` objects. Similar to `generate_for_functions`, it processes inputs in batches, creating JSON payloads and conversations with the `class_system_prompt`. It uses the `class_llm` (configured for structured output of `ClassAnalysis`) to perform batched API calls. Error handling ensures that if a batch fails, the corresponding results are filled with `None` to maintain list order. A delay is introduced between batches to respect API rate limits.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing class details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, where each object represents the generated and validated documentation for a class, or `None` if an error occurred during generation for that specific class.
        *   **Usage:**
            *   **Calls:** `json.dumps`, `len`, `min`, `logging.info`, `logging.error`, `self.class_llm.batch`, `time.sleep`
            *   **Called By:** This method is not explicitly called by other methods within the provided `method_context`.
#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analysis inputs and outputs for several example functions (add_item, check_stock, generate_report) using Pydantic models. It then initializes an LLMHelper instance and simulates the process of generating documentation for these functions, logging the results. The function demonstrates the expected data flow and structure for the LLMHelper's operations.
*   **Parameters:**
    *Analysis data not available for this component.*
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by other functions in the provided context.

---
### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a versatile interface for interacting with various Large Language Models (LLMs), abstracting away the specifics of different providers. It handles the initialization of LLM clients (Gemini, OpenAI-compatible, Ollama) based on configuration, loads a system prompt, and provides methods for both synchronous and streaming communication with the chosen LLM. This class centralizes LLM interactions, making it easier to switch between models and manage prompts.
*   **Instantiation:** This class is not explicitly instantiated by any other components within the provided context.
*   **Dependencies:** This class relies on external libraries such as `langchain_google_genai`, `langchain_ollama`, `langchain_openai`, `langchain.messages`, and the `logging` module. It also depends on environment variables like `SCADSLLM_URL` and `OLLAMA_BASE_URL` for certain model configurations.
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by setting up the system prompt from a file and configuring the appropriate LLM client based on the `model_name`. It supports Google Generative AI (Gemini/GPT), custom OpenAI-compatible APIs (SCADSLLM_URL), and Ollama, raising errors if required environment variables or files are missing or if the API key is not provided.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the chosen LLM provider.
        - **prompt_file_path** (`str`): The file path to the system prompt that will be used for LLM interactions.
        - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This determines which LLM client is initialized.
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, used if `model_name` doesn't match specific providers like Gemini or OpenAI, or if an Ollama model is specified.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, prompt_file_path, model_name, base_url)`
        *   *Description:* The constructor initializes the MainLLM instance by setting up the system prompt from a file and configuring the appropriate LLM client based on the `model_name`. It supports Google Generative AI (Gemini/GPT), custom OpenAI-compatible APIs (SCADSLLM_URL), and Ollama, raising errors if required environment variables or files are missing or if the API key is not provided.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the class.
            - **api_key** (`str`): The API key for the chosen LLM provider.
            - **prompt_file_path** (`str`): The file path to the system prompt that will be used for LLM interactions.
            - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This determines which LLM client is initialized.
            - **base_url** (`str`): An optional base URL for custom LLM endpoints, used if `model_name` doesn't match specific providers like Gemini or OpenAI, or if an Ollama model is specified.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method performs a synchronous call to the configured LLM. It constructs a list of messages including the system prompt and the user's input, then invokes the LLM and returns the content of the response. Error handling is included to log any issues during the API call, returning None in case of an exception.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the class.
            - **user_input** (`str`): The user's query or message to send to the LLM for a synchronous response.
        *   *Returns:*
            - **content** (`str`): The textual content of the LLM's response.
            - **None** (`None`): Returns None if an error occurs during the LLM call.
        *   **Usage:**
            *   **Calls:** `SystemMessage`, `HumanMessage`, `self.llm.invoke`, `logging.info`, `logging.error`
            *   **Called By:** This method is not explicitly called by any other functions or methods within the provided context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method initiates a streaming interaction with the LLM, yielding chunks of the response as they become available. It prepares the messages with the system prompt and user input, then iterates through the LLM's stream, yielding each content chunk. In case of an error, it logs the error and yields an error message string.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the class.
            - **user_input** (`str`): The user's query or message for the streaming LLM interaction.
        *   *Returns:*
            - **chunk.content** (`str`): Yields individual content chunks from the LLM's streaming response.
            - **error_message** (`str`): Yields an error message string if an exception occurs during the streaming call.
        *   **Usage:**
            *   **Calls:** `SystemMessage`, `HumanMessage`, `self.llm.stream`, `logging.info`, `logging.error`
            *   **Called By:** This method is not explicitly called by any other functions or methods within the provided context.

---
### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract and consolidate fundamental project information from various common project files like README, pyproject.toml, and requirements.txt. It initializes an internal dictionary structure with placeholder values and then systematically parses these files to populate the fields. The class prioritizes information from pyproject.toml for dependencies and provides fallback mechanisms, such as deriving a project title from the repository URL, ensuring a comprehensive overview of the project.
*   **Instantiation:** This class is not explicitly instantiated by any known component.
*   **Dependencies:** The class depends on the 're' module for regular expression operations, the 'os' module for path manipulation, and 'tomllib' for parsing TOML files. It also uses 'typing' for type hints.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the ProjektInfoExtractor instance. It sets a constant `INFO_NICHT_GEFUNDEN` (German for "Information not found") and initializes a nested dictionary `self.info` with various project information fields, all pre-filled with this placeholder. This structure ensures that if no information is found during parsing, a default "not found" message is present.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, )`
        *   *Description:* The __init__ method initializes the ProjektInfoExtractor instance. It sets a constant `INFO_NICHT_GEFUNDEN` (German for "Information not found") and initializes a nested dictionary `self.info` with various project information fields, all pre-filled with this placeholder. This structure ensures that if no information is found during parsing, a default "not found" message is present.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content)`
        *   *Description:* This private helper method is responsible for sanitizing string content by removing null bytes (\x00). Null bytes can appear due to encoding errors, especially when a file encoded as UTF-16 is incorrectly read as UTF-8. It returns an empty string if the input content is empty, ensuring that subsequent parsing operations receive clean data.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **content** (`str`): The string content to be cleaned.
        *   *Returns:*
            - **cleaned_content** (`str`): The content with null bytes removed.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods, classes, or functions.
            *   **Called By:** `_parse_readme`, `_parse_toml`, `_parse_requirements`
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches for a file within a given list of file objects. It takes a list of filename patterns and a list of file objects, each expected to have a 'path' attribute. It performs a case-insensitive comparison of each file's path against the provided patterns, returning the first matching file object or None if no match is found.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **patterns** (`List[str]`): A list of filename patterns to search for.
            - **dateien** (`List[Any]`): A list of file objects, each expected to have a 'path' attribute.
        *   *Returns:*
            - **found_file** (`Optional[Any]`): The first file object that matches a pattern, or None if no file is found.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods, classes, or functions.
            *   **Called By:** `extrahiere_info`
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private method extracts text content located under a Markdown level 2 heading (e.g., '## Heading'). It takes the Markdown content and a list of keywords. It constructs a regular expression to find any of the keywords in a heading and captures all text following it until the next level 2 heading or the end of the document, returning the stripped text.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The Markdown content to parse.
            - **keywords** (`List[str]`): A list of keywords to match against Markdown headings.
        *   *Returns:*
            - **extracted_section** (`Optional[str]`): The stripped text content under the matched heading, or None if no matching section is found.
        *   **Usage:**
            *   **Calls:** `re.escape`, `re.compile`, `re.search`
            *   **Called By:** `_parse_readme`
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This private method parses the content of a README file to extract various project details. It first cleans the content using `_clean_content`. It then attempts to extract the project title from a level 1 Markdown heading, a general description, key features, tech stack, current status, installation instructions, and a quick start guide by calling `_extrahiere_sektion_aus_markdown` with different keyword lists. The extracted information updates the `self.info` dictionary.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The raw content of the README file.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `_clean_content`, `_extrahiere_sektion_aus_markdown`, `re.search`
            *   **Called By:** `extrahiere_info`
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This private method parses the content of a pyproject.toml file. It first cleans the content. If the `tomllib` module is not available, it prints a warning and returns. Otherwise, it attempts to load the TOML content, extract the project name, description, and dependencies from the `[project]` section, and update the `self.info` dictionary. It includes error handling for `tomllib.TOMLDecodeError`.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The raw content of the pyproject.toml file.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `_clean_content`, `tomllib.loads`, `data.get`
            *   **Called By:** `extrahiere_info`
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This private method parses the content of a requirements.txt file. It cleans the content and then extracts dependencies by splitting the content into lines, stripping whitespace, and filtering out empty lines or comments. It only updates the `self.info` dictionary's `dependencies` field if it hasn't already been populated by the TOML parser, ensuring `pyproject.toml` takes precedence.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The raw content of the requirements.txt file.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `_clean_content`
            *   **Called By:** `extrahiere_info`
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This public method orchestrates the entire information extraction process. It first identifies relevant files (README, pyproject.toml, requirements.txt) using `_finde_datei`. It then parses these files in a prioritized order (pyproject.toml, then requirements.txt, then README) to populate the `self.info` dictionary. Finally, it formats the extracted dependencies and attempts to derive a project title from the `repo_url` if no title was found elsewhere, returning the complete `self.info` dictionary.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **dateien** (`List[Any]`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo_url** (`str`): The URL of the repository, used as a fallback for the project title.
        *   *Returns:*
            - **project_info** (`Dict[str, Any]`): A dictionary containing all extracted project information.
        *   **Usage:**
            *   **Calls:** `_finde_datei`, `_parse_toml`, `_parse_requirements`, `_parse_readme`, `os.path.basename`, `repo_url.removesuffix`
            *   **Called By:** This method is not explicitly called by any other method in the provided context.

---
### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class extends `ast.NodeVisitor` to construct a directed call graph from a Python source file. It systematically traverses the Abstract Syntax Tree (AST) to identify and record function definitions, class structures, import statements, and function calls. By maintaining context about the current file, class, and function scope, it accurately resolves fully qualified names for all callable entities, ultimately building a comprehensive graph of inter-function dependencies within the analyzed code.
*   **Instantiation:** This class is not explicitly instantiated by any other components based on the provided context.
*   **Dependencies:** This class does not explicitly depend on any external components based on the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes the CallGraph instance by setting up essential attributes required for AST traversal and call graph construction. It stores the filename, initializes `current_function` and `current_class` to track scope, and sets up dictionaries and sets like `local_defs`, `import_mapping`, `function_set`, and `edges` to store collected call graph data. A `networkx.DiGraph` is also initialized to represent the graph structure.
    *   *Parameters:*
        - **filename** (`str`): The path or name of the Python source file being analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename)`
        *   *Description:* The `__init__` method initializes the CallGraph instance by setting up essential attributes required for AST traversal and call graph construction. It stores the filename, initializes `current_function` and `current_class` to track scope, and sets up dictionaries and sets like `local_defs`, `import_mapping`, `function_set`, and `edges` to store collected call graph data. A `networkx.DiGraph` is also initialized to represent the graph structure.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **filename** (`str`): The path or name of the Python source file being analyzed.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively traverses an Abstract Syntax Tree (AST) node to extract the components of a dotted name, typically representing a function or attribute call. It handles `ast.Call`, `ast.Name`, and `ast.Attribute` nodes, building a list of string parts that form the fully qualified name. For instance, `obj.method()` would yield `['obj', 'method']`, providing a structured representation of the call target.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.AST`): The AST node to be recursively analyzed, typically an `ast.Call`, `ast.Name`, or `ast.Attribute`.
        *   *Returns:*
            - **parts** (`list[str]`): A list of string components representing the dotted name of the call target.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private method takes a list of potential callee name components and resolves them to their fully qualified names. It first checks `self.local_defs` for local definitions, then `self.import_mapping` for imported entities. If no direct resolution is found, it constructs a full name using the current `filename` and `current_class` context. This ensures that call targets are accurately identified regardless of their origin (local, imported, or within the same file/class).
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains string components of a potential callee's name.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of fully qualified string names for the resolved callees.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This private utility method constructs a fully qualified name for a given base name, optionally including a class name. It prepends the `self.filename` and, if provided, the `class_name` to the `basename`, using `::` as a separator. This standardization ensures that all functions and methods within the call graph have unique and traceable identifiers, facilitating accurate graph construction and analysis.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`str | None`): The name of the class if the entity is a method; otherwise, it is None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name of the function or method as a string.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self, )`
        *   *Description:* This private helper method determines the identifier of the current calling context. If `self.current_function` is set, it returns that value, indicating an active function scope. Otherwise, it defaults to a global scope identifier, using the `self.filename` if available, or a generic `<global-scope>`. This is crucial for correctly attributing calls to their originating scope within the call graph.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
        *   *Returns:*
            - **caller_identifier** (`str`): A string representing the identifier of the current function or global scope.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method, part of the `ast.NodeVisitor` pattern, processes `ast.Import` nodes. It iterates through the aliases within the import statement, extracting the original module name and any assigned alias (`asname`). These mappings are then stored in `self.import_mapping`, which is used later to resolve calls to imported modules. After processing, it calls `generic_visit` to continue the AST traversal.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an `import` statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent `from ... import ...` statements. It extracts the base module name and then iterates through the imported names and their aliases. These mappings are stored in `self.import_mapping`, allowing the call graph builder to correctly resolve references to functions or classes imported from specific modules. It ensures proper context for resolving call targets.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a `from ... import ...` statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which define classes in the source code. It temporarily updates `self.current_class` to the name of the class being visited, ensuring that any methods defined within this class are correctly associated with it. After traversing the class's body using `self.generic_visit(node)`, it restores the `self.current_class` to its previous value, maintaining proper scope context.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, handling regular function definitions. It constructs the fully qualified name of the function using `_make_full_name` and stores it in `self.local_defs` for later resolution. It updates `self.current_function` to reflect the current scope, adds the function as a node to the `self.graph`, and records it in `self.function_set`. After traversing the function's body, it restores the previous function context.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method processes `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. It delegates the primary processing logic to the `visit_FunctionDef` method. This approach ensures that asynchronous functions are treated similarly to regular functions for the purpose of call graph construction, allowing for consistent handling of function definitions regardless of their synchronous or asynchronous nature.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method is invoked for every `ast.Call` node encountered during AST traversal, representing a function or method invocation. It first identifies the `caller` using `_current_caller` and then extracts the `callee` name components using `_recursive_call`. These components are then resolved to their fully qualified names using `_resolve_all_callee_names`. Finally, it records the call as an edge in `self.edges` from the identified caller to each resolved callee, building the core of the call graph.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method processes `ast.If` nodes, handling conditional statements. It includes special logic to detect and manage the `if __name__ == "__main__":` block, which is a common entry point in Python scripts. When this block is identified, `self.current_function` is temporarily set to `<main_block>` to correctly attribute calls within this specific execution context. For all other `if` statements, it simply proceeds with a generic AST traversal.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.If`): The AST node representing an `if` statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods, classes, or functions within its source code.
            *   **Called By:** This method is not explicitly called by any other functions or methods based on the provided context.
#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and an output file path. Its primary purpose is to create a DOT file representation of the graph where node names are 'safe' for DOT rendering, preventing issues with special characters. It achieves this by creating a copy of the graph, relabeling all nodes with simple, sequential identifiers (e.g., 'n0', 'n1'), and then storing the original node names as 'label' attributes for these new safe nodes. Finally, the modified graph is written to the specified path in DOT format.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph object to be processed and saved.
    - **out_path** (`str`): The file path where the DOT representation of the graph will be written.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions in the provided context.
#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** This function constructs a directed call graph for a given Git repository. It first iterates through all Python files in the repository, parsing their Abstract Syntax Trees (ASTs) to identify and collect all functions defined within these files into a set of 'own functions'. Subsequently, it re-processes the parsed files to detect caller-callee relationships. The function then builds a NetworkX directed graph, adding an edge only if both the calling and called functions are part of the previously identified 'own functions' set. This process effectively filters the call graph to include only internal calls within the repository's codebase, excluding external library or framework calls.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which to extract Python files and build the call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the filtered call graph, containing only edges between functions defined within the repository.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

---
### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content: str)`
*   **Description:** This function, `wrap_cdata`, takes a single string argument and encapsulates it within XML CDATA tags. It constructs a new string by prepending "<![CDATA[\n" and appending "\n]]>" to the provided content. This utility is typically used to ensure that arbitrary text, which might contain characters that would otherwise be interpreted as XML markup, is treated as plain character data by an XML parser. The function directly returns the newly formatted string.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped within CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): The input content string enclosed within `<![CDATA[\n...\n]]>` tags.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs: list, image_list: list)`
*   **Description:** This function processes a list of output objects, typically from a notebook execution, to extract relevant content. It iterates through each output, categorizing it by type. For display data or execution results, it prioritizes extracting PNG images, falling back to JPEG, and generates an image placeholder while storing the base64 image data in a provided list. If no image is found, it extracts plain text. Stream outputs are appended directly, and error outputs are formatted as error messages. The function ultimately returns a list of these extracted text strings or image placeholders.
*   **Parameters:**
    - **outputs** (`list`): A list of output objects, likely from a notebook execution, each containing data or text.
    - **image_list** (`list`): A list to which dictionaries containing image metadata and Base64 data will be appended.
*   **Returns:**
    - **extracted_xml_snippets** (`List[str]`): A list of strings, where each string is either extracted plain text, an XML-like image placeholder, or an error message.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `process_image`
*   **Signature:** `def process_image(mime_type: str)`
*   **Description:** This function processes image data based on a provided MIME type. It checks if the MIME type exists within an external 'data' dictionary. If found, it retrieves and cleans a base64 encoded string, appends a dictionary containing the MIME type and cleaned data to an external 'image_list', and returns a formatted placeholder string. Error handling is included to catch decoding issues, returning an error message string in such cases. If the MIME type is not present in 'data', the function returns None.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed, used as a key to retrieve its base64 encoded data from an external source.
*   **Returns:**
    - **image_placeholder_tag** (`str`): A formatted string representing an image placeholder, including its assigned index and MIME type, if processing is successful.
    - **error_message** (`str`): An error message string indicating that the image could not be decoded due to an exception.
    - **None** (`NoneType`): Returns None if the specified MIME type is not found in the 'data' dictionary.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content: str)`
*   **Description:** This function takes the raw content of a Jupyter notebook as a string and converts it into an XML representation. It processes each cell, distinguishing between markdown and code cells. Markdown cell content is directly embedded, while code cell source is wrapped. If code cells have outputs, these are also processed and included in the XML, and any embedded images are extracted. The function handles potential parsing errors by returning a specific error message.
*   **Parameters:**
    - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be in JSON format.
*   **Returns:**
    - **xml_output** (`str`): A string containing the XML representation of the notebook cells, or an error message if parsing fails.
    - **extracted_images** (`list`): A list of extracted images from the notebook outputs.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files: list)`
*   **Description:** This function processes a list of repository files to identify Jupyter notebooks. It iterates through these identified notebooks, converting each one into an XML representation and extracting any associated images. The function then compiles these conversion results into a dictionary, where each notebook's path maps to its generated XML and extracted images.
*   **Parameters:**
    - **repo_files** (`List[object]`): A list of file objects from a repository. Each object is expected to have a 'path' attribute (string) for file identification and a 'content' attribute for the notebook's raw content.
*   **Returns:**
    - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the paths of the processed Jupyter notebooks (string). Each value is another dictionary containing the 'xml' output (string) and 'images' (list of any type) generated from the notebook conversion.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, designed for efficient access to its content and metadata. It employs a lazy-loading strategy for the Git blob object, file content, and size, ensuring these resources are only retrieved when explicitly requested. This class provides structured properties to access the file's underlying Git blob, its decoded content, and its size, along with utility methods for basic content analysis and serialization into a dictionary format.
*   **Instantiation:** No specific instantiation points for this class are identified in the provided context.
*   **Dependencies:** No external dependencies are explicitly listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes a RepoFile object by storing the file's path and the Git Tree object from which it originates. It also sets up internal attributes (`_blob`, `_content`, `_size`) to None, indicating that the file's Git blob, content, and size will be loaded lazily upon first access.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, file_path, commit_tree)`
        *   *Description:* The constructor initializes a RepoFile object by storing the file's path and the Git Tree object from which it originates. It also sets up internal attributes (`_blob`, `_content`, `_size`) to None, indicating that the file's Git blob, content, and size will be loaded lazily upon first access.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
            - **file_path** (`str`): The path to the file within the repository.
            - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`blob`**
        *   *Signature:* `def blob(self, )`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if the `_blob` attribute is already set; if not, it attempts to retrieve the blob from the `_tree` using the stored `path`. If the file is not found in the commit tree, it raises a `FileNotFoundError` to indicate the issue.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:**
            *   **Calls:** No external functions or methods are explicitly called by this method according to the provided context.
            *   **Called By:** No other functions or methods are identified as calling this method in the provided context.
    *   **`content`**
        *   *Signature:* `def content(self, )`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It first checks if the `_content` attribute is None. If so, it accesses the `blob` property to get the Git blob, reads its data stream, and decodes it using UTF-8, ignoring any decoding errors. The decoded string content is then stored and returned for subsequent access.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:**
            *   **Calls:** No external functions or methods are explicitly called by this method according to the provided context.
            *   **Called By:** No other functions or methods are identified as calling this method in the provided context.
    *   **`size`**
        *   *Signature:* `def size(self, )`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the `_size` attribute is None. If it is, it accesses the `blob` property to get the Git blob and retrieves its `size` attribute. The file size is then stored internally and returned, avoiding redundant calculations.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   **Calls:** No external functions or methods are explicitly called by this method according to the provided context.
            *   **Called By:** No other functions or methods are identified as calling this method in the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self, )`
        *   *Description:* This method serves as an example analysis function, demonstrating how to process the file's content. It calculates and returns the total number of words present in the file's content. It achieves this by first accessing the `content` property to retrieve the file's text, then splitting the content string by whitespace, and finally returning the length of the resulting list of words.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **word_count** (`int`): The total number of words in the file content.
        *   **Usage:**
            *   **Calls:** No external functions or methods are explicitly called by this method according to the provided context.
            *   **Called By:** No other functions or methods are identified as calling this method in the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self, )`
        *   *Description:* This special method provides a developer-friendly string representation of the RepoFile object. It constructs a concise string that includes the class name and the path of the file. This representation is useful for debugging, logging, and quickly identifying instances of the RepoFile class.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:**
            *   **Calls:** No external functions or methods are explicitly called by this method according to the provided context.
            *   **Called By:** No other functions or methods are identified as calling this method in the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method converts the RepoFile object into a dictionary representation, making it suitable for serialization or structured data exchange. It includes essential metadata such as the file's path, its base name, its size, and its type. Optionally, the file's content can be included in the dictionary if the `include_content` parameter is set to True.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
            - **include_content** (`bool`): A flag indicating whether the file's content should be included in the dictionary. Defaults to False.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing the file's metadata and optionally its content.
        *   **Usage:**
            *   **Calls:** No external functions or methods are explicitly called by this method according to the provided context.
            *   **Called By:** No other functions or methods are identified as calling this method in the provided context.
#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with remote Git repositories. It handles the cloning of a specified repository into a temporary local directory, manages the retrieval of all files as RepoFile objects, and can construct a hierarchical file tree. Furthermore, it implements the context manager protocol, ensuring proper cleanup of the temporary directory upon exiting a 'with' block or in case of initialization errors.
*   **Instantiation:** The input context indicates that this class is not explicitly instantiated by any known components within the provided context.
*   **Dependencies:** The class depends on tempfile for temporary directory management, git.Repo and git.GitCommandError from the git library for Git operations, and logging for informational messages.
*   **Constructor:**
    *   *Description:* The constructor initializes the GitRepository by cloning a remote Git repository into a temporary local directory. It sets up attributes like the repository URL, the path to the temporary directory, the git.Repo object, and the latest commit and its tree. It handles potential GitCommandError during cloning by cleaning up the temporary directory.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, repo_url)`
        *   *Description:* The constructor initializes the GitRepository by cloning a remote Git repository into a temporary local directory. It sets up attributes like the repository URL, the path to the temporary directory, the git.Repo object, and the latest commit and its tree. It handles potential GitCommandError during cloning by cleaning up the temporary directory.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
            - **repo_url** (`str`): The URL of the Git repository to clone.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self, )`
        *   *Description:* This method retrieves all file paths from the cloned Git repository using 'git.ls_files()'. It then creates a list of RepoFile objects, one for each file path, associating them with the repository's commit tree. This list of RepoFile objects is stored internally in 'self.files' and returned.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:*
            - **null** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:**
            *   **Calls:** `self.repo.git.ls_files()`, `RepoFile`
            *   **Called By:** `get_file_tree`
    *   **`close`**
        *   *Signature:* `def close(self, )`
        *   *Description:* This method is responsible for cleaning up the temporary directory where the Git repository was cloned. It checks if 'self.temp_dir' is set, prints a message indicating deletion, and then sets 'self.temp_dir' to None. This prevents further access to the deleted directory.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods or functions, but it interacts with the file system implicitly by indicating deletion of self.temp_dir.
            *   **Called By:** `__init__`, `__exit__`
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self, )`
        *   *Description:* This special method makes the GitRepository class compatible with the 'with' statement (context manager protocol). When entering a 'with' block, it simply returns the instance of the GitRepository itself, allowing it to be bound to a variable.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:*
            - **null** (`GitRepository`): The instance of the GitRepository itself.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods or functions.
            *   **Called By:** This method is implicitly called when a GitRepository instance is used in a 'with' statement.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This special method is part of the context manager protocol and is automatically called when exiting a 'with' block, regardless of whether an exception occurred. Its primary responsibility is to ensure that the temporary directory created for the repository is cleaned up by calling the 'close' method.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
            - **exc_type** (`type | None`): The type of the exception that caused the exit, or None if no exception occurred.
            - **exc_val** (`Exception | None`): The exception instance that caused the exit, or None.
            - **exc_tb** (`traceback | None`): The traceback object associated with the exception, or None.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `self.close()`
            *   **Called By:** This method is implicitly called when exiting a 'with' statement that uses a GitRepository instance.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method constructs a hierarchical tree representation of the files within the Git repository. If 'self.files' is not already populated, it first calls 'get_all_files' to retrieve them. It then iterates through each RepoFile object, splitting its path to build nested dictionary structures representing directories and files. Each file is appended to its corresponding directory's children list, optionally including file content.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
            - **include_content** (`bool`): If True, the content of each file will be included in its dictionary representation.
        *   *Returns:*
            - **null** (`dict`): A dictionary representing the hierarchical file tree of the repository.
        *   **Usage:**
            *   **Calls:** `self.get_all_files()`, `file_obj.to_dict()`
            *   **Called By:** The input method_context does not specify any callers for this method.

---
### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart comparing two token counts, `json_tokens` and `toon_tokens`. It visualizes these values using distinct colors and includes a title that displays a calculated `savings_percent`. The chart features a y-axis label, a grid, and explicitly shows the token count values above each bar for clarity. Finally, the function saves the generated chart to the specified `output_path` and closes the plot to release resources.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens representing the JSON format.
    - **toon_tokens** (`int`): The number of tokens representing the TOON format.
    - **savings_percent** (`float`): The percentage of savings to be displayed in the chart's title.
    - **output_path** (`str`): The file path where the generated bar chart will be saved.
*   **Returns:**
    - **None** (`None`): This function does not explicitly return any value; it saves a file as a side effect.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.
#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the net processing time, accounting for potential sleep durations introduced by rate-limiting, specifically for 'gemini-' models. It first determines the total elapsed time between a start and end timestamp. If the model_name does not begin with 'gemini-', the total duration is returned directly. For 'gemini-' models, it calculates the number of batches based on total_items and batch_size, then estimates the total sleep time. The net time is derived by subtracting this estimated sleep time from the total duration, ensuring the result is non-negative.
*   **Parameters:**
    - **start_time** (`float`): The timestamp when the process began.
    - **end_time** (`float`): The timestamp when the process concluded.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed per batch.
    - **model_name** (`str`): The name of the model used, which influences rate-limit calculations.
*   **Returns:**
    - **net_time** (`float`): The calculated duration in seconds, adjusted for rate-limiting sleep times, or the total duration if no rate-limiting adjustment is needed.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.
#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable | None)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive analysis pipeline for a given GitHub repository. It begins by extracting API keys and model names from the provided inputs, then clones the specified repository URL. The function proceeds to extract basic project information, construct a file tree, analyze code relationships, and build an Abstract Syntax Tree (AST) schema, which is subsequently enriched with relationship data. It then prepares and dispatches analysis tasks for individual functions and classes to a Helper LLM, before finally utilizing a Main LLM to synthesize a comprehensive report based on all collected and analyzed data. The process includes status updates, error handling, token evaluation, and saving the final report along with performance metrics.
*   **Parameters:**
    - **input** (`str`): The initial user input, expected to contain a GitHub repository URL for analysis.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions and other services.
    - **model_names** (`dict`): A dictionary specifying the names of the models to be used for the 'helper' and 'main' LLMs in the workflow.
    - **status_callback** (`callable | None`): An optional callable function used to provide progress updates throughout the workflow.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM, detailing the repository analysis.
    - **metrics** (`dict`): A dictionary containing performance metrics such as helper_time, main_time, total_time, helper_model, main_model, json_tokens, toon_tokens, and savings_percent.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `update_status`
*   **Signature:** `def update_status(msg: str)`
*   **Description:** This function is designed to handle status updates. It accepts a message string as input. It first checks if a 'status_callback' is defined in the current scope; if so, it invokes this callback with the provided message. Subsequently, it logs the message at the INFO level using the 'logging' module, ensuring the message is recorded.
*   **Parameters:**
    - **msg** (`str`): The message string to be processed, potentially passed to a status callback, and logged.
*   **Returns:**
    - **None** (`None`): This function performs side effects by potentially invoking a callback and logging a message; it does not return any explicit value.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback: callable | None)`
*   **Description:** The notebook_workflow function orchestrates the analysis of Jupyter notebooks from a given GitHub repository. It clones the repository, extracts basic project information, converts notebooks to an XML-like structure with image placeholders, and then iteratively processes each notebook using a specified Large Language Model (LLM). It constructs a payload for the LLM, handles different LLM API key configurations, and aggregates individual notebook reports into a final markdown report, which is then saved to a file. Finally, it returns the combined report and execution metrics.
*   **Parameters:**
    - **input** (`str`): The input string, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing API keys for various LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
    - **model** (`str`): The name of the LLM model to be used for notebook analysis (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`callable | None`): An optional callback function to provide status updates during the workflow execution. If provided, it will be called with status messages.
*   **Returns:**
    - **report** (`str`): A concatenated markdown string containing the analysis reports for all processed notebooks.
    - **metrics** (`dict`): A dictionary containing execution metrics such as 'helper_time', 'main_time', 'total_time', 'helper_model', 'main_model', 'json_tokens', 'toon_tokens', and 'savings_percent'.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by other functions in the provided context.
#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info: object, nb_path: str, xml_content: str, images: list)`
*   **Description:** This function constructs a multi-part payload suitable for the Gemini API, integrating textual content with base64-encoded images. It begins by serializing basic information and a notebook path into an introductory JSON string. The core logic involves parsing an XML-like string that may contain image placeholders. It extracts text segments and replaces image placeholders with corresponding base64 image data from a provided list. The function ultimately returns a list of dictionaries, each representing either a text or an image part, formatted for a generative AI model's input.
*   **Parameters:**
    - **basic_info** (`object`): A dictionary or object containing basic contextual information to be included in the payload.
    - **nb_path** (`str`): The file path of the current notebook, used as part of the contextual information.
    - **xml_content** (`str`): An XML-like string representing the notebook's content, which may include special image placeholder tags.
    - **images** (`list`): A list of image data objects, where each object is expected to contain 'data' (base64 string) and 'mime' type.
*   **Returns:**
    - **payload_content** (`list[dict]`): A list of dictionaries, each formatted as a content part (either 'text' or 'image_url') for the Gemini API.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

---
### File: `backend/relationship_analyzer.py`

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform static analysis on a Python project to build a comprehensive call graph. It identifies all Python files, collects definitions of classes, functions, and methods, and then resolves the call relationships between these entities. The class provides methods to initiate the analysis, retrieve the raw call graph, and format the relationships into incoming and outgoing structures, offering a structured view of code dependencies.
*   **Instantiation:** This class is not explicitly instantiated by other functions or methods within the provided context.
*   **Dependencies:** This class depends on `os` for file system operations, `ast` for parsing Python code, `logging` for error reporting, and `collections.defaultdict` for its internal graph representation. It also implicitly depends on `path_to_module` and `CallResolverVisitor` which are not defined in the provided source but are used.
*   **Constructor:**
    *   *Description:* This method initializes a new ProjectAnalyzer instance. It sets the project's root directory, initializes internal data structures such as dictionaries for definitions, a defaultdict for the call graph, and a dictionary for storing file ASTs. It also defines a set of directories to be ignored during the analysis process.
    *   *Parameters:*
        - **project_root** (`str`): The absolute path to the root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, project_root)`
        *   *Description:* This method initializes a new ProjectAnalyzer instance. It sets the project's root directory, initializes internal data structures such as dictionaries for definitions, a defaultdict for the call graph, and a dictionary for storing file ASTs. It also defines a set of directories to be ignored during the analysis process.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **project_root** (`str`): The absolute path to the root directory of the Python project to be analyzed.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`analyze`**
        *   *Signature:* `def analyze(self, )`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect definitions of functions, classes, and methods. Subsequently, it iterates through the files again to resolve call relationships between these defined entities. Finally, it clears the stored ASTs to free up memory and returns the populated call graph.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary-like structure representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:**
            *   **Calls:** `_find_py_files`, `_collect_definitions`, `_resolve_calls`
            *   **Called By:** This method is not explicitly called by other functions or methods within the provided context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self, )`
        *   *Description:* This method processes the internal `call_graph` to generate two dictionaries: `outgoing` and `incoming` relationships. It iterates through the call graph, extracting caller and callee identifiers, and populates sets for outgoing calls from a caller and incoming calls to a callee. The final output provides sorted lists of these relationships, offering a clear view of dependencies.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, 'outgoing' and 'incoming'. Each key maps to a dictionary where keys are entity identifiers and values are sorted lists of related entity identifiers.
        *   **Usage:**
            *   **Calls:** `defaultdict`, `list`, `sorted`
            *   **Called By:** This method is not explicitly called by other functions or methods within the provided context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self, )`
        *   *Description:* This private helper method is responsible for recursively traversing the project root directory to locate all Python files. It uses `os.walk` to navigate the directory structure, filtering out specified `ignore_dirs` to avoid analyzing irrelevant content. It compiles a list of absolute paths to all discovered Python files.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found within the project root, excluding ignored directories.
        *   **Usage:**
            *   **Calls:** `os.walk`, `os.path.join`
            *   **Called By:** `analyze`
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method parses a given Python file to identify and record definitions of classes, functions, and methods. It reads the file, parses its content into an Abstract Syntax Tree (AST), and then walks the AST to find `FunctionDef` and `ClassDef` nodes. For each definition, it constructs a unique path name and stores its file path, line number, and type in the `self.definitions` dictionary, also storing the AST in `self.file_asts`.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **filepath** (`str`): The absolute path to the Python file being analyzed.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `open`, `ast.parse`, `ast.walk`, `_get_parent`, `path_to_module` (an external utility), `logging.error`, `isinstance`, `ast.FunctionDef`, `ast.ClassDef`
            *   **Called By:** `analyze`
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This private helper method traverses an Abstract Syntax Tree (AST) to find the immediate parent node of a given child node. It iterates through all nodes in the tree and checks their children to identify if any child matches the provided node. If a match is found, the parent node is returned.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent_node** (`ast.AST | None`): The parent AST node of the given `node`, or `None` if no parent is found (e.g., if `node` is the root of the `tree`).
        *   **Usage:**
            *   **Calls:** `ast.walk`, `ast.iter_child_nodes`
            *   **Called By:** `_collect_definitions`
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method processes the AST of a given file to identify and resolve function and method calls. It retrieves the pre-parsed AST for the file and then uses a `CallResolverVisitor` (an external class) to traverse the AST and detect calls. The resolved calls, along with their caller information, are then extended into the class's `self.call_graph`.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **filepath** (`str`): The absolute path to the Python file whose calls are to be resolved.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** `self.file_asts.get`, `CallResolverVisitor` instantiation, `resolver.visit`, `logging.error`
            *   **Called By:** `analyze`
#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST NodeVisitor designed to traverse an Abstract Syntax Tree (AST) of Python code to identify and resolve function and method calls. It maintains a scope of imported names and instantiated object types to accurately determine the fully qualified name of called entities. The visitor collects information about each call, including the caller's identifier, file, line number, and type, storing these relationships for later analysis.
*   **Instantiation:** The class is not explicitly instantiated by any known components according to the provided context.
*   **Dependencies:** The class does not have explicit external dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallResolverVisitor with the current file path, the project's root directory, and a dictionary of known definitions. It sets up internal state variables such as `module_path`, `scope`, `instance_types`, `current_caller_name`, `current_class_name`, and a `defaultdict` to store discovered calls.
    *   *Parameters:*
        - **filepath** (`str`): The path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the project, used to determine module paths.
        - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) within the project, used for validation.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filepath, project_root, definitions)`
        *   *Description:* The constructor initializes the CallResolverVisitor with the current file path, the project's root directory, and a dictionary of known definitions. It sets up internal state variables such as `module_path`, `scope`, `instance_types`, `current_caller_name`, `current_class_name`, and a `defaultdict` to store discovered calls.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **filepath** (`str`): The path to the Python file being analyzed.
            - **project_root** (`str`): The root directory of the project, used to determine module paths.
            - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) within the project, used for validation.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *Analysis data not available for this component.*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is invoked when the AST visitor encounters a class definition. It updates the `current_class_name` attribute to reflect the newly entered class scope. After visiting all child nodes within the class, it restores the `current_class_name` to its previous value, ensuring correct scope management during AST traversal.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods according to the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method is called when the AST visitor encounters a function definition (either a global function or a method within a class). It constructs a fully qualified identifier for the function, incorporating the module and class name if applicable. This identifier is then set as `current_caller_name` for subsequent call resolution within the function's body, and the previous caller name is restored upon exiting the function's scope.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods according to the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method processes function and method call expressions within the AST. It attempts to resolve the fully qualified name of the called entity using the `_resolve_call_qname` helper method. If the callee's qualified name is successfully resolved and exists in the known definitions, it records the call, including the caller's file, line number, full identifier, and type (module, local function, or method). This information is stored in the `self.calls` dictionary.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods according to the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method handles `import` statements in the source code. It iterates through the imported names and their aliases, storing the mapping from the alias (or original name) to the full module name in the `self.scope` dictionary. This allows the visitor to resolve imported names later during call analysis.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods according to the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `from ... import ...` statements. It determines the full module path for the imported names, considering relative imports (`node.level`). It then stores the mapping from the imported name (or its alias) to its fully qualified path in the `self.scope` dictionary, enabling accurate resolution of imported entities.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods according to the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method processes assignment statements to identify instances of class instantiation. If an assignment involves a call to a name that is resolved as a known class within the `self.scope` and `self.definitions`, it records the qualified class name associated with the assigned variable. This information is stored in `self.instance_types` to help resolve method calls on these instances later.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
            *Analysis data not available for this component.*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods according to the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods according to the provided context.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method attempts to determine the fully qualified name (QName) of a function or method being called. It handles various scenarios: direct name calls (checking `self.scope` and local module paths), and attribute calls on variables (checking `self.instance_types` for class instances or `self.scope` for module attributes). It returns the resolved QName as a string or `None` if it cannot be resolved.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., `ast.Name` or `ast.Attribute`).
        *   *Returns:*
            - **None** (`str | None`): The fully qualified name of the called entity if resolved, otherwise None.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods according to the provided context.
            *   **Called By:** This method is not explicitly called by other functions or methods according to the provided context.
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into a Python module path string. It first attempts to calculate the path relative to a specified project root. If that fails, it uses the base name of the file. It then removes the '.py' extension if present, replaces path separators with dots, and finally adjusts for '__init__.py' files to represent their parent package.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/scads_key_test.py`
*Analysis data not available for this component.*
---
### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** The `encrypt_text` function is designed to encrypt a given string using a `cipher_suite` object. It first performs a check: if the input `text` is empty or if `cipher_suite` is not initialized, the function bypasses encryption and returns the original text. Otherwise, it prepares the text by stripping leading/trailing whitespace, encodes it to bytes, performs the encryption, and then decodes the encrypted bytes back into a string before returning it.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string. If the input text is empty or `cipher_suite` is unavailable, the original text is returned.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given string using an external `cipher_suite` object. It first checks if the input `text` is empty or if `cipher_suite` is not initialized, returning the original text immediately in such cases. If conditions are met, it proceeds to decrypt the text by stripping leading/trailing whitespace, encoding it to bytes, applying the `cipher_suite.decrypt` method, and then decoding the result back into a string. The function includes error handling, returning the original, unencrypted text if any exception occurs during the decryption process.
*   **Parameters:**
    - **text** (`str`): The string value that needs to be decrypted.
*   **Returns:**
    - **decrypted_or_original_text** (`str`): The decrypted string if the operation is successful, or the original string if decryption fails or if the initial conditions (non-empty text and initialized cipher_suite) are not met.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function creates a new user document and inserts it into a database collection. It accepts a username, display name, and a plain-text password. The provided password is first hashed using `stauth.Hasher.hash` for security before being stored. The user document also includes initialized empty fields for Gemini, Ollama, and GPT API keys. Finally, the function inserts this prepared user document into the `dbusers` collection and returns the unique identifier of the newly created document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user.
    - **name** (`str`): The display name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier of the newly inserted user document.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is designed to retrieve all user records from a database collection. It executes a find operation on the `dbusers` collection, which is presumed to be a database interface. The results, typically a cursor of documents, are then converted into a standard Python list. This list, containing all fetched user data, is subsequently returned by the function.
*   **Parameters:**
    *Analysis data not available for this component.*
*   **Returns:**
    - **users** (`list`): A list containing all user documents fetched from the 'dbusers' collection. Each item in the list represents a user record.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.
#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The `fetch_user` function is designed to retrieve a single user record from a database collection. It takes a username as input and uses it to query the `dbusers` collection. The function specifically searches for a document where the `_id` field matches the provided username, returning the first matching document found or `None` if no user is found.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be retrieved from the database.
*   **Returns:**
    - **user_document** (`dict | None`): The user document as a dictionary if a matching user is found, otherwise `None`.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.
#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function is designed to update a user's name in a database. It takes the existing username, which serves as the unique identifier (`_id`), and a new name. The function performs an update operation on the `dbusers` collection, specifically setting the 'name' field for the matching user. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose name is to be updated, corresponding to the `_id` field in the database.
    - **new_name** (`str`): The new name to assign to the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 0 indicates no document was found or updated.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in a database. It takes a username and the new Gemini API key as input. The provided API key is first stripped of any leading/trailing whitespace and then encrypted. Finally, it attempts to locate a user document by its username and updates the 'gemini_api_key' field with the encrypted value. The function returns the count of documents that were successfully modified.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored, which will be encrypted before being saved to the database.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation. This is typically 0 or 1, indicating whether the user's key was successfully updated.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** This function updates a user's GPT API key in the database. It takes a username and a plain-text GPT API key as input. The provided API key is first stripped of leading/trailing whitespace and then encrypted. The encrypted key is then stored in the 'gpt_api_key' field for the specified user in the 'dbusers' collection.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new plain-text GPT API key to be stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specific user in a database. It takes a username and a new Ollama base URL as input. The provided URL is first stripped of any leading or trailing whitespace before being stored. The function then performs an update operation on the database, targeting the document identified by the username. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Ollama base URL needs to be updated.
    - **ollama_base_url** (`str`): The new Ollama base URL to be set for the specified user. Any leading or trailing whitespace will be removed before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. This will typically be 1 if the user exists and the URL was updated, or 0 if the user was not found or the URL was already the same.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function updates a user's Open Source API key in the database. It first encrypts the provided API key after removing leading/trailing whitespace. Then, it uses the `dbusers` collection to find the user by their username and sets the `opensrc_api_key` field to the newly encrypted value. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API key is to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database by the update operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.
#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** This function updates a user's open-source base URL in the database. It takes a username and a new URL as input. The function performs an update operation on the `dbusers` collection, setting the `opensrc_base_url` field for the document matching the provided username. The `opensrc_base_url` is stripped of leading and trailing whitespace before being stored. It returns the count of modified documents.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose open-source base URL needs to be updated.
    - **opensrc_base_url** (`str`): The new open-source base URL to be set for the user. This value will be stripped of whitespace.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** The `fetch_gemini_key` function retrieves a user's Gemini API key from a database. It accepts a `username` string to identify the specific user. The function queries the `dbusers` collection, searching for a document where the `_id` matches the provided `username`. It then extracts the `gemini_api_key` field from the found user document. If a user is found and has a Gemini API key, that key is returned; otherwise, the function returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key associated with the user, or None if the user is not found or the key does not exist.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL for a specified user from a database. It queries the `dbusers` collection using the provided username as the `_id`. The function specifically projects the `ollama_base_url` field. It returns the extracted URL if a user is found and the URL exists, otherwise it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL associated with the user, or None if the user is not found or the URL is not set.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** This function, `fetch_gpt_key`, is responsible for retrieving a user's GPT API key from a database. It queries the `dbusers` collection, using the provided `username` as the document's `_id` to locate the specific user. The function is designed to project only the `gpt_api_key` field from the found document. It returns the API key as a string if a user is found and has an associated key, otherwise it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the user, or None if the user or key is not found.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.
#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** This function, `fetch_opensrc_key`, is designed to retrieve an Open Source API key associated with a specific user from a database. It takes a username as input and queries the `dbusers` collection to find the corresponding user document. If a user is found, it extracts the `opensrc_api_key` from that document. The function returns the API key if present, or `None` otherwise.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) for which to retrieve the Open Source API key.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key associated with the provided username, or None if the user or key is not found.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.
#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** This function is designed to retrieve a user's Open Source base URL from a database. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided 'username'. If a user document is found, it extracts the 'opensrc_base_url' field. The function then returns this URL. If no user is found or the 'opensrc_base_url' field is absent, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The Open Source base URL associated with the user, or None if the user is not found or the URL is not set.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is designed to remove a user record from a database collection. It takes a username as input and uses it to identify the document to be deleted. The function performs a delete operation on the `dbusers` collection, targeting the document where the `_id` field matches the provided username. It returns the count of documents successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents (users) that were successfully deleted from the collection. Typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves a user's API keys and base URLs from a database. It queries the 'dbusers' collection using the provided username. If the user is found, it decrypts specific API keys (Gemini, GPT, and open-source) using a 'decrypt_text' function and retrieves other URLs directly. The function returns a tuple containing all the processed keys and URLs. If the user is not found, it returns a tuple of two None values.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user is not found.
    - **ollama_plain** (`str | None`): The Ollama base URL, or None if the user is not found.
    - **gpt_plain** (`str | None`): The decrypted GPT API key, or None if the user is not found.
    - **opensrc_plain** (`str | None`): The decrypted open-source API key, or None if the user is not found.
    - **opensrc_url** (`str | None`): The open-source base URL, or None if the user is not found.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** The `insert_chat` function is responsible for creating a new chat entry within a database. It constructs a dictionary representing the chat, assigning a unique ID using `uuid.uuid4()`, the provided `username` and `chat_name`, and the current timestamp via `datetime.now()`. This chat document is then persisted to a MongoDB collection, likely `dbchats`, using the `insert_one` method. The function concludes by returning the unique `inserted_id` generated by the database for the new entry.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier of the newly created chat entry in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** This function retrieves all chat documents associated with a specific user from a database collection. It queries the 'dbchats' collection for documents where the 'username' field matches the provided input. The retrieved chats are then sorted in ascending order based on their 'created_at' timestamp before being returned as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the associated chat documents.
*   **Returns:**
    - **chats** (`list`): A list of chat documents (dictionaries) belonging to the specified user, sorted by their creation date.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function, `check_chat_exists`, is designed to verify the presence of a specific chat within the `dbchats` collection. It takes a username and a chat name as input parameters. The function executes a query to find a document that matches both the provided username and chat name. It returns a boolean value indicating whether such a chat exists in the database.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked for existence.
*   **Returns:**
    - **exists** (`bool`): Returns `True` if a chat with the specified username and chat name is found in the `dbchats` collection, otherwise returns `False`.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and all its associated exchanges (messages) in the database. It first updates the chat entry in the 'dbchats' collection by changing the 'chat_name' from 'old_name' to 'new_name' for a specific 'username'. Subsequently, it updates all related exchanges in the 'dbexchanges' collection, also changing their 'chat_name' from 'old_name' to 'new_name' for the same 'username'. The function returns the count of modified chat entries from the initial update operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The desired new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat entries that were modified by the update_one operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.
#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str, json_tokens: int, toon_tokens: int, savings_percent: float)`
*   **Description:** This function inserts a new exchange record into a database collection. It generates a unique identifier for the record using `uuid.uuid4()` and constructs a dictionary containing the question, answer, feedback, user details, chat name, and various optional performance metrics like helper/main models used, time taken, and token counts. A `created_at` timestamp is added using `datetime.now()`. The function attempts to insert this prepared record into the `dbexchanges` collection. If successful, it returns the new record's ID; otherwise, it catches any exceptions, prints an error, and returns `None`.
*   **Parameters:**
    - **question** (`str`): The user's question in the exchange.
    - **answer** (`str`): The generated answer for the question.
    - **feedback** (`str`): The feedback provided for the exchange.
    - **username** (`str`): The username associated with the exchange.
    - **chat_name** (`str`): The name of the chat where the exchange occurred.
    - **helper_used** (`str`): Optional: Information about the helper model used, defaults to an empty string.
    - **main_used** (`str`): Optional: Information about the main model used, defaults to an empty string.
    - **total_time** (`str`): Optional: The total time taken for the exchange, defaults to an empty string.
    - **helper_time** (`str`): Optional: The time spent by the helper model, defaults to an empty string.
    - **main_time** (`str`): Optional: The time spent by the main model, defaults to an empty string.
    - **json_tokens** (`int`): Optional: The number of JSON tokens used, defaults to 0.
    - **toon_tokens** (`int`): Optional: The number of Toon tokens used, defaults to 0.
    - **savings_percent** (`float`): Optional: The percentage of savings achieved, defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly inserted exchange record if the operation is successful.
    - **None** (`None`): Returned if an exception occurs during the database insertion.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function is designed to retrieve all exchange records associated with a specific user from a database. It queries the `dbexchanges` collection using the provided username as a filter. The results are then sorted chronologically by their 'created_at' timestamp in ascending order. Finally, the function returns these sorted exchange records as a list, facilitating their display or further processing.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose exchange records are to be fetched.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents (dictionaries) belonging to the specified user, sorted by their creation timestamp.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a list of exchange documents from a database collection named `dbexchanges`. It filters these documents based on a provided username and a specific chat name. The results are then sorted by their `created_at` timestamp in ascending order and returned as a list.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchanges.
    - **chat_name** (`str`): The name of the chat used to filter the exchanges.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents matching the specified username and chat name, sorted by creation time.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function is responsible for updating the feedback score associated with a specific exchange record in a database. It accepts an exchange identifier and an integer feedback value. The function performs an update operation on the 'dbexchanges' collection, targeting the document with the matching '_id' and setting its 'feedback' field to the provided integer. It then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange record that needs its feedback updated. This is used to locate the specific document in the database.
    - **feedback** (`int`): The integer value representing the new feedback score to be assigned to the specified exchange record.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified as a result of the update operation. A value of 1 typically indicates a successful update, while 0 suggests no matching document was found or no change was necessary.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates a specific exchange record in a database collection named 'dbexchanges'. It identifies the target record using the provided 'exchange_id' and sets its 'feedback_message' field to the new string value. The function then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange record to be updated. This is used to match the '_id' field in the database.
    - **feedback_message** (`str`): The new string value to be set as the feedback message for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. This will typically be 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.
#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is designed to remove a specific exchange record from a database collection. It accepts a unique identifier, `exchange_id`, and uses it to locate and delete a single document within the `dbexchanges` collection. The function then reports the number of documents successfully deleted, which will typically be 1 if a match was found and removed, or 0 otherwise.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted (0 or 1).
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is designed to completely remove a specific chat and all its associated message exchanges from the database. It operates by first deleting all message exchanges linked to the provided username and chat name, and then proceeds to delete the chat entry itself. This two-step process ensures data consistency between the frontend and backend systems. The function returns the count of chat documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted from the database. This will typically be 0 or 1 for a delete_one operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list: List[str])`
*   **Description:** This function processes a list of strings, where each string is expected to represent a path or an identifier containing forward slashes. It iterates through the provided list and for each item, it splits the string by the '/' character. The function then extracts and returns only the last segment of the split string, effectively cleaning the names to their base components.
*   **Parameters:**
    - **model_list** (`List[str]`): A list of strings, where each string is expected to be a path-like identifier that may contain '/' characters.
*   **Returns:**
    - **cleaned_names** (`List[str]`): A new list containing the last segment of each input string after splitting by '/', effectively providing cleaned base names.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list: list, category_name: str)`
*   **Description:** This function filters a given list of models, referred to as `source_list`, based on a specified `category_name`. It retrieves a set of keywords associated with the category from a global `CATEGORY_KEYWORDS` mapping. If the category's keywords include "STANDARD", the function returns only those models from the `source_list` that are also present in a predefined `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list` and includes models whose names contain any of the category's keywords, performing a case-insensitive check. If no models match the keywords during this process, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The list of models to be filtered.
    - **category_name** (`str`): The name of the category to use for filtering.
*   **Returns:**
    - **filtered_models** (`list`): A new list containing models that match the specified category's keywords, or the original `source_list` if no matches are found or if the 'STANDARD' category logic applies.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function, `save_gemini_cb`, is designed to handle the saving of a new Gemini API key. It retrieves the potential new key from the Streamlit session state. If a non-empty key is found, it updates the user's Gemini key in the database using `db.update_gemini_key`. After successfully updating, it clears the temporary key from the session state and displays a success notification to the user.
*   **Parameters:**
    *Analysis data not available for this component.*
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function is designed to save a new Ollama URL. It retrieves the URL from the Streamlit session state, specifically from the 'in_ollama_url' key. If a valid URL is found, it updates the database using the 'db.update_ollama_url' function, passing the current username and the new URL. Upon successful update, it displays a confirmation toast message to the user.
*   **Parameters:**
    *Analysis data not available for this component.*
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function is responsible for loading chat and exchange data from the database into the Streamlit session state for a given user. It first checks if the data for the current user is already loaded to prevent redundant operations. If not, it initializes the session state, fetches predefined chats, then loads and organizes individual exchanges within those chats. The function also includes logic to handle legacy data where exchanges might exist for undefined chats and ensures a default chat is created if no chats are found for the user. It concludes by setting an active chat and marking the user's data as loaded.
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat and exchange data.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: dict, val: Any)`
*   **Description:** This function updates the feedback value for a given exchange object. It first modifies the 'feedback' key within the 'ex' dictionary-like object with the provided 'val'. Subsequently, it persists this feedback change to the database by calling 'db.update_exchange_feedback' using the exchange's '_id' and the new feedback value. Finally, it triggers a Streamlit rerun to refresh the UI.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing an exchange, expected to contain at least '_id' and 'feedback' keys.
    - **val** (`Any`): The new feedback value to be assigned to the exchange.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: str, ex: dict)`
*   **Description:** This function is responsible for deleting a specific exchange from the database and subsequently updating the application's session state. It first calls a database utility to remove the exchange by its ID. Afterwards, it checks if the associated chat exists in the Streamlit session state and, if the exchange is found within that chat's exchanges, it removes it from the session state. Finally, it triggers a Streamlit rerun to refresh the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be removed in the Streamlit session state.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' key for database deletion and to be matched in the session state.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** This function handles the deletion of a specific chat identified by a username and chat name. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the chat from the Streamlit session state. If other chats exist, it sets the active chat to the first one available. If no chats remain after deletion, it creates a new default chat named 'Chat 1', inserts it into the database, and sets it as the active chat in the session state. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text: str)`
*   **Description:** This function `extract_repo_name` is designed to parse a given text string and identify a repository name within it. It first attempts to find a URL using a regular expression. If a URL is present, it then uses `urlparse` to break down the URL and extract the path component. The last segment of this path is considered the potential repository name, with any ".git" suffix being removed for cleanliness. The function returns the extracted repository name as a string or None if no URL is found or a repository name cannot be successfully derived.
*   **Parameters:**
    - **text** (`str`): The input string that may contain a URL from which a repository name needs to be extracted.
*   **Returns:**
    - **repository_name** (`str | None`): The extracted repository name as a string, or None if no URL is found or a repository name cannot be determined from the URL path.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text: str)`
*   **Description:** This function acts as a text generator, taking a string as input and yielding its words sequentially. It splits the input text by spaces and iterates through each word. For every word, it yields the word followed by a space, introducing a small delay of 0.01 seconds between each yield operation using `time.sleep`. This creates a streaming effect, delivering text word by word with a brief pause.
*   **Parameters:**
    - **text** (`str`): The input string that will be split into words and streamed.
*   **Returns:**
    - **word** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.
#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str, should_stream: bool)`
*   **Description:** This function processes a given markdown text, identifying and rendering both standard markdown content and embedded Mermaid diagrams. It splits the input text based on ` ```mermaid ... ``` ` blocks. Regular markdown sections are rendered using `st.markdown` or streamed via `st.write_stream` if `should_stream` is true. Mermaid diagram code blocks are attempted to be rendered using `st_mermaid`, with a fallback to `st.code` if an error occurs during Mermaid rendering.
*   **Parameters:**
    - **markdown_text** (`str`): The input text containing markdown and potentially embedded Mermaid diagram syntax.
    - **should_stream** (`bool`): A flag indicating whether to stream the markdown output using `st.write_stream` or render it directly with `st.markdown`. Defaults to `False`.
*   **Returns:**
    - **None** (`None`): This function performs side effects by rendering content to a Streamlit application and does not explicitly return a value.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.
#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** This function is responsible for rendering a single chat exchange, which includes both the user's question and the assistant's answer, within a Streamlit application. It first displays the user's question. Subsequently, it renders the assistant's response along with an interactive toolbar. The toolbar provides options for users to give feedback (like/dislike), add comments, download the answer, and delete the exchange. In case the assistant's answer indicates an error, a specific error message and a delete option are displayed instead of the full toolbar.
*   **Parameters:**
    - **ex** (`dict`): An exchange object containing details such as the user's question, the assistant's answer, a unique identifier ('_id'), feedback status ('feedback'), and an optional feedback message ('feedback_message').
    - **current_chat_name** (`str`): The name of the current chat session, used when handling the deletion of an exchange.
*   **Returns:**
    *Analysis data not available for this component.*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to provide a structured representation for a single parameter of a function. It encapsulates essential information such as the parameter's name, its data type, and a descriptive explanation of its purpose. This class serves as a standardized data structure for consistent parameter documentation and analysis within a larger system.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, has an implicitly generated constructor. It initializes an instance of ParameterDescription by taking 'name', 'type', and 'description' as keyword arguments, validating them against their respective string types, and assigning them as instance attributes.
    *   *Parameters:*
        - **name** (`str`): The name of the function parameter.
        - **type** (`str`): The data type of the parameter, typically as a string representation (e.g., 'str', 'int', 'List[str]').
        - **description** (`str`): A textual explanation detailing the purpose and usage of the parameter.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to structure and validate information about a function's return value. It encapsulates the return value's identifier, its Python type, and a descriptive explanation. This class serves as a standardized data structure for documenting function outputs within a larger system, ensuring consistency and machine-readability.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance of `ReturnDescription` by validating and assigning the `name`, `type`, and `description` fields based on the provided arguments.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The Python type hint or a descriptive string of the return value's type.
        - **description** (`str`): A detailed explanation of what the return value represents.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about the calling context of a function or method. It provides a structured way to store details regarding what a function calls and where it is called from, using two string attributes. This model ensures data validation and serialization for these context-related strings.
*   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The __init__ method for UsageContext is implicitly generated by Pydantic's BaseModel. It initializes an instance of UsageContext by setting the 'calls' and 'called_by' attributes based on the provided string values, ensuring they conform to the defined types.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions, methods, or external entities that the analyzed component calls.
        - **called_by** (`str`): A string describing the functions, methods, or external contexts that call the analyzed component.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data container for describing a function's high-level purpose, its input parameters, its return values, and its operational context within a larger system. This model is crucial for generating detailed documentation or for AI systems that need to understand function behavior.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, so its constructor is automatically generated by Pydantic. It initializes an instance of FunctionDescription by accepting values for its defined fields: overall, parameters, returns, and usage_context.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the function's purpose and implementation.
        - **parameters** (`List[ParameterDescription]`): A list of objects describing each parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of objects describing the return values of the function.
        - **usage_context** (`UsageContext`): An object describing where the function is called and what it calls.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to structure and validate the comprehensive analysis of a single function. It acts as the primary data model for representing a function's identifier, its detailed description (including purpose, parameters, and return values), and any errors encountered during its analysis. This class is crucial for standardizing the output of automated function analysis within a larger system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is implicitly generated, allowing instantiation by providing values for its fields: 'identifier', 'description', and optionally 'error'. These fields are validated upon object creation according to their specified types.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): A detailed analysis object containing the function's overall purpose, parameters, return values, and usage context.
        - **error** (`Optional[str]`): An optional string detailing any errors encountered during the function's analysis, defaulting to None if no errors occurred.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to structure information about the `__init__` method of another class. It serves as a data container, holding a textual summary of the constructor's purpose and a list of its individual parameters. This class is crucial for providing a standardized, machine-readable representation of constructor details within a larger documentation or analysis system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. It is initialized by providing values for its defined fields: a string `description` and a list of `ParameterDescription` objects. This constructor sets up the instance with the provided details about a class's `__init__` method.
    *   *Parameters:*
        - **description** (`str`): A string containing a summary or explanation of the constructor's behavior and purpose.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing a specific parameter of the constructor, including its name, type, and description.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's contextual relationships. It specifically stores details regarding the external dependencies that a class relies upon and the locations or entities responsible for its instantiation. This model provides a structured way to represent and manage metadata about a class's integration within a larger system.
*   **Instantiation:** This class does not explicitly list any points of instantiation in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This method initializes an instance of `ClassContext`, setting up its `dependencies` and `instantiated_by` attributes. As a Pydantic model, the constructor handles validation and assignment of these fields based on the provided arguments.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of a class.
        - **instantiated_by** (`str`): A string describing where the class is instantiated.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `ClassDescription`
*   **Summary:** The `ClassDescription` class is a Pydantic model designed to structure and store a comprehensive analysis of a Python class. It serves as a schema for representing various aspects of a class, including its high-level purpose, details about its constructor, a list of its methods with their individual analyses, and its contextual usage within a larger system. This model is crucial for generating structured documentation or for further automated processing of class definitions.
*   **Instantiation:** This class is not explicitly listed as being instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ClassDescription` is implicitly generated by Pydantic's `BaseModel`. It initializes an instance of `ClassDescription` by validating and assigning values to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`. These fields are expected to conform to their respective type hints, ensuring data integrity upon instantiation.
    *   *Parameters:*
        - **overall** (`str`): A string describing the overall purpose and functionality of the analyzed class.
        - **init_method** (`ConstructorDescription`): An object containing the detailed analysis of the analyzed class's constructor (`__init__` method).
        - **methods** (`List[FunctionAnalysis]`): A list of `FunctionAnalysis` objects, each detailing an individual method within the analyzed class.
        - **usage_context** (`ClassContext`): An object providing context about the analyzed class's dependencies and where it is instantiated.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the root Pydantic model for representing a comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed ClassDescription object containing its constructor and method analyses, and an optional error field to indicate any issues during the analysis process. This model is designed to structure the output of an AI code analyst, providing a standardized format for class-level insights.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. It inherits from `pydantic.BaseModel`, and its initialization is handled automatically by Pydantic based on the type hints of its fields, allowing instantiation by passing keyword arguments corresponding to its defined fields.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event identified by a relationship analyzer. It encapsulates details about where a call originated, including the file, the function or method name, the type of calling entity (e.g., 'method', 'function'), and the exact line number. This model is intended for use in lists that track 'called_by' or 'instantiated_by' relationships within a system.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, CallInfo's constructor is automatically generated. It initializes an instance of CallInfo by validating and assigning values to its fields: file, function, mode, and line. This allows for easy creation of CallInfo objects with structured data.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that made the call.
        - **mode** (`str`): The type of the calling entity, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the file where the call event occurred.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class serves as a Pydantic BaseModel, defining a structured schema for capturing context relevant to function analysis. It is designed to hold information about what a function calls and by whom it is called, facilitating a standardized way to represent this data. This class acts as a data transfer object or a configuration model for function-related context.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly declare external functional dependencies within the provided context, beyond its inheritance from Pydantic's BaseModel.
*   **Constructor:**
    *   *Description:* The class utilizes Pydantic's BaseModel for initialization, meaning its attributes `calls` and `called_by` are automatically validated and assigned upon instantiation based on the provided input. There is no explicit `__init__` method defined within the class itself.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to standardize the input data required for analyzing a Python function. It serves as a data transfer object, ensuring that all necessary components—such as the function's identifier, its source code, relevant imports, and contextual information—are present and correctly typed before analysis proceeds. This class facilitates robust data validation and clear communication between different parts of a larger AI system focused on code analysis.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is implicitly generated to accept keyword arguments corresponding to its defined fields: mode, identifier, source_code, imports, and context.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, which must be 'function_analysis'.
        - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
        - **source_code** (`str`): The raw source code of the function.
        - **imports** (`List[str]`): A list of import statements relevant to the function.
        - **context** (`FunctionContextInput`): Additional contextual information required for the analysis.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to provide a structured schema for capturing and validating contextual information about a specific method. It defines fields to store the method's unique identifier, a list of other functions or methods it calls, a list of `CallInfo` objects indicating where it is called from, its arguments, and its optional docstring. This class serves as a data transfer object or a configuration model for method-level analysis within a larger system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `MethodContextInput` is automatically generated by Pydantic. It handles the instantiation of a `MethodContextInput` object by accepting keyword arguments corresponding to its defined fields, performing data validation and type coercion during the object's creation.
    *   *Parameters:*
        - **identifier** (`str`): The unique string identifier for the method being described.
        - **calls** (`List[str]`): A list of string identifiers for other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects, each detailing a location or context from which this method is invoked.
        - **args** (`List[str]`): A list of string representations of the arguments passed to this method.
        - **docstring** (`Optional[str]`): The docstring content of the method, if available; otherwise, it can be null.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information necessary for analyzing a Python class. It serves as a data container, defining fields for external dependencies, instantiation points, and detailed context for each method within the class. This model provides a standardized format for collecting and organizing metadata about a class's environment and internal structure.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The class is initialized by Pydantic's BaseModel constructor. It automatically handles the assignment of `dependencies`, `instantiated_by`, and `method_context` based on the provided type hints, ensuring data validation and type enforcement upon instantiation.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies of the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where the class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing detailed context for a specific method within the class.
*   **Methods:**
    *Analysis data not available for this component.*
#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a data validation and parsing schema, ensuring that all necessary components like the analysis mode, class identifier, source code, import statements, and contextual information are present and correctly typed before proceeding with the analysis. This class acts as a contract for the data payload used in the class analysis workflow.
*   **Instantiation:** The instantiation points for this class are not provided in the current context, but it is typically instantiated by a system component that prepares data for class analysis.
*   **Dependencies:** This class does not explicitly list any direct functional dependencies within its definition, relying on Pydantic's BaseModel for its core functionality.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. Pydantic's BaseModel automatically generates a constructor based on the defined fields, allowing instantiation by providing values for `mode`, `identifier`, `source_code`, `imports`, and `context`.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operation mode, which must be 'class_analysis' to indicate a class analysis request.
        - **identifier** (`str`): The unique name or identifier of the class being analyzed.
        - **source_code** (`str`): The raw Python source code of the entire class definition to be analyzed.
        - **imports** (`List[str]`): A list of import statements relevant to the source file where the class is defined.
        - **context** (`ClassContextInput`): Additional contextual information, such as dependencies and instantiation points, relevant for the class analysis.
*   **Methods:**
    *Analysis data not available for this component.*

---
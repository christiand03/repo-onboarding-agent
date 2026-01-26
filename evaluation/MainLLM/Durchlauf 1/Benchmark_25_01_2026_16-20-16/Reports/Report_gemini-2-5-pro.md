# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** This project is an automated code documentation agent. It clones a given Git repository, performs a static analysis to understand its structure by building an Abstract Syntax Tree (AST), and then leverages Large Language Models (LLMs) to analyze and describe the functionality of individual functions and classes. The final output is a comprehensive, human-readable Markdown report, accessible through a Streamlit-based web frontend.
- **Key Features:**
  - Clones and analyzes public Git repositories.
  - Generates a detailed Abstract Syntax Tree (AST) to map code structure.
  - Utilizes a two-tiered LLM system (Helper and Main) for in-depth code analysis.
  - Automatically produces structured documentation for classes, methods, and functions.
  - Provides an interactive Streamlit frontend for user input and report visualization.
- **Tech Stack:** Python, Streamlit, LangChain, Pydantic, GitPython, NetworkX

*   **Repository Structure:**
    ```mermaid
    graph LR
        subgraph root
            A[".env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json"]
        end
        subgraph SystemPrompts
            B["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt"]
        end
        subgraph backend
            C["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py"]
        end
        subgraph database
            D["db.py"]
        end
        subgraph frontend
            E["__init__.py<br/>frontend.py"]
        end
        subgraph "frontend/.streamlit"
            F["config.toml"]
        end
        subgraph "frontend/gifs"
            G["4j.gif"]
        end
        subgraph notizen
            H["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
        end
        subgraph result
            I["... 28 result files ..."]
        end
        subgraph schemas
            J["types.py"]
        end
        subgraph statistics
            K["... 5 statistics files ..."]
        end
        root --> SystemPrompts
        root --> backend
        root --> database
        root --> frontend
        root --> notizen
        root --> result
        root --> schemas
        root --> statistics
        frontend --> "frontend/.streamlit"
        frontend --> "frontend/gifs"
    ```

    ## 2. Installation
    ### Dependencies
    As this project has numerous dependencies, it is recommended to install them directly from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
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
    ### Setup Guide
    1.  Clone the repository to your local machine.
    2.  It is recommended to create and activate a Python virtual environment.
    3.  Install the required dependencies using the command: `pip install -r requirements.txt`.
    4.  Copy the `.env.example` file to a new file named `.env`.
    5.  Fill in the necessary API keys and configuration variables in the `.env` file.
    ### Quick Startup
    To run the application, execute the following command from the root directory:
    ```bash
    streamlit run frontend/frontend.py
    ```

    ## 3. Use Cases & Commands
    The primary use case for this application is to automatically generate technical documentation for a software project hosted on GitHub.

    **Workflow:**
    1.  Launch the application using the `streamlit run frontend/frontend.py` command.
    2.  Open the provided URL in your web browser to access the Streamlit frontend.
    3.  Input the URL of a public GitHub repository into the designated text field.
    4.  Select the desired LLM models for the "Helper" (code analysis) and "Main" (report synthesis) tasks.
    5.  Provide the necessary API keys for the selected models.
    6.  Initiate the analysis process. The application will clone the repository, analyze its structure and code, and generate a comprehensive Markdown report.
    7.  The final report will be displayed in the web interface for viewing and download.

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here



## 5. Code Analysis
### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into a Python module path. It first determines the file's relative path to a specified project root, handling potential `ValueError` by falling back to the base filename. It then removes the '.py' extension if present and replaces path separators with dots. Finally, it adjusts the module path by removing '.__init__' if it appears at the end.
*   **Parameters:**
    - **name** (`str`): The absolute or relative path to the file that needs to be converted.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path of the file.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path, suitable for import statements.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.AST_Schema.ASTVisitor.__init__`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to perform a structured traversal of a Python Abstract Syntax Tree (AST). Its primary purpose is to extract and organize metadata about imports, top-level functions, and class definitions, including their nested methods, into a hierarchical schema. This class is instrumental in building a comprehensive understanding of a Python module's structure and contents.
*   **Instantiation:** This class is not explicitly instantiated in the provided context, suggesting it might be instantiated by a higher-level AST processing orchestrator.
*   **Dependencies:** This class depends on `backend.AST_Schema.path_to_module` for converting file paths to module paths.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor instance with the source code of the file being analyzed, its file path, and the project's root directory. It calculates the module path and sets up an empty schema dictionary to store discovered imports, functions, and classes. It also initializes an internal `_current_class` attribute to track the current class being visited during traversal.
    *   *Parameters:*
        - **self** (`ASTVisitor`): The instance of the class.
        - **source_code** (`str`): The raw source code of the file to be analyzed.
        - **file_path** (`str`): The absolute path to the file being analyzed.
        - **project_root** (`str`): The root directory of the entire project.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code, file_path, project_root)`
        *   *Description:* The constructor initializes the ASTVisitor instance with the source code of the file being analyzed, its file path, and the project's root directory. It calculates the module path and sets up an empty schema dictionary to store discovered imports, functions, and classes. It also initializes an internal `_current_class` attribute to track the current class being visited during traversal.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **source_code** (`str`): The raw source code of the file to be analyzed.
            - **file_path** (`str`): The absolute path to the file being analyzed.
            - **project_root** (`str`): The root directory of the entire project.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** `backend.AST_Schema.path_to_module`
            *   **Called By:** This method is called by no other functions.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method is part of the `ast.NodeVisitor` pattern and is automatically called when an `ast.Import` node is encountered during AST traversal. It iterates through each alias specified in the import statement and appends the name of the imported module to the `imports` list within the `self.schema` dictionary. After processing the current import node, it calls `self.generic_visit(node)` to ensure that the traversal continues to any child nodes.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an 'import' statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method implicitly calls `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method is invoked by the AST visitor when an `ast.ImportFrom` node is encountered, which represents a 'from ... import ...' statement. It iterates through the names being imported from the specified module and constructs a fully qualified import string (e.g., 'module.name'). This constructed string is then appended to the `imports` list in `self.schema`. Finally, it calls `self.generic_visit(node)` to ensure that the AST traversal continues to any child nodes.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method implicitly calls `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when an `ast.ImportFrom` node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is triggered when an `ast.ClassDef` node is visited, indicating a class definition in the source code. It constructs a unique identifier for the class using the module path and the class name. It then creates a dictionary containing comprehensive metadata about the class, including its identifier, name, docstring, source code segment, and line numbers, and appends this information to the `classes` list within `self.schema`. Crucially, it sets `self._current_class` to this `class_info` before recursively visiting child nodes, which allows nested methods to be correctly associated with this class. After all children have been visited, `self._current_class` is reset to `None`.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `ast.get_docstring` and `ast.get_source_segment` to extract class details, and `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when an `ast.ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method is called when an `ast.FunctionDef` node, representing a regular function definition, is encountered during AST traversal. It first checks if a class is currently being visited by examining `self._current_class`. If a class is active, the function is treated as a method, and its metadata (identifier, name, arguments, docstring, line numbers) is appended to the `method_context` list of the current class. If no class is active, it's treated as a top-level function, and its metadata is appended to the `functions` list in `self.schema`. In both scenarios, `self.generic_visit(node)` is called to continue the AST traversal.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `ast.get_docstring` and `ast.get_source_segment` to extract function details, and `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when an `ast.FunctionDef` node is encountered during AST traversal.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method is invoked when an `ast.AsyncFunctionDef` node is encountered, which represents an asynchronous function definition. Its implementation simply delegates the processing of the asynchronous function node to the `visit_FunctionDef` method. This design choice means that asynchronous functions are treated identically to regular functions in terms of how their metadata is extracted and stored within the overall schema.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method explicitly calls `self.visit_FunctionDef` to process the async function node.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when an `ast.AsyncFunctionDef` node is encountered during AST traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for processing a collection of Python source files within a repository to generate a structured Abstract Syntax Tree (AST) schema. It can parse individual files to extract their structural components like functions, classes, and imports, and then integrate dynamic relationship data (like calls and instantiations) into this schema. This class serves as a central component for static code analysis, providing a detailed, machine-readable representation of a codebase's structure and interdependencies.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** This class depends on backend.AST_Schema.ASTVisitor for parsing Abstract Syntax Trees.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. This constructor does not perform any specific setup or attribute assignments, serving as a placeholder.
    *   *Parameters:*
        - **self** (`ASTAnalyzer`): The instance of the class.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* Initializes an instance of the ASTAnalyzer class. This constructor does not perform any specific setup or attribute assignments, serving as a placeholder.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, raw_relationships)`
        *   *Description:* This method integrates relationship data, specifically incoming and outgoing calls and instantiations, into a pre-existing full AST schema. It iterates through all functions and classes identified within the schema, updating their respective 'context' fields with the provided relationship information. For classes, it also computes and stores a list of external dependencies based on the methods' outgoing calls, excluding calls to methods within the same class.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): The comprehensive AST schema of the repository, containing parsed file, function, and class nodes.
            - **raw_relationships** (`dict`): A dictionary containing raw 'outgoing' and 'incoming' call/instantiation relationships, typically derived from dynamic analysis or a separate static analysis pass.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary with the relationship data integrated into the context of functions and classes.
        *   **Usage:**
            *   **Calls:** This method primarily accesses dictionary methods like get and items, and list methods like add and append. It does not call other custom functions or classes.
            *   **Called By:** `backend.main.main_workflow`
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files, repo)`
        *   *Description:* This method processes a list of file objects from a Git repository to construct a comprehensive AST schema. It filters for Python files, reads their content, and then uses the ASTVisitor to parse each file's Abstract Syntax Tree, extracting structural components like functions, classes, and imports. The collected data is organized into a 'full_schema' dictionary, with robust error handling for parsing failures.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): A list of file objects, where each object is expected to have 'path' and 'content' attributes representing a source file.
            - **repo** (`GitRepository`): An object representing the Git repository, used to provide context for file paths, though not directly used for content retrieval in this method.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed repository, structured by file paths and containing parsed AST nodes.
        *   **Usage:**
            *   **Calls:** `backend.AST_Schema.ASTVisitor`
            *   **Called By:** `backend.main.main_workflow`

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and then uses a `FileDependencyGraph` visitor to traverse the provided AST, collecting import relationships. The collected dependencies are then added to the graph as nodes and edges, where nodes represent files and edges indicate an import. The function ultimately returns the populated dependency graph.
*   **Parameters:**
    - **filename** (`str`): The path to the file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be processed for dependencies.
    - **repo_root** (`str`): The root directory of the repository, used for resolving file paths and dependencies.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph where nodes are file paths and edges represent import dependencies between them.
*   **Usage:**
    *   **Calls:** `backend.File_Dependency.FileDependencyGraph`
    *   **Called By:** `backend.File_Dependency.build_repository_graph`

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function constructs a directed graph representing the dependencies within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses the content to build a file-specific dependency graph using `build_file_dependency_graph`. Finally, it aggregates all these individual file graphs into a single, comprehensive `networkx.DiGraph` that represents the global dependencies across the entire repository.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to extract and build the dependency graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the aggregated dependencies between files, functions, and classes found within the repository.
*   **Usage:**
    *   **Calls:** `backend.File_Dependency.build_file_dependency_graph`
    *   **Called By:** This function is called by no other functions.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as a string input and converts it into an absolute `pathlib.Path` object. The function then recursively searches this root path for all files that have a '.py' extension. Finally, it compiles and returns a list of these Python files, with each file's path represented as a `pathlib.Path` object relative to the initial input directory.
*   **Parameters:**
    - **directory** (`str`): The string path to the root directory from which to start the recursive search for Python files.
*   **Returns:**
    - **all_files** (`list[pathlib.Path]`): A list of `pathlib.Path` objects, where each object represents a Python file found within the specified directory, with its path relative to the provided root directory.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.File_Dependency.FileDependencyGraph._resolve_module_name`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class, inheriting from ast.NodeVisitor, is designed to analyze Python source code files to build a graph of import dependencies. It utilizes a class-level dictionary, import_dependencies, to store the mapping of files to their imported modules. The class traverses the Abstract Syntax Tree (AST) of a given file, identifying both absolute and relative import statements. Its primary responsibility is to accurately resolve module names, especially for complex relative imports, and populate this import_dependencies dictionary, thereby providing a structured representation of file-to-module dependencies within a repository.
*   **Instantiation:** `backend.File_Dependency.build_file_dependency_graph`
*   **Dependencies:** This class depends on `backend.File_Dependency.get_all_temp_files` for repository file discovery, `backend.File_Dependency.init_exports_symbol` for checking __init__.py exports, and `backend.File_Dependency.module_file_exists` for verifying module file existence.
*   **Constructor:**
    *   *Description:* This constructor initializes an instance of the FileDependencyGraph by setting the filename attribute to the path of the file currently being analyzed and repo_root to the root directory of the repository. These instance attributes are essential for resolving file paths and module dependencies during the AST traversal.
    *   *Parameters:*
        - **self** (`FileDependencyGraph`): The instance of the class.
        - **filename** (`str`): The path to the file for which dependencies are being analyzed.
        - **repo_root** (`Any`): The root directory of the repository, used for resolving absolute paths.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename, repo_root)`
        *   *Description:* This constructor initializes an instance of the FileDependencyGraph by setting the filename attribute to the path of the file currently being analyzed and repo_root to the root directory of the repository. These instance attributes are essential for resolving file paths and module dependencies during the AST traversal.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **filename** (`str`): The path to the file for which dependencies are being analyzed.
            - **repo_root** (`Any`): The root directory of the repository, used for resolving absolute paths.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This method is responsible for resolving relative import statements (e.g., from .. import name). It calculates the correct base directory based on the import level and the current file's location within the repository. It then checks if the imported names correspond to existing module files or symbols exported via __init__.py files. If successful, it returns a list of resolved module/symbol names; otherwise, it raises an ImportError.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`ImportFrom`): An AST ImportFrom node representing the relative import statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:**
            *   **Calls:** `backend.File_Dependency.get_all_temp_files`, `backend.File_Dependency.init_exports_symbol`, `backend.File_Dependency.module_file_exists`
            *   **Called By:** This method is called by visit_ImportFrom when processing relative import statements.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method processes Import and ImportFrom AST nodes to record file dependencies. It iterates through the imported names and adds them to the import_dependencies dictionary, mapping the current self.filename to a set of imported module names. If a base_name is provided (typically from visit_ImportFrom for specific module parts), it uses that; otherwise, it uses the alias name directly. After processing, it calls generic_visit to continue traversing the AST.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`Import | ImportFrom`): An AST node representing either an import or from ... import ... statement.
            - **base_name** (`str | None`): An optional base name for the imported module, used primarily for from ... import ... statements where only the module part is relevant.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls self.generic_visit to continue AST traversal.
            *   **Called By:** This method is called by visit_ImportFrom after determining the base module name.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method specifically handles ImportFrom AST nodes. It first attempts to extract the module name from the node. If a direct module name exists (e.g., from a.b.c import d), it extracts the last part (c) and passes it to visit_Import. If the import is relative (no direct module name, indicated by node.level > 0), it calls _resolve_module_name to resolve the actual module paths. Any resolved base names are then passed to visit_Import. Errors during relative import resolution are caught and printed. Finally, it calls generic_visit to continue AST traversal.
        *   *Parameters:*
            - **self** (`FileDependencyGraph`): The instance of the class.
            - **node** (`ImportFrom`): An AST ImportFrom node representing a from ... import ... statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method is part of the NodeVisitor pattern and is implicitly called by the AST traversal mechanism when an ImportFrom node is encountered.
            *   **Called By:** This method is part of the NodeVisitor pattern and is implicitly called by the AST traversal mechanism when an ImportFrom node is encountered.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy data and processing loop, primarily for testing the LLMHelper class. It defines several example `FunctionAnalysisInput` and `FunctionAnalysis` objects, simulating pre-computed analysis for various functions like `add_item`, `check_stock`, and `generate_report`. It also constructs a `ClassAnalysisInput` for an `InventoryManager` class. Finally, it instantiates an `LLMHelper` and uses it to process the defined function inputs, logging the results and printing the final aggregated documentation.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `backend.HelperLLM.LLMHelper`, `schemas.types.ClassAnalysisInput`, `schemas.types.ClassContextInput`
    *   **Called By:** This function calls no other functions.

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a robust interface for interacting with various large language models (LLMs) to generate structured documentation for Python functions and classes. It centralizes the configuration and interaction with LLM providers like Google Gemini, OpenAI, or Ollama, ensuring that outputs adhere to specific Pydantic schemas. The class manages system prompt loading, dynamic LLM client initialization, batch processing, and rate limiting to efficiently handle documentation generation tasks.
*   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
*   **Dependencies:** The class depends on logging for output, time for rate limiting, json for payload serialization, langchain_google_genai.ChatGoogleGenerativeAI, langchain_ollama.ChatOllama, langchain_openai.ChatOpenAI for LLM integration, langchain.messages.HumanMessage, langchain.messages.SystemMessage for conversation construction, and schemas.types.FunctionAnalysis, schemas.types.ClassAnalysis, schemas.types.FunctionAnalysisInput, schemas.types.ClassAnalysisInput for structured data handling. It also relies on SCADSLLM_URL and OLLAMA_BASE_URL environment variables for certain model configurations.
*   **Constructor:**
    *   *Description:* This constructor initializes the LLMHelper by setting up API keys, loading system prompts from specified file paths, and configuring the underlying Language Model. It dynamically selects and initializes an LLM client (Gemini, OpenAI, or Ollama) based on the provided model name and base URL. It also configures batch processing settings and prepares structured output LLM instances for function and class analysis.
    *   *Parameters:*
        - **self** (`LLMHelper`): The instance of the class.
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **function_prompt_path** (`str`): The file path to the system prompt used for generating function documentation.
        - **class_prompt_path** (`str`): The file path to the system prompt used for generating class documentation.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
        - **base_url** (`str`): An optional base URL for custom or Ollama LLM endpoints.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, function_prompt_path, class_prompt_path, model_name, base_url)`
        *   *Description:* This constructor initializes the LLMHelper by setting up API keys, loading system prompts from specified file paths, and configuring the underlying Language Model. It dynamically selects and initializes an LLM client (Gemini, OpenAI, or Ollama) based on the provided model name and base URL. It also configures batch processing settings and prepares structured output LLM instances for function and class analysis.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
            - **function_prompt_path** (`str`): The file path to the system prompt used for generating function documentation.
            - **class_prompt_path** (`str`): The file path to the system prompt used for generating class documentation.
            - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
            - **base_url** (`str`): An optional base URL for custom or Ollama LLM endpoints.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method configures the batch size for LLM API calls based on the specified `model_name`. It assigns a specific integer value to `self.batch_size` to optimize performance and respect rate limits for different LLM providers and models. The method includes specific batch sizes for various Gemini, Llama, and GPT models, as well as custom/alias models. If the model name is not recognized, it logs a warning and applies a conservative default batch size of 2.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** `backend.HelperLLM.LLMHelper.__init__`
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates structured documentation for a list of functions by interacting with the configured LLM. It processes `FunctionAnalysisInput` objects in batches, converting them into JSON payloads for the LLM. The method uses `self.function_llm` to perform batch API calls, handles potential errors by returning `None` for failed items, and incorporates a waiting period between batches to manage API rate limits effectively. The output is a list of validated `FunctionAnalysis` objects, or `None` for any failed analyses.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing function data for analysis and documentation generation.
        *   *Returns:*
            - **all_validated_functions** (`List[Optional[FunctionAnalysis]]`): A list of FunctionAnalysis objects, where each object represents the structured documentation for a function, or None if an error occurred during its generation.
        *   **Usage:**
            *   **Calls:** json.dumps, function_input.model_dump, SystemMessage, HumanMessage, self.function_llm.batch, logging.info, logging.error, and time.sleep.
            *   **Called By:** `backend.main.main_workflow`
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating structured documentation for a batch of classes using the configured LLM. It takes a list of `ClassAnalysisInput` objects, converts them into JSON, and sends them to `self.class_llm` in batches. The method includes error handling to manage API call failures, extending the results with `None` for any failed items. It also implements a waiting period between batches to comply with API rate limits, ultimately returning a list of validated `ClassAnalysis` objects.
        *   *Parameters:*
            - **self** (`LLMHelper`): The instance of the class.
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing class data for analysis and documentation generation.
        *   *Returns:*
            - **all_validated_classes** (`List[Optional[ClassAnalysis]]`): A list of ClassAnalysis objects, where each object represents the structured documentation for a class, or None if an error occurred during its generation.
        *   **Usage:**
            *   **Calls:** json.dumps, class_input.model_dump, SystemMessage, HumanMessage, self.class_llm.batch, logging.info, logging.error, and time.sleep.
            *   **Called By:** `backend.main.main_workflow`

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a versatile interface for interacting with various large language models (LLMs), abstracting away the specifics of different providers. It handles the initialization of LLM clients (Gemini, OpenAI-compatible, Ollama) based on configuration, loads a system prompt from a file, and provides methods for both synchronous (`call_llm`) and streaming (`stream_llm`) interactions. This class centralizes LLM communication, making it easier to switch between models and manage prompts.
*   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
*   **Dependencies:** The class depends on external libraries for LLM integration, specifically `langchain_google_genai`, `langchain_ollama`, `langchain_openai`, and `langchain.messages`. It also relies on the `logging` module for operational insights.
*   **Constructor:**
    *   *Description:* This constructor initializes the MainLLM class by setting up the API key, loading a system prompt from a specified file path, and configuring the appropriate Language Model (LLM) client based on the `model_name`. It supports various LLM providers like Google Gemini, OpenAI-compatible APIs (e.g., SCADSLLM), and Ollama, raising `ValueError` if essential configurations like API keys or URLs are missing.
    *   *Parameters:*
        - **self** (`MainLLM`): The instance of the class.
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM provider.
        - **prompt_file_path** (`str`): The file path to a text file containing the system prompt for the LLM.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.5-pro").
        - **base_url** (`str | None`): An optional base URL for custom LLM endpoints, particularly for Ollama or OpenAI-compatible models.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, prompt_file_path, model_name, base_url)`
        *   *Description:* This constructor initializes the MainLLM class by setting up the API key, loading a system prompt from a specified file path, and configuring the appropriate Language Model (LLM) client based on the `model_name`. It supports various LLM providers like Google Gemini, OpenAI-compatible APIs (e.g., SCADSLLM), and Ollama, raising `ValueError` if essential configurations like API keys or URLs are missing.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the class.
            - **api_key** (`str`): The API key required for authenticating with the chosen LLM provider.
            - **prompt_file_path** (`str`): The file path to a text file containing the system prompt for the LLM.
            - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.5-pro").
            - **base_url** (`str | None`): An optional base URL for custom LLM endpoints, particularly for Ollama or OpenAI-compatible models.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method sends a user input to the configured LLM for a single, synchronous response. It constructs a message list including the system prompt and the user's input, then invokes the LLM client. The method logs the call status and returns the content of the LLM's response or `None` if an error occurs during the invocation.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the class.
            - **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:*
            - **content** (`str`): The text content of the LLM's response.
            - **None** (`None`): Indicates an error occurred during the LLM call.
        *   **Usage:**
            *   **Calls:** SystemMessage, HumanMessage, self.llm.invoke, logging.info, and logging.error.
            *   **Called By:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method initiates a streaming interaction with the configured LLM, allowing for real-time reception of response chunks. It prepares the messages with the system prompt and user input, then uses the LLM client's `stream` method. It yields each content chunk as it arrives or yields an error message if an exception occurs during the streaming process.
        *   *Parameters:*
            - **self** (`MainLLM`): The instance of the class.
            - **user_input** (`str`): The user's query or message for which a streaming response is desired.
        *   *Returns:*
            - **chunk.content** (`str`): A generator yielding individual content chunks from the LLM's streaming response.
            - **error_message** (`str`): An error message string yielded if an exception occurs during the streaming call.
        *   **Usage:**
            *   **Calls:** SystemMessage, HumanMessage, self.llm.stream, logging.info, and logging.error.
            *   **Called By:** This method is not explicitly called by any other methods in the provided context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract fundamental project information from various common project files such as README, pyproject.toml, and requirements.txt. It initializes a structured dictionary to store details like project overview, installation instructions, and dependencies. Through a series of private parsing methods, it processes the content of these files, prioritizing information from `pyproject.toml` and then `requirements.txt` over `README.md` where overlaps exist. The class provides a public method to orchestrate this extraction, consolidate the findings, and offer fallback mechanisms for missing information, such as deriving a project title from a repository URL.
*   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
*   **Dependencies:** The class depends on the `re` module for regular expression operations, the `os` module for path manipulation, and conditionally on the `tomllib` module for parsing TOML files.
*   **Constructor:**
    *   *Description:* The constructor initializes the class by setting a constant `INFO_NICHT_GEFUNDEN` for placeholder values and creating a nested dictionary `self.info`. This dictionary is pre-populated with default 'Information not found' strings for various project details, including title, description, features, tech stack, status, dependencies, setup instructions, and quick start guide. This structure ensures a consistent output format even when specific information cannot be extracted.
    *   *Parameters:*
        - **self** (`ProjektInfoExtractor`): The instance of the class.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* The constructor initializes the class by setting a constant `INFO_NICHT_GEFUNDEN` for placeholder values and creating a nested dictionary `self.info`. This dictionary is pre-populated with default 'Information not found' strings for various project details, including title, description, features, tech stack, status, dependencies, setup instructions, and quick start guide. This structure ensures a consistent output format even when specific information cannot be extracted.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content)`
        *   *Description:* This private helper method is responsible for sanitizing input string content by removing null bytes (`\x00`). Null bytes can occasionally appear in text files due to encoding mismatches, such as reading a UTF-16 encoded file as UTF-8, and can cause issues in subsequent string processing. The method first checks if the input content is empty to avoid unnecessary operations, returning an empty string if so, otherwise it performs the replacement.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **content** (`str`): The string content to be cleaned.
        *   *Returns:*
            - **** (`str`): The cleaned string with all null bytes removed, or an empty string if the input was empty.
        *   **Usage:**
            *   **Calls:** This method primarily uses Python's built-in string manipulation methods like `replace`.
            *   **Called By:** _parse_readme, _parse_toml, and _parse_requirements
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private method searches through a list of file-like objects to find one whose path matches any of the provided patterns. The search is case-insensitive, ensuring flexibility in file naming conventions. It iterates through each file and then through each pattern, returning the first file object that satisfies any pattern. If no matching file is found after checking all possibilities, the method returns `None`.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **patterns** (`List[str]`): A list of string patterns (e.g., file extensions or names) to match against file paths.
            - **dateien** (`List[Any]`): A list of file-like objects, where each object is expected to have a `path` attribute.
        *   *Returns:*
            - **** (`Optional[Any]`): The first file object found that matches one of the patterns, or `None` if no match is made.
        *   **Usage:**
            *   **Calls:** This method uses string methods such as `lower()` and `endswith()` for case-insensitive path matching.
            *   **Called By:** extrahiere_info
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private method is designed to extract specific text sections from a Markdown content string. It identifies sections based on Markdown level 2 headings (##) that contain any of the specified keywords. A regular expression is dynamically built to match these headings and capture all content following them until another level 2 heading or the end of the document. This allows for structured extraction of information like 'Features' or 'Installation' from README files.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The Markdown content string from which to extract a section.
            - **keywords** (`List[str]`): A list of keywords to match within the Markdown heading (e.g., 'Features', 'Installation').
        *   *Returns:*
            - **** (`Optional[str]`): The extracted section content as a string, with leading/trailing whitespace removed, or `None` if no matching section is found.
        *   **Usage:**
            *   **Calls:** This method utilizes the `re` module for regular expression operations, specifically `re.escape`, `re.compile`, and `re.search`.
            *   **Called By:** _parse_readme
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This method parses the content of a README file to extract various project details and populate the `self.info` dictionary. It begins by cleaning the content using `_clean_content`. It then attempts to find the project title and a general description using regular expressions. Subsequently, it leverages `_extrahiere_sektion_aus_markdown` to extract specific sections like 'Key Features', 'Tech Stack', 'Current Status', 'Installation', and 'Quick Start Guide', updating the `self.info` dictionary only if the information hasn't been found already.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The raw content of the README file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** _clean_content for preprocessing, re.search for title and description, and _extrahiere_sektion_aus_markdown for structured section extraction.
            *   **Called By:** extrahiere_info
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This method parses the content of a `pyproject.toml` file to extract project-level metadata. It first cleans the input content using `_clean_content`. It then attempts to load the TOML content using the `tomllib` module. If `tomllib` is not installed or a `TOMLDecodeError` occurs during parsing, a warning is printed and the method returns. Upon successful parsing, it extracts the project `name`, `description`, and `dependencies` from the 'project' table and updates the `self.info` dictionary accordingly.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The raw content of the `pyproject.toml` file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `_clean_content` for preprocessing and `tomllib.loads` to parse the TOML content. It also uses dictionary `get` method.
            *   **Called By:** extrahiere_info
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This method parses the content of a `requirements.txt` file to extract project dependencies. It starts by cleaning the input content using `_clean_content`. It then splits the content into individual lines, filtering out any empty lines or lines that begin with a '#' (comments). The extracted dependencies are then used to update the `self.info` dictionary's 'dependencies' field, but only if this information has not already been populated from a `pyproject.toml` file, ensuring `pyproject.toml` takes precedence for dependency information.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The raw content of the `requirements.txt` file.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls `_clean_content` for preprocessing.
            *   **Called By:** extrahiere_info
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This is the primary public method that orchestrates the entire project information extraction process. It first identifies relevant project files (README, pyproject.toml, requirements.txt) using `_finde_datei`. It then parses these files in a specific order of precedence: `pyproject.toml` first, then `requirements.txt`, and finally `README.md`. After parsing, it formats the extracted dependencies into a human-readable list. As a fallback, if no project title is found from the files, it attempts to derive one from the provided repository URL. The method returns a comprehensive dictionary containing all gathered project information.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have `path` and `content` attributes, representing files in the repository.
            - **repo_url** (`str`): The URL of the repository, used as a fallback to generate a project title if none is found in the files.
        *   *Returns:*
            - **** (`Dict[str, Any]`): A dictionary containing all extracted project information, structured into 'projekt_uebersicht' and 'installation' categories.
        *   **Usage:**
            *   **Calls:** _finde_datei to locate files, _parse_toml, _parse_requirements, and _parse_readme to process file contents. It also uses os.path.basename and string methods like removesuffix.
            *   **Called By:** `backend.main.main_workflow`, `backend.main.notebook_workflow`

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function takes a NetworkX directed graph and an output file path. Its main purpose is to prepare the graph for DOT file generation by ensuring all node names are 'safe' for DOT syntax. It creates a copy of the input graph and relabels all nodes with generic identifiers like 'n0', 'n1', etc. The original node names are then stored as a 'label' attribute on these new nodes. Finally, the function writes this modified graph to the specified output path as a DOT file.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph to be processed and written to a DOT file.
    - **out_path** (`str`): The file path where the 'safe' DOT graph will be saved.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.callgraph`

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo)`
*   **Description:** This function constructs a directed call graph for a given Git repository. It first identifies all Python files and extracts a set of 'own functions' by parsing the Abstract Syntax Trees (ASTs) of these files using a CallGraph visitor. Subsequently, it builds a global call graph, adding edges only between functions that are part of the identified 'own functions' set, effectively filtering out external or library calls. The final output is a networkx.DiGraph representing these filtered call relationships.
*   **Parameters:**
    - **repo** (`GitRepository`): The GitRepository object containing the files to analyze for building the call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the call relationships exclusively between the 'self-written' functions found within the repository.
*   **Usage:**
    *   **Calls:** `backend.callgraph.CallGraph`
    *   **Called By:** `backend.callgraph`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an ast.NodeVisitor subclass designed to construct a directed call graph for a given Python source file. It traverses the Abstract Syntax Tree (AST) of a file, identifying function definitions, class definitions, import statements, and function calls. By maintaining context such as the current class and function, and resolving names through local definitions and import mappings, it accurately maps callers to callees and builds a comprehensive representation of function dependencies within the file, storing them in a NetworkX graph.
*   **Instantiation:** `backend.callgraph.build_filtered_callgraph`
*   **Dependencies:** This class depends on the 'ast' module for parsing Python code and the 'networkx' library for graph representation.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph instance by setting the filename of the source code being analyzed. It sets up internal state variables to track the current function and class context during AST traversal. Additionally, it initializes several data structures: `local_defs` for local name resolution, `graph` as a NetworkX directed graph to store the call graph, `import_mapping` for resolving imported names, `function_set` to keep track of defined functions, and `edges` to store raw caller-callee relationships.
    *   *Parameters:*
        - **self** (`CallGraph`): The instance of the class.
        - **filename** (`str`): The path or identifier of the source file being analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename)`
        *   *Description:* The constructor initializes the CallGraph instance by setting the filename of the source code being analyzed. It sets up internal state variables to track the current function and class context during AST traversal. Additionally, it initializes several data structures: `local_defs` for local name resolution, `graph` as a NetworkX directed graph to store the call graph, `import_mapping` for resolving imported names, `function_set` to keep track of defined functions, and `edges` to store raw caller-callee relationships.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **filename** (`str`): The path or identifier of the source file being analyzed.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively extracts the components of a function or method call from an AST node. It processes `ast.Call` nodes to get to the function being called, `ast.Name` nodes for simple identifiers, and `ast.Attribute` nodes to build a list representing the fully qualified name components (e.g., ['pkg', 'mod', 'Class', 'method']). This function is crucial for deconstructing call expressions into their constituent parts for later resolution.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.AST`): The AST node representing a call, name, or attribute expression.
        *   *Returns:*
            - **parts** (`list[str]`): A list of string components representing the dotted name of the called entity.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods within its own source code.
            *   **Called By:** _resolve_all_callee_names and visit_Call.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private helper method takes a list of potential callee name components (e.g., `[['module', 'function'], ['Class', 'method']]`) and attempts to resolve them to their full, unique identifiers within the context of the current file. It prioritizes resolution by checking local definitions first, then the `import_mapping`, and finally constructs a full name based on the current filename and class context. This resolution is critical for accurately mapping call targets to their canonical names in the call graph.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **callee_nodes** (`list[list[str]]`): A list where each inner list represents the name components of a potential callee.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of fully resolved string identifiers for the callees.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods within its own source code.
            *   **Called By:** visit_Call.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This private helper method constructs a fully qualified name for a function or method, incorporating the filename and, optionally, the class name. It formats the name as `filename::[class_name::]basename`, providing a unique and unambiguous identifier for functions within the call graph. This ensures that functions with the same base name but different contexts (e.g., in different classes or files) are uniquely identified.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`str | None`): The name of the class if the function is a method, otherwise None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name of the function or method.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods within its own source code.
            *   **Called By:** visit_FunctionDef.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private helper method determines the identifier of the current calling context. If `self.current_function` is set, it returns that value, indicating that the AST traversal is currently inside a defined function. Otherwise, it returns a placeholder indicating the global scope within the current file (`<filename>`) or a generic global scope (`<global-scope>`) if the filename is not available. This provides the 'source' for any detected calls.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
        *   *Returns:*
            - **caller_identifier** (`str`): The identifier of the current caller (function name or scope indicator).
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods within its own source code.
            *   **Called By:** visit_Call.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method, overriding `ast.NodeVisitor.visit_Import`, processes `import` statements. It iterates through the imported modules and their aliases, storing the mapping from the alias (or original name) to the module's actual name in `self.import_mapping`. This mapping is crucial for resolving imported names to their original module paths when analyzing function calls. After processing, it calls `self.generic_visit(node)` to continue AST traversal.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** self.generic_visit.
            *   **Called By:** This method is implicitly called by the ast.NodeVisitor traversal mechanism when an ast.Import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method, overriding `ast.NodeVisitor.visit_ImportFrom`, processes `from ... import ...` statements. It extracts the module name (handling dotted imports by taking the last component) and any aliases for the imported names. It then stores these mappings in `self.import_mapping`, which is essential for correctly resolving names imported from specific modules. Finally, it calls `self.generic_visit(node)` to continue the AST traversal.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** self.generic_visit.
            *   **Called By:** This method is implicitly called by the ast.NodeVisitor traversal mechanism when an ast.ImportFrom node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method, overriding `ast.NodeVisitor.visit_ClassDef`, handles class definitions during AST traversal. It temporarily updates `self.current_class` to the name of the class being visited, allowing any nested methods or functions to correctly identify their enclosing class context. After traversing the class body using `self.generic_visit(node)`, it restores the previous `self.current_class` to maintain the correct scope for subsequent nodes.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** self.generic_visit.
            *   **Called By:** This method is implicitly called by the ast.NodeVisitor traversal mechanism when an ast.ClassDef node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method, overriding `ast.NodeVisitor.visit_FunctionDef`, processes synchronous function definitions. It constructs a full, unique name for the function using `_make_full_name`, stores this name in `self.local_defs` for local resolution, and updates `self.current_function` to track the current scope. The function is added as a node to the `self.graph` and its full name is added to `self.function_set`. After traversing the function's body using `self.generic_visit(node)`, it restores the previous function context.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** _make_full_name and self.generic_visit.
            *   **Called By:** This method is implicitly called by the ast.NodeVisitor traversal mechanism when an ast.FunctionDef node is encountered, and explicitly by visit_AsyncFunctionDef.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method, overriding `ast.NodeVisitor.visit_AsyncFunctionDef`, processes asynchronous function definitions. It delegates the actual processing of the function definition to `visit_FunctionDef`. This approach ensures that both synchronous and asynchronous functions are handled consistently for the purpose of building the call graph, treating them similarly in terms of name resolution and graph node creation.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** self.visit_FunctionDef.
            *   **Called By:** This method is implicitly called by the ast.NodeVisitor traversal mechanism when an ast.AsyncFunctionDef node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method, overriding `ast.NodeVisitor.visit_Call`, is central to building the call graph. It first identifies the current calling context using `_current_caller`. Then, it uses `_recursive_call` to extract the components of the called entity and `_resolve_all_callee_names` to resolve its full, canonical identifier. Finally, it records the call by adding an edge from the `caller` to the `callee` in the `self.edges` dictionary, effectively mapping the dependency. It then continues AST traversal with `self.generic_visit(node)`.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.Call`): The AST node representing a function call.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** _current_caller, _recursive_call, _resolve_all_callee_names, and self.generic_visit.
            *   **Called By:** This method is implicitly called by the ast.NodeVisitor traversal mechanism when an ast.Call node is encountered.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method, overriding `ast.NodeVisitor.visit_If`, processes `if` statements. It includes special logic to detect the `if __name__ == "__main__":` block. When this specific condition is met, it temporarily sets `self.current_function` to "<main_block>" to correctly attribute calls within this block to a special main execution scope. For all other `if` statements, it simply continues the generic AST traversal without altering the current function context.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the class.
            - **node** (`ast.If`): The AST node representing an 'if' statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** self.generic_visit.
            *   **Called By:** This method is implicitly called by the ast.NodeVisitor traversal mechanism when an ast.If node is encountered.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content)`
*   **Description:** The `wrap_cdata` function is designed to encapsulate a given string within XML CDATA tags. It takes a single string argument, `content`, and returns a new string where the original content is embedded between `<![CDATA[\n` and `\n]]>` markers. This effectively escapes the content for safe inclusion within XML documents, preventing issues with special characters.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped within CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A new string containing the original content enclosed within CDATA tags.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.converter.convert_notebook_to_xml`

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs, image_list)`
*   **Description:** This function processes a list of output objects, typically from a notebook execution, to extract and categorize their content. It iterates through each output, identifying its type to handle text, images, or errors. For image data (PNG or JPEG), it decodes Base64 strings, stores them in an external list, and inserts an XML-like placeholder into the result. Text streams and error messages are directly appended to the output list. The function's primary goal is to consolidate diverse output types into a unified list of strings, including image references.
*   **Parameters:**
    - **outputs** (`list`): A list of output objects, presumably from a notebook execution, containing various types of data like text, images, or errors.
    - **image_list** (`list`): A list that will be populated with dictionaries, each containing Base64 encoded image data and its MIME type, along with an index.
*   **Returns:**
    - **extracted_xml_snippets** (`list of str`): A list of strings, where each string is either plain text content, a formatted error message, or an XML-like placeholder for an image.
*   **Usage:**
    *   **Calls:** `backend.converter.process_image`
    *   **Called By:** `backend.converter.convert_notebook_to_xml`

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type)`
*   **Description:** The process_image function is responsible for extracting and preparing base64-encoded image data. It takes a mime_type as input and attempts to retrieve the corresponding image string from an externally accessible data object. If found, it cleans the base64 string by removing newline characters and appends the image's MIME type and data to an external image_list. The function returns a formatted placeholder string upon successful processing. In cases where the mime_type is not present in data, it returns None, and any exceptions during processing result in an error message string.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed, which serves as a key to locate the corresponding base64 image data.
*   **Returns:**
    - **image_placeholder_tag** (`str`): A string formatted as an XML-like tag, <IMAGE_PLACEHOLDER>, containing the assigned index and the MIME type of the processed image.
    - **error_message_tag** (`str`): A string formatted as an error tag, <ERROR>, detailing the exception encountered during image decoding.
    - **no_image_data** (`None`): Returned when no image data corresponding to the provided MIME type is found in the external data object.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.converter.extract_output_content`

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content)`
*   **Description:** This function takes the raw content of a Jupyter notebook as a string and converts it into an XML representation. It parses the notebook cells, distinguishing between markdown and code cells. For code cells, it also processes their outputs, extracting content and images. If the input content cannot be parsed as a valid Jupyter notebook, it returns an error message.
*   **Parameters:**
    - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a JSON string.
*   **Returns:**
    - **xml_output** (`str`): A string containing the XML representation of the notebook cells or an error message if parsing fails.
    - **extracted_images** (`list`): A list of extracted image data or paths found within the notebook outputs. This list is empty if parsing fails or no images are found.
*   **Usage:**
    *   **Calls:** `backend.converter.extract_output_content`, `backend.converter.wrap_cdata`
    *   **Called By:** `backend.converter.process_repo_notebooks`

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files)`
*   **Description:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It filters the input list to find files ending with '.ipynb'. For each identified notebook, it extracts its content and uses the 'convert_notebook_to_xml' function to generate XML output and associated images. The function then aggregates these results into a dictionary, keyed by the notebook's file path, and returns this collection.
*   **Parameters:**
    - **repo_files** (`List[Any]`): A list of file-like objects from a repository. Each object is expected to have 'path' (string) and 'content' (Any) attributes.
*   **Returns:**
    - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the paths of the processed notebook files (str) and values are dictionaries containing the 'xml' output (str) and 'images' (Any) generated from each notebook.
*   **Usage:**
    *   **Calls:** `backend.converter.convert_notebook_to_xml`
    *   **Called By:** `backend.main.notebook_workflow`

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, designed for efficient, lazy loading of its content and metadata. It encapsulates the file's path and its associated Git Tree object, providing properties to access the Git blob, decoded content, and size only when needed. This approach optimizes resource usage by deferring heavy operations until data is actually requested. The class also offers utility methods for converting its data to a dictionary and performing basic content analysis.
*   **Instantiation:** `backend.getRepo.GitRepository.get_all_files`
*   **Dependencies:** This class does not explicitly depend on other components in the provided context.
*   **Constructor:**
    *   *Description:* This method initializes a RepoFile object by storing the file path and the Git Tree object from which the file originates. It sets up internal attributes (`_blob`, `_content`, `_size`) to `None`, indicating that the Git blob, file content, and size are to be loaded lazily upon first access.
    *   *Parameters:*
        - **self** (`RepoFile`): The instance of the class.
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, file_path, commit_tree)`
        *   *Description:* This method initializes a RepoFile object by storing the file path and the Git Tree object from which the file originates. It sets up internal attributes (`_blob`, `_content`, `_size`) to `None`, indicating that the Git blob, file content, and size are to be loaded lazily upon first access.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
            - **file_path** (`str`): The path to the file within the repository.
            - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It first checks if the `_blob` attribute is already set; if not, it attempts to retrieve the blob from the `_tree` using the stored `path`. If the file cannot be found within the commit's tree, a `FileNotFoundError` is raised to indicate the absence of the specified file.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It checks if the `_content` attribute is already loaded; if not, it accesses the Git blob object (via the `blob` property), reads its data stream, and decodes it using UTF-8 encoding, ignoring any decoding errors. This ensures the file content is only processed when explicitly requested.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the `_size` attribute is already loaded; if not, it accesses the Git blob object (via the `blob` property) and retrieves its `size` attribute. This ensures the file size is only determined and stored when needed.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function, demonstrating how to process the file's content. It calculates and returns the total number of words present in the file's content. This is achieved by accessing the `content` property, splitting the string by whitespace, and then counting the resulting elements.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **word_count** (`int`): The total number of words in the file content.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This special method provides a developer-friendly string representation of the `RepoFile` object. It returns a string formatted to show the class name and the file's path, which is particularly useful for debugging, logging, and interactive console sessions, offering a concise summary of the object's identity.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method converts the `RepoFile` object into a dictionary representation, providing a structured way to access its properties. It includes the file's path, its base name, its size, and a type indicator. Optionally, it can also include the full file content if the `include_content` parameter is set to `True`, allowing for flexible data export.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the class.
            - **include_content** (`bool`): A flag indicating whether the file's content should be included in the dictionary. Defaults to False.
        *   *Returns:*
            - **file_data** (`dict`): A dictionary containing the file's metadata and optionally its content.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other functions or methods.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.

#### Class: `GitRepository`
*   **Summary:** This class provides a robust mechanism for interacting with a Git repository. It handles the cloning of a remote repository into a temporary local directory, offers methods to retrieve all files within the repository as structured objects, and can generate a hierarchical representation of the file tree. Furthermore, it implements the context manager protocol, ensuring proper cleanup of the temporary directory upon exiting a 'with' block.
*   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
*   **Dependencies:** This class depends on backend.getRepo.RepoFile for representing individual files within the repository.
*   **Constructor:**
    *   *Description:* Initializes the GitRepository object by cloning a remote Git repository into a temporary directory. It sets up attributes for the repository URL, the temporary directory path, the GitPython Repo object, and an empty list for files. It also captures the latest commit and its tree. Error handling is included for cloning failures.
    *   *Parameters:*
        - **self** (`GitRepository`): The instance of the class.
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, repo_url)`
        *   *Description:* Initializes the GitRepository object by cloning a remote Git repository into a temporary directory. It sets up attributes for the repository URL, the temporary directory path, the GitPython Repo object, and an empty list for files. It also captures the latest commit and its tree. Error handling is included for cloning failures.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
            - **repo_url** (`str`): The URL of the Git repository to be cloned.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It uses Git's 'ls-files' command to get file paths and then creates RepoFile objects for each path, storing them in the 'self.files' attribute. Finally, it returns this list of RepoFile instances.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:**
            *   **Calls:** `backend.getRepo.RepoFile`
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is responsible for cleaning up resources by deleting the temporary directory where the Git repository was cloned. It checks if 'self.temp_dir' is set before attempting to delete it and then sets 'self.temp_dir' to 'None'.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods or functions.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This special method allows the GitRepository class to be used as a context manager. When entering a 'with' statement, this method is invoked and simply returns the instance of the GitRepository itself, making it available as the 'as' target.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods or functions.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This special method is part of the context manager protocol. It is automatically called when exiting a 'with' statement, regardless of whether an exception occurred. Its primary responsibility is to ensure that the 'close' method is invoked to clean up the temporary repository directory.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
            - **exc_type** (`type or None`): The type of the exception that caused the context to be exited, or None if no exception occurred.
            - **exc_val** (`Exception or None`): The exception instance that caused the context to be exited, or None.
            - **exc_tb** (`traceback or None`): The traceback object associated with the exception, or None.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods or functions.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method constructs a hierarchical dictionary representation of the repository's file structure, similar to a file system tree. If 'self.files' is empty, it first calls 'get_all_files' to populate it. It then iterates through the files, splitting their paths to build nested dictionaries representing directories and appending file objects at the leaf nodes. The 'include_content' parameter determines if file content is included in the file objects.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the class.
            - **include_content** (`bool`): A flag indicating whether the content of the files should be included in the generated file tree. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree of the repository.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods or functions.
            *   **Called By:** This method is not explicitly called by other methods in the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare two token counts, `json_tokens` and `toon_tokens`, highlighting a `savings_percent` in the title. It customizes the plot with labels, colors, and displays the token values above each bar. The generated chart is then saved to a specified file path using `matplotlib.pyplot`.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens representing the JSON format.
    - **toon_tokens** (`int`): The number of tokens representing the TOON format.
    - **savings_percent** (`float`): The percentage of savings to be displayed in the chart's title.
    - **output_path** (`str`): The file path where the generated bar chart will be saved.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.main.main_workflow`

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the effective processing time by subtracting estimated sleep durations, primarily for rate-limiting, from the total elapsed time. It first determines the total duration between a start and end time. If the `model_name` does not start with 'gemini-', it returns the total duration without adjustments. For 'gemini-' models, it calculates the number of batches and estimates total sleep time based on a fixed sleep duration per batch. The final net time is the total duration minus this estimated sleep time, ensuring the result is never negative.
*   **Parameters:**
    - **start_time** (`float`): The starting numerical timestamp or time value.
    - **end_time** (`float`): The ending numerical timestamp or time value.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed per batch.
    - **model_name** (`str`): The name of the model, used to determine if sleep time adjustments are needed.
*   **Returns:**
    - **net_time** (`float`): The calculated net processing time in a numerical format (e.g., seconds), adjusted for estimated rate-limit sleep times if the model is 'gemini-', otherwise the total duration. Returns 0 if total items are 0 or if the calculated net time is negative.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.main.main_workflow`

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive analysis pipeline for a given GitHub repository. It begins by extracting API keys and model configurations, then clones the specified repository to access its files. The workflow proceeds to extract basic project information, construct a file tree, analyze code relationships, and build an Abstract Syntax Tree (AST) schema, which is subsequently enriched with relationship data. It then prepares inputs for a Helper LLM to analyze individual functions and classes, and finally uses a Main LLM to generate a comprehensive report based on the aggregated analysis. The function concludes by saving the generated report, along with performance metrics and token savings data, to disk.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL for analysis.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the helper and main LLM models to be utilized in the workflow.
    - **status_callback** (`callable`): An optional callback function used to report status updates and progress messages during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM, detailing the repository analysis, or an error message if report generation failed.
    - **metrics** (`dict`): A dictionary containing performance metrics such as helper LLM processing time, main LLM processing time, total active time, model names used, and token savings data.
*   **Usage:**
    *   **Calls:** `backend.AST_Schema.ASTAnalyzer`, `backend.AST_Schema.ASTAnalyzer.analyze_repository`, `backend.AST_Schema.ASTAnalyzer.merge_relationship_data`, `backend.HelperLLM.LLMHelper`, `backend.HelperLLM.LLMHelper.generate_for_classes`, `backend.HelperLLM.LLMHelper.generate_for_functions`, `backend.MainLLM.MainLLM`, `backend.MainLLM.MainLLM.call_llm`, `backend.basic_info.ProjektInfoExtractor`, `backend.basic_info.ProjektInfoExtractor.extrahiere_info`, `backend.getRepo.GitRepository`, `backend.main.calculate_net_time`, `backend.main.create_savings_chart`, `backend.main.update_status`, `backend.relationship_analyzer.ProjectAnalyzer`, `backend.relationship_analyzer.ProjectAnalyzer.analyze`, `backend.relationship_analyzer.ProjectAnalyzer.get_raw_relationships`, `schemas.types.ClassAnalysisInput`, `schemas.types.ClassContextInput`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, `schemas.types.MethodContextInput`
    *   **Called By:** `frontend.frontend`

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function, `update_status`, is designed to handle status updates. It accepts a message string as input. If a `status_callback` function is available in the current scope, it invokes this callback with the provided message. Additionally, it logs the message at the INFO level using the `logging` module, ensuring that the status update is recorded.
*   **Parameters:**
    - **msg** (`str`): The message string to be used for status updates and logging.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.main.main_workflow`, `backend.main.notebook_workflow`

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback)`
*   **Description:** The notebook_workflow function orchestrates the analysis of Jupyter notebooks found within a specified GitHub repository. It begins by cloning the repository and extracting basic project information. The function then converts the repository's notebooks into an XML-like structure, handling embedded images. It iterates through each processed notebook, constructing a payload for an external Large Language Model (LLM) based on the extracted data and images. Finally, it uses the LLM to generate individual reports for each notebook, concatenates them into a single comprehensive report, saves this report to a file, and returns the report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): The input string, expected to contain a GitHub repository URL from which notebooks will be processed.
    - **api_keys** (`dict`): A dictionary containing API keys for various LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
    - **model** (`str`): The name of the Large Language Model to be used for generating reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`callable or None`): An optional callback function that receives status messages during the workflow execution, allowing for real-time updates.
*   **Returns:**
    - **report** (`str`): A comprehensive markdown string containing the concatenated analysis reports generated by the LLM for all processed notebooks.
    - **metrics** (`dict`): A dictionary providing performance and usage metrics for the workflow, including execution times and model details.
*   **Usage:**
    *   **Calls:** `backend.MainLLM.MainLLM`, `backend.MainLLM.MainLLM.call_llm`, `backend.basic_info.ProjektInfoExtractor`, `backend.basic_info.ProjektInfoExtractor.extrahiere_info`, `backend.converter.process_repo_notebooks`, `backend.getRepo.GitRepository`, `backend.main.gemini_payload`, `backend.main.update_status`
    *   **Called By:** `backend.main`, `frontend.frontend`

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a multi-part content payload, typically for a large language model API like Google Gemini. It takes basic contextual information, a notebook path, XML content representing the notebook structure, and a list of image data. The function first serializes basic information into a JSON string. It then processes the XML content, identifying and extracting text segments and image placeholders. For each image placeholder, it retrieves the corresponding base64 encoded image data from the provided 'images' list and formats it appropriately. The final output is a list of dictionaries, where each dictionary represents either a text part or an image part, interleaved in the order they appear in the XML content.
*   **Parameters:**
    - **basic_info** (`dict`): Contains general information about the project or context, which will be serialized into an introductory JSON block.
    - **nb_path** (`str`): The file path to the current notebook being processed, included in the introductory JSON block.
    - **xml_content** (`str`): The XML structure of the notebook, which may contain '<IMAGE_PLACEHOLDER>' tags that need to be replaced with actual image data.
    - **images** (`list`): A list of dictionaries, where each dictionary is expected to contain at least an 'data' key holding a base64 encoded string of an image, and a 'mime' type.
*   **Returns:**
    - **payload_content** (`list`): A list of dictionaries, where each dictionary represents a content part (either text or image_url) formatted according to the Gemini API's multi-part content structure.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.main.notebook_workflow`

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file system path into a Python module path string. It first calculates the relative path of the file from a specified project root, gracefully handling potential `ValueError` by using the file's base name if a relative path cannot be determined. The function then removes the `.py` extension if present and replaces file system path separators with dots. Finally, it specifically processes paths ending with `.__init__` to represent the package itself, returning the resulting module path string.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used as a base for calculating the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string (e.g., 'my_package.my_module').
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `backend.relationship_analyzer.CallResolverVisitor.__init__`, `backend.relationship_analyzer.ProjectAnalyzer._collect_definitions`

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform a static analysis of a Python project to build a comprehensive call graph. It identifies all Python files, collects definitions of classes, functions, and methods, and then resolves calls between these entities. The class provides methods to initiate the analysis and retrieve the raw relationships in a structured format, making it a core component for understanding code dependencies and structure.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** This class depends on `backend.relationship_analyzer.CallResolverVisitor` for resolving calls and `backend.relationship_analyzer.path_to_module` for converting file paths to module paths. It also utilizes standard library modules such as `ast`, `os`, `logging`, and `collections.defaultdict`.
*   **Constructor:**
    *   *Description:* This constructor initializes the ProjectAnalyzer instance by setting the project's root directory and establishing several internal data structures. It sets up dictionaries for definitions, a defaultdict for the call graph, and a dictionary for file ASTs. Additionally, it defines a set of common directories to be ignored during file system traversal.
    *   *Parameters:*
        - **self** (`ProjectAnalyzer`): The instance of the class.
        - **project_root** (`str`): The absolute path to the root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, project_root)`
        *   *Description:* This constructor initializes the ProjectAnalyzer instance by setting the project's root directory and establishing several internal data structures. It sets up dictionaries for definitions, a defaultdict for the call graph, and a dictionary for file ASTs. Additionally, it defines a set of common directories to be ignored during file system traversal.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **project_root** (`str`): The absolute path to the root directory of the Python project to be analyzed.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method calls no other functions.
            *   **Called By:** This method is called by no other functions.
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire analysis process for the project. It begins by identifying all Python files within the specified project root, excluding ignored directories. It then iterates through these files twice: first to collect all function, method, and class definitions, and second to resolve all calls made between these defined entities. After resolving calls, it clears the stored ASTs to free up memory and returns the generated call graph.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:**
            *   **Calls:** _find_py_files to locate Python files, _collect_definitions to gather entity definitions, and _resolve_calls to establish call relationships.
            *   **Called By:** `backend.main.main_workflow`
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* This method processes the internal call graph to generate a structured representation of outgoing and incoming relationships between code entities. It iterates through the call graph, extracting caller and callee identifiers, and populates two defaultdict(set) objects: one for outgoing calls (caller to callee) and one for incoming calls (callee from caller). The collected sets are then converted to sorted lists for a consistent and ordered output format.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing 'outgoing' and 'incoming' keys, each mapping to a dictionary where keys are entity identifiers and values are sorted lists of related entity identifiers.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods, classes, or functions within the provided context.
            *   **Called By:** `backend.main.main_workflow`
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private helper method is responsible for recursively traversing the project's root directory to locate all Python files. It utilizes `os.walk` to navigate the file system, ensuring that directories specified in `self.ignore_dirs` are skipped. For each file encountered, it checks if the file's extension is '.py' and, if so, appends its full absolute path to a list of Python files.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found in the project, excluding ignored directories.
        *   **Usage:**
            *   **Calls:** This method calls `os.walk` to traverse directories and `os.path.join` to construct file paths.
            *   **Called By:** The `analyze` method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method parses a given Python file to identify and store definitions of functions, methods, and classes. It reads the file's source code, parses it into an Abstract Syntax Tree (AST) using `ast.parse`, and stores this AST in `self.file_asts`. The method then walks the AST to find `ast.FunctionDef` and `ast.ClassDef` nodes, determining their fully qualified path names and types (function, method, or class), and stores this information in `self.definitions`. Error handling is included to log any parsing exceptions.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **filepath** (`str`): The path to the Python file from which to collect definitions.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** `backend.relationship_analyzer.path_to_module`
            *   **Called By:** The `analyze` method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This private helper method traverses an Abstract Syntax Tree (AST) to find the immediate parent node of a given child node. It iterates through all nodes in the provided AST and, for each potential parent, checks its direct children. If the target child node is found among the children of a potential parent, that parent node is returned. If no parent is found after traversing the entire tree, the method returns `None`.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent_node** (`ast.AST | None`): The parent AST node if found, otherwise None.
        *   **Usage:**
            *   **Calls:** This method calls `ast.walk` to traverse the AST and `ast.iter_child_nodes` to iterate over a node's children.
            *   **Called By:** The `_collect_definitions` method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method processes a given Python file's AST to identify and resolve function and method calls within it. It first retrieves the AST for the specified `filepath` from `self.file_asts`. It then instantiates a `CallResolverVisitor` with the file's context and known definitions, and uses this visitor to traverse the AST, populating its internal `calls` attribute. Finally, it merges the resolved calls from the `resolver` into the class's `self.call_graph`. Error handling is included to log any exceptions encountered during call resolution.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the class.
            - **filepath** (`str`): The path to the Python file whose calls need to be resolved.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** `backend.relationship_analyzer.CallResolverVisitor`
            *   **Called By:** The `analyze` method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an `ast.NodeVisitor` designed to traverse an Abstract Syntax Tree (AST) of a Python file and identify all function and method calls. It resolves the fully qualified names of both callers and callees, tracking imports, class definitions, function definitions, and instance types to accurately map call relationships. The visitor collects this information into a `calls` dictionary, providing a comprehensive call graph for the analyzed module.
*   **Instantiation:** `backend.relationship_analyzer.ProjectAnalyzer._resolve_calls`
*   **Dependencies:** This class depends on `backend.relationship_analyzer.path_to_module` for converting file paths to module paths.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with the file path, project root, and a dictionary of known definitions. It sets up internal state variables like `module_path`, `scope` for local name resolution, `instance_types` for tracking object types, and `calls` to store detected call relationships, using `defaultdict` for convenience.
    *   *Parameters:*
        - **self** (`CallResolverVisitor`): The instance of the class.
        - **filepath** (`str`): The path to the source file being analyzed.
        - **project_root** (`str`): The root directory of the project, used to determine the module path.
        - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) for resolution.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filepath, project_root, definitions)`
        *   *Description:* The constructor initializes the visitor with the file path, project root, and a dictionary of known definitions. It sets up internal state variables like `module_path`, `scope` for local name resolution, `instance_types` for tracking object types, and `calls` to store detected call relationships, using `defaultdict` for convenience.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **filepath** (`str`): The path to the source file being analyzed.
            - **project_root** (`str`): The root directory of the project, used to determine the module path.
            - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) for resolution.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** `backend.relationship_analyzer.path_to_module`
            *   **Called By:** This method is called by no other functions.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is part of the `ast.NodeVisitor` pattern and is called when an `ast.ClassDef` node is encountered. It updates the `current_class_name` attribute to reflect the class being visited, allowing nested methods to correctly form their full identifiers. After processing the class's children by calling `generic_visit`, it restores the previous `current_class_name` to maintain correct scope.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method implicitly calls `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when traversing an AST and encountering a class definition.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, which represent function or method definitions. It constructs a `full_identifier` for the function, incorporating the module path and class name if applicable, and updates `current_caller_name`. This ensures that calls made within this function are correctly attributed to its full qualified name. It then traverses the function's body using `generic_visit` and restores the `current_caller_name` upon exit.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method implicitly calls `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when traversing an AST and encountering a function definition.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method is invoked for `ast.Call` nodes, representing function or method calls. It attempts to resolve the qualified name of the called function using the private helper method `_resolve_call_qname`. If the callee is successfully resolved and found within the known `definitions`, it records the call, including the caller's file, line number, full identifier, and type (module, local function, method, or function). This method is central to collecting call graph information.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** _resolve_call_qname to determine the qualified name of the called function.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when traversing an AST and encountering a function or method call.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes `ast.Import` nodes, which represent `import module` statements. It populates the `self.scope` dictionary, mapping the imported module's alias (or its original name) to its full name. This scope is later used by `_resolve_call_qname` to resolve calls to imported modules or their members. After processing, it calls `generic_visit` to continue traversal.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method implicitly calls `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when traversing an AST and encountering an import statement.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, representing `from module import name` statements. It calculates the full qualified path for each imported name, carefully considering relative imports indicated by `node.level`. It then adds these resolved names to the `self.scope` dictionary, enabling subsequent resolution of calls to these imported entities. It then continues AST traversal with `generic_visit`.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.ImportFrom`): The AST node representing a `from ... import ...` statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method implicitly calls `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when traversing an AST and encountering a `from ... import ...` statement.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method processes `ast.Assign` nodes, specifically looking for assignments where the right-hand side is a call to a class constructor (e.g., `x = MyClass()`). If such an assignment is found and the class name can be resolved via `self.scope` and `self.definitions`, it records the type of the assigned variable in `self.instance_types`. This allows for resolving method calls on instances later in the AST traversal. It then calls `generic_visit`.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:* This method does not return a value.
        *   **Usage:**
            *   **Calls:** This method implicitly calls `self.generic_visit` to continue AST traversal.
            *   **Called By:** This method is called by the `ast.NodeVisitor` framework when traversing an AST and encountering an assignment statement.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method attempts to determine the fully qualified name (QName) of a function or method call. It handles two main cases: direct name calls (`ast.Name`) and attribute calls (`ast.Attribute`, e.g., `obj.method`). It first checks `self.scope` for imported names, then local definitions, and for attribute calls, it tries to resolve the instance type from `self.instance_types` or the module from `self.scope`. If a resolution is found, the QName is returned; otherwise, `None` is returned.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the class.
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., `ast.Name` or `ast.Attribute`).
        *   *Returns:*
            - **name** (`str | None`): The fully qualified name of the called entity if resolved, otherwise `None`.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call other methods or functions.
            *   **Called By:** This method is called by `visit_Call` to resolve the qualified name of a function or method being invoked.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** The `encrypt_text` function is designed to encrypt a given string using a `cipher_suite` object, likely an instance of `cryptography.fernet.Fernet`. It first performs a conditional check: if the input `text` is empty or if the `cipher_suite` is not initialized, it bypasses encryption and returns the original text. Otherwise, it prepares the text by stripping leading/trailing whitespace and encoding it to bytes. The byte-encoded text is then encrypted by the `cipher_suite` and subsequently decoded back into a string before being returned.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input text, or the original text if encryption was skipped due to empty input or uninitialized cipher suite.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `database.db.update_gemini_key`, `database.db.update_gpt_key`, `database.db.update_opensrc_key`

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** This function attempts to decrypt a given string using an external `cipher_suite` object. It first performs a preliminary check, returning the original text if the input `text` is empty or if `cipher_suite` is not initialized. If decryption proceeds, the function strips whitespace from the input string, encodes it to bytes, performs the decryption, and then decodes the resulting bytes back into a string. A `try-except` block is used to gracefully handle any exceptions that may occur during the decryption process, returning the original text in case of failure.
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_or_original_text** (`str`): The decrypted string if the operation is successful, or the original string if decryption conditions are not met or an error occurs during decryption.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `database.db.get_decrypted_api_keys`

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function creates a new user document by taking a username, name, and password. It hashes the provided password using `stauth.Hasher.hash` and initializes fields for various API keys as empty strings. The constructed user document is then inserted into the `dbusers` collection. It returns the unique identifier assigned to the newly created user.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which will also serve as the document's `_id`.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (`_id`) of the newly inserted user document, which corresponds to the provided username.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function, `fetch_all_users`, is responsible for retrieving all user records from a database collection. It executes a find operation on the `dbusers` object, which is presumed to be a database collection or similar data store. The results of this operation, typically a cursor or iterable of user documents, are then converted into a standard Python list before being returned.
*   **Parameters:** *None*
*   **Returns:**
    - **users** (`list`): A list containing all user documents or records retrieved from the 'dbusers' collection.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** This function is designed to retrieve a single user record from a database collection named `dbusers`. It takes a username as input and uses it to query the `_id` field within the collection. The function returns the first document that matches the given username.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched, which is used to match the `_id` field in the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if found, or `None` if no user matches the provided username.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username, new_name)`
*   **Description:** This function updates the 'name' field for a user identified by their '_id' in the 'dbusers' collection. It takes the current username (which serves as the document's _id) and the new name to be assigned. The function utilizes the `update_one` method to locate the user by their '_id' and then sets the 'name' attribute to the provided `new_name`. It returns an integer representing the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The current username, which is used as the unique identifier (_id) to locate the user document in the database.
    - **new_name** (`str`): The new name to be set for the identified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function updates a user's Gemini API key in the database. It first encrypts the provided API key using the `encrypt_text` function. Then, it uses the `dbusers` collection to find the user by their username and sets the `gemini_api_key` field to the encrypted value. The function returns the count of modified documents.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored for the user. This key will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:**
    *   **Calls:** `database.db.encrypt_text`
    *   **Called By:** `frontend.frontend`, `frontend.frontend.save_gemini_cb`

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username, gpt_api_key)`
*   **Description:** This function updates a user's GPT API key in the database. It takes a username and a new GPT API key as input. The provided API key is first stripped of any leading/trailing whitespace and then encrypted using the `encrypt_text` function. The function then performs an update operation on the `dbusers` collection, setting the `gpt_api_key` field for the specified user. Finally, it returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be stored for the user. It will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:**
    *   **Calls:** `database.db.encrypt_text`
    *   **Called By:** `frontend.frontend`

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function updates the Ollama base URL for a specific user in the database. It takes a username and a new Ollama base URL as input. The function strips any leading or trailing whitespace from the provided URL before storing it. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The username identifying the user whose Ollama base URL is to be updated.
    - **ollama_base_url** (`str`): The new Ollama base URL to set for the user. Leading and trailing whitespace will be removed before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation. A value of 1 indicates success if the user existed, 0 otherwise.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`, `frontend.frontend.save_ollama_cb`

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username, opensrc_api_key)`
*   **Description:** This function updates the Open Source API key for a specified user in the database. It first encrypts the provided API key, ensuring any leading or trailing whitespace is removed. The encrypted key is then stored in the 'opensrc_api_key' field for the user identified by their username. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The username of the user whose Open Source API key needs to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be stored. It will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents (users) that were modified by the update operation.
*   **Usage:**
    *   **Calls:** `database.db.encrypt_text`
    *   **Called By:** `frontend.frontend`

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username, opensrc_base_url)`
*   **Description:** This function updates a user's 'opensrc_base_url' in the database. It takes a 'username' and a new 'opensrc_base_url' string. The function uses 'dbusers.update_one' to locate the user by their '_id' (username) and sets the 'opensrc_base_url' field to the provided URL after stripping any leading or trailing whitespace. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose 'opensrc_base_url' is to be updated.
    - **opensrc_base_url** (`str`): The new base URL for opensource projects to be associated with the user. Leading/trailing whitespace will be removed.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** This function retrieves the Gemini API key associated with a specific username from a database. It queries the 'dbusers' collection, searching for a document where the '_id' matches the provided username. If a user document is found, it extracts and returns the 'gemini_api_key' field. If no user is found or the key is not present, the function returns None.
*   **Parameters:**
    - **username** (`str`): The username used to identify the user in the database.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key string if found for the user, otherwise None.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** This function retrieves the Ollama base URL associated with a given username from a database. It queries the `dbusers` collection, using the provided username as the document's `_id`. It specifically projects only the `ollama_base_url` field. The function returns the extracted URL if a user is found, otherwise it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`Optional[str]`): The Ollama base URL for the specified user, or None if the user is not found in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username)`
*   **Description:** This function, `fetch_gpt_key`, is designed to retrieve a user's GPT API key from a database. It takes a username as input and queries a `dbusers` collection to find a matching user document. The function specifically projects the `gpt_api_key` field, excluding the `_id`. It returns the found API key or `None` if no user is found with the given username.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the username, or None if no user document is found.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username)`
*   **Description:** This function is designed to retrieve a user's 'opensrc_api_key' from a database. It takes a username as input and queries the 'dbusers' collection. The function specifically looks for a document where the '_id' matches the provided username and projects only the 'opensrc_api_key' field. If a user is found, it returns the associated API key; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose 'opensrc_api_key' is to be fetched.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The 'opensrc_api_key' associated with the given username, or None if the user is not found.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username)`
*   **Description:** This function retrieves the 'opensrc_base_url' for a specified user from a database. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided 'username'. If a user document is found, it extracts the 'opensrc_base_url' field. The function returns this URL if available, or None if the user is not found or the field is absent.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Open Source base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The base URL for the user's open source profile if found, otherwise None.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** The `delete_user` function is responsible for removing a specific user record from a database collection. It takes a username as input, which serves as the primary key (`_id`) to locate the user document. The function then executes a `delete_one` operation on the `dbusers` collection and returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation. For `delete_one`, this will typically be 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function retrieves a user's API keys and base URLs from a database based on the provided username. It queries the 'dbusers' collection to find the user. If the user is not found, it returns a tuple of None values. Otherwise, it decrypts specific API keys (Gemini, GPT, open-source) using the 'decrypt_text' function and retrieves other URLs (Ollama, open-source) directly from the user object. Finally, it returns all these decrypted keys and URLs.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user is not found or the key is absent.
    - **ollama_plain** (`str | None`): The Ollama base URL, or None if the user is not found or the URL is absent.
    - **gpt_plain** (`str | None`): The decrypted GPT API key, or None if the user is not found or the key is absent.
    - **opensrc_plain** (`str | None`): The decrypted open-source API key, or None if the user is not found or the key is absent.
    - **opensrc_url** (`str | None`): The open-source base URL, or None if the user is not found or the URL is absent.
*   **Usage:**
    *   **Calls:** `database.db.decrypt_text`
    *   **Called By:** `frontend.frontend`

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username, chat_name)`
*   **Description:** This function creates a new chat entry within a database. It constructs a dictionary containing a unique identifier generated by `uuid.uuid4()`, the provided username, the chat name, and the current timestamp using `datetime.now()`. This chat dictionary is then inserted into a database collection, likely `dbchats`, using the `insert_one` method. The function's primary purpose is to persist new chat metadata into the database. It returns the unique ID assigned to the newly inserted chat document.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier (e.g., ObjectId or string) of the newly inserted chat document in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`, `frontend.frontend.handle_delete_chat`, `frontend.frontend.load_data_from_db`

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username)`
*   **Description:** This function is designed to retrieve all chat records associated with a given username from a database collection named `dbchats`. It performs a query filtering by the provided username and then sorts the results chronologically by their creation timestamp in ascending order. The function converts the database cursor into a list before returning it.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat records.
*   **Returns:**
    - **chats** (`list`): A list of chat records associated with the specified username, sorted by creation date.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend.load_data_from_db`

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username, chat_name)`
*   **Description:** This function, `check_chat_exists`, is designed to verify the existence of a specific chat within a database collection named `dbchats`. It takes a username and a chat name as input. The function queries the `dbchats` collection to find a document that matches both the provided username and chat name. It returns a boolean value indicating whether such a chat was found.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to check for existence.
    - **chat_name** (`str`): The name of the chat to check for existence.
*   **Returns:**
    - **exists** (`bool`): True if a chat matching the given username and chat name is found in the database, False otherwise.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
*   **Description:** This function renames a chat and all its associated exchanges (messages) in the database. It first updates the chat entry in the `dbchats` collection by changing its `chat_name` from `old_name` to `new_name` for a given `username`. Subsequently, it updates all related exchanges in the `dbexchanges` collection to reflect the new chat name. The function returns the number of documents modified during the initial chat entry update operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat that needs to be changed.
    - **new_name** (`str`): The new desired name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the `dbchats.update_one` operation, indicating if the chat entry was successfully renamed.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time, json_tokens, toon_tokens, savings_percent)`
*   **Description:** This function inserts a new exchange record into a database collection. It generates a unique identifier for the exchange, constructs a dictionary containing various details such as the question, answer, feedback, user information, and performance metrics. It then attempts to insert this dictionary into the 'dbexchanges' collection. If the insertion is successful, it returns the newly generated ID; otherwise, it catches any exceptions, prints an error, and returns None.
*   **Parameters:**
    - **question** (`str`): The question string associated with the exchange.
    - **answer** (`str`): The answer string generated for the exchange.
    - **feedback** (`str`): The feedback string provided for the exchange.
    - **username** (`str`): The username associated with the exchange.
    - **chat_name** (`str`): The name of the chat where the exchange occurred.
    - **helper_used** (`str`): Indicates if a helper component was used, defaults to an empty string.
    - **main_used** (`str`): Indicates if the main component was used, defaults to an empty string.
    - **total_time** (`str`): The total time taken for the exchange, defaults to an empty string.
    - **helper_time** (`str`): The time taken by the helper component, defaults to an empty string.
    - **main_time** (`str`): The time taken by the main component, defaults to an empty string.
    - **json_tokens** (`int`): The number of JSON tokens used, defaults to 0.
    - **toon_tokens** (`int`): The number of TOON tokens used, defaults to 0.
    - **savings_percent** (`float`): The percentage of savings achieved, defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly inserted exchange if successful.
    - **None** (`NoneType`): Returns None if an error occurs during the database insertion.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** This function retrieves a list of exchange records associated with a specific username from the `dbexchanges` collection. It queries the database using the provided username and sorts the results chronologically by their creation timestamp in ascending order. The sorted database documents are then converted into a list and returned.
*   **Parameters:**
    - **username** (`str`): The username used to filter and fetch relevant exchange records from the database.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (documents) found for the given username, sorted by their 'created_at' timestamp.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend.load_data_from_db`

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function retrieves a list of exchange documents from the 'dbexchanges' collection. It filters the exchanges by a specified username and chat name. The results are then sorted in ascending order based on their 'created_at' timestamp and returned as a list.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchanges.
    - **chat_name** (`str`): The name of the chat used to filter the exchanges.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation date.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function updates the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function uses a database client, likely `dbexchanges`, to perform an `update_one` operation, targeting the document by its `_id` and setting the `feedback` field. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated in the database.
    - **feedback** (`int`): The integer feedback value to be set for the specified exchange record.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend.handle_feedback_change`

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function updates a specific exchange record in the database by setting or modifying its 'feedback_message' field. It takes an exchange identifier and the new feedback message as input. The function leverages a database client to perform an update operation on a document matching the provided exchange ID.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange document to be updated. Its specific type is inferred from its usage as a MongoDB '_id'.
    - **feedback_message** (`str`): The new feedback message to be stored for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend.render_exchange`

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function is responsible for deleting a single exchange document from the 'dbexchanges' collection within a database. It takes an exchange ID as input and uses it to locate and remove the corresponding document. The function leverages a database client's 'delete_one' method to perform the operation. It then reports the number of documents that were successfully deleted.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange document to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted by the operation. This will typically be 0 or 1.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend.handle_delete_exchange`

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username, chat_name)`
*   **Description:** This function is responsible for completely deleting a chat and all associated messages (exchanges) for a given user. It first removes all messages linked to the specified chat name and username using `dbexchanges.delete_many`. Subsequently, it deletes the chat entry itself from the chat list using `dbchats.delete_one`. The function ensures data consistency between frontend and backend by removing both the chat and its contents.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted by the `dbchats.delete_one` operation, typically 1 if the chat existed and was deleted, or 0 otherwise.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend.handle_delete_chat`

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list)`
*   **Description:** This function processes a list of strings, where each string is expected to represent a path or a hierarchical identifier. It iterates through the input list, and for each string, it splits the string by the '/' character. The function then extracts the last segment from the split string and compiles these segments into a new list, which is then returned. This effectively 'cleans' the names by removing any preceding path information.
*   **Parameters:**
    - **model_list** (`list`): A list of strings, where each string is typically a path or an identifier containing '/' characters.
*   **Returns:**
    - **cleaned_names** (`list`): A new list of strings, where each string is the last segment of the corresponding input string after splitting by '/'.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list, category_name)`
*   **Description:** This function filters a list of models (`source_list`) based on a specified category (`category_name`). It retrieves keywords associated with the category from a global `CATEGORY_KEYWORDS` mapping. If the category's keywords include "STANDARD", it returns only those models from the `source_list` that are also present in `STANDARD_MODELS`. Otherwise, it iterates through the `source_list` and includes models whose names (case-insensitively) contain any of the category's keywords. If no models match the keywords, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The initial list of models (presumably strings) to be filtered.
    - **category_name** (`str`): The name of the category used to determine the filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered based on the category keywords, or the original `source_list` if no matches are found or if the 'STANDARD' category logic is applied.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function serves as a callback to save a user-provided Gemini API key. It retrieves the potential new key from the Streamlit session state. If a non-empty key is found, it proceeds to update the user's Gemini key in the database using the `db.update_gemini_key` function, associating it with the current username from the session state. After a successful update, the `in_gemini_key` field is cleared from the session state, and a success toast notification is displayed to the user.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `database.db.update_gemini_key`
    *   **Called By:** This function is called by no other functions.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function is designed to save a user-provided Ollama URL. It first attempts to retrieve a potential new Ollama URL from the Streamlit session state, specifically from the key 'in_ollama_url'. If a valid URL is found, it proceeds to update this URL in the database using the `db.update_ollama_url` function, associating it with the current user's username also retrieved from the session state. Upon successful update, a confirmation toast message is displayed to the user.
*   **Parameters:** *None*
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `database.db.update_ollama_url`
    *   **Called By:** This function is called by no other functions.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** This function loads chat and exchange data from the database for a specified user and populates the Streamlit session state. It first checks if the data for the current user is already loaded; if not, it proceeds to fetch the data. The function initializes the `st.session_state.chats` dictionary, then retrieves defined chats and their corresponding exchanges from the database. It handles cases where exchanges might exist for undefined chats, ensuring data consistency and setting default feedback values. Finally, it ensures at least one chat exists, creating a default 'Chat 1' if necessary, and sets the `active_chat` in the session state.
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat and exchange data from the database.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `database.db.fetch_chats_by_user`, `database.db.fetch_exchanges_by_user`, `database.db.insert_chat`
    *   **Called By:** `frontend.frontend`

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function is designed to process a change in feedback for a specific exchange object. It first updates the 'feedback' key within the provided 'ex' dictionary with the new 'val'. Subsequently, it persists this feedback change to the database by invoking 'db.update_exchange_feedback', passing the exchange's '_id' and the new feedback value. Finally, it triggers a rerun of the Streamlit application, likely to refresh the UI and reflect the updated feedback.
*   **Parameters:**
    - **ex** (`dict`): The exchange object, expected to be a dictionary containing at least an '_id' and a 'feedback' key.
    - **val** (`Any`): The new feedback value to be assigned to the exchange.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `database.db.update_exchange_feedback`
    *   **Called By:** `frontend.frontend.render_exchange`

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it updates the Streamlit session state by removing the exchange from the relevant chat's exchanges list, if it exists. Finally, it triggers a Streamlit rerun to reflect the changes in the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be removed in the session state.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' key for database deletion and to be present in the session state's exchanges list.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `database.db.delete_exchange_by_id`
    *   **Called By:** `frontend.frontend.render_exchange`

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function handles the deletion of a specified chat for a given user. It first calls the database to permanently remove the chat. Subsequently, it updates the Streamlit session state by removing the chat from the active list. If no chats remain after deletion, a new default chat named "Chat 1" is created in the database and set as the active chat. Finally, it triggers a Streamlit rerun to refresh the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `database.db.delete_full_chat`, `database.db.insert_chat`
    *   **Called By:** `frontend.frontend`

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** This function is designed to extract a repository name from a given text string. It first attempts to find a URL within the text using a regular expression. If a URL is found, it parses the URL to isolate the path component. The last segment of this path is then considered the potential repository name. It includes logic to remove the ".git" suffix if present. If no URL is found or a repository name cannot be successfully extracted, the function returns None.
*   **Parameters:**
    - **text** (`str`): The input string from which to attempt to extract a repository name, potentially containing a URL.
*   **Returns:**
    - **repo_name** (`str`): The extracted repository name as a string.
    - **None** (`None`): Indicates that no repository name could be extracted from the input text.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend`

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** This function acts as a generator that takes a string of text and yields its words sequentially. It splits the input text by spaces and then iterates through each word. For every word, it yields the word followed by a space, introducing a small delay to simulate a streaming effect. This is useful for displaying text incrementally, such as in a user interface.
*   **Parameters:**
    - **text** (`str`): The input string that will be split into words and streamed.
*   **Returns:**
    - **word_chunk** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** `frontend.frontend.render_text_with_mermaid`

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream)`
*   **Description:** This function processes a given markdown text, identifying and rendering embedded Mermaid diagrams separately from standard markdown content. It splits the input text based on '```mermaid' delimiters. Non-Mermaid sections are rendered as standard markdown, with an option to stream the text. Mermaid code blocks are attempted to be rendered using a specialized Streamlit Mermaid component, falling back to displaying the code block if rendering fails.
*   **Parameters:**
    - **markdown_text** (`str`): The input text, which may contain standard markdown and embedded Mermaid diagram code blocks.
    - **should_stream** (`bool`): A boolean flag indicating whether non-Mermaid text parts should be streamed to the output. Defaults to False.
*   **Returns:**
    - **None** (`None`): This function does not explicitly return a value. It performs side effects by rendering content to a Streamlit application. It returns implicitly if 'markdown_text' is empty.
*   **Usage:**
    *   **Calls:** `frontend.frontend.stream_text_generator`
    *   **Called By:** `frontend.frontend`, `frontend.frontend.render_exchange`

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function `render_exchange` is responsible for rendering a single chat exchange (user question and assistant answer) within a Streamlit application. It first displays the user's question using `st.chat_message`. For the assistant's response, it provides an interactive toolbar that includes options for feedback (like/dislike buttons), adding a comment via a popover, downloading the answer as Markdown, and deleting the exchange. It handles error states in the assistant's answer by displaying an error message and offering only a delete option. Finally, it renders the answer content using `render_text_with_mermaid` within a bordered container.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing a chat exchange, containing the user's question, the assistant's answer, feedback status, and other metadata like '_id' and 'feedback_message'.
    - **current_chat_name** (`str`): The name of the current chat, used as context when handling the deletion of an exchange.
*   **Returns:** *None*
*   **Usage:**
    *   **Calls:** `database.db.update_exchange_feedback_message`, `frontend.frontend.handle_delete_exchange`, `frontend.frontend.handle_feedback_change`, `frontend.frontend.render_text_with_mermaid`
    *   **Called By:** `frontend.frontend`

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to provide a structured representation for a single parameter within a function's signature. It serves as a data model to encapsulate essential information about a parameter, including its name, its data type, and a descriptive explanation of its role. This class is fundamental for generating comprehensive documentation or for programmatic analysis of function interfaces.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, inheriting from Pydantic's BaseModel, automatically generates an __init__ method. This constructor initializes an instance of ParameterDescription by validating and assigning the 'name', 'type', and 'description' fields based on the provided arguments.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type hint or inferred type of the parameter.
        - **description** (`str`): A brief explanation of the parameter's purpose.
*   **Methods:** *None*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to standardize the representation of a function's return value. It serves as a data structure to clearly define the name, data type, and a descriptive explanation of what a function returns. This class is crucial for generating structured documentation or for systems that require a programmatic understanding of function outputs.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for ReturnDescription is automatically generated. It initializes an instance of the class by accepting `name`, `type`, and `description` as keyword arguments, validating them against their string type hints.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The data type of the return value, e.g., 'str', 'int', 'List[str]'.
        - **description** (`str`): A detailed explanation of the return value's purpose, content, or behavior.
*   **Methods:** *None*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about the calling context of a function or method. It serves as a structured data container, defining two essential string attributes: 'calls', which describes the entities invoked by the function, and 'called_by', which indicates where the function itself is utilized. This class provides a clear and validated structure for representing functional dependencies and interactions within a system.
*   **Instantiation:** This class's instantiation points are not explicitly provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is implicitly generated. It initializes instances of `UsageContext` by accepting `calls` and `called_by` as keyword arguments, performing type validation according to their annotations.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or classes that this entity calls.
        - **called_by** (`str`): A string summarizing the functions, methods, or classes that call this entity.
*   **Methods:** *None*

#### Class: `FunctionDescription`
*   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data container for detailing a function's high-level purpose, its input parameters, its return values, and its operational context within a larger system. This class is fundamental for generating structured documentation or for AI systems that need to understand and process function metadata.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class relies on `BaseModel` from Pydantic for its structure and validation, and `List` from `typing` for type hinting. It also depends on `ParameterDescription`, `ReturnDescription`, and `UsageContext` for its field types.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `FunctionDescription` is implicitly generated by Pydantic. It handles the initialization of an instance by validating and assigning values to its defined fields: `overall`, `parameters`, `returns`, and `usage_context` upon object creation.
    *   *Parameters:*
        - **overall** (`str`): A concise, high-level summary describing the function's primary purpose and what it achieves.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing an input parameter of the function, including its name, type, and description.
        - **returns** (`List[ReturnDescription]`): A list of `ReturnDescription` objects, each describing a value or type that the function is expected to return.
        - **usage_context** (`UsageContext`): An object providing contextual information about the function's interactions, such as other functions it calls or where it is called from.
*   **Methods:** *None*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate the comprehensive analysis of a single function. It serves as a structured data container, holding the function's unique identifier, a detailed description object, and an optional error message. This model is crucial for standardizing the output of automated function analysis processes within a larger system.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class does not explicitly define an __init__ method. As a pydantic.BaseModel, its constructor is implicitly generated, allowing instantiation by providing keyword arguments corresponding to its defined fields: identifier, description, and an optional error.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional field to store an error message if the function analysis encounters issues, otherwise it is None.
*   **Methods:** *None*

#### Class: `ConstructorDescription`
*   **Summary:** The `ConstructorDescription` class is a Pydantic BaseModel designed to structure and validate information about a Python class's `__init__` method. It serves as a data model to encapsulate a textual summary of the constructor's behavior along with a detailed list of its parameters. This class is crucial for standardizing the representation of constructor metadata within a larger system, likely for automated documentation, code analysis, or API schema generation.
*   **Instantiation:** The specific points where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class depends on `pydantic.BaseModel` for its data modeling capabilities and `typing.List` for type hinting the list of parameters.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, `ConstructorDescription` has an implicitly generated `__init__` method. This constructor is responsible for validating and assigning values to its `description` (a string) and `parameters` (a list of `ParameterDescription` objects) fields upon instantiation. It ensures that any data used to create an instance of this class adheres to the specified types and structure.
    *   *Parameters:*
        - **description** (`str`): A string providing a high-level summary of the constructor's purpose and functionality.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing a specific parameter of the constructor, including its name, type, and individual description.
*   **Methods:** *None*

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate contextual information about a Python class. It specifically tracks the external dependencies that a class relies on and the locations or modules where the class is instantiated. This model provides a structured way to represent and validate these two critical pieces of contextual metadata.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ClassContext` is implicitly generated by Pydantic's `BaseModel`. It initializes instances of `ClassContext` by accepting values for `dependencies` and `instantiated_by` as keyword arguments, performing validation according to their type hints.
    *   *Parameters:*
        - **dependencies** (`str`): A string summarizing the external dependencies of the class.
        - **instantiated_by** (`str`): A string summarizing where the class is instantiated.
*   **Methods:** *None*

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to store a comprehensive, structured analysis of a Python class. It serves as a data container, encapsulating various aspects of a class, including its high-level purpose, details about its constructor, a list of all its methods with their individual analyses, and contextual information regarding its usage and dependencies. This model provides a standardized format for representing class analysis results, facilitating machine-readable documentation and further automated processing.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for ClassDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance of ClassDescription by validating and assigning values to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`. This constructor ensures that all required components for a class analysis are present and correctly typed upon object creation.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose.
        - **init_method** (`ConstructorDescription`): A detailed description of the class's constructor.
        - **methods** (`List[FunctionAnalysis]`): A list containing detailed analyses of each method within the class.
        - **usage_context** (`ClassContext`): Contextual information about the class's dependencies and where it is instantiated.
*   **Methods:** *None*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as a Pydantic model to structure the comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed ClassDescription object containing its constructor, methods, and usage context, and an optional field to report any analysis errors. This model is designed to provide a standardized, machine-readable representation of a class's structure and behavior.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The __init__ method for this Pydantic model initializes an instance of ClassAnalysis by accepting values for `identifier`, `description`, and an optional `error` string. It leverages Pydantic's validation to ensure the provided data conforms to the defined types and structure.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifying the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its constructor, methods, and usage context.
        - **error** (`Optional[str]`): An optional string indicating an error message if the class analysis failed, defaulting to None.
*   **Methods:** *None*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event within a relationship analyzer. It encapsulates details about where a call originates, including the file path, the name of the calling function, the mode of the call (e.g., 'method', 'function', 'module'), and the specific line number. This model serves as a structured data container for tracking and analyzing call relationships, particularly in contexts like 'called_by' and 'instantiated_by' lists.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* The CallInfo class, as a Pydantic BaseModel, automatically generates its constructor. It initializes an instance by accepting keyword arguments that correspond to its defined fields: file, function, mode, and line. These parameters are validated upon instantiation to ensure they conform to their specified types, providing robust data integrity for call event information.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that is making the call.
        - **mode** (`str`): The type or context of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the file where the call event is located.
*   **Methods:** *None*

#### Class: `FunctionContextInput`
*   **Summary:** The `FunctionContextInput` class is a Pydantic BaseModel designed to structure the contextual information required for analyzing a function. It serves as a data container, defining the expected format for inputs related to a function's interactions within a larger system. This class explicitly tracks what other entities a function calls and by which entities it is called, providing a clear, machine-readable representation of its dependencies and usage.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** This class implicitly depends on `pydantic.BaseModel` for its core functionality and `typing.List` for type hinting. It also relies on the `CallInfo` type, which is not defined within this source code but is expected to be available.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, meaning its constructor is implicitly generated by Pydantic. It initializes instances by validating and assigning values to its `calls` and `called_by` fields based on the provided arguments, ensuring data integrity according to the defined types.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of identifiers (strings) representing other methods, classes, or functions that the function being analyzed calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects, each detailing an entity that calls the function being analyzed, providing context on its callers.
*   **Methods:** *None*

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a FunctionAnalysis object. It serves as a data contract, ensuring that all necessary components—such as the analysis mode, function identifier, source code, relevant imports, and contextual information—are provided and correctly typed before a function analysis can proceed. This class facilitates robust data validation and clear communication of analysis requirements within the system.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is implicitly generated, allowing instantiation by passing keyword arguments corresponding to its defined fields.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, which must be 'function_analysis'.
        - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
        - **source_code** (`str`): The raw source code of the function.
        - **imports** (`List[str]`): A list of import statements relevant to the function's source file.
        - **context** (`FunctionContextInput`): Additional contextual information required for the function analysis.
*   **Methods:** *None*

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information about a specific method. It serves as a data transfer object, holding details such as the method's unique identifier, a list of other functions or methods it calls, a list of entities that call it, its arguments, and its docstring. This model is crucial for providing a standardized format for method-level context within a larger system.
*   **Instantiation:** `backend.main.main_workflow`
*   **Dependencies:** This class depends on pydantic.BaseModel for its core functionality and typing.List and typing.Optional for type hinting its fields.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, is initialized by providing values for its defined fields. These fields represent structured context information about a method, such as its identifier, calls it makes, where it is called from, its arguments, and its docstring.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions called by this method.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this method is called from.
        - **args** (`List[str]`): A list of argument names for the method.
        - **docstring** (`Optional[str]`): The docstring of the method, if available.
*   **Methods:** *None*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured context information necessary for analyzing a Python class. It serves as a data container, defining the expected format for dependencies, instantiation points, and detailed method contexts, facilitating a holistic understanding of a class's role and interactions within a larger system.
*   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an __init__ method. This constructor is responsible for validating and assigning the provided `dependencies`, `instantiated_by`, and `method_context` lists to the instance attributes upon object creation, ensuring data integrity according to the defined types.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies of the class.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing context for a specific method within the class.
*   **Methods:** *None*

#### Class: `ClassAnalysisInput`
*   **Summary:** The `ClassAnalysisInput` class is a Pydantic BaseModel designed to define the structured input required for performing a class analysis. It acts as a data contract, ensuring that all necessary information—such as the class identifier, its source code, relevant imports, and contextual details—is provided in a standardized format. This class is fundamental for systems that automate code analysis, providing a clear schema for data exchange.
*   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. As a `pydantic.BaseModel`, its constructor is implicitly generated by Pydantic based on the defined fields, allowing instantiation by passing keyword arguments corresponding to its attributes.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): The operational mode, which is fixed to 'class_analysis' for this specific input type, indicating the type of analysis to be performed.
        - **identifier** (`str`): The unique identifier or fully qualified name of the class that is to be analyzed.
        - **source_code** (`str`): The complete raw source code string of the entire class definition, including its methods and docstrings.
        - **imports** (`List[str]`): A list of strings, each representing an import statement relevant to the class or its containing module, providing necessary context for type resolution.
        - **context** (`ClassContextInput`): An object containing additional contextual information pertinent to the class, such as its dependencies and where it is instantiated within the larger codebase.
*   **Methods:** *None*

---
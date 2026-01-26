# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
*   **Description:** The "Repo Onboarding Agent" is a sophisticated automated documentation and code analysis tool designed to accelerate the onboarding process for developers. It parses a target repository to generate Abstract Syntax Trees (AST) and dependency graphs, then utilizes a multi-LLM architecture (supporting Google Gemini, OpenAI, and Ollama) to generate detailed, granular documentation for functions and classes. The system features a Streamlit-based frontend for interactive visualization and report management, and it employs a custom "TOON" data format to optimize token usage during analysis.
*   **Key Features:**
    - **Automated Code Analysis:** detailed AST parsing and file dependency graph generation.
    - **Multi-LLM Support:** Orchestrates analysis using Gemini, OpenAI, or local Ollama models.
    - **Granular Documentation:** Generates specific documentation for individual functions and classes.
    - **Interactive Frontend:** Streamlit UI for managing chats, viewing reports, and visualizing graphs.
    - **Token Optimization:** Uses a custom TOON format to reduce context window usage compared to JSON.
*   **Tech Stack:** Python, Streamlit, LangChain, NetworkX, PyMongo, GitPython, Pydantic, Matplotlib.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root[root] --> root_files[".env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json"]
    root --> SystemPrompts
    SystemPrompts --> SystemPrompts_files["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt"]
    root --> backend
    backend --> backend_files["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py"]
    root --> database
    database --> database_files["db.py"]
    root --> frontend
    frontend --> frontend_files[".streamlit/config.toml<br/>__init__.py<br/>frontend.py<br/>gifs/4j.gif"]
    root --> notizen
    notizen --> notizen_files["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken/...<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
    root --> result
    result --> result_files["[Various Report & Stats Files]"]
    root --> schemas
    schemas --> schemas_files["types.py"]
    root --> statistics
    statistics --> statistics_files["[Savings PNGs]"]
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

*Note: You can install these using `pip install -r requirements.txt`.*

### Setup Guide
1.  Clone the repository.
2.  Install dependencies using `pip install -r requirements.txt`.
3.  Set up environment variables by copying `.env.example` to `.env` and filling in your API keys (Gemini, OpenAI, or SCADSLLM) and Database credentials.
4.  Ensure MongoDB is running.

### Quick Startup
To launch the application interface:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
This project is primarily used by developers or teams needing to quickly understand the structure and functionality of a Python repository.

**Primary Use Cases:**
1.  **Repository Analysis:** Users input a GitHub URL, and the agent clones, parses, and analyzes the codebase structure.
2.  **Documentation Generation:** The agent uses LLMs to generate description and usage context for every function and class.
3.  **Onboarding Assistance:** New developers can query the system (via the Frontend chat) to understand specific modules or the overall architecture.
4.  **Token Optimization Analysis:** Users can view how much token overhead is saved by using the TOON format vs JSON.

**Primary Commands:**
*   **Start UI:** `streamlit run frontend/frontend.py`
*   **Run Backend Logic (Dev):** `python backend/main.py` (assumes hardcoded inputs or modification for CLI usage).

## 4. Architecture
*No specific architecture diagram was provided in the input configuration.*

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to systematically traverse the Abstract Syntax Tree (AST) of a Python source file. Its core responsibility is to extract and organize structural information, including import statements, top-level functions, and class definitions, into a structured schema. It differentiates between global functions and methods nested within classes, providing a comprehensive overview of the code's components.
*   **Instantiation:** *Analysis data not available for this component.*
*   **Dependencies:** The class depends on the `ast` module for its core functionality as an AST visitor and implicitly relies on `path_to_module` for resolving file paths to module paths.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes an `ASTVisitor` instance by storing the provided source code, file path, and project root. It calculates the module's qualified path and sets up an empty dictionary, `self.schema`, to accumulate discovered imports, functions, and classes. Additionally, it initializes `_current_class` to `None` to track the class context during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being visited.
        - **file_path** (`str`): The absolute path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the entire project, used for module path calculation.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method is invoked by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered during AST traversal. It iterates through each alias defined in the import statement and appends the full name of the imported module to the `imports` list within the visitor's `schema`. After processing the current node, it calls `generic_visit` to ensure continued traversal of its children.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an 'import module' statement.
        *   *Returns:*
        *   **Usage:** Calls `self.schema.append` to add import names and `self.generic_visit` to continue AST traversal.; Called by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent 'from module import name' statements. It iterates through the names imported from a specific module, constructs a fully qualified import string (e.g., 'module.name'), and appends it to the `imports` list in the visitor's `schema`. Following this, `generic_visit` is called to ensure all child nodes are also processed.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** Calls `self.schema.append` to add fully qualified import names and `self.generic_visit` to continue AST traversal.; Called by the `ast.NodeVisitor` framework when an `ast.ImportFrom` node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which define Python classes. It generates a unique identifier for the class, extracts its name, docstring, and the source code segment. A `class_info` dictionary is then created with these details and appended to the `classes` list within the visitor's `schema`. The `_current_class` attribute is temporarily set to this `class_info` to correctly associate nested methods, and then reset to `None` after `generic_visit` completes.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** Calls `ast.get_docstring`, `ast.get_source_segment`, `self.schema.append`, and `self.generic_visit`.; Called by the `ast.NodeVisitor` framework when an `ast.ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, representing both standalone functions and class methods. It checks the `_current_class` attribute to determine if the function is nested within a class. If so, it creates `method_context_info` and appends it to the `method_context` of the current class; otherwise, it creates `func_info` for a top-level function and appends it to the `functions` list in `self.schema`. Finally, `generic_visit` is called to continue AST traversal.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function or method definition.
        *   *Returns:*
        *   **Usage:** Calls `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit`. It also accesses and modifies `self._current_class` and `self.schema`.; Called by the `ast.NodeVisitor` framework when an `ast.FunctionDef` node is encountered during AST traversal.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is responsible for processing `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation delegates the entire processing logic to the `visit_FunctionDef` method. This ensures that asynchronous functions are handled identically to regular functions for the purpose of schema generation, collecting the same structural information.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** Calls `self.visit_FunctionDef` to process the asynchronous function node.; Called by the `ast.NodeVisitor` framework when an `ast.AsyncFunctionDef` node is encountered during AST traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for conducting a comprehensive analysis of a Git repository's Python files. It constructs a detailed Abstract Syntax Tree (AST) schema for the codebase and subsequently integrates inter-component relationship data, such as function calls and class instantiations. This class serves as a core utility for generating a structured, holistic overview of a Python project's architecture and its internal dependencies.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** The class depends on the 'ast' module for parsing Python code, the 'os' module for path manipulation, and the 'GitRepository' class for handling repository files.
*   **Constructor:**
    *   *Description:* The constructor for the ASTAnalyzer class initializes a new instance. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments, effectively creating a stateless instance ready for analysis operations.
    *   *Parameters:*
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates call relationship data, including both incoming and outgoing calls, into an existing AST schema. It iterates through the functions and classes defined within the `full_schema`, populating their respective 'calls', 'called_by', 'instantiated_by', and 'dependencies' contexts. The primary goal is to enrich the structural schema with dynamic interaction information, providing a more complete picture of the codebase's behavior.
        *   *Parameters:*
            - **full_schema** (`dict`): The comprehensive AST schema, which will be updated with relationship data.
            - **raw_relationships** (`dict`): A dictionary containing raw incoming and outgoing call relationships, typically structured with 'outgoing' and 'incoming' keys.
        *   *Returns:*
            - **full_schema** (`dict`): The updated 'full_schema' dictionary, now enriched with call relationship data for functions, classes, and methods.
        *   **Usage:** This method primarily uses dictionary and list manipulation methods such as 'get', 'items', 'startswith', 'add', 'sorted', and 'list' to process and merge data.; This method is not explicitly called by other methods within the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository)`
        *   *Description:* This method processes a given list of file objects from a Git repository to construct a comprehensive AST schema. It filters for Python files, parses their content using the 'ast' module, and then employs an 'ASTVisitor' to extract structural information like imports, functions, and classes. The extracted schema for each valid Python file is then added to a 'full_schema' dictionary, which is returned upon completion, with error handling for parsing failures.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, where each object is expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, used to provide context for the files, though its direct methods are not called within this function.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the complete AST schema of the analyzed repository, structured by file paths.
        *   **Usage:** This method calls 'os.path.commonpath', 'os.path.isfile', 'os.path.dirname', 'ast.parse', and instantiates 'ASTVisitor', subsequently calling 'visitor.visit' and accessing 'visitor.schema'.; This method is not explicitly called by other methods within the provided context.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system filepath into a Python module import path. It first attempts to determine the path relative to a specified project_root, falling back to the base filename if a ValueError occurs. The function then removes the '.py' extension if present and replaces system-specific path separators with dots. Finally, it handles '__init__.py' files by removing the '.__init__' suffix to yield the correct package module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative file system path to be converted into a module path.
    - **project_root** (`str`): The root directory of the project, used as a reference to calculate the relative module path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class, inheriting from NodeVisitor, is designed to analyze Python source code files and build a graph of their import dependencies. It processes both direct and relative import statements to identify how different modules and symbols within a repository relate to each other. The class maintains an 'import_dependencies' dictionary to store these relationships, mapping a source file to the set of modules it imports, providing a structured representation of the codebase's inter-file dependencies.
*   **Instantiation:** The class is not explicitly instantiated by any other functions or methods according to the provided context.
*   **Dependencies:** The class depends on `networkx`, `os`, `ast.Assign`, `ast.AST`, `ast.ClassDef`, `ast.FunctionDef`, `ast.Import`, `ast.ImportFrom`, `ast.Name`, `ast.NodeVisitor`, `ast.literal_eval`, `ast.parse`, `ast.walk`, `keyword.iskeyword`, `pathlib.Path`, `getRepo.GitRepository`, and `callgraph.make_safe_dot`.
*   **Constructor:**
    *   *Description:* This constructor initializes the FileDependencyGraph instance by setting the 'filename' attribute to the path of the file being analyzed and the 'repo_root' attribute to the root directory of the repository. These attributes are crucial for resolving file paths and understanding dependencies within the given repository context.
    *   *Parameters:*
        - **filename** (`str`): The path to the file currently being analyzed for dependencies.
        - **repo_root** (`Any`): The root directory of the repository, used as a base for resolving file paths and locating modules.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ImportFrom)`
        *   *Description:* This method resolves relative import statements, such as 'from .. import name1, name2', into actual module or symbol names. It calculates the correct base directory based on the import level and the current file's location. It then checks for the existence of corresponding module files or symbols exported via `__init__.py` files using nested helper functions `module_file_exists` and `init_exports_symbol`. If no matching modules or symbols are found, an ImportError is raised.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names that actually exist.
        *   **Usage:** This method does not explicitly call other methods, classes, or functions according to the provided context.; This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* This method processes AST nodes representing both 'import' and 'from ... import ...' statements. It iterates through the imported aliases and adds them to the 'import_dependencies' dictionary. The current 'filename' is mapped to a set of imported module names. If an optional 'base_name' is provided, it is used as the dependency; otherwise, the alias name itself is used. After processing, it calls `generic_visit` to continue AST traversal.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing the import statement being visited.
            - **base_name** (`str | None`): An optional base name for the module, used when the module part of a 'from ... import ...' statement has already been resolved.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call other methods, classes, or functions according to the provided context.; This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
        *   *Description:* This method specifically handles 'ImportFrom' AST nodes. For direct imports (e.g., 'from a.b.c import d'), it extracts the last part of the module name (e.g., 'c') and passes it to `visit_Import`. For relative imports (e.g., 'from .. import name'), it invokes `_resolve_module_name` to determine the actual module names before recording them via `visit_Import`. It includes error handling to print messages if relative import resolution fails.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call other methods, classes, or functions according to the provided context.; This method is not explicitly called by other functions or methods according to the provided context.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and creates an instance of `FileDependencyGraph` to traverse the AST. The visitor collects import relationships, which are then used to populate the graph with nodes for files and directed edges representing dependencies. The function returns the fully constructed dependency graph.
*   **Parameters:**
    - **filename** (`str`): The path to the file being analyzed for dependencies.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph representing the file-level import dependencies.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a directed graph representing the dependencies within a given Git repository. It iterates through all Python files in the repository, parses each file's content into an Abstract Syntax Tree (AST), and then builds a file-specific dependency graph using an external utility. Finally, it merges these individual file graphs into a single global directed graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to build the dependency graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependencies between Python files and their internal components across the entire repository.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is called by no other functions.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function identifies all Python files within a specified directory and its subdirectories. It takes a directory path as input, converts it to an absolute `pathlib.Path` object, and then recursively searches for all files ending with '.py'. For each found Python file, it calculates its path relative to the initial root directory. The function then returns a list of these relative `pathlib.Path` objects.
*   **Parameters:**
    - **directory** (`str`): The string path to the root directory from which to recursively find Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each object represents a Python file found recursively within the specified directory, with its path relative to the input directory.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is called by no other functions.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized and robust interface for interacting with various Large Language Models (LLMs) to generate structured documentation for Python functions and classes. It handles the complexities of LLM initialization, dynamic loading of system prompts from files, and model-specific batch size configuration. The class supports different LLM providers like Google Gemini, OpenAI, and custom Ollama/SCADSLLM endpoints, implementing mechanisms for efficient batch processing, error handling, and rate-limiting to ensure reliable and scalable API interactions.
*   **Instantiation:** No explicit instantiation points are identified in the provided context.
*   **Dependencies:** No external dependencies are explicitly listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper instance by validating the API key and loading system prompts for both function and class analysis from specified file paths. It dynamically configures the underlying LLM client (e.g., ChatGoogleGenerativeAI, ChatOpenAI, ChatOllama) based on the provided `model_name` and `base_url`. The constructor also wraps these LLM clients to enable structured output using Pydantic schemas for `FunctionAnalysis` and `ClassAnalysis`, and calls a private method to set model-specific batch processing settings.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen Large Language Model service.
        - **function_prompt_path** (`str`): The file path to the system prompt that guides the LLM in generating function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt that guides the LLM in generating class analysis.
        - **model_name** (`str`): The name of the LLM model to be used for generation, defaulting to 'gemini-2.0-flash-lite'.
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, such as Ollama or other OpenAI-compatible APIs. Defaults to None.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* This private method is responsible for setting the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It assigns optimized batch sizes for various known LLM models, including specific Gemini, Llama, and GPT versions, to enhance API call efficiency and manage rate limits. For any unrecognized models or custom API configurations, it defaults to a conservative batch size and logs a warning.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure the batch processing settings.
        *   *Returns:*
        *   **Usage:** This method calls `logging.warning` to log messages when an unknown model is encountered.; This method is called by the `__init__` method during the initialization of the LLMHelper class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* This method orchestrates the generation of structured documentation for a batch of functions using the configured LLM. It takes a list of `FunctionAnalysisInput` objects, converts them into JSON payloads, and constructs conversational prompts with the function system prompt. These prompts are then sent to the `function_llm` in batches, with built-in error handling for API calls and a rate-limiting delay between batches. It returns a list of `FunctionAnalysis` objects, with `None` for any failed generations.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary data for a function to be analyzed and documented by the LLM.
        *   *Returns:*
            - **null** (`List[Optional[FunctionAnalysis]]`): A list where each element is either a successfully generated `FunctionAnalysis` object or `None` if an error occurred during its generation.
        *   **Usage:** This method calls `json.dumps` to serialize input models, `function_input.model_dump` to convert input objects, `SystemMessage` and `HumanMessage` to construct conversational prompts, `self.function_llm.batch` to send requests to the LLM, `logging.info` and `logging.error` for logging, and `time.sleep` to implement rate limiting.; No explicit callers identified in the provided context.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* This method is responsible for generating structured documentation for a batch of classes by interacting with the configured LLM. It processes a list of `ClassAnalysisInput` objects, converting them into JSON payloads and preparing conversational prompts using the class system prompt. These prompts are then sent to the `class_llm` in batches, incorporating error handling for API calls and a rate-limiting delay between batches. The method returns a list of `ClassAnalysis` objects, with `None` indicating any failed documentation generations.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary data for a class to be analyzed and documented by the LLM.
        *   *Returns:*
            - **null** (`List[Optional[ClassAnalysis]]`): A list where each element is either a successfully generated `ClassAnalysis` object or `None` if an error occurred during its generation.
        *   **Usage:** This method calls `json.dumps` to serialize input models, `class_input.model_dump` to convert input objects, `SystemMessage` and `HumanMessage` to construct conversational prompts, `self.class_llm.batch` to send requests to the LLM, `logging.info` and `logging.error` for logging, and `time.sleep` to implement rate limiting.; No explicit callers identified in the provided context.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a test orchestrator and demonstration for the LLMHelper class. It defines pre-computed dummy data for function and class analysis inputs and their expected outputs, simulating the process of analyzing multiple Python functions. It then instantiates an LLMHelper, uses it to process the dummy function inputs, and aggregates the results into a final documentation structure, which is subsequently printed. The primary purpose is to validate the LLMHelper's integration and data flow.
*   **Parameters:**
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is called by no other functions.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class provides a unified interface for interacting with various Large Language Models (LLMs), including Google Gemini, OpenAI-compatible services, and Ollama. It handles the initialization of the appropriate LangChain LLM client based on the specified model name and API key, and loads a system prompt from a file. This class abstracts the underlying LLM provider, offering consistent methods for both direct response generation and streaming output.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the MainLLM instance by configuring the chosen LLM client, loading a system prompt, and setting up necessary credentials. It validates the API key and prompt file path, raising `ValueError` or `FileNotFoundError` if critical components are missing. Based on the `model_name`, it dynamically instantiates either `ChatGoogleGenerativeAI`, `ChatOpenAI`, or `ChatOllama` to handle subsequent LLM interactions.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the selected LLM service.
        - **prompt_file_path** (`str`): The file path to a text file containing the system-level prompt for the LLM.
        - **model_name** (`str`): The identifier for the LLM model to be used, defaulting to 'gemini-2.5-pro'. This determines which LangChain client is initialized.
        - **base_url** (`str | None`): An optional base URL for custom LLM API endpoints, primarily used for Ollama or other self-hosted models.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* The call_llm method sends a user's input to the configured LLM and retrieves a complete, single response. It constructs a list of messages, including the pre-loaded system prompt and the user's query, which are then passed to the LLM's `invoke` method. This method includes error handling to catch exceptions during the LLM call, logging any issues and returning `None` in case of failure.
        *   *Parameters:*
            - **user_input** (`str`): The textual input from the user to be processed by the LLM.
        *   *Returns:*
            - **content** (`str | None`): The full textual response generated by the LLM, or `None` if an error occurred during the call.
        *   **Usage:** This method calls `SystemMessage`, `HumanMessage`, `logging.info`, `self.llm.invoke`, and `logging.error`.; This method is not explicitly called by other functions or methods within the provided context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* The stream_llm method facilitates a real-time, streaming interaction with the LLM, yielding chunks of content as they are generated. It prepares the conversation messages, including the system prompt and user input, and then utilizes the LLM's `stream` method. The method iterates through the incoming stream, yielding each content chunk, and incorporates error handling to provide an error message within the stream if an exception occurs.
        *   *Parameters:*
            - **user_input** (`str`): The textual input from the user for which a streaming response is requested.
        *   *Returns:*
            - **chunk.content** (`generator[str]`): A generator that yields individual string chunks of the LLM's response as they become available, or an error message string if an exception occurs.
        *   **Usage:** This method calls `SystemMessage`, `HumanMessage`, `logging.info`, `self.llm.stream`, and `logging.error`.; This method is not explicitly called by other functions or methods within the provided context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to systematically extract and consolidate fundamental project information from common project files such as README.md, pyproject.toml, and requirements.txt. It initializes a structured dictionary to hold various project details, including project overview, installation instructions, and dependencies. Through a series of private parsing methods, it processes these files, prioritizing pyproject.toml for core metadata, and then formats the collected data into a comprehensive project information object.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components in the provided context.
*   **Dependencies:** The class relies on external modules such as 're' for regular expressions, 'os' for path manipulation, and 'tomllib' for parsing TOML files.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjektInfoExtractor instance by setting a constant string 'INFO_NICHT_GEFUNDEN' as a placeholder for missing information. It then creates a nested dictionary `self.info` which serves as the primary data structure to store extracted project details, pre-populating all fields with this placeholder.
    *   *Parameters:*
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content: str)`
        *   *Description:* This method takes a string content as input and removes any null bytes ('\x00') present within it. Null bytes can often appear due to encoding errors, such as reading a UTF-16 encoded file as UTF-8. If the input content is empty or None, the method returns an empty string, ensuring that subsequent parsing operations receive clean, valid string data.
        *   *Parameters:*
            - **content** (`str`): The string content to be cleaned of null bytes.
        *   *Returns:*
            - **** (`str`): The cleaned string with all null bytes removed, or an empty string if the input was empty.
        *   **Usage:** This method does not make any external calls.; This method is called by _parse_readme, _parse_toml, and _parse_requirements.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This method searches for a specific file within a given list of file-like objects. It iterates through each file in the 'dateien' list and checks if its path (case-insensitively) ends with any of the provided 'patterns'. The first file that matches any of the patterns is returned. If no file matches any of the specified patterns after checking all possibilities, the method returns None.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of string patterns to match against the end of file paths (e.g., ['readme.md']). The matching is case-insensitive.
            - **dateien** (`List[Any]`): A list of file-like objects, where each object is expected to have a 'path' attribute (e.g., 'datei.path').
        *   *Returns:*
            - **** (`Optional[Any]`): The first file object whose path matches one of the patterns, or None if no matching file is found.
        *   **Usage:** This method does not make any external calls.; This method is called by extrahiere_info.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This method extracts text content from a Markdown string that appears under a level 2 heading (##) matching one of the specified keywords. It constructs a regular expression pattern to find headings like '## Keyword' and captures all subsequent text until another level 2 heading or the end of the document. The search is performed case-insensitively and allows newlines within the captured content. If a matching section is found, its stripped content is returned; otherwise, None is returned.
        *   *Parameters:*
            - **inhalt** (`str`): The Markdown content string from which to extract a section.
            - **keywords** (`List[str]`): A list of keywords to match against the Markdown section headings (e.g., 'Features', 'Installation').
        *   *Returns:*
            - **** (`Optional[str]`): The stripped text content of the matched Markdown section, or None if no section matching the keywords is found.
        *   **Usage:** This method calls re.escape, re.compile, re.IGNORECASE, re.DOTALL, pattern.search, and match.group.; This method is called by _parse_readme.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This method parses the content of a README file to extract various project details and update the `self.info` dictionary. It first cleans the input content using `_clean_content`. It then attempts to extract the project title from a level 1 Markdown heading and a general description. For specific sections like 'Key Features', 'Tech Stack', 'Status', 'Installation', and 'Quick Start Guide', it utilizes the `_extrahiere_sektion_aus_markdown` method to find and extract relevant text based on predefined keywords.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the README file to be parsed.
        *   *Returns:*
        *   **Usage:** This method calls self._clean_content, re.search, and self._extrahiere_sektion_aus_markdown.; This method is called by extrahiere_info.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This method parses the content of a `pyproject.toml` file to extract project-related information such as the project name, description, and dependencies. It begins by cleaning the input content using `_clean_content`. It then checks for the availability of the `tomllib` module, printing a warning and returning if it's not installed. If `tomllib` is available, it attempts to load and parse the TOML content. Extracted 'name', 'description', and 'dependencies' from the `[project]` table are used to update the `self.info` dictionary. Error handling is included for `tomllib.TOMLDecodeError` during parsing.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the `pyproject.toml` file to be parsed.
        *   *Returns:*
        *   **Usage:** This method calls self._clean_content, print, tomllib.loads, and data.get.; This method is called by extrahiere_info.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This method parses the content of a `requirements.txt` file to extract project dependencies. It first cleans the input content using `_clean_content`. It only proceeds to extract dependencies if the `dependencies` field in `self.info` is still set to the 'INFO_NICHT_GEFUNDEN' placeholder, indicating that dependencies haven't been found from a higher-priority source like `pyproject.toml`. It splits the content into lines, filters out empty lines and comments, and then stores the valid dependency strings as a list in `self.info`.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the `requirements.txt` file to be parsed.
        *   *Returns:*
        *   **Usage:** This method calls self._clean_content.; This method is called by extrahiere_info.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This is the main orchestration method responsible for extracting comprehensive project information from various source files. It first identifies relevant files like README, pyproject.toml, and requirements.txt using `_finde_datei`. It then parses these files in a specific order of priority: pyproject.toml, then requirements.txt, and finally README.md, allowing information from higher-priority files to override or supplement lower-priority ones. After parsing, it formats the collected dependencies and, if a project title is still missing, attempts to derive one from the provided repository URL. The method concludes by returning the fully populated `self.info` dictionary.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have 'path' and 'content' attributes, representing the files to be analyzed.
            - **repo_url** (`str`): The URL of the repository, used as a fallback to derive a project title if none is found in the files.
        *   *Returns:*
            - **** (`Dict[str, Any]`): A dictionary containing all extracted and formatted project information.
        *   **Usage:** This method calls self._finde_datei, self._parse_toml, self._parse_requirements, self._parse_readme, os.path.basename, and repo_url.removesuffix.; This method is not explicitly called by other methods within the provided context, suggesting it is a primary public interface for the class.

### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST NodeVisitor designed to construct a directed call graph for a given Python source file. It traverses the Abstract Syntax Tree (AST) of a file, identifying function definitions, class definitions, import statements, and function calls. The class maintains internal state to track the current file, function, and class context, resolving call targets by considering local definitions and import mappings to build a comprehensive representation of function-to-function calls within the codebase.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components in the provided context.
*   **Dependencies:** This class does not explicitly list external dependencies in its context, but it uses `ast` for parsing and `networkx` for graph representation.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph instance with the filename being analyzed. It sets up internal state variables such as the current function and class, and initializes data structures like dictionaries for local definitions, import mappings, and edges, along with a NetworkX DiGraph to store the call graph.
    *   *Parameters:*
        - **filename** (`str`): The path or name of the source file being analyzed to build the call graph.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node: ast.AST)`
        *   *Description:* This private helper method recursively traverses an AST node to extract its full dotted name components. It handles `ast.Call` nodes by processing their `func` attribute, `ast.Name` nodes by returning their ID, and `ast.Attribute` nodes by recursively processing their value and appending the attribute name. The method aims to break down complex call expressions into a list of their constituent name parts.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node to be recursively processed to extract name components, typically an ast.Call, ast.Name, or ast.Attribute node.
        *   *Returns:*
            - **parts** (`list[str]`): A list of strings representing the dotted name components of the call or attribute, e.g., ['pkg', 'mod', 'Class', 'method'].
        *   **Usage:** This method calls itself recursively.; This method is called by other methods within the CallGraph class.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* This private method takes a list of potential callee name components and resolves them into fully qualified names. It prioritizes resolution by first checking local definitions, then the import mapping, and finally constructs a full name based on the current file and class context if no explicit mapping is found. This ensures that calls to local functions, imported modules/functions, and class methods are correctly identified.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains the name components (steps) of a potential callee.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of fully qualified string names for the resolved callees.
        *   **Usage:** This method accesses internal attributes such as self.local_defs and self.import_mapping.; This method is called by other methods within the CallGraph class.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None)`
        *   *Description:* This private helper method constructs a fully qualified name for a given basename, optionally including a class name. It prepends the filename and, if provided, the class name to the basename, separated by '::'. This standardization ensures that all function and method identifiers in the call graph are unique and fully traceable to their origin.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method (e.g., 'my_function').
            - **class_name** (`str | None`): The name of the class if the entity is a method, otherwise None.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name, e.g., 'filename::ClassName::methodName' or 'filename::functionName'.
        *   **Usage:** This method does not make any explicit calls to other methods or functions.; This method is called by other methods within the CallGraph class.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private helper method determines the identifier of the current calling context. If a function is currently being visited, its full name is returned. Otherwise, it returns a placeholder indicating either the global scope of the current file or a generic global scope if the filename is not available. This is crucial for correctly attributing calls in the graph.
        *   *Parameters:*
        *   *Returns:*
            - **caller_identifier** (`str`): A string representing the identifier of the current caller, which could be a function's full name, '<filename>', or '<global-scope>'.
        *   **Usage:** This method does not make any explicit calls to other methods or functions.; This method is called by other methods within the CallGraph class.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method is an AST visitor for `ast.Import` nodes. It iterates through the aliases defined in the import statement, extracting the module name and its potential alias. It then populates the `import_mapping` dictionary, associating the alias (or original name) with the actual module name. After processing, it calls `generic_visit` to continue traversing the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The `ast.Import` node representing an import statement like `import module as alias`.
        *   *Returns:*
        *   **Usage:** This method calls `self.generic_visit` to continue AST traversal.; This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.Import` node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method is an AST visitor for `ast.ImportFrom` nodes. It extracts the module name from which objects are imported and then iterates through the imported names and their aliases. It updates the `import_mapping` dictionary to record the relationship between the alias (or original name) and the source module. This helps in resolving fully qualified names for imported entities.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The `ast.ImportFrom` node representing an import statement like `from module import name as alias`.
        *   *Returns:*
        *   **Usage:** This method does not make any explicit calls to other methods or functions.; This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.ImportFrom` node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is an AST visitor for `ast.ClassDef` nodes. It temporarily updates the `current_class` attribute to the name of the class being visited, allowing subsequent method definitions within that class to be correctly associated. After visiting the class's children using `generic_visit`, it restores the `current_class` to its previous value, ensuring proper context management during AST traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The `ast.ClassDef` node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method calls `self.generic_visit` to continue AST traversal.; This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.ClassDef` node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method is an AST visitor for `ast.FunctionDef` nodes. It generates a full name for the function, considering the current class context, and stores it in `local_defs`. It then sets the `current_function` to this full name, adds the function as a node to the call graph, and traverses its body using `generic_visit`. Finally, it adds the function to the `function_set` and restores the previous `current_function` context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The `ast.FunctionDef` node representing a function definition.
        *   *Returns:*
        *   **Usage:** This method calls `_make_full_name`, `self.graph.add_node`, and `self.generic_visit`.; This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.FunctionDef` node is encountered, and explicitly by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method is an AST visitor for `ast.AsyncFunctionDef` nodes. It acts as a wrapper, simply delegating the processing of asynchronous function definitions to the `visit_FunctionDef` method. This allows the call graph builder to treat both synchronous and asynchronous function definitions uniformly for the purpose of identifying and adding them to the graph.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The `ast.AsyncFunctionDef` node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** This method calls `self.visit_FunctionDef`.; This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.AsyncFunctionDef` node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method is an AST visitor for `ast.Call` nodes, responsible for identifying function calls and recording them in the call graph. It first determines the current caller, then uses `_recursive_call` to extract the callee's name components, and `_resolve_all_callee_names` to get the fully qualified callee names. Finally, it adds edges from the caller to all resolved callees in the `edges` dictionary, then continues AST traversal.
        *   *Parameters:*
            - **node** (`ast.Call`): The `ast.Call` node representing a function call expression.
        *   *Returns:*
        *   **Usage:** This method calls `_current_caller`, `_recursive_call`, `_resolve_all_callee_names`, and `self.generic_visit`.; This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.Call` node is encountered.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node: ast.If)`
        *   *Description:* This method is an AST visitor for `ast.If` nodes. It includes special handling for the `if __name__ == "__main__"` block, which is common in Python scripts. When such a block is detected, it temporarily sets the `current_function` to '<main_block>' to correctly attribute calls within this entry point. For other `if` statements, it simply proceeds with a generic visit, ensuring all branches are traversed.
        *   *Parameters:*
            - **node** (`ast.If`): The `ast.If` node representing an if statement.
        *   *Returns:*
        *   **Usage:** This method calls `self.generic_visit` to continue AST traversal.; This method is implicitly called by the `ast.NodeVisitor` mechanism when an `ast.If` node is encountered.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and an output file path, then generates a DOT file with 'safe' node names. It creates a copy of the input graph and generates a mapping from original node identifiers to simple, unique string identifiers (e.g., "n0", "n1"). The graph's nodes are relabeled using this mapping to ensure compatibility with DOT format. The original node names are then stored as 'label' attributes on the newly relabeled nodes. Finally, the modified graph is written to the specified output path as a DOT file.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph whose nodes need to be made safe for DOT output.
    - **out_path** (`str`): The file path where the DOT representation of the graph will be saved.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is called by no other functions.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** The build_filtered_callgraph function constructs a directed call graph for a given Git repository. It first processes all Python files within the repository to identify a set of 'own functions' using an Abstract Syntax Tree (AST) visitor. Subsequently, it iterates through these parsed files again to determine caller-callee relationships. Only calls where both the caller and callee are identified as 'own functions' are added as edges to the resulting NetworkX directed graph, which is then returned.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which to extract files and build the call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the filtered call graph, containing only edges between functions identified as 'own functions' within the repository.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content: str)`
*   **Description:** This function, `wrap_cdata`, is designed to encapsulate a given string `content` within XML CDATA tags. It constructs an f-string that prepends "<![CDATA[\n" and appends "\n]]>" to the provided content. This process ensures that the content, including any special characters, is treated as character data and not parsed by an XML parser. The function directly returns the newly formed CDATA-wrapped string.
*   **Parameters:**
    - **content** (`str`): The string content that needs to be wrapped inside CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A new string with the original content enclosed within CDATA tags, including leading and trailing newlines.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs: Iterable[Output], image_list: List[Dict[str, str]])`
*   **Description:** This function processes a list of notebook output objects to extract their content, handling various output types. It prioritizes image data (PNG or JPEG) from 'display_data' or 'execute_result' outputs, decoding Base64 strings and storing them in a provided `image_list` while returning an XML placeholder. For other text-based outputs, it appends plain text, stream output, or formatted error messages directly. The function returns a consolidated list of these extracted content snippets, which can include image placeholders or text.
*   **Parameters:**
    - **outputs** (`Iterable[Output]`): An iterable collection of output objects, typically from notebook execution, which can contain display data, execution results, streams, or errors.
    - **image_list** (`List[Dict[str, str]]`): A mutable list passed by reference, used to accumulate dictionaries of image data (mime type and Base64 string) extracted from the outputs. This list is modified in place.
*   **Returns:**
    - **extracted_content_snippets** (`List[str]`): A list of strings, where each string represents a processed content snippet. These snippets can be XML placeholders for images, plain text, stream output text, or formatted error messages.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type: str)`
*   **Description:** This function, process_image, is designed to handle and store base64 encoded image data. It takes a mime_type as input and checks for corresponding data in an external 'data' dictionary. If found, it cleans the base64 string, appends the image data to an external 'image_list', and returns a formatted placeholder string. This placeholder includes the image's index and MIME type. The function includes error handling for decoding issues, returning an error message string in such cases. If the specified mime_type is not present in the 'data' dictionary, it returns None.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type string identifying the image data to be processed.
*   **Returns:**
    - **image_placeholder_tag** (`str`): A string formatted as an image placeholder tag, containing the image's assigned index and its MIME type.
    - **error_message_tag** (`str`): An error message string, formatted as an XML-like tag, indicating a failure during image decoding.
    - **no_data_found** (`None`): Indicates that no image data corresponding to the provided MIME type was found.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content: str)`
*   **Description:** This function converts the content of a Jupyter notebook, provided as a string, into a structured XML format. It processes each cell, categorizing them as markdown or code. Markdown cells' source is directly embedded, while code cells' source is wrapped in CDATA. If code cells have outputs, these outputs are also processed, potentially extracting images, and then embedded as CDATA within an output cell tag. The function handles parsing errors by returning a specific error message.
*   **Parameters:**
    - **file_content** (`str`): The raw string content of a Jupyter notebook file, expected to be in JSON format.
*   **Returns:**
    - **xml_representation** (`str`): A string containing the XML representation of the notebook's cells, or an error message if parsing fails.
    - **extracted_images** (`list`): A list of any images extracted from the notebook's cell outputs.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files: list)`
*   **Description:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It filters the input `repo_files` to find those with a `.ipynb` extension. For each identified notebook, it logs its processing and then calls `convert_notebook_to_xml` to transform its content into XML and extract associated images. The function aggregates these conversion results, mapping each notebook's path to its corresponding XML output and images, and finally returns this dictionary of processed notebooks.
*   **Parameters:**
    - **repo_files** (`list`): A list of file-like objects from a repository. Each object is expected to have `path` (string) and `content` (string) attributes.
*   **Returns:**
    - **results** (`dict`): A dictionary where keys are the paths of processed Jupyter notebooks (string) and values are dictionaries containing the converted XML output (string) and any extracted images (type depends on `convert_notebook_to_xml`'s return type for images).
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class serves as an abstraction for a single file within a Git repository, emphasizing lazy loading of its content and metadata. It stores the file's path and its originating Git tree upon initialization. Through properties, it provides on-demand access to the Git blob object, the file's decoded content, and its size, raising an error if the file is not found. The class also includes utility methods for basic content analysis and for serializing its data into a dictionary format.
*   **Instantiation:** The class is not explicitly instantiated by any other components in the provided context.
*   **Dependencies:** The class does not have any explicit functional dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* This constructor initializes a RepoFile object by setting its file path and the Git Tree object from which it originates. It also sets up internal attributes (`_blob`, `_content`, `_size`) to `None`, indicating that these properties will be loaded lazily upon first access.
    *   *Parameters:*
        - **file_path** (`str`): Der Pfad zur Datei innerhalb des Repositories.
        - **commit_tree** (`git.Tree`): Das Tree-Objekt des Commits, aus dem die Datei stammt.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if the `_blob` attribute is already set; if not, it attempts to retrieve the blob from the `_tree` using the stored `path`. If the file is not found in the commit tree, it raises a `FileNotFoundError`, ensuring that blob access is efficient and robust.
        *   *Parameters:*
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:** This method does not explicitly call other functions or methods from the provided context.; This method is not explicitly called by other functions or methods from the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It first checks if the `_content` attribute is already populated. If not, it accesses the `blob` property (which handles its own lazy loading), reads its data stream, and decodes it using UTF-8, ignoring any errors, to provide the file's textual content.
        *   *Parameters:*
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:** This method does not explicitly call other functions or methods from the provided context.; This method is not explicitly called by other functions or methods from the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the `_size` attribute is already set. If not, it retrieves the size from the `blob` property (which ensures the blob is loaded) and stores it, making the file size readily available upon request.
        *   *Parameters:*
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:** This method does not explicitly call other functions or methods from the provided context.; This method is not explicitly called by other functions or methods from the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function, demonstrating how to process the file's content. It calculates the number of words in the file's content by accessing the `content` property, splitting the content by whitespace, and then returning the length of the resulting list of words.
        *   *Parameters:*
        *   *Returns:*
            - **word_count** (`int`): The total number of words found in the file content.
        *   **Usage:** This method does not explicitly call other functions or methods from the provided context.; This method is not explicitly called by other functions or methods from the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This special method provides a developer-friendly string representation of the `RepoFile` object. It returns a string that includes the class name and the path of the file, making it easy to identify instances in debugging or logging contexts.
        *   *Parameters:*
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:** This method does not explicitly call other functions or methods from the provided context.; This method is not explicitly called by other functions or methods from the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content: bool)`
        *   *Description:* This method converts the `RepoFile` object into a dictionary representation, useful for serialization or structured data output. It includes the file's path, its base name, size, and type. Optionally, if `include_content` is set to `True`, the full content of the file will also be added to the dictionary.
        *   *Parameters:*
            - **include_content** (`bool`): If True, the file's content will be included in the dictionary.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing the file's metadata and optionally its content.
        *   **Usage:** This method does not explicitly call other functions or methods from the provided context.; This method is not explicitly called by other functions or methods from the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with Git repositories programmatically. It handles the cloning of a remote repository into a temporary local directory upon instantiation, ensuring a clean workspace. The class offers functionalities to list all files, represent the repository's structure as a hierarchical tree, and manage the lifecycle of the temporary directory through context management for automatic cleanup.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** The class depends on `tempfile` for temporary directory management, `git.Repo` and `git.GitCommandError` for Git operations, and `logging` for informational messages.
*   **Constructor:**
    *   *Description:* This constructor initializes a GitRepository object by cloning a specified Git repository into a temporary directory. It sets up instance attributes such as the repository URL, the path to the temporary directory, the GitPython Repo object, and initializes lists for files. It also captures the latest commit and its tree, handling potential GitCommandError during cloning and cleaning up if an error occurs.
    *   *Parameters:*
        - **repo_url** (`string`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It uses the `git.ls_files()` command to get file paths, then iterates through these paths to create `RepoFile` objects. These `RepoFile` instances are stored in the `self.files` attribute and also returned by the method.
        *   *Parameters:*
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:** This method calls `self.repo.git.ls_files()` and the `RepoFile` constructor.; This method is called by `get_file_tree`.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is responsible for cleaning up resources used by the `GitRepository` instance. Specifically, it prints a message indicating the deletion of the temporary directory and then sets `self.temp_dir` to `None`. This effectively marks the temporary directory for cleanup, although the actual deletion of the directory content is handled by the `tempfile` module's lifecycle.
        *   *Parameters:*
        *   *Returns:*
        *   **Usage:** This method does not explicitly call other methods or functions within the provided snippet, beyond a `print` statement.; This method is called by `__init__` (in case of cloning error) and `__exit__`.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This special method allows the `GitRepository` class to be used as a context manager. When entering a `with` statement, this method is invoked, and it simply returns the instance of the `GitRepository` itself. This enables the object to be bound to a variable in the `as` clause of the `with` statement.
        *   *Parameters:*
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   **Usage:** This method does not call any other methods or functions.; This method is implicitly called when the `GitRepository` object is used in a `with` statement.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type: type | None, exc_val: Exception | None, exc_tb: traceback | None)`
        *   *Description:* This special method is part of the context manager protocol. It is automatically called when exiting a `with` statement, regardless of whether an exception occurred. Its primary responsibility is to ensure that the `close()` method is invoked, which handles the cleanup of the temporary repository directory.
        *   *Parameters:*
            - **exc_type** (`type | None`): The type of the exception that caused the exit, or None if no exception occurred.
            - **exc_val** (`Exception | None`): The exception instance that caused the exit, or None.
            - **exc_tb** (`traceback | None`): The traceback object associated with the exception, or None.
        *   *Returns:*
        *   **Usage:** This method calls `self.close()`.; This method is implicitly called when exiting a `with` statement where the `GitRepository` object is the context manager.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content: bool)`
        *   *Description:* This method constructs a hierarchical tree representation of the files within the Git repository. If `self.files` is not already populated, it first calls `get_all_files()` to retrieve them. It then iterates through each `RepoFile` object, splitting its path to build a nested dictionary structure that mimics the directory hierarchy. Each file is appended to its respective directory's `children` list, optionally including its content.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether the content of the files should be included in the dictionary representation. Defaults to `False`.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the file tree, with 'name', 'type', and 'children' keys, where children can be directories or file dictionaries.
        *   **Usage:** This method calls `self.get_all_files()` and `file_obj.to_dict()`.; This method is not explicitly called by other methods within the provided class definition.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart to visually compare the number of JSON tokens against TOON tokens. It calculates and displays a savings percentage in the chart's title. The chart includes labels, colors, a grid, and token counts displayed directly above each bar, before saving the generated plot to a specified output file path and closing the plot to free up memory.
*   **Parameters:**
    - **json_tokens** (`int`): The count of tokens for the JSON format.
    - **toon_tokens** (`int`): The count of tokens for the TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings, displayed in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart image will be saved.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the net operational time by adjusting the total elapsed duration for estimated rate-limiting sleep times. It first determines the total duration between a start and end timestamp. If the provided `model_name` does not begin with "gemini-", the function returns the total duration without any adjustments. For "gemini-" models, it calculates the number of batches and estimates the total sleep time based on a fixed duration per sleep interval. This estimated sleep time is then subtracted from the total duration, ensuring the final net time is not negative.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp of the operation.
    - **end_time** (`float`): The ending timestamp of the operation.
    - **total_items** (`int`): The total number of items processed during the operation.
    - **batch_size** (`int`): The number of items processed per batch.
    - **model_name** (`str`): The name of the model used, which determines if rate-limit sleep adjustments are applied.
*   **Returns:**
    - **net_duration** (`float`): The calculated net duration in seconds, adjusted for estimated rate-limiting sleep times if the model is a 'gemini-' model, or the total duration otherwise.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: Callable | None)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive analysis of a GitHub repository. It handles the extraction of API keys and model names, clones the specified repository, and then proceeds to extract basic project information, construct a file tree, and analyze code relationships. It builds and enriches an Abstract Syntax Tree (AST) schema, prepares inputs for a Helper LLM to analyze individual functions and classes, and finally utilizes a Main LLM to generate a comprehensive report based on the gathered data. The workflow also includes token evaluation and saves the final report along with performance metrics.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL for analysis.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs ('scadsllm_base_url', 'ollama') required for external service authentication.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' language models to be used in the workflow, e.g., 'gpt-5-mini', 'gemini-pro'.
    - **status_callback** (`Callable | None`): An optional callable function that receives a string message for real-time status updates during the workflow's execution.
*   **Returns:**
    - **report** (`str`): The comprehensive final report generated by the Main LLM, typically in markdown format.
    - **metrics** (`dict`): A dictionary containing performance metrics (e.g., helper_time, main_time, total_time), model names (helper_model, main_model), and token savings data (json_tokens, toon_tokens, savings_percent).
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_status`
*   **Signature:** `def update_status(msg: str)`
*   **Description:** The `update_status` function is designed to handle status updates within the application. It accepts a message and, if a `status_callback` function is available in its scope, it invokes that callback with the provided message. Additionally, it logs the message at the INFO level using the `logging` module, ensuring that status updates are recorded.
*   **Parameters:**
    - **msg** (`str`): The message string to be used for the status update and logging.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback: Callable)`
*   **Description:** The `notebook_workflow` function orchestrates the end-to-end analysis of Jupyter notebooks from a specified GitHub repository. It begins by extracting the repository URL from the input, cloning the repository, and processing its notebook files into an XML format. Concurrently, it extracts basic project information. The function then dynamically selects an appropriate Large Language Model (LLM) based on the provided model name and API keys. It iterates through each notebook, generating a specific payload for the LLM (including basic project info, notebook path, XML content, and embedded images), and calls the LLM to produce an individual report. Finally, all individual reports are concatenated into a single `final_report`, which is then saved to a markdown file, and a dictionary containing the report and execution metrics is returned.
*   **Parameters:**
    - **input** (`str`): The input string, expected to contain a GitHub repository URL from which notebooks will be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various Large Language Model providers (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
    - **model** (`str`): The name of the Large Language Model to be used for generating reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`Callable`): An optional callback function that receives status messages during the workflow execution. Defaults to `None`.
*   **Returns:**
    - **analysis_result** (`dict`): A dictionary containing the `report` (str) of the analyzed notebooks and `metrics` (dict) detailing execution times and models used.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not called by any other functions.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info: object, nb_path: str, xml_content: str, images: list)`
*   **Description:** This function constructs a multimodal payload suitable for the Gemini API. It takes basic information, a notebook path, XML content that may include image placeholders, and a list of image data. The function serializes the basic information and notebook path into an introductory JSON text block. It then processes the XML content, extracting text segments and converting image placeholders into base64 encoded image URLs, assembling them into a structured list of content blocks. The final output is a list of dictionaries, where each dictionary represents either a text segment or an image.
*   **Parameters:**
    - **basic_info** (`object`): A dictionary or object containing basic information to be included as context in the payload.
    - **nb_path** (`str`): The file path of the current notebook, included as context in the payload.
    - **xml_content** (`str`): The XML string content of the notebook, which may contain image placeholders to be replaced.
    - **images** (`list`): A list of image data objects. Each object is expected to contain a 'data' key with a base64 encoded image string and potentially a 'mime' type.
*   **Returns:**
    - **payload_content** (`list`): A list of dictionaries, each representing a content block for a Gemini API payload. Blocks are of type 'text' or 'image_url'.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

### File: `backend/relationship_analyzer.py`

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to identify and map out definitions of functions, methods, and classes, and to resolve calls between these entities. It constructs a comprehensive call graph representing the relationships within the codebase, which can then be used to understand code structure and dependencies. The class provides methods to find Python files, collect definitions, resolve calls, and present the relationships in a raw, outgoing/incoming format.
*   **Instantiation:** This class is not explicitly instantiated by other methods or classes within the provided context.
*   **Dependencies:** This class does not have any explicit external dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer instance by setting the project's root directory and preparing internal data structures. It converts the provided project_root to an absolute path and initializes dictionaries for definitions, a defaultdict for the call graph, a dictionary to store ASTs of files, and a set of directories to ignore during file traversal.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all relevant Python files within the project, then iterates through them to collect all function, method, and class definitions. Following definition collection, it resolves calls made between these entities across all files. Finally, it clears the stored file ASTs to free up memory and returns the constructed call graph.
        *   *Parameters:*
        *   *Returns:*
            - **call_graph** (`collections.defaultdict[list]`): A dictionary-like object representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:** This method does not explicitly call other methods, classes, or functions within the provided context.; This method is not explicitly called by other methods within the provided context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* This method processes the internal call graph to generate a more structured representation of relationships. It creates two dictionaries: 'outgoing' to list entities called by a specific caller, and 'incoming' to list entities that call a specific callee. The resulting relationships are sorted and returned as a dictionary containing both outgoing and incoming call sets.
        *   *Parameters:*
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, 'outgoing' and 'incoming'. Each value is a dictionary mapping entity identifiers to sorted lists of related entity identifiers.
        *   **Usage:** This method does not explicitly call other methods, classes, or functions within the provided context.; This method is not explicitly called by other methods within the provided context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private helper method is responsible for recursively traversing the project directory structure, starting from `self.project_root`. It identifies all Python files while skipping directories specified in `self.ignore_dirs`. The method compiles a list of absolute paths to all discovered Python files.
        *   *Parameters:*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found in the project, excluding ignored directories.
        *   **Usage:** This method does not explicitly call other methods, classes, or functions within the provided context.; This method is not explicitly called by other methods within the provided context.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath: str)`
        *   *Description:* This private method processes a given Python file to extract all function, method, and class definitions. It reads the file, parses its Abstract Syntax Tree (AST), and then walks the AST to identify `FunctionDef` and `ClassDef` nodes. For each definition, it constructs a unique path name and stores its file path, line number, and type ('function', 'method', or 'class') in `self.definitions`. It also stores the AST in `self.file_asts` for later use.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file to be analyzed for definitions.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call other methods, classes, or functions within the provided context.; This method is not explicitly called by other methods within the provided context.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree: ast.AST, node: ast.AST)`
        *   *Description:* This private helper method is used to find the immediate parent node of a given AST node within a larger AST. It iterates through all nodes in the AST and checks their children to identify if any child matches the target node. This is crucial for determining if a `FunctionDef` node is a standalone function or a method within a `ClassDef`.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree (AST) to search within.
            - **node** (`ast.AST`): The specific AST node for which to find the parent.
        *   *Returns:*
            - **parent** (`ast.AST | None`): The parent AST node if found, otherwise None.
        *   **Usage:** This method does not explicitly call other methods, classes, or functions within the provided context.; This method is not explicitly called by other methods within the provided context.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath: str)`
        *   *Description:* This private method takes a file path, retrieves its AST, and then uses a `CallResolverVisitor` to identify all function and method calls within that file. It populates the `self.call_graph` by extending the list of callers for each identified callee. Error handling is included to log any issues during the call resolution process.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   **Usage:** This method does not explicitly call other methods, classes, or functions within the provided context.; This method is not explicitly called by other methods within the provided context.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST NodeVisitor designed to traverse a Python Abstract Syntax Tree (AST) and identify all function and method calls within a given source file. It resolves the fully qualified names of both callers and callees by maintaining a scope of imported names and inferred instance types. The primary purpose is to build a comprehensive map of call relationships, storing details like the caller's file, line number, and type for each resolved callee.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** This class depends on the 'ast' module for Abstract Syntax Tree traversal, 'os' for path manipulation, and 'collections.defaultdict' for managing call relationships. It also implicitly relies on the 'path_to_module' utility function.
*   **Constructor:**
    *   *Description:* This constructor initializes the CallResolverVisitor with the necessary context for AST traversal and call resolution. It sets up attributes to store the file path, module path, known definitions, a scope for name resolution, inferred instance types, the current caller's identifier, the current class name, and a defaultdict to accumulate detected calls.
    *   *Parameters:*
        - **filepath** (`str`): The path to the source file being analyzed by the visitor.
        - **project_root** (`str`): The root directory of the project, used to determine the module path.
        - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) within the project for resolving call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is invoked when the AST visitor encounters a class definition. It temporarily updates the `current_class_name` attribute to the name of the class being visited, which is crucial for correctly forming fully qualified names for methods defined within that class. After processing the class's children through a generic visit, it restores the `current_class_name` to its previous value, ensuring proper scope management during the AST traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
        *   **Usage:** This method calls self.generic_visit(node) to continue the AST traversal.; This method is called by the ast.NodeVisitor's dispatch mechanism when a ClassDef node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method handles function definition nodes in the AST. It constructs the fully qualified identifier for the function, taking into account whether it is a method within a class or a top-level function. The `current_caller_name` attribute is updated to this identifier before the function's body is traversed, and then restored to its original value upon exiting the function, ensuring the correct calling context for nested calls.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
        *   **Usage:** This method calls self.generic_visit(node) to continue the AST traversal.; This method is called by the ast.NodeVisitor's dispatch mechanism when a FunctionDef node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method processes AST nodes representing function or method calls. It attempts to resolve the fully qualified name of the called entity using the private helper method `_resolve_call_qname`. If the callee is successfully resolved and found within the `definitions`, it records the call, including details such as the caller's file, line number, full identifier, and type (e.g., module, method). This information is then appended to the `self.calls` dictionary, indexed by the callee's pathname.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
        *   **Usage:** This method calls self._resolve_call_qname(node.func) and self.generic_visit(node).; This method is called by the ast.NodeVisitor's dispatch mechanism when a Call node is encountered.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method handles `import` statements in the AST. For each alias specified in the import, it stores a mapping from the alias name (or the original name if no alias is used) to the imported module's original name within the `self.scope` dictionary. This mapping is essential for accurately resolving fully qualified names of imported modules later in the analysis. After processing all aliases, it proceeds with the generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   **Usage:** This method calls self.generic_visit(node) to continue the AST traversal.; This method is called by the ast.NodeVisitor's dispatch mechanism when an Import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method processes `from ... import ...` statements in the AST. It constructs the full module path, correctly handling relative imports based on `node.level`. For each name imported, it stores a mapping from its alias (or original name) to its fully qualified path (e.g., `full_module_path.alias.name`) in `self.scope`. This mechanism ensures that imported entities can be accurately resolved to their complete identifiers during the call analysis.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing an 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method calls self.generic_visit(node) to continue the AST traversal.; This method is called by the ast.NodeVisitor's dispatch mechanism when an ImportFrom node is encountered.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node: ast.Assign)`
        *   *Description:* This method processes assignment statements in the AST, specifically looking for instances where a variable is assigned the result of a class constructor call (e.g., `instance = MyClass()`). If such an assignment is identified, and the class name can be resolved through `self.scope` and exists in `self.definitions`, it records the fully qualified type of the instantiated object in `self.instance_types`. This mapping is crucial for resolving method calls on these instances later in the analysis.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
        *   **Usage:** This method calls self.generic_visit(node) to continue the AST traversal.; This method is called by the ast.NodeVisitor's dispatch mechanism when an Assign node is encountered.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node: ast.expr)`
        *   *Description:* This private helper method is responsible for determining the fully qualified name (QName) of a function or method being called, given its AST node. It handles direct name calls (e.g., `func()`) by checking `self.scope` and local pathnames, and attribute access calls (e.g., `obj.method()`) by attempting to resolve the type of the instance variable via `self.instance_types` or the module via `self.scope`. If a QName cannot be resolved, the method returns `None`.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called, which can be an ast.Name or ast.Attribute.
        *   *Returns:*
            - **name** (`str | None`): The fully qualified name of the called entity if successfully resolved, otherwise None.
        *   **Usage:** This method does not explicitly call other methods but accesses self.scope, self.definitions, and self.instance_types.; This method is called by self.visit_Call to resolve the qualified name of a called function or method.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into its corresponding Python module path string. It first attempts to determine the path relative to a specified project root. If that fails, it uses the base name of the file. It then removes the '.py' extension if present, replaces directory separators with dots, and finally handles `__init__.py` files by stripping the '.__init__' suffix to yield the correct module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The Python module path string derived from the input filepath.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

### File: `backend/scads_key_test.py`
*Analysis data not available for this component.*

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function, `encrypt_text`, is responsible for encrypting a given string using a `cipher_suite` object. It first performs a conditional check: if the input `text` is empty or if the `cipher_suite` is not initialized, it bypasses encryption and returns the original text directly. Otherwise, it prepares the text by stripping leading/trailing whitespace, encodes it into bytes, encrypts these bytes using the `cipher_suite`, and then decodes the resulting encrypted bytes back into a string. The function ensures that only valid text is processed for encryption when the necessary encryption suite is available.
*   **Parameters:**
    - **text** (`str`): The string to be encrypted. If this string is empty or if the `cipher_suite` is not available, the original text will be returned unencrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input string, or the original string if encryption was skipped due to empty input or an unavailable cipher suite.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given string using an external `cipher_suite` object. It first checks if the input `text` is empty or if `cipher_suite` is not initialized, returning the original text in such scenarios. If decryption proceeds, the text is stripped, encoded to bytes, decrypted, and then decoded back into a string. The function includes error handling, returning the original text if any exception occurs during the decryption process.
*   **Parameters:**
    - **text** (`str`): The string value that needs to be decrypted.
*   **Returns:**
    - **decrypted_or_original_text** (`str`): Returns the successfully decrypted string. If the input text is empty, `cipher_suite` is not configured, or an error occurs during decryption, the original input string is returned instead.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function creates a new user record and inserts it into a database. It constructs a user dictionary using the provided username as the document ID, the user's name, and a hashed version of their password. It also initializes fields for Gemini, Ollama, and GPT API keys as empty strings. The function then uses `dbusers.insert_one` to store this user record and returns the unique ID of the newly inserted document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which will also serve as the document's primary key.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before being stored in the database.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier of the user document that was inserted into the database.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is designed to retrieve all user records from a database collection named 'dbusers'. It executes a find operation on the 'dbusers' collection and converts the resulting cursor or iterable into a Python list, effectively returning all stored user data. The function does not take any input parameters.
*   **Parameters:**
*   **Returns:**
    - **users** (`list`): A list containing all user documents or records retrieved from the 'dbusers' collection.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The `fetch_user` function is designed to retrieve a single user document from a database collection. It accepts a username as an argument and performs a lookup using the `_id` field. The function then returns the document corresponding to the specified username, or `None` if no matching user is found.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be fetched from the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user's document if found, otherwise None.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is called by no other functions.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the 'name' field for a specific user in the 'dbusers' collection. It identifies the user by their '_id', which is provided as the 'username' parameter. The function sets the 'name' field to the 'new_name' value. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (_id) of the user whose name is to be updated.
    - **new_name** (`str`): The new name to be set for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in a database. It takes a username and the new Gemini API key as input. The API key is first stripped of whitespace and then encrypted before being stored. The function interacts with a database collection, likely `dbusers`, to update the specified user's record. It returns an integer indicating the number of documents that were modified.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be encrypted and stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database by the update operation.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** This function updates a user's GPT API key in the database. It takes a username and a new GPT API key as input. The provided API key is first stripped of whitespace and then encrypted. Finally, the function updates the 'dbusers' collection, setting the 'gpt_api_key' field for the specified user with the encrypted key. It returns the count of modified documents.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be stored for the user, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specific user in a database. It takes a username and a new Ollama base URL as input. The provided URL is stripped of any leading or trailing whitespace before being stored. The function then performs an update operation on the database, targeting the user identified by the username. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The username identifying the user whose Ollama base URL is to be updated.
    - **ollama_base_url** (`str`): The new Ollama base URL to set for the user. Leading and trailing whitespace will be removed before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function updates a user's Open Source API key in the database. It takes a username and the raw API key as input. The API key is first stripped of whitespace and then encrypted. Finally, the encrypted key is stored in the `opensrc_api_key` field for the specified user in the `dbusers` collection. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API key is to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be encrypted and stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** This function updates the 'opensrc_base_url' field for a specific user in the 'dbusers' collection. It takes the username and the new open-source base URL as input. The provided URL is stripped of any leading or trailing whitespace before being stored. The function then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose open-source base URL is to be updated.
    - **opensrc_base_url** (`str`): The new open-source base URL to be set for the user. Leading and trailing whitespace will be removed.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation (typically 0 or 1).
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** This function retrieves the Gemini API key for a specified user from a database. It queries the 'dbusers' collection, searching for a document where the '_id' matches the provided username. If a user document is found, it extracts and returns the 'gemini_api_key' field. If no user is found or the 'gemini_api_key' is not present, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key as a string if found, otherwise None if the user does not exist or the key is not present.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL associated with a specific user from a database. It queries the `dbusers` collection using the provided username as the `_id`. The query projects only the `ollama_base_url` field. If a user document is found, the function returns the value of the `ollama_base_url` field; otherwise, it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL associated with the user, or None if the user is not found or the URL is not set.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** This function is designed to retrieve a user's GPT API key from a database. It takes a username as input and queries a 'dbusers' collection to find the corresponding user document. If a user is found, the function extracts the 'gpt_api_key' field from that document. It returns the API key if present, otherwise it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the specified username, or None if the user is not found or has no key.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** The `fetch_opensrc_key` function is designed to retrieve a specific user's Open Source API key from a database. It takes a username as input and queries the `dbusers` collection to locate a matching user document. If a user is found, the function extracts the 'opensrc_api_key' field from that document. It returns this key if present, or `None` if the user is not found or the key does not exist.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose Open Source API key is to be fetched.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key as a string if found, otherwise None.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not called by any other functions.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** This function is designed to retrieve the 'opensrc_base_url' for a specified user from a database. It queries the 'dbusers' collection, searching for a document where the '_id' matches the provided username. The query is optimized to return only the 'opensrc_base_url' field. If a matching user document is found, the function extracts and returns the value associated with 'opensrc_base_url'. If no user is found, or if the 'opensrc_base_url' field is not present, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier string for the user whose Open Source base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The Open Source base URL associated with the user, or None if the user is not found or the URL is not set.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is responsible for deleting a specific user record from the database. It takes a username as input and uses it to identify the document to be removed from the `dbusers` collection. The function executes a `delete_one` operation based on the provided username acting as the document's `_id`. It then returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): An integer representing the number of documents deleted (typically 0 or 1).
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function, `get_decrypted_api_keys`, retrieves and decrypts various API keys and base URLs associated with a specific user from a database. It queries the `dbusers` collection using the provided `username`. If the user is not found, the function immediately returns a tuple of two `None` values. Otherwise, it fetches and decrypts the Gemini, GPT, and Open Source API keys, and retrieves the Ollama and Open Source base URLs. The function then returns these five processed values as a tuple.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str`): The decrypted Gemini API key. If the user is not found, the function returns None for this value.
    - **ollama_plain** (`str`): The Ollama base URL. If the user is not found, the function returns None for this value.
    - **gpt_plain** (`str`): The decrypted GPT API key. This value is only returned if the user is found in the database.
    - **opensrc_plain** (`str`): The decrypted Open Source API key. This value is only returned if the user is found in the database.
    - **opensrc_url** (`str`): The Open Source base URL. This value is only returned if the user is found in the database.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is called by no other functions.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** This function is responsible for creating a new chat entry in a database. It constructs a dictionary containing a unique UUID for the chat ID, the provided username, the chat name, and the current timestamp. This chat dictionary is then inserted into the 'dbchats' collection. The function concludes by returning the unique identifier of the newly created chat entry.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (UUID) of the newly created chat entry.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** This function is designed to retrieve all chat documents associated with a specific user from a database. It queries a collection named `dbchats` using the provided username. The results are then sorted by their `created_at` timestamp in ascending order before being returned as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat documents.
*   **Returns:**
    - **chats** (`list`): A list of chat documents belonging to the specified user, sorted by their creation date.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks for the existence of a specific chat associated with a given user within the `dbchats` collection. It queries the database using both the provided `username` and `chat_name` as search criteria. The function leverages `dbchats.find_one` to attempt to locate a matching document. It then returns a boolean value indicating whether a chat document satisfying the criteria was found.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked for existence.
*   **Returns:**
    - **chat_exists** (`bool`): True if a chat matching the username and chat name exists in the database, False otherwise.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and all its associated exchanges within a database. It first updates the main chat entry in the 'dbchats' collection, changing its 'chat_name' from the 'old_name' to the 'new_name' for a specific 'username'. Subsequently, it updates all related message entries (exchanges) in the 'dbexchanges' collection, ensuring their 'chat_name' also reflects the 'new_name' for the same 'username'. The function returns the count of documents modified during the initial chat entry renaming operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat that needs to be changed.
    - **new_name** (`str`): The new desired name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat documents that were modified in the 'dbchats' collection.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is called by no other functions.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str, json_tokens: int, toon_tokens: int, savings_percent: float)`
*   **Description:** This function is responsible for creating and storing a new exchange record in a database. It generates a unique identifier using UUID, compiles various details such as the question, answer, feedback, user information, chat name, and optional performance metrics into a dictionary. It also adds a creation timestamp. The function then attempts to insert this record into the 'dbexchanges' collection. If the insertion is successful, it returns the newly generated ID; otherwise, it catches any exceptions, prints an error message, and returns None.
*   **Parameters:**
    - **question** (`str`): The user's question or prompt in the exchange.
    - **answer** (`str`): The generated answer or response for the question.
    - **feedback** (`str`): The feedback provided for the exchange, typically a rating or category.
    - **username** (`str`): The username associated with the exchange record.
    - **chat_name** (`str`): The name of the chat session to which this exchange belongs.
    - **helper_used** (`str`): An optional string indicating the helper model or component used. Defaults to an empty string.
    - **main_used** (`str`): An optional string indicating the main model or component used. Defaults to an empty string.
    - **total_time** (`str`): An optional string representing the total time taken for the exchange process. Defaults to an empty string.
    - **helper_time** (`str`): An optional string representing the time taken specifically by the helper model. Defaults to an empty string.
    - **main_time** (`str`): An optional string representing the time taken specifically by the main model. Defaults to an empty string.
    - **json_tokens** (`int`): An optional integer representing the number of JSON tokens used in the exchange. Defaults to 0.
    - **toon_tokens** (`int`): An optional integer representing the number of 'toon' tokens used in the exchange. Defaults to 0.
    - **savings_percent** (`float`): An optional float representing the percentage of savings achieved for this exchange. Defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier (UUID) of the newly inserted exchange record, if the database insertion is successful.
    - **None** (`NoneType`): Indicates that the database insertion failed due to an exception.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function, `fetch_exchanges_by_user`, is designed to retrieve exchange records from a database based on a provided username. It queries a collection, likely a MongoDB collection named `dbexchanges`, for all documents where the 'username' field matches the input. The results are then sorted by the 'created_at' field in ascending order to ensure a consistent display sequence. Finally, the function returns these sorted exchange records as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the associated exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (documents) found for the specified username, sorted by their 'created_at' timestamp in ascending order.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function, `fetch_exchanges_by_chat`, is responsible for retrieving a list of exchange records from a database. It queries the `dbexchanges` collection, filtering documents based on a given username and chat name. The results are then sorted chronologically by their creation timestamp in ascending order. Finally, the function returns the retrieved documents as a list.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchange records.
    - **chat_name** (`str`): The name of the chat used to filter the exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents that match the specified username and chat name, sorted by their 'created_at' field.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function is designed to update the feedback for a specific exchange record within a database. It takes an exchange_id and an integer feedback value as input. The function uses a database object, assumed to be `dbexchanges`, to call its `update_one` method. This method locates the document matching the provided `exchange_id` and then sets its `feedback` field to the new integer value. Finally, it returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated. Its specific type is not explicitly hinted but is used as a query key.
    - **feedback** (`int`): The integer value representing the feedback to be set for the exchange record.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates a specific exchange document in the database by its unique identifier. It sets or modifies the 'feedback_message' field of the document to the provided string value. The function then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    - **feedback_message** (`str`): The new feedback message string to assign to the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is designed to remove a specific exchange record from a database collection. It takes a unique exchange identifier as input and uses it to locate and delete the corresponding document. The function then reports the number of documents that were successfully deleted, typically returning 0 or 1.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier (ID) of the exchange record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted from the collection. This will typically be 1 if a document matching the ID was found and deleted, or 0 if no matching document was found.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is called by no other functions.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is responsible for deleting a specific chat and all its associated message exchanges. It ensures data consistency between the frontend and backend by first removing all messages linked to the given chat and then deleting the chat entry itself. The function returns an integer indicating the number of chat documents that were deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted (typically 0 or 1 for delete_one operations).
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list: list)`
*   **Description:** This function processes a list of strings, assumed to be model paths or identifiers. For each string in the input list, it splits the string by the '/' character and extracts the last segment. The primary purpose is to 'clean' or simplify model names by removing any preceding path information, returning a new list of these simplified names.
*   **Parameters:**
    - **model_list** (`list`): A list of strings, where each string is expected to represent a path-like model name (e.g., 'path/to/model_name').
*   **Returns:**
    - **cleaned_model_names** (`list[str]`): A new list containing the cleaned model names. Each name is the last component of the original path-like string after splitting by '/'.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list: list, category_name: str)`
*   **Description:** This function filters a given list of models (`source_list`) based on a specified category name. It retrieves keywords associated with the `category_name` from a global `CATEGORY_KEYWORDS` mapping. If the category's keywords include "STANDARD", the function returns only those models that are also present in a `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list` and collects models whose names contain any of the retrieved keywords. If any models match the keywords, the filtered list is returned; otherwise, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The initial list of models to be filtered.
    - **category_name** (`str`): The name of the category used to determine the filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered according to the specified category, or the original list if no filters apply or no matches are found.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function is designed to save a user-provided Gemini API key. It retrieves the potential new key from the Streamlit session state. If a new key is present, it updates the Gemini key associated with the current user in the database. After a successful update, it clears the key from the session state and displays a success toast notification to the user.
*   **Parameters:**
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function is designed to save a user-provided Ollama URL. It retrieves the URL from the Streamlit session state, specifically from the 'in_ollama_url' key. If a new URL is present, it updates the Ollama URL in the database using the current session's username. Finally, it displays a confirmation toast message to the user indicating that the URL has been saved.
*   **Parameters:**
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function is designed to load chat and exchange data from a database into the Streamlit session state for a specific user. It first checks if the data for the given username is already loaded to prevent redundant operations. If not loaded, it initializes the session state, fetches predefined chats, and then loads associated exchanges, organizing them by chat name. It also handles cases where chat names might be missing or new, and ensures a default chat is created if no chats exist for the user. Finally, it sets an active chat in the session state.
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat and exchange data.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: dict, val: Any)`
*   **Description:** This function is responsible for updating the feedback associated with an exchange object. It takes an exchange object, `ex`, and a new feedback value, `val`, as input. The function first updates the 'feedback' key within the `ex` object locally, then persists this change to a database by calling `db.update_exchange_feedback` using the exchange's unique identifier and the new feedback value. Finally, it triggers a re-run of the Streamlit application.
*   **Parameters:**
    - **ex** (`dict`): The exchange object, expected to be a dictionary-like structure containing at least 'feedback' and '_id' keys.
    - **val** (`Any`): The new feedback value to be assigned to the exchange.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: str, ex: dict)`
*   **Description:** This function is responsible for deleting a specific exchange. It first removes the exchange from the database using its unique identifier. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if the exchange is found within that chat's exchanges, it removes it from the session state. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be removed in the session state.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' key for database deletion.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** This function manages the deletion of a specific chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it updates the Streamlit session state by removing the deleted chat and resetting the `active_chat`. If no chats remain after deletion, a new default chat named 'Chat 1' is created, inserted into the database, and set as the active chat. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text: str)`
*   **Description:** This function aims to extract a repository name from an input text string. It first attempts to find a URL within the provided text using a regular expression. If a URL is identified, it is then parsed to isolate its path component. The last segment of this path is considered the potential repository name, with any trailing ".git" suffix removed. The function returns the cleaned repository name as a string, or None if no URL is found or a repository name cannot be successfully extracted.
*   **Parameters:**
    - **text** (`str`): The input string that may contain a URL from which a repository name should be extracted.
*   **Returns:**
    - **repository_name** (`str | None`): The extracted repository name as a string, or None if no URL is found or a repository name cannot be determined.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text: str)`
*   **Description:** This function acts as a text generator, designed to simulate streaming text output. It takes a single string as input, splits it into individual words, and then yields each word sequentially. A small delay is introduced between yielding each word, making it suitable for applications that require a gradual display of text, such as user interfaces or chat simulations.
*   **Parameters:**
    - **text** (`str`): The input string that will be split into words and streamed.
*   **Returns:**
    - **word** (`str`): A generator that yields individual words from the input text, each followed by a space, with a 0.01-second delay between yields.
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by any other functions in the provided context.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str, should_stream: bool)`
*   **Description:** This function processes a given markdown string, identifying and rendering both standard markdown content and embedded Mermaid diagrams. It splits the input text based on ````mermaid` delimiters. Standard markdown sections are rendered using `st.markdown` or streamed via `st.write_stream` if `should_stream` is true. Mermaid diagram blocks are attempted to be rendered using `st_mermaid`, with a fallback to `st.code` if rendering fails. The function handles cases where the input markdown text is empty.
*   **Parameters:**
    - **markdown_text** (`str`): The input string containing markdown content, potentially with embedded Mermaid diagrams.
    - **should_stream** (`bool`): A flag indicating whether standard markdown content should be streamed (True) or rendered directly (False). Defaults to False.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not called by any other functions.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** This function `render_exchange` is designed to render a single chat exchange, comprising a user's question and an assistant's answer, within a Streamlit application. It displays the user's message and then presents the assistant's response, which includes logic to identify and display errors. The function also generates an interactive toolbar featuring feedback buttons (like/dislike), a popover for adding comments, a download button for the answer, and a delete button for the entire exchange. It dynamically updates the UI based on existing feedback and handles user interactions to modify feedback or delete messages.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing a single chat exchange. It is expected to contain keys such as 'question' (str), 'answer' (str), 'feedback' (int, 0 or 1), 'feedback_message' (str), and '_id' (str) for unique identification. This object holds all data pertinent to a specific user-assistant interaction.
    - **current_chat_name** (`str`): A string representing the identifier or name of the currently active chat session. This parameter is utilized in operations that require context about the chat, such as when deleting an exchange.
*   **Returns:**
*   **Usage:** Calls: This function calls no other functions.; Called by: This function is not explicitly called by other functions in the provided context.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to provide a structured representation for a single parameter of a function. It defines a clear schema for capturing essential metadata, including the parameter's name, its data type, and a descriptive explanation of its role. This class facilitates consistent data handling and validation for function parameter specifications.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly generates an __init__ method. This constructor is responsible for initializing an instance of ParameterDescription by validating and assigning the 'name', 'type', and 'description' attributes based on the provided arguments.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type hint or inferred type of the parameter.
        - **description** (`str`): A brief explanation of the parameter's purpose.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to structure and validate information about the return value of a function. It serves as a data model to encapsulate the name, data type, and a descriptive explanation of a function's output. This class ensures that return value descriptions adhere to a consistent format, facilitating structured documentation and analysis within a larger system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance of `ReturnDescription` by validating and assigning the provided `name`, `type`, and `description` attributes according to their specified types.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value, if it has one (e.g., for a named tuple field).
        - **type** (`str`): The Python type hint or a string representation of the return value's data type.
        - **description** (`str`): A detailed explanation of what the return value represents or its purpose.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function interacts within a system. It serves as a structured data container, specifically holding details about the functions or methods that a particular function calls and the functions or methods that call it. This class provides a clear and type-hinted way to represent the contextual usage of a function.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The `UsageContext` class, being a Pydantic BaseModel, implicitly defines its constructor based on its field annotations. It initializes instances by accepting `calls` and `called_by` as string arguments, ensuring type validation upon instantiation.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions, methods, or classes that this function calls.
        - **called_by** (`str`): A string describing the functions or methods that call this function.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** This class serves as a structured data model for representing a comprehensive analysis of a Python function. It encapsulates key aspects such as the function's overall purpose, its input parameters, its return values, and its operational context within a larger system. As a Pydantic BaseModel, it is designed to facilitate machine-readable descriptions of functions, ensuring data validation and clear structure.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, meaning its constructor is automatically generated. It initializes instances by accepting values for its defined fields: 'overall', 'parameters', 'returns', and 'usage_context', ensuring they conform to their specified types.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the function's purpose and implementation.
        - **parameters** (`List[ParameterDescription]`): A list of objects describing each parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of objects describing the return values of the function.
        - **usage_context** (`UsageContext`): An object describing where the function is called and what it calls.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to represent a structured analysis of a Python function. It serves as the top-level schema for capturing key information about a function, including its unique identifier, a detailed description of its purpose and signature, and any errors encountered during its analysis. This model ensures a consistent and machine-readable format for function analysis results within a larger system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. It inherits from pydantic.BaseModel, which automatically generates a constructor based on the defined fields: identifier, description, and error. Instances are created by passing keyword arguments corresponding to these fields.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the function being analyzed.
        - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose and signature.
        - **error** (`Optional[str]`): An optional string describing any error encountered during the function analysis.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to provide a structured representation of a class's `__init__` method. It encapsulates a textual description of the constructor's purpose and a list of ParameterDescription objects, detailing each parameter accepted by the `__init__` method. This class serves as a data schema for documenting how other classes are initialized.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates its `__init__` method. This constructor accepts keyword arguments corresponding to its defined fields: `description` and `parameters`. It validates the input data against the specified types, ensuring that a string is provided for the description and a list of ParameterDescription objects for the parameters.
    *   *Parameters:*
        - **description** (`str`): A string detailing the overall purpose and behavior of the `__init__` method.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each describing a single parameter of the `__init__` method, including its name, type, and individual description.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate contextual information about another class. It provides a structured format to store details regarding the external dependencies that a class relies upon and the specific locations or modules where that class is instantiated. This model serves as a metadata container, facilitating a clear understanding of a class's integration and functional relationships within a larger system.
*   **Instantiation:** No specific instantiation points were provided in the input context for this class.
*   **Dependencies:** No specific external dependencies were provided in the input context for this class.
*   **Constructor:**
    *   *Description:* The `__init__` method for ClassContext is implicitly generated by Pydantic's BaseModel. It initializes an instance of ClassContext by accepting values for `dependencies` and `instantiated_by`. These values are then validated and assigned as attributes to the new object, ensuring that the class context is properly structured upon creation.
    *   *Parameters:*
        - **dependencies** (`str`): A string representing the external dependencies of the class being described.
        - **instantiated_by** (`str`): A string indicating where the class being described is instantiated.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The `ClassDescription` class serves as a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python class. It structures information about a class's high-level purpose, its constructor's behavior, a detailed breakdown of all its methods, and its external usage context. This model is crucial for generating structured documentation or for further automated processing of class analyses.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context, relying on its Pydantic BaseModel inheritance and type hints for structure.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly defines its constructor based on its field annotations. It initializes instances by accepting values for `overall`, `init_method`, `methods`, and `usage_context`, ensuring type validation and data integrity upon instantiation.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary string describing the class's main purpose and functionality.
        - **init_method** (`ConstructorDescription`): An object containing a detailed description of the class's constructor (__init__ method).
        - **methods** (`List[FunctionAnalysis]`): A list of `FunctionAnalysis` objects, each providing a detailed analysis of a method within the class.
        - **usage_context** (`ClassContext`): An object describing the class's external dependencies and where it is instantiated.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as a Pydantic model designed to structure the output of a comprehensive class analysis. It encapsulates essential information about a Python class, including its unique identifier, a detailed ClassDescription object, and an optional field for any errors encountered during the analysis. This model ensures a standardized and machine-readable format for representing analyzed class data.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, inheriting from Pydantic's BaseModel, does not explicitly define an __init__ method. Pydantic automatically generates a constructor based on the defined fields: identifier, description, and error. Instances are initialized by providing values for these fields, with error being optional.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
        - **error** (`Optional[str]`): An optional string containing an error message if the class analysis failed.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event within a system, typically used by a relationship analyzer. It acts as a structured data container for tracking where functions or methods are called or classes are instantiated, providing details such as the file, function name, call mode, and line number.
*   **Instantiation:** This class is not explicitly instantiated by any known entities within the provided context.
*   **Dependencies:** This class does not explicitly depend on any external modules or classes beyond its base Pydantic BaseModel.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the CallInfo class's constructor is automatically generated. It initializes an instance of CallInfo by validating and assigning values to its defined fields: file, function, mode, and line. This allows for robust data integrity when creating new call event records.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that made the call.
        - **mode** (`str`): The type of the calling entity, e.g., 'method', 'function', 'module'.
        - **line** (`int`): The line number in the file where the call event occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information required for analyzing a function. It defines a schema for tracking both the outbound calls made by a function and the inbound calls that invoke it. This class facilitates the standardized representation and validation of function interaction data within a larger system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes instances of `FunctionContextInput` by accepting values for `calls` and `called_by`, which are then validated against their specified types.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings representing other methods, classes, or functions called by the function being analyzed.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where the function being analyzed is called.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to serve as the structured input for generating a FunctionAnalysis object. It defines the schema for data required to analyze a Python function, including its source code, identifier, and contextual information. This class ensures that all necessary components for a function analysis are present and correctly typed before processing.
*   **Instantiation:** The specific points where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any direct external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is implicitly generated to accept and validate the defined fields: mode, identifier, source_code, imports, and context.
    *   *Parameters:*
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to encapsulate structured contextual information for a method. It serves as a data transfer object, defining the expected fields for a method's identifier, its outgoing calls, its incoming calls, its arguments, and its docstring. This model is crucial for providing a standardized format for method analysis within a larger system.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `MethodContextInput` is implicitly generated. It allows for the instantiation of a `MethodContextInput` object by accepting keyword arguments corresponding to its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`. These arguments are used to initialize the instance's attributes, ensuring type validation and data integrity.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method.
        - **calls** (`List[str]`): A list of strings representing other methods, classes, or functions called by this method.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where this method is called from. The `CallInfo` type is not defined in this snippet but is expected to be another structured type.
        - **args** (`List[str]`): A list of strings representing the arguments of the method.
        - **docstring** (`Optional[str]`): An optional string containing the method's docstring.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to provide a structured schema for collecting and organizing contextual information related to a Python class. It serves as a data container, defining the expected format for dependencies, instantiation points, and method-specific contexts, which are crucial for comprehensive class analysis.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The class is initialized via Pydantic's BaseModel constructor, which automatically handles the assignment of its defined fields: 'dependencies', 'instantiated_by', and 'method_context'. These fields are populated directly from the arguments passed during object creation.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies of the class.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects providing context for each method within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a data transfer object, ensuring that all necessary information for class analysis, such as the analysis mode, class identifier, source code, import statements, and contextual data, is provided in a validated format. This class facilitates the standardized input for an AI system performing code analysis.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. It inherits from pydantic.BaseModel, and its initialization is handled implicitly by Pydantic, which constructs instances based on the provided field values and their type annotations.
    *   *Parameters:*
*   **Methods:**

---
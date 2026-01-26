# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** This project is an automated documentation pipeline designed to analyze Python-based Git repositories. It clones a given repository, performs a static analysis of the source code to build an Abstract Syntax Tree (AST) and understand code relationships, and then leverages Large Language Models (LLMs) to generate detailed, human-readable documentation for all classes, methods, and functions. The final output is a comprehensive Markdown report, accessible through a Streamlit web interface.
- **Key Features:**
  - **Git Repository Analysis:** Clones public Git repositories for local analysis.
  - **AST-Based Code Parsing:** Builds a detailed Abstract Syntax Tree (AST) to understand the static structure and relationships within the code.
  - **LLM-Powered Documentation:** Utilizes Helper LLMs to analyze and describe individual code components (functions, classes) and a Main LLM to synthesize the final report.
  - **Efficient Data Handling:** Converts the detailed analysis into the TOON format for efficient data transfer to the final synthesis LLM.
  - **Web Interface:** Provides a user-friendly frontend built with Streamlit for initiating analysis and viewing results.
- **Tech Stack:** Streamlit, LangChain, GitPython, Pydantic, NetworkX, TOON Format.

*   **Repository Structure:**
    ```mermaid
    graph LR
        subgraph root
            A["/.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>test.json"]
        end
        subgraph SystemPrompts
            B["/SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt"]
        end
        subgraph backend
            C["/AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py"]
        end
        subgraph database
            D["/db.py"]
        end
        subgraph frontend
            E["/__init__.py<br/>frontend.py"]
            E_sub1[".streamlit/config.toml"]
            E_sub2["gifs/4j.gif"]
            E --> E_sub1
            E --> E_sub2
        end
        subgraph schemas
            F["/types.py"]
        end
        root --> SystemPrompts
        root --> backend
        root --> database
        root --> frontend
        root --> schemas
    ```

## 2. Installation
### Dependencies
To install the required dependencies, run the following command in your terminal:
`pip install -r requirements.txt`

A full list of dependencies includes:
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
```
### Setup Guide
1.  Clone the repository to your local machine.
2.  Create a virtual environment: `python -m venv venv`.
3.  Activate the virtual environment.
4.  Install the dependencies using the command: `pip install -r requirements.txt`.
5.  Create a `.env` file by copying the `.env.example` file.
6.  Populate the `.env` file with the necessary API keys and configuration values.
### Quick Startup
To run the web application, execute the following command from the root directory:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The primary use case for this application is to automatically generate technical documentation for a Python Git repository.

-   **Primary Use Case:** A user navigates to the Streamlit web application, enters the URL of a public GitHub repository, selects the desired LLM models for analysis, and initiates the process. The application then performs the full analysis pipeline and displays the final, detailed Markdown report in the user interface.
-   **Jupyter Notebook Analysis:** A separate workflow is available to specifically analyze Jupyter Notebooks (`.ipynb`) within a repository, converting them to an intermediate XML format and using a multimodal LLM to interpret both code and outputs.

**Primary Command:**
The application is launched via the Streamlit CLI.
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
*   **Description:** This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to a specified project root. If the file is a Python file, it removes the '.py' extension. Subsequently, it replaces path separators with dots to form the module path. Special handling is included for '__init__.py' files, where the '.__init__' suffix is removed to represent the package itself.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) of Python source code. Its primary purpose is to extract and structure metadata about imports, classes, and functions found within a given source file. It builds a schema containing lists of imports, functions, and classes, providing a programmatic representation of the code's structure.
*   **Instantiation:** This class is not explicitly instantiated by any known components within the provided context.
*   **Dependencies:** This class depends on `backend.AST_Schema.path_to_module` for resolving module paths.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor with the source code, file path, and project root. It calculates the module path, sets up an empty schema dictionary to store extracted information, and initializes `_current_class` to `None` for tracking the current class context during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the Python file being visited.
        - **project_root** (`str`): The root directory of the project, used to determine the module path.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes `ast.Import` nodes, which represent `import module` statements. It iterates through each alias in the import statement, extracting the module name and appending it to the `self.schema["imports"]` list. After recording the import, it calls `self.generic_visit(node)` to ensure that the AST traversal continues for any child nodes.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.Import` node is encountered. It calls `self.generic_visit` to continue AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to `from module import name` statements. It constructs fully qualified import names by combining the module name (if present) with each alias name, then appends these to `self.schema["imports"]`. This ensures that specific imports from modules are correctly captured. Finally, it invokes `self.generic_visit(node)` to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ImportFrom` node is encountered. It calls `self.generic_visit` to continue AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is responsible for processing `ast.ClassDef` nodes, which represent class definitions. It constructs a dictionary containing detailed information about the class, including its identifier, name, docstring, source code segment, and line numbers. This class information is then added to `self.schema["classes"]`, and the `_current_class` attribute is temporarily set to this class's info to provide context for any nested methods. After visiting child nodes via `self.generic_visit(node)`, `_current_class` is reset to `None`.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ClassDef` node is encountered. It calls `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit`.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, distinguishing between methods defined within a class and top-level functions. If `_current_class` is set, it means the function is a method, and its details (identifier, name, arguments, docstring, line numbers) are appended to the `method_context` of the current class. Otherwise, it's treated as a standalone function, and its details are added to `self.schema["functions"]`. It ensures proper AST traversal by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.FunctionDef` node is encountered, and also by `visit_AsyncFunctionDef`. It calls `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method handles `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Instead of implementing its own parsing logic, it delegates the processing directly to the `visit_FunctionDef` method. This approach ensures that both synchronous and asynchronous function definitions are handled uniformly, extracting the same structural and metadata information.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.AsyncFunctionDef` node is encountered. It calls `self.visit_FunctionDef`.

---
#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process source code, particularly Python files within a Git repository, to build a structured Abstract Syntax Tree (AST) schema. It can analyze individual files to extract functions, classes, and their internal structures using an ASTVisitor. Additionally, it provides functionality to merge external relationship data, such as call graphs, into the generated AST schema, enriching the structural information with dynamic interaction details.
*   **Instantiation:** This class is not explicitly instantiated by any known components in the provided context.
*   **Dependencies:** This class depends on 'backend.AST_Schema.ASTVisitor' for parsing ASTs, 'ast' for Python's built-in AST module, and 'os' for path manipulation.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments, effectively creating a stateless instance.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, raw_relationships)`
        *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing calls, into a structured full schema. It iterates through files, functions, and classes within the schema, updating their respective context fields with call and called-by information. For classes, it also calculates and stores external dependencies based on method calls.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): The comprehensive schema containing file, function, and class AST nodes.
            - **raw_relationships** (`dict`): A dictionary containing raw 'outgoing' and 'incoming' call relationships.
        *   *Returns:*
            - **full_schema** (`dict`): The updated 'full_schema' dictionary with integrated relationship data.
        *   **Usage:** This method is not explicitly called by any other functions or methods in the provided context. It primarily uses dictionary 'get' methods and iterates over data structures. It does not call other distinct functions or classes.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files, repo)`
        *   *Description:* This method processes a list of file objects from a Git repository to construct a full AST schema. It filters for Python files, reads their content, and uses an ASTVisitor to parse the Abstract Syntax Tree, extracting structural information. The method handles potential parsing errors and populates a 'full_schema' dictionary with the AST nodes for each successfully processed file.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though it's not directly used in the provided snippet beyond its type hint.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed repository, structured by file paths.
        *   **Usage:** This method is not explicitly called by any other functions or methods in the provided context. It calls 'os.path.commonpath', 'os.path.isfile', 'os.path.dirname', 'ast.parse', and instantiates 'ASTVisitor'.

---
### File: `backend/File_Dependency.py`
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and uses a custom `FileDependencyGraph` visitor to traverse the AST and identify import relationships. The visitor populates an internal dictionary of import dependencies. The function then iterates through these identified dependencies, adding nodes for both importing and imported files, and creating directed edges from the importer to the imported files. The resulting graph illustrates which files depend on others based on their import statements.
*   **Parameters:**
    - **filename** (`str`): The path to the file being analyzed for dependencies.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`networkx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies (from importer to imported).
*   **Usage:**
    - **Calls:** backend.File_Dependency.FileDependencyGraph
    - **Called By:** This function is called by no other functions.

---
#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses its content to build a file-specific dependency graph using an external helper function. Finally, it aggregates all these individual file graphs into a single global directed graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to build the dependency graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependencies between Python files across the entire repository.
*   **Usage:**
    - **Calls:** backend.File_Dependency.build_file_dependency_graph
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and returns a list of `Path` objects. The function first converts the input directory string into an absolute and canonical `Path` object. It then recursively searches for all files ending with ".py" within this root path. Finally, it returns these found file paths as a list, with each path made relative to the initial root directory.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory to search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each path represents a Python file found within the specified directory, relative to the root directory.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

---
#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends ast.NodeVisitor to traverse the Abstract Syntax Tree (AST) of a Python file and identify its import dependencies. It is designed to build a dictionary (import_dependencies) mapping the analyzed file to a set of modules it imports. The class handles both absolute and relative import statements, with a dedicated private method _resolve_module_name for robustly resolving relative imports within a given repository context. Its primary purpose is to establish a foundational understanding of file-level import relationships for a larger dependency analysis system.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components within the provided context.
*   **Dependencies:** This class depends on get_all_temp_files for repository file discovery, and init_exports_symbol and module_file_exists for resolving module and symbol existence during relative import processing.
*   **Constructor:**
    *   *Description:* The constructor initializes the FileDependencyGraph instance by storing the filename of the file being analyzed and the repo_root directory. These attributes are crucial for resolving relative imports and locating files within the repository.
    *   *Parameters:*
        - **filename** (`str`): The name of the file currently being analyzed for dependencies.
        - **repo_root** (`str`): The root directory of the repository, used for resolving file paths.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This private method is responsible for resolving relative import statements (e.g., from .. import name). It calculates the correct base directory based on the import level and the current file's location within the repository. It then iterates through the imported names, checking if they correspond to existing module files or symbols exported by __init__.py files. If no matching modules or symbols are found, it raises an ImportError. Nested functions `module_file_exists` and `init_exports_symbol` are defined within this method to assist in verifying file and symbol existence.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST ImportFrom node representing the relative import statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names as strings.
        *   **Usage:** This method is called by visit_ImportFrom when processing relative import statements. It calls get_all_temp_files to get all files in the repository, Path for path manipulation, iskeyword to check for Python keywords, and internally defines and calls module_file_exists and init_exports_symbol to verify module existence and symbol exports. It also uses literal_eval, parse, and walk from the ast module within init_exports_symbol.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method is part of the NodeVisitor pattern and is called for Import and ImportFrom AST nodes. It records the imported module names as dependencies for the current self.filename in the import_dependencies dictionary. If a base_name is provided (typically from visit_ImportFrom), it uses that; otherwise, it uses the alias name from the import node. After processing, it calls self.generic_visit(node) to continue the AST traversal.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing an import statement.
            - **base_name** (`str | None`): An optional base name for the module, typically used for from ... import ... statements where the module part is resolved separately.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the AST NodeVisitor when encountering Import nodes, and explicitly by visit_ImportFrom to record dependencies. It calls self.generic_visit to continue the AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method is invoked by the AST NodeVisitor when an ImportFrom node is encountered. It extracts the module name from the import statement. If it's an absolute import, it takes the last part of the module name and passes it to visit_Import. If it's a relative import (indicated by node.module being None), it attempts to resolve the module name using the _resolve_module_name helper method. Any resolved base names are then passed to visit_Import to record the dependency. Errors during relative import resolution are caught and printed. Finally, it ensures the AST traversal continues with self.generic_visit.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST ImportFrom node to be processed.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the AST NodeVisitor framework when traversing the AST and encountering an ImportFrom node. It calls self.visit_Import to record the dependency and self._resolve_module_name to handle relative imports. It also calls self.generic_visit to continue the AST traversal.

---
### File: `backend/HelperLLM.py`
#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy data and processing loop, primarily for testing the LLMHelper class. It defines pre-computed analysis inputs and outputs for several example functions, such as 'add_item', 'check_stock', and 'generate_report', using Pydantic models. It then instantiates an LLMHelper and simulates generating documentation for these functions, logging the process and displaying the final aggregated results. The function demonstrates how to use the `FunctionAnalysisInput` and `FunctionAnalysis` models.
*   **Parameters:**
    *This function takes no parameters.*
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** backend.HelperLLM.LLMHelper, schemas.types.ClassAnalysisInput, and schemas.types.ClassContextInput.
    - **Called By:** This function is called by no other functions.

---
#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs) to generate structured documentation for Python functions and classes. It abstracts away the complexities of LLM API integration, including model selection (supporting Gemini, OpenAI, custom APIs, and Ollama), system prompt management, batch processing, and rate limit handling. The class ensures that LLM outputs conform to predefined Pydantic schemas (FunctionAnalysis and ClassAnalysis), making it a robust tool for automated code documentation generation.
*   **Instantiation:** The class is not explicitly instantiated by other components in the provided context.
*   **Dependencies:** The class does not have explicitly listed external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper instance by setting up the API key, loading system prompts for function and class analysis from specified file paths, and configuring the underlying Language Model (LLM) based on the `model_name`. It supports various LLM providers like Google Gemini, OpenAI, custom APIs, and Ollama, and also configures batch processing settings.
    *   *Parameters:*
        - **api_key** (`str`): The API key for authenticating with the chosen LLM service.
        - **function_prompt_path** (`str`): The file path to the system prompt used for function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt used for class analysis.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, particularly for Ollama or custom OpenAI-compatible APIs.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method sets the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It uses a series of conditional statements to assign specific batch sizes for various known LLM models like different Gemini versions, Llama3, and GPT models. For unknown models or custom API models, it defaults to a conservative batch size of 2 or a larger size of 500, respectively, logging a warning if the model is unrecognized.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is not explicitly called by other functions or methods based on the provided context. It does not explicitly call other methods, classes, or functions based on the provided context.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method takes a list of `FunctionAnalysisInput` objects, converts them into JSON payloads, and then uses the configured `function_llm` to generate structured documentation for functions in batches. It iterates through the inputs, sending `BATCH_SIZE` conversations to the LLM concurrently, handles potential API errors by extending the results with `None` for failed items, and incorporates a waiting period between batches to respect rate limits. The method returns a list of `FunctionAnalysis` objects or `None` for failed generations.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary data for analyzing a single function.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, where each object represents the structured documentation for a function, or `None` if the analysis for a specific function failed.
        *   **Usage:** This method is not explicitly called by other functions or methods based on the provided context. It does not explicitly call other methods, classes, or functions based on the provided context.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is designed to generate structured documentation for a batch of classes. It takes a list of `ClassAnalysisInput` objects, serializes them into JSON, and then constructs conversations for the `class_llm`. The method processes these conversations in batches, sending them to the LLM, handling potential exceptions by marking failed items as `None`, and pausing between batches to manage API rate limits. It ultimately returns a list of `ClassAnalysis` objects or `None` for any failed analysis.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary data for analyzing a single class.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, where each object represents the structured documentation for a class, or `None` if the analysis for a specific class failed.
        *   **Usage:** This method is not explicitly called by other functions or methods based on the provided context. It does not explicitly call other methods, classes, or functions based on the provided context.

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class provides a unified interface for interacting with various Large Language Models (LLMs). It dynamically configures the appropriate LLM client (e.g., Gemini, OpenAI-compatible, Ollama) based on the specified model name and manages a system prompt loaded from a file. This class offers methods for both single-response and streaming interactions with the underlying LLM, incorporating robust error handling for API calls.
*   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
*   **Dependencies:** The class depends on logging for output, os (implicitly for environment variables like SCADSLLM_URL, OLLAMA_BASE_URL), langchain_google_genai.ChatGoogleGenerativeAI, langchain_ollama.ChatOllama, langchain_openai.ChatOpenAI, langchain.messages.HumanMessage, and langchain.messages.SystemMessage for its core LLM functionalities.
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by setting up the system prompt from a specified file and configuring the underlying Large Language Model (LLM) client based on the provided model name. It supports various LLM providers and performs validation for the API key and prompt file path, raising errors if essential configurations are missing.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **prompt_file_path** (`str`): The file path to the system prompt that will be used for LLM interactions.
        - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This parameter determines which LLM client (Gemini, OpenAI, Ollama) is initialized.
        - **base_url** (`str | None`): An optional base URL for custom LLM endpoints, primarily used for Ollama or other OpenAI-compatible services if the SCADSLLM_URL environment variable is not set.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method sends a user's input to the configured Large Language Model (LLM) and retrieves a single, complete response. It constructs a message list that includes the system prompt and the user's input, then invokes the LLM to get the generated content. The method includes error handling to log any issues during the LLM call and returns None if an exception occurs.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM for a single, non-streaming response.
        *   *Returns:*
            - **content** (`str | None`): The generated content from the LLM if the call is successful, otherwise None in case of an error.
        *   **Usage:** This method is not explicitly called by other methods in the provided context. It calls SystemMessage, HumanMessage, logging.info, self.llm.invoke, and logging.error.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method interacts with the LLM to obtain a streaming response, yielding chunks of content as they become available. It prepares the messages, including the system prompt and user input, and then iterates through the stream iterator provided by the LLM client, yielding each content chunk. Error handling is implemented to log any issues during the streaming call and yield an error message if an exception occurs.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message for which a streaming response is requested from the LLM.
        *   *Returns:*
            - **chunk.content** (`str`): Yields individual content chunks from the LLM's streaming response.
            - **error_message** (`str`): Yields an error message string if an exception occurs during the streaming call.
        *   **Usage:** This method is not explicitly called by other methods in the provided context. It calls SystemMessage, HumanMessage, logging.info, self.llm.stream, and logging.error.

---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to systematically extract fundamental project details from various common project files, such as README.md, pyproject.toml, and requirements.txt. It orchestrates the parsing of these files, prioritizing certain sources (e.g., TOML over requirements.txt for dependencies), and consolidates the gathered information into a structured dictionary. The class also includes mechanisms for cleaning file content and deriving fallback information, like a project title from a repository URL, ensuring comprehensive data collection.
*   **Instantiation:** This class is not explicitly instantiated by any known components in the provided context.
*   **Dependencies:** This class does not explicitly list external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjektInfoExtractor instance by setting a default 'Information not found' string and establishing the core data structure, `self.info`. This dictionary is pre-populated with nested keys for project overview and installation details, all initially set to the 'Information not found' placeholder, preparing it for subsequent data extraction.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content)`
        *   *Description:* This private helper method is responsible for sanitizing string content by removing null bytes. Null bytes can often appear due to encoding errors, particularly when a file encoded in UTF-16 is mistakenly read as UTF-8. By removing these characters, the method ensures that subsequent parsing operations on the content are not disrupted by malformed data.
        *   *Parameters:*
            - **content** (`str`): The string content that needs to be cleaned of null bytes.
        *   *Returns:*
            - **""** (`str`): The cleaned string with all null bytes removed, or an empty string if the input was empty.
        *   **Usage:** This method is called by _parse_readme, _parse_toml, and _parse_requirements. It does not call any other functions or methods.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private method searches through a list of file objects to find one whose path matches any of the provided patterns. The search is case-insensitive, making it robust against variations in file naming conventions. It iterates through each file and pattern, returning the first file that satisfies a match.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of string patterns to match against file paths (e.g., 'readme.md').
            - **dateien** (`List[Any]`): A list of file objects, where each object is expected to have a 'path' attribute.
        *   *Returns:*
            - **""** (`Optional[Any]`): The first file object found that matches any of the patterns, or None if no match is found.
        *   **Usage:** This method is called by extrahiere_info. It does not call any other functions or methods.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private method extracts text content from a Markdown string that appears directly under an H2 heading (##) matching one of the specified keywords. It constructs a regular expression dynamically to find the heading and then captures all content following it until the next H2 heading or the end of the input string. This is useful for parsing structured sections within README files.
        *   *Parameters:*
            - **inhalt** (`str`): The Markdown content string to be parsed.
            - **keywords** (`List[str]`): A list of keywords to match against the H2 headings (e.g., 'Features', 'Installation').
        *   *Returns:*
            - **""** (`Optional[str]`): The extracted text content under the matched H2 heading, or None if no matching section is found.
        *   **Usage:** This method is called by _parse_readme. It calls re.escape, re.compile, and pattern.search for regular expression operations.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This private method parses the content of a README file to populate various fields within the `self.info` dictionary related to project overview and installation. It first cleans the content using `_clean_content` and then uses regular expressions to extract the project title and a fallback description. For structured sections like 'Key Features', 'Tech Stack', 'Status', 'Installation', and 'Quick Start', it leverages `_extrahiere_sektion_aus_markdown` to find and extract relevant information.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the README file.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by extrahiere_info. It calls _clean_content, re.search, and _extrahiere_sektion_aus_markdown.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This private method is responsible for parsing the content of a `pyproject.toml` file. It cleans the input content and then attempts to load it using the `tomllib` library. If `tomllib` is not available or a `TOMLDecodeError` occurs, it prints a warning. Upon successful parsing, it extracts the project name, description, and dependencies from the 'project' section of the TOML data and updates the `self.info` dictionary accordingly.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the pyproject.toml file.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by extrahiere_info. It calls _clean_content, tomllib.loads, and print.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This private method parses the content of a `requirements.txt` file to extract project dependencies. It first cleans the input content and then processes each line, filtering out comments and empty lines. The extracted dependencies are then stored in the `self.info` dictionary, but only if the 'dependencies' field has not already been populated by a higher-priority source like `pyproject.toml`.
        *   *Parameters:*
            - **inhalt** (`str`): The raw string content of the requirements.txt file.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by extrahiere_info. It calls _clean_content.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This public method orchestrates the entire information extraction process. It identifies relevant project files (README, pyproject.toml, requirements.txt) from a given list of file objects using `_finde_datei`. It then parses these files in a specific order of priority: `pyproject.toml`, then `requirements.txt`, and finally the README file. After parsing, it formats the collected dependencies and, if no project title was found, attempts to derive one from the provided repository URL. The method returns a comprehensive dictionary of all extracted project information.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo_url** (`str`): The URL of the repository, used as a fallback to derive a project title.
        *   *Returns:*
            - **""** (`Dict[str, Any]`): A dictionary containing all extracted project information, including overview and installation details.
        *   **Usage:** This method is not explicitly called by other methods within the provided context, suggesting it is a primary entry point for external usage. It calls _finde_datei, _parse_toml, _parse_requirements, _parse_readme, os.path.basename, and repo_url.removesuffix.

---
### File: `backend/callgraph.py`
#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function takes a NetworkX directed graph and a file path, then generates a DOT file representation of the graph. It first creates a copy of the input graph. It then relabels all nodes in the copied graph with simple, safe identifiers (e.g., "n0", "n1") to ensure compatibility with DOT format. The original node names are preserved by adding them as a 'label' attribute to the newly relabeled nodes before writing the graph to the specified output path.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph to be converted into a DOT file.
    - **out_path** (`str`): The file path where the generated DOT graph will be saved.
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo)`
*   **Description:** This function constructs a filtered call graph for a given Git repository. It begins by iterating through all Python files within the repository, parsing their Abstract Syntax Trees (ASTs) to identify and collect a set of 'own functions' defined within the project. Subsequently, it initializes a `networkx.DiGraph` and re-processes the parsed ASTs. During this second pass, it detects caller-callee relationships and adds an edge to the graph only if both the calling and called functions are part of the previously identified 'own functions' set. The function ultimately returns this directed graph, which represents the internal call structure exclusively among the project's own codebase.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which to extract Python files and build the call graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the filtered call relationships between functions defined within the repository, excluding external calls.
*   **Usage:**
    - **Calls:** backend.callgraph.CallGraph
    - **Called By:** This function is called by no other functions.

---
#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an ast.NodeVisitor designed to construct a call graph for a given Python source file. It traverses the Abstract Syntax Tree (AST) of a file, identifying function and class definitions, import statements, and function calls. It maintains context about the current function and class to accurately resolve call targets, including local definitions and imported modules. The class builds a directed graph (networkx.DiGraph) where nodes represent functions/methods and edges represent calls between them, providing a structured representation of the code's execution flow.
*   **Instantiation:** This class is not explicitly instantiated by any known entities based on the provided context.
*   **Dependencies:** The class relies on the ast module for parsing Python code and the networkx library for graph manipulation.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph instance, setting up the filename, tracking current function and class context during AST traversal, and initializing data structures like local_defs, graph (a NetworkX DiGraph), import_mapping, function_set, and edges to store call graph information.
    *   *Parameters:*
        - **filename** (`str`): The name of the file being analyzed, used for full name resolution.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively extracts the components of a function or method call from an AST node. It handles ast.Call, ast.Name, and ast.Attribute nodes to build a list of name parts, effectively converting an AST representation of a call (e.g., obj.method(), module.function()) into a list of its dotted components (e.g., ['obj', 'method']).
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a call, name, or attribute.
        *   *Returns:*
            - **name** (`list[str]`): A list of string components representing the fully qualified name of the called entity.
        *   **Usage:** This method is called by visit_Call. It does not explicitly call other functions or methods within its own source code.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private method takes a list of potential callee name components (e.g., [['my_func'], ['obj', 'method']]) and attempts to resolve them to their full, unique identifiers within the context of the current file. It prioritizes local definitions, then import mappings, and finally constructs a full name based on the current filename and class context. This ensures that calls are correctly linked to their definitions.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains string components of a potential callee's name.
        *   *Returns:*
            - **name** (`list[str]`): A list of fully resolved string identifiers for the callees.
        *   **Usage:** This method is called by visit_Call. It does not explicitly call other functions or methods within its own source code.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This private helper method constructs a fully qualified name for a function or method. It prepends the filename and optionally the class_name to the given basename, using "::" as a separator. This standardized naming convention helps in uniquely identifying functions and methods across the project.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method (e.g., "my_function").
            - **class_name** (`str | None`): The name of the class if the entity is a method, otherwise None.
        *   *Returns:*
            - **name** (`str`): The fully qualified name (e.g., "filename::ClassName::methodName" or "filename::functionName").
        *   **Usage:** This method is called by visit_FunctionDef. It does not explicitly call other functions or methods within its own source code.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self, )`
        *   *Description:* This private method determines the identifier of the current calling context. If self.current_function is set, it returns that. Otherwise, it returns a placeholder indicating the global scope, using the filename if available, or "<global-scope>" as a fallback. This is crucial for correctly attributing calls in the graph.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **name** (`str`): The identifier of the current function or a global scope placeholder.
        *   **Usage:** This method is called by visit_Call. It does not explicitly call other functions or methods within its own source code.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method, part of the ast.NodeVisitor pattern, is called when an ast.Import node is encountered. It processes top-level import statements (e.g., import module as alias) to populate the self.import_mapping dictionary, which maps aliases or module names to their original module names. After processing, it calls generic_visit to continue traversing the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the ast.NodeVisitor framework when an ast.Import node is visited. It calls self.generic_visit.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method, part of the ast.NodeVisitor pattern, is called when an ast.ImportFrom node is encountered. It processes from ... import ... statements (e.g., from package.module import name as alias) to update self.import_mapping. It maps imported names (or their aliases) to their originating module. This helps in resolving fully qualified names later.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a from ... import ... statement.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the ast.NodeVisitor framework when an ast.ImportFrom node is visited. It does not explicitly call other functions or methods within its own source code.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method, part of the ast.NodeVisitor pattern, is invoked when an ast.ClassDef node is found. It manages the self.current_class context, setting it to the name of the current class before recursively visiting its children, and then restoring the previous class context upon exit. This ensures that methods defined within a class are correctly associated with that class.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the ast.NodeVisitor framework when an ast.ClassDef node is visited. It calls self.generic_visit.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method, part of the ast.NodeVisitor pattern, is called for ast.FunctionDef nodes. It constructs the full, unique name for the function using _make_full_name, updates self.local_defs to map the function's simple name (and potentially class-qualified name) to its full name, and sets self.current_function to track the current scope. It adds the function as a node to the self.graph and then recursively visits its body, finally adding the function to self.function_set and restoring the previous function context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the ast.NodeVisitor framework when an ast.FunctionDef node is visited, and by visit_AsyncFunctionDef. It calls `self._make_full_name`, `self.generic_visit`, `self.graph.add_node`, and `self.function_set.add`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method, part of the ast.NodeVisitor pattern, handles ast.AsyncFunctionDef nodes by simply delegating to visit_FunctionDef. This allows the call graph generation logic to treat synchronous and asynchronous function definitions identically for the purpose of identifying and tracking functions.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the ast.NodeVisitor framework when an ast.AsyncFunctionDef node is visited. It calls self.visit_FunctionDef.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method, part of the ast.NodeVisitor pattern, is triggered when an ast.Call node is encountered. It identifies the caller using _current_caller, extracts the components of the callee using _recursive_call, and then resolves the full name of the callee using _resolve_all_callee_names. Finally, it records the call relationship by adding the callee to the self.edges dictionary under the caller's entry, representing an edge in the call graph. It then continues AST traversal.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the ast.NodeVisitor framework when an ast.Call node is visited. It calls `self._current_caller`, `self._recursive_call`, `self._resolve_all_callee_names`, and `self.generic_visit`. It also interacts with `self.edges`.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method, part of the ast.NodeVisitor pattern, handles ast.If nodes. It specifically checks for the if __name__ == "__main__": block. If such a block is detected, it temporarily sets self.current_function to "<main_block>" before visiting the children of the if statement, effectively treating the main execution block as a distinct caller in the call graph. For other if statements, it simply delegates to generic_visit.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing an if statement.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the ast.NodeVisitor framework when an ast.If node is visited. It calls self.generic_visit.

---
### File: `backend/converter.py`
#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content)`
*   **Description:** The `wrap_cdata` function is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string by prepending "<![CDATA[\n" and appending "\n]]>" to the input content. This ensures that the enclosed content is treated as character data, preventing XML parsers from interpreting it as markup. The function directly returns this newly formatted string.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped within CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A new string containing the original content enclosed within CDATA tags.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs, image_list)`
*   **Description:** This function processes a list of output objects, typically from a notebook execution, to extract their content. It handles various output types, including display data (like images and text), stream outputs, and error messages. For images, it prioritizes PNG over JPEG, encodes them as Base64 strings, stores them in a provided list, and inserts an XML-like placeholder into the output. Text content is extracted directly, and errors are formatted into a string. The function returns a list of these extracted text snippets or image placeholders.
*   **Parameters:**
    - **outputs** (`list`): A list of output objects, each potentially containing different types of data such as display data, stream text, or error information. Each object is expected to have attributes like 'output_type', 'data', 'text', 'ename', and 'evalue'.
    - **image_list** (`list`): A list that is modified in-place to store dictionaries of image data (mime_type and Base64 string). This list accumulates all images processed by the function.
*   **Returns:**
    - **extracted_xml_snippets** (`list[str]`): A list of strings, where each string is either extracted text content, a formatted error message, or an XML-like placeholder for an image that was processed and added to the 'image_list'.
*   **Usage:**
    - **Calls:** backend.converter.process_image
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `process_image`
*   **Signature:** `def process_image(mime_type)`
*   **Description:** This function, `process_image`, is designed to handle image data based on a given MIME type. It expects to find the image's base64 encoded string within an external `data` dictionary, using the `mime_type` as a key. Upon successful retrieval, it cleans the base64 string and appends a dictionary containing the `mime_type` and the cleaned data to an external `image_list`. The function then returns a unique placeholder string that includes the image's assigned index and its MIME type. If the `mime_type` is not found in `data`, it returns `None`; if any error occurs during processing, it returns an error message string.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed, which serves as a key to retrieve the corresponding base64 encoded image data from an external `data` dictionary.
*   **Returns:**
    - **image_placeholder_tag** (`str`): A formatted string representing an image placeholder, containing the image's index in `image_list` and its MIME type, if processing is successful.
    - **error_message** (`str`): An error message string, prefixed with "<ERROR>", if an exception occurs during the image data processing.
    - **no_image_data** (`NoneType`): None if the provided `mime_type` is not found as a key in the external `data` dictionary.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content)`
*   **Description:** This function converts the content of a Jupyter notebook, provided as a string, into an XML representation. It attempts to parse the input as a notebook and handles `NotJSONError` by returning an error message. It iterates through each cell, converting markdown cells to XML markdown tags and code cells to XML code tags. If code cells have outputs, it processes them to extract content and images, then appends them as XML output tags. Finally, it returns the concatenated XML string and a list of any extracted images.
*   **Parameters:**
    - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a JSON string.
*   **Returns:**
    - **xml_representation** (`str`): A string containing the XML representation of the notebook, or an error message if parsing fails.
    - **extracted_images** (`list`): A list of images extracted from the notebook's output cells.
*   **Usage:**
    - **Calls:** backend.converter.extract_output_content and backend.converter.wrap_cdata.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files)`
*   **Description:** This function processes a collection of repository files, identifying and converting Jupyter notebooks. It filters the input `repo_files` to select only those with a '.ipynb' extension. For each identified notebook, it extracts its content and invokes `convert_notebook_to_xml` to generate XML output and associated image data. The function then aggregates these conversion results into a dictionary, mapping each notebook's file path to its corresponding XML and image data, before returning the complete set of processed information.
*   **Parameters:**
    - **repo_files** (`list`): An iterable collection of file objects, where each object is expected to have a 'path' attribute (string) and a 'content' attribute (string or bytes).
*   **Returns:**
    - **results** (`dict`): A dictionary where keys are the paths of the processed notebook files (string) and values are dictionaries containing the 'xml' output (string) and 'images' (list or dictionary of image data) generated from each notebook.
*   **Usage:**
    - **Calls:** backend.converter.convert_notebook_to_xml
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, providing a structured way to access its metadata and content. It implements lazy loading for the Git blob, file content, and size, ensuring that these potentially heavy operations are only performed when explicitly requested. The class offers properties to retrieve the Git blob, the decoded file content, and its size, along with utility methods for analysis and dictionary conversion.
*   **Instantiation:** This class is not explicitly shown to be instantiated by other components in the provided context.
*   **Dependencies:** This class does not have any explicit external dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes a RepoFile object by storing the file path and the Git `commit_tree`. It sets up internal attributes (`_blob`, `_content`, `_size`) to `None` for lazy loading of the Git blob, file content, and size, respectively, deferring their actual retrieval until they are accessed.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self, )`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if the `_blob` attribute is already set; if not, it attempts to retrieve the blob from the `_tree` using the file's path. If the file is not found in the tree, it raises a `FileNotFoundError`.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:** This method is not explicitly called by other components. It does not explicitly call other methods or functions.
    *   **`content`**
        *   *Signature:* `def content(self, )`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It checks if the `_content` attribute is already set; if not, it accesses the `blob` property to get the Git blob, reads its data stream, and decodes it using UTF-8 with error ignoring.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:** This method is not explicitly called by other components. It does not explicitly call other methods or functions.
    *   **`size`**
        *   *Signature:* `def size(self, )`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the `_size` attribute is already set; if not, it accesses the `blob` property to get the Git blob and retrieves its size attribute.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:** This method is not explicitly called by other components. It does not explicitly call other methods or functions.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self, )`
        *   *Description:* This method serves as an example analysis function. It calculates and returns the total number of words in the file's content by accessing the `content` property, splitting the string by whitespace, and counting the resulting elements.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **word_count** (`int`): The total number of words found in the file content.
        *   **Usage:** This method is not explicitly called by other components. It does not explicitly call other methods or functions.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self, )`
        *   *Description:* This special method provides a developer-friendly string representation of the `RepoFile` object. It returns a string that includes the class name and the path of the file it represents, making debugging and logging easier.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:** This method is not explicitly called by other components. It does not explicitly call other methods or functions.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method converts the `RepoFile` object into a dictionary representation. It includes the file's path, name (basename), size, and type. Optionally, it can also include the file's content if `include_content` is set to `True`.
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether to include the file's content in the dictionary.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing metadata about the file, optionally including its content.
        *   **Usage:** This method is not explicitly called by other components. It does not explicitly call other methods or functions.

---
#### Class: `GitRepository`
*   **Summary:** The GitRepository class is designed to manage a Git repository by cloning it into a temporary directory, providing structured access to its files, and ensuring proper cleanup. It acts as a context manager, allowing for automatic resource management. The class facilitates retrieving all files as `RepoFile` objects and organizing them into a hierarchical tree structure.
*   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
*   **Dependencies:** This class depends on `backend.getRepo.RepoFile` for representing individual files.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes a GitRepository instance by cloning the specified `repo_url` into a newly created temporary directory. It sets up essential instance attributes such as the repository object, the latest commit, and its commit tree. The constructor includes error handling for `GitCommandError` during the cloning process, ensuring the temporary directory is cleaned up if cloning fails.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self, )`
        *   *Description:* This method is responsible for retrieving all file paths from the cloned Git repository. It uses the underlying Git command `ls-files` to get a list of all tracked files. For each file path, it instantiates a `RepoFile` object, associating it with the repository's commit tree. The method stores this list of `RepoFile` objects internally and returns it.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository.
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:** This method is not explicitly called by other methods in the provided context. It calls `backend.getRepo.RepoFile` to create `RepoFile` instances.
    *   **`close`**
        *   *Signature:* `def close(self, )`
        *   *Description:* The `close` method handles the cleanup of the temporary directory created during the repository cloning process. It checks if `self.temp_dir` is set to ensure a directory exists before attempting to delete it. After deletion, `self.temp_dir` is set to `None` to prevent further attempts to delete a non-existent directory.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is not explicitly called by other methods in the provided context. It does not explicitly call other functions or methods.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self, )`
        *   *Description:* This special method enables the GitRepository class to be used as a context manager. When an instance of GitRepository is used in a `with` statement, the `__enter__` method is automatically invoked. It simply returns the instance itself, allowing it to be bound to a variable in the `with` statement.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository.
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository itself.
        *   **Usage:** This method is not explicitly called by other methods in the provided context. It does not explicitly call other functions or methods.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This special method is part of the context manager protocol and is automatically called when exiting a `with` statement block, regardless of whether an exception occurred. Its primary purpose is to ensure that the `close` method is invoked, thereby cleaning up the temporary repository directory. It accepts exception details but does not explicitly handle them, allowing them to propagate.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository.
            - **exc_type** (`type | None`): The type of the exception that caused the context to be exited, or None if no exception occurred.
            - **exc_val** (`Exception | None`): The exception instance that caused the context to be exited, or None.
            - **exc_tb** (`TracebackType | None`): A traceback object encapsulating the call stack at the point where the exception originally occurred, or None.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is not explicitly called by other methods in the provided context. It does not explicitly call other functions or methods.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method generates a hierarchical dictionary representation of the repository's file structure, mimicking a file system tree. It first ensures that all files have been retrieved by calling `get_all_files` if `self.files` is empty. It then iterates through the `RepoFile` objects, parsing their paths to build a nested dictionary structure where directories are represented by dictionaries with a 'children' list, and files are appended at their respective levels.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository.
            - **include_content** (`bool`): A flag indicating whether to include the file content in the dictionary representation. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree of the repository.
        *   **Usage:** This method is not explicitly called by other methods in the provided context. It does not explicitly call other functions or methods.

---
### File: `backend/main.py`
#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare the number of tokens between JSON and TOON formats. It takes the token counts for both formats, a savings percentage, and an output file path as input. The chart displays two bars, one for JSON tokens and one for TOON tokens, with their respective values shown above each bar. The chart is titled with the token comparison and the provided savings percentage, then saved to the specified output path before closing the plot.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated savings percentage to be displayed in the chart's title.
    - **output_path** (`str`): The file path where the generated bar chart image will be saved.
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep durations, which are incurred due to rate-limiting, from the total elapsed time. It takes start and end times, total items, batch size, and the model name as input. If the model is not a 'gemini-' model, it returns the total duration directly. Otherwise, it computes the number of batches and corresponding sleep time, then subtracts this from the total duration to yield the net time.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp or time value of the operation.
    - **end_time** (`float`): The ending timestamp or time value of the operation.
    - **total_items** (`int`): The total number of items processed during the operation.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model used, which determines if rate-limiting adjustments are applied.
*   **Returns:**
    - **net_time** (`float`): The calculated net duration of the operation, adjusted for estimated rate-limiting sleep times, or the total duration if no adjustment is needed.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing a software repository. It begins by parsing input to extract API keys, model configurations, and a GitHub repository URL. The repository is then cloned, and its contents are processed to extract basic project information, construct a file tree, perform relationship analysis, and generate an Abstract Syntax Tree (AST) schema. The AST schema is subsequently enriched with the extracted relationship data. Finally, the function prepares and dispatches analysis tasks to a Helper LLM for individual functions and classes, and then to a Main LLM to synthesize a final report, while also calculating token usage metrics.
*   **Parameters:**
    - **input** (`str`): The initial user input, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs ('scadsllm_base_url', 'ollama') required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used (e.g., 'gpt-5-mini', 'gpt-5.1').
    - **status_callback** (`callable | None`): An optional callback function used to provide status updates during the workflow execution.
*   **Returns:**
    - **result** (`dict`): A dictionary containing the 'report' (the final generated markdown report) and 'metrics' (a dictionary of performance and token usage statistics).
*   **Usage:**
    - **Calls:** backend.AST_Schema.ASTAnalyzer, backend.AST_Schema.ASTAnalyzer.analyze_repository, backend.AST_Schema.ASTAnalyzer.merge_relationship_data, backend.HelperLLM.LLMHelper, backend.HelperLLM.LLMHelper.generate_for_classes, backend.HelperLLM.LLMHelper.generate_for_functions, backend.MainLLM.MainLLM, backend.MainLLM.MainLLM.call_llm, backend.basic_info.ProjektInfoExtractor, backend.basic_info.ProjektInfoExtractor.extrahiere_info, backend.getRepo.GitRepository, backend.main.calculate_net_time, backend.main.create_savings_chart, backend.main.update_status, backend.relationship_analyzer.ProjectAnalyzer, backend.relationship_analyzer.ProjectAnalyzer.analyze, backend.relationship_analyzer.ProjectAnalyzer.get_raw_relationships, schemas.types.ClassAnalysisInput, schemas.types.ClassContextInput, schemas.types.FunctionAnalysisInput, schemas.types.FunctionContextInput, and schemas.types.MethodContextInput.
    - **Called By:** This function is called by no other functions.

---
#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function, `update_status`, processes and logs a given status message. It first checks for the existence of a `status_callback` and, if present, invokes it with the provided message. Subsequently, it logs the message using the `logging.info` facility. The primary purpose is to provide a centralized mechanism for status updates that can optionally trigger an external callback and always ensures logging.
*   **Parameters:**
    - **msg** (`str`): The status message string to be processed and logged.
*   **Returns:**
    - **None** (`None`): This function does not return any value; it performs side effects by potentially calling a callback and always logging the message.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback)`
*   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks within a specified GitHub repository using a Large Language Model (LLM). It begins by extracting a repository URL from the input, cloning the repository, and then processing its notebooks into an XML-like structure with embedded images. The function identifies the appropriate API key and base URL based on the chosen LLM model. It extracts basic project information and then iteratively generates individual reports for each notebook by constructing a specific payload and calling the LLM. Finally, it consolidates these reports, saves the comprehensive analysis to a markdown file, and returns the final report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): The input string, which is expected to contain a GitHub repository URL from which notebooks will be processed.
    - **api_keys** (`dict`): A dictionary containing various API keys required for different LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
    - **model** (`str`): The identifier for the specific Large Language Model to be used for generating reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`callable | None`): An optional callback function that receives status messages during the workflow execution, allowing for real-time updates.
*   **Returns:**
    - **report** (`str`): A concatenated string containing the final markdown report generated by the LLM for all processed notebooks.
    - **metrics** (`dict`): A dictionary providing performance and usage metrics of the workflow, including execution times and LLM model details.
*   **Usage:**
    - **Calls:** backend.MainLLM.MainLLM, backend.MainLLM.MainLLM.call_llm, backend.basic_info.ProjektInfoExtractor, backend.basic_info.ProjektInfoExtractor.extrahiere_info, backend.converter.process_repo_notebooks, backend.getRepo.GitRepository, backend.main.gemini_payload, and backend.main.update_status.
    - **Called By:** This function is not called by any other functions.

---
#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a multimodal payload suitable for the Gemini API. It takes basic project information, a notebook path, XML content of a notebook, and a list of image data. The function first serializes basic information and the notebook path into an introductory JSON string. It then processes the XML content, extracting text segments and replacing image placeholders with base64 encoded image URLs, assembling these into a list of content parts. The final output is a structured list containing text and image objects, ready for a multimodal AI model.
*   **Parameters:**
    - **basic_info** (`object`): A dictionary or object containing basic project information to be included in the payload context.
    - **nb_path** (`str`): The file path of the current notebook, included in the payload context.
    - **xml_content** (`str`): The XML string content of the notebook, which may contain image placeholders to be replaced.
    - **images** (`list`): A list of image data objects, where each object contains base64 encoded image data and its MIME type, corresponding to the image placeholders in the XML content.
*   **Returns:**
    - **payload_content** (`list`): A list of dictionaries, each representing a content part (text or image_url) formatted for a Gemini API multimodal payload.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/relationship_analyzer.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file system path into a Python module path string. It first attempts to calculate the path relative to a specified project root. If that fails, it uses the base name of the file. It then removes the '.py' extension if present, replaces path separators with dots, and finally adjusts the path for '__init__.py' files to represent their parent package.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform a static analysis of a Python project to build a comprehensive call graph. It identifies all Python files, collects definitions of functions, methods, and classes, and then resolves calls between these defined entities. The class provides methods to initiate the analysis and retrieve the raw relationships in a structured format, aiding in understanding the project's internal dependencies and structure.
*   **Instantiation:** This class is not explicitly instantiated by any entities listed in the provided context.
*   **Dependencies:** This class depends on backend.relationship_analyzer.CallResolverVisitor and backend.relationship_analyzer.path_to_module. It also utilizes standard library modules such as ast, os, logging, and collections.defaultdict.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer instance by setting up the project's root directory and various internal data structures. It prepares dictionaries for storing definitions, the call graph, and file ASTs, along with a set of directories to ignore during file traversal.
    *   *Parameters:*
        - **project_root** (`string`): The root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self, )`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect function, method, and class definitions. Subsequently, it resolves calls within each file to build a comprehensive call graph, clearing intermediate ASTs to free memory. The method returns the generated call graph upon completion.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:** This method is not explicitly called by other methods within the provided method_context. It calls _find_py_files, _collect_definitions, and _resolve_calls.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self, )`
        *   *Description:* This method processes the internal call_graph to generate structured outgoing and incoming relationship dictionaries. It iterates through the call graph, extracting caller and callee identifiers, and populates two defaultdict(set) objects to store the relationships. The sets are then converted to sorted lists for the final output, providing a clear view of dependencies.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, 'outgoing' and 'incoming', each mapping identifiers to sorted lists of related identifiers.
        *   **Usage:** This method is not explicitly called by other methods within the provided method_context. It does not explicitly call other methods, classes, or functions within its source code.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self, )`
        *   *Description:* This private helper method traverses the project directory starting from self.project_root to locate all Python files. It uses os.walk and filters out specified ignore_dirs to avoid analyzing irrelevant directories. The method compiles and returns a list of absolute paths to all '.py' files found within the project scope.
        *   *Parameters:*
            *Analysis data not available for this component.*
        *   *Returns:*
            - **py_files** (`list`): A list of absolute file paths to all Python files found in the project, excluding ignored directories.
        *   **Usage:** This method is called by analyze. It calls os.walk and os.path.join.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method is responsible for parsing a given Python file and collecting all function, method, and class definitions within it. It reads the file, parses it into an Abstract Syntax Tree (AST), and then walks the AST to identify FunctionDef and ClassDef nodes. For each definition, it constructs a unique path name and stores its file, line number, and type in self.definitions, also caching the AST in self.file_asts.
        *   *Parameters:*
            - **filepath** (`string`): The absolute path to the Python file being analyzed for definitions.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by analyze. It calls path_to_module, _get_parent, ast.parse, ast.walk, ast.FunctionDef, ast.ClassDef, and logging.error.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This private helper method finds the direct parent AST node of a given child node within a specific AST tree. It iterates through all nodes in the tree and checks their children to find a match for the provided node. This is primarily used to determine if a FunctionDef is nested within a ClassDef to correctly identify it as a method.
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent_node** (`ast.AST or None`): The parent AST node of the given node if found, otherwise None.
        *   **Usage:** This method is called by _collect_definitions. It calls ast.walk and ast.iter_child_nodes.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method takes a file's AST and uses a CallResolverVisitor to identify all function and method calls within that file. It retrieves the AST from self.file_asts, initializes the resolver with the file's context and collected definitions, and then visits the AST. The identified calls from the resolver are subsequently merged into the self.call_graph structure, with error logging for robustness.
        *   *Parameters:*
            - **filepath** (`string`): The absolute path to the Python file whose calls are to be resolved.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by analyze. It calls CallResolverVisitor and logging.error.

---
#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor is an AST NodeVisitor designed to traverse Python source code's Abstract Syntax Tree to identify and resolve function and method calls. It systematically builds a call graph by tracking the fully qualified names of callers and callees, managing import scopes, and inferring types of instantiated objects. This class is crucial for understanding the dynamic relationships between different parts of a codebase by collecting detailed information about each detected call.
*   **Instantiation:** The class is not explicitly instantiated by any known components in the provided context.
*   **Dependencies:** This class depends on `backend.relationship_analyzer.path_to_module` for converting file paths to module paths.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallResolverVisitor with the file path of the code being analyzed, the project's root directory, and a dictionary of known definitions. It sets up internal state variables such as the module path, a scope dictionary for imports, a dictionary to track instance types, and a defaultdict to store the collected call relationships. This setup is essential for accurately resolving call targets during AST traversal.
    *   *Parameters:*
        - **filepath** (`str`): The absolute path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the entire project, used to determine module paths.
        - **definitions** (`dict`): A dictionary containing known fully qualified definitions within the project, used for validating resolved call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is invoked when the AST visitor encounters a class definition (`ast.ClassDef`). Its primary role is to manage the `current_class_name` state variable, which tracks the class currently being processed. It saves the old class name, sets the new one, recursively visits all child nodes within the class, and then restores the `current_class_name` to its previous value. This ensures that methods defined within the class are correctly associated with their parent class for accurate call resolution.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the AST visitor framework when a ClassDef node is encountered. It calls the generic visitor method to continue traversing the AST.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, which represent function or method definitions. It constructs a fully qualified identifier for the current function, taking into account whether it's a method within a class or a top-level function. The method then updates `self.current_caller_name` to this identifier before recursively visiting the function's body, ensuring that any calls made within this function are correctly attributed. Finally, it restores the `current_caller_name` to its state before entering the function.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the AST visitor framework when a FunctionDef node is encountered. It calls the generic visitor method to continue traversing the AST.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method is triggered upon encountering an `ast.Call` node, signifying a function or method invocation. It attempts to resolve the fully qualified name of the called entity using the `_resolve_call_qname` helper method. If a valid callee pathname is resolved and exists in the `self.definitions`, it records comprehensive information about the caller, including its file, line number, full identifier, and type (module, local function, or method). This collected caller information is then appended to the `self.calls` dictionary, keyed by the callee's pathname, effectively building the call graph.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the AST visitor framework when a Call node is encountered. It calls `_resolve_call_qname` to determine the callee's qualified name and the generic visitor method to continue traversing the AST.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method processes `ast.Import` nodes, which correspond to `import module_name` statements. It iterates through all aliases defined in the import statement, mapping the local name (either the alias or the original module name) to its fully qualified name. This mapping is stored in `self.scope`, which is later used to resolve calls to imported modules or their members. After processing the import, it continues the generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the AST visitor framework when an Import node is encountered. It calls the generic visitor method to continue traversing the AST.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent `from module import name` statements. It first determines the full module path, correctly handling relative imports based on `node.level`. For each imported name (and its alias, if present), it constructs its fully qualified path by combining the module path and the imported name. This resolved path is then stored in `self.scope`, mapping the local name to its global identifier, which is crucial for subsequent call resolution. The method then continues the generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the AST visitor framework when an ImportFrom node is encountered. It calls the generic visitor method to continue traversing the AST.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method processes `ast.Assign` nodes, which represent assignment statements. It specifically looks for assignments where the right-hand side is a function call (e.g., `x = MyClass()`). If the called function is identified as a class constructor that exists in both `self.scope` and `self.definitions`, it records the fully qualified class name as the inferred type for the assigned variable. This type information is stored in `self.instance_types`, enabling more accurate resolution of method calls on these instances later in the analysis.
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
             *Analysis data not available for this component.*
        *   **Usage:** This method is called by the AST visitor framework when an Assign node is encountered. It calls the generic visitor method to continue traversing the AST.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method is responsible for determining the fully qualified name (QName) of a function or method being called. It handles two primary scenarios: direct function calls (`ast.Name`) and method calls on an object (`ast.Attribute`). For direct calls, it first checks `self.scope` for imported names, then local module paths. For attribute calls, it uses `self.instance_types` to resolve the class of an instance variable or `self.scope` for module-level attributes, subsequently appending the method name. If resolution is successful, it returns the QName; otherwise, it returns `None`.
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., ast.Name or ast.Attribute).
        *   *Returns:*
            - **qualified_name** (`str | None`): The fully qualified name of the callable if resolved, otherwise None.
        *   **Usage:** This method is called by `visit_Call` to resolve the qualified name of a function or method invocation. It does not explicitly call other methods within its own source code.

---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** This function encrypts a given string using a `cipher_suite` object. It first checks if the input `text` or `cipher_suite` is empty; if either is, it returns the original text without encryption. Otherwise, it strips whitespace from the text, encodes it to bytes, encrypts it using `cipher_suite.encrypt`, and then decodes the resulting bytes back into a string before returning it. This process ensures that sensitive text data can be securely stored or transmitted.
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string, or the original string if encryption was skipped due to missing text or cipher_suite.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** This function attempts to decrypt a given text string using a `cipher_suite` object. It first checks if the input `text` or `cipher_suite` is empty, returning the original text if either condition is true. If both are present, it proceeds to strip whitespace from the text, encode it to bytes, decrypt it using `cipher_suite.decrypt`, and then decode the result back into a string. The function includes error handling, returning the original text if any exception occurs during the decryption process.
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_or_original_text** (`str`): The decrypted string if successful, or the original string if decryption is not performed (due to empty input/cipher_suite) or if an error occurs during decryption.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function is responsible for creating a new user entry in the database. It takes a username, a user's name, and a plaintext password as input. The password is first hashed using a security utility before being stored. The function constructs a user document with the provided details, including empty fields for various API keys, and then inserts this document into the 'dbusers' collection. Finally, it returns the unique identifier of the newly inserted user document.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which will be used as the document's _id.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plaintext password provided by the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`Any`): The unique identifier (typically a string or ObjectId) of the newly inserted user document.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** The `fetch_all_users` function retrieves all user records from a database collection. It invokes the `find()` method on the `dbusers` object, which is expected to be a database collection, to obtain a cursor of all documents. The function then converts this cursor into a standard Python list, effectively returning all user data as a collection of documents. This provides a direct method to access the complete set of user information stored.
*   **Parameters:**
    *This function takes no parameters.*
*   **Returns:**
    - **users** (`list`): A list containing all user documents (e.g., dictionaries) retrieved from the 'dbusers' collection.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** The `fetch_user` function is designed to retrieve a single user document from a database collection. It takes a `username` as an argument and uses it to query the `dbusers` collection. The function specifically searches for a document where the `_id` field matches the provided username. It then returns the first matching document found.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) used to locate a specific user document in the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if a match is found, otherwise None if no user with the given username exists.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

---
#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username, new_name)`
*   **Description:** This function updates the 'name' field for a specific user in the 'dbusers' collection. It identifies the target user document using the provided 'username' as the '_id' field. The function then sets the 'name' field of that document to the 'new_name' value. It returns an integer indicating the number of documents that were modified by this update operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user, used to locate the document by its '_id' field.
    - **new_name** (`str`): The new name to be assigned to the user's 'name' field.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function updates a user's Gemini API key in a database. It accepts a username and the new API key as input. The provided Gemini API key is first stripped of any leading or trailing whitespace and then encrypted using the `encrypt_text` utility. The function then attempts to locate the user document by their `_id` (username) in the `dbusers` collection and sets the `gemini_api_key` field to the newly encrypted value. It returns the count of documents that were modified by this update operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored, which will be encrypted before being saved to the database.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 typically indicates a successful update, while 0 suggests the user was not found or no change was necessary.
*   **Usage:**
    - **Calls:** database.db.encrypt_text
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username, gpt_api_key)`
*   **Description:** This function updates a user's GPT API key in the database. It takes a username and a new GPT API key as input. The provided API key is first stripped of whitespace and then encrypted using the `encrypt_text` function. The function then performs an update operation on the `dbusers` collection, locating the user by their `_id` (username) and setting the `gpt_api_key` field to the newly encrypted value. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key provided by the user, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:**
    - **Calls:** database.db.encrypt_text
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function updates the Ollama base URL associated with a specific user in a database. It takes a username and a new Ollama base URL as input. The provided URL is first stripped of any leading or trailing whitespace before being stored. The function then performs an update operation on the database, targeting the user identified by the given username. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Ollama base URL needs to be updated.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service. Any leading or trailing whitespace will be removed before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 typically indicates a successful update for the specified user.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username, opensrc_api_key)`
*   **Description:** This function is responsible for updating a user's Open Source API key within a database. It takes a username and the new API key as input. The provided API key is first stripped of any leading or trailing whitespace and then encrypted using a helper function. Finally, the function updates the 'opensrc_api_key' field for the specified user in the 'dbusers' collection with the encrypted value.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source API key needs to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be stored for the user, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. Typically 1 if the user was found and updated, or 0 if no matching user was found.
*   **Usage:**
    - **Calls:** database.db.encrypt_text
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username, opensrc_base_url)`
*   **Description:** This function updates the 'opensrc_base_url' for a specific user in a database. It takes a username and a new opensrc base URL as input. The function uses the provided username to locate the user record and then sets the new base URL, ensuring any leading or trailing whitespace is removed from the URL. It returns the count of documents that were modified by this update operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose opensrc base URL needs to be updated.
    - **opensrc_base_url** (`str`): The new base URL for opensrc, which will be stripped of leading/trailing whitespace before being stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** This function is designed to retrieve a user's Gemini API key from a database. It takes a username as input and queries a 'dbusers' collection to find a matching user document. The function specifically projects the 'gemini_api_key' field. If a user is found, it safely extracts and returns the 'gemini_api_key' using the .get() method. If no user document is found for the given username, or if the 'gemini_api_key' field is absent, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched from the database.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key string associated with the specified username, or None if the user is not found or the key does not exist in the user's document.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** This function retrieves the Ollama base URL associated with a given username from a database. It queries the `dbusers` collection, using the provided username as the document's `_id`. The function specifically projects and fetches the `ollama_base_url` field. If a user document is found, it returns the value of `ollama_base_url`; otherwise, it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL associated with the user, or `None` if the user is not found in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username)`
*   **Description:** This function is designed to retrieve a user's GPT API key from a database. It takes a username as input and performs a database query on a 'dbusers' collection, likely a MongoDB collection, to locate the corresponding user document. The query specifically fetches the 'gpt_api_key' field. If a user is found, the function returns the value of their 'gpt_api_key'; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the user, or None if the user is not found or does not have a key.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

---
#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username)`
*   **Description:** This function, `fetch_opensrc_key`, is designed to retrieve an Open Source API key for a specific user from a database. It queries the `dbusers` collection using the provided username as the document's `_id`. The query is configured to return only the `opensrc_api_key` field, excluding the `_id` itself. If a matching user document is found, the function extracts and returns the `opensrc_api_key` value. If no user is found or the key is absent, the function returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Open Source API key is to be fetched.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key associated with the specified user, or None if the user is not found or the key does not exist.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username)`
*   **Description:** This function retrieves the 'opensrc_base_url' for a specified user from a database. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided username. If a matching user document is found, the function extracts the value of the 'opensrc_base_url' field. The function returns this URL if found, otherwise it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose opensrc base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The opensrc base URL associated with the user, or None if the user is not found or the 'opensrc_base_url' field is not present.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** This function removes a user record from the database. It takes a username as input, which serves as the unique identifier (`_id`) for the user document. The function executes a delete operation on the `dbusers` collection and returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user to be deleted, corresponding to the `_id` field in the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of user documents that were successfully deleted from the database. This will typically be 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function retrieves and decrypts various API keys and base URLs associated with a given username from a database. It queries the `dbusers` collection for a user document matching the provided `username`. If no user is found, it returns `None` for all expected values. Otherwise, it extracts specific API keys and URLs, decrypting the `gemini_api_key`, `gpt_api_key`, and `opensrc_api_key` using the `decrypt_text` function. The `ollama_base_url` and `opensrc_base_url` are retrieved without decryption.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The decrypted Gemini API key, or an empty string if not found, or None if the user does not exist.
    - **ollama_base_url** (`str | None`): The Ollama base URL, or an empty string if not found, or None if the user does not exist.
    - **gpt_api_key** (`str | None`): The decrypted GPT API key, or an empty string if not found, or None if the user does not exist.
    - **opensrc_api_key** (`str | None`): The decrypted Open Source API key, or an empty string if not found, or None if the user does not exist.
    - **opensrc_base_url** (`str | None`): The Open Source base URL, or an empty string if not found, or None if the user does not exist.
*   **Usage:**
    - **Calls:** database.db.decrypt_text
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username, chat_name)`
*   **Description:** This function creates a new chat entry in the database. It constructs a chat document with a unique identifier generated by `uuid.uuid4()`, the provided username, the chat name, and the current timestamp using `datetime.now()`. The constructed chat document is then inserted into the `dbchats` collection. Finally, it returns the `_id` of the newly inserted chat document.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier of the newly created chat entry in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

---
#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username)`
*   **Description:** This function retrieves all chat records associated with a specific user from a database. It queries a collection, presumably `dbchats`, for documents where the 'username' field matches the provided input. The results are then sorted in ascending order based on their 'created_at' timestamp before being returned as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat records.
*   **Returns:**
    - **chats** (`list`): A list of chat records (documents) associated with the specified username, sorted by their creation date.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username, chat_name)`
*   **Description:** This function checks for the existence of a specific chat within the 'dbchats' collection. It takes a username and a chat name as input and queries the database to see if a document matching both criteria exists. The function returns a boolean value indicating whether such a chat was found.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to check for existence.
*   **Returns:**
    - **chat_exists** (`bool`): True if a chat matching the provided username and chat name exists in the database, False otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
*   **Description:** This function is designed to fully rename a chat entry and all its associated message exchanges within a database. It first updates the chat's name in the `dbchats` collection, changing the `chat_name` from `old_name` to `new_name` for a given `username`. Subsequently, it updates all related message exchanges in the `dbexchanges` collection, ensuring their `chat_name` also reflects the `new_name`. The function returns the count of chat entries modified during the initial update operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat that needs to be changed.
    - **new_name** (`str`): The new desired name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat documents modified in the 'dbchats' collection.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time, json_tokens, toon_tokens, savings_percent)`
*   **Description:** This function `insert_exchange` is responsible for storing a new chat exchange record into a database collection. It first generates a unique identifier for the exchange using `uuid.uuid4()`. It then compiles an `exchange` dictionary containing the provided question, answer, feedback, user details, chat name, various usage metrics (helper/main used, time, tokens), and a `created_at` timestamp. Finally, it attempts to insert this dictionary into the database. If successful, it returns the newly generated ID; otherwise, it catches any exceptions, prints an error, and returns `None`.
*   **Parameters:**
    - **question** (`str`): The user's question in the exchange.
    - **answer** (`str`): The generated answer for the question.
    - **feedback** (`str`): Feedback provided for the exchange.
    - **username** (`str`): The username associated with this exchange.
    - **chat_name** (`str`): The name of the chat session this exchange belongs to.
    - **helper_used** (`str`): Indicates which helper was used, if any. Defaults to an empty string.
    - **main_used** (`str`): Indicates which main system was used, if any. Defaults to an empty string.
    - **total_time** (`str`): The total time taken for the exchange. Defaults to an empty string.
    - **helper_time** (`str`): The time taken by the helper. Defaults to an empty string.
    - **main_time** (`str`): The time taken by the main system. Defaults to an empty string.
    - **json_tokens** (`int`): The number of JSON tokens used. Defaults to 0.
    - **toon_tokens** (`int`): The number of Toon tokens used. Defaults to 0.
    - **savings_percent** (`float`): The percentage of savings achieved. Defaults to 0.0.
*   **Returns:**
    - **result** (`str | None`): The unique identifier (string) of the newly inserted exchange if successful, or None if a database error occurs during insertion.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by other functions in the provided context.

---
#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** The `fetch_exchanges_by_user` function is responsible for retrieving exchange records from a database. It queries the `dbexchanges` collection, filtering documents by a specified username. The results are then sorted by their `created_at` timestamp in ascending order, which is noted as important for display. Finally, the function returns the sorted list of exchange records.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchange records from the database.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records associated with the given username, sorted by their creation timestamp.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function is designed to retrieve chat exchanges from a database. It queries a collection, likely named 'dbexchanges', using a specified username and chat name as filtering criteria. The retrieved exchanges are then sorted chronologically by their 'created_at' timestamp in ascending order. The function processes the database cursor into a list before returning the results.
*   **Parameters:**
    - **username** (`str`): The username used to filter the chat exchanges.
    - **chat_name** (`str`): The name of the chat to filter the exchanges by.
*   **Returns:**
    - **exchanges** (`list`): A list of chat exchange documents that match the provided username and chat name, sorted by their creation time.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function is responsible for updating the feedback value associated with a specific exchange record in a database. It accepts an exchange identifier and an integer feedback value. The function performs an update operation on the 'dbexchanges' collection, targeting the document matching the provided 'exchange_id' and setting its 'feedback' field. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated. Its specific type is inferred to be compatible with a database document's '_id' field.
    - **feedback** (`int`): The integer value representing the feedback to be set for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation, typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function is responsible for updating the feedback message associated with a specific exchange record in a database. It takes an exchange identifier and a new feedback message string as input. The function uses an `update_one` operation to locate the exchange by its `_id` and then sets the `feedback_message` field to the provided string. Finally, it returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated.
    - **feedback_message** (`str`): The new feedback message string to be stored for the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function is designed to remove a specific exchange record from a database collection. It accepts a unique identifier, `exchange_id`, to locate the target document. The function interacts with the `dbexchanges` collection, likely a MongoDB collection object, to execute a delete operation based on the provided ID. Upon completion, it returns an integer indicating how many documents were successfully removed. This count will typically be 1 if a matching record was found and deleted, or 0 if no such record existed.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were successfully deleted (0 or 1).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username, chat_name)`
*   **Description:** This function is designed to completely remove a specified chat and all its associated message exchanges from the database. It first deletes all message exchanges linked to the given username and chat name. Following this, it proceeds to delete the chat entry itself. This two-step deletion process ensures data consistency by preventing orphaned message records. The function returns the count of chat documents successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted from the database. This will typically be 1 if the chat was found and deleted, or 0 if it was not found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `frontend/frontend.py`
#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list)`
*   **Description:** This function processes a list of strings, where each string is expected to represent a model name or path. It iterates through the provided list and for each item, it splits the string by the '/' character. The function then extracts the last component of the split string, effectively removing any preceding path information. The result is a new list containing these cleaned, simplified model names.
*   **Parameters:**
    - **model_list** (`List[str]`): A list of strings, where each string is expected to be a model identifier or path that may contain '/' separators.
*   **Returns:**
    - **cleaned_model_names** (`List[str]`): A new list containing strings, where each string is the last component of the original model name after splitting by '/'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list, category_name)`
*   **Description:** This function, `get_filtered_models`, filters a provided list of models based on a specified category name. It retrieves a set of keywords associated with the `category_name` from a global `CATEGORY_KEYWORDS` mapping. If the category's keywords include "STANDARD", the function returns only those models from the `source_list` that are also present in a `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list`, checking if any of the category's keywords are contained within each model's lowercase name. The function returns the resulting filtered list, or the original `source_list` if no models matched the filtering criteria.
*   **Parameters:**
    - **source_list** (`list`): The initial list of models to be filtered.
    - **category_name** (`str`): The name of the category used to determine filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered according to the specified category, or the original `source_list` if no models match the filter.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function serves as a callback to handle the saving of a Gemini API key. It retrieves a potential new Gemini key from the Streamlit session state. If a valid key is found, it proceeds to update this key in the database, associating it with the currently logged-in username. After a successful update, the input field for the Gemini key in the session state is cleared, and a success toast notification is displayed to the user.
*   **Parameters:**
    *This function takes no parameters.*
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** database.db.update_gemini_key
    - **Called By:** This function is called by no other functions.

---
#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function, `save_ollama_cb`, is designed to save a user-provided Ollama URL. It retrieves the potential new URL from the Streamlit session state under the key 'in_ollama_url'. If a valid, non-empty URL is found, the function proceeds to update this URL in the database. The update operation uses the current user's username, also retrieved from the session state, to associate the URL. Upon successful database update, a confirmation toast message is displayed to the user.
*   **Parameters:**
    *This function takes no parameters.*
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** database.db.update_ollama_url
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** This function `load_data_from_db` is designed to load chat and exchange data for a specific user from the database into the Streamlit session state. It first verifies if the data for the provided username is already loaded to avoid redundant operations. The process involves fetching predefined chats, then loading individual exchanges and associating them with their respective chats, including support for legacy data where exchanges might exist for undefined chats. Finally, it ensures that at least one chat exists, creating a default 'Chat 1' if none are found, and sets an active chat for the user's session state.
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat and exchange data.
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** database.db.fetch_chats_by_user, database.db.fetch_exchanges_by_user, and database.db.insert_chat.
    - **Called By:** This function is called by no other functions.

---
#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function handles changes to feedback for an exchange object. It updates the 'feedback' key of the provided exchange dictionary 'ex' with the new 'val'. Subsequently, it persists this feedback change to the database by calling 'db.update_exchange_feedback' using the exchange's '_id' and the new feedback value. Finally, it triggers a rerun of the Streamlit application to reflect the changes in the UI.
*   **Parameters:**
    - **ex** (`dict`): The exchange object, expected to be a dictionary containing at least 'feedback' and '_id' keys.
    - **val** (`Any`): The new feedback value to be assigned to the exchange object.
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** database.db.update_exchange_feedback
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it updates the Streamlit session state by locating the associated chat and removing the exchange from its list of exchanges. Finally, it triggers a full Streamlit rerun to reflect these changes in the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat to which the exchange belongs, used to locate it within the Streamlit session state.
    - **ex** (`dict`): The exchange object to be deleted, which is expected to contain an '_id' key for database deletion and to be present in the chat's exchanges list.
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** database.db.delete_exchange_by_id
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function handles the deletion of a specified chat for a given user. It first calls the database to delete the full chat record. Subsequently, it cleans up the chat from the Streamlit session state. If other chats exist, it sets the first available chat as the active one; otherwise, it creates a new default chat named 'Chat 1' and sets it as active. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** database.db.delete_full_chat and database.db.insert_chat.
    - **Called By:** This function is called by no other functions.

---
#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** This function is designed to extract a repository name from a given text string. It first attempts to find a URL within the text using a regular expression. If a URL is successfully matched, it then parses this URL to isolate its path component. The last segment of the path is then considered the potential repository name. A specific check is included to remove a '.git' suffix if present, before returning the cleaned repository name. If no URL is found or a repository name cannot be extracted, the function returns None.
*   **Parameters:**
    - **text** (`str`): The input string from which to extract a repository name, potentially containing a URL.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string, or None if no repository name could be found or extracted.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

---
#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** This function acts as a generator that streams an input string word by word. It takes a complete text string, splits it into individual words, and then yields each word sequentially, appending a space after it. A small delay is introduced between yielding each word to simulate a streaming effect, often used for displaying text progressively in user interfaces.
*   **Parameters:**
    - **text** (`str`): The input string that needs to be streamed word by word.
*   **Returns:**
    - **word** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

---
#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream)`
*   **Description:** This function processes a given markdown text, identifying and rendering embedded Mermaid diagrams. It splits the input text into parts based on '```mermaid' delimiters. Non-Mermaid text is rendered as standard markdown, optionally streamed if 'should_stream' is true. Mermaid diagram code blocks are attempted to be rendered using 'st_mermaid', with a fallback to displaying the code block if rendering fails. The function handles cases where the input markdown text is empty by returning early.
*   **Parameters:**
    - **markdown_text** (`str`): The input text, which may contain embedded Mermaid diagram syntax.
    - **should_stream** (`bool`): A boolean flag indicating whether non-Mermaid text parts should be streamed using 'st.write_stream' or rendered directly with 'st.markdown'. Defaults to False.
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** frontend.frontend.stream_text_generator
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** The `render_exchange` function is responsible for displaying a single chat exchange, consisting of a user's question and an assistant's answer, within a Streamlit application. It first renders the user's question. Subsequently, it displays the assistant's response along with an interactive toolbar. This toolbar provides functionalities such as feedback (like/dislike), adding comments, downloading the response, and deleting the exchange. In cases where the answer indicates an error, a simplified error message and a delete option are presented. Finally, the function uses `render_text_with_mermaid` to display the answer content.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing a single chat exchange, containing keys like 'question', 'answer', '_id', 'feedback', and 'feedback_message'.
    - **current_chat_name** (`str`): The name of the current chat, used as context when performing operations like deleting an exchange.
*   **Returns:**
    *This function does not return a value.*
*   **Usage:**
    - **Calls:** database.db.update_exchange_feedback_message, frontend.frontend.handle_delete_exchange, frontend.frontend.handle_feedback_change, and frontend.frontend.render_text_with_mermaid.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to structure and validate information about a single parameter of a function. It serves as a data model, ensuring that parameter details such as its name, data type, and a descriptive explanation are consistently represented as strings. This class facilitates the standardized description of function parameters within a larger system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an __init__ method. It initializes an instance of ParameterDescription by accepting 'name', 'type', and 'description' as keyword arguments, validating them against their respective string types as defined by the model schema.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type hint or inferred type of the parameter.
        - **description** (`str`): A textual description of the parameter's purpose.
*   **Methods:**
    *No methods defined.*

---
#### Class: `ReturnDescription`
*   **Summary:** The `ReturnDescription` class is a Pydantic BaseModel designed to provide a structured representation for the return value of a function. It encapsulates essential information such as the return value's name, its data type, and a descriptive explanation. This class acts as a schema for consistent data handling when describing function outputs.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `ReturnDescription` is automatically generated. It initializes an instance of the class by accepting `name`, `type`, and `description` as keyword arguments, performing type validation, and assigning these values as instance attributes.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The Python type hint or a string representation of the return value's data type.
        - **description** (`str`): A detailed textual explanation of what the return value represents or its purpose.
*   **Methods:**
    *No methods defined.*

---
#### Class: `UsageContext`
*   **Summary:** This class serves as a Pydantic BaseModel, designed to structure and validate information regarding the usage context of a function. It defines two string attributes, `calls` and `called_by`, which are intended to describe what a function invokes and where it is invoked from, respectively. Essentially, it acts as a data container for contextual call information.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method, implicitly generated by Pydantic, initializes an instance of `UsageContext`. It expects `calls` and `called_by` as keyword arguments, which are then assigned as instance attributes, ensuring type validation according to their string annotations.
    *   *Parameters:*
        - **calls** (`str`): A string describing other methods, classes, or functions that this method calls inside its source code.
        - **called_by** (`str`): A string describing the name of another function or method that calls this method.
*   **Methods:**
    *No methods defined.*

---
#### Class: `FunctionDescription`
*   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data schema to store details such as the function's high-level purpose, its input parameters, its return values, and its operational context within a larger system. This class ensures that function analysis data is consistently formatted and validated.
*   **Instantiation:** There are no explicit instantiation points provided in the context for this class.
*   **Dependencies:** This class primarily depends on Pydantic's BaseModel for data validation and structuring. It also relies on `List` from `typing` and other custom types like `ParameterDescription`, `ReturnDescription`, and `UsageContext` for its field definitions.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is implicitly generated to validate and assign values to the class's fields. It initializes an instance of `FunctionDescription` by taking the function's overall description, a list of its parameters, a list of its return values, and its usage context as arguments.
    *   *Parameters:*
        - **overall** (`str`): A concise, high-level summary describing the function's purpose and its implementation details.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing an input parameter of the function, including its name, type, and description.
        - **returns** (`List[ReturnDescription]`): A list of `ReturnDescription` objects, each describing a value returned by the function, including its name, type, and description.
        - **usage_context** (`UsageContext`): An object providing context on how the function interacts with other parts of the system, specifically what it calls and where it is called from.
*   **Methods:**
    *No methods defined.*

---
#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate the comprehensive analysis of a single Python function. It serves as a structured data container, holding the function's unique identifier, a detailed description of its purpose and signature, and an optional field for any errors encountered during its analysis. This model is fundamental for generating machine-readable reports on individual functions.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class does not define an explicit `__init__` method. Pydantic's `BaseModel` handles the initialization of its fields (`identifier`, `description`, `error`) based on the provided type hints, allowing instances to be created by passing keyword arguments corresponding to these fields.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *No methods defined.*

---
#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to structure information about the `__init__` method of another class. It encapsulates a high-level textual description of the constructor and a list of its individual parameters, each detailed by a `ParameterDescription` object. This model is used to standardize the representation of constructor metadata within a larger system.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly generates its `__init__` method. It initializes instances by accepting values for its `description` and `parameters` fields, performing data validation based on their type hints.
    *   *Parameters:*
        - **description** (`str`): A textual summary of the constructor's purpose.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each describing a parameter of the constructor.
*   **Methods:**
    *No methods defined.*

---
#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to describe the contextual information of another class. It encapsulates details about the external dependencies that a class relies upon and specifies where that class is primarily instantiated within a larger system. This model serves as a structured way to convey usage and integration context.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not define an explicit `__init__` method. Pydantic's `BaseModel` handles the initialization of its fields based on the provided type hints, automatically creating an initializer that accepts `dependencies` and `instantiated_by` as string arguments.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *No methods defined.*

---
#### Class: `ClassDescription`
*   **Summary:** The `ClassDescription` class is a Pydantic model designed to encapsulate a comprehensive analysis of another Python class. It structures information about a class's overall purpose, its constructor, a list of its methods with detailed analysis, and its usage context within a larger system. This model serves as a data container for structured class metadata.
*   **Instantiation:** This class is not explicitly listed as being instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, `ClassDescription`'s constructor is implicitly generated. It initializes an instance by validating and assigning values to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose and functionality.
        - **init_method** (`ConstructorDescription`): An object containing a detailed description of the class's constructor method.
        - **methods** (`List[FunctionAnalysis]`): A list of `FunctionAnalysis` objects, each providing a detailed analysis of a method within the class.
        - **usage_context** (`ClassContext`): An object describing the class's external dependencies and where it is instantiated.
*   **Methods:**
    *No methods defined.*

---
#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python class. It serves as the top-level schema for structured output, containing the class's unique identifier, a detailed description object that further breaks down its constructor and methods, and an optional field for error reporting. This model provides a standardized format for representing the analytical results of a class.
*   **Instantiation:** The specific instantiation points for this class are not provided in the given context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `ClassAnalysis` class, being a Pydantic BaseModel, has its `__init__` method implicitly generated by Pydantic. This constructor is responsible for initializing instances with the `identifier`, `description`, and an optional `error` field, ensuring type validation and data integrity upon object creation.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
        - **error** (`Optional[str]`): An optional string field to store any error messages if the analysis process encounters issues.
*   **Methods:**
    *No methods defined.*

---
#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event identified by a relationship analyzer. It encapsulates details about where a call originated, including the file path, the name of the calling function, its type (mode), and the exact line number. This model is primarily used to structure data for 'called_by' and 'instantiated_by' lists within a larger system.
*   **Instantiation:** This class is not explicitly instantiated by any known components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, CallInfo's constructor is automatically generated. It initializes an instance by validating and assigning values to its fields: file, function, mode, and line. This ensures that all call event data conforms to the specified types upon instantiation.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that made the call.
        - **mode** (`str`): The type of the calling entity, e.g., 'method', 'function', 'module'.
        - **line** (`int`): The line number in the file where the call event is located.
*   **Methods:**
    *No methods defined.*

---
#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class serves as a Pydantic BaseModel for structuring the contextual information necessary to analyze a specific function. It encapsulates details about other functions or methods that the target function invokes, as well as information about where the target function itself is called within the codebase. This structured approach facilitates a comprehensive understanding of a function's interactions and dependencies.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, has its constructor implicitly generated by Pydantic. It is responsible for initializing the `calls` and `called_by` attributes, ensuring that the provided input data conforms to the specified types for structured function context.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of identifiers (strings) representing other functions, methods, or classes that the function under analysis calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, each providing details about a specific location or entity that calls the function under analysis.
*   **Methods:**
    *No methods defined.*

---
#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a FunctionAnalysis object. It serves as a data transfer object, ensuring that all necessary information for analyzing a Python function, such as its source code, identifier, and contextual data, is provided in a consistent and validated format. This class is crucial for standardizing the input for an AI code analysis system.
*   **Instantiation:** The instantiation points for this class are not provided in the current context, but it is typically instantiated by components that prepare data for function analysis tasks.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within its definition, relying primarily on Pydantic for its model capabilities.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. It inherits from `pydantic.BaseModel`, which automatically generates a constructor based on the declared fields. The constructor will accept keyword arguments corresponding to the `mode`, `identifier`, `source_code`, `imports`, and `context` fields to initialize an instance.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, fixed to 'function_analysis' to indicate a function analysis request.
        - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
        - **source_code** (`str`): The raw source code of the entire function definition.
        - **imports** (`List[str]`): A list of import statements relevant to the function's context, potentially including those from the source file.
        - **context** (`FunctionContextInput`): Additional contextual information required for the function analysis, such as call graphs.
*   **Methods:**
    *No methods defined.*

---
#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to encapsulate structured contextual information for a method. It serves as a data schema to store details such as the method's unique identifier, a list of other functions or methods it calls, a list of where it is called from, its arguments, and its docstring. This model provides a standardized format for representing method-level context, which is crucial for analysis and processing within a larger system.
*   **Instantiation:** The specific instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The `__init__` method for `MethodContextInput` is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting keyword arguments that correspond to its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`. Pydantic handles the validation and assignment of these values, ensuring they conform to their specified types.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method.
        - **calls** (`List[str]`): A list of strings representing other methods, classes, or functions called by this method.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where this method is called from.
        - **args** (`List[str]`): A list of strings representing the arguments of the method.
        - **docstring** (`Optional[str]`): An optional string containing the method's docstring.
*   **Methods:**
    *No methods defined.*

---
#### Class: `ClassContextInput`
*   **Summary:** The `ClassContextInput` class is a Pydantic model designed to encapsulate structured context information relevant for analyzing a Python class. It serves as a data container, defining the expected structure for inputs related to class dependencies, instantiation points, and method-specific context. This model ensures that class analysis data adheres to a predefined schema.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within its definition.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ClassContextInput` is implicitly generated by Pydantic's `BaseModel`. It initializes an instance of the class by validating and assigning values to its fields: `dependencies`, `instantiated_by`, and `method_context` based on the provided input during object creation.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings, each representing an external dependency of the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of `CallInfo` objects, indicating the locations or contexts where the class being analyzed is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of `MethodContextInput` objects, providing specific context for each method within the class being analyzed.
*   **Methods:**
    *No methods defined.*

---
#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a schema for validating and organizing the data necessary to perform a detailed analysis of a Python class. This includes the analysis mode, the class identifier, its source code, associated import statements, and contextual information.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context, but it is typically instantiated when validating input for a class analysis operation, likely by a data processing or API endpoint.
*   **Dependencies:** This class relies on `pydantic.BaseModel` for its core functionality and `typing.Literal` and `typing.List` for type hinting, but does not explicitly list other external functional dependencies.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. It inherits from Pydantic's `BaseModel`, and its initialization is handled implicitly by Pydantic based on the declared fields, ensuring type validation and data structuring upon instantiation.
    *   *Parameters:*
        *Analysis data not available for this component.*
*   **Methods:**
    *No methods defined.*

---
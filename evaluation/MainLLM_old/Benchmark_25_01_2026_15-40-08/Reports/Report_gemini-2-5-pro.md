# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** This project is an automated documentation pipeline that analyzes Git repositories to generate comprehensive technical documentation. It clones a repository, performs static analysis to build an Abstract Syntax Tree (AST) and understand code relationships, then leverages a multi-LLM architecture to analyze code snippets and synthesize a final Markdown report. The system includes a Streamlit-based frontend for user interaction and database integration for managing users and analysis results.
- **Key Features:**
  - **Automated Git Repository Analysis:** Clones remote Git repositories and extracts file structures and content.
  - **Static Code Analysis:** Builds an Abstract Syntax Tree (AST) and analyzes call graphs and inter-file dependencies.
  - **Multi-LLM Architecture:** Uses specialized "Helper LLMs" for detailed code analysis and a "Main LLM" for synthesizing the final report.
  - **TOON Format Optimization:** Converts analysis data into the efficient TOON format for LLM processing, reducing token usage.
  - **Interactive Frontend:** Provides a Streamlit web interface for user authentication, repository input, and viewing generated documentation.
- **Tech Stack:** Python, Streamlit, LangChain, Pydantic, GitPython, NetworkX, Google Generative AI, OpenAI, Ollama.

*   **Repository Structure:**
    ```mermaid
    graph TD
      root["Repo Onboarding Agent 🚀"]
      
      root --> f1[".env.example"]
      root --> f2[".gitignore"]
      root --> d1["SystemPrompts/"]
      root --> f3["analysis_output.json"]
      root --> d2["backend/"]
      root --> d3["database/"]
      root --> d4["frontend/"]
      root --> d5["notizen/"]
      root --> f4["output.json"]
      root --> f5["output.toon"]
      root --> f6["readme.md"]
      root --> f7["requirements.txt"]
      root --> d6["result/"]
      root --> d7["schemas/"]
      root --> d8["statistics/"]
      root --> f8["test.json"]

      d1 --> d1_files["- SystemPromptClassHelperLLM.txt<br/>- SystemPromptFunctionHelperLLM.txt<br/>- SystemPromptHelperLLM.txt<br/>- SystemPromptMainLLM.txt<br/>- SystemPromptMainLLMToon.txt<br/>- SystemPromptNotebookLLM.txt"]
      d2 --> d2_files["- AST_Schema.py<br/>- File_Dependency.py<br/>- HelperLLM.py<br/>- MainLLM.py<br/>- __init__.py<br/>- basic_info.py<br/>- callgraph.py<br/>- converter.py<br/>- getRepo.py<br/>- main.py<br/>- relationship_analyzer.py<br/>- scads_key_test.py"]
      d3 --> d3_files["- db.py"]
      d4 --> d4_files["- .streamlit/config.toml<br/>- __init__.py<br/>- frontend.py<br/>- gifs/4j.gif"]
      d7 --> d7_files["- types.py"]
    ```

## 2. Installation
### Dependencies
To install the required dependencies, run the following command in your terminal:
`pip install -r requirements.txt`

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
```
### Setup Guide
1.  Clone the repository to your local machine.
2.  Navigate to the project directory.
3.  Install the required dependencies by running `pip install -r requirements.txt`.
4.  Create a `.env` file by copying the `.env.example` file: `cp .env.example .env`.
5.  Open the `.env` file and add your API keys for the desired LLM services (e.g., GEMINI_API_KEY, OPENAI_API_KEY).
6.  Start the application by running the frontend.

### Quick Startup
```bash
git clone https://github.com/your-username/repo-onboarding-agent.git
cd repo-onboarding-agent
pip install -r requirements.txt
cp .env.example .env
# Edit .env to add your API keys
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The primary use case of this application is to automatically generate technical documentation for a software project hosted on GitHub.

**Primary Commands:**

The application is run through a Streamlit web interface. The main command to start the server is:
```bash
streamlit run frontend/frontend.py
```
Once the application is running in your browser, you can:
1.  **Log in or Register:** The application uses a database to manage users and their API keys.
2.  **Configure API Keys:** In the settings, provide API keys for services like Google Gemini or OpenAI.
3.  **Analyze a Repository:**
    *   Enter the full URL of a public GitHub repository.
    *   Select the "Helper" and "Main" LLM models to use for the analysis.
    *   Click the "Generate" button to start the documentation pipeline.
4.  **Analyze Notebooks:**
    *   A separate workflow is available to specifically analyze Jupyter Notebooks (`.ipynb`) within a repository, including their code, markdown, and visual outputs.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added


## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is a specialized `ast.NodeVisitor` designed to traverse the Abstract Syntax Tree (AST) of Python code. Its primary purpose is to extract structured information about imports, classes, and functions within a given source file. It collects details such as identifiers, names, docstrings, and source code segments, organizing them into a hierarchical schema. The visitor uses an internal state (`_current_class`) to correctly associate methods with their parent classes during traversal.
*   **Instantiation:** This class is not explicitly listed as being instantiated by other components in the provided context.
*   **Dependencies:** This class does not have explicitly listed external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor instance with the raw source code, the file's absolute path, and the project's root directory. It calculates the module's fully qualified path and sets up an empty dictionary, `self.schema`, to store discovered imports, functions, and classes. It also initializes `_current_class` to `None` to track the current class context during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code content of the file being analyzed.
        - **file_path** (`str`): The absolute path to the Python file being visited.
        - **project_root** (`str`): The root directory of the project, used to determine module paths.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code, file_path, project_root)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **source_code** (`None`): None
            - **file_path** (`None`): None
            - **project_root** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method is invoked when an `ast.Import` node is encountered during AST traversal. It iterates through each alias defined in the import statement and appends the full name of the imported module to the `imports` list within the `self.schema` dictionary. After processing the import, it calls `self.generic_visit(node)` to ensure that any child nodes of the import statement (though rare for `ast.Import`) are also visited.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.Import`): The AST node representing an 'import module' statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.Import` node is encountered in the AST.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method is triggered upon encountering an `ast.ImportFrom` node, which represents a 'from module import name' statement. It processes each alias within the import, constructing a fully qualified import string (e.g., 'module.name') and adding it to the `imports` list in `self.schema`. Following this, `self.generic_visit(node)` is called to continue the traversal of the AST, ensuring all child nodes are processed.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ImportFrom` node is encountered in the AST.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions in the source code. It constructs a unique identifier for the class, extracts its name, docstring using `ast.get_docstring`, and its complete source code segment using `ast.get_source_segment`. This information, along with line numbers, is stored in a `class_info` dictionary and appended to the `classes` list in `self.schema`. The `_current_class` attribute is temporarily set to this `class_info` to provide context for any nested methods, and then reset to `None` after `self.generic_visit(node)` completes its traversal of the class's body.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `ast.get_docstring`, `ast.get_source_segment`, `self.generic_visit`
            - **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ClassDef` node is encountered in the AST.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, distinguishing between methods defined within a class and standalone functions. If `_current_class` is set, indicating the function is a method, its details (identifier, name, arguments, docstring, and line numbers) are appended to the `method_context` list of the current class. Otherwise, if it's a standalone function, its full details, including source code, are appended to the `functions` list in `self.schema`. Finally, `self.generic_visit(node)` is called to process any nested nodes within the function's body.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `ast.get_docstring`, `ast.get_source_segment`, `self.generic_visit`
            - **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.FunctionDef` node is encountered in the AST.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method is designed to handle `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Instead of duplicating logic, it simply delegates the processing of the async function node to the `visit_FunctionDef` method. This ensures that asynchronous functions are analyzed and stored in the schema in the same manner as regular synchronous functions, capturing their metadata and context.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.visit_FunctionDef`
            - **Called By:** This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.AsyncFunctionDef` node is encountered in the AST.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to perform static analysis on Python code within a repository. Its primary functions include parsing Python files to build an Abstract Syntax Tree (AST) schema and integrating call relationship data into this schema. It processes files, extracts structural information like functions, classes, and imports, and then enriches this data with details about how different code elements interact, including dependencies and call hierarchies.
*   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
*   **Dependencies:** The class depends on the 'ast' module for parsing Python code, the 'os' module for path manipulation, and 'getRepo.GitRepository' for repository interaction, although 'GitRepository' is only used as a type hint in the method signature. It also implicitly depends on an 'ASTVisitor' class for schema extraction.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It currently performs no specific setup or attribute initialization, simply passing.
    *   *Parameters:* *No parameters.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, )`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, raw_relationships)`
        *   *Description:* This method integrates call relationship data (incoming and outgoing calls) into a pre-existing full AST schema. It iterates through files, functions, and classes within the schema, populating their respective 'calls', 'called_by', and 'instantiated_by' contexts. Additionally, it identifies and lists external dependencies for each class based on method calls, ensuring the schema is enriched with interaction details.
        *   *Parameters:*
            - **self** (`None`): None
            - **full_schema** (`dict`): The comprehensive AST schema containing file, function, and class definitions to be updated.
            - **raw_relationships** (`dict`): A dictionary containing raw 'outgoing' and 'incoming' call relationships to be merged.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full AST schema with integrated relationship data.
        *   **Usage:**
            - **Calls:** This method retrieves 'outgoing' and 'incoming' data from 'raw_relationships' and accesses various nested dictionary and list elements within 'full_schema'.
            - **Called By:** This method is not explicitly called by other functions or methods in the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files, repo)`
        *   *Description:* This method processes a list of file objects from a Git repository to construct a full AST schema. It filters for Python files, parses their content using the 'ast' module, and then uses an 'ASTVisitor' to extract AST nodes (imports, functions, classes). The extracted schema for each file is then added to a 'full_schema' dictionary, handling potential parsing errors during the process.
        *   *Parameters:*
            - **self** (`None`): None
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though it's not directly used in the provided method body.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed repository, organized by file paths.
        *   **Usage:**
            - **Calls:** `os.path.commonpath`, `os.path.isfile`, `os.path.dirname`, `ast.parse`, and instantiates 'ASTVisitor'.
            - **Called By:** This method is not explicitly called by other functions or methods in the provided context.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to the project root. If the file is a Python file, it removes the '.py' extension. Subsequently, it replaces system path separators with dots to form the module path. Special handling is included for '__init__.py' files, where the '.__init__' suffix is removed to represent the package itself.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path for the given file.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends `ast.NodeVisitor` to analyze the Abstract Syntax Tree (AST) of a given Python file and identify its import dependencies. It constructs a dictionary mapping the analyzed file to a set of modules it imports. The class is capable of resolving both absolute and complex relative import statements, including checking for module files and symbols exported via `__init__.py` files within packages.
*   **Instantiation:** The class is not explicitly shown to be instantiated by other components in the provided context.
*   **Dependencies:** The class depends on `ast` module components such as `NodeVisitor`, `Import`, `ImportFrom`, `Assign`, `Name`, `FunctionDef`, `ClassDef`, `literal_eval`, `parse`, `walk`, `keyword.iskeyword`, `pathlib.Path`, and a custom function `get_all_temp_files`.
*   **Constructor:**
    *   *Description:* This constructor initializes the FileDependencyGraph instance with the path to the file being analyzed and the root directory of the repository. It sets these as instance attributes `self.filename` and `self.repo_root` respectively, providing the necessary context for dependency resolution.
    *   *Parameters:*
        - **filename** (`str`): The path to the Python file whose dependencies are to be analyzed.
        - **repo_root** (`str`): The root directory of the repository, used as a base for resolving file paths and imports.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename, repo_root)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **filename** (`None`): None
            - **repo_root** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This method is responsible for resolving relative import statements, such as `from .. import name1, name2`. It determines the correct base directory by traversing up the directory tree based on the import level specified in the AST node. It then checks if the imported names correspond to actual module files (e.g., `name.py`) or symbols explicitly exported by an `__init__.py` file within a package. If successful, it returns a list of resolved module or symbol names; otherwise, it raises an `ImportError`.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of successfully resolved module or symbol names.
        *   **Usage:**
            - **Calls:** `get_all_temp_files`, `pathlib.Path`, `Path.stem`, `Path.name`, `Path.parent`, `Path.resolve`, `Path.exists`, `Path.read_text`, `ast.parse`, `ast.walk`, `ast.literal_eval`, `keyword.iskeyword`
            - **Called By:** `visit_ImportFrom`
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method is a visitor function for `ast.Import` and `ast.ImportFrom` nodes. Its primary role is to record the identified import dependencies. It adds the imported module names (either from `base_name` if provided, or from the alias name in the node) to the `import_dependencies` dictionary, associating them with the current `self.filename`. After processing, it calls `self.generic_visit` to continue the AST traversal.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`Import | ImportFrom`): The AST node representing the import statement.
            - **base_name** (`str | None`): An optional base name for the module, typically used when the module part of a 'from ... import ...' statement has already been resolved.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** `visit_ImportFrom`
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method specifically handles `ast.ImportFrom` nodes, which represent 'from ... import ...' statements. If the import is absolute (i.e., `node.module` is present), it extracts the last component of the module name and passes it to `visit_Import`. If the import is relative (i.e., `node.module` is `None` and `node.level > 0`), it attempts to resolve the module names using the `_resolve_module_name` helper method. Any resolved base names are then passed to `visit_Import` to record the dependency. It includes error handling for `ImportError` during relative import resolution and calls `self.generic_visit`.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self._resolve_module_name`, `self.visit_Import`, `self.generic_visit`, `print`
            - **Called By:** This method is implicitly called by the `ast.NodeVisitor` mechanism when traversing the AST and encountering an `ImportFrom` node.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Abstract Syntax Tree (AST). It initializes a networkx.DiGraph and then utilizes a FileDependencyGraph visitor to traverse the provided AST, collecting import relationships. Finally, it populates the networkx.DiGraph with nodes for each file and edges indicating import dependencies based on the collected data.
*   **Parameters:**
    - **filename** (`str`): The name of the file whose dependencies are being analyzed.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to analyze for dependencies.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository, )`
*   **Description:** This function constructs a directed graph representing the call dependencies across all Python files within a given Git repository. It iterates through each Python file, parses its content into an Abstract Syntax Tree (AST), and then uses a helper function, `build_file_dependency_graph`, to create a dependency graph for that specific file. The nodes and edges from these individual file graphs are then aggregated into a single global NetworkX directed graph. This global graph ultimately illustrates how different functions and classes within the repository's Python codebase interact with each other.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to extract and analyze Python files for dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent functions or classes and edges represent call dependencies between them across the entire repository.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory, )`
*   **Description:** This function, `get_all_temp_files`, is responsible for identifying all Python files within a given directory and its subdirectories. It takes a string representing a directory path, converts it into an absolute `pathlib.Path` object, and then recursively searches for files ending with the ".py" extension. For each Python file found, its path is made relative to the initial root directory. The function then returns a list of these relative `pathlib.Path` objects.
*   **Parameters:**
    - **directory** (`str`): The string path to the root directory where the search for Python files should begin.
*   **Returns:**
    - **all_files** (`list[pathlib.Path]`): A list of `pathlib.Path` objects, each representing a Python file found within the specified directory, with paths relative to the input `directory`.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs), specifically designed for generating structured documentation for Python functions and classes. It abstracts away the complexities of LLM API interaction, including dynamic model selection (supporting Gemini, OpenAI, Ollama, and custom APIs), API key management, loading system prompts from files, and enforcing structured output validation using Pydantic schemas. The class is engineered to efficiently handle batch processing of documentation requests, incorporating built-in rate limiting and robust error handling to ensure reliable and scalable documentation generation.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** The class depends on external libraries for LLM interaction (`langchain_google_genai`, `langchain_ollama`, `langchain_openai`), message formatting (`langchain.messages`), JSON serialization (`json`), logging (`logging`), time management (`time`), and Pydantic schemas for structured input/output (`schemas.types`).
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by setting up API keys and loading system prompts from specified file paths for both function and class analysis. It dynamically configures the appropriate LLM client (Gemini, OpenAI, custom API, or Ollama) based on the provided `model_name` and `base_url`. Crucially, it wraps these clients to enforce structured output using `FunctionAnalysis` and `ClassAnalysis` Pydantic schemas, and also calls a private method to configure an internal batch size.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt that guides the LLM for function analysis tasks.
        - **class_prompt_path** (`str`): The file path to the system prompt that guides the LLM for class analysis tasks.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, such as those for Ollama or other OpenAI-compatible APIs.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, function_prompt_path, class_prompt_path, model_name, base_url)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **api_key** (`None`): None
            - **function_prompt_path** (`None`): None
            - **class_prompt_path** (`None`): None
            - **model_name** (`None`): None
            - **base_url** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private helper method dynamically sets the `batch_size` attribute for the LLMHelper instance based on the provided `model_name`. It uses a series of conditional checks to assign specific batch sizes tailored for various Gemini, Llama, and GPT models, as well as custom or open-source models, aiming to optimize for API rate limits and processing efficiency. If the specified model name is not recognized, it logs a warning and defaults to a conservative batch size of 2 to prevent potential issues.
        *   *Parameters:*
            - **self** (`None`): None
            - **model_name** (`str`): The name of the LLM model for which the batch processing settings need to be configured.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods or functions within its body, beyond standard Python operations.
            - **Called By:** `__init__`
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates structured documentation for a batch of functions by interacting with the configured LLM. It takes a list of `FunctionAnalysisInput` objects, serializes each into a JSON payload, and constructs a list of conversations, each paired with the `function_system_prompt`. These conversations are then processed by the LLM in batches, with `WAITING_TIME` delays introduced between batches to adhere to API rate limits. The method collects the `FunctionAnalysis` results, extending the list with `None` for any items that encounter errors during processing.
        *   *Parameters:*
            - **self** (`None`): None
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of `FunctionAnalysisInput` objects, each containing the necessary data for analyzing a single function.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, where each object represents the structured documentation for a function, or `None` if an error occurred during its generation.
        *   **Usage:**
            - **Calls:** `json.dumps`, `SystemMessage`, `HumanMessage`, `self.function_llm.batch`, `logging.info`, `logging.error`, `time.sleep`
            - **Called By:** The input context does not specify explicit callers for this method, suggesting it may be an external entry point or called dynamically.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating structured documentation for a batch of classes using the LLM configured specifically for class analysis. It processes a list of `ClassAnalysisInput` objects, converting them into JSON payloads and preparing them as LLM conversations, each utilizing the class-specific system prompt. The conversations are then sent to the LLM in batches, with built-in mechanisms for managing concurrency and respecting API rate limits. The method collects the validated `ClassAnalysis` results, handling potential errors by inserting `None` into the result list for any failed items to maintain order.
        *   *Parameters:*
            - **self** (`None`): None
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of `ClassAnalysisInput` objects, each containing the necessary data for analyzing a single class.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, where each object represents the structured documentation for a class, or `None` if an error occurred during its generation.
        *   **Usage:**
            - **Calls:** `json.dumps`, `SystemMessage`, `HumanMessage`, `self.class_llm.batch`, `logging.info`, `logging.error`, `time.sleep`
            - **Called By:** The input context does not specify explicit callers for this method, suggesting it may be an external entry point or called dynamically.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a testing orchestrator for the LLMHelper class, defining dummy data for function and class analysis inputs. It simulates the process of generating documentation by creating pre-computed analysis objects, initializing an LLMHelper instance, and then invoking the `generate_for_functions` method. Finally, it processes the results and prints the aggregated documentation in JSON format.
*   **Parameters:** *No parameters.*
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a versatile interface for interacting with various large language models, abstracting away the specifics of different LLM providers. It handles the initialization of the LLM client based on the model name, loads a system prompt for consistent behavior, and provides both synchronous (call_llm) and asynchronous streaming (stream_llm) methods for communication. This class centralizes LLM interaction logic, making it easier to switch between models and manage prompts.
*   **Instantiation:** The class is not explicitly instantiated by any other components within the provided context.
*   **Dependencies:** The class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by validating the API key, loading a system prompt from a specified file, and configuring an appropriate LLM client (Google Generative AI, OpenAI-compatible, or Ollama) based on the provided model name and optional base URL. It sets up self.system_prompt, self.model_name, and self.llm for subsequent interactions.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM provider.
        - **prompt_file_path** (`str`): The file path to the system prompt that will guide the LLM's behavior.
        - **model_name** (`str`): The name of the language model to use, defaulting to 'gemini-2.5-pro'. This determines which LLM client is initialized.
        - **base_url** (`str`): An optional base URL for custom LLM endpoints, particularly for Ollama or other OpenAI-compatible services.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, prompt_file_path, model_name, base_url)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **api_key** (`None`): None
            - **prompt_file_path** (`None`): None
            - **model_name** (`None`): None
            - **base_url** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method sends a single user input to the initialized LLM. It constructs a list of messages including the system prompt and the user's query, then invokes the self.llm client to get a response. The method logs the process and returns the content of the LLM's reply, or None if an error occurs during the call.
        *   *Parameters:*
            - **self** (`None`): None
            - **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:*
            - **content** (`str`): The textual content of the LLM's response.
            - **None** (`None`): Returns None if an error occurs during the LLM call.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other functions or methods from the provided context.
            - **Called By:** This method is not explicitly called by other functions or methods from the provided context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method provides a streaming interface to the LLM, allowing for real-time reception of responses. It prepares the system and human messages, then initiates a stream from the self.llm client. The method yields each content chunk as it arrives and handles potential errors by yielding an error message.
        *   *Parameters:*
            - **self** (`None`): None
            - **user_input** (`str`): The user's query or message for which a streaming response is desired.
        *   *Returns:*
            - **chunk.content** (`str`): Yields individual content chunks from the LLM's streaming response.
            - **error_message** (`str`): Yields an error message string if an exception occurs during the streaming process.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other functions or methods from the provided context.
            - **Called By:** This method is not explicitly called by other functions or methods from the provided context.

---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to systematically extract core project information from common project files such as README.md, pyproject.toml, and requirements.txt. It initializes a structured dictionary to hold project details, which are then populated by parsing these files in a prioritized manner. The class provides methods for cleaning content, finding specific files, extracting Markdown sections, and parsing different file types, ultimately consolidating all available information into a comprehensive project overview.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** The class relies on the re module for regular expression operations, the os module for path manipulation, and the tomllib module for parsing TOML files. It also uses typing for type hints.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjektInfoExtractor instance. It sets a constant `INFO_NICHT_GEFUNDEN` for placeholder values and creates a nested dictionary `self.info` to store extracted project details. This `info` dictionary is pre-populated with "Information not found" for all expected fields, ensuring a consistent structure.
    *   *Parameters:* *No parameters.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, )`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content)`
        *   *Description:* This private helper method is responsible for sanitizing string content by removing null bytes (\x00). Null bytes can appear due to incorrect encoding assumptions, such as reading UTF-16 encoded files as UTF-8. The method checks if the input content is empty and returns an empty string if so; otherwise, it performs the replacement.
        *   *Parameters:*
            - **self** (`None`): None
            - **content** (`str`): The string content to be cleaned.
        *   *Returns:*
            - **None** (`str`): The cleaned string content, free of null bytes.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods or functions within its body.
            - **Called By:** `_parse_readme`, `_parse_toml`, `_parse_requirements`
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches a list of file-like objects for a file whose path matches any of the provided patterns. The search is case-insensitive, comparing the lowercased file path ending with a lowercased pattern. It iterates through each file and each pattern, returning the first matching file object found or None if no match is made.
        *   *Parameters:*
            - **self** (`None`): None
            - **patterns** (`List[str]`): A list of string patterns (e.g., file extensions or names) to search for.
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have a `path` attribute.
        *   *Returns:*
            - **None** (`Optional[Any]`): The first file-like object that matches a pattern, or None if no matching file is found.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods or functions within its body.
            - **Called By:** `extrahiere_info`
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private method extracts content from a Markdown string that appears under a level 2 heading (##). It takes the Markdown content and a list of keywords. It constructs a regular expression to find a heading matching any of the keywords (case-insensitive) and then captures all text following that heading until the next level 2 heading or the end of the document.
        *   *Parameters:*
            - **self** (`None`): None
            - **inhalt** (`str`): The Markdown content string to parse.
            - **keywords** (`List[str]`): A list of keywords to match against Markdown section headers.
        *   *Returns:*
            - **None** (`Optional[str]`): The extracted section content as a string, or None if no matching section is found.
        *   **Usage:**
            - **Calls:** `re.escape`, `re.compile`, `re.search`
            - **Called By:** `_parse_readme`
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This method parses the content of a README file to extract various project information. It first cleans the content using _clean_content. It then attempts to extract the project title from a level 1 Markdown heading, a general description, and specific sections like "Key Features", "Tech Stack", "Status", "Setup Instructions", and "Quick Start Guide" using _extrahiere_sektion_aus_markdown. Extracted information updates the self.info dictionary, prioritizing existing values if they are not the INFO_NICHT_GEFUNDEN placeholder.
        *   *Parameters:*
            - **self** (`None`): None
            - **inhalt** (`str`): The raw content of the README file.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `_clean_content`, `_extrahiere_sektion_aus_markdown`, `re.search`
            - **Called By:** `extrahiere_info`
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This method parses the content of a pyproject.toml file. It first cleans the input content using _clean_content. It then checks if the tomllib module is available, printing a warning and returning if not. If tomllib is present, it attempts to load the TOML content, extracting the project name, description, and dependencies from the [project] section and updating self.info. It includes error handling for TOMLDecodeError.
        *   *Parameters:*
            - **self** (`None`): None
            - **inhalt** (`str`): The raw content of the pyproject.toml file.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `_clean_content`, `tomllib.loads`, `print`
            - **Called By:** `extrahiere_info`
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This method parses the content of a requirements.txt file. It first cleans the input content using _clean_content. It then extracts dependencies by splitting the content into lines, filtering out empty lines and comments (lines starting with '#'). The extracted dependencies are stored in self.info["installation"]["dependencies"], but only if this field has not already been populated (i.e., it still holds the INFO_NICHT_GEFUNDEN placeholder).
        *   *Parameters:*
            - **self** (`None`): None
            - **inhalt** (`str`): The raw content of the requirements.txt file.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `_clean_content`
            - **Called By:** `extrahiere_info`
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This is the main public method that orchestrates the extraction of project information. It first identifies relevant project files (README, pyproject.toml, requirements.txt) from a list of file-like objects using _finde_datei. It then parses these files in a prioritized order: pyproject.toml first, then requirements.txt, and finally README.md, allowing later parsers to fill in gaps or provide supplementary details. After parsing, it formats the dependencies and derives a project title from the repo_url if no title was found elsewhere.
        *   *Parameters:*
            - **self** (`None`): None
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have `path` and `content` attributes.
            - **repo_url** (`str`): The URL of the repository, used as a fallback to derive the project title.
        *   *Returns:*
            - **info** (`Dict[str, Any]`): A dictionary containing all extracted project information, structured into "projekt_uebersicht" and "installation" sections.
        *   **Usage:**
            - **Calls:** `_finde_datei`, `_parse_toml`, `_parse_requirements`, `_parse_readme`, `os.path.basename`, `str.removesuffix`
            - **Called By:** This method is an entry point and is not explicitly called by other methods within the provided context.

---
### File: `backend/callgraph.py`
#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an ast.NodeVisitor designed to construct a directed call graph for a given Python source file. It systematically traverses the Abstract Syntax Tree (AST) of the file, identifying function and class definitions, import statements, and function calls. By tracking context such as the current class and function, and resolving names through local definitions and import mappings, it builds a comprehensive representation of inter-function dependencies within the file.
*   **Instantiation:** This class is not explicitly instantiated by any known components in the provided context.
*   **Dependencies:** The CallGraph class depends on the 'ast' module for parsing Python source code and the 'networkx' library for graph manipulation.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph instance by setting up the filename, current context trackers (current_function, current_class), and various data structures essential for building the call graph. These structures include local_defs for tracking local definitions, a networkx.DiGraph for the graph itself, import_mapping for resolving imports, function_set for unique function names, and edges to store call relationships.
    *   *Parameters:*
        - **filename** (`str`): The path to the Python file being analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filename)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **filename** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively traverses Abstract Syntax Tree (AST) nodes to extract the full dotted name components of a function or attribute call. It handles ast.Call, ast.Name, and ast.Attribute nodes to build a list representing the hierarchical path of the called entity.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.AST`): The AST node to process, typically an ast.Call, ast.Name, or ast.Attribute.
        *   *Returns:*
            - **None** (`list[str]`): A list of string components representing the dotted name of the called entity (e.g., ['pkg', 'mod', 'Class', 'method']).
        *   **Usage:**
            - **Calls:** This method recursively calls itself to traverse the AST node structure.
            - **Called By:** `visit_Call`
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This method takes a list of potential callee name components and attempts to resolve them to their fully qualified names. It prioritizes local definitions, then checks the import_mapping for imported modules/functions, and finally constructs a full name based on the current file and class context if no other resolution is found.
        *   *Parameters:*
            - **self** (`None`): None
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains string components of a potential callee's name.
        *   *Returns:*
            - **None** (`list[str]`): A list of fully resolved, qualified names for the callees.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods within the class but accesses self.local_defs and self.import_mapping.
            - **Called By:** `visit_Call`
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* This helper method constructs a fully qualified name for a given base name, incorporating the filename and an optional class name. This ensures that functions and methods are uniquely identified within the context of the file and class they belong to.
        *   *Parameters:*
            - **self** (`None`): None
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`str | None`): The name of the class if the entity is a method, otherwise None.
        *   *Returns:*
            - **None** (`str`): The fully qualified name (e.g., filename::ClassName::methodName or filename::functionName).
        *   **Usage:**
            - **Calls:** This method does not call any other methods.
            - **Called By:** `visit_FunctionDef`
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self, )`
        *   *Description:* This method determines the identifier of the currently active caller. If a function is being visited (self.current_function is set), that function's full name is returned. Otherwise, it returns a placeholder indicating the global scope of the current file.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **None** (`str`): The fully qualified name of the current function or a string representing the global scope.
        *   **Usage:**
            - **Calls:** This method does not call any other methods.
            - **Called By:** `visit_Call`
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method overrides the ast.NodeVisitor's visit_Import to process import statements. It extracts the module names and their aliases, then populates the self.import_mapping dictionary to track how modules are referenced. After processing, it calls generic_visit to continue traversing the AST.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.Import`): The ast.Import node representing an import statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is implicitly called by the ast.NodeVisitor mechanism when an ast.Import node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method overrides the ast.NodeVisitor's visit_ImportFrom to handle from ... import ... statements. It extracts the module name and the imported names (and their aliases), then updates self.import_mapping to correctly resolve these imported entities to their source module.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.ImportFrom`): The ast.ImportFrom node representing a 'from ... import ...' statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods within the class.
            - **Called By:** This method is implicitly called by the ast.NodeVisitor mechanism when an ast.ImportFrom node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method overrides ast.NodeVisitor's visit_ClassDef to manage the context of class definitions. It saves the current class context, sets the new class as current_class, performs a generic visit to process the class's body (including methods), and then restores the previous class context upon exit.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.ClassDef`): The ast.ClassDef node representing a class definition.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is implicitly called by the ast.NodeVisitor mechanism when an ast.ClassDef node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method processes ast.FunctionDef nodes to identify and record function definitions. It constructs a fully qualified name for the function, stores it in local_defs, adds the function as a node to the call graph, sets it as the current_function for nested calls, and then performs a generic visit before restoring the previous function context.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.FunctionDef`): The ast.FunctionDef node representing a function definition.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self._make_full_name`, `self.graph.add_node`, `self.generic_visit`
            - **Called By:** `visit_AsyncFunctionDef`
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method handles ast.AsyncFunctionDef nodes, which represent asynchronous function definitions. It delegates the processing directly to visit_FunctionDef, ensuring that asynchronous functions are treated similarly to regular functions for the purpose of call graph construction.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.AsyncFunctionDef`): The ast.AsyncFunctionDef node representing an asynchronous function definition.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.visit_FunctionDef`
            - **Called By:** This method is implicitly called by the ast.NodeVisitor mechanism when an ast.AsyncFunctionDef node is encountered during AST traversal.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method processes ast.Call nodes to detect and record function calls. It identifies the caller using _current_caller, extracts the callee's name components using _recursive_call, resolves these names with _resolve_all_callee_names, and then adds the call relationship as an edge to the self.edges dictionary.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.Call`): The ast.Call node representing a function call.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self._current_caller`, `self._recursive_call`, `self._resolve_all_callee_names`, `self.generic_visit`
            - **Called By:** This method is implicitly called by the ast.NodeVisitor mechanism when an ast.Call node is encountered during AST traversal.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method processes ast.If nodes, with special handling for the if __name__ == "__main__" block. For this specific block, it temporarily sets the current_function to <main_block> to correctly attribute calls within the main execution entry point. For all other if statements, it performs a standard generic visit.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.If`): The ast.If node representing an if statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is implicitly called by the ast.NodeVisitor mechanism when an ast.If node is encountered during AST traversal.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function takes a NetworkX directed graph and an output file path, then generates a DOT file representation of the graph. It first creates a copy of the input graph and renames its nodes to generic, safe identifiers (e.g., "n0", "n1") to prevent issues with special characters in the DOT format. The original node names are preserved by assigning them as 'label' attributes to the new safe nodes. Finally, the modified graph, with its safe node identifiers and original labels, is written to the specified output path as a DOT file.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph to be processed and written to a DOT file.
    - **out_path** (`str`): The file path where the safe DOT representation of the graph will be saved.
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo, )`
*   **Description:** This function constructs a directed call graph for a given Git repository. It first identifies all Python files within the repository and parses their Abstract Syntax Trees (ASTs) to determine a set of 'self-written' functions. Subsequently, it iterates through these parsed files again to detect call relationships between functions. An edge is added to the resulting networkx.DiGraph only if both the calling and the called function are part of the identified 'self-written' set. The function ultimately returns this filtered call graph.
*   **Parameters:**
    - **repo** (`GitRepository`): The GitRepository object representing the repository to analyze.
*   **Returns:**
    - **global_graph** (`networkx.DiGraph`): A directed graph representing the call relationships between self-written functions within the repository.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/converter.py`
#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content, )`
*   **Description:** This function, `wrap_cdata`, is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string by prepending "<![CDATA[\n" and appending "\n]]>" to the input content. This process ensures that the enclosed content is treated as character data by an XML parser, preventing interpretation of special characters within it.
*   **Parameters:**
    - **content** (`str`): The string content that needs to be wrapped inside CDATA tags to be treated as raw character data in XML.
*   **Returns:**
    - **wrapped_content** (`str`): A new string where the original content is enclosed within CDATA tags (e.g., "<![CDATA[\n{content}\n]]>").
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs, image_list)`
*   **Description:** This function processes a list of notebook output objects to extract their content, primarily text and images. It iterates through each output, categorizing it by type. For display data or execution results, it prioritizes extracting PNG or JPEG images, converting them into an XML-like placeholder and storing their Base64 data in a provided list. If no image is found, it extracts plain text. Stream outputs are appended as raw text, and error outputs are formatted as 'ename: evalue'. The function ultimately returns a list of these extracted text snippets or image placeholders.
*   **Parameters:**
    - **outputs** (`list of Output objects`): A list of output objects, typically from notebook execution, containing various types of data like text, images, or errors.
    - **image_list** (`list`): A list used to store dictionaries of image data (mime_type and Base64 string) as they are encountered and processed, modified in place.
*   **Returns:**
    - **extracted_xml_snippets** (`list of str`): A list containing extracted text content, error messages, or XML-formatted image placeholders for images found within the outputs.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type, )`
*   **Description:** This function, process_image, takes a mime_type as input and attempts to process base64 encoded image data. It checks if the provided mime_type exists as a key in an externally accessible 'data' dictionary. If found, it retrieves the corresponding base64 string, removes newline characters, and then appends a dictionary containing the mime_type and cleaned base64 data to an externally accessible 'image_list'. Upon successful processing, it returns a formatted string acting as an image placeholder. The function includes error handling for any exceptions during this process, returning an error message string. If the mime_type is not found in the 'data' dictionary, the function returns None.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type of the image to be processed, used to retrieve its corresponding base64 data from an external 'data' dictionary.
*   **Returns:**
    - **result** (`str | None`): Returns a formatted string representing an image placeholder upon successful processing, an error message string if an exception occurs during base64 decoding, or None if the mime_type is not found in the external 'data' dictionary.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content, )`
*   **Description:** This function takes the raw content of a Jupyter notebook as a string and converts it into a structured XML representation. It parses the notebook cells, categorizing them as markdown, code, or output, and wraps their content in appropriate XML tags. The function also extracts any images found within the code cell outputs. In case of a parsing error (e.g., if the input is not valid JSON/Notebook format), it returns an error message.
*   **Parameters:**
    - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a JSON string.
*   **Returns:**
    - **xml_output** (`str`): The converted notebook content in XML format, or an error message if parsing failed.
    - **extracted_images** (`list`): A list of extracted image data or paths from the notebook outputs.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files, )`
*   **Description:** This function processes a list of repository files to identify and convert Jupyter notebooks. It filters the input list to find files with a '.ipynb' extension. For each identified notebook, it logs the processing, calls an external conversion utility to transform the notebook's content into XML and extract images. The results, including the XML output and image data, are stored in a dictionary keyed by the notebook's file path.
*   **Parameters:**
    - **repo_files** (`List[object]`): A list of objects, each representing a file from a repository. Each object is expected to have a 'path' attribute (string) ending with '.ipynb' and a 'content' attribute (string) containing the file's raw data.
*   **Returns:**
    - **conversion_results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the paths of the processed notebook files (string) and values are dictionaries. Each inner dictionary contains the 'xml' output (string) and any extracted 'images' data (which is itself a dictionary or list) generated from the notebook conversion.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** The RepoFile class is designed to represent a single file within a Git repository, offering a robust abstraction for accessing file metadata and content. It employs a lazy loading mechanism for its Git blob object, content, and size, optimizing performance by deferring resource-intensive operations until data is actually required. The class provides properties for accessing these attributes and includes utility methods like `analyze_word_count` for content analysis and `to_dict` for serialization into a dictionary format.
*   **Instantiation:** This class is not explicitly instantiated by any other components within the provided context.
*   **Dependencies:** This class does not have any explicit external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This method initializes a RepoFile object by storing the file path and the Git Tree object from which the file originates. It also sets up internal attributes such as `_blob`, `_content`, and `_size` to `None`, preparing them for lazy loading upon first access.
    *   *Parameters:*
        - **file_path** (`str`): Der Pfad zur Datei innerhalb des Repositories.
        - **commit_tree** (`git.Tree`): Das Tree-Objekt des Commits, aus dem die Datei stammt.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, file_path, commit_tree)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **file_path** (`None`): None
            - **commit_tree** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`blob`**
        *   *Signature:* `def blob(self, )`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if `_blob` is already loaded; if not, it attempts to retrieve the blob from the `_tree` using the stored `path`. If the file is not found in the commit tree, a `FileNotFoundError` is raised to indicate the missing file.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other functions or methods.
            - **Called By:** This method is not explicitly called by any other methods within the provided context.
    *   **`content`**
        *   *Signature:* `def content(self, )`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It first ensures the `blob` property is loaded to access the Git blob. Then, it reads the data stream from the blob, decodes it using UTF-8 with error ignoring, and stores the result. The decoded string content of the file is then returned.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other functions or methods.
            - **Called By:** This method is not explicitly called by any other methods within the provided context.
    *   **`size`**
        *   *Signature:* `def size(self, )`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the `_size` attribute is already loaded; if not, it accesses the `size` attribute of the `blob` property to retrieve the file's size. The retrieved size is then stored internally and returned as an integer.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other functions or methods.
            - **Called By:** This method is not explicitly called by any other methods within the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self, )`
        *   *Description:* This method serves as an example analysis method, designed to count the words within the file's content. It retrieves the file content via the `content` property, splits it into words using whitespace as a delimiter, and then returns the total count of these words.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **word_count** (`int`): The total number of words found in the file content.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other functions or methods.
            - **Called By:** This method is not explicitly called by any other methods within the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self, )`
        *   *Description:* This special method provides a concise and informative string representation of the `RepoFile` object, primarily for debugging and logging purposes. It constructs a string that includes the class name and the file's path, making it easy to identify the object's state when printed or inspected.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, showing its path.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other functions or methods.
            - **Called By:** This method is not explicitly called by any other methods within the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method serializes the `RepoFile` object into a dictionary format, providing key metadata about the file. It includes the file's path, its base name, its size, and a fixed type "file". An optional `include_content` parameter allows for the file's actual content to be added to the dictionary if needed.
        *   *Parameters:*
            - **self** (`None`): None
            - **include_content** (`bool`): A boolean flag that, when true, includes the file's content in the returned dictionary. Defaults to false.
        *   *Returns:*
            - **file_data** (`dict`): A dictionary containing the file's path, name, size, type, and optionally its content.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other functions or methods.
            - **Called By:** This method is not explicitly called by any other methods within the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with a Git repository. It handles the cloning of a remote repository into a temporary local directory, ensuring proper cleanup through its context manager implementation. The class allows for retrieving all files within the repository as RepoFile objects and can generate a hierarchical tree structure of these files, optionally including their content. It centralizes repository management, making it easier to access and process repository contents.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** The class depends on `tempfile` for temporary directory creation, `git.Repo` and `git.GitCommandError` for Git operations, and `logging` for informational messages. It also implicitly depends on `RepoFile` which is used in `get_all_files` and `get_file_tree`.
*   **Constructor:**
    *   *Description:* Initializes the GitRepository by setting the repository URL, creating a temporary directory, and cloning the Git repository into it. It captures the latest commit and its tree, handling potential cloning errors by cleaning up the temporary directory and raising a RuntimeError.
    *   *Parameters:*
        - **repo_url** (`string`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, repo_url)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **repo_url** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self, )`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It uses `git.ls_files()` to get file paths, then creates `RepoFile` objects for each path, associating them with the current commit tree. The generated list of `RepoFile` objects is stored internally in `self.files` and then returned.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **None** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:**
            - **Calls:** `self.repo.git.ls_files()`, `RepoFile`
            - **Called By:** `get_file_tree`
    *   **`close`**
        *   *Signature:* `def close(self, )`
        *   *Description:* This method is responsible for cleaning up resources by deleting the temporary directory where the Git repository was cloned. It checks if `self.temp_dir` is set before attempting to delete it, and then sets `self.temp_dir` to `None` to prevent further cleanup attempts.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods or functions beyond standard Python operations like `print`.
            - **Called By:** `__init__`, `__exit__`
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self, )`
        *   *Description:* This method makes the `GitRepository` class compatible with the context manager protocol. When the `with` statement is entered, this method is called and simply returns the instance of the `GitRepository` itself, allowing it to be assigned to a variable in the `as` clause.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **None** (`GitRepository`): The instance of the GitRepository itself.
        *   **Usage:**
            - **Calls:** This method does not call any other methods or functions.
            - **Called By:** This method is implicitly called when the `GitRepository` object is used in a `with` statement.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This method is part of the context manager protocol and is automatically called when exiting a `with` statement block. Its primary responsibility is to ensure that the `close()` method is invoked, thereby cleaning up the temporary repository directory, regardless of whether an exception occurred within the `with` block.
        *   *Parameters:*
            - **self** (`None`): None
            - **exc_type** (`type`): The type of the exception that caused the `with` block to be exited, or `None` if no exception occurred.
            - **exc_val** (`Exception`): The exception instance that caused the `with` block to be exited, or `None`.
            - **exc_tb** (`traceback`): The traceback object associated with the exception, or `None`.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.close()`
            - **Called By:** This method is implicitly called when exiting a `with` statement block using the `GitRepository` object.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* This method constructs a hierarchical tree representation of the files within the Git repository. If `self.files` is not already populated, it first calls `get_all_files()` to retrieve them. It then iterates through these files, splitting their paths to build a nested dictionary structure representing directories and files. Each file is converted to a dictionary using `file_obj.to_dict()`, optionally including its content.
        *   *Parameters:*
            - **self** (`None`): None
            - **include_content** (`bool`): A flag indicating whether the content of each file should be included in its dictionary representation. Defaults to `False`.
        *   *Returns:*
            - **None** (`dict`): A dictionary representing the file tree structure, with 'name', 'type', and 'children' keys for directories, and file details for files.
        *   **Usage:**
            - **Calls:** `self.get_all_files()`, `file_obj.to_dict()`
            - **Called By:** This method is not explicitly called by other methods within the provided class definition.

---
### File: `backend/main.py`
#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare the number of JSON tokens and TOON tokens. It calculates and displays the token counts, along with a savings percentage, in a graphical format. The chart includes a title, y-axis label, grid, and displays the exact token values above each bar. Finally, the generated chart is saved to a specified output file path.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens for the JSON format.
    - **toon_tokens** (`int`): The number of tokens for the TOON format.
    - **savings_percent** (`float`): The calculated percentage of savings between the two token counts.
    - **output_path** (`str`): The file path where the generated chart image will be saved.
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the effective processing time by subtracting estimated sleep times, which are introduced due to rate limits for 'gemini-' models, from the total elapsed duration. It first determines the total duration between a start and end time. If the model name does not start with 'gemini-', it returns the total duration directly. Otherwise, it calculates the number of batches and corresponding sleep intervals, assuming 61 seconds per sleep, and then subtracts this total sleep time from the overall duration to yield the net processing time.
*   **Parameters:**
    - **start_time** (`datetime.datetime | float`): The starting timestamp of the operation.
    - **end_time** (`datetime.datetime | float`): The ending timestamp of the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed per batch.
    - **model_name** (`str`): The name of the model used, which determines if sleep times are considered for rate limiting.
*   **Returns:**
    - **net_time** (`float`): The calculated net processing time, excluding estimated sleep times for rate limits, or the total duration if the model is not 'gemini-'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive process to analyze a GitHub repository and generate a detailed report. It begins by extracting API keys and model configurations, then validates the input for a valid GitHub URL. The function proceeds to clone the repository, extract basic project information, construct a file tree, and perform relationship analysis. It then builds and enriches an Abstract Syntax Tree (AST) schema with the gathered relationship data. Subsequently, it prepares and dispatches inputs to a 'Helper LLM' for detailed analysis of individual functions and classes. Finally, it prepares the aggregated data for a 'Main LLM', performs token evaluation, calls the Main LLM to generate a final report, and saves the report along with performance metrics and a token savings chart.
*   **Parameters:**
    - **input** (`str`): The user input, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs ('scadsllm_base_url', 'ollama').
    - **model_names** (`dict`): A dictionary specifying the names of the helper and main LLM models to be used (e.g., 'helper', 'main').
    - **status_callback** (`None`): An optional callback function used to provide status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM.
    - **metrics** (`dict`): A dictionary containing performance metrics such as helper_time, main_time, total_time, model names, and token savings data.
*   **Usage:**
    - **Calls:** `update_status`, `logging.info`, `api_keys.get`, `model_names.get`, `re.search`, `match.group`, `GitRepository`, `repo.get_all_files`, `repo.temp_dir`, `logging.error`, `ProjektInfoExtractor`, `info_extractor.extrahiere_info`, `repo.get_file_tree`, `ProjectAnalyzer`, `rel_analyzer.analyze`, `rel_analyzer.get_raw_relationships`, `ASTAnalyzer`, `ast_analyzer.analyze_repository`, `ast_analyzer.merge_relationship_data`, `file_data.get`, `ast_nodes.get`, `function.get`, `context.get`, `FunctionContextInput`, `FunctionAnalysisInput`, `_class.get`, `method.get`, `MethodContextInput`, `ClassContextInput`, `ClassAnalysisInput`, `LLMHelper`, `os.environ.__setitem__`, `time.time`, `llm_helper.generate_for_functions`, `calculate_net_time`, `doc.identifier`, `doc.model_dump`, `llm_helper.model_name.startswith`, `time.sleep`, `llm_helper.generate_for_classes`, `json.dumps`, `encode`, `estimate_savings`, `MainLLM`, `main_llm.model_name`, `main_llm.call_llm`, `os.makedirs`, `datetime.now`, `datetime.strftime`, `os.path.join`, `create_savings_chart`, `report_filename.replace`
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_status`
*   **Signature:** `def update_status(msg, )`
*   **Description:** This function, `update_status`, is designed to handle and log status messages. It takes a single message as input. The function first checks if a `status_callback` function is available and, if so, invokes it with the provided message. Regardless of the callback's presence, it then logs the message using the `logging.info` facility.
*   **Parameters:**
    - **msg** (`str`): The status message to be processed and logged.
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback)`
*   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks within a GitHub repository using a Language Model (LLM). It begins by extracting a repository URL from the input, cloning the repository, and then processing its notebook files. It extracts basic project information and converts notebooks into an XML-like structure, handling embedded images by encoding them in base64. The function dynamically selects an LLM based on the provided model name and API keys, then iterates through each processed notebook, generating a specific payload for the LLM and requesting a report. Finally, it concatenates all individual notebook reports, saves the comprehensive report to a markdown file with a timestamp, and returns the final report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): A string containing the GitHub repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
    - **model** (`str`): The name of the LLM model to be used for analysis (e.g., 'gpt-4', 'gemini-pro', 'alias-model').
    - **status_callback** (`callable | None`): An optional callback function to provide status updates during the workflow execution. If provided, it receives a string message.
*   **Returns:**
    - **result** (`dict`): A dictionary containing the 'report' (the concatenated markdown string of all notebook analyses) and 'metrics' (a dictionary of performance statistics like total time and model used).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by other functions in the provided context.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function `gemini_payload` constructs a multi-part content payload designed for the Gemini API. It integrates basic project information, the current notebook path, structured XML content, and a list of image data. The process involves serializing initial context into a JSON string and then parsing the XML content to interleave text segments with base64 encoded image URLs. The function dynamically builds a list of dictionaries, where each dictionary represents either a text part or an image part, ensuring all content is correctly formatted for the Gemini API.
*   **Parameters:**
    - **basic_info** (`Any`): Contains general information about the project or context, which will be serialized into JSON.
    - **nb_path** (`str`): The file path of the current notebook, also included in the initial JSON context.
    - **xml_content** (`str`): The XML content of the notebook, which may contain `<IMAGE_PLACEHOLDER/>` tags that need to be replaced with actual image data.
    - **images** (`list`): A list of image data objects. Each object is expected to be a dictionary containing at least a 'data' key with a base64 encoded string and potentially other metadata like 'mime_type'.
*   **Returns:**
    - **payload_content** (`list`): A list of dictionaries, where each dictionary represents a content part (either 'text' or 'image_url') formatted for a Gemini API request.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/relationship_analyzer.py`
#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform static analysis on a Python project to build a comprehensive call graph. It achieves this by first discovering all Python files, then parsing them to collect definitions of functions, methods, and classes. Subsequently, it resolves calls between these defined entities to construct a detailed representation of how different parts of the codebase interact. The class provides methods to initiate this analysis and to retrieve the resulting relationships in a structured format.
*   **Instantiation:** This class is not explicitly listed as being instantiated by any other components in its provided context.
*   **Dependencies:** This class relies on external modules such as 'ast' for parsing Python code, 'os' for file system operations, 'logging' for error reporting, and 'collections.defaultdict' for managing graph data structures.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the ProjectAnalyzer instance by setting up the project's root directory, converting it to an absolute path. It also initializes several internal data structures: `definitions` (a dictionary for storing entity definitions), `call_graph` (a defaultdict for storing call relationships), and `file_asts` (a dictionary for caching ASTs). Additionally, it defines a set of common directories to be ignored during file traversal.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, project_root)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **project_root** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`analyze`**
        *   *Signature:* `def analyze(self, )`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect function, method, and class definitions. Subsequently, it iterates through the files again to resolve all function and method calls. Finally, it clears the stored ASTs to free up memory and returns the generated call graph.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **call_graph** (`collections.defaultdict[list]`): A dictionary-like object representing the call graph, where keys are callee identifiers and values are lists of caller information.
        *   **Usage:**
            - **Calls:** Based on the provided method context for 'analyze', this method does not explicitly list any calls to other functions or methods.
            - **Called By:** Based on the provided method context for 'analyze', this method is not explicitly listed as being called by any other functions or methods.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self, )`
        *   *Description:* This method processes the internal `call_graph` to generate two distinct dictionaries: `outgoing` and `incoming` relationships. It iterates through the call graph, populating these dictionaries with unique caller-callee pairs. The final output is a dictionary containing both outgoing and incoming relationships, with the relationship lists sorted for consistency.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, "outgoing" and "incoming", each mapping to a dictionary of relationships where keys are entity identifiers and values are sorted lists of related entity identifiers.
        *   **Usage:**
            - **Calls:** Based on the provided method context for 'get_raw_relationships', this method does not explicitly list any calls to other functions or methods.
            - **Called By:** Based on the provided method context for 'get_raw_relationships', this method is not explicitly listed as being called by any other functions or methods.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self, )`
        *   *Description:* This private helper method is responsible for recursively traversing the project directory, starting from `self.project_root`. It filters out directories specified in `self.ignore_dirs` and collects the absolute paths of all files ending with `.py`. The method returns a list of these Python file paths.
        *   *Parameters:*
            - **self** (`None`): None
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found within the project, excluding ignored directories.
        *   **Usage:**
            - **Calls:** Based on the provided method context for '_find_py_files', this method does not explicitly list any calls to other functions or methods.
            - **Called By:** Based on the provided method context for '_find_py_files', this method is not explicitly listed as being called by any other functions or methods.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method reads a given Python file, parses its source code into an Abstract Syntax Tree (AST), and stores the AST. It then walks the AST to identify all function, method, and class definitions. For each definition, it constructs a unique path name and stores metadata (file path, line number, type) in the `self.definitions` dictionary. Error handling is included to log issues during parsing.
        *   *Parameters:*
            - **self** (`None`): None
            - **filepath** (`str`): The path to the Python file whose definitions are to be collected.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** Based on the provided method context for '_collect_definitions', this method does not explicitly list any calls to other functions or methods.
            - **Called By:** Based on the provided method context for '_collect_definitions', this method is not explicitly listed as being called by any other functions or methods.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This private helper method iterates through all nodes in a given AST (`tree`) to find the direct parent of a specific `node`. It does this by checking if the target `node` is a child of any `parent` node encountered during the AST walk. If a parent is found, it is returned; otherwise, `None` is returned.
        *   *Parameters:*
            - **self** (`None`): None
            - **tree** (`ast.AST`): The Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent_node** (`ast.AST | None`): The parent AST node of the given child node, or `None` if no parent is found.
        *   **Usage:**
            - **Calls:** Based on the provided method context for '_get_parent', this method does not explicitly list any calls to other functions or methods.
            - **Called By:** Based on the provided method context for '_get_parent', this method is not explicitly listed as being called by any other functions or methods.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method takes a file path, retrieves its previously stored AST, and then uses a `CallResolverVisitor` to analyze the AST for function and method calls. It initializes the resolver with the file path, project root, and collected definitions. After the visitor processes the AST, the method iterates through the resolved calls and extends the class's `call_graph` with the identified caller-callee relationships. Errors during call resolution are logged.
        *   *Parameters:*
            - **self** (`None`): None
            - **filepath** (`str`): The path to the Python file whose calls are to be resolved.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** Based on the provided method context for '_resolve_calls', this method does not explicitly list any calls to other functions or methods.
            - **Called By:** Based on the provided method context for '_resolve_calls', this method is not explicitly listed as being called by any other functions or methods.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an ast.NodeVisitor subclass designed to traverse a Python Abstract Syntax Tree (AST) and identify all function and method calls within a given source file. It maintains a scope for imported names and tracks the current class and function context to construct fully qualified names for both callers and callees. The visitor collects detailed information about each call, including the caller's identifier, type, file, and line number, associating this data with the fully qualified name of the called entity.
*   **Instantiation:** The input context indicates that there are no explicit instantiations recorded for this class.
*   **Dependencies:** This class depends on the 'ast' module for AST traversal, 'os' for path manipulation, and 'collections.defaultdict' for storing call relationships.
*   **Constructor:**
    *   *Description:* This constructor initializes the CallResolverVisitor instance with the necessary context for AST traversal and call resolution. It sets up attributes to store the file path, module path, known definitions, current scope for names, instance types for variables, and tracking for the current caller and class names. A defaultdict is also initialized to store the discovered call relationships.
    *   *Parameters:*
        - **filepath** (`str`): The path to the source file being analyzed.
        - **project_root** (`str`): The root directory of the project, used to determine the module path.
        - **definitions** (`dict`): A dictionary containing known fully qualified names of functions, classes, and methods within the project.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, filepath, project_root, definitions)`
        *   *Description:* *Analysis data not available for this component.*
        *   *Parameters:*
            - **self** (`None`): None
            - **filepath** (`None`): None
            - **project_root** (`None`): None
            - **definitions** (`None`): None
        *   *Returns:* *No return value.*
        *   **Usage:** *Analysis data not available for this component.*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is invoked by the AST visitor framework when an 'ast.ClassDef' node is encountered. Its primary role is to manage the `current_class_name` attribute, ensuring that the visitor correctly tracks the class context during traversal. It temporarily updates the class name to the current class's name before recursively visiting its children and restores the previous class name upon exiting the class definition.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is called by the ast.NodeVisitor framework when a ClassDef node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles 'ast.FunctionDef' nodes, which represent function or method definitions. It constructs a fully qualified identifier for the function or method based on the current module and class context. The method updates the `current_caller_name` attribute to this new identifier before recursively visiting the function's body, and then restores the previous caller name upon completing the visit to maintain correct scope.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.FunctionDef`): The AST node representing a function or method definition.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is called by the ast.NodeVisitor framework when a FunctionDef node is encountered during AST traversal.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method processes 'ast.Call' nodes, which represent function or method invocations. It attempts to resolve the fully qualified name of the called entity using the internal helper method `_resolve_call_qname`. If the callee's qualified name is successfully resolved and exists within the known definitions, the method records detailed information about the call, including the caller's file, line number, full identifier, and type, storing this data in the `self.calls` dictionary.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self._resolve_call_qname`, `os.path.basename`
            - **Called By:** This method is called by the ast.NodeVisitor framework when a Call node is encountered during AST traversal.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method handles 'ast.Import' nodes, which correspond to `import module` statements in Python. It iterates through the imported names and their aliases, populating the `self.scope` dictionary. This dictionary maps the local name (or alias) to the original module name, which is essential for later resolving fully qualified names of entities accessed via these imports.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is called by the ast.NodeVisitor framework when an Import node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes 'ast.ImportFrom' nodes, representing `from module import name` statements. It calculates the full module path, correctly handling relative imports based on the current module's path and the import level. It then populates `self.scope` with mappings from the imported name (or its alias) to its fully qualified path, which is critical for accurately resolving calls to imported entities.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is called by the ast.NodeVisitor framework when an ImportFrom node is encountered during AST traversal.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method handles 'ast.Assign' nodes, specifically focusing on assignments where the right-hand side is a call to a class constructor. If it identifies such a pattern, and the class name is found in the current scope and known definitions, it records the fully qualified class name as the type of the assigned variable in `self.instance_types`. This mapping is crucial for resolving method calls made on instantiated objects later in the AST traversal.
        *   *Parameters:*
            - **self** (`None`): None
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:* *No return value.*
        *   **Usage:**
            - **Calls:** `self.generic_visit`
            - **Called By:** This method is called by the ast.NodeVisitor framework when an Assign node is encountered during AST traversal.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method is responsible for determining the fully qualified name (QName) of a function or method being called. It handles two primary scenarios: direct calls to names (`ast.Name`) by checking `self.scope` and local definitions, and method calls on objects (`ast.Attribute`) by consulting `self.instance_types` for the object's class or `self.scope` for module-level attributes. The method returns the resolved QName as a string or `None` if the name cannot be determined.
        *   *Parameters:*
            - **self** (`None`): None
            - **func_node** (`ast.expr`): The AST node representing the function or method being called, which can be an 'ast.Name' or 'ast.Attribute' node.
        *   *Returns:*
            - **name** (`str | None`): The fully qualified name of the called entity, or None if it cannot be resolved.
        *   **Usage:**
            - **Calls:** This method does not explicitly call other methods within the provided source code snippet.
            - **Called By:** `self.visit_Call`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file system path into a Python module path string. It first determines the relative path of the file with respect to a specified project root. If a ValueError occurs during relative path calculation, it falls back to using just the base name of the file. The function then removes the '.py' extension if present and replaces file system path separators with dots. Finally, it handles '__init__' modules by stripping the '.__init__' suffix to yield the package name.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `backend/scads_key_test.py`
*No classes or functions were found in this file.*

---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text, )`
*   **Description:** This function `encrypt_text` is designed to encrypt a given string using a `cipher_suite` object. It first performs a conditional check: if the input `text` is empty or if the `cipher_suite` object is not available, it returns the original `text` without any modification. Otherwise, the function processes the `text` by removing leading/trailing whitespace, encoding it into bytes, encrypting these bytes using the `cipher_suite.encrypt` method, and then decoding the resulting encrypted bytes back into a string before returning it. The `cipher_suite` is expected to be an externally defined object, likely an instance of `cryptography.fernet.Fernet` based on the imports.
*   **Parameters:**
    - **text** (`str`): The string to be encrypted. If this string is empty or falsy, or if the `cipher_suite` is not available, the original string is returned unencrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input string, or the original string if encryption was skipped due to empty text or an unavailable cipher suite.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text, )`
*   **Description:** This function attempts to decrypt a given string using a global `cipher_suite` object. It first checks if the input `text` is empty or if `cipher_suite` is not initialized, in which case it returns the original text without modification. If decryption is attempted, the text is stripped, encoded to bytes, decrypted, and then decoded back into a string. A `try-except` block handles potential errors during the decryption process, returning the original text if any exception occurs.
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted string if successful, or the original string if decryption is not performed or fails due to an exception.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function is designed to create a new user record and store it in a database. It accepts a username, the user's full name, and a plain-text password. The provided password is first hashed using a utility from `streamlit_authenticator` for security purposes. A user document is then constructed, including default empty strings for various API keys, and inserted into the `dbusers` collection. The function's primary role is to facilitate user registration by securely storing new user credentials and associated data.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier of the newly inserted user document in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is designed to retrieve all user records from a database collection named 'dbusers'. It executes a find operation on the collection, which typically returns a cursor, and then converts the results into a Python list. The primary purpose is to provide a complete list of all users stored in the database.
*   **Parameters:** *No parameters.*
*   **Returns:**
    - **users** (`list`): A list containing all user documents (dictionaries) retrieved from the 'dbusers' collection.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username, )`
*   **Description:** The `fetch_user` function is responsible for retrieving a single user document from a database collection named `dbusers`. It takes a `username` as input and uses it to query the collection for a document where the `_id` field matches the provided username. The function returns the first document that satisfies this query.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched, which is used to match the `_id` field in the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if a match is found, or `None` if no user with the specified `_id` exists.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username, new_name)`
*   **Description:** This function updates a user's name in the `dbusers` collection. It identifies the user by their `username`, which is used as the `_id` field in the database. The function then sets the `name` field of the matching document to the provided `new_name`. It returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The current username, which serves as the unique identifier (_id) for the user to be updated.
    - **new_name** (`str`): The new name to be assigned to the user's 'name' field.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. Typically 0 or 1 for an update_one operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function updates a user's Gemini API key in a database. It takes a username and the raw API key, encrypts the key after stripping any leading/trailing whitespace, and then stores the encrypted key in the `dbusers` collection associated with the provided username. The function returns the count of documents that were modified by this update operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be encrypted and stored for the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation. A value of 1 typically indicates a successful update for an existing user.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username, gpt_api_key)`
*   **Description:** This function is responsible for updating a user's GPT API key within a database. It takes a username and the new API key as input. The API key is first stripped of any leading/trailing whitespace and then encrypted using an external `encrypt_text` function. Finally, it performs an update operation on the `dbusers` collection, setting the `gpt_api_key` field for the specified user with the newly encrypted key. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be stored for the user, which will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation. This will typically be 1 if the user exists and the key was updated, or 0 if no matching user was found or no change was made.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function updates the Ollama base URL for a specific user within a database. It takes a username and a new Ollama base URL as input. The function then performs an update operation on the 'dbusers' collection, setting the 'ollama_base_url' field for the document matching the provided username. The input URL is stripped of leading/trailing whitespace before being stored. It returns an integer indicating the number of documents that were modified.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be updated.
    - **ollama_base_url** (`str`): The new base URL for Ollama, which will be stored after stripping whitespace.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username, opensrc_api_key)`
*   **Description:** The `update_opensrc_key` function is designed to securely update a user's Open Source API key within a database. It takes a username and the new API key as input. The function first processes the provided API key by stripping whitespace and then encrypting it. Finally, it performs an update operation on the `dbusers` collection, setting the `opensrc_api_key` field for the specified user with the newly encrypted key. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source API key is to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be encrypted and stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, indicating whether the user's API key was successfully updated.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username, opensrc_base_url)`
*   **Description:** This function updates the 'opensrc_base_url' for a specific user in the database. It takes a username and a new base URL as input. The function uses the 'dbusers' collection to find a document matching the provided username as its '_id' and then sets the 'opensrc_base_url' field. The provided URL is stripped of leading/trailing whitespace before being stored. The function returns the count of documents that were modified by the update operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose 'opensrc_base_url' is to be updated. This is used as the '_id' in the database query.
    - **opensrc_base_url** (`str`): The new base URL for opensrc to be associated with the user. This string will have leading/trailing whitespace removed before being saved.
*   **Returns:**
    - **modified_count** (`int`): An integer representing the number of documents that were modified by the update operation. Typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username, )`
*   **Description:** This function retrieves the Gemini API key associated with a given username from a database. It queries the `dbusers` collection for a document matching the provided username and specifically projects the `gemini_api_key` field. If a user document is found and contains the `gemini_api_key`, that key is returned. Otherwise, the function returns `None`.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the Gemini API key.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key if found for the specified user, otherwise None.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username, )`
*   **Description:** This function retrieves the Ollama base URL associated with a specific username from a database. It queries the 'dbusers' collection using the provided username as the document ID. If a user is found, it attempts to extract the 'ollama_base_url' field. The function returns this URL or None if the user is not found or the URL field is missing.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL string if found for the user, otherwise None.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username, )`
*   **Description:** This function, `fetch_gpt_key`, is designed to retrieve a user's GPT API key from a database. It takes a username as input and queries a `dbusers` collection to locate the corresponding user document. If a user is found, the function attempts to extract the 'gpt_api_key' field from that document. It returns the API key if present, otherwise it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the user, or None if the user or key is not found in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username, )`
*   **Description:** This function, `fetch_opensrc_key`, is responsible for retrieving an Open Source API key from a database based on a provided username. It performs a database query on the `dbusers` collection to find a user document matching the given username. If a user is found, the function extracts and returns the associated `opensrc_api_key`. If no user document is found for the specified username, the function returns `None`.
*   **Parameters:**
    - **username** (`str`): The username for which to retrieve the Open Source API key.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key associated with the username, or None if the user is not found in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username, )`
*   **Description:** The `fetch_opensrc_url` function is designed to retrieve the opensource base URL associated with a specific user from a database. It queries the `dbusers` collection using the provided username as the document's `_id`. The function projects only the `opensrc_base_url` field, excluding the `_id` field from the result. If a user document is found, it extracts and returns the `opensrc_base_url`; otherwise, it returns `None` to indicate that the user or URL was not found.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose opensource base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str | None`): The opensource base URL associated with the user, or `None` if the user is not found or the URL is not present.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username, )`
*   **Description:** The `delete_user` function is designed to remove a specific user record from the `dbusers` collection. It takes a username as input and uses it to identify the document to be deleted by matching it against the `_id` field. The function then returns the count of documents that were successfully deleted, typically 0 or 1.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted from the `dbusers` collection. This will typically be 0 if no user was found, or 1 if a user was successfully deleted.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username, )`
*   **Description:** This function retrieves and decrypts API keys and base URLs for a specified user from a database. It queries the 'dbusers' collection using the provided username. If the user is found, it decrypts the Gemini, GPT, and open-source API keys, and retrieves the Ollama and open-source base URLs. The function returns all these values, or None for all if the user does not exist.
*   **Parameters:**
    - **username** (`str`): The username used to identify the user in the database.
*   **Returns:**
    - **gemini_plain** (`str`): The decrypted Gemini API key.
    - **ollama_plain** (`str`): The Ollama base URL.
    - **gpt_plain** (`str`): The decrypted GPT API key.
    - **opensrc_plain** (`str`): The decrypted open-source API key.
    - **opensrc_url** (`str`): The open-source base URL.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username, chat_name)`
*   **Description:** The `insert_chat` function is responsible for creating a new chat entry within a database. It constructs a dictionary containing a unique identifier generated by `uuid.uuid4()`, the provided username, the chat name, and the current timestamp using `datetime.now()`. This prepared chat dictionary is then inserted into the `dbchats` collection using `insert_one()`. The function concludes by returning the unique `_id` of the newly inserted chat document.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (`_id`) of the newly created chat document in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username, )`
*   **Description:** The `fetch_chats_by_user` function is responsible for retrieving all chat records associated with a specific user from a database. It queries a collection, presumably `dbchats`, using the provided username as a filter. The results are then sorted chronologically by their `created_at` timestamp in ascending order. Finally, the function returns the collected chat documents as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat records.
*   **Returns:**
    - **chats** (`list`): A list of chat records (documents) associated with the specified username, sorted by their creation timestamp.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username, chat_name)`
*   **Description:** This function checks for the existence of a specific chat entry within the 'dbchats' collection. It queries the database using a provided username and chat name. The function returns a boolean value indicating whether a matching chat record was found.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked.
*   **Returns:**
    - **chat_exists** (`bool`): True if a chat matching the username and chat name exists, False otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
*   **Description:** This function renames a chat entry and all its associated exchange messages within a database. It updates the 'chat_name' field in both the 'dbchats' and 'dbexchanges' collections for a specific user, changing the 'old_name' to 'new_name'. The function returns the number of chat documents modified during the initial chat renaming operation.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The desired new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat documents that were modified in the 'dbchats' collection.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time, json_tokens, toon_tokens, savings_percent)`
*   **Description:** This function is designed to insert a new chat exchange record into a database. It generates a unique identifier for each exchange using UUID. The function constructs a comprehensive dictionary containing the user's question, the generated answer, feedback, user details, chat session name, and various optional performance metrics such as time taken and token usage. It also automatically records the current timestamp for creation. The function attempts to persist this structured data into the `dbexchanges` collection and returns the unique ID upon success, or `None` if a database error occurs.
*   **Parameters:**
    - **question** (`str`): The user's question or prompt in the exchange.
    - **answer** (`str`): The generated answer or response to the question.
    - **feedback** (`str`): The feedback provided for the exchange.
    - **username** (`str`): The username associated with this exchange.
    - **chat_name** (`str`): The name of the chat session to which this exchange belongs.
    - **helper_used** (`str`): Optional: Identifier for the helper model used in the exchange.
    - **main_used** (`str`): Optional: Identifier for the main model used in the exchange.
    - **total_time** (`str`): Optional: The total time taken for the exchange process.
    - **helper_time** (`str`): Optional: The time taken specifically by the helper model.
    - **main_time** (`str`): Optional: The time taken specifically by the main model.
    - **json_tokens** (`int`): Optional: The number of JSON tokens processed or generated.
    - **toon_tokens** (`int`): Optional: The number of Toon tokens processed or generated.
    - **savings_percent** (`float`): Optional: The percentage of savings achieved for this exchange.
*   **Returns:**
    - **new_id** (`str`): The unique identifier (UUID) of the newly inserted exchange record upon successful database operation.
    - **None** (`NoneType`): Indicates that an error occurred during the database insertion process.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username, )`
*   **Description:** This function retrieves all exchange records from the database that are associated with a specific username. It queries a collection, presumably `dbexchanges`, filtering by the provided `username`. The retrieved records are then sorted in ascending order based on their `created_at` timestamp. Finally, the function returns these sorted exchange records as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (e.g., dictionaries or objects) associated with the specified username, sorted by their creation timestamp.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function, `fetch_exchanges_by_chat`, is designed to retrieve a collection of exchange records from a database. It queries the `dbexchanges` collection, filtering documents based on a provided username and chat name. The matching records are then sorted by their 'created_at' timestamp in ascending order. Finally, the function returns these sorted records as a list.
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchange records.
    - **chat_name** (`str`): The name of the chat used to filter the exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents that match the specified username and chat name, sorted by creation time.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function is responsible for updating the feedback value associated with a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function performs a targeted update operation on a database collection, setting the 'feedback' field for the document matching the provided exchange ID. It then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange record that needs its feedback updated. This ID is used to locate the specific document in the database.
    - **feedback** (`int`): The integer value representing the feedback to be set for the identified exchange record.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. For an 'update_one' operation, this will typically be 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function updates an existing exchange record in a database collection. It identifies the record by its unique exchange ID and sets or updates its 'feedback_message' field with the provided string. The function then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier for the exchange record to be updated.
    - **feedback_message** (`str`): The new feedback message to associate with the specified exchange record.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id, )`
*   **Description:** This function, `delete_exchange_by_id`, is designed to remove a specific exchange record from a database collection. It takes a unique identifier, `exchange_id`, as an argument to locate the target record. The function executes a delete operation on the `dbexchanges` collection, targeting the document whose `_id` field matches the provided `exchange_id`. It then returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **exchange_id** (`str`): The unique string identifier of the exchange record to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted by the operation. This will typically be 0 or 1 for a 'delete_one' operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username, chat_name)`
*   **Description:** This function is responsible for deleting a complete chat, including all its associated exchanges, to maintain data consistency between the frontend and backend. It first removes all messages (exchanges) linked to the specified username and chat name. Subsequently, it deletes the chat entry itself from the chat list. The function returns the count of chats that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted by the operation. Typically 1 if the chat was found and deleted, or 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

---
### File: `frontend/frontend.py`
#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list, )`
*   **Description:** This function takes a list of strings, assumed to be model identifiers or paths, and processes each string. It splits each input string by the '/' character and extracts the last segment. The function then returns a new list containing these extracted base names or identifiers.
*   **Parameters:**
    - **model_list** (`List[str]`): A list of strings, where each string is expected to represent a path or identifier containing '/' delimiters.
*   **Returns:**
    - **cleaned_names** (`List[str]`): A new list containing the last segment of each string from the input 'model_list' after splitting by '/'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list, category_name)`
*   **Description:** This function filters a given list of models based on a specified category name. It retrieves associated keywords for the category from a global `CATEGORY_KEYWORDS` mapping. If the 'STANDARD' keyword is present, it returns only those models from the source list that are also found in `STANDARD_MODELS`. Otherwise, it filters the `source_list` to include models whose names contain any of the category's keywords (case-insensitive). If no models match the keywords, the original `source_list` is returned.
*   **Parameters:**
    - **source_list** (`list`): The list of models to be filtered.
    - **category_name** (`str`): The name of the category used to determine filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A new list containing models that match the specified category's keywords, or the original `source_list` if no matches are found or if the 'STANDARD' filter applies.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function handles the saving of a new Gemini API key. It retrieves the potential new key from the Streamlit session state. If a new key is present, it updates the Gemini key in the database for the current user and then clears the key from the session state. Finally, it displays a success toast message to the user.
*   **Parameters:** *No parameters.*
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function, `save_ollama_cb`, acts as a callback to persist a user-defined Ollama URL. It retrieves a potential new Ollama URL from the Streamlit session state, specifically from the key 'in_ollama_url'. If a non-empty URL is found, the function proceeds to update this URL in the database. It utilizes the current username, also obtained from the session state, to associate the URL with the correct user. Upon successful update, a confirmation toast message is displayed to the user.
*   **Parameters:** *No parameters.*
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username, )`
*   **Description:** This function is responsible for loading chat and exchange data for a specified user from the database into the Streamlit session state. It first checks if the data for the current user has already been loaded to prevent redundant operations. It initializes the session state's chat structure, then fetches predefined chats and their associated exchanges, organizing them within the session state. The function also handles cases where exchanges might exist for chats not initially loaded and ensures a default chat is created if no chat data is found for the user. Finally, it sets an active chat if one isn't already defined or valid.
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat and exchange data.
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function, `handle_feedback_change`, is responsible for updating feedback associated with an exchange object. It first modifies the provided exchange dictionary in-place by setting its 'feedback' key to the new value. Subsequently, it invokes a database utility to persist this feedback change using the exchange's unique identifier. Finally, it triggers a Streamlit application rerun, likely to refresh the user interface and display the updated feedback status.
*   **Parameters:**
    - **ex** (`dict`): Represents an exchange object or a data record, expected to contain at least 'feedback' and '_id' keys.
    - **val** (`Any`): The new feedback value to be assigned to the exchange object and updated in the database.
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if so, removes the exchange object from that chat's list of exchanges. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be removed in the session state.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' field for database deletion.
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function manages the deletion of a specific chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it updates the Streamlit session state by removing the chat from `st.session_state.chats`. If other chats exist, the `active_chat` is reset to the first available chat; otherwise, a new default chat named "Chat 1" is created, inserted into the database via `db.insert_chat`, and set as the active chat. The function concludes by triggering a Streamlit rerun.
*   **Parameters:**
    - **username** (`str`): The identifier for the user whose chat is to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted for the specified user.
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text, )`
*   **Description:** This function aims to extract a repository name from a given text string. It first attempts to find a URL within the text using a regular expression. If a URL is identified, it then parses the URL to extract its path component. The last segment of the path is considered the repository name, with an additional check to remove a ".git" suffix if present. If no URL is found or no valid repository path can be extracted, the function returns None.
*   **Parameters:**
    - **text** (`str`): The input string from which to extract a repository name. This string is expected to potentially contain a URL.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string, or None if no URL is found or no repository name can be extracted from the URL path.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text, )`
*   **Description:** This function acts as a generator that takes a single string of text and yields its words sequentially. It splits the input text by spaces and then iterates through each word. For every word, it yields the word followed by a space, introducing a small delay of 0.01 seconds between each yield operation. This creates a streaming effect, delivering text word by word with a brief pause.
*   **Parameters:**
    - **text** (`str`): The input string of text to be streamed word by word.
*   **Returns:**
    - **word_with_space** (`str`): A generator that yields individual words from the input text, each followed by a space, with a short delay.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream)`
*   **Description:** This function processes a given markdown text, identifying and rendering embedded Mermaid diagrams. It splits the input text into parts, distinguishing between regular markdown content and Mermaid diagram blocks. Regular text content is rendered using either `st.write_stream` for streaming or `st.markdown` for direct display, based on the `should_stream` flag. Mermaid diagram blocks are attempted to be rendered using `st_mermaid`, with a fallback to `st.code` if an error occurs during rendering. The function returns early if the input markdown text is empty.
*   **Parameters:**
    - **markdown_text** (`str`): The input text, potentially containing embedded Mermaid diagrams formatted with '```mermaid ... ```'.
    - **should_stream** (`bool`): A flag indicating whether regular text parts should be streamed using `st.write_stream` (True) or rendered directly with `st.markdown` (False). Defaults to False.
*   **Returns:**
    - **None** (`None`): The function does not explicitly return a value; it performs side effects by rendering content to a Streamlit application. It implicitly returns None.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function, `render_exchange`, is designed to display a single user-assistant interaction within a Streamlit chat interface. It first renders the user's question, followed by the assistant's response. The assistant's message includes a dynamic toolbar with feedback options (like/dislike), a comment popover, download functionality, and a delete button, which are only shown if the answer is not an error. If the answer indicates an error, a simplified error message and a delete option are presented. Finally, the assistant's answer content is rendered, potentially including Mermaid diagrams.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing a single exchange, containing keys such as 'question', 'answer', 'feedback', '_id', and 'feedback_message'.
    - **current_chat_name** (`str`): The name of the current chat, used for context in operations like deleting an exchange.
*   **Returns:** *No return value.*
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to provide a structured representation for a single parameter of a function. It encapsulates the essential details of a parameter, including its name, data type, and a descriptive explanation of its purpose. This class serves as a standardized data structure for documenting function parameters.
*   **Instantiation:** This class's instantiation points are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the ParameterDescription class automatically generates an `__init__` method. This constructor is responsible for initializing the instance attributes `name`, `type`, and `description` based on the arguments provided during object creation, ensuring type validation according to the defined schema.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type annotation or inferred type of the parameter.
        - **description** (`str`): A textual explanation of the parameter's role and purpose.
*   **Methods:** *No methods defined.*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to structure and validate information about a function's return value. It serves as a clear, standardized data container for describing the name, type, and purpose of a value returned by a function. This class ensures that return value descriptions adhere to a consistent format, facilitating automated documentation and analysis within a larger system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance of `ReturnDescription` by accepting `name`, `type`, and `description` as keyword arguments, validating their types, and assigning them as instance attributes.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The Python type hint or a descriptive string indicating the data type of the return value.
        - **description** (`str`): A detailed explanation of what the return value represents or its purpose.
*   **Methods:** *No methods defined.*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts with other components. It provides a structured format to describe what a function calls and where it is called from, using two string attributes: 'calls' and 'called_by'. This model facilitates consistent representation of functional dependencies and usage patterns within a system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* The `__init__` method for this Pydantic model is implicitly generated by BaseModel. It takes 'calls' and 'called_by' as arguments to initialize the instance attributes, ensuring type validation according to their annotations.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions, methods, or classes that this context calls.
        - **called_by** (`str`): A string describing where this context is used or called from.
*   **Methods:** *No methods defined.*

#### Class: `FunctionDescription`
*   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to provide a comprehensive, structured analysis of a Python function. It serves as a data container, encapsulating key aspects such as the function's general purpose and implementation, detailed descriptions of its parameters, its return values, and its contextual usage within a larger system. This class is fundamental for standardizing the output of automated function analysis.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `FunctionDescription` is implicitly generated by Pydantic. It handles the instantiation of a `FunctionDescription` object by validating and assigning values to its defined fields: `overall`, `parameters`, `returns`, and `usage_context`.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the function's purpose and implementation.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each describing a single parameter of the function, including its name, type, and purpose.
        - **returns** (`List[ReturnDescription]`): A list of objects, each describing a return value of the function, including its type and purpose.
        - **usage_context** (`UsageContext`): An object containing information about where the function is called and what other functions or methods it calls.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data container, holding the function's unique identifier, a detailed description object, and an optional error message. This model is crucial for standardizing the representation of function analysis results within a larger system, enabling consistent data exchange and processing.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class inherits from Pydantic's BaseModel, and as such, it does not define an explicit __init__ method. Pydantic automatically generates a constructor that initializes the instance attributes based on the type hints and default values provided in the class definition.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): An object containing a detailed analysis of the function, including its overall purpose, parameters, return values, and usage context.
        - **error** (`Optional[str]`): An optional string that provides details about any errors encountered during the analysis of the function. It defaults to None if no errors occurred.
*   **Methods:** *No methods defined.*

#### Class: `ConstructorDescription`
*   **Summary:** The `ConstructorDescription` class is a Pydantic BaseModel designed to encapsulate the metadata of a class's `__init__` method. It provides a structured format to store a textual description of the constructor's purpose and a list of its individual parameters. This model is crucial for standardizing the representation of constructor information within a larger code analysis or documentation generation system.
*   **Instantiation:** The input context does not specify where this class is instantiated. It is likely instantiated programmatically when parsing or generating structured data related to class constructors.
*   **Dependencies:** This class primarily depends on `pydantic.BaseModel` for its data modeling capabilities and `typing.List` for type hinting its `parameters` attribute.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance of `ConstructorDescription` by accepting a string `description` and a list of `ParameterDescription` objects, which define the constructor's overall purpose and its individual input parameters, respectively.
    *   *Parameters:*
        - **description** (`str`): A concise textual summary describing the purpose and behavior of the `__init__` method.
        - **parameters** (`List[ParameterDescription]`): A list containing `ParameterDescription` objects, each detailing an individual parameter accepted by the `__init__` method, including its name, type, and specific description.
*   **Methods:** *No methods defined.*

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate information about a class's operational context. It specifically stores details regarding the external dependencies that the class relies upon and the locations or modules where the class is instantiated. This model provides a structured way to represent and manage metadata about a class's integration within a larger system.
*   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is automatically generated. It initializes instances of ClassContext by setting the `dependencies` and `instantiated_by` attributes based on the provided string values during object creation.
    *   *Parameters:*
        - **dependencies** (`str`): A string representing the external dependencies of the class being described.
        - **instantiated_by** (`str`): A string indicating where the class being described is primarily instantiated within the system.
*   **Methods:** *No methods defined.*

#### Class: `ClassDescription`
*   **Summary:** The `ClassDescription` class serves as a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python class. It structures data related to a class's high-level purpose, its constructor's details, a list of analyses for all its methods, and its external usage context. This model is fundamental for representing structured class metadata within a larger documentation or analysis system.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly declare external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates its `__init__` method. It accepts keyword arguments corresponding to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`. These arguments are used to initialize the instance's attributes, ensuring type validation and data integrity upon creation.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary describing the class's main purpose and functionality.
        - **init_method** (`ConstructorDescription`): An object containing the detailed analysis of the class's constructor (`__init__`) method.
        - **methods** (`List[FunctionAnalysis]`): A list of `FunctionAnalysis` objects, each detailing an individual method within the class.
        - **usage_context** (`ClassContext`): An object providing context about the class's external dependencies and where it is instantiated.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the top-level Pydantic model for structuring the comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed ClassDescription object containing constructor and method analyses, and an optional field for reporting any errors during the analysis process. This model is designed to provide a standardized, machine-readable representation of a class's structure and behavior.
*   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly generates an __init__ method. It initializes an instance of ClassAnalysis by accepting values for its identifier, description, and an optional error field, ensuring type validation according to the Pydantic schema.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, its constructor, and methods.
        - **error** (`Optional[str]`): An optional string field to capture any errors encountered during the class analysis.
*   **Methods:** *No methods defined.*

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to represent a specific call event within a system, likely used by a relationship analyzer. It acts as a structured data container, encapsulating key details about a call's origin, such as the file path, the name of the calling function, the mode of the call (e.g., method, function), and the line number where the call occurs. This class provides a standardized format for tracking and referencing call events.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The CallInfo class, being a Pydantic BaseModel, automatically generates its `__init__` method. This constructor is responsible for initializing the instance attributes `file`, `function`, `mode`, and `line` based on the values provided during object creation, ensuring type validation and data integrity.
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event originated.
        - **function** (`str`): The name of the function or method that performed the call.
        - **mode** (`str`): The type or context of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The specific line number in the source file where the call was made.
*   **Methods:** *No methods defined.*

#### Class: `FunctionContextInput`
*   **Summary:** This class serves as a Pydantic model to structure contextual information required for analyzing a function. It encapsulates details about other functions or classes that the target function calls, as well as information about where the target function itself is invoked. This model facilitates the standardized exchange and validation of function-level context data within a larger system.
*   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, has an implicitly generated constructor. It initializes instances with `calls` and `called_by` attributes, which are validated against their respective types upon instantiation.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of identifiers (strings) representing the functions, methods, or classes that the function under analysis calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, each detailing a specific location or context from which the function under analysis is invoked.
*   **Methods:** *No methods defined.*

#### Class: `FunctionAnalysisInput`
*   **Summary:** This class defines the data structure for input required to perform a function analysis. It is a Pydantic BaseModel that enforces the schema for analyzing a function, including its source code, identifier, and contextual information. This model ensures that all necessary data points are present and correctly typed before a function analysis can proceed, acting as a contract for data exchange.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method, implicitly provided by Pydantic's BaseModel, initializes an instance of `FunctionAnalysisInput`. It validates and assigns the provided `mode`, `identifier`, `source_code`, `imports`, and `context` values to corresponding instance attributes, ensuring type correctness according to the defined schema.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the operational mode, fixed to 'function_analysis' for this input type.
        - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
        - **source_code** (`str`): The raw source code of the function to be analyzed.
        - **imports** (`List[str]`): A list of import statements relevant to the function's source file.
        - **context** (`FunctionContextInput`): Additional contextual information pertinent to the function's analysis.
*   **Methods:** *No methods defined.*

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to provide a structured representation of a method's contextual information. It serves as a data schema to encapsulate various attributes pertinent to a method, such as its unique identifier, the functions or methods it calls, where it is invoked from, its arguments, and its associated docstring. This class is crucial for standardizing the input data for analysis or documentation generation processes related to individual methods.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within its provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method for `MethodContextInput` is implicitly generated by Pydantic. It handles the validation and assignment of the class's fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`, ensuring that instances are created with valid data types according to the defined schema.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method being described.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method invokes.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects detailing the locations or entities that call this method.
        - **args** (`List[str]`): A list of argument names that the method accepts in its signature.
        - **docstring** (`Optional[str]`): The docstring content of the method, if one is present, otherwise null.
*   **Methods:** *No methods defined.*

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate comprehensive context information for a Python class analysis. It serves as a structured input for systems that require detailed data about a class's dependencies, where it is instantiated, and specific context for each of its methods. This model facilitates a holistic understanding of a class's role and interactions within a larger codebase.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly declare external functional dependencies within its definition, relying on its Pydantic BaseModel inheritance.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an __init__ method. Pydantic's BaseModel automatically generates a constructor based on the type-hinted fields, allowing instances to be created by passing keyword arguments corresponding to 'dependencies', 'instantiated_by', and 'method_context'.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of external dependencies required by the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where the class being analyzed is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects providing context for each method within the class being analyzed.
*   **Methods:** *No methods defined.*

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel that defines the structured input required for generating a ClassAnalysis object. It serves as a data contract, ensuring that all necessary components like the operation mode, class identifier, source code, import statements, and contextual information are provided in a validated format for subsequent analysis. This class is fundamental for standardizing the input data for an AI code analysis system.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the given context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `ClassAnalysisInput` class inherits from Pydantic's `BaseModel`, meaning its constructor is implicitly generated by Pydantic. This constructor handles the initialization and validation of instance attributes based on the type hints defined for `mode`, `identifier`, `source_code`, `imports`, and `context` when an object of this class is created.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operational mode, which is fixed to 'class_analysis' for this input type.
        - **identifier** (`str`): The unique name or identifier of the class that is to be analyzed.
        - **source_code** (`str`): The raw Python source code of the entire class definition to be analyzed.
        - **imports** (`List[str]`): A list of import statements found in the source file, which may be relevant to the class or its methods.
        - **context** (`ClassContextInput`): An object containing additional contextual information pertinent to the class analysis, such as dependencies and instantiation points.
*   **Methods:** *No methods defined.*

---
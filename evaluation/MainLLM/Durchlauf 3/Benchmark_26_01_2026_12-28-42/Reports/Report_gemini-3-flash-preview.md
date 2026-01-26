# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** The Repo Onboarding Agent is an automated documentation pipeline designed to analyze Python-based repositories. It uses a multi-stage LLM architecture (Helper and Main LLMs) to process source code via Abstract Syntax Tree (AST) analysis, mapping function/class relationships and generating high-quality Markdown reports to aid developer onboarding.
- **Key Features:** 
  - Automated Repository Analysis: Clones and parses Git repositories to extract structural metadata.
  - AST-Driven Documentation: Generates granular analysis of classes and functions using specialized LLMs.
  - Relationship Mapping: Tracks function call graphs and class instantiation dependencies across the project.
  - Jupyter Notebook Support: Converts and analyzes `.ipynb` files into structured documentation.
  - Interactive UI: Streamlit-based frontend for repository exploration and documentation orchestration.
- **Tech Stack:** Python, Streamlit, LangChain, Pydantic, NetworkX, GitPython, MongoDB.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root --> root_files[".env.example <br/> .gitignore <br/> readme.md <br/> requirements.txt <br/> analysis_output.json <br/> output.toon <br/> test.json"]
    root --> SystemPrompts["SystemPrompts/ <br/> SystemPromptClassHelperLLM.txt <br/> SystemPromptFunctionHelperLLM.txt <br/> SystemPromptMainLLM.txt <br/> SystemPromptNotebookLLM.txt"]
    root --> backend["backend/ <br/> AST_Schema.py <br/> File_Dependency.py <br/> HelperLLM.py <br/> MainLLM.py <br/> basic_info.py <br/> callgraph.py <br/> main.py <br/> relationship_analyzer.py"]
    root --> database["database/ <br/> db.py"]
    root --> frontend["frontend/ <br/> frontend.py <br/> .streamlit/config.toml"]
    root --> schemas["schemas/ <br/> types.py"]
    root --> result["result/ <br/> (Generated MD Reports)"]
    ```

## 2. Installation
### Dependencies
- altair, anyio, GitPython, langchain, langchain-google-genai, langchain-ollama, networkx, pydantic, pymongo, streamlit, streamlit-authenticator, toon_format.
Note: **pip install -r requirements.txt**

### Setup Guide
1. Clone the repository.
2. Copy `.env.example` to `.env` and fill in your API keys (Gemini, OpenAI, or Ollama URL).
3. Ensure MongoDB is accessible if using the database features.

### Quick Startup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the frontend: `streamlit run frontend/frontend.py`

## 3. Use Cases & Commands
- **Onboarding Developers:** Generate a complete architectural and code-level report for a new repository to reduce the time-to-understanding.
- **Documentation Generation:** Create technical documentation for legacy projects lacking READMEs or docstrings.
- **Visualizing Dependencies:** Generate Mermaid diagrams of file-level and function-level dependencies.
- **Notebook Analysis:** Synthesize findings from research notebooks into the main project report.

**Primary Commands:**
- `streamlit run frontend/frontend.py`: Launches the web interface for the agent.

## 4. Architecture
*No specific architecture diagrams were provided in the input dataset.*

## 5. Code Analysis

### File: `backend/AST_Schema.py`

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
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method processes `ast.Import` nodes, which represent `import module` statements. It iterates through each alias in the import statement, extracting the module name and appending it to the `self.schema["imports"]` list. After recording the import, it calls `self.generic_visit(node)` to ensure that the AST traversal continues for any child nodes.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* N/A
        *   **Usage:** Called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.Import` node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to `from module import name` statements. It constructs fully qualified import names by combining the module name (if present) with each alias name, then appends these to `self.schema["imports"]`. This ensures that specific imports from modules are correctly captured. Finally, it invokes `self.generic_visit(node)` to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* N/A
        *   **Usage:** Called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ImportFrom` node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is responsible for processing `ast.ClassDef` nodes, which represent class definitions. It constructs a dictionary containing detailed information about the class, including its identifier, name, docstring, source code segment, and line numbers. This class information is then added to `self.schema["classes"]`, and the `_current_class` attribute is temporarily set to this class's info to provide context for any nested methods. After visiting child nodes via `self.generic_visit(node)`, `_current_class` is reset to `None`.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* N/A
        *   **Usage:** Called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ClassDef` node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, distinguishing between methods defined within a class and top-level functions. If `_current_class` is set, it means the function is a method, and its details (identifier, name, arguments, docstring, line numbers) are appended to the `method_context` of the current class. Otherwise, it's treated as a standalone function, and its details are added to `self.schema["functions"]`. It ensures proper AST traversal by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* N/A
        *   **Usage:** Called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.FunctionDef` node is encountered, and also by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method handles `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Instead of implementing its own parsing logic, it delegates the processing directly to the `visit_FunctionDef` method. This approach ensures that both synchronous and asynchronous function definitions are handled uniformly, extracting the same structural and metadata information.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* N/A
        *   **Usage:** Called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.AsyncFunctionDef` node is encountered.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process source code, particularly Python files within a Git repository, to build a structured Abstract Syntax Tree (AST) schema. It can analyze individual files to extract functions, classes, and their internal structures using an ASTVisitor. Additionally, it provides functionality to merge external relationship data, such as call graphs, into the generated AST schema, enriching the structural information with dynamic interaction details.
*   **Instantiation:** This class is not explicitly instantiated by any known components in the provided context.
*   **Dependencies:** This class depends on 'backend.AST_Schema.ASTVisitor' for parsing ASTs, 'ast' for Python's built-in AST module, and 'os' for path manipulation.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments, effectively creating a stateless instance.
    *   *Parameters:* N/A
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing calls, into a structured full schema. It iterates through files, functions, and classes within the schema, updating their respective context fields with call and called-by information. For classes, it also calculates and stores external dependencies based on method calls.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **full_schema** (`dict`): The comprehensive schema containing file, function, and class AST nodes.
            - **raw_relationships** (`dict`): A dictionary containing raw 'outgoing' and 'incoming' call relationships.
        *   *Returns:*
            - **full_schema** (`dict`): The updated 'full_schema' dictionary with integrated relationship data.
        *   **Usage:** This method is not explicitly called by any other functions or methods in the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to construct a full AST schema. It filters for Python files, reads their content, and uses an ASTVisitor to parse the Abstract Syntax Tree, extracting structural information. The method handles potential parsing errors and populates a 'full_schema' dictionary with the AST nodes for each successfully processed file.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the class.
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though it's not directly used in the provided snippet beyond its type hint.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed repository, structured by file paths.
        *   **Usage:** This method is not explicitly called by any other functions or methods in the provided context.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to a specified project root. If the file is a Python file, it removes the '.py' extension. Subsequently, it replaces path separators with dots to form the module path. Special handling is included for '__init__.py' files, where the '.__init__' suffix is removed to represent the package itself.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:** This function is not explicitly called by any other functions in the provided context.

---

### File: `backend/File_Dependency.py`

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
        *   *Signature:* `def _resolve_module_name(self, node: ImportFrom)`
        *   *Description:* This private method is responsible for resolving relative import statements (e.g., from .. import name). It calculates the correct base directory based on the import level and the current file's location within the repository. It then iterates through the imported names, checking if they correspond to existing module files or symbols exported by __init__.py files. If no matching modules or symbols are found, it raises an ImportError. Nested functions `module_file_exists` and `init_exports_symbol` are defined within this method to assist in verifying file and symbol existence.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST ImportFrom node representing the relative import statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of resolved module or symbol names as strings.
        *   **Usage:** This method is called by visit_ImportFrom when processing relative import statements.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* This method is part of the NodeVisitor pattern and is called for Import and ImportFrom AST nodes. It records the imported module names as dependencies for the current self.filename in the import_dependencies dictionary. If a base_name is provided (typically from visit_ImportFrom), it uses that; otherwise, it uses the alias name from the import node. After processing, it calls self.generic_visit(node) to continue the AST traversal.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing an import statement.
            - **base_name** (`str | None`): An optional base name for the module, typically used for from ... import ... statements where the module part is resolved separately.
        *   *Returns:* N/A
        *   **Usage:** This method is called by the AST NodeVisitor when encountering Import nodes, and explicitly by visit_ImportFrom to record dependencies.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
        *   *Description:* This method is invoked by the AST NodeVisitor when an ImportFrom node is encountered. It extracts the module name from the import statement. If it's an absolute import, it takes the last part of the module name and passes it to visit_Import. If it's a relative import (indicated by node.module being None), it attempts to resolve the module name using the _resolve_module_name helper method. Any resolved base names are then passed to visit_Import to record the dependency. Errors during relative import resolution are caught and printed. Finally, it ensures the AST traversal continues with self.generic_visit.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST ImportFrom node to be processed.
        *   *Returns:* N/A
        *   **Usage:** This method is called by the AST NodeVisitor framework when traversing the AST and encountering an ImportFrom node.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and uses a custom `FileDependencyGraph` visitor to traverse the AST and identify import relationships. The visitor populates an internal dictionary of import dependencies. The function then iterates through these identified dependencies, adding nodes for both importing and imported files, and creating directed edges from the importer to the imported files. The resulting graph illustrates which files depend on others based on their import statements.
*   **Parameters:**
    - **filename** (`str`): The path to the file being analyzed for dependencies.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`networkx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies (from importer to imported).
*   **Usage:** This function is called by no other functions.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses its content to build a file-specific dependency graph using an external helper function. Finally, it aggregates all these individual file graphs into a single global directed graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The Git repository object from which to build the dependency graph.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependencies between Python files across the entire repository.
*   **Usage:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and returns a list of `Path` objects. The function first converts the input directory string into an absolute and canonical `Path` object. It then recursively searches for all files ending with ".py" within this root path. Finally, it returns these found file paths as a list, with each path made relative to the initial root directory.
*   **Parameters:**
    - **directory** (`str`): The path to the root directory to search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each path represents a Python file found within the specified directory, relative to the root directory.
*   **Usage:** This function is called by no other functions.

---

### File: `backend/HelperLLM.py`

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
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* This private method sets the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It uses a series of conditional statements to assign specific batch sizes for various known LLM models like different Gemini versions, Llama3, and GPT models. For unknown models or custom API models, it defaults to a conservative batch size of 2 or a larger size of 500, respectively, logging a warning if the model is unrecognized.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:* N/A
        *   **Usage:** This method is not explicitly called by other functions or methods based on the provided context.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* This method takes a list of `FunctionAnalysisInput` objects, converts them into JSON payloads, and then uses the configured `function_llm` to generate structured documentation for functions in batches. It iterates through the inputs, sending `BATCH_SIZE` conversations to the LLM concurrently, handles potential API errors by extending the results with `None` for failed items, and incorporates a waiting period between batches to respect rate limits. The method returns a list of `FunctionAnalysis` objects or `None` for failed generations.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary data for analyzing a single function.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, where each object represents the structured documentation for a function, or `None` if the analysis for a specific function failed.
        *   **Usage:** This method is not explicitly called by other functions or methods based on the provided context.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* This method is designed to generate structured documentation for a batch of classes. It takes a list of `ClassAnalysisInput` objects, serializes them into JSON, and then constructs conversations for the `class_llm`. The method processes these conversations in batches, sending them to the LLM, handling potential exceptions by marking failed items as `None`, and pausing between batches to manage API rate limits. It ultimately returns a list of `ClassAnalysis` objects or `None` for any failed analysis.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary data for analyzing a single class.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, where each object represents the structured documentation for a class, or `None` if the analysis for a specific class failed.
        *   **Usage:** This method is not explicitly called by other functions or methods based on the provided context.

#### Function: `main_orchestrator`
*   **Signature:* `def main_orchestrator()`
*   **Description:** This function serves as a dummy data and processing loop, primarily for testing the LLMHelper class. It defines pre-computed analysis inputs and outputs for several example functions, such as 'add_item', 'check_stock', and 'generate_report', using Pydantic models. It then instantiates an LLMHelper and simulates generating documentation for these functions, logging the process and displaying the final aggregated results. The function demonstrates how to use the `FunctionAnalysisInput` and `FunctionAnalysis` models.
*   **Parameters:** N/A
*   **Returns:** N/A
*   **Usage:** This function is called by no other functions.

---

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function generates a bar chart to visually compare the number of tokens between JSON and TOON formats. It takes the token counts for both formats, a savings percentage, and an output file path as input. The chart displays two bars, one for JSON tokens and one for TOON tokens, with their respective values shown above each bar. The chart is titled with the token comparison and the provided savings percentage, then saved to the specified output path before closing the plot.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated savings percentage to be displayed in the chart's title.
    - **output_path** (`str`): The file path where the generated bar chart image will be saved.
*   **Returns:** N/A
*   **Usage:** This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep durations, which are incurred due to rate-limiting, from the total elapsed time. It takes start and end times, total items, batch_size, and the model name as input. If the model is not a 'gemini-' model, it returns the total duration directly. Otherwise, it computes the number of batches and corresponding sleep time, then subtracts this from the total duration to yield the net time.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp or time value of the operation.
    - **end_time** (`float`): The ending timestamp or time value of the operation.
    - **total_items** (`int`): The total number of items processed during the operation.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model used, which determines if rate-limiting adjustments are applied.
*   **Returns:**
    - **net_time** (`float`): The calculated net duration of the operation, adjusted for estimated rate-limiting sleep times, or the total duration if no adjustment is needed.
*   **Usage:** This function is not explicitly called by any other functions in the provided context.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable | None)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing a software repository. It begins by parsing input to extract API keys, model configurations, and a GitHub repository URL. The repository is then cloned, and its contents are processed to extract basic project information, construct a file tree, perform relationship analysis, and generate an Abstract Syntax Tree (AST) schema. The AST schema is subsequently enriched with the extracted relationship data. Finally, the function prepares and dispatches analysis tasks to a Helper LLM for individual functions and classes, and then to a Main LLM to synthesize a final report, while also calculating token usage metrics.
*   **Parameters:**
    - **input** (`str`): The initial user input, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs ('scadsllm_base_url', 'ollama') required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used (e.g., 'gpt-5-mini', 'gpt-5.1').
    - **status_callback** (`callable | None`): An optional callback function used to provide status updates during the workflow execution.
*   **Returns:**
    - **result** (`dict`): A dictionary containing the 'report' (the final generated markdown report) and 'metrics' (a dictionary of performance and token usage statistics).
*   **Usage:** This function is called by no other functions.

---

### File: `database/db.py`

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** This function creates a new chat entry in the database. It constructs a chat document with a unique identifier generated by `uuid.uuid4()`, the provided username, the chat name, and the current timestamp using `datetime.now()`. The constructed chat document is then inserted into the `dbchats` collection. Finally, it returns the `_id` of the newly inserted chat document.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier of the newly created chat entry in the database.
*   **Usage:** This function is called by no other functions.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is designed to completely remove a specified chat and all its associated message exchanges from the database. It first deletes all message exchanges linked to the given username and chat name. Following this, it proceeds to delete the chat entry itself. This two-step deletion process ensures data consistency by preventing orphaned message records. The function returns the count of chat documents successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted from the database. This will typically be 1 if the chat was found and deleted, or 0 if it was not found.
*   **Usage:** This function is not explicitly called by any other functions in the provided context.

---
```markdown
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview (can be accessed under 'basic_info')
    - **Description:** Information not found
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** Information not found

*   **Repository Structure:**
    ```mermaid
    graph LR
        root -->|SystemPrompts, backend, database, frontend, notizen, result, schemas, output.json, output.toon, readme.md, requirements.txt, test.json, .env.example, .gitignore| directories_and_files
    
    directories_and_files -->|SystemPrompts| SystemPrompts_dir
    SystemPrompts_dir -->|SystemPromptClassHelperLLM.txt, SystemPromptFunctionHelperLLM.txt, SystemPromptHelperLLM.txt, SystemPromptMainLLM.txt, SystemPromptMainLLMToon.txt, SystemPromptNotebookLLM.txt| SystemPrompts_files
    
    directories_and_files -->|backend| backend_dir
    backend_dir -->|AST_Schema.py, File_Dependency.py, HelperLLM.py, MainLLM.py, __init__.py, basic_info.py, callgraph.py, converter.py, getRepo.py, main.py, relationship_analyzer.py, scads_key_test.py| backend_files
    
    directories_and_files -->|database| database_dir
    database_dir -->|db.py| database_files
    
    directories_and_files -->|frontend| frontend_dir
    frontend_dir -->|.streamlit, __init__.py, frontend.py, gifs| frontend_children
    .streamlit -->|config.toml| streamlit_config
    gifs -->|4j.gif| gifs_files
    
    directories_and_files -->|notizen| notizen_dir
    notizen_dir -->|Report Agenda.txt, Zwischenpraesentation Agenda.txt, doc_bestandteile.md, grafiken, notizen.md, paul_notizen.md, praesentation_notizen.md, technische_notizen.md| notizen_children
    grafiken -->|"1", "2", "Flask-Repo", "Repo-onboarding"| grafiken_subdirs
    "1" -->|"File_Dependency_Graph_Repo.dot, global_callgraph.png, global_graph.png, global_graph_2.png, repo.dot"| grafiken_1_files
    "2" -->|"FDG_repo.dot, fdg_graph.png, fdg_graph_2.png, filtered_callgraph_flask.png, filtered_callgraph_repo-agent.png, filtered_callgraph_repo-agent_3.png, filtered_repo_callgraph_flask.dot, filtered_repo_callgraph_repo-agent-3.dot, filtered_repo_callgraph_repo-agent.dot, global_callgraph.png, graph_flask.md, repo.dot"| grafiken_2_files
    "Flask-Repo" -->|... (65 files)| grafiken_flask_files
    "Repo-onboarding" -->|"AST.dot, Frontend.dot, HelperLLM.dot, HelperLLM.png, MainLLM.dot, agent.dot, basic_info.dot, callgraph.dot, getRepo.dot, graph_AST.png, graph_AST2.png, graph_AST3.png, main.dot, tools.dot, types.dot"| grafiken_repo_onboarding_files
    
    directories_and_files -->|result| result_dir
    result_dir -->|... (28 files)| result_files
    
    directories_and_files -->|schemas| schemas_dir
    schemas_dir -->|types.py| schemas_files
    
    directories_and_files -->|statistics| statistics_dir
    statistics_dir -->|"savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png, savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png, savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png, savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png, savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png"| statistics_files
    
    directories_and_files -->|analysis_output.json| analysis_output_json_file
    ```

    ## 2. Installation (can be accessed under 'basic_info')
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
    
    *   **If Repo contains requirements.txt:** pip install -r requirements.txt
    ### Setup Guide
    Information not found
    ### Quick Startup
    Information not found

    ## 3. Use Cases & Commands
    The Repo Onboarding Agent 🚀 appears to be a tool designed for analyzing GitHub repositories. It automates the process of cloning a repository, extracting key information such as project metadata, file structure, and code dependencies. It leverages Abstract Syntax Trees (AST) and Large Language Models (LLMs) to generate detailed analyses of functions, classes, and their relationships. The tool also converts Jupyter notebooks into an XML format and analyzes token usage for potential savings.

    Primary commands or functionalities would likely revolve around initiating the analysis process by providing a GitHub repository URL.

    ## 4. Architecture
    The Mermaid Syntax to visualize Graphs is not set up yet and will be added
    but if there is mermaid syntax in your input json display it here



    ## 5. Code Analysis

    ### File: `backend/AST_Schema.py`

    #### Class: `ASTVisitor`
    *   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to systematically traverse the Abstract Syntax Tree (AST) of a Python source file. Its primary purpose is to extract and organize structured information about imports, functions, and classes found within the analyzed code. It populates an internal `schema` dictionary with details such as identifiers, docstrings, and source code segments, providing a comprehensive representation of the code's structure. The visitor manages context to correctly associate methods with their parent classes and distinguishes between standalone functions and class methods.
    *   **Instantiation:** `backend.AST_Schema.ASTAnalyzer.analyze_repository`
    *   **Dependencies:** `backend.AST_Schema.path_to_module`
    *   **Constructor:**
        *   *Description:* The constructor initializes the ASTVisitor instance with the raw source code, the file's absolute path, and the project's root directory. It calculates the module path based on these inputs and sets up an empty `schema` dictionary to store parsed imports, functions, and classes. An internal `_current_class` attribute is also initialized to `None` to track the class currently being visited during AST traversal.
        *   *Parameters:*
            - **self** (ASTVisitor): The instance of the ASTVisitor class.
            - **source_code** (str): The raw string content of the Python source file being analyzed.
            - **file_path** (str): The absolute path to the Python file being processed.
            - **project_root** (str): The root directory of the entire project, used for calculating relative module paths.
    *   **Methods:**
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method is invoked by the `ast.NodeVisitor` framework when an `ast.Import` node is encountered, representing a simple `import module` statement. It iterates through each alias specified in the import node. For every alias, it extracts the module name and appends it to the `imports` list within the `self.schema` dictionary. After processing the import, it calls `self.generic_visit(node)` to ensure that any child nodes of the import statement are also visited.
            *   *Parameters:*
                - **self** (ASTVisitor): The instance of the ASTVisitor class.
                - **node** (ast.Import): The AST node representing an 'import' statement.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to `from module import name` statements. It processes each alias defined in the import statement. For each alias, it constructs a fully qualified import name by combining the module specified in `node.module` with the alias name, and then adds this string to the `imports` list in `self.schema`. Following this, `self.generic_visit(node)` is called to ensure proper traversal of any nested nodes.
            *   *Parameters:*
                - **self** (ASTVisitor): The instance of the ASTVisitor class.
                - **node** (ast.ImportFrom): The AST node representing a 'from ... import ...' statement.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* This method is responsible for processing `ast.ClassDef` nodes, which represent Python class definitions. It generates a unique identifier for the class and constructs a dictionary (`class_info`) containing comprehensive details such as the class name, its docstring, the exact source code segment, and its start and end line numbers. This `class_info` is then appended to the `classes` list within `self.schema`. To correctly associate methods with their parent class, `self._current_class` is temporarily set to this `class_info` before `self.generic_visit(node)` is called to traverse the class's body, and then reset to `None` afterwards.
            *   *Parameters:*
                - **self** (ASTVisitor): The instance of the ASTVisitor class.
                - **node** (ast.ClassDef): The AST node representing a class definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method processes `ast.FunctionDef` nodes, handling both standalone functions and methods defined within a class. It checks the `self._current_class` attribute to determine if the function is a method of an actively visited class. If it is a method, it creates `method_context_info` and appends it to the `method_context` of the `_current_class`. Otherwise, it treats the node as a standalone function, creating `func_info` with details like its identifier, name, arguments, docstring, source code, and line numbers, which is then appended to the `functions` list in `self.schema`. Finally, `self.generic_visit(node)` is called to continue the AST traversal.
            *   *Parameters:*
                - **self** (ASTVisitor): The instance of the ASTVisitor class.
                - **node** (ast.FunctionDef): The AST node representing a function or method definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_AsyncFunctionDef`**
            *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
            *   *Description:* This method is designed to handle `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation is concise, as it directly delegates the processing of the asynchronous function node to the `visit_FunctionDef` method. This approach ensures that both synchronous and asynchronous functions are analyzed using the same core logic, streamlining the visitor's functionality.
            *   *Parameters:*
                - **self** (ASTVisitor): The instance of the ASTVisitor class.
                - **node** (ast.AsyncFunctionDef): The AST node representing an asynchronous function definition.
            *   *Returns:*
            *   **Usage:**
    #### Class: `ASTAnalyzer`
    *   **Summary:** The ASTAnalyzer class is designed to process and analyze the Abstract Syntax Trees (ASTs) of Python files within a repository. It provides functionalities to parse source code, extract structured information about functions, classes, and imports using an ASTVisitor, and then integrate relationship data (like calls and dependencies) into the generated schema. Its primary role is to build a comprehensive, interconnected AST representation of a codebase.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `ast`, `os`, `backend.AST_Schema.ASTVisitor`, `getRepo.GitRepository`
    *   **Constructor:**
        *   *Description:* The constructor for the ASTAnalyzer class. It does not initialize any instance attributes, serving as a placeholder for potential future setup.
        *   *Parameters:*
    *   **Methods:**
        *   **`merge_relationship_data`**
            *   *Signature:* `def merge_relationship_data(self, full_schema, raw_relationships)`
            *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing calls, into an existing structured AST schema. It iterates through the functions and classes defined within the schema's files. For each function, it populates its 'calls' and 'called_by' context. For each class, it populates 'instantiated_by' and then iterates through its methods to populate their 'calls' and 'called_by' contexts, also identifying external class dependencies based on method calls.
            *   *Parameters:*
                - **self** (ASTAnalyzer): The instance of the ASTAnalyzer class.
                - **full_schema** (dict): The complete AST schema, typically containing 'files' with 'ast_nodes' for functions and classes.
                - **raw_relationships** (dict): A dictionary containing 'outgoing' and 'incoming' call relationships, mapping identifiers to lists of related entities.
            *   *Returns:*
                - **full_schema** (dict): The updated full schema with integrated relationship data for functions, classes, and methods.
            *   *Usage:*
        *   **`analyze_repository`**
            *   *Signature:* `def analyze_repository(self, files, repo)`
            *   *Description:* This method processes a list of file objects from a repository to construct a comprehensive AST schema. It filters for Python files, reads their content, and then uses the `ast` module to parse the code into an Abstract Syntax Tree. An `ASTVisitor` is then employed to traverse this tree and extract structured information about functions, classes, and imports, which is then aggregated into a `full_schema` dictionary. The method handles potential `SyntaxError` or `ValueError` exceptions during parsing.
            *   *Parameters:*
                - **self** (ASTAnalyzer): The instance of the ASTAnalyzer class.
                - **files** (list): A list of file objects, where each object is expected to have 'path' and 'content' attributes.
                - **repo** (GitRepository): An object representing the Git repository, though it is not directly used within this method's logic.
            *   *Returns:*
                - **full_schema** (dict): A dictionary representing the structured AST schema of the analyzed repository files.
            *   *Usage:*

    ### File: `backend/File_Dependency.py`

    #### Function: `build_file_dependency_graph`
    *   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
    *   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Abstract Syntax Tree (AST). It initializes an empty `networkx.DiGraph` and then uses a `FileDependencyGraph` visitor to traverse the provided AST. The visitor collects import relationships, which are then used to populate the graph. Each key in the collected dependencies represents a source file, and its corresponding values are the files it imports. The function adds nodes for both callers and callees, then creates directed edges from callers to their respective callees, finally returning the complete dependency graph.
    *   **Parameters:**
        - **filename** (str): The path to the file being analyzed.
        - **tree** (AST): The Abstract Syntax Tree (AST) of the file to be analyzed.
        - **repo_root** (str): The root directory of the repository, used for resolving relative paths.
    *   **Returns:**
        - **graph** (nx.DiGraph): A directed graph representing the file-level import dependencies.
    *   **Usage:**
    #### Function: `build_repository_graph`
    *   **Signature:** `def build_repository_graph(repository)`
    *   **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses the content and builds a file-specific dependency graph using an external helper function. Finally, it aggregates the nodes and edges from all individual file graphs into a single global directed graph, which is then returned.
    *   **Parameters:**
        - **repository** (GitRepository): The Git repository object from which to extract and analyze Python files for dependencies.
    *   **Returns:**
        - **global_graph** (nx.DiGraph): A NetworkX directed graph where nodes represent Python files or entities within them, and edges represent dependencies between them across the repository.
    *   **Usage:**
    #### Function: `get_all_temp_files`
    *   **Signature:** `def get_all_temp_files(directory)`
    *   **Description:** This function identifies all Python (.py) files within a specified directory and its subdirectories. It takes a directory path as input, resolves it to an absolute path, and then recursively searches for all files ending with '.py'. The function returns a list of these file paths, with each path represented as a pathlib.Path object relative to the initial root directory provided.
    *   **Parameters:**
        - **directory** (str): The path to the root directory from which to start searching for Python files.
    *   **Returns:**
        - **all_files** (list[Path]): A list of pathlib.Path objects, where each path represents a Python file found within the specified directory, relative to the root directory.
    *   **Usage:**
    #### Class: `FileDependencyGraph`
    *   **Summary:** The FileDependencyGraph class is an AST NodeVisitor designed to analyze Python source code files and build a graph of their import dependencies. It identifies both absolute and relative import statements, resolving relative paths to concrete module or symbol names within a given repository. The class maintains a dictionary, `import_dependencies`, to store which files import which modules, effectively mapping a file to its direct external dependencies.
    *   **Instantiation:** `backend.File_Dependency.build_file_dependency_graph`
    *   **Dependencies:** `get_all_temp_files`, `backend.File_Dependency.init_exports_symbol`, `backend.File_Dependency.module_file_exists`
    *   **Constructor:**
        *   *Description:* Initializes the FileDependencyGraph instance by storing the current filename and the repository root path. These attributes are crucial for resolving file paths and dependencies within the repository.
        *   *Parameters:*
            - **self** (FileDependencyGraph): The instance of the FileDependencyGraph class.
            - **filename** (str): The name of the file currently being processed for dependencies.
            - **repo_root** (str): The root directory of the repository.
    *   **Methods:**
        *   **`_resolve_module_name`**
            *   *Signature:* `def _resolve_module_name(self, node)`
            *   *Description:* This method resolves relative import statements (e.g., `from .. import name1`). It determines the actual module or symbol names that are being imported by navigating the file system relative to the current file and the specified import level. It checks for existing module files or symbols exported via `__init__.py` files. If no modules or symbols can be resolved, it raises an ImportError.
            *   *Parameters:*
                - **self** (FileDependencyGraph): The instance of the FileDependencyGraph class.
                - **node** (ImportFrom): An AST ImportFrom node representing the relative import statement to be resolved.
            *   *Returns:*
                - **resolved** (list[str]): A list of resolved module or symbol names.
            *   *Usage:*
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node, base_name=None)`
            *   *Description:* This method processes Import and ImportFrom AST nodes to record import dependencies. It adds the imported module or symbol name to the `import_dependencies` dictionary, mapping the current `self.filename` to a set of its direct dependencies. If a `base_name` is provided, it uses that; otherwise, it uses the alias name from the node. After processing, it calls `generic_visit` to continue AST traversal.
            *   *Parameters:*
                - **self** (FileDependencyGraph): The instance of the FileDependencyGraph class.
                - **node** (Import | ImportFrom): The AST node representing an import statement.
                - **base_name** (str | None): An optional base name for the module, used primarily for `from ... import ...` statements where the module part is explicitly resolved.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method is a specialized visitor for ImportFrom AST nodes. It handles both absolute and relative `from ... import ...` statements. For absolute imports, it extracts the base module name and delegates to `visit_Import`. For relative imports, it calls `_resolve_module_name` to determine the actual imported modules/symbols and then records them using `visit_Import`. It includes error handling for failed relative import resolutions.
            *   *Parameters:*
                - **self** (FileDependencyGraph): The instance of the FileDependencyGraph class.
                - **node** (ImportFrom): The AST node representing an `from ... import ...` statement.
            *   *Returns:*
            *   **Usage:**

    ### File: `backend/HelperLLM.py`

    #### Function: `main_orchestrator`
    *   **Signature:** `def main_orchestrator()`
    *   **Description:** This function serves as a dummy data and processing loop, primarily for testing the LLMHelper class. It defines pre-computed analysis examples for various functions like 'add_item', 'check_stock', and 'generate_report', validating them against Pydantic models. It then initializes an LLMHelper instance and simulates the generation of documentation for these functions, aggregating the results into a final documentation structure. The function demonstrates the expected input and output formats for the documentation generation process.
    *   **Parameters:**
    *   **Returns:**
    *   **Usage:**
    #### Class: `LLMHelper`
    *   **Summary:** The LLMHelper class serves as a robust interface for interacting with various Large Language Models (LLMs) to generate structured documentation for Python functions and classes. It centralizes the logic for API interaction, manages system prompts, and dynamically configures different LLM providers like Google Gemini, OpenAI, custom APIs, and Ollama. The class is designed to handle batch processing efficiently, incorporating error handling and rate-limiting to ensure reliable and structured data generation using Pydantic schemas.
    *   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
    *   **Dependencies:** `os`, `json`, `logging`, `time`, `typing.List`, `typing.Optional`, `dotenv.load_dotenv`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`, `pydantic.ValidationError`, `schemas.types.FunctionAnalysis`, `schemas.types.ClassAnalysis`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, `schemas.types.ClassAnalysisInput`, `schemas.types.ClassContextInput`
    *   **Constructor:**
        *   *Description:* This constructor initializes the LLMHelper instance by setting up the API key, loading system prompts for function and class analysis from specified file paths, and configuring the underlying Large Language Model (LLM) based on the `model_name`. It supports various LLM providers, dynamically setting up the appropriate `langchain` chat model, and initializes specialized LLM instances for structured function and class output.
        *   *Parameters:*
            - **self** (LLMHelper): The instance of the LLMHelper class.
            - **api_key** (str): The API key required for authenticating with the chosen LLM service.
            - **function_prompt_path** (str): The file path to the system prompt text used specifically for function analysis.
            - **class_prompt_path** (str): The file path to the system prompt text used specifically for class analysis.
            - **model_name** (str): The identifier for the LLM model to be used, defaulting to "gemini-2.0-flash-lite".
            - **base_url** (str | None): An optional base URL for custom LLM APIs or Ollama instances.
    *   **Methods:**
        *   **`_configure_batch_settings`**
            *   *Signature:* `def _configure_batch_settings(self, model_name)`
            *   *Description:* This private method dynamically sets the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It employs a series of conditional checks to assign specific batch sizes tailored for various known LLM models, optimizing for performance and adherence to API rate limits. For models not explicitly listed, it applies a conservative default batch size, ensuring efficient processing of LLM requests.
            *   *Parameters:*
                - **self** (LLMHelper): The instance of the LLMHelper class.
                - **model_name** (str): The name of the LLM model for which to configure the batch processing settings.
            *   *Returns:*
            *   **Usage:**
        *   **`generate_for_functions`**
            *   *Signature:* `def generate_for_functions(self, function_inputs)`
            *   *Description:* This method generates and validates structured documentation for a batch of functions using the configured LLM. It takes a list of `FunctionAnalysisInput` objects, serializes them into JSON payloads, and sends them to `self.function_llm` in batches. The method includes logging for progress and errors, handles potential API exceptions by returning `None` for failed items, and incorporates a `time.sleep` delay between batches to respect API rate limits, ensuring robust and efficient processing.
            *   *Parameters:*
                - **self** (LLMHelper): The instance of the LLMHelper class.
                - **function_inputs** (List[FunctionAnalysisInput]): A list of input objects, each containing the necessary data for a function to be analyzed and documented.
            *   *Returns:*
                - **None** (List[Optional[FunctionAnalysis]]): A list of `FunctionAnalysis` objects, where each object represents the structured documentation for a function, or `None` if an error occurred during its generation.
            *   *Usage:*
        *   **`generate_for_classes`**
            *   *Signature:* `def generate_for_classes(self, class_inputs)`
            *   *Description:* This method generates and validates structured documentation for a batch of classes using the configured LLM. It accepts a list of `ClassAnalysisInput` objects, converts them into JSON payloads, and dispatches them to `self.class_llm` in batches. The method incorporates comprehensive logging for operational transparency, robust error handling to manage API exceptions by returning `None` for problematic items, and a rate-limiting mechanism via `time.sleep` to ensure stable interaction with the LLM API.
            *   *Parameters:*
                - **self** (LLMHelper): The instance of the LLMHelper class.
                - **class_inputs** (List[ClassAnalysisInput]): A list of input objects, each containing the necessary data for a class to be analyzed and documented.
            *   *Returns:*
                - **None** (List[Optional[ClassAnalysis]]): A list of `ClassAnalysis` objects, where each object represents the structured documentation for a class, or `None` if an error occurred during its generation.
            *   *Usage:*

    ### File: `backend/MainLLM.py`

    #### Class: `MainLLM`
    *   **Summary:** The MainLLM class serves as a central interface for interacting with various Large Language Models (LLMs) by abstracting away the specifics of different providers like Google Generative AI, OpenAI-compatible APIs, or Ollama. It initializes an LLM client based on the model name and a system prompt loaded from a file. The class provides methods for both single-shot synchronous LLM calls and streaming responses, ensuring robust interaction with different LLM backends.
    *   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
    *   **Dependencies:** `logging`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`
    *   **Constructor:**
        *   *Description:* The constructor initializes the MainLLM class by setting up the system prompt from a file and configuring the appropriate LLM client (Google Generative AI, OpenAI, or Ollama) based on the `model_name` and provided API key. It handles different LLM providers and validates the API key and prompt file path, raising errors if essential information is missing or files are not found.
        *   *Parameters:*
            - **self** (MainLLM): The instance of the MainLLM class.
            - **api_key** (str): The API key required for authenticating with the chosen LLM service.
            - **prompt_file_path** (str): The file path to the system prompt that will be used as context for LLM interactions.
            - **model_name** (str): The name of the LLM model to be used, defaulting to 'gemini-2.5-pro'. This determines which LLM client is initialized.
            - **base_url** (str): An optional base URL for custom LLM APIs, used when the model name does not match predefined patterns for Gemini, GPT, or custom SCADSLLM models.
    *   **Methods:**
        *   **`call_llm`**
            *   *Signature:* `def call_llm(self, user_input)`
            *   *Description:* This method sends a user input along with the pre-configured system prompt to the initialized LLM and retrieves a single, complete response. It constructs a list of messages including the system prompt and the user's query, then invokes the LLM client. The method includes error handling for the LLM call and logs the process, returning the content of the response or None in case of an error.
            *   *Parameters:*
                - **self** (MainLLM): The instance of the MainLLM class.
                - **user_input** (str): The user's query or message to be sent to the LLM for a single response.
            *   *Returns:*
                - **content** (str): The content of the LLM's response if the call is successful, otherwise None.
            *   *Usage:*
        *   **`stream_llm`**
            *   *Signature:* `def stream_llm(self, user_input)`
            *   *Description:* This method interacts with the LLM to get a streaming response, yielding chunks of content as they become available. It prepares the messages similar to call_llm but utilizes the stream method of the LLM client, allowing for real-time display of the LLM's output. Error handling is included to catch exceptions during the streaming process and yield an error message.
            *   *Parameters:*
                - **self** (MainLLM): The instance of the MainLLM class.
                - **user_input** (str): The user's query or message for which a streaming response is desired from the LLM.
            *   *Returns:*
                - **chunk.content** (str): Yields chunks of the LLM's response content as they are generated during the stream.
                - **error_message** (str): Yields an error message string if an exception occurs during the LLM stream call.
            *   *Usage:*

    ### File: `backend/basic_info.py`

    #### Class: `ProjektInfoExtractor`
    *   **Summary:** The ProjektInfoExtractor class is designed to extract fundamental project details from common project files such as READMEs, pyproject.toml, and requirements.txt. It initializes a structured dictionary to hold various project information, populating it by parsing different file types. The class prioritizes information from pyproject.toml, then requirements.txt, and finally README files, ensuring a comprehensive overview of a project's metadata, installation instructions, and features.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* The constructor initializes the `ProjektInfoExtractor` instance by setting a default 'Information not found' string and creating a nested dictionary `self.info`. This dictionary serves as a structured container for various project details, including project overview (title, description, status, features, tech stack) and installation information (dependencies, setup guide, quick start guide), all initially set to the 'not found' placeholder.
        *   *Parameters:*
    *   **Methods:**
        *   **`_clean_content`**
            *   *Signature:* `def _clean_content(self, content)`
            *   *Description:* This private method is responsible for cleaning a given string content by removing null bytes. Null bytes can often appear due to encoding errors, particularly when a file encoded in UTF-16 is incorrectly read as UTF-8. The method ensures that the content is free from these problematic characters before further processing, returning an empty string if the input content is empty.
            *   *Parameters:*
                - **self** (ProjektInfoExtractor): The instance of the ProjektInfoExtractor class.
                - **content** (str): The string content to be cleaned.
            *   *Returns:*
                - **cleaned_content** (str): The content string with all null bytes removed.
            *   *Usage:*
        *   **`_finde_datei`**
            *   *Signature:* `def _finde_datei(self, patterns, dateien)`
            *   *Description:* This private method searches through a list of file objects to find one that matches any of the provided patterns. The search is case-insensitive, comparing the lowercased file path against lowercased patterns. It iterates through each file and each pattern, returning the first file object that satisfies a match, or None if no matching file is found.
            *   *Parameters:*
                - **self** (ProjektInfoExtractor): The instance of the ProjektInfoExtractor class.
                - **patterns** (List[str]): A list of string patterns to match against file paths.
                - **dateien** (List[Any]): A list of file-like objects, each expected to have a 'path' attribute.
            *   *Returns:*
                - **matching_file** (Optional[Any]): The first file object that matches a pattern, or None if no match is found.
            *   *Usage:*
        *   **`_extrahiere_sektion_aus_markdown`**
            *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
            *   *Description:* This private method extracts text content located under a Markdown H2 heading, identified by a list of keywords. It constructs a regular expression pattern to find headings like '## Keyword' and then captures all content following it until the next H2 heading or the end of the file. The search is case-insensitive and handles multi-line content, returning the stripped section or None if no matching section is found.
            *   *Parameters:*
                - **self** (ProjektInfoExtractor): The instance of the ProjektInfoExtractor class.
                - **inhalt** (str): The Markdown content string to parse.
                - **keywords** (List[str]): A list of keywords to match against H2 headings.
            *   *Returns:*
                - **extracted_section** (Optional[str]): The stripped text content under the matched H2 heading, or None.
            *   *Usage:*
        *   **`_parse_readme`**
            *   *Signature:* `def _parse_readme(self, inhalt)`
            *   *Description:* This private method parses the content of a README file to extract various project details and populate the `self.info` dictionary. It first cleans the content, then attempts to find the project title and a fallback description using regular expressions. Subsequently, it utilizes the `_extrahiere_sektion_aus_markdown` method to extract specific sections like Key Features, Tech Stack, Status, Installation instructions, and Quick Start guides, updating the `self.info` dictionary if information is found and not already populated.
            *   *Parameters:*
                - **self** (ProjektInfoExtractor): The instance of the ProjektInfoExtractor class.
                - **inhalt** (str): The content of the README file as a string.
            *   *Returns:*
            *   **Usage:**
        *   **`_parse_toml`**
            *   *Signature:* `def _parse_toml(self, inhalt)`
            *   *Description:* This private method parses the content of a `pyproject.toml` file to extract project-level information. It first cleans the input content and checks if the `tomllib` module is available. If `tomllib` is present, it attempts to load the TOML content, then extracts the project name, description, and dependencies from the 'project' table, updating the `self.info` dictionary accordingly. It includes error handling for `TOMLDecodeError` to gracefully manage malformed TOML files.
            *   *Parameters:*
                - **self** (ProjektInfoExtractor): The instance of the ProjektInfoExtractor class.
                - **inhalt** (str): The content of the pyproject.toml file as a string.
            *   *Returns:*
            *   **Usage:**
        *   **`_parse_requirements`**
            *   *Signature:* `def _parse_requirements(self, inhalt)`
            *   *Description:* This private method parses the content of a `requirements.txt` file to extract project dependencies. It first cleans the input content. It only proceeds to extract dependencies if the `self.info` dictionary's 'dependencies' field is still set to the 'Information not found' placeholder, indicating that dependencies were not already found from a `pyproject.toml` file. It processes each line, filtering out empty lines and comments, and populates the `self.info` dictionary with the list of identified dependencies.
            *   *Parameters:*
                - **self** (ProjektInfoExtractor): The instance of the ProjektInfoExtractor class.
                - **inhalt** (str): The content of the requirements.txt file as a string.
            *   *Returns:*
            *   **Usage:**
        *   **`extrahiere_info`**
            *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
            *   *Description:* This public method orchestrates the entire information extraction process for a project. It first identifies relevant project files (README, pyproject.toml, requirements.txt) from a given list of file objects. It then parses these files in a prioritized order: pyproject.toml first, then requirements.txt, and finally README.md, allowing later parsers to fill in gaps if earlier ones didn't provide specific information. Finally, it formats the extracted dependencies and derives a project title from the repository URL if no title was found, returning the complete `self.info` dictionary.
            *   *Parameters:*
                - **self** (ProjektInfoExtractor): The instance of the ProjektInfoExtractor class.
                - **dateien** (List[Any]): A list of file-like objects, each containing content and a path.
                - **repo_url** (str): The URL of the repository, used as a fallback for the project title.
            *   *Returns:*
                - **project_info** (Dict[str, Any]): A dictionary containing all extracted project information.
            *   *Usage:*

    ### File: `backend/callgraph.py`

    #### Function: `make_safe_dot`
    *   **Signature:** `def make_safe_dot(graph, out_path)`
    *   **Description:** The `make_safe_dot` function takes a NetworkX directed graph and an output file path. Its main purpose is to prepare the graph for DOT visualization by ensuring all node identifiers are safe for DOT rendering. It achieves this by creating a copy of the input graph and relabeling all nodes with simple, sequential identifiers like 'n0', 'n1', etc. The original node names are then stored as 'label' attributes on these new, safe nodes, preserving the original context for visualization. Finally, the modified graph is written to the specified file path in DOT format using `nx.drawing.nx_pydot.write_dot`.
    *   **Parameters:**
        - **graph** (nx.DiGraph): The input directed graph to be processed and made safe for DOT representation.
        - **out_path** (str): The file path where the DOT formatted graph will be written.
    *   **Returns:**
    *   **Usage:**
    #### Function: `build_filtered_callgraph`
    *   **Signature:** `def build_filtered_callgraph(repo)`
    *   **Description:** This function constructs a directed call graph for Python files within a given Git repository. It first identifies all 'self-written' functions across all Python files by parsing their Abstract Syntax Trees (ASTs) using a CallGraph visitor. Subsequently, it iterates through the parsed file trees again to identify call relationships. Only calls where both the caller and the callee are identified as 'self-written' functions are included in the final graph. The function returns a networkx.DiGraph representing these filtered call relationships.
    *   **Parameters:**
        - **repo** (GitRepository): The Git repository object containing the source code files to analyze.
    *   **Returns:**
        - **global_graph** (networkx.DiGraph): A directed graph representing the call relationships between 'self-written' functions found within the repository.
    *   **Usage:**
    #### Class: `CallGraph`
    *   **Summary:** The CallGraph class is an ast.NodeVisitor subclass designed to construct a call graph for a given Python source file. It systematically traverses the Abstract Syntax Tree (AST) of a Python file, identifying function and class definitions, import statements, and function calls. By maintaining internal state such as current_function and current_class, and using helper methods to resolve names and build fully qualified identifiers, it maps calls between functions and methods. The class ultimately populates a networkx.DiGraph with nodes representing functions and edges representing calls, along with auxiliary data structures for imports and local definitions.
    *   **Instantiation:** `backend.callgraph.build_filtered_callgraph`
    *   **Dependencies:** `backend.callgraph.CallGraph`
    *   **Constructor:**
        *   *Description:* The constructor initializes the CallGraph instance by setting up various internal data structures and state variables. It stores the filename being analyzed, initializes current_function and current_class to None, and creates dictionaries for local_defs and import_mapping, a networkx.DiGraph for graph, a set for function_set, and a dictionary for edges. These attributes are crucial for tracking definitions, imports, and building the call graph.
        *   *Parameters:*
            - **self** (CallGraph): The instance of the CallGraph class.
            - **filename** (str): The path to the file being analyzed, used to qualify function names.
    *   **Methods:**
        *   **`_recursive_call`**
            *   *Signature:* `def _recursive_call(self, node)`
            *   *Description:* This private helper method recursively traverses an Abstract Syntax Tree (AST) node to extract the full dotted name components of a function call. It handles ast.Call nodes by recurring on the func attribute, ast.Name nodes by returning their id, and ast.Attribute nodes by combining the parts from the value and attr. The method aims to decompose complex call expressions into a list of name parts, such as ['pkg', 'mod', 'Class', 'method'].
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **node** (ast.AST): The AST node representing a call expression or part of it.
            *   *Returns:*
                - **name** (list[str]): A list of string components representing the dotted name of the call.
            *   *Usage:*
        *   **`_resolve_all_callee_names`**
            *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
            *   *Description:* This private helper method takes a list of potential callee name components (e.g., [['module', 'function'], ['Class', 'method']]) and attempts to resolve them into fully qualified names. It prioritizes resolving names against self.local_defs (local function/method definitions) first, then self.import_mapping (imported modules/objects). If a name cannot be resolved locally or via imports, it constructs a full name using the current filename and current_class context. The goal is to provide a canonical, fully qualified name for each called entity.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **callee_nodes** (list[list[str]]): A list where each inner list represents the name components of a potential callee.
            *   *Returns:*
                - **name** (list[str]): A list of fully qualified string names for the resolved callees.
            *   *Usage:*
        *   **`_make_full_name`**
            *   *Signature:* `def _make_full_name(self, basename, class_name=None)`
            *   *Description:* This private helper method constructs a fully qualified name for a function or method. It takes a basename (the function/method's local name) and an optional class_name. If class_name is provided, the full name is formatted as filename::class_name::basename; otherwise, it's filename::basename. This ensures that all functions and methods within the call graph have unique, globally identifiable names.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **basename** (str): The local name of the function or method.
                - **class_name** (str | None): The name of the class if the entity is a method, or None if it's a top-level function.
            *   *Returns:*
                - **name** (str): The fully qualified name of the function or method.
            *   *Usage:*
        *   **`_current_caller`**
            *   *Signature:* `def _current_caller(self)`
            *   *Description:* This private helper method determines the fully qualified name of the current caller context. If self.current_function is set, it returns that value, indicating the AST visitor is currently inside a function definition. Otherwise, it returns a string representing the global scope, either <filename> if a filename is available, or <global-scope> as a fallback. This method is crucial for identifying the source of a call within the AST traversal.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
            *   *Returns:*
                - **name** (str): The fully qualified name of the current calling context (function or global scope).
            *   *Usage:*
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method is an AST visitor for ast.Import nodes. It processes 'import module as alias' statements. For each alias, it maps the asname (or original name if no asname is present) to the actual module_name in self.import_mapping. This mapping is essential for resolving imported call targets later. After processing, it calls self.generic_visit(node) to continue traversing the AST.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **node** (ast.Import): The AST node representing an import statement.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method is an AST visitor for ast.ImportFrom nodes, handling 'from module import name as alias' statements. It extracts the base module name from node.module and then iterates through the imported names. For each alias, it maps the asname (or original name) to the extracted module_name or the alias's name itself if the module name is empty. This populates self.import_mapping to aid in resolving fully qualified names for imported entities.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **node** (ast.ImportFrom): The AST node representing a 'from ... import ...' statement.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* This method is an AST visitor for ast.ClassDef nodes. It manages the self.current_class state to correctly contextualize methods defined within a class. Before traversing the class body, it saves the previous current_class and sets self.current_class to the name of the current class. After visiting all child nodes within the class, it restores the current_class to its previous value, ensuring proper scope management during AST traversal.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **node** (ast.ClassDef): The AST node representing a class definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method is an AST visitor for ast.FunctionDef nodes, handling both regular and async function definitions. It generates a fully qualified name for the function using _make_full_name and stores it in self.local_defs. It also updates self.current_function to reflect the current scope, adds the function as a node to self.graph, and ensures the function's full name is added to self.function_set. The method manages the current_function state by saving and restoring it, allowing for correct nesting of function definitions.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **node** (ast.FunctionDef): The AST node representing a function definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_AsyncFunctionDef`**
            *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
            *   *Description:* This method is an AST visitor for ast.AsyncFunctionDef nodes. It simply delegates its processing to the visit_FunctionDef method. This indicates that asynchronous function definitions are treated identically to regular function definitions for the purpose of call graph construction, specifically regarding name resolution and graph node creation.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **node** (ast.AsyncFunctionDef): The AST node representing an asynchronous function definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_Call`**
            *   *Signature:* `def visit_Call(self, node)`
            *   *Description:* This method is an AST visitor for ast.Call nodes, which represent function or method calls. It first identifies the caller using _current_caller and then extracts the callee's name components using _recursive_call. These components are then resolved into fully qualified names using _resolve_all_callee_names. Finally, it records the call by adding an edge from the caller to each resolved_callee in the self.edges dictionary, effectively building the call graph.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **node** (ast.Call): The AST node representing a function or method call.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_If`**
            *   *Signature:* `def visit_If(self, node)`
            *   *Description:* This method is an AST visitor for ast.If nodes. It includes special handling for the common 'if __name__ == "__main__":' block. If such a block is detected, it temporarily sets self.current_function to "<main_block>" before traversing the if block's body. This ensures that any calls within the main execution block are attributed to a distinct "main_block" caller. After traversing, it restores the current_function to its previous state. For other if statements, it simply performs a generic visit.
            *   *Parameters:*
                - **self** (CallGraph): The instance of the CallGraph class.
                - **node** (ast.If): The AST node representing an if statement.
            *   *Returns:*
            *   **Usage:**

    ### File: `backend/converter.py`

    #### Function: `wrap_cdata`
    *   **Signature:** `def wrap_cdata(content)`
    *   **Description:** The `wrap_cdata` function takes a single string argument, `content`, and encapsulates it within XML CDATA tags. This process ensures that the enclosed content is treated as character data, preventing XML parsers from interpreting it as markup. The function constructs an f-string to format the output, including newline characters around the content for readability within the CDATA block.
    *   **Parameters:**
        - **content** (str): The string content to be wrapped inside the CDATA block.
    *   **Returns:**
        - **wrapped_content** (str): A new string containing the original content enclosed within `<![CDATA[\n...\n]]>` tags.
    *   **Usage:**
    #### Function: `extract_output_content`
    *   **Signature:** `def extract_output_content(outputs, image_list)`
    *   **Description:** This function processes a list of notebook output objects to extract various content types, including text, images, stream data, and error messages. It iterates through each output, identifying its type. For display or execution results, it prioritizes extracting PNG images, falling back to JPEG, and stores their base64 data in the provided image_list while adding an XML placeholder to the result. If no image is found, it extracts plain text. Stream outputs are appended directly, and error outputs are formatted as strings. The function returns a list of these extracted content snippets.
    *   **Parameters:**
        - **outputs** (list): A list of output objects, typically from a notebook execution, which can contain display data, execution results, stream data, or error information.
        - **image_list** (list): A mutable list that is populated with dictionaries, each containing the mime type and base64 encoded data of any images found in the outputs.
    *   **Returns:**
        - **extracted_xml_snippets** (list[str]): A list of strings, where each string represents extracted text content, an XML placeholder for an image, or a formatted error message.
    *   **Usage:**
    #### Function: `process_image`
    *   **Signature:** `def process_image(mime_type)`
    *   **Description:** This function is designed to process image data associated with a given MIME type. It attempts to retrieve a base64 encoded image string from an external "data" dictionary, clean it by removing newline characters, and then store it along with its MIME type in an external "image_list". Upon successful processing, it returns a formatted string serving as an image placeholder. If an exception occurs during image decoding, an error message string is returned. If the specified MIME type is not found in "data", the function returns None.
    *   **Parameters:**
        - **mime_type** (str): The MIME type string used to identify and retrieve the corresponding image data.
    *   **Returns:**
        - **image_placeholder_or_error** (str | None): Returns a formatted string representing an image placeholder if successful, an error message string if decoding fails, or None if the MIME type is not found in the external data source.
    *   **Usage:**
    *   **Warning:** The function references undeclared variables "data" and "image_list", which are not passed as parameters or defined within its local scope. This makes the function's execution context ambiguous without further information about its enclosing scope or global environment.
    #### Function: `convert_notebook_to_xml`
    *   **Signature:** `def convert_notebook_to_xml(file_content)`
    *   **Description:** This function converts the raw string content of a Jupyter notebook into a structured XML representation. It parses the notebook, iterates through its cells, and formats them into XML tags. Markdown cells are embedded directly, while code cells are wrapped in CDATA and their outputs are processed to extract content and images, which are also wrapped in CDATA. The function handles potential parsing errors by returning a specific error message.
    *   **Parameters:**
        - **file_content** (str): The raw string content of a Jupyter notebook file, expected to be in JSON format.
    *   **Returns:**
        - **xml_output_or_error** (str): The XML representation of the notebook cells if successful, or an error message string if the input `file_content` cannot be parsed as a notebook.
        - **extracted_images** (list): A list of image data extracted from the notebook's code cell outputs. This list will be empty if no images are found or if an error occurred during parsing.
    *   **Usage:**
    #### Function: `process_repo_notebooks`
    *   **Signature:** `def process_repo_notebooks(repo_files)`
    *   **Description:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It filters the input list to find files ending with '.ipynb' and then iterates through each identified notebook. For every notebook, it calls an external function, `convert_notebook_to_xml`, to transform its content into an XML representation and extract any associated images. The function logs its progress and finally returns a dictionary mapping each notebook's path to its generated XML output and extracted images.
    *   **Parameters:**
        - **repo_files** (List[Any]): An iterable collection of file-like objects from a repository. Each object is expected to have a 'path' attribute (string) to identify notebook files and a 'content' attribute (string) containing the notebook's raw data.
    *   **Returns:**
        - **results** (Dict[str, Dict[str, Any]]): A dictionary where keys are the paths (string) of the processed Jupyter notebooks. Each value is another dictionary containing two keys: 'xml' (string, the XML representation of the notebook) and 'images' (Any, the extracted images from the notebook).
    *   **Usage:**

    ### File: `backend/getRepo.py`

    #### Class: `RepoFile`
    *   **Summary:** The RepoFile class represents a single file within a Git repository, providing a structured interface to access its metadata and content. It implements a lazy-loading mechanism for the Git blob, file content, and size, ensuring these resources are only fetched when needed. The class offers properties to retrieve the underlying Git blob, the decoded file content, and its size, along with utility methods for basic analysis and conversion to a dictionary format.
    *   **Instantiation:** `backend.getRepo.GitRepository.get_all_files`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* The `__init__` method initializes a RepoFile object by storing the file's path and the Git Tree object from which it originates. It sets up internal attributes (`_blob`, `_content`, `_size`) to `None`, indicating that these resources will be lazy-loaded upon first access.
        *   *Parameters:*
            - **self** (RepoFile): The instance of the RepoFile class.
            - **file_path** (str): The path to the file within the repository.
            - **commit_tree** (git.Tree): The Tree-object of the commit from which the file originates.
    *   **Methods:**
        *   **`blob`**
            *   *Signature:* `def blob(self)`
            *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if the `_blob` attribute is already set; if not, it attempts to retrieve the blob from the `_tree` using the file's path. If the file is not found in the commit tree, it raises a `FileNotFoundError`.
            *   *Parameters:*
            *   *Returns:*
                - **None** (git.Blob): The Git blob object representing the file.
            *   *Usage:*
        *   **`content`**
            *   *Signature:* `def content(self)`
            *   *Description:* This property provides lazy loading for the decoded content of the file. It first checks if the `_content` attribute is already populated. If not, it accesses the `blob` property to get the Git blob, reads its data stream, and decodes it using UTF-8, ignoring errors.
            *   *Parameters:*
            *   *Returns:*
                - **None** (str): The decoded content of the file as a string.
            *   *Usage:*
        *   **`size`**
            *   *Signature:* `def size(self)`
            *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the `_size` attribute is already set. If not, it accesses the `blob` property to get the Git blob and retrieves its `size` attribute.
            *   *Parameters:*
            *   *Returns:*
                - **None** (int): The size of the file in bytes.
            *   *Usage:*
        *   **`analyze_word_count`**
            *   *Signature:* `def analyze_word_count(self)`
            *   *Description:* This method serves as an example analysis method, calculating and returning the total number of words present in the file's content. It achieves this by accessing the `content` property, splitting the string by whitespace, and then counting the resulting elements.
            *   *Parameters:*
                - **self** (RepoFile): The instance of the RepoFile class.
            *   *Returns:*
                - **None** (int): The total word count of the file content.
            *   *Usage:*
        *   **`__repr__`**
            *   *Signature:* `def __repr__(self)`
            *   *Description:* This special method provides a developer-friendly string representation of the `RepoFile` object. It returns a string that includes the class name and the path of the file it represents, making it useful for debugging and logging.
            *   *Parameters:*
                - **self** (RepoFile): The instance of the RepoFile class.
            *   *Returns:*
                - **None** (str): A string representation of the RepoFile object, including its path.
            *   *Usage:*
        *   **`to_dict`**
            *   *Signature:* `def to_dict(self, include_content=False)`
            *   *Description:* This method converts the `RepoFile` object into a dictionary representation. It includes the file's path, name (extracted from the path), size, and type. Optionally, it can also include the file's content if `include_content` is set to `True`.
            *   *Parameters:*
                - **self** (RepoFile): The instance of the RepoFile class.
                - **include_content** (bool): A flag indicating whether to include the file's content in the output dictionary. Defaults to `False`.
            *   *Returns:*
                - **data** (dict): A dictionary representation of the file, optionally including its content.
            *   *Usage:*
    #### Class: `GitRepository`
    *   **Summary:** The GitRepository class provides a robust mechanism for interacting with Git repositories programmatically. It handles the cloning of a remote repository into a temporary local directory, ensuring isolation and easy cleanup. The class allows for the retrieval of all files within the repository as RepoFile objects and can generate a hierarchical tree structure of these files. Furthermore, it implements the context manager protocol, guaranteeing that the temporary directory is properly cleaned up upon exiting a 'with' block, even if errors occur.
    *   **Instantiation:** `backend.main.main_workflow`, `backend.main.notebook_workflow`
    *   **Dependencies:** `backend.getRepo.RepoFile`
    *   **Constructor:**
        *   *Description:* Initializes the GitRepository by cloning a specified Git repository into a temporary directory. It sets up instance attributes for the repository URL, the temporary directory path, the GitPython Repo object, and initializes lists for files. It also captures the latest commit and its tree for file access, handling potential cloning errors.
        *   *Parameters:*
            - **self** (GitRepository): The instance of the GitRepository class.
            - **repo_url** (str): The URL of the Git repository to clone.
    *   **Methods:**
        *   **`get_all_files`**
            *   *Signature:* `def get_all_files(self)`
            *   *Description:* This method retrieves all file paths from the cloned Git repository using Git's 'ls-files' command. It then iterates through these paths, creating a RepoFile object for each file, associating it with the repository's commit tree. Finally, it stores these RepoFile instances in the self.files attribute and returns the list.
            *   *Parameters:*
                - **self** (GitRepository): The instance of the GitRepository class.
            *   *Returns:*
                - **files** (list[RepoFile]): A list of RepoFile instances representing all files in the repository.
            *   *Usage:*
        *   **`close`**
            *   *Signature:* `def close(self)`
            *   *Description:* This method is responsible for cleaning up resources used by the GitRepository instance. Specifically, it checks if a temporary directory (self.temp_dir) exists and, if so, prints a message indicating its deletion. It then sets self.temp_dir to None, effectively marking the directory for cleanup.
            *   *Parameters:*
                - **self** (GitRepository): The instance of the GitRepository class.
            *   *Returns:*
            *   **Usage:**
        *   **`__enter__`**
            *   *Signature:* `def __enter__(self)`
            *   *Description:* This special method allows the GitRepository class to be used as a context manager. When entering a 'with' statement, this method is automatically invoked. It simply returns the instance of the GitRepository itself, making it available as the 'as' target in the 'with' statement.
            *   *Parameters:*
                - **self** (GitRepository): The instance of the GitRepository itself.
            *   *Returns:*
                - **self** (GitRepository): The instance of the GitRepository itself.
            *   *Usage:*
        *   **`__exit__`**
            *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
            *   *Description:* This special method is part of the context manager protocol. It is automatically called when exiting a 'with' statement, regardless of whether an exception occurred. Its primary responsibility is to ensure that the 'close' method is invoked, which handles the cleanup of the temporary directory used for the cloned repository.
            *   *Parameters:*
                - **self** (GitRepository): The instance of the GitRepository class.
                - **exc_type** (type): The type of the exception that caused the exit, or None if no exception occurred.
                - **exc_val** (Exception): The exception instance, or None.
                - **exc_tb** (traceback): The traceback object, or None.
            *   *Returns:*
            *   **Usage:**
        *   **`get_file_tree`**
            *   *Signature:* `def get_file_tree(self, include_content=False)`
            *   *Description:* This method constructs a hierarchical tree representation of the repository's files. If self.files is not already populated, it first calls get_all_files to retrieve them. It then iterates through each RepoFile object, splitting its path to build a nested dictionary structure representing directories and files. Each file is added to its respective directory level, optionally including its content.
            *   *Parameters:*
                - **self** (GitRepository): The instance of the GitRepository class.
                - **include_content** (bool): A flag indicating whether the content of each file should be included in its dictionary representation. Defaults to False.
            *   *Returns:*
                - **tree** (dict): A dictionary representing the hierarchical file tree of the repository, with directories and files nested.
            *   *Usage:*

    ### File: `backend/main.py`

    #### Function: `create_savings_chart`
    *   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
    *   **Description:** This function generates a bar chart to visually compare two token counts, specifically 'JSON' and 'TOON' tokens. It displays a calculated savings percentage in the chart's title. The function then saves the generated plot as an image file to a specified output path and ensures the plot is closed to free up resources.
    *   **Parameters:**
        - **json_tokens** (int): The number of tokens representing the JSON format.
        - **toon_tokens** (int): The number of tokens representing the TOON format.
        - **savings_percent** (float): The calculated percentage of savings to be displayed in the chart title.
        - **output_path** (str): The file path where the generated bar chart image will be saved.
    *   **Returns:**
    *   **Usage:**
    #### Function: `calculate_net_time`
    *   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
    *   **Description:** This function calculates the net processing time between a start and end time, specifically adjusting for rate-limit induced sleep times when a 'gemini-' model is used. It first determines the total duration. If the model is not a 'gemini-' model, the raw total duration is returned. For 'gemini-' models, it calculates the number of batches based on total items and batch size, then estimates the total sleep time by assuming 61 seconds per sleep interval between batches. Finally, it subtracts the estimated total sleep time from the total duration, ensuring the net time is not negative.
    *   **Parameters:**
        - **start_time** (datetime.datetime | float): The starting timestamp or datetime object for the operation.
        - **end_time** (datetime.datetime | float): The ending timestamp or datetime object for the operation.
        - **total_items** (int): The total number of items processed during the operation.
        - **batch_size** (int): The number of items processed in each batch.
        - **model_name** (str): The name of the model used, which determines if rate-limit adjustments are applied.
    *   **Returns:**
        - **net_time** (float | int): The calculated net processing time, adjusted for rate-limit induced sleep times, or the total duration if no adjustments are needed. Returns 0 if total_items is 0 or if the net time calculation results in a negative value.
    *   **Usage:**
    #### Function: `main_workflow`
    *   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback=None)`
    *   **Description:** This function orchestrates a comprehensive project analysis workflow. It begins by extracting API keys and model configurations, then parses a GitHub repository URL from the provided input. The workflow proceeds to clone the repository, extract basic project information, and construct a file tree. It performs a detailed relationship analysis and generates an Abstract Syntax Tree (AST) schema, which is then enriched with the relationship data. Finally, it prepares and dispatches analysis tasks to a Helper LLM for functions and classes, and a Main LLM for generating a final report, including token usage metrics and saving the results.
    *   **Parameters:**
        - **input** (str): The initial user input string, which is expected to contain a GitHub repository URL for analysis.
        - **api_keys** (dict): A dictionary containing various API keys (e.g., for Gemini, GPT, SCADSLLM) and base URLs required for interacting with different language models.
        - **model_names** (dict): A dictionary specifying the names of the "helper" and "main" LLM models to be utilized throughout the analysis process.
        - **status_callback** (callable): An optional callable function that, if provided, will be invoked with status messages to report progress during the workflow execution.
    *   **Returns:**
        - **report** (str): A string containing the final generated project analysis report, typically in Markdown format.
        - **metrics** (dict): A dictionary providing performance and usage statistics, including execution times for helper and main LLMs, model names used, and token savings data.
    *   **Usage:**
    #### Function: `update_status`
    *   **Signature:** `def update_status(msg)`
    *   **Description:** The `update_status` function is designed to process and display status messages. It takes a message string as input. If a `status_callback` function is available in the current scope, it invokes this callback with the provided message, presumably to update a UI or external system. Additionally, it logs the message at the INFO level using the `logging` module, ensuring that the status update is recorded.
    *   **Parameters:**
        - **msg** (str): The status message to be processed, displayed, or logged.
    *   **Returns:**
    *   **Usage:**
    #### Function: `notebook_workflow`
    *   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
    *   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks from a given GitHub repository using a Large Language Model (LLM). It begins by extracting a repository URL from the input, cloning the repository, and processing its notebook files into an XML format. It then extracts basic project information and initializes an LLM client based on the specified model and API keys. The function iterates through each processed notebook, constructs a specific payload (including text and embedded images), calls the LLM to generate a report for each, and aggregates these individual reports into a final comprehensive document. Finally, it saves this report to a timestamped file and returns the report along with execution metrics.
    *   **Parameters:**
        - **input** (str): The input string, expected to contain a GitHub repository URL.
        - **api_keys** (dict): A dictionary containing API keys for various LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
        - **model** (str): The name of the LLM model to be used for generating reports (e.g., 'gpt-4', 'gemini-pro').
        - **status_callback** (callable | None): An optional callback function to provide real-time status updates during the workflow execution.
    *   **Returns:**
        - **result** (dict): A dictionary containing the final aggregated report and execution metrics. It includes 'report' (str) with the concatenated markdown reports and 'metrics' (dict) with performance data.
    *   **Usage:**
    #### Function: `gemini_payload`
    *   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
    *   **Description:** This function constructs a Gemini-compatible payload by processing various input components. It serializes basic information and a notebook path into an introductory JSON string. It then parses an XML content string, extracting both plain text segments and image placeholders. For each identified image placeholder, it retrieves the corresponding base64-encoded image data from a provided list and embeds it with the correct MIME type. The function combines these text and image parts into a structured list of dictionaries, which represents the final payload content.
    *   **Parameters:**
        - **basic_info** (object): A dictionary or object containing basic information to be included in the payload's context.
        - **nb_path** (str): The current notebook's file path, which is included in the payload's context.
        - **xml_content** (str): An XML string that may contain text and image placeholders to be parsed and included in the payload.
        - **images** (list): A list of image data objects, where each object is expected to contain a 'data' key with a base64 string. Images are referenced by index from the `xml_content`.
    *   **Returns:**
        - **payload_content** (list): A list of dictionaries, where each dictionary represents a content part for a Gemini payload. Parts can be of type 'text' or 'image_url', containing the processed text segments and base64-encoded images from the input.
    *   **Usage:**
    #### Function: `path_to_module`
    *   **Signature:** `def path_to_module(filepath, project_root)`
    *   **Description:** This function converts a given file system path into its corresponding Python module path string. It first attempts to determine the relative path from a specified project root, falling back to the base filename if a `ValueError` occurs. It then removes the `.py` extension if present and replaces system path separators with dots. Finally, it handles `__init__.py` files by removing the `.__init__` suffix to yield the package name.
    *   **Parameters:**
        - **filepath** (str): The absolute or relative path to a Python file.
        - **project_root** (str): The root directory of the project, used to calculate the relative path.
    *   **Returns:**
        - **module_path** (str): The Python module path derived from the filepath.
    *   **Usage:**

    ### File: `database/db.py`

    #### Function: `encrypt_text`
    *   **Signature:** `def encrypt_text(text)`
    *   **Description:** This function, `encrypt_text`, is designed to encrypt a given string using an external `cipher_suite` object. It first performs a conditional check: if the input `text` is empty or if the `cipher_suite` is not initialized, it bypasses encryption and returns the original text. Otherwise, it processes the input by stripping whitespace, encoding it to bytes, encrypting these bytes via the `cipher_suite.encrypt` method, and finally decoding the encrypted result back into a string. The function then returns this encrypted string.
    *   **Parameters:**
        - **text** (str): The string value to be encrypted.
    *   **Returns:**
        - **encrypted_text** (str): The encrypted version of the input string, or the original string if encryption was skipped due to empty input or an uninitialized cipher suite.
    *   **Usage:**
    #### Function: `decrypt_text`
    *   **Signature:** `def decrypt_text(text)`
    *   **Description:** The decrypt_text function attempts to decrypt a given string using an external `cipher_suite` object. It first checks if the input `text` is empty or if `cipher_suite` is not initialized, returning the original text in such cases. If decryption proceeds, the input text is stripped of whitespace, encoded into bytes, decrypted by `cipher_suite`, and then decoded back into a string. In the event of any exception during the decryption process, the function gracefully returns the original, unencrypted text.
    *   **Parameters:**
        - **text** (str): The string value to be decrypted.
    *   **Returns:**
        - **decrypted_text** (str): The decrypted string if the operation is successful, or the original string if decryption is skipped or fails due to an error.
    *   **Usage:**
    #### Function: `insert_user`
    *   **Signature:** `def insert_user(username, name, password)`
    *   **Description:** This function `insert_user` is responsible for creating a new user record in the database. It takes a username, full name, and a plain-text password as input. The password is first hashed using `stauth.Hasher.hash` before storage. The function then constructs a user dictionary, setting the `_id` to the provided username and initializing API keys for Gemini, Ollama, and GPT to empty strings. Finally, it inserts this user dictionary into the `dbusers` collection and returns the `_id` of the newly inserted document.
    *   **Parameters:**
        - **username** (str): The unique username for the new user, which will also serve as the document's `_id`.
        - **name** (str): The full name of the new user.
        - **password** (str): The plain-text password for the new user, which will be hashed before storage.
    *   **Returns:**
        - **inserted_id** (str): The `_id` of the newly inserted user document, which corresponds to the provided username.
    *   **Usage:**
    #### Function: `fetch_all_users`
    *   **Signature:** `def fetch_all_users()`
    *   **Description:** This function, `fetch_all_users`, is designed to retrieve all user records from a database collection named `dbusers`. It executes a `find()` operation on the `dbusers` collection, which typically returns a cursor containing all documents. The function then converts this cursor into a standard Python list, effectively returning all user documents as a collection.
    *   **Parameters:**
    *   **Returns:**
        - **users** (list): A list containing all user documents retrieved from the 'dbusers' collection.
    *   **Usage:**
    #### Function: `fetch_user`
    *   **Signature:** `def fetch_user(username)`
    *   **Description:** The `fetch_user` function is responsible for retrieving a single user document from a database collection, presumably named `dbusers`. It takes a `username` as input and uses it to query the collection for a document where the `_id` field matches the provided username. The function returns the first document that satisfies this query.
    *   **Parameters:**
        - **username** (str): The unique identifier string for the user to be retrieved from the database.
    *   **Returns:**
        - **user_document** (dict | None): A dictionary representing the user document if a match is found, otherwise `None` if no user with the specified username exists.
    *   **Usage:**
    #### Function: `update_user_name`
    *   **Signature:** `def update_user_name(username, new_name)`
    *   **Description:** This function updates the 'name' field for a specific user within the 'dbusers' collection. It identifies the target user by their '_id', which is provided as the 'username' parameter. The function then sets the 'name' field of the identified user's document to the 'new_name' value. It returns an integer representing the count of documents that were successfully modified by this update operation.
    *   **Parameters:**
        - **username** (str): The unique identifier ('_id') of the user whose name is to be updated.
        - **new_name** (str): The new name to be assigned to the specified user.
    *   **Returns:**
        - **modified_count** (int): The number of documents that were modified by the update operation.
    *   **Usage:**
    #### Function: `update_gemini_key`
    *   **Signature:** `def update_gemini_key(username, gemini_api_key)`
    *   **Description:** This function is responsible for updating a user's Gemini API key within a database. It takes the username and the new Gemini API key as input. The provided API key is first processed by stripping any leading or trailing whitespace, and then it is encrypted using an external `encrypt_text` function. Finally, the function attempts to locate the user by their username in the `dbusers` collection and updates their `gemini_api_key` field with the newly encrypted value. It returns an integer indicating the number of documents that were modified.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose Gemini API key needs to be updated.
        - **gemini_api_key** (str): The new Gemini API key to be stored for the user. This key will be stripped of whitespace and encrypted before being saved.
    *   **Returns:**
        - **modified_count** (int): The number of documents that were modified by the update operation. This will typically be 0 or 1.
    *   **Usage:**
    #### Function: `update_gpt_key`
    *   **Signature:** `def update_gpt_key(username, gpt_api_key)`
    *   **Description:** The update_gpt_key function is designed to securely update a user's GPT API key within the database. It accepts a username and the new API key as arguments. The function first processes the provided API key by stripping any leading or trailing whitespace and then encrypts it using an external helper function. Subsequently, it performs an update operation on the 'dbusers' collection, setting the 'gpt_api_key' field for the specified user with the newly encrypted key. The function returns an integer indicating the number of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose GPT API key is to be updated.
        - **gpt_api_key** (str): The new GPT API key to be stored for the user.
    *   **Returns:**
        - **modified_count** (int): The number of documents modified by the update operation, typically 1 if the user was found and updated, or 0 if no matching user was found.
    *   **Usage:**
    #### Function: `update_ollama_url`
    *   **Signature:** `def update_ollama_url(username, ollama_base_url)`
    *   **Description:** This function updates the 'ollama_base_url' for a specified user in the database. It takes a username and a new Ollama base URL as input. The function uses the username as the document identifier and sets the 'ollama_base_url' field, ensuring that any leading or trailing whitespace is removed from the provided URL. It then returns the count of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose Ollama base URL is to be updated.
        - **ollama_base_url** (str): The new base URL for Ollama, which will be stored after stripping leading/trailing whitespace.
    *   **Returns:**
        - **modified_count** (int): The number of documents that were modified by the update operation.
    *   **Usage:**
    #### Function: `update_opensrc_key`
    *   **Signature:** `def update_opensrc_key(username, opensrc_api_key)`
    *   **Description:** This function is responsible for updating a user's Open Source API key within a database. It accepts a username and the new API key as input. The provided API key is first processed by stripping any leading or trailing whitespace, then it is encrypted using the `encrypt_text` utility. Finally, the function performs an update operation on the `dbusers` collection, setting the `opensrc_api_key` field for the specified user to the newly encrypted value. It returns an integer indicating the number of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose Open Source API key needs to be updated.
        - **opensrc_api_key** (str): The new Open Source API key string to be stored, which will be encrypted before saving.
    *   **Returns:**
        - **modified_count** (int): The number of documents that were modified by the update operation (typically 0 or 1).
    *   **Usage:**
    #### Function: `update_opensrc_url`
    *   **Signature:** `def update_opensrc_url(username, opensrc_base_url)`
    *   **Description:** This function updates a user's open-source base URL in a database. It takes a username and a new open-source base URL as input. The function performs an update operation on the 'dbusers' collection, identifying the user by their username and setting the 'opensrc_base_url' field. The provided URL is stripped of leading/trailing whitespace before being stored. It returns the count of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose open-source base URL is to be updated. This is used as the document's '_id'.
        - **opensrc_base_url** (str): The new open-source base URL to be set for the specified user. This string will have leading/trailing whitespace removed before storage.
    *   **Returns:**
        - **modified_count** (int): The number of documents that were modified by the update operation. A value of 1 indicates success if the user existed and the URL was different, 0 if the user existed but the URL was the same, or if the user did not exist.
    *   **Usage:**
    #### Function: `fetch_gemini_key`
    *   **Signature:** `def fetch_gemini_key(username)`
    *   **Description:** This function retrieves the Gemini API key associated with a specific username from a database. It queries the `dbusers` collection, searching for a document where the `_id` matches the provided username. If a user document is found, it extracts the `gemini_api_key` field. The function returns this key if present, or `None` if the user is not found or the key does not exist.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose Gemini API key is to be fetched.
    *   **Returns:**
        - **gemini_api_key** (str | None): The Gemini API key as a string if found, otherwise None.
    *   **Usage:**
    #### Function: `fetch_ollama_url`
    *   **Signature:** `def fetch_ollama_url(username)`
    *   **Description:** This function retrieves the Ollama base URL associated with a specific username from a database. It queries the `dbusers` collection, searching for a user document where the `_id` matches the provided username. The function specifically projects the `ollama_base_url` field. If a user document is found, it returns the value of the `ollama_base_url` field; otherwise, it returns `None`.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose Ollama base URL is to be fetched.
    *   **Returns:**
        - **ollama_base_url** (str | None): The Ollama base URL associated with the user, or None if the user is not found or the URL is not set.
    *   **Usage:**
    #### Function: `fetch_gpt_key`
    *   **Signature:** `def fetch_gpt_key(username)`
    *   **Description:** This function retrieves the GPT API key associated with a specific user from a database. It queries the `dbusers` collection, searching for a document where the `_id` matches the provided username. If a user document is found, it extracts and returns the value of the `gpt_api_key` field. If no user document is found, or if the key is not present, it returns None.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose GPT API key is to be fetched.
    *   **Returns:**
        - **gpt_api_key** (str | None): The GPT API key string if found, otherwise None.
    *   **Usage:**
    #### Function: `fetch_opensrc_key`
    *   **Signature:** `def fetch_opensrc_key(username)`
    *   **Description:** This function is designed to retrieve a user's 'opensrc_api_key' from a database. It takes a username as input and queries the 'dbusers' collection to find a matching user document. The function specifically projects only the 'opensrc_api_key' field. If a user is found, it returns the associated API key; otherwise, it returns None.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose Open Source API key is to be fetched.
    *   **Returns:**
        - **opensrc_api_key** (str | None): The Open Source API key associated with the provided username, or None if the user or key is not found.
    *   **Usage:**
    #### Function: `fetch_opensrc_url`
    *   **Signature:** `def fetch_opensrc_url(username)`
    *   **Description:** This function retrieves the 'opensrc_base_url' for a specified user from a database. It queries the 'dbusers' collection, using the provided 'username' as the document's '_id'. The function projects only the 'opensrc_base_url' field from the matching document. If a user is found, it returns the value of 'opensrc_base_url'. If no user document matches the given username, the function returns None.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose opensrc base URL is to be fetched from the database.
    *   **Returns:**
        - **opensrc_base_url** (str or None): The opensrc base URL associated with the user, or None if the user is not found or the URL field is not present.
    *   **Usage:**
    #### Function: `delete_user`
    *   **Signature:** `def delete_user(username)`
    *   **Description:** The `delete_user` function is designed to remove a specific user record from a database collection. It accepts a username string, which it uses as the primary key (`_id`) to locate and delete the corresponding document. The function leverages a database client's `delete_one` method to perform this operation. It then returns the count of documents that were successfully deleted.
    *   **Parameters:**
        - **username** (str): The unique identifier (username) of the user to be deleted from the database.
    *   **Returns:**
        - **deleted_count** (int): The number of documents that were successfully deleted. This will typically be 1 if a user was found and deleted, or 0 if no matching user was found.
    *   **Usage:**
    #### Function: `get_decrypted_api_keys`
    *   **Signature:** `def get_decrypted_api_keys(username)`
    *   **Description:** This function retrieves various API keys and URLs associated with a given username from a database. It queries the `dbusers` collection for a user document matching the provided `username`. If no user is found, it returns `None` for all expected values. For existing users, it retrieves specific API keys (Gemini, GPT, Open Source) and base URLs (Ollama, Open Source). The API keys are decrypted using the `decrypt_text` function before being returned, while the base URLs are returned as-is.
    *   **Parameters:**
        - **username** (str): The unique identifier for the user whose API keys and URLs are to be retrieved.
    *   **Returns:**
        - **gemini_plain** (str | None): The decrypted Gemini API key, or None if the user is not found or the key is absent.
        - **ollama_plain** (str | None): The Ollama base URL, or None if the user is not found or the URL is absent.
        - **gpt_plain** (str | None): The decrypted GPT API key, or None if the user is not found or the key is absent.
        - **opensrc_plain** (str | None): The decrypted Open Source API key, or None if the user is not found or the key is absent.
        - **opensrc_url** (str | None): The Open Source base URL, or None if the user is not found or the URL is absent.
    *   **Usage:**
    #### Function: `insert_chat`
    *   **Signature:** `def insert_chat(username, chat_name)`
    *   **Description:** The `insert_chat` function is responsible for creating a new chat entry within a database. It constructs a dictionary containing a unique identifier generated by `uuid.uuid4()`, the provided username, the chat name, and the current timestamp. This chat dictionary is then inserted into the `dbchats` collection using the `insert_one` method. The function concludes by returning the unique ID of the newly inserted document.
    *   **Parameters:**
        - **username** (str): The username associated with the new chat entry.
        - **chat_name** (str): The name of the chat to be created.
    *   **Returns:**
        - **inserted_id** (str): The unique identifier (`_id`) of the newly created chat entry in the database.
    *   **Usage:**
    #### Function: `fetch_chats_by_user`
    *   **Signature:** `def fetch_chats_by_user(username)`
    *   **Description:** This function, `fetch_chats_by_user`, is designed to retrieve all chat records associated with a specific user from a database. It takes a username as input and queries the `dbchats` collection for documents matching that username. The retrieved chat records are then sorted by their `created_at` timestamp in ascending order. Finally, the function returns these sorted chat records as a list.
    *   **Parameters:**
        - **username** (str): The username for which to fetch all associated chat records.
    *   **Returns:**
        - **chats** (list): A list of chat documents (dictionaries) belonging to the specified user, sorted by their creation date.
    *   **Usage:**
    #### Function: `check_chat_exists`
    *   **Signature:** `def check_chat_exists(username, chat_name)`
    *   **Description:** This function checks for the existence of a specific chat within the 'dbchats' collection. It takes a username and a chat name as input. The function queries the database to find a document that matches both the provided username and chat name. It returns a boolean indicating whether such a chat exists.
    *   **Parameters:**
        - **username** (str): The username associated with the chat to be checked.
        - **chat_name** (str): The name of the chat to be checked for existence.
    *   **Returns:**
        - **chat_exists** (bool): True if a chat matching the username and chat name is found in the database, False otherwise.
    *   **Usage:**
    #### Function: `rename_chat_fully`
    *   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
    *   **Description:** This function renames a chat and all its associated exchanges (messages) within the database for a specific user. It first updates the chat entry in the 'dbchats' collection, changing the 'chat_name' from the 'old_name' to the 'new_name' for the given 'username'. Subsequently, it updates all related exchange entries in the 'dbexchanges' collection, similarly updating their 'chat_name' to reflect the new name. The function returns the count of chat entries that were modified by the initial update operation.
    *   **Parameters:**
        - **username** (str): The username associated with the chat to be renamed.
        - **old_name** (str): The current name of the chat.
        - **new_name** (str): The new desired name for the chat.
    *   **Returns:**
        - **modified_count** (int): The number of chat entries that were modified by the initial update operation in 'dbchats'.
    *   **Usage:**
    #### Function: `insert_exchange`
    *   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used='', main_used='', total_time='', helper_time='', main_time='', json_tokens=0, toon_tokens=0, savings_percent=0.0)`
    *   **Description:** This function records a chat exchange into a database. It generates a unique identifier using `uuid.uuid4()` for the exchange, compiles the provided chat details along with timestamps and token usage into a document. It then attempts to insert this document into the `dbexchanges` MongoDB collection using `insert_one`. Upon successful insertion, it returns the unique ID; otherwise, it handles the exception by printing an error and returning `None`.
    *   **Parameters:**
        - **question** (str): The user's question in the exchange.
        - **answer** (str): The generated answer for the question.
        - **feedback** (str): Feedback provided for the exchange.
        - **username** (str): The username associated with the exchange.
        - **chat_name** (str): The name of the chat session.
        - **helper_used** (str): Indicates if a helper model was used, defaults to an empty string.
        - **main_used** (str): Indicates if a main model was used, defaults to an empty string.
        - **total_time** (str): The total time taken for the exchange, defaults to an empty string.
        - **helper_time** (str): The time taken by the helper model, defaults to an empty string.
        - **main_time** (str): The time taken by the main model, defaults to an empty string.
        - **json_tokens** (int): The number of JSON tokens used, defaults to 0.
        - **toon_tokens** (int): The number of Toon tokens used, defaults to 0.
        - **savings_percent** (float): The percentage of savings, defaults to 0.0.
    *   **Returns:**
        - **new_id** (str): The unique identifier of the newly inserted exchange document upon success.
        - **None** (NoneType): Indicates that the insertion failed due to a database error.
    *   **Usage:**
    #### Function: `fetch_exchanges_by_user`
    *   **Signature:** `def fetch_exchanges_by_user(username)`
    *   **Description:** This function retrieves exchange records from a database based on a provided username. It queries the `dbexchanges` collection for all documents where the 'username' field matches the input. The results are then sorted in ascending order by their 'created_at' timestamp, which is noted as important for display purposes. Finally, the function returns these sorted exchange records as a list.
    *   **Parameters:**
        - **username** (str): The username to filter the exchange records by.
    *   **Returns:**
        - **exchanges** (list): A list of exchange documents associated with the specified username, sorted by their 'created_at' timestamp in ascending order.
    *   **Usage:**
    #### Function: `fetch_exchanges_by_chat`
    *   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
    *   **Description:** This function retrieves a list of exchange documents from the `dbexchanges` collection. It filters these documents based on a provided username and chat name. The results are then sorted by their `created_at` timestamp in ascending order before being returned as a list.
    *   **Parameters:**
        - **username** (str): The username used to filter the exchanges.
        - **chat_name** (str): The name of the chat used to filter the exchanges.
    *   **Returns:**
        - **exchanges** (list): A list of exchange documents that match the specified username and chat name, sorted by creation time.
    *   **Usage:**
    #### Function: `update_exchange_feedback`
    *   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
    *   **Description:** This function updates the feedback for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function uses `dbexchanges.update_one` to locate the document by its `_id` and set its 'feedback' field to the provided value. It then returns the count of documents that were modified by this operation.
    *   **Parameters:**
        - **exchange_id** (Any): The unique identifier for the exchange record to be updated. Its specific type is not explicitly hinted but is used as a MongoDB document ID.
        - **feedback** (int): The integer value representing the feedback to be set for the specified exchange.
    *   **Returns:**
        - **modified_count** (int): The number of documents that were modified by the update operation. A value of 1 indicates success, 0 indicates no document was found or changed.
    *   **Usage:**
    #### Function: `update_exchange_feedback_message`
    *   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
    *   **Description:** This function updates an existing exchange record in the database. It takes an exchange identifier and a new feedback message as input. The function uses the `dbexchanges.update_one` method to locate the document by its `_id` and then sets the `feedback_message` field to the provided string. It returns the count of documents that were successfully modified by the operation.
    *   **Parameters:**
        - **exchange_id** (Any): The unique identifier of the exchange record to be updated.
        - **feedback_message** (str): The new feedback message to be associated with the specified exchange.
    *   **Returns:**
        - **modified_count** (int): The number of documents that were modified by the update operation.
    *   **Usage:**
    #### Function: `delete_exchange_by_id`
    *   **Signature:** `def delete_exchange_by_id(exchange_id)`
    *   **Description:** This function is designed to remove a specific exchange record from a database collection. It takes a unique identifier for an exchange as input. The function then executes a delete operation on the `dbexchanges` collection, targeting the document whose `_id` field matches the provided `exchange_id`. Finally, it returns an integer indicating how many documents were successfully deleted by the operation.
    *   **Parameters:**
        - **exchange_id** (str): The unique identifier (ID) of the exchange record to be deleted from the database.
    *   **Returns:**
        - **deleted_count** (int): The number of documents that were successfully deleted. This will typically be 0 or 1 for a single-document delete operation.
    *   **Usage:**
    #### Function: `delete_full_chat`
    *   **Signature:** `def delete_full_chat(username, chat_name)`
    *   **Description:** This function is responsible for completely deleting a specified chat and all its associated messages (exchanges) for a given user. It first removes all messages linked to the chat using `dbexchanges.delete_many`, then proceeds to delete the chat entry itself from the chat list using `dbchats.delete_one`. This two-step process ensures data consistency between the frontend and backend by removing all related data.
    *   **Parameters:**
        - **username** (str): The username associated with the chat to be deleted.
        - **chat_name** (str): The name of the chat to be deleted.
    *   **Returns:**
        - **deleted_count** (int): The number of chat documents deleted, typically 1 if successful, or 0 if the chat was not found.
    *   **Usage:**

    ### File: `frontend/frontend.py`

    #### Function: `clean_names`
    *   **Signature:** `def clean_names(model_list)`
    *   **Description:** This function processes a list of strings, where each string is expected to represent a path or a similar structure. It iterates through the input list and for each element, it splits the string by the forward slash ('/') character. The function then extracts the last component of the split string, effectively cleaning or simplifying the names. The result is a new list containing these extracted, cleaned names.
    *   **Parameters:**
        - **model_list** (List[str]): A list of strings, where each string is expected to be a path-like structure that can be split by a forward slash ('/').
    *   **Returns:**
        - **cleaned_names** (List[str]): A new list containing the last component of each input string after splitting by the '/' character.
    *   **Usage:**
    #### Function: `get_filtered_models`
    *   **Signature:** `def get_filtered_models(source_list, category_name)`
    *   **Description:** This function filters a given list of models (`source_list`) based on a specified `category_name`. It retrieves filtering keywords associated with the category from a global `CATEGORY_KEYWORDS` mapping. If the category's keywords include "STANDARD", the function returns only those models that are also present in a `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list` and includes models whose names (case-insensitively) contain any of the category's keywords. If no models match the keywords, the original `source_list` is returned.
    *   **Parameters:**
        - **source_list** (list): The initial list of models to be filtered.
        - **category_name** (str): The name of the category used to determine filtering keywords.
    *   **Returns:**
        - **filtered_models** (list): A list of models filtered according to the specified category, or the original `source_list` if no filtering criteria are met or no models match.
    *   **Usage:**
    #### Function: `save_gemini_cb`
    *   **Signature:** `def save_gemini_cb()`
    *   **Description:** This function serves as a callback to save a user's Gemini API key. It first attempts to retrieve a new Gemini key from the Streamlit session state. If a new key is found and is not an empty string, the function proceeds to update this key in the database, associating it with the currently logged-in username. Following a successful database update, the temporary key is cleared from the session state, and a success toast notification is displayed to the user.
    *   **Parameters:**
    *   **Returns:**
    *   **Usage:**
    #### Function: `save_ollama_cb`
    *   **Signature:** `def save_ollama_cb()`
    *   **Description:** This function is designed to save a new Ollama URL. It retrieves the potential new URL from the Streamlit session state, specifically from the key "in_ollama_url". If a non-empty URL is found, the function proceeds to update this URL in the database using the `db.update_ollama_url` method, associating it with the current user's username also retrieved from the session state. Upon successful update, a confirmation toast message is displayed to the user via Streamlit. This ensures that the user's specified Ollama endpoint is persisted.
    *   **Parameters:**
    *   **Returns:**
    *   **Usage:**
    #### Function: `load_data_from_db`
    *   **Signature:** `def load_data_from_db(username)`
    *   **Description:** This function loads chat data and associated exchanges for a specified user from the database into the Streamlit session state. It first checks if the data for the given username is already loaded; if not, it proceeds with the loading process. The function initializes the session state's chat structure, then fetches predefined chats and their exchanges, organizing them by chat name. It also handles legacy support for exchanges without predefined chats and ensures feedback values are consistently represented. Finally, it creates a default chat if none exist and sets an active chat in the session state.
    *   **Parameters:**
        - **username** (str): The username for which to load chat data and exchanges from the database.
    *   **Returns:**
    *   **Usage:**
    #### Function: `handle_feedback_change`
    *   **Signature:** `def handle_feedback_change(ex, val)`
    *   **Description:** This function is responsible for handling changes to feedback associated with an exchange object. It takes an exchange object, `ex`, and a new feedback value, `val`, as input. The function first updates the 'feedback' key within the `ex` object with the new `val`. Subsequently, it calls a database utility function, `db.update_exchange_feedback`, to persist this feedback change in the database, using the `_id` from the `ex` object. Finally, it triggers a Streamlit rerun to refresh the application's UI, reflecting the updated feedback.
    *   **Parameters:**
        - **ex** (dict): An exchange object or dictionary that contains at least an '_id' and a 'feedback' key, representing the item whose feedback is being changed.
        - **val** (Any): The new feedback value to be assigned to the 'feedback' key of the exchange object.
    *   **Returns:**
    *   **Usage:**
    #### Function: `handle_delete_exchange`
    *   **Signature:** `def handle_delete_exchange(chat_name, ex)`
    *   **Description:** This function handles the deletion of a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if the exchange is found within that chat's exchanges list, it removes it from the session state. Finally, it triggers a Streamlit rerun to update the UI.
    *   **Parameters:**
        - **chat_name** (str): The name of the chat from which the exchange should be deleted in the session state.
        - **ex** (dict): The exchange object to be deleted, expected to contain an '_id' key for database deletion.
    *   **Returns:**
    *   **Usage:**
    #### Function: `handle_delete_chat`
    *   **Signature:** `def handle_delete_chat(username, chat_name)`
    *   **Description:** This function handles the deletion of a specific chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the Streamlit session state by removing the chat from `st.session_state.chats`. If other chats exist, the first one is set as the new active chat; otherwise, a new default chat named "Chat 1" is created, inserted into the database, and set as the active chat. Finally, it triggers a Streamlit rerun to update the UI.
    *   **Parameters:**
        - **username** (str): The username associated with the chat to be deleted or managed.
        - **chat_name** (str): The name of the chat to be deleted.
    *   **Returns:**
    *   **Usage:**
    #### Function: `extract_repo_name`
    *   **Signature:** `def extract_repo_name(text)`
    *   **Description:** This function aims to extract a repository name from a given text string. It first attempts to find a URL within the text using a regular expression. If a URL is identified, it is parsed to isolate the path component. The last segment of this path is then considered the repository name, with any trailing ".git" suffix removed. The function returns the extracted repository name as a string, or None if no URL is found or a repository name cannot be determined.
    *   **Parameters:**
        - **text** (str): The input string from which to extract a repository name, potentially containing a URL.
    *   **Returns:**
        - **repo_name** (str): The extracted repository name, if found and processed.
        - **None** (NoneType): Indicates that no repository name could be extracted from the input text.
    *   **Usage:**
    #### Function: `stream_text_generator`
    *   **Signature:** `def stream_text_generator(text)`
    *   **Description:** This generator function takes a string of text and yields its words one by one, each followed by a space. It simulates a streaming effect by introducing a small delay after yielding each word. This can be used to display text progressively, for example, in a user interface.
    *   **Parameters:**
        - **text** (str): The input string of text that needs to be streamed word by word.
    *   **Returns:**
        - **word_with_space** (str): A single word from the input text, followed by a space, yielded sequentially.
    *   **Usage:**
    #### Function: `render_text_with_mermaid`
    *   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream=False)`
    *   **Description:** This function processes a given markdown text, identifying and rendering embedded Mermaid diagrams. It splits the input text into parts based on '```mermaid' delimiters. Non-Mermaid text sections are rendered using Streamlit's markdown functionality, optionally streaming the content. Mermaid diagram code blocks are rendered using `streamlit_mermaid.st_mermaid`, with a fallback to displaying the code as a plain code block if rendering fails.
    *   **Parameters:**
        - **markdown_text** (str): The input text, potentially containing markdown and embedded Mermaid diagram blocks.
        - **should_stream** (bool): A flag indicating whether non-Mermaid text parts should be streamed using `st.write_stream` or rendered directly with `st.markdown`.
    *   **Returns:**
        - **None** (None): This function does not explicitly return a value. It performs side effects by rendering content to a Streamlit application. It returns early if `markdown_text` is empty.
    *   **Usage:**
    #### Function: `render_exchange`
    *   **Signature:** `def render_exchange(ex, current_chat_name)`
    *   **Description:** This function is responsible for rendering a single chat exchange within a Streamlit application, displaying both the user's question and the assistant's answer. It dynamically generates a toolbar for the assistant's response, offering user interaction features such as feedback (like/dislike), a popover for adding notes, and buttons for downloading the response or deleting the exchange. The function handles error states in the assistant's answer by displaying an error message and a delete option. It integrates with other functions for managing feedback and exchange deletion.
    *   **Parameters:**
        - **ex** (dict): A dictionary-like object representing a single chat exchange, containing fields like 'question', 'answer', '_id', 'feedback', and 'feedback_message'.
        - **current_chat_name** (str): The identifier or name of the current chat session, used for context in operations like deleting an exchange.
    *   **Returns:**
    *   **Usage:**

    ### File: `schemas/types.py`

    #### Class: `ParameterDescription`
    *   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to structure and validate information about a single parameter of a function. It serves as a clear, machine-readable schema for defining a parameter's name, its data type, and a concise description of its role. This class is fundamental for generating accurate documentation, API specifications, or for internal systems that require structured metadata about function arguments.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* The `__init__` method for ParameterDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance by validating and assigning values for the `name`, `type`, and `description` attributes based on the provided arguments, ensuring they conform to the specified string types.
        *   *Parameters:*
            - **name** (str): The name of the parameter being described.
            - **type** (str): The data type of the parameter, typically as a string representation (e.g., 'str', 'int', 'List[str]').
            - **description** (str): A brief textual explanation of the parameter's purpose or role.
    *   **Methods:**
    #### Class: `ReturnDescription`
    *   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to encapsulate the details of a function's return value. It provides a standardized structure to describe the name, data type, and a textual explanation of what a function returns, facilitating clear and machine-readable documentation of function outputs.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, has an implicitly generated constructor. It initializes an instance of ReturnDescription by accepting values for `name`, `type`, and `description`, which are then validated according to their type hints.
        *   *Parameters:*
            - **name** (str): The name or identifier of the return value.
            - **type** (str): The data type of the return value.
            - **description** (str): A brief explanation of what the return value represents.
    *   **Methods:**
    #### Class: `UsageContext`
    *   **Summary:** The `UsageContext` class is a Pydantic BaseModel designed to encapsulate the calling context of a function. It serves as a structured data container, holding information about what a function calls and by what it is called. This class provides a clear and consistent way to represent functional relationships within a system.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* This class does not define an explicit `__init__` method. As a Pydantic BaseModel, its constructor is implicitly generated, allowing instances to be created by passing keyword arguments corresponding to its defined fields: `calls` and `called_by`.
        *   *Parameters:*
            - **calls** (str): Information about what the function calls.
            - **called_by** (str): Information about where the function is called from.
    *   **Methods:**
    #### Class: `FunctionDescription`
    *   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to provide a structured and detailed analysis of a Python function. It serves as a schema for encapsulating various aspects of a function, including its high-level purpose, signature parameters, return values, and its operational context within a larger system. This class is crucial for standardizing the representation of function metadata, enabling machine-readable documentation and analysis.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* This class is a Pydantic BaseModel, meaning its constructor (`__init__`) is automatically generated based on the defined fields. It initializes instances by validating and assigning values for the function's overall description, its parameters, its return values, and its usage context.
        *   *Parameters:*
            - **overall** (str): A concise, high-level summary describing the function's purpose and how it achieves its goal.
            - **parameters** (List[ParameterDescription]): A list of `ParameterDescription` objects, each detailing a specific input parameter of the function, including its name, type, and description.
            - **returns** (List[ReturnDescription]): A list of `ReturnDescription` objects, each detailing a specific return value of the function, including its name, type, and description.
            - **usage_context** (UsageContext): An object providing information about the function's external dependencies and where it is called within the codebase.
    *   **Methods:**
    #### Class: `FunctionAnalysis`
    *   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate the structured analysis of a single Python function. It serves as a standardized data model, holding the function's unique identifier, a comprehensive description object, and an optional field to report any errors encountered during its analysis. This class is crucial for representing machine-readable function metadata within a larger system.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`, `typing.Optional`
    *   **Constructor:**
        *   *Description:* The FunctionAnalysis class inherits from Pydantic's BaseModel, meaning its constructor is automatically generated. It initializes the instance by validating and assigning values to its `identifier`, `description`, and `error` fields based on the provided arguments during instantiation.
        *   *Parameters:*
            - **identifier** (str): The unique name or identifier of the function being analyzed.
            - **description** (FunctionDescription): An object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
            - **error** (Optional[str]): An optional string providing details if an error occurred during the function's analysis. Defaults to None.
    *   **Methods:**
    #### Class: `ConstructorDescription`
    *   **Summary:** The `ConstructorDescription` class is a Pydantic BaseModel designed to provide a structured representation of a Python class's `__init__` method. It encapsulates a high-level textual description of the constructor's purpose and a detailed list of its individual parameters, each described by a `ParameterDescription` object. This class serves as a data schema for documenting how other classes are initialized.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ConstructorDescription` is implicitly generated by Pydantic's BaseModel. It initializes an instance of this model by assigning the provided string `description` and a list of `ParameterDescription` objects to the corresponding instance attributes.
        *   *Parameters:*
            - **description** (str): A string summarizing the purpose and behavior of the constructor being described.
            - **parameters** (List[ParameterDescription]): A list of `ParameterDescription` objects, each detailing a parameter accepted by the constructor.
    *   **Methods:**
    #### Class: `ClassContext`
    *   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate contextual information about another class. It specifically stores details regarding the external dependencies that the class relies on and the locations within the codebase where the class is instantiated. This model provides a structured way to represent and manage usage context for classes.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The `__init__` method, implicitly generated by Pydantic's BaseModel, initializes an instance of ClassContext. It sets the `dependencies` and `instantiated_by` attributes based on the provided string values, ensuring the object accurately reflects the class's usage context."
        *   *Parameters:*
            - **dependencies** (str): A string summarizing the external dependencies of the class being described.
            - **instantiated_by** (str): A string summarizing where the class being described is instantiated within the codebase.
    *   **Methods:**
    #### Class: `ClassDescription`
    *   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of another Python class. It serves as a structured data container, holding an overall textual summary of the class, detailed information about its constructor, a list of analyses for each of its methods, and contextual information regarding its dependencies and instantiation points. This model is crucial for representing the output of a class analysis process in a standardized, machine-readable format.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "This class is a Pydantic BaseModel, meaning its constructor is implicitly generated by Pydantic. It initializes instances by accepting keyword arguments corresponding to its defined fields: 'overall', 'init_method', 'methods', and 'usage_context'. Pydantic handles validation and assignment of these values upon instantiation."
        *   *Parameters:*
            - **overall** (str): A high-level summary describing the primary purpose and responsibilities of the class being analyzed.
            - **init_method** (ConstructorDescription): An object containing a detailed description of the analyzed class's constructor, including its parameters.
            - **methods** (List[FunctionAnalysis]): A list of FunctionAnalysis objects, where each object provides a detailed analysis of a method within the analyzed class.
            - **usage_context** (ClassContext): An object containing contextual information about the analyzed class, such as its external dependencies and where it is instantiated.
    *   **Methods:**
    #### Class: `ClassAnalysis`
    *   **Summary:** The ClassAnalysis class serves as the primary Pydantic model for structuring the comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed description object that includes constructor and method analyses, and an optional field to report any errors encountered during the analysis. This model is designed to provide a standardized, machine-readable format for AI-driven code analysis outputs.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* The ClassAnalysis class does not explicitly define an `__init__` method. As a Pydantic BaseModel, its initialization is handled automatically by Pydantic, which validates and assigns values to its fields: `identifier`, `description`, and `error` upon instantiation.
        *   *Parameters:*
            - **identifier** (str): The unique name or identifier of the class to be analyzed.
            - **description** (ClassDescription): A detailed description object containing constructor and method analyses, and usage context.
            - **error** (Optional[str]): An optional field to report any errors encountered during the analysis. Defaults to None.
    *   **Methods:**
    #### Class: `CallInfo`
    *   **Summary:** The CallInfo class is a Pydantic BaseModel designed to structure and validate data related to a specific call event within a software system. It captures essential details such as the file path, the name of the calling function, the mode of the call (e.g., method, function), and the line number. This model serves as a standardized representation for tracking and analyzing relationships like 'called_by' and 'instantiated_by' across different code components.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* "This class utilizes Pydantic's BaseModel to automatically generate an __init__ method. The constructor is implicitly defined to accept and validate the 'file', 'function', 'mode', and 'line' attributes, ensuring that instances of CallInfo are created with the correct data types and structure."
        *   *Parameters:*
            - **file** (str): The path to the file where the call event occurred.
            - **function** (str): The name of the function or method that made the call.
            - **mode** (str): The type of call, e.g., 'method', 'function', 'module'.
            - **line** (int): The line number in the file where the call event occurred.
    *   **Methods:**
    #### Class: `FunctionContextInput`
    *   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to structure and encapsulate contextual information for analyzing a function. It serves as a data transfer object, defining two key attributes: 'calls', which lists the entities invoked by the function, and 'called_by', which details the locations or entities that invoke this function. This class provides a standardized and validated format for collecting and exchanging function-related context within a larger system, likely for automated code analysis or documentation.
    *   **Instantiation:** `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "This class inherits from Pydantic's BaseModel, meaning its __init__ method is automatically generated by Pydantic. It is used to initialize instances of FunctionContextInput by validating and assigning values to its 'calls' and 'called_by' attributes based on the provided arguments, ensuring data integrity according to the defined types."
        *   *Parameters:*
            - **calls** (List[str]): A list of identifiers (strings) representing other functions, methods, or classes that the function being analyzed calls.
            - **called_by** (List[CallInfo]): A list of CallInfo objects indicating the functions or methods that call the function being analyzed.
    *   **Methods:**
    #### Class: `FunctionAnalysisInput`
    *   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a FunctionAnalysis object. It acts as a data validation and parsing schema, ensuring that all necessary components like the analysis mode, function identifier, source code, imports, and contextual information are present and correctly typed before a function analysis can proceed. This class is fundamental for standardizing the data contract for function analysis tasks.
    *   **Instantiation:** `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The constructor for FunctionAnalysisInput is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting keyword arguments corresponding to its defined fields, performing data validation and type coercion as per the schema. This allows for easy creation of validated input objects."
        *   *Parameters:*
            - **mode** (Literal["function_analysis"]): Specifies the operational mode, which is fixed to 'function_analysis' for this input type, indicating the intent to analyze a function.
            - **identifier** (str): The unique name or identifier of the function that is to be analyzed.
            - **source_code** (str): The raw source code of the entire function definition to be analyzed.
            - **imports** (List[str]): A list of import statements (as strings) that are relevant to the source file where the function is defined.
            - **context** (FunctionContextInput): An object containing additional contextual information pertinent to the function, such as its dependencies or where it is called.
    *   **Methods:**
    #### Class: `MethodContextInput`
    *   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to define a structured schema for capturing contextual information about a method. It serves as a data transfer object or a validation schema for method-specific details, including its unique identifier, the functions or methods it calls, where it is called from, its arguments, and its docstring. This class ensures that method context data adheres to a predefined structure for consistency and validation.
    *   **Instantiation:** `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The `__init__` method for `MethodContextInput` is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting keyword arguments corresponding to its defined fields. During initialization, Pydantic performs data validation to ensure that the provided values conform to the specified types and constraints for each field."
        *   *Parameters:*
            - **identifier** (str): The unique name or identifier of the method being described.
            - **calls** (List[str]): A list of identifiers (strings) representing other methods, classes, or functions that this method calls within its implementation.
            - **called_by** (List[CallInfo]): A list of CallInfo objects, each detailing a specific location or context from which this method is invoked.
            - **args** (List[str]): A list of strings, where each string represents the name of an argument accepted by the method.
            - **docstring** (Optional[str]): An optional string containing the docstring associated with the method, providing a description of its purpose and usage.
    *   **Methods:**
    #### Class: `ClassContextInput`
    *   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information for analyzing a Python class. It serves as a data transfer object, holding lists of dependencies, instantiation points, and detailed method contexts. This model provides a standardized format for collecting and passing comprehensive data required for a holistic class analysis within a larger system.
    *   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The `__init__` method for ClassContextInput is implicitly generated by Pydantic's BaseModel. It handles the initialization of an instance by validating and assigning values to its defined fields: `dependencies`, `instantiated_by`, and `method_context` based on the provided input."
        *   *Parameters:*
            - **dependencies** (List[str]): A list of strings representing external dependencies relevant to the class being analyzed.
            - **instantiated_by** (List[CallInfo]): A list of CallInfo objects indicating where the class being analyzed is instantiated within the codebase.
            - **method_context** (List[MethodContextInput]): A list of MethodContextInput objects, each providing specific contextual information for individual methods within the class being analyzed.
    *   **Methods:**
    #### Class: `ClassAnalysisInput`
    *   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It acts as a schema validator, ensuring that all necessary components like the analysis mode, class identifier, source code, import statements, and contextual information are present and correctly typed before further processing. This class is fundamental for standardizing the input data for the class analysis pipeline.
    *   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The ClassAnalysisInput class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is implicitly generated, allowing instantiation by passing keyword arguments corresponding to its defined fields. This ensures automatic validation and assignment of input data to the class attributes."
        *   *Parameters:*
            - **mode** (Literal["class_analysis"]): Specifies the operational mode, which is fixed to 'class_analysis' for this input type.
            - **identifier** (str): The unique name or identifier of the class to be analyzed.
            - **source_code** (str): The raw source code of the entire class definition.
            - **imports** (List[str]): A list of import statements relevant to the source file containing the class.
            - **context** (ClassContextInput): Additional contextual information related to the class, such as dependencies and instantiation points.
    *   **Methods:**

    ### File: `backend/relationship_analyzer.py`

    #### Function: `path_to_module`
    *   **Signature:** `def path_to_module(filepath, project_root)`
    *   **Description:** This function converts a given file system path into its corresponding Python module path string. It first attempts to determine the relative path from a specified project root, falling back to the base filename if a `ValueError` occurs. It then removes the `.py` extension if present and replaces system path separators with dots. Finally, it handles `__init__.py` files by removing the `.__init__` suffix to yield the package name.
    *   **Parameters:**
        - **filepath** (str): The absolute or relative path to a Python file.
        - **project_root** (str): The root directory of the project, used to calculate the relative path.
    *   **Returns:**
        - **module_path** (str): The Python module path derived from the filepath.
    *   **Usage:**
    #### Class: `ProjectAnalyzer`
    *   **Summary:** The ProjectAnalyzer class is designed to perform a static analysis of a Python project to build a comprehensive call graph. It systematically identifies all Python files, parses their Abstract Syntax Trees (ASTs) to collect definitions of classes, functions, and methods, and then resolves the call relationships between these entities. The class provides methods to initiate the analysis, retrieve the raw call graph, and extract structured incoming and outgoing relationship data, making it a core component for understanding code structure and dependencies.
    *   **Instantiation:** `backend.main.main_workflow`
    *   **Dependencies:** `backend.relationship_analyzer.CallResolverVisitor`, `backend.relationship_analyzer.path_to_module`
    *   **Constructor:**
        *   *Description:* Initializes the ProjectAnalyzer with the root directory of the project. It sets up various internal data structures like 'definitions' for storing discovered entities, 'call_graph' for tracking relationships, and 'file_asts' for parsed ASTs, along with a set of directories to ignore during file traversal.
        *   *Parameters:*
            - **project_root** (str): The absolute path to the root directory of the project to be analyzed.
    *   **Methods:**
        *   **`analyze`**
            *   *Signature:* `def analyze(self)`
            *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect definitions of functions, classes, and methods. Subsequently, it resolves call relationships between these defined entities. Finally, it clears the stored ASTs to free up memory and returns the populated call graph.
            *   *Parameters:*
                - **self** (ProjectAnalyzer): The instance of the ProjectAnalyzer class.
            *   *Returns:*
                - **call_graph** (collections.defaultdict): A dictionary-like object representing the call graph, where keys are callee identifiers and values are lists of caller information.
            *   *Usage:*
        *   **`get_raw_relationships`**
            *   *Signature:* `def get_raw_relationships(self)`
            *   *Description:* This method processes the internal call_graph to generate a structured representation of outgoing and incoming relationships. It iterates through the call graph, populating two defaultdict(set) objects: 'outgoing' to track what each entity calls, and 'incoming' to track what calls each entity. The final output is a dictionary containing sorted lists of these relationships.
            *   *Parameters:*
                - **self** (ProjectAnalyzer): The instance of the ProjectAnalyzer class.
            *   *Returns:*
                - **relationships** (dict): A dictionary containing two keys, "outgoing" and "incoming", each mapping entity identifiers to sorted lists of related entity identifiers.
            *   *Usage:*
        *   **`_find_py_files`**
            *   *Signature:* `def _find_py_files(self)`
            *   *Description:* This private helper method is responsible for traversing the project directory structure to locate all Python files. It uses os.walk to navigate the file system, filtering out directories specified in self.ignore_dirs to avoid irrelevant paths. For each Python file found, its full path is added to a list which is then returned.
            *   *Parameters:*
                - **self** (ProjectAnalyzer): The instance of the ProjectAnalyzer class.
            *   *Returns:*
                - **py_files** (list[str]): A list of absolute file paths to all Python files found within the project root, excluding ignored directories.
            *   *Usage:*
        *   **`_collect_definitions`**
            *   *Signature:* `def _collect_definitions(self, filepath)`
            *   *Description:* This private method parses a given Python file to identify and store definitions of functions, classes, and methods. It reads the file, parses its Abstract Syntax Tree (AST), and stores the AST in self.file_asts. It then walks the AST to find FunctionDef and ClassDef nodes, determines their fully qualified path names, and records their file, line number, and type in self.definitions. Error handling is included to log any parsing issues.
            *   *Parameters:*
                - **self** (ProjectAnalyzer): The instance of the ProjectAnalyzer class.
                - **filepath** (str): The path to the Python file to be analyzed for definitions.
            *   *Returns:*
            *   **Usage:**
        *   **`_get_parent`**
            *   *Signature:* `def _get_parent(self, tree, node)`
            *   *Description:* This private helper method traverses an Abstract Syntax Tree (AST) to find the direct parent node of a given child node. It iterates through all nodes in the tree, and for each node, it checks its immediate children. If a child matches the target node, the current node is identified as its parent and returned. If no parent is found after traversing the entire tree, it returns None.
            *   *Parameters:*
                - **self** (ProjectAnalyzer): The instance of the ProjectAnalyzer class.
                - **tree** (ast.AST): The root of the Abstract Syntax Tree to search within.
                - **node** (ast.AST): The child node for which to find the parent.
            *   *Returns:*
                - **parent_node** (ast.AST or None): The direct parent AST node of the given node, or None if no parent is found.
            *   *Usage:*
        *   **`_resolve_calls`**
            *   *Signature:* `def _resolve_calls(self, filepath)`
            *   *Description:* This private method is responsible for identifying and resolving function and method calls within a specific Python file. It retrieves the AST for the given filepath and then instantiates a CallResolverVisitor to traverse the AST and detect calls. The resolved calls, along with their caller information, are then aggregated into the self.call_graph attribute. Any errors during this process are caught and logged.
            *   *Parameters:*
                - **self** (ProjectAnalyzer): The instance of the ProjectAnalyzer class.
                - **filepath** (str): The path to the Python file whose calls need to be resolved.
            *   *Returns:*
            *   **Usage:**
    #### Class: `CallResolverVisitor`
    *   **Summary:** The CallResolverVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) and identify function and method calls within Python source code. Its primary purpose is to build a comprehensive map of call relationships within a Python project by resolving qualified names for calls, imports, and assigned instance types. It tracks the current scope, class, and caller to accurately record where each call originates.
    *   **Instantiation:** `backend.relationship_analyzer.ProjectAnalyzer._resolve_calls`
    *   **Dependencies:** `backend.relationship_analyzer.path_to_module`
    *   **Constructor:**
        *   *Description:* The constructor initializes the CallResolverVisitor with the file path of the code being analyzed, the project's root directory, and a dictionary of known definitions. It sets up internal state variables such as the module path, a scope dictionary for name resolution, a dictionary to track instance types, and a `defaultdict` to store discovered call relationships.
        *   *Parameters:*
            - **self** (CallResolverVisitor): The instance of the CallResolverVisitor class.
            - **filepath** (str): The absolute path to the Python file being analyzed.
            - **project_root** (str): The root directory of the entire project, used for calculating module paths.
            - **definitions** (dict): A dictionary containing known fully qualified names of functions, classes, and methods within the project, used for validating resolved call targets.
    *   **Methods:**
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* This method is invoked by the AST visitor when a class definition (`ast.ClassDef`) is encountered. It temporarily updates the `current_class_name` attribute to the name of the class being visited, allowing nested methods to correctly form their fully qualified names. After processing the class's children, it restores the previous `current_class_name` to maintain the correct scope.
            *   *Parameters:*
                - **self** (CallResolverVisitor): The instance of the CallResolverVisitor class.
                - **node** (ast.ClassDef): The AST node representing the class definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method processes `ast.FunctionDef` nodes, which represent function or method definitions. It constructs a full identifier for the function, taking into account whether it's a method within a class or a top-level function. It then updates `current_caller_name` to this identifier before recursively visiting the function's body, and finally restores the `current_caller_name` to its previous value.
            *   *Parameters:*
                - **self** (CallResolverVisitor): The instance of the CallResolverVisitor class.
                - **node** (ast.FunctionDef): The AST node representing the function or method definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_Call`**
            *   *Signature:* `def visit_Call(self, node)`
            *   *Description:* This method is central to identifying and recording function and method calls. It attempts to resolve the fully qualified name of the called entity using the `_resolve_call_qname` helper method. If the callee is successfully resolved and exists in the `definitions` dictionary, it records the call, including information about the caller's file, line number, full identifier, and its type (e.g., module, method).
            *   *Parameters:*
                - **self** (CallResolverVisitor): The instance of the CallResolverVisitor class.
                - **node** (ast.Call): The AST node representing the function or method call.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method handles `ast.Import` statements. It iterates through the imported aliases and stores them in the `self.scope` dictionary, mapping the local name (either the alias or the original module name) to its fully qualified name. This mapping is crucial for `_resolve_call_qname` to correctly identify calls to imported modules or functions.
            *   *Parameters:*
                - **self** (CallResolverVisitor): The instance of the CallResolverVisitor class.
                - **node** (ast.Import): The AST node representing an import statement.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method processes `ast.ImportFrom` statements. It calculates the full module path for relative imports based on the `node.level` and the current `module_path`. It then stores the fully qualified name of each imported alias in `self.scope`, similar to `visit_Import`, which enables the resolution of names imported from specific modules.
            *   *Parameters:*
                - **self** (CallResolverVisitor): The instance of the CallResolverVisitor class.
                - **node** (ast.ImportFrom): The AST node representing an 'from ... import ...' statement.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_Assign`**
            *   *Signature:* `def visit_Assign(self, node)`
            *   *Description:* This method analyzes assignment statements to identify instances of classes. If an assignment involves a call to a constructor (e.g., `x = MyClass()`), it resolves the qualified name of the class and records the type of the assigned variable in `self.instance_types`. This information is later utilized by `_resolve_call_qname` to correctly resolve method calls made on these instances.
            *   *Parameters:*
                - **self** (CallResolverVisitor): The instance of the CallResolverVisitor class.
                - **node** (ast.Assign): The AST node representing an assignment statement.
            *   *Returns:*
            *   **Usage:**
        *   **`_resolve_call_qname`**
            *   *Signature:* `def _resolve_call_qname(self, func_node)`
            *   *Description:* This private helper method attempts to determine the fully qualified name (QName) of a function or method being called. It handles various scenarios, including direct name calls (checking `self.scope` and local pathnames) and attribute calls (e.g., `obj.method`). For attribute calls, it uses `self.instance_types` to find the class of the object or `self.scope` for module-level attributes to construct the QName.
            *   *Parameters:*
                - **self** (CallResolverVisitor): The instance of the CallResolverVisitor class.
                - **func_node** (ast.expr): The AST node representing the function or method being called (e.g., `ast.Name` for a direct call, `ast.Attribute` for a method call).
            *   *Returns:*
                - **name** (str | None): The fully qualified name of the callable if successfully resolved, otherwise `None`.
            *   *Usage:*

    ### File: `schemas/types.py`

    #### Class: `ParameterDescription`
    *   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to structure and validate information about a single parameter of a function. It serves as a clear, machine-readable schema for defining a parameter's name, its data type, and a concise description of its role. This class is fundamental for generating accurate documentation, API specifications, or for internal systems that require structured metadata about function arguments.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* The `__init__` method for ParameterDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance by validating and assigning values for the `name`, `type`, and `description` attributes based on the provided arguments, ensuring they conform to the specified string types.
        *   *Parameters:*
            - **name** (str): The name of the parameter being described.
            - **type** (str): The data type of the parameter, typically as a string representation (e.g., 'str', 'int', 'List[str]').
            - **description** (str): A brief textual explanation of the parameter's purpose or role.
    *   **Methods:**
    #### Class: `ReturnDescription`
    *   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to encapsulate the details of a function's return value. It provides a standardized structure to describe the name, data type, and a textual explanation of what a function returns, facilitating clear and machine-readable documentation of function outputs.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, has an implicitly generated constructor. It initializes an instance of ReturnDescription by accepting values for `name`, `type`, and `description`, which are then validated according to their type hints.
        *   *Parameters:*
            - **name** (str): The name or identifier of the return value.
            - **type** (str): The data type of the return value.
            - **description** (str): A brief explanation of what the return value represents.
    *   **Methods:**
    #### Class: `UsageContext`
    *   **Summary:** The `UsageContext` class is a Pydantic BaseModel designed to encapsulate the calling context of a function. It serves as a structured data container, holding information about what a function calls and by what it is called. This class provides a clear and consistent way to represent functional relationships within a system.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* "This class does not define an explicit `__init__` method. As a Pydantic BaseModel, its constructor is implicitly generated, allowing instances to be created by passing keyword arguments corresponding to its defined fields: `calls` and `called_by`."
        *   *Parameters:*
            - **calls** (str): Information about what the function calls.
            - **called_by** (str): Information about where the function is called from.
    *   **Methods:**
    #### Class: `FunctionDescription`
    *   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to provide a structured and detailed analysis of a Python function. It serves as a schema for encapsulating various aspects of a function, including its high-level purpose, signature parameters, return values, and its operational context within a larger system. This class is crucial for standardizing the representation of function metadata, enabling machine-readable documentation and analysis.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "This class is a Pydantic BaseModel, meaning its constructor (`__init__`) is automatically generated based on the defined fields. It initializes instances by validating and assigning values for the function's overall description, its parameters, its return values, and its usage context."
        *   *Parameters:*
            - **overall** (str): A concise, high-level summary describing the function's purpose and how it achieves its goal.
            - **parameters** (List[ParameterDescription]): A list of `ParameterDescription` objects, each detailing a specific input parameter of the function, including its name, type, and description.
            - **returns** (List[ReturnDescription]): A list of `ReturnDescription` objects, each detailing a specific return value of the function, including its name, type, and description.
            - **usage_context** (UsageContext): An object providing information about the function's external dependencies and where it is called within the codebase.
    *   **Methods:**
    #### Class: `FunctionAnalysis`
    *   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate the structured analysis of a single Python function. It serves as a standardized data model, holding the function's unique identifier, a comprehensive description object, and an optional field to report any errors encountered during its analysis. This class is crucial for representing machine-readable function metadata within a larger system.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`, `typing.Optional`
    *   **Constructor:**
        *   *Description:* The FunctionAnalysis class inherits from Pydantic's BaseModel, meaning its constructor is automatically generated. It initializes the instance by validating and assigning values to its `identifier`, `description`, and `error` fields based on the provided arguments during instantiation.
        *   *Parameters:*
            - **identifier** (str): The unique name or identifier of the function being analyzed.
            - **description** (FunctionDescription): An object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
            - **error** (Optional[str]): An optional string providing details if an error occurred during the function's analysis. Defaults to None.
    *   **Methods:**
    #### Class: `ConstructorDescription`
    *   **Summary:** The `ConstructorDescription` class is a Pydantic BaseModel designed to provide a structured representation of a Python class's `__init__` method. It encapsulates a high-level textual description of the constructor's purpose and a detailed list of its individual parameters, each described by a `ParameterDescription` object. This class serves as a data schema for documenting how other classes are initialized.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ConstructorDescription` is implicitly generated by Pydantic's BaseModel. It initializes an instance of this model by assigning the provided string `description` and a list of `ParameterDescription` objects to the corresponding instance attributes.
        *   *Parameters:*
            - **description** (str): A string summarizing the purpose and behavior of the constructor being described.
            - **parameters** (List[ParameterDescription]): A list of `ParameterDescription` objects, each detailing a parameter accepted by the constructor.
    *   **Methods:**
    #### Class: `ClassContext`
    *   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate contextual information about another class. It specifically stores details regarding the external dependencies that the class relies on and the locations within the codebase where the class is instantiated. This model provides a structured way to represent and manage usage context for classes.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The `__init__` method, implicitly generated by Pydantic's BaseModel, initializes an instance of ClassContext. It sets the `dependencies` and `instantiated_by` attributes based on the provided string values, ensuring the object accurately reflects the class's usage context."
        *   *Parameters:*
            - **dependencies** (str): A string summarizing the external dependencies of the class being described.
            - **instantiated_by** (str): A string summarizing where the class being described is instantiated within the codebase.
    *   **Methods:**
    #### Class: `ClassDescription`
    *   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of another Python class. It serves as a structured data container, holding an overall textual summary of the class, detailed information about its constructor, a list of analyses for each of its methods, and contextual information regarding its dependencies and instantiation points. This model is crucial for representing the output of a class analysis process in a standardized, machine-readable format.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "This class is a Pydantic BaseModel, meaning its constructor is implicitly generated by Pydantic. It initializes instances by accepting keyword arguments corresponding to its defined fields: 'overall', 'init_method', 'methods', and 'usage_context'. Pydantic handles validation and assignment of these values upon instantiation."
        *   *Parameters:*
            - **overall** (str): A high-level summary describing the primary purpose and responsibilities of the class being analyzed.
            - **init_method** (ConstructorDescription): An object containing a detailed description of the analyzed class's constructor, including its parameters.
            - **methods** (List[FunctionAnalysis]): A list of FunctionAnalysis objects, where each object provides a detailed analysis of a method within the analyzed class.
            - **usage_context** (ClassContext): An object containing contextual information about the analyzed class, such as its external dependencies and where it is instantiated.
    *   **Methods:**
    #### Class: `ClassAnalysis`
    *   **Summary:** The ClassAnalysis class serves as the primary Pydantic model for structuring the comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed description object that includes constructor and method analyses, and an optional field to report any errors encountered during the analysis. This model is designed to provide a standardized, machine-readable format for AI-driven code analysis outputs.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* The ClassAnalysis class does not explicitly define an `__init__` method. As a Pydantic BaseModel, its initialization is handled automatically by Pydantic, which validates and assigns values to its fields: `identifier`, `description`, and `error` upon instantiation.
        *   *Parameters:*
            - **identifier** (str): The unique name or identifier of the class to be analyzed.
            - **description** (ClassDescription): A detailed description object containing constructor and method analyses, and usage context.
            - **error** (Optional[str]): An optional field to report any errors encountered during the analysis. Defaults to None.
    *   **Methods:**
    #### Class: `CallInfo`
    *   **Summary:** The CallInfo class is a Pydantic BaseModel designed to structure and validate data related to a specific call event within a software system. It captures essential details such as the file path, the name of the calling function, the mode of the call (e.g., method, function), and the line number. This model serves as a standardized representation for tracking and analyzing relationships like 'called_by' and 'instantiated_by' across different code components.
    *   **Instantiation:** None explicitly in context.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* "This class utilizes Pydantic's BaseModel to automatically generate an __init__ method. The constructor is implicitly defined to accept and validate the 'file', 'function', 'mode', and 'line' attributes, ensuring that instances of CallInfo are created with the correct data types and structure."
        *   *Parameters:*
            - **file** (str): The path to the file where the call event occurred.
            - **function** (str): The name of the function or method that made the call.
            - **mode** (str): The type of call, e.g., 'method', 'function', 'module'.
            - **line** (int): The line number in the file where the call event occurred.
    *   **Methods:**
    #### Class: `FunctionContextInput`
    *   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to structure and encapsulate contextual information for analyzing a function. It serves as a data transfer object, defining two key attributes: 'calls', which lists the entities invoked by the function, and 'called_by', which details the locations or entities that invoke this function. This class provides a standardized and validated format for collecting and exchanging function-related context within a larger system, likely for automated code analysis or documentation.
    *   **Instantiation:** `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "This class inherits from Pydantic's BaseModel, meaning its __init__ method is automatically generated by Pydantic. It is used to initialize instances of FunctionContextInput by validating and assigning values to its 'calls' and 'called_by' attributes based on the provided arguments, ensuring data integrity according to the defined types."
        *   *Parameters:*
            - **calls** (List[str]): A list of identifiers (strings) representing other functions, methods, or classes that the function being analyzed calls.
            - **called_by** (List[CallInfo]): A list of CallInfo objects indicating the functions or methods that call the function being analyzed.
    *   **Methods:**
    #### Class: `FunctionAnalysisInput`
    *   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a FunctionAnalysis object. It acts as a data validation and parsing schema, ensuring that all necessary components like the analysis mode, function identifier, source code, imports, and contextual information are present and correctly typed before a function analysis can proceed. This class is fundamental for standardizing the data contract for function analysis tasks.
    *   **Instantiation:** `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The constructor for FunctionAnalysisInput is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting keyword arguments corresponding to its defined fields, performing data validation and type coercion as per the schema. This allows for easy creation of validated input objects."
        *   *Parameters:*
            - **mode** (Literal["function_analysis"]): Specifies the operational mode, which is fixed to 'function_analysis' for this input type, indicating the intent to analyze a function.
            - **identifier** (str): The unique name or identifier of the function that is to be analyzed.
            - **source_code** (str): The raw source code of the entire function definition to be analyzed.
            - **imports** (List[str]): A list of import statements (as strings) that are relevant to the source file where the function is defined.
            - **context** (FunctionContextInput): An object containing additional contextual information pertinent to the function, such as its dependencies or where it is called.
    *   **Methods:**
    #### Class: `MethodContextInput`
    *   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to define a structured schema for capturing contextual information about a method. It serves as a data transfer object or a validation schema for method-specific details, including its unique identifier, the functions or methods it calls, where it is called from, its arguments, and its docstring. This class ensures that method context data adheres to a predefined structure for consistency and validation.
    *   **Instantiation:** `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The `__init__` method for `MethodContextInput` is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting keyword arguments corresponding to its defined fields. During initialization, Pydantic performs data validation to ensure that the provided values conform to the specified types and constraints for each field."
        *   *Parameters:*
            - **identifier** (str): The unique name or identifier of the method being described.
            - **calls** (List[str]): A list of identifiers (strings) representing other methods, classes, or functions that this method calls within its implementation.
            - **called_by** (List[CallInfo]): A list of CallInfo objects, each detailing a specific location or context from which this method is invoked.
            - **args** (List[str]): A list of strings, where each string represents the name of an argument accepted by the method.
            - **docstring** (Optional[str]): An optional string containing the docstring associated with the method, providing a description of its purpose and usage.
    *   **Methods:**
    #### Class: `ClassContextInput`
    *   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information for analyzing a Python class. It serves as a data transfer object, holding lists of dependencies, instantiation points, and detailed method contexts. This model provides a standardized format for collecting and passing comprehensive data required for a holistic class analysis within a larger system.
    *   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The `__init__` method for ClassContextInput is implicitly generated by Pydantic's BaseModel. It handles the initialization of an instance by validating and assigning values to its defined fields: `dependencies`, `instantiated_by`, and `method_context` based on the provided input."
        *   *Parameters:*
            - **dependencies** (List[str]): A list of strings representing external dependencies relevant to the class being analyzed.
            - **instantiated_by** (List[CallInfo]): A list of CallInfo objects indicating where the class being analyzed is instantiated within the codebase.
            - **method_context** (List[MethodContextInput]): A list of MethodContextInput objects, each providing specific contextual information for individual methods within the class being analyzed.
    *   **Methods:**
    #### Class: `ClassAnalysisInput`
    *   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It acts as a schema validator, ensuring that all necessary components like the analysis mode, class identifier, source code, import statements, and contextual information are present and correctly typed before further processing. This class is fundamental for standardizing the input data for the class analysis pipeline.
    *   **Instantiation:** `backend.HelperLLM.main_orchestrator`, `backend.main.main_workflow`
    *   **Dependencies:** None explicitly listed.
    *   **Constructor:**
        *   *Description:* "The ClassAnalysisInput class does not explicitly define an __init__ method. As a Pydantic BaseModel, its constructor is implicitly generated, allowing instantiation by passing keyword arguments corresponding to its defined fields. This ensures automatic validation and assignment of input data to the class attributes."
        *   *Parameters:*
            - **mode** (Literal["class_analysis"]): Specifies the operational mode, which is fixed to 'class_analysis' for this input type.
            - **identifier** (str): The unique name or identifier of the class to be analyzed.
            - **source_code** (str): The raw source code of the entire class definition.
            - **imports** (List[str]): A list of import statements relevant to the source file containing the class.
            - **context** (ClassContextInput): Additional contextual information related to the class, such as dependencies and instantiation points.
    *   **Methods:**
```
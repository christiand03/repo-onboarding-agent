# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
    - **Description:** Repo Onboarding Agent is an AI-powered tool designed to facilitate the understanding of codebase architectures. It automates the documentation process by cloning repositories, analyzing abstract syntax trees (AST), generating dependency graphs, and utilizing Large Language Models (LLMs) to create detailed code documentation and interactive onboarding assistance.
    - **Key Features:** 
      - **Automated Repository Analysis:** Clones and parses Git repositories to extract file structures and ASTs.
      - **AI-Driven Documentation:** Uses Helper LLMs (Gemini, OpenAI, Ollama) to generate descriptions for functions and classes.
      - **Dependency Visualization:** Generates call graphs and file dependency charts using NetworkX.
      - **Interactive Frontend:** Provides a Streamlit-based UI for users to view reports and interact with the analyzed data.
      - **Multi-LLM Support:** Supports various models including Google Gemini, OpenAI GPT, and local Ollama models.
    - **Tech Stack:** Python, Streamlit, LangChain, NetworkX, GitPython, MongoDB (pymongo), Pydantic, Matplotlib, OpenAI, Google Generative AI.

*   **Repository Structure:**
    ```mermaid
    graph LR
    root --> .env.example <br/> .gitignore <br/> analysis_output.json <br/> output.json <br/> output.toon <br/> readme.md <br/> requirements.txt <br/> test.json
    root --> SystemPrompts
    SystemPrompts --> SystemPromptClassHelperLLM.txt <br/> SystemPromptFunctionHelperLLM.txt <br/> SystemPromptHelperLLM.txt <br/> SystemPromptMainLLM.txt <br/> SystemPromptMainLLMToon.txt <br/> SystemPromptNotebookLLM.txt
    root --> backend
    backend --> AST_Schema.py <br/> File_Dependency.py <br/> HelperLLM.py <br/> MainLLM.py <br/> __init__.py <br/> basic_info.py <br/> callgraph.py <br/> converter.py <br/> getRepo.py <br/> main.py <br/> relationship_analyzer.py <br/> scads_key_test.py
    root --> database
    database --> db.py
    root --> frontend
    frontend --> .streamlit
    .streamlit --> config.toml
    frontend --> __init__.py <br/> frontend.py
    frontend --> gifs
    gifs --> 4j.gif
    root --> notizen
    notizen --> Report Agenda.txt <br/> Zwischenpraesentation Agenda.txt <br/> doc_bestandteile.md <br/> notizen.md <br/> paul_notizen.md <br/> praesentation_notizen.md <br/> technische_notizen.md
    notizen --> grafiken
    grafiken --> 1
    1 --> File_Dependency_Graph_Repo.dot <br/> global_callgraph.png <br/> global_graph.png <br/> global_graph_2.png <br/> repo.dot
    grafiken --> 2
    2 --> FDG_repo.dot <br/> fdg_graph.png <br/> fdg_graph_2.png <br/> filtered_callgraph_flask.png <br/> filtered_callgraph_repo-agent.png <br/> filtered_callgraph_repo-agent_3.png <br/> filtered_repo_callgraph_flask.dot <br/> filtered_repo_callgraph_repo-agent-3.dot <br/> filtered_repo_callgraph_repo-agent.dot <br/> global_callgraph.png <br/> graph_flask.md <br/> repo.dot
    grafiken --> Flask-Repo
    Flask-Repo --> __init__.dot <br/> __main__.dot <br/> app.dot <br/> auth.dot <br/> blog.dot <br/> blueprints.dot <br/> cli.dot <br/> conf.dot <br/> config.dot <br/> conftest.dot <br/> ctx.dot <br/> db.dot <br/> debughelpers.dot <br/> factory.dot <br/> flask.dot <br/> globals.dot <br/> hello.dot <br/> helpers.dot <br/> importerrorapp.dot <br/> logging.dot <br/> make_celery.dot <br/> multiapp.dot <br/> provider.dot <br/> scaffold.dot <br/> sessions.dot <br/> signals.dot <br/> tag.dot <br/> tasks.dot <br/> templating.dot <br/> test_appctx.dot <br/> test_async.dot <br/> test_auth.dot <br/> test_basic.dot <br/> test_blog.dot <br/> test_blueprints.dot <br/> test_cli.dot <br/> test_config.dot <br/> test_config.png <br/> test_converters.dot <br/> test_db.dot <br/> test_factory.dot <br/> test_helpers.dot <br/> test_instance_config.dot <br/> test_js_example.dot <br/> test_json.dot <br/> test_json_tag.dot <br/> test_logging.dot <br/> test_regression.dot <br/> test_reqctx.dot <br/> test_request.dot <br/> test_session_interface.dot <br/> test_signals.dot <br/> test_subclassing.dot <br/> test_templating.dot <br/> test_testing.dot <br/> test_user_error_handler.dot <br/> test_views.dot <br/> testing.dot <br/> typing.dot <br/> typing_app_decorators.dot <br/> typing_error_handler.dot <br/> typing_route.dot <br/> views.dot <br/> wrappers.dot <br/> wsgi.dot
    grafiken --> Repo-onboarding
    Repo-onboarding --> AST.dot <br/> Frontend.dot <br/> HelperLLM.dot <br/> HelperLLM.png <br/> MainLLM.dot <br/> agent.dot <br/> basic_info.dot <br/> callgraph.dot <br/> getRepo.dot <br/> graph_AST.png <br/> graph_AST2.png <br/> graph_AST3.png <br/> main.dot <br/> tools.dot <br/> types.dot
    root --> result
    result --> ast_schema_01_12_2025_11-49-24.json <br/> notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md <br/> notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md <br/> notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md <br/> notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md <br/> notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md <br/> notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md <br/> report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md <br/> report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md <br/> report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md <br/> report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md <br/> report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md <br/> report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md <br/> report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md <br/> report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md <br/> report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md <br/> report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md <br/> report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md <br/> report_14_11_2025_14-52-36.md <br/> report_14_11_2025_15-21-53.md <br/> report_14_11_2025_15-26-24.md <br/> report_21_11_2025_15-43-30.md <br/> report_21_11_2025_16-06-12.md <br/> report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md <br/> report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md <br/> result_2025-11-11_12-30-53.md <br/> result_2025-11-11_12-43-51.md <br/> result_2025-11-11_12-45-37.md
    root --> schemas
    schemas --> types.py
    root --> statistics
    statistics --> savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png <br/> savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png <br/> savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png <br/> savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png <br/> savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png
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
    
    *Note: "pip install -r requirements.txt"*

    ### Setup Guide
    1. Clone the repository.
    2. Install dependencies using `pip install -r requirements.txt`.
    3. Configure environment variables by copying `.env.example` to `.env`.
    4. Ensure a MongoDB instance is running (as `pymongo` is used).

    ### Quick Startup
    To launch the frontend application:
    ```bash
    streamlit run frontend/frontend.py
    ```

    ## 3. Use Cases & Commands
    ### Use Cases
    1.  **Codebase Onboarding**: New developers can use the tool to generate a comprehensive report on a Git repository, understanding its file structure, call graphs, and class hierarchies without manual code review.
    2.  **Legacy Code Documentation**: Users can analyze older projects to generate automated documentation where it is missing, including visualizing dependency graphs.
    3.  **Notebook Analysis**: The tool supports processing Jupyter Notebooks (`.ipynb`) to extract logic and generate reports, useful for data science projects.

    ### Commands
    *   **Start Application**: `streamlit run frontend/frontend.py`

    ## 4. Architecture
    The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here



## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to systematically traverse a Python Abstract Syntax Tree (AST). Its core function is to extract and structure metadata about imports, class definitions, and function definitions (both synchronous and asynchronous) found within a given source code. It populates an internal `schema` dictionary with detailed information, including identifiers, names, docstrings, and source code segments, while maintaining context to correctly associate methods with their parent classes.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** The class depends on the `ast` module for its core functionality as an AST visitor, and implicitly relies on the `path_to_module` function for resolving module paths.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes an `ASTVisitor` instance, setting up essential attributes for AST traversal and data collection. It stores the raw source code, file path, and project root, then calculates the `module_path`. It also initializes an empty `schema` dictionary to store discovered imports, functions, and classes, and sets `_current_class` to `None` to track the class currently being visited.
    *   *Parameters:*
        - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
        - **source_code** (`str`): The raw Python source code string to be analyzed.
        - **file_path** (`str`): The absolute file path of the source code being analyzed.
        - **project_root** (`str`): The root directory of the project, used to determine the module path.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self: ASTVisitor, node: ast.Import)`
        *   *Description:* This method is invoked by the `ast.NodeVisitor` when an `ast.Import` node is encountered, representing a simple import statement (e.g., `import os`). It iterates through each alias in the import node and appends the name of the imported module or package to the `self.schema["imports"]` list. After processing the import, it calls `self.generic_visit(node)` to ensure that any child nodes (though typically none for simple imports) are also visited.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.Import`): The AST node representing an 'import' statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self.generic_visit` to continue AST traversal.
            *   Called By: This method is implicitly called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.Import` node is encountered during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self: ASTVisitor, node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to 'from ... import ...' statements. It iterates over the aliases within the import node and constructs a fully qualified import string (e.g., 'module.name') which is then appended to the `self.schema["imports"]` list. Following this, `self.generic_visit(node)` is called to ensure that any nested nodes within the import statement, if present, are also processed.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self.generic_visit` to continue AST traversal.
            *   Called By: This method is implicitly called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ImportFrom` node is encountered during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self: ASTVisitor, node: ast.ClassDef)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions in the source code. It constructs a dictionary containing comprehensive information about the class, including its identifier, name, docstring, and the exact source code segment. This `class_info` is then added to `self.schema["classes"]`. Crucially, it sets `self._current_class` to this `class_info` before calling `self.generic_visit(node)` to allow nested methods to be correctly associated with this class, and then resets `_current_class` to `None` after the visit.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `ast.get_docstring` to extract the class docstring, `ast.get_source_segment` to retrieve the class's source code, and `self.generic_visit` for further AST traversal.
            *   Called By: This method is implicitly called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ClassDef` node is encountered during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self: ASTVisitor, node: ast.FunctionDef)`
        *   *Description:* This method is responsible for processing `ast.FunctionDef` nodes, which represent standard function definitions. It first checks if a class is currently being visited (`self._current_class`). If a class context exists, the function is treated as a method, and its details are appended to the `method_context` of the current class. Otherwise, it's considered a standalone function, and its information is added to `self.schema["functions"]`. Finally, `self.generic_visit(node)` is called to continue traversing any nested nodes within the function definition.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `ast.get_docstring` to extract the function docstring, `ast.get_source_segment` to retrieve the function's source code, and `self.generic_visit` for further AST traversal.
            *   Called By: This method is implicitly called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.FunctionDef` node is encountered during AST traversal. It is also explicitly called by `visit_AsyncFunctionDef`.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self: ASTVisitor, node: ast.AsyncFunctionDef)`
        *   *Description:* This method handles `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation is straightforward: it simply delegates the entire processing logic to the `visit_FunctionDef` method. This approach ensures that asynchronous functions are treated similarly to regular functions for the purpose of schema extraction, capturing their identifier, name, arguments, docstring, and line numbers within the appropriate class or module context.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self.visit_FunctionDef` to process the asynchronous function node.
            *   Called By: This method is implicitly called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.AsyncFunctionDef` node is encountered during AST traversal.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to perform static analysis on a codebase, specifically focusing on Python files within a Git repository. It constructs a detailed Abstract Syntax Tree (AST) schema for the files, identifying functions, classes, and their internal structures. Furthermore, it integrates call relationship data, such as incoming/outgoing calls and class instantiations, to provide a holistic view of the codebase's structure and interdependencies.
*   **Instantiation:** This class is not explicitly instantiated by any known entities in the provided context.
*   **Dependencies:** This class depends on the `ast` module for parsing Python code, the `os` module for path manipulation, and `getRepo.GitRepository` for repository interaction.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It currently does not perform any specific setup or attribute initialization, acting as a placeholder.
    *   *Parameters:*
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates call relationship data (incoming and outgoing calls, class instantiations, and method dependencies) into an existing AST schema. It iterates through files, functions, and classes within the `full_schema`. For each function, it assigns `calls` and `called_by` lists from `raw_relationships`. For each class, it assigns `instantiated_by` and then iterates through its methods to assign their `calls` and `called_by` lists, also calculating class-level dependencies based on method calls external to the class.
        *   *Parameters:*
            - **full_schema** (`dict`): The complete AST schema containing file, function, and class definitions to be updated.
            - **raw_relationships** (`dict`): A dictionary containing raw incoming and outgoing call relationships to be merged.
        *   *Returns:*
            - **full_schema** (`dict`): The `full_schema` dictionary updated with the integrated relationship data.
        *   **Usage:**
            *   Calls: This method does not explicitly call other functions or methods based on the provided context.
            *   Called By: This method is not explicitly called by any other functions or methods based on the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to build a comprehensive AST-based schema for the Python files. It initializes an empty `full_schema` and determines the `project_root`. It then iterates through each file, skipping non-Python files or empty files. For valid Python files, it parses the content into an AST, uses an `ASTVisitor` to extract schema nodes (imports, functions, classes), and populates the `full_schema` dictionary, including error handling for parsing failures.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each expected to have `path` and `content` attributes, representing files from the repository.
            - **repo** (`GitRepository`): An object representing the Git repository, used for context but not directly manipulated within this method's provided source.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed repository, containing parsed nodes for files, functions, and classes.
        *   **Usage:**
            *   Calls: This method calls `os.path.commonpath`, `os.path.isfile`, `os.path.dirname`, `ast.parse`, instantiates `ASTVisitor`, calls `visitor.visit`, and `print` for warnings.
            *   Called By: This method is not explicitly called by any other functions or methods based on the provided context.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into a Python module import path. It first attempts to determine the relative path of the file from a specified project root. If this fails, it defaults to using just the base name of the file. The function then removes the '.py' extension if present and replaces system path separators with dots to form the module path. Finally, it handles '__init__.py' files by removing the '.__init__' suffix from the module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path (e.g., 'my_package.my_module').
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class extends NodeVisitor to analyze Python source code files and construct a graph of their import dependencies. It processes AST nodes representing import statements, specifically handling both direct and relative imports. The class's core functionality involves resolving module and symbol names, especially for complex relative imports, and populating an internal dictionary that maps each analyzed file to the set of modules or symbols it imports.
*   **Instantiation:** The class is not explicitly instantiated by any other components according to the provided context.
*   **Dependencies:** The class has no explicit external functional dependencies listed in the provided context.
*   **Constructor:**
    *   *Description:* This constructor initializes the FileDependencyGraph instance by storing the path to the Python file currently being analyzed and the root directory of the repository. These attributes, `self.filename` and `self.repo_root`, are essential for correctly resolving file paths and relative import statements during the AST traversal.
    *   *Parameters:*
        - **filename** (`str`): The path to the Python file whose dependencies are being analyzed.
        - **repo_root** (`str`): The root directory of the repository, used as a base for resolving file paths.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(node: ImportFrom)`
        *   *Description:* This private method is responsible for resolving relative import statements, such as `from .. import name1, name2`. It calculates the correct base directory by traversing up the file system hierarchy based on the import level specified in the AST node. It then checks for the existence of corresponding module files or symbols exported via `__init__.py` files using nested helper functions. If no valid module or symbol can be resolved from the relative import, an `ImportError` is raised.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the relative import statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of successfully resolved module or symbol names.
        *   **Usage:**
            *   Calls: This method does not explicitly call other functions or methods according to the provided context.
            *   Called By: This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* This method, part of the AST NodeVisitor pattern, is invoked when an `Import` or `ImportFrom` node is encountered during the AST traversal. Its primary purpose is to record the identified import dependencies. It adds the imported module or symbol, specified by `base_name` or `alias.name`, to the `import_dependencies` dictionary, associating it with the `self.filename`. After processing the current node, it calls `self.generic_visit(node)` to continue the traversal.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing the import statement.
            - **base_name** (`str | None`): An optional base name for the module, typically used when the module part of an `ImportFrom` statement has already been resolved.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method does not explicitly call other functions or methods according to the provided context.
            *   Called By: This method is not explicitly called by other functions or methods according to the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ImportFrom)`
        *   *Description:* This method specifically handles `ImportFrom` AST nodes, which represent `from module import name` statements. It first attempts to extract the module name from the node. If an explicit module name exists, it extracts the last part of the module path and record it as a dependency using `visit_Import`. If the import is relative (i.e., no explicit module name), it delegates the resolution to the `_resolve_module_name` method. For each resolved dependency, it then calls `visit_Import` to record it. The method includes error handling for failed relative import resolutions and continues the AST traversal by calling `self.generic_visit(node).
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the `from ... import ...` statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method does not explicitly call other functions or methods according to the provided context.
            *   Called By: This method is not explicitly called by other functions or methods according to the provided context.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and uses a custom `FileDependencyGraph` visitor to traverse the AST, collecting import relationships. It then populates the graph with nodes for files and edges representing import dependencies, finally returning the complete dependency graph.
*   **Parameters:**
    - **filename** (`str`): The name of the file being analyzed to build its dependency graph.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file, which will be traversed to find dependencies.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative file paths during dependency analysis.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies between them.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** The `build_repository_graph` function constructs a directed graph representing file-level dependencies across an entire Git repository. It processes each Python file within the provided repository, parsing its content into an Abstract Syntax Tree (AST). For each file, it generates a local dependency graph and then integrates these into a single global NetworkX directed graph. The function aggregates nodes and edges from individual file graphs to form a comprehensive repository-wide dependency view.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object representing the code repository to be analyzed for file dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph (DiGraph) where nodes represent files or entities within files, and edges represent dependencies between them, aggregated across the entire repository.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input, resolves it to an absolute path, and then recursively searches for all files with a '.py' extension. For each identified Python file, it calculates its path relative to the initial root directory. The function then returns a list containing these relative `pathlib.Path` objects.
*   **Parameters:**
    - **directory** (`str`): The string path to the root directory from which to start the recursive search for Python files.
*   **Returns:**
    - **all_files** (`list[pathlib.Path]`): A list of `pathlib.Path` objects, where each object represents a Python file found. The paths are relative to the `directory` argument provided.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs), including Google Gemini, OpenAI, and custom/Ollama models, to generate structured documentation for Python functions and classes. It handles API key management, prompt loading, dynamic LLM configuration based on the model name, and robust batch processing with error handling and rate limiting. The class ensures that generated outputs conform to predefined Pydantic schemas for `FunctionAnalysis` and `ClassAnalysis`.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes the LLMHelper instance by setting up the API key, loading system prompts from specified file paths, and configuring the appropriate LLM client based on the `model_name`. It also determines the batch size for API calls and initializes specialized LLM clients for structured output of function and class analyses.
    *   *Parameters:*
        - **self** (`LLMHelper`): 
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt used for generating function documentation.
        - **class_prompt_path** (`str`): The file path to the system prompt used for generating class documentation.
        - **model_name** (`str`): The name of the LLM model to use (default: 'gemini-2.0-flash-lite'). This determines the specific LLM client and batch settings.
        - **base_url** (`str`): An optional base URL for custom or Ollama LLM endpoints. If not provided, OLLAMA_BASE_URL is used for Ollama models.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* The `_configure_batch_settings` method dynamically sets the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. This internal method optimizes API call concurrency and rate limit adherence for different LLM models. It assigns specific batch sizes for various Gemini, Llama, and GPT models, and applies a conservative default for unknown or custom models.
        *   *Parameters:*
            - **self** (`LLMHelper`): 
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods or functions.
            *   Called By: This method is not explicitly called by other functions or methods.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* The `generate_for_functions` method processes a list of `FunctionAnalysisInput` objects to generate structured documentation for functions using the configured LLM. It prepares JSON payloads, batches conversations for efficient API calls, and includes mechanisms for error handling and respecting API rate limits by pausing between batches. The method returns a list of `FunctionAnalysis` objects, with `None` for any failed generations.
        *   *Parameters:*
            - **self** (`LLMHelper`): 
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary context for generating documentation for a single function.
        *   *Returns:*
            - **all_validated_functions** (`List[Optional[FunctionAnalysis]]`): A list of generated `FunctionAnalysis` objects, or `None` for inputs where generation failed.
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods or functions.
            *   Called By: This method is not explicitly called by other functions or methods.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* The `generate_for_classes` method is responsible for generating structured documentation for a batch of classes. It takes a list of `ClassAnalysisInput` objects, converts them into JSON payloads, and constructs conversations for the LLM. The method then performs batched API calls to the LLM, managing concurrency, handling potential errors, and implementing a waiting period to comply with rate limits. It returns a list of `ClassAnalysis` objects, with `None` for any inputs that failed processing.
        *   *Parameters:*
            - **self** (`LLMHelper`): 
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary context for generating documentation for a single class.
        *   *Returns:*
            - **all_validated_classes** (`List[Optional[ClassAnalysis]]`): A list of generated `ClassAnalysis` objects, or `None` for inputs where generation failed.
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods or functions.
            *   Called By: This method is not explicitly called by other functions or methods.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a test orchestrator for the LLMHelper class, demonstrating its functionality by processing pre-defined dummy data. It defines multiple `FunctionAnalysisInput` and `FunctionAnalysis` objects, along with a `ClassAnalysisInput`. It then initializes an `LLMHelper` instance and uses it to generate documentation for the defined functions, finally logging and printing the aggregated results.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a central interface for interacting with various Large Language Models (LLMs). It abstracts away the specifics of different LLM providers (Google Gemini, OpenAI, Ollama, or custom APIs) by dynamically configuring the appropriate client during initialization based on the model name. The class provides methods for both single-shot synchronous calls and streaming responses, making it versatile for different interaction patterns with LLMs.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the MainLLM instance by setting up the API key, loading a system prompt from a specified file path, and configuring the appropriate LLM client (ChatGoogleGenerativeAI, ChatOpenAI, or ChatOllama) based on the provided model name and an optional base URL. It validates the API key and handles potential FileNotFoundError for the prompt file, raising exceptions if critical setup fails.
    *   *Parameters:*
        - **self** (`MainLLM`): 
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **prompt_file_path** (`str`): The file path to a text file containing the system prompt that will guide the LLM's behavior.
        - **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.5-pro'. This name determines which LLM client (e.g., Gemini, OpenAI, Ollama) is instantiated.
        - **base_url** (`str`): An optional base URL for custom LLM APIs, such as those hosted locally or via specific services like SCADSLLM or Ollama.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* This method sends a user's input to the configured Large Language Model for a single, non-streaming response. It constructs a list of messages, including the pre-loaded system prompt and the user's query, and then invokes the LLM client. The method logs the process and returns the content of the LLM's response, or None if an error occurs during the API call.
        *   *Parameters:*
            - **self** (`MainLLM`): 
            - **user_input** (`str`): The textual input or query provided by the user to be processed by the LLM.
        *   *Returns:*
            - **content** (`str | None`): The textual response content from the LLM, or None if an exception occurred during the call.
        *   **Usage:**
            *   Calls: This method calls SystemMessage, HumanMessage, self.llm.invoke, logging.info, and logging.error.
            *   Called By: This method is not explicitly called by other methods within the provided context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* This method facilitates streaming responses from the configured Large Language Model for a given user input, allowing for real-time processing of content chunks. It prepares the system and human messages, then initiates a streaming call to the LLM client. Each chunk of content received from the stream is yielded, and any errors encountered during the streaming process are logged and yielded as an error message string.
        *   *Parameters:*
            - **self** (`MainLLM`): 
            - **user_input** (`str`): The textual input or query from the user for which a streaming LLM response is requested.
        *   *Returns:*
            - **chunk.content** (`str`): A generator yielding individual string chunks of the LLM's streamed response, or an error message string if an exception occurs.
        *   **Usage:**
            *   Calls: This method calls SystemMessage, HumanMessage, self.llm.stream, logging.info, and logging.error.
            *   Called By: This method is not explicitly called by other methods within the provided context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is responsible for systematically extracting and consolidating fundamental project information from various common project files. It parses README files for general overview, pyproject.toml for structured metadata and dependencies, and requirements.txt as a fallback for dependencies. The class prioritizes information sources and provides a structured dictionary containing details like project title, description, features, tech stack, status, installation instructions, quick start guides, and dependencies. It also includes utility methods for content cleaning, file searching, and Markdown section extraction.
*   **Instantiation:** The class is not explicitly instantiated by other functions or methods according to the provided context.
*   **Dependencies:** The class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the ProjektInfoExtractor instance. It sets a constant INFO_NICHT_GEFUNDEN for placeholder values and creates a nested dictionary self.info to store extracted project details, pre-populating all fields with the "Information not found" placeholder.
    *   *Parameters:*
        - **self** (`ProjektInfoExtractor`): The instance of the class.
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content: str)`
        *   *Description:* This private helper method is designed to sanitize string content by removing null bytes (\x00). Null bytes can appear in text due to incorrect encoding assumptions, such as reading a UTF-16 encoded file as UTF-8. The method first checks if the input content is empty; if so, it returns an empty string. Otherwise, it performs a string replacement to remove all occurrences of the null byte.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): 
            - **content** (`str`): The string content to be cleaned.
        *   *Returns:*
            - **None** (`str`): The cleaned string content with null bytes removed.
        *   **Usage:**
            *   Calls: This method does not explicitly call other functions or methods according to the provided context.
            *   Called By: This method is called by _parse_readme, _parse_toml, and _parse_requirements.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This private helper method searches a list of file objects for a file whose path matches any of the provided patterns. It performs a case-insensitive comparison by converting both the file path and the patterns to lowercase. The method iterates through each file and then through each pattern, returning the first file that matches any pattern. If no matching file is found after checking all files and patterns, it returns None.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): 
            - **patterns** (`List[str]`): A list of string patterns to match against file paths.
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have a 'path' attribute.
        *   *Returns:*
            - **None** (`Optional[Any]`): The first file object whose path matches one of the patterns, or None if no match is found.
        *   **Usage:**
            *   Calls: This method does not explicitly call other functions or methods according to the provided context.
            *   Called By: This method is called by extrahiere_info.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This private method extracts content from a Markdown string that appears under a level 2 heading (##). It takes the full Markdown content and a list of keywords. It constructs a regular expression to find headings matching any of the keywords (case-insensitively) and then captures all text following that heading until the next level 2 heading or the end of the document. If a match is found, the extracted and stripped text is returned; otherwise, None is returned.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): 
            - **inhalt** (`str`): The Markdown content string to parse.
            - **keywords** (`List[str]`): A list of keywords to match against Markdown section headings.
        *   *Returns:*
            - **None** (`Optional[str]`): The extracted section content as a string, or None if no matching section is found.
        *   **Usage:**
            *   Calls: This method calls re.escape, re.compile, and re.search.
            *   Called By: This method is called by _parse_readme.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This private method parses the content of a README file to extract various project details and update the self.info dictionary. It first cleans the input content using _clean_content. It then attempts to extract the project title from a level 1 Markdown heading (#) and a general description. Subsequently, it uses _extrahiere_sektion_aus_markdown to find and extract specific sections like "Key Features", "Tech Stack", "Status", "Installation", and "Quick Start" based on predefined keywords. The extracted information is stored in the self.info attribute, prioritizing existing values if they are not the INFO_NICHT_GEFUNDEN placeholder.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): 
            - **inhalt** (`str`): The raw string content of the README file.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls self._clean_content, re.search, and self._extrahiere_sektion_aus_markdown.
            *   Called By: This method is called by extrahiere_info.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project metadata. It first cleans the input content using _clean_content. It then checks for the availability of the tomllib module; if not found, it prints a warning and exits. Using tomllib.loads, it attempts to parse the TOML content. If successful, it extracts the project name, description, and dependencies from the [project] section and updates the self.info dictionary. Error handling is included for TOMLDecodeError.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): 
            - **inhalt** (`str`): The raw string content of the pyproject.toml file.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls self._clean_content, tomllib.loads, data.get, and print.
            *   Called By: This method is called by extrahiere_info.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This private method parses the content of a requirements.txt file to extract project dependencies. It first cleans the input content using _clean_content. It only proceeds to extract dependencies if the dependencies field in self.info is still set to the INFO_NICHT_GEFUNDEN placeholder, indicating that dependencies were not already found in a pyproject.toml file. It then splits the content into lines, filters out empty lines and comments, and stores the non-comment lines as a list of dependencies in self.info.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): 
            - **inhalt** (`str`): The raw string content of the requirements.txt file.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls self._clean_content.
            *   Called By: This method is called by extrahiere_info.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This public method orchestrates the entire process of extracting project information from a given list of file objects and a repository URL. It first uses _finde_datei to locate README, pyproject.toml, and requirements.txt files. It then parses these files in a prioritized order: pyproject.toml first (for dependencies), then requirements.txt (as a fallback for dependencies), and finally README (for general project overview). After parsing, it formats the extracted dependencies into a human-readable string. If no project title is found from the files, it attempts to derive one from the repository URL. Finally, it returns the self.info dictionary containing all gathered project details.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): 
            - **dateien** (`List[Any]`): A list of file-like objects, each expected to have path and content attributes.
            - **repo_url** (`str`): The URL of the repository, used as a fallback for deriving the project title.
        *   *Returns:*
            - **None** (`Dict[str, Any]`): A dictionary containing all extracted project information.
        *   **Usage:**
            *   Calls: This method calls self._finde_datei, self._parse_toml, self._parse_requirements, self._parse_readme, os.path.basename, and repo_url.removesuffix.
            *   Called By: This method is not explicitly called by other functions or methods according to the provided context.

### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an ast.NodeVisitor designed to construct a directed call graph for a given Python source file. It traverses the Abstract Syntax Tree (AST) of the file, identifying function and class definitions, import statements, and function calls. By maintaining context of the current file, class, and function, it resolves call targets to fully qualified names and records them as edges in a NetworkX graph. This class effectively maps out the inter-function dependencies within a Python module.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** This class depends on the 'ast' module for parsing Python code and the 'networkx' library for graph representation.
*   **Constructor:**
    *   *Description:* This constructor initializes the CallGraph instance by setting the filename, initializing internal state variables for tracking current function/class context, and setting up various data structures. These include a NetworkX DiGraph for the call graph, dictionaries for local definitions and import mappings, and sets for functions and edges, all essential for building the call graph.
    *   *Parameters:*
        - **filename** (`str`): The path to the source file being analyzed by the call graph.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node: ast.AST)`
        *   *Description:* This private helper method recursively extracts the components of a callable's name from an AST node. It handles different AST node types: for an ast.Call, it recurses on the function part; for an ast.Name, it returns the identifier; and for an ast.Attribute, it recurses on the value and appends the attribute name. This process effectively reconstructs the dotted path of a function or method call, such as ['pkg', 'mod', 'Class', 'method'].
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **node** (`ast.AST`): An AST node representing a call, name, or attribute from which to extract name components.
        *   *Returns:*
            - **name_components** (`list[str]`): A list of string components representing the dotted name of the callable.
        *   **Usage:**
            *   Calls: This method calls itself recursively to traverse the AST node structure.
            *   Called By: This method is called by visit_Call.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* This private method takes a list of potential callee name components and attempts to resolve them to their fully qualified names. It prioritizes resolution by checking local definitions, then import mappings, and finally constructs a full name based on the current filename and class context if no other resolution is found. This ensures that call targets are identified consistently across different scopes within the analyzed code.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **callee_nodes** (`list[list[str]]`): A list where each inner list represents the name components of a potential callee.
        *   *Returns:*
            - **resolved_names** (`list[str]`): A list of fully qualified string names for the resolved callees.
        *   **Usage:**
            *   Calls: This method accesses self.local_defs, self.import_mapping, self.current_class, and self.filename.
            *   Called By: This method is called by visit_Call.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None)`
        *   *Description:* This private helper method constructs a fully qualified name for a function or method. It prepends the self.filename to the basename provided. If a class_name is also supplied, it includes the class name in the fully qualified path, using '::' as a separator. This ensures unique identification of functions and methods within the context of the file and class, which is crucial for building an accurate call graph.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`str | None`): An optional name of the class if the function is a method within a class.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name of the function or method.
        *   **Usage:**
            *   Calls: This method accesses self.filename.
            *   Called By: This method is called by visit_FunctionDef.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private method determines the identifier of the current calling context. If self.current_function is set, it returns that value, indicating a function is currently being processed. Otherwise, it constructs a string representing the global scope, using the self.filename if available, or '<global-scope>' as a fallback. This is crucial for correctly attributing calls in the call graph to their origin.
        *   *Parameters:*
            - **self** (`CallGraph`): 
        *   *Returns:*
            - **caller_identifier** (`str`): The identifier of the current caller, which can be a fully qualified function name or a global scope identifier.
        *   **Usage:**
            *   Calls: This method accesses self.current_function and self.filename.
            *   Called By: This method is called by visit_Call.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method, overriding an ast.NodeVisitor method, processes 'import' statements. It iterates through the imported modules and their aliases, populating self.import_mapping to store the relationship between the alias (or original name) and the module name. This mapping is essential for resolving fully qualified names of imported entities later during call graph construction. After processing, it calls self.generic_visit(node) to continue traversing the AST.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **node** (`ast.Import`): An AST node representing an 'import' statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls self.generic_visit.
            *   Called By: This method is implicitly called by the AST traversal mechanism when an ast.Import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method, overriding an ast.NodeVisitor method, processes 'from ... import ...' statements. It extracts the module name and then iterates through the imported names and their aliases. It populates self.import_mapping to associate the alias (or original name) with the module from which it was imported. This mapping is crucial for resolving fully qualified names of imported entities during subsequent call graph analysis.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **node** (`ast.ImportFrom`): An AST node representing an 'import from' statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method accesses self.import_mapping.
            *   Called By: This method is implicitly called by the AST traversal mechanism when an ast.ImportFrom node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method, overriding an ast.NodeVisitor method, handles class definitions. It temporarily updates self.current_class to the name of the class currently being visited, allowing nested methods to correctly determine their full names. It then performs a generic visit to traverse the class's body and restores the previous self.current_class context upon exiting the class definition, ensuring proper scope management.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **node** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls self.generic_visit.
            *   Called By: This method is implicitly called by the AST traversal mechanism when an ast.ClassDef node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method processes regular function definitions within the AST. It saves the current function context, constructs the full qualified name for the new function using _make_full_name, and registers this name in self.local_defs. It then updates self.current_function, adds the function as a node to the self.graph, performs a generic visit to traverse the function's body, adds the function to self.function_set, and finally restores the previous function context, ensuring proper call graph construction.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **node** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls _make_full_name and self.generic_visit.
            *   Called By: This method is implicitly called by the AST traversal mechanism when an ast.FunctionDef node is encountered. It is also called by visit_AsyncFunctionDef.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
        *   *Description:* This method processes asynchronous function definitions within the AST. It delegates the entire processing to the visit_FunctionDef method, as the logic for handling both synchronous and asynchronous function definitions is identical in terms of call graph construction and name resolution. This approach avoids code duplication and maintains consistency in how functions, regardless of their async nature, are added to the call graph.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **node** (`ast.AsyncFunctionDef`): An AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls visit_FunctionDef.
            *   Called By: This method is implicitly called by the AST traversal mechanism when an ast.AsyncFunctionDef node is encountered.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method processes function call expressions encountered during AST traversal. It first determines the current caller using _current_caller, then extracts the potential callee name components using _recursive_call, and finally resolves these components to fully qualified names using _resolve_all_callee_names. It then records the call by adding the resolved callees to the self.edges dictionary under the caller. A generic visit is performed to continue traversing the AST after recording the call.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **node** (`ast.Call`): An AST node representing a function call.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls _current_caller, _recursive_call, _resolve_all_callee_names, and self.generic_visit.
            *   Called By: This method is implicitly called by the AST traversal mechanism when an ast.Call node is encountered.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node: ast.If)`
        *   *Description:* This method processes 'if' statements within the AST. It includes special handling for the 'if __name__ == "__main__":' block, temporarily setting self.current_function to '<main_block>' to correctly attribute calls originating from this entry point. For all other 'if' statements, or after processing the main block, it performs a generic visit to continue AST traversal, ensuring all branches of conditional logic are examined.
        *   *Parameters:*
            - **self** (`CallGraph`): 
            - **node** (`ast.If`): An AST node representing an 'if' statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls self.generic_visit.
            *   Called By: This method is implicitly called by the AST traversal mechanism when an ast.If node is encountered.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and a file path, then generates a DOT file with sanitized node names. It creates a copy of the input graph and relabels its nodes with simple, unique identifiers (e.g., "n0", "n1"). The original node names are preserved as 'label' attributes on the new nodes. Finally, the modified graph is written to the specified output path as a DOT file, suitable for visualization tools.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph to be processed and written to a DOT file.
    - **out_path** (`str`): The file path where the sanitized DOT graph will be saved.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** This function constructs a filtered call graph for a given Git repository. It first identifies all Python files within the repository and parses their Abstract Syntax Trees (ASTs) to determine a set of 'own functions' defined within these files. Subsequently, it iterates through the parsed file trees again to build a directed graph using the networkx library. The graph includes edges only between functions where both the caller and the callee are part of the identified 'own functions', effectively filtering out external or library calls.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which to extract Python files and analyze their call relationships.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the call relationships exclusively between functions defined within the provided repository's Python files.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content: str)`
*   **Description:** This function takes a string `content` as input and encapsulates it within XML CDATA tags. It constructs a new string that begins with "<![CDATA[\n", followed by the provided content, and then concludes with "\n]]>". This is typically used to prevent XML parsers from interpreting special characters within the content, ensuring the raw content is treated as character data.
*   **Parameters:**
    - **content** (`str`): The string content to be wrapped in CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A string with the provided content wrapped in CDATA tags, including leading and trailing newlines.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs: list, image_list: list)`
*   **Description:** This function processes a list of output objects, typically from a notebook execution, to extract their content into a list of XML snippets or text strings. It handles various output types including 'display_data', 'execute_result', 'stream', and 'error'. For image data within 'display_data' or 'execute_result', it decodes Base64 strings, stores the image data in a separate `image_list`, and inserts an XML placeholder into the main output. If no image is found, it extracts plain text. Stream outputs are appended as raw text, and error outputs are formatted as strings.
*   **Parameters:**
    - **outputs** (`list`): A list of output objects, likely representing execution results from a notebook, each potentially containing different types of data like text, images, or error messages.
    - **image_list** (`list`): A mutable list that will be populated with dictionaries. Each dictionary will contain the 'mime_type' and the Base64 'data' string for any images successfully extracted from the outputs.
*   **Returns:**
    - **extracted_xml_snippets** (`list[str]`): A list of strings. These strings can be extracted plain text content, XML placeholders for images (e.g., '<IMAGE_PLACEHOLDER index="..." mime="..."/>'), or formatted error messages.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type: str)`
*   **Description:** The process_image function is designed to handle image data identified by a given MIME type. It expects to operate within a context where `data` (presumably a dictionary containing base64 encoded image strings) and `image_list` (presumably a list to store processed image metadata) are accessible. The function attempts to retrieve a base64 string using the `mime_type` as a key from `data`, remove newline characters, and then append a dictionary containing the MIME type and the processed base64 data to `image_list`. Upon successful processing, it returns a string formatted as an image placeholder tag. If an error occurs during processing, it returns an error message string. If the `mime_type` is not found in `data`, the function returns `None`.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type string used to identify and retrieve image data from an external `data` source.
*   **Returns:**
    - **image_placeholder_tag** (`str`): A string representing an image placeholder tag, including the dynamically assigned image index and the MIME type, returned upon successful processing.
    - **error_message** (`str`): An error message string indicating that the image data could not be decoded due to an exception during processing.
    - **none** (`NoneType`): Returned when the specified `mime_type` is not found as a key in the external `data` source.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content: str)`
*   **Description:** This function converts the content of a Jupyter notebook, provided as a string, into a structured XML representation. It first attempts to parse the input string as a notebook, returning an error if parsing fails. It then iterates through each cell, converting markdown cells to XML markdown tags and code cells to XML code tags. If code cells contain outputs, it processes them to extract content and potential images, wrapping the output content in XML output tags. The function returns the concatenated XML parts and a list of any extracted images.
*   **Parameters:**
    - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a JSON string.
*   **Returns:**
    - **xml_output** (`str`): The XML representation of the notebook content, or an error message if parsing fails.
    - **extracted_images** (`list`): A list of any images extracted from the notebook's output cells.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files: List[object])`
*   **Description:** This function processes a list of repository file objects to identify and convert Jupyter notebooks. It filters the input list for files ending with '.ipynb' and then iterates through these identified notebooks. For each notebook, it extracts its content and uses an external function, 'convert_notebook_to_xml', to generate XML output and associated images. The results, comprising the XML and images, are stored in a dictionary keyed by the notebook's file path.
*   **Parameters:**
    - **repo_files** (`List[object]`): A list of file objects from a repository. Each object is expected to have a 'path' attribute (string) indicating its file path and a 'content' attribute (string) holding its raw content.
*   **Returns:**
    - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the file paths (string) of the processed notebooks. Each value is another dictionary containing 'xml' (string, the converted XML content) and 'images' (list, the extracted image data) from the notebook conversion.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, providing a structured interface to its properties and content. It employs a lazy-loading strategy for the Git blob object, file content, and size, ensuring that these resources are only fetched when explicitly requested. This design optimizes performance by avoiding unnecessary data loading. The class offers methods to retrieve file attributes, perform basic content analysis, and serialize its data into a dictionary format.
*   **Instantiation:** This class is not explicitly instantiated by any other components listed in the provided context.
*   **Dependencies:** This class depends on the `git` library for `git.Tree` and `git.Blob` objects, and on the `os` module for path manipulation.
*   **Constructor:**
    *   *Description:* This constructor initializes a RepoFile object by setting its file path and the Git tree object from which it originates. It also sets up internal attributes (`_blob`, `_content`, `_size`) to `None`, indicating that these properties will be lazy-loaded upon their first access.
    *   *Parameters:*
        - **self** (`RepoFile`): 
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree-object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading for the Git blob object associated with the file. It checks if the `_blob` attribute is already set; if not, it attempts to retrieve the blob from the `_tree` using the file's path. If the file cannot be found within the commit tree, a `FileNotFoundError` is raised, ensuring robust error handling for missing files.
        *   *Parameters:*
            - **self** (`RepoFile`): 
        *   *Returns:*
            - **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:**
            *   Calls: This method accesses `self._tree` and `self.path` to retrieve the Git tree object and file path.
            *   Called By: This method is called by the `content` and `size` properties.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading for the decoded content of the file. It first verifies if the `_content` attribute has already been loaded. If not, it accesses the `blob` property (which handles its own lazy loading), reads the data stream from the blob, and decodes it into a UTF-8 string, ignoring any decoding errors to prevent crashes.
        *   *Parameters:*
            - **self** (`RepoFile`): 
        *   *Returns:*
            - **content** (`str`): The decoded string content of the file.
        *   **Usage:**
            *   Calls: This method calls the `blob` property to retrieve the Git blob object, and then `data_stream.read()` and `decode()` on the blob's data stream.
            *   Called By: This method is called by `analyze_word_count` and `to_dict`.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading for the size of the file in bytes. It checks if the `_size` attribute is already loaded. If not, it accesses the `blob` property (which handles its own lazy loading) and retrieves the `size` attribute directly from the Git blob object. This ensures the file size is only computed or fetched when needed.
        *   *Parameters:*
            - **self** (`RepoFile`): 
        *   *Returns:*
            - **size** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   Calls: This method calls the `blob` property to retrieve the Git blob object.
            *   Called By: This method is called by `to_dict`.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function, demonstrating how to process the file's content. It calculates the total number of words present in the file's content. This is achieved by accessing the `content` property, which lazy-loads the file's text, and then splitting the resulting string by whitespace to count the individual words.
        *   *Parameters:*
            - **self** (`RepoFile`): 
        *   *Returns:*
            - **word_count** (`int`): The total number of words found in the file content.
        *   **Usage:**
            *   Calls: This method calls the `content` property and the `split()` and `len()` functions.
            *   Called By: This method is not explicitly called by any other methods within the class.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This special method provides a developer-friendly string representation of the RepoFile object. It constructs a concise string that includes the class name and the file's path. This representation is useful for debugging and logging, allowing for easy identification of the object when printed or inspected.
        *   *Parameters:*
            - **self** (`RepoFile`): 
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, including its path.
        *   **Usage:**
            *   Calls: This method calls `self.path`.
            *   Called By: This method is implicitly called by Python's `repr()` function or when the object is printed.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content: bool)`
        *   *Description:* This method converts the RepoFile object into a dictionary representation, providing a structured way to export its data. It includes essential metadata such as the file's path, name (basename), size, and type. An optional `include_content` parameter allows for the inclusion of the file's full content, which is also lazy-loaded, making this method versatile for various data export needs.
        *   *Parameters:*
            - **self** (`RepoFile`): 
            - **include_content** (`bool`): If `True`, the file's content will be included in the dictionary. Defaults to `False`.
        *   *Returns:*
            - **file_data** (`dict`): A dictionary containing metadata about the file, optionally including its content.
        *   **Usage:**
            *   Calls: This method calls `self.path`, `os.path.basename`, `self.size`, and `self.content`.
            *   Called By: This method is not explicitly called by any other methods within the class.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with Git repositories. It handles the cloning of a remote repository into a temporary local directory, manages the lifecycle of this temporary directory, and offers functionalities to list all files and represent the repository's structure as a hierarchical file tree. It also implements the context manager protocol, ensuring proper cleanup of temporary resources.
*   **Instantiation:** This class is not explicitly instantiated by other components listed in the provided context.
*   **Dependencies:** The class relies on external libraries such as tempfile for temporary directory management, git.Repo and git.GitCommandError from the GitPython library for Git operations, and logging for informational messages.
*   **Constructor:**
    *   *Description:* This constructor initializes a GitRepository instance by cloning a specified Git repository into a temporary directory. It sets up instance attributes such as the repository URL, the path to the temporary directory, the GitPython Repo object, and the latest commit and its tree. It includes error handling for cloning failures.
    *   *Parameters:*
        - **self** (`GitRepository`): 
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It uses the `git ls-files` command to get file paths, then creates `RepoFile` objects for each path, storing them in `self.files` and returning the list.
        *   *Parameters:*
            - **self** (`GitRepository`): 
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods, classes, or functions listed in the provided context.
            *   Called By: This method is not explicitly called by other functions or methods listed in the provided context.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is responsible for cleaning up resources by deleting the temporary directory where the Git repository was cloned. It sets `self.temp_dir` to `None` after printing a message about the deletion.
        *   *Parameters:*
            - **self** (`GitRepository`): 
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods, classes, or functions listed in the provided context.
            *   Called By: This method is not explicitly called by other functions or methods listed in the provided context.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This special method allows the `GitRepository` object to be used as a context manager. When entering a `with` statement, it simply returns the instance itself, making it available within the context block.
        *   *Parameters:*
            - **self** (`GitRepository`): 
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository itself.
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods, classes, or functions listed in the provided context.
            *   Called By: This method is not explicitly called by other functions or methods listed in the provided context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type: type | None, exc_val: Exception | None, exc_tb: traceback | None)`
        *   *Description:* This special method is part of the context manager protocol. When exiting a `with` statement, it ensures that the `close` method is called to clean up the temporary directory, regardless of whether an exception occurred within the context block.
        *   *Parameters:*
            - **self** (`GitRepository`): 
            - **exc_type** (`type | None`): The type of the exception raised, or None if no exception occurred.
            - **exc_val** (`Exception | None`): The exception instance raised, or None.
            - **exc_tb** (`traceback | None`): The traceback object, or None.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods, classes, or functions listed in the provided context.
            *   Called By: This method is not explicitly called by other functions or methods listed in the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content: bool)`
        *   *Description:* This method constructs a hierarchical dictionary representation of the repository's file structure, similar to a file system tree. It first ensures all files are loaded via `get_all_files` if not already present. It then iterates through the `RepoFile` objects, parsing their paths to build a nested dictionary structure with directories and files.
        *   *Parameters:*
            - **self** (`GitRepository`): 
            - **include_content** (`bool`): A flag indicating whether the content of each file should be included in its dictionary representation. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree, with "name", "type", and "children" keys.
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods, classes, or functions listed in the provided context.
            *   Called By: This method is not explicitly called by other functions or methods listed in the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** This function `create_savings_chart` generates a bar chart to visually compare the number of tokens between JSON and TOON formats. It takes the token counts for both formats and a calculated savings percentage as input. The chart displays two bars, one for JSON and one for TOON, with their respective token counts labeled above. The generated chart is then saved to a specified output file path.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens representing the JSON format.
    - **toon_tokens** (`int`): The number of tokens representing the TOON format.
    - **savings_percent** (`float`): The calculated percentage of token savings to be displayed in the chart title.
    - **output_path** (`str`): The file path, including the filename and extension, where the generated chart will be saved.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str)`
*   **Description:** The calculate_net_time function determines the effective processing duration by adjusting for estimated rate-limiting sleep times. It takes start and end timestamps, total item count, batch size, and the model name as input. For models not starting with 'gemini-', it returns the direct difference between end and start times. Otherwise, it calculates the number of batches and subtracts a fixed sleep duration (61 seconds per batch, excluding the first) from the total duration. The function ensures the returned net time is non-negative.
*   **Parameters:**
    - **start_time** (`float`): The starting timestamp of the process, typically in seconds.
    - **end_time** (`float`): The ending timestamp of the process, typically in seconds.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items to process in each batch.
    - **model_name** (`str`): The name of the model being used, which influences sleep time calculations.
*   **Returns:**
    - **net_time** (`float`): The calculated net duration in seconds, after subtracting estimated sleep times for rate limits, or the total duration if not a 'gemini-' model, or 0 if no items were processed.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable | None)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive analysis pipeline for a given GitHub repository URL. It begins by parsing input to extract API keys and model configurations, then validates the repository URL. The core process involves cloning the repository, extracting basic project information, constructing a file tree, and performing a detailed relationship analysis. Subsequently, it generates and enriches an Abstract Syntax Tree (AST) schema. The function then prepares and dispatches analysis tasks to a Helper LLM for individual functions and classes, aggregating their results. Finally, it compiles all gathered data for a Main LLM to generate a comprehensive final report, including token usage estimations, and saves the report along with performance metrics.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary mapping API service names (e.g., "gemini", "gpt", "scadsllm") to their respective API keys or base URLs.
    - **model_names** (`dict`): A dictionary specifying the names of the "helper" and "main" language models to be used in the workflow.
    - **status_callback** (`callable | None`): An optional callable function used to provide status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): A string containing the final generated report from the Main LLM, detailing the repository analysis.
    - **metrics** (`dict`): A dictionary containing various performance statistics and token usage data, such as helper_time, main_time, total_time, helper_model, main_model, json_tokens, toon_tokens, and savings_percent.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_status`
*   **Signature:** `def update_status(msg: str)`
*   **Description:** This function serves to update a status message. It accepts a message string as input. If a `status_callback` is defined and accessible in the current scope, the function invokes this callback with the provided message. Regardless of the callback's presence, the message is always logged at the INFO level using the `logging` module. This ensures that status updates are both potentially communicated externally and consistently recorded internally.
*   **Parameters:**
    - **msg** (`str`): The status message string to be processed. This message will be passed to a `status_callback` if available and subsequently logged.
*   **Returns:**
    - **None** (`None`): This function does not explicitly return any value; it performs side effects by potentially calling a `status_callback` and always logging the provided message.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback: callable | None)`
*   **Description:** This function orchestrates a workflow to analyze notebooks from a GitHub repository. It begins by extracting a repository URL from the input, cloning the repository, and then processing its notebook files. It extracts basic project information and then iteratively generates reports for each notebook using a specified Large Language Model (LLM). The function handles different LLM providers based on the 'model' parameter, manages API keys, and includes an optional status callback for progress updates. Finally, it concatenates all individual notebook reports into a single final report, saves it to a file, and returns the report along with performance metrics.
*   **Parameters:**
    - **input** (`str`): The input string, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing API keys for various LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
    - **model** (`str`): The name of the LLM model to be used for generating reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`callable | None`): An optional callback function to provide status updates during the workflow execution.
*   **Returns:**
    - **result** (`dict`): A dictionary containing the 'report' (concatenated LLM outputs) and 'metrics' (performance statistics).
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info: dict, nb_path: str, xml_content: str, images: list[dict])`
*   **Description:** This function constructs a multimodal payload for the Gemini API, integrating textual context, notebook XML structure, and embedded images. It begins by serializing basic project information and the notebook path into a JSON string. The function then processes the provided XML content, using a regular expression to identify and extract image placeholders. For each placeholder, it retrieves the corresponding base64 encoded image data and formats it as an 'image_url' part. Any text segments from the XML content, including those before, between, and after image placeholders, are added as 'text' parts to the payload. The final output is a list of dictionaries, each representing a component of the Gemini API request.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing basic project information to be included in the payload's contextual text.
    - **nb_path** (`str`): The file path of the current notebook, also included in the payload's contextual text.
    - **xml_content** (`str`): The XML structure of the notebook, which may contain image placeholders to be replaced with actual image data.
    - **images** (`list[dict]`): A list of dictionaries, where each dictionary contains base64 encoded image data ('data' key) and potentially other image metadata, indexed to match image placeholders in 'xml_content'.
*   **Returns:**
    - **payload_content** (`list[dict]`): A list of dictionaries, each representing a part of a multimodal payload suitable for the Gemini API, containing 'text' and 'image_url' components.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file system path into its corresponding Python module path string. It first attempts to determine the relative path from a specified project root. If that fails, it uses the base name of the file. It then strips the '.py' extension if present, replaces path separators with dots, and finally removes the '.__init__' suffix if the module represents a package's initialization file.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to perform static analysis on a Python project to build a comprehensive call graph. It identifies all Python files, collects definitions of functions, methods, and classes, and then resolves calls between these entities. The class provides methods to initiate the analysis, retrieve the raw call graph, and present relationships in an outgoing/incoming format, leveraging Python's `ast` module for parsing and `os` for file system navigation.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** This class depends on `os` for file system operations, `ast` for parsing Python source code, `logging` for error reporting, `collections.defaultdict` for its internal graph structure, and an external `CallResolverVisitor` for call resolution.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjectAnalyzer instance. It sets the project's root directory, initializes internal data structures like `definitions` (for storing code entity definitions), `call_graph` (to store relationships), and `file_asts` (for parsed ASTs). It also defines a set of directories to ignore during file system traversal.
    *   *Parameters:*
        - **self** (`ProjectAnalyzer`): 
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect definitions of functions, classes, and methods. Finally, it resolves calls between these definitions to build a comprehensive call graph, clearing temporary ASTs afterwards.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): 
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph where keys are callee identifiers and values are lists of caller information.
        *   **Usage:**
            *   Calls: This method calls `_find_py_files` to locate Python files, `_collect_definitions` to gather code entity definitions, and `_resolve_calls` to establish relationships between entities.
            *   Called By: This method is not explicitly called by other methods within the provided context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* This method processes the internal `call_graph` to generate a more structured representation of relationships, separating them into outgoing and incoming calls. It iterates through the call graph, extracting caller and callee identifiers, and populates two dictionaries: `outgoing` (what each entity calls) and `incoming` (what calls each entity). The results are then sorted and returned.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): 
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, 'outgoing' and 'incoming', each mapping entity identifiers to sorted lists of related entity identifiers.
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods or functions.
            *   Called By: This method is not explicitly called by other methods within the provided context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private helper method is responsible for recursively traversing the `project_root` directory to locate all Python files. It uses `os.walk` to navigate the directory structure and filters out specified `ignore_dirs` to avoid analyzing irrelevant or temporary directories. It returns a list of absolute paths to all identified Python files.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): 
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to Python files found in the project.
        *   **Usage:**
            *   Calls: This method utilizes `os.walk` for directory traversal and `os.path.join` to construct file paths.
            *   Called By: This method is called by `analyze` to get a list of Python files for processing.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath: str)`
        *   *Description:* This private method parses a given Python file to identify and record all function, method, and class definitions. It reads the file, parses its Abstract Syntax Tree (AST), and then walks the AST to find `FunctionDef` and `ClassDef` nodes. For each definition, it determines its full module path, type (function, method, or class), and line number, storing this information in the `self.definitions` dictionary. It also stores the AST for later use.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): 
            - **filepath** (`str`): The absolute path to the Python file being analyzed.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method uses `ast.parse` to create an AST, `ast.walk` to traverse it, `path_to_module` to determine module paths, `_get_parent` to find parent nodes, and `logging.error` for error handling.
            *   Called By: This method is called by `analyze` for each Python file to gather definitions.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree: ast.AST, node: ast.AST)`
        *   *Description:* This private helper method traverses an Abstract Syntax Tree (AST) to find the immediate parent node of a given child node. It iterates through all nodes in the tree and checks their children to identify if any child matches the provided node. If a match is found, the parent node is returned.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): 
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent_node** (`ast.AST or None`): The parent AST node if found, otherwise None.
        *   **Usage:**
            *   Calls: This method utilizes `ast.walk` to iterate through nodes and `ast.iter_child_nodes` to check children of each node.
            *   Called By: This method is called by `_collect_definitions` to determine the parent of a function or class definition.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath: str)`
        *   *Description:* This private method is responsible for identifying and resolving function, method, and class calls within a given Python file. It retrieves the previously stored AST for the file and then uses a `CallResolverVisitor` (an external dependency) to traverse the AST and detect calls. The resolved calls, along with their caller information, are then aggregated into the `self.call_graph`.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): 
            - **filepath** (`str`): The absolute path to the Python file whose calls are to be resolved.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method instantiates and uses `CallResolverVisitor` to visit the AST, accesses `resolver.calls` for identified calls, and uses `logging.error` for error handling.
            *   Called By: This method is called by `analyze` for each Python file to resolve calls within it.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class extends `ast.NodeVisitor` to systematically traverse a Python Abstract Syntax Tree (AST) and identify all function and method calls. Its core responsibility is to resolve the fully qualified names of both the calling and called entities, building a detailed map of inter-function and inter-method relationships. It manages scope for imported modules and objects, tracks current class and function contexts, and records call information for later analysis.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** This class depends on the `ast` module for Abstract Syntax Tree traversal, the `os` module for path manipulation, and `collections.defaultdict` for its internal data structures.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with the source file path, the project's root directory, and a dictionary of known definitions. It sets up internal state variables such as the module path, a scope for tracking imports, a dictionary for instance types, and variables to keep track of the current caller and class context. A `defaultdict` named `calls` is also initialized to store the detected call relationships.
    *   *Parameters:*
        - **self** (`CallResolverVisitor`): 
        - **filepath** (`str`): The absolute path to the Python source file being analyzed.
        - **project_root** (`str`): The root directory of the project, used to derive module paths from file paths.
        - **definitions** (`dict`): A dictionary containing all known definitions (functions, classes, etc.) within the project, used for validating resolved call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* This method is invoked by the AST visitor framework when a `ClassDef` node is encountered, signifying the definition of a class. It temporarily updates `self.current_class_name` to the name of the class being visited, which is crucial for correctly identifying methods belonging to this class. After processing the class's children, it restores the previous `current_class_name` to ensure proper context for subsequent AST nodes.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): 
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self.generic_visit(node)` to continue the AST traversal for child nodes within the class definition.
            *   Called By: This method is called by the `ast.NodeVisitor` framework when it encounters an `ast.ClassDef` node during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node: ast.FunctionDef)`
        *   *Description:* This method processes `FunctionDef` nodes, which represent function or method definitions within the AST. It constructs a fully qualified identifier for the current function, incorporating the module path and class name if the function is a method. This identifier is then set as `self.current_caller_name` to establish the context for any calls made within this function. The method ensures that the `current_caller_name` is reverted to its previous state after the function's body has been visited.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): 
            - **node** (`ast.FunctionDef`): The AST node representing the function or method definition.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self.generic_visit(node)` to continue the AST traversal for child nodes within the function definition.
            *   Called By: This method is called by the `ast.NodeVisitor` framework when it encounters an `ast.FunctionDef` node during AST traversal.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node: ast.Call)`
        *   *Description:* This method is triggered for every `ast.Call` node, indicating a function or method invocation. It first attempts to resolve the fully qualified name of the called entity using the `_resolve_call_qname` helper. If the callee is successfully resolved and present in the project's definitions, the method records detailed information about the call, including the caller's file, line number, full identifier, and type. This call information is then appended to a list associated with the callee's qualified name in the `self.calls` dictionary.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): 
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self._resolve_call_qname(node.func)` to determine the qualified name of the called function and `self.generic_visit(node)` to continue AST traversal.
            *   Called By: This method is called by the `ast.NodeVisitor` framework when it encounters an `ast.Call` node during AST traversal.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: ast.Import)`
        *   *Description:* This method handles `ast.Import` nodes, which correspond to `import module [as alias]` statements. It iterates through all names specified in the import statement, whether they are original module names or aliases. For each name, it stores a mapping in `self.scope` from the local name (the alias or original name used in the current file) to its fully qualified module name. This mapping is essential for resolving calls to imported modules later in the analysis.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): 
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self.generic_visit(node)` to continue the AST traversal for child nodes.
            *   Called By: This method is called by the `ast.NodeVisitor` framework when it encounters an `ast.Import` node during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
        *   *Description:* This method processes `ast.ImportFrom` nodes, which represent `from module import name [as alias]` statements. It first determines the full module path, correctly handling relative imports based on `node.level`. For each imported name, it constructs its fully qualified path and stores this mapping in `self.scope`, associating the local name (alias or original name) with its global identifier. This allows the visitor to accurately resolve references to functions or classes imported from other modules.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): 
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self.generic_visit(node)` to continue the AST traversal for child nodes.
            *   Called By: This method is called by the `ast.NodeVisitor` framework when it encounters an `ast.ImportFrom` node during AST traversal.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node: ast.Assign)`
        *   *Description:* This method processes `ast.Assign` nodes to identify instances of classes being created. It specifically looks for assignments where the right-hand side is a call expression, and the function being called is a simple name (e.g., `x = MyClass()`). If the called name corresponds to a known class definition, it records the qualified class name against the target variable's ID in `self.instance_types`. This mapping is crucial for resolving method calls on these instantiated objects later.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): 
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
        *   **Usage:**
            *   Calls: This method calls `self.generic_visit(node)` to continue the AST traversal for child nodes.
            *   Called By: This method is called by the `ast.NodeVisitor` framework when it encounters an `ast.Assign` node during AST traversal.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node: ast.expr)`
        *   *Description:* This private helper method is responsible for determining the fully qualified name (QName) of a function or method being called. It handles two primary scenarios: direct calls to names (`ast.Name`) and attribute access calls (`ast.Attribute`, e.g., `object.method`). For simple names, it checks the `self.scope` for imports and then local definitions. For attribute access, it uses `self.instance_types` to resolve methods on instantiated objects or `self.scope` for module-level functions. It returns the resolved QName as a string or `None` if resolution fails.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): 
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., `ast.Name` or `ast.Attribute`).
        *   *Returns:*
            - **qname** (`str | None`): The fully qualified name of the called function or method, or `None` if it cannot be resolved.
        *   **Usage:**
            *   Calls: This method does not explicitly call other methods within the provided source code.
            *   Called By: This method is called by `self.visit_Call` to resolve the qualified name of a function or method being invoked.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** This function encrypts a provided string using a `cipher_suite` object. It first validates if the input text or the `cipher_suite` itself is available, returning the original text if not. If valid, the text is stripped of leading/trailing whitespace, encoded to UTF-8 bytes, encrypted using the `cipher_suite`, and finally decoded back into a string before being returned. This ensures sensitive text data is protected.
*   **Parameters:**
    - **text** (`str`): The string to be encrypted. If this is empty or `cipher_suite` is not initialized, the original text is returned.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string, or the original text if encryption was skipped due to empty input or uninitialized `cipher_suite`.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** This function attempts to decrypt a given string using a `cipher_suite` object, which is expected to be available in the scope. It first performs a guard clause, returning the original text if the input text is empty or if the `cipher_suite` is not initialized. If decryption proceeds, the function strips whitespace from the input string, encodes it to bytes, decrypts it using the `cipher_suite`, and then decodes the result back into a string. An exception handler is included to catch any errors during decryption, in which case the original, un-decrypted text is returned.
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted string if the operation is successful, or the original string if decryption is skipped or an error occurs.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function is responsible for creating a new user entry in the database. It takes a username, full name, and a plain-text password as input. The password is then hashed using `stauth.Hasher.hash` before being stored. The function constructs a user dictionary, initializes API keys to empty strings, and inserts this user record into the `dbusers` collection. It returns the unique identifier of the newly inserted user.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user, which also serves as the document's `_id`.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password provided by the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The `_id` of the newly inserted user document, which corresponds to the provided username.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function is responsible for retrieving all user records from a database collection named `dbusers`. It executes a find operation without any filters, effectively fetching all documents from the collection. The result of the find operation, which is typically a cursor, is then converted into a standard Python list. This list, containing all the retrieved user documents, is subsequently returned by the function. It provides a straightforward way to access the entire user dataset stored in `dbusers`.
*   **Parameters:**
*   **Returns:**
    - **users** (`list[dict]`): A list containing all user documents/dictionaries retrieved from the `dbusers` collection.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The `fetch_user` function is designed to retrieve a single user document from a database collection named `dbusers`. It takes a `username` as input and uses it to query the collection for a document where the `_id` field matches the provided username. The function returns the first document found that matches the query criteria.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched from the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if found, or None if no matching user is found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the 'name' field for a specific user within the `dbusers` collection. It identifies the target user document by matching the provided `username` with the document's `_id` field. The function then sets the 'name' attribute of that user's document to the `new_name` value. It returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier (expected to be the _id) of the user whose name is to be updated.
    - **new_name** (`str`): The new name to be assigned to the specified user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** The `update_gemini_key` function is designed to securely store a user's Gemini API key in a database. It takes a username and the API key as input. The function first strips any whitespace from the provided API key and then encrypts it using an external `encrypt_text` function. Finally, it updates the `gemini_api_key` field for the specified user in the `dbusers` collection with the newly encrypted key. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored, which will be encrypted before being saved.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** This function updates a user's GPT API key in the database. It first encrypts the provided `gpt_api_key` after removing leading/trailing whitespace. Then, it uses the `dbusers` collection to find the document corresponding to the given `username` and updates its `gpt_api_key` field with the newly encrypted value. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be stored for the user. This key will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 1 if the user exists and the key was updated, or 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specific user in a database. It takes a username and a new Ollama base URL as input. The function locates the user document using the provided username as the unique identifier. It then sets the 'ollama_base_url' field for that user, ensuring any leading or trailing whitespace is removed from the URL. Finally, it returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL needs to be updated.
    - **ollama_base_url** (`str`): The new Ollama base URL to be associated with the user, which will be stripped of whitespace.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function updates a user's Open Source API key in the database. It first encrypts the provided API key after removing leading/trailing whitespace. Then, it uses the `dbusers` collection to find the user by their username and sets the `opensrc_api_key` field to the newly encrypted value. The function returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API key is to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key to be stored for the user. This key will be encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation, typically 1 if the user is found and updated, or 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** This function updates the 'opensrc_base_url' field for a specific user in a database collection. It takes a username and a new opensource base URL as input. The function locates the user record using the provided username as the document's '_id' and sets the 'opensrc_base_url' field to the new URL after stripping any leading or trailing whitespace. It then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose 'opensrc_base_url' is to be updated.
    - **opensrc_base_url** (`str`): The new base URL for opensource projects, which will be stripped of leading/trailing whitespace before being stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** This function retrieves the Gemini API key associated with a given username from a database. It queries the 'dbusers' collection for a user document matching the provided username. The function specifically projects the 'gemini_api_key' field from the found document. If a user is found and the key exists, it returns the key; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the Gemini API key.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key associated with the username, or None if the user is not found or the key is not present.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** This function retrieves the Ollama base URL associated with a specific user from a database. It queries the `dbusers` collection using the provided `username` as the document's `_id`. The function projects only the `ollama_base_url` field. If a user document is found, it extracts and returns the `ollama_base_url`; otherwise, it returns `None`.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama base URL associated with the user, or `None` if the user is not found or the URL is not set.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** This function retrieves the GPT API key associated with a specific username from a database. It queries the `dbusers` collection to find a user document matching the provided username. If a user is found, it attempts to extract the 'gpt_api_key' field. The function returns the API key if present, otherwise it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key as a string if found, otherwise None.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** This function is designed to retrieve a user's Open Source API key from a database. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided username. If a matching user document is found, the function extracts the 'opensrc_api_key' from it. If no user is found, or if the 'opensrc_api_key' field is not present, the function returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user whose Open Source API key is to be fetched.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key associated with the specified username, or None if the user is not found or the key does not exist.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** This function retrieves the 'opensrc_base_url' associated with a specific user from a database. It queries the 'dbusers' collection using the provided username as the document's '_id'. The function projects only the 'opensrc_base_url' field. If a user document is found, it returns the value of 'opensrc_base_url'; otherwise, it returns None.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose opensource base URL is to be fetched.
*   **Returns:**
    - **opensrc_base_url** (`str or None`): The opensource base URL for the specified user, or None if the user is not found in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is designed to remove a user record from a database collection. It takes a username as input and attempts to delete the corresponding document identified by that username. The function leverages a database client's `delete_one` method to perform the operation. It then returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted by the operation, typically 0 or 1.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys and base URLs for a specified user from a database. It queries the `dbusers` collection using the provided username. If the user is not found, it returns a tuple of `None` values. Otherwise, it decrypts specific API keys such as Gemini, GPT, and open-source keys, and retrieves Ollama and open-source base URLs, returning all five values.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user is not found or the key is not set.
    - **ollama_plain** (`str | None`): The Ollama base URL, or None if the user is not found or the URL is not set.
    - **gpt_plain** (`str | None`): The decrypted GPT API key, or None if the user is not found or the key is not set.
    - **opensrc_plain** (`str | None`): The decrypted open-source API key, or None if the user is not found or the key is not set.
    - **opensrc_url** (`str | None`): The open-source base URL, or None if the user is not found or the URL is not set.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** This function is responsible for creating a new chat entry in a database. It constructs a dictionary containing a unique identifier generated using UUID, the provided username, the chat name, and the current timestamp. This chat dictionary is then inserted into the 'dbchats' collection. The function returns the unique ID assigned to the newly created chat entry.
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier of the newly created chat entry in the database.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** This function, `fetch_chats_by_user`, is responsible for retrieving all chat records associated with a given user from a database. It accepts a username as input and queries a database collection, presumably `dbchats`, to locate relevant chat entries. The retrieved chat documents are then sorted chronologically by their `created_at` timestamp in ascending order. The function concludes by returning the collection of sorted chat records as a list.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat records.
*   **Returns:**
    - **chats** (`list`): A list of chat records associated with the specified username, sorted by creation time.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks for the existence of a specific chat within the 'dbchats' collection. It queries the database using a provided username and chat name. The function returns a boolean indicating whether a matching chat record was found.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked for existence.
*   **Returns:**
    - **chat_exists** (`bool`): True if a chat matching the given username and chat name exists in the database, False otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat entry and all its associated exchanges (messages) within a database. It first updates the 'chat_name' for the specified 'username' and 'old_name' in the 'dbchats' collection. Subsequently, it updates the 'chat_name' for all related entries in the 'dbexchanges' collection. The function returns the number of chat documents that were modified in the 'dbchats' collection.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat.
    - **new_name** (`str`): The new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat documents that were modified in the 'dbchats' collection.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str, json_tokens: int, toon_tokens: int, savings_percent: float)`
*   **Description:** This function inserts a new exchange record into a database collection named `dbexchanges`. It generates a unique identifier for the new record using `uuid.uuid4()`. A dictionary is constructed containing various details such as the question, answer, feedback, user information, chat name, usage metrics, token counts, savings percentage, and a timestamp for creation. The function attempts to insert this dictionary as a new document into the database. If the insertion is successful, it returns the generated unique ID; otherwise, it catches any exceptions, prints an error message, and returns `None`.
*   **Parameters:**
    - **question** (`str`): The question string of the exchange.
    - **answer** (`str`): The answer string provided for the exchange.
    - **feedback** (`str`): The feedback string associated with the exchange.
    - **username** (`str`): The username of the participant in the exchange.
    - **chat_name** (`str`): The name of the chat session where the exchange occurred.
    - **helper_used** (`str`): Optional. Specifies which helper component was utilized. Defaults to an empty string.
    - **main_used** (`str`): Optional. Specifies which main component was utilized. Defaults to an empty string.
    - **total_time** (`str`): Optional. The total time recorded for the exchange. Defaults to an empty string.
    - **helper_time** (`str`): Optional. The time attributed to the helper component. Defaults to an empty string.
    - **main_time** (`str`): Optional. The time attributed to the main component. Defaults to an empty string.
    - **json_tokens** (`int`): Optional. The number of JSON tokens processed. Defaults to 0.
    - **toon_tokens** (`int`): Optional. The number of 'toon' tokens processed. Defaults to 0.
    - **savings_percent** (`float`): Optional. The calculated savings percentage. Defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly inserted exchange record if the operation is successful.
    - **None** (`NoneType`): Returns None if an exception occurs during the database insertion.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is called by no other functions.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves exchange records from a database based on a provided username. It queries the 'dbexchanges' collection, filtering documents where the 'username' field matches the input. The results are then sorted by the 'created_at' timestamp in ascending order, which is noted as important for display purposes. Finally, the function returns the sorted list of exchange records.
*   **Parameters:**
    - **username** (`str`): The username used to filter and retrieve specific exchange records from the database.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (documents) associated with the given username, sorted by their creation timestamp.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by other functions in the provided context.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a list of chat exchanges from a database collection named `dbexchanges`. It filters these exchanges based on a provided username and a specific chat name. The results are then sorted in ascending order by their `created_at` timestamp before being returned as a list.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat exchanges to fetch.
    - **chat_name** (`str`): The name of the chat for which to fetch exchanges.
*   **Returns:**
    - **exchanges** (`list`): A list of chat exchange documents matching the specified username and chat name, sorted by creation time.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id: Any, feedback: int)`
*   **Description:** This function updates the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function uses the `dbexchanges.update_one` method to locate the document by its `_id` and sets the 'feedback' field to the provided integer. It then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated.
    - **feedback** (`int`): The integer value representing the feedback to be set for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id: Any, feedback_message: str)`
*   **Description:** This function updates a specific exchange record in a database collection. It identifies the record using an `exchange_id` and sets its `feedback_message` field to the provided string. The function then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated in the database.
    - **feedback_message** (`str`): The new feedback message string to be stored for the specified exchange record.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is designed to remove a single exchange record from the 'dbexchanges' collection within a database. It takes an exchange identifier as input and uses it to locate and delete the corresponding document. The function then reports the number of documents that were successfully deleted, which is typically 0 or 1.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange document to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The count of documents that were successfully deleted. This will be 1 if a document matching the exchange_id was found and deleted, and 0 otherwise.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** This function is designed to completely remove a specific chat and all its associated messages (exchanges) from the database. It first executes a bulk deletion of all exchange records linked to the provided username and chat name. Subsequently, it deletes the chat record itself using the same criteria. This two-step process ensures data consistency by removing all related data points for a given chat.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted. This is typically 1 if the chat was found and deleted, or 0 if no matching chat was found.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list: list[str])`
*   **Description:** This function processes a list of strings, where each string is expected to represent a path or a structured identifier. It iterates through the provided list, and for each string, it splits the string by the '/' character. The function then extracts the last segment from the split string and compiles these segments into a new list. This new list of cleaned names is then returned.
*   **Parameters:**
    - **model_list** (`list[str]`): A list of strings, where each string is expected to contain one or more '/' characters, representing a path or a similar structured identifier.
*   **Returns:**
    - **cleaned_names** (`list[str]`): A new list containing the last segment of each input string after splitting by '/'.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list: list, category_name: str)`
*   **Description:** This function, get_filtered_models, filters a provided list of models (source_list) based on a specified category name. It retrieves filtering keywords from a global CATEGORY_KEYWORDS dictionary. If the category includes the keyword "STANDARD", it returns only models that are also present in a STANDARD_MODELS list. Otherwise, it filters the source_list to include models whose names contain any of the category's keywords (case-insensitively). If no models match the keyword-based filter, the original source_list is returned.
*   **Parameters:**
    - **source_list** (`list`): The list of models to be filtered.
    - **category_name** (`str`): The name of the category used to determine filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models filtered according to the specified category, or the original source_list if no models match the filter.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function, `save_gemini_cb`, is designed to handle the saving of a Gemini API key. It retrieves a potential new Gemini key from the Streamlit session state. If a new key is present, it updates the user's Gemini key in the database via `db.update_gemini_key`, clears the temporary key from the session state, and displays a success toast message to the user. This function acts as a callback, likely triggered by a user action in a Streamlit application.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function, `save_ollama_cb`, is designed to handle the saving of a new Ollama URL. It retrieves the potential new URL from the Streamlit session state. If a valid URL is found, it proceeds to update this URL in the database associated with the current user's session. Upon successful update, it displays a confirmation toast message to the user.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** This function loads chat and exchange data from the database for a specified user. It first checks if the data for the given username is already present in the Streamlit session state. If not, it initializes the session state, fetches chats, then fetches and sorts exchanges into their respective chats. It handles cases where exchanges might exist for undefined chats and ensures feedback values are properly set. Finally, it creates a default chat if none exist and sets the active chat for the session.
*   **Parameters:**
    - **username** (`str`): The username for which to load chat and exchange data from the database.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex: dict, val: Any)`
*   **Description:** The `handle_feedback_change` function is responsible for updating the feedback associated with a specific exchange. It takes an exchange object and a new feedback value as input. The function first updates the 'feedback' key within the provided exchange object locally. Subsequently, it calls a database utility to persist this feedback change, using the exchange's unique identifier. Finally, it triggers a re-execution of the Streamlit application to reflect the changes in the UI.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing an exchange or a data record, expected to contain at least an '_id' key for identification and a 'feedback' key to be updated.
    - **val** (`Any`): The new feedback value to be assigned to the 'feedback' key of the 'ex' object and stored in the database.
*   **Returns:**
    - **None** (`None`): The function does not explicitly return any value; it performs side effects by modifying the 'ex' object, updating a database record, and triggering a Streamlit rerun.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name: str, ex: dict)`
*   **Description:** This function is responsible for deleting a specific exchange. It first removes the exchange from the database using its unique identifier. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if the exchange is found within that chat's exchanges list, it removes it from the session state as well. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat associated with the exchange to be deleted.
    - **ex** (`dict`): A dictionary representing the exchange to be deleted, expected to contain an '_id' key.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username: str, chat_name: str)`
*   **Description:** This function handles the deletion of a specific chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it updates the Streamlit session state by removing the chat from `st.session_state.chats`. If there are remaining chats, it sets the `active_chat` to the first available chat. If no chats remain, it creates a new default chat named "Chat 1" in both the database and session state, then sets it as the active chat. Finally, it triggers a Streamlit rerun to update the UI.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text: str)`
*   **Description:** This function aims to extract a repository name from a given text string. It first attempts to locate a URL within the input text using a regular expression. If a URL is found, it proceeds to parse it to isolate the path component. The last segment of this path is then considered the potential repository name, with any trailing ".git" suffix removed for cleanliness. The function returns the extracted repository name as a string or None if no URL is found or a repository name cannot be successfully derived.
*   **Parameters:**
    - **text** (`str`): The input string, potentially containing a URL from which a repository name should be extracted.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string, or None if no URL is found or a repository name cannot be determined from the URL path.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text: str)`
*   **Description:** This function acts as a generator that takes a string of text and yields its words one by one. It splits the input text by spaces and then iterates through each word. After yielding a word followed by a space, it introduces a small delay of 0.01 seconds. This behavior is typically used to simulate a streaming effect, where text appears gradually.
*   **Parameters:**
    - **text** (`str`): The input string of text that needs to be streamed word by word.
*   **Returns:**
    - **word_with_space** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text: str, should_stream: bool)`
*   **Description:** This function processes a given markdown text, identifying and rendering both standard markdown content and embedded Mermaid diagrams. It splits the input text based on ````mermaid` delimiters. Non-Mermaid sections are rendered using Streamlit's markdown capabilities, optionally streaming the text. Mermaid diagram code blocks are passed to a specialized Streamlit Mermaid component for rendering, with a fallback to displaying the raw code if rendering fails.
*   **Parameters:**
    - **markdown_text** (`str`): The input text, which may contain standard markdown and embedded Mermaid diagram syntax.
    - **should_stream** (`bool`): A boolean flag indicating whether non-Mermaid text content should be streamed to the output. Defaults to False.
*   **Returns:**
    - **None** (`None`): This function does not explicitly return a value. It performs side effects by rendering content to a Streamlit application.
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex: dict, current_chat_name: str)`
*   **Description:** This function `render_exchange` is responsible for displaying a single chat exchange in a Streamlit application. It first renders the user's question. Subsequently, it displays the assistant's answer, which includes a dynamic toolbar. This toolbar provides options for giving feedback (like/dislike), adding comments, downloading the response, and deleting the exchange. In case the assistant's response indicates an error, a simplified error message and a delete option are presented. Finally, the function renders the answer content using a specialized text rendering utility.
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing a single chat exchange, containing the question, answer, feedback status, and a unique identifier.
    - **current_chat_name** (`str`): A string representing the name of the current chat session, used for contextual operations like deleting exchanges.
*   **Returns:**
*   **Usage:**
    - **Calls:** This function calls no other functions.
    - **Called By:** This function is not called by any other functions.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to provide a structured representation for a single parameter of a function. It defines a schema requiring a 'name', 'type', and 'description' for each parameter. This class facilitates consistent data handling and validation for function parameter metadata within a larger system.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly declare external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly defines its constructor to initialize an instance with 'name', 'type', and 'description' attributes. It performs validation on these inputs upon instantiation, ensuring they conform to the specified string types.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The data type of the parameter.
        - **description** (`str`): A textual description of the parameter's purpose.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to structure information about a function's return value. It serves as a data model to consistently represent the name, type, and a descriptive explanation of what a function returns. This class facilitates clear and standardized documentation or programmatic handling of return value metadata.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is automatically generated to initialize instances of ReturnDescription. It accepts and validates `name`, `type`, and `description` as string arguments, setting them as instance attributes.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The Python type hint or a descriptive string indicating the type of the return value.
        - **description** (`str`): A detailed explanation of what the return value represents or its purpose.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts with other parts of a system. It provides a structured way to describe what a function calls and what calls it, using two string attributes. This class serves as a data structure for documenting the operational context of a code entity.
*   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an __init__ method that initializes its fields `calls` and `called_by`. It sets up the instance with the provided string values for these attributes, ensuring type validation.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or external entities that this context (e.g., a function) calls.
        - **called_by** (`str`): A string summarizing the functions, methods, or external entities that call this context (e.g., a function).
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** This class serves as a Pydantic model designed to hold a comprehensive analysis of a function. It structures information about a function's high-level purpose, its input parameters, its expected return values, and how it integrates into a broader system. This model facilitates the standardized representation and exchange of function metadata.
*   **Instantiation:** The specific instantiation points for this class are not provided within the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `FunctionDescription` is implicitly generated by Pydantic's BaseModel. It initializes an instance by accepting values for its defined fields: `overall`, `parameters`, `returns`, and `usage_context`, ensuring type validation upon instantiation.
    *   *Parameters:*
        - **overall** (`str`): A string describing the function's overall purpose.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects detailing each parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of `ReturnDescription` objects describing the function's return values.
        - **usage_context** (`UsageContext`): An object providing context about where and how the function is used.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class serves as a Pydantic model designed to represent a comprehensive analysis of a single function. It encapsulates the function's unique identifier, a detailed `FunctionDescription` object, and an optional `error` field for reporting issues during analysis. This model is fundamental for structuring and validating the output of function analysis processes within the system.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. Initialization is handled by Pydantic's `BaseModel` based on the class's field definitions, which include `identifier`, `description`, and `error`.
    *   *Parameters:*
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to structure metadata about a Python class's __init__ method. It serves as a data container, holding a string description of the constructor's purpose and a list of ParameterDescription objects, each detailing a parameter of the __init__ method. This class is used to provide a standardized representation of how a class is initialized, including its parameters.
*   **Instantiation:** This class is not explicitly instantiated by any components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context, aside from pydantic.BaseModel for its structural definition and ParameterDescription for its `parameters` field type.
*   **Constructor:**
    *   *Description:* This class does not define an explicit __init__ method. It inherits its constructor behavior from pydantic.BaseModel, which automatically handles the initialization of its fields `description` and `parameters` based on provided keyword arguments.
    *   *Parameters:*
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to structure metadata about a Python class's operational context. It specifically defines two string fields: 'dependencies' to describe external functional requirements and 'instantiated_by' to indicate where the class is created or utilized. This model provides a standardized format for capturing and conveying essential contextual information for documentation or analysis purposes.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for ClassContext is implicitly generated by Pydantic's BaseModel. It handles the validation and assignment of the `dependencies` and `instantiated_by` string fields upon instantiation, ensuring that instances conform to the defined schema.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies required by the class.
        - **instantiated_by** (`str`): A string describing the locations or components responsible for instantiating this class.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription Pydantic model serves as a structured data schema for representing a comprehensive analysis of a Python class. It aggregates various aspects of a class, including its general purpose, the specifics of its constructor, a list of analyses for all its methods, and its external usage context. This model is designed to standardize the output format for class analysis, making it machine-readable and consistent for further processing by other AI systems.
*   **Instantiation:** There is no explicit information provided about where this class is instantiated.
*   **Dependencies:** This class does not explicitly declare any external functional dependencies within its definition.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly generates an __init__ method. This constructor is responsible for initializing the instance attributes `overall`, `init_method`, `methods`, and `usage_context` based on the provided arguments, ensuring they conform to their respective types.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary of the class's purpose.
        - **init_method** (`ConstructorDescription`): Details about the class's constructor (__init__ method).
        - **methods** (`List[FunctionAnalysis]`): A list of detailed analyses for each method within the class.
        - **usage_context** (`ClassContext`): Contextual information regarding the class's dependencies and instantiation.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data structure for encapsulating the comprehensive analysis of a Python class. It is a Pydantic BaseModel, ensuring data validation and serialization capabilities. This model holds the class's unique identifier, a detailed ClassDescription object containing its constructor and method analyses, and an optional error field to indicate any issues encountered during the analysis process.
*   **Instantiation:** The instantiation points for this class are not explicitly provided in the current context.
*   **Dependencies:** The ClassAnalysis class depends on pydantic.BaseModel for its core functionality and typing.Optional for type hinting.
*   **Constructor:**
    *   *Description:* The ClassAnalysis class is a Pydantic BaseModel, meaning its constructor is implicitly generated by Pydantic. It initializes the instance with an identifier string, a ClassDescription object, and an optional error string, ensuring type validation for all provided arguments.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, its constructor, and methods.
        - **error** (`Optional[str]`): An optional string containing an error message if the analysis failed, otherwise None.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The `CallInfo` class is a Pydantic BaseModel designed to encapsulate details about a specific call event within a codebase. It serves as a structured data container, providing information such as the file path, the name of the calling function, the mode of the call (e.g., 'method', 'function'), and the line number where the call occurs. This class is primarily used in relationship analysis to track and represent 'called_by' and 'instantiated_by' relationships.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* The `CallInfo` class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance by accepting values for its defined fields: `file`, `function`, `mode`, and `line`. Pydantic handles the validation and assignment of these attributes, ensuring data integrity according to their specified types.
    *   *Parameters:*
        - **file** (`str`): The file path where the call event occurred.
        - **function** (`str`): The name of the calling function or method.
        - **mode** (`str`): The type of call, indicating if it's a 'method', 'function', or 'module' level call.
        - **line** (`int`): The line number within the file where the call event took place.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to provide a structured data model for encapsulating context information related to the analysis of a specific function. It defines two key attributes: 'calls', which is a list of strings representing the identifiers of functions or methods invoked by the analyzed function, and 'called_by', which is a list of CallInfo objects detailing the locations or contexts from which the analyzed function itself is invoked. This model facilitates a standardized format for collecting and exchanging function-level usage data within a larger system.
*   **Instantiation:** The class is not explicitly shown to be instantiated by any other components in the provided context.
*   **Dependencies:** The class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, meaning its `__init__` method is implicitly generated by Pydantic. It allows for the creation of instances by passing keyword arguments that match its defined fields: `calls` and `called_by`.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of identifiers for other functions, methods, or classes that this function calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this function is called from.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The `FunctionAnalysisInput` class is a Pydantic BaseModel designed to serve as a structured input for generating a `FunctionAnalysis` object. It encapsulates all necessary data points required to perform a detailed analysis of a Python function, including its source code, identifier, relevant imports, and additional contextual information. This class ensures that all required data for function analysis is provided in a consistent and validated format.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, meaning its constructor is implicitly generated by Pydantic. It initializes instances by validating and assigning values to its defined fields: `mode`, `identifier`, `source_code`, `imports`, and `context`. These fields serve as the parameters for creating an instance of this input schema.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, which must be 'function_analysis' to indicate the type of analysis requested.
        - **identifier** (`str`): The unique name or identifier of the function that is to be analyzed.
        - **source_code** (`str`): The raw source code string of the entire function definition to be analyzed.
        - **imports** (`List[str]`): A list of import statements that are relevant to the function's source code, providing necessary context for dependencies.
        - **context** (`FunctionContextInput`): An object containing additional contextual information pertinent to the function, such as its calls and where it is called by.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information about a specific method. It serves as a data transfer object, holding details such as the method's unique identifier, a list of entities it calls, a list of entities that call it, its arguments, and its docstring. This model is crucial for providing a standardized representation of method context within a larger system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an __init__ method. This constructor is used to initialize instances of MethodContextInput by assigning values to its defined fields: identifier, calls, called_by, args, and docstring.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions called by this method.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, representing where this method is called.
        - **args** (`List[str]`): A list of string representations of the arguments passed to the method.
        - **docstring** (`Optional[str]`): The docstring content of the method, if available.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The `ClassContextInput` class is a Pydantic BaseModel designed to encapsulate structured context information for the analysis of a Python class. It serves as a data container, defining the expected format for input data related to a class's dependencies, where it is instantiated, and detailed context for its methods. This model ensures consistency and validation of the contextual data used in a larger analysis system.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly declare external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ClassContextInput` is implicitly generated by Pydantic's `BaseModel`. It initializes an instance of the class by validating and assigning values to its `dependencies`, `instantiated_by`, and `method_context` fields based on the provided arguments.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external functional dependencies of the class being analyzed.
        - **instantiated_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where the class being analyzed is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of `MethodContextInput` objects, each providing specific context for a method within the class being analyzed.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a data validation and serialization schema, ensuring that all necessary components like the class identifier, its source code, relevant imports, and contextual information are present and correctly typed before analysis proceeds. This model standardizes the data format for class analysis operations within the system.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class does not explicitly define an `__init__` method. It inherits from `pydantic.BaseModel`, and its constructor is implicitly generated by Pydantic based on the type-hinted fields, allowing direct instantiation with keyword arguments corresponding to its attributes.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the operation mode, which must be 'class_analysis' to indicate a class analysis request.
        - **identifier** (`str`): The unique name or identifier of the class being analyzed.
        - **source_code** (`str`): The raw source code string of the entire class definition.
        - **imports** (`List[str]`): A list of import statements from the source file, which may include imports relevant to the class or its methods.
        - **context** (`ClassContextInput`): Additional contextual information required for the class analysis, such as dependencies and instantiation points.
*   **Methods:**

---
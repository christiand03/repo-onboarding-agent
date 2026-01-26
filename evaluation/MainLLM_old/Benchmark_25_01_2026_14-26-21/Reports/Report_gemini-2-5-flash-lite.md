# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview (can be accessed under 'basic_info')
    - **Description:** Information not found
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** Information not found

*   **Repository Structure:**
    ```mermaid
    graph LR
    root --> SystemPrompts
    root --> backend
    root --> database
    root --> frontend
    root --> notizen
    root --> result
    root --> schemas
    root --> statistics
    SystemPrompts --> SystemPromptClassHelperLLM.txt
    SystemPrompts --> SystemPromptFunctionHelperLLM.txt
    SystemPrompts --> SystemPromptHelperLLM.txt
    SystemPrompts --> SystemPromptMainLLM.txt
    SystemPrompts --> SystemPromptMainLLMToon.txt
    SystemPrompts --> SystemPromptNotebookLLM.txt
    backend --> AST_Schema.py
    backend --> File_Dependency.py
    backend --> HelperLLM.py
    backend --> MainLLM.py
    backend --> __init__.py
    backend --> basic_info.py
    backend --> callgraph.py
    backend --> converter.py
    backend --> getRepo.py
    backend --> main.py
    backend --> relationship_analyzer.py
    backend --> scads_key_test.py
    database --> db.py
    frontend --> .streamlit
    frontend --> __init__.py
    frontend --> frontend.py
    frontend --> gifs
    frontend/.streamlit --> config.toml
    frontend/gifs --> 4j.gif
    notizen --> Report Agenda.txt
    notizen --> Zwischenpraesentation Agenda.txt
    notizen --> doc_bestandteile.md
    notizen --> grafiken
    notizen --> notizen.md
    notizen --> paul_notizen.md
    notizen --> praesentation_notizen.md
    notizen --> technische_notizen.md
    notizen/grafiken --> "1"
    notizen/grafiken --> "2"
    notizen/grafiken --> Flask-Repo
    notizen/grafiken --> Repo-onboarding
    notizen/grafiken/1 --> File_Dependency_Graph_Repo.dot
    notizen/grafiken/1 --> global_callgraph.png
    notizen/grafiken/1 --> global_graph.png
    notizen/grafiken/1 --> global_graph_2.png
    notizen/grafiken/1 --> repo.dot
    notizen/grafiken/2 --> FDG_repo.dot
    notizen/grafiken/2 --> fdg_graph.png
    notizen/grafiken/2 --> fdg_graph_2.png
    notizen/grafiken/2 --> filtered_callgraph_flask.png
    notizen/grafiken/2 --> filtered_callgraph_repo-agent.png
    notizen/grafiken/2 --> filtered_callgraph_repo-agent_3.png
    notizen/grafiken/2 --> filtered_repo_callgraph_flask.dot
    notizen/grafiken/2 --> filtered_repo_callgraph_repo-agent-3.dot
    notizen/grafiken/2 --> filtered_repo_callgraph_repo-agent.dot
    notizen/grafiken/2 --> global_callgraph.png
    notizen/grafiken/2 --> graph_flask.md
    notizen/grafiken/2 --> repo.dot
    notizen/grafiken/Flask-Repo --> __init__.dot
    notizen/grafiken/Flask-Repo --> __main__.dot
    notizen/grafiken/Flask-Repo --> app.dot
    notizen/grafiken/Flask-Repo --> auth.dot
    notizen/grafiken/Flask-Repo --> blog.dot
    notizen/grafiken/Flask-Repo --> blueprints.dot
    notizen/grafiken/Flask-Repo --> cli.dot
    notizen/grafiken/Flask-Repo --> conf.dot
    notizen/grafiken/Flask-Repo --> config.dot
    notizen/grafiken/Flask-Repo --> conftest.dot
    notizen/grafiken/Flask-Repo --> ctx.dot
    notizen/grafiken/Flask-Repo --> db.dot
    notizen/grafiken/Flask-Repo --> debughelpers.dot
    notizen/grafiken/Flask-Repo --> factory.dot
    notizen/grafiken/Flask-Repo --> flask.dot
    notizen/grafiken/Flask-Repo --> globals.dot
    notizen/grafiken/Flask-Repo --> hello.dot
    notizen/grafiken/Flask-Repo --> helpers.dot
    notizen/grafiken/Flask-Repo --> importerrorapp.dot
    notizen/grafiken/Flask-Repo --> logging.dot
    notizen/grafiken/Flask-Repo --> make_celery.dot
    notizen/grafiken/Flask-Repo --> multiapp.dot
    notizen/grafiken/Flask-Repo --> provider.dot
    notizen/grafiken/Flask-Repo --> scaffold.dot
    notizen/grafiken/Flask-Repo --> sessions.dot
    notizen/grafiken/Flask-Repo --> signals.dot
    notizen/grafiken/Flask-Repo --> tag.dot
    notizen/grafiken/Flask-Repo --> tasks.dot
    notizen/grafiken/Flask-Repo --> templating.dot
    notizen/grafiken/Flask-Repo --> test_appctx.dot
    notizen/grafiken/Flask-Repo --> test_async.dot
    notizen/grafiken/Flask-Repo --> test_auth.dot
    notizen/grafiken/Flask-Repo --> test_basic.dot
    notizen/grafiken/Flask-Repo --> test_blog.dot
    notizen/grafiken/Flask-Repo --> test_blueprints.dot
    notizen/grafiken/Flask-Repo --> test_cli.dot
    notizen/grafiken/Flask-Repo --> test_config.dot
    notizen/grafiken/Flask-Repo --> test_config.png
    notizen/grafiken/Flask-Repo --> test_converters.dot
    notizen/grafiken/Flask-Repo --> test_db.dot
    notizen/grafiken/Flask-Repo --> test_factory.dot
    notizen/grafiken/Flask-Repo --> test_helpers.dot
    notizen/grafiken/Flask-Repo --> test_instance_config.dot
    notizen/grafiken/Flask-Repo --> test_js_example.dot
    notizen/grafiken/Flask-Repo --> test_json.dot
    notizen/grafiken/Flask-Repo --> test_json_tag.dot
    notizen/grafiken/Flask-Repo --> test_logging.dot
    notizen/grafiken/Flask-Repo --> test_regression.dot
    notizen/grafiken/Flask-Repo --> test_reqctx.dot
    notizen/grafiken/Flask-Repo --> test_request.dot
    notizen/grafiken/Flask-Repo --> test_session_interface.dot
    notizen/grafiken/Flask-Repo --> test_signals.dot
    notizen/grafiken/Flask-Repo --> test_subclassing.dot
    notizen/grafiken/Flask-Repo --> test_templating.dot
    notizen/grafiken/Flask-Repo --> test_testing.dot
    notizen/grafiken/Flask-Repo --> test_user_error_handler.dot
    notizen/grafiken/Flask-Repo --> test_views.dot
    notizen/grafiken/Flask-Repo --> testing.dot
    notizen/grafiken/Flask-Repo --> typing.dot
    notizen/grafiken/Flask-Repo --> typing_app_decorators.dot
    notizen/grafiken/Flask-Repo --> typing_error_handler.dot
    notizen/grafiken/Flask-Repo --> typing_route.dot
    notizen/grafiken/Flask-Repo --> views.dot
    notizen/grafiken/Flask-Repo --> wrappers.dot
    notizen/grafiken/Flask-Repo --> wsgi.dot
    notizen/grafiken/Repo-onboarding --> AST.dot
    notizen/grafiken/Repo-onboarding --> Frontend.dot
    notizen/grafiken/Repo-onboarding --> HelperLLM.dot
    notizen/grafiken/Repo-onboarding --> HelperLLM.png
    notizen/grafiken/Repo-onboarding --> MainLLM.dot
    notizen/grafiken/Repo-onboarding --> agent.dot
    notizen/grafiken/Repo-onboarding --> basic_info.dot
    notizen/grafiken/Repo-onboarding --> callgraph.dot
    notizen/grafiken/Repo-onboarding --> getRepo.dot
    notizen/grafiken/Repo-onboarding --> graph_AST.png
    notizen/grafiken/Repo-onboarding --> graph_AST2.png
    notizen/grafiken/Repo-onboarding --> graph_AST3.png
    notizen/grafiken/Repo-onboarding --> main.dot
    notizen/grafiken/Repo-onboarding --> tools.dot
    notizen/grafiken/Repo-onboarding --> types.dot
    result --> ast_schema_01_12_2025_11-49-24.json
    result --> notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md
    result --> report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md
    result --> report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md
    result --> report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md
    result --> report_14_11_2025_14-52-36.md
    result --> report_14_11_2025_15-21-53.md
    result --> report_14_11_2025_15-26-24.md
    result --> report_21_11_2025_15-43-30.md
    result --> report_21_11_2025_16-06-12.md
    result --> report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md
    result --> report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md
    result --> result_2025-11-11_12-30-53.md
    result --> result_2025-11-11_12-43-51.md
    result --> result_2025-11-11_12-45-37.md
    schemas --> types.py
    statistics --> savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png
    statistics --> savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png
    statistics --> savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png
    statistics --> savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png
    statistics --> savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png
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
    ### Setup Guide
    Information not found
    ### Quick Startup
    Information not found

    ## 3. Use Cases & Commands
    This project appears to be a sophisticated system for onboarding and documenting software repositories. Its core functionality revolves around:

    *   **Repository Analysis:** Cloning Git repositories, parsing their file structures, and analyzing their codebases using Abstract Syntax Trees (ASTs).
    *   **LLM Integration:** Leveraging Large Language Models (LLMs) like Google Gemini, OpenAI (GPT), and Ollama for various tasks including generating documentation for functions and classes, and creating comprehensive repository reports.
    *   **Code Understanding:** Building call graphs and analyzing relationships between different code components (functions, classes, methods) to understand dependencies and code flow.
    *   **Data Persistence:** Utilizing MongoDB for storing user information, API keys, chat history, and conversation exchanges.
    *   **Frontend Interface:** Providing a Streamlit-based web interface for users to interact with the system, manage their API keys, view chat history, and potentially trigger analyses.

    **Primary Commands/Workflows:**

    *   **Repository Analysis and Reporting:** The main workflow (`backend.main.main_workflow`) likely orchestrates the entire process, from cloning a repository URL provided in the input to generating a final markdown report using LLMs. This includes extracting basic project info, AST schemas, and relationship data.
    *   **Notebook Analysis:** The `backend.main.notebook_workflow` specifically targets Jupyter notebooks within a repository, converting them to XML, extracting images, and generating reports for each notebook using an LLM.
    *   **Database Operations:** Functions within `database/db.py` handle user management (insert, fetch, update, delete), API key storage (with encryption), chat management, and exchange recording.
    *   **LLM Interaction:** `backend/HelperLLM.py` and `backend/MainLLM.py` manage the core LLM interactions, including generating structured documentation and synthesizing final reports.
    *   **Frontend Interactions:** Functions in `frontend/frontend.py` handle UI logic, user authentication, data loading from the database, rendering chat history, and managing feedback.

    ## 4. Architecture
    The Mermaid Syntax to visualize Graphs is not set up yet and will be added
    but if there is mermaid syntax in your input json display it here



    ## 5. Code Analysis

    ### File: `backend/AST_Schema.py`

    #### Class: `ASTVisitor`
    *   **Summary:** The ASTVisitor class, inheriting from `ast.NodeVisitor`, is designed to traverse the Abstract Syntax Tree (AST) of a Python source file. Its primary purpose is to extract structured information about imports, classes, and functions defined within that source code. It systematically builds a `schema` dictionary that categorizes these elements, including details like identifiers, names, docstrings, and source code segments, providing a comprehensive overview of the file's structure.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** The class does not explicitly list any external functional dependencies in the provided context, but it relies on the `ast` module for its core functionality and `path_to_module` for path resolution.
    *   **Constructor:**
        *   *Description:* The `__init__` method initializes an `ASTVisitor` instance by storing the raw source code, the file's absolute path, and the project's root directory. It calculates the module's qualified path and sets up an empty `schema` dictionary to accumulate discovered imports, functions, and classes. It also initializes `_current_class` to `None` to track the context of the class currently being visited during AST traversal.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            - **source_code** (`str`): The raw source code of the file being visited.
            - **file_path** (`str`): The absolute path to the file being visited.
            - **project_root** (`str`): The root directory of the project.
    *   **Methods:**
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method processes `ast.Import` nodes, which represent `import module` statements. It iterates through each alias defined in the import statement and appends the full module name to the `schema["imports"]` list. After recording the import, it calls `self.generic_visit(node)` to ensure continued traversal of the AST for any child nodes.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
                - **node** (`ast.Import`): The AST node representing an import statement.
            *   *Returns:*
            *   **Usage:** This method calls `self.generic_visit(node)` to continue AST traversal. It is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.Import` node is encountered during AST traversal.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method processes `ast.ImportFrom` nodes, which represent `from module import name` statements. It iterates through each alias in the import statement and appends the fully qualified name (e.g., `module.alias`) to the `schema["imports"]` list. Following this, it invokes `self.generic_visit(node)` to ensure that any nested AST nodes are also visited.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
                - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
            *   *Returns:*
            *   **Usage:** This method calls `self.generic_visit(node)` to continue AST traversal. It is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ImportFrom` node is encountered during AST traversal.
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions. It constructs a `class_info` dictionary containing the class's fully qualified identifier, its name, docstring, the source code segment, and its start and end line numbers. This `class_info` is then appended to `self.schema["classes"]`. It temporarily sets `self._current_class` to this class's information to correctly attribute nested methods, performs a generic visit to traverse the class's body, and then resets `self._current_class` to `None`.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
                - **node** (`ast.ClassDef`): The AST node representing a class definition.
            *   *Returns:*
            *   **Usage:** This method calls `path_to_module`, `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit(node)`. It is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.ClassDef` node is encountered during AST traversal.
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method processes `ast.FunctionDef` nodes, distinguishing between methods defined within a class and standalone functions. If `_current_class` is set, it extracts method-specific details like identifier, name, arguments, docstring, and line numbers, appending them to the `method_context` of the current class. Otherwise, it extracts similar details for a standalone function and appends them to `self.schema["functions"]`. Finally, it calls `self.generic_visit(node)` to continue AST traversal.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
                - **node** (`ast.FunctionDef`): The AST node representing a function definition.
            *   *Returns:*
            *   **Usage:** This method calls `ast.get_docstring`, `ast.get_source_segment`, and `self.generic_visit(node)`. It also implicitly uses `self.module_path` which is derived from `path_to_module`. This method is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.FunctionDef` node is encountered, and explicitly by `visit_AsyncFunctionDef`.
        *   **`visit_AsyncFunctionDef`**
            *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
            *   *Description:* This method processes `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. It delegates the entire processing logic directly to the `visit_FunctionDef` method. This approach ensures that asynchronous functions are handled consistently with regular functions for the purpose of schema extraction, capturing their details without duplicating code.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor class.
                - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
            *   *Returns:*
            *   **Usage:** This method calls `self.visit_FunctionDef(node)`. It is called by the `ast.NodeVisitor`'s dispatch mechanism when an `ast.AsyncFunctionDef` node is encountered during AST traversal.
    *   **Usage:** The provided context does not specify where this class is instantiated.

    #### Class: `ASTAnalyzer`
    *   **Summary:** The ASTAnalyzer class is responsible for processing a repository's Python files to build a comprehensive Abstract Syntax Tree (AST) schema and then enriching this schema with inter-component relationship data. It first parses individual Python files to extract AST nodes like functions and classes, and then integrates call and instantiation relationships to provide a holistic view of the codebase's structure and dependencies.
    *   **Instantiation:** This class is not instantiated by any other components based on the provided context.
    *   **Dependencies:** This class has no listed external functional dependencies based on the provided context.
    *   **Constructor:**
        *   *Description:* The constructor for the ASTAnalyzer class currently performs no specific initialization logic, serving as a placeholder for future setup if needed.
        *   *Parameters:*
    *   **Methods:**
        *   **`merge_relationship_data`**
            *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict) -> dict`
            *   *Description:* This method takes a full AST schema and raw relationship data (incoming/outgoing calls) and merges the relationship information into the schema. It iterates through functions and classes within the schema, populating their respective 'calls', 'called_by', and 'instantiated_by' contexts. Additionally, it identifies and lists external dependencies for each class based on its methods' outgoing calls.
            *   *Parameters:*
                - **full_schema** (`dict`): The complete AST schema of the repository, containing file, function, and class definitions.
                - **raw_relationships** (`dict`): A dictionary containing raw 'outgoing' and 'incoming' call relationships between identifiers.
            *   *Returns:*
                - **full_schema** (`dict`): The updated full schema dictionary, now enriched with call and instantiation relationship data.
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context. It is not called by any other functions or methods based on the provided context.
        *   **`analyze_repository`**
            *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository) -> dict`
            *   *Description:* This method analyzes a list of file objects from a Git repository to construct an initial AST schema. It filters for Python files, parses their content using the `ast` module, and then uses an `ASTVisitor` to extract structured AST nodes (imports, functions, classes). The extracted data for each file is then added to a `full_schema` dictionary, handling potential parsing errors gracefully.
            *   *Parameters:*
                - **files** (`list`): A list of file objects, each containing a path and content, to be analyzed.
                - **repo** (`GitRepository`): An object representing the Git repository, though its direct use is not evident in the provided snippet beyond potentially providing file objects.
            *   *Returns:*
                - **full_schema** (`dict`): A dictionary representing the AST schema of the repository, organized by file paths.
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context. It is not called by any other functions or methods based on the provided context.

    ### File: `backend/File_Dependency.py`

    #### Class: `FileDependencyGraph`
    *   **Summary:** The FileDependencyGraph class extends ast.NodeVisitor to construct a graph of file-level import dependencies within a Python repository. It traverses the Abstract Syntax Tree (AST) of Python files, specifically looking for import and from ... import ... statements. The class's core functionality involves accurately resolving both absolute and relative imports, including handling symbols exported via __init__.py files. It maintains an import_dependencies dictionary to store the relationships, mapping each file to the set of modules it imports.
    *   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
    *   **Dependencies:** This class does not explicitly list any functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* This constructor initializes the FileDependencyGraph instance. It sets the filename attribute, representing the file being analyzed, and the repo_root attribute, indicating the root directory of the repository. These attributes are crucial for resolving file paths and dependencies within the repository.
        *   *Parameters:*
            - **filename** (`str`): The path or name of the file for which dependencies are being analyzed.
            - **repo_root** (`Any`): The root directory of the repository, used for resolving file paths.
    *   **Methods:**
        *   **`_resolve_module_name`**
            *   *Signature:* `def _resolve_module_name(self, node: ImportFrom) -> list[str]`
            *   *Description:* This method is responsible for resolving relative import statements (e.g., from .. import name). It determines the actual module or symbol names based on the import level and the current file's location within the repository. It first identifies the base directory for the relative import, then checks if the imported names correspond to existing module files or symbols exported by __init__.py files using nested helper functions. If no valid modules or symbols can be resolved, it raises an ImportError.
            *   *Parameters:*
                - **node** (`ImportFrom`): An AST ImportFrom node representing the relative import statement.
            *   *Returns:*
                - **resolved** (`list[str]`): A list of resolved module or symbol names.
            *   **Usage:** This method calls `get_all_temp_files`, `Path`, `Path.stem`, `Path.name`, `Path.parent`, `Path.resolve`, `Path.exists`, `Path.read_text`, `parse`, `walk`, `isinstance`, `literal_eval`, `iskeyword`. It also defines and calls nested functions `module_file_exists` and `init_exports_symbol`. It is called by `visit_ImportFrom`.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None = None)`
            *   *Description:* This method is part of the NodeVisitor pattern and is called when an Import or ImportFrom AST node is encountered. Its primary function is to record import dependencies. It adds the imported module or symbol name to the import_dependencies dictionary, mapping the current filename to a set of its dependencies. If a base_name is provided (typically for from ... import ... statements), it uses that; otherwise, it uses the alias name from the import node.
            *   *Parameters:*
                - **node** (`Import | ImportFrom`): The AST node representing an import statement.
                - **base_name** (`str | None`): An optional base name for the module, used when resolving from ... import ... statements. Defaults to None.
            *   *Returns:*
            *   **Usage:** This method calls `self.generic_visit`. It is called by `visit_ImportFrom`.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
            *   *Description:* This method, also part of the NodeVisitor pattern, handles ImportFrom AST nodes. It extracts the module name from the import statement. If it's a direct import (e.g., from a.b.c import d), it takes the last part of the module (c) as the base name and delegates to visit_Import. If it's a relative import (e.g., from .. import x), it uses the `_resolve_module_name` helper to determine the actual module names before calling `visit_Import` for each resolved name. It includes error handling for failed relative import resolutions.
            *   *Parameters:*
                - **node** (`ImportFrom`): The AST node representing an ImportFrom statement.
            *   *Returns:*
            *   **Usage:** This method calls `str.split`, `self.visit_Import`, `self._resolve_module_name`, `print`, `self.generic_visit`. It is primarily invoked by the AST NodeVisitor framework.
        *   **`module_file_exists`**
            *   *Signature:* `def module_file_exists(rel_base: Path, name: str) -> bool`
            *   *Description:* This helper function, nested within `_resolve_module_name`, checks if a given module or package exists relative to a base directory. It verifies if a file named `name.py` exists or if a directory named `name` contains an `__init__.py` file, indicating a package. This is used to validate potential import targets during relative import resolution.
            *   *Parameters:*
                - **rel_base** (`Path`): The base directory relative to the repository root.
                - **name** (`str`): The name of the module or package to check.
            *   *Returns:*
                - **exists** (`bool`): True if the module file or package `__init__.py` exists, False otherwise.
            *   **Usage:** This method calls `Path`, `Path.exists`. It is called by `_resolve_module_name`.
        *   **`init_exports_symbol`**
            *   *Signature:* `def init_exports_symbol(rel_base: Path, symbol: str) -> bool`
            *   *Description:* This helper function, nested within `_resolve_module_name`, determines if a given symbol is exported by an `__init__.py` file within a specified relative base directory. It checks if the `__init__.py` file exists, parses its content, and then inspects for `__all__` assignments (using `literal_eval`) or direct definitions of functions, classes, or assignments matching the symbol name. This helps resolve symbols imported from packages.
            *   *Parameters:*
                - **rel_base** (`Path`): The base directory relative to the repository root.
                - **symbol** (`str`): The symbol name to check for export.
            *   *Returns:*
                - **exports** (`bool`): True if the `__init__.py` exports the symbol, False otherwise.
            *   **Usage:** This method calls `Path`, `Path.exists`, `Path.read_text`, `parse`, `walk`, `isinstance`, `literal_eval`. It is called by `_resolve_module_name`.
    *   **Usage:** This class is not explicitly shown to be instantiated by any other components in the provided context.

    #### Function: `backend.File_Dependency.build_file_dependency_graph`
    *   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph`
    *   **Description:** This function constructs a directed graph representing file-level import dependencies. It initializes a NetworkX directed graph and then uses a `FileDependencyGraph` visitor to traverse the provided Abstract Syntax Tree (AST). The visitor collects import relationships, which are then used to populate the graph with nodes for callers and callees, and edges representing the import dependencies. The resulting graph illustrates which files import other files.
    *   **Parameters:**
        - **filename** (`str`): The name of the file whose dependencies are being analyzed.
        - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be processed for dependencies.
        - **repo_root** (`str`): The root directory of the repository, used for resolving file paths and dependencies.
    *   **Returns:**
        - **graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies between them.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.File_Dependency.build_repository_graph`
    *   **Signature:** `def build_repository_graph(repository: GitRepository) -> nx.DiGraph`
    *   **Description:** This function constructs a directed graph representing the dependencies within a given Git repository. It iterates through all Python files in the repository, parses each file's content into an Abstract Syntax Tree (AST), and then builds a file-specific dependency graph. These individual file graphs are then merged into a single global directed graph, capturing the overall repository structure and inter-file relationships.
    *   **Parameters:**
        - **repository** (`GitRepository`): The Git repository object from which to extract file dependencies.
    *   **Returns:**
        - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependencies found across the repository's Python files.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.File_Dependency.get_all_temp_files`
    *   **Signature:** `def get_all_temp_files(directory: str) -> list[Path]`
    *   **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as a string input. The function converts this string into an absolute `pathlib.Path` object and then recursively searches for all files ending with the ".py" extension. For each Python file found, it calculates its path relative to the initial root directory. Finally, it returns a list containing these relative `pathlib.Path` objects.
    *   **Parameters:**
        - **directory** (`str`): The path to the root directory from which to start searching for Python files.
    *   **Returns:**
        - **all_files** (`list[pathlib.Path]`): A list of `pathlib.Path` objects, where each object represents a Python file found within the specified directory and its subdirectories, with paths relative to the input directory.
    *   **Usage:** This function is called by no other functions.

    ### File: `backend/HelperLLM.py`

    #### Function: `backend.HelperLLM.main_orchestrator`
    *   **Signature:** `def main_orchestrator()`
    *   **Description:** This function serves as a testing and orchestration loop for the LLMHelper class, primarily demonstrating how to process function and class analysis inputs. It defines pre-computed dummy data conforming to Pydantic models for `FunctionAnalysisInput` and `FunctionAnalysis`. The function then initializes an `LLMHelper` instance and simulates the generation of documentation for these functions, logging the process and printing the final aggregated results.
    *   **Parameters:**
    *   **Returns:**
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Class: `LLMHelper`
    *   **Summary:** This class provides a centralized interface for interacting with various Large Language Models (LLMs) to generate structured documentation for Python functions and classes. It handles API key validation, loads system prompts from files, dynamically configures the LLM client based on the specified model (supporting Gemini, OpenAI, Ollama, and custom APIs), and manages batch processing with rate limiting. The class ensures that LLM outputs conform to predefined Pydantic schemas for FunctionAnalysis and ClassAnalysis.
    *   **Instantiation:** This class is not explicitly instantiated by any other components listed in the provided context.
    *   **Dependencies:** This class does not have any explicit external dependencies listed in the provided context.
    *   **Constructor:**
        *   *Description:* The constructor initializes the LLMHelper by validating the provided API key and loading system prompts for function and class analysis from specified file paths. It then configures the appropriate LLM client (Google Gemini, OpenAI, Ollama, or a custom API) based on the `model_name` and sets up structured output parsing using Pydantic schemas. Finally, it calls a private method to configure batch processing settings for the chosen model.
        *   *Parameters:*
            - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
            - **function_prompt_path** (`str`): The file path to the system prompt used for generating function documentation.
            - **class_prompt_path** (`str`): The file path to the system prompt used for generating class documentation.
            - **model_name** (`str`): The name of the LLM model to use (e.g., 'gemini-2.0-flash-lite', 'gpt-4'). Defaults to 'gemini-2.0-flash-lite'.
            - **base_url** (`str`): An optional base URL for custom LLM endpoints, particularly for Ollama or self-hosted models. Defaults to None.
    *   **Methods:**
        *   **`_configure_batch_settings`**
            *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
            *   *Description:* This private method configures the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It assigns different batch sizes for various Gemini, Llama, and GPT models, as well as custom API models, to optimize API calls and respect rate limits. If an unknown model is provided, it defaults to a conservative batch size of 2.
            *   *Parameters:*
                - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
            *   *Returns:*
            *   **Usage:** This method does not explicitly call other methods, classes, or functions within its source code. It is not explicitly called by other functions or methods.
        *   **`generate_for_functions`**
            *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]`
            *   *Description:* This method generates structured documentation for a list of function inputs using the configured LLM. It processes inputs in batches, converts them to JSON payloads, and sends them to the `function_llm` for analysis. The method includes error handling for batch calls and implements a waiting period between batches to comply with API rate limits, returning a list of validated `FunctionAnalysis` objects or `None` for failed items.
            *   *Parameters:*
                - **function_inputs** (`List[FunctionAnalysisInput]`): A list of FunctionAnalysisInput objects, each containing data for a function to be documented.
            *   *Returns:*
                - **None** (`List[Optional[FunctionAnalysis]]`): A list of FunctionAnalysis objects, where each object represents the structured documentation for a function, or None if an error occurred during its generation.
            *   **Usage:** This method does not explicitly call other methods, classes, or functions within its source code. It is not explicitly called by other functions or methods.
        *   **`generate_for_classes`**
            *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]`
            *   *Description:* This method generates structured documentation for a list of class inputs using the configured LLM. Similar to `generate_for_functions`, it processes inputs in batches, converts them to JSON payloads, and dispatches them to the `class_llm` for analysis. It incorporates error handling for API calls and includes a rate-limiting delay between batches, returning a list of validated `ClassAnalysis` objects or `None` for failed items.
            *   *Parameters:*
                - **class_inputs** (`List[ClassAnalysisInput]`): A list of ClassAnalysisInput objects, each containing data for a class to be documented.
            *   *Returns:*
                - **None** (`List[Optional[ClassAnalysis]]`): A list of ClassAnalysis objects, where each object represents the structured documentation for a class, or None if an error occurred during its generation.
            *   **Usage:** This method does not explicitly call other methods, classes, or functions within its source code. It is not explicitly called by other functions or methods.
    *   **Usage:** This class is not explicitly instantiated by other components listed in the provided context.

    ### File: `backend/MainLLM.py`

    #### Class: `MainLLM`
    *   **Summary:** The MainLLM class serves as a central interface for interacting with various Large Language Models (LLMs). It abstracts away the complexities of different LLM providers by dynamically initializing the appropriate client (Gemini, OpenAI, or Ollama) based on configuration parameters like model name and base URL. The class manages a system prompt loaded from a file and offers both synchronous (`call_llm`) and asynchronous streaming (`stream_llm`) methods for sending user input and receiving LLM responses. Its primary responsibility is to provide a unified and flexible way to integrate LLM capabilities into an application.
    *   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
    *   **Dependencies:** This class does not have explicit external dependencies listed in the provided context.
    *   **Constructor:**
        *   *Description:* The constructor initializes the MainLLM instance by setting up the system prompt from a specified file and configuring the underlying Large Language Model (LLM) client. It supports various LLM providers like Gemini, OpenAI-compatible APIs, and Ollama, dynamically selecting the appropriate client based on the `model_name` and an optional `base_url`. The method also performs validation for the API key and ensures the prompt file exists, raising `ValueError` or `FileNotFoundError` if issues are encountered.
        *   *Parameters:*
            - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
            - **prompt_file_path** (`str`): The file path to the system prompt that will be used for LLM interactions.
            - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This parameter dictates which LLM client (Gemini, OpenAI, Ollama) is initialized.
            - **base_url** (`str | None`): An optional base URL for custom LLM endpoints, particularly for Ollama or OpenAI-compatible services. If not provided, a default Ollama URL might be used.
    *   **Methods:**
        *   **`call_llm`**
            *   *Signature:* `def call_llm(self, user_input: str)`
            *   *Description:* This method sends a user input along with the pre-configured system prompt to the initialized LLM for a single, synchronous response. It constructs a list of messages (system and human), invokes the LLM client, and returns the content of the LLM's response. Error handling is included to catch any exceptions during the LLM call, logging them and returning None.
            *   *Parameters:*
                - **user_input** (`str`): The user's query or message to be sent to the LLM.
            *   *Returns:*
                - **content** (`str | None`): The generated text content from the LLM, or None if an error occurred during the call.
            *   **Usage:** This method does not explicitly call other functions or methods according to the provided context. It is not explicitly called by other functions or methods according to the provided context.
        *   **`stream_llm`**
            *   *Signature:* `def stream_llm(self, user_input: str)`
            *   *Description:* This method provides a streaming interface to the LLM, allowing for real-time processing of the LLM's response. It constructs the message payload (system and human messages) and then utilizes the LLM client's `stream` method. The method yields chunks of the LLM's content as they become available, enabling a responsive user experience. Error handling is included to catch exceptions during the streaming process, yielding an error message if one occurs.
            *   *Parameters:*
                - **user_input** (`str`): The user's query or message to be streamed to the LLM.
            *   *Returns:*
                - **chunk.content** (`Generator[str, None, None]`): A generator that yields string chunks of the LLM's streamed response. In case of an error, it yields a single string containing the error message.
            *   **Usage:** This method does not explicitly call other functions or methods according to the provided context. It is not explicitly called by other functions or methods according to the provided context.

    ### File: `backend/basic_info.py`

    #### Class: `ProjektInfoExtractor`
    *   **Summary:** The ProjektInfoExtractor class is designed to systematically extract and consolidate fundamental project information from various common project files, including READMEs, pyproject.toml, and requirements.txt. It initializes a structured dictionary to hold project overview and installation details, populating it by parsing these files with a defined priority. The class provides utility methods for content cleaning, file location, and specific Markdown section extraction, culminating in a comprehensive information dictionary.
    *   **Instantiation:** The input context does not specify where this class is instantiated, implying it's a standalone utility or its instantiation points are not tracked in this context.
    *   **Dependencies:** "The class depends on the 're' module for regular expression operations, the 'os' module for path manipulation, and the 'tomllib' module for parsing TOML files. It also uses 'typing' for type hints."
    *   **Constructor:**
        *   *Description:* The constructor initializes the ProjektInfoExtractor instance. It sets a constant `INFO_NICHT_GEFUNDEN` to 'Information not found' and creates a nested dictionary `self.info` to store extracted project details. This `self.info` dictionary is pre-populated with placeholders using `INFO_NICHT_GEFUNDEN` for various project overview and installation fields, ensuring a consistent initial state.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
    *   **Methods:**
        *   **`_clean_content`**
            *   *Signature:* `def _clean_content(self, content: str) -> str`
            *   *Description:* This private utility method is designed to sanitize string content by removing null bytes (\\x00). Null bytes can appear in text due to encoding errors, such as reading a UTF-16 encoded file as UTF-8. The method first checks if the input content is empty; if so, it returns an empty string. Otherwise, it performs a global replacement of all null bytes with an empty string, effectively deleting them, and returns the cleaned string.
            *   *Parameters:*
                - **content** (`str`): The string content to be cleaned.
            *   *Returns:*
                - **cleaned_content** (`str`): The input string with all null bytes removed.
            *   **Usage:** This method does not explicitly call other functions or methods. It is called by `_parse_readme`, `_parse_toml`, and `_parse_requirements` to preprocess file contents.
        *   **`_finde_datei`**
            *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any]) -> Optional[Any]`
            *   *Description:* This private helper method searches for a specific file within a list of given files based on a list of filename patterns. It iterates through each file in the provided `dateien` list and then through each `pattern` in the `patterns` list. It performs a case-insensitive check to see if the file's path ends with any of the specified patterns. The first file that matches any pattern is returned. If no matching file is found after checking all files against all patterns, the method returns None.
            *   *Parameters:*
                - **patterns** (`List[str]`): A list of string patterns (e.g., file extensions or names) to search for.
                - **dateien** (`List[Any]`): A list of file objects, where each object is expected to have a 'path' attribute.
            *   *Returns:*
                - **matching_file** (`Optional[Any]`): The first file object that matches any of the provided patterns, or None if no match is found.
            *   **Usage:** This method does not explicitly call other functions or methods. It is called by `extrahiere_info` to locate specific project files like README, pyproject.toml, and requirements.txt.
        *   **`_extrahiere_sektion_aus_markdown`**
            *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str]) -> Optional[str]`
            *   *Description:* This private method extracts text content located under a specific Markdown heading (level 2, '##') within a given string. It takes the full content and a list of keywords. It constructs a regular expression to find '##' followed by any of the keywords, capturing the text that follows until the next '##' heading or the end of the content. The search is case-insensitive and considers newlines. If a match is found, the extracted section is returned after stripping leading/trailing whitespace; otherwise, None is returned.
            *   *Parameters:*
                - **inhalt** (`str`): The full Markdown content string to search within.
                - **keywords** (`List[str]`): A list of keywords that identify the target Markdown heading.
            *   *Returns:*
                - **extracted_section** (`Optional[str]`): The text content found under the matching Markdown heading, or None if no such section is found.
            *   **Usage:** This method calls `re.escape`, `re.compile`, and `re.search` from the 're' module. It is called by `_parse_readme` to extract specific sections like features, tech stack, status, installation instructions, and quick start guides.
        *   **`_parse_readme`**
            *   *Signature:* `def _parse_readme(self, inhalt: str)`
            *   *Description:* This private method parses the content of a README file to extract various project information, populating the `self.info` dictionary. It first cleans the content using `_clean_content`. It then attempts to extract the project title from a level 1 Markdown heading ('#'). Subsequently, it tries to find a general project description. The method heavily relies on `_extrahiere_sektion_aus_markdown` to find and extract specific sections like 'Key Features', 'Tech Stack', 'Status', 'Installation', and 'Quick Start' based on predefined keyword lists. Information is only updated if the corresponding field in `self.info` is still set to `INFO_NICHT_GEFUNDEN`, ensuring that information from higher-priority sources (like pyproject.toml) is not overwritten.
            *   *Parameters:*
                - **inhalt** (`str`): The raw string content of the README file.
            *   *Returns:*
            *   **Usage:** This method calls `_clean_content` and `_extrahiere_sektion_aus_markdown` from the same class, and `re.search` from the 're' module. It is called by `extrahiere_info` after pyproject.toml and requirements.txt have been parsed, giving it lower priority for certain fields.
        *   **`_parse_toml`**
            *   *Signature:* `def _parse_toml(self, inhalt: str)`
            *   *Description:* This private method parses the content of a pyproject.toml file to extract project metadata. It first cleans the input content using `_clean_content`. It checks for the availability of the `tomllib` module and returns early with a warning if it's not installed. If `tomllib` is available, it attempts to load the TOML content into a Python dictionary. It then extracts the project 'name', 'description', and 'dependencies' from the '[project]' section of the TOML data, updating the `self.info` dictionary. Error handling is included to catch `tomllib.TOMLDecodeError` during parsing.
            *   *Parameters:*
                - **inhalt** (`str`): The raw string content of the pyproject.toml file.
            *   *Returns:*
            *   **Usage:** This method calls `_clean_content` from the same class, `tomllib.loads`, and `tomllib.TOMLDecodeError` from the 'tomllib' module. It is called by `extrahiere_info` to process pyproject.toml content, typically with higher priority for certain fields.
        *   **`_parse_requirements`**
            *   *Signature:* `def _parse_requirements(self, inhalt: str)`
            *   *Description:* This private method parses the content of a requirements.txt file to extract project dependencies. It first cleans the input content using `_clean_content`. It only proceeds to extract dependencies if the 'dependencies' field in `self.info` is still at its default `INFO_NICHT_GEFUNDEN` value, ensuring that pyproject.toml dependencies take precedence. It splits the content into lines, filters out empty lines and comments (lines starting with '#'), and then stores the cleaned dependency strings in the `self.info` dictionary.
            *   *Parameters:*
                - **inhalt** (`str`): The raw string content of the requirements.txt file.
            *   *Returns:*
            *   **Usage:** This method calls `_clean_content` from the same class. It is called by `extrahiere_info` to process requirements.txt content, with lower priority than pyproject.toml for dependencies.
        *   **`extrahiere_info`**
            *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str) -> Dict[str, Any]`
            *   *Description:* This public method orchestrates the entire information extraction process from various project files and a repository URL. It first uses `_finde_datei` to locate README, pyproject.toml, and requirements.txt files within the provided list of `dateien`. It then parses these files in a specific order of priority: pyproject.toml first, then requirements.txt, and finally README.md. After parsing, it formats the extracted dependencies into a human-readable string if they were found as a list. Finally, if a `repo_url` is provided and a project title hasn't been found or is generic, it attempts to derive a title from the URL. The method returns the fully populated `self.info` dictionary containing all extracted project details.
            *   *Parameters:*
                - **dateien** (`List[Any]`): A list of file objects (e.g., from a repository scan), each expected to have 'path' and 'content' attributes.
                - **repo_url** (`str`): The URL of the repository, used as a fallback to derive a project title.
            *   *Returns:*
                - **project_info** (`Dict[str, Any]`): A dictionary containing all extracted project information, including overview, installation details, and dependencies.
            *   **Usage:** This method calls `_finde_datei`, `_parse_toml`, `_parse_requirements`, and `_parse_readme` from the same class, and `os.path.basename` and `str.removesuffix`. The input context does not specify any callers for this method, implying it's a primary entry point for the class's functionality.

    ### File: `backend/callgraph.py`

    #### Function: `backend.callgraph.make_safe_dot`
    *   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
    *   **Description:** This function takes a NetworkX directed graph and a file path, then generates a DOT file representation of the graph. It first creates a copy of the input graph and relabels its nodes with simple, safe identifiers (e.g., 'n0', 'n1') to avoid potential issues with complex node names in DOT format. The original node names are preserved by assigning them as 'label' attributes to the newly relabeled nodes. Finally, the modified graph is written to the specified output path as a DOT file.
    *   **Parameters:**
        - **graph** (`nx.DiGraph`): The NetworkX directed graph to be converted into a DOT file.
        - **out_path** (`str`): The file path where the DOT graph representation will be saved.
    *   **Returns:**
        - **None**: This function does not return any value; it performs a side effect by writing a file to disk.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.callgraph.build_filtered_callgraph`
    *   **Signature:** `def build_filtered_callgraph(repo: GitRepository) -> nx.DiGraph`
    *   **Description:** This function constructs a directed call graph for a given Git repository, focusing exclusively on functions identified as "self-written" within the repository's Python files. It first traverses all Python files to identify and collect all locally defined functions using an AST visitor. Subsequently, it re-processes these files to detect call relationships between functions. Only calls where both the caller and the callee are among the identified "self-written" functions are included in the final NetworkX directed graph, which is then returned.
    *   **Parameters:**
        - **repo** (`GitRepository`): The GitRepository object representing the code repository to analyze.
    *   **Returns:**
        - **global_graph** (`networkx.DiGraph`): A NetworkX directed graph representing the call relationships between self-written functions within the repository.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Class: `CallGraph`
    *   **Summary:** The CallGraph class is an ast.NodeVisitor designed to construct a call graph for a given Python source file. It traverses the Abstract Syntax Tree (AST) of a file, identifying function definitions, class definitions, import statements, and function calls. Through its visit_* methods, it maps local definitions, resolves imported names, and records caller-callee relationships in a NetworkX directed graph, ultimately providing a structured representation of how functions and methods interact within the codebase.
    *   **Instantiation:** This class is not explicitly instantiated by any known components according to the provided context.
    *   **Dependencies:** This class depends on 'ast' for parsing Python code, 'networkx' (aliased as nx) for graph representation, and 'typing.Dict' for type hinting.
    *   **Constructor:**
        *   *Description:* This constructor initializes the CallGraph instance by setting up various internal state variables. It stores the filename, initializes context trackers for the current function and class, and sets up dictionaries and sets for managing local definitions, the NetworkX graph, import mappings, discovered functions, and recorded call edges.
        *   *Parameters:*
            - **filename** (`str`): The path to the source file being analyzed.
    *   **Methods:**
        *   **`_recursive_call`**
            *   *Signature:* `def _recursive_call(self, node)`
            *   *Description:* This private helper method recursively traverses an AST node to extract the full dotted name components of a function or method call. It handles `ast.Call`, `ast.Name`, and `ast.Attribute` nodes, returning a list of strings representing these components. This is crucial for identifying the target of a call expression.
            *   *Parameters:*
                - **node** (`ast.AST`): The AST node to be recursively processed, typically representing a call, name, or attribute.
            *   *Returns:*
                - **name_components** (`list[str]`): A list of string components forming the fully qualified name of the called entity (e.g., ['pkg', 'mod', 'Class', 'method']).
            *   **Usage:** This method calls itself recursively to traverse the AST node structure. It is called by `visit_Call`.
        *   **`_resolve_all_callee_names`**
            *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]]) -> list[str]`
            *   *Description:* This private helper method takes a list of potential callee name components and attempts to resolve them to their fully qualified names. It prioritizes resolution by checking local definitions, then import mappings, and finally constructs a full name based on the current file and class context. This ensures that call targets are correctly identified regardless of their origin (local, imported, or within the same file/class).
            *   *Parameters:*
                - **callee_nodes** (`list[list[str]]`): A list where each inner list represents the name components of a potential callee.
            *   *Returns:*
                - **resolved_names** (`list[str]`): A list of fully resolved, fully qualified names for the callees.
            *   **Usage:** This method accesses `self.local_defs`, `self.import_mapping`, `self.current_class`, and `self.filename`. It is called by `visit_Call`.
        *   **`_make_full_name`**
            *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None = None) -> str`
            *   *Description:* This private helper method constructs a fully qualified name for a function or method. It prepends the filename and optionally the class_name to the given basename, using '::' as a separator. This ensures a consistent and unique identifier for each callable entity within the call graph.
            *   *Parameters:*
                - **basename** (`str`): The base name of the function or method.
                - **class_name** (`str | None`): The name of the class if the entity is a method; otherwise, None.
            *   *Returns:*
                - **full_name** (`str`): The fully qualified name of the function or method.
            *   **Usage:** This method accesses `self.filename`. It is called by `visit_FunctionDef`.
        *   **`_current_caller`**
            *   *Signature:* `def _current_caller(self) -> str`
            *   *Description:* This private helper method determines the identifier of the current calling context. If a function is currently being visited (i.e., `self.current_function` is set), it returns that function's full name. Otherwise, it returns a placeholder indicating the global scope within the current file, ensuring all calls are attributed to a source.
            *   *Parameters:*
            *   *Returns:*
                - **caller_identifier** (`str`): The fully qualified name of the current function or a global scope identifier.
            *   **Usage:** This method accesses `self.current_function` and `self.filename`. It is called by `visit_Call`.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method, overriding `ast.NodeVisitor.visit_Import`, processes 'import' statements. It extracts the module name and any alias, then stores this mapping in `self.import_mapping`. This mapping is crucial for resolving fully qualified names of imported modules and functions later during call analysis. After processing, it continues the AST traversal.
            *   *Parameters:*
                - **node** (`ast.Import`): The AST node representing an 'import' statement.
            *   *Returns:*
            *   **Usage:** This method calls `self.generic_visit`. It is called by the `ast.NodeVisitor` traversal mechanism.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node: ast.ImportFrom)`
            *   *Description:* This method, overriding `ast.NodeVisitor.visit_ImportFrom`, processes 'from ... import ...' statements. It extracts the module name and any aliases for the imported names, storing them in `self.import_mapping`. This helps in resolving names that are directly imported from a module, ensuring accurate call graph construction. It then continues the AST traversal.
            *   *Parameters:*
                - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
            *   *Returns:*
            *   **Usage:** This method accesses `self.import_mapping`. It is called by the `ast.NodeVisitor` traversal mechanism.
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
            *   *Description:* This method, overriding `ast.NodeVisitor.visit_ClassDef`, processes class definitions. It temporarily updates `self.current_class` to the name of the current class before traversing its body. This ensures that any methods defined within the class are correctly associated with their parent class. Upon exiting the class definition, it restores the previous class context.
            *   *Parameters:*
                - **node** (`ast.ClassDef`): The AST node representing a class definition.
            *   *Returns:*
            *   **Usage:** This method calls `self.generic_visit`. It is called by the `ast.NodeVisitor` traversal mechanism.
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method, overriding `ast.NodeVisitor.visit_FunctionDef`, processes function definitions (including methods). It constructs the full qualified name of the function, registers it in `self.local_defs` and adds it as a node to the NetworkX graph. It updates `self.current_function` for context, traverses the function's body, adds the function to `self.function_set`, and then restores the previous function context.
            *   *Parameters:*
                - **node** (`ast.FunctionDef`): The AST node representing a function definition.
            *   *Returns:*
            *   **Usage:** This method calls `self._make_full_name` and `self.generic_visit`. It also interacts with `self.local_defs`, `self.current_class`, `self.current_function`, `self.graph.add_node`, and `self.function_set`. It is called by the `ast.NodeVisitor` traversal mechanism and by `visit_AsyncFunctionDef`.
        *   **`visit_AsyncFunctionDef`**
            *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
            *   *Description:* This method, overriding `ast.NodeVisitor.visit_AsyncFunctionDef`, processes asynchronous function definitions. It delegates the actual processing to `visit_FunctionDef`, effectively treating async functions similarly to regular functions for the purpose of call graph construction. This simplifies the logic by reusing the existing function definition handling.
            *   *Parameters:*
                - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
            *   *Returns:*
            *   **Usage:** This method calls `self.visit_FunctionDef`. It is called by the `ast.NodeVisitor` traversal mechanism.
        *   **`visit_Call`**
            *   *Signature:* `def visit_Call(self, node)`
            *   *Description:* This method processes function and method call expressions within the AST. It identifies the current caller using `_current_caller`, extracts the callee's name components using `_recursive_call`, and resolves the full callee names using `_resolve_all_callee_names`. Finally, it records the call as an edge in the `self.edges` dictionary, mapping the caller to its callees. It ensures the caller is initialized in the edges dictionary before adding the callee.
            *   *Parameters:*
                - **node** (`ast.Call`): The AST node representing a function call.
            *   *Returns:*
            *   **Usage:** This method calls `self._current_caller`, `self._recursive_call`, `self._resolve_all_callee_names`, and `self.generic_visit`. It also interacts with `self.edges`. It is called by the `ast.NodeVisitor` traversal mechanism.
        *   **`visit_If`**
            *   *Signature:* `def visit_If(self, node)`
            *   *Description:* This method, overriding `ast.NodeVisitor.visit_If`, processes 'if' statements. It includes special handling for the 'if __name__ == "__main__":' block by temporarily setting `self.current_function` to '<main_block>'. This ensures that calls within this entry point are correctly attributed. For all other 'if' statements, it simply continues the generic AST traversal.
            *   *Parameters:*
                - **node** (`ast.If`): The AST node representing an 'if' statement.
            *   *Returns:*
            *   **Usage:** This method calls `self.generic_visit`. It also interacts with `self.current_function`. It is called by the `ast.NodeVisitor` traversal mechanism.
    *   **Usage:** This class is not explicitly instantiated by other components according to the provided context.

    ### File: `backend/converter.py`

    #### Function: `backend.converter.wrap_cdata`
    *   **Signature:** `def wrap_cdata(content)`
    *   **Description:** The `wrap_cdata` function takes a string `content` as input and encapsulates it within XML CDATA tags. It constructs a new string that starts with "<\![CDATA[\\n", inserts the provided content, and concludes with "\\n]]>". This process is designed to ensure that the content can be safely embedded within an XML document without being parsed as XML markup.
    *   **Parameters:**
        - **content** (`str`): The string content to be wrapped inside the CDATA block.
    *   **Returns:**
        - **wrapped_content** (`str`): A new string containing the original content enclosed within CDATA tags.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.converter.extract_output_content`
    *   **Signature:** `def extract_output_content(outputs, image_list)`
    *   **Description:** This function processes a list of output objects, typically from a notebook cell, to extract their content. It iterates through each output, handling different types such as display data, execute results, streams, and errors. For image data (PNG or JPEG), it decodes the Base64 string, stores the image data in a provided list, and inserts an XML placeholder into the extracted content. Textual content is appended directly, and error outputs are formatted into a string. The function ultimately returns a consolidated list of these extracted content snippets.
    *   **Parameters:**
        - **outputs** (`list`): A list of output objects, typically from a notebook cell execution, which can contain various data types like text, images, or errors.
        - **image_list** (`list`): A list that will be populated with dictionaries containing image data (mime_type and Base64 string) as they are extracted and processed.
    *   **Returns:**
        - **extracted_xml_snippets** (`List[str]`): A list of strings, where each string is either plain text, an XML placeholder for an image, or an error message, representing the extracted content from the outputs.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.converter.process_image`
    *   **Signature:** `def process_image(mime_type)`
    *   **Description:** This function attempts to process an image identified by its MIME type. It checks if the `mime_type` exists within an external `data` object. If found, it retrieves a base64 encoded string, removes newline characters, and then appends a dictionary containing the `mime_type` and cleaned base64 data to an external `image_list`. The function then returns an HTML-like placeholder string with an index and the MIME type. Error handling is included for issues during image decoding. If the `mime_type` is not present in `data`, the function returns `None`.
    *   **Parameters:**
        - **mime_type** (`str`): The MIME type of the image to be processed, such as 'image/png' or 'image/jpeg'.
    *   **Returns:**
        - **image_placeholder_tag** (`str`): An HTML-like string representing a placeholder for the processed image, including its index and MIME type, if successful.
        - **error_message** (`str`): An error message string indicating that the image could not be decoded if an exception occurs during processing.
        - **None**: Returns None if the specified mime_type is not found in the external 'data' object.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.
    *   **Error:** The function `process_image` uses undeclared variables `data` and `image_list`. Without their definition or context, the function's behavior and dependencies cannot be fully analyzed, as it relies on external state.

    #### Function: `backend.converter.convert_notebook_to_xml`
    *   **Signature:** `def convert_notebook_to_xml(file_content)`
    *   **Description:** This function converts the content of a Jupyter Notebook into an XML string, extracting any embedded images. It processes the input `file_content` by attempting to parse it as a notebook using `nbformat`. If the parsing fails due to a `NotJSONError`, it returns an error message. Otherwise, it iterates through markdown and code cells, wrapping their content in appropriate XML tags. Code cell outputs are also processed, potentially extracting images, and included as XML output cells. The function returns the accumulated XML string and a list of extracted images.
    *   **Parameters:**
        - **file_content** (`str`): The raw string content of a Jupyter Notebook file, expected to be in JSON format.
    *   **Returns:**
        - **xml_output** (`str`): A string containing the XML representation of the notebook content, or an error message if the input could not be parsed.
        - **extracted_images** (`list`): A list of extracted image data or references found within the notebook's output cells. This list will be empty if no images are extracted or if an error occurs.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.converter.process_repo_notebooks`
    *   **Signature:** `def process_repo_notebooks(repo_files)`
    *   **Description:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It filters the input list to find files ending with '.ipynb'. For each identified notebook, it logs the processing activity and then calls an external utility, 'convert_notebook_to_xml', to transform the notebook's content into an XML output and extract any associated images. The results, including the generated XML and images, are stored in a dictionary keyed by the notebook's path. Finally, this dictionary containing all processed notebook data is returned.
    *   **Parameters:**
        - **repo_files** (`List[object]`): A list of file-like objects from a repository. Each object is expected to have a 'path' attribute (string) indicating its file path and a 'content' attribute (string or bytes) representing its content.
    *   **Returns:**
        - **results** (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the string paths of the processed notebook files. Each value is a dictionary containing 'xml' (string, the XML representation of the notebook) and 'images' (Any, extracted images from the notebook).
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    ### File: `backend/getRepo.py`

    #### Class: `RepoFile`
    *   **Summary:** The RepoFile class represents a single file within a Git repository, providing a structured way to access its metadata and content. It implements lazy loading for the Git blob object, file content, and file size, ensuring that these resources are only retrieved and processed when explicitly requested. This design pattern optimizes performance by avoiding unnecessary data retrieval until needed, making it efficient for handling potentially large repositories or files.
    *   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
    *   **Dependencies:** The class has no explicit external dependencies listed in the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method initializes a RepoFile object by setting its file path and linking it to a specific Git commit tree. It also sets up internal attributes (`_blob`, `_content`, `_size`) to `None`, indicating that the file's blob, content, and size are to be loaded lazily upon first access.
        *   *Parameters:*
            - **file_path** (`str`): The path to the file within the Git repository.
            - **commit_tree** (`git.Tree`): The Git Tree object corresponding to the commit from which the file originates.
    *   **Methods:**
        *   **`blob`**
            *   *Signature:* `def blob(self)`
            *   *Description:* This property provides lazy loading for the Git blob object associated with the file. Upon first access, it checks if the `_blob` attribute is `None`. If so, it attempts to retrieve the corresponding blob from the `_tree` using the file's path. If the file is not found within the commit tree, a `FileNotFoundError` is raised, otherwise the retrieved blob is stored and returned.
            *   *Parameters:*
            *   *Returns:*
                - **None** (`git.Blob`): The Git blob object representing the file.
            *   **Usage:** Based on the provided context, this method does not explicitly call any other functions or methods. Based on the provided context, this method is not explicitly called by any other functions or methods.
        *   **`content`**
            *   *Signature:* `def content(self)`
            *   *Description:* This property provides lazy loading for the decoded content of the file. When accessed for the first time, it ensures that the Git blob object is loaded via the `blob` property. It then reads the data stream from the blob, decodes it using UTF-8 (with error ignoring), and stores the resulting string in the `_content` attribute for subsequent accesses.
            *   *Parameters:*
            *   *Returns:*
                - **None** (`str`): The decoded content of the file as a string.
            *   **Usage:** Based on the provided context, this method does not explicitly call any other functions or methods. Based on the provided context, this method is not explicitly called by any other functions or methods.
        *   **`size`**
            *   *Signature:* `def size(self)`
            *   *Description:* This property provides lazy loading for the size of the file in bytes. Upon its initial access, it ensures that the Git blob object is loaded by calling the `blob` property. It then retrieves the `size` attribute directly from the loaded blob object and stores it in `_size` for future requests, returning the integer value.
            *   *Parameters:*
            *   *Returns:*
                - **None** (`int`): The size of the file in bytes.
            *   **Usage:** Based on the provided context, this method does not explicitly call any other functions or methods. Based on the provided context, this method is not explicitly called by any other functions or methods.
        *   **`analyze_word_count`**
            *   *Signature:* `def analyze_word_count(self)`
            *   *Description:* This method serves as an example analysis function, designed to count the total number of words present within the file's content. It achieves this by accessing the `content` property, which lazily loads the file's text. The content string is then split into words using whitespace as a delimiter, and the length of the resulting list of words is returned.
            *   *Parameters:*
            *   *Returns:*
                - **None** (`int`): The total count of words in the file content.
            *   **Usage:** Based on the provided context, this method does not explicitly call any other functions or methods. Based on the provided context, this method is not explicitly called by any other functions or methods.
        *   **`__repr__`**
            *   *Signature:* `def __repr__(self)`
            *   *Description:* This special method defines the official string representation of the RepoFile object, primarily for debugging and logging purposes. It returns a concise, unambiguous string that includes the class name and the file's path, allowing developers to easily identify the object's state.
            *   *Parameters:*
            *   *Returns:*
                - **None** (`str`): A string representation of the RepoFile object, including its path.
            *   **Usage:** Based on the provided context, this method does not explicitly call any other functions or methods. Based on the provided context, this method is not explicitly called by any other functions or methods.
        *   **`to_dict`**
            *   *Signature:* `def to_dict(self, include_content=False)`
            *   *Description:* This method converts the RepoFile object into a dictionary representation, facilitating serialization or structured data exchange. It includes essential metadata such as the file's path, its base name, its size (lazy-loaded), and a fixed type 'file'. An optional `include_content` parameter allows for the file's content to be included in the dictionary if set to `True`.
            *   *Parameters:*
                - **include_content** (`bool`): If True, the file's content will be included in the dictionary.
            *   *Returns:*
                - **data** (`dict`): A dictionary containing the file's metadata and optionally its content.
            *   **Usage:** Based on the provided context, this method does not explicitly call any other functions or methods. Based on the provided context, this method is not explicitly called by any other functions or methods.

    #### Class: `GitRepository`
    *   **Summary:** The GitRepository class provides a robust mechanism for interacting with Git repositories. It handles the cloning of a remote repository into a temporary local directory upon instantiation and ensures proper cleanup of this directory when the object is no longer needed, especially when used as a context manager. It offers functionalities to list all files within the repository and to construct a hierarchical representation of the file structure, optionally including file contents.
    *   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
    *   **Dependencies:** "This class depends on `tempfile` for temporary directory management, `git.Repo` and `git.GitCommandError` from the GitPython library for Git operations, and `logging` for informational messages."
    *   **Constructor:**
        *   *Description:* The constructor initializes a GitRepository object by cloning the specified remote Git repository into a newly created temporary directory. It sets up various instance attributes such as the repository URL, the path to the temporary directory, the GitPython Repo object, and an empty list to store RepoFile objects. It also captures the latest commit and its tree for subsequent file operations. If cloning fails, it cleans up the temporary directory and raises a RuntimeError.
        *   *Parameters:*
            - **repo_url** (`str`): The URL of the Git repository to be cloned.
    *   **Methods:**
        *   **`get_all_files`**
            *   *Signature:* `def get_all_files(self)`
            *   *Description:* This method retrieves a list of all file paths present in the cloned Git repository using the `git ls-files` command. For each identified file path, it instantiates a `RepoFile` object, which presumably handles file-specific operations or data. These `RepoFile` instances are then stored in the `self.files` attribute and returned as a list.
            *   *Parameters:*
            *   *Returns:*
                - **files** (`list[RepoFile]`): A list of RepoFile instances, each representing a file in the repository.
            *   **Usage:** This method calls `self.repo.git.ls_files()` to list files and `RepoFile()` to create file objects. It is called by `get_file_tree` if the `self.files` attribute is empty.
        *   **`close`**
            *   *Signature:* `def close(self)`
            *   *Description:* This method is responsible for cleaning up the resources used by the GitRepository instance. Specifically, it deletes the temporary directory where the Git repository was cloned. It first checks if `self.temp_dir` is set to ensure there's a directory to remove, then prints a message indicating the deletion, and finally sets `self.temp_dir` to `None` to mark it as cleaned.
            *   *Parameters:*
            *   *Returns:*
            *   **Usage:** This method calls `print()` for logging purposes. It is called by the `__exit__` context manager method and by the `__init__` method in case of a cloning error.
        *   **`__enter__`**
            *   *Signature:* `def __enter__(self)`
            *   *Description:* This method implements the `__enter__` part of Python's context manager protocol. When a `GitRepository` object is used in a `with` statement, this method is automatically invoked. Its purpose is to return the instance of the object itself, allowing it to be bound to a variable in the `with` statement for use within the context block.
            *   *Parameters:*
            *   *Returns:*
                - **self** (`GitRepository`): The instance of the GitRepository class.
            *   **Usage:** This method does not explicitly call other methods or functions. It is implicitly called when the `GitRepository` object is used in a `with` statement.
        *   **`__exit__`**
            *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
            *   *Description:* This method implements the `__exit__` part of Python's context manager protocol. It is automatically called when the execution leaves the `with` statement block, regardless of whether an exception occurred. Its primary function is to ensure that the `close()` method is invoked to clean up the temporary repository directory, thereby releasing system resources.
            *   *Parameters:*
                - **exc_type** (`type`): The type of the exception that caused the exit, or None if no exception occurred.
                - **exc_val** (`Exception`): The exception instance that caused the exit, or None.
                - **exc_tb** (`traceback`): The traceback object associated with the exception, or None.
            *   *Returns:*
            *   **Usage:** This method calls `self.close()` to perform cleanup. It is implicitly called when exiting a `with` statement where the `GitRepository` object is used.
        *   **`get_file_tree`**
            *   *Signature:* `def get_file_tree(self, include_content=False)`
            *   *Description:* This method generates a hierarchical dictionary representation of the files within the repository, mimicking a file system tree structure. If the `self.files` list is not already populated, it first calls `get_all_files()` to retrieve them. It then iterates through these `RepoFile` objects, parsing their paths to build a nested dictionary where directories are represented by 'name', 'type', and 'children' keys, and files are added using their `to_dict` method, optionally including their content.
            *   *Parameters:*
                - **include_content** (`bool`): A flag indicating whether the content of each file should be included in its dictionary representation. Defaults to False.
            *   *Returns:*
                - **tree** (`dict`): A dictionary representing the file tree, with nested dictionaries for directories and file-specific data.
            *   **Usage:** This method calls `self.get_all_files()` if `self.files` is empty and `file_obj.to_dict()` for each file. This method is not explicitly called by other methods within the provided class definition.

    ### File: `backend/main.py`

    #### Function: `backend.main.create_savings_chart`
    *   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
    *   **Description:** This function generates a bar chart comparing two token counts, `json_tokens` and `toon_tokens`, and displays a calculated `savings_percent` in the title. It utilizes `matplotlib.pyplot` to visualize these values with distinct colors, adds labels and a grid, and annotates the bars with their respective integer values. The function sets a title indicating the token comparison and savings percentage. Finally, the generated chart is saved to a specified file path.
    *   **Parameters:**
        - **json_tokens** (`int`): The number of tokens associated with the JSON format.
        - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
        - **savings_percent** (`float`): The percentage of token savings to be displayed in the chart's title.
        - **output_path** (`str`): The file path where the generated bar chart will be saved.
    *   **Returns:**
    *   **Usage:** This function is not called by any other functions.

    #### Function: `backend.main.calculate_net_time`
    *   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
    *   **Description:** This function calculates the effective duration of a process by subtracting estimated sleep times, which are introduced to handle rate limits. It specifically applies this adjustment logic only if the `model_name` starts with "gemini-". If the model is not a 'gemini-' model, or if there are no items, the raw total duration or zero is returned, respectively. Otherwise, it calculates the number of batches, determines the total estimated sleep time based on a fixed sleep duration per batch, and then subtracts this from the total duration to yield the net time.
    *   **Parameters:**
        - **start_time** (`Any`): The starting timestamp or time value for the duration calculation.
        - **end_time** (`Any`): The ending timestamp or time value for the duration calculation.
        - **total_items** (`int`): The total number of items processed, used to determine the number of batches.
        - **batch_size** (`int`): The number of items processed per batch, used in conjunction with total_items to calculate batches.
        - **model_name** (`str`): The name of the model being used, which determines if rate-limit sleep time adjustments are applied.
    *   **Returns:**
        - **net_time** (`float`): The calculated net duration, after subtracting estimated sleep times for rate limits, or the total duration if no adjustments are made. Returns 0 if total_items is 0 or if the net time calculation results in a negative value.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.main.main_workflow`
    *   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None)`
    *   **Description:** This function orchestrates a comprehensive workflow for analyzing a GitHub repository and generating a detailed report using multiple Language Model (LLM) stages. It begins by extracting API keys and model configurations from the input, then clones a specified GitHub repository. It proceeds to extract basic project information, construct a file tree, and perform a relationship analysis. An Abstract Syntax Tree (AST) schema is generated and enriched with the relationship data. The function then prepares and dispatches analysis tasks to a 'Helper LLM' for individual functions and classes, collecting their structured outputs. Finally, it consolidates all gathered information and the Helper LLM results into a structured input for a 'Main LLM', which generates the final project report. The process includes error handling, status updates, token evaluation, and saving the final report along with performance metrics and a token savings chart.
    *   **Parameters:**
        - **input** (`str`): The user input, expected to contain a GitHub repository URL.
        - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs ('scadsllm_base_url', 'ollama').
        - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used.
        - **status_callback** (`None`): An optional callback function used to provide progress updates during the workflow execution.
    *   **Returns:**
        - **result** (`dict`): A dictionary containing the 'report' (the final generated report as a string) and 'metrics' (a dictionary of performance and token usage statistics).
    *   **Usage:** This function is not explicitly called by other functions in the provided context.

    #### Function: `backend.main.update_status`
    *   **Signature:** `def update_status(msg)`
    *   **Description:** This function, `update_status`, is designed to handle status updates within the system. It accepts a message as input. The function first checks if a `status_callback` function is available in its scope. If `status_callback` exists, it is invoked with the provided message. Regardless of whether a callback is present, the function proceeds to log the message at the INFO level using the `logging` module.
    *   **Parameters:**
        - **msg** (`str`): The message string to be used for the status update and logging.
    *   **Returns:**
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.main.notebook_workflow`
    *   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
    *   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks from a given GitHub repository. It clones the repository, processes notebook files into an XML structure, and extracts basic project information. The function then iterates through each notebook, generating a detailed report for each using a specified Large Language Model (LLM). It handles various LLM API keys and models, constructs LLM payloads, provides status updates via a callback, and logs errors. Finally, it concatenates all individual reports into a single markdown file and returns the final report along with performance metrics.
    *   **Parameters:**
        - **input** (`str`): The input string, expected to contain a GitHub repository URL from which notebooks will be analyzed.
        - **api_keys** (`dict`): A dictionary containing API keys for various Large Language Model (LLM) services, such as 'gpt', 'gemini', 'scadsllm', or 'ollama'.
        - **model** (`str`): The name of the LLM model to be used for generating reports (e.g., 'gpt-4', 'gemini-pro').
        - **status_callback** (`callable | None`): An optional callback function that receives status messages during the workflow execution for real-time updates.
    *   **Returns:**
        - **report** (`str`): The concatenated final report generated from all processed notebooks, formatted in markdown.
        - **metrics** (`dict`): A dictionary containing performance metrics for the workflow, including 'main_time', 'total_time', and 'main_model'.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `backend.main.gemini_payload`
    *   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
    *   **Description:** This function `gemini_payload` is responsible for constructing a multi-modal payload suitable for the Gemini API. It first serializes `basic_info` and `nb_path` into an introductory JSON string. The core logic involves parsing the `xml_content` to identify and replace `<IMAGE_PLACEHOLDER>` tags with actual image data. It uses regular expressions to locate these placeholders, extracting image indices and MIME types. Corresponding image data from the `images` list is then base64 encoded and formatted as image URLs. The function returns a list of dictionaries, interleaving text segments from the XML with these formatted image URLs, ready for a Gemini API request.
    *   **Parameters:**
        - **basic_info** (`Dict`): A dictionary containing general information about the project or context, which will be serialized into an introductory JSON string.
        - **nb_path** (`str`): The file path of the current notebook, included in the introductory context information.
        - **xml_content** (`str`): The XML string representing the notebook's structure, potentially containing `<IMAGE_PLACEHOLDER>` tags.
        - **images** (`List[Dict]`): A list of dictionaries, where each dictionary contains image data (e.g., base64 string) and metadata, indexed to match placeholders in `xml_content`.
    *   **Returns:**
        - **payload_content** (`List[Dict]`): A list of dictionaries, each representing a content part for the Gemini API. Each dictionary specifies either 'text' content or an 'image_url' with base64 encoded image data.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    ### File: `backend/relationship_analyzer.py`

    #### Function: `backend.relationship_analyzer.path_to_module`
    *   **Signature:** `def path_to_module(filepath, project_root)`
    *   **Description:** This function transforms a given file system path into its corresponding Python module path. It first computes the relative path of the file from the specified project root, handling potential `ValueError` by using the base filename. It then removes the '.py' extension if present and replaces directory separators with dots. Finally, it removes a trailing '.__init__' to yield the canonical module path.
    *   **Parameters:**
        - **filepath** (`str`): The file system path to be converted into a module path.
        - **project_root** (`str`): The root directory of the project, used to determine the relative path of the file.
    *   **Returns:**
        - **module_path** (`str`): The Python module path derived from the input filepath.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Class: `ProjectAnalyzer`
    *   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to build a comprehensive call graph and identify relationships between functions, methods, and classes. It systematically traverses the project directory, parses Python files into Abstract Syntax Trees, collects definitions of callable entities, and then resolves calls between these entities. The class provides methods to initiate the analysis and retrieve the raw outgoing and incoming call relationships, making it a core component for understanding code structure and dependencies within a project.
    *   **Instantiation:** This class is not explicitly instantiated by any other functions or methods in the provided context.
    *   **Dependencies:** "This class depends on os for file system operations, ast for parsing Python code, logging for error reporting, and collections.defaultdict for managing graph data structures. It also implicitly depends on path_to_module and CallResolverVisitor which are not defined in the provided source but are used."
    *   **Constructor:**
        *   *Description:* The constructor initializes the ProjectAnalyzer instance by setting up the project's root directory, various data structures to store definitions and call graphs, and a set of directories to ignore during file traversal. It converts the provided project_root to an absolute path and initializes dictionaries for definitions, call graphs, file ASTs, and a set of common directories to exclude from analysis.
        *   *Parameters:*
            - **project_root** (`str`): The root directory of the project to be analyzed.
    *   **Methods:**
        *   **`analyze`**
            *   *Signature:* `def analyze(self)`
            *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project root, excluding ignored directories. Then, it iterates through these files twice: once to collect all function, method, and class definitions, and a second time to resolve calls between these definitions. Finally, it clears the stored ASTs to free memory and returns the populated call graph.
            *   *Parameters:*
            *   *Returns:*
                - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee identifiers and values are lists of caller information.
            *   **Usage:** This method is not explicitly called by any other functions or methods in the provided context.
        *   **`get_raw_relationships`**
            *   *Signature:* `def get_raw_relationships(self)`
            *   *Description:* This method processes the internal call_graph to generate structured outgoing and incoming relationship dictionaries. It iterates through the call_graph to identify caller-callee pairs. For each valid pair, it populates 'outgoing' with calls made from a caller_id and 'incoming' with calls received by a callee_id. The final output sorts and converts the sets of relationships into lists for consistent representation.
            *   *Parameters:*
            *   *Returns:*
                - **relationships** (`dict`): A dictionary containing two keys: 'outgoing' (mapping caller IDs to a sorted list of callee IDs) and 'incoming' (mapping callee IDs to a sorted list of caller IDs).
            *   **Usage:** This method is not explicitly called by any other functions or methods in the provided context.
        *   **`_find_py_files`**
            *   *Signature:* `def _find_py_files(self)`
            *   *Description:* This private helper method is responsible for recursively traversing the project_root to locate all Python files. It uses `os.walk` to navigate the directory structure, filtering out directories specified in `self.ignore_dirs`. For each directory, it updates the 'dirs' list in place to skip ignored directories, and then checks if files end with '.py' before adding their full paths to a list.
            *   *Parameters:*
            *   *Returns:*
                - **py_files** (`list[str]`): A list of absolute file paths to all Python files found within the project, excluding ignored directories.
            *   **Usage:** This method calls `os.walk` and `os.path.join`. It is called by `analyze`.
        *   **`_collect_definitions`**
            *   *Signature:* `def _collect_definitions(self, filepath)`
            *   *Description:* This private method parses a given Python file to identify and store all function, method, and class definitions. It reads the file, parses its source code into an Abstract Syntax Tree (AST) using `ast.parse`, and stores the AST in `self.file_asts`. It then walks the AST to find `FunctionDef` and `ClassDef` nodes, determines their fully qualified path names, and stores their file, line number, and type ('function', 'method', 'class') in `self.definitions`. Error handling is included for file operations and AST parsing.
            *   *Parameters:*
                - **filepath** (`str`): The path to the Python file to be analyzed.
            *   *Returns:*
            *   **Usage:** This method calls `open`, `ast.parse`, `path_to_module`, `ast.walk`, `_get_parent`, and `logging.error`. It is called by `analyze`.
        *   **`_get_parent`**
            *   *Signature:* `def _get_parent(self, tree, node)`
            *   *Description:* This private helper method is designed to find the direct parent AST node of a given child node within a larger AST. It iterates through all nodes in the provided 'tree' and, for each node, checks its children. If a child matches the 'node' parameter, the current parent node is returned. If no parent is found after traversing the entire tree, it returns None.
            *   *Parameters:*
                - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
                - **node** (`ast.AST`): The child node for which to find the parent.
            *   *Returns:*
                - **parent_node** (`ast.AST | None`): The parent AST node if found, otherwise None.
            *   **Usage:** This method calls `ast.walk` and `ast.iter_child_nodes`. It is called by `_collect_definitions`.
        *   **`_resolve_calls`**
            *   *Signature:* `def _resolve_calls(self, filepath)`
            *   *Description:* This private method processes a file's AST to identify and resolve function and method calls. It retrieves the AST for the given 'filepath' from `self.file_asts`. It then instantiates a `CallResolverVisitor` with the file context, project root, and collected definitions. The visitor traverses the AST to find calls, and the identified calls are then extended into the `self.call_graph` structure. Error logging is implemented for issues during call resolution.
            *   *Parameters:*
                - **filepath** (`str`): The path to the Python file whose calls need to be resolved.
            *   *Returns:*
            *   **Usage:** This method calls `CallResolverVisitor`, `resolver.visit`, and `logging.error`. It is called by `analyze`.

    #### Class: `CallResolverVisitor`
    *   **Summary:** The CallResolverVisitor class is an AST NodeVisitor designed to traverse Python abstract syntax trees to identify and resolve function and method calls. It maintains a scope for imported modules and tracks instance types to accurately determine the fully qualified names of call targets. The visitor records detailed information about each call, including the caller, file, line number, and caller type, facilitating a comprehensive analysis of inter-component relationships within a codebase.
    *   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* The constructor initializes the visitor with the file path of the code being analyzed, the project's root directory, and a dictionary of known definitions. It sets up internal state variables for tracking module paths, local scopes, instance types, current class and caller names, and a defaultdict to store identified calls.
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file currently being processed by the visitor.
            - **project_root** (`str`): The root directory of the entire project, used to derive module paths.
            - **definitions** (`dict`): A dictionary containing all known qualified definitions (functions, classes, methods) within the project, used for validating call targets.
    *   **Methods:**
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
            *   *Description:* This method is invoked when the AST visitor encounters a class definition. It temporarily updates the `current_class_name` attribute to reflect the class being visited, allowing subsequent nested function definitions to correctly form their fully qualified names. After processing the class's children, it restores the previous class name.
            *   *Parameters:*
                - **node** (`ast.ClassDef`): The AST node representing the class definition.
            *   *Returns:*
            *   **Usage:** This method does not explicitly call any other functions or methods according to the provided context. It is not explicitly called by any other functions or methods according to the provided context.
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method is called when the AST visitor encounters a function definition. It constructs the full qualified identifier for the function, considering whether it's a method within a class or a top-level function. It then updates `current_caller_name` to this identifier for the duration of the function's traversal, restoring the previous caller name afterwards.
            *   *Parameters:*
                - **node** (`ast.FunctionDef`): The AST node representing the function definition.
            *   *Returns:*
            *   **Usage:** This method does not explicitly call any other functions or methods according to the provided context. It is not explicitly called by any other functions or methods according to the provided context.
        *   **`visit_Call`**
            *   *Signature:* `def visit_Call(self, node)`
            *   *Description:* This method processes function and method call expressions within the AST. It attempts to resolve the fully qualified name of the callee using a helper method. If the callee's qualified name is found within the known project definitions, it records the call, including the file, line number, the current caller's qualified name, and the type of the caller (module, local function, method, or function).
            *   *Parameters:*
                - **node** (`ast.Call`): The AST node representing the function or method call.
            *   *Returns:*
            *   **Usage:** This method does not explicitly call any other functions or methods according to the provided context. It is not explicitly called by any other functions or methods according to the provided context.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method handles `import` statements, such as `import module_name` or `import module_name as alias`. It populates the `self.scope` dictionary, mapping the imported name (or alias) to its original module name, which aids in resolving qualified names later.
            *   *Parameters:*
                - **node** (`ast.Import`): The AST node representing an import statement.
            *   *Returns:*
            *   **Usage:** This method does not explicitly call any other functions or methods according to the provided context. It is not explicitly called by any other functions or methods according to the provided context.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method processes `from ... import ...` statements. It calculates the full module path for the imported names, correctly handling relative imports based on the `node.level`. It then adds these resolved qualified names to the `self.scope` dictionary for subsequent lookup.
            *   *Parameters:*
                - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
            *   *Returns:*
            *   **Usage:** This method does not explicitly call any other functions or methods according to the provided context. It is not explicitly called by any other functions or methods according to the provided context.
        *   **`visit_Assign`**
            *   *Signature:* `def visit_Assign(self, node)`
            *   *Description:* This method inspects assignment statements to identify class instantiations. If an assignment involves calling a constructor (e.g., `variable = ClassName()`), it resolves the qualified name of the class and stores it in `self.instance_types`, mapping the assigned variable's name to its class's qualified name. This helps in resolving method calls on instances.
            *   *Parameters:*
                - **node** (`ast.Assign`): The AST node representing an assignment statement.
            *   *Returns:*
            *   **Usage:** This method does not explicitly call any other functions or methods according to the provided context. It is not explicitly called by any other functions or methods according to the provided context.
        *   **`_resolve_call_qname`**
            *   *Signature:* `def _resolve_call_qname(self, func_node)`
            *   *Description:* This private helper method attempts to determine the fully qualified name (QName) of a function or method being called. It handles direct name calls, resolving them against the current scope or local module definitions. It also resolves attribute calls (e.g., `instance.method` or `module.function`) by checking `instance_types` for object instances or `scope` for imported modules.
            *   *Parameters:*
                - **func_node** (`ast.expr`): The AST node representing the function or method being called, typically an `ast.Name` or `ast.Attribute` node.
            *   *Returns:*
                - **qualified_name** (`str | None`): The fully qualified name of the called function or method if resolvable, otherwise None.
            *   **Usage:** This method does not explicitly call any other functions or methods according to the provided context. It is not explicitly called by any other functions or methods according to the provided context.
    *   **Usage:** This class is not explicitly instantiated by other components within the provided context.

    ### File: `schemas/types.py`

    #### Class: `ParameterDescription`
    *   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to encapsulate the essential details of a function parameter. It provides a structured format for its name, type, and a descriptive text, ensuring that parameter information is consistently represented and validated. This class serves as a fundamental data structure for describing function signatures within a broader system.
    *   **Instantiation:** The instantiation points for this class are not provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes the instance attributes `name`, `type`, and `description` based on the provided arguments, leveraging Pydantic's validation capabilities to ensure data integrity upon instantiation.
        *   *Parameters:*
            - **name** (`str`): The name of the parameter being described.
            - **type** (`str`): The data type of the parameter, typically as a string representation.
            - **description** (`str`): A textual explanation of the parameter's purpose or role.
    *   **Usage:** The instantiation points for this class are not provided in the context.

    #### Class: `ReturnDescription`
    *   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to provide a standardized structure for describing the return value of a function. It encapsulates three essential pieces of information: the name of the return value, its type, and a description explaining its purpose or content. This model is likely used within a larger system to generate documentation or validate function signatures.
    *   **Instantiation:** The context provided does not specify where this class is instantiated.
    *   **Dependencies:** "This class depends on `pydantic.BaseModel` for its structural definition and validation capabilities. No other explicit functional dependencies are identified."
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, implicitly generates an `__init__` method. This constructor is used to initialize instances of `ReturnDescription` by providing values for its `name`, `type`, and `description` fields, ensuring data validation according to their specified types.
        *   *Parameters:*
            - **name** (`str`): The name or identifier of the return value.
            - **type** (`str`): The data type of the return value.
            - **description** (`str`): A textual description of what the return value represents or its purpose.
    *   **Usage:** The context provided does not specify where this class is instantiated.

    #### Class: `UsageContext`
    *   **Summary:** The UsageContext class is a Pydantic BaseModel designed to describe the calling context of a function or method. It serves as a structured data container, holding two string fields: 'calls' to summarize what the entity calls, and 'called_by' to summarize where the entity is utilized. This class is primarily used for metadata aggregation within a larger system.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `UsageContext` is implicitly generated by Pydantic's BaseModel. It initializes an instance of `UsageContext` by accepting `calls` and `called_by` as string arguments, validating them according to their type hints to ensure data integrity.
        *   *Parameters:*
            - **calls** (`str`): A string describing the functions, methods, or external entities that this context's subject calls.
            - **called_by** (`str`): A string describing the functions, methods, or external entities that call this context's subject.
    *   **Usage:** The provided context does not specify where this class is instantiated.

    #### Class: `FunctionDescription`
    *   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It provides a structured format for detailing a function's high-level purpose, its input parameters, its expected return values, and its operational context within a larger system. This model serves as a standardized data structure for representing and exchanging function analysis results, facilitating automated documentation and understanding.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
    *   **Constructor:**
        *   *Description:* As a Pydantic BaseModel, the `__init__` method for `FunctionDescription` is implicitly generated by Pydantic. It initializes an instance of the class by accepting values for its defined fields: `overall`, `parameters`, `returns`, and `usage_context`, ensuring type validation and data integrity upon instantiation.
        *   *Parameters:*
            - **overall** (`str`): A high-level summary describing the function's primary purpose and functionality.
            - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing an input parameter of the function, including its name, type, and description.
            - **returns** (`List[ReturnDescription]`): A list of `ReturnDescription` objects, each detailing a possible return value of the function, including its type and description.
            - **usage_context** (`UsageContext`): An object containing information about where the function is called and what other functions or methods it calls internally.
    *   **Usage:** The specific locations where this class is instantiated are not provided in the context.

    #### Class: `FunctionAnalysis`
    *   **Summary:** The FunctionAnalysis class serves as the main Pydantic model for structuring the comprehensive analysis of a single function. It encapsulates the function's unique identifier, a detailed `FunctionDescription` object (an external type), and an optional `error` field for reporting issues during analysis. This model is fundamental for standardizing the output of function analysis within a larger system, ensuring a consistent data structure for function-level insights.
    *   **Instantiation:** The instantiation points for this class are not provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* This class does not explicitly define an `__init__` method. As a Pydantic BaseModel, its constructor is implicitly generated to accept and validate values for its defined fields: `identifier`, `description`, and `error`.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifying the function being analyzed.
            - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose, parameters, return values, and usage context.
            - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the analysis of the function. Defaults to `None`.
    *   **Usage:** The instantiation points for this class are not provided in the context.

    #### Class: `ConstructorDescription`
    *   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to provide a structured representation of a Python class's `__init__` method. It encapsulates a textual summary of the constructor's behavior and a list of detailed descriptions for each of its parameters. This model is crucial for generating comprehensive documentation or for static analysis of class constructors.
    *   **Instantiation:** No specific instantiation points for this class were provided in the input context.
    *   **Dependencies:** "This class depends on `pydantic.BaseModel` for its data structure and validation, and `typing.List` for type hinting. It also implicitly depends on the `ParameterDescription` class, which defines the structure of individual parameters."
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ConstructorDescription` is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting and validating the `description` string and a list of `ParameterDescription` objects, assigning them to the corresponding instance attributes.
        *   *Parameters:*
            - **description** (`str`): A string summary detailing the functionality and purpose of the constructor.
            - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each providing details about a specific parameter of the constructor.
    *   **Usage:** No specific instantiation points for this class were provided in the input context.

    #### Class: `ClassContext`
    *   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's operational context. It specifically tracks external dependencies and the locations or components responsible for its instantiation. This model provides a structured way to describe how a class interacts with its environment and where it is utilized within a larger system.
    *   **Instantiation:** No specific instantiation points are listed in the provided context for this class.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ClassContext` is implicitly generated by Pydantic's BaseModel. It initializes an instance with two string attributes: `dependencies` and `instantiated_by`. These attributes are directly mapped from the constructor's arguments, setting up the class's contextual description upon creation.
        *   *Parameters:*
            - **dependencies** (`str`): A string describing the external dependencies required by the class.
            - **instantiated_by** (`str`): A string describing the primary points or modules where this class is instantiated.
    *   **Usage:** No specific instantiation points are listed in the provided context for this class.

    #### Class: `ClassDescription`
    *   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of another Python class. It acts as a structured data container, holding a high-level overall description, a detailed `init_method` analysis, a list of `methods` analyses, and `usage_context` information regarding dependencies and instantiation points. This model is crucial for standardizing the output of class analysis within a larger system.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** "This class does not explicitly declare external functional dependencies within its source code, relying on its Pydantic BaseModel inheritance and type hints."
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, implicitly generates its constructor. The constructor is responsible for initializing instances of `ClassDescription` by validating and assigning values to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`.
        *   *Parameters:*
            - **overall** (`str`): A high-level summary of the class's purpose and functionality.
            - **init_method** (`ConstructorDescription`): An object containing the description and parameters of the class's constructor.
            - **methods** (`List[FunctionAnalysis]`): A list of detailed analyses for each method defined within the class.
            - **usage_context** (`ClassContext`): An object describing the class's external dependencies and where it is instantiated.
    *   **Usage:** The provided context does not specify where this class is instantiated.

    #### Class: `ClassAnalysis`
    *   **Summary:** The `ClassAnalysis` class serves as the main Pydantic model for structuring the comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed `ClassDescription` object containing its constructor and method analyses, and an optional error field. This model is designed to provide a standardized, machine-readable format for representing the output of a class analysis process.
    *   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* This class does not explicitly define an `__init__` method. Pydantic's `BaseModel` handles the initialization of its fields based on the provided type hints, automatically creating attributes for `identifier`, `description`, and `error` upon instantiation.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifying the class being analyzed.
            - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
            - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the analysis of the class. Defaults to `None`.
    *   **Usage:** The specific points of instantiation for this class are not provided in the current context.

    #### Class: `CallInfo`
    *   **Summary:** The CallInfo class is a Pydantic BaseModel designed to encapsulate details about a specific code call event. It serves as a structured data container for tracking where a function, method, or module is called or instantiated. This class helps in analyzing code relationships by providing a standardized format for call information, including the file path, the name of the calling entity, the type of call, and the line number.
    *   **Instantiation:** The instantiation points for this class are not specified in the provided context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `CallInfo` is implicitly generated by Pydantic's BaseModel. It initializes an instance of `CallInfo` by validating and assigning the provided `file`, `function`, `mode`, and `line` attributes based on their type annotations.
        *   *Parameters:*
            - **file** (`str`): The file path where the call event occurred.
            - **function** (`str`): The name of the calling function or method.
            - **mode** (`str`): The type of call, e.g., 'method', 'function', 'module'.
            - **line** (`int`): The line number in the file where the call event occurred.
    *   **Usage:** The instantiation points for this class are not specified in the provided context.

    #### Class: `FunctionContextInput`
    *   **Summary:** The FunctionContextInput class serves as a Pydantic data model designed to encapsulate the contextual information surrounding a function's interactions. It defines a structured schema for tracking which other functions or methods a given function 'calls' and by which other functions or methods it is 'called_by'. This model is crucial for providing a clear, machine-readable representation of a function's dependencies and usage within a larger system, facilitating analysis and documentation.
    *   **Instantiation:** The specific points of instantiation for this class are not provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* This class, inheriting from Pydantic's BaseModel, implicitly initializes its attributes 'calls' and 'called_by' upon instantiation. Pydantic handles validation and assignment of these fields based on the provided input data, ensuring type correctness for the list of called entities and the list of CallInfo objects for callers.
        *   *Parameters:*
            - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this function calls.
            - **called_by** (`List[CallInfo]`): A list of CallInfo objects representing other functions or methods that call this function.
    *   **Usage:** The specific points of instantiation for this class are not provided in the context.

    #### Class: `FunctionAnalysisInput`
    *   **Summary:** This class serves as a Pydantic model defining the precise structure and validation rules for input data required to initiate a function analysis process. It encapsulates all necessary information, including the function's identifier, its source code, associated import statements, and contextual details, ensuring that any incoming data conforms to the expected schema before processing. This model is crucial for robust data handling in a larger AI system focused on code analysis.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `FunctionAnalysisInput` is implicitly provided by Pydantic's BaseModel. It initializes an instance of `FunctionAnalysisInput` by validating and assigning the provided `mode`, `identifier`, `source_code`, `imports`, and `context` attributes based on their defined types and constraints.
        *   *Parameters:*
            - **mode** (`Literal["function_analysis"]`): Specifies the mode of operation, which must be 'function_analysis'.
            - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
            - **source_code** (`str`): The raw source code of the function to be analyzed.
            - **imports** (`List[str]`): A list of import statements relevant to the function's source code.
            - **context** (`FunctionContextInput`): Additional contextual information required for the function analysis.
    *   **Usage:** The provided context does not specify where this class is instantiated.

    #### Class: `MethodContextInput`
    *   **Summary:** The MethodContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information for a method. It defines fields such as the method's unique identifier, a list of other functions or methods it calls, a list of entities that call it, its arguments, and its docstring. This class serves as a data structure to standardize and transfer method-specific metadata within a larger analysis or documentation generation system.
    *   **Instantiation:** This class is not explicitly shown to be instantiated by other components within the provided context.
    *   **Dependencies:** This class does not explicitly depend on other components within the provided context.
    *   **Constructor:**
        *   *Description:* The constructor for `MethodContextInput` is automatically generated by Pydantic. It initializes an instance of the class by validating and assigning values to its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`. This ensures that all method context data conforms to the specified types upon instantiation.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifier for the method.
            - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls.
            - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects representing other functions or methods that call this method.
            - **args** (`List[str]`): A list of string representations of the arguments accepted by this method.
            - **docstring** (`Optional[str]`): The docstring of the method, if available; otherwise, it can be null.
    *   **Usage:** This class is not explicitly shown to be instantiated by other components within the provided context.

    #### Class: `ClassContextInput`
    *   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured context information for the analysis of a Python class. It defines the data structure for dependencies, instantiation points, and method-specific contexts. This model serves as an input schema for processes that require detailed contextual data about a class.
    *   **Instantiation:** There is no explicit information provided about where this class is instantiated.
    *   **Dependencies:** This class does not explicitly declare external functional dependencies within its definition.
    *   **Constructor:**
        *   *Description:* This class does not define an explicit `__init__` method. Pydantic's `BaseModel` handles the initialization of its fields based on the provided type hints, automatically creating attributes for `dependencies`, `instantiated_by`, and `method_context` upon instantiation.
        *   *Parameters:*
            - **dependencies** (`List[str]`): A list of strings describing the external dependencies required by the class.
            - **instantiated_by** (`List[CallInfo]`): A list of `CallInfo` objects describing the primary points or modules where this class is instantiated.
            - **method_context** (`List[MethodContextInput]`): A list of `MethodContextInput` objects, each detailing the context of a specific method within the class.
    *   **Usage:** There is no explicit information provided about where this class is instantiated.

    #### Class: `ClassAnalysisInput`
    *   **Summary:** The ClassAnalysisInput class serves as a Pydantic data model, defining the precise structure and validation rules for input data required to initiate a class analysis process. It encapsulates all necessary information, including the class's identifier, its full source code, associated import statements, and contextual details, ensuring that any incoming data conforms to the expected schema before processing. This model is crucial for robust data handling in a larger AI system focused on code analysis.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The `ClassAnalysisInput` class inherits from `pydantic.BaseModel` and therefore does not define an explicit `__init__` method. Pydantic automatically generates a constructor that accepts keyword arguments corresponding to the class's defined fields, enabling robust data validation and parsing upon instantiation.
        *   *Parameters:*
            - **mode** (`Literal["class_analysis"]`): A literal string indicating the type of analysis to be performed, which must be 'class_analysis'.
            - **identifier** (`str`): The unique name or identifier of the Python class that is the subject of the analysis.
            - **source_code** (`str`): The complete raw source code string of the class definition to be analyzed.
            - **imports** (`List[str]`): A list of strings, each representing an import statement relevant to the source file where the class is defined.
            - **context** (`ClassContextInput`): An object containing additional contextual information pertinent to the class, such as its dependencies and where it is instantiated.
    *   **Usage:** The provided context does not specify where this class is instantiated.

    ### File: `database/db.py`

    #### Function: `database.db.encrypt_text`
    *   **Signature:** `def encrypt_text(text: str) -> str`
    *   **Description:** This function, `encrypt_text`, is responsible for encrypting a given string using an external `cipher_suite` object. It first performs a validation check: if the input `text` is empty or if the `cipher_suite` is not initialized, the function returns the original text without any modification. If both conditions are met, the function proceeds to strip any leading or trailing whitespace from the input string. The cleaned string is then encoded into bytes, encrypted by the `cipher_suite`, and finally decoded back into a string before being returned.
    *   **Parameters:**
        - **text** (`str`): The string value to be encrypted.
    *   **Returns:**
        - **encrypted_text** (`str`): The encrypted version of the input string, or the original string if encryption is skipped due to empty text or uninitialized cipher_suite.
    *   **Usage:** This function is called by no other functions.

    #### Function: `database.db.decrypt_text`
    *   **Signature:** `def decrypt_text(text: str) -> str`
    *   **Description:** This function attempts to decrypt a given text string using a globally available `cipher_suite` object. It first checks if the input text or `cipher_suite` is empty; if either is, it returns the original text without modification. If both are present, it proceeds to strip whitespace from the text, encode it, decrypt it using `cipher_suite.decrypt`, and then decode the result back into a string. The function includes error handling, returning the original text if any exception occurs during the decryption process.
    *   **Parameters:**
        - **text** (`str`): The string value to be decrypted.
    *   **Returns:**
        - **decrypted_text** (`str`): The decrypted string, or the original string if decryption is not performed (due to empty input or cipher_suite) or if an error occurs during decryption.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.insert_user`
    *   **Signature:** `def insert_user(username: str, name: str, password: str)`
    *   **Description:** This function is designed to create a new user record and persist it into a database collection. It accepts a username, a display name, and a plain-text password as input. Before storing, the password is securely hashed using `stauth.Hasher.hash`, and several API key fields are initialized as empty strings. The constructed user dictionary is then inserted into the `dbusers` collection. The function concludes by returning the unique identifier assigned to the newly created user document.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user, which also serves as the document's primary key.
        - **name** (`str`): The display name of the user.
        - **password** (`str`): The plain-text password provided by the user, which will be hashed before storage.
    *   **Returns:**
        - **inserted_id** (`string`): The unique identifier (e.g., MongoDB ObjectId) of the newly inserted user document.
    *   **Usage:** This function is called by no other functions.

    #### Function: `database.db.fetch_all_users`
    *   **Signature:** `def fetch_all_users()`
    *   **Description:** The `fetch_all_users` function is responsible for retrieving all user records from a database collection. It executes a `find()` operation on the `dbusers` object, which is presumed to be a database collection. The results obtained from this query are then cast into a standard Python list before being returned by the function.
    *   **Parameters:**
    *   *Returns:*
        - **users** (`list`): A list containing all user records retrieved from the database collection.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.fetch_user`
    *   **Signature:** `def fetch_user(username: str)`
    *   **Description:** This function is designed to retrieve a single user record from a database. It takes a username as input and uses it to query a collection named `dbusers`. The `find_one` method is employed to locate a document where the `_id` field matches the provided username. The function then returns the found user document or `None` if no matching user is located.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user to be fetched, which is used to match the `_id` field in the database.
    *   *Returns:*
        - **user_document** (`dict | None`): A dictionary representing the user's document if a match is found, otherwise `None`.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.update_user_name`
    *   **Signature:** `def update_user_name(username: str, new_name: str)`
    *   **Description:** This function updates the 'name' field of a user document in the 'dbusers' collection. It identifies the user by their `username`, which is mapped to the MongoDB `_id` field. The function sets the 'name' field to the provided `new_name` using a MongoDB `update_one` operation. It returns the count of documents that were successfully modified.
    *   **Parameters:**
        - **username** (`str`): The unique identifier of the user, corresponding to the MongoDB `_id` field.
        - **new_name** (`str`): The new name to set for the user.
    *   *Returns:*
        - **modified_count** (`int`): The number of documents that were modified by the update operation.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.update_gemini_key`
    *   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
    *   **Description:** This function is responsible for updating a user's Gemini API key within the database. It accepts a username and the new Gemini API key as input. The provided API key is first stripped of leading/trailing whitespace and then encrypted before storage. The function then performs an update operation on the `dbusers` collection, setting the `gemini_api_key` field for the specified user with the encrypted value. It returns an integer indicating the number of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
        - **gemini_api_key** (`str`): The new Gemini API key provided by the user, which will be encrypted and stored.
    *   *Returns:*
        - **modified_count** (`int`): The number of documents that were modified in the database by the update operation. Typically 0 or 1.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.update_gpt_key`
    *   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
    *   **Description:** This function updates a user's GPT API key in the database. It first encrypts the provided API key, ensuring any leading or trailing whitespace is removed. The encrypted key is then stored in the "gpt_api_key" field for the specified username in the "dbusers" collection. The function returns the number of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose GPT API key is to be updated.
        - **gpt_api_key** (`str`): The new GPT API key to be encrypted and stored for the user.
    *   *Returns:*
        - **modified_count** (`int`): The number of documents modified by the update operation, typically 1 if the user exists and the key was updated, or 0 otherwise.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.update_ollama_url`
    *   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
    *   **Description:** This function updates the Ollama base URL for a specific user within the database. It takes a username and a new Ollama base URL as input. The provided URL is first stripped of leading/trailing whitespace before being used to update the corresponding user's record. The function then returns the count of documents that were successfully modified.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be updated.
        - **ollama_base_url** (`str`): The new base URL for Ollama, which will be stripped of whitespace before being stored.
    *   *Returns:*
        - **modified_count** (`int`): The number of documents that were modified by the update operation.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `database.db.update_opensrc_key`
    *   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
    *   **Description:** This function, `update_opensrc_key`, is responsible for securely updating a user's OpenSRC API key in a database. It takes a username and the new API key as input. The provided API key is first stripped of whitespace and then encrypted using an external `encrypt_text` function. The encrypted key is subsequently stored in the `dbusers` collection, associated with the specified username. The function returns an integer indicating the number of database documents that were modified by the update operation.
    *   **Parameters:**
        - **username** (`str`): The username of the user whose OpenSRC API key is to be updated.
        - **opensrc_api_key** (`str`): The new OpenSRC API key to be encrypted and stored for the user.
    *   *Returns:*
        - **modified_count** (`int`): The number of documents modified by the update operation in the database, typically 0 or 1.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `database.db.update_opensrc_url`
    *   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
    *   **Description:** This function updates a user's `opensrc_base_url` in a database. It takes a username and a new base URL as input. The function performs an `update_one` operation on the `dbusers` collection, identifying the document by the provided username. It sets the `opensrc_base_url` field to the new URL after stripping any leading or trailing whitespace. The function then returns the count of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose `opensrc_base_url` is to be updated.
        - **opensrc_base_url** (`str`): The new base URL for opensource projects to be associated with the user. This value will be stripped of whitespace before storage.
    *   *Returns:*
        - **modified_count** (`int`): The number of documents that were modified by the update operation.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.fetch_gemini_key`
    *   **Signature:** `def fetch_gemini_key(username: str)`
    *   **Description:** This function retrieves the Gemini API key associated with a specific user from a database. It queries the `dbusers` collection, searching for a document where the `_id` matches the provided username. If a user document is found, it extracts and returns the `gemini_api_key` field. If no user is found in the database, the function returns `None`.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
    *   *Returns:*
        - **gemini_api_key** (`str | None`): The Gemini API key string if found for the user, otherwise None.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.fetch_ollama_url`
    *   **Signature:** `def fetch_ollama_url(username: str)`
    *   **Description:** This function retrieves the Ollama base URL associated with a specific user from a database. It takes a username as input and queries the 'dbusers' collection to find the corresponding user document. If the user is found, it extracts and returns the 'ollama_base_url' field. If the user is not found or the URL is missing, it returns None.
    *   **Parameters:**
        - **username** (`str`): The unique identifier of the user whose Ollama base URL is to be fetched.
    *   *Returns:*
        - **ollama_base_url** (`str | None`): The Ollama base URL for the specified user, or None if the user is not found or the URL is not set.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `database.db.fetch_gpt_key`
    *   **Signature:** `def fetch_gpt_key(username: str)`
    *   **Description:** This function is designed to retrieve a user's GPT API key from a database. It accepts a username as input and performs a database query to locate the corresponding user record. The function specifically targets the 'gpt_api_key' field within the user's document. If a user is found and has an associated API key, that key is returned; otherwise, the function returns None.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched from the database.
    *   *Returns:*
        - **gpt_api_key** (`str | None`): The GPT API key associated with the specified username, or None if the user is not found or the key does not exist.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `database.db.fetch_opensrc_key`
    *   **Signature:** `def fetch_opensrc_key(username: str)`
    *   **Description:** This function is designed to retrieve a user's 'opensrc_api_key' from a database. It takes a username as input and queries the 'dbusers' collection to find a matching user document. The function specifically projects the 'opensrc_api_key' field. It returns the found API key or None if the user is not found in the database.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose Open Source API key is to be fetched.
    *   *Returns:*
        - **opensrc_api_key** (`str | None`): The Open Source API key associated with the provided username, or None if the user is not found.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.fetch_opensrc_url`
    *   **Signature:** `def fetch_opensrc_url(username: str)`
    *   **Description:** This function retrieves the 'opensrc_base_url' for a specified user from a database. It queries the 'dbusers' collection, searching for a document where the '_id' matches the provided 'username'. The query is optimized to fetch only the 'opensrc_base_url' field. If a matching user document is found, the function extracts and returns the 'opensrc_base_url'. If no user is found for the given username, the function returns None.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose opensrc_base_url is to be fetched.
    *   *Returns:*
        - **opensrc_base_url** (`str | None`): The base URL for opensrc associated with the user, or None if the user is not found in the database.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.delete_user`
    *   **Signature:** `def delete_user(username: str)`
    *   **Description:** This function, `delete_user`, is designed to remove a specific user record from a database collection. It accepts a username as input, which serves as the primary key (`_id`) to identify the user document. The function then executes a `delete_one` operation on the `dbusers` collection and returns the count of documents that were successfully deleted.
    *   **Parameters:**
        - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
    *   *Returns:*
        - **deleted_count** (`int`): The number of documents deleted. This will typically be 1 if a user matching the username was found and deleted, or 0 if no such user was found.
    *   **Usage:** This function is called by no other functions.

    #### Function: `database.db.get_decrypted_api_keys`
    *   **Signature:** `def get_decrypted_api_keys(username: str)`
    *   **Description:** This function retrieves and decrypts various API keys and base URLs associated with a specific user from a database. It first attempts to locate the user by their username. If the user is not found, it immediately returns None for all expected values. Otherwise, it fetches the Gemini, GPT, and open-source API keys, decrypting them using `decrypt_text`, and also retrieves the Ollama and open-source base URLs, returning all five values.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
    *   *Returns:*
        - **gemini_plain** (`str | None`): The decrypted Gemini API key. Returns an empty string if the key is not found for the user, or None if the user does not exist.
        - **ollama_plain** (`str | None`): The Ollama base URL. Returns an empty string if the URL is not found for the user, or None if the user does not exist.
        - **gpt_plain** (`str | None`): The decrypted GPT API key. Returns an empty string if the key is not found for the user, or None if the user does not exist.
        - **opensrc_plain** (`str | None`): The decrypted open-source API key. Returns an empty string if the key is not found for the user, or None if the user does not exist.
        - **opensrc_url** (`str | None`): The open-source base URL. Returns an empty string if the URL is not found for the user, or None if the user does not exist.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.insert_chat`
    *   **Signature:** `def insert_chat(username: str, chat_name: str)`
    *   **Description:** This function creates a new chat entry in a database. It generates a unique identifier using UUID, records the provided username and chat name, and captures the current timestamp. The constructed chat document is then inserted into the 'dbchats' collection. Finally, it returns the unique ID of the newly inserted chat document.
    *   **Parameters:**
        - **username** (`str`): The username associated with the new chat entry.
        - **chat_name** (`str`): The name of the chat to be created.
    *   *Returns:*
        - **inserted_id** (`str`): The unique identifier of the newly created chat document in the database.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.fetch_chats_by_user`
    *   **Signature:** `def fetch_chats_by_user(username: str)`
    *   **Description:** This function retrieves all chat records associated with a given username from the 'dbchats' collection. It queries the collection using the provided username, sorts the results by the 'created_at' field in ascending order, and then converts the resulting cursor into a list. The function's primary purpose is to provide a comprehensive list of chats for a specific user.
    *   **Parameters:**
        - **username** (`str`): The username for which to fetch chat records.
    *   *Returns:*
        - **chats** (`list`): A list of chat documents (dictionaries) associated with the specified username, sorted by their creation timestamp.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.check_chat_exists`
    *   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
    *   **Description:** This function determines if a chat entry, identified by a specific username and chat name, exists within the 'dbchats' collection. It performs a database query using `find_one` to locate a document that matches both the provided username and chat name. The function then evaluates if a matching document was found, returning a boolean result. This effectively checks for the presence of a unique chat record.
    *   **Parameters:**
        - **username** (`str`): The username associated with the chat to be checked for existence.
        - **chat_name** (`str`): The name of the chat to be checked for existence.
    *   *Returns:*
        - **exists** (`bool`): True if a chat matching the specified username and chat name is found in the database; False otherwise.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.rename_chat_fully`
    *   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
    *   **Description:** This function renames a chat and all its associated message exchanges within a database. It first updates the `chat_name` field for a specific chat entry in the `dbchats` collection, changing it from `old_name` to `new_name` for a given `username`. Subsequently, it updates the `chat_name` for all related message exchanges in the `dbexchanges` collection, ensuring data consistency across both collections. The function returns the count of modified chat entries.
    *   **Parameters:**
        - **username** (`str`): The username associated with the chat to be renamed.
        - **old_name** (`str`): The current name of the chat.
        - **new_name** (`str`): The new name for the chat.
    *   *Returns:*
        - **modified_count** (`int`): The number of chat entries modified in the 'dbchats' collection.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `database.db.insert_exchange`
    *   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str="", main_used: str="", total_time: str="", helper_time: str="", main_time: str="", json_tokens=0, toon_tokens=0, savings_percent=0.0)`
    *   **Description:** The `insert_exchange` function is responsible for creating and storing a new exchange record in a database. It generates a unique identifier for the exchange and constructs a dictionary containing the question, answer, feedback, user details, chat name, and various optional metrics like time and token usage. A timestamp for creation is also added. The function attempts to insert this structured data into the `dbexchanges` collection. Upon successful insertion, it returns the unique ID of the new record; otherwise, it catches any exceptions, prints an error message, and returns `None`.
    *   **Parameters:**
        - **question** (`str`): The user's question in the exchange.
        - **answer** (`str`): The generated answer for the question.
        - **feedback** (`str`): The feedback provided for the exchange.
        - **username** (`str`): The username associated with this exchange.
        - **chat_name** (`str`): The name of the chat session where the exchange occurred.
        - **helper_used** (`str`): Optional: Identifier for the helper model used in the exchange, defaults to an empty string.
        - **main_used** (`str`): Optional: Identifier for the main model used in the exchange, defaults to an empty string.
        - **total_time** (`str`): Optional: The total time taken for the exchange, defaults to an empty string.
        - **helper_time** (`str`): Optional: The time taken by the helper model, defaults to an empty string.
        - **main_time** (`str`): Optional: The time taken by the main model, defaults to an empty string.
        - **json_tokens** (`int`): Optional: The number of JSON tokens used, defaults to 0.
        - **toon_tokens** (`int`): Optional: The number of Toon tokens used, defaults to 0.
        - **savings_percent** (`float`): Optional: The percentage of savings achieved, defaults to 0.0.
    *   *Returns:*
        - **new_id** (`str`): The unique identifier of the newly inserted exchange record upon successful insertion.
        - **None**: Returned if an exception occurs during the database insertion process.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.fetch_exchanges_by_user`
    *   **Signature:** `def fetch_exchanges_by_user(username: str)`
    *   **Description:** This function is designed to retrieve exchange records from a database based on a given username. It queries a collection, presumably `dbexchanges`, to find all documents where the 'username' field matches the input. The retrieved records are then sorted by their 'created_at' timestamp in ascending order. Finally, the function converts these sorted records into a list and returns them.
    *   **Parameters:**
        - **username** (`str`): The username for which to fetch exchange records.
    *   *Returns:*
        - **exchanges** (`list`): A list of exchange records (documents) associated with the specified username, sorted by their creation timestamp in ascending order.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.fetch_exchanges_by_chat`
    *   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
    *   **Description:** This function retrieves a list of exchange records from a database collection, identified as `dbexchanges`. It filters these records based on a specific username and chat name provided as arguments. The retrieved exchanges are then sorted by their `created_at` timestamp in ascending order before being returned as a list.
    *   **Parameters:**
        - **username** (`str`): The username used to filter the exchange records.
        - **chat_name** (`str`): The name of the chat used to filter the exchange records.
    *   *Returns:*
        - **exchanges** (`list`): A list of exchange documents (dictionaries) that match the provided username and chat name, sorted by their creation timestamp.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `database.db.update_exchange_feedback`
    *   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
    *   **Description:** This function updates the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function uses a database client, `dbexchanges`, to locate the document by its `_id` and then sets the `feedback` field to the provided integer value. It returns the count of documents that were successfully modified by this operation.
    *   **Parameters:**
        - **exchange_id** (`Any`): The unique identifier for the exchange record that needs its feedback updated. Its specific type depends on the database's ID format (e.g., ObjectId, string).
        - **feedback** (`int`): The integer value representing the feedback to be assigned to the specified exchange record.
    *   *Returns:*
        - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 indicates success if the document existed, 0 otherwise.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `database.db.update_exchange_feedback_message`
    *   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
    *   **Description:** This function updates an existing exchange record in the database. It identifies the target record using a unique `exchange_id` and then sets or updates its `feedback_message` field with the provided string. The function leverages a database collection named `dbexchanges` to perform a `update_one` operation. It returns the count of documents that were successfully modified by the update operation.
    *   **Parameters:**
        - **exchange_id** (`Any`): The unique identifier for the exchange record to be updated in the database. This is used to locate the specific document.
        - **feedback_message** (`str`): The new feedback message string to be stored in the specified exchange record.
    *   *Returns:*
        - **modified_count** (`int`): The number of documents that were modified by the update operation. Typically 0 or 1 for `update_one`.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `database.db.delete_exchange_by_id`
    *   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
    *   **Description:** This function is designed to remove a specific exchange record from a database collection. It takes an exchange identifier as input and uses it to locate and delete a single document. The function then reports the number of documents successfully deleted.
    *   **Parameters:**
        - **exchange_id** (`str`): The unique string identifier of the exchange document to be deleted from the database.
    *   *Returns:*
        - **deleted_count** (`int`): The number of documents that were deleted, typically 0 or 1.
    *   **Usage:** This function is called by no other functions.

    #### Function: `database.db.delete_full_chat`
    *   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
    *   **Description:** This function, `delete_full_chat`, is designed to completely remove a specific chat and all its associated message exchanges from the database. It first deletes all message exchanges linked to the provided username and chat name. Subsequently, it proceeds to delete the chat entry itself from the chat collection. This two-step process ensures data consistency by removing both the chat record and its related messages. The function returns the count of chat documents that were successfully deleted.
    *   **Parameters:**
        - **username** (`str`): The username associated with the chat to be deleted.
        - **chat_name** (`str`): The name of the chat to be deleted.
    *   *Returns:*
        - **deleted_chat_count** (`int`): The number of chat documents successfully deleted from the database.
    *   **Usage:** This function is not called by any other functions.

    ### File: `frontend/frontend.py`

    #### Function: `frontend.frontend.clean_names`
    *   **Signature:** `def clean_names(model_list)`
    *   **Description:** This function takes a list of strings, where each string is expected to represent a path or a similar structure with segments separated by '/'. It processes each string by splitting it based on the '/' delimiter and then extracts the last segment. The function returns a new list containing these extracted last segments, effectively "cleaning" the names by removing preceding path information.
    *   **Parameters:**
        - **model_list** (`list[str]`): A list of strings, where each string is expected to contain path-like segments separated by '/'. For example, a list of file paths or URLs.
    *   *Returns:*
        - **cleaned_names** (`list[str]`): A new list of strings, where each string is the last segment of the corresponding input string after splitting by '/'.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `frontend.frontend.get_filtered_models`
    *   **Signature:** `def get_filtered_models(source_list, category_name)`
    *   **Description:** This function filters a given list of models (`source_list`) based on a specified `category_name`. It retrieves associated keywords for the category from a global `CATEGORY_KEYWORDS` mapping. If the category's keywords include "STANDARD", the function returns only those models from the `source_list` that are also present in a `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list` and includes models whose names contain any of the category's keywords (case-insensitively). If no models match the keywords, the original `source_list` is returned.
    *   **Parameters:**
        - **source_list** (`list`): The list of models to be filtered.
        - **category_name** (`str`): The name of the category to filter by, used to retrieve associated keywords.
    *   *Returns:*
        - **filtered_models** (`list`): A list of models filtered according to the specified category's keywords, or the original list if no filters apply or no models match.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `frontend.frontend.save_gemini_cb`
    *   **Signature:** `def save_gemini_cb()`
    *   **Description:** This function serves as a callback to save a user's Gemini API key. It retrieves the potential new key from the Streamlit session state. If a valid new key is found, it updates the Gemini key in the database for the current user. Subsequently, it clears the input field in the session state and displays a success toast message to the user.
    *   **Parameters:**
    *   *Returns:*
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `frontend.frontend.save_ollama_cb`
    *   **Signature:** `def save_ollama_cb()`
    *   **Description:** This function, `save_ollama_cb`, acts as a callback to save a user-provided Ollama URL. It retrieves the potential new URL from the Streamlit session state, specifically from the key 'in_ollama_url'. If a non-empty URL is found, it proceeds to update this URL in the database using `db.update_ollama_url`, associating it with the current user's username from the session state. Upon successful update, a confirmation toast message is displayed to the user via `st.toast`.
    *   **Parameters:**
    *   *Returns:*
    *   **Usage:** This function is called by no other functions.

    #### Function: `frontend.frontend.load_data_from_db`
    *   **Signature:** `def load_data_from_db(username: str)`
    *   **Description:** This function loads chat and exchange data from the database for a given username. It first checks if the data for the specified user is already loaded in the Streamlit session state. If not, it initializes the session state for chats, then fetches predefined chats and their associated exchanges from the database. It handles cases where exchanges might exist for chats not initially defined and ensures feedback values are standardized. Finally, it creates a default chat if no chats are found and sets the active chat in the session state.
    *   **Parameters:**
        - **username** (`str`): The username for whom to load chat and exchange data from the database.
    *   *Returns:*
    *   **Usage:** This function is called by no other functions.

    #### Function: `frontend.frontend.handle_feedback_change`
    *   **Signature:** `def handle_feedback_change(ex, val)`
    *   **Description:** This function, `handle_feedback_change`, is designed to process and persist user feedback for an exchange object within a Streamlit application. It takes an exchange object (`ex`) and a new feedback value (`val`) as input. The function first updates the `feedback` key of the `ex` object with the provided `val`. Subsequently, it calls a database utility function, `db.update_exchange_feedback`, to store this feedback persistently using the exchange's unique identifier. Finally, it triggers a full rerun of the Streamlit application to reflect the changes in the user interface.
    *   **Parameters:**
        - **ex** (`dict`): The exchange object, expected to be a dictionary containing at least an '_id' for database identification and a 'feedback' key to be updated.
        - **val** (`Any`): The new feedback value to be assigned to the exchange object.
    *   *Returns:*
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `frontend.frontend.handle_delete_exchange`
    *   **Signature:** `def handle_delete_exchange(chat_name, ex)`
    *   **Description:** This function is responsible for deleting a specific exchange. It first removes the exchange from the database using its unique identifier. Subsequently, it checks if the associated chat and exchange exist within the Streamlit session state and, if found, removes the exchange from the chat's list of exchanges. Finally, it triggers a Streamlit rerun to update the UI.
    *   **Parameters:**
        - **chat_name** (`str`): The name of the chat from which the exchange is to be potentially removed in the session state.
        - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' field for database deletion and to be present in the session state.
    *   *Returns:*
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `frontend.frontend.handle_delete_chat`
    *   **Signature:** `def handle_delete_chat(username, chat_name)`
    *   **Description:** This function handles the deletion of a specific chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it updates the Streamlit session state by removing the chat from `st.session_state.chats`. If other chats remain, the first one becomes the active chat; otherwise, a new default chat named "Chat 1" is created, inserted into the database via `db.insert_chat`, and set as the active chat. Finally, `st.rerun()` is called to refresh the Streamlit application.
    *   **Parameters:**
        - **username** (`str`): The username of the user whose chat is being deleted.
        - **chat_name** (`str`): The name of the chat to be deleted.
    *   *Returns:*
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `frontend.frontend.extract_repo_name`
    *   **Signature:** `def extract_repo_name(text)`
    *   **Description:** This function extracts a repository name from an input text string. It first searches for a URL within the text using a regular expression. If a URL is found, it parses the URL to extract its path component. The function then takes the last segment of the path as the potential repository name and removes a ".git" suffix if present. If no URL is found or no valid repository name can be derived, the function returns None.
    *   **Parameters:**
        - **text** (`str`): The input string that may contain a URL from which to extract a repository name.
    *   *Returns:*
        - **repo_name** (`str | None`): The extracted repository name as a string, or None if no URL or repository name could be identified in the input text.
    *   **Usage:** This function is not called by any other functions.

    #### Function: `frontend.frontend.stream_text_generator`
    *   **Signature:** `def stream_text_generator(text)`
    *   **Description:** This function acts as a generator that takes a single string of text and yields its words one by one. It splits the input text by spaces and then iterates through each resulting word. After yielding each word appended with a space, it introduces a small delay using `time.sleep(0.01)` to simulate a streaming effect.
    *   **Parameters:**
        - **text** (`str`): The input string of text to be streamed word by word.
    *   *Returns:*
        - **word_chunk** (`str`): A single word from the input text, followed by a space, yielded sequentially.
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `frontend.frontend.render_text_with_mermaid`
    *   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream=False)`
    *   **Description:** This function processes a given markdown string, identifying and separating standard markdown content from embedded Mermaid diagram code blocks. It then renders the standard markdown using `st.markdown` (with an option to stream via `st.write_stream`) and attempts to render the Mermaid diagrams using `st_mermaid`. In case of an error during Mermaid rendering, the Mermaid code is displayed as a code block using `st.code`. The function returns early if the input markdown text is empty.
    *   **Parameters:**
        - **markdown_text** (`str`): The input string containing markdown content, potentially with embedded Mermaid diagram syntax.
        - **should_stream** (`bool`): A flag indicating whether standard markdown content should be streamed using `st.write_stream` (if True) or rendered directly with `st.markdown` (if False). Defaults to False.
    *   *Returns:*
    *   **Usage:** This function is not explicitly called by any other functions in the provided context.

    #### Function: `frontend.frontend.render_exchange`
    *   **Signature:** `def render_exchange(ex, current_chat_name)`
    *   **Description:** This function `render_exchange` is designed to display a single chat interaction, comprising a user's question and an assistant's answer, within a Streamlit application. It first renders the user's query, followed by the assistant's response. The assistant's message area includes an interactive toolbar with feedback options (like, dislike, comment), a download button for the response, and a delete button. These interactive elements trigger actions such as `handle_feedback_change`, `db.update_exchange_feedback_message`, `st.rerun`, and `handle_delete_exchange`. The function also manages error states by displaying an error message and a delete option. Finally, the assistant's answer content is rendered using `render_text_with_mermaid` within a bordered container.
    *   **Parameters:**
        - **ex** (`dict`): A dictionary-like object representing a chat exchange, containing keys such as 'question', 'answer', 'feedback' status, 'feedback_message', and a unique identifier '_id'.
        - **current_chat_name** (`str`): A string indicating the name of the current chat session, used to provide context for operations like deleting exchanges.
    *   *Returns:*
    *   **Usage:** This function is not explicitly called by other functions in the provided context.

    ### File: `schemas/types.py`

    #### Class: `ParameterDescription`
    *   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to encapsulate the essential details of a function parameter. It provides a structured format for its name, type, and a descriptive text, ensuring that parameter information is consistently represented and validated. This class serves as a fundamental data structure for describing function signatures within a broader system.
    *   **Instantiation:** The instantiation points for this class are not provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes the instance attributes `name`, `type`, and `description` based on the provided arguments, leveraging Pydantic's validation capabilities to ensure data integrity upon instantiation.
        *   *Parameters:*
            - **name** (`str`): The name of the parameter being described.
            - **type** (`str`): The data type of the parameter, typically as a string representation.
            - **description** (`str`): A textual explanation of the parameter's purpose or role.
    *   **Usage:** The instantiation points for this class are not provided in the context.

    #### Class: `ReturnDescription`
    *   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to provide a standardized structure for describing the return value of a function. It encapsulates three essential pieces of information: the name of the return value, its type, and a description explaining its purpose or content. This model is likely used within a larger system to generate documentation or validate function signatures.
    *   **Instantiation:** The context provided does not specify where this class is instantiated.
    *   **Dependencies:** "This class depends on `pydantic.BaseModel` for its structural definition and validation capabilities. No other explicit functional dependencies are identified."
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, implicitly generates an `__init__` method. This constructor is used to initialize instances of `ReturnDescription` by providing values for its `name`, `type`, and `description` fields, ensuring data validation according to their specified types.
        *   *Parameters:*
            - **name** (`str`): The name or identifier of the return value.
            - **type** (`str`): The data type of the return value.
            - **description** (`str`): A textual description of what the return value represents or its purpose.
    *   **Usage:** The context provided does not specify where this class is instantiated.

    #### Class: `UsageContext`
    *   **Summary:** The UsageContext class is a Pydantic BaseModel designed to describe the calling context of a function or method. It serves as a structured data container, holding two string fields: 'calls' to summarize what the entity calls, and 'called_by' to summarize where the entity is utilized. This class is primarily used for metadata aggregation within a larger system.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `UsageContext` is implicitly generated by Pydantic's BaseModel. It initializes an instance of `UsageContext` by accepting `calls` and `called_by` as string arguments, validating them according to their type hints to ensure data integrity.
        *   *Parameters:*
            - **calls** (`str`): A string describing the functions, methods, or external entities that this context's subject calls.
            - **called_by** (`str`): A string describing the functions, methods, or external entities that call this context's subject.
    *   **Usage:** The provided context does not specify where this class is instantiated.

    #### Class: `FunctionDescription`
    *   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It provides a structured format for detailing a function's high-level purpose, its input parameters, its expected return values, and its operational context within a larger system. This model serves as a standardized data structure for representing and exchanging function analysis results, facilitating automated documentation and understanding.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
    *   **Constructor:**
        *   *Description:* As a Pydantic BaseModel, the `__init__` method for `FunctionDescription` is implicitly generated by Pydantic. It initializes an instance of the class by accepting values for its defined fields: `overall`, `parameters`, `returns`, and `usage_context`, ensuring type validation and data integrity upon instantiation.
        *   *Parameters:*
            - **overall** (`str`): A high-level summary describing the function's primary purpose and functionality.
            - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing an input parameter of the function, including its name, type, and description.
            - **returns** (`List[ReturnDescription]`): A list of `ReturnDescription` objects, each detailing a possible return value of the function, including its type and description.
            - **usage_context** (`UsageContext`): An object containing information about where the function is called and what other functions or methods it calls internally.
    *   **Usage:** The specific locations where this class is instantiated are not provided in the context.

    #### Class: `FunctionAnalysis`
    *   **Summary:** The FunctionAnalysis class serves as the main Pydantic model for structuring the comprehensive analysis of a single function. It encapsulates the function's unique identifier, a detailed `FunctionDescription` object (an external type), and an optional `error` field for reporting issues during analysis. This model is fundamental for standardizing the output of function analysis within a larger system, ensuring a consistent data structure for function-level insights.
    *   **Instantiation:** The instantiation points for this class are not provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* This class does not explicitly define an `__init__` method. As a Pydantic BaseModel, its constructor is implicitly generated to accept and validate values for its defined fields: `identifier`, `description`, and `error`.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifying the function being analyzed.
            - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose, parameters, return values, and usage context.
            - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the analysis of the function. Defaults to `None`.
    *   **Usage:** The instantiation points for this class are not provided in the context.

    #### Class: `ConstructorDescription`
    *   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to provide a structured representation of a Python class's `__init__` method. It encapsulates a textual summary of the constructor's behavior and a list of detailed descriptions for each of its parameters. This model is crucial for generating comprehensive documentation or for static analysis of class constructors.
    *   **Instantiation:** No specific instantiation points for this class were provided in the input context.
    *   **Dependencies:** "This class depends on `pydantic.BaseModel` for its data structure and validation, and `typing.List` for type hinting. It also implicitly depends on the `ParameterDescription` class, which defines the structure of individual parameters."
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ConstructorDescription` is implicitly generated by Pydantic's BaseModel. It initializes an instance of the class by accepting and validating the `description` string and a list of `ParameterDescription` objects, assigning them to the corresponding instance attributes.
        *   *Parameters:*
            - **description** (`str`): A string summary detailing the functionality and purpose of the constructor.
            - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each providing details about a specific parameter of the constructor.
    *   **Usage:** No specific instantiation points for this class were provided in the input context.

    #### Class: `ClassContext`
    *   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's operational context. It specifically tracks external dependencies and the locations or components responsible for its instantiation. This model provides a structured way to describe how a class interacts with its environment and where it is utilized within a larger system.
    *   **Instantiation:** No specific instantiation points are listed in the provided context for this class.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ClassContext` is implicitly generated by Pydantic's BaseModel. It initializes an instance with two string attributes: `dependencies` and `instantiated_by`. These attributes are directly mapped from the constructor's arguments, setting up the class's contextual description upon creation.
        *   *Parameters:*
            - **dependencies** (`str`): A string describing the external dependencies required by the class.
            - **instantiated_by** (`str`): A string describing the primary points or modules where this class is instantiated.
    *   **Usage:** No specific instantiation points are listed in the provided context for this class.

    #### Class: `ClassDescription`
    *   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of another Python class. It acts as a structured data container, holding a high-level overall description, a detailed `init_method` analysis, a list of `methods` analyses, and `usage_context` information regarding dependencies and instantiation points. This model is crucial for standardizing the output of class analysis within a larger system.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** "This class does not explicitly declare external functional dependencies within its source code, relying on its Pydantic BaseModel inheritance and type hints."
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, implicitly generates its constructor. The constructor is responsible for initializing instances of `ClassDescription` by validating and assigning values to its defined fields: `overall`, `init_method`, `methods`, and `usage_context`.
        *   *Parameters:*
            - **overall** (`str`): A high-level summary of the class's purpose and functionality.
            - **init_method** (`ConstructorDescription`): An object containing the description and parameters of the class's constructor.
            - **methods** (`List[FunctionAnalysis]`): A list of detailed analyses for each method defined within the class.
            - **usage_context** (`ClassContext`): An object describing the class's external dependencies and where it is instantiated.
    *   **Usage:** The provided context does not specify where this class is instantiated.

    #### Class: `ClassAnalysis`
    *   **Summary:** The `ClassAnalysis` class serves as the main Pydantic model for structuring the comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed `ClassDescription` object containing its constructor and method analyses, and an optional error field. This model is designed to provide a standardized, machine-readable format for representing the output of a class analysis process.
    *   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* This class does not explicitly define an `__init__` method. Pydantic's `BaseModel` handles the initialization of its fields based on the provided type hints, automatically creating attributes for `identifier`, `description`, and `error` upon instantiation.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifying the class being analyzed.
            - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
            - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the analysis of the class. Defaults to `None`.
    *   **Usage:** The specific points of instantiation for this class are not provided in the current context.

    #### Class: `CallInfo`
    *   **Summary:** The CallInfo class is a Pydantic BaseModel designed to encapsulate details about a specific code call event. It serves as a structured data container for tracking where a function, method, or module is called or instantiated. This class helps in analyzing code relationships by providing a standardized format for call information, including the file path, the name of the calling entity, the type of call, and the line number.
    *   **Instantiation:** The instantiation points for this class are not specified in the provided context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `CallInfo` is implicitly generated by Pydantic's BaseModel. It initializes an instance of `CallInfo` by validating and assigning the provided `file`, `function`, `mode`, and `line` attributes based on their type annotations.
        *   *Parameters:*
            - **file** (`str`): The file path where the call event occurred.
            - **function** (`str`): The name of the calling function or method.
            - **mode** (`str`): The type of call, e.g., 'method', 'function', 'module'.
            - **line** (`int`): The line number in the file where the call event occurred.
    *   **Usage:** The instantiation points for this class are not specified in the provided context.

    #### Class: `FunctionContextInput`
    *   **Summary:** The FunctionContextInput class serves as a Pydantic data model designed to encapsulate the contextual information surrounding a function's interactions. It defines a structured schema for tracking which other functions or methods a given function 'calls' and by which other functions or methods it is 'called_by'. This model is crucial for providing a clear, machine-readable representation of a function's dependencies and usage within a larger system, facilitating analysis and documentation.
    *   **Instantiation:** The specific points of instantiation for this class are not provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* This class, inheriting from Pydantic's BaseModel, implicitly initializes its attributes 'calls' and 'called_by' upon instantiation. Pydantic handles validation and assignment of these fields based on the provided input data, ensuring type correctness for the list of called entities and the list of CallInfo objects for callers.
        *   *Parameters:*
            - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this function calls.
            - **called_by** (`List[CallInfo]`): A list of CallInfo objects representing other functions or methods that call this function.
    *   **Usage:** The specific points of instantiation for this class are not provided in the context.

    #### Class: `FunctionAnalysisInput`
    *   **Summary:** This class serves as a Pydantic model defining the precise structure and validation rules for input data required to initiate a function analysis process. It encapsulates all necessary information, including the function's identifier, its source code, associated import statements, and contextual details, ensuring that any incoming data conforms to the expected schema before processing. This model is crucial for robust data handling in a larger AI system focused on code analysis.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `FunctionAnalysisInput` is implicitly provided by Pydantic's BaseModel. It initializes an instance of `FunctionAnalysisInput` by validating and assigning the provided `mode`, `identifier`, `source_code`, `imports`, and `context` attributes based on their defined types and constraints.
        *   *Parameters:*
            - **mode** (`Literal["function_analysis"]`): Specifies the mode of operation, which must be 'function_analysis'.
            - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
            - **source_code** (`str`): The raw source code of the function to be analyzed.
            - **imports** (`List[str]`): A list of import statements relevant to the function's source code.
            - **context** (`FunctionContextInput`): Additional contextual information required for the function analysis.
    *   **Usage:** The provided context does not specify where this class is instantiated.

    #### Class: `MethodContextInput`
    *   **Summary:** The MethodContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information for a method. It defines fields such as the method's unique identifier, a list of other functions or methods it calls, a list of entities that call it, its arguments, and its docstring. This class serves as a data structure to standardize and transfer method-specific metadata within a larger analysis or documentation generation system.
    *   **Instantiation:** This class is not explicitly shown to be instantiated by other components within the provided context.
    *   **Dependencies:** This class does not explicitly depend on other components within the provided context.
    *   **Constructor:**
        *   *Description:* The constructor for `MethodContextInput` is automatically generated by Pydantic. It initializes an instance of the class by validating and assigning values to its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`. This ensures that all method context data conforms to the specified types upon instantiation.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifier for the method.
            - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls.
            - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects representing other functions or methods that call this method.
            - **args** (`List[str]`): A list of string representations of the arguments accepted by this method.
            - **docstring** (`Optional[str]`): The docstring of the method, if available; otherwise, it can be null.
    *   **Usage:** This class is not explicitly shown to be instantiated by other components within the provided context.

    #### Class: `ClassContextInput`
    *   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured context information for the analysis of a Python class. It defines the data structure for dependencies, instantiation points, and method-specific contexts. This model serves as an input schema for processes that require detailed contextual data about a class.
    *   **Instantiation:** There is no explicit information provided about where this class is instantiated.
    *   **Dependencies:** This class does not explicitly declare external functional dependencies within its definition.
    *   **Constructor:**
        *   *Description:* This class does not define an explicit `__init__` method. Pydantic's `BaseModel` handles the initialization of its fields based on the provided type hints, automatically creating attributes for `dependencies`, `instantiated_by`, and `method_context` upon instantiation.
        *   *Parameters:*
            - **dependencies** (`List[str]`): A list of strings describing the external dependencies required by the class.
            - **instantiated_by** (`List[CallInfo]`): A list of `CallInfo` objects describing the primary points or modules where this class is instantiated.
            - **method_context** (`List[MethodContextInput]`): A list of `MethodContextInput` objects, each detailing the context of a specific method within the class.
    *   **Usage:** There is no explicit information provided about where this class is instantiated.

    #### Class: `ClassAnalysisInput`
    *   **Summary:** The ClassAnalysisInput class serves as a Pydantic data model, defining the precise structure and validation rules for input data required to initiate a class analysis process. It encapsulates all necessary information, including the class's identifier, its full source code, associated import statements, and contextual details, ensuring that any incoming data conforms to the expected schema before processing. This model is crucial for robust data handling in a larger AI system focused on code analysis.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The `ClassAnalysisInput` class inherits from `pydantic.BaseModel` and therefore does not define an explicit `__init__` method. Pydantic automatically generates a constructor that accepts keyword arguments corresponding to the class's defined fields, enabling robust data validation and parsing upon instantiation.
        *   *Parameters:*
            - **mode** (`Literal["class_analysis"]`): A literal string indicating the type of analysis to be performed, which must be 'class_analysis'.
            - **identifier** (`str`): The unique name or identifier of the Python class that is the subject of the analysis.
            - **source_code** (`str`): The complete raw source code string of the class definition to be analyzed.
            - **imports** (`List[str]`): A list of strings, each representing an import statement relevant to the source file where the class is defined.
            - **context** (`ClassContextInput`): An object containing additional contextual information pertinent to the class, such as its dependencies and where it is instantiated.
    *   **Usage:** The provided context does not specify where this class is instantiated.

---
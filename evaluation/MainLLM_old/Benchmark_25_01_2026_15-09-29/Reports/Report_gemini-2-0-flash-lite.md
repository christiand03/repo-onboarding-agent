```markdown
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** Description: [Could not be determined due to a missing README file and insufficient context.]
- **Key Features:** 
  - [Feature 1]
  - [Feature 2]
  - Total Number of Key Features should not exceed five
- **Tech Stack:** - altair==4.2.2
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

*   **Repository Structure:**
    ```mermaid
    graph LR
    root[root]
    root --> .env.example
    root --> .gitignore
    root --> SystemPrompts
    root --> analysis_output.json
    root --> backend
    root --> database
    root --> frontend
    root --> notizen
    root --> output.json
    root --> output.toon
    root --> readme.md
    root --> requirements.txt
    root --> result
    root --> schemas
    root --> statistics
    root --> test.json
    SystemPrompts[SystemPrompts]
    backend[backend]
    database[database]
    frontend[frontend]
    notizen[notizen]
    result[result]
    schemas[schemas]
    statistics[statistics]
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
    notizen --> Report Agenda.txt
    notizen --> Zwischenpraesentation Agenda.txt
    notizen --> doc_bestandteile.md
    notizen --> grafiken
    notizen --> notizen.md
    notizen --> paul_notizen.md
    notizen --> praesentation_notizen.md
    notizen --> technische_notizen.md
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
    SystemPrompts --> SystemPromptClassHelperLLM.txt
    SystemPrompts --> SystemPromptFunctionHelperLLM.txt
    SystemPrompts --> SystemPromptHelperLLM.txt
    SystemPrompts --> SystemPromptMainLLM.txt
    SystemPrompts --> SystemPromptMainLLMToon.txt
    SystemPrompts --> SystemPromptNotebookLLM.txt
    notizen --> grafiken --> "1"
    notizen --> grafiken --> "2"
    notizen --> grafiken --> Flask-Repo
    notizen --> grafiken --> Repo-onboarding
    "1" --> File_Dependency_Graph_Repo.dot
    "1" --> global_callgraph.png
    "1" --> global_graph.png
    "1" --> global_graph_2.png
    "1" --> repo.dot
    "2" --> FDG_repo.dot
    "2" --> fdg_graph.png
    "2" --> fdg_graph_2.png
    "2" --> filtered_callgraph_flask.png
    "2" --> filtered_callgraph_repo-agent.png
    "2" --> filtered_callgraph_repo-agent_3.png
    "2" --> filtered_repo_callgraph_flask.dot
    "2" --> filtered_repo_callgraph_repo-agent-3.dot
    "2" --> filtered_repo_callgraph_repo-agent.dot
    "2" --> global_callgraph.png
    "2" --> graph_flask.md
    "2" --> repo.dot
    Flask-Repo --> __init__.dot
    Flask-Repo --> __main__.dot
    Flask-Repo --> app.dot
    Flask-Repo --> auth.dot
    Flask-Repo --> blog.dot
    Flask-Repo --> blueprints.dot
    Flask-Repo --> cli.dot
    Flask-Repo --> conf.dot
    Flask-Repo --> config.dot
    Flask-Repo --> conftest.dot
    Flask-Repo --> ctx.dot
    Flask-Repo --> db.dot
    Flask-Repo --> debughelpers.dot
    Flask-Repo --> factory.dot
    Flask-Repo --> flask.dot
    Flask-Repo --> globals.dot
    Flask-Repo --> hello.dot
    Flask-Repo --> helpers.dot
    Flask-Repo --> importerrorapp.dot
    Flask-Repo --> logging.dot
    Flask-Repo --> make_celery.dot
    Flask-Repo --> multiapp.dot
    Flask-Repo --> provider.dot
    Flask-Repo --> scaffold.dot
    Flask-Repo --> sessions.dot
    Flask-Repo --> signals.dot
    Flask-Repo --> tag.dot
    Flask-Repo --> tasks.dot
    Flask-Repo --> templating.dot
    Flask-Repo --> test_appctx.dot
    Flask-Repo --> test_async.dot
    Flask-Repo --> test_auth.dot
    Flask-Repo --> test_basic.dot
    Flask-Repo --> test_blog.dot
    Flask-Repo --> test_blueprints.dot
    Flask-Repo --> test_cli.dot
    Flask-Repo --> test_config.dot
    Flask-Repo --> test_config.png
    Flask-Repo --> test_converters.dot
    Flask-Repo --> test_db.dot
    Flask-Repo --> test_factory.dot
    Flask-Repo --> test_helpers.dot
    Flask-Repo --> test_instance_config.dot
    Flask-Repo --> test_js_example.dot
    Flask-Repo --> test_json.dot
    Flask-Repo --> test_json_tag.dot
    Flask-Repo --> test_logging.dot
    Flask-Repo --> test_regression.dot
    Flask-Repo --> test_reqctx.dot
    Flask-Repo --> test_request.dot
    Flask-Repo --> test_session_interface.dot
    Flask-Repo --> test_signals.dot
    Flask-Repo --> test_subclassing.dot
    Flask-Repo --> test_templating.dot
    Flask-Repo --> test_testing.dot
    Flask-Repo --> test_user_error_handler.dot
    Flask-Repo --> test_views.dot
    Flask-Repo --> testing.dot
    Flask-Repo --> typing.dot
    Flask-Repo --> typing_app_decorators.dot
    Flask-Repo --> typing_error_handler.dot
    Flask-Repo --> typing_route.dot
    Flask-Repo --> views.dot
    Flask-Repo --> wrappers.dot
    Flask-Repo --> wsgi.dot
    Repo-onboarding --> AST.dot
    Repo-onboarding --> Frontend.dot
    Repo-onboarding --> HelperLLM.dot
    Repo-onboarding --> HelperLLM.png
    Repo-onboarding --> MainLLM.dot
    Repo-onboarding --> agent.dot
    Repo-onboarding --> basic_info.dot
    Repo-onboarding --> callgraph.dot
    Repo-onboarding --> getRepo.dot
    Repo-onboarding --> graph_AST.png
    Repo-onboarding --> graph_AST2.png
    Repo-onboarding --> graph_AST3.png
    Repo-onboarding --> main.dot
    Repo-onboarding --> tools.dot
    Repo-onboarding --> types.dot
    ```

## 2. Installation
### Dependencies
-   altair==4.2.2
-   annotated-types==0.7.0
-   anyio==4.11.0
-   attrs==25.4.0
-   bcrypt==5.0.0
-   blinker==1.9.0
-   cachetools==6.2.2
-   captcha==0.7.1
-   certifi==2025.11.12
-   cffi==2.0.0
-   charset-normalizer==3.4.4
-   click==8.3.1
-   colorama==0.4.6
-   contourpy==1.3.3
-   cryptography==46.0.3
-   cycler==0.12.1
-   distro==1.9.0
-   dnspython==2.8.0
-   dotenv==0.9.9
-   entrypoints==0.4
-   extra-streamlit-components==0.1.81
-   filetype==1.2.0
-   fonttools==4.61.0
-   gitdb==4.0.12
-   GitPython==3.1.45
-   google-ai-generativelanguage==0.9.0
-   google-api-core==2.28.1
-   google-auth==2.43.0
-   googleapis-common-protos==1.72.0
-   grpcio==1.76.0
-   grpcio-status==1.76.0
-   h11==0.16.0
-   httpcore==1.0.9
-   httpx==0.28.1
-   idna==3.11
-   Jinja2==3.1.6
-   jiter==0.12.0
-   jsonpatch==1.33
-   jsonpointer==3.0.0
-   jsonschema==4.25.1
-   jsonschema-specifications==2025.9.1
-   kiwisolver==1.4.9
-   langchain==1.0.8
-   langchain-core==1.1.0
-   langchain-google-genai==3.1.0
-   langchain-ollama==1.0.0
-   langchain-openai==1.1.0
-   langgraph==1.0.3
-   langgraph-checkpoint==3.0.1
-   langgraph-prebuilt==1.0.5
-   langgraph-sdk==0.2.9
-   langsmith==0.4.46
-   MarkupSafe==3.0.3
-   matplotlib==3.10.7
-   narwhals==2.12.0
-   networkx==3.6
-   numpy==2.3.5
-   ollama==0.6.1
-   openai==2.8.1
-   orjson==3.11.4
-   ormsgpack==1.12.0
-   packaging==25.0
-   pandas==2.3.3
-   pillow==12.0.0
-   proto-plus==1.26.1
-   protobuf==6.33.1
-   pyarrow==21.0.0
-   pyasn1==0.6.1
-   pyasn1_modules==0.4.2
-   pycparser==2.23
-   pydantic==2.12.4
-   pydantic_core==2.41.5
-   pydeck==0.9.1
-   PyJWT==2.10.1
-   pymongo==4.15.4
-   pyparsing==3.2.5
-   python-dateutil==2.9.0.post0
-   python-dotenv==1.2.1
-   pytz==2025.2
-   PyYAML==6.0.3
-   referencing==0.37.0
-   regex==2025.11.3
-   requests==2.32.5
-   requests-toolbelt==1.0.0
-   rpds-py==0.29.0
-   rsa==4.9.1
-   setuptools==75.9.1
-   six==1.17.0
-   smmap==5.0.2
-   sniffio==1.3.1
-   streamlit==1.51.0
-   streamlit-authenticator==0.4.2
-   streamlit-mermaid==0.3.0
-   tenacity==9.1.2
-   tiktoken==0.12.0
-   toml==0.10.2
-   toolz==1.1.0
-   toon_format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c9006de6
-   tornado==6.5.2
-   tqdm==4.67.1
-   typing-inspection==0.4.2
-   typing_extensions==4.15.0
-   tzdata==2025.2
-   urllib3==2.5.0
-   watchdog==6.0.0
-   xxhash==3.6.0
-   zstandard==0.25.0
-   nbformat
### Setup Guide
Description: Information not found
### Quick Startup
Description: Information not found

## 3. Use Cases & Commands
Description: Information not found

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** The `path_to_module` function converts a given file path into its corresponding Python module path string. It first calculates the relative path of the file with respect to a specified project root. The function then removes the '.py' extension if present and replaces path separators with dots to form the module path. Special handling is included for `__init__.py` files, where the '.__init__' suffix is removed from the module path.
*   **Parameters:**
    -   **filepath** (str): The absolute or relative path to a Python file.
    -   **project_root** (str): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    -   **module_path** (str): The Python module path string derived from the input filepath.
*   **Usage:** - Analysis data not available for this component.
---
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` and is designed to traverse an Abstract Syntax Tree (AST) of Python source code. Its primary purpose is to extract structured information about imports, functions, and classes found within the provided source code. It builds a `schema` dictionary that categorizes these elements, including details like identifiers, names, docstrings, and source code segments. The visitor uses specific `visit_` methods to handle different AST node types, populating its internal schema with the discovered code elements.
*   **Instantiation:** - Analysis data not available for this component.
*   **Dependencies:** - Analysis data not available for this component.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes the ASTVisitor with the raw source code, the file's absolute path, and the project's root directory. It calculates the module path from these inputs and sets up an empty dictionary `self.schema` to store discovered imports, functions, and classes. Additionally, it initializes `_current_class` to `None` to track the context of class definitions during AST traversal.
    *   *Parameters:*
        -   **self** (ASTVisitor): The instance of the ASTVisitor class.
        -   **source_code** (str): The raw source code of the file being visited.
        -   **file_path** (str): The absolute path to the file being visited.
        -   **project_root** (str): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(node: ast.Import)`
        *   *Description:* This method is invoked when an `ast.Import` node is encountered during AST traversal, indicating a module import statement. It iterates through each alias defined in the import statement and appends the module's name to the `imports` list within the `self.schema` dictionary. After processing the import, it calls `self.generic_visit(node)` to ensure continued traversal of the AST.
        *   *Parameters:*
            -   **self** (ASTVisitor): The instance of the ASTVisitor class.
            -   **node** (ast.Import): The AST node representing an import statement.
        *   *Returns:* - Analysis data not available for this component.
        *   **Usage:** - Analysis data not available for this component.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent `from ... import ...` statements. It iterates through each alias within the import statement, constructing a fully qualified name (e.g., `module.name`) and appending it to the `imports` list in `self.schema`. Following this, it ensures the AST traversal continues by calling `self.generic_visit(node)`
        *   *Parameters:*
            -   **self** (ASTVisitor): The instance of the ASTVisitor class.
            -   **node** (ast.ImportFrom): The AST node representing a 'from ... import ...' statement.
        *   *Returns:* - Analysis data not available for this component.
        *   **Usage:** - Analysis data not available for this component.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions in the source code. It constructs a unique identifier for the class, extracts its name, docstring, and the relevant source code segment. This information is then stored in a `class_info` dictionary and appended to the `classes` list within `self.schema`. The `_current_class` attribute is temporarily set to this `class_info` to provide context for nested methods, and then reset to `None` after visiting the class's children to maintain correct scope.
        *   *Parameters:*
            -   **self** (ASTVisitor): The instance of the ASTVisitor class.
            -   **node** (ast.ClassDef): The AST node representing a class definition.
        *   *Returns:* - Analysis data not available for this component.
        *   **Usage:** - Analysis data not available for this component.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, representing function definitions. It distinguishes between methods defined within a class and standalone functions. If a class is currently being visited (indicated by `_current_class`), it extracts method details such as identifier, name, arguments, docstring, and line numbers, appending this as `method_context_info` to the current class's context. Otherwise, for standalone functions, it creates a `func_info` dictionary with similar details and appends it to the `functions` list in `self.schema`. Finally, it calls `self.generic_visit(node)` to continue AST traversal.
        *   *Parameters:*
            -   **self** (ASTVisitor): The instance of the ASTVisitor class.
            -   **node** (ast.FunctionDef): The AST node representing a function definition.
        *   *Returns:* - Analysis data not available for this component.
        *   **Usage:** - Analysis data not available for this component.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(node)`
        *   *Description:* This method is designed to process `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation simply delegates the actual processing to the `visit_FunctionDef` method. This ensures that both synchronous and asynchronous functions are handled uniformly for the purpose of schema generation, extracting similar metadata regardless of their asynchronous nature.
        *   *Parameters:*
            -   **self** (ASTVisitor): The instance of the ASTVisitor class.
            -   **node** (ast.AsyncFunctionDef): The AST node representing an asynchronous function definition.
        *   *Returns:* - Analysis data not available for this component.
        *   **Usage:** - Analysis data not available for this component.
---
#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process Python source code within a repository to generate a structured Abstract Syntax Tree (AST) schema and integrate relationship data. It provides methods to parse individual Python files, extract their AST nodes (functions, classes, imports), and then enrich this schema with call graph information (incoming/outgoing calls) and class instantiation details. This class serves as a central component for building a comprehensive understanding of a codebase's structure and interdependencies.
*   **Instantiation:** - Analysis data not available for this component.
*   **Dependencies:** - Analysis data not available for this component.
*   **Constructor:**
    *   *Description:* The constructor for the ASTAnalyzer class. It initializes an instance of the analyzer without requiring any specific parameters or setting up initial state, as indicated by the 'pass' statement.
    *   *Parameters:*
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing calls, into a pre-existing full AST schema. It iterates through each file, function, and class within the provided schema. For functions, it populates their 'calls' and 'called_by' contexts. For classes, it sets 'instantiated_by' and then processes each method within the class to populate its 'calls' and 'called_by' contexts, also identifying external dependencies for the class. The method modifies the 'full_schema' in place to include this relationship information.
        *   *Parameters:*
            -   **full_schema** (dict): The comprehensive schema containing AST nodes for files, functions, and classes, which will be updated with relationship data.
            -   **raw_relationships** (dict): A dictionary containing raw incoming and outgoing call relationships to be merged into the schema.
        *   *Returns:*
            -   **full_schema** (dict): The updated full_schema dictionary with integrated relationship data.
        *   **Usage:** - Analysis data not available for this component.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to construct a detailed AST schema. It first determines the project root and then iterates through the provided files, filtering for Python files with content. For each valid Python file, it parses the content into an Abstract Syntax Tree using the 'ast' module and then employs an ASTVisitor to extract structural information (imports, functions, classes). The extracted nodes are organized into a 'full_schema' dictionary, keyed by file path, and potential parsing errors are caught and logged.
        *   *Parameters:*
            -   **files** (list): A list of file objects, each expected to have 'path' and 'content' attributes representing a file from the repository.
            -   **repo** (GitRepository): An object representing the Git repository, though its direct attributes are not used within this method's provided source code.
        *   *Returns:*
            -   **full_schema** (dict): A dictionary representing the AST schema of the analyzed repository, structured by file paths and containing AST nodes.
        *   **Usage:** - Analysis data not available for this component.
---
### File: `backend/File_Dependency.py`
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a codebase. It initializes a
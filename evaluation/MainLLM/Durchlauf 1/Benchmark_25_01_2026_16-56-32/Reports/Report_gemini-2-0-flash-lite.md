```markdown
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview

- **Description:** 
Could not be determined due to a missing README file and insufficient context.
- **Key Features:** 
  - Total Number of Key Features should not exceed five
- **Tech Stack:** 
- **Repository Structure:**
```mermaid
graph LR
    root --> .env.example
    root --> .gitignore
    root --> SystemPrompts
    SystemPrompts --> SystemPrompts/SystemPromptClassHelperLLM.txt
    SystemPrompts --> SystemPrompts/SystemPromptFunctionHelperLLM.txt
    SystemPrompts --> SystemPrompts/SystemPromptHelperLLM.txt
    SystemPrompts --> SystemPrompts/SystemPromptMainLLM.txt
    SystemPrompts --> SystemPrompts/SystemPromptMainLLMToon.txt
    SystemPrompts --> SystemPrompts/SystemPromptNotebookLLM.txt
    root --> analysis_output.json
    root --> backend
    backend --> backend/AST_Schema.py
    backend --> backend/File_Dependency.py
    backend --> backend/HelperLLM.py
    backend --> backend/MainLLM.py
    backend --> backend/__init__.py
    backend --> backend/basic_info.py
    backend --> backend/callgraph.py
    backend --> backend/converter.py
    backend --> backend/getRepo.py
    backend --> backend/main.py
    backend --> backend/relationship_analyzer.py
    backend --> backend/scads_key_test.py
    root --> database
    database --> database/db.py
    root --> frontend
    frontend --> frontend/.streamlit
    frontend/.streamlit --> frontend/.streamlit/config.toml
    frontend --> frontend/__init__.py
    frontend --> frontend/frontend.py
    frontend --> frontend/gifs
    frontend/gifs --> frontend/gifs/4j.gif
    root --> notizen
    notizen --> notizen/Report Agenda.txt
    notizen --> notizen/Zwischenpraesentation Agenda.txt
    notizen --> notizen/doc_bestandteile.md
    notizen --> notizen/grafiken
    notizen/grafiken --> notizen/grafiken/1
    notizen/grafiken/1 --> notizen/grafiken/1/File_Dependency_Graph_Repo.dot
    notizen/grafiken/1 --> notizen/grafiken/1/global_callgraph.png
    notizen/grafiken/1 --> notizen/grafiken/1/global_graph.png
    notizen/grafiken/1 --> notizen/grafiken/1/global_graph_2.png
    notizen/grafiken/1 --> notizen/grafiken/1/repo.dot
    notizen/grafiken --> notizen/grafiken/2
    notizen/grafiken/2 --> notizen/grafiken/2/FDG_repo.dot
    notizen/grafiken/2 --> notizen/grafiken/2/fdg_graph.png
    notizen/grafiken/2 --> notizen/grafiken/2/fdg_graph_2.png
    notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_flask.png
    notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_repo-agent.png
    notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_repo-agent_3.png
    notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_flask.dot
    notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_repo-agent-3.dot
    notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_repo-agent.dot
    notizen/grafiken/2 --> notizen/grafiken/2/global_callgraph.png
    notizen/grafiken/2 --> notizen/grafiken/2/graph_flask.md
    notizen/grafiken/2 --> notizen/grafiken/2/repo.dot
    notizen/grafiken --> notizen/grafiken/Flask-Repo
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/__init__.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/__main__.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/app.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/auth.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/blog.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/blueprints.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/cli.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/conf.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/config.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/conftest.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/ctx.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/db.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/debughelpers.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/factory.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/flask.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/globals.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/hello.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/helpers.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/importerrorapp.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/logging.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/make_celery.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/multiapp.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/provider.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/scaffold.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/sessions.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/signals.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/tag.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/tasks.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/templating.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_appctx.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_async.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_auth.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_basic.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_blog.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_blueprints.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_cli.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_config.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_config.png
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_converters.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_db.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_factory.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_helpers.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_instance_config.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_js_example.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_json.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_json_tag.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_logging.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_regression.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_reqctx.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_request.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_session_interface.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_signals.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_subclassing.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_templating.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_testing.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_user_error_handler.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_views.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/testing.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_app_decorators.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_error_handler.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_route.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/views.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/wrappers.dot
    notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/wsgi.dot
    notizen/grafiken --> notizen/grafiken/Repo-onboarding
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/AST.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/Frontend.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/HelperLLM.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/HelperLLM.png
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/MainLLM.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/agent.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/basic_info.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/callgraph.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/getRepo.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST.png
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST2.png
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST3.png
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/main.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/tools.dot
    notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/types.dot
    root --> notizen/notizen.md
    root --> notizen/paul_notizen.md
    root --> notizen/praesentation_notizen.md
    root --> notizen/technische_notizen.md
    root --> output.json
    root --> output.toon
    root --> readme.md
    root --> requirements.txt
    root --> result
    result --> result/ast_schema_01_12_2025_11-49-24.json
    result --> result/notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md
    result --> result/notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md
    result --> result/notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md
    result --> result/notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md
    result --> result/notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md
    result --> result/notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md
    result --> result/report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> result/report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> result/report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> result/report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> result/report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> result/report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> result/report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md
    result --> result/report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> result/report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> result/report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md
    result --> result/report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md
    result --> result/report_14_11_2025_14-52-36.md
    result --> result/report_14_11_2025_15-21-53.md
    result --> result/report_14_11_2025_15-26-24.md
    result --> result/report_21_11_2025_15-43-30.md
    result --> result/report_21_11_2025_16-06-12.md
    result --> result/report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md
    result --> result/report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md
    result --> result/result_2025-11-11_12-30-53.md
    result --> result/result_2025-11-11_12-43-51.md
    result --> result/result_2025-11-11_12-45-37.md
    root --> schemas
    schemas --> schemas/types.py
    root --> statistics
    statistics --> statistics/savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png
    statistics --> statistics/savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png
    statistics --> statistics/savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png
    statistics --> statistics/savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png
    statistics --> statistics/savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png
    root --> test.json
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
pip install -r requirements.txt
### Setup Guide
-  Information not found
### Quick Startup
-  Information not found

## 3. Use Cases & Commands
-  Information not found

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to a specified project root. If the file is a Python file, it removes the '.py' extension. Subsequently, it replaces path separators with dots to form the module path. Special handling is included for '__init__.py' files, where the '.__init__' suffix is removed to represent the package itself.
*   **Parameters:**
    - **filepath** (str): The absolute or relative path to the Python file.
    - **project_root** (str): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (str): The converted Python module path string.
*   **Usage:**
    -   *Called by:* backend.AST_Schema.ASTVisitor.__init__, backend.relationship_analyzer.ProjectAnalyzer._collect_definitions
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) of Python source code. Its primary purpose is to extract and structure metadata about imports, classes, and functions found within a given source file. It builds a schema containing lists of imports, functions, and classes, providing a programmatic representation of the code's structure.
*   **Instantiation:** Instantiated by backend.AST_Schema.ASTAnalyzer.analyze_repository
*   **Dependencies:** backend.AST_Schema.path_to_module
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor with the source code, file path, and project root. It calculates the module path, sets up an empty schema dictionary to store extracted information, and initializes `_current_class` to `None` for tracking the current class context during AST traversal.
    *   *Parameters:*
        - **self** (str): 
        - **source_code** (str): The raw source code of the file being analyzed.
        - **file_path** (str): The absolute path to the Python file being visited.
        - **project_root** (str): The root directory of the project, used to determine the module path.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self: str, source_code: str, file_path: str, project_root: str)`
        *   *Description:* The constructor initializes the ASTVisitor with the source code, file path, and project root. It calculates the module path, sets up an empty schema dictionary to store extracted information, and initializes `_current_class` to `None` for tracking the current class context during AST traversal.
        *   *Parameters:*
            - **self** (str): 
            - **source_code** (str): The raw source code of the file being analyzed.
            - **file_path** (str): The absolute path to the Python file being visited.
            - **project_root** (str): The root directory of the project, used to determine the module path.
        *   *Returns:*
        *   **Usage:**
            -   *Calls:* backend.AST_Schema.path_to_module
            -   *Called by:* 
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self: str, node: ast.Import)`
        *   *Description:* This method processes `ast.Import` nodes, which represent `import module` statements. It iterates through each alias in the import statement, extracting the module name and appending it to the `self.schema["imports"]` list. After recording the import, it calls `self.generic_visit(node)` to ensure that the AST traversal continues for any child nodes.
        *   *Parameters:*
            - **self** (str): 
            - **node** (ast.Import): The AST node representing an import statement.
        *   *Returns:*
        *   **Usage:**
            -   *Calls:* 
            -   *Called by:* 
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self: str, node: ast.ImportFrom)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which correspond to `from module import name` statements. It constructs fully qualified import names by combining the module name (if present) with each alias name, then appends these to `self.schema["imports"]`. This ensures that specific imports from modules are correctly captured. Finally, it invokes `self.generic_visit(node)` to continue the AST traversal.
        *   *Parameters:*
            - **self** (str): 
            - **node** (ast.ImportFrom): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            -   *Calls:* 
            -   *Called by:* 
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self: str, node: ast.ClassDef)`
        *   *Description:* This method is responsible for processing `ast.ClassDef` nodes, which represent class definitions. It constructs a dictionary containing detailed information about the class, including its identifier, name, docstring, source code segment, and line numbers. This class information is then added to `self.schema["classes"]`, and the `_current_class` attribute is temporarily set to this class's info to provide context for any nested methods. After visiting child nodes via `self.generic_visit(node)`, `_current_class` is reset to `None`.
        *   *Parameters:*
            - **self** (str): 
            - **node** (ast.ClassDef): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            -   *Calls:* 
            -   *Called by:* 
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self: str, node: ast.FunctionDef)`
        *   *Description:* This method processes `ast.FunctionDef` nodes, distinguishing between methods defined within a class and top-level functions. If `_current_class` is set, it means the function is a method, and its details (identifier, name, arguments, docstring, line numbers) are appended to the `method_context` of the current class. Otherwise, it's treated as a standalone function, and its details are added to `self.schema["functions"]`. It ensures proper AST traversal by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **self** (str): 
            - **node** (ast.FunctionDef): The AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            -   *Calls:* 
            -   *Called by:* 
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self: str, node: ast.AsyncFunctionDef)`
        *   *Description:* This method handles `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Instead of implementing its own parsing logic, it delegates the processing directly to the `visit_FunctionDef` method. This approach ensures that both synchronous and asynchronous function definitions are handled uniformly, extracting the same structural and metadata information.
        *   *Parameters:*
            - **self** (str): 
            - **node** (ast.AsyncFunctionDef): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:**
            -   *Calls:* 
            -   *Called by:* 
#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process source code, particularly Python files within a Git repository, to build a structured Abstract Syntax Tree (AST) schema. It can analyze individual files to extract functions, classes, and their internal structures using an ASTVisitor. Additionally, it provides functionality to merge external relationship data, such as call graphs, into the generated AST schema, enriching the structural information with dynamic interaction details.
*   **Instantiation:** Instantiated by backend.main.main_workflow
*   **Dependencies:** backend.AST_Schema.ASTVisitor
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments, effectively creating a stateless instance.
    *   *Parameters:*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute assignments, effectively creating a stateless instance.
        *   *Parameters:*
        *   *Returns:*
        *   **Usage:**
            -   *Calls:* 
            -   *Called by:* 
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict) -> dict`
        *   *Description:* This method integrates raw relationship data, specifically incoming and outgoing calls, into a structured full schema. It iterates through files, functions, and classes within the schema, updating their respective context fields with call and called-by information. For classes, it also calculates and stores external dependencies based on method calls.
        *   *Parameters:*
            - **self** (backend.
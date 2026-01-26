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
        root -->|SystemPrompts| SystemPrompts_dir
        root -->|backend| backend_dir
        root -->|database| database_dir
        root -->|frontend| frontend_dir
        root -->|notizen| notizen_dir
        root -->|.env.example
        root -->|.gitignore
        root -->|analysis_output.json| analysis_output.json_file
        root -->|output.json| output.json_file
        root -->|output.toon| output.toon_file
        root -->|readme.md| readme.md_file
        root -->|requirements.txt| requirements.txt_file
        root -->|result| result_dir
        root -->|schemas| schemas_dir
        root -->|statistics| statistics_dir
        root -->|test.json| test.json_file

        SystemPrompts_dir -->|SystemPromptClassHelperLLM.txt| SystemPromptClassHelperLLM_txt
        SystemPrompts_dir -->|SystemPromptFunctionHelperLLM.txt| SystemPromptFunctionHelperLLM_txt
        SystemPrompts_dir -->|SystemPromptHelperLLM.txt| SystemPromptHelperLLM_txt
        SystemPrompts_dir -->|SystemPromptMainLLM.txt| SystemPromptMainLLM_txt
        SystemPrompts_dir -->|SystemPromptMainLLMToon.txt| SystemPromptMainLLMToon_txt
        SystemPrompts_dir -->|SystemPromptNotebookLLM.txt| SystemPromptNotebookLLM_txt

        backend_dir -->|AST_Schema.py| AST_Schema_py
        backend_dir -->|File_Dependency.py| File_Dependency_py
        backend_dir -->|HelperLLM.py| HelperLLM_py
        backend_dir -->|MainLLM.py| MainLLM_py
        backend_dir -->|__init__.py| __init___py
        backend_dir -->|basic_info.py| basic_info_py
        backend_dir -->|callgraph.py| callgraph_py
        backend_dir -->|converter.py| converter_py
        backend_dir -->|getRepo.py| getRepo_py
        backend_dir -->|main.py| main_py
        backend_dir -->|relationship_analyzer.py| relationship_analyzer_py
        backend_dir -->|scads_key_test.py| scads_key_test_py

        database_dir -->|db.py| db_py

        frontend_dir -->|.streamlit| .streamlit_dir
        frontend_dir -->|__init__.py| frontend___init___py
        frontend_dir -->|frontend.py| frontend_py
        frontend_dir -->|gifs| gifs_dir

        .streamlit_dir -->|config.toml| config_toml
        gifs_dir -->|4j.gif| 4j_gif

        notizen_dir -->|Report Agenda.txt| Report_Agenda_txt
        notizen_dir -->|Zwischenpraesentation Agenda.txt| Zwischenpraesentation_Agenda_txt
        notizen_dir -->|doc_bestandteile.md| doc_bestandteile_md
        notizen_dir -->|grafiken| grafiken_dir
        notizen_dir -->|notizen.md| notizen_md
        notizen_dir -->|paul_notizen.md| paul_notizen_md
        notizen_dir -->|praesentation_notizen.md| praesentation_notizen_md
        notizen_dir -->|technische_notizen.md| technische_notizen_md

        grafiken_dir -->|"1"| grafiken_1_dir
        grafiken_dir -->|"2"| grafiken_2_dir
        grafiken_dir -->|Flask-Repo| Flask_Repo_dir
        grafiken_dir -->|Repo-onboarding| Repo_onboarding_dir

        grafiken_1_dir -->|File_Dependency_Graph_Repo.dot| File_Dependency_Graph_Repo_dot
        grafiken_1_dir -->|global_callgraph.png| global_callgraph_png
        grafiken_1_dir -->|global_graph.png| global_graph_png
        grafiken_1_dir -->|global_graph_2.png| global_graph_2_png
        grafiken_1_dir -->|repo.dot| repo_dot

        grafiken_2_dir -->|FDG_repo.dot| FDG_repo_dot
        grafiken_2_dir -->|fdg_graph.png| fdg_graph_png
        grafiken_2_dir -->|fdg_graph_2.png| fdg_graph_2_png
        grafiken_2_dir -->|filtered_callgraph_flask.png| filtered_callgraph_flask_png
        grafiken_2_dir -->|filtered_callgraph_repo-agent.png| filtered_callgraph_repo_agent_png
        grafiken_2_dir -->|filtered_callgraph_repo-agent_3.png| filtered_callgraph_repo_agent_3_png
        grafiken_2_dir -->|filtered_repo_callgraph_flask.dot| filtered_repo_callgraph_flask_dot
        grafiken_2_dir -->|filtered_repo_callgraph_repo-agent-3.dot| filtered_repo_callgraph_repo_agent_3_dot
        grafiken_2_dir -->|filtered_repo_callgraph_repo-agent.dot| filtered_repo_callgraph_repo_agent_dot
        grafiken_2_dir -->|global_callgraph.png| global_callgraph_2_png
        grafiken_2_dir -->|graph_flask.md| graph_flask_md
        grafiken_2_dir -->|repo.dot| repo_2_dot

        Flask_Repo_dir -->|__init__.dot| __init___dot
        Flask_Repo_dir -->|__main__.dot| __main___dot
        Flask_Repo_dir -->|app.dot| app_dot
        Flask_Repo_dir -->|auth.dot| auth_dot
        Flask_Repo_dir -->|blog.dot| blog_dot
        Flask_Repo_dir -->|blueprints.dot| blueprints_dot
        Flask_Repo_dir -->|cli.dot| cli_dot
        Flask_Repo_dir -->|conf.dot| conf_dot
        Flask_Repo_dir -->|config.dot| config_dot
        Flask_Repo_dir -->|conftest.dot| conftest_dot
        Flask_Repo_dir -->|ctx.dot| ctx_dot
        Flask_Repo_dir -->|db.dot| db_dot
        Flask_Repo_dir -->|debughelpers.dot| debughelpers_dot
        Flask_Repo_dir -->|factory.dot| factory_dot
        Flask_Repo_dir -->|flask.dot| flask_dot
        Flask_Repo_dir -->|globals.dot| globals_dot
        Flask_Repo_dir -->|hello.dot| hello_dot
        Flask_Repo_dir -->|helpers.dot| helpers_dot
        Flask_Repo_dir -->|importerrorapp.dot| importerrorapp_dot
        Flask_Repo_dir -->|logging.dot| logging_dot
        Flask_Repo_dir -->|make_celery.dot| make_celery_dot
        Flask_Repo_dir -->|multiapp.dot| multiapp_dot
        Flask_Repo_dir -->|provider.dot| provider_dot
        Flask_Repo_dir -->|scaffold.dot| scaffold_dot
        Flask_Repo_dir -->|sessions.dot| sessions_dot
        Flask_Repo_dir -->|signals.dot| signals_dot
        Flask_Repo_dir -->|tag.dot| tag_dot
        Flask_Repo_dir -->|tasks.dot| tasks_dot
        Flask_Repo_dir -->|templating.dot| templating_dot
        Flask_Repo_dir -->|test_appctx.dot| test_appctx_dot
        Flask_Repo_dir -->|test_async.dot| test_async_dot
        Flask_Repo_dir -->|test_auth.dot| test_auth_dot
        Flask_Repo_dir -->|test_basic.dot| test_basic_dot
        Flask_Repo_dir -->|test_blog.dot| test_blog_dot
        Flask_Repo_dir -->|test_blueprints.dot| test_blueprints_dot
        Flask_Repo_dir -->|test_cli.dot| test_cli_dot
        Flask_Repo_dir -->|test_config.dot| test_config_dot
        Flask_Repo_dir -->|test_config.png| test_config_png
        Flask_Repo_dir -->|test_converters.dot| test_converters_dot
        Flask_Repo_dir -->|test_db.dot| test_db_dot
        Flask_Repo_dir -->|test_factory.dot| test_factory_dot
        Flask_Repo_dir -->|test_helpers.dot| test_helpers_dot
        Flask_Repo_dir -->|test_instance_config.dot| test_instance_config_dot
        Flask_Repo_dir -->|test_js_example.dot| test_js_example_dot
        Flask_Repo_dir -->|test_json.dot| test_json_dot
        Flask_Repo_dir -->|test_json_tag.dot| test_json_tag_dot
        Flask_Repo_dir -->|test_logging.dot| test_logging_dot
        Flask_Repo_dir -->|test_regression.dot| test_regression_dot
        Flask_Repo_dir -->|test_reqctx.dot| test_reqctx_dot
        Flask_Repo_dir -->|test_request.dot| test_request_dot
        Flask_Repo_dir -->|test_session_interface.dot| test_session_interface_dot
        Flask_Repo_dir -->|test_signals.dot| test_signals_dot
        Flask_Repo_dir -->|test_subclassing.dot| test_subclassing_dot
        Flask_Repo_dir -->|test_templating.dot| test_templating_dot
        Flask_Repo_dir -->|test_testing.dot| test_testing_dot
        Flask_Repo_dir -->|test_user_error_handler.dot| test_user_error_handler_dot
        Flask_Repo_dir -->|test_views.dot| test_views_dot
        Flask_Repo_dir -->|testing.dot| testing_dot
        Flask_Repo_dir -->|typing.dot| typing_dot
        Flask_Repo_dir -->|typing_app_decorators.dot| typing_app_decorators_dot
        Flask_Repo_dir -->|typing_error_handler.dot| typing_error_handler_dot
        Flask_Repo_dir -->|typing_route.dot| typing_route_dot
        Flask_Repo_dir -->|views.dot| views_dot
        Flask_Repo_dir -->|wrappers.dot| wrappers_dot
        Flask_Repo_dir -->|wsgi.dot| wsgi_dot

        Repo_onboarding_dir -->|AST.dot| AST_dot
        Repo_onboarding_dir -->|Frontend.dot| Frontend_dot
        Repo_onboarding_dir -->|HelperLLM.dot| HelperLLM_dot
        Repo_onboarding_dir -->|HelperLLM.png| HelperLLM_png
        Repo_onboarding_dir -->|MainLLM.dot| MainLLM_dot
        Repo_onboarding_dir -->|agent.dot| agent_dot
        Repo_onboarding_dir -->|basic_info.dot| basic_info_dot
        Repo_onboarding_dir -->|callgraph.dot| callgraph_dot
        Repo_onboarding_dir -->|getRepo.dot| getRepo_dot
        Repo_onboarding_dir -->|graph_AST.png| graph_AST_png
        Repo_onboarding_dir -->|graph_AST2.png| graph_AST2_png
        Repo_onboarding_dir -->|graph_AST3.png| graph_AST3_png
        Repo_onboarding_dir -->|main.dot| main_dot
        Repo_onboarding_dir -->|tools.dot| tools_dot
        Repo_onboarding_dir -->|types.dot| types_dot

        result_dir -->|ast_schema_01_12_2025_11-49-24.json| ast_schema_01_12_2025_11_49_24_json
        result_dir -->|notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md| notebook_report_23_12_2025_12_56_24_md
        result_dir -->|notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md| notebook_report_27_12_2025_15_06_09_md
        result_dir -->|notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md| notebook_report_27_12_2025_15_09_29_md
        result_dir -->|notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md| notebook_report_27_12_2025_15_26_34_md
        result_dir -->|notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md| notebook_report_27_12_2025_15_33_06_md
        result_dir -->|notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md| notebook_report_29_12_2025_15_03_21_md
        result_dir -->|report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| report_01_12_2025_12_26_46_md
        result_dir -->|report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| report_01_12_2025_12_55_01_md
        result_dir -->|report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| report_01_12_2025_13_37_30_md
        result_dir -->|report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md| report_01_12_2025_14_15_04_md
        result_dir -->|report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md| report_01_12_2025_14_42_38_md
        result_dir -->|report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md| report_01_12_2025_15_27_23_md
        result_dir -->|report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md| report_02_12_2025_15_41_27_md
        result_dir -->|report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| report_03_12_2025_22_46_01_md
        result_dir -->|report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| report_03_12_2025_23_13_20_md
        result_dir -->|report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md| report_05_12_2025_11_07_10_md
        result_dir -->|report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md| report_09_12_2025_14_07_49_md
        result_dir -->|report_14_11_2025_14-52-36.md| report_14_11_2025_14_52_36_md
        result_dir -->|report_14_11_2025_15-21-53.md| report_14_11_2025_15_21_53_md
        result_dir -->|report_14_11_2025_15-26-24.md| report_14_11_2025_15_26_24_md
        result_dir -->|report_21_11_2025_15-43-30.md| report_21_11_2025_15_43_30_md
        result_dir -->|report_21_11_2025_16-06-12.md| report_21_11_2025_16_06_12_md
        result_dir -->|report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md| report_22_11_2025_14_01_50_md
        result_dir -->|report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md| report_22_11_2025_14_39_55_md
        result_dir -->|result_2025-11-11_12-30-53.md| result_2025_11_11_12_30_53_md
        result_dir -->|result_2025-11-11_12-43-51.md| result_2025_11_11_12_43_51_md
        result_dir -->|result_2025-11-11_12-45-37.md| result_2025_11_11_12_45_37_md

        schemas_dir -->|types.py| types_py

        statistics_dir -->|savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png| savings_01_12_2025_15_27_23_png
        statistics_dir -->|savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png| savings_02_12_2025_15_41_27_png
        statistics_dir -->|savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png| savings_03_12_2025_23_13_20_png
        statistics_dir -->|savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png| savings_05_12_2025_11_07_10_png
        statistics_dir -->|savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png| savings_09_12_2025_14_07_49_png

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

Repo contains requirements.txt. Install dependencies using: `pip install -r requirements.txt`
### Setup Guide
Information not found
### Quick Startup
Information not found

## 3. Use Cases & Commands
This project appears to be an AI-powered onboarding agent for software repositories. It clones repositories, analyzes their code structure, dependencies, and call graphs, and then uses Large Language Models (LLMs) to generate comprehensive documentation. It can also process Jupyter notebooks within a repository, converting them to an XML format and extracting image data for analysis.

Primary commands and workflows likely involve:
- Providing a GitHub repository URL to the application.
- The application cloning the repository and performing static code analysis.
- Utilizing LLMs (like Gemini, GPT, or Ollama) to generate documentation for functions, classes, and the overall repository.
- Processing and documenting Jupyter notebooks.
- Storing user information, API keys, and chat history in a database.
- Providing a Streamlit-based frontend for user interaction, including chat history management and API key configuration.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends ast.NodeVisitor to traverse an Abstract Syntax Tree (AST) of Python code. Its primary purpose is to extract structured information about imports, functions, and classes from the provided source code. It builds a schema dictionary that categorizes these code elements, distinguishing between top-level functions and methods nested within classes, providing a foundational structure for code analysis.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class depends on the 'ast' module for its core functionality and 'path_to_module' for path manipulation.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the ASTVisitor instance by storing the raw source code, the file's absolute path, and the project's root directory. It calculates the module path based on these inputs and sets up an empty schema dictionary to accumulate discovered imports, functions, and classes. It also initializes an internal attribute, _current_class, to None, which is used to track the class context during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code string of the file being analyzed.
        - **file_path** (`str`): The absolute file path of the Python module being visited.
        - **project_root** (`str`): The root directory of the entire project, used for calculating module paths.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(...)`
        *   *Description:* This method processes 'ast.Import' nodes, which represent simple import statements like 'import module'. It iterates through each alias defined in the import statement and appends the module name to the 'imports' list within the class's schema. After processing the current node, it calls 'self.generic_visit' to ensure continued traversal of the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an 'import' statement.
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.Import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(...)`
        *   *Description:* This method handles 'ast.ImportFrom' nodes, which correspond to 'from module import name' statements. It iterates through the imported aliases and constructs a fully qualified import string (e.g., 'module.name'), which is then appended to the 'imports' list in the class's schema. Following this, it invokes 'self.generic_visit' to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.ImportFrom node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(...)`
        *   *Description:* This method processes 'ast.ClassDef' nodes, which represent class definitions in the source code. It constructs a unique identifier for the class, extracts its name, docstring, and the source code segment. It then creates a 'class_info' dictionary, populates it with these details, and appends it to the 'classes' list in the schema. The method temporarily sets '_current_class' to this 'class_info' to correctly associate any nested methods, performs a generic visit to traverse the class's body, and then resets '_current_class' to None.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.ClassDef node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(...)`
        *   *Description:* This method processes 'ast.FunctionDef' nodes, representing function definitions. It first checks if a class is currently being visited (i.e., '_current_class' is not None). If a class context exists, the function is treated as a method, and its details are appended to the 'method_context' of the current class. Otherwise, it's considered a top-level function, and its information is added to the 'functions' list in the schema. Finally, it calls 'self.generic_visit' to continue traversing the function's body.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition (either top-level or a method).
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.FunctionDef node is encountered, and explicitly called by visit_AsyncFunctionDef.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(...)`
        *   *Description:* This method is specifically designed to handle 'ast.AsyncFunctionDef' nodes, which represent asynchronous function definitions. Its implementation simply delegates the processing to the 'visit_FunctionDef' method. This ensures that both synchronous and asynchronous functions are processed using the same logic for schema generation, avoiding code duplication.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.AsyncFunctionDef node is encountered.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process and analyze Python source code within a repository to generate a structured Abstract Syntax Tree (AST) schema. It provides functionalities to parse Python files, extract their structural components (imports, functions, classes), and then integrate relationship data (like calls and dependencies) into this schema. This class serves as a core component for understanding the structure and interdependencies of a Python codebase.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class has no explicitly listed external functional dependencies.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It currently does not perform any specific setup or attribute assignments, serving as a placeholder or indicating that no initial state is required.
    *   *Parameters:*
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(full_schema, raw_relationships)`
        *   *Description:* This method integrates raw relationship data (incoming and outgoing calls) into a structured full schema. It iterates through functions and classes within the schema's AST nodes, populating their respective 'calls', 'called_by', and 'instantiated_by' contexts. For classes, it also identifies and lists external dependencies based on method calls that are not internal to the class, ensuring a comprehensive view of inter-component relationships.
        *   *Parameters:*
            - **full_schema** (`dict`): The complete schema structure, expected to contain file data with AST nodes for functions and classes.
            - **raw_relationships** (`dict`): A dictionary containing 'outgoing' and 'incoming' call relationships, typically mapping identifiers to lists of related entities.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary, now enriched with relationship data.
        *   *Usage:* This method calls no other methods, classes, or functions.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(files, repo)`
        *   *Description:* This method processes a list of file objects from a Git repository to build an Abstract Syntax Tree (AST) schema for Python files. It initializes a 'full_schema' dictionary, determines the project root, and then iterates through each file. For Python files, it parses their content into an AST, uses an ASTVisitor to extract schema nodes (imports, functions, classes), and populates the 'full_schema' with this information, handling parsing errors gracefully.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though its specific usage is not detailed within this method's body.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed Python files, organized by file path.
        *   *Usage:* This method calls `os.path.commonpath`, `os.path.isfile`, `os.path.dirname`, `ast.parse`, and instantiates and calls the `visit` method of `ASTVisitor`.

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is an AST NodeVisitor designed to build a graph of file-level import dependencies within a Python repository. It traverses the Abstract Syntax Tree of Python files to identify 'import' and 'from ... import ...' statements. The class handles both absolute and complex relative imports by checking file existence and `__init__.py` exports. It maintains a dictionary, `import_dependencies`, mapping filenames to sets of modules they import, providing a structured representation of file-level dependencies.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class has no explicitly listed external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This constructor initializes the FileDependencyGraph instance. It takes the `filename` of the Python file currently being analyzed and the `repo_root` directory as arguments, storing them as instance attributes for later use in resolving dependencies.
    *   *Parameters:*
        - **filename** (`str`): The path to the Python file currently being analyzed for dependencies.
        - **repo_root** (`Any`): The root directory of the repository, used as a base for resolving file paths and imports.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This method is responsible for resolving relative Python imports, such as `from .. import name1, name2`. It calculates the correct base directory for the import based on the `node.level` and the current file's path. It then uses two internal helper functions, `module_file_exists` and `init_exports_symbol`, to verify if the imported names correspond to actual files or symbols exported by `__init__.py` files. The method returns a list of successfully resolved module or symbol names, raising an `ImportError` if no valid resolutions are found.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement to be resolved.
        *   *Returns:*
            - **resolved** (`list[str]`): A list of strings, where each string is a successfully resolved module or symbol name.
        *   *Usage:* This method calls `get_all_temp_files`, `Path`, `Path.stem`, `Path.name`, `Path.parent`, `Path.resolve`, `Path.exists`, `Path.read_text`, `parse`, `walk`, `isinstance`, `literal_eval`, `iskeyword`, `print`. It also internally defines and calls `module_file_exists` and `init_exports_symbol`.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name=None)`
        *   *Description:* This method is part of the AST `NodeVisitor` pattern, specifically designed to process `Import` or `ImportFrom` AST nodes. It records the imported module or symbol as a dependency for the current file, identified by `self.filename`, within the `self.import_dependencies` dictionary. If an optional `base_name` is provided, it uses that; otherwise, it defaults to the alias name from the import node. After processing the import, it calls `self.generic_visit(node)` to continue the AST traversal.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing either an 'import' or 'from ... import ...' statement.
            - **base_name** (`str | None`): An optional base name for the module, typically used when resolving 'from ... import ...' statements to specify the module part.
        *   *Returns:*
        *   *Usage:* This method calls `self.generic_visit` and accesses `self.import_dependencies`.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `ImportFrom` AST nodes, which represent 'from ... import ...' statements. If the import has an explicit module name (e.g., `from a.b.c import d`), it extracts the last component of the module name and passes it to `visit_Import`. For relative imports (e.g., `from .. import x`), it attempts to resolve the module names using the `_resolve_module_name` method. If resolution is successful, it calls `visit_Import` for each resolved base name; otherwise, it prints an error message. Finally, it ensures continued AST traversal by calling `self.generic_visit(node)`.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   *Usage:* This method calls `self._resolve_module_name`, `self.visit_Import`, `print`, and `self.generic_visit`.

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies within a given Python Abstract Syntax Tree (AST). It initializes a networkx.DiGraph object to store these relationships. It leverages a FileDependencyGraph visitor to traverse the provided AST, collecting import relationships between files. The function then iterates through the collected dependencies, adding nodes for both importing and imported files, and creating directed edges from the importing files to their respective imported files. The resulting graph illustrates which files depend on which others.
*   **Parameters:**
    - **filename** (`str`): The path or name of the file being analyzed for dependencies.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
    - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies between them.
*   **Usage:** This function calls no other functions.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function constructs a directed graph representing the file-level dependencies within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses the file's content into an Abstract Syntax Tree (AST) and then uses a helper function, `build_file_dependency_graph`, to create a dependency graph for that specific file. Finally, it aggregates the nodes and edges from these individual file graphs into a single, global NetworkX directed graph, which is then returned.
*   **Parameters:**
    - **repository** (`GitRepository`): The GitRepository object representing the repository to be analyzed for file dependencies.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph (DiGraph) where nodes represent files or components within files, and edges represent dependencies between them, aggregated across the entire repository.
*   **Usage:** This function calls no other functions.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function identifies all Python files within a specified directory and its subdirectories. It takes a directory path as input, converts it into an absolute `pathlib.Path` object, and then recursively searches for all files ending with the '.py' extension. For each discovered Python file, its path is converted to be relative to the initial root directory. The function then returns a list containing these relative `pathlib.Path` objects.
*   **Parameters:**
    - **directory** (`str`): The string path to the root directory from which to start the recursive search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each object represents a Python file found within the specified directory or its subdirectories, with paths relative to the input `directory`.
*   **Usage:** This function calls no other functions.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various large language models (LLMs) to generate structured documentation for Python functions and classes. It abstracts away the complexities of LLM API calls, including model selection, prompt management, batch processing, and rate limiting. The class is designed to ensure robust and validated output by leveraging Pydantic schemas for both input and output, making it a reliable component for automated code documentation generation.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** The class depends on `os`, `json`, `logging`, `time`, `typing.List`, `typing.Dict`, `typing.Any`, `typing.Optional`, `typing.Union`, `dotenv.load_dotenv`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`, `langchain.messages.AIMessage`, `pydantic.ValidationError`, `schemas.types.FunctionAnalysis`, `schemas.types.ClassAnalysis`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, `schemas.types.ClassAnalysisInput`, and `schemas.types.ClassContextInput`.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by setting up the API key, loading system prompts from specified file paths, configuring batch processing settings based on the LLM model name, and initializing various LangChain LLM clients (Google Gemini, OpenAI, custom API, or Ollama) with structured output capabilities for FunctionAnalysis and ClassAnalysis schemas. It ensures essential parameters are provided and handles file loading errors.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the chosen LLM service (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt for function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt for class analysis.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
        - **base_url** (`str`): The base URL for custom LLM endpoints like Ollama or custom OpenAI-compatible APIs, or None if not applicable.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method dynamically sets the `batch_size` attribute for the LLM operations based on the provided `model_name`. It assigns specific batch sizes for various Gemini, Llama, and GPT models, as well as for custom or unknown models, to optimize API calls and respect rate limits. If an unknown model is encountered, it logs a warning and uses a conservative default batch size.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other methods or functions within its source code.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates and validates documentation for a list of functions by interacting with the configured LLM. It takes a list of FunctionAnalysisInput objects, converts them into JSON payloads, and then sends them to the `function_llm` in batches. It handles potential errors during batch processing by extending the results with None for failed items and includes a waiting period between batches to manage API rate limits. The method returns a list of FunctionAnalysis objects or None for failed generations.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing function details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of FunctionAnalysis objects, where each object represents the generated and validated documentation for a function, or None if generation failed for that specific function.
        *   *Usage:* The input context does not specify where this method is called.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating and validating documentation for a batch of classes using the `class_llm`. It processes a list of ClassAnalysisInput objects, serializes them into JSON payloads, and constructs conversation messages with the class system prompt. The method then sends these conversations to the LLM in batches, managing concurrency and rate limits. It includes error handling to log failures and ensures that the output list maintains the order of inputs, returning None for any class documentation that could not be generated.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing class details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of ClassAnalysis objects, where each object represents the generated and validated documentation for a class, or None if generation failed for that specific class.
        *   *Usage:* The input context does not specify where this method is called.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function acts as a test orchestrator for the LLMHelper class, defining pre-computed analysis data for various functions and classes. It simulates the process of generating documentation by initializing an LLMHelper instance with API keys and prompt paths. The function then feeds predefined function analysis inputs to the helper and processes the simulated results, logging successful generations and aggregating them into a final documentation structure. Its primary purpose is to validate the LLMHelper's interaction with Pydantic models and its documentation generation flow.
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function calls no other functions.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a versatile interface for interacting with various Large Language Models (LLMs). It abstracts away the complexities of different LLM providers by dynamically initializing the appropriate client (Gemini, OpenAI, or Ollama) based on configuration. The class manages a system prompt loaded from a file and offers both single-response (`call_llm`) and streaming (`stream_llm`) capabilities, making it a central component for integrating diverse LLM functionalities into an application.
*   **Instantiation:** This class is not explicitly instantiated by any other components within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by setting up the system prompt from a specified file and configuring the underlying Large Language Model (LLM) client. It supports various LLM providers like Gemini, OpenAI-compatible APIs, and Ollama, dynamically selecting the appropriate client based on the `model_name` and an optional `base_url`. It also performs validation for the API key and ensures the prompt file exists.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        - **prompt_file_path** (`str`): The file path to the system prompt that will be used for LLM interactions.
        - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This parameter determines which LLM client (Gemini, OpenAI, Ollama) is initialized.
        - **base_url** (`str | None`): An optional base URL for custom LLM endpoints, particularly for Ollama or OpenAI-compatible services. If not provided, it defaults to `OLLAMA_BASE_URL` for Ollama models.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method sends a user input to the configured LLM and retrieves a single, complete response. It constructs a list of messages including the class's system prompt and the user's query, then invokes the LLM client. The method includes basic error handling, logging any exceptions during the LLM call and returning `None` in case of failure.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM for a single response.
        *   *Returns:*
            - **response.content** (`str | None`): The content of the LLM's response as a string, or `None` if an error occurred during the call.
        *   *Usage:* This method calls no other functions or methods within the provided context.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method provides a streaming interface to the LLM, allowing for real-time processing of responses as they are generated. It constructs messages similar to `call_llm` but utilizes the LLM client's `stream` method to yield chunks of content. This is particularly useful for applications requiring immediate feedback or handling large responses incrementally. Error handling is included to yield an error message string if the streaming process encounters an exception.
        *   *Parameters:*
            - **user_input** (`str`): The user's query or message to be sent to the LLM for streaming.
        *   *Returns:*
            - **chunk.content** (`Generator[str, None, None]`): A generator that yields chunks of the LLM's response content as strings, or an error message string if an exception occurs during streaming.
        *   *Usage:* This method calls no other functions or methods within the provided context.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to comprehensively extract and consolidate fundamental project information from common project files such as README.md, pyproject.toml, and requirements.txt. It initializes a structured dictionary to store details like project title, description, features, tech stack, status, installation instructions, and dependencies, using placeholders for missing information. Through a series of private parsing methods, it intelligently processes these files, prioritizing structured data sources like pyproject.toml over less structured ones like README.md, and provides a unified view of the project's basic metadata.
*   **Instantiation:** This class is not explicitly instantiated by any known components in the provided context.
*   **Dependencies:** The class relies on the re module for regular expression operations, the os module for path manipulation, and the tomllib module for parsing TOML files. It also uses typing for type hints.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the ProjektInfoExtractor instance. It sets a constant INFO_NICHT_GEFUNDEN string and creates a nested dictionary self.info to store extracted project details, pre-populating all fields with the "Information not found" placeholder.
    *   *Parameters:*
        - **self** (`ProjektInfoExtractor`): The instance of the class.
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content)`
        *   *Description:* This private helper method is designed to sanitize string content by removing null bytes (\\x00). Null bytes can appear in text due to encoding mismatches, such as reading a UTF-16 encoded file as UTF-8. The method first checks if the input content is empty and returns an empty string if so; otherwise, it performs a string replacement operation to eliminate all occurrences of null bytes.
        *   *Parameters:*
            - **content** (`str`): The string content to be cleaned.
        *   *Returns:*
            - **""** (`str`): The cleaned string content without null bytes.
        *   *Usage:* This method does not explicitly call other functions or methods.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches for a specific file within a list of files based on a set of provided patterns. It iterates through each file and then through each pattern, performing a case-insensitive check to see if the file's path ends with any of the given patterns. If a match is found, the corresponding file object is returned immediately. If no file matches any of the patterns after checking all possibilities, the method returns None.
        *   *Parameters:*
            - **patterns** (`List[str]`): A list of string patterns to match against file paths.
            - **dateien** (`List[Any]`): A list of file objects, each expected to have a path attribute.
        *   *Returns:*
            - **""** (`Optional[Any]`): The file object that matches one of the patterns, or None if no match is found.
        *   *Usage:* This method calls `_finde_datei`.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private method extracts text content located directly beneath a specified Markdown level 2 heading (e.g., ## Heading). It constructs a regular expression pattern dynamically based on a list of keywords, allowing it to match any of the provided keywords in a case-insensitive manner. The regex captures all content following the matched heading until the next level 2 heading or the end of the input string. The extracted text is then stripped of leading/trailing whitespace before being returned.
        *   *Parameters:*
            - **inhalt** (`str`): The Markdown content string to parse.
            - **keywords** (`List[str]`): A list of keywords (e.g., "Features", "Status") to look for in Markdown headings.
        *   *Returns:*
            - **""** (`Optional[str]`): The extracted text content under the matched Markdown heading, or None if no matching section is found.
        *   *Usage:* This method calls `re.escape`, `re.compile`, and `re.search`.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This private method is responsible for parsing the content of a README file to extract various project details. It first cleans the content using _clean_content. It then attempts to extract the project title and a fallback description using regular expressions. Subsequently, it utilizes _extrahiere_sektion_aus_markdown to find and extract specific sections like "Key Features", "Tech Stack", "Status", "Installation/Setup", and "Quick Start Guide" from the Markdown content, updating the self.info dictionary with the found information.
        *   *Parameters:*
            - **inhalt** (`str`): The raw content of the README file.
        *   *Returns:*
        *   *Usage:* This method calls `self._clean_content`, `re.search`, and `self._extrahiere_sektion_aus_markdown`.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project metadata. It begins by cleaning the input content using _clean_content. It then checks for the availability of the tomllib module and issues a warning if it's not installed, preventing further parsing. If tomllib is available, it attempts to load the TOML content, extract the project name, description, and dependencies from the [project] table, and update the self.info dictionary accordingly. It includes error handling for tomllib.TOMLDecodeError during parsing.
        *   *Parameters:*
            - **inhalt** (`str`): The raw content of the pyproject.toml file.
        *   *Returns:*
        *   *Usage:* This method calls `self._clean_content`, `tomllib.loads`, `data.get`, and handles `tomllib.TOMLDecodeError`. It also uses `print` for warnings.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This private method parses the content of a requirements.txt file to identify project dependencies. It first cleans the input content using _clean_content. It then checks if dependencies have already been found and stored in self.info (e.g., from a pyproject.toml file); if not, it proceeds to extract dependencies. It splits the content into lines, filters out empty lines and comments, and stores the cleaned dependency strings in the self.info dictionary.
        *   *Parameters:*
            - **inhalt** (`str`): The raw content of the requirements.txt file.
        *   *Returns:*
        *   *Usage:* This method calls `self._clean_content`.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This is the main public method that orchestrates the extraction of project information from various files. It first uses _finde_datei to locate README, pyproject.toml, and requirements.txt files within the provided list of files. It then parses these files in a prioritized order: pyproject.toml first, then requirements.txt, and finally README.md, ensuring that information from more structured files (TOML) takes precedence. After parsing, it formats the extracted dependencies and, if no project title was found, attempts to derive one from the repo_url. Finally, it returns the self.info dictionary containing all gathered project details.
        *   *Parameters:*
            - **dateien** (`List[Any]`): A list of file objects, each expected to have path and content attributes.
            - **repo_url** (`str`): The URL of the repository, used as a fallback for the project title.
        *   *Returns:*
            - **""** (`Dict[str, Any]`): A dictionary containing all extracted project information, structured into "projekt_uebersicht" and "installation" sections.
        *   *Usage:* This method calls `self._finde_datei`, `self._parse_toml`, `self._parse_requirements`, `self._parse_readme`, `os.path.basename`, and `repo_url.removesuffix`.

### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST (Abstract Syntax Tree) visitor designed to construct a call graph for a given Python source file. It traverses the AST, identifying function and class definitions, import statements, and function calls. By maintaining context of the current file, class, and function, it resolves fully qualified names for calls and builds a directed graph representing the relationships between functions and methods.
*   **Instantiation:** This class is not explicitly instantiated by any other components based on the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph instance by setting up the filename for analysis, tracking the current function and class contexts during AST traversal, and initializing various data structures. These structures include dictionaries for local definitions and import mappings, a NetworkX graph to store the call graph, a set for all encountered function names, and a dictionary to store call edges.
    *   *Parameters:*
        - **filename** (`str`): The path to the source file being analyzed by the call graph generator.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively traverses an Abstract Syntax Tree (AST) node, specifically looking for `ast.Call`, `ast.Name`, or `ast.Attribute` nodes. Its purpose is to extract the components of a function or method call, such as `['pkg', 'mod', 'Class', 'method']`, which can then be used to form a fully qualified name. It returns a list of strings representing these name components.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node to be processed, typically an ast.Call, ast.Name, or ast.Attribute.
        *   *Returns:*
            - **name_components** (`list[str]`): A list of strings representing the dotted name components of the call.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* This private method takes a list of potential callee name components (e.g., `[['module', 'function']]`) and attempts to resolve them into fully qualified names. It first checks `self.local_defs` for local function/method definitions, then `self.import_mapping` for imported names, and finally constructs a full name based on the current file and class context if no other resolution is found. This ensures that call targets are correctly identified within the project's scope.
        *   *Parameters:*
            - **callee_nodes** (`list[list[str]]`): A list where each inner list contains the name components of a potential callee.
        *   *Returns:*
            - **resolved_callees** (`list[str]`): A list of fully qualified names for the resolved callees.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name=None)`
        *   *Description:* This private helper method constructs a fully qualified name for a given base name, incorporating the filename and an optional class name. This is crucial for creating unique identifiers for functions and methods within the call graph, distinguishing between functions in different files or methods within different classes.
        *   *Parameters:*
            - **basename** (`str`): The base name of the function or method (e.g., 'my_function').
            - **class_name** (`str | None`): The name of the class if the function is a method, or None otherwise.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name (e.g., 'filename::ClassName::methodName' or 'filename::functionName').
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private helper method determines the identifier of the current calling context. If `self.current_function` is set, it returns that value, indicating a function or method is currently being visited. Otherwise, it returns a placeholder string, either '<filename>' if a filename is available or '<global-scope>' if not, to represent calls made from the global scope.
        *   *Parameters:*
        *   *Returns:*
            - **caller_id** (`str`): The identifier of the current caller context.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method, part of the `ast.NodeVisitor` pattern, processes `ast.Import` nodes. It iterates through the imported modules, extracts their original names and any aliases, and populates `self.import_mapping` to track these imports. This mapping is later used to resolve fully qualified names for imported functions or classes. After processing, it calls `self.generic_visit` to continue AST traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `from ... import ...` statements. It extracts the module name from which objects are imported and then iterates through the specific names being imported (e.g., `from module import name as alias`). It updates `self.import_mapping` with these resolved import paths, which is essential for correctly identifying external function calls. After processing, it calls `self.generic_visit` to continue AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method, part of the `ast.NodeVisitor` pattern, processes `ast.ClassDef` nodes. It temporarily updates `self.current_class` to the name of the class being visited, allowing nested methods to correctly identify their parent class. After visiting all children nodes within the class definition, it restores `self.current_class` to its previous value, ensuring proper context management during AST traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods based on the provided context.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method, part of the `ast.NodeVisitor` pattern, processes `ast.FunctionDef` nodes (regular function definitions). It generates a fully qualified name for the function using `_make_full_name`, updates `self.local_defs` with this mapping, and sets `self.current_function` to track the current context. The function is added as a node to the `self.graph`, and its name is added to `self.function_set`. Finally, it calls `self.generic_visit` to process the function's body and restores the previous function context.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method, part of the `ast.NodeVisitor` pattern, processes `ast.AsyncFunctionDef` nodes (asynchronous function definitions). It delegates the entire processing logic to `visit_FunctionDef`, ensuring that asynchronous functions are handled identically to regular functions in terms of call graph construction and context management.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method, part of the `ast.NodeVisitor` pattern, processes `ast.Call` nodes, which represent function or method calls. It first identifies the caller using `_current_caller`, then extracts the callee's name components using `_recursive_call`, and finally resolves the callee's full name using `_resolve_all_callee_names`. The identified caller and resolved callee are then recorded as an edge in `self.edges`, building the call graph. After processing the call, it calls `self.generic_visit` to continue AST traversal.
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method, part of the `ast.NodeVisitor` pattern, processes `ast.If` nodes. It includes special handling for the `if __name__ == "__main__":` block. When such a block is detected, it temporarily sets `self.current_function` to `<main_block>` before visiting the nodes within that block, allowing calls originating from the main execution block to be correctly attributed in the call graph. For other `if` statements, it simply continues the generic AST traversal.
        *   *Parameters:*
            - **node** (`ast.If`): The AST node representing an 'if' statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function takes a NetworkX directed graph and an output file path. Its purpose is to create a DOT file representation of the graph where original node names are replaced with safe, generic identifiers (e.g., "n0", "n1"). It first creates a copy of the input graph and generates a mapping from original node names to these safe identifiers. The graph's nodes are then relabeled using this mapping, and the original node names are stored as a 'label' attribute on the new, safe nodes. Finally, the modified graph is written to the specified output path in DOT format.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The NetworkX directed graph to be processed and written to a DOT file.
    - **out_path** (`str`): The file path where the safe DOT representation of the graph will be saved.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo)`
*   **Description:** The `build_filtered_callgraph` function constructs a directed call graph for Python functions found within a given Git repository. It begins by iterating through all Python files in the repository, parsing each into an Abstract Syntax Tree (AST) to identify and collect all user-defined functions. In a second pass, it builds a `networkx.DiGraph` by identifying call relationships. An edge is added to this graph only if both the calling function and the called function are among the user-defined functions previously identified within the repository. The function ultimately returns this filtered call graph.
*   **Parameters:**
    - **repo** (`GitRepository`): The Git repository object from which to extract Python files and analyze function calls.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the filtered call relationships, where nodes are user-defined functions from the repository and edges indicate calls between them.
*   **Usage:** This function calls no other functions.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content)`
*   **Description:** The `wrap_cdata` function takes a string as input and encapsulates it within XML CDATA tags. It constructs an f-string that prepends "![CDATA[\n" and appends "\n]]>" to the provided content. This process ensures that the content is treated as character data by an XML parser, preventing interpretation of any special characters within the content as XML markup.
*   **Parameters:**
    - **content** (`str`): The string content that needs to be wrapped inside CDATA tags.
*   **Returns:**
    - **wrapped_content** (`str`): A new string with the original content enclosed within CDATA tags.
*   **Usage:** This function calls no other functions.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs, image_list)`
*   **Description:** This function processes a list of notebook output objects, extracting relevant content into a list of XML-like snippets. It iterates through each output, categorizing it by type such as display data, execution results, stream, or error. For display data and execution results, it prioritizes extracting image data (PNG then JPEG), converting Base64 strings into an image placeholder and storing the raw image data in a provided `image_list`. If no image is found, it extracts plain text. Stream outputs are appended as raw text, and error outputs are formatted into a string.
*   **Parameters:**
    - **outputs** (list of Output objects): A list of output objects, typically from notebook execution, containing various types of data like text, images, or error messages.
    - **image_list** (list of dict): A list passed by reference to accumulate dictionaries of image data (mime_type and Base64 string) that are extracted from the outputs.
*   **Returns:**
    - **extracted_xml_snippets** (list of str): A list of strings, where each string is either extracted plain text, an XML-like image placeholder, or a formatted error message.
*   **Usage:** This function calls no other functions.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type)`
*   **Description:** This function is designed to handle image processing based on a given MIME type. It checks for the `mime_type` within an undeclared `data` object. If found, it attempts to extract and clean a base64 string, then appends a dictionary containing the `mime_type` and data to an undeclared `image_list`. It returns a formatted placeholder string or an error message if an exception occurs during processing. If the `mime_type` is not present in `data`, it returns `None`.
*   **Parameters:**
    - **mime_type** (`str`): The MIME type string used to identify and process an image from the external `data` object.
*   **Returns:**
    - **image_placeholder_or_error** (`str`): Returns a formatted string placeholder like `\n<IMAGE_PLACEHOLDER index="{image_index}" mime="{mime_type}"/>\n` upon successful processing. If an exception occurs during image decoding, it returns an error string in the format `"<ERROR>Could not decode image: {e}</ERROR>"`.
    - **no_image_found** (`None`): Returns `None` if the provided `mime_type` is not found as a key in the external `data` object.
*   **Usage:** This function calls no other functions.
*   **Warning:** The function's source code references undeclared variables 'data' and 'image_list'. Without their definition or explicit passing as parameters, the function's complete behavior and dependencies cannot be fully determined from the provided snippet, leading to ambiguity in its local execution context.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content)`
*   **Description:** This function processes the raw content of a Jupyter notebook, provided as a string, to convert it into an XML representation. It uses `nbformat` to parse the notebook content. The function iterates through each cell, wrapping markdown cell source in `<CELL type="markdown">` tags and code cell source in `<CELL type="code">` tags. If code cells have outputs, these are further processed, potentially extracting images, and then wrapped in `<CELL type="output">` tags. It returns the combined XML string and a list of any extracted images, or an error message if the input cannot be parsed as a valid notebook.
*   **Parameters:**
    - **file_content** (`str`): The raw content of a Jupyter notebook file, provided as a string. This content is expected to be in JSON format, parsable by `nbformat`.
*   **Returns:**
    - **conversion_result** (`tuple[str, list]`): A tuple where the first element is a string containing the XML representation of the notebook or an error message if parsing fails. The second element is a list of extracted image data (e.g., base64 encoded strings) found within the notebook's output cells, which will be empty if no images are found or if an error occurs during parsing.
*   **Usage:** This function calls no other functions.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files)`
*   **Description:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It iterates through the provided `repo_files`, filtering for those with a `.ipynb` extension. For each identified notebook, it invokes `convert_notebook_to_xml` to transform its content into an XML representation and extract associated images. The function then aggregates these results into a dictionary, mapping each notebook's path to its converted XML and extracted images. Finally, it returns this dictionary containing all processed notebook data.
*   **Parameters:**
    - **repo_files** (`list[object]`): An iterable collection of file-like objects, where each object is expected to have a `path` attribute (string) to identify its location and a `content` attribute (string) holding its raw data.
*   **Returns:**
    - **results** (`dict[str, dict[str, str | Any]]`): A dictionary where each key is the string path of a processed Jupyter notebook, and each value is another dictionary containing the "xml" (string) output of the conversion and "images" (type depends on `convert_notebook_to_xml` output, potentially a list or dictionary of image data).
*   **Usage:** This function calls no other functions.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, providing mechanisms for lazy loading its content, size, and underlying Git blob object. It encapsulates file-related metadata and offers utility methods for data extraction and basic analysis, such as word counting. The class ensures efficient resource usage by deferring the loading of heavy data until it is explicitly accessed.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* The __init__ method initializes a RepoFile instance by storing the file's path and the git.Tree object from which it originates. It also sets up internal attributes (_blob, _content, _size) to None, indicating that these properties will be loaded lazily upon first access.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`** (property)
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading of the Git blob object associated with the file. It checks if _blob is already loaded; if not, it attempts to retrieve the blob from the _tree using the file path. A FileNotFoundError is raised if the file is not found in the commit tree.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`git.Blob`): The Git blob object for the file.
        *   *Usage:* This method does not explicitly call other functions or methods.
    *   **`content`** (property)
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading and decoding of the file's content. It checks if _content is already loaded; if not, it accesses the blob property, reads its data stream, and decodes it as UTF-8, ignoring errors.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`str`): The decoded content of the file as a string.
        *   *Usage:* This method does not explicitly call other functions or methods.
    *   **`size`** (property)
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading of the file's size in bytes. It checks if _size is already loaded; if not, it accesses the blob property and retrieves its size attribute.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`int`): The size of the file in bytes.
        *   *Usage:* This method does not explicitly call other functions or methods.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function. It calculates the number of words in the file's content by splitting the content property by whitespace and returning the length of the resulting list.
        *   *Parameters:*
        *   *Returns:*
            - **null** (`int`): The total word count of the file content.
        *   *Usage:* This method does not explicitly call other functions or methods.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* "This special method provides a developer-friendly string representation of the RepoFile object, showing its class name and the file path."
        *   *Parameters:*
        *   *Returns:*
            - **null** (`str`): A string representation of the RepoFile object.
        *   *Usage:* This method does not explicitly call other functions or methods.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content=False)`
        *   *Description:* "This method converts the RepoFile object into a dictionary representation. It includes the file path, name (basename), size, and type. Optionally, it can include the file's content if include_content is set to True."
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether to include the file's content in the dictionary. Defaults to False.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing file metadata and optionally its content.
        *   *Usage:* This method does not explicitly call other functions or methods.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with Git repositories programmatically. It handles the cloning of a remote repository into a temporary local directory, offers methods to retrieve all files as RepoFile objects, and can generate a hierarchical representation of the repository's file structure. Furthermore, it implements the context manager protocol, ensuring that the temporary directory and its contents are properly cleaned up upon exiting the context.
*   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes a GitRepository instance by taking a repository URL, creating a temporary directory for cloning, and then performing the clone operation. It sets up attributes for the repository object, its latest commit, and the commit tree, handling potential GitCommandError during cloning by cleaning up the temporary directory.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to be cloned.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* "This method retrieves a list of all files present in the cloned Git repository. It uses the `git ls-files` command to get file paths, then iterates through these paths to create RepoFile objects, which are stored internally and returned."
        *   *Parameters:*
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   *Usage:* This method does not explicitly call other functions or methods within its defined scope.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is responsible for cleaning up resources by deleting the temporary directory where the Git repository was cloned. It checks if `self.temp_dir` is set before attempting to delete it and then sets `self.temp_dir` to `None` to prevent further attempts.
        *   *Parameters:*
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods within its defined scope.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* "This special method allows the GitRepository class to be used as a context manager. When entering a `with` statement, it simply returns the instance itself, making it available for operations within the context block."
        *   *Parameters:*
        *   *Returns:*
            - **self** (`GitRepository`): The instance of the GitRepository itself.
        *   *Usage:* This method does not explicitly call other functions or methods within its defined scope.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* "This special method is part of the context manager protocol and is automatically called when exiting a `with` statement. Its primary responsibility is to ensure proper cleanup by invoking the `close` method, regardless of whether an exception occurred within the context block."
        *   *Parameters:*
            - **exc_type** (`type | None`): The type of the exception that caused the context to be exited, or None if no exception occurred.
            - **exc_val** (`Exception | None`): The exception instance that caused the context to be exited, or None.
            - **exc_tb** (`TracebackType | None`): The traceback object associated with the exception, or None.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods within its defined scope.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content=False)`
        *   *Description:* "This method constructs a hierarchical dictionary representation of the repository's file structure. It first ensures that all files are loaded using `get_all_files` if they haven't been already. It then iterates through the RepoFile objects, splitting their paths to build a nested dictionary structure that mimics the directory tree, optionally including file content."
        *   *Parameters:*
            - **include_content** (`bool`): A flag indicating whether to include the content of each file in the generated tree structure. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the hierarchical file tree of the repository.
        *   *Usage:* This method does not explicitly call other functions or methods within its defined scope.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare two token counts, specifically 'JSON' and 'TOON' tokens. It takes the token counts and a savings percentage as input. The chart displays the number of tokens for each category, includes a title indicating the calculated savings, and annotates each bar with its corresponding token value. The generated chart is then saved to a specified file path.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of savings to be displayed in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart will be saved.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep durations, which are introduced due to rate-limiting for specific models. It takes start and end times, total items, batch size, and the model name as input. If the model name does not start with "gemini-", the total duration is returned directly. Otherwise, it computes the number of batches and corresponding sleep time, then subtracts this from the total duration, ensuring the net time is not negative.
*   **Parameters:**
    - **start_time** (`float | datetime.datetime`): The starting timestamp or numerical time value for the operation.
    - **end_time** (`float | datetime.datetime`): The ending timestamp or numerical time value for the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model used, which determines if sleep time calculations are applied.
*   **Returns:**
    - **net_time** (`float | int`): The calculated net duration, which is the total duration minus any estimated sleep times, or 0 if total items are 0, or the total duration if the model is not 'gemini-'.
*   **Usage:** This function calls no other functions.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback=None)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing a GitHub repository. It begins by extracting API keys and model names, then clones the specified repository. It proceeds to extract basic project information, construct a file tree, analyze relationships between code components, and build an Abstract Syntax Tree (AST) schema, which is then enriched with relationship data. The function prepares inputs for a Helper LLM to analyze individual functions and classes, and subsequently uses a Main LLM to generate a final report based on the collected and analyzed data. Finally, it saves the generated report and associated metrics, including token savings, to disk.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used in the workflow.
    - **status_callback** (`Callable | None`): An optional callback function to provide status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM, detailing the repository analysis.
    - **metrics** (`dict`): A dictionary containing performance metrics and token usage statistics for the workflow.
*   **Usage:** This function calls no other functions.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function, `update_status`, is designed to handle status reporting. It takes a message as input and performs two primary actions: it conditionally invokes a `status_callback` function with the provided message if `status_callback` is defined, and it always logs the message using `logging.info`. This mechanism allows for flexible status updates, either through a registered callback or via standard logging, or both. The function does not return any value.
*   **Parameters:**
    - **msg** (`str`): The message string to be used for updating the status and for logging.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
*   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks from a given GitHub repository URL. It begins by extracting the repository URL from the input, cloning the repository, and processing its notebook files. It then extracts basic project information and initializes a Large Language Model (LLM) based on the specified model and API keys. The function iterates through each identified notebook, constructs a detailed payload including its XML structure and embedded images, and sends it to the LLM for report generation. Finally, it concatenates all individual notebook reports, saves the combined report to a timestamped markdown file, and returns the final report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): A string containing the GitHub repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various Large Language Model (LLM) providers, such as 'gpt', 'gemini', 'scadsllm', or 'ollama'.
    - **model** (`str`): The name of the specific LLM model to be used for generating notebook reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`Callable | None`): An optional callback function that receives status messages during the workflow execution, allowing for real-time updates.
*   **Returns:**
    - **report** (`str`): A concatenated markdown string containing the analysis reports generated by the LLM for all processed notebooks.
    - **metrics** (`dict`): A dictionary containing performance metrics of the workflow, such as total execution time, the LLM model used, and token usage information.
*   **Usage:** This function calls no other functions.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a multi-modal payload designed for a Gemini-like model by combining textual context with embedded images. It begins by serializing `basic_info` and `nb_path` into an introductory JSON string. The function then processes `xml_content`, using a regular expression to identify and extract text segments and image placeholders. For each image placeholder, it retrieves the corresponding base64 encoded image data from the `images` list and formats it as an `image_url` entry. All extracted text and image components are appended to a list, which is then returned as the complete payload.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing general project or context information.
    - **nb_path** (`str`): The file path of the current notebook being processed.
    - **xml_content** (`str`): An XML string representing the notebook's structure, potentially containing image placeholders.
    - **images** (`list[dict]`): A list of dictionaries, where each dictionary contains 'data' (base64 string) for an image.
*   **Returns:**
    - **payload_content** (`list[dict]`): A list of dictionaries, each formatted as a content part for a multi-modal model, containing either text or image data.
*   **Usage:** This function calls no other functions.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file system `filepath` into a Python module import path. It first determines the path relative to the `project_root`, falling back to the base filename if a `ValueError` occurs during relative path calculation. The function then removes the `.py` extension and replaces directory separators with dots. Finally, it specifically handles `__init__.py` files by stripping the `.__init__` suffix to yield the package name.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path (e.g., 'my_package.my_module').
*   **Usage:** This function calls no other functions.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to build a comprehensive call graph and identify definitions of functions, methods, and classes. It systematically traverses the project directory, parses Python files into ASTs, collects all defined entities, and then resolves the relationships between callers and callees. This class provides a structured way to understand the internal dependencies and interactions within a codebase, making it valuable for code comprehension, refactoring, and impact analysis.
*   **Instantiation:** This class is not explicitly instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer instance by setting the project's root directory, and initializing internal data structures like `definitions`, `call_graph`, and `file_asts`. It also defines a set of directories to ignore during file traversal.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect definitions of functions, methods, and classes. Subsequently, it iterates again to resolve call relationships between these definitions, building a comprehensive call graph. Finally, it clears the cached ASTs and returns the generated call graph.
        *   *Parameters:*
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee pathnames and values are lists of caller information.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* "This method processes the internal `call_graph` to generate a structured representation of outgoing and incoming call relationships. It iterates through the call graph, extracting caller and callee identifiers, and populates two dictionaries: `outgoing` (showing what each entity calls) and `incoming` (showing what calls each entity). The results are then sorted and returned."
        *   *Parameters:*
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, "outgoing" and "incoming". Each value is a dictionary mapping entity identifiers to sorted lists of related entity identifiers.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* "This private helper method traverses the project's root directory to locate all Python files, excluding directories specified in `self.ignore_dirs`. It uses `os.walk` to recursively search through the directory structure and filters for files ending with ".py". The absolute paths of these files are collected and returned."
        *   *Parameters:*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found in the project, excluding ignored directories.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* "This private method is responsible for parsing a given Python file, building its Abstract Syntax Tree (AST), and identifying all function, method, and class definitions within it. It stores the AST in `self.file_asts` and populates `self.definitions` with details like the definition's full path name, file path, line number, and type (function, method, or class). Error handling is included for file reading or parsing issues."
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file to be analyzed for definitions.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* "This private helper method traverses an Abstract Syntax Tree (AST) to find the direct parent node of a given child node. It iterates through all nodes in the tree and checks their children to identify if any child matches the provided `node`. If a parent is found, it is returned; otherwise, `None` is returned."
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent** (`ast.AST | None`): The parent AST node if found, otherwise `None`.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* "This private method takes a Python file's path, retrieves its cached AST, and uses a `CallResolverVisitor` to identify all function and method calls within that file. It then extends the class's `call_graph` with the resolved call relationships. If the AST for the file is not found or an error occurs during call resolution, it logs the error and exits gracefully."
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) and identify function and method calls within Python source code. It resolves the fully qualified names of these calls and records caller information, including the file, line number, and type of caller. This class is instrumental in building a call graph or understanding inter-function relationships within a project by mapping call sites to their definitions.
*   **Instantiation:** This class is not explicitly instantiated by any other components based on the provided context.
*   **Dependencies:** This class does not explicitly list any functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with the current file path, the project's root directory, and a dictionary of known definitions. It sets up internal state variables like `module_path`, `scope` for imports, `instance_types` for tracking object types, and `calls` (a defaultdict) to store discovered call relationships.
    *   *Parameters:*
        - **filepath** (`str`): The absolute path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the entire project, used to determine module paths.
        - **definitions** (`dict`): A dictionary mapping fully qualified names to their definitions, used for validating resolved call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* "This method is invoked when the AST visitor encounters a class definition. Its primary responsibility is to update the `current_class_name` attribute to reflect the class being visited, allowing subsequent method definitions within that class to be correctly identified. After processing the class's children, it restores the `current_class_name` to its previous value, ensuring proper scope management during traversal."
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* "This method is triggered upon visiting a function or method definition within the AST. It constructs the full qualified identifier for the function, considering whether it's a method within a class or a top-level function. This identifier is then set as `current_caller_name` to correctly attribute calls made within this function. The original caller name is restored after the function's body has been visited."
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function or method definition.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* "This method processes function and method call nodes in the AST. It attempts to resolve the fully qualified name of the callee using the `_resolve_call_qname` helper. If a valid callee is found and exists in the known definitions, it records detailed information about the caller, including its file, line number, full identifier, and type (module, local function, method, or function). This information is then appended to the `calls` dictionary, mapping callees to their callers."
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* "This method handles `import` statements in the AST. It iterates through all imported names and their aliases, storing the mapping between the alias (or original name) and the full module name in the `scope` dictionary. This `scope` is later used to resolve qualified names of calls. After processing the import statement, it continues the generic AST traversal."
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* "This method processes `from ... import ...` statements. It determines the full module path for the imported names, correctly handling relative imports based on the `node.level` attribute and the current `module_path`. Each imported name (or its alias) is then mapped to its fully qualified path in the `scope` dictionary. This allows for accurate resolution of imported functions or classes during call analysis."
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* "This method inspects assignment statements to identify object instantiations. Specifically, if an assignment involves a call expression (e.g., `x = MyClass()`) and the called function is a known class from the `scope` and `definitions`, it records the qualified class name as the type for the assigned variable's identifier in `instance_types`. This helps in resolving method calls on instantiated objects later."
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* "This private helper method is responsible for determining the fully qualified name (QName) of a function or method being called. It handles two main scenarios: direct calls to names (e.g., `func()`) by checking local scope and module-level definitions, and attribute calls on objects (e.g., `obj.method()`) by looking up the object's type in `instance_types` or its module in `scope`. It returns the resolved QName as a string or `None` if it cannot be resolved."
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g. ast.Name, ast.Attribute).
        *   *Returns:*
            - **qualified_name** (`str | None`): The fully qualified name of the callable, or None if it cannot be resolved.
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** "This function encrypts a given string using a `cipher_suite` object. It first checks if the input `text` or `cipher_suite` is empty; if either is, it returns the original text without encryption. Otherwise, it strips whitespace from the text, encodes it to bytes, encrypts it using `cipher_suite.encrypt`, and then decodes the resulting bytes back into a string before returning it."
*   **Parameters:**
    - **text** (`str`): The string value to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted version of the input string, or the original string if encryption conditions are not met.
*   **Usage:** This function calls no other functions.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** "This function attempts to decrypt a given text string using a globally available 'cipher_suite' object. It first checks if the input text or the 'cipher_suite' is empty or null, returning the original text if either condition is met. If both are valid, it proceeds to strip whitespace from the text, encode it to bytes, decrypt it using 'cipher_suite.decrypt', and then decode the result back into a string. A try-except block handles potential decryption errors, ensuring the original text is returned in case of any failure."
*   **Parameters:**
    - **text** (`str`): The string value to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted string, or the original 'text' if decryption is skipped or an error occurs.
*   **Usage:** This function calls no other functions.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** "This function is responsible for creating a new user entry in a database. It takes a username, name, and plain-text password as input. The password is first hashed using `stauth.Hasher.hash` before being stored. A user document is constructed with the provided details and initialized with empty strings for various API keys. This document is then inserted into the `dbusers` collection, and the unique ID generated by the database for the new user is returned."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier (e.g., MongoDB ObjectId) of the newly inserted user document.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** "This function is designed to retrieve all user documents from a database collection named `dbusers`. It executes a `find()` operation on this collection, which typically returns a cursor object. The results from this cursor are then immediately converted into a standard Python list, which is subsequently returned by the function. It takes no input parameters."
*   **Parameters:**
*   **Returns:**
    - **users** (`list`): A list containing all user documents or records retrieved from the `dbusers` collection. Each item in the list represents a user.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** This function is designed to retrieve a single user document from a database collection named `dbusers`. It queries the collection by matching the provided `username` against the `_id` field of the documents. The function returns the first document found that matches the specified username.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user to be fetched, which is used to query the `_id` field in the database.
*   **Returns:**
    - **user_document** (`dict | None`): A dictionary representing the user document if a match is found, otherwise `None`.
*   **Usage:** This function calls no other functions.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username, new_name)`
*   **Description:** This function updates the 'name' field for a user identified by their 'username'. It uses the 'dbusers.update_one' method to locate a document where the '_id' matches the provided 'username' and then sets the 'name' field to the 'new_name'. The function returns an integer indicating the number of documents that were successfully modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier of the user whose name is to be updated, corresponding to the '_id' field in the database.
    - **new_name** (`str`): The new name to be assigned to the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** This function calls no other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function is responsible for updating a user's Gemini API key within a database. It takes a username and the new Gemini API key as input. The provided API key is first stripped of whitespace and then encrypted before being stored. The function then uses the username to find the corresponding user record in the `dbusers` collection and updates the `gemini_api_key` field with the encrypted value. It returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be stored for the user. This key will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    - **modified_count** (`int`): The number of documents modified by the update operation. This will typically be 1 if the user exists and the key was updated, or 0 if the user was not found or the key was already the same.
*   **Usage:** This function calls no other functions.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username, gpt_api_key)`
*   **Description:** "This function updates a user's GPT API key in the database. It takes a username and a new GPT API key as input. The provided API key is first stripped of whitespace and then encrypted. Finally, the function updates the `gpt_api_key` field for the specified user in the `dbusers` collection with the encrypted key, returning the count of modified documents."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key needs to be updated.
    - **gpt_api_key** (`str`): The new GPT API key to be encrypted and stored for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** This function calls no other functions.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** "This function updates the Ollama base URL associated with a specific user in the database. It takes a username and a new Ollama base URL as input. The provided URL is stripped of leading/trailing whitespace before being stored. The function then performs an update operation on the `dbusers` collection, setting the `ollama_base_url` field for the document matching the given username. It returns the count of documents that were modified by this operation."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL needs to be updated.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service to be associated with the user. Whitespace will be trimmed.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 indicates success if the user was found and updated, 0 if the user was not found or the URL was already the same.
*   **Usage:** This function calls no other functions.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username, opensrc_api_key)`
*   **Description:** "This function is responsible for updating a user's Open Source API key within a database. It takes a username and the new API key as input. The provided API key is first stripped of any leading or trailing whitespace, then encrypted using an external `encrypt_text` function. Finally, it performs an update operation on the `dbusers` collection, setting the `opensrc_api_key` field for the specified user with the newly encrypted value. The function returns the count of documents that were modified by this operation."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source API key needs to be updated.
    - **opensrc_api_key** (`str`): The new Open Source API key provided by the user, which will be encrypted and stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 indicates successful update for the user.
*   **Usage:** This function calls no other functions.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username, opensrc_base_url)`
*   **Description:** "This function updates the 'opensrc_base_url' for a specific user in a database. It takes a username and a new opensource base URL as input. The provided URL is first stripped of leading/trailing whitespace before being stored. The function then performs an update operation on the user's document in the 'dbusers' collection, setting the 'opensrc_base_url' field. It returns the count of documents that were modified by this operation."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose opensource base URL needs to be updated. This is used as the '_id' in the database query.
    - **opensrc_base_url** (`str`): The new opensource base URL to be assigned to the user. This string will have leading/trailing whitespace removed before being stored.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 indicates success if the user existed and the URL was different, 0 if the user existed but the URL was the same, or if the user did not exist.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** "This function retrieves the Gemini API key associated with a specific user from a database. It takes a username as input and queries the 'dbusers' collection to find a matching user document. If a user is found, it extracts and returns the 'gemini_api_key' field. If no user is found or the key is absent, the function returns None."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key as a string if found, otherwise None.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** "This function is designed to retrieve the Ollama base URL for a specific user from a database. It takes a username as input and queries a user collection to find the corresponding user document. The function specifically projects the 'ollama_base_url' field. If a user is found and has an 'ollama_base_url' defined, that URL is returned. Otherwise, if the user is not found or the URL is not present, the function returns None."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama base URL needs to be fetched.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The base URL for the Ollama service associated with the user, or None if the user is not found or the URL is not set.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username)`
*   **Description:** "This function, `fetch_gpt_key`, is designed to retrieve a user's GPT API key from a database. It takes a username as input and queries a collection named `dbusers` to find the corresponding user document. If a user is found, the function extracts the `gpt_api_key` field from the user's document. The extracted key is then returned; otherwise, if no user is found, the function returns `None`."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
*   **Returns:**
    - **gpt_api_key** (`str | None`): The GPT API key associated with the specified user, or `None` if the user is not found in the database.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username)`
*   **Description:** "This function is designed to retrieve an Open Source API key associated with a specific username from a database. It performs a database query on the 'dbusers' collection, searching for a document where the '_id' field matches the provided username. If a matching user document is found, it extracts and returns the 'opensrc_api_key' field. If no user is found or the key is not present, the function returns None."
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) for which to fetch the Open Source API key.
*   **Returns:**
    - **opensrc_api_key** (`str | None`): The Open Source API key as a string if found, otherwise None if the user does not exist or the key is not set.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username)`
*   **Description:** "This function, `fetch_opensrc_url`, is designed to retrieve a user's Open Source base URL from a database. It takes a username as input and queries a `dbusers` collection to find the corresponding user document. If a user is found, it extracts the `opensrc_base_url` field. The function returns this URL if available, otherwise it returns `None`."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Open Source base URL is to be fetched.
*   **Returns:**
    - **opensrc_url** (`str | None`): The Open Source base URL associated with the user, or None if the user is not found or the URL is not set.
*   **Usage:** This function calls no other functions.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** This function is designed to remove a user record from a database collection. It takes a username as input and uses it as the unique identifier (`_id`) to locate and delete the corresponding document. The function then reports the number of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted as a result of the operation.
*   **Usage:** This function calls no other functions.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** "This function retrieves a user's API keys and base URLs from a database based on their username. It queries the 'dbusers' collection to find the user. If the user is found, it decrypts the Gemini, GPT, and open-source API keys using a 'decrypt_text' utility and retrieves the Ollama and open-source base URLs directly. The function returns a tuple containing all these processed keys and URLs. If the user is not found in the database, it returns two None values."
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose API keys and URLs are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str | None`): The decrypted Gemini API key, or None if the user is not found.
    - **ollama_plain** (`str | None`): The Ollama base URL, or None if the user is not found.
    - **gpt_plain** (`str | None`): The decrypted GPT API key, or None if the user is not found.
    - **opensrc_plain** (`str | None`): The decrypted open-source API key, or None if the user is not found.
    - **opensrc_url** (`str | None`): The open-source base URL, or None if the user is not found.
*   **Usage:** This function calls no other functions.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username, chat_name)`
*   **Description:** "This function creates a new chat entry in the database. It generates a unique ID using UUID, records the provided username and chat name, and captures the current timestamp. The constructed chat dictionary is then inserted into the 'dbchats' collection."
*   **Parameters:**
    - **username** (`str`): The username associated with the new chat entry.
    - **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    - **inserted_id** (`str`): The unique identifier of the newly created chat entry in the database.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username)`
*   **Description:** "This function, `fetch_chats_by_user`, is responsible for retrieving all chat records associated with a specific user from a database. It accepts a username as input and performs a query on a `dbchats` collection. The query filters documents by the provided username and sorts the results by their `created_at` timestamp in ascending order. The function then returns the collected chat documents as a list."
*   **Parameters:**
    - **username** (`str`): The username for which to fetch chat records.
*   **Returns:**
    - **chats** (`list`): A list of chat documents associated with the specified username, sorted by creation date.
*   **Usage:** This function calls no other functions.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username, chat_name)`
*   **Description:** This function determines if a chat entry exists in the 'dbchats' collection based on a provided username and chat name. It queries the database for a document that matches both criteria. The function returns a boolean indicating the presence or absence of such a chat.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be checked.
    - **chat_name** (`str`): The name of the chat to be checked.
*   **Returns:**
    - **chat_exists** (`bool`): True if a chat with the specified username and chat name exists in the database, False otherwise.
*   **Usage:** This function calls no other functions.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
*   **Description:** "This function renames a chat and all its associated exchanges within a database. It first updates the `dbchats` collection to change the `chat_name` for a specific user and old chat name to the new chat name. Subsequently, it updates all related entries in the `dbexchanges` collection, ensuring consistency across chat and message records. The function returns the count of chat entries that were modified."
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be renamed.
    - **old_name** (`str`): The current name of the chat that needs to be changed.
    - **new_name** (`str`): The desired new name for the chat.
*   **Returns:**
    - **modified_count** (`int`): The number of chat entries (from dbchats) that were modified during the rename operation.
*   **Usage:** This function calls no other functions.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used='', main_used='', total_time='', helper_time='', main_time='', json_tokens=0, toon_tokens=0, savings_percent=0.0)`
*   **Description:** "This function records a user exchange by creating a new document with details such as the question, answer, feedback, user information, and various performance metrics. It generates a unique ID for the exchange and timestamps its creation. The function attempts to insert this record into the `dbexchanges` collection and returns the new ID upon success, or `None` if an error occurs during the database operation."
*   **Parameters:**
    - **question** (`str`): The user's question in the exchange.
    - **answer** (`str`): The generated answer for the question.
    - **feedback** (`str`): The feedback provided for the exchange.
    - **username** (`str`): The username associated with the exchange.
    - **chat_name** (`str`): The name of the chat session where the exchange occurred.
    - **helper_used** (`str`): Optional. Indicates which helper model was used, defaults to an empty string.
    - **main_used** (`str`): Optional. Indicates which main model was used, defaults to an empty string.
    - **total_time** (`str`): Optional. The total time taken for the exchange, defaults to an empty string.
    - **helper_time** (`str`): Optional. The time taken by the helper model, defaults to an empty string.
    - **main_time** (`str`): Optional. The time taken by the main model, defaults to an empty string.
    - **json_tokens** (`int`): Optional. The number of JSON tokens used, defaults to 0.
    - **toon_tokens** (`int`): Optional. The number of 'toon' tokens used, defaults to 0.
    - **savings_percent** (`float`): Optional. The percentage of savings achieved, defaults to 0.0.
*   **Returns:**
    - **new_id** (`str`): The unique identifier of the newly inserted exchange record.
    - **None**: Indicates that an error occurred during the database insertion.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** This function retrieves a list of exchange records associated with a specific username from a database collection named `dbexchanges`. It filters the records by the provided username and then sorts them chronologically by their `created_at` timestamp in ascending order. The sorted results are then converted into a list and returned.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records (dictionaries) associated with the given username, sorted by their creation timestamp.
*   **Usage:** This function calls no other functions.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** "This function is designed to retrieve a collection of exchange records from a database. It filters these records based on a specific username and a chat name provided as arguments. The matching exchanges are then sorted chronologically by their creation timestamp in ascending order. Finally, the function returns the sorted list of exchange documents."
*   **Parameters:**
    - **username** (`str`): The username used to filter the exchange records.
    - **chat_name** (`str`): The name of the chat used to filter the exchange records.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange documents that match the provided username and chat name, sorted by their 'created_at' field.
*   **Usage:** This function calls no other functions.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** "This function is responsible for updating the feedback value associated with a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function executes an update operation on the 'dbexchanges' collection, targeting the document matching the provided 'exchange_id' and setting its 'feedback' field to the new value. It then returns a count of how many documents were successfully modified by this operation."
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated in the database.
    - **feedback** (`int`): The integer value representing the feedback to be assigned to the specified exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** This function calls no other functions.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function updates the feedback message for a specific exchange record in the database. It takes an exchange identifier and a new feedback message string. It uses the `dbexchanges.update_one` method to locate the document by its `_id` and set the `feedback_message` field. The function then returns the count of documents that were modified by this operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated.
    - **feedback_message** (`str`): The new feedback message string to be set for the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:** This function calls no other functions.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function is designed to remove a specific exchange record from a database collection. It takes an exchange identifier as input and uses it to locate and delete a single document. The function then reports the number of documents that were successfully deleted.
*   **Parameters:**
    - **exchange_id** (`str`): The unique string identifier of the exchange document to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted as a result of the operation. This will typically be 0 or 1.
*   **Usage:** This function calls no other functions.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username, chat_name)`
*   **Description:** "This function is responsible for completely deleting a chat and all its associated messages (exchanges) for a given user. It ensures data consistency between the frontend and backend by removing all related records. The process involves first deleting all messages belonging to the specified chat and then deleting the chat entry itself. It returns a count of the chat documents deleted."
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat documents deleted, typically 0 or 1 for a single chat deletion.
*   **Usage:** This function calls no other functions.

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list)`
*   **Description:** "The `clean_names` function processes a list of model names, each potentially containing path separators. It iterates through the provided list, and for each model name, it splits the string by the '/' character. The function then extracts the last segment of the split string, effectively isolating the base name of the model. Finally, it returns a new list composed of these extracted base names."
*   **Parameters:**
    - **model_list** (`list[str]`): A list of strings, where each string is expected to be a model identifier that may contain path-like separators (e.g., '/').
*   **Returns:**
    - **cleaned_model_names** (`list[str]`): A new list containing the cleaned model names, where each name is the last segment after splitting by '/'.
*   **Usage:** This function calls no other functions.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list, category_name)`
*   **Description:** "This function filters a given list of models based on a specified category name. It retrieves a set of keywords associated with the `category_name` from an external `CATEGORY_KEYWORDS` mapping. If the category's keywords include \"STANDARD\", the function returns only those models from the `source_list` that are also present in an external `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list` and includes models whose names contain any of the category's keywords (case-insensitively). If no models match the keywords, the original `source_list` is returned."
*   **Parameters:**
    - **source_list** (`list`): The initial list of models to be filtered. Each model is expected to be a string.
    - **category_name** (`str`): The name of the category used to determine the filtering keywords.
*   **Returns:**
    - **filtered_models** (`list`): A list of models that match the filtering criteria, or the original source_list if no matches are found.
*   **Usage:** This function calls no other functions.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** "This function is designed to save a new Gemini API key. It retrieves the potential new key from the Streamlit session state. If a new key is present, it updates the Gemini key in the database for the current user, clears the input field in the session state, and displays a success toast notification to the user."
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** "This function serves as a callback to save a user-provided Ollama URL. It retrieves the potential new Ollama URL from the Streamlit session state, specifically from the 'in_ollama_url' key. If a valid, non-empty URL is found, the function proceeds to update this URL in the database, associating it with the currently logged-in user's username, also retrieved from the session state. Upon successful database update, a confirmation toast message is displayed to the user. This function does not explicitly return any value."
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** "This function loads chat and exchange data for a specified user from the database into the Streamlit session state. It first checks if the data for the given username has already been loaded to prevent redundant operations. If not loaded, it initializes the session state, fetches predefined chats, then retrieves and organizes exchanges, handling cases where chats might not yet exist for an exchange. Finally, it ensures a default chat exists if none are found and sets the active chat."
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat and exchange data.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** "The handle_feedback_change function updates feedback information associated with an exchange object. It takes an exchange dictionary and a new feedback value. The function first modifies the 'feedback' key within the provided exchange dictionary. It then calls a database utility to persist this feedback change using the exchange's identifier. Finally, it triggers a Streamlit application rerun to refresh the user interface."
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing an exchange or data record, expected to contain 'feedback' and '_id' keys.
    - **val** (`Any`): The new value to be set for the feedback.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** "This function is responsible for deleting a specific exchange. It first removes the exchange from the database using its unique identifier. Subsequently, it checks if the associated chat and exchange exist within the Streamlit session state and removes the exchange from there if found. Finally, it triggers a Streamlit rerun to update the user interface."
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat from which the exchange should be deleted.
    - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' key for database deletion.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** "This function handles the deletion of a specific chat identified by a username and chat name. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the Streamlit session state by removing the chat from `st.session_state.chats`. If other chats remain, the first one is set as the `active_chat`; otherwise, a new default chat named 'Chat 1' is created, inserted into the database via `db.insert_chat`, and set as the active chat. Finally, it triggers a Streamlit rerun using `st.rerun()` to update the UI."
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** "This function is designed to extract a repository name from an input text string. It first uses a regular expression to search for a URL within the provided text. If a URL is successfully matched, the function then parses this URL to isolate its path component. The last segment of the URL path is then considered the potential repository name, with any trailing '.git' suffix removed. If no URL is found in the text or if the extracted URL path is empty, the function returns None."
*   **Parameters:**
    - **text** (`str`): The input string that may contain a URL from which a repository name needs to be extracted.
*   **Returns:**
    - **repo_name** (`str | None`): The extracted repository name as a string if a valid URL and path are found and processed, otherwise None.
*   **Usage:* This function calls no other functions.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** "This function acts as a generator that takes a string of text and yields its words one by one, each followed by a space. It simulates a streaming effect by introducing a small delay after yielding each word. The primary purpose is to provide text incrementally, which can be useful for user interfaces or real-time displays. It achieves this by splitting the input string by spaces and iterating through the resulting words."
*   **Parameters:**
    - **text** (`str`): The input string of text that needs to be streamed word by word.
*   **Returns:**
    - **word_with_space** (`str`): A single word from the input text, followed by a space, yielded sequentially.
*   **Usage:* This function calls no other functions.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream=False)`
*   **Description:** "This function processes a given markdown text string, identifying and rendering both standard markdown content and embedded Mermaid diagrams. It first checks if the input text is empty, returning early if so. The text is then split into parts based on ````mermaid` delimiters. Regular markdown sections are rendered using `st.markdown` or streamed via `st.write_stream` depending on the `should_stream` flag. Mermaid diagram blocks are attempted to be rendered using `st_mermaid`, with a fallback to `st.code` if an error occurs during Mermaid rendering."
*   **Parameters:**
    - **markdown_text** (`str`): The input text string which may contain standard markdown and embedded Mermaid diagrams.
    - **should_stream** (`bool`): A flag indicating whether non-Mermaid markdown content should be streamed using st.write_stream or rendered directly with st.markdown. Defaults to False.
*   **Returns:**
*   **Usage:* This function calls no other functions.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** "The render_exchange function is responsible for displaying a single chat exchange, consisting of a user's question and an assistant's answer, within a Streamlit application. It first renders the user's question, then displays the assistant's answer. Alongside the answer, it presents an interactive toolbar that allows users to provide feedback (like/dislike), add a comment via a popover, download the answer content, and delete the entire exchange. The function also includes specific error handling to display an error message and a delete option if the assistant's answer indicates a problem. It interacts with a database to update feedback messages and uses Streamlit's rerun functionality after certain actions."
*   **Parameters:**
    - **ex** (`dict`): A dictionary-like object representing a single chat exchange, expected to contain keys such as 'question', 'answer', 'feedback', 'feedback_message', and '_id'.
    - **current_chat_name** (`str`): The name of the current chat session, used when handling the deletion of an exchange.
*   **Returns:**
*   **Usage:* This function calls no other functions.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to provide a structured representation for a single parameter within a function's signature. It serves as a data model to consistently store the parameter's name, its data type, and a brief textual description of its purpose. This class facilitates the programmatic handling and documentation of function parameters.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is automatically generated. It initializes an instance of `ParameterDescription` by validating and assigning the provided `name`, `type`, and `description` to its corresponding attributes, ensuring data integrity according to the defined schema.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type hint or inferred type of the parameter.
        - **description** (`str`): A textual explanation of the parameter's purpose.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to standardize the description of a function's return value. It encapsulates three key pieces of information: the name of the return value, its data type, and a textual description. This class serves as a structured data model for representing function outputs consistently across a system.
*   **Instantiation:** The provided context does not specify the instantiation points for this class.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the __init__ method for ReturnDescription is automatically generated. It accepts keyword arguments corresponding to its defined fields (name, type, description) to initialize a new instance of the class, ensuring type validation upon instantiation.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The data type of the return value, represented as a string.
        - **description** (`str`): A detailed textual explanation of what the return value represents or contains.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts within a larger system. It serves as a structured data container, holding two string attributes: 'calls', which describes the external entities or functions it invokes, and 'called_by', which indicates where it is invoked from. This class provides a standardized way to represent the operational context of a code component.
*   **Instantiation:** The provided context does not specify the instantiation points for this class.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
*   **Constructor:**
    *   *Description:* This class, inheriting from Pydantic's BaseModel, automatically generates an __init__ method. This constructor initializes an instance of UsageContext by accepting 'calls' and 'called_by' as string arguments, which are then stored as instance attributes.
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or external entities called by the component being described.
        - **called_by** (`str`): A string summarizing the functions, methods, or external entities that call the component being described.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The `FunctionDescription` class is a Pydantic BaseModel designed to structure and validate the detailed analysis of a Python function. It encapsulates key aspects such as the function's overall purpose, its input parameters, its return values, and its usage context within a larger system. This model serves as a standardized data structure for representing function metadata, facilitating consistent data exchange and processing.
*   **Instantiation:** The specific instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is automatically generated. It initializes an instance of `FunctionDescription` by validating and assigning values to its defined fields: `overall`, `parameters`, `returns`, and `usage_context`.
    *   *Parameters:*
        - **overall** (`str`): A high-level summary describing the function's purpose and its implementation details.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing an input parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of `ReturnDescription` objects, each describing a value returned by the function.
        - **usage_context** (`UsageContext`): An object containing information about the function's call graph, including what it calls and where it is called from.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data container, holding the function's unique identifier, a detailed description object (FunctionDescription), and an optional field to report any errors encountered during the analysis process. This model is crucial for standardizing the output of function analysis within a larger system, ensuring consistent data representation.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class inherits from Pydantic's BaseModel, which automatically generates an `__init__` method. This constructor initializes instances of FunctionAnalysis by accepting values for its defined fields: `identifier`, `description`, and `error`.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the function's analysis. Defaults to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** "The `ConstructorDescription` class is a Pydantic model designed to formally describe the `__init__` method of another Python class. It acts as a structured schema, ensuring that any constructor description includes a textual summary and a list of its individual parameters, each detailed by a `ParameterDescription` object. This model facilitates consistent and machine-readable documentation of class constructors within a larger system."
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance of `ConstructorDescription` by accepting values for its `description` and `parameters` fields, ensuring they conform to the specified types."
    *   *Parameters:*
        - **description** (`str`): A string summarizing the constructor's behavior.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each describing a parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's operational context. It specifically stores information regarding the external dependencies that the class relies upon and the locations or modules where the class is instantiated. This model serves as a structured way to represent and manage contextual data for class analysis.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "The __init__ method for ClassContext is implicitly generated by Pydantic's BaseModel. It allows for the creation of ClassContext instances by providing values for its defined fields: 'dependencies' and 'instantiated_by'. These values are typically passed as keyword arguments during object creation."
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class, indicating what other components or libraries it relies on.
        - **instantiated_by** (`str`): A string describing the primary points or locations within the system where this class is instantiated.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** "The ClassDescription class is a Pydantic BaseModel designed to structure the comprehensive analysis of a Python class. It serves as a data container, encapsulating various aspects such as the class's overall purpose, the details of its constructor, a list of analyses for its individual methods, and its broader usage context within a system. This model is crucial for standardizing the output of a class analysis process, ensuring all relevant information is captured in a consistent format."
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "The `__init__` method for ClassDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance of ClassDescription by validating and assigning values to its defined fields: overall, init_method, methods, and usage_context."
    *   *Parameters:*
        - **overall** (`str`): A string describing the overall purpose and functionality of the class being analyzed.
        - **init_method** (`ConstructorDescription`): An object containing the detailed analysis of the class's constructor (__init__ method).
        - **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each detailing an individual method within the class.
        - **usage_context** (`ClassContext`): An object providing context about the class's dependencies and where it is instantiated.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** "The ClassAnalysis model serves as the primary data structure for encapsulating a comprehensive analysis of a Python class. It is designed to hold a unique identifier for the class, a detailed description object containing its constructor and method analyses, and an optional field to report any errors encountered during the analysis process. This model is fundamental for structuring the output of an AI-driven class analysis system."
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "The ClassAnalysis model is initialized by accepting values for its `identifier`, `description`, and an optional `error` field. As a Pydantic BaseModel, it automatically handles validation and assignment of these fields upon instantiation, ensuring that the provided data conforms to the defined types."
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its constructor and methods.
        - **error** (`Optional[str]`): An optional string indicating an error encountered during the class analysis, or None if the analysis was successful.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** "The `CallInfo` class is a Pydantic BaseModel designed to represent a specific call event within a system, typically used by a relationship analyzer. It encapsulates essential details about a function or method call, including its location and type. This model serves as a structured data container for tracking where and how code components interact."
*   **Instantiation:** This class is not explicitly instantiated by any known components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* "The `__init__` method for `CallInfo` is implicitly generated by Pydantic, as `CallInfo` inherits from `BaseModel`. It initializes an instance of `CallInfo` by validating and assigning values to its fields: `file`, `function`, `mode`, and `line`. This allows for easy creation of call event records with type-checked data."
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that is making the call.
        - **mode** (`str`): The classification of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The specific line number within the file where the call event is located.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** "The FunctionContextInput class is a Pydantic BaseModel designed to encapsulate structured context for analyzing a function. It serves as a data transfer object, holding information about a function's internal and external interactions. Specifically, it tracks a list of entities that the function calls and a list of entities that call the function, providing a clear overview of its operational context."
*   **Instantiation:** The instantiation points for this class are not specified within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "This class implicitly inherits its constructor from Pydantic's BaseModel. The `__init__` method automatically handles the initialization of its fields, `calls` and `called_by`, based on the provided arguments during instantiation. It ensures type validation and data integrity for the structured context."
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings, where each string represents the identifier of another method, class, or function that the analyzed function calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, each providing details about another function or method that calls the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** "This class functions as a Pydantic BaseModel, defining the structured input required for performing a function analysis. It specifies the necessary data fields such as the analysis mode, the function's unique identifier, its raw source code, a list of relevant import statements, and additional contextual information. The model ensures that all essential data for a comprehensive function analysis is provided in a consistent and validated format."
*   **Instantiation:** This class does not explicitly list any locations where it is instantiated within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "As a Pydantic BaseModel, the `__init__` method for this class is implicitly generated by Pydantic. It automatically handles the validation and assignment of attributes based on the defined type hints and any provided default values, ensuring data integrity upon instantiation."
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): The mode of analysis, fixed to "function_analysis".
        - **identifier** (`str`): The unique identifier of the function.
        - **source_code** (`str`): The source code of the function.
        - **imports** (`List[str]`): A list of import statements relevant to the function.
        - **context** (`FunctionContextInput`): Structured contextual information for the function.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** "The MethodContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information about a specific method. It serves as a data schema to represent various aspects of a method's definition and its interactions within a larger codebase. This model is crucial for providing a standardized format for method analysis, allowing for consistent data exchange and processing."
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "This class is a Pydantic model, so its `__init__` method is automatically generated by Pydantic. It initializes an instance of `MethodContextInput` by accepting values for its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`."
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where this method is called from.
        - **args** (`List[str]`): A list of argument names for the method.
        - **docstring** (`Optional[str]`): The docstring of the method, if available.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** "The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information relevant for analyzing a Python class. It defines the schema for input data that describes a class's external dependencies, where it is instantiated, and detailed context for its individual methods. This model facilitates the standardized exchange of class analysis data within a larger AI system."
*   **Instantiation:** The provided context does not specify any locations where this class is instantiated.
*   **Dependencies:** This class does not explicitly declare any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "This class does not explicitly define an `__init__` method. It inherits from `pydantic.BaseModel`, and its constructor is implicitly generated by Pydantic, which initializes its fields based on the provided type hints: `dependencies` (List[str]), `instantiated_by` (List[CallInfo]), and `method_context` (List[MethodContextInput])."
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies of the class.
        - **instantiated_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where the class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of `MethodContextInput` objects detailing the context of the class's methods.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** "The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a schema validator, ensuring that all necessary components like the analysis mode, class identifier, source code, import statements, and contextual information are present and correctly typed before further processing. This class acts as a contract for data exchange within a system that performs class analysis."
*   **Instantiation:** The points of instantiation for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* "The ClassAnalysisInput class does not explicitly define an __init__ method. As a Pydantic BaseModel, its initialization is handled implicitly by Pydantic, which constructs instances based on the type-hinted fields defined within the class. Pydantic automatically validates and assigns values to these attributes upon instantiation."
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): The analysis mode, fixed to "class_analysis".
        - **identifier** (`str`): The unique identifier of the class.
        - **source_code** (`str`): The source code of the class.
        - **imports** (`List[str]`): A list of import statements relevant to the class.
        - **context** (`ClassContextInput`): Structured contextual information for the class.
*   **Methods:**

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** "This function converts a given file system path into a Python module path string. It first attempts to make the path relative to a specified project root, falling back to just the basename if the relative path cannot be determined. It then removes the '.py' extension if present and replaces system path separators with dots. Finally, it removes the '.__init__' suffix if the module path represents an initialization file, returning the cleaned module path."
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the file that needs to be converted.
    - **project_root** (`str`): The root directory of the project, used as a base to calculate the relative module path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string, e.g., 'my_package.my_module'.
*   **Usage:** This function calls no other functions.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various large language models (LLMs) to generate structured documentation for Python functions and classes. It abstracts away the complexities of LLM API calls, including model selection, prompt management, batch processing, and rate limiting. The class is designed to ensure robust and validated output by leveraging Pydantic schemas for both input and output, making it a reliable component for automated code documentation generation.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** The class depends on `os`, `json`, `logging`, `time`, `typing.List`, `typing.Dict`, `typing.Any`, `typing.Optional`, `typing.Union`, `dotenv.load_dotenv`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`, `langchain.messages.AIMessage`, `pydantic.ValidationError`, `schemas.types.FunctionAnalysis`, `schemas.types.ClassAnalysis`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, `schemas.types.ClassAnalysisInput`, and `schemas.types.ClassContextInput`.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by setting up the API key, loading system prompts from specified file paths, configuring batch processing settings based on the LLM model name, and initializing various LangChain LLM clients (Google Gemini, OpenAI, custom API, or Ollama) with structured output capabilities for FunctionAnalysis and ClassAnalysis schemas. It ensures essential parameters are provided and handles file loading errors.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the chosen LLM service (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt for function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt for class analysis.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
        - **base_url** (`str`): The base URL for custom LLM endpoints like Ollama or custom OpenAI-compatible APIs, or None if not applicable.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method dynamically sets the `batch_size` attribute for the LLM operations based on the provided `model_name`. It assigns specific batch sizes for various Gemini, Llama, and GPT models, as well as for custom or unknown models, to optimize API calls and respect rate limits. If an unknown model is encountered, it logs a warning and uses a conservative default batch size.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other methods or functions within its source code.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates and validates documentation for a list of functions by interacting with the configured LLM. It takes a list of FunctionAnalysisInput objects, converts them into JSON payloads, and then sends them to the `function_llm` in batches. It handles potential errors during batch processing by extending the results with None for failed items and includes a waiting period between batches to manage API rate limits. The method returns a list of FunctionAnalysis objects or None for failed generations.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing function details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of FunctionAnalysis objects, where each object represents the generated and validated documentation for a function, or None if generation failed for that specific function.
        *   *Usage:* The input context does not specify where this method is called.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating and validating documentation for a batch of classes using the `class_llm`. It processes a list of ClassAnalysisInput objects, serializes them into JSON payloads, and constructs conversation messages with the class system prompt. The method then sends these conversations to the LLM in batches, managing concurrency and rate limits. It includes error handling to log failures and ensures that the output list maintains the order of inputs, returning None for any class documentation that could not be generated.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing class details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of ClassAnalysis objects, where each object represents the generated and validated documentation for a class, or None if generation failed for that specific class.
        *   *Usage:* The input context does not specify where this method is called.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function acts as a test orchestrator for the LLMHelper class, defining pre-computed analysis data for various functions and classes. It simulates the process of generating documentation by initializing an LLMHelper instance with API keys and prompt paths. The function then feeds predefined function analysis inputs to the helper and processes the simulated results, logging successful generations and aggregating them into a final documentation structure. Its primary purpose is to validate the LLMHelper's interaction with Pydantic models and its documentation generation flow.
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function calls no other functions.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare two token counts, specifically 'JSON' and 'TOON' tokens. It takes the token counts and a savings percentage as input. The chart displays the number of tokens for each category, includes a title indicating the calculated savings, and annotates each bar with its corresponding token value. The generated chart is then saved to a specified file path.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of savings to be displayed in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart will be saved.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep durations, which are introduced due to rate-limiting for specific models. It takes start and end times, total items, batch size, and the model name as input. If the model name does not start with "gemini-", the total duration is returned directly. Otherwise, it computes the number of batches and corresponding sleep time, then subtracts this from the total duration, ensuring the net time is not negative.
*   **Parameters:**
    - **start_time** (`float | datetime.datetime`): The starting timestamp or numerical time value for the operation.
    - **end_time** (`float | datetime.datetime`): The ending timestamp or numerical time value for the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model used, which determines if sleep time calculations are applied.
*   **Returns:**
    - **net_time** (`float | int`): The calculated net duration, which is the total duration minus any estimated sleep times, or 0 if total items are 0, or the total duration if the model is not 'gemini-'.
*   **Usage:** This function calls no other functions.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback=None)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing a GitHub repository. It begins by extracting API keys and model names, then clones the specified repository. It proceeds to extract basic project information, construct a file tree, analyze relationships between code components, and build an Abstract Syntax Tree (AST) schema, which is then enriched with relationship data. The function prepares inputs for a Helper LLM to analyze individual functions and classes, and subsequently uses a Main LLM to generate a final report based on the collected and analyzed data. Finally, it saves the generated report and associated metrics, including token savings, to disk.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used in the workflow.
    - **status_callback** (`Callable | None`): An optional callback function to provide status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM, detailing the repository analysis.
    - **metrics** (`dict`): A dictionary containing performance metrics and token usage statistics for the workflow.
*   **Usage:** This function calls no other functions.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function, `update_status`, is designed to handle status reporting. It takes a message as input and performs two primary actions: it conditionally invokes a `status_callback` function with the provided message if `status_callback` is defined, and it always logs the message using `logging.info`. This mechanism allows for flexible status updates, either through a registered callback or via standard logging, or both. The function does not return any value.
*   **Parameters:**
    - **msg** (`str`): The message string to be used for updating the status and for logging.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
*   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks from a given GitHub repository URL. It begins by extracting the repository URL from the input, cloning the repository, and processing its notebook files. It then extracts basic project information and initializes a Large Language Model (LLM) based on the specified model and API keys. The function iterates through each identified notebook, constructs a detailed payload including its XML structure and embedded images, and sends it to the LLM for report generation. Finally, it concatenates all individual notebook reports, saves the combined report to a timestamped markdown file, and returns the final report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): A string containing the GitHub repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various Large Language Model (LLM) providers, such as 'gpt', 'gemini', 'scadsllm', or 'ollama'.
    - **model** (`str`): The name of the specific LLM model to be used for generating notebook reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`Callable | None`): An optional callback function that receives status messages during the workflow execution, allowing for real-time updates.
*   **Returns:**
    - **report** (`str`): A concatenated markdown string containing the analysis reports generated by the LLM for all processed notebooks.
    - **metrics** (`dict`): A dictionary containing performance metrics of the workflow, such as total execution time, the LLM model used, and token usage information.
*   **Usage:** This function calls no other functions.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a multi-modal payload designed for a Gemini-like model by combining textual context with embedded images. It begins by serializing `basic_info` and `nb_path` into an introductory JSON string. The function then processes `xml_content`, using a regular expression to identify and extract text segments and image placeholders. For each image placeholder, it retrieves the corresponding base64 encoded image data from the `images` list and formats it as an `image_url` entry. All extracted text and image components are appended to a list, which is then returned as the complete payload.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing general project or context information.
    - **nb_path** (`str`): The file path of the current notebook being processed.
    - **xml_content** (`str`): An XML string representing the notebook's structure, potentially containing image placeholders.
    - **images** (`list[dict]`): A list of dictionaries, where each dictionary contains 'data' (base64 string) for an image.
*   **Returns:**
    - **payload_content** (`list[dict]`): A list of dictionaries, each formatted as a content part for a multi-modal model, containing either text or image data.
*   **Usage:** This function calls no other functions.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to provide a structured representation for a single parameter within a function's signature. It serves as a data model to consistently store the parameter's name, its data type, and a brief textual description of its purpose. This class facilitates the programmatic handling and documentation of function parameters.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is automatically generated. It initializes an instance of `ParameterDescription` by validating and assigning the provided `name`, `type`, and `description` to its corresponding attributes, ensuring data integrity according to the defined schema.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type hint or inferred type of the parameter.
        - **description** (`str`): A textual explanation of the parameter's purpose.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to standardize the description of a function's return value. It encapsulates three key pieces of information: the name of the return value, its data type, and a textual description. This class serves as a structured data model for representing function outputs consistently across a system.
*   **Instantiation:** The provided context does not specify the instantiation points for this class.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the __init__ method for ReturnDescription is automatically generated. It accepts keyword arguments corresponding to its defined fields (name, type, description) to initialize a new instance of the class, ensuring type validation upon instantiation.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The data type of the return value, represented as a string.
        - **description** (`str`): A detailed textual explanation of what the return value represents or contains.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts within a larger system. It serves as a structured data container, holding two string attributes: 'calls', which describes the external entities or functions it invokes, and 'called_by', which indicates where it is invoked from. This class provides a standardized way to represent the operational context of a code component.
*   **Instantiation:** The provided context does not specify the instantiation points for this class.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
*   **Constructor:**
    *   *Description:* "This class, inheriting from Pydantic's BaseModel, automatically generates an __init__ method. This constructor initializes an instance of UsageContext by accepting 'calls' and 'called_by' as string arguments, which are then stored as instance attributes."
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or external entities called by the component being described.
        - **called_by** (`str`): A string summarizing the functions, methods, or external entities that call the component being described.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** "The `FunctionDescription` class is a Pydantic BaseModel designed to structure and validate the detailed analysis of a Python function. It encapsulates key aspects such as the function's overall purpose, its input parameters, its return values, and its usage context within a larger system. This model serves as a standardized data structure for representing function metadata, facilitating consistent data exchange and processing."
*   **Instantiation:** The specific instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* "As a Pydantic BaseModel, the `__init__` method is automatically generated. It initializes an instance of `FunctionDescription` by validating and assigning values to its defined fields: `overall`, `parameters`, `returns`, and `usage_context`."
    *   *Parameters:*
        - **overall** (`str`): A high-level summary describing the function's purpose and its implementation details.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing an input parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of `ReturnDescription` objects, each describing a value returned by the function.
        - **usage_context** (`UsageContext`): An object containing information about the function's call graph, including what it calls and where it is called from.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** "The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data container, holding the function's unique identifier, a detailed description object (FunctionDescription), and an optional field to report any errors encountered during the analysis process. This model is crucial for standardizing the output of function analysis within a larger system, ensuring consistent data representation."
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "The FunctionAnalysis class inherits from Pydantic's BaseModel, which automatically generates an `__init__` method. This constructor initializes instances of FunctionAnalysis by accepting values for its defined fields: `identifier`, `description`, and `error`."
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the function's analysis. Defaults to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** "The `ConstructorDescription` class is a Pydantic model designed to formally describe the `__init__` method of another Python class. It acts as a structured schema, ensuring that any constructor description includes a textual summary and a list of its individual parameters, each detailed by a `ParameterDescription` object. This model facilitates consistent and machine-readable documentation of class constructors within a larger system."
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance of `ConstructorDescription` by accepting values for its `description` and `parameters` fields, ensuring they conform to the specified types."
    *   *Parameters:*
        - **description** (`str`): A string summarizing the constructor's behavior.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each describing a parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's operational context. It specifically stores information regarding the external dependencies that the class relies upon and the locations or modules where the class is instantiated. This model serves as a structured way to represent and manage contextual data for class analysis.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "The __init__ method for ClassContext is implicitly generated by Pydantic's BaseModel. It allows for the creation of ClassContext instances by providing values for its defined fields: 'dependencies' and 'instantiated_by'. These values are typically passed as keyword arguments during object creation."
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class, indicating what other components or libraries it relies on.
        - **instantiated_by** (`str`): A string describing the primary points or locations within the system where this class is instantiated.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** "The ClassDescription class is a Pydantic BaseModel designed to structure the comprehensive analysis of a Python class. It serves as a data container, encapsulating various aspects such as the class's overall purpose, the details of its constructor, a list of analyses for its individual methods, and its broader usage context within a system. This model is crucial for standardizing the output of a class analysis process, ensuring all relevant information is captured in a consistent format."
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "The `__init__` method for ClassDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance of ClassDescription by validating and assigning values to its defined fields: overall, init_method, methods, and usage_context."
    *   *Parameters:*
        - **overall** (`str`): A string describing the overall purpose and functionality of the class being analyzed.
        - **init_method** (`ConstructorDescription`): An object containing the detailed analysis of the class's constructor (__init__ method).
        - **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each detailing an individual method within the class.
        - **usage_context** (`ClassContext`): An object providing context about the class's dependencies and where it is instantiated.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** "The ClassAnalysis model serves as the primary data structure for encapsulating a comprehensive analysis of a Python class. It is designed to hold a unique identifier for the class, a detailed description object containing its constructor and method analyses, and an optional field to report any errors encountered during the analysis process. This model is fundamental for structuring the output of an AI-driven class analysis system."
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "The ClassAnalysis model is initialized by accepting values for its `identifier`, `description`, and an optional `error` field. As a Pydantic BaseModel, it automatically handles validation and assignment of these fields upon instantiation, ensuring that the provided data conforms to the defined types."
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its constructor and methods.
        - **error** (`Optional[str]`): An optional string indicating an error encountered during the class analysis, or None if the analysis was successful.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** "The `CallInfo` class is a Pydantic BaseModel designed to represent a specific call event within a system, typically used by a relationship analyzer. It encapsulates essential details about a function or method call, including its location and type. This model serves as a structured data container for tracking where and how code components interact."
*   **Instantiation:** This class is not explicitly instantiated by any known components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* "The `__init__` method for `CallInfo` is implicitly generated by Pydantic, as `CallInfo` inherits from `BaseModel`. It initializes an instance of `CallInfo` by validating and assigning values to its fields: `file`, `function`, `mode`, and `line`. This allows for easy creation of call event records with type-checked data."
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that is making the call.
        - **mode** (`str`): The classification of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The specific line number within the file where the call event is located.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** "The FunctionContextInput class is a Pydantic BaseModel designed to encapsulate structured context for analyzing a function. It serves as a data transfer object, holding information about a function's internal and external interactions. Specifically, it tracks a list of entities that the function calls and a list of entities that call the function, providing a clear overview of its operational context."
*   **Instantiation:** The instantiation points for this class are not specified within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "This class implicitly inherits its constructor from Pydantic's BaseModel. The `__init__` method automatically handles the initialization of its fields, `calls` and `called_by`, based on the provided arguments during instantiation. It ensures type validation and data integrity for the structured context."
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings, where each string represents the identifier of another method, class, or function that the analyzed function calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, each providing details about another function or method that calls the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** "This class functions as a Pydantic BaseModel, defining the structured input required for performing a function analysis. It specifies the necessary data fields such as the analysis mode, the function's unique identifier, its raw source code, a list of relevant import statements, and additional contextual information. The model ensures that all essential data for a comprehensive function analysis is provided in a consistent and validated format."
*   **Instantiation:** This class does not explicitly list any locations where it is instantiated within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "As a Pydantic BaseModel, the `__init__` method for this class is implicitly generated by Pydantic. It automatically handles the validation and assignment of attributes based on the defined type hints and any provided default values, ensuring data integrity upon instantiation."
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): The mode of analysis, fixed to "function_analysis".
        - **identifier** (`str`): The unique identifier of the function.
        - **source_code** (`str`): The source code of the function.
        - **imports** (`List[str]`): A list of import statements relevant to the function.
        - **context** (`FunctionContextInput`): Structured contextual information for the function.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** "The MethodContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information about a specific method. It serves as a data schema to represent various aspects of a method's definition and its interactions within a larger codebase. This model is crucial for providing a standardized format for method analysis, allowing for consistent data exchange and processing."
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "This class is a Pydantic model, so its `__init__` method is automatically generated by Pydantic. It initializes an instance of `MethodContextInput` by accepting values for its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`."
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where this method is called from.
        - **args** (`List[str]`): A list of argument names for the method.
        - **docstring** (`Optional[str]`): The docstring of the method, if available.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** "The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information relevant for analyzing a Python class. It defines the schema for input data that describes a class's external dependencies, where it is instantiated, and detailed context for its individual methods. This model facilitates the standardized exchange of class analysis data within a larger AI system."
*   **Instantiation:** The provided context does not specify any locations where this class is instantiated.
*   **Dependencies:** This class does not explicitly declare any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "This class does not explicitly define an `__init__` method. It inherits from `pydantic.BaseModel`, and its constructor is implicitly generated by Pydantic, which initializes its fields based on the provided type hints: `dependencies` (List[str]), `instantiated_by` (List[CallInfo]), and `method_context` (List[MethodContextInput])."
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies of the class.
        - **instantiated_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where the class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of `MethodContextInput` objects detailing the context of the class's methods.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** "The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a schema validator, ensuring that all necessary components like the analysis mode, class identifier, source code, import statements, and contextual information are present and correctly typed before further processing. This class acts as a contract for data exchange within a system that performs class analysis."
*   **Instantiation:** The points of instantiation for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* "The ClassAnalysisInput class does not explicitly define an __init__ method. As a Pydantic BaseModel, its initialization is handled implicitly by Pydantic, which constructs instances based on the type-hinted fields defined within the class. Pydantic automatically validates and assigns values to these attributes upon instantiation."
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): The analysis mode, fixed to "class_analysis".
        - **identifier** (`str`): The unique identifier of the class.
        - **source_code** (`str`): The source code of the class.
        - **imports** (`List[str]`): A list of import statements relevant to the class.
        - **context** (`ClassContextInput`): Structured contextual information for the class.
*   **Methods:**

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends ast.NodeVisitor to traverse an Abstract Syntax Tree (AST) of Python code. Its primary purpose is to extract structured information about imports, functions, and classes from the provided source code. It builds a schema dictionary that categorizes these code elements, distinguishing between top-level functions and methods nested within classes, providing a foundational structure for code analysis.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class depends on the 'ast' module for its core functionality and 'path_to_module' for path manipulation.
*   **Constructor:**
    *   *Description:* The __init__ method initializes the ASTVisitor instance by storing the raw source code, the file's absolute path, and the project's root directory. It calculates the module path based on these inputs and sets up an empty schema dictionary to accumulate discovered imports, functions, and classes. It also initializes an internal attribute, _current_class, to None, which is used to track the class context during AST traversal.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code string of the file being analyzed.
        - **file_path** (`str`): The absolute file path of the Python module being visited.
        - **project_root** (`str`): The root directory of the entire project, used for calculating module paths.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(...)`
        *   *Description:* This method processes 'ast.Import' nodes, which represent simple import statements like 'import module'. It iterates through each alias defined in the import statement and appends the module name to the 'imports' list within the class's schema. After processing the current node, it calls 'self.generic_visit' to ensure continued traversal of the AST.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an 'import' statement.
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.Import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(...)`
        *   *Description:* This method handles 'ast.ImportFrom' nodes, which correspond to 'from module import name' statements. It iterates through the imported aliases and constructs a fully qualified import string (e.g., 'module.name'), which is then appended to the 'imports' list in the class's schema. Following this, it invokes 'self.generic_visit' to continue the AST traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.ImportFrom node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(...)`
        *   *Description:* This method processes 'ast.ClassDef' nodes, which represent class definitions in the source code. It constructs a unique identifier for the class, extracts its name, docstring, and the source code segment. It then creates a 'class_info' dictionary, populates it with these details, and appends it to the 'classes' list in the schema. The method temporarily sets '_current_class' to this 'class_info' to correctly associate any nested methods, performs a generic visit to traverse the class's body, and then resets '_current_class' to None.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.ClassDef node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(...)`
        *   *Description:* This method processes 'ast.FunctionDef' nodes, representing function definitions. It first checks if a class is currently being visited (i.e., '_current_class' is not None). If a class context exists, the function is treated as a method, and its details are appended to the 'method_context' of the current class. Otherwise, it's considered a top-level function, and its information is added to the 'functions' list in the schema. Finally, it calls 'self.generic_visit' to continue traversing the function's body.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function definition (either top-level or a method).
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.FunctionDef node is encountered, and explicitly called by visit_AsyncFunctionDef.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(...)`
        *   *Description:* This method is specifically designed to handle 'ast.AsyncFunctionDef' nodes, which represent asynchronous function definitions. Its implementation simply delegates the processing to the 'visit_FunctionDef' method. This ensures that both synchronous and asynchronous functions are processed using the same logic for schema generation, avoiding code duplication.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** This method is implicitly called by the ast.NodeVisitor's dispatch mechanism when an ast.AsyncFunctionDef node is encountered.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process and analyze Python source code within a repository to generate a structured Abstract Syntax Tree (AST) schema. It provides functionalities to parse Python files, extract their structural components (imports, functions, classes), and then integrate relationship data (like calls and dependencies) into this schema. This class serves as a core component for understanding the structure and interdependencies of a Python codebase.
*   **Instantiation:** Analysis data not available for this component.
*   **Dependencies:** This class has no explicitly listed external functional dependencies.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It currently does not perform any specific setup or attribute assignments, serving as a placeholder or indicating that no initial state is required.
    *   *Parameters:*
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(full_schema, raw_relationships)`
        *   *Description:* This method integrates raw relationship data (incoming and outgoing calls) into a structured full schema. It iterates through functions and classes within the schema's AST nodes, populating their respective 'calls', 'called_by', and 'instantiated_by' contexts. For classes, it also identifies and lists external dependencies based on method calls that are not internal to the class, ensuring a comprehensive view of inter-component relationships.
        *   *Parameters:*
            - **full_schema** (`dict`): The complete schema structure, expected to contain file data with AST nodes for functions and classes.
            - **raw_relationships** (`dict`): A dictionary containing 'outgoing' and 'incoming' call relationships, typically mapping identifiers to lists of related entities.
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary, now enriched with relationship data.
        *   *Usage:* This method calls no other methods, classes, or functions.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(files, repo)`
        *   *Description:* This method processes a list of file objects from a Git repository to build an Abstract Syntax Tree (AST) schema for Python files. It initializes a 'full_schema' dictionary, determines the project root, and then iterates through each file. For Python files, it parses their content into an AST, uses an ASTVisitor to extract schema nodes (imports, functions, classes), and populates the 'full_schema' with this information, handling parsing errors gracefully.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo** (`GitRepository`): An object representing the Git repository, though its specific usage is not detailed within this method's body.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the AST schema of the analyzed Python files, organized by file path.
        *   *Usage:* This method calls `os.path.commonpath`, `os.path.isfile`, `os.path.dirname`, `ast.parse`, and instantiates and calls the `visit` method of `ASTVisitor`.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various large language models (LLMs) to generate structured documentation for Python functions and classes. It abstracts away the complexities of LLM API calls, including model selection, prompt management, batch processing, and rate limiting. The class is designed to ensure robust and validated output by leveraging Pydantic schemas for both input and output, making it a reliable component for automated code documentation generation.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** The class depends on `os`, `json`, `logging`, `time`, `typing.List`, `typing.Dict`, `typing.Any`, `typing.Optional`, `typing.Union`, `dotenv.load_dotenv`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`, `langchain.messages.AIMessage`, `pydantic.ValidationError`, `schemas.types.FunctionAnalysis`, `schemas.types.ClassAnalysis`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, `schemas.types.ClassAnalysisInput`, and `schemas.types.ClassContextInput`.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by setting up the API key, loading system prompts from specified file paths, configuring batch processing settings based on the LLM model name, and initializing various LangChain LLM clients (Google Gemini, OpenAI, custom API, or Ollama) with structured output capabilities for FunctionAnalysis and ClassAnalysis schemas. It ensures essential parameters are provided and handles file loading errors.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the chosen LLM service (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt for function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt for class analysis.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
        - **base_url** (`str`): The base URL for custom LLM endpoints like Ollama or custom OpenAI-compatible APIs, or None if not applicable.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method dynamically sets the `batch_size` attribute for the LLM operations based on the provided `model_name`. It assigns specific batch sizes for various Gemini, Llama, and GPT models, as well as for custom or unknown models, to optimize API calls and respect rate limits. If an unknown model is encountered, it logs a warning and uses a conservative default batch size.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other methods or functions within its source code.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates and validates documentation for a list of functions by interacting with the configured LLM. It takes a list of FunctionAnalysisInput objects, converts them into JSON payloads, and then sends them to the `function_llm` in batches. It handles potential errors during batch processing by extending the results with None for failed items and includes a waiting period between batches to manage API rate limits. The method returns a list of FunctionAnalysis objects or None for failed generations.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing function details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of FunctionAnalysis objects, where each object represents the generated and validated documentation for a function, or None if generation failed for that specific function.
        *   *Usage:* The input context does not specify where this method is called.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating and validating documentation for a batch of classes using the `class_llm`. It processes a list of ClassAnalysisInput objects, serializes them into JSON payloads, and constructs conversation messages with the class system prompt. The method then sends these conversations to the LLM in batches, managing concurrency and rate limits. It includes error handling to log failures and ensures that the output list maintains the order of inputs, returning None for any class documentation that could not be generated.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing class details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of ClassAnalysis objects, where each object represents the generated and validated documentation for a class, or None if generation failed for that specific class.
        *   *Usage:* The input context does not specify where this method is called.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function acts as a test orchestrator for the LLMHelper class, defining pre-computed analysis data for various functions and classes. It simulates the process of generating documentation by initializing an LLMHelper instance with API keys and prompt paths. The function then feeds predefined function analysis inputs to the helper and processes the simulated results, logging successful generations and aggregating them into a final documentation structure. Its primary purpose is to validate the LLMHelper's interaction with Pydantic models and its documentation generation flow.
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function calls no other functions.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare two token counts, specifically 'JSON' and 'TOON' tokens. It takes the token counts and a savings percentage as input. The chart displays the number of tokens for each category, includes a title indicating the calculated savings, and annotates each bar with its corresponding token value. The generated chart is then saved to a specified file path.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of savings to be displayed in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart will be saved.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep durations, which are introduced due to rate-limiting for specific models. It takes start and end times, total items, batch size, and the model name as input. If the model name does not start with "gemini-", the total duration is returned directly. Otherwise, it computes the number of batches and corresponding sleep time, then subtracts this from the total duration, ensuring the net time is not negative.
*   **Parameters:**
    - **start_time** (`float | datetime.datetime`): The starting timestamp or numerical time value for the operation.
    - **end_time** (`float | datetime.datetime`): The ending timestamp or numerical time value for the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model used, which determines if sleep time calculations are applied.
*   **Returns:**
    - **net_time** (`float | int`): The calculated net duration, which is the total duration minus any estimated sleep times, or 0 if total items are 0, or the total duration if the model is not 'gemini-'.
*   **Usage:** This function calls no other functions.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback=None)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing a GitHub repository. It begins by extracting API keys and model names, then clones the specified repository. It proceeds to extract basic project information, construct a file tree, analyze relationships between code components, and build an Abstract Syntax Tree (AST) schema, which is then enriched with relationship data. The function prepares inputs for a Helper LLM to analyze individual functions and classes, and subsequently uses a Main LLM to generate a final report based on the collected and analyzed data. Finally, it saves the generated report and associated metrics, including token savings, to disk.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used in the workflow.
    - **status_callback** (`Callable | None`): An optional callback function to provide status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM, detailing the repository analysis.
    - **metrics** (`dict`): A dictionary containing performance metrics and token usage statistics for the workflow.
*   **Usage:** This function calls no other functions.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function, `update_status`, is designed to handle status reporting. It takes a message as input and performs two primary actions: it conditionally invokes a `status_callback` function with the provided message if `status_callback` is defined, and it always logs the message using `logging.info`. This mechanism allows for flexible status updates, either through a registered callback or via standard logging, or both. The function does not return any value.
*   **Parameters:**
    - **msg** (`str`): The message string to be used for updating the status and for logging.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
*   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks from a given GitHub repository URL. It begins by extracting the repository URL from the input, cloning the repository, and processing its notebook files. It then extracts basic project information and initializes a Large Language Model (LLM) based on the specified model and API keys. The function iterates through each identified notebook, constructs a detailed payload including its XML structure and embedded images, and sends it to the LLM for report generation. Finally, it concatenates all individual notebook reports, saves the combined report to a timestamped markdown file, and returns the final report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): A string containing the GitHub repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various Large Language Model (LLM) providers, such as 'gpt', 'gemini', 'scadsllm', or 'ollama'.
    - **model** (`str`): The name of the specific LLM model to be used for generating notebook reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`Callable | None`): An optional callback function that receives status messages during the workflow execution, allowing for real-time updates.
*   **Returns:**
    - **report** (`str`): A concatenated markdown string containing the analysis reports generated by the LLM for all processed notebooks.
    - **metrics** (`dict`): A dictionary containing performance metrics of the workflow, such as total execution time, the LLM model used, and token usage information.
*   **Usage:** This function calls no other functions.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a multi-modal payload designed for a Gemini-like model by combining textual context with embedded images. It begins by serializing `basic_info` and `nb_path` into an introductory JSON string. The function then processes `xml_content`, using a regular expression to identify and extract text segments and image placeholders. For each image placeholder, it retrieves the corresponding base64 encoded image data from the `images` list and formats it as an `image_url` entry. All extracted text and image components are appended to a list, which is then returned as the complete payload.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing general project or context information.
    - **nb_path** (`str`): The file path of the current notebook being processed.
    - **xml_content** (`str`): An XML string representing the notebook's structure, potentially containing image placeholders.
    - **images** (`list[dict]`): A list of dictionaries, where each dictionary contains 'data' (base64 string) for an image.
*   **Returns:**
    - **payload_content** (`list[dict]`): A list of dictionaries, each formatted as a content part for a multi-modal model, containing either text or image data.
*   **Usage:** This function calls no other functions.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** "This function converts a given file system `filepath` into a Python module import path. It first determines the path relative to the `project_root`, falling back to the base filename if a `ValueError` occurs during relative path calculation. The function then removes the `.py` extension and replaces directory separators with dots. Finally, it specifically handles `__init__.py` files by stripping the `.__init__` suffix to yield the package name."
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path (e.g., 'my_package.my_module').
*   **Usage:** This function calls no other functions.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to build a comprehensive call graph and identify definitions of functions, methods, and classes. It systematically traverses the project directory, parses Python files into ASTs, collects all defined entities, and then resolves the relationships between callers and callees. This class provides a structured way to understand the internal dependencies and interactions within a codebase, making it valuable for code comprehension, refactoring, and impact analysis.
*   **Instantiation:** This class is not explicitly instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer instance by setting the project's root directory, and initializing internal data structures like `definitions`, `call_graph`, and `file_asts`. It also defines a set of directories to ignore during file traversal.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect definitions of functions, methods, and classes. Subsequently, it iterates again to resolve call relationships between these definitions, building a comprehensive call graph. Finally, it clears the cached ASTs and returns the generated call graph.
        *   *Parameters:*
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee pathnames and values are lists of caller information.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* "This method processes the internal `call_graph` to generate a structured representation of outgoing and incoming call relationships. It iterates through the call graph, extracting caller and callee identifiers, and populates two dictionaries: `outgoing` (showing what each entity calls) and `incoming` (showing what calls each entity). The results are then sorted and returned."
        *   *Parameters:*
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, "outgoing" and "incoming". Each value is a dictionary mapping entity identifiers to sorted lists of related entity identifiers.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* "This private helper method traverses the project's root directory to locate all Python files, excluding directories specified in `self.ignore_dirs`. It uses `os.walk` to recursively search through the directory structure and filters for files ending with ".py". The absolute paths of these files are collected and returned."
        *   *Parameters:*
        *   *Returns:*
            - **py_files** (`list[str]`): A list of absolute file paths to all Python files found in the project, excluding ignored directories.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* "This private method is responsible for parsing a given Python file, building its Abstract Syntax Tree (AST), and identifying all function, method, and class definitions within it. It stores the AST in `self.file_asts` and populates `self.definitions` with details like the definition's full path name, file path, line number, and type (function, method, or class). Error handling is included for file reading or parsing issues."
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file to be analyzed for definitions.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* "This private helper method traverses an Abstract Syntax Tree (AST) to find the direct parent node of a given child node. It iterates through all nodes in the tree and checks their children to identify if any child matches the provided `node`. If a parent is found, it is returned; otherwise, `None` is returned."
        *   *Parameters:*
            - **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node for which to find the parent.
        *   *Returns:*
            - **parent** (`ast.AST | None`): The parent AST node if found, otherwise `None`.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* "This private method takes a Python file's path, retrieves its cached AST, and uses a `CallResolverVisitor` to identify all function and method calls within that file. It then extends the class's `call_graph` with the resolved call relationships. If the AST for the file is not found or an error occurs during call resolution, it logs the error and exits gracefully."
        *   *Parameters:*
            - **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call any other functions or methods.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) and identify function and method calls within Python source code. It resolves the fully qualified names of these calls and records caller information, including the file, line number, and type of caller. This class is instrumental in building a call graph or understanding inter-function relationships within a project by mapping call sites to their definitions.
*   **Instantiation:** This class is not explicitly instantiated by any other components based on the provided context.
*   **Dependencies:** This class does not explicitly list any functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with the current file path, the project's root directory, and a dictionary of known definitions. It sets up internal state variables like `module_path`, `scope` for imports, `instance_types` for tracking object types, and `calls` (a defaultdict) to store discovered call relationships.
    *   *Parameters:*
        - **filepath** (`str`): The absolute path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the entire project, used to determine module paths.
        - **definitions** (`dict`): A dictionary mapping fully qualified names to their definitions, used for validating resolved call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* "This method is invoked when the AST visitor encounters a class definition. Its primary responsibility is to update the `current_class_name` attribute to reflect the class being visited, allowing subsequent method definitions within that class to be correctly identified. After processing the class's children, it restores the `current_class_name` to its previous value, ensuring proper scope management during traversal."
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* "This method is triggered upon visiting a function or method definition within the AST. It constructs the full qualified identifier for the function, considering whether it's a method within a class or a top-level function. This identifier is then set as `current_caller_name` to correctly attribute calls made within this function. The original caller name is restored after the function's body has been visited."
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing the function or method definition.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* "This method processes function and method call nodes in the AST. It attempts to resolve the fully qualified name of the callee using the `_resolve_call_qname` helper. If a valid callee is found and exists in the known definitions, it records detailed information about the caller, including its file, line number, full identifier, and type (module, local function, method, or function). This information is then appended to the `calls` dictionary, mapping callees to their callers."
        *   *Parameters:*
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* "This method handles `import` statements in the AST. It iterates through all imported names and their aliases, storing the mapping between the alias (or original name) and the full module name in the `scope` dictionary. This `scope` is later used to resolve qualified names of calls. After processing the import statement, it continues the generic AST traversal."
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* "This method processes `from ... import ...` statements. It determines the full module path for the imported names, correctly handling relative imports based on the `node.level` attribute and the current `module_path`. Each imported name (or its alias) is then mapped to its fully qualified path in the `scope` dictionary. This allows for accurate resolution of imported functions or classes during call analysis."
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* "This method inspects assignment statements to identify object instantiations. Specifically, if an assignment involves a call expression (e.g., `x = MyClass()`) and the called function is a known class from the `scope` and `definitions`, it records the qualified class name as the type for the assigned variable's identifier in `instance_types`. This helps in resolving method calls on instantiated objects later."
        *   *Parameters:*
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* "This private helper method is responsible for determining the fully qualified name (QName) of a function or method being called. It handles two main scenarios: direct calls to names (e.g., `func()`) by checking local scope and module-level definitions, and attribute calls on objects (e.g., `obj.method()`) by looking up the object's type in `instance_types` or its module in `scope`. It returns the resolved QName as a string or `None` if it cannot be resolved."
        *   *Parameters:*
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g. ast.Name, ast.Attribute).
        *   *Returns:*
            - **qualified_name** (`str | None`): The fully qualified name of the callable, or None if it cannot be resolved.
        *   *Usage:* This method does not explicitly call other functions or methods based on the provided context.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to provide a structured representation for a single parameter within a function's signature. It serves as a data model to consistently store the parameter's name, its data type, and a brief textual description of its purpose. This class facilitates the programmatic handling and documentation of function parameters.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the `__init__` method is automatically generated. It initializes an instance of `ParameterDescription` by validating and assigning the provided `name`, `type`, and `description` to its corresponding attributes, ensuring data integrity according to the defined schema.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The type hint or inferred type of the parameter.
        - **description** (`str`): A textual explanation of the parameter's purpose.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to standardize the description of a function's return value. It encapsulates three key pieces of information: the name of the return value, its data type, and a textual description. This class serves as a structured data model for representing function outputs consistently across a system.
*   **Instantiation:** The provided context does not specify the instantiation points for this class.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, the __init__ method for ReturnDescription is automatically generated. It accepts keyword arguments corresponding to its defined fields (name, type, description) to initialize a new instance of the class, ensuring type validation upon instantiation.
    *   *Parameters:*
        - **name** (`str`): The name or identifier of the return value.
        - **type** (`str`): The data type of the return value, represented as a string.
        - **description** (`str`): A detailed textual explanation of what the return value represents or contains.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts within a larger system. It serves as a structured data container, holding two string attributes: 'calls', which describes the external entities or functions it invokes, and 'called_by', which indicates where it is invoked from. This class provides a standardized way to represent the operational context of a code component.
*   **Instantiation:** The provided context does not specify the instantiation points for this class.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in its provided context.
*   **Constructor:**
    *   *Description:* "This class, inheriting from Pydantic's BaseModel, automatically generates an __init__ method. This constructor initializes an instance of UsageContext by accepting 'calls' and 'called_by' as string arguments, which are then stored as instance attributes."
    *   *Parameters:*
        - **calls** (`str`): A string summarizing the functions, methods, or external entities called by the component being described.
        - **called_by** (`str`): A string summarizing the functions, methods, or external entities that call the component being described.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** "The `FunctionDescription` class is a Pydantic BaseModel designed to structure and validate the detailed analysis of a Python function. It encapsulates key aspects such as the function's overall purpose, its input parameters, its return values, and its usage context within a larger system. This model serves as a standardized data structure for representing function metadata, facilitating consistent data exchange and processing."
*   **Instantiation:** The specific instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* "As a Pydantic BaseModel, the `__init__` method is automatically generated. It initializes an instance of `FunctionDescription` by validating and assigning values to its defined fields: `overall`, `parameters`, `returns`, and `usage_context`."
    *   *Parameters:*
        - **overall** (`str`): A high-level summary describing the function's purpose and its implementation details.
        - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing an input parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of `ReturnDescription` objects, each describing a value returned by the function.
        - **usage_context** (`UsageContext`): An object containing information about the function's call graph, including what it calls and where it is called from.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** "The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data container, holding the function's unique identifier, a detailed description object (FunctionDescription), and an optional field to report any errors encountered during the analysis process. This model is crucial for standardizing the output of function analysis within a larger system, ensuring consistent data representation."
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "The FunctionAnalysis class inherits from Pydantic's BaseModel, which automatically generates an `__init__` method. This constructor initializes instances of FunctionAnalysis by accepting values for its defined fields: `identifier`, `description`, and `error`."
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): An object containing the detailed analysis of the function's purpose, parameters, returns, and usage context.
        - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the function's analysis. Defaults to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** "The `ConstructorDescription` class is a Pydantic model designed to formally describe the `__init__` method of another Python class. It acts as a structured schema, ensuring that any constructor description includes a textual summary and a list of its individual parameters, each detailed by a `ParameterDescription` object. This model facilitates consistent and machine-readable documentation of class constructors within a larger system."
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "This class, being a Pydantic BaseModel, automatically generates an `__init__` method. This constructor initializes an instance of `ConstructorDescription` by accepting values for its `description` and `parameters` fields, ensuring they conform to the specified types."
    *   *Parameters:*
        - **description** (`str`): A string summarizing the constructor's behavior.
        - **parameters** (`List[ParameterDescription]`): A list of objects, each describing a parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's operational context. It specifically stores information regarding the external dependencies that the class relies upon and the locations or modules where the class is instantiated. This model serves as a structured way to represent and manage contextual data for class analysis.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "The __init__ method for ClassContext is implicitly generated by Pydantic's BaseModel. It allows for the creation of ClassContext instances by providing values for its defined fields: 'dependencies' and 'instantiated_by'. These values are typically passed as keyword arguments during object creation."
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class, indicating what other components or libraries it relies on.
        - **instantiated_by** (`str`): A string describing the primary points or locations within the system where this class is instantiated.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** "The ClassDescription class is a Pydantic BaseModel designed to structure the comprehensive analysis of a Python class. It serves as a data container, encapsulating various aspects such as the class's overall purpose, the details of its constructor, a list of analyses for its individual methods, and its broader usage context within a system. This model is crucial for standardizing the output of a class analysis process, ensuring all relevant information is captured in a consistent format."
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "The `__init__` method for ClassDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance of ClassDescription by validating and assigning values to its defined fields: overall, init_method, methods, and usage_context."
    *   *Parameters:*
        - **overall** (`str`): A string describing the overall purpose and functionality of the class being analyzed.
        - **init_method** (`ConstructorDescription`): An object containing the detailed analysis of the class's constructor (__init__ method).
        - **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each detailing an individual method within the class.
        - **usage_context** (`ClassContext`): An object providing context about the class's dependencies and where it is instantiated.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** "The ClassAnalysis model serves as the primary data structure for encapsulating a comprehensive analysis of a Python class. It is designed to hold a unique identifier for the class, a detailed description object containing its constructor and method analyses, and an optional field to report any errors encountered during the analysis process. This model is fundamental for structuring the output of an AI-driven class analysis system."
*   **Instantiation:** The specific points of instantiation for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "The ClassAnalysis model is initialized by accepting values for its `identifier`, `description`, and an optional `error` field. As a Pydantic BaseModel, it automatically handles validation and assignment of these fields upon instantiation, ensuring that the provided data conforms to the defined types."
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its constructor and methods.
        - **error** (`Optional[str]`): An optional string indicating an error encountered during the class analysis, or None if the analysis was successful.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** "The `CallInfo` class is a Pydantic BaseModel designed to represent a specific call event within a system, typically used by a relationship analyzer. It encapsulates essential details about a function or method call, including its location and type. This model serves as a structured data container for tracking where and how code components interact."
*   **Instantiation:** This class is not explicitly instantiated by any known components within the provided context.
*   **Dependencies:** This class does not explicitly depend on other components within the provided context.
*   **Constructor:**
    *   *Description:* "The `__init__` method for `CallInfo` is implicitly generated by Pydantic, as `CallInfo` inherits from `BaseModel`. It initializes an instance of `CallInfo` by validating and assigning values to its fields: `file`, `function`, `mode`, and `line`. This allows for easy creation of call event records with type-checked data."
    *   *Parameters:*
        - **file** (`str`): The path to the file where the call event occurred.
        - **function** (`str`): The name of the function or method that is making the call.
        - **mode** (`str`): The classification of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The specific line number within the file where the call event is located.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** "The FunctionContextInput class is a Pydantic BaseModel designed to encapsulate structured context for analyzing a function. It serves as a data transfer object, holding information about a function's internal and external interactions. Specifically, it tracks a list of entities that the function calls and a list of entities that call the function, providing a clear overview of its operational context."
*   **Instantiation:** The instantiation points for this class are not specified within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "This class implicitly inherits its constructor from Pydantic's BaseModel. The `__init__` method automatically handles the initialization of its fields, `calls` and `called_by`, based on the provided arguments during instantiation. It ensures type validation and data integrity for the structured context."
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings, where each string represents the identifier of another method, class, or function that the analyzed function calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, each providing details about another function or method that calls the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** "This class functions as a Pydantic BaseModel, defining the structured input required for performing a function analysis. It specifies the necessary data fields such as the analysis mode, the function's unique identifier, its raw source code, a list of relevant import statements, and additional contextual information. The model ensures that all essential data for a comprehensive function analysis is provided in a consistent and validated format."
*   **Instantiation:** This class does not explicitly list any locations where it is instantiated within the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "As a Pydantic BaseModel, the `__init__` method for this class is implicitly generated by Pydantic. It automatically handles the validation and assignment of attributes based on the defined type hints and any provided default values, ensuring data integrity upon instantiation."
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): The mode of analysis, fixed to "function_analysis".
        - **identifier** (`str`): The unique identifier of the function.
        - **source_code** (`str`): The source code of the function.
        - **imports** (`List[str]`): A list of import statements relevant to the function.
        - **context** (`FunctionContextInput`): Structured contextual information for the function.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** "The MethodContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information about a specific method. It serves as a data schema to represent various aspects of a method's definition and its interactions within a larger codebase. This model is crucial for providing a standardized format for method analysis, allowing for consistent data exchange and processing."
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* "This class is a Pydantic model, so its `__init__` method is automatically generated by Pydantic. It initializes an instance of `MethodContextInput` by accepting values for its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`."
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the method.
        - **calls** (`List[str]`): A list of identifiers for other methods, classes, or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where this method is called from.
        - **args** (`List[str]`): A list of argument names for the method.
        - **docstring** (`Optional[str]`): The docstring of the method, if available.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** "The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured contextual information relevant for analyzing a Python class. It defines the schema for input data that describes a class's external dependencies, where it is instantiated, and detailed context for its individual methods. This model facilitates the standardized exchange of class analysis data within a larger AI system."
*   **Instantiation:** The provided context does not specify any locations where this class is instantiated.
*   **Dependencies:** This class does not explicitly declare any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* "This class does not explicitly define an `__init__` method. It inherits from `pydantic.BaseModel`, and its constructor is implicitly generated by Pydantic, which initializes its fields based on the provided type hints: `dependencies` (List[str]), `instantiated_by` (List[CallInfo]), and `method_context` (List[MethodContextInput])."
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies of the class.
        - **instantiated_by** (`List[CallInfo]`): A list of `CallInfo` objects indicating where the class is instantiated.
        - **method_context** (`List[MethodContextInput]`): A list of `MethodContextInput` objects detailing the context of the class's methods.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** "The ClassAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for generating a ClassAnalysis object. It serves as a schema validator, ensuring that all necessary components like the analysis mode, class identifier, source code, import statements, and contextual information are present and correctly typed before further processing. This class acts as a contract for data exchange within a system that performs class analysis."
*   **Instantiation:** The points of instantiation for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies.
*   **Constructor:**
    *   *Description:* "The ClassAnalysisInput class does not explicitly define an __init__ method. As a Pydantic BaseModel, its initialization is handled implicitly by Pydantic, which constructs instances based on the type-hinted fields defined within the class. Pydantic automatically validates and assigns values to these attributes upon instantiation."
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): The analysis mode, fixed to "class_analysis".
        - **identifier** (`str`): The unique identifier of the class.
        - **source_code** (`str`): The source code of the class.
        - **imports** (`List[str]`): A list of import statements relevant to the class.
        - **context** (`ClassContextInput`): Structured contextual information for the class.
*   **Methods:**

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** "This function converts a given file system path into a Python module path string. It first attempts to make the path relative to a specified project root, falling back to just the basename if the relative path cannot be determined. It then removes the '.py' extension if present and replaces system path separators with dots. Finally, it removes the '.__init__' suffix if the module path represents an initialization file, returning the cleaned module path."
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the file that needs to be converted.
    - **project_root** (`str`): The root directory of the project, used as a base to calculate the relative module path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path string, e.g., 'my_package.my_module'.
*   **Usage:** This function calls no other functions.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various large language models (LLMs) to generate structured documentation for Python functions and classes. It abstracts away the complexities of LLM API calls, including model selection, prompt management, batch processing, and rate limiting. The class is designed to ensure robust and validated output by leveraging Pydantic schemas for both input and output, making it a reliable component for automated code documentation generation.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** The class depends on `os`, `json`, `logging`, `time`, `typing.List`, `typing.Dict`, `typing.Any`, `typing.Optional`, `typing.Union`, `dotenv.load_dotenv`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`, `langchain.messages.AIMessage`, `pydantic.ValidationError`, `schemas.types.FunctionAnalysis`, `schemas.types.ClassAnalysis`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, `schemas.types.ClassAnalysisInput`, and `schemas.types.ClassContextInput`.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by setting up the API key, loading system prompts from specified file paths, configuring batch processing settings based on the LLM model name, and initializing various LangChain LLM clients (Google Gemini, OpenAI, custom API, or Ollama) with structured output capabilities for FunctionAnalysis and ClassAnalysis schemas. It ensures essential parameters are provided and handles file loading errors.
    *   *Parameters:*
        - **api_key** (`str`): The API key for the chosen LLM service (e.g., Gemini, OpenAI).
        - **function_prompt_path** (`str`): The file path to the system prompt for function analysis.
        - **class_prompt_path** (`str`): The file path to the system prompt for class analysis.
        - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
        - **base_url** (`str`): The base URL for custom LLM endpoints like Ollama or custom OpenAI-compatible APIs, or None if not applicable.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This private method dynamically sets the `batch_size` attribute for the LLM operations based on the provided `model_name`. It assigns specific batch sizes for various Gemini, Llama, and GPT models, as well as for custom or unknown models, to optimize API calls and respect rate limits. If an unknown model is encountered, it logs a warning and uses a conservative default batch size.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
        *   *Usage:* This method does not explicitly call other methods or functions within its source code.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates and validates documentation for a list of functions by interacting with the configured LLM. It takes a list of FunctionAnalysisInput objects, converts them into JSON payloads, and then sends them to the `function_llm` in batches. It handles potential errors during batch processing by extending the results with None for failed items and includes a waiting period between batches to manage API rate limits. The method returns a list of FunctionAnalysis objects or None for failed generations.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing function details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[FunctionAnalysis]]`): A list of FunctionAnalysis objects, where each object represents the generated and validated documentation for a function, or None if generation failed for that specific function.
        *   *Usage:* The input context does not specify where this method is called.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method is responsible for generating and validating documentation for a batch of classes using the `class_llm`. It processes a list of ClassAnalysisInput objects, serializes them into JSON payloads, and constructs conversation messages with the class system prompt. The method then sends these conversations to the LLM in batches, managing concurrency and rate limits. It includes error handling to log failures and ensures that the output list maintains the order of inputs, returning None for any class documentation that could not be generated.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing class details for which documentation is to be generated.
        *   *Returns:*
            - **None** (`List[Optional[ClassAnalysis]]`): A list of ClassAnalysis objects, where each object represents the generated and validated documentation for a class, or None if generation failed for that specific class.
        *   *Usage:* The input context does not specify where this method is called.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function acts as a test orchestrator for the LLMHelper class, defining pre-computed analysis data for various functions and classes. It simulates the process of generating documentation by initializing an LLMHelper instance with API keys and prompt paths. The function then feeds predefined function analysis inputs to the helper and processes the simulated results, logging successful generations and aggregating them into a final documentation structure. Its primary purpose is to validate the LLMHelper's interaction with Pydantic models and its documentation generation flow.
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function calls no other functions.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare two token counts, specifically 'JSON' and 'TOON' tokens. It takes the token counts and a savings percentage as input. The chart displays the number of tokens for each category, includes a title indicating the calculated savings, and annotates each bar with its corresponding token value. The generated chart is then saved to a specified file path.
*   **Parameters:**
    - **json_tokens** (`int`): The number of tokens associated with the JSON format.
    - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    - **savings_percent** (`float`): The calculated percentage of savings to be displayed in the chart title.
    - **output_path** (`str`): The file path where the generated bar chart will be saved.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep durations, which are introduced due to rate-limiting for specific models. It takes start and end times, total items, batch size, and the model name as input. If the model name does not start with "gemini-", the total duration is returned directly. Otherwise, it computes the number of batches and corresponding sleep time, then subtracts this from the total duration, ensuring the net time is not negative.
*   **Parameters:**
    - **start_time** (`float | datetime.datetime`): The starting timestamp or numerical time value for the operation.
    - **end_time** (`float | datetime.datetime`): The ending timestamp or numerical time value for the operation.
    - **total_items** (`int`): The total number of items processed.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model used, which determines if sleep time calculations are applied.
*   **Returns:**
    - **net_time** (`float | int`): The calculated net duration, which is the total duration minus any estimated sleep times, or 0 if total items are 0, or the total duration if the model is not 'gemini-'.
*   **Usage:** This function calls no other functions.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback=None)`
*   **Description:** This function orchestrates a comprehensive workflow for analyzing a GitHub repository. It begins by extracting API keys and model names, then clones the specified repository. It proceeds to extract basic project information, construct a file tree, analyze relationships between code components, and build an Abstract Syntax Tree (AST) schema, which is then enriched with relationship data. The function prepares inputs for a Helper LLM to analyze individual functions and classes, and subsequently uses a Main LLM to generate a final report based on the collected and analyzed data. Finally, it saves the generated report and associated metrics, including token savings, to disk.
*   **Parameters:**
    - **input** (`str`): The initial input string, expected to contain a GitHub repository URL.
    - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used in the workflow.
    - **status_callback** (`Callable | None`): An optional callback function to provide status updates during the workflow execution.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM, detailing the repository analysis.
    - **metrics** (`dict`): A dictionary containing performance metrics and token usage statistics for the workflow.
*   **Usage:** This function calls no other functions.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function, `update_status`, is designed to handle status reporting. It takes a message as input and performs two primary actions: it conditionally invokes a `status_callback` function with the provided message if `status_callback` is defined, and it always logs the message using `logging.info`. This mechanism allows for flexible status updates, either through a registered callback or via standard logging, or both. The function does not return any value.
*   **Parameters:**
    - **msg** (`str`): The message string to be used for updating the status and for logging.
*   **Returns:**
*   **Usage:** This function calls no other functions.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
*   **Description:** This function orchestrates a workflow to analyze Jupyter notebooks from a given GitHub repository URL. It begins by extracting the repository URL from the input, cloning the repository, and processing its notebook files. It then extracts basic project information and initializes a Large Language Model (LLM) based on the specified model and API keys. The function iterates through each identified notebook, constructs a detailed payload including its XML structure and embedded images, and sends it to the LLM for report generation. Finally, it concatenates all individual notebook reports, saves the combined report to a timestamped markdown file, and returns the final report along with execution metrics.
*   **Parameters:**
    - **input** (`str`): A string containing the GitHub repository URL to be analyzed.
    - **api_keys** (`dict`): A dictionary containing API keys for various Large Language Model (LLM) providers, such as 'gpt', 'gemini', 'scadsllm', or 'ollama'.
    - **model** (`str`): The name of the specific LLM model to be used for generating notebook reports (e.g., 'gpt-4', 'gemini-pro').
    - **status_callback** (`Callable | None`): An optional callback function that receives status messages during the workflow execution, allowing for real-time updates.
*   **Returns:**
    - **report** (`str`): A concatenated markdown string containing the analysis reports generated by the LLM for all processed notebooks.
    - **metrics** (`dict`): A dictionary containing performance metrics of the workflow, such as total execution time, the LLM model used, and token usage information.
*   **Usage:** This function calls no other functions.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a multi-modal payload designed for a Gemini-like model by combining textual context with embedded images. It begins by serializing `basic_info` and `nb_path` into an introductory JSON string. The function then processes `xml_content`, using a regular expression to identify and extract text segments and image placeholders. For each image placeholder, it retrieves the corresponding base64 encoded image data from the `images` list and formats it as an `image_url` entry. All extracted text and image components are appended to a list, which is then returned as the complete payload.
*   **Parameters:**
    - **basic_info** (`dict`): A dictionary containing general project or context information.
    - **nb_path** (`str`): The file path of the current notebook being processed.
    - **xml_content** (`str`): An XML string representing the notebook's structure, potentially containing image placeholders.
    - **images** (`list[dict]`): A list of dictionaries, where each dictionary contains 'data' (base64 string) for an image.
*   **Returns:**
    - **payload_content** (`list[dict]`): A list of dictionaries, each formatted as a content part for a multi-modal model, containing either text or image data.
*   **Usage:** This function calls no other functions.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** "This function converts a given file system `filepath` into a Python module import path. It first determines the path relative to the `project_root`, falling back to the base filename if a `ValueError` occurs during relative path calculation. The function then removes the `.py` extension and replaces directory separators with dots. Finally, it specifically handles `__init__.py` files by stripping the `.__init__` suffix to yield the package name."
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to a Python file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The converted Python module path (e.g., 'my_package.my_module').
*   **Usage:** This function calls no other functions.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to build a comprehensive call graph and identify definitions of functions, methods, and classes. It systematically traverses the project directory, parses Python files into ASTs, collects all defined entities, and then resolves the relationships between callers and callees. This class provides a structured way to understand the internal dependencies and interactions within a codebase, making it valuable for code comprehension, refactoring, and impact analysis.
*   **Instantiation:** This class is not explicitly instantiated by any other components in the provided context.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer instance by setting the project's root directory, and initializing internal data structures like `definitions`, `call_graph`, and `file_asts`. It also defines a set of directories to ignore during file traversal.
    *   *Parameters:*
        - **project_root** (`str`): The root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project, then iterates through them to collect definitions of functions, methods, and classes. Subsequently, it iterates again to resolve call relationships between these definitions, building a comprehensive call graph. Finally, it clears the cached ASTs and returns the generated call graph.
        *   *Parameters:*
        *   *Returns:*
            - **call_graph** (`defaultdict(list)`): A dictionary representing the call graph, where keys are callee pathnames and values are lists of caller information.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* "This method processes the internal `call_graph` to generate a structured representation of outgoing and incoming call relationships. It iterates through the call graph, extracting caller and callee identifiers, and populates two dictionaries: `outgoing` (showing what each entity calls) and `incoming` (showing what calls each entity). The results are then sorted and returned."
        *   *Parameters:*
        *   *Returns:*
            - **relationships** (`dict`): A dictionary containing two keys, "outgoing" and "incoming". Each value is a dictionary mapping entity identifiers to sorted lists of related entity identifiers.
        *   *Usage:* This method does not explicitly call any other functions or methods.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview (can be accessed under 'basic_info')
    - **Description:** Information not found
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** Information not found

*   **Repository Structure:**
    ```mermaid
    graph LR
        root -->|SystemPrompts| SystemPrompts
        root -->|backend| backend
        root -->|database| database
        root -->|frontend| frontend
        root -->|notizen| notizen
        root -->|.env.example|.env.example
        root -->|.gitignore|.gitignore
        root -->|analysis_output.json| analysis_output.json
        root -->|output.json| output.json
        root -->|output.toon| output.toon
        root -->|readme.md| readme.md
        root -->|requirements.txt| requirements.txt
        root -->|test.json| test.json
        SystemPrompts -->|SystemPromptClassHelperLLM.txt| SystemPrompts/SystemPromptClassHelperLLM.txt
        SystemPrompts -->|SystemPromptFunctionHelperLLM.txt| SystemPrompts/SystemPromptFunctionHelperLLM.txt
        SystemPrompts -->|SystemPromptHelperLLM.txt| SystemPrompts/SystemPromptHelperLLM.txt
        SystemPrompts -->|SystemPromptMainLLM.txt| SystemPrompts/SystemPromptMainLLM.txt
        SystemPrompts -->|SystemPromptMainLLMToon.txt| SystemPrompts/SystemPromptMainLLMToon.txt
        SystemPrompts -->|SystemPromptNotebookLLM.txt| SystemPrompts/SystemPromptNotebookLLM.txt
        backend -->|AST_Schema.py| backend/AST_Schema.py
        backend -->|File_Dependency.py| backend/File_Dependency.py
        backend -->|HelperLLM.py| backend/HelperLLM.py
        backend -->|MainLLM.py| backend/MainLLM.py
        backend -->|__init__.py| backend/__init__.py
        backend -->|basic_info.py| backend/basic_info.py
        backend -->|callgraph.py| backend/callgraph.py
        backend -->|converter.py| backend/converter.py
        backend -->|getRepo.py| backend/getRepo.py
        backend -->|main.py| backend/main.py
        backend -->|relationship_analyzer.py| backend/relationship_analyzer.py
        backend -->|scads_key_test.py| backend/scads_key_test.py
        database -->|db.py| database/db.py
        frontend -->|.streamlit|.streamlit
        frontend -->|__init__.py| frontend/__init__.py
        frontend -->|frontend.py| frontend/frontend.py
        frontend -->|gifs| gifs
        .streamlit -->|config.toml| frontend/.streamlit/config.toml
        gifs -->|4j.gif| frontend/gifs/4j.gif
        notizen -->|Report Agenda.txt| notizen/Report Agenda.txt
        notizen -->|Zwischenpraesentation Agenda.txt| notizen/Zwischenpraesentation Agenda.txt
        notizen -->|doc_bestandteile.md| notizen/doc_bestandteile.md
        notizen -->|grafiken| grafiken
        notizen -->|notizen.md| notizen/notizen.md
        notizen -->|paul_notizen.md| notizen/paul_notizen.md
        notizen -->|praesentation_notizen.md| notizen/praesentation_notizen.md
        notizen -->|technische_notizen.md| notizen/technische_notizen.md
        grafiken -->|"1"|"2"|"Flask-Repo"|"Repo-onboarding"
        grafiken/1 -->|File_Dependency_Graph_Repo.dot| notizen/grafiken/1/File_Dependency_Graph_Repo.dot
        grafiken/1 -->|global_callgraph.png| notizen/grafiken/1/global_callgraph.png
        grafiken/1 -->|global_graph.png| notizen/grafiken/1/global_graph.png
        grafiken/1 -->|global_graph_2.png| notizen/grafiken/1/global_graph_2.png
        grafiken/1 -->|repo.dot| notizen/grafiken/1/repo.dot
        grafiken/2 -->|FDG_repo.dot| notizen/grafiken/2/FDG_repo.dot
        grafiken/2 -->|fdg_graph.png| notizen/grafiken/2/fdg_graph.png
        grafiken/2 -->|fdg_graph_2.png| notizen/grafiken/2/fdg_graph_2.png
        grafiken/2 -->|filtered_callgraph_flask.png| notizen/grafiken/2/filtered_callgraph_flask.png
        grafiken/2 -->|filtered_callgraph_repo-agent.png| notizen/grafiken/2/filtered_callgraph_repo-agent.png
        grafiken/2 -->|filtered_callgraph_repo-agent_3.png| notizen/grafiken/2/filtered_callgraph_repo-agent_3.png
        grafiken/2 -->|filtered_repo_callgraph_flask.dot| notizen/grafiken/2/filtered_repo_callgraph_flask.dot
        grafiken/2 -->|filtered_repo_callgraph_repo-agent-3.dot| notizen/grafiken/2/filtered_repo_callgraph_repo-agent-3.dot
        grafiken/2 -->|filtered_repo_callgraph_repo-agent.dot| notizen/grafiken/2/filtered_repo_callgraph_repo-agent.dot
        grafiken/2 -->|global_callgraph.png| notizen/grafiken/2/global_callgraph.png
        grafiken/2 -->|graph_flask.md| notizen/grafiken/2/graph_flask.md
        grafiken/2 -->|repo.dot| notizen/grafiken/2/repo.dot
        grafiken/Flask-Repo -->|__init__.dot| notizen/grafiken/Flask-Repo/__init__.dot
        grafiken/Flask-Repo -->|__main__.dot| notizen/grafiken/Flask-Repo/__main__.dot
        grafiken/Flask-Repo -->|app.dot| notizen/grafiken/Flask-Repo/app.dot
        grafiken/Flask-Repo -->|auth.dot| notizen/grafiken/Flask-Repo/auth.dot
        grafiken/Flask-Repo -->|blog.dot| notizen/grafiken/Flask-Repo/blog.dot
        grafiken/Flask-Repo -->|blueprints.dot| notizen/grafiken/Flask-Repo/blueprints.dot
        grafiken/Flask-Repo -->|cli.dot| notizen/grafiken/Flask-Repo/cli.dot
        grafiken/Flask-Repo -->|conf.dot| notizen/grafiken/Flask-Repo/conf.dot
        grafiken/Flask-Repo -->|config.dot| notizen/grafiken/Flask-Repo/config.dot
        grafiken/Flask-Repo -->|conftest.dot| notizen/grafiken/Flask-Repo/conftest.dot
        grafiken/Flask-Repo -->|ctx.dot| notizen/grafiken/Flask-Repo/ctx.dot
        grafiken/Flask-Repo -->|db.dot| notizen/grafiken/Flask-Repo/db.dot
        grafiken/Flask-Repo -->|debughelpers.dot| notizen/grafiken/Flask-Repo/debughelpers.dot
        grafiken/Flask-Repo -->|factory.dot| notizen/grafiken/Flask-Repo/factory.dot
        grafiken/Flask-Repo -->|flask.dot| notizen/grafiken/Flask-Repo/flask.dot
        grafiken/Flask-Repo -->|globals.dot| notizen/grafiken/Flask-Repo/globals.dot
        grafiken/Flask-Repo -->|hello.dot| notizen/grafiken/Flask-Repo/hello.dot
        grafiken/Flask-Repo -->|helpers.dot| notizen/grafiken/Flask-Repo/helpers.dot
        grafiken/Flask-Repo -->|importerrorapp.dot| notizen/grafiken/Flask-Repo/importerrorapp.dot
        grafiken/Flask-Repo -->|logging.dot| notizen/grafiken/Flask-Repo/logging.dot
        grafiken/Flask-Repo -->|make_celery.dot| notizen/grafiken/Flask-Repo/make_celery.dot
        grafiken/Flask-Repo -->|multiapp.dot| notizen/grafiken/Flask-Repo/multiapp.dot
        grafiken/Flask-Repo -->|provider.dot| notizen/grafiken/Flask-Repo/provider.dot
        grafiken/Flask-Repo -->|scaffold.dot| notizen/grafiken/Flask-Repo/scaffold.dot
        grafiken/Flask-Repo -->|sessions.dot| notizen/grafiken/Flask-Repo/sessions.dot
        grafiken/Flask-Repo -->|signals.dot| notizen/grafiken/Flask-Repo/signals.dot
        grafiken/Flask-Repo -->|tag.dot| notizen/grafiken/Flask-Repo/tag.dot
        grafiken/Flask-Repo -->|tasks.dot| notizen/grafiken/Flask-Repo/tasks.dot
        grafiken/Flask-Repo -->|templating.dot| notizen/grafiken/Flask-Repo/templating.dot
        grafiken/Flask-Repo -->|test_appctx.dot| notizen/grafiken/Flask-Repo/test_appctx.dot
        grafiken/Flask-Repo -->|test_async.dot| notizen/grafiken/Flask-Repo/test_async.dot
        grafiken/Flask-Repo -->|test_auth.dot| notizen/grafiken/Flask-Repo/test_auth.dot
        grafiken/Flask-Repo -->|test_basic.dot| notizen/grafiken/Flask-Repo/test_basic.dot
        grafiken/Flask-Repo -->|test_blog.dot| notizen/grafiken/Flask-Repo/test_blog.dot
        grafiken/Flask-Repo -->|test_blueprints.dot| notizen/grafiken/Flask-Repo/test_blueprints.dot
        grafiken/Flask-Repo -->|test_cli.dot| notizen/grafiken/Flask-Repo/test_cli.dot
        grafiken/Flask-Repo -->|test_config.dot| notizen/grafiken/Flask-Repo/test_config.dot
        grafiken/Flask-Repo -->|test_config.png| notizen/grafiken/Flask-Repo/test_config.png
        grafiken/Flask-Repo -->|test_converters.dot| notizen/grafiken/Flask-Repo/test_converters.dot
        grafiken/Flask-Repo -->|test_db.dot| notizen/grafiken/Flask-Repo/test_db.dot
        grafiken/Flask-Repo -->|test_factory.dot| notizen/grafiken/Flask-Repo/test_factory.dot
        grafiken/Flask-Repo -->|test_helpers.dot| notizen/grafiken/Flask-Repo/test_helpers.dot
        grafiken/Flask-Repo -->|test_instance_config.dot| notizen/grafiken/Flask-Repo/test_instance_config.dot
        grafiken/Flask-Repo -->|test_js_example.dot| notizen/grafiken/Flask-Repo/test_js_example.dot
        grafiken/Flask-Repo -->|test_json.dot| notizen/grafiken/Flask-Repo/test_json.dot
        grafiken/Flask-Repo -->|test_json_tag.dot| notizen/grafiken/Flask-Repo/test_json_tag.dot
        grafiken/Flask-Repo -->|test_logging.dot| notizen/grafiken/Flask-Repo/test_logging.dot
        grafiken/Flask-Repo -->|test_regression.dot| notizen/grafiken/Flask-Repo/test_regression.dot
        grafiken/Flask-Repo -->|test_reqctx.dot| notizen/grafiken/Flask-Repo/test_reqctx.dot
        grafiken/Flask-Repo -->|test_request.dot| notizen/grafiken/Flask-Repo/test_request.dot
        grafiken/Flask-Repo -->|test_session_interface.dot| notizen/grafiken/Flask-Repo/test_session_interface.dot
        grafiken/Flask-Repo -->|test_signals.dot| notizen/grafiken/Flask-Repo/test_signals.dot
        grafiken/Flask-Repo -->|test_subclassing.dot| notizen/grafiken/Flask-Repo/test_subclassing.dot
        grafiken/Flask-Repo -->|test_templating.dot| notizen/grafiken/Flask-Repo/test_templating.dot
        grafiken/Flask-Repo -->|test_testing.dot| notizen/grafiken/Flask-Repo/test_testing.dot
        grafiken/Flask-Repo -->|test_user_error_handler.dot| notizen/grafiken/Flask-Repo/test_user_error_handler.dot
        grafiken/Flask-Repo -->|test_views.dot| notizen/grafiken/Flask-Repo/test_views.dot
        grafiken/Flask-Repo -->|testing.dot| notizen/grafiken/Flask-Repo/testing.dot
        grafiken/Flask-Repo -->|typing.dot| notizen/grafiken/Flask-Repo/typing.dot
        grafiken/Flask-Repo -->|typing_app_decorators.dot| notizen/grafiken/Flask-Repo/typing_app_decorators.dot
        grafiken/Flask-Repo -->|typing_error_handler.dot| notizen/grafiken/Flask-Repo/typing_error_handler.dot
        grafiken/Flask-Repo -->|typing_route.dot| notizen/grafiken/Flask-Repo/typing_route.dot
        grafiken/Flask-Repo -->|views.dot| notizen/grafiken/Flask-Repo/views.dot
        grafiken/Flask-Repo -->|wrappers.dot| notizen/grafiken/Flask-Repo/wrappers.dot
        grafiken/Flask-Repo -->|wsgi.dot| notizen/grafiken/Flask-Repo/wsgi.dot
        grafiken/Repo-onboarding -->|AST.dot| notizen/grafiken/Repo-onboarding/AST.dot
        grafiken/Repo-onboarding -->|Frontend.dot| notizen/grafiken/Repo-onboarding/Frontend.dot
        grafiken/Repo-onboarding -->|HelperLLM.dot| notizen/grafiken/Repo-onboarding/HelperLLM.dot
        grafiken/Repo-onboarding -->|HelperLLM.png| notizen/grafiken/Repo-onboarding/HelperLLM.png
        grafiken/Repo-onboarding -->|MainLLM.dot| notizen/grafiken/Repo-onboarding/MainLLM.dot
        grafiken/Repo-onboarding -->|agent.dot| notizen/grafiken/Repo-onboarding/agent.dot
        grafiken/Repo-onboarding -->|basic_info.dot| notizen/grafiken/Repo-onboarding/basic_info.dot
        grafiken/Repo-onboarding -->|callgraph.dot| notizen/grafiken/Repo-onboarding/callgraph.dot
        grafiken/Repo-onboarding -->|getRepo.dot| notizen/grafiken/Repo-onboarding/getRepo.dot
        grafiken/Repo-onboarding -->|graph_AST.png| notizen/grafiken/Repo-onboarding/graph_AST.png
        grafiken/Repo-onboarding -->|graph_AST2.png| notizen/grafiken/Repo-onboarding/graph_AST2.png
        grafiken/Repo-onboarding -->|graph_AST3.png| notizen/grafiken/Repo-onboarding/graph_AST3.png
        grafiken/Repo-onboarding -->|main.dot| notizen/grafiken/Repo-onboarding/main.dot
        grafiken/Repo-onboarding -->|tools.dot| notizen/grafiken/Repo-onboarding/tools.dot
        grafiken/Repo-onboarding -->|types.dot| notizen/grafiken/Repo-onboarding/types.dot
        root -->|result| result
        result -->|ast_schema_01_12_2025_11-49-24.json| result/ast_schema_01_12_2025_11-49-24.json
        result -->|notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md| result/notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md
        result -->|notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md| result/notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md
        result -->|notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md| result/notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md
        result -->|notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md| result/notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md
        result -->|notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md| result/notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md
        result -->|notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md| result/notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md
        result -->|report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| result/report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result -->|report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| result/report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result -->|report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| result/report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result -->|report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md| result/report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result -->|report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md| result/report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result -->|report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md| result/report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result -->|report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md| result/report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md
        result -->|report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| result/report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result -->|report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md| result/report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result -->|report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md| result/report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md
        result -->|report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md| result/report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md
        result -->|report_14_11_2025_14-52-36.md| result/report_14_11_2025_14-52-36.md
        result -->|report_14_11_2025_15-21-53.md| result/report_14_11_2025_15-21-53.md
        result -->|report_14_11_2025_15-26-24.md| result/report_14_11_2025_15-26-24.md
        result -->|report_21_11_2025_15-43-30.md| result/report_21_11_2025_15-43-30.md
        result -->|report_21_11_2025_16-06-12.md| result/report_21_11_2025_16-06-12.md
        result -->|report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md| result/report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md
        result -->|report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md| result/report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md
        result -->|result_2025-11-11_12-30-53.md| result/result_2025-11-11_12-30-53.md
        result -->|result_2025-11-11_12-43-51.md| result/result_2025-11-11_12-43-51.md
        result -->|result_2025-11-11_12-45-37.md| result/result_2025-11-11_12-45-37.md

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
    
    If Repo contains requirements.txt:
    pip install -r requirements.txt

### Setup Guide
    Information not found
### Quick Startup
    Information not found

    ## 3. Use Cases & Commands
    This project appears to be a sophisticated tool for analyzing and documenting Python code repositories. It leverages Large Language Models (LLMs) to understand code structure, generate documentation, and provide insights into code relationships and potential savings from format conversions.

    Key use cases include:
    *   **Repository Analysis:** Cloning a Git repository and analyzing its codebase.
    *   **LLM-driven Documentation:** Generating documentation for functions and classes using LLMs.
    *   **Code Relationship Mapping:** Building call graphs and identifying dependencies between different code components.
    *   **Notebook Processing:** Converting Jupyter notebooks into structured XML formats, potentially for analysis or integration with LLMs.
    *   **Format Comparison:** Evaluating token usage and savings between JSON and TOON formats using LLMs.
    *   **User Management:** Storing user credentials and API keys securely (encrypted) in a database.
    *   **Interactive Chat Interface:** Providing a Streamlit-based frontend for users to interact with LLMs, manage chats, and provide feedback on responses.

    Specific commands or entry points are not detailed in the provided metadata, but the project structure suggests a primary execution likely managed through scripts like `main.py` or `frontend.py`.

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

    ## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` and is designed to traverse an Abstract Syntax Tree (AST) of a Python source file. Its primary purpose is to extract structured information about imports, functions, and classes defined within the visited source code. It builds a `schema` dictionary that categorizes these elements, differentiating between standalone functions and methods within classes, and handles both regular and asynchronous function definitions by delegating to a common processing method.
*   **Instantiation:** Not explicitly listed.
*   **Dependencies:** The class `ASTVisitor` does not explicitly list any external dependencies in the provided `context.dependencies` list.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes the ASTVisitor instance with the raw source code, the file path, and the project's root directory. It calculates the module path, sets up an empty schema dictionary to store parsed imports, functions, and classes, and initializes a `_current_class` attribute to `None` for tracking the current class being visited.
    *   *Parameters:*
        *   **self** (`ASTVisitor`): The instance of the ASTVisitor class.
        *   **source_code** (`str`): The raw source code of the file being visited.
        *   **file_path** (`str`): The absolute path to the Python file being analyzed.
        *   **project_root** (`str`): The root directory of the entire project, used for calculating module paths.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method is part of the `ast.NodeVisitor` pattern and is called when an `ast.Import` node is encountered. It iterates through the imported names (aliases) within the node and appends each import's name to the `imports` list within the instance's `schema` dictionary. After processing, it calls `self.generic_visit(node)` to continue traversing the AST.
        *   *Parameters:*
            *   **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            *   **node** (`ast.Import`): The AST node representing an import statement (e.g., `import module`).
        *   *Returns:* None
        *   **Usage:** Implicitly called by the `ast.NodeVisitor` traversal mechanism.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `ast.ImportFrom` nodes, which represent `from ... import ...` statements. It iterates through the aliases in the node, formats the import string as `"{module}.{name}"`, and appends it to the `imports` list in the `schema`. It then calls `self.generic_visit(node)` to ensure further traversal of the AST.
        *   *Parameters:*
            *   **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            *   **node** (`ast.ImportFrom`): The AST node representing a `from ... import ...` statement.
        *   *Returns:* None
        *   **Usage:** Implicitly called by the `ast.NodeVisitor` traversal mechanism.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method processes `ast.ClassDef` nodes, which represent class definitions. It constructs a `class_info` dictionary containing details like the class identifier, name, docstring, source code segment, and line numbers. This `class_info` is then appended to the `classes` list within the `schema`. The method also sets `_current_class` to the newly created `class_info` before recursively visiting child nodes, and then resets it to `None` after the class's children have been visited.
        *   *Parameters:*
            *   **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            *   **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* None
        *   **Usage:** Implicitly called by the `ast.NodeVisitor` traversal mechanism.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles `ast.FunctionDef` nodes, representing function definitions. It differentiates between methods (functions defined within a class) and standalone functions. If `_current_class` is set, it extracts method details and appends them to the `method_context` of the current class. Otherwise, it extracts standalone function details and appends them to the `functions` list in the `schema`. Finally, it calls `self.generic_visit(node)` for further traversal.
        *   *Parameters:*
            *   **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            *   **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* None
        *   **Usage:** Implicitly called by the `ast.NodeVisitor` traversal mechanism.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method is designed to handle `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. Its implementation simply delegates to `self.visit_FunctionDef(node)`, treating asynchronous functions the same way as regular functions for the purpose of schema extraction.
        *   *Parameters:*
            *   **self** (`ASTVisitor`): The instance of the ASTVisitor class.
            *   **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:* None
        *   **Usage:** Implicitly called by the `ast.NodeVisitor` traversal mechanism.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process source code from a repository to generate a structured Abstract Syntax Tree (AST) schema and then enrich this schema with inter-component relationship data. It provides functionalities to parse Python files, extract their AST nodes (functions, classes, imports), and subsequently merge call graph information into this schema, including identifying class dependencies.
*   **Instantiation:** Not explicitly listed.
*   **Dependencies:** The class depends on the 'ast' module for parsing Python code, the 'os' module for path manipulation, and 'getRepo.GitRepository' for handling repository file objects. It also implicitly depends on an 'ASTVisitor' class for detailed AST traversal.
*   **Constructor:**
    *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any specific parameters beyond 'self' and performs no explicit setup or attribute initialization.
    *   *Parameters:* None
*   **Methods:**
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict)`
        *   *Description:* This method integrates call relationship data (outgoing and incoming calls) into a pre-existing full schema of AST nodes. It iterates through files, functions, and classes within the schema, updating their respective 'context' fields with call information. For classes, it also calculates and stores external dependencies based on method calls that are not internal to the class.
        *   *Parameters:*
            *   **self** (`ASTAnalyzer`): Refers to the instance of the ASTAnalyzer class.
            *   **full_schema** (`dict`): A dictionary representing the complete AST schema, including files, functions, and classes, which will be updated with relationship data.
            *   **raw_relationships** (`dict`): A dictionary containing raw outgoing and incoming call relationships, typically structured with "outgoing" and "incoming" keys.
        *   *Returns:* `full_schema` (`dict`): The full_schema dictionary, now enriched with call relationship data and class dependencies.
        *   **Usage:** Not explicitly called by any other functions or methods in the provided context.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository)`
        *   *Description:* This method processes a list of file objects from a Git repository to build a comprehensive AST schema. It filters for Python files, parses their content using the 'ast' module, and then uses an 'ASTVisitor' to extract AST nodes (imports, functions, classes). The extracted schema for each file is then added to a 'full_schema' dictionary, handling potential parsing errors. It also determines the project root for relative path calculations.
        *   *Parameters:*
            *   **self** (`ASTAnalyzer`): Refers to the instance of the ASTAnalyzer class.
            *   **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes, representing files from the repository.
            *   **repo** (`GitRepository`): An object representing the Git repository, though its specific methods are not directly called in this snippet.
        *   *Returns:* `full_schema` (`dict`): A dictionary representing the full AST schema of the repository, organized by file paths, containing parsed AST nodes.
        *   **Usage:** Not explicitly called by any other functions or methods in the provided context.

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file-level import dependencies for a given Python file. It initializes a NetworkX directed graph and then utilizes a `FileDependencyGraph` visitor to traverse the provided Abstract Syntax Tree (AST). The visitor identifies import relationships within the file. Finally, the function populates the NetworkX graph with nodes for each file and adds directed edges to represent the identified import dependencies, indicating which files import others.
*   **Parameters:**
    *   **filename** (`str`): The path to the file for which dependencies are being built.
    *   **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed for dependencies.
    *   **repo_root** (`str`): The root directory of the repository, used for resolving file paths.
*   **Returns:** `graph` (`nx.DiGraph`): A NetworkX directed graph where nodes represent files and edges represent import dependencies.
*   **Usage:** Not called by any other functions.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a comprehensive directed graph representing dependencies across an entire Git repository. It iterates through all Python files within the provided repository, parsing each file's content into an Abstract Syntax Tree (AST). For each file, it builds a local dependency graph using `build_file_dependency_graph` and then aggregates these individual graphs into a single global NetworkX directed graph. The resulting graph shows relationships between entities (e.g., functions, classes) found in the repository's Python files.
*   **Parameters:**
    *   **repository** (`GitRepository`): The Git repository object from which to extract files and analyze dependencies.
*   **Returns:** `global_graph` (`nx.DiGraph`): A NetworkX directed graph representing the aggregated dependencies across all Python files in the repository.
*   **Usage:** Not called by any other functions.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function identifies all Python files (`.py`) within a specified root directory and its subdirectories. It takes a directory path as input, resolves it to an absolute path, and then performs a recursive glob search for all files ending with '.py'. The paths of the found files are then made relative to the initial root directory before being returned. This effectively provides a list of all Python files within a given project structure.
*   **Parameters:**
    *   **directory** (`str`): The path to the root directory from which to start searching for Python files.
*   **Returns:** `all_files` (`list[Path]`): A list of `pathlib.Path` objects, where each Path represents a Python file found within the specified directory, relative to the provided root directory.
*   **Usage:** Not called by any other functions.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is an AST NodeVisitor designed to build a graph of file dependencies within a Python repository. It traverses the Abstract Syntax Tree (AST) of a given file to identify import statements. Its primary function is to accurately resolve both absolute and relative imports, including complex relative paths and symbols exported via `__init__.py` files. The class maintains a dictionary, `import_dependencies`, to store the mapping from the analyzed file to the modules it imports, providing a structured representation of file-level dependencies.
*   **Instantiation:** Not explicitly listed.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes a new instance of the FileDependencyGraph. It sets up the `filename` of the file currently being analyzed and the `repo_root` path, which are essential for resolving module paths and dependencies within the repository structure.
    *   *Parameters:*
        *   **filename** (`str`): The path to the file currently being analyzed for dependencies.
        *   **repo_root** (`str`): The root directory of the repository where the file resides, used for resolving relative paths.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node: ImportFrom)`
        *   *Description:* This method is responsible for resolving relative import statements, such as `from .. import name1, name2`. It calculates the correct module path based on the import level and the current file's location within the repository. It identifies existing module files or symbols exported through `__init__.py` files using internal helper functions `module_file_exists` and `init_exports_symbol`. If the resolution fails to find any matching modules or symbols, it raises an `ImportError` to indicate the failure.
        *   *Parameters:*
            *   **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement to be resolved.
        *   *Returns:* `null` (`list[str]`): A list of resolved module or symbol names that actually exist.
        *   **Usage:** Not explicitly called by any other functions or methods.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None = None)`
        *   *Description:* This method is part of the AST NodeVisitor pattern and is invoked when an `Import` or `ImportFrom` node is encountered. Its purpose is to record the identified import dependencies. It adds the imported module or symbol name to the `import_dependencies` dictionary, associating it with the current `filename`. It handles cases where a specific `base_name` is provided, typically from a resolved `ImportFrom` statement, or extracts the name directly from the import alias. After processing, it ensures the AST traversal continues by calling `self.generic_visit(node)`.
        *   *Parameters:*
            *   **node** (`Import | ImportFrom`): The AST node representing either an `import` or `from ... import` statement.
            *   **base_name** (`str | None`): An optional base name for the module, typically used when the module part of an `ImportFrom` statement has already been resolved.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by any other functions or methods.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
        *   *Description:* This method, also part of the AST NodeVisitor pattern, specifically handles `ImportFrom` nodes. It differentiates between absolute and relative import statements. For absolute imports, it extracts the base module name and delegates to `visit_Import` for recording. For relative imports, it utilizes `_resolve_module_name` to determine the actual module paths, handling potential `ImportError` exceptions during resolution. Each successfully resolved base name is then passed to `visit_Import`. Finally, it ensures the AST traversal continues by calling `self.generic_visit(node)`.
        *   *Parameters:*
            *   **node** (`ImportFrom`): The AST node representing a `from ... import ...` statement.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by any other functions or methods.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** The main_orchestrator function acts as a testing and demonstration loop for the LLMHelper class. It defines several pre-computed analysis inputs for various functions, including 'add_item', 'check_stock', and 'generate_report', along with their expected analysis outputs. It then initializes an LLMHelper instance and simulates the process of generating documentation by passing these inputs to the helper. The function aggregates the results into a final documentation structure and prints it to the console, showcasing the system's capability to process and structure function and class analyses.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:** Not explicitly called by any other functions.

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs), including Google Gemini, OpenAI, and Ollama, to generate structured documentation for Python functions and classes. It handles the loading of system prompts, dynamic configuration of LLM clients based on the model name, and manages batch processing with rate limiting to efficiently generate and validate documentation outputs using Pydantic schemas.
*   **Instantiation:** No explicit instantiation points were provided in the context.
*   **Dependencies:** No explicit dependencies were provided in the context.
*   **Constructor:**
    *   *Description:* The constructor initializes the LLMHelper by setting up the API key, loading system prompts from specified file paths, and configuring the appropriate LLM client (Gemini, OpenAI, or Ollama) based on the provided model name. It also calls a private method to set batch processing settings and prepares structured output clients for function and class analysis.
    *   *Parameters:*
        *   **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
        *   **function_prompt_path** (`str`): The file path to the system prompt used for generating function documentation.
        *   **class_prompt_path** (`str`): The file path to the system prompt used for generating class documentation.
        *   **model_name** (`str`): The name of the LLM model to be used, defaulting to 'gemini-2.0-flash-lite'.
        *   **base_url** (`str`): An optional base URL for custom LLM endpoints, such as Ollama or other self-hosted models.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
        *   *Description:* This private method configures the `batch_size` attribute of the LLMHelper instance based on the provided `model_name`. It assigns specific batch sizes optimized for different Gemini, Llama, and GPT models, or a conservative default for unknown models, to manage API call concurrency and rate limits effectively.
        *   *Parameters:*
            *   **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:* None
        *   **Usage:** No specific callers were identified from the context.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* This method generates and validates documentation for a batch of functions by sending their analysis inputs to the configured LLM. It processes inputs in batches, applies system prompts, handles potential API errors, and incorporates waiting periods to respect rate limits, returning a list of validated function analyses.
        *   *Parameters:*
            *   **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects, each containing the necessary data for a function to be analyzed by the LLM.
        *   *Returns:* `all_validated_functions` (`List[Optional[FunctionAnalysis]]`): A list of `FunctionAnalysis` objects, or `None` for inputs where analysis failed, representing the generated and validated documentation for each function.
        *   **Usage:** No specific calls were identified from the context.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* This method generates and validates documentation for a batch of classes by submitting their analysis inputs to the configured LLM. It manages the process in batches, constructs conversations with system and human messages, handles potential exceptions during API calls, and includes delays to comply with rate limits, ultimately returning a list of validated class analyses.
        *   *Parameters:*
            *   **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects, each containing the necessary data for a class to be analyzed by the LLM.
        *   *Returns:* `all_validated_classes` (`List[Optional[ClassAnalysis]]`): A list of `ClassAnalysis` objects, or `None` for inputs where analysis failed, representing the generated and validated documentation for each class.
        *   **Usage:** No specific calls were identified from the context.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as a central interface for interacting with various Large Language Models (LLMs), abstracting away the specifics of different LLM providers like Google Generative AI, OpenAI, or Ollama. It initializes the chosen LLM client based on configuration, loads a system prompt from a specified file, and provides methods for both single-shot synchronous calls and streaming asynchronous responses. This class is designed to standardize LLM interactions within an application, ensuring consistent behavior regardless of the underlying model.
*   **Instantiation:** No explicit instantiation points were provided in the context.
*   **Dependencies:** This class does not explicitly declare any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The constructor initializes the MainLLM instance by setting up the API key, loading a system prompt from a file, and configuring the appropriate LLM client (Google Generative AI, OpenAI, or Ollama) based on the `model_name` provided. It stores the system prompt, model name, and the LLM client instance as attributes. It ensures the API key is present and handles `FileNotFoundError` for the prompt file.
    *   *Parameters:*
        *   **api_key** (`str`): The API key for accessing the LLM service.
        *   **prompt_file_path** (`str`): The file path to the system prompt text.
        *   **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This parameter dictates which underlying LLM client (e.g., ChatGoogleGenerativeAI, ChatOpenAI, ChatOllama) is initialized and used for interactions.
        *   **base_url** (`str | None`): An optional base URL for custom LLM endpoints, used primarily for Ollama or custom OpenAI-compatible services.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input: str)`
        *   *Description:* This method sends a user input along with the pre-loaded system prompt to the configured LLM and returns the LLM's response content. It constructs a list of `SystemMessage` and `HumanMessage` objects, then invokes the `llm` client to get a response. Error handling is included to catch exceptions during the LLM call and log them, returning `None` in case of failure.
        *   *Parameters:*
            *   **user_input** (`str`): The user's query or message to be sent to the LLM.
        *   *Returns:* `response.content` (`str | None`): The content of the LLM's response as a string, or `None` if an error occurs during the LLM call.
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input: str)`
        *   *Description:* This method provides a streaming interface to the LLM, sending user input and the system prompt, and yielding chunks of the LLM's response content as they become available. It utilizes the `stream` method of the configured LLM client to process the messages. Error handling is implemented to catch exceptions during the streaming process, yielding an error message if an issue arises.
        *   *Parameters:*
            *   **user_input** (`str`): The user's query or message for which a streaming LLM response is desired.
        *   *Returns:* `chunk.content` (`Generator[str, None, None]`): A generator that yields string chunks of the LLM's response content. In case of an error, it yields a descriptive error message string.
        *   **Usage:** Not explicitly called by other functions or methods.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to systematically extract core project details from common project configuration and documentation files. It initializes with a structured dictionary to hold various project aspects like overview, installation, and features, using placeholders for missing information. Through a series of specialized parsing methods for README, pyproject.toml, and requirements.txt files, it populates this structure, prioritizing information from configuration files over documentation. The class provides a robust mechanism to gather a comprehensive snapshot of a project's basic information.
*   **Instantiation:** Not explicitly listed.
*   **Dependencies:** The class depends on the 're' module for regular expression operations, the 'os' module for path manipulation, and 'tomllib' for parsing TOML files. It also uses 'typing' for type hints.
*   **Constructor:**
    *   *Description:* The constructor initializes the extractor with a default string "Information not found" for placeholders. It sets up a nested dictionary `self.info` to store extracted project details, pre-filled with these placeholder values across categories like project overview and installation.
    *   *Parameters:* None
*   **Methods:**
    *   **`_clean_content`**
        *   *Signature:* `def _clean_content(self, content: str)`
        *   *Description:* This method sanitizes a given string by removing null bytes (`\x00`). These null bytes often appear due to incorrect encoding interpretations, such as reading a UTF-16 encoded file as UTF-8. The method first checks if the content is empty, returning an empty string if so, otherwise it performs the replacement.
        *   *Parameters:*
            *   **content** (`str`): The string content to be cleaned.
        *   *Returns:* `""` (`str`): The cleaned string with null bytes removed.
        *   **Usage:** Called by `_parse_readme`, `_parse_toml`, and `_parse_requirements`.
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This utility method searches through a list of file objects to find one whose path matches any of the provided patterns. The search is case-insensitive, comparing the lowercased file path with lowercased patterns. It iterates through each file and then each pattern, returning the first matching file object found. If no match is found after checking all files and patterns, it returns None.
        *   *Parameters:*
            *   **patterns** (`List[str]`): A list of string patterns to match against file paths.
            *   **dateien** (`List[Any]`): A list of file-like objects, each expected to have a 'path' attribute.
        *   *Returns:* `""` (`Optional[Any]`): The first file object that matches a pattern, or None if no match is found.
        *   **Usage:** Called by `extrahiere_info`.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This method extracts text content located under a Markdown level 2 heading (##). It constructs a regular expression pattern to match any of the provided keywords within a '##' heading, then captures all subsequent content until another '##' heading or the end of the document. The search is case-insensitive and handles multi-line content. If a matching section is found, its stripped content is returned; otherwise, None is returned.
        *   *Parameters:*
            *   **inhalt** (`str`): The Markdown content string to parse.
            *   **keywords** (`List[str]`): A list of keywords to match against Markdown section titles.
        *   *Returns:* `""` (`Optional[str]`): The extracted section content as a string, or None if no matching section is found.
        *   **Usage:** Called by `_parse_readme`.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt: str)`
        *   *Description:* This method processes the content of a README file to extract various project details. It first cleans the content using `_clean_content`. It then attempts to find the project title (H1 heading), a general description, key features, tech stack, current status, installation instructions, and a quick start guide by calling `_extrahiere_sektion_aus_markdown` with different keyword lists. Extracted information is stored in the `self.info` dictionary, prioritizing existing `INFO_NICHT_GEFUNDEN` values.
        *   *Parameters:*
            *   **inhalt** (`str`): The content of the README file as a string.
        *   *Returns:* None
        *   **Usage:** Called by `extrahiere_info`.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt: str)`
        *   *Description:* This method parses the content of a pyproject.toml file to extract project information. It first cleans the content. It checks if the `tomllib` module is available, printing a warning and returning if not. It then attempts to load the TOML content, extracting the project 'name', 'description', and 'dependencies' from the '[project]' section. These values update the `self.info` dictionary. Error handling is included for `TOMLDecodeError`.
        *   *Parameters:*
            *   **inhalt** (`str`): The content of the pyproject.toml file as a string.
        *   *Returns:* None
        *   **Usage:** Called by `extrahiere_info`.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt: str)`
        *   *Description:* This method parses the content of a requirements.txt file to extract project dependencies. It first cleans the content. It only proceeds if the 'dependencies' field in `self.info` is still set to `INFO_NICHT_GEFUNDEN`, indicating that dependencies haven't been found from a pyproject.toml file yet. It splits the content into lines, filters out empty lines and comments, and then stores the extracted dependencies as a list in `self.info`.
        *   *Parameters:*
            *   **inhalt** (`str`): The content of the requirements.txt file as a string.
        *   *Returns:* None
        *   **Usage:** Called by `extrahiere_info`.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This is the main orchestration method for extracting project information. It first identifies relevant project files (README, pyproject.toml, requirements.txt) using `_finde_datei`. It then parses these files in a prioritized order: pyproject.toml first, then requirements.txt, and finally README.md. After parsing, it formats the extracted dependencies and, if no project title was found, attempts to derive one from the `repo_url`. Finally, it returns the accumulated project information stored in `self.info`.
        *   *Parameters:*
            *   **dateien** (`List[Any]`): A list of file-like objects, each containing 'path' and 'content' attributes.
            *   **repo_url** (`str`): The URL of the repository, used as a fallback for the project title.
        *   *Returns:* `""` (`Dict[str, Any]`): A dictionary containing all extracted project information.
        *   **Usage:** Not explicitly called by other methods or functions within the provided context.

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** This function takes a NetworkX directed graph and an output file path, then generates a DOT file. It first creates a copy of the input graph. To ensure compatibility with DOT format, it relabels all nodes with simple, unique identifiers like 'n0', 'n1', etc. The original node names are preserved by storing them as 'label' attributes on the newly relabeled nodes. Finally, the modified graph is written to the specified output path as a DOT file.
*   **Parameters:**
    *   **graph** (`nx.DiGraph`): The input NetworkX directed graph to be processed and converted to a DOT file.
    *   **out_path** (`str`): The file path where the generated DOT file will be saved.
*   **Returns:** None
*   **Usage:** Not called by any other functions.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** This function constructs a filtered call graph for a given Git repository. It first identifies all Python files within the repository and parses their Abstract Syntax Trees (ASTs) to extract a set of functions defined by the repository itself. Subsequently, it iterates through these parsed files again to build a directed graph where nodes represent these 'own' functions and edges indicate calls between them, ensuring only calls between functions defined within the repository are included. The resulting graph represents the internal call structure of the repository's code.
*   **Parameters:**
    *   **repo** (`GitRepository`): The Git repository object from which to extract Python files and build the call graph.
*   **Returns:** `global_graph` (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions defined within the repository.
*   **Usage:** Not called by any other functions.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST (Abstract Syntax Tree) visitor designed to construct a call graph for a given Python source file. It extends `ast.NodeVisitor` to traverse the AST, identifying function definitions, class definitions, import statements, and function calls. The class maintains internal state to track the current file, class, and function context, resolving full names for functions and methods, and recording caller-callee relationships in a directed graph.
*   **Instantiation:** No explicit instantiation points were provided in the context.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the context.
*   **Constructor:**
    *   *Description:* The constructor initializes the CallGraph instance with the filename of the source code being analyzed. It sets up various internal attributes to manage the AST traversal state, including the current function and class, local definitions, a NetworkX directed graph to store the call graph, import mappings, a set of all discovered functions, and a dictionary to store edges (caller-callee relationships).
    *   *Parameters:*
        *   **filename** (`str`): The path or name of the source file being analyzed.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* This private helper method recursively traverses an AST node to extract its full name components as a list of strings. It handles `ast.Call` nodes by recurring on the function being called, `ast.Name` nodes by returning their ID, and `ast.Attribute` nodes by recursively getting the value's parts and appending the attribute name. This is crucial for resolving complex call expressions.
        *   *Parameters:*
            *   **node** (`ast.AST`): The AST node to analyze for name components, typically an ast.Call, ast.Name, or ast.Attribute node.
        *   *Returns:* `parts` (`list[str]`): A list of string components representing the dotted name of the call, e.g., ['pkg', 'mod', 'Class', 'method'].
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* This private method takes a list of potential callee name components and resolves them into fully qualified names. It first checks for local definitions (functions or methods defined within the current scope), then consults the import mapping to resolve imported modules or functions. If neither applies, it constructs a full name based on the current filename and class context. This ensures that call targets are accurately identified.
        *   *Parameters:*
            *   **callee_nodes** (`list[list[str]]`): A list where each inner list contains name components (e.g., ['module', 'function']) of a potential callee.
        *   *Returns:* `resolved` (`list[str]`): A list of fully qualified string names for the resolved callees.
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None = None)`
        *   *Description:* This private helper method constructs a fully qualified name for a given base name, optionally including a class name. It prepends the filename and, if provided, the class name, to the base name, using '::' as a separator. This ensures consistent naming conventions for all functions and methods within the call graph.
        *   *Parameters:*
            *   **basename** (`str`): The base name of the function or method.
            *   **class_name** (`str | None`): The name of the class if the entity is a method, otherwise None.
        *   *Returns:* `full_name` (`str`): The fully qualified name of the function or method.
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* This private method determines the identifier of the current calling context. If a function is currently being visited, its full name is returned. Otherwise, it returns a placeholder indicating either the filename (if available) or a generic '<global-scope>' to represent calls made outside any specific function.
        *   *Parameters:* None
        *   *Returns:* `caller_identifier` (`str`): The fully qualified name of the current function or a placeholder for the global scope.
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method is an AST visitor for `ast.Import` nodes. It processes import statements to populate the `import_mapping` dictionary, associating the imported module's alias (or its original name) with its module name. This mapping is later used to resolve fully qualified names for imported functions or classes. After processing, it calls `generic_visit` to continue traversing the AST.
        *   *Parameters:*
            *   **node** (`ast.Import`): The `ast.Import` node representing an import statement.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `from ... import ...` statements (`ast.ImportFrom`). It determines the full module path for each imported name, considering relative imports (`node.level`). The resolved fully qualified name for each imported alias is then stored in the `self.scope` dictionary, allowing the visitor to correctly resolve calls to these imported entities. It then continues the generic AST traversal.
        *   *Parameters:*
            *   **node** (`ast.ImportFrom`): The `ast.ImportFrom` node representing an 'from ... import ...' statement.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is an AST visitor for `ast.ClassDef` nodes. It manages the `current_class` context during AST traversal. Before visiting the class's body, it sets `self.current_class` to the name of the class node. After visiting the class's children, it restores the previous `current_class` value, ensuring correct scope tracking for methods defined within nested classes.
        *   *Parameters:*
            *   **node** (`ast.ClassDef`): The `ast.ClassDef` node representing a class definition.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method is an AST visitor for `ast.FunctionDef` nodes. It processes function definitions by constructing a fully qualified name for the function, adding it to `local_defs` and the call graph as a node. It then sets `self.current_function` to this full name, allowing subsequent call nodes within this function to correctly identify their caller. After visiting the function's body, it adds the function to `function_set` and restores the previous `current_function`.
        *   *Parameters:*
            *   **node** (`ast.FunctionDef`): The `ast.FunctionDef` node representing a function definition.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method is an AST visitor for `ast.AsyncFunctionDef` nodes. It handles asynchronous function definitions by simply delegating the processing to the `visit_FunctionDef` method. This ensures that both synchronous and asynchronous functions are treated similarly for the purpose of call graph construction, capturing their names and adding them to the graph.
        *   *Parameters:*
            *   **node** (`ast.AsyncFunctionDef`): The `ast.AsyncFunctionDef` node representing an asynchronous function definition.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method is an AST visitor for `ast.Call` nodes, which represent function calls. It identifies the current caller using `_current_caller`, extracts the callee's name components using `_recursive_call`, and resolves the callee's full name using `_resolve_all_callee_names`. Finally, it records the caller-callee relationship by adding the resolved callee to the `edges` dictionary under the caller's identifier, effectively building the call graph.
        *   *Parameters:*
            *   **node** (`ast.Call`): The `ast.Call` node representing a function call.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by other functions or methods.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* This method is an AST visitor for `ast.If` nodes. It specifically handles the common `if __name__ == "__main__"` block. When such a block is encountered, it temporarily sets `self.current_function` to '<main_block>' to correctly attribute calls within this entry point. For other `if` statements, it simply continues the generic AST traversal. This ensures that code executed in the main block is properly represented in the call graph.
        *   *Parameters:*
            *   **node** (`ast.If`): The `ast.If` node representing an if statement.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by other functions or methods.

### File: `backend/converter.py`

#### Function: `wrap_cdata`
*   **Signature:** `def wrap_cdata(content)`
*   **Description:** The `wrap_cdata` function is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string by prepending "![CDATA[\\n" and appending "\\n]]>" to the input, ensuring that the content is treated as character data and not parsed as XML markup. This is useful for embedding raw text that might contain characters otherwise interpreted as XML.
*   **Parameters:**
    *   **content**: The string content to be wrapped within CDATA tags.
*   **Returns:** `wrapped_content` (`str`): The input content string, formatted and enclosed within CDATA tags.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `extract_output_content`
*   **Signature:** `def extract_output_content(outputs, image_list)`
*   **Description:** This function processes a list of notebook output objects, extracting relevant content such as text, images, or error messages. It iterates through each output, categorizing it by type. For display data or execution results, it prioritizes extracting PNG images, then JPEG, storing their Base64 data in a provided list and returning an XML placeholder. If no image is found, it extracts plain text. Stream outputs are appended as raw text, and error outputs are formatted into a string. The function returns a consolidated list of these extracted content snippets.
*   **Parameters:**
    *   **outputs** (`list[object]`): A list of output objects, typically from a notebook execution, which can include display data, execution results, stream data, or error information.
    *   **image_list** (`list[dict]`): A mutable list that is modified in place to store dictionaries of extracted image data. Each dictionary contains the 'mime_type' and the Base64 'data' string of an image.
*   **Returns:** `extracted_xml_snippets` (`list[str]`): A list of strings, where each string is either plain text, an XML placeholder for an extracted image, or a formatted error message.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `process_image`
*   **Signature:** `def process_image(mime_type)`
*   **Description:** This function processes an image identified by its MIME type. It checks if the provided `mime_type` exists within an external `data` dictionary. If found, it retrieves a base64 encoded string, removes newline characters, and stores it along with its MIME type in an `image_list`. Upon successful processing, it returns a placeholder string indicating the image's index and MIME type. In case of any exception during processing, it returns an error message string. If the `mime_type` is not present in `data`, the function returns `None`.
*   **Parameters:**
    *   **mime_type** (`str`): The MIME type of the image to be processed, used as a key to retrieve its base64 data from an external 'data' dictionary.
*   **Returns:** `image_placeholder_tag` (`str`): A string representing an image placeholder tag, including the image's assigned index and MIME type, if processing is successful. `error_message` (`str`): An error message string indicating that the image could not be decoded, along with the exception details, if an error occurs during processing. `None` (`NoneType`): Returns None if the specified MIME type is not found in the external 'data' dictionary.
*   **Usage:** Not called by any other functions.

#### Function: `convert_notebook_to_xml`
*   **Signature:** `def convert_notebook_to_xml(file_content)`
*   **Description:** This function converts the content of a Jupyter notebook, provided as a string, into an XML representation. It attempts to parse the input using nbformat.reads and handles NotJSONError by returning an error message. The function iterates through notebook cells, converting markdown cells to <CELL type="markdown"> and code cells to <CELL type="code">. If code cells have outputs, these are processed by extract_output_content and included as <CELL type="output"> tags. It returns the concatenated XML string and a list of any extracted images.
*   **Parameters:**
    *   **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a string in JSON format.
*   **Returns:** `xml_output` (`str`): A string containing the XML representation of the notebook, or an error message if parsing fails. `extracted_images` (`list`): A list of extracted image data or paths from the notebook outputs.
*   **Usage:** Not called by any other functions.

#### Function: `process_repo_notebooks`
*   **Signature:** `def process_repo_notebooks(repo_files)`
*   **Description:** This function processes a list of repository files to identify and convert Jupyter notebooks. It filters the input list for files ending with '.ipynb' and then iterates through each identified notebook. For every notebook, it invokes an external conversion utility, 'convert_notebook_to_xml', to transform its content into XML and extract associated images. The function aggregates these conversion results, storing the XML output and images for each notebook, keyed by its file path. Finally, it returns a dictionary containing all the processed notebook data.
*   **Parameters:**
    *   **repo_files** (`list[object]`): A list of file objects from a repository. Each object is expected to have a 'path' attribute (string) and a 'content' attribute (string or bytes) for notebook processing.
*   **Returns:** `results` (`dict[str, dict[str, str | Any]]`): A dictionary where keys are the paths of the processed notebook files (string). Each value is a dictionary containing 'xml' (string) representing the converted notebook content and 'images' (Any) which are any extracted images.
*   **Usage:** Not explicitly called by any other functions.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository, providing a structured way to access its metadata and content. It implements a lazy loading mechanism for the Git blob object, file content, and size, ensuring that these potentially heavy resources are only loaded when explicitly accessed. The class offers properties to retrieve the Git blob, the decoded file content, and its size, along with utility methods for basic analysis like word counting and converting the file's data into a dictionary format.
*   **Instantiation:** Not explicitly listed.
*   **Dependencies:** This class depends on the `git` library for `git.Tree` and `git.Blob` objects, and the `os` module for path manipulation.
*   **Constructor:**
    *   *Description:* The `__init__` method initializes a RepoFile object by setting its file path and the Git tree object it belongs to. It also initializes internal attributes (`_blob`, `_content`, `_size`) to `None` to facilitate lazy loading of these properties upon first access.
    *   *Parameters:*
        *   **file_path** (`str`): The path to the file within the repository.
        *   **commit_tree** (`git.Tree`): The Tree-object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property provides lazy loading of the Git blob object associated with the file. It first checks if the `_blob` attribute is already loaded; if not, it attempts to retrieve the blob from the `_tree` using the file's path. If the file is not found within the commit tree, a `FileNotFoundError` is raised, otherwise the retrieved blob is stored and returned.
        *   *Parameters:* None
        *   *Returns:* `blob` (`git.Blob`): The Git blob object representing the file.
        *   **Usage:** Accessed as a property by `content` and `size`.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property provides lazy loading and decoding of the file's content. It checks if the `_content` attribute is already loaded; if not, it accesses the `blob` property to get the Git blob, reads its data stream, and decodes it using UTF-8, ignoring any errors. The decoded string content is then stored in `_content` and returned.
        *   *Parameters:* None
        *   *Returns:* `content` (`str`): The decoded string content of the file.
        *   **Usage:** Accessed as a property by `analyze_word_count` and `to_dict`.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property provides lazy loading of the file's size in bytes. It first checks if the `_size` attribute is already loaded; if not, it accesses the `blob` property to get the Git blob and retrieves its `size` attribute. The file size is then stored in `_size` and returned.
        *   *Parameters:* None
        *   *Returns:* `size` (`int`): The size of the file in bytes.
        *   **Usage:** Accessed as a property by `to_dict`.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method serves as an example analysis function, calculating the number of words present in the file's content. It achieves this by accessing the `content` property, splitting the resulting string by whitespace, and then returning the total count of the words found.
        *   *Parameters:* None
        *   *Returns:* `word_count` (`int`): The total number of words found in the file's content.
        *   **Usage:** Not explicitly called by other methods or functions.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This special method provides a developer-friendly string representation of the RepoFile object. It constructs a string that includes the class name and the file's path, which is useful for debugging and logging purposes, allowing for easy identification of the object.
        *   *Parameters:* None
        *   *Returns:* `representation` (`str`): A string representation of the RepoFile object, typically in the format <RepoFile(path='...')>.
        *   **Usage:** Implicitly called by Python's `repr()` function or when the object is printed.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content=False)`
        *   *Description:* This method converts the RepoFile object into a dictionary representation, providing a structured way to export its data. It includes the file's path, its base name (extracted using `os.path.basename`), its size, and a 'type' field set to 'file'. Optionally, if `include_content` is `True`, the file's content is also added to the dictionary.
        *   *Parameters:*
            *   **include_content** (`bool`): A flag indicating whether to include the file's content in the dictionary. Defaults to False.
        *   *Returns:* `file_data` (`dict`): A dictionary containing the file's path, name, size, type, and optionally its content.
        *   **Usage:** Not explicitly called by other methods or functions.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class provides a robust mechanism for interacting with Git repositories programmatically. It handles the cloning of a remote repository into a temporary local directory, ensuring isolation and easy cleanup. The class acts as a context manager, automatically managing the lifecycle of the temporary repository directory. It offers functionalities to retrieve all files within the repository as RepoFile objects and to generate a hierarchical tree structure of these files, which can optionally include file content.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class depends on tempfile for temporary directory management, git.Repo and git.GitCommandError from the GitPython library for Git operations, and logging for informational messages. It also implicitly depends on a RepoFile class, which is not defined in the provided source but is used for file representation.
*   **Constructor:**
    *   *Description:* The constructor initializes a GitRepository instance by cloning the specified repository URL into a temporary directory. It sets up internal attributes such as the repository URL, the path to the temporary directory, and the git.Repo object, capturing the latest commit and its tree. It also includes error handling for cloning failures, ensuring cleanup and raising a RuntimeError.
    *   *Parameters:*
        *   **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* This method retrieves a list of all files present in the cloned Git repository. It utilizes the `git.ls_files()` command to obtain relative paths of all tracked files within the repository. For each identified path, it instantiates a `RepoFile` object, passing the file path and the commit tree, and stores these objects in the `self.files` attribute before returning the complete list of `RepoFile` instances.
        *   *Parameters:*
            *   **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:* `files` (`list[RepoFile]`): A list of RepoFile instances, each representing a file in the repository.
        *   **Usage:** Called by `get_file_tree`.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* This method is intended to clean up resources by deleting the temporary directory that was created for cloning the Git repository. According to its docstring, it should delete the directory and its contents. The current implementation prints a message indicating deletion and then sets the `self.temp_dir` attribute to `None`, effectively marking the directory as no longer managed by this instance.
        *   *Parameters:*
            *   **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:* None
        *   **Usage:** Called by `__exit__` and within the `__init__` method's error handling.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* This special method allows the `GitRepository` class to be used as a context manager. When an instance of `GitRepository` is entered using a `with` statement, this method is automatically called and simply returns the instance itself, making it available as the `as` target in the `with` statement.
        *   *Parameters:*
            *   **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:* `self` (`GitRepository`): The instance of the GitRepository class itself.
        *   **Usage:** Implicitly called by Python when the GitRepository object is used in a with statement.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* This special method is part of the context manager protocol and is automatically invoked when exiting a `with` statement block, regardless of whether an exception occurred. Its primary responsibility is to ensure that resources are properly cleaned up by calling the `self.close()` method, which is intended to delete the temporary repository directory.
        *   *Parameters:*
            *   **self** (`GitRepository`): The instance of the GitRepository class.
            *   **exc_type** (`type | None`): The type of the exception that caused the context to be exited, or None if no exception occurred.
            *   **exc_val** (`Exception | None`): The exception instance that caused the context to be exited, or None.
            *   **exc_tb** (`TracebackType | None`): The traceback object that caused the context to be exited, or None.
        *   *Returns:* None
        *   **Usage:** Implicitly called by Python when exiting a with statement block that uses a GitRepository object.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content=False)`
        *   *Description:* This method constructs a hierarchical dictionary representation of the repository's file structure, similar to a file system tree. It first ensures that all files are loaded by calling `get_all_files()` if `self.files` is empty. It then iterates through each `RepoFile` object, splits its path into components, and dynamically builds a nested dictionary structure where directories are represented by dictionaries with a "children" list, and files are added at their respective locations using `file_obj.to_dict()`.
        *   *Parameters:*
            *   **include_content** (`bool`): A flag indicating whether the content of the files should be included in the dictionary representation. Defaults to False.
        *   *Returns:* `tree` (`dict`): A dictionary representing the hierarchical file tree of the repository.
        *   **Usage:** Not explicitly called by other methods in the provided method_context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** This function generates a bar chart to visually compare the number of JSON tokens and TOON tokens. It displays the calculated savings percentage in the chart's title. The chart includes labels for the axes, a grid for readability, and numerical token values displayed above each bar. The generated plot is then saved to a specified output file path and the plot is closed to free up resources.
*   **Parameters:**
    *   **json_tokens** (`int`): The number of tokens associated with the JSON format.
    *   **toon_tokens** (`int`): The number of tokens associated with the TOON format.
    *   **savings_percent** (`float`): The percentage of token savings, displayed in the chart title.
    *   **output_path** (`str`): The file path where the generated chart image will be saved.
*   **Returns:** None
*   **Usage:** Not explicitly called by any other functions.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the effective processing time, subtracting estimated sleep durations imposed by rate limits, specifically for 'gemini-' models. It first determines the total elapsed time between a start and end point. If the model is not a 'gemini-' type, the total duration is returned directly. For 'gemini-' models, it calculates the number of batches based on total items and batch size, then estimates the total sleep time by multiplying the number of sleep intervals by 61 seconds. The final net time is the total duration minus this estimated sleep time, ensuring the result is not negative.
*   **Parameters:**
    *   **start_time** (`datetime.datetime`): The starting timestamp of the operation.
    *   **end_time** (`datetime.datetime`): The ending timestamp of the operation.
    *   **total_items** (`int`): The total number of items processed.
    *   **batch_size** (`int`): The number of items processed per batch.
    *   **model_name** (`str`): The name of the model used, which determines if rate limit adjustments are applied.
*   **Returns:** `net_time` (`float`): The calculated duration in seconds, adjusted for estimated rate limit sleep times, or the total duration if no adjustment is needed. Returns 0 if total_items is 0 or if the net time is negative.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None)`
*   **Description:** The main_workflow function orchestrates a comprehensive process for analyzing a GitHub repository. It begins by extracting API keys and configuring LLM models based on provided api_keys and model_names. It then extracts a repository URL from the input, clones the repository, and performs various analyses including basic project information extraction, file tree construction, relationship analysis, and Abstract Syntax Tree (AST) schema generation. The AST schema is enriched with relationship data. Subsequently, it prepares and dispatches analysis tasks for individual functions and classes to a HelperLLM. Finally, it consolidates all analysis results, evaluates token savings, and generates a comprehensive final report using a MainLLM, saving the report and associated metrics.
*   **Parameters:**
    *   **input** (`str`): The primary input, expected to contain a GitHub repository URL.
    *   **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
    *   **model_names** (`dict`): A dictionary specifying the names of the helper and main LLM models to be used.
    *   **status_callback** (`callable | None`): An optional callback function used to provide status updates during the workflow execution.
*   **Returns:** `report` (`str`): The final generated report from the Main LLM, detailing the repository analysis. `metrics` (`dict`): A dictionary containing performance metrics such as helper LLM time, main LLM time, total time, model names, and token savings data.
*   **Usage:** Not explicitly called by other functions in the provided context.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The update_status function processes a given message by conditionally invoking a status callback and always logging the message. It checks for the existence of a 'status_callback' in its scope; if present, the message is passed to it. Subsequently, the function logs the provided message at the INFO level using the 'logging' module. This function does not return any explicit value.
*   **Parameters:**
    *   **msg** (`Any`): The message string or object to be processed and logged.
*   **Returns:** None
*   **Usage:** Called by `main_workflow`.

#### Function: `notebook_workflow`
*   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
*   **Description:** The notebook_workflow function orchestrates the analysis of Jupyter notebooks from a given GitHub repository. It extracts the repository URL, clones the repository, and processes its notebooks into a structured format. The function then initializes an appropriate Large Language Model (LLM) based on the provided model type and API keys. It iterates through each processed notebook, generates a specific payload including content and images, and uses the LLM to generate an individual report. Finally, it aggregates these reports, saves the combined result to a markdown file, and returns the final report along with execution metrics.
*   **Parameters:**
    *   **input** (`str`): The input string, expected to contain a GitHub repository URL from which notebooks will be analyzed.
    *   **api_keys** (`dict`): A dictionary containing various API keys required for different LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
    *   **model** (`str`): The name of the Large Language Model (LLM) to be used for the notebook analysis (e.g., 'gpt-4', 'gemini-pro').
    *   **status_callback** (`callable | None`): An optional callback function used to provide real-time status updates during the workflow execution.
*   **Returns:** `report` (`str`): The final concatenated markdown report generated by the LLM, summarizing the analysis of all processed notebooks. `metrics` (`dict`): A dictionary containing execution metrics such as helper_time, main_time, total_time, helper_model, main_model, json_tokens, toon_tokens, and savings_percent.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `gemini_payload`
*   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
*   **Description:** This function constructs a multi-part payload suitable for the Gemini API. It combines initial context information, the notebook's XML structure, and embedded images. The function parses the `xml_content` to identify image placeholders, replacing them with base64 encoded image URLs from the `images` list, while preserving surrounding text segments.
*   **Parameters:**
    *   **basic_info** (`dict`): A dictionary containing fundamental project or contextual information.
    *   **nb_path** (`str`): The file path of the current notebook being processed.
    *   **xml_content** (`str`): The XML representation of the notebook content, which may include special image placeholder tags.
    *   **images** (`list[dict]`): A list of dictionaries, where each dictionary contains image data, specifically the base64 encoded string under the 'data' key.
*   **Returns:** `payload_content` (`list[dict]`): A list of dictionaries, each representing a part of the Gemini API payload. These parts can be of type 'text' or 'image_url', with image URLs being base64 encoded.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The update_status function processes a given message by conditionally invoking a status callback and always logging the message. It checks for the existence of a 'status_callback' in its scope; if present, the message is passed to it. Subsequently, the function logs the provided message at the INFO level using the 'logging' module. This function does not return any explicit value.
*   **Parameters:**
    *   **msg** (`Any`): The message string or object to be processed and logged.
*   **Returns:** None
*   **Usage:** Called by `notebook_workflow`.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into its corresponding Python module path. It first attempts to determine the relative path from a specified project root, falling back to the base filename if a relative path cannot be computed. It then removes the '.py' extension if present and replaces directory separators with dots. Finally, it handles '__init__.py' files by removing the '.__init__' suffix to correctly represent the package itself.
*   **Parameters:**
    *   **filepath** (`str`): The full path to the Python file.
    *   **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:** `module_path` (`str`): The converted Python module path string.
*   **Usage:** Not called by any other functions.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze a Python project's source code to build a comprehensive call graph. It identifies all Python files, collects definitions of functions, methods, and classes, and then resolves the relationships between these defined entities by identifying where they are called. The class provides methods to initiate the analysis and retrieve the raw incoming and outgoing call relationships, offering a structured view of code dependencies.
*   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
*   **Dependencies:** This class depends on 'os' for file system operations, 'ast' for parsing Python code, 'logging' for error reporting, and 'collections.defaultdict' for managing graph data structures. It also implicitly depends on 'path_to_module' and 'CallResolverVisitor' which are not defined in the provided source but are used.
*   **Constructor:**
    *   *Description:* This constructor initializes a new ProjectAnalyzer instance. It sets the absolute path to the project's root directory and initializes several internal data structures: 'definitions' (for storing identified code entities), 'call_graph' (to store call relationships), and 'file_asts' (for caching Abstract Syntax Trees). It also defines a set of common directories to be ignored during the analysis process.
    *   *Parameters:*
        *   **project_root** (`str`): The root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This method orchestrates the entire project analysis workflow. It begins by locating all Python files within the specified project root, excluding ignored directories. It then processes each file in two passes: first to collect all function, method, and class definitions, and then to resolve the call relationships between these definitions. Finally, it clears the cached ASTs to free memory and returns the complete call graph.
        *   *Parameters:* None
        *   *Returns:* `call_graph` (`defaultdict(list)`): A dictionary representing the call graph, where keys are fully qualified callee identifiers and values are lists of caller information.
        *   **Usage:** Not explicitly called by other methods in the provided context.
    *   **`get_raw_relationships`**
        *   *Signature:* `def get_raw_relationships(self)`
        *   *Description:* This method processes the internally stored call graph to generate a structured representation of incoming and outgoing call relationships. It iterates through the populated 'call_graph' to build two separate dictionaries: 'outgoing' which maps callers to the entities they call, and 'incoming' which maps callees to the entities that call them. The results are returned as dictionaries with sorted lists for consistency.
        *   *Parameters:* None
        *   *Returns:* `relationships` (`dict`): A dictionary containing 'outgoing' and 'incoming' keys, each mapping entity identifiers to sorted lists of related entity identifiers.
        *   **Usage:** Not explicitly called by other methods in the provided context.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* This private helper method is responsible for recursively traversing the project directory to identify all Python source files. It utilizes 'os.walk' to navigate the file system, actively pruning directories that are specified in the 'ignore_dirs' set. For each directory, it checks files for the '.py' extension and appends their absolute paths to a list.
        *   *Parameters:* None
        *   *Returns:* `py_files` (`list[str]`): A list of absolute file paths to all Python files found within the project root, excluding ignored directories.
        *   **Usage:** Called by `analyze`.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* This private method parses a given Python file to extract and store definitions of functions, methods, and classes. It reads the file content, parses it into an Abstract Syntax Tree (AST) using 'ast.parse', and caches this AST. It then walks the AST to identify 'FunctionDef' and 'ClassDef' nodes, determines their fully qualified path names, and records their type, file path, and line number in the 'definitions' dictionary. Error handling is included for file operations and AST parsing.
        *   *Parameters:*
            *   **filepath** (`str`): The absolute path to the Python file from which to collect definitions.
        *   *Returns:* None
        *   **Usage:** Called by `analyze`.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This private helper method is designed to find the immediate parent node of a given child node within an Abstract Syntax Tree (AST). It iterates through all nodes in the provided AST 'tree' and for each node, it checks its direct children. If a child matches the 'node' argument, the current iterating node is identified and returned as the parent. If no parent is found after traversing the entire tree, it returns None.
        *   *Parameters:*
            *   **tree** (`ast.AST`): The root of the Abstract Syntax Tree to search within.
            *   **node** (`ast.AST`): The child AST node for which to find the parent.
        *   *Returns:* `parent_node` (`ast.AST | None`): The parent AST node of the given node, or None if no parent is found.
        *   **Usage:** Called by `_collect_definitions`.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* This private method is responsible for identifying and resolving all function, method, and class calls within a specified Python file. It retrieves the previously cached AST for the given 'filepath'. It then instantiates and uses an external 'CallResolverVisitor' to traverse the AST and collect call information. The resolved calls, including callee pathnames and caller details, are then aggregated into the class's 'call_graph'. Error handling is implemented for the call resolution process.
        *   *Parameters:*
            *   **filepath** (`str`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:* None
        *   **Usage:** Called by `analyze`.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST NodeVisitor designed to traverse an abstract syntax tree (AST) of Python code. Its primary function is to identify all function and method calls within the code, resolve their fully qualified names (pathnames), and record detailed information about the caller. It maintains internal state to track the current module, class, and function scope, as well as imported names and instantiated object types, enabling accurate resolution of call targets.
*   **Instantiation:** This class is not explicitly instantiated by any known components according to the provided context.
*   **Dependencies:** This class has no explicit external functional dependencies listed in the context.
*   **Constructor:**
    *   *Description:* The constructor initializes the visitor with the file path of the analyzed code, the project's root directory, and a dictionary of known definitions. It sets up internal state variables such as `filepath`, `module_path` (derived from `filepath` and `project_root`), `definitions`, `scope` for imports, `instance_types` for tracking object types, `current_caller_name`, `current_class_name`, and `calls` (a defaultdict) to store the collected call relationships.
    *   *Parameters:*
        *   **filepath** (`str`): The absolute path to the Python file being analyzed.
        *   **project_root** (`str`): The root directory of the entire project, used to determine module paths.
        *   **definitions** (`dict`): A dictionary containing known fully qualified names of functions, classes, and methods, used to validate resolved call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is invoked when the AST visitor encounters a class definition (`ast.ClassDef`). It updates the visitor's internal state to reflect the current class being processed by setting `self.current_class_name` to the name of the class node. After visiting the class's children nodes to process its contents, it restores the `current_class_name` to its previous value, ensuring correct scope management during AST traversal.
        *   *Parameters:*
            *   **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by any known components based on the provided context.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method is called when the AST visitor encounters a function definition (`ast.FunctionDef`). It updates the `self.current_caller_name` to the fully qualified name of the function, considering whether it's a method within a class or a top-level function. This allows subsequent call resolution to correctly identify the calling context. After processing the function's body, it restores the `current_caller_name` to its previous state.
        *   *Parameters:*
            *   **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by any known components based on the provided context.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* This method is triggered when the AST visitor encounters a function or method call (`ast.Call`). It attempts to resolve the fully qualified name of the called entity using the `_resolve_call_qname` helper. If the callee's pathname is successfully resolved and exists in the provided definitions, it records information about the caller, including its file, line number, full identifier, and type (module, local function, method, or function). This collected data is stored in the `self.calls` dictionary.
        *   *Parameters:*
            *   **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by any known components based on the provided context.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method handles `import` statements (`ast.Import`). It iterates through the imported names and their aliases, storing the mapping from the local name (or alias) to the full module name in the `self.scope` dictionary. This scope information is crucial for later resolving qualified names of calls originating from these imported modules. After processing the import, it continues the generic AST traversal.
        *   *Parameters:*
            *   **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by any known components based on the provided context.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `from ... import ...` statements (`ast.ImportFrom`). It determines the full module path for each imported name, considering relative imports (`node.level`). The resolved fully qualified name for each imported alias is then stored in the `self.scope` dictionary, allowing the visitor to correctly resolve calls to these imported entities. It then continues the generic AST traversal.
        *   *Parameters:*
            *   **node** (`ast.ImportFrom`): The AST node representing an 'from ... import ...' statement.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by any known components based on the provided context.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* This method is invoked when an assignment statement (`ast.Assign`) is encountered. It specifically looks for assignments where the right-hand side is a call to a class constructor (e.g., `x = MyClass()`). If such an instantiation is detected and the class name is resolvable within the current scope and known definitions, it records the qualified class name as the type for the assigned variable in `self.instance_types`. This helps in resolving method calls on these instances later.
        *   *Parameters:*
            *   **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:* None
        *   **Usage:** Not explicitly called by any known components based on the provided context.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* This private helper method attempts to resolve the fully qualified name (QName) of a function or method call. It handles two main cases: direct name calls (`ast.Name`) and attribute calls on an object (`ast.Attribute`). For `ast.Name`, it checks `self.scope` and then local module path. For `ast.Attribute`, it checks `self.instance_types` for object methods or `self.scope` for module-level attributes. If a QName cannot be resolved, it returns `None`.
        *   *Parameters:*
            *   **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., `ast.Name` or `ast.Attribute`).
        *   *Returns:* `qualified_name` (`str | None`): The fully qualified name of the called entity if resolved, otherwise `None`.
        *   **Usage:** Not explicitly called by any known components based on the provided context.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str) -> str`
*   **Description:** This function encrypts a given string using a `cipher_suite` object. It first checks if the input text is empty or if the `cipher_suite` is not initialized; if either condition is true, it returns the original text without encryption. Otherwise, it strips leading/trailing whitespace from the text, encodes it to bytes, encrypts it using the `cipher_suite`, and then decodes the resulting bytes back into a string before returning it.
*   **Parameters:**
    *   **text** (`str`): The string value to be encrypted.
*   **Returns:** `encrypted_text` (`str`): The encrypted string, or the original string if encryption was skipped due to empty input or uninitialized cipher_suite.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str) -> str`
*   **Description:** The decrypt_text function attempts to decrypt a given string using an external 'cipher_suite' object. It first performs a guard clause, returning the original text if the input text is empty or if the 'cipher_suite' is not initialized. If conditions are met, the function strips whitespace from the input, encodes it to bytes, decrypts it using 'cipher_suite.decrypt', and then decodes the result back into a string. In case any exception occurs during the decryption process, the function catches it and returns the original, unencrypted text.
*   **Parameters:**
    *   **text** (`str`): The string value to be decrypted.
*   **Returns:** `decrypted_text` (`str`): The decrypted string if successful, or the original string if decryption fails or is skipped due to initial conditions.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** This function is responsible for inserting a new user record into a database collection. It takes a username, the user's full name, and a plain-text password as input. The provided password is first hashed using `stauth.Hasher.hash` before being stored. The user document also includes placeholder fields for Gemini, Ollama, and GPT API keys, initialized as empty strings. The function then performs an insertion operation and returns the unique identifier of the newly created user document.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user, which will also serve as the document's `_id`.
    *   **name** (`str`): The full name of the user.
    *   **password** (`str`): The plain-text password for the user, which will be hashed before storage.
*   **Returns:** `inserted_id` (`Any`): The unique identifier (`_id`) of the newly inserted user document.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** The `fetch_all_users` function retrieves all user records from the `dbusers` collection. It executes a `find()` operation, which typically returns a cursor or iterable of documents, and then converts the entire result into a Python list. This function provides a complete dump of all user data stored in the specified collection.
*   **Parameters:** None
*   **Returns:** `users` (`list`): A list containing all user records retrieved from the 'dbusers' collection. Each item in the list represents a user document.
*   **Usage:** Not called by any other functions.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The `fetch_user` function is designed to retrieve a single user document from a database collection named `dbusers`. It takes a `username` as input and uses it to query the collection based on the `_id` field. The function returns the first document that matches the provided username.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user to be fetched from the database.
*   **Returns:** `user_document` (`dict | None`): A dictionary representing the user document if found, otherwise None.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the 'name' field for a specific user in the 'dbusers' collection. It identifies the user document by matching the provided 'username' with the '_id' field. The function uses a MongoDB 'update_one' operation to set the new name. It then returns the count of documents that were successfully modified by this operation.
*   **Parameters:**
    *   **username** (`str`): The unique identifier (expected to be the '_id' in the database) of the user whose name is to be updated.
    *   **new_name** (`str`): The new name to be assigned to the specified user.
*   **Returns:** `modified_count` (`int`): The number of documents that were modified by the update operation. This will typically be 0 or 1.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** "This function is responsible for updating a user's Gemini API key within a database. It takes a username and the new Gemini API key as input. The provided API key is first processed by stripping any leading or trailing whitespace, then it is encrypted. Finally, the function performs an update operation on the 'dbusers' collection, setting the 'gemini_api_key' field for the specified user with the newly encrypted key. It returns an integer indicating the number of database documents that were modified."
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose Gemini API key is to be updated.
    *   **gemini_api_key** (`str`): The new Gemini API key to be stored for the user. This key will be stripped of whitespace and encrypted before being saved.
*   **Returns:** `modified_count` (`int`): The number of documents that were modified in the database by the update operation.
*   **Usage:** Not called by any other functions.

#### Function: `update_gpt_key`
*   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
*   **Description:** "This function updates a user's GPT API key in the database. It first encrypts the provided API key, ensuring any leading or trailing whitespace is removed. Then, it performs an update operation on the 'dbusers' collection, setting the 'gpt_api_key' field for the specified username with the encrypted value. The function returns the count of documents that were modified by this operation."
*   **Parameters:**
    *   **username** (`str`): The username of the user whose GPT API key is to be updated.
    *   **gpt_api_key** (`str`): "The new GPT API key to be stored, which will be encrypted before saving."
*   **Returns:** `modified_count` (`int`): The number of documents modified by the update operation.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates a user's Ollama base URL in the database. It takes a username and a new Ollama base URL as input. The function uses the provided username to locate the specific user document and then sets the 'ollama_base_url' field. The new URL is stripped of leading/trailing whitespace before being stored. It returns the count of documents that were modified by the update operation.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose Ollama base URL needs to be updated.
    *   **ollama_base_url** (`str`): "The new base URL for Ollama, which will be stripped of whitespace before being saved."
*   **Returns:** `modified_count` (`int`): The number of documents that were modified by the update operation. A value of 1 indicates successful modification of the user's URL.
*   **Usage:** Not called by any other functions.

#### Function: `update_opensrc_key`
*   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
*   **Description:** This function updates a user's OpenSRC API key in the database. It first encrypts the provided `opensrc_api_key` after stripping any leading or trailing whitespace. The encrypted key is then stored in the `opensrc_api_key` field for the user identified by the `username`. The function returns the count of documents that were modified by this update operation.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose OpenSRC API key needs to be updated.
    *   **opensrc_api_key** (`str`): The new OpenSRC API key to be encrypted and stored for the user.
*   **Returns:** `modified_count` (`int`): The number of documents modified by the update operation.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `update_opensrc_url`
*   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
*   **Description:** "This function updates a user's open-source base URL within a database. It accepts a username and a new base URL string. The function targets a specific user document in the 'dbusers' collection using the provided username as the identifier. It then updates the 'opensrc_base_url' field for that user, ensuring the new URL is stripped of any leading or trailing whitespace. The operation's result, specifically the count of modified documents, is then returned."
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose open-source base URL needs to be updated.
    *   **opensrc_base_url** (`str`): "The new base URL for the user's open-source profile, which will be stripped of whitespace before being stored."
*   **Returns:** `modified_count` (`int`): "The number of documents that were modified by the update operation, typically 0 or 1."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** "This function retrieves the Gemini API key associated with a given username from a database. It queries the `dbusers` collection for a user document matching the provided username. The query specifically projects only the `gemini_api_key` field. If a user document is found, the function extracts and returns the `gemini_api_key`; otherwise, it returns `None`."
*   **Parameters:**
    *   **username** (`str`): The username for which to fetch the Gemini API key.
*   **Returns:** `gemini_api_key` (`str | None`): The Gemini API key if found for the specified username, otherwise None.
*   **Usage:** Not called by any other functions.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** "This function retrieves the Ollama base URL for a specified user from a database. It queries the 'dbusers' collection, using the provided username as the document's '_id'. The function specifically fetches only the 'ollama_base_url' field. It returns the found URL as a string if the user exists, otherwise it returns None."
*   **Parameters:**
    *   **username** (`str`): The username used to identify the user in the database.
*   **Returns:** `ollama_base_url` (`str | None`): The Ollama base URL associated with the user, or None if the user is not found in the database.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `fetch_gpt_key`
*   **Signature:** `def fetch_gpt_key(username: str)`
*   **Description:** "This function, `fetch_gpt_key`, is designed to retrieve a user's GPT API key from a database. It takes a username as input and queries a `dbusers` collection to find a matching user document. If a user is found, it extracts the `gpt_api_key` field from that document. The function returns the API key as a string if found, otherwise it returns `None`."
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched from the database.
*   **Returns:** `gpt_api_key` (`str | None`): The GPT API key associated with the specified username, or `None` if the user is not found or the key is not present.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `fetch_opensrc_key`
*   **Signature:** `def fetch_opensrc_key(username: str)`
*   **Description:** "This function retrieves the 'opensrc_api_key' for a specified username from a database collection named 'dbusers'. It queries the collection to find a document where the '_id' matches the provided username, specifically projecting only the 'opensrc_api_key' field. If a user document is found, the function returns the value of the 'opensrc_api_key'. If no user is found matching the username, it returns None."
*   **Parameters:**
    *   **username** (`str`): "The username, which corresponds to the '_id' field in the 'dbusers' collection, for which to retrieve the opensrc API key."
*   **Returns:** `opensrc_api_key` (`str | None`): "The opensrc API key associated with the given username, or None if the user is not found in the database."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `fetch_opensrc_url`
*   **Signature:** `def fetch_opensrc_url(username: str)`
*   **Description:** "This function is designed to retrieve the 'opensrc_base_url' associated with a specific user from a database. It queries the 'dbusers' collection, using the provided username as the document's unique identifier. The query specifically projects only the 'opensrc_base_url' field, excluding the document's '_id'. If a user document matching the username is found, the function extracts and returns the 'opensrc_base_url' value. If no user is found, the function returns None."
*   **Parameters:**
    *   **username** (`str`): The unique identifier (username) of the user whose opensrc base URL is to be fetched.
*   **Returns:** `opensrc_base_url` (`str | None`): "The opensrc base URL string associated with the user, or None if no user is found with the given username."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** This function is designed to remove a user record from a database collection. It takes a username as input, which it uses as the unique identifier ('_id') to locate and delete the corresponding document. The function then returns the count of documents that were successfully deleted, indicating whether the user was found and removed.
*   **Parameters:**
    *   **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:** `deleted_count` (`int`): "The number of documents deleted by the operation, typically 0 or 1."
*   **Usage:** Not called by any other functions.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** "This function retrieves a user's API keys and URLs from a database based on their username. It queries the 'dbusers' collection, and if a user is found, it decrypts specific API keys (Gemini, GPT, and open-source) while retrieving others directly. If the user is not found, it returns a tuple of None values. The function returns a tuple containing the decrypted API keys and base URLs."
*   **Parameters:**
    *   **username** (`str`): The username of the user whose API keys and URLs are to be retrieved.
*   **Returns:** `gemini_plain` (`str | None`): The decrypted Gemini API key, or an empty string/None if not found or user not found. `ollama_plain` (`str | None`): The Ollama base URL, or an empty string/None if not found or user not found. `gpt_plain` (`str | None`): The decrypted GPT API key, or an empty string/None if not found or user not found. `opensrc_plain` (`str | None`): The decrypted open-source API key, or an empty string/None if not found or user not found. `opensrc_url` (`str | None`): The open-source base URL, or an empty string/None if not found or user not found.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** "This function is responsible for creating a new chat entry within a database. It constructs a dictionary representing the chat, which includes a unique identifier generated using `uuid.uuid4()`, the provided username, the specified chat name, and the current timestamp from `datetime.now()`. This prepared chat document is then inserted into the `dbchats` collection using the `insert_one()` method. The function concludes by returning the unique `_id` assigned to the newly inserted chat document."
*   **Parameters:**
    *   **username** (`str`): The username associated with the new chat entry.
    *   **chat_name** (`str`): The name of the chat to be created.
*   **Returns:** `inserted_id` (`str`): The unique identifier (`_id`) of the newly created chat document in the database.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** "This function, `fetch_chats_by_user`, is designed to retrieve all chat records associated with a specific user. It takes a username as input and queries a database collection, `dbchats`, to find all entries where the 'username' field matches the provided value. The retrieved chat records are then sorted by their 'created_at' timestamp in ascending order. Finally, the function returns these sorted chat records as a list."
*   **Parameters:**
    *   **username** (`str`): The username for which to fetch chat records.
*   **Returns:** `chats` (`list`): "A list of chat records associated with the specified username, sorted by creation date."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** "This function, `check_chat_exists`, is designed to verify the presence of a specific chat within the `dbchats` collection. It takes a username and a chat name as input. The function performs a lookup in the database for a document that matches both the provided username and chat name. It returns a boolean indicating whether such a chat entry exists."
*   **Parameters:**
    *   **username** (`str`): The username associated with the chat to be checked.
    *   **chat_name** (`str`): The name of the chat to be checked for existence.
*   **Returns:** `exists` (`bool`): "Returns `True` if a chat matching the provided username and chat name is found in the database, `False` otherwise."
*   **Usage:** Not called by any other functions.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** "This function renames a chat and all its associated message exchanges (messages) within the database. It first updates the chat entry in the 'dbchats' collection by changing its 'chat_name' from 'old_name' to 'new_name' for a specific 'username'. Subsequently, it updates all related exchange entries in the 'dbexchanges' collection, also changing their 'chat_name' from 'old_name' to 'new_name' for the same 'username'. The function returns the count of chat entries that were modified in the initial update operation."
*   **Parameters:**
    *   **username** (`str`): The username associated with the chat to be renamed.
    *   **old_name** (`str`): The current name of the chat.
    *   **new_name** (`str`): The new desired name for the chat.
*   **Returns:** `modified_count` (`int`): The number of chat entries that were modified in the 'dbchats' collection during the rename operation.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str = '', main_used: str = '', total_time: str = '', helper_time: str = '', main_time: str = '', json_tokens = 0, toon_tokens = 0, savings_percent = 0.0)`
*   **Description:** "This function is responsible for persisting an exchange record into a database. It generates a unique identifier for the new record and constructs a dictionary containing various details such as the question, answer, feedback, user information, and performance metrics. A timestamp is also added to the record. The function then attempts to insert this structured data into the dbexchanges collection."
*   **Parameters:**
    *   **question** (`str`): The user's question in the exchange.
    *   **answer** (`str`): The generated answer for the question.
    *   **feedback** (`str`): The feedback provided for the exchange.
    *   **username** (`str`): The username associated with this exchange.
    *   **chat_name** (`str`): The name of the chat session.
    *   **helper_used** (`str`): An optional field indicating the helper tool utilized.
    *   **main_used** (`str`): An optional field indicating the main tool utilized.
    *   **total_time** (`str`): An optional field representing the total time taken for the exchange.
    *   **helper_time** (`str`): An optional field representing the time taken by the helper tool.
    *   **main_time** (`str`): An optional field representing the time taken by the main tool.
    *   **json_tokens** (`int`): An optional field for the number of JSON tokens used.
    *   **toon_tokens** (`int`): An optional field for the number of 'toon' tokens used.
    *   **savings_percent** (`float`): An optional field for the percentage of savings.
*   **Returns:** `new_id` (`str`): The unique identifier of the newly inserted exchange record upon successful insertion. `None`: Returned if an exception occurs during the database insertion process.
*   **Usage:** Not explicitly called by any other functions.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** "The function `fetch_exchanges_by_user` retrieves exchange records from a database based on a given username. It queries a collection, presumably `dbexchanges`, for documents where the 'username' field matches the input. The retrieved records are then sorted by their 'created_at' timestamp in ascending order. Finally, the function returns these sorted exchange records as a list."
*   **Parameters:**
    *   **username** (`str`): The username for which to fetch exchange records from the database.
*   **Returns:** `exchanges` (`list`): "A list of exchange records associated with the provided username, sorted by their creation timestamp."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a list of chat exchanges from a database collection named `dbexchanges`. It queries for exchanges associated with a specific username and chat name. The results are then sorted by their creation timestamp in ascending order before being converted into a list and returned.
*   **Parameters:**
    *   **username** (`str`): The username used to filter the chat exchanges.
    *   **chat_name** (`str`): The name of the chat to filter the exchanges by.
*   **Returns:** `exchanges` (`list`): "A list of exchange documents matching the provided username and chat name, sorted by 'created_at'."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** "This function updates the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function uses a database client, likely `dbexchanges`, to locate the document matching the provided `exchange_id` and sets its 'feedback' field to the new value. It then returns the count of documents that were successfully modified by this operation."
*   **Parameters:**
    *   **exchange_id** (`Any`): The unique identifier of the exchange record to be updated in the database.
    *   **feedback** (`int`): The integer value representing the feedback to be set for the specified exchange.
*   **Returns:** `modified_count` (`int`): "The number of documents that were modified by the update operation. A value of 1 typically indicates a successful update, while 0 suggests no document was found or changed."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** "This function updates the feedback message for a specific exchange record in a database. It takes an exchange identifier and a new feedback message as input. The function uses a database client, likely `dbexchanges`, to locate the exchange document by its `_id` and then sets the `feedback_message` field. Finally, it returns the count of documents that were successfully modified by this operation."
*   **Parameters:**
    *   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    *   **feedback_message** (`str`): The new feedback message to be stored for the specified exchange.
*   **Returns:** `modified_count` (`int`): The number of documents that were modified by the update operation.
*   **Usage:** Not called by any other functions.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function is designed to remove a specific exchange record from the `dbexchanges` collection. It identifies the record to be deleted using a unique `exchange_id`. The function executes a `delete_one` operation on the collection and subsequently returns the count of documents that were successfully deleted.
*   **Parameters:**
    *   **exchange_id** (`str`): The unique identifier of the exchange record to be deleted from the database.
*   **Returns:** `deleted_count` (`int`): "The number of documents that were deleted by the operation, typically 0 or 1."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** "This function is designed to completely remove a specific chat and all its associated message exchanges from the database. It first deletes all messages (exchanges) linked to the given username and chat name. Subsequently, it deletes the chat entry itself from the chat collection. This two-step deletion process ensures data consistency by removing all related records."
*   **Parameters:**
    *   **username** (`str`): The username associated with the chat to be deleted.
    *   **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:** `deleted_count` (`int`): The number of chat documents successfully deleted from the database.
*   **Usage:** Not explicitly called by any other functions.

### File: `frontend/frontend.py`

#### Function: `clean_names`
*   **Signature:** `def clean_names(model_list)`
*   **Description:** "This function processes a list of model names, where each name may contain path separators. It iterates through the provided list and for each model name, it extracts the last component after splitting by the '/' character. The function then returns a new list containing these simplified, base model names."
*   **Parameters:**
    *   **model_list** (`list[str]`): "A list of strings, where each string represents a model name that might include path separators (e.g., 'path/to/model_name')."
*   **Returns:** `cleaned_model_names` (`list[str]`): "A new list of strings, where each string is the base name of a model, with any preceding path information removed."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `get_filtered_models`
*   **Signature:** `def get_filtered_models(source_list, category_name)`
*   **Description:** "This function, `get_filtered_models`, filters a given list of models based on a specified category name. It first retrieves associated keywords from a global `CATEGORY_KEYWORDS` mapping. If the 'STANDARD' keyword is present for the category, it returns only those models from the source list that are also found in `STANDARD_MODELS`. Otherwise, it iterates through the `source_list` and includes models whose names (case-insensitively) contain any of the retrieved keywords. If no models match the keywords, the original `source_list` is returned."
*   **Parameters:**
    *   **source_list**: The list of models to be filtered.
    *   **category_name** (`str`): The name of the category used to determine filtering keywords.
*   **Returns:** `filtered_models` (`list`): "A list of models filtered according to the specified category's keywords. If no models match the keywords, the original `source_list` is returned."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** "This function, `save_gemini_cb`, acts as a callback to save a new Gemini API key. It retrieves the potential new key from the Streamlit session state. If a new key is present, it updates the user's Gemini key in the database via `db.update_gemini_key`, clears the key from the session state, and then displays a success toast message to the user."
*   **Parameters:** None
*   **Returns:** None
*   **Usage:** Not explicitly called by any other functions.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** "This function, `save_ollama_cb`, is designed to save a user-provided Ollama URL. It retrieves the URL from the Streamlit session state. If a new URL is present, it updates the database with this URL, associating it with the current user's username. Upon successful update, a confirmation toast message is displayed to the user."
*   **Parameters:** None
*   **Returns:** None
*   **Usage:** Not explicitly called by any other functions.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** "This function, `load_data_from_db`, is designed to load chat and exchange data for a specified user from the database into the Streamlit session state. It first verifies if the data for the given username has already been loaded to avoid redundant operations. If not, it initializes the session state's `chats` dictionary and proceeds to fetch defined chats and then individual exchanges from the database. The function organizes these exchanges into their respective chats within the session state, handling cases for legacy data and ensuring feedback values are properly set. Finally, it includes logic to create a default chat if no data exists and sets an active chat for the user."
*   **Parameters:**
    *   **username** (`str`): The username for whom chat and exchange data should be loaded from the database.
*   **Returns:** None
*   **Usage:** Called by no other functions.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** "This function handles changes to feedback for a specific exchange object. It updates the 'feedback' key of the provided 'ex' object with the new 'val'. Subsequently, it calls a database utility to persist this feedback change using the '_id' from the 'ex' object. Finally, it triggers a re-run of the Streamlit application to reflect the updated state."
*   **Parameters:**
    *   **ex** (`dict`): "A dictionary-like object representing an exchange, expected to contain at least '_id' and 'feedback' keys."
    *   **val**: The new feedback value to be assigned.
*   **Returns:** None
*   **Usage:** Not explicitly called by any other functions.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** "This function handles the deletion of a specific exchange. It first removes the exchange from the database using its unique identifier. Subsequently, it checks if the chat associated with the exchange exists in the Streamlit session state and, if found, removes the exchange from that chat's list of exchanges. Finally, it triggers a Streamlit rerun to update the UI."
*   **Parameters:**
    *   **chat_name** (`str`): The name of the chat from which the exchange should be removed in the session state.
    *   **ex** (`dict`): "The exchange object to be deleted, expected to contain an '_id' key for database deletion."
*   **Returns:** None
*   **Usage:** Not explicitly called by any other functions.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** "This function handles the deletion of a specific chat identified by `chat_name` for a given `username`. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the Streamlit session state by removing the chat from `st.session_state.chats`. If other chats exist, the `active_chat` is updated to the first available chat. If no chats remain, a new default chat named \"Chat 1\" is created in both the database and session state, and then set as the active chat. Finally, it triggers a Streamlit rerun to update the UI."
*   **Parameters:**
    *   **username**: The username of the user whose chat is to be deleted.
    *   **chat_name**: The name of the chat to be deleted.
*   **Returns:** None
*   **Usage:** Not called by any other functions.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** "This function aims to extract a repository name from a given input text. It first attempts to find a URL within the text using a regular expression. If a URL is successfully identified, it then parses this URL to isolate its path component. The last segment of the path is considered the potential repository name, with any '.git' suffix being removed. If no URL is found or a repository name cannot be derived, the function returns None."
*   **Parameters:**
    *   **text** (`str`): "The input string from which to extract a repository name, potentially containing a URL."
*   **Returns:** `repo_name` (`str | None`): "The extracted repository name as a string, or None if no valid repository name could be found."
*   **Usage:** Not called by any other functions.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** "This function acts as a text generator, designed to simulate streaming text word by word. It takes a single string as input, splits it into individual words based on spaces, and then yields each word sequentially. After yielding each word, it introduces a small delay using `time.sleep` to mimic a real-time streaming effect."
*   **Parameters:**
    *   **text** (`str`): The input string that needs to be streamed word by word.
*   **Returns:** `word` (`str`): "A single word from the input text, followed by a space, yielded sequentially."
*   **Usage:** Not explicitly called by any other functions.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream=False)`
*   **Description:** "This function processes a given markdown string, identifying and rendering both standard markdown content and embedded Mermaid diagrams. It splits the input text based on ````mermaid` delimiters. Regular text segments are rendered using Streamlit's markdown capabilities, optionally streaming the output. Mermaid diagram code blocks are attempted to be rendered via `st_mermaid`, with a fallback to `st.code` if rendering fails."
*   **Parameters:**
    *   **markdown_text** (`str`): "The input string containing markdown content, potentially with embedded Mermaid diagram blocks."
    *   **should_stream** (`bool`): A flag indicating whether to stream the rendering of non-Mermaid text parts. Defaults to `False`.
*   **Returns:** None
*   **Usage:** Not called by any other functions.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** "This function `render_exchange` is designed to render a single chat exchange, comprising a user's question and an assistant's answer, within a Streamlit application. It displays the user's input and the assistant's response, dynamically adjusting its presentation based on whether the response is an error. The function includes an interactive toolbar with feedback buttons (like/dislike), a popover for adding comments, a download option for the answer, and a delete button for the entire exchange. It also handles the display of the assistant's answer content, potentially including Mermaid diagrams."
*   **Parameters:**
    *   **ex** (`dict`): "A dictionary-like object representing a single chat exchange. It is expected to contain keys such as 'question' (str), 'answer' (str), 'feedback' (int, 0 or 1), 'feedback_message' (str), and '_id' (str), which are used to populate the UI elements and interact with backend logic."
    *   **current_chat_name** (`str`): "A string representing the name or identifier of the current chat session. This parameter is utilized when an exchange needs to be deleted, to correctly identify the chat it belongs to."
*   **Returns:** None
*   **Usage:** Not explicitly called by any other functions.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to encapsulate the metadata for a single function parameter. It provides a structured format to store the parameter's name, its data type, and a descriptive explanation of its role or purpose. This class is primarily used for defining clear and consistent parameter specifications within a larger system, likely for documentation or code generation purposes.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, automatically generates an __init__ method. This constructor initializes an instance of ParameterDescription by validating and assigning the 'name', 'type', and 'description' fields based on the provided arguments.
    *   *Parameters:*
        *   **name** (`str`): The name of the parameter.
        *   **type** (`str`): The type hint or inferred type of the parameter.
        *   **description** (`str`): A brief explanation of the parameter's purpose.
*   **Methods:** None

#### Class: `ReturnDescription`
*   **Summary:** The `ReturnDescription` class is a Pydantic BaseModel designed to encapsulate metadata about the return value of a function. It provides a structured format to define the name, type, and a descriptive explanation of what a function returns. This class acts as a data schema for documenting function outputs.
*   **Instantiation:** The instantiation points for this class are not specified in the provided context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for `ReturnDescription` is automatically generated by Pydantic. It initializes an instance of the class by accepting values for `name`, `type`, and `description`, which are then validated according to their respective type hints.
    *   *Parameters:*
        *   **name** (`str`): The name or identifier of the return value.
        *   **type** (`str`): The Python type of the return value.
        *   **description** (`str`): A detailed explanation of what the return value represents.
*   **Methods:** None

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts with other parts of a system. It provides a structured format to describe what functions or methods an entity calls and by which entities it is called, facilitating a clear understanding of its operational context. This model is used to provide machine-readable context for code analysis.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external functional dependencies beyond its base Pydantic BaseModel.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly defines its constructor to accept 'calls' and 'called_by' as keyword arguments. These arguments are used to initialize the corresponding instance attributes, ensuring the object holds the specified usage context information upon creation.
    *   *Parameters:*
        *   **calls** (`str`): A string describing the functions, methods, or external entities that this particular function or method calls.
        *   **called_by** (`str`): A string describing the functions, methods, or external entities that call this particular function or method.
*   **Methods:** None

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a Python function. It serves as a structured data schema for documenting a function's high-level purpose, its input parameters, its expected return values, and its contextual usage within a software system. This model ensures consistency and validation when representing detailed function metadata.
*   **Instantiation:** The instantiation points for this class are not provided in the context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic model, so its `__init__` method is implicitly generated by Pydantic. It initializes an instance of `FunctionDescription` by accepting values for `overall`, `parameters`, `returns`, and `usage_context` as keyword arguments, performing validation according to their type hints.
    *   *Parameters:*
        *   **overall** (`str`): A high-level summary of the function's purpose and implementation.
        *   **parameters** (`List[ParameterDescription]`): A list of objects describing each parameter of the function.
        *   **returns** (`List[ReturnDescription]`): A list of objects describing the return values of the function.
        *   **usage_context** (`UsageContext`): An object describing where the function is called and what it calls.
*   **Methods:** None

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to represent a comprehensive analysis of a Python function. It serves as a structured schema for capturing the function's unique identifier, a detailed description object, and an optional error message. This class is fundamental for standardizing the output of automated function analysis, ensuring all necessary information is consistently present.
*   **Instantiation:** The specific points of instantiation for this class are not provided in the context.
*   **Dependencies:** This class does not explicitly list external functional dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The FunctionAnalysis class is initialized via Pydantic's BaseModel constructor. This constructor automatically handles the assignment of the 'identifier', 'description', and 'error' fields based on the arguments provided during instantiation. It ensures type validation and default value handling for the optional 'error' field.
    *   *Parameters:*
        *   **identifier** (`str`): A unique string that identifies the function being analyzed.
        *   **description** (`FunctionDescription`): An object containing a detailed analysis of the function, including its purpose, parameters, returns, and usage context.
        *   **error** (`Optional[str]`): An optional string field to store any error messages encountered during the function's analysis. Defaults to None.
*   **Methods:** None

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's `__init__` method. It provides a structured format to store a textual summary of the constructor and a list of its individual parameters. This class serves as a data model for representing constructor signatures and their descriptions within a larger system, likely for automated documentation or code analysis.
*   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class depends on `pydantic.BaseModel` for its core functionality and `typing.List` for type hinting, as indicated by its inheritance and field definitions.
*   **Constructor:**
    *   *Description:* This Pydantic BaseModel automatically generates an `__init__` method. It initializes instances with a string `description` and a list of `ParameterDescription` objects, corresponding to the class's defined fields.
    *   *Parameters:*
        *   **description** (`str`): A string summarizing the constructor's purpose.
        *   **parameters** (`List[ParameterDescription]`): A list of objects, each describing a parameter of the constructor.
*   **Methods:** None

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate and validate contextual information about another class. It specifically stores two string fields: 'dependencies', which describes the external dependencies, and 'instantiated_by', which indicates where the class is created. This model facilitates structured data representation for class usage context within a larger system.
*   **Instantiation:** The provided context does not specify where this class is instantiated.
*   **Dependencies:** This class does not explicitly list any external dependencies in the provided context.
*   **Constructor:**
    *   *Description:* The `__init__` method for ClassContext is implicitly generated by Pydantic's BaseModel. It initializes instances by accepting `dependencies` and `instantiated_by` as keyword arguments, validating their types as strings, and assigning them as instance attributes.
    *   *Parameters:*
        *   **dependencies** (`str`): A string summarizing the external dependencies of the class being described.
        *   **instantiated_by** (`str`): A string summarizing the locations or components where the class being described is instantiated.
*   **Methods:** None

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of another Python class. It serves as a structured data container, holding information about a class's overall purpose, its constructor, a list of its individual methods' analyses, and its contextual usage within a larger system. This model is crucial for representing detailed class metadata in a machine-readable format.
*   **Instantiation:** The instantiation points for this class are not specified.
*   **Dependencies:** This class does not explicitly list any external dependencies.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, the `__init__` method for ClassDescription is implicitly generated by Pydantic. It handles the initialization of instance attributes based on the provided data, ensuring type validation and assignment for 'overall', 'init_method', 'methods', and 'usage_context'.
    *   *Parameters:*
        *   **overall** (`str`): A high-level summary describing the class's main purpose and functionality.
        *   **init_method** (`ConstructorDescription`): An object containing a detailed analysis of the class's constructor (__init__ method).
        *   **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each providing a detailed analysis of a method within the class.
        *   **usage_context** (`ClassContext`): An object providing contextual information about the class, including its dependencies and where it is instantiated.
*   **Methods:** None

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class is a Pydantic model that serves as the top-level data structure for a comprehensive analysis of a Python class. It encapsulates the class's identifier, a detailed description object, and an optional error message. This model is designed to provide a structured and machine-readable representation of a class's properties, methods, and usage context, facilitating automated documentation and analysis within a larger system.
*   **Instantiation:** The specific points where this class is instantiated are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, is initialized by accepting keyword arguments corresponding to its defined fields. It sets up the `identifier`, `description`, and an optional `error` attribute, performing validation based on their type hints. The constructor ensures that the provided data conforms to the expected schema for a class analysis report.
    *   *Parameters:*
        *   **identifier** (`str`): The unique name or identifier of the class being analyzed.
        *   **description** (`ClassDescription`): A detailed analysis object containing the class's overall purpose, constructor, and methods.
        *   **error** (`Optional[str]`): An optional string field to report any errors encountered during the class analysis, defaulting to None.
*   **Methods:** None

#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic BaseModel designed to standardize the representation of a specific call event within a codebase. It encapsulates crucial information such as the file path, the name of the calling function or method, the mode of the call (e.g., 'method', 'function'), and the exact line number where the call occurs. This structure is intended for use in tracking and analyzing code relationships, particularly for 'called_by' and 'instantiated_by' lists, providing a consistent data format for such events.
*   **Instantiation:** The input context does not specify where this class is instantiated.
*   **Dependencies:** This class depends on `pydantic.BaseModel` for its data validation and serialization capabilities.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, implicitly generates an __init__ method. This constructor is responsible for validating and assigning the 'file', 'function', 'mode', and 'line' attributes based on the provided arguments during instantiation, ensuring data integrity according to the defined types.
    *   *Parameters:*
        *   **file** (`str`): The path to the file where the call event occurred.
        *   **function** (`str`): The name of the function or method involved in the call event.
        *   **mode** (`str`): The type of call, e.g., 'method', 'function', 'module'.
        *   **line** (`int`): The line number in the file where the call event occurred.
*   **Methods:** None

#### Class: `FunctionContextInput`
*   **Summary:** The `FunctionContextInput` class is a Pydantic BaseModel designed to provide a structured schema for representing the contextual information of a function during analysis. It encapsulates details about other functions, methods, or classes that the analyzed function interacts with, as well as where the analyzed function itself is invoked. This class serves as a data container for understanding a function's role and relationships within a larger codebase.
*   **Instantiation:** The instantiation points for this class are not provided in the current context.
*   **Dependencies:** "This class does not explicitly list any external functional dependencies in the provided context, but it relies on `pydantic.BaseModel` for its core functionality and `typing.List` for type hinting."
*   **Constructor:**
    *   *Description:* As a Pydantic BaseModel, `FunctionContextInput` has an implicitly generated constructor. This constructor handles the validation and assignment of the `calls` and `called_by` attributes based on the provided input arguments during instantiation.
    *   *Parameters:*
        *   **calls** (`List[str]`): "A list of identifiers (strings) representing other functions, methods, or classes that the function being analyzed calls or interacts with."
        *   **called_by** (`List[CallInfo]`): "A list of `CallInfo` objects, each detailing a specific location or context from which the function being analyzed is invoked."
*   **Methods:** None

#### Class: `FunctionAnalysisInput`
*   **Summary:** This class serves as a Pydantic model, defining the structured input required for performing a function analysis. It encapsulates all necessary data, such as the function's identifier, its source code, relevant import statements, and additional contextual information, ensuring a standardized format for analysis requests. This model is crucial for validating and organizing the data before any analysis is performed.
*   **Instantiation:** The instantiation points for this class are not provided in the provided context.
*   **Dependencies:** This class does not explicitly declare any external functional dependencies within the provided context.
*   **Constructor:**
    *   *Description:* This class is a Pydantic BaseModel, and its constructor (`__init__`) is implicitly generated by Pydantic. It initializes instances by validating and assigning values to its defined fields: `mode`, `identifier`, `source_code`, `imports`, and `context` based on the provided arguments.
    *   *Parameters:* None
*   **Methods:** None

#### Class: `MethodContextInput`
*   **Summary:** The `MethodContextInput` class is a Pydantic BaseModel designed to provide a structured representation of the context surrounding a class's methods. It encapsulates essential information such as the method's unique identifier, a list of other functions or methods it calls, a list of entities that call it, its arguments, and its docstring. This model is crucial for organizing and transmitting method-specific contextual data within a larger system.
*   **Instantiation:** This class is not explicitly shown to be instantiated by any other components within the provided context.
*   **Dependencies:** "This class does not explicitly list any external functional dependencies beyond its base class, `pydantic.BaseModel`."
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, has an implicitly generated constructor. It initializes an instance of `MethodContextInput` by accepting values for its defined fields: `identifier`, `calls`, `called_by`, `args`, and `docstring`. These parameters are used to set the initial state of the object, providing a comprehensive context for a method.
    *   *Parameters:*
        *   **identifier** (`str`): A unique string identifier for the method.
        *   **calls** (`List[str]`): "A list of strings, where each string represents another method, class, or function that this method calls."
        *   **called_by** (`List[CallInfo]`): "A list of CallInfo objects, each detailing where this method is called from."
        *   **args** (`List[str]`): "A list of strings, representing the arguments accepted by the method."
        *   **docstring** (`Optional[str]`): "An optional string containing the method's docstring, if available."
*   **Methods:** None

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to encapsulate structured contextual information necessary for analyzing a Python class. It serves as a data container, holding lists of external dependencies, points of instantiation, and detailed context for each method within the target class. This model facilitates the organized transfer and processing of comprehensive class analysis data.
*   **Instantiation:** The instantiation points for this class are not provided.
*   **Dependencies:** This class relies on `List` from `typing` and `BaseModel` from `pydantic` for its structure and validation. It also implicitly depends on `CallInfo` and `MethodContextInput` for the types of its fields.
*   **Constructor:**
    *   *Description:* This class, being a Pydantic BaseModel, does not define an explicit __init__ method. Initialization is handled automatically by Pydantic, which validates and assigns values to its fields based on the arguments provided during instantiation. It sets up the initial state by populating the 'dependencies', 'instantiated_by', and 'method_context' attributes.
    *   *Parameters:*
        *   **dependencies** (`List[str]`): A list of strings representing external dependencies relevant to the class being analyzed.
        *   **instantiated_by** (`List[CallInfo]`): "A list of CallInfo objects, each describing a location or context where the class being analyzed is instantiated."
        *   **method_context** (`List[MethodContextInput]`): "A list of MethodContextInput objects, each providing specific context for a method within the class being analyzed."
*   **Methods:** None

#### Class: `ClassAnalysisInput`
*   **Summary:** This class defines the structured input required to perform a class analysis. It is a Pydantic BaseModel, ensuring data validation for the analysis process. The model specifies fields such as the analysis mode, the class identifier, its source code, import statements, and additional context necessary for a comprehensive analysis.
*   **Instantiation:** The specific instantiation points for this class are not provided in the current context.
*   **Dependencies:** This class does not explicitly list any external dependencies within the provided context.
*   **Constructor:**
    *   *Description:* The ClassAnalysisInput class does not define an explicit __init__ method. As a Pydantic BaseModel, its initialization is automatically handled by Pydantic, which validates and assigns values to its fields based on the provided arguments during instantiation.
    *   *Parameters:* None
*   **Methods:** None

---
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
        root --> SystemPrompts:::dir
        root --> backend:::dir
        root --> database:::dir
        root --> frontend:::dir
        root --> notizen:::dir
        root --> result:::dir
        root --> schemas:::dir
        root --> statistics:::dir
        root --> .env.example:::file
        root --> .gitignore:::file
        root --> analysis_output.json:::file
        root --> output.json:::file
        root --> output.toon:::file
        root --> readme.md:::file
        root --> requirements.txt:::file
        root --> test.json:::file

        SystemPrompts --> SystemPrompts/SystemPromptClassHelperLLM.txt:::file
        SystemPrompts --> SystemPrompts/SystemPromptFunctionHelperLLM.txt:::file
        SystemPrompts --> SystemPrompts/SystemPromptHelperLLM.txt:::file
        SystemPrompts --> SystemPrompts/SystemPromptMainLLM.txt:::file
        SystemPrompts --> SystemPrompts/SystemPromptMainLLMToon.txt:::file
        SystemPrompts --> SystemPrompts/SystemPromptNotebookLLM.txt:::file

        backend --> backend/AST_Schema.py:::file
        backend --> backend/File_Dependency.py:::file
        backend --> backend/HelperLLM.py:::file
        backend --> backend/MainLLM.py:::file
        backend --> backend/__init__.py:::file
        backend --> backend/basic_info.py:::file
        backend --> backend/callgraph.py:::file
        backend --> backend/converter.py:::file
        backend --> backend/getRepo.py:::file
        backend --> backend/main.py:::file
        backend --> backend/relationship_analyzer.py:::file
        backend --> backend/scads_key_test.py:::file

        database --> database/db.py:::file

        frontend --> frontend/.streamlit:::dir
        frontend --> frontend/__init__.py:::file
        frontend --> frontend/frontend.py:::file
        frontend --> frontend/gifs:::dir

        frontend/.streamlit --> frontend/.streamlit/config.toml:::file

        frontend/gifs --> frontend/gifs/4j.gif:::file

        notizen --> notizen/Report Agenda.txt:::file
        notizen --> notizen/Zwischenpraesentation Agenda.txt:::file
        notizen --> notizen/doc_bestandteile.md:::file
        notizen --> notizen/grafiken:::dir
        notizen --> notizen/notizen.md:::file
        notizen --> notizen/paul_notizen.md:::file
        notizen --> notizen/praesentation_notizen.md:::file
        notizen --> notizen/technische_notizen.md:::file

        notizen/grafiken --> notizen/grafiken/1:::dir
        notizen/grafiken --> notizen/grafiken/2:::dir
        notizen/grafiken --> notizen/grafiken/Flask-Repo:::dir
        notizen/grafiken --> notizen/grafiken/Repo-onboarding:::dir

        notizen/grafiken/1 --> notizen/grafiken/1/File_Dependency_Graph_Repo.dot:::file
        notizen/grafiken/1 --> notizen/grafiken/1/global_callgraph.png:::file
        notizen/grafiken/1 --> notizen/grafiken/1/global_graph.png:::file
        notizen/grafiken/1 --> notizen/grafiken/1/global_graph_2.png:::file
        notizen/grafiken/1 --> notizen/grafiken/1/repo.dot:::file

        notizen/grafiken/2 --> notizen/grafiken/2/FDG_repo.dot:::file
        notizen/grafiken/2 --> notizen/grafiken/2/fdg_graph.png:::file
        notizen/grafiken/2 --> notizen/grafiken/2/fdg_graph_2.png:::file
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_flask.png:::file
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_repo-agent.png:::file
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_repo-agent_3.png:::file
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_flask.dot:::file
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_repo-agent-3.dot:::file
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_repo-agent.dot:::file
        notizen/grafiken/2 --> notizen/grafiken/2/global_callgraph.png:::file
        notizen/grafiken/2 --> notizen/grafiken/2/graph_flask.md:::file
        notizen/grafiken/2 --> notizen/grafiken/2/repo.dot:::file

        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/__init__.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/__main__.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/app.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/auth.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/blog.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/blueprints.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/cli.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/conf.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/config.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/conftest.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/ctx.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/db.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/debughelpers.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/factory.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/flask.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/globals.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/hello.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/helpers.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/importerrorapp.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/logging.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/make_celery.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/multiapp.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/provider.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/scaffold.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/sessions.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/signals.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/tag.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/tasks.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/templating.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_appctx.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_async.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_auth.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_basic.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_blog.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_blueprints.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_cli.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_config.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_config.png:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_converters.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_db.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_factory.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_helpers.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_instance_config.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_js_example.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_json.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_json_tag.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_logging.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_regression.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_reqctx.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_request.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_session_interface.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_signals.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_subclassing.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_templating.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_testing.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_user_error_handler.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_views.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/testing.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_app_decorators.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_error_handler.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_route.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/views.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/wrappers.dot:::file
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/wsgi.dot:::file

        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/AST.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/Frontend.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/HelperLLM.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/HelperLLM.png:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/MainLLM.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/agent.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/basic_info.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/callgraph.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/getRepo.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST.png:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST2.png:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST3.png:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/main.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/tools.dot:::file
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/types.dot:::file

        result --> result/ast_schema_01_12_2025_11-49-24.json:::file
        result --> result/notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md:::file
        result --> result/notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md:::file
        result --> result/notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md:::file
        result --> result/notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md:::file
        result --> result/notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md:::file
        result --> result/notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md:::file
        result --> result/report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md:::file
        result --> result/report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md:::file
        result --> result/report_14_11_2025_14-52-36.md:::file
        result --> result/report_14_11_2025_15-21-53.md:::file
        result --> result/report_14_11_2025_15-26-24.md:::file
        result --> result/report_21_11_2025_15-43-30.md:::file
        result --> result/report_21_11_2025_16-06-12.md:::file
        result --> result/report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md:::file
        result --> result/report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md:::file
        result --> result/result_2025-11-11_12-30-53.md:::file
        result --> result/result_2025-11-11_12-43-51.md:::file
        result --> result/result_2025-11-11_12-45-37.md:::file

        statistics --> statistics/savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png:::file
        statistics --> statistics/savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png:::file
        statistics --> statistics/savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png:::file
        statistics --> statistics/savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png:::file
        statistics --> statistics/savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png:::file

    class Subdirectory {
      type:::dir
    }
    class File {
      type:::file
    }
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
    
    Repo contains requirements.txt: "pip install -r requirements.txt"
    ### Setup Guide
    Information not found
    ### Quick Startup
    Information not found

    ## 3. Use Cases & Commands
    This project appears to be a sophisticated tool for onboarding and analyzing code repositories. Its core functionality involves:

    *   **Repository Analysis:** Cloning specified GitHub repositories, parsing their file structures, and analyzing their Abstract Syntax Trees (ASTs).
    *   **Code Relationship Mapping:** Building detailed call graphs and dependency maps to understand how different functions, methods, and classes interact within a project.
    *   **LLM-Powered Documentation Generation:** Leveraging Large Language Models (LLMs) to generate documentation for functions and classes, including descriptions, parameters, return values, and usage contexts.
    *   **Notebook Analysis:** Processing Jupyter notebooks, converting them to XML, and extracting embedded image data for LLM analysis.
    *   **Format Comparison:** Evaluating token usage and savings between JSON and TOON formats.
    *   **Database Integration:** Storing user information, API keys, and chat history for personalized LLM interactions.
    *   **Web Interface:** Providing a Streamlit-based frontend for users to interact with the system, manage API keys, and view analysis results.

    **Primary Commands/Workflows:**

    The `main.py` script orchestrates the core functionalities. The primary workflow involves:
    1.  Providing a GitHub repository URL as input.
    2.  Cloning the repository.
    3.  Extracting basic project information.
    4.  Analyzing code relationships and ASTs.
    5.  Using LLMs (HelperLLM and MainLLM) to generate documentation and a final report.
    6.  Processing Jupyter notebooks within the repository separately.

    The `frontend/frontend.py` script likely serves as the user interface, allowing users to input repository URLs, manage LLM API keys, and view the generated reports and analysis.

    ## 4. Architecture
    The Mermaid Syntax to visualize Graphs is not set up yet and will be added
    but if there is mermaid syntax in your input json display it here



    ## 5. Code Analysis
    ### File: `backend/AST_Schema.py`

    #### Class: `ASTVisitor`
    *   **Summary:** The ASTVisitor class extends `ast.NodeVisitor` and is designed to traverse an Abstract Syntax Tree (AST) of Python code. Its primary purpose is to extract structured information about imports, functions, and classes found within the provided source code. It maintains a `schema` dictionary to accumulate this parsed data, distinguishing between module-level functions and methods nested within classes.
    *   **Instantiation:** Information not available.
    *   **Dependencies:** The class `ASTVisitor` depends on the `ast` module for AST traversal and node manipulation, and implicitly on the `path_to_module` function which is used in its constructor.
    *   **Constructor:**
        *   *Description:* The constructor initializes the ASTVisitor with the raw source code, the file path of the code, and the project's root directory. It calculates the module's full path, sets up an empty dictionary `schema` to store discovered imports, functions, and classes, and initializes `_current_class` to `None` to track the context of methods.
        *   *Parameters:*
            - **self** (`ASTVisitor`): The instance of the ASTVisitor.
            - **source_code** (`str`): The raw source code of the Python file to be analyzed.
            - **file_path** (`str`): The absolute path to the Python file being visited.
            - **project_root** (`str`): The root directory of the entire project, used for calculating module paths.
    *   **Methods:**
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method processes `ast.Import` nodes, which represent simple import statements (e.g., `import module`). It iterates through each alias in the import statement and appends the full name of the imported module to the `imports` list within the `self.schema` dictionary. After processing the current node, it calls `self.generic_visit(node)` to ensure continued traversal of the AST.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor.
                - **node** (`ast.Import`): The AST node representing an 'import' statement.
            *   *Returns:* None
            *   **Usage:** This method calls `self.generic_visit` to continue AST traversal.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method handles `ast.ImportFrom` nodes, which represent 'from ... import ...' statements. It iterates through each alias (name) imported from the specified module and constructs a fully qualified import string (e.g., 'module.name'). This formatted string is then appended to the `imports` list in `self.schema`. Finally, it calls `self.generic_visit(node)` to ensure all child nodes are also visited.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor.
                - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
            *   *Returns:* None
            *   **Usage:** This method calls `self.generic_visit` to continue AST traversal.
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* This method processes `ast.ClassDef` nodes, which define classes within the source code. It constructs a dictionary containing comprehensive information about the class, including its fully qualified identifier, name, docstring, the exact source code segment, and its start and end line numbers. This class information is then appended to the `classes` list in `self.schema`. It temporarily sets `_current_class` to the newly created class info to correctly associate nested methods, then traverses child nodes, and finally resets `_current_class` to `None` after the class's children have been visited.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor.
                - **node** (`ast.ClassDef`): The AST node representing a class definition.
            *   *Returns:* None
            *   **Usage:** This method calls `ast.get_docstring` and `ast.get_source_segment` to extract class details, and `self.generic_visit` for AST traversal.
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method handles `ast.FunctionDef` nodes, which represent both standalone functions and methods within classes. It first checks if a class is currently being visited (indicated by `_current_class` being set). If so, it creates method-specific context information, including its identifier, name, arguments, docstring, and line numbers, and appends this to the `method_context` of the current class. Otherwise, for module-level functions, it creates similar function-specific information and appends it to the `functions` list in `self.schema`. After processing, it calls `self.generic_visit(node)` to continue the AST traversal for any nested elements.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor.
                - **node** (`ast.FunctionDef`): The AST node representing a function or method definition.
            *   *Returns:* None
            *   **Usage:** This method calls `ast.get_docstring` and `ast.get_source_segment` to extract function/method details, and `self.generic_visit` for AST traversal.
        *   **`visit_AsyncFunctionDef`**
            *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
            *   *Description:* This method processes `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions. It delegates its processing directly to the `visit_FunctionDef` method, effectively treating asynchronous functions similarly to regular functions for the purpose of schema generation and information extraction. This ensures consistent handling of both synchronous and asynchronous function definitions.
            *   *Parameters:*
                - **self** (`ASTVisitor`): The instance of the ASTVisitor.
                - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
            *   *Returns:* None
            *   **Usage:** This method calls `self.visit_FunctionDef` to handle the actual processing.
    #### Class: `ASTAnalyzer`
    *   **Summary:** The ASTAnalyzer class is designed to process source code files, specifically Python files, to construct a detailed Abstract Syntax Tree (AST) schema of a repository. It leverages an ASTVisitor to extract structural information like functions, classes, and imports. Furthermore, it can integrate raw call relationship data into this schema, enriching the AST nodes with information about incoming and outgoing calls and class dependencies.
    *   **Instantiation:** The instantiation points for this class are not provided in the current context.
    *   **Dependencies:** The class depends on the `ast` module for parsing Python code, the `os` module for path manipulation, and `getRepo.GitRepository` for repository interaction.
    *   **Constructor:**
        *   *Description:* This constructor initializes the ASTAnalyzer class. It does not take any parameters beyond 'self' and does not set up any instance attributes, effectively creating a stateless analyzer instance.
        *   *Parameters:* None
    *   **Methods:**
        *   **`merge_relationship_data`**
            *   *Signature:* `def merge_relationship_data(self, full_schema: dict, raw_relationships: dict) -> dict`
            *   *Description:* This method integrates raw call relationship data (incoming and outgoing calls) into a structured AST schema. It iterates through files, functions, and classes within the 'full_schema', populating their respective 'context' fields with call information. For classes, it also calculates and stores external dependencies based on method calls, ensuring that the schema is enriched with comprehensive relationship data.
            *   *Parameters:*
                - **full_schema** (`dict`): The complete AST schema containing file, function, and class definitions to be updated.
                - **raw_relationships** (`dict`): A dictionary containing 'outgoing' and 'incoming' call relationships to be merged.
            *   *Returns:* `full_schema` (`dict`): The updated 'full_schema' dictionary with integrated relationship data.
            *   **Usage:** This method calls dictionary methods like 'get', string methods like 'startswith', set methods like 'add', and the built-in 'sorted' function.
        *   **`analyze_repository`**
            *   *Signature:* `def analyze_repository(self, files: list, repo: GitRepository) -> dict`
            *   *Description:* This method processes a list of files from a Git repository to build a comprehensive AST schema. It filters for Python files, parses their content using the 'ast' module, and then uses an 'ASTVisitor' to extract structured AST nodes. The extracted data for each file is then added to a 'full_schema' dictionary, handling potential parsing errors during the process.
            *   *Parameters:*
                - **files** (`list`): A list of file objects, each expected to have 'path' and 'content' attributes.
                - **repo** (`GitRepository`): An object representing the Git repository, though its direct use is not shown in the provided snippet beyond being a parameter.
            *   *Returns:* `full_schema` (`dict`): A dictionary representing the full AST schema of the analyzed repository, organized by file path.
            *   **Usage:** This method calls 'os.path.commonpath', 'os.path.isfile', 'os.path.dirname', string methods like 'endswith' and 'strip', 'ast.parse', instantiates 'ASTVisitor', calls 'visitor.visit', and the built-in 'print' function.

    ### File: `backend/File_Dependency.py`

    #### Class: `FileDependencyGraph`
    *   **Summary:** The FileDependencyGraph class is an AST NodeVisitor designed to analyze Python source code files and build a graph of their import dependencies. It initializes with a specific filename and the repository root to correctly resolve module paths. The class overrides visit_Import and visit_ImportFrom methods to capture import statements and store them in an import_dependencies dictionary. It includes sophisticated logic to resolve complex relative imports, ensuring accurate dependency mapping within a given repository structure.
    *   **Instantiation:** This class is not explicitly instantiated by any other components according to the provided context.
    *   **Dependencies:** This class does not have any explicit external dependencies according to the provided context.
    *   **Constructor:**
        *   *Description:* This constructor initializes the FileDependencyGraph instance by storing the filename of the file being analyzed and the repo_root directory. These attributes are crucial for resolving relative imports and locating files within the repository.
        *   *Parameters:*
            - **filename** (`str`): The name of the file currently being analyzed for dependencies.
            - **repo_root** (`Any`): The root directory of the repository where the file resides.
    *   **Methods:**
        *   **`_resolve_module_name`**
            *   *Signature:* `def _resolve_module_name(self, node: ImportFrom) -> list[str]`
            *   *Description:* This method resolves relative import statements like `from .. import name`. It determines the actual module or symbol names that are being imported by navigating the file system based on the import level and the current file's path. It checks for the existence of module files (.py) or package __init__.py files, and also verifies if symbols are explicitly exported via __all__ or defined within __init__.py. If no valid module or symbol can be resolved, it raises an ImportError.
            *   *Parameters:*
                - **node** (`ImportFrom`): The AST `ImportFrom` node representing the relative import statement.
            *   *Returns:* `resolved` (`list[str]`): A list of resolved module or symbol names that actually exist.
            *   **Usage:** This method does not explicitly call other methods or functions according to the provided context.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None = None)`
            *   *Description:* This method is part of the AST NodeVisitor pattern, specifically handling Import and ImportFrom nodes. It iterates through the imported aliases and records them as dependencies for the current self.filename in the import_dependencies dictionary. If a base_name is provided (typically for from ... import ... statements), it uses that; otherwise, it uses the alias name directly. Finally, it calls generic_visit to continue AST traversal.
            *   *Parameters:*
                - **node** (`Import | ImportFrom`): The AST node representing an import statement (either `Import` or `ImportFrom`).
                - **base_name** (`str | None`): An optional base name for the import, typically used for `from ... import ...` statements to specify the module being imported from.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods or functions according to the provided context.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
            *   *Description:* This method is an AST NodeVisitor handler for ImportFrom nodes. It extracts the module name from the import statement. If it's a direct import (e.g., `from a.b.c import d`), it takes the last part of the module name (`c`) as the base and delegates to visit_Import. If it's a relative import (no explicit module name, e.g., `from .. import x`), it attempts to resolve the actual module names using the _resolve_module_name helper. Any ImportError during resolution is caught and printed. It then calls generic_visit to continue AST traversal.
            *   *Parameters:*
                - **node** (`ImportFrom`): The AST `ImportFrom` node representing the import statement.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods or functions according to the provided context.
    #### Function: `build_file_dependency_graph`
    *   **Summary:** This function constructs a directed graph representing file dependencies within a repository. It initializes an empty networkx.DiGraph object. It then creates an instance of FileDependencyGraph, which is an AST visitor, to process the provided Abstract Syntax Tree (AST) of a specific file. The visitor populates an internal dictionary with import dependencies. Finally, the function iterates through these collected dependencies, adding nodes for both callers and callees, and creating directed edges from each caller to its respective callees in the graph, before returning the complete dependency graph.
    *   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph`
    *   **Description:** This function constructs a directed graph representing file dependencies within a repository. It initializes an empty networkx.DiGraph object. It then creates an instance of FileDependencyGraph, which is an AST visitor, to process the provided Abstract Syntax Tree (AST) of a specific file. The visitor populates an internal dictionary with import dependencies. Finally, the function iterates through these collected dependencies, adding nodes for both callers and callees, and creating directed edges from each caller to its respective callees in the graph, before returning the complete dependency graph.
    *   **Parameters:**
        - **filename** (`str`): The path to the file for which dependencies are being built.
        - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed for dependencies.
        - **repo_root** (`str`): The root directory of the repository, used for resolving file paths and dependencies.
    *   **Returns:** `graph` (`nx.DiGraph`): A directed graph where nodes represent files/modules and edges indicate import dependencies.
    *   **Usage:** This function calls no other functions.

    #### Function: `build_repository_graph`
    *   **Summary:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It iterates through all Python files, parses each file's content into an Abstract Syntax Tree (AST), and then uses a helper function to build a dependency graph for that individual file. Finally, it aggregates all these individual file graphs into a single, global networkx.DiGraph, adding nodes and edges to represent the overall repository structure.
    *   **Signature:** `def build_repository_graph(repository: GitRepository) -> nx.DiGraph`
    *   **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It iterates through all Python files, parses each file's content into an Abstract Syntax Tree (AST), and then uses a helper function to build a dependency graph for that individual file. Finally, it aggregates all these individual file graphs into a single, global networkx.DiGraph, adding nodes and edges to represent the overall repository structure.
    *   **Parameters:**
        - **repository** (`GitRepository`): The GitRepository object containing the files to be analyzed for dependencies.
    *   **Returns:** `global_graph` (`nx.DiGraph`): A directed graph representing the aggregated file-level dependencies across the entire repository.
    *   **Usage:** This function calls no other functions.

    #### Function: `get_all_temp_files`
    *   **Summary:** This function identifies and retrieves all Python files within a specified directory and its subdirectories. It takes a directory path as input, resolves it to an absolute path, and then recursively searches for all files with a '.py' extension. The function returns a list of these file paths, each represented as a pathlib.Path object relative to the initial root directory. This utility is useful for tasks requiring a comprehensive list of Python source files within a given project structure.
    *   **Signature:** `def get_all_temp_files(directory: str) -> list[Path]`
    *   **Description:** This function identifies and retrieves all Python files within a specified directory and its subdirectories. It takes a directory path as input, resolves it to an absolute path, and then recursively searches for all files with a '.py' extension. The function returns a list of these file paths, each represented as a pathlib.Path object relative to the initial root directory. This utility is useful for tasks requiring a comprehensive list of Python source files within a given project structure.
    *   **Parameters:**
        - **directory** (`str`): The path to the root directory from which to start searching for Python files.
    *   **Returns:** `all_files` (`list[Path]`): A list of pathlib.Path objects, each representing a Python file found within the specified directory, relative to the root_path.
    *   **Usage:** This function calls no other functions.

    #### Class: `FileDependencyGraph`
    *   **Summary:** The FileDependencyGraph class is an AST NodeVisitor designed to analyze Python source code files and build a graph of their import dependencies. It initializes with a specific filename and the repository root to correctly resolve module paths. The class overrides visit_Import and visit_ImportFrom methods to capture import statements and store them in an import_dependencies dictionary. It includes sophisticated logic to resolve complex relative imports, ensuring accurate dependency mapping within a given repository structure.
    *   **Instantiation:** This class is not explicitly instantiated by any other components according to the provided context.
    *   **Dependencies:** This class does not have any explicit external dependencies according to the provided context.
    *   **Constructor:**
        *   *Description:* This constructor initializes the FileDependencyGraph instance by storing the filename of the file being analyzed and the repo_root directory. These attributes are crucial for resolving relative imports and locating files within the repository.
        *   *Parameters:*
            - **filename** (`str`): The name of the file currently being analyzed for dependencies.
            - **repo_root** (`Any`): The root directory of the repository where the file resides.
    *   **Methods:**
        *   **`_resolve_module_name`**
            *   *Signature:* `def _resolve_module_name(self, node: ImportFrom) -> list[str]`
            *   *Description:* This method resolves relative import statements like `from .. import name`. It determines the actual module or symbol names that are being imported by navigating the file system based on the import level and the current file's path. It checks for the existence of module files (.py) or package __init__.py files, and also verifies if symbols are explicitly exported via __all__ or defined within __init__.py. If no valid module or symbol can be resolved, it raises an ImportError.
            *   *Parameters:*
                - **node** (`ImportFrom`): The AST `ImportFrom` node representing the relative import statement.
            *   *Returns:* `resolved` (`list[str]`): A list of resolved module or symbol names that actually exist.
            *   **Usage:** This method does not explicitly call other methods or functions according to the provided context.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node: Import | ImportFrom, base_name: str | None = None)`
            *   *Description:* This method is part of the AST NodeVisitor pattern, specifically handling Import and ImportFrom nodes. It iterates through the imported aliases and records them as dependencies for the current self.filename in the import_dependencies dictionary. If a base_name is provided (typically for from ... import ... statements), it uses that; otherwise, it uses the alias name directly. Finally, it calls generic_visit to continue AST traversal.
            *   *Parameters:*
                - **node** (`Import | ImportFrom`): The AST node representing an import statement (either `Import` or `ImportFrom`).
                - **base_name** (`str | None`): An optional base name for the import, typically used for `from ... import ...` statements to specify the module being imported from.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods or functions according to the provided context.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node: ImportFrom)`
            *   *Description:* This method is an AST NodeVisitor handler for ImportFrom nodes. It extracts the module name from the import statement. If it's a direct import (e.g., `from a.b.c import d`), it takes the last part of the module name (`c`) as the base and delegates to visit_Import. If it's a relative import (no explicit module name, e.g., `from .. import x`), it attempts to resolve the actual module names using the _resolve_module_name helper. Any ImportError during resolution is caught and printed. It then calls generic_visit to continue AST traversal.
            *   *Parameters:*
                - **node** (`ImportFrom`): The AST `ImportFrom` node representing the import statement.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods or functions according to the provided context.

    ### File: `backend/HelperLLM.py`

    #### Class: `LLMHelper`
    *   **Summary:** The LLMHelper class provides a centralized interface for interacting with various Large Language Models (LLMs) to generate structured documentation for Python functions and classes. It handles the configuration of different LLM providers (Gemini, OpenAI, Ollama, or custom endpoints) and manages API interaction, including batch processing and rate limiting. The class ensures that LLM outputs conform to predefined Pydantic schemas for FunctionAnalysis and ClassAnalysis, streamlining the documentation generation workflow.
    *   **Instantiation:** The instantiation points for this class are not specified in the provided context.
    *   **Dependencies:** The class depends on logging, json, time, langchain_google_genai.ChatGoogleGenerativeAI, langchain_ollama.ChatOllama, langchain_openai.ChatOpenAI, langchain.messages.HumanMessage, langchain.messages.SystemMessage, schemas.types.FunctionAnalysis, schemas.types.ClassAnalysis, schemas.types.FunctionAnalysisInput, and schemas.types.ClassAnalysisInput. It also implicitly depends on SCADSLLM_URL and OLLAMA_BASE_URL environment variables for certain model configurations.
    *   **Constructor:**
        *   *Description:* The constructor initializes the LLMHelper instance by setting up the API key and loading system prompts for function and class analysis from specified file paths. It then configures the appropriate language model (Gemini, OpenAI, custom, or Ollama) based on the model_name and base_url parameters, integrating it with structured output capabilities for FunctionAnalysis and ClassAnalysis schemas. Finally, it sets the batch size for API calls by invoking _configure_batch_settings.
        *   *Parameters:*
            - **api_key** (`str`): The API key for the chosen LLM service.
            - **function_prompt_path** (`str`): Path to the file containing the system prompt for function analysis.
            - **class_prompt_path** (`str`): Path to the file containing the system prompt for class analysis.
            - **model_name** (`str`): The name of the LLM model to use (default: "gemini-2.0-flash-lite").
            - **base_url** (`str | None`): The base URL for custom or Ollama LLM endpoints (optional).
    *   **Methods:**
        *   **`_configure_batch_settings`**
            *   *Signature:* `def _configure_batch_settings(self, model_name: str)`
            *   *Description:* This private method dynamically sets the batch_size attribute of the LLMHelper instance based on the provided model_name. It uses a series of conditional checks to assign specific batch sizes for various known Gemini, GPT, and custom models, optimizing the number of concurrent API calls. If the model name is unrecognized, it defaults to a conservative batch size of 2 and logs a warning.
            *   *Parameters:*
                - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
            *   *Returns:* None
            *   **Usage:** This method uses logging.warning for informational purposes.
        *   **`generate_for_functions`**
            *   *Signature:* `def generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]`
            *   *Description:* This method takes a list of FunctionAnalysisInput objects, converts them into JSON payloads, and then constructs a list of conversations for the LLM. It processes these conversations in batches, using the self.function_llm to generate structured function analyses. The method includes error handling for batch calls and implements a waiting period between batches to respect API rate limits, ultimately returning a list of FunctionAnalysis objects or None for failed items.
            *   *Parameters:*
                - **function_inputs** (`List[FunctionAnalysisInput]`): A list of input objects containing data required for function analysis.
            *   *Returns:* `None` (`List[Optional[FunctionAnalysis]]`): A list of generated FunctionAnalysis objects, with None for any failed analyses.
            *   **Usage:** This method calls json.dumps, len, logging.info, logging.error, time.sleep, and self.function_llm.batch.
        *   **`generate_for_classes`**
            *   *Signature:* `def generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]`
            *   *Description:* This method is responsible for generating structured documentation for a batch of classes. It takes a list of ClassAnalysisInput objects, converts them into JSON payloads, and prepares them as conversations for the LLM. The method then iteratively calls self.class_llm.batch to process these conversations, managing potential errors and implementing rate-limiting delays. It returns a list of ClassAnalysis objects, with None for any entries that failed during processing.
            *   *Parameters:*
                - **class_inputs** (`List[ClassAnalysisInput]`): A list of input objects containing data required for class analysis.
            *   *Returns:* `None` (`List[Optional[ClassAnalysis]]`): A list of generated ClassAnalysis objects, with None for any failed analyses.
            *   **Usage:** This method calls json.dumps, len, logging.info, logging.error, time.sleep, and self.class_llm.batch.

    #### Function: `main_orchestrator`
    *   **Summary:** This function serves as a dummy orchestrator and processing loop designed for testing the LLMHelper class. It defines pre-computed analysis data for several example functions and a class, simulating the input and output structures of a documentation generation process. The function instantiates an LLMHelper, uses it to generate documentation for the defined functions, and then aggregates and prints the results. It demonstrates the workflow of using the LLMHelper to process function and class analysis inputs.
    *   **Signature:** `def main_orchestrator()`
    *   **Description:** This function serves as a dummy orchestrator and processing loop designed for testing the LLMHelper class. It defines pre-computed analysis data for several example functions and a class, simulating the input and output structures of a documentation generation process. The function instantiates an LLMHelper, uses it to generate documentation for the defined functions, and then aggregates and prints the results. It demonstrates the workflow of using the LLMHelper to process function and class analysis inputs.
    *   **Parameters:** None
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    ### File: `backend/MainLLM.py`

    #### Class: `MainLLM`
    *   **Summary:** The MainLLM class serves as a versatile interface for interacting with various Large Language Models (LLMs), abstracting away the specifics of different providers. It initializes with a system prompt loaded from a file and dynamically configures an LLM client (e.g., Google Gemini, OpenAI-compatible, Ollama) based on the provided model name and optional base URL. The class offers methods for both single-shot LLM calls and streaming responses, ensuring robust communication with the chosen language model while handling potential errors.
    *   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* This constructor initializes the MainLLM class by setting up the system prompt from a file and configuring the underlying Large Language Model (LLM) client. It supports various LLM providers like Google Gemini, OpenAI-compatible APIs (potentially custom ones via SCADSLLM_URL), and Ollama, dynamically selecting the client based on the model_name and base_url parameters. It also performs validation for the API key and prompt file path.
        *   *Parameters:*
            - **api_key** (`str`): The API key required for authenticating with the chosen LLM service.
            - **prompt_file_path** (`str`): The file path to the system prompt that will guide the LLM's behavior.
            - **model_name** (`str`): The name of the LLM model to use, defaulting to 'gemini-2.5-pro'. This determines which LLM client is instantiated.
            - **base_url** (`str | None`): An optional base URL for custom LLM endpoints, used primarily for Ollama or other compatible services.
    *   **Methods:**
        *   **`call_llm`**
            *   *Signature:* `def call_llm(self, user_input: str)`
            *   *Description:* This method sends a user input to the configured LLM and retrieves a single, complete response. It constructs a list of messages including the class's system prompt and the provided user input. The method then invokes the underlying LLM client, logs the process, and returns the content of the LLM's response. Error handling is included to catch exceptions during the LLM call and return None in case of failure.
            *   *Parameters:*
                - **user_input** (`str`): The user's query or message to be sent to the LLM.
            *   *Returns:* `content` (`str | None`): The generated text content from the LLM, or None if an error occurred during the call.
            *   **Usage:** Based on the provided context, this method does not explicitly call other functions or methods.
        *   **`stream_llm`**
            *   *Signature:* `def stream_llm(self, user_input: str)`
            *   *Description:* This method interacts with the configured LLM to receive a response in a streaming fashion, yielding chunks of content as they become available. It constructs the message payload using the system prompt and user input, then initiates a streaming call to the LLM. Each yielded chunk's content is passed back to the caller. Error handling is implemented to catch exceptions during the streaming process and yield an error message.
            *   *Parameters:*
                - **user_input** (`str`): The user's query or message for which a streaming LLM response is desired.
            *   *Returns:* `chunk.content` (`generator[str]`): A generator that yields successive string chunks of the LLM's response as they are generated, or an error message string if an exception occurs.
            *   **Usage:** Based on the provided context, this method does not explicitly call other functions or methods.

    ### File: `backend/basic_info.py`

    #### Class: `ProjektInfoExtractor`
    *   **Summary:** The ProjektInfoExtractor class is designed to extract and structure fundamental project information from various common project files, such as READMEs, pyproject.toml, and requirements.txt. It orchestrates the parsing of these files, prioritizing certain sources, and consolidates the extracted data into a structured dictionary. The class handles content cleaning, Markdown section extraction, and provides fallback mechanisms for missing information, including deriving a project title from a repository URL.
    *   **Instantiation:** This class is not explicitly shown to be instantiated by any other components in the provided context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The constructor initializes the `INFO_NICHT_GEFUNDEN` constant, which serves as a placeholder for information that could not be found. It also sets up the `info` dictionary, which is the primary data structure for storing extracted project details, pre-populating all fields with the `INFO_NICHT_GEFUNDEN` placeholder.
        *   *Parameters:* None
    *   **Methods:**
        *   **`_clean_content`**
            *   *Signature:* `def _clean_content(self, content: str) -> str`
            *   *Description:* This private helper method is responsible for sanitizing string content by removing null bytes (`\x00`). Null bytes can often appear in text files due to encoding mismatches, such as reading a UTF-16 encoded file as UTF-8. The method first checks if the input content is empty; if so, it returns an empty string. Otherwise, it performs a global replacement of null bytes with an empty string, returning the cleaned content.
            *   *Parameters:*
                - **content** (`str`): The string content to be cleaned.
            *   *Returns:* `None` (`str`): The cleaned string with null bytes removed.
            *   **Usage:** This method does not explicitly call other methods, classes, or functions in the provided context.
        *   **`_finde_datei`**
            *   *Signature:* `def _finde_datei(self, patterns: List[str], dateien: List[Any]) -> Optional[Any]`
            *   *Description:* This private helper method searches through a list of file objects to find one whose path matches any of the provided patterns. The search is performed case-insensitively, checking if a file's path ends with any of the specified patterns. It iterates through each file and each pattern, returning the first matching file object found. If no file matches any of the patterns, the method returns `None`.
            *   *Parameters:*
                - **patterns** (`List[str]`): A list of string patterns to match against file paths.
                - **dateien** (`List[Any]`): A list of file objects, where each object is expected to have a 'path' attribute.
            *   *Returns:* `None` (`Optional[Any]`): The first file object that matches a pattern, or None if no match is found.
            *   **Usage:** This method does not explicitly call other methods, classes, or functions in the provided context.
        *   **`_extrahiere_sektion_aus_markdown`**
            *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str]) -> Optional[str]`
            *   *Description:* This private helper method extracts text content from a Markdown string that appears under a level 2 heading (##) matching any of the given keywords. It constructs a regular expression pattern dynamically from the keywords to locate the heading. The method then captures all content following the matched heading up to the next level 2 heading or the end of the document. The extracted content is stripped of leading/trailing whitespace before being returned, or `None` if no matching section is found.
            *   *Parameters:*
                - **inhalt** (`str`): The Markdown content string from which to extract a section.
                - **keywords** (`List[str]`): A list of keywords to match against Markdown level 2 headings.
            *   *Returns:* `None` (`Optional[str]`): The extracted and stripped text content of the section, or None if no matching section is found.
            *   **Usage:** This method does not explicitly call other methods, classes, or functions in the provided context.
        *   **`_parse_readme`**
            *   *Signature:* `def _parse_readme(self, inhalt: str)`
            *   *Description:* This private method parses the content of a README file to extract various project details, including the title, description, key features, tech stack, current status, installation instructions, and a quick start guide. It first cleans the input content using `_clean_content`. It then uses regular expressions to find the main title and description, and leverages `_extrahiere_sektion_aus_markdown` to locate and extract specific sections based on predefined keywords. Information is only updated in the `info` dictionary if it hasn't already been found (i.e., still holds the `INFO_NICHT_GEFUNDEN` placeholder).
            *   *Parameters:*
                - **inhalt** (`str`): The content of the README file as a string.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods, classes, or functions in the provided context.
        *   **`_parse_toml`**
            *   *Signature:* `def _parse_toml(self, inhalt: str)`
            *   *Description:* This private method parses the content of a `pyproject.toml` file to extract project-level information such as the project name, description, and dependencies. It begins by cleaning the input content using `_clean_content`. The method then attempts to load and parse the TOML content using the `tomllib` module. If `tomllib` is not available or a `TOMLDecodeError` occurs during parsing, a warning is printed. Upon successful parsing, it extracts relevant data from the `[project]` table and updates the class's `info` dictionary.
            *   *Parameters:*
                - **inhalt** (`str`): The content of the pyproject.toml file as a string.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods, classes, or functions in the provided context.
        *   **`_parse_requirements`**
            *   *Signature:* `def _parse_requirements(self, inhalt: str)`
            *   *Description:* This private method parses the content of a `requirements.txt` file to identify project dependencies. It first cleans the input content using `_clean_content`. The method only proceeds to populate the `dependencies` field in the class's `info` dictionary if it has not already been set by a higher-priority source (e.g., `pyproject.toml`). It processes each line of the file, filtering out empty lines and comments, and stores the remaining non-comment lines as a list of dependencies.
            *   *Parameters:*
                - **inhalt** (`str`): The content of the requirements.txt file as a string.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods, classes, or functions in the provided context.
        *   **`extrahiere_info`**
            *   *Signature:* `def extrahiere_info(self, dateien: List[Any], repo_url: str) -> Dict[str, Any]`
            *   *Description:* This is the main public method that orchestrates the entire information extraction process. It takes a list of file objects and a repository URL as input. The method first uses `_finde_datei` to locate relevant project files (README, pyproject.toml, requirements.txt). It then parses these files in a specific order of priority: `pyproject.toml`, then `requirements.txt`, and finally `README.md`, allowing later parsing steps to fill in information not found by earlier ones. After parsing, it formats the extracted dependencies and, as a fallback, attempts to derive a project title from the `repo_url` if no title was found elsewhere. Finally, it returns the comprehensive `info` dictionary containing all extracted project details.
            *   *Parameters:*
                - **dateien** (`List[Any]`): A list of file objects (e.g., from a repository scan) to be analyzed for project information.
                - **repo_url** (`str`): The URL of the repository, used as a fallback to derive a project title if none is found in the files.
            *   *Returns:* `None` (`Dict[str, Any]`): A dictionary containing all extracted project information, structured into 'projekt_uebersicht' and 'installation' categories.
            *   **Usage:** This method does not explicitly call other methods, classes, or functions in the provided context.

    ### File: `backend/callgraph.py`

    #### Class: `CallGraph`
    *   **Summary:** The CallGraph class is an ast.NodeVisitor designed to construct a call graph for a given Python source file. It traverses the Abstract Syntax Tree (AST) of a file, identifying function and class definitions, import statements, and function calls. By maintaining context of the current file, class, and function, it resolves call targets to fully qualified names and records these relationships in an internal directed graph and an edge dictionary. This class is crucial for understanding the dynamic flow and dependencies between functions within a Python project.
    *   **Instantiation:** This class is not explicitly instantiated by other components based on the provided context.
    *   **Dependencies:** This class does not explicitly depend on other components based on the provided context.
    *   **Constructor:**
        *   *Description:* The constructor initializes the CallGraph instance by setting the filename, and preparing internal state variables to track the current function and class during AST traversal. It also sets up data structures such as a dictionary for local definitions, a NetworkX directed graph, an import mapping, a set for discovered functions, and a dictionary to store call edges.
        *   *Parameters:*
            - **filename** (`str`): The path to the source file that this CallGraph instance will analyze.
    *   **Methods:**
        *   **`_recursive_call`**
            *   *Signature:* `def _recursive_call(self, node)`
            *   *Description:* This method recursively traverses an AST node to extract the components of a called name. It handles different node types: for an ast.Call, it recurses on the function part; for an ast.Name, it returns the identifier; and for an ast.Attribute, it recurses on the value and appends the attribute name. The method's purpose is to decompose complex call expressions into a list of their dotted name components, such as ['pkg', 'mod', 'Class', 'method'].
            *   *Parameters:*
                - **node** (`ast.AST`): The AST node representing a function call, name, or attribute access.
            *   *Returns:* `parts` (`list[str]`): A list of string components representing the fully qualified name of the called entity.
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`_resolve_all_callee_names`**
            *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes: list[list[str]]) -> list[str]`
            *   *Description:* This method takes a list of potential callee name components and resolves them to their fully qualified names. It prioritizes resolution by checking local definitions (self.local_defs) first, then import mappings (self.import_mapping). If no local or imported resolution is found, it constructs a full name based on the current filename and class context. This ensures that each call target is identified with a unique, global identifier within the project.
            *   *Parameters:*
                - **callee_nodes** (`list[list[str]]`): A list where each inner list represents the name components of a potential callee (e.g., [['module', 'function']]).
            *   *Returns:* `resolved` (`list[str]`): A list of fully qualified string names for the resolved callees.
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`_make_full_name`**
            *   *Signature:* `def _make_full_name(self, basename: str, class_name: str | None = None) -> str`
            *   *Description:* This helper method constructs a fully qualified name for a function or method. It prepends the self.filename to the basename. If a class_name is provided, it also includes the class name in the format filename::ClassName::basename. This ensures unique identification of functions within the project, distinguishing them by their file and class context.
            *   *Parameters:*
                - **basename** (`str`): The base name of the function or method.
                - **class_name** (`str | None`): The name of the class if the function is a method, or None otherwise.
            *   *Returns:* `full_name` (`str`): The fully qualified name of the function or method.
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`_current_caller`**
            *   *Signature:* `def _current_caller(self) -> str`
            *   *Description:* This method determines the identifier of the current calling context. If self.current_function is set, it returns that value, indicating a function is currently being processed. Otherwise, it returns a placeholder indicating the global scope, using the self.filename if available, or a generic '<global-scope>'. This is used to identify the source of a function call when recording edges in the call graph.
            *   *Parameters:* None
            *   *Returns:* `caller_identifier` (`str`): The fully qualified name of the current function or a global scope identifier.
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method is an override from ast.NodeVisitor, specifically for processing ast.Import nodes. It iterates through each alias in the import statement, mapping the imported module's name (or its 'asname') to its original module name in the self.import_mapping dictionary. This mapping is crucial for resolving imported names during call graph construction. After processing, it calls self.generic_visit to continue traversing the AST.
            *   *Parameters:*
                - **node** (`ast.Import`): The AST node representing an 'import' statement.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method is an override from ast.NodeVisitor, designed to process ast.ImportFrom nodes. It extracts the base module name from node.module and then iterates through each alias in the import statement. It maps the alias (or its original name) to the module name in self.import_mapping. This helps in resolving imported names to their source modules, especially for 'from ... import ...' statements.
            *   *Parameters:*
                - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node: ast.ClassDef)`
            *   *Description:* This method is an override from ast.NodeVisitor for processing ast.ClassDef nodes. It temporarily sets self.current_class to the name of the class being visited, which is essential for nested methods to correctly form their fully qualified names. It then performs a generic visit to traverse the class's body and restores the previous self.current_class after the class definition has been fully processed, ensuring proper context management.
            *   *Parameters:*
                - **node** (`ast.ClassDef`): The AST node representing a class definition.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method is an override from ast.NodeVisitor for processing ast.FunctionDef nodes. It constructs the fully qualified name of the function using _make_full_name and stores it in self.local_defs. It updates self.current_function to track the current context, adds the function as a node to self.graph, and then performs a generic visit to process the function's body. Finally, it adds the function to self.function_set and restores the previous self.current_function, maintaining the correct scope.
            *   *Parameters:*
                - **node** (`ast.FunctionDef`): The AST node representing a function definition.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`visit_AsyncFunctionDef`**
            *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
            *   *Description:* This method is an override from ast.NodeVisitor for processing ast.AsyncFunctionDef nodes. It simplifies the handling of asynchronous function definitions by delegating their processing directly to the visit_FunctionDef method. This approach ensures that asynchronous functions are treated similarly to regular functions for the purpose of call graph construction, capturing their names and call relationships effectively.
            *   *Parameters:*
                - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`visit_Call`**
            *   *Signature:* `def visit_Call(self, node)`
            *   *Description:* This method is an override from ast.NodeVisitor for processing ast.Call nodes, which are central to building the call graph. It first identifies the 'caller' using _current_caller, then extracts the potential 'callee' name components using _recursive_call, and resolves these names to fully qualified identifiers using _resolve_all_callee_names. Finally, it records the call relationship by adding the resolved callees to the self.edges dictionary for the current caller. It then continues the AST traversal with self.generic_visit.
            *   *Parameters:*
                - **node** (`ast.Call`): The AST node representing a function call.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.
        *   **`visit_If`**
            *   *Signature:* `def visit_If(self, node)`
            *   *Description:* This method is an override from ast.NodeVisitor for processing ast.If nodes. It specifically handles the common 'if __name__ == "__main__":' block by temporarily setting self.current_function to "<main_block>". This allows any function calls within this block to be correctly attributed to the main execution scope. For other 'if' statements, it simply performs a generic visit, ensuring all branches of conditional logic are traversed.
            *   *Parameters:*
                - **node** (`ast.If`): The AST node representing an 'if' statement.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call any other functions or methods based on the provided context.

    #### Function: `make_safe_dot`
    *   **Summary:** This function takes a NetworkX directed graph and a file path, then generates a DOT file. It first creates a copy of the input graph and relabels its nodes with safe, generic identifiers (e.g., "n0", "n1"). The original node names are preserved by assigning them as 'label' attributes to the newly relabeled nodes. Finally, the modified graph is written to the specified output path in DOT format.
    *   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
    *   **Description:** This function takes a NetworkX directed graph and a file path, then generates a DOT file. It first creates a copy of the input graph and relabels its nodes with safe, generic identifiers (e.g., "n0", "n1"). The original node names are preserved by assigning them as 'label' attributes to the newly relabeled nodes. Finally, the modified graph is written to the specified output path in DOT format.
    *   **Parameters:**
        - **graph** (`nx.DiGraph`): The NetworkX directed graph to be converted into a DOT file.
        - **out_path** (`str`): The file path where the DOT graph representation will be saved.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `build_filtered_callgraph`
    *   **Summary:** This function constructs a directed call graph for a given Git repository. It first identifies all user-defined functions across the Python files within the repository by parsing their Abstract Syntax Trees (ASTs). Subsequently, it builds a global call graph, including only those call relationships where both the caller and the callee are identified as user-defined functions. The resulting graph is an nx.DiGraph representing the filtered call relationships.
    *   **Signature:** `def build_filtered_callgraph(repo: GitRepository) -> nx.DiGraph`
    *   **Description:** This function constructs a directed call graph for a given Git repository. It first identifies all user-defined functions across the Python files within the repository by parsing their Abstract Syntax Trees (ASTs). Subsequently, it builds a global call graph, including only those call relationships where both the caller and the callee are identified as user-defined functions. The resulting graph is an nx.DiGraph representing the filtered call relationships.
    *   **Parameters:**
        - **repo** (`GitRepository`): The GitRepository object from which to extract files and build the call graph.
    *   **Returns:** `global_graph` (`networkx.DiGraph`): A directed graph representing the filtered call relationships between user-defined functions within the repository.
    *   **Usage:** This function calls no other functions.

    #### Function: `wrap_cdata`
    *   **Summary:** This function is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string that begins with "<![CDATA[", followed by a newline, the provided `content`, another newline, and finally "]]>" to close the CDATA section. This ensures that the `content` is treated as raw character data by an XML parser, preventing issues with special characters.
    *   **Signature:** `def wrap_cdata(content)`
    *   **Description:** This function is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string that begins with "<![CDATA[", followed by a newline, the provided `content`, another newline, and finally "]]>" to close the CDATA section. This ensures that the `content` is treated as raw character data by an XML parser, preventing issues with special characters.
    *   **Parameters:**
        - **content** (`str`): The string content to be wrapped in CDATA tags.
    *   **Returns:** `wrapped_content` (`str`): A string with the provided content wrapped inside CDATA tags.
    *   **Usage:** This function calls no other functions.

    #### Function: `extract_output_content`
    *   **Summary:** This function processes a list of notebook output objects to extract their content, converting them into a list of strings or special placeholders. It iterates through each output, handling different types such as display data, execution results, streams, and errors. For image data (PNG or JPEG), it decodes the Base64 string, stores the raw Base64 data in a provided mutable image list, and generates an XML-like placeholder string for the extracted content. Textual outputs, including plain text, stream output, and formatted error messages, are directly appended to the result list.
    *   **Signature:** `def extract_output_content(outputs, image_list)`
    *   **Description:** This function processes a list of notebook output objects to extract their content, converting them into a list of strings or special placeholders. It iterates through each output, handling different types such as display data, execution results, streams, and errors. For image data (PNG or JPEG), it decodes the Base64 string, stores the raw Base64 data in a provided mutable image list, and generates an XML-like placeholder string for the extracted content. Textual outputs, including plain text, stream output, and formatted error messages, are directly appended to the result list.
    *   **Parameters:**
        - **outputs** (`list`): A list of output objects, typically from a notebook execution, each potentially containing different types of data.
        - **image_list** (`list[dict]`): A mutable list passed by reference, used to collect dictionaries of image data (mime_type and Base64 string) found within the outputs.
    *   **Returns:** `extracted_xml_snippets` (`list[str]`): A list of strings, where each string is either extracted text content, an XML-like image placeholder, or a formatted error message.
    *   **Usage:** This function calls no other functions.

    #### Function: `process_image`
    *   **Summary:** This function aims to process image data identified by a given MIME type. It attempts to retrieve a base64 encoded string from an external `data` dictionary using the `mime_type` as a key. The retrieved string is then cleaned by removing newline characters. Subsequently, the function intends to store the processed image data and its MIME type into an external `image_list`. Finally, it returns a formatted string representing an image placeholder, or an error message if an exception occurs during processing, or `None` if the `mime_type` is not found in `data`.
    *   **Signature:** `def process_image(mime_type)`
    *   **Description:** This function aims to process image data identified by a given MIME type. It attempts to retrieve a base64 encoded string from an external `data` dictionary using the `mime_type` as a key. The retrieved string is then cleaned by removing newline characters. Subsequently, the function intends to store the processed image data and its MIME type into an external `image_list`. Finally, it returns a formatted string representing an image placeholder, or an error message if an exception occurs during processing, or `None` if the `mime_type` is not found in `data`.
    *   **Parameters:**
        - **mime_type** (`str`): The MIME type of the image to be processed, used as a key to retrieve image data.
    *   **Returns:** `return_value` (`str` or None): Returns a formatted string acting as an image placeholder if successful, an error message string if an exception occurs during image processing, or `None` if the specified `mime_type` is not found in the external `data` source.
    *   **Usage:** This function calls no other functions.
    *   **Error:** The function `process_image` relies on external variables `data` and `image_list` which are not defined within its scope or passed as parameters, making its direct execution context and operational viability unclear from the provided snippet.

    #### Function: `convert_notebook_to_xml`
    *   **Summary:** This function converts the raw content of a Jupyter notebook, provided as a string, into a structured XML representation. It first attempts to parse the input using `nbformat.reads` and gracefully handles `NotJSONError` by returning an error message. The function then iterates through each cell, generating XML tags for markdown and code cell sources. For code cells with outputs, it processes them to extract content and potential images, which are also wrapped in XML output tags. Finally, it returns the combined XML string and a list of any extracted images.
    *   **Signature:** `def convert_notebook_to_xml(file_content)`
    *   **Description:** This function converts the raw content of a Jupyter notebook, provided as a string, into a structured XML representation. It first attempts to parse the input using `nbformat.reads` and gracefully handles `NotJSONError` by returning an error message. The function then iterates through each cell, generating XML tags for markdown and code cell sources. For code cells with outputs, it processes them to extract content and potential images, which are also wrapped in XML output tags. Finally, it returns the combined XML string and a list of any extracted images.
    *   **Parameters:**
        - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a JSON string.
    *   **Returns:** `xml_output_or_error` (`str`): The XML representation of the notebook content if successful, or an error message string if parsing fails.
        `extracted_images` (`list`): A list of extracted image data (e.g., base64 encoded strings) from the notebook outputs.
    *   **Usage:** This function calls no other functions.

    #### Function: `process_repo_notebooks`
    *   **Summary:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It filters the input list to include only files with a '.ipynb' extension. For each identified notebook, it attempts to convert its content into an XML representation and extract any associated images. The function then compiles these conversion results into a dictionary, where each notebook's path maps to its XML output and extracted images, and returns this aggregated data.
    *   **Signature:** `def process_repo_notebooks(repo_files)`
    *   **Description:** This function processes a collection of repository files to identify and convert Jupyter notebooks. It filters the input list to include only files with a '.ipynb' extension. For each identified notebook, it attempts to convert its content into an XML representation and extract any associated images. The function then compiles these conversion results into a dictionary, where each notebook's path maps to its XML output and extracted images, and returns this aggregated data.
    *   **Parameters:**
        - **repo_files** (`List[file-like objects]`): A list of file-like objects from a repository. Each object is expected to have a 'path' attribute (string) and a 'content' attribute (representing the file's raw content).
    *   **Returns:** `results` (`Dict[str, Dict[str, Any]]`): A dictionary where keys are the paths (string) of the processed notebook files. Each value is a dictionary containing the 'xml' (string) conversion of the notebook and 'images' (any type) extracted during the conversion process.
    *   **Usage:** This function calls no other functions.

    ### File: `backend/getRepo.py`

    #### Class: `RepoFile`
    *   **Summary:** The `RepoFile` class represents a single file within a Git repository, designed to provide lazy loading of its content and metadata. It encapsulates the file's path and the Git tree object from which it originates. The class offers properties to access the Git blob, decoded file content, and file size efficiently, only loading them upon first access. Additionally, it includes utility methods for basic file analysis and structured data export.
    *   **Instantiation:** This class is not explicitly instantiated by other components listed in the provided context.
    *   **Dependencies:** This class does not have explicit external functional dependencies listed in the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method initializes a `RepoFile` object by setting its file path and the Git tree object. It also sets up internal attributes (`_blob`, `_content`, `_size`) to `None`, indicating that these properties will be loaded lazily upon their first access.
        *   *Parameters:*
            - **file_path** (`str`): The path to the file within the repository.
            - **commit_tree** (`git.Tree`): The Git Tree object of the commit from which the file originates.
    *   **Methods:**
        *   **`blob`**
            *   *Signature:* `@property def blob(self)`
            *   *Description:* This property provides lazy loading for the Git blob object corresponding to the file. It checks if the `_blob` attribute is already populated; if not, it attempts to retrieve the blob from the `_tree` using the stored file path. If the file is not found within the commit tree, a `FileNotFoundError` is raised.
            *   *Parameters:* None
            *   *Returns:* `git.Blob`: The Git blob object representing the file.
            *   **Usage:** This method does not explicitly call other methods or functions listed in the provided context.
        *   **`content`**
            *   *Signature:* `@property def content(self)`
            *   *Description:* This property provides lazy loading for the decoded content of the file. It first ensures that the `blob` property has been loaded. If the `_content` attribute is `None`, it reads the data stream from the Git blob, decodes it using UTF-8 (ignoring errors), and stores the result before returning it.
            *   *Parameters:* None
            *   *Returns:* `str`: The decoded content of the file as a string.
            *   **Usage:** This method does not explicitly call other methods or functions listed in the provided context.
        *   **`size`**
            *   *Signature:* `@property def size(self)`
            *   *Description:* This property provides lazy loading for the size of the file in bytes. It first ensures that the `blob` property has been loaded. If the `_size` attribute is `None`, it retrieves the size attribute directly from the Git blob object and stores it before returning the value.
            *   *Parameters:* None
            *   *Returns:* `int`: The size of the file in bytes.
            *   **Usage:** This method does not explicitly call other methods or functions listed in the provided context.
        *   **`analyze_word_count`**
            *   *Signature:* `def analyze_word_count(self)`
            *   *Description:* This method serves as an example analysis function, calculating the total number of words within the file's content. It accesses the `content` property to retrieve the file's text, then splits the string by whitespace to count the resulting words.
            *   *Parameters:* None
            *   *Returns:* `int`: The total number of words in the file content.
            *   **Usage:** This method does not explicitly call other methods or functions listed in the provided context.
        *   **`__repr__`**
            *   *Signature:* `def __repr__(self)`
            *   *Description:* This special method provides a concise and informative string representation of the `RepoFile` object. It returns a string formatted to include the class name and the file's path, which is useful for debugging and logging purposes.
            *   *Parameters:* None
            *   *Returns:* `str`: A string representation of the RepoFile object, typically showing its path.
            *   **Usage:** This method does not explicitly call other methods or functions listed in the provided context.
        *   **`to_dict`**
            *   *Signature:* `def to_dict(self, include_content=False)`
            *   *Description:* This method converts the `RepoFile` object's essential data into a dictionary format. It includes the file's path, its base name, its size, and its type as 'file'. An optional `include_content` parameter allows for the file's decoded content to be added to the dictionary if set to `True`.
            *   *Parameters:*
                - **include_content** (`bool`): A flag indicating whether to include the file's content in the output dictionary. Defaults to `False`.
            *   *Returns:* `dict`: A dictionary containing the file's metadata and optionally its content.
            *   **Usage:** This method does not explicitly call other methods or functions listed in the provided context.

    #### Class: `GitRepository`
    *   **Summary:** The GitRepository class provides a robust mechanism for interacting with a Git repository by cloning it into a temporary location. It manages the lifecycle of the cloned repository, including its creation and cleanup through a context manager protocol. The class offers functionality to list all files within the repository and to represent its structure as a hierarchical file tree, making it suitable for analysis or processing of repository contents.
    *   **Instantiation:** This class is not explicitly instantiated by any known components within the provided context.
    *   **Dependencies:** "The class relies on external libraries such as 'tempfile' for temporary directory management, 'git.Repo' and 'git.GitCommandError' from the GitPython library for Git operations, and 'logging' for informational messages."
    *   **Constructor:**
        *   *Description:* This constructor initializes a GitRepository instance by cloning the specified repository URL into a newly created temporary directory. It sets up essential attributes like the repository URL, the path to the temporary directory, the GitPython Repo object, and an empty list to store file objects. During initialization, it also captures the latest commit and its tree for subsequent file operations, handling potential cloning errors by cleaning up and raising a RuntimeError.
        *   *Parameters:*
            - **repo_url** (`str`): The URL of the Git repository to be cloned.
    *   **Methods:**
        *   **`get_all_files`**
            *   *Signature:* `def get_all_files(self)`
            *   *Description:* This method retrieves a comprehensive list of all files present in the cloned Git repository. It utilizes the underlying GitPython `repo.git.ls_files()` command to obtain file paths, which are then split by newline characters. For each valid file path, a `RepoFile` object is instantiated using the path and the commit tree, and these objects are collected into the `self.files` list, which is then returned.
            *   *Parameters:* None
            *   *Returns:* `files` (`list[RepoFile]`): A list of RepoFile instances, each representing a file in the repository.
            *   **Usage:** This method calls 'self.repo.git.ls_files()' to list files, 'str.split()' to parse the output, and 'RepoFile()' to create file objects.
        *   **`close`**
            *   *Signature:* `def close(self)`
            *   *Description:* This method is intended to clean up resources by nullifying the reference to the temporary directory path, `self.temp_dir`. It prints a message indicating the directory is being 'deleted', but the code itself only sets the `self.temp_dir` attribute to `None`, without explicitly removing the directory from the filesystem.
            *   *Parameters:* None
            *   *Returns:* None
            *   **Usage:** This method calls 'print()' to output a message.
        *   **`__enter__`**
            *   *Signature:* `def __enter__(self)`
            *   *Description:* This special method enables the GitRepository object to function as a context manager, allowing its use within a 'with' statement. When the 'with' block is entered, this method is automatically invoked and simply returns the instance of the GitRepository itself, making it available for use within the block.
            *   *Parameters:* None
            *   *Returns:* `self` (`GitRepository`): The instance of the GitRepository class.
            *   **Usage:** This method does not call any other functions or methods.
        *   **`__exit__`**
            *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
            *   *Description:* This special method is part of the context manager protocol and is automatically executed when exiting a 'with' statement block, regardless of whether an exception occurred. Its primary purpose is to ensure that the `close()` method is invoked, facilitating the cleanup of any resources, such as the temporary directory, that were allocated during the context manager's lifecycle.
            *   *Parameters:*
                - **exc_type** (`type | None`): The type of exception that was raised, or None if no exception occurred.
                - **exc_val** (`Exception | None`): The exception instance that was raised, or None.
                - **exc_tb** (`TracebackType | None`): The traceback object associated with the exception, or None.
            *   *Returns:* None
            *   **Usage:** This method calls 'self.close()' to perform cleanup.
        *   **`get_file_tree`**
            *   *Signature:* `def get_file_tree(self, include_content=False)`
            *   *Description:* This method generates a hierarchical dictionary representation of the repository's file structure, mimicking a file system tree. It first ensures that `self.files` is populated by calling `get_all_files()` if necessary. Then, it iterates through each `RepoFile` object, parsing its path to construct nested dictionary entries for directories and appending file dictionaries at their respective leaf nodes. The `include_content` flag determines whether the actual file content is embedded within the file dictionaries.
            *   *Parameters:*
                - **include_content** (`bool`): A flag indicating whether to include the content of each file in its dictionary representation. Defaults to False.
            *   *Returns:* `tree` (`dict`): A dictionary representing the hierarchical file tree of the repository.
            *   **Usage:** This method calls 'self.get_all_files()' to retrieve files, 'file_obj.path.split()' to parse file paths, and 'file_obj.to_dict()' to convert file objects to dictionaries.

    ### File: `backend/main.py`

    #### Function: `create_savings_chart`
    *   **Summary:** This function generates a bar chart to visually compare two token counts: JSON tokens and TOON tokens. It calculates and displays a savings percentage in the chart's title. The chart includes labels, colors, a grid, and displays the exact token values above each bar. Finally, the generated chart is saved to a specified output file path.
    *   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
    *   **Description:** This function generates a bar chart to visually compare two token counts: JSON tokens and TOON tokens. It calculates and displays a savings percentage in the chart's title. The chart includes labels, colors, a grid, and displays the exact token values above each bar. Finally, the generated chart is saved to a specified output path.
    *   **Parameters:**
        - **json_tokens** (`int`): The number of tokens associated with the JSON format.
        - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
        - **savings_percent** (`float`): The calculated percentage of token savings to be displayed in the chart title.
        - **output_path** (`str`): The file path where the generated bar chart image will be saved.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `calculate_net_time`
    *   **Summary:** This function calculates the effective processing time by subtracting estimated sleep times, which are introduced due to rate-limiting for "gemini-" models, from the total elapsed duration. It first determines the total duration between a start and end time. If the model name does not indicate a 'gemini-' model, or if there are no items, it returns the total duration or zero, respectively. Otherwise, it calculates the number of batches and corresponding sleep time based on a fixed sleep duration per batch, then subtracts this from the total duration to yield the net processing time.
    *   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
    *   **Description:** This function calculates the effective processing time by subtracting estimated sleep times, which are introduced due to rate-limiting for "gemini-" models, from the total elapsed duration. It first determines the total duration between a start and end time. If the model name does not indicate a 'gemini-' model, or if there are no items, it returns the total duration or zero, respectively. Otherwise, it calculates the number of batches and corresponding sleep time based on a fixed sleep duration per batch, then subtracts this from the total duration to yield the net processing time.
    *   **Parameters:**
        - **start_time** (`float`): The starting timestamp or time value for the duration calculation.
        - **end_time** (`float`): The ending timestamp or time value for the duration calculation.
        - **total_items** (`int`): The total number of items processed, used to determine the number of batches.
        - **batch_size** (`int`): The number of items processed per batch, used in conjunction with total_items to calculate batches.
        - **model_name** (`str`): The name of the model, used to check if rate-limiting sleep time calculations are necessary (e.g., for 'gemini-' models).
    *   **Returns:** `net_time` (`float`): The calculated net processing time after accounting for rate-limit sleep durations, or the total duration if no rate-limiting applies, or 0 if total_items is 0 or net_time is negative.
    *   **Usage:** This function calls no other functions.

    #### Function: `main_workflow`
    *   **Summary:** The `main_workflow` function orchestrates a comprehensive analysis of a GitHub repository. It handles the extraction of API keys and model names, clones the specified repository, and then proceeds to extract basic project information, construct a file tree, and analyze code relationships. It builds and enriches an Abstract Syntax Tree (AST) schema, prepares inputs for a Helper LLM to analyze functions and classes, and finally utilizes a Main LLM to generate a detailed final report. The workflow includes error handling, status updates via a callback, token evaluation, and saves the final report along with performance metrics.
    *   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None)`
    *   **Description:** The `main_workflow` function orchestrates a comprehensive analysis of a GitHub repository. It handles the extraction of API keys and model names, clones the specified repository, and then proceeds to extract basic project information, construct a file tree, and analyze code relationships. It builds and enriches an Abstract Syntax Tree (AST) schema, prepares inputs for a Helper LLM to analyze functions and classes, and finally utilizes a Main LLM to generate a detailed final report. The workflow includes error handling, status updates via a callback, token evaluation, and saves the final report along with performance metrics.
    *   **Parameters:**
        - **input** (`Any`): The primary input, expected to contain a GitHub repository URL.
        - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs required for LLM interactions.
        - **model_names** (`dict`): A dictionary specifying the names of the helper and main LLM models to be used.
        - **status_callback** (`Callable`): An optional callback function used to provide status updates during the workflow execution. Defaults to None.
    *   **Returns:**
        - `report` (`str`): The final generated report from the Main LLM, or an error message if report generation failed.
        - `metrics` (`dict`): A dictionary containing performance metrics such as helper LLM time, main LLM time, total active time, model names used, and token savings data.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_status`
    *   **Summary:** This function, `update_status`, is designed to process and log a given message. It first checks if a `status_callback` function is available and, if so, invokes it with the provided message. Regardless of the callback's presence, the function then logs the message using the `logging.info` facility. Its primary purpose is to provide a consistent mechanism for status updates and logging.
    *   **Signature:** `def update_status(msg)`
    *   **Description:** This function, `update_status`, is designed to process and log a given message. It first checks if a `status_callback` function is available and, if so, invokes it with the provided message. Regardless of the callback's presence, the function then logs the message using the `logging.info` facility. Its primary purpose is to provide a consistent mechanism for status updates and logging.
    *   **Parameters:**
        - **msg** (`str`): The message string to be updated and logged.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `notebook_workflow`
    *   **Summary:** This function orchestrates a comprehensive workflow to analyze Jupyter notebooks from a specified GitHub repository. It begins by extracting the repository URL from the input, cloning the repository, and then converting the notebooks into a structured XML format, handling embedded images. Concurrently, it extracts basic project information from the repository files. The function then utilizes a configured Large Language Model (LLM) to generate individual reports for each processed notebook, concatenating them into a final report. It saves this report to a markdown file and returns the report content along with execution metrics.
    *   **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
    *   **Description:** This function orchestrates a comprehensive workflow to analyze Jupyter notebooks from a specified GitHub repository. It begins by extracting the repository URL from the input, cloning the repository, and then converting the notebooks into a structured XML format, handling embedded images. Concurrently, it extracts basic project information from the repository files. The function then utilizes a configured Large Language Model (LLM) to generate individual reports for each processed notebook, concatenating them into a final report. It saves this report to a markdown file and returns the report content along with execution metrics.
    *   **Parameters:**
        - **input** (`str`): The input string, which is expected to contain a GitHub repository URL from which notebooks will be processed.
        - **api_keys** (`dict`): A dictionary containing API keys for various Large Language Model services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama') used for report generation.
        - **model** (`str`): The name of the specific Large Language Model to be used for generating the notebook reports (e.g., 'gpt-4', 'gemini-pro').
        - **status_callback** (`callable | None`): An optional callback function that receives status messages, allowing for real-time progress updates during the workflow execution.
    *   **Returns:**
        - `report` (`str`): The final concatenated markdown report generated by the LLM, summarizing the analysis of all processed notebooks.
        - `metrics` (`dict`): A dictionary containing various execution metrics, including 'helper_time', 'main_time', 'total_time', 'helper_model', 'main_model', 'json_tokens', 'toon_tokens', and 'savings_percent'.
    *   **Usage:** This function calls no other functions.

    #### Function: `gemini_payload`
    *   **Summary:** This function constructs a multi-part payload suitable for the Gemini API, integrating textual context with embedded images. It begins by serializing basic information and a notebook path into an initial JSON text block. The core logic involves parsing an XML-like content string for image placeholders using regular expressions. For each detected placeholder, it extracts the corresponding image data from a provided list, converts it to a base64 URL, and adds it to the payload. Any text segments found between or around these image placeholders are included as separate text entries, resulting in a structured list of content parts.
    *   **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
    *   **Description:** This function constructs a multi-part payload suitable for the Gemini API, integrating textual context with embedded images. It begins by serializing basic information and a notebook path into an initial JSON text block. The core logic involves parsing an XML-like content string for image placeholders using regular expressions. For each detected placeholder, it extracts the corresponding image data from a provided list, converts it to a base64 URL, and adds it to the payload. Any text segments found between or around these image placeholders are included as separate text entries, resulting in a structured list of content parts.
    *   **Parameters:**
        - **basic_info** (`dict`): A dictionary containing basic information to be included as a JSON string in the payload's initial context.
        - **nb_path** (`str`): The string path of the current notebook, which is included as part of the initial JSON context.
        - **xml_content** (`str`): A string containing XML-like content that may include <IMAGE_PLACEHOLDER/> tags, which are parsed to embed images.
        - **images** (`list[dict]`): A list of dictionaries, where each dictionary contains image data (e.g., a base64 string under the 'data' key) corresponding to the image placeholders in `xml_content`.
    *   **Returns:** `payload_content` (`list[dict]`): A list of dictionaries, each representing a content part (either 'text' or 'image_url') formatted for a Gemini API request.
    *   **Usage:** This function calls no other functions.

    ### File: `backend/relationship_analyzer.py`

    #### Function: `path_to_module`
    *   **Summary:** This function converts a given file path into a Python module path string. It first calculates the relative path of the file with respect to a specified project root, falling back to the file's base name if a `ValueError` occurs. It then removes the '.py' extension if present, replaces path separators with dots, and specifically handles `__init__.py` files by removing the '.__init__' suffix to yield the package name.
    *   **Signature:** `def path_to_module(filepath, project_root)`
    *   **Description:** This function converts a given file path into a Python module path string. It first calculates the relative path of the file with respect to a specified project root, falling back to the file's base name if a `ValueError` occurs. It then removes the '.py' extension if present, replaces path separators with dots, and specifically handles `__init__.py` files by removing the '.__init__' suffix to yield the package name.
    *   **Parameters:**
        - **filepath** (`str`): The absolute or relative path to a Python file.
        - **project_root** (`str`): The root directory of the project, used to determine the relative path.
    *   **Returns:** `module_path` (`str`): The Python module path string derived from the input file path.
    *   **Usage:** This function calls no other functions.

    #### Class: `ProjectAnalyzer`
    *   **Summary:** The ProjectAnalyzer class is designed to perform static analysis on a Python project to build a comprehensive call graph. It identifies all Python files within a specified root directory, collects definitions of classes, functions, and methods, and then resolves calls between these defined entities. The class provides methods to initiate the analysis, retrieve the raw call graph, and present relationships in a structured format, effectively mapping out the functional dependencies within a codebase.
    *   **Instantiation:** This class is not explicitly instantiated by other components within the provided context.
    *   **Dependencies:** This class does not explicitly declare external dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method initializes the ProjectAnalyzer instance by setting up the project's root directory, converting it to an absolute path. It also initializes various internal data structures such as 'definitions' (to store collected definitions), 'call_graph' (to store call relationships), and 'file_asts' (to cache ASTs). Additionally, it defines a set of common directories to ignore during file traversal.
        *   *Parameters:*
            - **project_root** (`str`): The root directory of the project to be analyzed.
    *   **Methods:**
        *   **`analyze`**
            *   *Signature:* `def analyze(self)`
            *   *Description:* This method orchestrates the entire project analysis process. It first identifies all Python files within the project by calling an internal helper. Subsequently, it iterates through these files twice: once to collect all definitions of functions, classes, and methods, and then again to resolve calls made within these files, building a comprehensive call graph. Finally, it clears the cached file ASTs before returning the generated call graph.
            *   *Parameters:* None
            *   *Returns:* `call_graph` (`defaultdict[list]`): A dictionary representing the call graph, where keys are callee identifiers and values are lists of caller information.
            *   **Usage:** This method does not explicitly call other methods or functions within the provided context.
        *   **`get_raw_relationships`**
            *   *Signature:* `def get_raw_relationships(self)`
            *   *Description:* This method processes the internal 'call_graph' to generate structured outgoing and incoming relationship dictionaries. It iterates through the call graph, extracting caller and callee identifiers from each entry. Based on these, it populates 'outgoing' and 'incoming' dictionaries, which are then returned with their values sorted for consistent output.
            *   *Parameters:* None
            *   *Returns:* `relationships` (`dict`): A dictionary containing 'outgoing' and 'incoming' call relationships, where keys are identifiers and values are sorted lists of related identifiers.
            *   **Usage:** This method does not explicitly call other methods or functions within the provided context.
        *   **`_find_py_files`**
            *   *Signature:* `def _find_py_files(self)`
            *   *Description:* This private helper method traverses the project directory, starting from 'self.project_root', to locate all Python files. It utilizes 'os.walk' to navigate the file system, filtering out directories specified in 'self.ignore_dirs' to avoid analyzing irrelevant paths. The method compiles and returns a list of absolute file paths for all discovered Python files.
            *   *Parameters:* None
            *   *Returns:* `py_files` (`list[str]`): A list of absolute file paths to all Python files found in the project, excluding ignored directories.
            *   **Usage:** This method does not explicitly call other methods or functions within the provided context.
        *   **`_collect_definitions`**
            *   *Signature:* `def _collect_definitions(self, filepath)`
            *   *Description:* This private method is responsible for parsing a given Python file and collecting definitions of functions, methods, and classes. It reads the file, parses its Abstract Syntax Tree (AST), and stores the AST in 'self.file_asts'. It then walks the AST to identify 'FunctionDef' and 'ClassDef' nodes, constructing unique path names for each definition and storing them in 'self.definitions' along with their file path, line number, and type. Error handling is included for file processing and AST parsing.
            *   *Parameters:*
                - **filepath** (`str`): The absolute path to the Python file being analyzed.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods or functions within the provided context.
        *   **`_get_parent`**
            *   *Signature:* `def _get_parent(self, tree, node)`
            *   *Description:* This private helper method iterates through the nodes of an Abstract Syntax Tree (AST) to find the immediate parent of a given node. It walks the entire tree and for each potential parent node, it checks its children to see if any child matches the target node. If a match is found, the parent node is returned. If no parent is found (e.g., for the root node), it returns None.
            *   *Parameters:*
                - **tree** (`ast.AST`): The Abstract Syntax Tree to search within.
                - **node** (`ast.AST`): The child AST node for which to find the parent.
            *   *Returns:* `parent_node` (`ast.AST | None`): The parent AST node of the given node, or None if no parent is found.
            *   **Usage:** This method does not explicitly call other methods or functions within the provided context.
        *   **`_resolve_calls`**
            *   *Signature:* `def _resolve_calls(self, filepath)`
            *   *Description:* This private method processes a given file's AST to identify and resolve function and method calls. It retrieves the AST from 'self.file_asts' and, if available, instantiates a 'CallResolverVisitor' to traverse the tree and collect call information. The resolved calls, including callee pathnames and caller details, are then extended into the 'self.call_graph'. Error handling is included for the call resolution process.
            *   *Parameters:*
                - **filepath** (`str`): The path to the Python file whose calls are to be resolved.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other methods or functions within the provided context.

    #### Class: `CallResolverVisitor`
    *   **Summary:** The CallResolverVisitor class extends `ast.NodeVisitor` to traverse an Abstract Syntax Tree (AST) and identify call relationships within Python code. It resolves fully qualified names for functions, methods, and class instantiations, tracking the current scope and caller context. The visitor collects information about which functions or methods call others, storing this data for further analysis of code relationships.
    *   **Instantiation:** This class is not explicitly instantiated by other components based on the provided context.
    *   **Dependencies:** This class does not explicitly depend on other components based on the provided context.
    *   **Constructor:**
        *   *Description:* The constructor initializes the visitor with the file path, project root, and a dictionary of known definitions. It sets up internal state variables such as `module_path`, `scope` for name resolution, `instance_types` for tracking object types, and `calls` to store the detected call relationships.
        *   *Parameters:*
            - **filepath** (`str`): The path to the source file being analyzed.
            - **project_root** (`str`): The root directory of the project, used to determine module paths.
            - **definitions** (`dict`): A dictionary containing known definitions (e.g., functions, classes) for resolution.
    *   **Methods:**
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* This method is invoked when the AST visitor encounters a class definition (`ast.ClassDef`). It updates the `current_class_name` attribute to reflect the class being visited, which is essential for nested methods to correctly form their fully qualified names. After processing the class's children, it restores the previous `current_class_name` to maintain correct scope.
            *   *Parameters:*
                - **node** (`ast.ClassDef`): The AST node representing the class definition.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other functions or methods based on the provided context.
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* This method is called when the AST visitor encounters a function definition (`ast.FunctionDef`). It updates the `current_caller_name` to the fully qualified name of the function or method being visited. This ensures that any calls made within this function are correctly attributed to it. The previous caller name is restored after the function's body has been processed.
            *   *Parameters:*
                - **node** (`ast.FunctionDef`): The AST node representing the function definition.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other functions or methods based on the provided context.
        *   **`visit_Call`**
            *   *Signature:* `def visit_Call(self, node)`
            *   *Description:* This method processes function or method call expressions (`ast.Call`). It attempts to resolve the fully qualified name of the callee using `_resolve_call_qname`. If the callee is successfully resolved and found in the known definitions, it records the caller's information, including its file, line number, full identifier, and type (module, local function, method, or function), into the `calls` dictionary.
            *   *Parameters:*
                - **node** (`ast.Call`): The AST node representing the call expression.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other functions or methods based on the provided context.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* This method handles `import` statements (`ast.Import`). It iterates through the imported names and adds them to the visitor's `scope` dictionary. The `scope` maps the alias (or original name) to the full module path, which is crucial for resolving qualified names later during call analysis.
            *   *Parameters:*
                - **node** (`ast.Import`): The AST node representing the import statement.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other functions or methods based on the provided context.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* This method processes `from ... import ...` statements (`ast.ImportFrom`). It determines the full module path for the imported names, considering relative imports (`node.level`). Each imported name (or its alias) is then added to the `scope` dictionary, mapping it to its fully qualified path for subsequent name resolution.
            *   *Parameters:*
                - **node** (`ast.ImportFrom`): The AST node representing the 'from ... import ...' statement.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other functions or methods based on the provided context.
        *   **`visit_Assign`**
            *   *Signature:* `def visit_Assign(self, node)`
            *   *Description:* This method is triggered by assignment statements (`ast.Assign`). Specifically, it looks for assignments where the right-hand side is a call to a class constructor (e.g., `x = MyClass()`). If such an assignment is found and the class name is resolvable, it records the qualified class name in `instance_types`, mapping the assigned variable's name to its class type.
            *   *Parameters:*
                - **node** (`ast.Assign`): The AST node representing the assignment statement.
            *   *Returns:* None
            *   **Usage:** This method does not explicitly call other functions or methods based on the provided context.
        *   **`_resolve_call_qname`**
            *   *Signature:* `def _resolve_call_qname(self, func_node)`
            *   *Description:* This private helper method attempts to resolve the fully qualified name (QName) of a function or method being called. It handles two main cases: direct name calls (e.g., `func()`) by checking the current scope and local path, and attribute calls (e.g., `obj.method()`) by looking up the instance type or module in the scope. It returns the resolved QName as a string or `None` if it cannot be resolved.
            *   *Parameters:*
                - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., ast.Name or ast.Attribute).
            *   *Returns:* `callee_qname` (`str | None`): The fully qualified name of the callee, or None if it cannot be resolved.
            *   **Usage:** This method does not explicitly call other functions or methods based on the provided context.

    ### File: `schemas/types.py`

    #### Class: `ParameterDescription`
    *   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to structure information about a single parameter of a function. It serves as a data model to consistently represent a parameter's name, its type, and a descriptive explanation of its purpose. This class is primarily used for documentation generation or static analysis where structured parameter data is required.
    *   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* This class, being a Pydantic BaseModel, automatically generates an `__init__` method. It initializes an instance by accepting `name`, `type`, and `description` as arguments, which are then validated and stored as instance attributes.
        *   *Parameters:*
            - **name** (`str`): The name of the parameter.
            - **type** (`str`): The type hint or inferred type of the parameter.
            - **description** (`str`): A brief explanation of the parameter's purpose.
    *   **Methods:** None

    #### Class: `ReturnDescription`
    *   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to structure information about a function's return value. It serves as a data container, ensuring that return value descriptions consistently include a name, type, and a detailed explanation. This class is fundamental for standardizing how function outputs are documented and understood within the system.
    *   **Instantiation:** "The instantiation points for this class are not explicitly provided in the current context, but it is typically instantiated when describing the return values of functions or methods within a larger schema definition."
    *   **Dependencies:** This class primarily depends on `pydantic.BaseModel` for its structural definition and data validation capabilities.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ReturnDescription` is automatically generated by Pydantic's BaseModel. It initializes an instance of `ReturnDescription` by accepting `name`, `type`, and `description` as keyword arguments, validating them against their respective string types as defined in the class attributes.
        *   *Parameters:*
            - **name** (`str`): The name or label for the return value.
            - **type** (`str`): The data type of the return value, e.g., 'str', 'int', 'List[str]'.
            - **description** (`str`): A detailed explanation of what the return value represents or contains.
    *   **Methods:** None

    #### Class: `UsageContext`
    *   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts with other parts of a system. It provides a structured way to describe what an entity calls and where it is called from. This class serves as a data model for representing the operational context of a code component, facilitating clear and consistent documentation of inter-component relationships.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class relies on `pydantic.BaseModel` for its data model capabilities. No other explicit external dependencies are listed in the provided context.
    *   **Constructor:**
        *   *Description:* "This class does not explicitly define an `__init__` method. As a Pydantic `BaseModel`, it automatically generates a constructor that initializes its fields, `calls` and `called_by`, based on the arguments provided during instantiation."
        *   *Parameters:*
            - **calls** (`str`): A string summarizing the functions, methods, or classes that this entity calls within its execution.
            - **called_by** (`str`): A string summarizing the functions, methods, or contexts from which this entity is invoked.
    *   **Methods:** None

    #### Class: `FunctionDescription`
    *   **Summary:** The FunctionDescription class is a Pydantic BaseModel designed to provide a structured and comprehensive analysis of a Python function. It serves as a data model to encapsulate various aspects of a function, including its high-level purpose, detailed descriptions of its input parameters, specifications of its return values, and information regarding its usage context within a larger system. This class facilitates the standardized representation and validation of function metadata.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for FunctionDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance of FunctionDescription by validating and assigning values to its fields: `overall`, `parameters`, `returns`, and `usage_context`. This ensures that all function descriptions conform to the defined schema and type hints.
        *   *Parameters:*
            - **overall** (`str`): A string providing a high-level summary of the function's purpose and functionality.
            - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing an input parameter of the function.
            - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects, each describing a value returned by the function.
            - **usage_context** (`UsageContext`): An object containing information about where and how the function is used or called.
    *   **Methods:** None

    #### Class: `FunctionAnalysis`
    *   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a single Python function. It serves as a structured data container, holding the function's unique identifier, a detailed description object, and an optional field for error messages. This model is crucial for standardizing the representation of function analysis results within a larger system, ensuring consistency and ease of data exchange.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The FunctionAnalysis class does not explicitly define an `__init__` method. As a Pydantic BaseModel, its initialization is handled automatically by Pydantic, which validates and assigns values to its fields (`identifier`, `description`, `error`) based on the arguments provided during object creation.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifier for the function being analyzed.
            - **description** (`FunctionDescription`): An object containing a detailed description of the function, including its purpose, parameters, returns, and usage context.
            - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the function's analysis. Defaults to None.
    *   **Methods:** None

    #### Class: `ConstructorDescription`
    *   **Summary:** The `ConstructorDescription` class is a Pydantic BaseModel designed to structure and describe the `__init__` method of a Python class. It serves as a data schema for capturing essential information about a constructor, including a textual summary of its behavior and a detailed list of its parameters. This model is crucial for systems that analyze or generate documentation for class constructors, providing a standardized format for their representation.
    *   **Instantiation:** "The specific instantiation points for this class are not provided in the current context, but it is typically instantiated when structured data about a class's constructor needs to be represented or processed."
    *   **Dependencies:** This class relies on `pydantic.BaseModel` for its data modeling capabilities and `typing.List` for type hinting its list of parameters. It does not explicitly list any other external functional dependencies.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ConstructorDescription` is implicitly generated by Pydantic. It handles the validation and assignment of the `description` string and the `parameters` list (which contains `ParameterDescription` objects) when an instance of `ConstructorDescription` is created. This ensures that all constructor descriptions conform to the defined schema.
        *   *Parameters:*
            - **description** (`str`): A string providing a summary or explanation of the constructor's purpose and behavior.
            - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing a parameter accepted by the constructor.
    *   **Methods:** None

    #### Class: `ClassContext`
    *   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's external interactions. It specifically stores information regarding the class's dependencies and where it is instantiated within a larger system. This model provides a structured way to represent contextual information for class analysis.
    *   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
    *   **Dependencies:** This class does not explicitly declare external dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* "As a Pydantic BaseModel, the __init__ method for ClassContext is automatically generated. It handles the validation and assignment of the `dependencies` and `instantiated_by` string fields upon instantiation, ensuring type correctness."
        *   *Parameters:*
            - **dependencies** (`str`): A string summarizing the external dependencies of the class.
            - **instantiated_by** (`str`): A string summarizing where the class is instantiated.
    *   **Methods:** None

    #### Class: `ClassDescription`
    *   **Summary:** The ClassDescription class is a Pydantic BaseModel that serves as a structured schema for representing a comprehensive analysis of a Python class. It aggregates information about a class's high-level purpose, its constructor, a list of its individual methods, and its external usage context. This model is crucial for organizing and validating the output of a class analysis process, ensuring consistency and completeness in the generated documentation.
    *   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* "This class is a Pydantic BaseModel, so its constructor is automatically generated by Pydantic. It initializes instances by validating and assigning values to its defined fields: overall, init_method, methods, and usage_context."
        *   *Parameters:*
            - **overall** (`str`): A string describing the overall purpose and functionality of the class being analyzed.
            - **init_method** (`ConstructorDescription`): An object containing the detailed description and parameters of the class's constructor (__init__ method).
            - **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each providing a detailed description of a method within the class being analyzed.
            - **usage_context** (`ClassContext`): An object containing information about the class's external dependencies and where it is instantiated within the codebase.
    *   **Methods:** None

    #### Class: `ClassAnalysis`
    *   **Summary:** The `ClassAnalysis` class is a Pydantic BaseModel designed to serve as the main schema for a comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed `ClassDescription` object containing its constructor and method analyses, and an optional `error` field to report issues during analysis. This model provides a structured format for representing the output of a class analysis process.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
    *   **Dependencies:** This class does not explicitly list any external dependencies within its definition.
    *   **Constructor:**
        *   *Description:* The `ClassAnalysis` class does not explicitly define an `__init__` method. It inherits from Pydantic's `BaseModel`, meaning its constructor is implicitly handled by Pydantic. It initializes the instance attributes `identifier`, `description`, and `error` based on the arguments passed during object creation, performing validation according to their type hints.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifier for the class being analyzed.
            - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
            - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the class analysis. Defaults to None.
    *   **Methods:** None

    #### Class: `CallInfo`
    *   **Summary:** The CallInfo class is a Pydantic BaseModel designed to encapsulate details about a specific call event within a software system. It acts as a structured data container, defining the essential attributes required to identify and describe where a function, method, or module call originates. This model is intended for use in tracking and analyzing relationships between different parts of a codebase, particularly in contexts like 'called_by' and 'instantiated_by' lists.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the context.
    *   **Dependencies:** This class does not explicitly list external functional dependencies in its context.
    *   **Constructor:**
        *   *Description:* "As a Pydantic BaseModel, CallInfo's constructor is implicitly generated. It handles the validation and assignment of the provided arguments (file, function, mode, line) to corresponding instance attributes, ensuring data integrity according to their defined types."
        *   *Parameters:*
            - **file** (`str`): The path to the file where the call event is recorded.
            - **function** (`str`): The name of the function or method that performed the call.
            - **mode** (`str`): The classification of the call, e.g., 'method', 'function', or 'module'.
            - **line** (`int`): The line number within the file where the call occurred.
    *   **Methods:** None

    #### Class: `FunctionContextInput`
    *   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to provide a structured representation of a function's operational context. It serves as a data container, holding information about other functions, methods, or classes that the analyzed function calls, as well as details about where the analyzed function itself is invoked. This class is fundamental for analyzing and understanding the interaction patterns of a specific function within a larger codebase.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
    *   **Dependencies:** "This class primarily depends on Pydantic's BaseModel for its structure and validation, and `typing.List` for type hinting. It also depends on the `CallInfo` type, which is not defined within this snippet."
    *   **Constructor:**
        *   *Description:* "The `__init__` method for FunctionContextInput is implicitly generated by Pydantic, as it inherits from BaseModel. It initializes the instance attributes `calls` and `called_by` based on the arguments provided during object creation, ensuring type validation according to their annotations."
        *   *Parameters:*
            - **calls** (`List[str]`): A list of strings, where each string represents the identifier of a function, method, or class that the subject function calls.
            - **called_by** (`List[CallInfo]`): A list of CallInfo objects, each providing details about a specific caller of the subject function.
    *   **Methods:** None

    #### Class: `FunctionAnalysisInput`
    *   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for performing a function analysis. It acts as a data transfer object, ensuring that all necessary components like the function's identifier, source code, relevant imports, and contextual information are provided in a consistent format. This class serves as a contract for the data expected by a function analysis process.
    *   **Instantiation:** There is no explicit information provided on where this class is instantiated within the given context.
    *   **Dependencies:** "This class does not explicitly list any external functional dependencies. It relies on Pydantic's BaseModel for its core functionality."
    *   **Constructor:**
        *   *Description:* "This class, being a Pydantic BaseModel, implicitly generates an `__init__` method. This constructor is responsible for validating and assigning the provided arguments to the class's fields, ensuring they conform to the specified types and constraints (e.g., `Literal` for `mode`). The fields defined in the class act as the parameters for its initialization."
        *   *Parameters:*
            - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, which is fixed to 'function_analysis' for this input type.
            - **identifier** (`str`): The unique name or identifier of the function that is to be analyzed.
            - **source_code** (`str`): The raw source code string of the function targeted for analysis.
            - **imports** (`List[str]`): A list of import statements that are relevant to the function's execution context.
            - **context** (`FunctionContextInput`): Additional contextual information, structured as a FunctionContextInput object, necessary for the analysis.
    *   **Methods:** None

    #### Class: `MethodContextInput`
    *   **Summary:** The MethodContextInput class is a Pydantic BaseModel designed to provide a structured schema for capturing comprehensive contextual information about a specific method. It defines fields such as the method's unique identifier, a list of entities it calls, a list of entities that call it, its arguments, and its docstring. This class serves as a data transfer object, ensuring consistent data representation for method analysis within a larger system.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
    *   **Dependencies:** "This class primarily depends on pydantic.BaseModel for its data modeling capabilities and typing.List and typing.Optional for type hinting. It also implicitly depends on a CallInfo type, which is not defined within this source code."
    *   **Constructor:**
        *   *Description:* "This class does not explicitly define an __init__ method. It inherits from pydantic.BaseModel, and its initialization is handled implicitly by Pydantic, which validates and assigns values to its fields upon instantiation."
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifying the method.
            - **calls** (`List[str]`): A list of strings representing other methods, classes, or functions called by this method.
            - **called_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this method is called from.
            - **args** (`List[str]`): A list of strings representing the arguments of the method.
            - **docstring** (`Optional[str]`): An optional string containing the method's docstring.
    *   **Methods:** None

    #### Class: `ClassContextInput`
    *   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured context information for analyzing a Python class. It serves as a data container, holding lists of external dependencies, points where the class is instantiated, and detailed context for each method within the class. This model facilitates the organized transfer of comprehensive contextual data for further processing or analysis.
    *   **Instantiation:** The instantiation points for this class are not specified in the provided context.
    *   **Dependencies:** This class does not explicitly declare external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* "This class, being a Pydantic BaseModel, initializes its attributes automatically based on the provided arguments during instantiation. It does not have an explicit __init__ method defined, relying on Pydantic's data validation and assignment mechanisms to set up its state."
        *   *Parameters:*
            - **dependencies** (`List[str]`): A list of strings representing external functional dependencies of the class.
            - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects, detailing where this class is instantiated within the codebase.
            - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing specific context for a method belonging to the class.
    *   **Methods:** None

    #### Class: `ClassAnalysisInput`
    *   **Summary:** The ClassAnalysisInput class is a Pydantic model designed to define the structured input required for generating a ClassAnalysis object. It serves as a data transfer object, ensuring that all necessary components for class analysis, such as the class identifier, its source code, relevant imports, and contextual information, are provided in a consistent format. This model facilitates robust data validation and parsing for the class analysis process.
    *   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* "This class does not explicitly define an __init__ method. It inherits from pydantic.BaseModel, and its initialization is handled implicitly by Pydantic, which validates and assigns values to its fields upon instantiation."
        *   *Parameters:*
            - **mode** (`Literal["class_analysis"]`): Specifies the analysis mode, fixed to 'class_analysis'.
            - **identifier** (`str`): The unique identifier for the class to be analyzed.
            - **source_code** (`str`): The raw source code of the class.
            - **imports** (`List[str]`): A list of import statements relevant to the class.
            - **context** (`ClassContextInput`): The contextual information for the class, provided as a ClassContextInput object.
    *   **Methods:** None

    ### File: `database/db.py`

    #### Function: `encrypt_text`
    *   **Summary:** This function encrypts a given text string using a `cipher_suite` object. It first checks if the input text or the `cipher_suite` itself is falsy; if so, it returns the original text without encryption. Otherwise, it prepares the text by stripping leading/trailing whitespace and encoding it to bytes, then encrypts it using `cipher_suite.encrypt`. Finally, the encrypted bytes are decoded back into a string before being returned.
    *   **Signature:** `def encrypt_text(text: str) -> str`
    *   **Description:** This function encrypts a given text string using a `cipher_suite` object. It first checks if the input text or the `cipher_suite` itself is falsy; if so, it returns the original text without encryption. Otherwise, it prepares the text by stripping leading/trailing whitespace and encoding it to bytes, then encrypts it using `cipher_suite.encrypt`. Finally, the encrypted bytes are decoded back into a string before being returned.
    *   **Parameters:**
        - **text** (`str`): The string to be encrypted.
    *   **Returns:** `encrypted_text` (`str`): The encrypted string, or the original string if encryption was skipped due to missing text or cipher_suite.
    *   **Usage:** This function calls no other functions.

    #### Function: `decrypt_text`
    *   **Summary:** This function attempts to decrypt a given string using an external `cipher_suite` object. It first performs a preliminary check, returning the original text if the input string is empty or if the `cipher_suite` is not initialized. If decryption proceeds, the input text is stripped of whitespace, encoded to bytes, passed to the `cipher_suite` for decryption, and then decoded back into a string. The function includes error handling, returning the original text if any exception occurs during the decryption process.
    *   **Signature:** `def decrypt_text(text: str) -> str`
    *   **Description:** This function attempts to decrypt a given string using an external `cipher_suite` object. It first performs a preliminary check, returning the original text if the input string is empty or if the `cipher_suite` is not initialized. If decryption proceeds, the input text is stripped of whitespace, encoded to bytes, passed to the `cipher_suite` for decryption, and then decoded back into a string. The function includes error handling, returning the original text if any exception occurs during the decryption process.
    *   **Parameters:**
        - **text** (`str`): The string value to be decrypted.
    *   **Returns:** `decrypted_text` (`str`): The decrypted string if successful, or the original string if decryption is skipped or an error occurs.
    *   **Usage:** This function calls no other functions.

    #### Function: `insert_user`
    *   **Summary:** This function is designed to create a new user record and store it in a database. It accepts a username, a display name, and a plain-text password. The provided password is first hashed using `stauth.Hasher.hash` for security before being stored. A user dictionary is constructed, including the hashed password and default empty strings for various API keys. Finally, the function inserts this user dictionary into the `dbusers` collection and returns the unique identifier assigned to the new document by the database.
    *   **Signature:** `def insert_user(username: str, name: str, password: str)`
    *   **Description:** This function is designed to create a new user record and store it in a database. It accepts a username, a display name, and a plain-text password. The provided password is first hashed using `stauth.Hasher.hash` for security before being stored. A user dictionary is constructed, including the hashed password and default empty strings for various API keys. Finally, the function inserts this user dictionary into the `dbusers` collection and returns the unique identifier assigned to the new document by the database.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user.
        - **name** (`str`): The display name of the user.
        - **password** (`str`): The plain-text password for the user, which will be hashed before storage.
    *   **Returns:** `inserted_id` (`Any`): The unique identifier assigned by the database to the newly inserted user document.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_all_users`
    *   **Summary:** The `fetch_all_users` function is designed to retrieve all user records from a database collection named `dbusers`. It executes a `find()` operation on this collection, which typically returns a cursor containing all documents. This cursor is then immediately converted into a standard Python list, effectively providing all user data as a collection of dictionaries or objects.
    *   **Signature:** `def fetch_all_users():`
    *   **Description:** The `fetch_all_users` function is designed to retrieve all user records from a database collection named `dbusers`. It executes a `find()` operation on this collection, which typically returns a cursor containing all documents. This cursor is then immediately converted into a standard Python list, effectively providing all user data as a collection of dictionaries or objects.
    *   **Parameters:** None
    *   **Returns:** `users` (`list`): A list of all user documents retrieved from the 'dbusers' collection.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_user`
    *   **Summary:** The `fetch_user` function is designed to retrieve a single user record from a database collection, presumably named `dbusers`. It takes a username as input and uses it to query the database for a document where the `_id` field matches the provided username. The function directly returns the result of this database lookup operation.
    *   **Signature:** `def fetch_user(username: str):`
    *   **Description:** The `fetch_user` function is designed to retrieve a single user record from a database collection, presumably named `dbusers`. It takes a username as input and uses it to query the database for a document where the `_id` field matches the provided username. The function directly returns the result of this database lookup operation.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user to be fetched, which is used to match the `_id` field in the database.
    *   **Returns:** `user_document` (`dict` or None): A dictionary representing the user document found in the `dbusers` collection, or `None` if no user with the specified username is found.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_user_name`
    *   **Summary:** This function is designed to update a user's name in a database. It takes an existing username, which serves as the unique identifier (_id), and a new name to be assigned. The function utilizes a database collection, presumably `dbusers`, to perform an `update_one` operation, setting the 'name' field for the specified user. It returns the count of documents that were successfully modified by the operation.
    *   **Signature:** `def update_user_name(username: str, new_name: str)`
    *   **Description:** This function is designed to update a user's name in a database. It takes an existing username, which serves as the unique identifier (_id), and a new name to be assigned. The function utilizes a database collection, presumably `dbusers`, to perform an `update_one` operation, setting the 'name' field for the specified user. It returns the count of documents that were successfully modified by the operation.
    *   **Parameters:**
        - **username** (`str`): The unique identifier (_id) of the user whose name is to be updated.
        - **new_name** (`str`): The new name to assign to the specified user.
    *   **Returns:** `modified_count` (`int`): The number of documents that were modified by the update operation.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_gemini_key`
    *   **Summary:** This function updates a user's Gemini API key in the database. It takes a username and the new Gemini API key as input. The API key is first stripped of leading/trailing whitespace and then encrypted. The function then updates the 'gemini_api_key' field for the specified user in the 'dbusers' collection with the encrypted key. It returns the count of modified documents.
    *   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
    *   **Description:** This function updates a user's Gemini API key in the database. It takes a username and the new Gemini API key as input. The API key is first stripped of leading/trailing whitespace and then encrypted. The function then updates the 'gemini_api_key' field for the specified user in the 'dbusers' collection with the encrypted key. It returns the count of modified documents.
    *   **Parameters:**
        - **username** (`str`): The username of the user whose Gemini API key is to be updated.
        - **gemini_api_key** (`str`): The new Gemini API key to be stored for the user. It will be stripped of whitespace and encrypted before storage.
    *   **Returns:** `modified_count` (`int`): The number of documents modified by the update operation, typically 1 if the user was found and updated, or 0 otherwise.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_gpt_key`
    *   **Summary:** This function updates a user's GPT API key in the database. It first encrypts the provided API key, ensuring any leading or trailing whitespace is removed. Then, it uses the `dbusers` collection to find the user by their username and sets their `gpt_api_key` field to the newly encrypted value. The function returns the number of documents that were modified by this operation.
    *   **Signature:** `def update_gpt_key(username: str, gpt_api_key: str)`
    *   **Description:** This function updates a user's GPT API key in the database. It first encrypts the provided API key, ensuring any leading or trailing whitespace is removed. Then, it uses the `dbusers` collection to find the user by their username and sets their `gpt_api_key` field to the newly encrypted value. The function returns the number of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (`str`): The username of the user whose GPT API key is to be updated.
        - **gpt_api_key** (`str`): The new GPT API key to be stored for the user. This key will be encrypted before storage.
    *   **Returns:** `modified_count` (`int`): The number of documents modified by the update operation.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_ollama_url`
    *   **Summary:** This function updates the Ollama base URL for a specific user in the database. It takes a username and a new Ollama base URL as input. The function uses the `dbusers` collection to find a document matching the provided username and updates its `ollama_base_url` field. The provided URL is stripped of leading/trailing whitespace before being stored. It returns the count of documents that were modified by this operation.
    *   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
    *   **Description:** This function updates the Ollama base URL for a specific user in the database. It takes a username and a new Ollama base URL as input. The function uses the `dbusers` collection to find a document matching the provided username and updates its `ollama_base_url` field. The provided URL is stripped of leading/trailing whitespace before being stored. It returns the count of documents that were modified by this operation.
    *   **Parameters:**
        - **username** (`str`): The unique identifier (username) of the user whose Ollama URL is to be updated.
        - **ollama_base_url** (`str`): The new base URL for Ollama, which will be stored after stripping whitespace.
    *   **Returns:** `modified_count` (`int`): The number of documents that were modified by the update operation. Typically 0 or 1.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_opensrc_key`
    *   **Summary:** This function updates a user's Open Source API key in the database. It takes a username and the new API key as input. The provided API key is first stripped of whitespace and then encrypted before being stored. The function then updates the 'opensrc_api_key' field for the specified user in the 'dbusers' collection. It returns the count of documents that were modified by this update operation.
    *   **Signature:** `def update_opensrc_key(username: str, opensrc_api_key: str)`
    *   **Description:** This function updates a user's Open Source API key in the database. It takes a username and the new API key as input. The provided API key is first stripped of whitespace and then encrypted before being stored. The function then updates the 'opensrc_api_key' field for the specified user in the 'dbusers' collection. It returns the count of documents that were modified by this update operation.
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose Open Source API key is to be updated.
        - **opensrc_api_key** (`str`): The new Open Source API key to be encrypted and stored for the user.
    *   **Returns:** `modified_count` (`int`): The number of documents modified by the update operation.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_opensrc_url`
    *   **Summary:** "This function updates the 'opensrc_base_url' field for a specific user in a database collection. It takes a username and a new opensrc base URL as input. The username is used to identify the target user record, and the provided URL is stripped of leading/trailing whitespace before being stored. The function returns the count of documents that were modified by this operation."
    *   **Signature:** `def update_opensrc_url(username: str, opensrc_base_url: str)`
    *   **Description:** "This function updates the 'opensrc_base_url' field for a specific user in a database collection. It takes a username and a new opensrc base URL as input. The username is used to identify the target user record, and the provided URL is stripped of leading/trailing whitespace before being stored. The function returns the count of documents that were modified by this operation."
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose opensrc URL is to be updated.
        - **opensrc_base_url** (`str`): The new base URL for opensrc, which will be stored after stripping whitespace.
    *   **Returns:** `modified_count` (`int`): The number of documents that were modified by the update operation.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_gemini_key`
    *   **Summary:** "This function is designed to retrieve a user's Gemini API key from a database. It takes a username as input and queries the 'dbusers' collection to find a matching user document. The function specifically projects the 'gemini_api_key' field from the found document. If a user is found and the key exists, it returns the API key; otherwise, it returns None."
    *   **Signature:** `def fetch_gemini_key(username: str)`
    *   **Description:** "This function is designed to retrieve a user's Gemini API key from a database. It takes a username as input and queries the 'dbusers' collection to find a matching user document. The function specifically projects the 'gemini_api_key' field from the found document. If a user is found and the key exists, it returns the API key; otherwise, it returns None."
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose Gemini API key is to be fetched.
    *   **Returns:** `gemini_api_key` (`str` or None): The Gemini API key associated with the user, or None if the user is not found or the key is not present in the user's document.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_ollama_url`
    *   **Summary:** "This function retrieves the Ollama base URL associated with a specific user from a database. It queries the 'dbusers' collection using the provided username as the document's '_id'. The function specifically projects the 'ollama_base_url' field. If a user document is found, it extracts and returns the 'ollama_base_url'; otherwise, it returns None."
    *   **Signature:** `def fetch_ollama_url(username: str)`
    *   **Description:** "This function retrieves the Ollama base URL associated with a specific user from a database. It queries the 'dbusers' collection using the provided username as the document's '_id'. The function specifically projects the 'ollama_base_url' field. If a user document is found, it extracts and returns the 'ollama_base_url'; otherwise, it returns None."
    *   **Parameters:**
        - **username** (`str`): The unique identifier (username) for which to fetch the Ollama base URL.
    *   **Returns:** `ollama_base_url` (`str` or None): The Ollama base URL as a string if found, otherwise None.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_gpt_key`
    *   **Summary:** "This function retrieves the GPT API key associated with a given username from a database. It queries the `dbusers` collection, searching for a document where the `_id` matches the provided username. If a user document is found, it extracts the `gpt_api_key` field. The function returns the API key as a string if found, otherwise it returns `None`."
    *   **Signature:** `def fetch_gpt_key(username: str)`
    *   **Description:** "This function retrieves the GPT API key associated with a given username from a database. It queries the `dbusers` collection, searching for a document where the `_id` matches the provided username. If a user document is found, it extracts the `gpt_api_key` field. The function returns the API key as a string if found, otherwise it returns `None`."
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose GPT API key is to be fetched.
    *   **Returns:** `gpt_api_key` (`str` or None): The GPT API key for the specified user, or None if the user is not found or the key is not present.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_opensrc_key`
    *   **Summary:** "The `fetch_opensrc_key` function is designed to retrieve a user's Open Source API key from a database. It takes a username as input and queries the `dbusers` collection to find a document matching that username as its `_id`. The function specifically projects only the `opensrc_api_key` field. If a user is found, it returns the associated API key; otherwise, it returns `None`."
    *   **Signature:** `def fetch_opensrc_key(username: str)`
    *   **Description:** "The `fetch_opensrc_key` function is designed to retrieve a user's Open Source API key from a database. It takes a username as input and queries the `dbusers` collection to find a document matching that username as its `_id`. The function specifically projects only the `opensrc_api_key` field. If a user is found, it returns the associated API key; otherwise, it returns `None`."
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose Open Source API key is to be retrieved.
    *   **Returns:** `opensrc_api_key` (`str` or None): The Open Source API key associated with the specified username, or `None` if the user is not found or the key does not exist.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_opensrc_url`
    *   **Summary:** "This function is designed to retrieve the 'opensrc_base_url' for a specified user from a database. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided 'username'. The query is optimized to only return the 'opensrc_base_url' field. If a user document is found, the function extracts and returns the value of 'opensrc_base_url'. If no user is found or the 'opensrc_base_url' field is absent, the function returns None."
    *   **Signature:** `def fetch_opensrc_url(username: str)`
    *   **Description:** "This function is designed to retrieve the 'opensrc_base_url' for a specified user from a database. It queries the 'dbusers' collection, searching for a document where the '_id' field matches the provided 'username'. The query is optimized to only return the 'opensrc_base_url' field. If a user document is found, the function extracts and returns the value of 'opensrc_base_url'. If no user is found or the 'opensrc_base_url' field is absent, the function returns None."
    *   **Parameters:**
        - **username** (`str`): The unique identifier (username) of the user whose opensrc base URL is to be fetched.
    *   **Returns:** `opensrc_base_url` (`str` or None): The base URL for opensrc associated with the user, or None if the user is not found or the URL is not available.
    *   **Usage:** This function calls no other functions.

    #### Function: `delete_user`
    *   **Summary:** "This function is responsible for deleting a single user record from the database. It takes a username as input and uses it to locate and remove the corresponding document within the `dbusers` collection. The operation leverages a `delete_one` method, targeting the document where the `_id` field matches the provided username. The function then returns a count of the documents that were successfully deleted."
    *   **Signature:** `def delete_user(username: str)`
    *   **Description:** "This function is responsible for deleting a single user record from the database. It takes a username as input and uses it to locate and remove the corresponding document within the `dbusers` collection. The operation leverages a `delete_one` method, targeting the document where the `_id` field matches the provided username. The function then returns a count of the documents that were successfully deleted."
    *   **Parameters:**
        - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
    *   **Returns:** `deleted_count` (`int`): The number of documents deleted by the operation, typically 0 or 1.
    *   **Usage:** This function calls no other functions.

    #### Function: `get_decrypted_api_keys`
    *   **Summary:** "This function retrieves a user's API keys and associated URLs from a database, decrypting sensitive keys. It queries the 'dbusers' collection using the provided username. If a user is found, it extracts and decrypts the Gemini, GPT, and open-source API keys, and retrieves the Ollama and open-source base URLs. If no user is found, it returns two None values."
    *   **Signature:** `def get_decrypted_api_keys(username: str)`
    *   **Description:** "This function retrieves a user's API keys and associated URLs from a database, decrypting sensitive keys. It queries the 'dbusers' collection using the provided username. If a user is found, it extracts and decrypts the Gemini, GPT, and open-source API keys, and retrieves the Ollama and open-source base URLs. If no user is found, it returns two None values."
    *   **Parameters:**
        - **username** (`str`): The unique identifier for the user whose API keys are to be retrieved.
    *   **Returns:**
        - `gemini_plain` (`str`): The decrypted Gemini API key, or an empty string if not found.
        - `ollama_plain` (`str`): The Ollama base URL, or an empty string if not found.
        - `gpt_plain` (`str`): The decrypted GPT API key, or an empty string if not found.
        - `opensrc_plain` (`str`): The decrypted open-source API key, or an empty string if not found.
        - `opensrc_url` (`str`): The open-source base URL, or an empty string if not found.
    *   **Usage:** This function calls no other functions.

    #### Function: `insert_chat`
    *   **Summary:** "This function is responsible for creating a new chat entry within a database. It generates a unique identifier for the chat using `uuid.uuid4()` and records the current timestamp with `datetime.now()`. The function then constructs a chat document containing the provided username, chat name, the generated ID, and the creation timestamp. This document is subsequently inserted into the `dbchats` collection, and the unique ID of the newly inserted document is returned."
    *   **Signature:** `def insert_chat(username: str, chat_name: str)`
    *   **Description:** "This function is responsible for creating a new chat entry within a database. It generates a unique identifier for the chat using `uuid.uuid4()` and records the current timestamp with `datetime.now()`. The function then constructs a chat document containing the provided username, chat name, the generated ID, and the creation timestamp. This document is subsequently inserted into the `dbchats` collection, and the unique ID of the newly inserted document is returned."
    *   **Parameters:**
        - **username** (`str`): The username associated with the new chat entry.
        - **chat_name** (`str`): The name of the chat to be created.
    *   **Returns:** `inserted_id` (`str`): The unique identifier (_id) of the newly created chat document.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_chats_by_user`
    *   **Summary:** "This function, `fetch_chats_by_user`, is designed to retrieve all chat records associated with a given username from a database. It queries the `dbchats` collection, filtering documents by the provided `username`. The retrieved chat documents are then sorted in ascending order based on their 'created_at' timestamp. Finally, the function returns these sorted chat documents as a list."
    *   **Signature:** `def fetch_chats_by_user(username: str)`
    *   **Description:** "This function, `fetch_chats_by_user`, is designed to retrieve all chat records associated with a given username from a database. It queries the `dbchats` collection, filtering documents by the provided `username`. The retrieved chat documents are then sorted in ascending order based on their 'created_at' timestamp. Finally, the function returns these sorted chat documents as a list."
    *   **Parameters:**
        - **username** (`str`): The username for which to fetch the associated chat records.
    *   **Returns:** `chats` (`list[dict]`): A list of chat documents (dictionaries) belonging to the specified user, sorted by their creation date.
    *   **Usage:** This function calls no other functions.

    #### Function: `check_chat_exists`
    *   **Summary:** "This function, `check_chat_exists`, is designed to verify the existence of a specific chat within a database collection named `dbchats`. It takes a username and a chat name as input. The function queries the `dbchats` collection to find a document that matches both the provided username and chat name. It returns a boolean value indicating whether such a chat was found."
    *   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
    *   **Description:** "This function, `check_chat_exists`, is designed to verify the existence of a specific chat within a database collection named `dbchats`. It takes a username and a chat name as input. The function queries the `dbchats` collection to find a document that matches both the provided username and chat name. It returns a boolean value indicating whether such a chat was found."
    *   **Parameters:**
        - **username** (`str`): The username associated with the chat to be checked for existence.
        - **chat_name** (`str`): The name of the chat to be checked for existence.
    *   **Returns:** `exists` (`bool`): True if a chat matching the given username and chat name is found in the database, False otherwise.
    *   **Usage:** This function calls no other functions.

    #### Function: `rename_chat_fully`
    *   **Summary:** "This function renames a chat and all its associated exchanges within a database. It takes a username, the current chat name, and the new chat name as input. The function updates the 'chat_name' field from the 'old_name' to the 'new_name' for the specified user in both the 'dbchats' and 'dbexchanges' collections. It returns the count of chat entries that were modified."
    *   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
    *   **Description:** "This function renames a chat and all its associated exchanges within a database. It takes a username, the current chat name, and the new chat name as input. The function updates the 'chat_name' field from the 'old_name' to the 'new_name' for the specified user in both the 'dbchats' and 'dbexchanges' collections. It returns the count of chat entries that were modified."
    *   **Parameters:**
        - **username** (`str`): The username associated with the chat to be renamed.
        - **old_name** (`str`): The current name of the chat.
        - **new_name** (`str`): The new desired name for the chat.
    *   **Returns:** `modified_count` (`int`): The number of chat entries that were modified by the update operation.
    *   **Usage:** This function calls no other functions.

    #### Function: `insert_exchange`
    *   **Summary:** "This function is responsible for inserting a new exchange record into a database collection. It generates a unique identifier for the exchange, constructs a dictionary containing the provided question, answer, feedback, user, chat details, and various optional metrics like time and token usage. It also records the creation timestamp. The function then attempts to insert this record into the `dbexchanges` collection."
    *   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str="", main_used: str="", total_time: str="", helper_time: str="", main_time: str="", json_tokens=0, toon_tokens=0, savings_percent=0.0)`
    *   **Description:** "This function is responsible for inserting a new exchange record into a database collection. It generates a unique identifier for the exchange, constructs a dictionary containing the provided question, answer, feedback, user, chat details, and various optional metrics like time and token usage. It also records the creation timestamp. The function then attempts to insert this record into the `dbexchanges` collection."
    *   **Parameters:**
        - **question** (`str`): The user's question in the exchange.
        - **answer** (`str`): The generated answer for the question.
        - **feedback** (`str`): User feedback provided for the exchange.
        - **username** (`str`): The username associated with this exchange.
        - **chat_name** (`str`): The name of the chat session where the exchange occurred.
        - **helper_used** (`str`): Optional: Identifier for the helper component used, defaults to an empty string.
        - **main_used** (`str`): Optional: Identifier for the main component used, defaults to an empty string.
        - **total_time** (`str`): Optional: The total time taken for the exchange, defaults to an empty string.
        - **helper_time** (`str`): Optional: The time taken by the helper component, defaults to an empty string.
        - **main_time** (`str`): Optional: The time taken by the main component, defaults to an empty string.
        - **json_tokens** (`int`): Optional: Number of JSON tokens used, defaults to 0.
        - **toon_tokens** (`int`): Optional: Number of Toon tokens used, defaults to 0.
        - **savings_percent** (`float`): Optional: Percentage of savings achieved, defaults to 0.0.
    *   **Returns:**
        - `new_id` (`str`): The unique identifier of the newly inserted exchange record if the insertion is successful.
        - `None`: Returns None if an exception occurs during the database insertion.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_exchanges_by_user`
    *   **Summary:** "This function retrieves a list of exchange records from a database collection, presumably named `dbexchanges`, based on a provided username. It queries the collection for documents where the 'username' field matches the input `username`. The retrieved exchanges are then sorted in ascending order by their 'created_at' timestamp. The sorted list of exchange records is then returned."
    *   **Signature:** `def fetch_exchanges_by_user(username: str)`
    *   **Description:** "This function retrieves a list of exchange records from a database collection, presumably named `dbexchanges`, based on a provided username. It queries the collection for documents where the 'username' field matches the input `username`. The retrieved exchanges are then sorted in ascending order by their 'created_at' timestamp. The sorted list of exchange records is then returned."
    *   **Parameters:**
        - **username** (`str`): The username used to filter the exchange records in the database.
    *   **Returns:** `exchanges` (`list[dict]`): A list of exchange records (dictionaries) associated with the specified username, sorted by their creation timestamp in ascending order.
    *   **Usage:** This function calls no other functions.

    #### Function: `fetch_exchanges_by_chat`
    *   **Summary:** This function retrieves a list of exchange documents from a database collection named `dbexchanges`. It filters these exchanges based on a specific `username` and `chat_name` provided as arguments. The results are then sorted in ascending order by their `created_at` timestamp and returned as a Python list.
    *   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
    *   **Description:** This function retrieves a list of exchange documents from a database collection named `dbexchanges`. It filters these exchanges based on a specific `username` and `chat_name` provided as arguments. The results are then sorted in ascending order by their `created_at` timestamp and returned as a Python list.
    *   **Parameters:**
        - **username** (`str`): The username used to filter the exchanges.
        - **chat_name** (`str`): The name of the chat used to filter the exchanges.
    *   **Returns:** `exchanges` (`list`): A list of exchange documents that match the specified username and chat name, sorted by creation date.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_exchange_feedback`
    *   **Summary:** "This function updates the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function utilizes a database client, likely `dbexchanges`, to perform an update operation. It targets the document where the `_id` field matches the provided `exchange_id` and sets its 'feedback' field to the new integer value. The function then returns the count of documents that were successfully modified by this operation."
    *   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
    *   **Description:** "This function updates the feedback value for a specific exchange record in a database. It takes an exchange identifier and an integer feedback value as input. The function utilizes a database client, likely `dbexchanges`, to perform an update operation. It targets the document where the `_id` field matches the provided `exchange_id` and sets its 'feedback' field to the new integer value. The function then returns the count of documents that were successfully modified by this operation."
    *   **Parameters:**
        - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated in the database.
        - **feedback** (`int`): The integer value representing the feedback to be set for the specified exchange.
    *   **Returns:** `modified_count` (`int`): The number of documents that were modified by the update operation.
    *   **Usage:** This function calls no other functions.

    #### Function: `update_exchange_feedback_message`
    *   **Summary:** This function updates an existing exchange record in the database. It targets a specific exchange identified by `exchange_id` and sets its `feedback_message` field to the provided `feedback_message` string. The function leverages a database update operation to modify a single document and reports the number of documents that were successfully modified.
    *   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
    *   **Description:** This function updates an existing exchange record in the database. It targets a specific exchange identified by `exchange_id` and sets its `feedback_message` field to the provided `feedback_message` string. The function leverages a database update operation to modify a single document and reports the number of documents that were successfully modified.
    *   **Parameters:**
        - **exchange_id** (`Any`): The unique identifier of the exchange record to be updated in the database.
        - **feedback_message** (`str`): The new feedback message string to be associated with the specified exchange record.
    *   **Returns:** `modified_count` (`int`): The count of documents that were modified by the update operation. Typically 0 or 1 for a single document update.
    *   **Usage:** This function calls no other functions.

    #### Function: `delete_exchange_by_id`
    *   **Summary:** "This function is designed to remove a specific exchange record from a database collection. It takes a unique exchange identifier as input and uses it to locate and delete a single document. The function returns an integer indicating how many documents were successfully deleted, which will typically be 0 or 1."
    *   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
    *   **Description:** "This function is designed to remove a specific exchange record from a database collection. It takes a unique exchange identifier as input and uses it to locate and delete a single document. The function returns an integer indicating how many documents were successfully deleted, which will typically be 0 or 1."
    *   **Parameters:**
        - **exchange_id** (`str`): The unique identifier (ID) of the exchange document to be deleted from the database.
    *   **Returns:** `deleted_count` (`int`): The number of documents that were deleted. This will be 1 if the exchange was found and deleted, or 0 if no matching exchange was found.
    *   **Usage:** This function calls no other functions.

    #### Function: `delete_full_chat`
    *   **Summary:** "This function is designed to completely remove a specific chat and all its associated message exchanges from the database. It first deletes all messages linked to the provided username and chat name. Following this, the function proceeds to delete the chat entry itself. This comprehensive deletion process aims to maintain data consistency between the frontend and backend systems. The function returns the count of chat documents that were successfully deleted."
    *   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
    *   **Description:** "This function is designed to completely remove a specific chat and all its associated message exchanges from the database. It first deletes all messages linked to the provided username and chat name. Following this, the function proceeds to delete the chat entry itself. This comprehensive deletion process aims to maintain data consistency between the frontend and backend systems. The function returns the count of chat documents that were successfully deleted."
    *   **Parameters:**
        - **username** (`str`): The username associated with the chat to be deleted.
        - **chat_name** (`str`): The name of the chat to be deleted.
    *   **Returns:** `deleted_count` (`int`): The number of chat documents deleted from the database, typically 0 or 1.
    *   **Usage:** This function calls no other functions.

    ### File: `frontend/frontend.py`

    #### Function: `clean_names`
    *   **Summary:** "This function processes a list of strings, `model_list`. For each string in the input list, it splits the string by the '/' delimiter. It then extracts the last segment of the split string. The function ultimately returns a new list containing these extracted last segments, effectively 'cleaning' or simplifying the names by removing any preceding path-like components."
    *   **Signature:** `def clean_names(model_list)`
    *   **Description:** "This function processes a list of strings, `model_list`. For each string in the input list, it splits the string by the '/' delimiter. It then extracts the last segment of the split string. The function ultimately returns a new list containing these extracted last segments, effectively 'cleaning' or simplifying the names by removing any preceding path-like components."
    *   **Parameters:**
        - **model_list** (`List[str]`): A list of strings, where each string potentially contains path-like components separated by '/'. These strings represent model names or identifiers that need to be simplified.
    *   **Returns:** `cleaned_names` (`List[str]`): A new list of strings, where each string is the last segment of the original input string after splitting by '/'. This represents the cleaned or simplified names.
    *   **Usage:** This function calls no other functions.

    #### Function: `get_filtered_models`
    *   **Summary:** "This function filters a given list of models, `source_list`, based on a specified `category_name`. It retrieves filtering keywords associated with the category from a global `CATEGORY_KEYWORDS` dictionary. If the category's keywords include \"STANDARD\", the function returns only those models from `source_list` that are also present in a `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list`, collecting models whose names contain any of the category's keywords (case-insensitive). If no models match the keywords, the original `source_list` is returned."
    *   **Signature:** `def get_filtered_models(source_list, category_name)`
    *   **Description:** "This function filters a given list of models, `source_list`, based on a specified `category_name`. It retrieves filtering keywords associated with the category from a global `CATEGORY_KEYWORDS` dictionary. If the category's keywords include \"STANDARD\", the function returns only those models from `source_list` that are also present in a `STANDARD_MODELS` list. Otherwise, it iterates through the `source_list`, collecting models whose names contain any of the category's keywords (case-insensitive). If no models match the keywords, the original `source_list` is returned."
    *   **Parameters:**
        - **source_list** (`list`): The list of models (likely strings) to be filtered.
        - **category_name** (`str`): The name of the category used to determine the filtering keywords.
    *   **Returns:** `filtered_models` (`list`): A new list containing models filtered by the specified category's keywords, or the original `source_list` if no models match the keywords.
    *   **Usage:** This function calls no other functions.

    #### Function: `save_gemini_cb`
    *   **Summary:** "This function is designed to save a new Gemini API key provided by the user. It retrieves the key from the Streamlit session state. If a new key is present, it updates the key in the database for the current user and then clears the key from the session state. Finally, it displays a success toast notification to the user."
    *   **Signature:** `def save_gemini_cb()`
    *   **Description:** "This function is designed to save a new Gemini API key provided by the user. It retrieves the key from the Streamlit session state. If a new key is present, it updates the key in the database for the current user and then clears the key from the session state. Finally, it displays a success toast notification to the user."
    *   **Parameters:** None
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `save_ollama_cb`
    *   **Summary:** "This function handles the saving of a new Ollama URL. It retrieves the URL from the Streamlit session state, specifically from the key 'in_ollama_url'. If a new URL is present, it updates the database with this URL for the current user and displays a confirmation toast message to the user."
    *   **Signature:** `def save_ollama_cb()`
    *   **Description:** "This function handles the saving of a new Ollama URL. It retrieves the URL from the Streamlit session state, specifically from the key 'in_ollama_url'. If a new URL is present, it updates the database with this URL for the current user and displays a confirmation toast message to the user."
    *   **Parameters:** None
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `load_data_from_db`
    *   **Summary:** "This function, `load_data_from_db`, is designed to load chat and exchange data from the database for a specified user. It first verifies if the data for the given username is already present in the Streamlit session state to avoid reloading. If the user data is not loaded or a new user is detected, it initializes the session state for chats. The function then fetches predefined chats and their associated exchanges from the database, organizing them within the session state. It also handles legacy cases where exchanges might exist for unlisted chats and ensures a default chat is created if no chats are found for the user, finally setting an active chat."
    *   **Signature:** `def load_data_from_db(username: str)`
    *   **Description:** "This function, `load_data_from_db`, is designed to load chat and exchange data from the database for a specified user. It first verifies if the data for the given username is already present in the Streamlit session state to avoid reloading. If the user data is not loaded or a new user is detected, it initializes the session state for chats. The function then fetches predefined chats and their associated exchanges from the database, organizing them within the session state. It also handles legacy cases where exchanges might exist for unlisted chats and ensures a default chat is created if no chats are found for the user, finally setting an active chat."
    *   **Parameters:**
        - **username** (`str`): The username for whom to load chat and exchange data.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `handle_feedback_change`
    *   **Summary:** "The handle_feedback_change function processes updates to user feedback associated with a specific exchange record. It takes an exchange dictionary and a new feedback value as input. The function first updates the 'feedback' key within the provided 'ex' dictionary with the new 'val'. Subsequently, it interacts with a database utility, calling 'db.update_exchange_feedback' to persist this change using the exchange's '_id' and the new feedback value. Finally, it triggers a Streamlit application rerun, likely to refresh the UI and reflect the updated feedback status."
    *   **Signature:** `def handle_feedback_change(ex, val)`
    *   **Description:** "The handle_feedback_change function processes updates to user feedback associated with a specific exchange record. It takes an exchange dictionary and a new feedback value as input. The function first updates the 'feedback' key within the provided 'ex' dictionary with the new 'val'. Subsequently, it interacts with a database utility, calling 'db.update_exchange_feedback' to persist this change using the exchange's '_id' and the new feedback value. Finally, it triggers a Streamlit rerun, likely to refresh the UI and reflect the updated feedback status."
    *   **Parameters:**
        - **ex** (`dict`): A dictionary-like object representing an exchange record, expected to contain 'feedback' and '_id' keys.
        - **val** (`Any`): The new feedback value to be assigned to the exchange record.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `handle_delete_exchange`
    *   **Summary:** "This function handles the deletion of a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if the exchange is found within that chat's exchanges list, it removes it from the session state. Finally, it triggers a Streamlit rerun to update the UI."
    *   **Signature:** `def handle_delete_exchange(chat_name, ex)`
    *   **Description:** "This function handles the deletion of a specific exchange. It first removes the exchange from the database using its ID. Subsequently, it checks if the associated chat exists in the Streamlit session state and, if the exchange is found within that chat's exchanges list, it removes it from the session state. Finally, it triggers a Streamlit rerun to update the UI."
    *   **Parameters:**
        - **chat_name** (`str`): The name of the chat from which the exchange should be deleted.
        - **ex** (`dict`): The exchange object to be deleted, expected to contain an '_id' field.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `handle_delete_chat`
    *   **Summary:** "This function handles the deletion of a specific chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the Streamlit session state by deleting the chat from `st.session_state.chats`. If other chats exist, it sets the first available chat as the new active chat; otherwise, it creates a new default chat named 'Chat 1', inserts it into the database, and sets it as the active chat. Finally, it triggers a Streamlit rerun to update the UI."
    *   **Signature:** `def handle_delete_chat(username, chat_name)`
    *   **Description:** "This function handles the deletion of a specific chat for a given user. It first removes the chat from the database using `db.delete_full_chat`. Subsequently, it cleans up the Streamlit session state by deleting the chat from `st.session_state.chats`. If other chats exist, it sets the first available chat as the new active chat; otherwise, it creates a new default chat named 'Chat 1', inserts it into the database, and sets it as the active chat. Finally, it triggers a Streamlit rerun to update the UI."
    *   **Parameters:**
        - **username** (`str`): The username of the user whose chat is to be deleted.
        - **chat_name** (`str`): The name of the chat to be deleted.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `extract_repo_name`
    *   **Summary:** "This function is designed to extract a repository name from a given input text string. It first attempts to locate a URL within the text using a regular expression. If a URL is successfully matched, it proceeds to parse the URL to isolate its path component. The last segment of this path is then treated as the potential repository name, with any trailing '.git' suffix removed for standardization. If no URL is found in the input text or if the extracted URL path is empty, the function returns None."
    *   **Signature:** `def extract_repo_name(text)`
    *   **Description:** "This function is designed to extract a repository name from a given input text string. It first attempts to locate a URL within the text using a regular expression. If a URL is successfully matched, it proceeds to parse the URL to isolate its path component. The last segment of this path is then treated as the potential repository name, with any trailing '.git' suffix removed for standardization. If no URL is found in the input text or if the extracted URL path is empty, the function returns None."
    *   **Parameters:**
        - **text** (`str`): The input string from which to extract a repository name, potentially containing a URL.
    *   **Returns:** `repo_name` (`str` or None): The extracted repository name as a string, or None if no valid repository name could be determined from the input text.
    *   **Usage:** This function calls no other functions.

    #### Function: `stream_text_generator`
    *   **Summary:** "This function acts as a generator that takes a string of text and yields its words one by one. It splits the input text by spaces and, for each word, appends a space before yielding it. A small delay of 0.01 seconds is introduced after yielding each word, simulating a streaming effect. This is useful for displaying text progressively."
    *   **Signature:** `def stream_text_generator(text)`
    *   **Description:** "This function acts as a generator that takes a string of text and yields its words one by one. It splits the input text by spaces and, for each word, appends a space before yielding it. A small delay of 0.01 seconds is introduced after yielding each word, simulating a streaming effect. This is useful for displaying text progressively."
    *   **Parameters:**
        - **text** (`str`): The input string to be processed and streamed word by word.
    *   **Returns:** `word_with_space` (`str`): Each word from the input text, followed by a space, yielded sequentially.
    *   **Usage:** This function calls no other functions.

    #### Function: `render_text_with_mermaid`
    *   **Summary:** "This function processes a given markdown string, identifying and rendering standard markdown content and embedded Mermaid diagrams. It splits the input text based on ````mermaid` delimiters. Regular markdown sections are rendered using `st.markdown` or `st.write_stream` if streaming is enabled. Mermaid diagram code blocks are rendered using `st_mermaid`, with a fallback to `st.code` if an error occurs during Mermaid rendering."
    *   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream=False)`
    *   **Description:** "This function processes a given markdown string, identifying and rendering standard markdown content and embedded Mermaid diagrams. It splits the input text based on ````mermaid` delimiters. Regular markdown sections are rendered using `st.markdown` or `st.write_stream` if streaming is enabled. Mermaid diagram code blocks are rendered using `st_mermaid`, with a fallback to `st.code` if an error occurs during Mermaid rendering."
    *   **Parameters:**
        - **markdown_text** (`str`): The input text containing markdown content and potentially embedded Mermaid diagrams.
        - **should_stream** (`bool`): A boolean flag indicating whether non-Mermaid markdown content should be streamed. Defaults to False.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    #### Function: `render_exchange`
    *   **Summary:** "The `render_exchange` function is designed to display a single chat exchange, comprising a user's question and an assistant's answer, within a Streamlit application. It first renders the user's question. Subsequently, it presents the assistant's response along with an interactive toolbar. This toolbar includes options for providing feedback (like/dislike), adding comments via a popover, downloading the answer, and deleting the exchange. The function also handles error states in the assistant's answer, displaying an error message and a delete option. Finally, it renders the answer content, which may include Mermaid diagrams."
    *   **Signature:** `def render_exchange(ex, current_chat_name)`
    *   **Description:** "The `render_exchange` function is designed to display a single chat exchange, comprising a user's question and an assistant's answer, within a Streamlit application. It first renders the user's question. Subsequently, it presents the assistant's response along with an interactive toolbar. This toolbar includes options for providing feedback (like/dislike), adding comments via a popover, downloading the answer, and deleting the exchange. The function also handles error states in the assistant's answer, displaying an error message and a delete option. Finally, it renders the answer content, which may include Mermaid diagrams."
    *   **Parameters:**
        - **ex** (`dict`): A dictionary-like object representing a single chat exchange. It is expected to contain keys such as 'question', 'answer', 'feedback', '_id', and 'feedback_message', which are used for rendering and interaction.
        - **current_chat_name** (`str`): A string representing the name of the current chat session. This is used as context when performing actions like deleting an exchange.
    *   **Returns:** None
    *   **Usage:** This function calls no other functions.

    ### File: `schemas/types.py`

    #### Class: `ParameterDescription`
    *   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to structure information about a single parameter of a function. It serves as a data model to consistently represent a parameter's name, its type, and a descriptive explanation of its purpose. This class is primarily used for documentation generation or static analysis where structured parameter data is required.
    *   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* "This class, being a Pydantic BaseModel, automatically generates an `__init__` method. It initializes an instance by accepting `name`, `type`, and `description` as arguments, which are then validated and stored as instance attributes."
        *   *Parameters:*
            - **name** (`str`): The name of the parameter.
            - **type** (`str`): The type hint or inferred type of the parameter.
            - **description** (`str`): A brief explanation of the parameter's purpose.
    *   **Methods:** None

    #### Class: `ReturnDescription`
    *   **Summary:** The ReturnDescription class is a Pydantic BaseModel designed to structure information about a function's return value. It serves as a data container, ensuring that return value descriptions consistently include a name, type, and a detailed explanation. This class is fundamental for standardizing how function outputs are documented and understood within the system.
    *   **Instantiation:** "The instantiation points for this class are not explicitly provided in the current context, but it is typically instantiated when describing the return values of functions or methods within a larger schema definition."
    *   **Dependencies:** This class primarily depends on `pydantic.BaseModel` for its structural definition and data validation capabilities.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ReturnDescription` is automatically generated by Pydantic's BaseModel. It initializes an instance of `ReturnDescription` by accepting `name`, `type`, and `description` as keyword arguments, validating them against their respective string types as defined in the class attributes.
        *   *Parameters:*
            - **name** (`str`): The name or label for the return value.
            - **type** (`str`): The data type of the return value, e.g., 'str', 'int', 'List[str]'.
            - **description** (`str`): A detailed explanation of what the return value represents or contains.
    *   **Methods:** None

    #### Class: `UsageContext`
    *   **Summary:** The UsageContext class is a Pydantic BaseModel designed to encapsulate information about how a function or method interacts with other parts of a system. It provides a structured way to describe what an entity calls and where it is called from. This class serves as a data model for representing the operational context of a code component, facilitating clear and consistent documentation of inter-component relationships.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class relies on `pydantic.BaseModel` for its data model capabilities. No other explicit external dependencies are listed in the provided context.
    *   **Constructor:**
        *   *Description:* "This class does not explicitly define an `__init__` method. As a Pydantic `BaseModel`, it automatically generates a constructor that initializes its fields, `calls` and `called_by`, based on the arguments provided during instantiation."
        *   *Parameters:*
            - **calls** (`str`): A string summarizing the functions, methods, or classes that this entity calls within its execution.
            - **called_by** (`str`): A string summarizing the functions, methods, or contexts from which this entity is invoked.
    *   **Methods:** None

    #### Class: `FunctionDescription`
    *   **Summary:** The FunctionDescription class is a Pydantic BaseModel designed to provide a structured and comprehensive analysis of a Python function. It serves as a data model to encapsulate various aspects of a function, including its high-level purpose, detailed descriptions of its input parameters, specifications of its return values, and information regarding its usage context within a larger system. This class facilitates the standardized representation and validation of function metadata.
    *   **Instantiation:** The provided context does not specify where this class is instantiated.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The `__init__` method for FunctionDescription is implicitly generated by Pydantic's BaseModel. It initializes an instance of FunctionDescription by validating and assigning values to its fields: `overall`, `parameters`, `returns`, and `usage_context`. This ensures that all function descriptions conform to the defined schema and type hints.
        *   *Parameters:*
            - **overall** (`str`): A string providing a high-level summary of the function's purpose and functionality.
            - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing an input parameter of the function.
            - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects, each describing a value returned by the function.
            - **usage_context** (`UsageContext`): An object containing information about where and how the function is used or called.
    *   **Methods:** None

    #### Class: `FunctionAnalysis`
    *   **Summary:** The FunctionAnalysis class is a Pydantic BaseModel designed to encapsulate a comprehensive analysis of a single Python function. It serves as a structured data container, holding the function's unique identifier, a detailed description object, and an optional field for error messages. This model is crucial for standardizing the representation of function analysis results within a larger system, ensuring consistency and ease of data exchange.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies in the provided context.
    *   **Constructor:**
        *   *Description:* The FunctionAnalysis class does not explicitly define an `__init__` method. As a Pydantic BaseModel, its initialization is handled automatically by Pydantic, which validates and assigns values to its fields (`identifier`, `description`, `error`) based on the arguments provided during object creation.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifier for the function being analyzed.
            - **description** (`FunctionDescription`): An object containing a detailed description of the function, including its purpose, parameters, returns, and usage context.
            - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the function's analysis. Defaults to None.
    *   **Methods:** None

    #### Class: `ConstructorDescription`
    *   **Summary:** The `ConstructorDescription` class is a Pydantic BaseModel designed to structure and describe the `__init__` method of a Python class. It serves as a data schema for capturing essential information about a constructor, including a textual summary of its behavior and a detailed list of its parameters. This model is crucial for systems that analyze or generate documentation for class constructors, providing a standardized format for their representation.
    *   **Instantiation:** "The specific instantiation points for this class are not provided in the current context, but it is typically instantiated when structured data about a class's constructor needs to be represented or processed."
    *   **Dependencies:** This class relies on `pydantic.BaseModel` for its data modeling capabilities and `typing.List` for type hinting its list of parameters. It does not explicitly list any other external functional dependencies.
    *   **Constructor:**
        *   *Description:* The `__init__` method for `ConstructorDescription` is implicitly generated by Pydantic. It handles the validation and assignment of the `description` string and the `parameters` list (which contains `ParameterDescription` objects) when an instance of `ConstructorDescription` is created. This ensures that all constructor descriptions conform to the defined schema.
        *   *Parameters:*
            - **description** (`str`): A string providing a summary or explanation of the constructor's purpose and behavior.
            - **parameters** (`List[ParameterDescription]`): A list of `ParameterDescription` objects, each detailing a parameter accepted by the constructor.
    *   **Methods:** None

    #### Class: `ClassContext`
    *   **Summary:** The ClassContext class is a Pydantic BaseModel designed to encapsulate metadata about a Python class's external interactions. It specifically stores information regarding the class's dependencies and where it is instantiated within a larger system. This model provides a structured way to represent contextual information for class analysis.
    *   **Instantiation:** This class is not explicitly instantiated by other components in the provided context.
    *   **Dependencies:** This class does not explicitly declare external dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* "As a Pydantic BaseModel, the __init__ method for ClassContext is automatically generated. It handles the validation and assignment of the `dependencies` and `instantiated_by` string fields upon instantiation, ensuring type correctness."
        *   *Parameters:*
            - **dependencies** (`str`): A string summarizing the external dependencies of the class.
            - **instantiated_by** (`str`): A string summarizing where the class is instantiated.
    *   **Methods:** None

    #### Class: `ClassDescription`
    *   **Summary:** The ClassDescription class is a Pydantic BaseModel that serves as a structured schema for representing a comprehensive analysis of a Python class. It aggregates information about a class's high-level purpose, its constructor, a list of its individual methods, and its external usage context. This model is crucial for organizing and validating the output of a class analysis process, ensuring consistency and completeness in the generated documentation.
    *   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* "This class is a Pydantic BaseModel, so its constructor is automatically generated by Pydantic. It initializes instances by validating and assigning values to its defined fields: overall, init_method, methods, and usage_context."
        *   *Parameters:*
            - **overall** (`str`): A string describing the overall purpose and functionality of the class being analyzed.
            - **init_method** (`ConstructorDescription`): An object containing the detailed description and parameters of the class's constructor (__init__ method).
            - **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each providing a detailed description of a method within the class being analyzed.
            - **usage_context** (`ClassContext`): An object containing information about the class's external dependencies and where it is instantiated within the codebase.
    *   **Methods:** None

    #### Class: `ClassAnalysis`
    *   **Summary:** The `ClassAnalysis` class is a Pydantic BaseModel designed to serve as the main schema for a comprehensive analysis of a Python class. It encapsulates the class's unique identifier, a detailed `ClassDescription` object containing its constructor and method analyses, and an optional `error` field to report issues during analysis. This model provides a structured format for representing the output of a class analysis process.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
    *   **Dependencies:** This class does not explicitly list any external dependencies within its definition.
    *   **Constructor:**
        *   *Description:* The `ClassAnalysis` class does not explicitly define an `__init__` method. It inherits from Pydantic's `BaseModel`, meaning its constructor is implicitly handled by Pydantic. It initializes the instance attributes `identifier`, `description`, and `error` based on the arguments passed during object creation, performing validation according to their type hints.
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifier for the class being analyzed.
            - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, and methods.
            - **error** (`Optional[str]`): An optional string field to store any error messages encountered during the class analysis. Defaults to None.
    *   **Methods:** None

    #### Class: `CallInfo`
    *   **Summary:** The CallInfo class is a Pydantic BaseModel designed to encapsulate details about a specific call event within a software system. It acts as a structured data container, defining the essential attributes required to identify and describe where a function, method, or module call originates. This model is intended for use in tracking and analyzing relationships between different parts of a codebase, particularly in contexts like 'called_by' and 'instantiated_by' lists.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the context.
    *   **Dependencies:** This class does not explicitly list external functional dependencies in its context.
    *   **Constructor:**
        *   *Description:* "As a Pydantic BaseModel, CallInfo's constructor is implicitly generated. It handles the validation and assignment of the provided arguments (file, function, mode, line) to corresponding instance attributes, ensuring data integrity according to their defined types."
        *   *Parameters:*
            - **file** (`str`): The path to the file where the call event is recorded.
            - **function** (`str`): The name of the function or method that performed the call.
            - **mode** (`str`): The classification of the call, e.g., 'method', 'function', or 'module'.
            - **line** (`int`): The line number within the file where the call occurred.
    *   **Methods:** None

    #### Class: `FunctionContextInput`
    *   **Summary:** The FunctionContextInput class is a Pydantic BaseModel designed to provide a structured representation of a function's operational context. It serves as a data container, holding information about other functions, methods, or classes that the analyzed function calls, as well as details about where the analyzed function itself is invoked. This class is fundamental for analyzing and understanding the interaction patterns of a specific function within a larger codebase.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
    *   **Dependencies:** "This class primarily depends on Pydantic's BaseModel for its structure and validation, and `typing.List` for type hinting. It also depends on the `CallInfo` type, which is not defined within this snippet."
    *   **Constructor:**
        *   *Description:* "The `__init__` method for FunctionContextInput is implicitly generated by Pydantic, as it inherits from BaseModel. It initializes the instance attributes `calls` and `called_by` based on the arguments provided during object creation, ensuring type validation according to their annotations."
        *   *Parameters:*
            - **calls** (`List[str]`): A list of strings, where each string represents the identifier of a function, method, or class that the subject function calls.
            - **called_by** (`List[CallInfo]`): A list of CallInfo objects, each providing details about a specific caller of the subject function.
    *   **Methods:** None

    #### Class: `FunctionAnalysisInput`
    *   **Summary:** The FunctionAnalysisInput class is a Pydantic BaseModel designed to define the structured input required for performing a function analysis. It acts as a data transfer object, ensuring that all necessary components like the function's identifier, source code, relevant imports, and contextual information are provided in a consistent format. This class serves as a contract for the data expected by a function analysis process.
    *   **Instantiation:** There is no explicit information provided on where this class is instantiated within the given context.
    *   **Dependencies:** "This class does not explicitly list any external functional dependencies. It relies on Pydantic's BaseModel for its core functionality."
    *   **Constructor:**
        *   *Description:* "This class, being a Pydantic BaseModel, implicitly generates an `__init__` method. This constructor is responsible for validating and assigning the provided arguments to the class's fields, ensuring they conform to the specified types and constraints (e.g., `Literal` for `mode`). The fields defined in the class act as the parameters for its initialization."
        *   *Parameters:*
            - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, which is fixed to 'function_analysis' for this input type.
            - **identifier** (`str`): The unique name or identifier of the function that is to be analyzed.
            - **source_code** (`str`): The raw source code string of the function targeted for analysis.
            - **imports** (`List[str]`): A list of import statements that are relevant to the function's execution context.
            - **context** (`FunctionContextInput`): Additional contextual information, structured as a FunctionContextInput object, necessary for the analysis.
    *   **Methods:** None

    #### Class: `MethodContextInput`
    *   **Summary:** The MethodContextInput class is a Pydantic BaseModel designed to provide a structured schema for capturing comprehensive contextual information about a specific method. It defines fields such as the method's unique identifier, a list of entities it calls, a list of entities that call it, its arguments, and its docstring. This class serves as a data transfer object, ensuring consistent data representation for method analysis within a larger system.
    *   **Instantiation:** The specific locations where this class is instantiated are not provided in the current context.
    *   **Dependencies:** "This class primarily depends on pydantic.BaseModel for its data modeling capabilities and typing.List and typing.Optional for type hinting. It also implicitly depends on a CallInfo type, which is not defined within this source code."
    *   **Constructor:**
        *   *Description:* "This class does not explicitly define an __init__ method. It inherits from pydantic.BaseModel, and its initialization is handled implicitly by Pydantic, which validates and assigns values to its fields upon instantiation."
        *   *Parameters:*
            - **identifier** (`str`): A unique string identifying the method.
            - **calls** (`List[str]`): A list of strings representing other methods, classes, or functions called by this method.
            - **called_by** (`List[CallInfo]`): A list of CallInfo objects, indicating where this method is called from.
            - **args** (`List[str]`): A list of strings representing the arguments of the method.
            - **docstring** (`Optional[str]`): An optional string containing the method's docstring.
    *   **Methods:** None

    #### Class: `ClassContextInput`
    *   **Summary:** The ClassContextInput class is a Pydantic BaseModel designed to encapsulate structured context information for analyzing a Python class. It serves as a data container, holding lists of external dependencies, points where the class is instantiated, and detailed context for each method within the class. This model facilitates the organized transfer of comprehensive contextual data for further processing or analysis.
    *   **Instantiation:** The instantiation points for this class are not specified in the provided context.
    *   **Dependencies:** This class does not explicitly declare external functional dependencies within the provided context.
    *   **Constructor:**
        *   *Description:* "This class, being a Pydantic BaseModel, initializes its attributes automatically based on the provided arguments during instantiation. It does not have an explicit __init__ method defined, relying on Pydantic's data validation and assignment mechanisms to set up its state."
        *   *Parameters:*
            - **dependencies** (`List[str]`): A list of strings representing external functional dependencies of the class.
            - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects, detailing where this class is instantiated within the codebase.
            - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing specific context for a method belonging to the class.
    *   **Methods:** None

    #### Class: `ClassAnalysisInput`
    *   **Summary:** The ClassAnalysisInput class is a Pydantic model designed to define the structured input required for generating a ClassAnalysis object. It serves as a data transfer object, ensuring that all necessary components for class analysis, such as the class identifier, its source code, relevant imports, and contextual information, are provided in a consistent format. This model facilitates robust data validation and parsing for the class analysis process.
    *   **Instantiation:** The instantiation points for this class are not explicitly provided in the context.
    *   **Dependencies:** This class does not explicitly list any external functional dependencies.
    *   **Constructor:**
        *   *Description:* "This class does not explicitly define an __init__ method. It inherits from pydantic.BaseModel, and its initialization is handled implicitly by Pydantic, which validates and assigns values to its fields upon instantiation."
        *   *Parameters:*
            - **mode** (`Literal["class_analysis"]`): Specifies the analysis mode, fixed to 'class_analysis'.
            - **identifier** (`str`): The unique identifier for the class to be analyzed.
            - **source_code** (`str`): The raw source code of the class.
            - **imports** (`List[str]`): A list of import statements relevant to the class.
            - **context** (`ClassContextInput`): The contextual information for the class, provided as a ClassContextInput object.
    *   **Methods:** None
```
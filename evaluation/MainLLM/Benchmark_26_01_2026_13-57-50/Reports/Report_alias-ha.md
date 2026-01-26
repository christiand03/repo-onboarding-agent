# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
    - **Description:** The_REPO_Onboarding_Agent is a tool designed to streamline the onboarding process for new repositories. It analyzes the repository's structure and codebase to provide insights and documentation.
    - **Key Features:**
      - Repository analysis
      - Code documentation generation
      - Onboarding process automation
    - **Tech Stack:** Python, Git, Streamlit, MongoDB

## 2. Installation
### Dependencies
The project depends on the following libraries:
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

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

### Setup Guide
To set up the project, follow these steps:
1. Clone the repository
2. Install the dependencies using `pip install -r requirements.txt`
3. Configure the environment variables

### Quick Startup
To quickly start the project, run:
```bash
streamlit run frontend/frontend.py
```

## 3. Use Cases & Commands
The_REPO_Onboarding_Agent can be used for:
- Repository analysis: `python backend/main.py analyze-repo <repo-url>`
- Code documentation generation: `python backend/main.py generate-docs <repo-url>`

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** A class to traverse the Abstract Syntax Tree (AST) of Python source code and extract metadata about imports, classes, and functions.
*   **Instantiation:** The class is instantiated in the `backend/main.py` file.
*   **Dependencies:** The class depends on the `ast`, `os`, and `getRepo.GitRepository` modules.
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor with the source code, file path, and project root.
    *   *Parameters:*
      - **source_code** (`str`): The raw source code of the file being analyzed.
      - **file_path** (`str`): The absolute path to the Python file being visited.
      - **project_root** (`str`): The root directory of the project, used to determine the module path.
*   **Methods:**
    ##### visit_Import
    *   **Signature:** `visit_Import(self, node: ast.Import)`
    *   **Description:** This method processes `ast.Import` nodes, which represent `import module` statements.
    *   **Parameters:**
      - **node** (`ast.Import`): The AST node representing an import statement.

    ##### visit_ImportFrom
    *   **Signature:** `visit_ImportFrom(self, node: ast.ImportFrom)`
    *   **Description:** This method handles `ast.ImportFrom` nodes, which correspond to `from module import name` statements.
    *   **Parameters:**
      - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.

    ##### visit_ClassDef
    *   **Signature:** `visit_ClassDef(self, node: ast.ClassDef)`
    *   **Description:** This method is responsible for processing `ast.ClassDef` nodes, which represent class definitions.
    *   **Parameters:**
      - **node** (`ast.ClassDef`): The AST node representing a class definition.

    ##### visit_FunctionDef
    *   **Signature:** `visit_FunctionDef(self, node: ast.FunctionDef)`
    *   **Description:** This method processes `ast.FunctionDef` nodes, distinguishing between methods defined within a class and top-level functions.
    *   **Parameters:**
      - **node** (`ast.FunctionDef`): The AST node representing a function definition.

    ##### visit_AsyncFunctionDef
    *   **Signature:** `visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef)`
    *   **Description:** This method handles `ast.AsyncFunctionDef` nodes, which represent asynchronous function definitions.
    *   **Parameters:**
      - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.

---
</SystemPrompt>
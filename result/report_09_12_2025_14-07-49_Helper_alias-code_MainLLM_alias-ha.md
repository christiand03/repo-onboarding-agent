# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
      - Could not be determined due to a missing README file and insufficient context.
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** 
      - Information not found

*   **Repository Structure:**
    ```mermaid
    graph TD
        subgraph root
            .env.example
            .gitignore
            SystemPrompts
            analysis_output.json
            backend
            database
            frontend
            notizen
            output.json
            output.toon
            readme.md
            requirements.txt
            result
            schemas
            statistics
        end
    ```

    ## 2. Installation 
    ### Dependencies
    ```plaintext
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
- dns-python==2.8.0
- dotenv==0.9.9
- entrypoints==0.4
- extra-streamlit-components==0.1.81
- filetype==1.2.0
- fonttools==4.61.0
- gitdb==4.0.12
- GitPython==3.1.45
- google-ai-generative-language==0.9.0
- google-api-core==2.28.1
- google-auth==2.43.0
- googleapis-common-protos==1.72.0
- grpcio==1.76.0
- grpcio-status==1.76.0
- h11==0.16.0
- httpx==0.28.1
- idna==3.11
- Jinja2==3.1.6
- jiter==0.12.0
- jsonpatch==1.33.0
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
- langsmit==0.4.46
- MarkupSafe==3.0.3
- matplotlib==3.10.7
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
- pyarrow==2.21.0
- pyasn1==0.9.1
- PyJWT==2.10.1
- pymongo==4.15.4
- pyparsing==3.2.5
- python-dateutil==2.9.0.post0
- python-dotenv==1.2.1
- pytz==2025.2
- PyYAML==6.0.3
- referencing==0.37.0
- regex==2025.11.3
- requests==2.33.0
- requests-toolbelt==1.0.0
- rpds-py==0.29.0
- rsa==4.9.1
- setuptools==69.0.1
- six==1.16.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.51.0
- streamlit-authenticator==0.4.2
- tenacity==9.1.2
- tiktoken==0.12.0
- toml==0.10.2
- toolz==1.1.0
- toon_format==0.2.6
- toon_schema==0.1.3
- tornado==6.5.2
- tqdm==4.67.1
- typing-inspect==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- url3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0
- 
```
If Repo contains requirements.txt note: "pip install -r requirements.txt"

### Setup Guide
    [Step-by-step guide.]
    ### Quick Startup
    [Minimal commands to run.]

    ## 3. Use Cases & Commands
    [Description of important use cases and list of primary commands.] # Derived by synthesizing all gained Information

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here



## 5. Code Analysis
[Iterate through files as defined in `ast_schema`. Create a subsection for each file.]

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** Wandelt einen Dateipfad in einen Python-Modulpfad um.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initialisiert den ASTVisitor mit source code, file path und project root. 
    *   *Parameters:* 
      - **self** (`object`): The instance of the class.
      - **source_code** (`str`): The full source code of the file being analyzed.
      - **file_path** (`str`): The file path of the source code being analyzed.
      - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code: str, file_path: str, project_root: str)`
        *   *Description:* Initialisiert den ASTVisitor mit source code, file path und project root. 
        *   *Parameters:* 
          - **self** (`object`): The instance of the class.
          - **source_code** (`str`): The full source code of the file being analyzed.
          - **file_path** (`str`): The file path of the source code being analyzed.
          - **project_root** (`str`): The root directory of the project.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It then continues visiting child nodes.
        *   *Parameters:* 
          - **self** (`object`): The instance of the class.
          - **node** (`ast.Import`): An AST node representing an import statement.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST by extracting the full module paths and appending them to the schema's imports list. It then continues visiting child nodes.
        *   *Parameters:* 
          - **self** (`object`): The instance of the class.
          - **node** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Processes class definition nodes in the AST by creating a structured representation of the class, including its identifier, name, docstring, source code segment, and line numbers. It appends this information to the schema's classes list and tracks the current class for subsequent method processing.
        *   *Parameters:* 
          - **self** (`object`): The instance of the class.
          - **node** (`ast.ClassDef`): An AST node representing a class definition.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definition nodes in the AST. If a class is currently being visited, it associates the function with that class by creating a method context entry. Otherwise, it creates a standalone function entry in the schema. It extracts function arguments, docstrings, and source code segments, and includes line number information.
        *   *Parameters:* 
          - **self** (`object`): The instance of the class.
          - **node** (`ast.FunctionDef`): An AST node representing a function definition.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating to the standard function definition visitor method. This ensures that async functions are processed similarly to regular functions.
        *   *Parameters:* 
          - **self** (`object`): The instance of the class.
          - **node** (`ast.AsyncFunctionDef`): An AST node representing an asynchronous function definition.

---
</details>
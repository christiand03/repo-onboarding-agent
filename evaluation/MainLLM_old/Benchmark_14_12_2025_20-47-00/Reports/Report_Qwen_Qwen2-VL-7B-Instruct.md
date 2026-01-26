# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
      - Could not be determined due to a missing README file and insufficient context.
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** 
      - The repository contains a requirements.txt file listing the following dependencies:
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
        - langs mith==0.4.46
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
        - pyarrow==2.1.0
        - pyasrn1==0.6.1
        - pyasrn1_modules==0.4.2
        - pycparser==2.23
        - pydantic==2.12.4
        - pydantic-core==2.41.5
        - pydeck==6.0.3
        - referencing==0.37.0
        - regex==2025.11.3
        - requests==2.32.5
        - requests-toolbelt==1.0.0
        - rpds-py==0.29.0
        - rsa==4.9.1
        - setuptools==69.0.2
        - six==1.17.0
        - smmap==5.0.2
        - sniffio==1.3.1
        - streamlit==1.51.0
        - streamlit-authenticator==0.4.2
        - tenacity==9.1.2
        - tiktoken==0.12.0
        - toml==0.10.2
        - toolz==1.1.0
        - toon==0.1.0
        - tornado==6.5.2
        - tqdm==4.67.1
        - typing-inspection==0.4.2
        - typing_extensions==4.15.0
        - tzdata==2025.2
        - urllib3==2.5.0
        - watchdogs==6.0.0
        - xxhash==3.6.0
        - zstandard==0.25.0

        To install the dependencies, run: `pip install -r requirements.txt`

## 2. Installation 
### Dependencies
The list of dependencies can be found in the `requirements.txt` file.

### Setup Guide
Information not found.

### Quick Startup
Information not found.

## 3. Use Cases & Commands
The repository appears to be a Streamlit application for onboarding a repository agent. 

## 4. Architecture

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
*   **Methods:**
    *   **`__init__`**
        *   *Description:* Initializes the ASTVisitor with source code, file path, and project root.
        *   *Parameters:* 
          - **self**
          - **source_code** (`str`): The full source code string of the file being analyzed.
          - **file_path** (`str`): The file path of the source code being processed.
          - **project_root** (`str`): The root directory of the project being analyzed.
    *   **`visit_Import`**
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules.
        *   *Parameters:* 
          - **self**
          - **node** (`ast.Import`): An AST node representing an import statement.
    *   **`visit_ImportFrom`**
        *   *Description:* Processes import-from nodes in the AST.
        *   *Parameters:* 
          - **self**
          - **node** (`ast.ImportFrom`): An AST node representing an import-from statement.
    *   **`visit_ClassDef`**
        *   *Description:* Handles class definition nodes in the AST.
        *   *Parameters:* 
          - **self**
          - **node** (`ast.ClassDef`): An AST node representing a class definition.
    *   **`visit_FunctionDef`**
        *   *Description:* Processes function definition nodes in the AST.
        *   *Parameters:* 
          - **self**
          - **node** (`ast.FunctionDef`): An AST node representing a function definition.

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
*   **Methods:**
    *   **`__init__`**
        *   *Description:* Initializes the FileDependencyGraph.
        *   *Parameters:* 
          - **self**
          - **filename** (`str`): The name of the file being analyzed.
          - **repo_root** (`Any`): The root directory path of the repository containing the file.
    *   **`_resolve_module_name`**
        *   *Description:* Resolves relative import statements.
        *   *Parameters:* 
          - **self**
          - **node** (`ImportFrom`): An AST node representing a relative import statement.
    *   **`visit_Import`**
        *   *Description:* Handles import statements.
        *   *Parameters:* 
          - **self**
          - **node** (`Import | ImportFrom`): An AST node representing an import statement.

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
*   **Methods:**
    *   **`__init__`**
        *   *Description:* Initializes the LLMHelper.
        *   *Parameters:* 
          - **self**
          - **api_key** (`str`): API key for accessing the language model service.
          - **function_prompt_path** (`str`): Path to the file containing the system prompt for function documentation.
          - **class_prompt_path** (`str`): Path to the file containing the system prompt for class documentation.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
*   **Methods:**
    *   **`__init__`**
        *   *Description:* Initializes the MainLLM.
        *   *Parameters:* 
          - **self**
          - **api_key** (`str`): The API key used for authenticating with the LLM provider.
          - **prompt_file_path** (`str`): The file path to the system prompt.
          - **model_name** (`str`): The name of the model to use.
          - **base_url** (`str`): Optional base URL for connecting to a custom LLM endpoint.

## Conclusion

---
</end.documentation>
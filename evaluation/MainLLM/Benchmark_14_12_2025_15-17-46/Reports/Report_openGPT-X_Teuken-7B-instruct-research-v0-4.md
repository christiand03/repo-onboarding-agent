# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
    aktueller_status: Information not found
    key_features: Information not found
    tech_stack: Information not found

## 2. Installation 
    ### Dependencies
    - aaltair==4.2.2
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
    - httpcore==1.0.9
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
    - pyarrow==2.1.0
    - pyas1==0.6.1
    - pyasn1==0.4.2
    - pycparser==2.23
    - pydantic==2.12.4
    - pydantic_core==2.41.5
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
    - streamlit-authenticator==0.2.5
    - tenacity==9.1.2
    - tiktoken==0.12.0
    - toml==0.10.2
    - toolz==1.1.0
    - toon-format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c99006de6
    - tornado==6.5.2
    - tqdm==4.67.1
    - typing-inspection==0.4.2
    - typing_extensions==4.15.0
    - tzdata==2025.2
    - url3==2.5.0
    - watchdog==6.0.0
    - xxhash==3.6.0
    - zstandard==0.25.0

    ### Setup Guide
    Information not found

    ### Quick Startup
    Information not found

## 3. Use Cases & Commands
Information not found

## 4. Architecture

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** null
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* null
    *   *Parameters:* `self`, `source_code`, `file_path`, `project_root`
*   **Methods:**
    ##### visit_Import
    *   **Signature:** `visit_Import(self, node)`
    *   **Description:** Handles import statements in the AST by extracting the names of imported modules and appending them to the schema's imports list. It processes each alias in the import statement and adds it to the list before continuing the generic visit.
    *   **Parameters:** 
      - **node** (`ast.Import`): The AST node representing an import statement.
    ##### visit_ImportFrom
    *   **Signature:** `visit_ImportFrom(self, node)`
    *   **Description:** Handles 'from ... import ...' statements in the AST by extracting the full module paths of imported items and appending them to the schema's imports list. It constructs the full qualified name for each imported item and appends it to the list before continuing the generic visit.
    *   **Parameters:** 
      - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
    ##### visit_ClassDef
    *   **Signature:** `visit_ClassDef(self, node)`
    *   **Description:** 
    Processes class definitions in the AST by creating a structured representation of the class and adding it to the schema. It assigns a unique identifier based on the module path and class name, extracts docstrings and source code segments, and tracks start and end lines. It also sets the current class context for subsequent function processing.
    *   **Parameters:** 
      - **node** (`ast.ClassDef`): The AST node representing a class definition.
    ##### visit_FunctionDef
    *   **Signature:** `visit_FunctionDef(self, node)`
    *   **Description:** 
    Handles function definitions in the AST by either associating them with the current class context or adding them as top-level functions to the schema. It generates identifiers for functions based on their context (either module or class), extracts arguments, docstrings, and source code segments, and tracks line numbers. If the function is within a class, it stores the function information in the class's context.
    *   **Parameters:** 
      - **node** (`ast.FunctionDef`): The AST node representing a function definition.
    ##### visit_AsyncFunctionDef
    *   **Signature:** `visit_AsyncFunctionDef(self, node)`
    *   **Description:** 
    Handles asynchronous function definitions in the AST by delegating to the visit_FunctionDef method. This allows async functions to be processed in the same way as regular functions, maintaining consistent handling of both sync and async function definitions.
    *   **Parameters:** 
      - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.

#### Class: `ASTAnalyzer`
*   **Summary:** null
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any operations.
    *   *Parameters:* `self`
*   **Methods:**
    ##### _enrich_schema_with_callgraph
    *   **Signature:** `_enrich_schema_with_callgraph(schema, call_graph, filename)`
    *   **Description:** 
    This static method enriches a given schema with call graph information by updating function and method contexts with details about which functions they call and which functions call them. It iterates over functions and class methods in the schema and updates their context fields based on the provided call graph.
    *   **Parameters:** 
      - **schema** (`dict`): A dictionary representing the schema of a parsed file, containing functions and classes.
      - **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions.
      - **filename** (`str`): The path of the file being processed, used to construct unique keys for lookup in the call graph.
    ##### merge_relationship_data
    *   **Signature:** `merge_relationship_data(self, full_schema, relationship_data)`
    *   **Description:** 
    This method merges relationship data into a full schema by mapping identifiers from relationship data to corresponding entries in the schema. It updates function and class contexts with 'called_by' information and class contexts with 'instantiated_by' information based on the provided relationship data.
    *   **Parameters:** 
      - **full_schema** (`dict`): A dictionary representing the full schema of the repository, containing file structures and AST nodes.
      - **relationship_data** (`list`): A list of dictionaries containing relationship information, including identifiers and called_by lists.
    ##### analyze_repository
    *   **Signature:** `analyze_repository(self, files, repo)`
    *   **Description:** 
    This method analyzes a list of Python files within a Git repository by parsing their ASTs, visiting nodes to extract schema information, and enriching that schema with call graph data. It constructs a full schema of files, functions, and classes, handling potential parsing errors gracefully.
    *   **Parameters:** 
      - **files** (`list`): A list of file objects containing paths and content of Python files to be analyzed.
      - **repo** (`GitRepository`): An object representing the Git repository containing the files to be analyzed.

---
</SystemPrompt>
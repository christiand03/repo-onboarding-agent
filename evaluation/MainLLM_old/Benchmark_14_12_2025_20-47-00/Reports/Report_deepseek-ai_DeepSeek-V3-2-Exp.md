# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
      - Could not be determined due to a missing README file and insufficient context.
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** 
      - Information not found

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
- dns-python==2.8.0
- dotenv==0.9.9
- entrypoints==0.4
- extra-streamlit-components==0.1.81
- filetype==1.2.0
- fonttools==4.61.0
- gidgethub==4.0.12
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
- langchain-ollama==1.1.0
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
- setuptools==69.0.1
- six==1.17.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.27.0
- streamlit-mermaid==0.1.0
- tenacity==9.1.2
- tiktoken==0.12.0
- toml==0.10.2
- toolz==1.1.0
- toon-format==0.1.0
- tornadotools==6.5.2
- tqdm==4.67.1
- typing-inspection==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2

### Setup Guide
Information not found

### Quick Startup
Information not found

## 3. Use Cases & Commands
The repository appears to be for an onboarding agent. There may be commands related to user onboarding and configuration.

## 4. Architecture
No Mermaid Syntax is provided.

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** A class used to traverse an Abstract Syntax Tree (AST) generated from Python source code. It collects information about imports, classes, and functions, organizing them into a structured schema.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It sets up internal tracking variables such as module path, schema structure, and current class context.
    *   *Parameters:* `self`, `source_code`, `file_path`, `project_root`
*   **Methods:**
    ##### visit_Import
    *   **Signature:** `visit_Import(self, node)`
    *   **Description:** Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list.
    *   **Parameters:** `self`, `node`
    *   **Returns:** 
    *   **Usage:** 
    ##### visit_ImportFrom
    *   **Signature:** `visit_ImportFrom(self, node)`
    *   **Description:** Processes import-from nodes in the AST by collecting the fully qualified names of imported items and adding them to the schema's imports list.
    *   **Parameters:** `self`, `node`
    *   **Returns:** 
    *   **Usage:** 
    ##### visit_ClassDef
    *   **Signature:** `visit_ClassDef(self, node)`
    *   **Description:** Handles class definition nodes in the AST by creating a structured representation of the class, including its identifier, name, docstring, and source code segment.
    *   **Parameters:** `self`, `node`
    *   **Returns:** 
    *   **Usage:** 
    ##### visit_FunctionDef
    *   **Signature:** `visit_FunctionDef(self, node)`
    *   **Description:** Processes function definition nodes in the AST. If a class context is active, it records the function as a method of that class. Otherwise, it treats the function as a top-level function and adds it to the schema accordingly.
    *   **Parameters:** `self`, `node`
    *   **Returns:** 
    *   **Usage:** 
    ##### visit_AsyncFunctionDef
    *   **Signature:** `visit_AsyncFunctionDef(self, node)`
    *   **Description:** Handles asynchronous function definition nodes in the AST by delegating to the standard function definition handler.
    *   **Parameters:** `self`, `node`
    *   **Returns:** 
    *   **Usage:** 

#### Class: `ASTAnalyzer`
*   **Summary:** A class responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any initialization actions.
    *   **Parameters:** 
*   **Methods:**
    ##### _enrich_schema_with_callgraph
    *   **Signature:** `_enrich_schema_with_callgraph(self, schema, call_graph, filename)`
    *   **Description:** Enriches a given schema with call graph information by adding 'calls' and 'called_by' details for functions and methods based on a provided call graph.
    *   **Parameters:** `self`, `schema`, `call_graph`, `filename`
    *   **Returns:** 
    *   **Usage:** 
    ##### merge_relationship_data
    *   **Signature:** `merge_relationship_data(self, full_schema, relationship_data)`
    *   **Description:** Merges relationship data into a full schema by updating function and class context with 'called_by' information.
    *   **Parameters:** `self`, `full_schema`, `relationship_data`
    *   **Returns:** `full_schema`
    *   **Usage:** 
    ##### analyze_repository
    *   **Signature:** `analyze_repository(self, files, repo)`
    *   **Description:** Analyzes a repository by processing a list of files, parsing their content into ASTs, and generating a schema for each file.
    *   **Parameters:** `self`, `files`, `repo`
    *   **Returns:** `full_schema`
    *   **Usage:** 

---
</SystemPrompt>
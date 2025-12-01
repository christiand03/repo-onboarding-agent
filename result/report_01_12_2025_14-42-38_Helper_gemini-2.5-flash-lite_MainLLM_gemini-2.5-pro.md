# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated documentation agent designed to analyze Git repositories. It clones a given repository, constructs an Abstract Syntax Tree (AST) to understand the code structure, and leverages a multi-LLM pipeline (Helper and Main LLMs) to generate comprehensive technical documentation. The final report is presented through an interactive Streamlit-based web frontend.
- **Key Features:**
  - **Git Repository Analysis:** Clones remote Git repositories for local analysis.
  - **AST Generation:** Parses Python code into Abstract Syntax Trees to map code structure and relationships.
  - **Multi-LLM Pipeline:** Utilizes specialized "Helper" LLMs for detailed code analysis and a "Main" LLM to synthesize the final documentation.
  - **Automated Documentation:** Generates a complete technical report, including overviews, architecture, and detailed code analysis.
  - **Interactive Frontend:** Provides a web interface using Streamlit for user interaction and displaying results.
- **Tech Stack:** Streamlit, LangChain, GitPython, NetworkX, Pydantic, Google Generative AI, Ollama.

*   **Repository Structure:**
    ```mermaid
    graph TD
      root["/ (root)"]

      root_files[".env.example<br/>.gitignore<br/>analysis_output.json<br/>readme.md<br/>requirements.txt"]
      root --> root_files

      SystemPrompts["SystemPrompts/"]
      root --> SystemPrompts
      SystemPrompts_files["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt"]
      SystemPrompts --> SystemPrompts_files

      backend["backend/"]
      root --> backend
      backend_files["AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py"]
      backend --> backend_files

      database["database/"]
      root --> database
      database_files["db.py"]
      database --> database_files

      frontend["frontend/"]
      root --> frontend
      frontend_files["Frontend.py<br/>__init__.py"]
      frontend --> frontend_files
      
      gifs["frontend/gifs/"]
      frontend --> gifs
      gifs_files["4j.gif"]
      gifs --> gifs_files

      notizen["notizen/"]
      root --> notizen
      notizen_files["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
      notizen --> notizen_files
      
      grafiken["notizen/grafiken/"]
      notizen --> grafiken
      grafiken_files["File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot"]
      grafiken --> grafiken_files
      
      result["result/"]
      root --> result
      result_files["ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>..."]
      result --> result_files
      
      schemas["schemas/"]
      root --> schemas
      schemas_files["types.py"]
      schemas --> schemas_files
    ```

## 2. Installation
### Dependencies
As this project contains a `requirements.txt` file, you can install all dependencies with the following command:
```bash
pip install -r requirements.txt
```
The dependencies include:
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
- cryptography==46.0.3
- dnspython==2.8.0
- dotenv==0.9.9
- entrypoints==0.4
- extra-streamlit-components==0.1.81
- filetype==1.2.0
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
- jsonpatch==1.33
- jsonpointer==3.0.0
- jsonschema==4.25.1
- jsonschema-specifications==2025.9.1
- langchain==1.0.8
- langchain-core==1.1.0
- langchain-google-genai==3.1.0
- langchain-ollama==1.0.0
- langgraph==1.0.3
- langgraph-checkpoint==3.0.1
- langgraph-prebuilt==1.0.5
- langgraph-sdk==0.2.9
- langsmith==0.4.46
- MarkupSafe==3.0.3
- narwhals==2.12.0
- networkx==3.6
- numpy==2.3.5
- ollama==0.6.1
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
- python-dateutil==2.9.0.post0
- python-dotenv==1.2.1
- pytz==2025.2
- PyYAML==6.0.3
- referencing==0.37.0
- requests==2.32.5
- requests-toolbelt==1.0.0
- rpds-py==0.29.0
- rsa==4.9.1
- six==1.17.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.51.0
- streamlit-authenticator==0.4.2
- streamlit-mermaid==0.3.0
- tenacity==9.1.2
- toml==0.10.2
- toolz==1.1.0
- toon_format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c90006de6
- tornado==6.5.2
- typing-inspection==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0

### Setup Guide
1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd repo-onboarding-agent
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment Variables:**
    - Copy the example environment file: `cp .env.example .env`
    - Edit the `.env` file to add your API keys (e.g., for Gemini, OpenAI) and any other required configurations like database connection strings.

### Quick Startup
To run the application and start the web interface, execute the following command from the root directory:
```bash
streamlit run frontend/Frontend.py
```

## 3. Use Cases & Commands
The primary use case for this application is to automatically generate comprehensive technical documentation for a given software project hosted in a Git repository.

**Workflow:**
1.  Launch the application using the Quick Startup command.
2.  The Streamlit web interface will open in your browser.
3.  Input the URL of a public Git repository into the designated field.
4.  Provide the necessary API keys for the selected Large Language Models (LLMs).
5.  Initiate the analysis process. The agent will clone the repository, analyze its structure and code, and generate a full documentation report, which will be displayed on the page.

**Primary Command:**
The main command to operate the tool is for running the frontend:
```bash
streamlit run frontend/Frontend.py
```

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It specifically focuses on extracting information about imports, classes, and functions within the code. The visitor populates a schema dictionary with this extracted data, organizing it into 'imports', 'functions', and 'classes' categories. It maintains state about the current class being visited to correctly attribute methods.
*   **Instantiation:** This class is instantiated by the `analyze_repository` function in the `AST_Schema.py` file on line 175.
*   **Dependencies:** This class depends on the 'ast' module for parsing Python code's Abstract Syntax Tree and a function `path_to_module` (presumably defined elsewhere) to convert file paths to module paths.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with the source code, file path, and project root. It sets up instance variables to store this information and derives the module path. It also initializes an empty schema dictionary to store extracted AST information and sets the current class context to None.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the source code file.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Visits an ast.Import node to extract imported module names. It iterates through the aliases in the import statement and appends the name of each imported module to the 'imports' list within the schema. After processing, it calls generic_visit to continue traversal.
        *   *Parameters:*
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
            - No return value.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Visits an ast.ImportFrom node to extract names imported from a specific module. It iterates through the aliases and constructs a fully qualified name (module.name) to append to the 'imports' list in the schema. It then calls generic_visit to ensure further traversal.
        *   *Parameters:*
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
            - No return value.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Visits an ast.ClassDef node to extract information about a class definition. It constructs a unique identifier for the class, gathers its name, docstring, source code segment, and line numbers. This information is stored in a dictionary which is then appended to the 'classes' list in the schema. It also sets the current class context for subsequent method visits and then continues the traversal.
        *   *Parameters:*
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            - No return value.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Visits an ast.FunctionDef node, which represents either a regular function or a method within a class. If currently inside a class definition (_current_class is set), it extracts method details like identifier, name, arguments, docstring, and line numbers, storing them in the class's context. If not within a class, it extracts function details and adds them to the 'functions' list in the schema. It then proceeds with generic traversal.
        *   *Parameters:*
            - **node** (`ast.FunctionDef`): The AST node representing a function or method definition.
        *   *Returns:*
            - No return value.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Visits an ast.AsyncFunctionDef node, which represents an asynchronous function or method. This method simply delegates the visit to `visit_FunctionDef`, effectively treating asynchronous functions the same way as regular functions for the purpose of schema generation.
        *   *Parameters:*
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function or method definition.
        *   *Returns:*
            - No return value.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is designed to process a collection of Python files, parse their Abstract Syntax Trees (ASTs), build call graphs, and enrich the schema with relationship data. It aggregates information about functions, classes, and methods across a repository, providing a comprehensive overview of the codebase's structure and interdependencies. This class acts as a central component for analyzing and understanding the relationships within a software project.
*   **Instantiation:** This class is instantiated by the main_workflow function in main.py.
*   **Dependencies:** This class depends on the 'ast' module for parsing Python code, the 'networkx' library for graph manipulation (specifically for call graphs), and the 'os' module for path operations. It also relies on a function `build_callGraph` from the `callgraph` module and an `ASTVisitor` class, presumably defined elsewhere.
*   **Constructor:**
    *   *Description:* Initializes the ASTAnalyzer instance. Currently, the constructor does not perform any specific setup or attribute initialization, as indicated by the 'pass' statement.
    *   *Parameters:*
        - No parameters.
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* This static method enriches a given schema dictionary with call graph information. It iterates through functions and methods defined in the schema and, using a provided networkx DiGraph representing the call graph and the filename, it populates the 'calls' and 'called_by' fields within the schema's context. This method is crucial for adding detailed relationship data derived from static analysis to the schema.
        *   *Parameters:*
            - **schema** (`dict`): The schema dictionary to be enriched with call graph data.
            - **call_graph** (`nx.DiGraph`): A networkx directed graph representing the call graph of the code.
            - **filename** (`str`): The name of the file for which the call graph is generated.
        *   *Returns:*
            - No return value.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
        *   *Description:* This method merges relationship data, such as 'called_by' and 'instantiated_by' information, into a comprehensive schema. It first creates a lookup dictionary from the provided relationship data. Then, it iterates through the files and their corresponding AST nodes within the full schema, updating the 'called_by' field for functions and methods, and the 'instantiated_by' field for classes with the data from the lookup. This process consolidates relationship information across the repository.
        *   *Parameters:*
            - **full_schema** (`dict`): The complete schema dictionary containing file and AST node information.
            - **relationship_data** (`list`): A list of dictionaries, where each dictionary contains relationship information like 'identifier' and 'called_by'.
        *   *Returns:*
            - **full_schema** (`dict`): The updated schema dictionary with merged relationship data.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files)`
        *   *Description:* This method orchestrates the analysis of an entire software repository. It initializes a full schema, determines the project root, and then iterates through each file. For Python files, it parses the content into an AST, uses an ASTVisitor to extract schema information, builds a call graph, and enriches the schema with call graph data. It handles potential parsing errors and aggregates the processed file schemas into a single output dictionary. This is the primary method for initiating the repository-wide analysis.
        *   *Parameters:*
            - **files** (`list`): A list of file objects, where each object contains file path and content.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary representing the aggregated schema of the repository, including file paths and their corresponding AST nodes.

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into a Python module path relative to a specified project root. It handles potential `ValueError` exceptions during relative path calculation by falling back to the base filename. It also strips the '.py' extension and replaces directory separators with dots to form the module path. Special handling is included for '__init__.py' files, returning the parent directory's module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path string.
*   **Usage:** The function utilizes os.path.relpath for relative path calculation, os.path.basename as a fallback, and string methods like endswith and replace for path manipulation. This function is called by the __init__ method within the AST_Schema.py file.
---
### File: `backend/File_Dependency.py`
*Analysis data not available for this component.*
---
### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class is designed to interact with various Large Language Models (LLMs) for generating and validating code documentation. It centralizes API interactions, handles prompt loading, configures model-specific batch sizes, and manages batched API calls with rate limiting. The class supports different LLM providers like Google Generative AI, OpenAI, and Ollama, and is capable of producing structured output for both function and class analyses.
*   **Instantiation:** The LLMHelper class is instantiated in `HelperLLM.py` within the `main_orchestrator` function and in `main.py` within the `main_workflow` function.
*   **Dependencies:** This class relies on several external libraries for LLM interactions, including `langchain_google_genai`, `langchain_ollama`, and `langchain_openai`. It also uses Pydantic for data validation (`FunctionAnalysis`, `ClassAnalysis`, `FunctionAnalysisInput`, `ClassAnalysisInput`) and standard Python libraries like `json`, `logging`, and `time` for data handling, logging, and execution control.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with necessary API keys, prompt file paths, and model configurations. It loads system prompts for function and class documentation, sets up batch processing parameters based on the chosen model, and instantiates the appropriate LLM client (Google Generative AI, OpenAI, or Ollama). It also configures the LLM to output structured data conforming to FunctionAnalysis and ClassAnalysis schemas.
    *   *Parameters:*
        - **api_key** (`str`): The API key required to authenticate with the LLM service.
        - **function_prompt_path** (`str`): The file path to the system prompt used for function documentation generation.
        - **class_prompt_path** (`str`): The file path to the system prompt used for class documentation generation.
        - **model_name** (`str`): The name of the LLM model to use (e.g., 'gemini-2.0-flash-lite'). Defaults to 'gemini-2.0-flash-lite'.
        - **ollama_base_url** (`str`): The base URL for Ollama if using an Ollama model. Defaults to a predefined OLLAMA_BASE_URL if not provided.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* This method configures the batch size for API calls based on the specified model name. Different LLM models have varying token limits and optimal processing batch sizes. It sets an appropriate `self.batch_size` attribute to manage how many requests can be sent in a single API call, with a default conservative setting for unknown models. It also logs a warning for unrecognized model names.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model currently in use.
        *   *Returns:*
            - No return value.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* This method generates and validates documentation for a list of function inputs. It takes a list of `FunctionAnalysisInput` objects, converts them into JSON payloads, and constructs conversation prompts using a predefined system prompt. The method then processes these inputs in batches, respecting the configured `BATCH_SIZE` and adding delays between batches to avoid rate limiting. It calls the LLM API using `self.function_llm.batch` and handles potential exceptions during the API calls, returning a list of validated `FunctionAnalysis` objects or `None` for failed batches.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of FunctionAnalysisInput objects, each containing the necessary information to generate documentation for a function.
        *   *Returns:*
            - **all_validated_functions** (`List[Optional[FunctionAnalysis]]`): A list containing the generated and validated FunctionAnalysis objects for each input, or None if an error occurred during processing for a specific batch.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* This method generates and validates documentation for a list of class inputs. Similar to `generate_for_functions`, it takes a list of `ClassAnalysisInput` objects, serializes them into JSON, and prepares conversation prompts using the class system prompt. It processes these inputs in batches, adhering to `self.batch_size` and incorporating delays for rate limiting. The method invokes the LLM API via `self.class_llm.batch`, manages potential exceptions, and returns a list of validated `ClassAnalysis` objects or `None` for any failed batches.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of ClassAnalysisInput objects, each containing the necessary information to generate documentation for a class.
        *   *Returns:*
            - **all_validated_classes** (`List[Optional[ClassAnalysis]]`): A list containing the generated and validated ClassAnalysis objects for each input, or None if an error occurred during processing for a specific batch.

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** The `main_orchestrator` function serves as a testing and demonstration harness for the `LLMHelper` class. It simulates the process of analyzing Python functions and classes by defining dummy input data and pre-computed analysis results for several methods (`add_item`, `check_stock`, `generate_report`) belonging to an `InventoryManager` class. It then instantiates an `LLMHelper` object and calls its `generate_for_functions` method with the prepared inputs. Finally, it processes the results, aggregates them into a dictionary, and prints the final documentation as a JSON string.
*   **Parameters:**
    - No parameters.
*   **Returns:**
    - No return value.
*   **Usage:** This function calls `ClassAnalysisInput`, `ClassContextInput`, `LLMHelper`, `dumps`, `generate_for_functions`, `info`, `model_dump`, `model_validate`, `print`, and `warning`. This function is called by `backend.HelperLLM` in the file `HelperLLM.py`.
---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class is the central component for interacting with Large Language Models (LLMs). It handles initialization with API keys and model configurations, loads system prompts from files, and provides methods to either get a direct response or stream responses from the LLM. It supports different LLM providers like Google Generative AI and Ollama based on the model name provided.
*   **Instantiation:** This class is instantiated within the main_workflow function in the main.py file.
*   **Dependencies:** This class relies on external libraries for LLM interactions, specifically ChatGoogleGenerativeAI from langchain_google_genai and ChatOllama from langchain_ollama. It also uses logging for output and standard Python file operations.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM class by setting up the LLM client. It validates the API key, loads the system prompt from a specified file, and configures the appropriate LLM client (ChatGoogleGenerativeAI or ChatOllama) based on the model name. It logs the initialization status and any file loading errors.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the LLM service.
        - **prompt_file_path** (`str`): The file path to the system prompt that will be used for all LLM interactions.
        - **model_name** (`str`): The name of the LLM model to use. Defaults to 'gemini-2.5-pro'.
        - **ollama_base_url** (`str`): The base URL for the Ollama service, used if the model name indicates an Ollama model. Defaults to a predefined OLLAMA_BASE_URL if not provided.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method sends a user's input to the configured LLM and returns the model's response content. It constructs a message list containing the system prompt and the user's input, then invokes the LLM client. It logs the process and handles potential exceptions during the LLM call, returning None if an error occurs.
        *   *Parameters:*
            - **user_input** (`str`): The input string provided by the user to be processed by the LLM.
        *   *Returns:*
            - **response.content** (`str`): The content of the LLM's response, or None if an error occurred.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method initiates a streaming call to the LLM, yielding chunks of the response content as they become available. It constructs the message list similarly to `call_llm` and then uses the LLM client's stream method. Any errors during the streaming process are logged, and an error message is yielded.
        *   *Parameters:*
            - **user_input** (`str`): The input string provided by the user for the streaming LLM interaction.
        *   *Returns:*
            - **chunk.content** (`str`): Yields chunks of the LLM's response content as they are received, or an error message if an exception occurs.
---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract fundamental project information from common project files such as README, pyproject.toml, and requirements.txt. It initializes a structured dictionary to hold project overview and installation details, populating it by parsing these files in a prioritized order. The class aims to provide a consolidated view of project metadata, including title, description, key features, tech stack, installation instructions, and dependencies.
*   **Instantiation:** The `ProjektInfoExtractor` class is instantiated within the `main_workflow` function in the `main.py` file.
*   **Dependencies:** This class relies on standard Python libraries such as `re` for regular expressions, `os` for path manipulation, and `typing` for type hints. It also conditionally uses `tomllib` for parsing TOML files, printing a warning if it's not installed.
*   **Constructor:**
    *   *Description:* Initializes the ProjektInfoExtractor by setting up a default structure for project information and defining a constant for indicating when information is not found. The `self.info` attribute is a dictionary pre-populated with placeholders for project overview and installation details.
    *   *Parameters:*
        - **self** (`ProjektInfoExtractor`): The instance of the class.
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches through a list of file objects to find a file that matches one of the provided patterns. The search is case-insensitive, comparing the lowercase version of the file path's suffix with the lowercase patterns. It returns the first matching file object found or None if no match is identified.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **patterns** (`List[str]`): A list of file name patterns (e.g., ['.md', 'requirements.txt']) to search for.
            - **dateien** (`List[Any]`): A list of file objects, where each object is expected to have a 'path' attribute.
        *   *Returns:*
            - **Optional[Any]** (`Optional[Any]`): The first file object that matches any of the patterns, or None if no file matches.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private helper method extracts a specific section of text from a Markdown content string. It uses regular expressions to find a section that starts with a Markdown heading (##) followed by one of the provided keywords. The method captures all text following the heading until it encounters another heading or the end of the file. It is designed to handle variations in keywords and case-insensitivity.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The full Markdown content as a string.
            - **keywords** (`List[str]`): A list of alternative keywords that can be used as section titles (e.g., ['Features', 'Key Features']).
        *   *Returns:*
            - **Optional[str]** (`Optional[str]`): The extracted text content of the section, stripped of leading/trailing whitespace, or None if the section is not found.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This private method parses the content of a README file to extract various pieces of project information. It attempts to find the project title from the main heading, a description from the text following the title, key features, tech stack, current status, installation instructions, and quick start guide by calling the `_extrahiere_sektion_aus_markdown` helper. It updates the `self.info` dictionary with the extracted data, using the README content as a fallback for information not found in other files.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the README file as a string.
        *   *Returns:*
            - No return value.
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This private method parses the content of a `pyproject.toml` file using the `tomllib` library. It attempts to extract the project name, description, and dependencies from the `[project]` section of the TOML data. If `tomllib` is not available, it prints a warning. It also handles potential `TOMLDecodeError` exceptions during parsing, printing a warning if an error occurs. The extracted dependencies overwrite any previously found dependencies due to `pyproject.toml` having the highest priority.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the pyproject.toml file as a string.
        *   *Returns:*
            - No return value.
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This private method parses the content of a `requirements.txt` file to extract a list of dependencies. It only proceeds if dependencies have not already been found and set from a `pyproject.toml` file. The method splits the content into lines, filters out empty lines and comments (lines starting with '#'), and stores the remaining lines as dependencies. If any dependencies are found, they are added to the `self.info['installation']['dependencies']` field.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the requirements.txt file as a string.
        *   *Returns:*
            - No return value.
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This public method orchestrates the extraction of project information from a provided list of file objects and a repository URL. It first identifies relevant files (README, pyproject.toml, requirements.txt) using `_finde_datei`. Then, it parses these files in a specific order of priority: `pyproject.toml` first, followed by `requirements.txt`, and finally README. This prioritization ensures that metadata from `pyproject.toml` takes precedence. After parsing, it formats the dependencies and sets the project title based on the repository URL. The method returns a dictionary containing all the extracted project information.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **dateien** (`List[Any]`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo_url** (`str`): The URL of the repository, used to derive the project name.
        *   *Returns:*
            - **Dict[str, Any]** (`Dict[str, Any]`): A dictionary containing the extracted project information, structured into 'projekt_uebersicht' and 'installation' sections.
---
### File: `backend/callgraph.py`
*Analysis data not available for this component.*
---
### File: `backend/getRepo.py`
*Analysis data not available for this component.*
---
### File: `backend/main.py`
#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep times from the total duration. It is specifically designed to account for rate-limiting delays when processing items in batches, particularly for models starting with 'gemini-'. If the model name does not start with 'gemini-', the total duration is returned directly. If there are no items to process, the net time is zero. Otherwise, it calculates the number of batches, the total sleep time based on the number of batches, and then subtracts this from the total duration, ensuring the net time is not negative.
*   **Parameters:**
    - **start_time** (`Any`): The timestamp when the process started.
    - **end_time** (`Any`): The timestamp when the process ended.
    - **total_items** (`int`): The total number of items being processed.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model being used, used to determine if rate-limiting logic should be applied.
*   **Returns:**
    - **net_time** (`Any`): The calculated net processing time after subtracting estimated sleep times, or the total duration if rate-limiting logic is not applicable. Returns 0 if total_items is 0.
*   **Usage:** This function calls math.ceil to determine the number of batches, math.max to ensure sleep count is non-negative and net time is non-negative, and the string method startswith to check the model name. This function is called by the main_workflow function in main.py at lines 265 and 296.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** The `main_workflow` function orchestrates a complex process of analyzing a given input, which is expected to contain a repository URL. It begins by extracting API keys and model names, then clones the specified repository. Following this, it performs several analysis steps: extracting basic project information, constructing a file tree, analyzing relationships (calls and instantiations), and creating an Abstract Syntax Tree (AST). The AST is then enriched with the relationship data. The function prepares inputs for a 'Helper LLM' to analyze functions and classes within the repository, generating documentation for each. Finally, it prepares an input for a 'Main LLM' using the collected information and analysis results to generate a final report. The function also handles status updates via a callback and logs various stages of the process. It returns the generated report and performance metrics.
*   **Parameters:**
    - **input** (`Any`): The primary input to the workflow, expected to contain a repository URL.
    - **api_keys** (`dict`): A dictionary containing API keys for different services (e.g., 'gemini', 'gpt', 'ollama').
    - **model_names** (`dict`): A dictionary specifying the model names to be used for helper and main LLM tasks.
    - **status_callback** (`Callable`): An optional callback function to report the status of the workflow's progress.
*   **Returns:**
    - **report** (`str`): The final generated report from the Main LLM.
    - **metrics** (`dict`): A dictionary containing performance metrics of the workflow, including helper and main LLM times, total time, and models used.
*   **Usage:** This function calls various internal helper functions and external classes such as `GitRepository`, `ProjektInfoExtractor`, `ProjectAnalyzer`, `ASTAnalyzer`, `LLMHelper`, and `MainLLM`. It also uses standard library modules like `logging`, `os`, `re`, `json`, and `time`. This function is called by `Frontend.py` (specifically within the `frontend.Frontend` class) and `main.py` (within the `backend.main` module).

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function is designed to report status updates. It first checks if a `status_callback` function is defined and, if so, calls it with the provided message. Subsequently, it logs the message using the `logging.info` method. This dual approach ensures that status messages are both communicated through a callback mechanism and recorded for logging purposes.
*   **Parameters:**
    - **msg** (`Any`): The status message to be reported and logged.
*   **Returns:**
    - No return value.
*   **Usage:** This function calls the `logging.info` method and potentially a `status_callback` function. This function is invoked multiple times from the `main_workflow` function in `main.py`.
---
### File: `backend/relationship_analyzer.py`
*Analysis data not available for this component.*
---
### File: `database/db.py`
*Analysis data not available for this component.*
---
### File: `frontend/Frontend.py`
*Analysis data not available for this component.*
---
### File: `schemas/types.py`
*Analysis data not available for this component.*
---
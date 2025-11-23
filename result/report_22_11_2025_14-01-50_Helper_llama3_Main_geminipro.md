# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated documentation agent designed to analyze a given Git repository. It clones the repository, parses the source code to build an Abstract Syntax Tree (AST) and a call graph, and then uses a Large Language Model (LLM) to generate comprehensive technical documentation based on the analysis.
- **Key Features:**
  - Clones remote Git repositories for local analysis.
  - Parses Python source code to build a detailed Abstract Syntax Tree (AST).
  - Generates call graphs to understand function and method relationships.
  - Leverages Google's Gemini LLM to analyze code components and generate human-readable descriptions.
  - Utilizes Pydantic for strict data structuring and validation throughout the pipeline.
- **Tech Stack:** Python, LangChain, Google Generative AI, Pydantic, NetworkX, GitPython.

*   **Repository Structure:**
    ```mermaid
    graph LR;
        subgraph root
            A0["<b>/</b><br/>.env.example<br/>.gitignore<br/>analysis_output.json<br/>readme.md<br/>requirements.txt"]
        end

        subgraph SystemPrompts
            B0["SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt"]
        end

        subgraph backend
            C0["AST_Schema.py<br/>HelperLLM.py<br/>MainLLM.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>tools.py"]
        end

        subgraph frontend
            D0["Frontend.py"]
        end

        subgraph notizen
            E0["Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md"]
        end

        subgraph notizen/grafiken
            F0["AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot"]
        end

        subgraph result
            G0["report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md"]
        end
        
        subgraph schemas
            H0["types.py"]
        end

        root --> SystemPrompts;
        root --> backend;
        root --> frontend;
        root --> notizen;
        notizen --> E0;
        notizen --> grafiken;
        grafiken --> F0;
        root --> result;
        root --> schemas;
        SystemPrompts --> B0;
        backend --> C0;
        frontend --> D0;
        result --> G0;
        schemas --> H0;
    ```

    ## 2. Installation
    ### Dependencies
    - langchain 
    - langchain-core 
    - langchain-google-genai 
    - google-generativeai 
    - python-dotenv 
    - pydantic 
    - regex 
    - networkx 
    - gitPython

    Since a `requirements.txt` file is present, you can install all dependencies with a single command:
    ```bash
    pip install -r requirements.txt
    ```
    ### Setup Guide
    1.  **Clone the repository:**
        ```bash
        git clone https://github.com/christiand03/repo-onboarding-agent.git
        cd repo-onboarding-agent
        ```
    2.  **Install dependencies:**
        ```bash
        pip install -r requirements.txt
        ```
    3.  **Set up environment variables:**
        -   Copy the `.env.example` file to a new file named `.env`.
        -   Open the `.env` file and add your Google Gemini API key:
            ```
            GEMINI_API_KEY="YOUR_API_KEY_HERE"
            ```
    ### Quick Startup
    To run the analysis pipeline, execute the main script:
    ```bash
    python backend/main.py
    ```

    ## 3. Use Cases & Commands
    The primary use case for this agent is to automatically generate technical documentation for a software project hosted in a Git repository.

    **Primary Command:**
    The core functionality is triggered by running the `main.py` script located in the `backend` directory. The script currently has a hardcoded repository URL inside the `main_workflow` function. To analyze a different repository, you would need to modify this line:

    ```python
    # in backend/main.py
    user_input = "Analyze the following Git Repository https://github.com/your/repository-url" 
    ```

    Upon execution, the agent performs the following steps:
    1.  Clones the specified repository.
    2.  Analyzes the file structure and basic metadata (from README, etc.).
    3.  Parses all Python files to create an AST.
    4.  Builds a call graph to map relationships between functions and methods.
    5.  Sends the structured code analysis to the Helper LLM for detailed description generation.
    6.  Synthesizes all collected information into a final Markdown report using the Main LLM.
    7.  Saves the generated report to the `result/` directory.

    ## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added


## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is a visitor pattern implementation for Abstract Syntax Trees (ASTs). It provides methods to traverse and analyze the structure of Python source code.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTVisitor with source code and schema information. It sets up internal data structures to store imports, functions, and classes.
    *   *Parameters:*
        - **source_code** (`str`): The source code string
        - **schema** (`dict`): Internal schema data structure
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, source_code)`
        *   *Description:* Initializes the ASTVisitor with source code and schema information.
        *   *Parameters:*
            - **self** (`object`): The current object instance
            - **source_code** (`str`): The source code string
        *   *Returns:* *No return value.*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Visits an Import node in the AST and appends imports to the schema.
        *   *Parameters:*
            - **self** (`object`): The current object instance
            - **node** (`ast.Node`): The Import node
        *   *Returns:* *No return value.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Visits an ImportFrom node in the AST and appends imports to the schema.
        *   *Parameters:*
            - **self** (`object`): The current object instance
            - **node** (`ast.Node`): The ImportFrom node
        *   *Returns:* *No return value.*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Visits a ClassDef node in the AST and appends class information to the schema.
        *   *Parameters:*
            - **self** (`object`): The current object instance
            - **node** (`ast.Node`): The ClassDef node
        *   *Returns:* *No return value.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Visits a FunctionDef node in the AST and appends function information to the schema.
        *   *Parameters:*
            - **self** (`object`): The current object instance
            - **node** (`ast.Node`): The FunctionDef node
        *   *Returns:* *No return value.*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Visits an AsyncFunctionDef node in the AST and appends function information to the schema.
        *   *Parameters:*
            - **self** (`object`): The current object instance
            - **node** (`ast.Node`): The AsyncFunctionDef node
        *   *Returns:* *No return value.*

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is a static analysis tool that enriches the schema of an Abstract Syntax Tree (AST) with call graph information. It analyzes Python files, extracts their ASTs, and then builds a call graph from the parsed trees.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* The constructor initializes the ASTAnalyzer instance without any specific parameters.
    *   *Parameters:* *No parameters.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* Initializes the ASTAnalyzer instance with no specific parameters.
        *   *Parameters:*
            - **self** (`self`): The instance of the class.
        *   *Returns:* *No return value.*
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* Enriches the schema of an Abstract Syntax Tree (AST) with call graph information. It iterates through the functions and classes in the schema, enriching their 'calls' and 'called_by' contexts.
        *   *Parameters:*
            - **schema** (`dict`): The schema of an Abstract Syntax Tree (AST).
            - **call_graph** (`networkx.DiGraph`): A directed graph representing the call graph.
            - **filename** (`str`): The name of the file being analyzed.
        *   *Returns:* *No return value.*
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files)`
        *   *Description:* Analyzes a repository of Python files, extracting their ASTs and building a call graph from the parsed trees.
        *   *Parameters:*
            - **self** (`self`): The instance of the class.
            - **files** (`list`): A list of file objects to be analyzed.
        *   *Returns:*
            - **full_schema** (`dict`): The enriched schema of the repository.

---
### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class is designed to interact with Google Gemini for generating code snippet documentation. It centralizes API interaction, error handling, and validates I/O using Pydantic.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper instance by setting up the necessary attributes and configuring batch settings based on the provided model name.
    *   *Parameters:*
        - **api_key** (`str`): The API key for Google Gemini.
        - **function_prompt_path** (`str`): The path to the function system prompt file.
        - **class_prompt_path** (`str`): The path to the class system prompt file.
        - **model_name** (`str`): The name of the model to use for generating documentation (default: 'gemini-flash-latest').
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, function_prompt_path, class_prompt_path, model_name)`
        *   *Description:* Initializes the LLMHelper instance by setting up the necessary attributes and configuring batch settings based on the provided model name.
        *   *Parameters:*
            - **self** (`object`): The LLMHelper instance.
            - **api_key** (`str`): The API key for Google Gemini.
            - **function_prompt_path** (`str`): The path to the function system prompt file.
            - **class_prompt_path** (`str`): The path to the class system prompt file.
            - **model_name** (`str`): The name of the model to use for generating documentation (default: 'gemini-flash-latest').
        *   *Returns:*
            - **None** (`None`): *Description not provided.*

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** Dummy Data and processing loop for testing the LLMHelper class. This version is syntactically correct and logically matches the Pydantic models.
*   **Parameters:** *No parameters.*
*   **Returns:** *No return value.*
*   **Usage:**
    *   **Calls:** 
    *   **Called By:** 

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class is the main entry point for interacting with a language model. It initializes itself by setting up an API key, reading a system prompt file, and creating a ChatGoogleGenerativeAI instance.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by setting up an API key, reading a system prompt file, and creating a ChatGoogleGenerativeAI instance.
    *   *Parameters:*
        - **api_key** (`str`): The Gemini API Key
        - **prompt_file_path** (`str`): Path to the system prompt file
        - **model_name** (`str`): Name of the model (default: gemini-2.5-pro)
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, api_key, prompt_file_path, model_name)`
        *   *Description:* Initializes the MainLLM instance by setting up an API key, reading a system prompt file, and creating a ChatGoogleGenerativeAI instance.
        *   *Parameters:*
            - **self** (`object`): The MainLLM instance
            - **api_key** (`str`): The Gemini API Key
            - **prompt_file_path** (`str`): Path to the system prompt file
            - **model_name** (`str`): Name of the model (default: gemini-2.5-pro)
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* Calls the language model with a given user input.
        *   *Parameters:*
            - **self** (`object`): The MainLLM instance
            - **user_input** (`str`): The user's input to be processed by the language model
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* Streams the language model's output for a given user input.
        *   *Parameters:*
            - **self** (`object`): The MainLLM instance
            - **user_input** (`str`): The user's input to be processed by the language model
        *   *Returns:*
            - **None** (`None`): *Description not provided.*

---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** A class for extracting basic project information from various files.
*   **Instantiation:** backend/basic_info.py::ProjektInfoExtractor::__init__
*   **Dependencies:** re, os, tomllib, typing.List, typing.Dict, typing.Any, typing.Optional
*   **Constructor:**
    *   *Description:* Initializes the structure with placeholders.
    *   *Parameters:*
        - **self** (`class ProjektInfoExtractor`): The current instance of this class.
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* Finds a file that matches one of the given patterns.
        *   *Parameters:*
            - **self** (`class ProjektInfoExtractor`): The current instance of this class.
            - **patterns** (`list[str]`): A list of file name patterns to search for.
            - **dateien** (`list[Any]`): A list of files to search in.
        *   *Returns:*
            - **Optional[Any]** (`Any`): The found file, or None if not found.

---
### File: `backend/callgraph.py`
#### Class: `CallGraph`
*   **Summary:** Visitor, der Funktionsaufrufe im AST sammelt und Kanten für den Call-Graph erstellt.
*   **Instantiation:** :[
*   **Dependencies:** :[
*   **Constructor:**
    *   *Description:* Initialisiert den Visitor mit einem Platzhalter für die aktuelle Funktion.
    *   *Parameters:*
        - **self** (`None`): none
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **node** (`None`): none
        *   *Returns:* *No return value.*
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **callee_nodes** (`None`): none
        *   *Returns:* *No return value.*
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **basename** (`None`): none
            - **class_name** (`None`): none
        *   *Returns:* *No return value.*
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
        *   *Returns:* *No return value.*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **node** (`None`): none
        *   *Returns:* *No return value.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **node** (`None`): none
        *   *Returns:* *No return value.*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **node** (`None`): none
        *   *Returns:* *No return value.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **node** (`None`): none
        *   *Returns:* *No return value.*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **node** (`None`): none
        *   *Returns:* *No return value.*
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **node** (`None`): none
        *   *Returns:* *No return value.*
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`None`): none
            - **node** (`None`): none
        *   *Returns:* *No return value.*

#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree, filename, file_content)`
*   **Description:** Erstellt einen Call-Graphen aus einem gegebenen Python-AST. Der Graph ist ein gerichteter Graph, in dem Knoten Funktionen, Methoden und der globale Scope (<module>) bzw. <main_block> für `if __name__ == "__main__"`-Code sind, und Kanten Funktions-/Methodenaufrufe zwischen diesen Knoten.
*   **Parameters:**
    - **tree** (`ast.AST`): Der AST der zu analysierenden Python-Datei.
    - **filename** (`str | None`): Der Name der analysierten Datei, z.B. "main.py" oder "src/utils.py".
*   **Returns:**
    - **nx.DiGraph** (`networkx.DiGraph`): Der vollständige Call-Graph.
*   **Usage:**
    *   **Calls:** The function calls `backend/callgraph.py::DiGraph`.
    *   **Called By:** This function is used by `<main_block>`. It is part of the call graph construction process.

#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph)`
*   **Description:** This function converts a networkx.DiGraph into an adjacency list (Dict) that is JSON-serializable. The function takes a graph as input and returns a dictionary where each key represents a caller node and the value is a list of callee nodes.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The graph to be converted
*   **Returns:**
    - **Dict[str, List[str]]** (`Adjacency list (Dict) where each key represents a caller node and the value is a list of callee nodes`): JSON-serializable adjacency list
*   **Usage:**
    *   **Calls:** The function calls several internal functions from the backend/callgraph.py module, including list, nodes, sorted, and successors.
    *   **Called By:** This function is not called by any other function in this context.

#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(all_repo_files)`
*   **Description:** A function that builds a global call graph, currently not implemented and returns an error.
*   **Parameters:**
    - **all_repo_files** (`list[RepoFile]`): A list of repository files
*   **Returns:**
    - **nx.DiGraph** (`networkx.DiGraph`): The global call graph
*   **Usage:**
    *   **Calls:** This function does not call any other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** Converts a directed graph to a safe dot format by relabeling nodes with a numeric identifier and storing the original node names as labels.
*   **Parameters:**
    - **graph** (`networkx.DiGraph`): The input directed graph
    - **out_path** (`str`): The path where the safe dot file will be written
*   **Returns:** *No return value.*
*   **Usage:**
    *   **Calls:** It calls various functions from the backend/callgraph.py module to manipulate the graph.
    *   **Called By:** This function is called by the main block of code.

---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** Represents a single file in a Git repository. The content of the file is lazily loaded, i.e., only when actually accessed.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the RepoFile object.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self, file_path, commit_tree)`
        *   *Description:* Initializes the RepoFile object.
        *   *Parameters:*
            - **self** (`RepoFile`): The RepoFile object.
            - **file_path** (`str`): The path to the file within the repository.
            - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* Lazy-loads the Git blob object.
        *   *Parameters:*
            - **self** (`RepoFile`): The RepoFile object.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* Lazy-loads and returns the decoded content of the file.
        *   *Parameters:*
            - **self** (`RepoFile`): The RepoFile object.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* Lazy-loads and returns the size of the file in bytes.
        *   *Parameters:*
            - **self** (`RepoFile`): The RepoFile object.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* Analyzes the word count of the file content.
        *   *Parameters:*
            - **self** (`RepoFile`): The RepoFile object.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* Returns a useful string representation of the object.
        *   *Parameters:*
            - **self** (`RepoFile`): The RepoFile object.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* Converts the RepoFile object to a dictionary.
        *   *Parameters:*
            - **self** (`RepoFile`): The RepoFile object.
            - **include_content** (`bool`): Whether to include the file content in the dictionary.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **``**
        *   *Signature:* `def ()`
        *   *Description:* 
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **None** (`None`): *Description not provided.*

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository, including cloning into a temporary directory and providing RepoFile objects.
*   **Instantiation:** This class can be instantiated by the main program.
*   **Dependencies:** The Git repository management library is required for this class.
*   **Constructor:**
    *   *Description:* Initializes the Git repository with a given URL.
    *   *Parameters:*
        - **repo_url** (`string`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(repo_url)`
        *   *Description:* Initializes the Git repository with a given URL.
        *   *Parameters:*
            - **repo_url** (`string`): The URL of the Git repository to clone.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* Returns a list of all files in the repository as RepoFile objects.
        *   *Parameters:*
            - **self** (`GitRepository`): The Git repository object.
        *   *Returns:*
            - **list[RepoFile]** (`list of RepoFile objects`): A list of RepoFile objects representing the files in the repository.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* Closes the temporary directory and its contents.
        *   *Parameters:*
            - **self** (`GitRepository`): The Git repository object.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* Returns the Git repository object for use with a 'with' statement.
        *   *Parameters:*
            - **self** (`GitRepository`): The Git repository object.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* Closes the temporary directory and its contents when exiting a 'with' statement.
        *   *Parameters:*
            - **self** (`GitRepository`): The Git repository object.
            - **exc_type** (`exception type`): The exception type.
            - **exc_val** (`exception value`): The exception value.
            - **exc_tb** (`exception traceback`): The exception traceback.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* Returns a tree-like representation of the file system, including files and directories.
        *   *Parameters:*
            - **self** (`GitRepository`): The Git repository object.
            - **include_content** (`boolean`): Whether to include file content in the tree representation.
        *   *Returns:*
            - **tree** (`dictionary representing a file system tree`): A dictionary representing a file system tree, including files and directories.

---
### File: `backend/main.py`
#### Function: `main_workflow`
*   **Signature:** `def main_workflow()`
*   **Description:** The main workflow function is a high-level entry point for the system. It takes user input, extracts repository URLs, and then proceeds to analyze the repository's file structure, basic project information, and AST schema.
*   **Parameters:**
    - **user_input** (`str`): The user-provided input string
*   **Returns:** *No return value.*
*   **Usage:**
    *   **Calls:** It calls various functions to extract repository information, such as `GitRepository`, `ProjektInfoExtractor`, and `ASTAnalyzer`.
    *   **Called By:** This function is called by the main program block.

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a data model that represents the description of a single function parameter. It encapsulates information about the name, type, and description of the parameter.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* The constructor initializes the class with three attributes: name, type, and description.
    *   *Parameters:*
        - **name** (`str`): The name of the function parameter.
        - **type** (`str`): The data type of the function parameter.
        - **description** (`str`): A human-readable description of the function parameter.
*   **Methods:** *No methods available.*

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model that describes the return value of a function. It has three attributes: name, type, and description.
*   **Instantiation:** This class is instantiated by the system when describing return values of functions.
*   **Dependencies:** This class does not have any dependencies.
*   **Constructor:**
    *   *Description:* Initializes the ReturnDescription class with its attributes.
    *   *Parameters:*
        - **name** (`str`): 
        - **type** (`str`): 
        - **description** (`str`): 
*   **Methods:** *No methods available.*

#### Class: `UsageContext`
*   **Summary:** The UsageContext class describes the calling context of a function, including its calls and being called by other functions.
*   **Instantiation:** The UsageContext class is instantiated by no specific context.
*   **Dependencies:** The UsageContext class does not depend on any external dependencies.
*   **Constructor:**
    *   *Description:* Initializes the class with no parameters.
    *   *Parameters:* *No parameters.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__()`
        *   *Description:* No specific description available, as this is a constructor method.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **None** (`None`): *Description not provided.*

#### Class: `FunctionDescription`
*   **Summary:** This class contains the detailed analysis of a function's purpose and signature.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* The constructor initializes the class with an overall description, parameters, returns, and usage context.
    *   *Parameters:*
        - **overall** (`str`): A brief summary of the function's purpose.
        - **parameters** (`List[ParameterDescription]`): A list of parameters and their descriptions.
        - **returns** (`Optional[List[ReturnDescription]]`): The return types and descriptions of the function.
        - **usage_context** (`UsageContext`): Information about where this class is used.
*   **Methods:** *No methods available.*

#### Class: `FunctionAnalysis`
*   **Summary:** The main model representing the entire JSON schema for a function.
*   **Instantiation:** This model is instantiated by itself, as it represents a standalone JSON schema for a function.
*   **Dependencies:** This model does not have any dependencies.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysis class with an identifier and description.
    *   *Parameters:*
        - **identifier** (`str`): A unique string identifier for the function.
        - **description** (`FunctionDescription`): A detailed description of the function's purpose and behavior.
*   **Methods:** *No methods available.*

#### Class: `ConstructorDescription`
*   **Summary:** The __init__ method initializes the class instance with a description.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the class instance with a description.
    *   *Parameters:*
        - **description** (`str`): The initial description of the class.
*   **Methods:** *No methods available.*

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is used to describe the external dependencies and primary points of instantiation for a given context.
*   **Instantiation:** This class is instantiated by no other classes or functions.
*   **Dependencies:** This class depends on no external dependencies.
*   **Constructor:**
    *   *Description:* This class initializes by setting its dependencies and instantiated_by attributes.
    *   *Parameters:*
        - **dependencies** (`str`): The list of dependencies required by the ClassContext.
        - **instantiated_by** (`str`): The point of instantiation for this ClassContext.
*   **Methods:** *No methods available.*

#### Class: `ClassDescription`
*   **Summary:** This class provides a detailed analysis of a class's purpose, constructor, and methods.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* The class is initialized by calling the __init__ method.
    *   *Parameters:*
        - **self** (`ClassDescription`): Reference to the current instance of the class.
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__(self)`
        *   *Description:* Initializes the class by setting its overall description.
        *   *Parameters:*
            - **self** (`ClassDescription`): Reference to the current instance of the class.
        *   *Returns:*
            - **None** (`None`): *Description not provided.*

#### Class: `ClassAnalysis`
*   **Summary:** The main model for the entire JSON schema for a class.
*   **Instantiation:** This model is instantiated by the main program.
*   **Dependencies:** This model does not have any dependencies.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysis with identifier and description.
    *   *Parameters:*
        - **identifier** (`str`): The unique identifier of the class.
        - **description** (`ClassDescription`): A detailed description of the class's purpose and functionality.
*   **Methods:** *No methods available.*

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class provides a structured context for analyzing functions, including information about the function's calls and callers.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* This class is initialized without any specific parameters.
    *   *Parameters:* *No parameters.*
*   **Methods:**
    *   **`__init__`**
        *   *Signature:* `def __init__()`
        *   *Description:* The constructor initializes the class with no specific parameters.
        *   *Parameters:* *No parameters.*
        *   *Returns:*
            - **None** (`None`): *Description not provided.*

#### Class: `FunctionAnalysisInput`
*   **Summary:** This class is the required input to generate a FunctionAnalysis object.
*   **Instantiation:** This input class is instantiated by itself, as it's a standalone class.
*   **Dependencies:** This input class does not have any dependencies.
*   **Constructor:**
    *   *Description:* The constructor initializes an instance of this class with its mode, identifier, source code, imports, and context.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): The required mode for the function analysis.
        - **identifier** (`str`): A unique identifier for this input class.
        - **source_code** (`str`): The source code of the class being analyzed.
        - **imports** (`List[str]`): A list of import statements used in this class.
        - **context** (`FunctionContextInput`): The context information for the function being analyzed.
*   **Methods:** *No methods available.*

#### Class: `MethodContextInput`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the class with identifier, calls, called_by, args and docstring.
    *   *Parameters:*
        - **identifier** (`str`): The identifier of the method.
        - **calls** (`List[str]`): A list of methods called by this method.
        - **called_by** (`List[str]`): A list of methods that call this method.
        - **args** (`List[str]`): A list of arguments passed to the method.
        - **docstring** (`Optional[str]`): The docstring for this method.
*   **Methods:**
    *   **`identifier`**
        *   *Signature:* `def identifier(self)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`MethodContextInput`): The instance of the class.
        *   *Returns:* *No return value.*
    *   **`calls`**
        *   *Signature:* `def calls(self)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`MethodContextInput`): The instance of the class.
        *   *Returns:* *No return value.*
    *   **`called_by`**
        *   *Signature:* `def called_by(self)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`MethodContextInput`): The instance of the class.
        *   *Returns:* *No return value.*
    *   **`args`**
        *   *Signature:* `def args(self)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`MethodContextInput`): The instance of the class.
        *   *Returns:* *No return value.*
    *   **`docstring`**
        *   *Signature:* `def docstring(self)`
        *   *Description:* 
        *   *Parameters:*
            - **self** (`MethodContextInput`): The instance of the class.
        *   *Returns:* *No return value.*

#### Class: `ClassContextInput`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* This class is initialized with no specific parameters.
    *   *Parameters:*
        - **dependencies** (`List[str]`): 
        - **instantiated_by** (`List[str]`): 
        - **method_context** (`List[MethodContextInput]`): 
*   **Methods:** *No methods available.*

#### Class: `ClassAnalysisInput`
*   **Summary:** The required input to generate a ClassAnalysis object.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the class with mode, identifier, source_code, imports, and context.
    *   *Parameters:*
        - **mode** (`Literal[str]`): The required input mode.
        - **identifier** (`str`): A unique identifier for the class.
        - **source_code** (`str`): The source code of the class definition.
        - **imports** (`List[str]`): Import statements from the source file.
        - **context** (`ClassContextInput`): The context in which this class is used.
*   **Methods:** *No methods available.*

---
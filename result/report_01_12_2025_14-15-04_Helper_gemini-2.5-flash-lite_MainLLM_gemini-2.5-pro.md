# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project is an automated documentation agent designed to onboard developers to a new software repository. It works by cloning a Git repository from a provided URL, performing a deep static analysis of the source code, and then leveraging a two-stage Large Language Model (LLM) pipeline to generate a comprehensive technical report. The analysis includes parsing the Abstract Syntax Tree (AST), building call graphs, and identifying file dependencies to create a detailed code schema. The final output is a human-readable Markdown document that details the project's structure, architecture, and code components.
- **Key Features:**
  - Automated repository cloning from a URL.
  - Abstract Syntax Tree (AST) parsing to build a detailed code schema.
  - Generation of call graphs and file dependency graphs.
  - A two-stage LLM pipeline (Helper/Main) for detailed code analysis and final report synthesis.
  - A Streamlit-based web interface for user interaction, including authentication and chat history management.
- **Tech Stack:** Python, Streamlit, LangChain, Pydantic, NetworkX, pymongo.

*   **Repository Structure:**
    ```mermaid
    graph LR
      subgraph root
        A["/.env.example<br/>/.gitignore<br/>/analysis_output.json<br/>/readme.md<br/>/requirements.txt"]
      end
      subgraph SystemPrompts
        B["/SystemPromptClassHelperLLM.txt<br/>/SystemPromptFunctionHelperLLM.txt<br/>/SystemPromptHelperLLM.txt<br/>/SystemPromptMainLLM.txt"]
      end
      subgraph backend
        C["/AST_Schema.py<br/>/File_Dependency.py<br/>/HelperLLM.py<br/>/MainLLM.py<br/>/__init__.py<br/>/basic_info.py<br/>/callgraph.py<br/>/getRepo.py<br/>/main.py<br/>/relationship_analyzer.py"]
      end
      subgraph database
        D["/db.py"]
      end
      subgraph frontend
        E["/Frontend.py<br/>/__init__.py"]
      end
      subgraph frontend/gifs
        F["/4j.gif"]
      end
      subgraph notizen
        G["/Report Agenda.txt<br/>/Zwischenpraesentation Agenda.txt<br/>/doc_bestandteile.md<br/>/notizen.md<br/>/paul_notizen.md<br/>/praesentation_notizen.md<br/>/technische_notizen.md"]
      end
      subgraph notizen/grafiken
        H["/File_Dependency_Graph_Repo.dot<br/>/global_callgraph.png<br/>/global_graph.png<br/>/global_graph_2.png<br/>/repo.dot"]
      end
      subgraph notizen/grafiken/Flask-Repo
        I[...]
      end
      subgraph notizen/grafiken/Repo-onboarding
        J[...]
      end
      subgraph result
        K[...]
      end
      subgraph schemas
        L["/types.py"]
      end
      
      root --> SystemPrompts
      root --> backend
      root --> database
      root --> frontend
      frontend --> frontend/gifs
      root --> notizen
      notizen --> notizen/grafiken
      notizen/grafiken --> notizen/grafiken/Flask-Repo
      notizen/grafiken --> notizen/grafiken/Repo-onboarding
      root --> result
      root --> schemas
    ```

## 2. Installation
### Dependencies
As this repository contains a `requirements.txt` file, dependencies can be installed using the following command:
```bash
pip install -r requirements.txt
```
The dependencies listed are:
- a l t a i r = = 4 . 2 . 2 
-  
-  a n n o t a t e d - t y p e s = = 0 . 7 . 0 
-  
-  a n y i o = = 4 . 1 1 . 0 
-  
-  a t t r s = = 2 5 . 4 . 0 
-  
-  b c r y p t = = 5 . 0 . 0 
-  
-  b l i n k e r = = 1 . 9 . 0 
-  
-  c a c h e t o o l s = = 6 . 2 . 2 
-  
-  c a p t c h a = = 0 . 7 . 1 
-  
-  c e r t i f i = = 2 0 2 5 . 1 1 . 1 2 
-  
-  c f f i = = 2 . 0 . 0 
-  
-  c h a r s e t - n o r m a l i z e r = = 3 . 4 . 4 
-  
-  c l i c k = = 8 . 3 . 1 
-  
-  c o l o r a m a = = 0 . 4 . 6 
-  
-  c r y p t o g r a p h y = = 4 6 . 0 . 3 
-  
-  d n s p y t h o n = = 2 . 8 . 0 
-  
-  d o t e n v = = 0 . 9 . 9 
-  
-  e n t r y p o i n t s = = 0 . 4 
-  
-  e x t r a - s t r e a m l i t - c o m p o n e n t s = = 0 . 1 . 8 1 
-  
-  f i l e t y p e = = 1 . 2 . 0 
-  
-  g i t d b = = 4 . 0 . 1 2 
-  
-  G i t P y t h o n = = 3 . 1 . 4 5 
-  
-  g o o g l e - a i - g e n e r a t i v e l a n g u a g e = = 0 . 9 . 0 
-  
-  g o o g l e - a p i - c o r e = = 2 . 2 8 . 1 
-  
-  g o o g l e - a u t h = = 2 . 4 3 . 0 
-  
-  g o o g l e a p i s - c o m m o n - p r o t o s = = 1 . 7 2 . 0 
-  
-  g r p c i o = = 1 . 7 6 . 0 
-  
-  g r p c i o - s t a t u s = = 1 . 7 6 . 0 
-  
-  h 1 1 = = 0 . 1 6 . 0 
-  
-  h t t p c o r e = = 1 . 0 . 9 
-  
-  h t t p x = = 0 . 2 8 . 1 
-  
-  i d n a = = 3 . 1 1 
-  
-  J i n j a 2 = = 3 . 1 . 6 
-  
-  j s o n p a t c h = = 1 . 3 3 
-  
-  j s o n p o i n t e r = = 3 . 0 . 0 
-  
-  j s o n s c h e m a = = 4 . 2 5 . 1 
-  
-  j s o n s c h e m a - s p e c i f i c a t i o n s = = 2 0 2 5 . 9 . 1 
-  
-  l a n g c h a i n = = 1 . 0 . 8 
-  
-  l a n g c h a i n - c o r e = = 1 . 1 . 0 
-  
-  l a n g c h a i n - g o o g l e - g e n a i = = 3 . 1 . 0 
-  
-  l a n g c h a i n - o l l a m a = = 1 . 0 . 0 
-  
-  l a n g g r a p h = = 1 . 0 . 3 
-  
-  l a n g g r a p h - c h e c k p o i n t = = 3 . 0 . 1 
-  
-  l a n g g r a p h - p r e b u i l t = = 1 . 0 . 5 
-  
-  l a n g g r a p h - s d k = = 0 . 2 . 9 
-  
-  l a n g s m i t h = = 0 . 4 . 4 6 
-  
-  M a r k u p S a f e = = 3 . 0 . 3 
-  
-  n a r w h a l s = = 2 . 1 2 . 0 
-  
-  n e t w o r k x = = 3 . 6 
-  
-  n u m p y = = 2 . 3 . 5 
-  
-  o l l a m a = = 0 . 6 . 1 
-  
-  o r j s o n = = 3 . 1 1 . 4 
-  
-  o r m s g p a c k = = 1 . 1 2 . 0 
-  
-  p a c k a g i n g = = 2 5 . 0 
-  
-  p a n d a s = = 2 . 3 . 3 
-  
-  p i l l o w = = 1 2 . 0 . 0 
-  
-  p r o t o - p l u s = = 1 . 2 6 . 1 
-  
-  p r o t o b u f = = 6 . 3 3 . 1 
-  
-  p y a r r o w = = 2 1 . 0 . 0 
-  
-  p y a s n 1 = = 0 . 6 . 1 
-  
-  p y a s n 1 _ m o d u l e s = = 0 . 4 . 2 
-  
-  p y c p a r s e r = = 2 . 2 3 
-  
-  p y d a n t i c = = 2 . 1 2 . 4 
-  
-  p y d a n t i c _ c o r e = = 2 . 4 1 . 5 
-  
-  p y d e c k = = 0 . 9 . 1 
-  
-  P y J W T = = 2 . 1 0 . 1 
-  
-  p y m o n g o = = 4 . 1 5 . 4 
-  
-  p y t h o n - d a t e u t i l = = 2 . 9 . 0 . p o s t 0 
-  
-  p y t h o n - d o t e n v = = 1 . 2 . 1 
-  
-  p y t z = = 2 0 2 5 . 2 
-  
-  P y Y A M L = = 6 . 0 . 3 
-  
-  r e f e r e n c i n g = = 0 . 3 7 . 0 
-  
-  r e q u e s t s = = 2 . 3 2 . 5 
-  
-  r e q u e s t s - t o o l b e l t = = 1 . 0 . 0 
-  
-  r p d s - p y = = 0 . 2 9 . 0 
-  
-  r s a = = 4 . 9 . 1 
-  
-  s i x = = 1 . 1 7 . 0 
-  
-  s m m a p = = 5 . 0 . 2 
-  
-  s n i f f i o = = 1 . 3 . 1 
-  
-  s t r e a m l i t = = 1 . 5 1 . 0 
-  
-  s t r e a m l i t - a u t h e n t i c a t o r = = 0 . 4 . 2 
-  
-  s t r e a m l i t - m e r m a i d = = 0 . 3 . 0 
-  
-  t e n a c i t y = = 9 . 1 . 2 
-  
-  t o m l = = 0 . 1 0 . 2 
-  
-  t o o l z = = 1 . 1 . 0 
-  
-  t o o n _ f o r m a t   @   g i t + h t t p s : / / g i t h u b . c o m / t o o n - f o r m a t / t o o n - p y t h o n . g i t @ 9 c 4 f 0 c 0 c 2 4 f 2 a 0 b 0 b 3 7 6 3 1 5 f 4 b 8 7 0 7 f 8 c 9 0 0 6 d e 6 
-  
-  t o r n a d o = = 6 . 5 . 2 
-  
-  t y p i n g - i n s p e c t i o n = = 0 . 4 . 2 
-  
-  t y p i n g _ e x t e n s i o n s = = 4 . 1 5 . 0 
-  
-  t z d a t a = = 2 0 2 5 . 2 
-  
-  u r l l i b 3 = = 2 . 5 . 0 
-  
-  w a t c h d o g = = 6 . 0 . 0 
-  
-  x x h a s h = = 3 . 6 . 0 
-  
-  z s t a n d a r d = = 0 . 2 5 . 0 
-  
-  
### Setup Guide
Information not found
### Quick Startup
Information not found

## 3. Use Cases & Commands
The primary use case of this project is to provide a user with a comprehensive, automatically generated documentation report for any public Git repository. The user interacts with the system through a web interface built with Streamlit.

**Workflow:**
1.  **Authentication:** The user logs into the Streamlit application.
2.  **Input:** The user provides the URL of a public Git repository.
3.  **Configuration:** The user selects the desired Large Language Models (LLMs) for the Helper and Main stages of the analysis pipeline. API keys for the selected models are also provided.
4.  **Execution:** The user initiates the analysis process. The application backend clones the repository, performs static code analysis (AST parsing, dependency analysis, call graph generation), and then feeds this structured data to the LLM pipeline.
5.  **Output:** The system generates a final Markdown report, which is displayed in the user interface and saved as a file. The interface also maintains a chat history of previous analyses.

There are no primary command-line commands as the application is designed to be run as a Streamlit web service. The main entry point is `Frontend.py`.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis
### File: `backend/AST_Schema.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into a Python module path relative to a specified project root. It handles potential errors during relative path calculation and normalizes the path by replacing directory separators with dots. It also specifically handles '__init__.py' files to represent package directories.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the file.
    - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path string.
*   **Usage:**
    - **Calls:** `basename`, `endswith`, `relpath`, `replace`
    - **Called By:** `__init__` (in class `ASTVisitor`)

---
#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It specifically focuses on extracting information about imports, classes, and functions within the code. The visitor pattern is employed to systematically process different node types in the AST, populating a schema dictionary with the gathered details. This class is instrumental in analyzing the structure and components of Python projects.
*   **Instantiation:** `analyze_repository` (in file `AST_Schema.py`)
*   **Dependencies:** This class relies on the `ast` module for parsing Python code into an Abstract Syntax Tree and the `path_to_module` function (presumably defined elsewhere) to convert file paths into module paths. It also utilizes `ast.get_docstring` and `ast.get_source_segment` for extracting metadata from AST nodes.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with the source code, file path, and project root directory. It sets up instance variables to store this information and initializes a schema dictionary to hold the extracted AST information, including imports, functions, and classes. It also initializes a variable to keep track of the current class being visited.
    *   *Parameters:*
        - **source_code** (`str`): The raw source code of the file being analyzed.
        - **file_path** (`str`): The absolute path to the file being analyzed.
        - **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* This method handles the `ast.Import` node, which represents a standard import statement (e.g., `import os`). It iterates through the imported names and appends them to the 'imports' list within the class's schema. After processing the import, it calls `generic_visit` to ensure that any nested nodes are also visited.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing an import statement.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method processes `ast.ImportFrom` nodes, which represent from-imports (e.g., `from os import path`). It extracts the module and alias names, constructing a fully qualified import path (e.g., `os.path`) and appends it to the 'imports' list in the schema. It then calls `generic_visit` to continue the traversal.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a from-import statement.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* This method is responsible for visiting `ast.ClassDef` nodes, representing class definitions. It constructs a unique identifier for the class, including its module path and name. It then creates a dictionary (`class_info`) containing details about the class, such as its name, docstring, source code segment, and line numbers. This `class_info` is appended to the 'classes' list in the schema, and `_current_class` is set to this information for subsequent method analysis within the class. Finally, it calls `generic_visit` to process nested nodes and resets `_current_class` upon completion.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a class definition.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* This method handles both top-level function definitions and methods within classes. If `_current_class` is set (meaning the visitor is currently inside a class definition), it creates method-specific information, including a fully qualified identifier, arguments, docstring, and line numbers, and appends it to the `method_context` of the current class in the schema. If not within a class, it treats the definition as a standalone function, creating similar information and appending it to the 'functions' list in the schema. In both cases, it calls `generic_visit` to process nested nodes.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing a function or method definition.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* This method is an alias for `visit_FunctionDef` and is designed to handle asynchronous function definitions (`async def`). It ensures that asynchronous functions are processed using the same logic as regular functions by simply calling `visit_FunctionDef`.
        *   *Parameters:*
            - **node** (`ast.AST`): The AST node representing an asynchronous function definition.
        *   *Returns:*
            - *No return value specified.*

---
#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for parsing Python files within a repository, building an Abstract Syntax Tree (AST) for each file, and then enriching this AST data with call graph information. It aggregates this information into a comprehensive schema representing the repository's structure, including files, classes, methods, and functions, along with their relationships and dependencies. The class facilitates the analysis of code structure and inter-component relationships.
*   **Instantiation:** `main_workflow` (in file `main.py`)
*   **Dependencies:** This class utilizes the 'ast' module for parsing Python code, 'networkx' for graph manipulation (specifically for call graphs), and 'os' for path operations. It also depends on a function `build_callGraph` from the `callgraph` module and an `ASTVisitor` class, which are not fully defined in the provided source.
*   **Constructor:**
    *   *Description:* Initializes the ASTAnalyzer instance. Currently, the constructor does not perform any specific setup or attribute initialization, as indicated by the 'pass' statement.
    *   *Parameters:*
        - *No parameters specified.*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
        *   *Description:* This static method takes a schema dictionary, a NetworkX call graph, and a filename as input. It iterates through the functions and classes defined in the schema and annotates them with call graph information. Specifically, for each function and method, it identifies the functions it calls (successors in the call graph) and the functions that call it (predecessors in the call graph), storing these as sorted lists within the schema's 'context' fields. This enriches the AST schema with dynamic call relationship data.
        *   *Parameters:*
            - **schema** (`dict`): A dictionary representing the AST schema of a file, containing information about functions and classes.
            - **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call graph of the analyzed code.
            - **filename** (`str`): The name of the file for which the schema and call graph were generated.
        *   *Returns:*
            - *No return value specified.*
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
        *   *Description:* This method merges relationship data, such as 'called_by' and 'instantiated_by' information, into a full schema. It first creates a lookup dictionary from the provided `relationship_data`. Then, it iterates through the files and their corresponding AST nodes within the `full_schema`. For each function, class, and method, it checks if its identifier exists in the relationship lookup and updates the schema with the relevant relationship information. This method is crucial for consolidating different types of code relationship data into a unified schema.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
            - **full_schema** (`dict`): A dictionary representing the complete schema of the repository, potentially containing data from multiple files.
            - **relationship_data** (`list`): A list of dictionaries, where each dictionary contains identifier and relationship information (e.g., 'called_by').
        *   *Returns:*
            - **full_schema** (`dict`): The updated full schema dictionary with merged relationship data.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files)`
        *   *Description:* This method orchestrates the analysis of an entire repository. It initializes an empty schema and determines the project's root directory. It then iterates through a list of file objects, processing only Python files that are not empty. For each file, it parses the content into an AST, creates an ASTVisitor to extract schema information, and builds a call graph. Subsequently, it enriches the file's schema with call graph data using `_enrich_schema_with_callgraph`. If the processed file yields any import, function, or class information, it's added to the `full_schema`. The method includes error handling for syntax and value errors during parsing.
        *   *Parameters:*
            - **self** (`ASTAnalyzer`): The instance of the ASTAnalyzer class.
            - **files** (`list`): A list of file objects, where each object contains file path and content.
        *   *Returns:*
            - **full_schema** (`dict`): A dictionary containing the aggregated schema for all processed files in the repository.

---
### File: `backend/File_Dependency.py`
#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes a filename, an Abstract Syntax Tree (AST) of the file, and the repository root as input. The function initializes a NetworkX directed graph and uses a custom visitor (`FileDependencyGraph`) to traverse the AST and identify import dependencies. It then populates the graph by adding nodes for each file and edges representing the import relationships between them. Finally, it returns the constructed dependency graph.
*   **Parameters:**
    - **filename** (`str`): The name of the file for which the dependency graph is being built.
    - **tree** (`AST`): The Abstract Syntax Tree (AST) representing the structure of the input file.
    - **repo_root** (`str`): The root directory of the repository.
*   **Returns:**
    - **graph** (`nx.DiGraph`): A directed graph (nx.DiGraph) where nodes represent files and edges represent import dependencies.
*   **Usage:**
    - **Calls:** `DiGraph`, `FileDependencyGraph`, `add_edge`, `add_node`, `add_nodes_from`, `items`, `visit`
    - **Called By:** `build_repository_graph` (in file `File_Dependency.py`)

---
#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function constructs a directed graph representing the file dependencies within a Git repository. It iterates through all Python files in the repository, parses their content to build an Abstract Syntax Tree (AST), and then generates a dependency graph for each file. These individual file graphs are merged into a single, global graph that captures the overall dependency structure of the repository. The function specifically focuses on Python files and ignores others.
*   **Parameters:**
    - **repository** (`GitRepository`): An object representing the Git repository to analyze, providing access to its files and temporary directory.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A NetworkX directed graph where nodes represent Python files or functions/classes within those files, and edges represent dependencies between them.
*   **Usage:**
    - **Calls:** `DiGraph`, `add_edge`, `add_node`, `basename`, `build_file_dependency_graph`, `endswith`, `get_all_files`, `parse`, `removesuffix`, `str`
    - **Called By:** `backend.File_Dependency` (in file `File_Dependency.py`)

---
#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function recursively searches a given directory for all Python files (*.py) and returns a list of their relative paths. It resolves the root directory to an absolute path and then uses `rglob` to find all matching files. The function then converts these file paths to be relative to the resolved root path before returning them. This is useful for identifying all source files within a project structure.
*   **Parameters:**
    - **directory** (`str`): The path to the directory to search for Python files.
*   **Returns:**
    - **all_files** (`list[Path]`): A list of Path objects, where each Path represents a Python file found in the directory, relative to the root directory.
*   **Usage:**
    - **Calls:** `Path`, `relative_to`, `resolve`, `rglob`
    - **Called By:** `_resolve_module_name` (in class `FileDependencyGraph`)

---
#### Function: `nx_to_mermaid_with_folders`
*   **Signature:** `def nx_to_mermaid_with_folders(G)`
*   **Description:** This function takes a NetworkX directed graph (G) representing file dependencies and converts it into a Mermaid.js graph definition string, organizing nodes into subgraphs based on their folder structure. It iterates through the graph's nodes to map files to their respective folders, then constructs Mermaid syntax for subgraphs representing these folders. Finally, it adds the edges from the original graph, translating file paths into valid node identifiers for Mermaid. The function returns a single string containing the complete Mermaid graph definition.
*   **Parameters:**
    - **G** (`nx.DiGraph`): A NetworkX directed graph where nodes represent file paths and edges represent dependencies between them.
*   **Returns:**
    - **mermaid_string** (`str`): A string formatted for Mermaid.js, representing the directed graph with nodes organized into folder subgraphs.
*   **Usage:**
    - **Calls:** `append`, `defaultdict`, `items`, `join`, `replace`, `split`
    - **Called By:** `backend.File_Dependency` (in file `File_Dependency.py`)

---
#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze Python source code and build a graph representing file dependencies based on import statements. It traverses the Abstract Syntax Tree (AST) of a given file to identify direct and relative imports. The class handles the resolution of relative imports by examining the file structure and the contents of __init__.py files to determine the actual module or symbol being imported. It stores these dependencies in a dictionary where keys are filenames and values are sets of imported module names.
*   **Instantiation:** `build_file_dependency_graph` (in file `File_Dependency.py`)
*   **Dependencies:** This class relies on various modules for AST parsing (`ast`), path manipulation (`pathlib.Path`), keyword checking (`keyword`), and potentially file system operations (`os`, `getRepo.GitRepository`). It also utilizes `collections.defaultdict` and functions from `ast.literal_eval`, `ast.parse`, and `ast.walk`.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with the filename to be analyzed and the root directory of the repository. This sets up the context for resolving imports within the specified file and repository.
    *   *Parameters:*
        - **filename** (`str`): The name of the Python file for which the dependency graph is being built.
        - **repo_root** (`str`): The root directory of the repository containing the Python files.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* This method is responsible for resolving relative import statements (e.g., `from .. import name`) within a Python file. It determines the actual module or symbol being imported by considering the current file's location within the repository and the import level specified. It searches for corresponding Python files or packages (`__init__.py`) in the repository and checks `__init__.py` for explicit exports (`__all__`) or defined symbols. If a valid resolution is found, it returns a list of resolved names; otherwise, it raises an ImportError.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            - **resolved** (`list[str]`): A sorted list of unique, resolved module or symbol names.
    *   **`module_file_exists`**
        *   *Signature:* `def module_file_exists(rel_base, name)`
        *   *Description:* A helper method to check if a Python file or a package directory (with an `__init__.py` file) exists at a given relative base path for a specified module name. It constructs the potential file path and checks for its existence on the filesystem.
        *   *Parameters:*
            - **rel_base** (`Path`): The relative base path within the repository.
            - **name** (`str`): The name of the module or package to check for.
        *   *Returns:*
            - **bool** (`bool`): True if the file or package exists, False otherwise.
    *   **`init_exports_symbol`**
        *   *Signature:* `def init_exports_symbol(rel_base, symbol)`
        *   *Description:* This method checks if a given symbol is exported by an `__init__.py` file within a specified relative base path. It reads the `__init__.py` file, parses its content, and then traverses the AST to find if the symbol is defined as a function, class, assignment, or explicitly listed in the `__all__` variable. It returns True if the symbol is found and exported, and False otherwise.
        *   *Parameters:*
            - **rel_base** (`Path`): The relative base path to the directory containing the `__init__.py` file.
            - **symbol** (`str`): The name of the symbol (function, class, variable) to check for.
        *   *Returns:*
            - **bool** (`bool`): True if the symbol is exported by the `__init__.py` file, False otherwise.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name)`
        *   *Description:* This method is called when the AST visitor encounters an `import` statement. It iterates through the imported names and adds them to the `import_dependencies` dictionary, mapping the current filename to the imported module name. If a `base_name` is provided (typically from `visit_ImportFrom`), it uses that as the dependency; otherwise, it uses the direct alias name.
        *   *Parameters:*
            - **node** (`Import | ImportFrom`): The AST node representing the import statement.
            - **base_name** (`str | None`): An optional base name to use for the dependency, typically derived from a `from ... import ...` statement.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* This method handles `from ... import ...` statements in the AST. It extracts the module name, determines the base module if it's a direct import, or calls `_resolve_module_name` to handle relative imports. It then uses `visit_Import` to record the identified dependencies. If resolving a relative import fails, it prints an error message.
        *   *Parameters:*
            - **node** (`ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
            - *No return value specified.*

---
### File: `backend/HelperLLM.py`
#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy orchestrator for testing the LLMHelper class and its documentation generation capabilities. It simulates the process of analyzing functions and classes by creating predefined input data and expected analysis results for several inventory management methods (`add_item`, `check_stock`, `generate_report`). It then uses these to instantiate an `LLMHelper` and calls its `generate_for_functions` method, ultimately printing the aggregated documentation in JSON format. The function is designed to be syntactically correct and logically aligned with Pydantic models for schema validation.
*   **Parameters:**
    - *No parameters specified.*
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `ClassAnalysisInput`, `ClassContextInput`, `LLMHelper`, `dumps`, `generate_for_functions`, `info`, `model_dump`, `model_validate`, `print`, `warning`
    - **Called By:** `backend.HelperLLM` (in file `HelperLLM.py`)

---
#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class is designed to interact with various Large Language Models (LLMs) for generating and validating documentation. It supports models from Google Gemini, OpenAI, and Ollama, centralizing API calls and handling batch processing with configurable batch sizes and rate limit delays. The class is initialized with API keys, prompt file paths, and model configurations, and it provides methods to generate documentation for both functions and classes, ensuring structured output validation through Pydantic models.
*   **Instantiation:** `main_orchestrator` (in file `HelperLLM.py`), `main_workflow` (in file `main.py`)
*   **Dependencies:** This class utilizes several external libraries including `json` for data serialization, `logging` for output, `time` for delays, and various Langchain components (`ChatGoogleGenerativeAI`, `ChatOllama`, `ChatOpenAI`, `HumanMessage`, `SystemMessage`) for LLM interaction. It also depends on Pydantic models (`FunctionAnalysis`, `ClassAnalysis`, `FunctionAnalysisInput`, `ClassAnalysisInput`) for input and output validation, and potentially environment variable loading via `dotenv`.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with necessary credentials and configuration. It loads system prompts for function and class documentation from specified files, sets up the LLM client based on the model name (supporting Gemini, OpenAI, and Ollama), and configures batch processing settings. It raises a ValueError if the API key is not provided and logs errors if prompt files are not found.
    *   *Parameters:*
        - **api_key** (`str`): The API key for authenticating with the LLM service.
        - **function_prompt_path** (`str`): The file path to the system prompt used for function documentation generation.
        - **class_prompt_path** (`str`): The file path to the system prompt used for class documentation generation.
        - **model_name** (`str`): The name of the LLM model to use (e.g., 'gemini-2.0-flash-lite'). Defaults to 'gemini-2.0-flash-lite'.
        - **ollama_base_url** (`str`): The base URL for Ollama if using an Ollama model. Defaults to a predefined OLLAMA_BASE_URL if not provided.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* Configures the batch size for LLM API calls based on the specified model name. It defines different batch sizes for various Gemini, Ollama, and OpenAI models to optimize performance and adhere to potential API rate limits. For unknown models, it logs a warning and defaults to a conservative batch size.
        *   *Parameters:*
            - **model_name** (`str`): The name of the LLM model for which to configure batch settings.
        *   *Returns:*
            - *No return value specified.*
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* Generates and validates documentation for a list of function inputs using the configured LLM. It processes inputs in batches according to the `batch_size` attribute, serializes Pydantic inputs to JSON, constructs conversation prompts with system and human messages, and calls the LLM's batch API. It includes error handling for API calls and implements a waiting period between batches to respect rate limits.
        *   *Parameters:*
            - **function_inputs** (`List[FunctionAnalysisInput]`): A list of FunctionAnalysisInput objects, each containing the necessary information to generate documentation for a function.
        *   *Returns:*
            - **all_validated_functions** (`List[Optional[FunctionAnalysis]]`): A list containing the validated FunctionAnalysis results for each input, or None if an error occurred during processing for a specific item.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* Generates and validates documentation for a list of class inputs using the configured LLM. Similar to `generate_for_functions`, it processes inputs in batches, serializes Pydantic inputs to JSON, constructs conversation prompts, and calls the LLM's batch API. It handles potential exceptions during API calls and includes a delay between batches to manage rate limits.
        *   *Parameters:*
            - **class_inputs** (`List[ClassAnalysisInput]`): A list of ClassAnalysisInput objects, each containing the necessary information to generate documentation for a class.
        *   *Returns:*
            - **all_validated_classes** (`List[Optional[ClassAnalysis]]`): A list containing the validated ClassAnalysis results for each input, or None if an error occurred during processing for a specific item.

---
### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the primary interface for interacting with Large Language Models (LLMs). It handles the initialization of different LLM backends (Google Generative AI or Ollama) based on the provided model name and configuration. The class is responsible for loading a system prompt from a file and provides methods to either get a direct response from the LLM or stream the response in chunks.
*   **Instantiation:** `main_workflow` (in file `main.py`)
*   **Dependencies:** This class depends on several external libraries for LLM interaction, including langchain_google_genai, langchain_ollama, and langchain_openai, as well as langchain's message classes (HumanMessage, SystemMessage). It also utilizes the logging module for output and error reporting.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM class by setting up the LLM backend. It validates the API key, loads the system prompt from a specified file, and configures either a ChatGoogleGenerativeAI or ChatOllama instance based on the model name. It logs the initialization process and any file loading errors.
    *   *Parameters:*
        - **api_key** (`str`): The API key required for authenticating with the LLM service, specifically for Google Generative AI models.
        - **prompt_file_path** (`str`): The file path to the system prompt that will be used to guide the LLM's responses.
        - **model_name** (`str`): The name of the LLM model to use. Defaults to 'gemini-2.5-pro'. It can be a Google Generative AI model (e.g., 'gemini-...') or an Ollama model (e.g., 'gpt-...').
        - **ollama_base_url** (`str`): The base URL for the Ollama service, used when the model_name indicates an Ollama model. Defaults to a predefined OLLAMA_BASE_URL if not provided.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `def call_llm(self, user_input)`
        *   *Description:* This method sends a user's input to the configured LLM and returns the complete response content. It constructs a message list containing the system prompt and the user's input, then invokes the LLM. Error handling is included to log any exceptions during the LLM call and return None if an error occurs.
        *   *Parameters:*
            - **user_input** (`str`): The input string provided by the user to be processed by the LLM.
        *   *Returns:*
            - **response.content** (`str`): The content of the LLM's response as a string, or None if an error occurred during the LLM call.
    *   **`stream_llm`**
        *   *Signature:* `def stream_llm(self, user_input)`
        *   *Description:* This method allows for streaming the LLM's response in chunks, which is useful for real-time applications. It constructs messages similar to `call_llm` but uses the `stream` method of the LLM. Each chunk of content received from the stream is yielded, and any errors during the streaming process are logged and returned as part of the yielded output.
        *   *Parameters:*
            - **user_input** (`str`): The input string provided by the user to be processed by the LLM for streaming.
        *   *Returns:*
            - **chunk.content** (`str`): Yields chunks of the LLM's response content as strings. If an error occurs, it yields an error message string.

---
### File: `backend/basic_info.py`
#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract fundamental project information from common project files such as README, pyproject.toml, and requirements.txt. It initializes a structured dictionary to hold project overview and installation details, populating it by parsing these files in a prioritized order. The class aims to provide a consolidated view of project metadata, including title, description, key features, tech stack, installation instructions, and dependencies.
*   **Instantiation:** `main_workflow` (in file `main.py`)
*   **Dependencies:** This class relies on the `re` module for regular expression operations and the `tomllib` module for parsing TOML files. It also uses standard library modules like `os` and types from the `typing` module.
*   **Constructor:**
    *   *Description:* The constructor initializes the ProjektInfoExtractor by setting a default string for when information is not found and creating a nested dictionary structure to store project information. This structure includes placeholders for project overview (title, description, status, key features, tech stack) and installation details (dependencies, setup instructions, quick start guide).
    *   *Parameters:*
        - **self** (`self`): The instance of the class.
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `def _finde_datei(self, patterns, dateien)`
        *   *Description:* This private helper method searches through a list of file objects to find a file whose path matches one of the provided patterns. The search is case-insensitive, meaning it will find files regardless of the casing in their names or the patterns. It returns the first matching file object found or None if no match is found after checking all files against all patterns.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **patterns** (`List[str]`): A list of file name patterns (e.g., 'readme.md') to search for.
            - **dateien** (`List[Any]`): A list of file objects, where each object is expected to have a 'path' attribute.
        *   *Returns:*
            - **Optional[Any]** (`Optional[Any]`): The first file object that matches any of the patterns, or None if no match is found.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
        *   *Description:* This private helper method extracts a specific section of text from a Markdown-formatted string. It uses regular expressions to find a section that starts with a second-level heading (##) followed by one of the provided keywords. The method captures all text following the heading until it encounters another second-level heading or the end of the file. It is designed to be flexible by accepting multiple keywords for a single section.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The Markdown content from which to extract the section.
            - **keywords** (`List[str]`): A list of keywords that identify the desired section's heading.
        *   *Returns:*
            - **Optional[str]** (`Optional[str]`): The extracted text content of the section, stripped of leading/trailing whitespace, or None if the section is not found.
    *   **`_parse_readme`**
        *   *Signature:* `def _parse_readme(self, inhalt)`
        *   *Description:* This private method parses the content of a README file to extract various pieces of project information. It attempts to find and populate the project's title, description, key features, tech stack, current status, setup instructions, and quick start guide by leveraging regular expressions and the `_extrahiere_sektion_aus_markdown` helper method. It prioritizes information already present in `self.info` and only updates if the information is still marked as not found.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the README file.
        *   *Returns:*
            - *No return value specified.*
    *   **`_parse_toml`**
        *   *Signature:* `def _parse_toml(self, inhalt)`
        *   *Description:* This private method parses the content of a `pyproject.toml` file using the `tomllib` library. It attempts to extract the project's name, description, and dependencies, updating the class's internal `self.info` structure. If `tomllib` is not installed, it prints a warning and returns. It also includes error handling for `TOMLDecodeError` during parsing.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the pyproject.toml file.
        *   *Returns:*
            - *No return value specified.*
    *   **`_parse_requirements`**
        *   *Signature:* `def _parse_requirements(self, inhalt)`
        *   *Description:* This private method parses the content of a `requirements.txt` file to extract a list of dependencies. It processes the file line by line, stripping whitespace and ignoring lines that start with a '#' (comments). This method only populates the dependencies if they have not already been found and set by `_parse_toml`, acting as a fallback mechanism.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **inhalt** (`str`): The content of the requirements.txt file.
        *   *Returns:*
            - *No return value specified.*
    *   **`extrahiere_info`**
        *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
        *   *Description:* This public method orchestrates the entire process of extracting project information from a given list of file objects and a repository URL. It first identifies relevant files (README, pyproject.toml, requirements.txt) using `_finde_datei`. Then, it parses these files in a specific order of priority (`pyproject.toml` > `requirements.txt` > `README`) to populate the internal `self.info` structure. Finally, it formats the dependencies and sets the project title based on the repository URL before returning the complete information dictionary.
        *   *Parameters:*
            - **self** (`ProjektInfoExtractor`): The instance of the class.
            - **dateien** (`List[Any]`): A list of file objects, each expected to have 'path' and 'content' attributes.
            - **repo_url** (`str`): The URL of the repository, used to derive the project title.
        *   *Returns:*
            - **Dict[str, Any]** (`Dict[str, Any]`): A dictionary containing the extracted project information, structured into 'projekt_uebersicht' and 'installation' sections.

---
### File: `backend/callgraph.py`
#### Function: `build_callGraph`
*   **Signature:** `def build_callGraph(tree, filename)`
*   **Description:** This function constructs a call graph from a Python Abstract Syntax Tree (AST). The call graph is represented as a directed graph using the `networkx` library. Nodes in the graph represent functions, methods, and specific scopes like the global scope ('<module>') or the main execution block ('<main_block>'). Edges represent the calls made between these functions or methods. The function initializes a `CallGraph` visitor, traverses the AST using this visitor, and then populates the graph with edges based on the collected call information. Finally, it returns the constructed `networkx.DiGraph` object.
*   **Parameters:**
    - **tree** (`ast.AST`): The Abstract Syntax Tree (AST) of the Python file to be analyzed.
    - **filename** (`str`): The name of the analyzed file, used for context within the call graph, e.g., 'main.py' or 'src/utils.py'.
*   **Returns:**
    - **graph** (`nx.DiGraph`): The complete call graph as a directed graph object.
*   **Usage:**
    - **Calls:** `CallGraph`, `add_edge`, `items`, `visit`
    - **Called By:** `analyze_repository` (in class `ASTAnalyzer`), `build_global_callgraph` (in file `callgraph.py`)

---
#### Function: `graph_to_adj_list`
*   **Signature:** `def graph_to_adj_list(graph)`
*   **Description:** This function converts a directed graph (nx.DiGraph) from the networkx library into an adjacency list format, which is suitable for JSON serialization. It iterates through each node in the graph, retrieves its successors (functions it calls), and stores this relationship in a dictionary. The keys of the dictionary represent the calling nodes (callers), and the values are lists of the called nodes (callees). The function ensures a consistent output by sorting both the nodes and their successors before adding them to the adjacency list. Only nodes that have outgoing edges (i.e., call other functions) are included in the final adjacency list.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The directed graph representing the call graph to be converted.
*   **Returns:**
    - **adj_list** (`Dict[str, list[str]]`): An adjacency list where keys are caller nodes (strings) and values are lists of callee nodes (strings).
*   **Usage:**
    - **Calls:** `list`, `nodes`, `sorted`, `successors`
    - **Called By:** *This function is not called by any other functions in the provided context.*

---
#### Function: `build_global_callgraph`
*   **Signature:** `def build_global_callgraph(repo)`
*   **Description:** This function constructs a global call graph for a given Git repository. It iterates through all Python files in the repository, parses their Abstract Syntax Trees (ASTs), and builds a call graph for each file. These individual file call graphs are then merged into a single, comprehensive global call graph. The function uses the networkx library to represent the call graph as a directed graph.
*   **Parameters:**
    - **repo** (`GitRepository`): An object representing the Git repository to analyze.
*   **Returns:**
    - **global_graph** (`nx.DiGraph`): A directed graph representing the global call graph of the repository.
*   **Usage:**
    - **Calls:** `DiGraph`, `add_edge`, `add_node`, `basename`, `build_callGraph`, `endswith`, `get_all_files`, `parse`, `removesuffix`, `str`
    - **Called By:** `backend.callgraph` (in file `callgraph.py`)

---
#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** This function takes a NetworkX directed graph and an output path, then creates a sanitized version of the graph for DOT file output. It renames nodes to be simple integers prefixed with 'n' to avoid issues with special characters in node labels. The original node names are preserved as 'label' attributes on the new nodes. Finally, it writes the relabeled graph to a DOT file at the specified path.
*   **Parameters:**
    - **graph** (`nx.DiGraph`): The input directed graph object from the NetworkX library.
    - **out_path** (`str`): The file path where the DOT representation of the graph will be saved.
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `copy`, `enumerate`, `items`, `list`, `nodes`, `relabel_nodes`, `write_dot`
    - **Called By:** `backend.callgraph` (in file `callgraph.py`)

---
#### Class: `CallGraph`
*   **Summary:** The CallGraph class is an AST visitor designed to traverse Python code, identify function and method calls, and construct a directed graph representing these relationships. It processes different definition types (classes, functions, async functions) and call sites, resolving callee names based on context (filename, class, function) to build a comprehensive call graph. The class also handles special cases like `if __name__ == '__main__'` blocks to represent global script execution.
*   **Instantiation:** `build_callGraph` (in file `callgraph.py`)
*   **Dependencies:** This class utilizes the `ast` module for parsing Python code into an Abstract Syntax Tree and `networkx` for graph manipulation. It also uses typing hints like `Dict` and `str | None`.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph visitor by setting up attributes for tracking the current file, function, and class context. It also initializes data structures for storing the graph, import mappings, function sets, and call edges.
    *   *Parameters:*
        - **self** (`CallGraph`): The instance of the CallGraph class.
        - **filename** (`str`): The name of the file being processed.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* Recursively traverses an AST node to extract function call names. It handles different AST node types like `ast.Call`, `ast.Name`, and `ast.Attribute` to identify the callable entity. The method aims to return a list of strings representing the names of the called functions or methods.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.AST`): The AST node to process.
        *   *Returns:*
            - **all_calls** (`list[str]`): A list of strings representing the extracted call names.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* Resolves raw callee names into fully qualified names based on the current file and class context. If a class context is available, it prepends the filename and class name; otherwise, it only prepends the filename. This ensures that callee names are unique within the context of the analysis.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **callee_nodes** (`list[str]`): A list of raw callee names to resolve.
        *   *Returns:*
            - **resolved_callees** (`list[str]`): A list of fully qualified callee names.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name)`
        *   *Description:* Constructs a fully qualified name for a function or method by combining the filename, an optional class name, and the base name. This method ensures consistent naming for nodes within the call graph.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **basename** (`str`): The base name of the function or method.
            - **class_name** (`str | None`): The name of the class, if the function is a method.
        *   *Returns:*
            - **full_name** (`str`): The fully qualified name.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* Determines the current caller's name for logging or graph construction. It returns the `self.current_function` if set, otherwise it constructs a name based on the filename or a global scope indicator.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
        *   *Returns:*
            - **caller_name** (`str`): The name of the current caller.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Visits a class definition node in the AST. It updates the `current_class` attribute to the name of the class being visited, then recursively visits all nodes within the class body (functions, methods, nested classes). Finally, it restores the `current_class` to its previous value.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Visits a standard function definition node (`def`). It sets the `current_function` attribute, adds the function as a node to the graph, recursively visits the function's body using `generic_visit`, adds the function to a set of all functions, and then resets `current_function`.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Visits an asynchronous function definition node (`async def`). This method simply delegates the processing to `visit_FunctionDef`, indicating that asynchronous functions are treated similarly to regular functions in terms of call graph construction.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.AsyncFunctionDef`): The AST node representing an asynchronous function definition.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Visits a function or method call node. It identifies the caller, extracts raw callee names using `_recursive_call`, resolves these names to fully qualified identifiers using `_resolve_all_callee_names`, and then adds edges to the call graph. It includes error handling to prevent crashes on unexpected call structures.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.Call`): The AST node representing a function or method call.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* Visits an `if` statement node. It specifically checks if the condition is `__name__ == '__main__'`, a common pattern for script entry points. If it is, it temporarily sets the `current_function` to '<main_block>' to treat calls within this block as originating from the script's main execution context, then proceeds with generic traversal. Otherwise, it just performs generic traversal.
        *   *Parameters:*
            - **self** (`CallGraph`): The instance of the CallGraph class.
            - **node** (`ast.If`): The AST node representing an if statement.
        *   *Returns:*
            - *No return value specified.*

---
### File: `backend/getRepo.py`
#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It is designed for lazy loading of file content and metadata, meaning that attributes like the file's blob object, content, and size are only fetched when they are first accessed. This approach optimizes performance by avoiding unnecessary data retrieval. The class provides methods to access file properties, analyze its content (e.g., word count), and represent the file as a dictionary.
*   **Instantiation:** `get_all_files` (in class `GitRepository`)
*   **Dependencies:** This class depends on the 'git' library for Git repository operations and the 'os' module for path manipulation.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object, setting up the file's path and its associated commit tree. It also initializes internal attributes for lazy loading of the blob, content, and size, setting them to None initially.
    *   *Parameters:*
        - **file_path** (`str`): The path to the file within the repository.
        - **commit_tree** (`git.Tree`): The Tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* This property lazily loads and returns the Git blob object for the file. If the blob has not been loaded yet, it attempts to retrieve it from the associated commit tree using the file's path. If the file is not found in the tree, it raises a FileNotFoundError. Once loaded, the blob object is cached for subsequent access.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the RepoFile class.
        *   *Returns:*
            - **self._blob** (`git.Blob`): The Git blob object representing the file.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* This property lazily loads and returns the decoded content of the file. It first ensures the blob object is loaded by accessing `self.blob`. Then, it reads the data from the blob's data stream, decodes it as UTF-8 with error handling for ignored characters, and caches the result. This ensures the file content is only read and decoded when explicitly requested.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the RepoFile class.
        *   *Returns:*
            - **self._content** (`str`): The decoded content of the file as a string.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* This property lazily loads and returns the size of the file in bytes. It first ensures the blob object is loaded by accessing `self.blob`. Then, it retrieves the size attribute from the blob object and caches it. This ensures the file size is only fetched when needed.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the RepoFile class.
        *   *Returns:*
            - **self._size** (`int`): The size of the file in bytes.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* This method performs a sample analysis on the file's content by counting the number of words. It accesses the file's content via `self.content`, splits the content into words using whitespace as a delimiter, and then returns the total count of these words. This serves as an example of how file content can be processed.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the RepoFile class.
        *   *Returns:*
            - **word_count** (`int`): The total number of words found in the file's content.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* This method provides a developer-friendly string representation of the RepoFile object. It returns a formatted string that includes the class name and the file's path, making it easy to identify the object when debugging or inspecting.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the RepoFile class.
        *   *Returns:*
            - **representation** (`str`): A string representation of the RepoFile object, e.g., "<RepoFile(path='...')>".
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content)`
        *   *Description:* This method converts the RepoFile object's relevant information into a dictionary. By default, it includes the file's path, its base name, its size, and its type ('file'). Optionally, if `include_content` is set to True, it also includes the file's content in the dictionary. This is useful for serializing file information.
        *   *Parameters:*
            - **self** (`RepoFile`): The instance of the RepoFile class.
            - **include_content** (`bool`): A flag to indicate whether to include the file's content in the returned dictionary. Defaults to False.
        *   *Returns:*
            - **data** (`dict`): A dictionary containing file metadata, and optionally its content.

---
#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory. It provides methods to access files within the repository, retrieve them as RepoFile objects, and construct a hierarchical file tree representation. The class is designed to be used as a context manager, ensuring that the temporary directory is cleaned up after use.
*   **Instantiation:** `main_workflow` (in file `main.py`)
*   **Dependencies:** This class depends on external libraries such as `tempfile` for temporary directory management, `shutil` for file operations (though commented out in `close`), `git.Repo` and `git.GitCommandError` for Git operations, `logging` for information messages, and `os` (implicitly used by other modules). It also relies on a `RepoFile` class which is not defined in the provided source.
*   **Constructor:**
    *   *Description:* Initializes the GitRepository by storing the repository URL, creating a temporary directory, and cloning the repository into it. It attempts to clone the repository and retrieves the latest commit and its tree. If cloning fails, it cleans up and raises a RuntimeError.
    *   *Parameters:*
        - **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* Retrieves all files from the cloned Git repository. It uses the Git command `ls-files` to get a list of file paths, then creates a `RepoFile` object for each path, associating it with the current commit's tree. This method populates and returns a list of `RepoFile` objects representing all files in the repository.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **files** (`list[RepoFile]`): A list of RepoFile objects, each representing a file in the repository.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* Cleans up the GitRepository by removing the temporary directory and its contents. If a temporary directory was created, it prints a message indicating its deletion and then sets the `temp_dir` attribute to `None` to signify that cleanup has occurred.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - *No return value specified.*
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* Enters the runtime context manager for the GitRepository. It simply returns the instance of the GitRepository itself, allowing it to be used in a `with` statement.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
        *   *Returns:*
            - **self** (`GitRepository`): The current instance of the GitRepository.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* Exits the runtime context manager for the GitRepository. It ensures that the `close` method is called to clean up the temporary directory and its contents, regardless of whether an exception occurred within the `with` block.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
            - **exc_type** (`type`): The type of the exception raised, if any.
            - **exc_val** (`Exception`): The exception instance raised, if any.
            - **exc_tb** (`traceback`): The traceback object for the exception, if any.
        *   *Returns:*
            - *No return value specified.*
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content)`
        *   *Description:* Constructs and returns a hierarchical tree representation of the files in the repository. If no files have been loaded, it first calls `get_all_files()` to populate the file list. It then iterates through the files, parsing their paths to build a nested dictionary structure representing directories and files, optionally including file content.
        *   *Parameters:*
            - **self** (`GitRepository`): The instance of the GitRepository class.
            - **include_content** (`bool`): A boolean flag indicating whether to include the content of each file in the output dictionary. Defaults to False.
        *   *Returns:*
            - **tree** (`dict`): A dictionary representing the file tree structure of the repository.

---
### File: `backend/main.py`
#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** This function calculates the net processing time by subtracting estimated sleep times from the total duration. It is specifically designed to account for rate-limiting delays when processing items in batches, particularly for models starting with 'gemini-'. If the model name does not start with 'gemini-', the total duration is returned directly. If there are no items to process, it returns 0. Otherwise, it calculates the number of batches, the total sleep time based on the number of batches, and then subtracts this sleep time from the total duration, ensuring the net time is not negative.
*   **Parameters:**
    - **start_time** (`Any`): The timestamp when the process started.
    - **end_time** (`Any`): The timestamp when the process ended.
    - **total_items** (`int`): The total number of items being processed.
    - **batch_size** (`int`): The number of items processed in each batch.
    - **model_name** (`str`): The name of the model being used, used to determine if rate-limiting logic should be applied.
*   **Returns:**
    - **net_time** (`Any`): The calculated net processing time after subtracting estimated sleep times, or the total duration if rate-limiting logic is not applicable. Returns 0 if total_items is 0.
*   **Usage:**
    - **Calls:** `ceil`, `max`, `startswith`
    - **Called By:** `main_workflow` (in file `main.py`)

---
#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
*   **Description:** This function orchestrates a complex workflow for analyzing a software repository and generating documentation. It begins by extracting information from the input, including API keys and model names, and then proceeds to clone the specified repository. The function analyzes the repository's structure, extracts basic project information, constructs a file tree, and performs relationship analysis (calls and instantiations). It then generates an Abstract Syntax Tree (AST) schema and enriches it with the relationship data. Finally, it prepares inputs for two language models: a Helper LLM to analyze individual functions and classes, and a Main LLM to generate a final report based on all the collected and analyzed data. The function also handles status callbacks, logging, and error management throughout the process.
*   **Parameters:**
    - **input** (`Any`): The primary input to the workflow, likely containing user queries or project details.
    - **api_keys** (`dict`): A dictionary containing API keys for various services like Gemini and OpenAI.
    - **model_names** (`dict`): A dictionary specifying the names of the models to be used for helper and main LLM tasks.
    - **status_callback** (`Callable`): An optional callback function to report the status of the workflow's progress.
*   **Returns:**
    - **report** (`str`): The final generated report, typically in Markdown format.
    - **metrics** (`dict`): A dictionary containing performance metrics for the workflow, including execution times and models used.
*   **Usage:**
    - **Calls:** *This function is a high-level orchestrator and calls numerous other components which are documented individually.*
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`), `backend.main` (in file `main.py`)

---
#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** This function is designed to report status updates. It first checks if a `status_callback` function is defined and, if so, calls it with the provided message. Subsequently, it logs the message using the `logging.info` function. This dual approach ensures that status messages are both communicated through a potential callback mechanism and recorded for logging purposes.
*   **Parameters:**
    - **msg** (`Any`): The status message to be reported and logged.
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `info`, `status_callback`
    - **Called By:** `main_workflow` (in file `main.py`)

---
### File: `backend/relationship_analyzer.py`
#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** This function converts a given file path into a Python module path. It first calculates the relative path of the file with respect to a project root. If the file is a Python file (ends with '.py'), the extension is removed. The path separators are then replaced with dots to form a module path. Special handling is included for '__init__.py' files, where the '__init__' suffix is removed from the module path.
*   **Parameters:**
    - **filepath** (`str`): The absolute or relative path to the file.
    - **project_root** (`str`): The root directory of the project, used to determine the relative path.
*   **Returns:**
    - **module_path** (`str`): The calculated Python module path string.
*   **Usage:**
    - **Calls:** `basename`, `endswith`, `relpath`, `replace`
    - **Called By:** `_collect_definitions` (in class `ProjectAnalyzer`), `__init__` (in class `CallResolverVisitor`)

---
#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to parse a Python project, identify all defined functions, classes, and methods, and build a call graph representing their relationships. It traverses the project directory, collects definitions using Python's AST module, resolves function and method calls, and formats the results into a structured output. This class is a core component for understanding code structure and dependencies within a Python project.
*   **Instantiation:** `main_workflow` (in file `main.py`)
*   **Dependencies:** This class relies on Python's built-in `ast` module for parsing code, `os` for file system operations, `logging` for error reporting, and `collections.defaultdict` for managing the call graph. It also implicitly depends on external components like `path_to_module` and `CallResolverVisitor` which are not defined within this class but are used in its methods.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with the root directory of the project. It sets up internal data structures to store file Abstract Syntax Trees (ASTs), definitions (functions, classes, methods), and the call graph. It also defines a set of directories to ignore during the file traversal.
    *   *Parameters:*
        - **project_root** (`string`): The absolute path to the root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* This is the main method to initiate the project analysis. It first finds all Python files within the project, then iterates through them to collect all definitions (functions, classes, methods). Subsequently, it resolves the call relationships between these definitions. Finally, it clears the stored ASTs to free up memory and returns the formatted results of the analysis.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
        *   *Returns:*
            - **output_list** (`list`): A list of dictionaries, where each dictionary represents a definition (function, class, or method) and details the calls made to it, including the origin file, line number, and caller information.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* Recursively walks through the project directory starting from `self.project_root` to find all Python files (`.py`). It respects the `self.ignore_dirs` set to exclude specific directories from the search, ensuring that irrelevant directories like version control metadata or virtual environments are skipped. The method collects the absolute paths of all found Python files.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
        *   *Returns:*
            - **py_files** (`list`): A list of strings, where each string is the absolute path to a Python file found in the project.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* Reads the source code of a given Python file, parses it into an Abstract Syntax Tree (AST) using the `ast` module, and stores the tree in `self.file_asts`. It then traverses the AST to identify and record definitions of functions, classes, and methods. For each definition, it stores its file path, line number, type (function, class, or method), and constructs a unique path name. Errors during file reading or parsing are logged, and the AST for the problematic file is set to `None`.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
            - **filepath** (`string`): The absolute path to the Python file to analyze for definitions.
        *   *Returns:*
            - *No return value specified.*
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* This utility method traverses the AST of a given tree to find the parent node of a specific child node. It iterates through all nodes in the tree and checks their direct children. If a child matches the provided `node`, the parent node is returned. If the node is not found within the tree's hierarchy, it returns `None`.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
            - **tree** (`ast.AST`): The Abstract Syntax Tree to search within.
            - **node** (`ast.AST`): The child node whose parent is to be found.
        *   *Returns:*
            - **parent** (`ast.AST | None`): The parent AST node of the given `node`, or `None` if the node is the root or not found.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* Resolves the call relationships within a given Python file by utilizing a `CallResolverVisitor`. It retrieves the AST for the file from `self.file_asts`. If the AST exists, it instantiates `CallResolverVisitor` with the file path, project root, and collected definitions. The visitor then traverses the AST to identify calls, and the results (callee pathnames and caller information) are aggregated into the `self.call_graph`. Errors during this process are logged.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
            - **filepath** (`string`): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
            - *No return value specified.*
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* Formats the collected call graph and definitions into a structured list suitable for output. It iterates through the `self.call_graph`, and for each callee, it retrieves its definition information. It then processes the callers, ensuring uniqueness based on file, line, and caller name, and formats this information into a dictionary. This dictionary, containing the callee's identifier, mode, origin file, origin line, and a list of callers, is added to the output list. Definitions not found in `self.definitions` are skipped.
        *   *Parameters:*
            - **self** (`ProjectAnalyzer`): The instance of the ProjectAnalyzer class.
        *   *Returns:*
            - **output_list** (`list`): A list of dictionaries, where each dictionary details a definition (function, class, or method) and includes information about where it is called from (file, line, caller name, caller type).

---
#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor is an Abstract Syntax Tree (AST) visitor designed to traverse Python code and identify function and method calls. It resolves the fully qualified names of called functions and methods, keeping track of the call graph within a project. This visitor is crucial for understanding code dependencies and call relationships.
*   **Instantiation:** `_resolve_calls` (in class `ProjectAnalyzer`)
*   **Dependencies:** This class utilizes the 'ast' module for parsing Python code into an Abstract Syntax Tree, the 'os' module for path manipulation (specifically `os.path.basename`), and 'collections.defaultdict' for managing the call graph. It also implicitly relies on helper functions like `path_to_module` which are not defined within this class.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with essential context for analyzing code. It stores the file path, derives the module path, and holds a reference to the project's definitions. It also sets up internal state for tracking scope, instance types, the current caller, and the call graph.
    *   *Parameters:*
        - **filepath** (`str`): The absolute path to the Python file being analyzed.
        - **project_root** (`str`): The root directory of the project, used to determine module paths.
        - **definitions** (`dict`): A dictionary containing definitions of functions and classes within the project.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Visits a class definition node in the AST. It temporarily stores the current class name, updates the current class name to the newly visited class, recursively visits child nodes within the class definition, and then restores the previous class name. This allows for tracking the class context during traversal.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.ClassDef`): The AST node representing a class definition.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Visits a function definition node in the AST. It temporarily stores the current caller name, updates it to the name of the function being visited, recursively visits any child nodes within the function definition, and then restores the original caller name. This mechanism helps in tracking the current function or method context.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.FunctionDef`): The AST node representing a function definition.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Visits a function call node in the AST. It resolves the fully qualified name of the called function using `_resolve_call_qname`. If the called function is found in the project's definitions, it records the call information, including the caller's file, line number, name, and type (module, method, or function). Finally, it continues the traversal to child nodes.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.Call`): The AST node representing a function call.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Visits an import statement (e.g., `import module` or `import module as alias`). It updates the visitor's scope dictionary to map the imported name (or its alias) to its module path. This helps in resolving names used later in the code. It then proceeds to visit child nodes.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.Import`): The AST node representing an import statement.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Visits a 'from ... import ...' statement. It determines the full module path based on the import level and the current module path, then updates the scope dictionary to map imported names (or their aliases) to their qualified module paths. This is essential for resolving names that are imported from other modules. It continues traversal to child nodes.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.ImportFrom`): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
            - *No return value specified.*
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* Visits an assignment statement. It specifically checks if the assignment involves calling a class constructor (e.g., `var = ClassName()`). If so, it resolves the qualified name of the class using the scope and stores the mapping from the variable name to the qualified class name in `self.instance_types`. This helps in tracking the types of instantiated objects. It then proceeds to visit child nodes.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **node** (`ast.Assign`): The AST node representing an assignment statement.
        *   *Returns:*
            - *No return value specified.*
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* Resolves the fully qualified name (QName) of a function or method call based on the AST node representing the function being called. It handles direct names (e.g., `func()`) by checking the scope and local module path, and attribute access (e.g., `obj.method()`) by using the `instance_types` and `scope` to reconstruct the QName. Returns `None` if the name cannot be resolved.
        *   *Parameters:*
            - **self** (`CallResolverVisitor`): The instance of the visitor.
            - **func_node** (`ast.expr`): The AST node representing the function or method being called (e.g., ast.Name or ast.Attribute).
        *   *Returns:*
            - **qualified_name** (`str | None`): The fully qualified name of the function/method, or None if it cannot be resolved.

---
### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** This function encrypts a given string using a pre-configured cipher suite. It first checks if the input text is empty or if the cipher suite is not initialized. If either condition is true, it returns the original text without encryption. Otherwise, it encodes the text into bytes, encrypts the bytes using the cipher suite, and then decodes the resulting encrypted bytes back into a string before returning it.
*   **Parameters:**
    - **text** (`str`): The plain text string to be encrypted.
*   **Returns:**
    - **encrypted_text** (`str`): The encrypted string, or the original string if encryption was not performed.
*   **Usage:**
    - **Calls:** `decode`, `encode`, `encrypt`
    - **Called By:** `update_gemini_key` (in file `db.py`)

---
#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** This function decrypts a given text string using a cipher suite. It first checks if the input text or the cipher suite is invalid, returning the original text if either is true. If valid, it attempts to decrypt the encoded text and decode the result. In case of any exception during decryption, it returns the original text.
*   **Parameters:**
    - **text** (`str`): The encrypted text string to be decrypted.
*   **Returns:**
    - **decrypted_text** (`str`): The decrypted text string. Returns the original text if decryption fails or if input is invalid.
*   **Usage:**
    - **Calls:** `decode`, `decrypt`, `encode`
    - **Called By:** `get_decrypted_api_keys` (in file `db.py`)

---
#### Function: `insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** This function inserts a new user record into a database collection named 'dbusers'. It takes a username, name, and password as input. The password is hashed using a specified hashing function before being stored along with the username and name. Additional fields like 'gemini_api_key' and 'ollama_base_url' are initialized as empty strings. The function returns the unique identifier of the newly inserted document.
*   **Parameters:**
    - **username** (`str`): The unique username for the new user, used as the document's ID.
    - **name** (`str`): The full name of the user.
    - **password** (`str`): The plain-text password for the new user, which will be hashed.
*   **Returns:**
    - **result.inserted_id** (`Any`): The unique identifier of the newly inserted user document in the database.
*   **Usage:**
    - **Calls:** `hash`, `insert_one`
    - **Called By:** *This function is not called by any other functions in the provided context.*

---
#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user records from a database. It interacts with a database collection named 'dbusers' and returns the entire set of documents found. The function is designed to fetch all available user data without any filtering or specific selection criteria.
*   **Parameters:**
    - *No parameters specified.*
*   **Returns:**
    - **users** (`list`): A list containing all user documents fetched from the database.
*   **Usage:**
    - **Calls:** `find`, `list`
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`)

---
#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** This function retrieves a single user record from a database based on their username. It queries a collection named 'dbusers' using the provided username as the document's '_id'. The function is designed to fetch user data for authentication or profile retrieval purposes.
*   **Parameters:**
    - **username** (`str`): The unique username of the user to fetch from the database.
*   **Returns:**
    - **user** (`Any`): A dictionary-like object representing the user document if found, otherwise None.
*   **Usage:**
    - **Calls:** `find_one`
    - **Called By:** *This function is not called by any other functions in the provided context.*

---
#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function updates the Gemini API key for a given user in the database. It first encrypts the provided API key using a helper function `encrypt_text`. Then, it uses `dbusers.update_one` to find the user by their username and set the `gemini_api_key` field to the encrypted value. The function returns the count of modified documents, indicating whether the update was successful.
*   **Parameters:**
    - **username** (`str`): The username of the user whose Gemini API key needs to be updated.
    - **gemini_api_key** (`str`): The new Gemini API key to be set for the user.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database. Typically 1 if the update was successful, 0 otherwise.
*   **Usage:**
    - **Calls:** `encrypt_text`, `update_one`
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`)

---
#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function updates the Ollama Base URL for a specific user in the database. It takes the username and the new Ollama Base URL as input. The function then uses the `dbusers.update_one` method to find the user document by their username and set the `ollama_base_url` field to the provided value. Finally, it returns the count of modified documents, which should ideally be 1 if the update was successful.
*   **Parameters:**
    - **username** (`str`): The unique identifier for the user whose Ollama Base URL needs to be updated.
    - **ollama_base_url** (`str`): The new base URL for the Ollama service to be associated with the user.
*   **Returns:**
    - **modified_count** (`int`): An integer representing the number of documents that were modified in the database. Typically 1 for a successful update.
*   **Usage:**
    - **Calls:** `update_one`
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`)

---
#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** This function retrieves the Gemini API key associated with a specific username from a database. It queries the database for a user document based on the provided username and extracts the 'gemini_api_key' field. If the key is found, it is returned; otherwise, `None` is returned.
*   **Parameters:**
    - **username** (`str`): The username of the user whose Gemini API key needs to be fetched.
*   **Returns:**
    - **gemini_api_key** (`str | None`): The Gemini API key for the specified user, or None if not found.
*   **Usage:**
    - **Calls:** `find_one`, `get`
    - **Called By:** *This function is not called by any other function in the provided context.*

---
#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** This function retrieves the Ollama Base URL associated with a given username from the database. It queries a user record based on the provided username and extracts the 'ollama_base_url' field. If the field is not present for the user, it returns None.
*   **Parameters:**
    - **username** (`str`): The username for which to fetch the Ollama Base URL.
*   **Returns:**
    - **ollama_base_url** (`str | None`): The Ollama Base URL for the specified user, or None if not found.
*   **Usage:**
    - **Calls:** `find_one`, `get`
    - **Called By:** *This function is not called by any other functions in the provided context.*

---
#### Function: `delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** This function deletes a user from the database based on their username. It interacts with a database collection named 'dbusers' to perform the deletion. The function returns the count of documents that were deleted.
*   **Parameters:**
    - **username** (`str`): The username of the user to be deleted from the database.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents deleted from the database, which should ideally be 1 if the user existed.
*   **Usage:**
    - **Calls:** `delete_one`
    - **Called By:** *This function is not called by any other function in the provided context.*

---
#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function retrieves and decrypts API keys for a given username from the database. It first fetches the user record using the provided username. If the user is not found, it returns None for both API keys. Otherwise, it decrypts the 'gemini_api_key' and retrieves the 'ollama_base_url', returning both decrypted values.
*   **Parameters:**
    - **username** (`str`): The username of the user whose API keys are to be retrieved.
*   **Returns:**
    - **gemini_plain** (`str`): The decrypted Gemini API key for the user.
    - **ollama_plain** (`str`): The Ollama base URL for the user.
*   **Usage:**
    - **Calls:** `decrypt_text`, `find_one`, `get`
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`)

---
#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used, main_used, total_time, helper_time, main_time)`
*   **Description:** This function inserts a new exchange record into a MongoDB collection. It takes various details about a user's interaction, such as the question, answer, feedback, username, chat name, and usage statistics for helper and main models, along with their respective times. It constructs a dictionary containing all these details, including a timestamp of when the record was created using `datetime.now()`. Finally, it inserts this dictionary as a document into the `dbexchanges` collection and returns the ID of the newly inserted document.
*   **Parameters:**
    - **question** (`str`): The user's question.
    - **answer** (`str`): The answer provided to the user's question.
    - **feedback** (`str`): User feedback on the answer.
    - **username** (`str`): The username of the user providing the exchange.
    - **chat_name** (`str`): The name of the chat session.
    - **helper_used** (`str`): Information about whether the helper model was used (default: '').
    - **main_used** (`str`): Information about whether the main model was used (default: '').
    - **total_time** (`str`): Total time taken for the exchange (default: '').
    - **helper_time** (`str`): Time taken by the helper model (default: '').
    - **main_time** (`str`): Time taken by the main model (default: '').
*   **Returns:**
    - **result.inserted_id** (`Any`): The unique identifier of the newly inserted exchange document.
*   **Usage:**
    - **Calls:** `insert_one`, `now`
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`)

---
#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** This function retrieves exchange records associated with a specific username from a database. It queries a collection named 'dbexchanges' for documents where the 'username' field matches the provided username. The results are then converted into a list and returned.
*   **Parameters:**
    - **username** (`str`): The username to filter exchange records by.
*   **Returns:**
    - **exchanges** (`list`): A list of exchange records matching the specified username.
*   **Usage:**
    - **Calls:** `find`, `list`
    - **Called By:** `load_data_from_db` (in file `Frontend.py`)

---
#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function retrieves a list of exchanges associated with a specific user and chat from a database. It queries the database for documents matching the provided username and chat name, then converts the result into a list. The function is designed to fetch historical chat data.
*   **Parameters:**
    - **username** (`str`): The username of the user whose exchanges are to be fetched.
    - **chat_name** (`str`): The name of the chat for which exchanges are to be fetched.
*   **Returns:**
    - **exchanges** (`list`): A list of dictionaries, where each dictionary represents an exchange document from the database.
*   **Usage:**
    - **Calls:** `find`, `list`
    - **Called By:** *This function is not called by any other functions in the provided context.*

---
#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** This function updates the feedback associated with a specific exchange in the database. It takes an exchange ID and an integer feedback value as input. The function then uses `dbexchanges.update_one` to find the exchange by its ID and set the new feedback value. Finally, it returns the count of documents that were modified, indicating the success of the update operation.
*   **Parameters:**
    - **exchange_id** (`Any`): The unique identifier of the exchange to be updated.
    - **feedback** (`int`): The new feedback value to be set for the exchange. This should be an integer.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database. Typically, this will be 1 if the update was successful, or 0 if the exchange ID was not found or the feedback value was the same.
*   **Usage:**
    - **Calls:** `update_one`
    - **Called By:** `handle_feedback_change` (in file `Frontend.py`)

---
#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** This function updates the feedback message associated with a specific exchange in the database. It takes an exchange ID and a feedback message string as input. The function then uses the `dbexchanges.update_one` method to locate the exchange by its ID and set the `feedback_message` field to the provided value. Finally, it returns the count of documents that were modified.
*   **Parameters:**
    - **exchange_id** (`any`): The unique identifier of the exchange to be updated.
    - **feedback_message** (`str`): The new feedback message to be associated with the exchange.
*   **Returns:**
    - **modified_count** (`int`): The number of documents that were modified in the database.
*   **Usage:**
    - **Calls:** `update_one`
    - **Called By:** `render_exchange` (in file `Frontend.py`)

---
#### Function: `delete_chats_by_user`
*   **Signature:** `def delete_chats_by_user(username, chat_name)`
*   **Description:** This function deletes all exchanges associated with a specific user and chat name from the database. It utilizes a helper function `dbexchanges.delete_many` to perform the deletion operation. The function then returns the count of documents that were successfully deleted.
*   **Parameters:**
    - **username** (`str`): The username of the user whose chats are to be deleted.
    - **chat_name** (`str`): The name of the chat from which exchanges should be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of chat exchanges that were deleted from the database.
*   **Usage:**
    - **Calls:** `delete_many`
    - **Called By:** `handle_delete_chat` (in file `Frontend.py`)

---
#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function deletes a specific exchange record from the database using its unique identifier. It interacts with a database collection named 'dbexchanges' and returns the count of deleted documents. The function is designed to remove a single entry based on the provided exchange ID.
*   **Parameters:**
    - **exchange_id** (`str`): The unique identifier of the exchange to be deleted.
*   **Returns:**
    - **deleted_count** (`int`): The number of documents that were deleted from the database. This is expected to be 1 if the exchange was found and deleted, or 0 otherwise.
*   **Usage:**
    - **Calls:** `delete_one`
    - **Called By:** `handle_delete_exchange` (in file `Frontend.py`)

---
### File: `frontend/Frontend.py`
#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** This function loads existing chat data from a database into the Streamlit session state. It initializes the session state for chats if it doesn't exist, then fetches chat exchanges for a given username from the database. The fetched exchanges are organized and appended to the session state, creating new chats or adding to existing ones. If no chats are found, a default 'Chat 1' is created. Finally, it sets the active chat to the first available chat or the newly created one and marks the data as loaded in the session state.
*   **Parameters:**
    - **username** (`str`): The username for whom to load chat data.
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `append`, `fetch_exchanges_by_user`, `get`, `keys`, `list`
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`)

---
#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function updates the feedback associated with an exchange object and persists this change to the database. It first modifies the 'feedback' field of the input dictionary 'ex' to the provided value 'val'. Subsequently, it calls a database function to update the feedback for the specific exchange identified by '_id' in the database. Finally, it triggers a rerun of the Streamlit application to reflect the changes.
*   **Parameters:**
    - **ex** (`dict`): A dictionary representing the exchange object, expected to contain at least '_id' and 'feedback' keys.
    - **val** (`any`): The new feedback value to be assigned to the exchange.
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `rerun`, `update_exchange_feedback`
    - **Called By:** `render_exchange` (in file `Frontend.py`)

---
#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function deletes an exchange from both the database and the application's state. It first removes the exchange record from the database using its ID and then removes the corresponding exchange object from the session state's chat data. Finally, it triggers a rerun of the Streamlit application to reflect the changes.
*   **Parameters:**
    - **chat_name** (`str`): The name of the chat session from which to delete the exchange.
    - **ex** (`dict`): A dictionary representing the exchange to be deleted, containing at least an '_id' key.
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `delete_exchange_by_id`, `remove`, `rerun`
    - **Called By:** `render_exchange` (in file `Frontend.py`)

---
#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** This function deletes a specified chat for a given username from the system. It first removes the chat data from the database using `db.delete_chats_by_user`. Subsequently, it deletes the chat from the session state. After deletion, it updates the `active_chat` session state to either the first available chat or creates a default 'Chat 1' if no chats remain. Finally, it triggers a rerun of the application to reflect these changes.
*   **Parameters:**
    - **username** (`str`): The username associated with the chat to be deleted.
    - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `delete_chats_by_user`, `keys`, `len`, `list`, `rerun`
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`)

---
#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text)`
*   **Description:** This function processes a given markdown text, specifically identifying and rendering blocks marked for Mermaid diagram visualization. It splits the input text based on ```mermaid delimiters. For regular text parts, it renders them using Streamlit's markdown function. For parts identified as Mermaid code, it attempts to render them graphically using `st_mermaid`; if this fails, it falls back to displaying the code block using Streamlit's `st.code` function with a mermaid language specification.
*   **Parameters:**
    - **markdown_text** (`str`): The input markdown text that may contain Mermaid diagram blocks.
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `code`, `enumerate`, `hash`, `markdown`, `split`, `st_mermaid`, `strip`
    - **Called By:** `render_exchange` (in file `Frontend.py`), `frontend.Frontend` (in file `Frontend.py`)

---
#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** This function renders a chat exchange, displaying the user's question and the assistant's answer. It includes a toolbar with buttons for positive/negative feedback, writing feedback, downloading the answer as a Markdown file, and deleting the message. The assistant's answer is displayed in a scrollable container, with support for rendering Mermaid diagrams within the text. The function uses Streamlit components to create the user interface and interacts with backend functions for handling feedback and deletions, as well as database operations for saving feedback messages.
*   **Parameters:**
    - **ex** (`dict`): A dictionary containing the exchange data, including 'question', 'answer', 'feedback' status, 'feedback_message', and '_id'.
    - **current_chat_name** (`str`): The name of the current chat session, used for handling message deletions.
*   **Returns:**
    - *No return value specified.*
*   **Usage:**
    - **Calls:** `button`, `caption`, `chat_message`, `columns`, `container`, `download_button`, `get`, `handle_delete_exchange`, `handle_feedback_change`, `popover`, `render_text_with_mermaid`, `rerun`, `sleep`, `success`, `text_area`, `update_exchange_feedback_message`, `write`
    - **Called By:** `frontend.Frontend` (in file `Frontend.py`)

---
### File: `schemas/types.py`
#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic model used to define the structure for describing a single parameter within a function or method. It captures the parameter's name, its data type, and a textual explanation of its purpose or usage.
*   **Instantiation:** This class is typically instantiated within schemas or data structures that require detailed descriptions of function or method parameters.
*   **Dependencies:** This class has no external dependencies beyond Pydantic's BaseModel.
*   **Constructor:**
    *   *Description:* Initializes a ParameterDescription object with the name, type, and description of a function parameter. This model is part of a larger schema for documenting code elements.
    *   *Parameters:*
        - **name** (`str`): The name of the parameter.
        - **type** (`str`): The data type of the parameter.
        - **description** (`str`): A textual description of the parameter's purpose or usage.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `ReturnDescription`
*   **Summary:** This class, ReturnDescription, is a Pydantic model designed to structure and validate information about a function's return value. It enforces that every return value must have a name, a type, and a descriptive string. This model is likely used within a larger system for documenting or analyzing code, ensuring consistency in how return values are represented.
*   **Instantiation:** This class is intended to be instantiated by systems that need to represent function return value descriptions, such as documentation generators or code analysis tools.
*   **Dependencies:** This class depends on the pydantic.BaseModel for its structure and validation capabilities.
*   **Constructor:**
    *   *Description:* The constructor for ReturnDescription initializes the object with three required string attributes: name, type, and description. These attributes define the characteristics of a function's return value.
    *   *Parameters:*
        - **name** (`str`): The name of the return value.
        - **type** (`str`): The data type of the return value.
        - **description** (`str`): A textual description of the return value.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to encapsulate the calling context of a function. It specifically details what other functions or methods a given function calls and which functions or methods call it. This is useful for understanding code flow and dependencies within a system.
*   **Instantiation:** This class is typically instantiated within systems that need to track and describe the invocation relationships between different code components, such as documentation generators or code analysis tools.
*   **Dependencies:** This class depends on Pydantic's BaseModel for its structure and validation capabilities.
*   **Constructor:**
    *   *Description:* Initializes the UsageContext model with information about the functions called and the functions that call it. It inherits from Pydantic's BaseModel for data validation.
    *   *Parameters:*
        - **calls** (`str`): A string describing the functions or methods that this function calls.
        - **called_by** (`str`): A string describing the functions or methods that call this function.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a function. It holds details about the function's overall purpose, its parameters, its return values, and its usage context within a larger system. This structure is likely used for documentation generation or code analysis tools.
*   **Instantiation:** This class is likely instantiated by systems that perform code analysis or documentation generation, where detailed information about functions needs to be structured and stored.
*   **Dependencies:** This class depends on Pydantic's BaseModel for its structure and validation. It also relies on the types ParameterDescription, ReturnDescription, and UsageContext, which are assumed to be defined elsewhere.
*   **Constructor:**
    *   *Description:* Initializes a FunctionDescription object. As this is a Pydantic model, initialization is handled by Pydantic's base model, which validates and assigns the provided attributes: overall description, a list of ParameterDescription objects, a list of ReturnDescription objects, and a UsageContext object.
    *   *Parameters:*
        - **overall** (`str`): A string providing an overall summary of the function's purpose and behavior.
        - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects, each detailing a parameter of the function.
        - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects, each detailing a return value of the function.
        - **usage_context** (`UsageContext`): A UsageContext object that describes how and where the function is called.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class serves as a Pydantic model to represent the structured analysis of a Python function. It encapsulates the function's identifier, a detailed description of its purpose, parameters, return values, and usage context, and optionally includes an error message if analysis failed. This model is designed to be a core component in a larger documentation generation system, providing a standardized format for function-level insights.
*   **Instantiation:** This class is intended to be instantiated by the main documentation generation system or other analysis tools that process Python code.
*   **Dependencies:** This class has no external dependencies beyond Pydantic's BaseModel and typing.Optional.
*   **Constructor:**
    *   *Description:* Initializes a FunctionAnalysis object, setting the core components of the function's analysis. It takes the function's identifier, a FunctionDescription object containing detailed analysis, and an optional error string. The error field defaults to None, indicating successful analysis unless otherwise specified.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the function being analyzed.
        - **description** (`FunctionDescription`): A FunctionDescription object containing the detailed analysis of the function, including its overall purpose, parameters, return values, and usage context.
        - **error** (`Optional[str]`): An optional string that holds an error message if the analysis of the function failed. Defaults to None.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to encapsulate the details of a class's initialization method (__init__). It serves to structure information about the constructor's purpose and its parameters, making it suitable for documentation generation or introspection systems.
*   **Instantiation:** This class is intended to be instantiated by systems that need to represent and process information about class constructors, such as documentation generators or code analysis tools.
*   **Dependencies:** This class has no external dependencies beyond Pydantic's BaseModel and typing.List.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription object. This constructor takes a description of the __init__ method and a list of ParameterDescription objects, which detail each parameter of the constructor.
    *   *Parameters:*
        - **description** (`str`): A textual summary of the __init__ method's purpose and behavior.
        - **parameters** (`List[ParameterDescription]`): A list containing ParameterDescription objects, where each object details a parameter of the __init__ method.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to describe a class's external dependencies and its primary points of instantiation. It serves as a structured way to document how a class interacts with other parts of a system and where it is typically created.
*   **Instantiation:** This class is not instantiated by any other classes or functions mentioned in the provided context.
*   **Dependencies:** This class does not have any external dependencies listed.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext object with details about the class's dependencies and instantiation points. It directly assigns the provided values to the corresponding attributes.
    *   *Parameters:*
        - **dependencies** (`str`): A string describing the external dependencies of the class.
        - **instantiated_by** (`str`): A string describing where the class is typically instantiated.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class serves as a Pydantic model to structure the comprehensive analysis of a Python class. It encapsulates the class's overall purpose, a detailed description of its constructor (__init__ method), an analysis of all its other methods, and its usage context including dependencies and instantiation points.
*   **Instantiation:** This class is intended to be instantiated by systems that perform code analysis and require a structured way to represent the findings about a Python class.
*   **Dependencies:** This class depends on Pydantic's BaseModel for its structure and validation. It also utilizes types from the 'typing' module, specifically List.
*   **Constructor:**
    *   *Description:* The constructor for ClassDescription initializes a new instance of the class by assigning values to its attributes. These attributes correspond to the different components of a class analysis: overall description, constructor details, method analyses, and usage context.
    *   *Parameters:*
        - **overall** (`str`): A string representing the overall purpose and responsibilities of the class.
        - **init_method** (`ConstructorDescription`): A ConstructorDescription object detailing the class's initialization method.
        - **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects, each detailing a method within the class.
        - **usage_context** (`ClassContext`): A ClassContext object providing information about the class's dependencies and where it is instantiated.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis model represents the overall structure for analyzing a Python class. It encapsulates the class's identifier, a detailed description of its components (constructor, methods, and usage context), and an optional error field for reporting analysis issues. This model serves as the primary output for the class analysis process.
*   **Instantiation:** This class is not shown to be instantiated within the provided source code snippet.
*   **Dependencies:** This class does not explicitly declare external dependencies within its source code.
*   **Constructor:**
    *   *Description:* Initializes a ClassAnalysis object. It takes the class identifier, a ClassDescription object containing the detailed analysis, and an optional error string. The error defaults to None, indicating successful analysis.
    *   *Parameters:*
        - **identifier** (`str`): The name of the class being analyzed.
        - **description** (`ClassDescription`): An object containing the detailed analysis of the class, including its overall purpose, constructor, methods, and usage context.
        - **error** (`Optional[str]`): An optional string that holds an error message if the analysis failed; otherwise, it is None.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `CallInfo`
*   **Summary:** The CallInfo class is a Pydantic model used to represent detailed information about a specific call event within a system. It captures the source file, the name of the calling function or method, the mode of the call (e.g., 'method', 'function', 'module'), and the line number where the call occurred. This structure is particularly useful for documenting relationships between different parts of the code, such as identifying which functions call a particular piece of code or where a specific class is instantiated.
*   **Instantiation:** This class is intended to be instantiated by systems that track code relationships, such as a relationship analyzer, and is used in lists like 'called_by' and 'instantiated_by'.
*   **Dependencies:** This class has no external dependencies beyond Pydantic's BaseModel.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo object with details about a specific call event. It sets the file, function, mode, and line number associated with the call.
    *   *Parameters:*
        - **file** (`str`): The name of the file where the call originated.
        - **function** (`str`): The name of the calling function or method.
        - **mode** (`str`): The mode of the call, such as 'method', 'function', or 'module'.
        - **line** (`int`): The line number in the source file where the call occurred.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to structure the input context for analyzing a function. It specifically captures information about other functions or methods that a given function calls and which functions or methods call it. This is useful for understanding function dependencies and call graphs within a codebase.
*   **Instantiation:** `main_workflow` (in file `main.py`)
*   **Dependencies:** This class depends on Pydantic's BaseModel for its structure and typing.List and CallInfo for its parameter types.
*   **Constructor:**
    *   *Description:* Initializes the FunctionContextInput model. It takes lists of strings for calls and CallInfo objects for called_by to define the context of a function.
    *   *Parameters:*
        - **calls** (`List[str]`): A list of strings, where each string represents a function or method called by the function being analyzed.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects, where each object details a function or method that calls the function being analyzed.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class is a Pydantic model designed to encapsulate all necessary information required for analyzing a Python function. It serves as a structured input for a function analysis process, ensuring that all relevant data like the function's identifier, source code, import statements, and contextual information are provided in a standardized format.
*   **Instantiation:** `main_workflow` (in file `main.py`)
*   **Dependencies:** This class does not have any external functional dependencies listed.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput model with all the required fields for function analysis. It takes the analysis mode, function identifier, source code, a list of import statements, and a FunctionContextInput object as arguments.
    *   *Parameters:*
        - **mode** (`Literal["function_analysis"]`): Specifies the analysis mode, which must be 'function_analysis' for this input type.
        - **identifier** (`str`): The unique name or identifier of the function to be analyzed.
        - **source_code** (`str`): The raw source code of the function.
        - **imports** (`List[str]`): A list of import statements relevant to the source code file where the function is defined.
        - **context** (`FunctionContextInput`): A nested object containing contextual information relevant to the function's analysis, such as its dependencies and call relationships.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to structure contextual information about a class's methods. It captures details such as the method's identifier, lists of other methods or functions it calls and is called by, its arguments, and an optional docstring. This structure is useful for documentation generation or code analysis tools.
*   **Instantiation:** `main_workflow` (in file `main.py`)
*   **Dependencies:** This class depends on Pydantic's BaseModel for its structure and validation. It also utilizes types from the typing module (List, Optional) and potentially a custom 'CallInfo' type.
*   **Constructor:**
    *   *Description:* Initializes a MethodContextInput object, which is a Pydantic model. It takes the identifier, calls, called_by, args, and an optional docstring as input to define the context of a method.
    *   *Parameters:*
        - **identifier** (`str`): The unique name or identifier of the method.
        - **calls** (`List[str]`): A list of identifiers for methods or functions that this method calls.
        - **called_by** (`List[CallInfo]`): A list of CallInfo objects indicating where this method is called from.
        - **args** (`List[str]`): A list of argument names for the method.
        - **docstring** (`Optional[str]`): An optional docstring describing the method.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput model is a Pydantic BaseModel designed to structure the contextual information required for analyzing a Python class. It encapsulates details about the class's dependencies, where it is instantiated, and the context of its individual methods. This structured data is crucial for AI-driven code analysis and documentation generation systems.
*   **Instantiation:** `main_orchestrator` (in file `HelperLLM.py`), `main_workflow` (in file `main.py`)
*   **Dependencies:** This class does not explicitly list any external dependencies within its own definition, but its fields suggest it might interact with or represent information about dependencies.
*   **Constructor:**
    *   *Description:* Initializes the ClassContextInput model with lists of dependencies, instantiation information, and method contexts. It leverages Pydantic's BaseModel for data validation.
    *   *Parameters:*
        - **dependencies** (`List[str]`): A list of strings representing external dependencies of the class.
        - **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects detailing where instances of the class are created.
        - **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects, each providing context for a specific method within the class.
*   **Methods:**
    *   *No methods defined.*

---
#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class is a Pydantic model designed to define the structure of input data required for a class analysis process. It specifies the mode of operation, the identifier of the class to be analyzed, its source code, a list of relevant imports, and a context object containing additional information such as dependencies and instantiation details.
*   **Instantiation:** `main_orchestrator` (in file `HelperLLM.py`), `main_workflow` (in file `main.py`)
*   **Dependencies:** This class does not appear to have any external code dependencies beyond the Pydantic library for its model definition.
*   **Constructor:**
    *   *Description:* Initializes a ClassAnalysisInput object, validating the input data against the defined schema. It takes the mode, identifier, source code, imports, and context as arguments, ensuring that all required fields are present and correctly typed according to Pydantic's validation rules.
    *   *Parameters:*
        - **mode** (`Literal["class_analysis"]`): Specifies the analysis mode, which must be 'class_analysis' for this input type.
        - **identifier** (`str`): The name or identifier of the class that is the subject of the analysis.
        - **source_code** (`str`): The raw source code of the class definition to be analyzed.
        - **imports** (`List[str]`): A list of import statements relevant to the source code, which may include both used and unused imports.
        - **context** (`ClassContextInput`): An object containing contextual information for the analysis, such as dependencies and instantiation points.
*   **Methods:**
    *   *No methods defined.*

---
# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
- **Description:** This project implements a comprehensive repository onboarding agent designed to automate the generation of technical documentation. It clones Git repositories, analyzes their Abstract Syntax Trees (ASTs), extracts detailed information about functions and classes using specialized Helper LLMs, and synthesizes this data into human-readable Markdown reports via a Main LLM. The system also includes a Streamlit-based frontend for user interaction, repository input, and documentation display, complete with user authentication and chat history management.
- **Key Features:** 
  - Automated Documentation Generation
  - Repository Analysis (AST, Call Graphs)
  - LLM Integration for Code Description
  - Interactive Streamlit Frontend with User Management
  - Token Usage Optimization
- **Tech Stack:** Python, Streamlit, LangChain, Google Gemini/Ollama/OpenAI (LLMs), PyMongo (MongoDB), GitPython, NetworkX, Pydantic, Matplotlib, TOON format.

*   **Repository Structure:**
    ```mermaid
    graph LR
        root --> A(backend<br/>database<br/>frontend<br/>notizen<br/>result<br/>schemas<br/>statistics<br/>SystemPrompts<br/>.env.example<br/>.gitignore<br/>analysis_output.json<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt)
        A --> B(SystemPrompts<br/>backend<br/>database<br/>frontend<br/>notizen<br/>result<br/>schemas<br/>statistics)
        B --> C(SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt)
        B --> D(backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py)
        B --> E(database<br/>db.py)
        B --> F(frontend<br/>.streamlit<br/>Frontend.py<br/>__init__.py<br/>gifs)
        F --> G(.streamlit<br/>gifs)
        G --> H(.streamlit<br/>config.toml)
        G --> I(gifs<br/>4j.gif)
        B --> J(notizen<br/>grafiken<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md)
        J --> K(grafiken<br/>1<br/>2<br/>Flask-Repo<br/>Repo-onboarding)
        K --> L(1<br/>File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot)
        K --> M(2<br/>FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot)
        K --> N(Flask-Repo<br/>__init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_config.png<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot)
        K --> O(Repo-onboarding<br/>AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot)
        B --> P(result<br/>ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md<br/>report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md<br/>report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md<br/>report_14_11_2025_14-52-36.md<br/>report_14_11_2025_15-21-53.md<br/>report_14_11_2025_15-26-24.md<br/>report_21_11_2025_15-43-30.md<br/>report_21_11_2025_16-06-12.md<br/>report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md<br/>report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md<br/>result_2025-11-11_12-30-53.md<br/>result_2025-11-11_12-43-51.md<br/>result_2025-11-11_12-45-37.md)
        B --> Q(schemas<br/>types.py)
        B --> R(statistics<br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png<br/>savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png<br/>savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png<br/>savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png)
    ```

## 2. Installation
### Dependencies
- a l t a i r = = 4 . 2 . 2 
- a n n o t a t e d - t y p e s = = 0 . 7 . 0 
- a n y i o = = 4 . 1 1 . 0 
- a t t r s = = 2 5 . 4 . 0 
- b c r y p t = = 5 . 0 . 0 
- b l i n k e r = = 1 . 9 . 0 
- c a c h e t o o l s = = 6 . 2 . 2 
- c a p t c h a = = 0 . 7 . 1 
- c e r t i f i = = 2 0 2 5 . 1 1 . 1 2 
- c f f i = = 2 . 0 . 0 
- c h a r s e t - n o r m a l i z e r = = 3 . 4 . 4 
- c l i c k = = 8 . 3 . 1 
- c o l o r a m a = = 0 . 4 . 6 
- c o n t o u r p y = = 1 . 3 . 3 
- c r y p t o g r a p h y = = 4 6 . 0 . 3 
- c y c l e r = = 0 . 1 2 . 1 
- d i s t r o = = 1 . 9 . 0 
- d n s p y t h o n = = 2 . 8 . 0 
- d o t e n v = = 0 . 9 . 9 
- e n t r y p o i n t s = = 0 . 4 
- e x t r a - s t r e a m l i t - c o m p o n e n t s = = 0 . 1 . 8 1 
- f i l e t y p e = = 1 . 2 . 0 
- f o n t t o o l s = = 4 . 6 1 . 0 
- g i t d b = = 4 . 0 . 1 2 
- G i t P y t h o n = = 3 . 1 . 4 5 
- g o o g l e - a i - g e n e r a t i v e l a n g u a g e = = 0 . 9 . 0 
- g o o g l e - a p i - c o r e = = 2 . 2 8 . 1 
- g o o g l e - a u t h = = 2 . 4 3 . 0 
- g o o g l e a p i s - c o m m o n - p r o t o s = = 1 . 7 2 . 0 
- g r p c i o = = 1 . 7 6 . 0 
- g r p c i o - s t a t u s = = 1 . 7 6 . 0 
- h 1 1 = = 0 . 1 6 . 0 
- h t t p c o r e = = 1 . 0 . 9 
- h t t p x = = 0 . 2 8 . 1 
- i d n a = = 3 . 1 1 
- J i n j a 2 = = 3 . 1 . 6 
- j i t e r = = 0 . 1 2 . 0 
- j s o n p a t c h = = 1 . 3 3 
- j s o n p o i n t e r = = 3 . 0 . 0 
- j s o n s c h e m a = = 4 . 2 5 . 1 
- j s o n s c h e m a - s p e c i f i c a t i o n s = = 2 0 2 5 . 9 . 1 
- k i w i s o l v e r = = 1 . 4 . 9 
- l a n g c h a i n = = 1 . 0 . 8 
- l a n g c h a i n - c o r e = = 1 . 1 . 0 
- l a n g c h a i n - g o o g l e - g e n a i = = 3 . 1 . 0 
- l a n g c h a i n - o l l a m a = = 1 . 0 . 0 
- l a n g c h a i n - o p e n a i = = 1 . 1 . 0 
- l a n g g r a p h = = 1 . 0 . 3 
- l a n g g r a p h - c h e c k p o i n t = = 3 . 0 . 1 
- l a n g g r a p h - p r e b u i l t = = 1 . 0 . 5 
- l a n g g r a p h - s d k = = 0 . 2 . 9 
- l a n g s m i t h = = 0 . 4 . 4 6 
- M a r k u p S a f e = = 3 . 0 . 3 
- m a t p l o t l i b = = 3 . 1 0 . 7 
- n a r w h a l s = = 2 . 1 2 . 0 
- n e t w o r k x = = 3 . 6 
- n u m p y = = 2 . 3 . 5 
- o l l a m a = = 0 . 6 . 1 
- o p e n a i = = 2 . 8 . 1 
- o r j s o n = = 3 . 1 1 . 4 
- o r m s g p a c k = = 1 . 1 2 . 0 
- p a c k a g i n g = = 2 5 . 0 
- p a n d a s = = 2 . 3 . 3 
- p i l l o w = = 1 2 . 0 . 0 
- p r o t o - p l u s = = 1 . 2 6 . 1 
- p r o t o b u f = = 6 . 3 3 . 1 
- p y a r r o w = = 2 1 . 0 . 0 
- p y a s n 1 = = 0 . 6 . 1 
- p y a s n 1 _ m o d u l e s = = 0 . 4 . 2 
- p y c p a r s e r = = 2 . 2 3 
- p y d a n t i c = = 2 . 1 2 . 4 
- p y d a n t i c _ c o r e = = 2 . 4 1 . 5 
- p y d e c k = = 0 . 9 . 1 
- P y J W T = = 2 . 1 0 . 1 
- p y m o n g o = = 4 . 1 5 . 4 
- p y p a r s i n g = = 3 . 2 . 5 
- p y t h o n - d a t e u t i l = = 2 . 9 . 0 . p o s t 0 
- p y t h o n - d o t e n v = = 1 . 2 . 1 
- p y t z = = 2 0 2 5 . 2 
- P y Y A M L = = 6 . 0 . 3 
- r e f e r e n c i n g = = 0 . 3 7 . 0 
- r e g e x = = 2 0 2 5 . 1 1 . 3 
- r e q u e s t s = = 2 . 3 2 . 5 
- r e q u e s t s - t o o l b e l t = = 1 . 0 . 0 
- r p d s - p y = = 0 . 2 9 . 0 
- r s a = = 4 . 9 . 1 
- s e t u p t o o l s = = 7 5 . 9 . 1 
- s i x = = 1 . 1 7 . 0 
- s m m a p = = 5 . 0 . 2 
- s n i f f i o = = 1 . 3 . 1 
- s t r e a m l i t = = 1 . 5 1 . 0 
- s t r e a m l i t - a u t h e n t i c a t o r = = 0 . 4 . 2 
- s t r e a m l i t - m e r m a i d = = 0 . 3 . 0 
- t e n a c i t y = = 9 . 1 . 2 
- t i k t o k e n = = 0 . 1 2 . 0 
- t o m l = = 0 . 1 0 . 2 
- t o o l z = = 1 . 1 . 0 
- t o o n _ f o r m a t   @   g i t + h t t p s : / / g i t h u b . c o m / t o o n - f o r m a t / t o o n - p y t h o n . g i t @ 9 c 4 f 0 c 0 c 2 4 f 2 a 0 b 0 b 3 7 6 3 1 5 f 4 b 8 7 0 7 f 8 c 9 0 0 6 d e 6 
- t o r n a d o = = 6 . 5 . 2 
- t q d m = = 4 . 6 7 . 1 
- t y p i n g - i n s p e c t i o n = = 0 . 4 . 2 
- t y p i n g _ e x t e n s i o n s = = 4 . 1 5 . 0 
- t z d a t a = = 2 0 2 5 . 2 
- u r l l i b 3 = = 2 . 5 . 0 
- w a t c h d o g = = 6 . 0 . 0 
- x x h a s h = = 3 . 6 . 0 
- z s t a n d a r d = = 0 . 2 5 . 0 
pip install -r requirements.txt
### Setup Guide
Information not found
### Quick Startup
Information not found

## 3. Use Cases & Commands
This repository serves as an automated documentation agent, primarily used for quickly understanding the structure and functionality of a given Git repository.

**Key Use Cases:**
*   **Automated Documentation Generation:** Generate comprehensive Markdown documentation for any Python project hosted on GitHub by simply providing its URL.
*   **Architectural Overview:** Gain insights into the repository's file structure, class definitions, function calls, and overall architectural relationships.
*   **Code Comprehension:** Quickly understand the purpose, parameters, and usage context of individual functions and methods without deep code inspection.
*   **LLM Experimentation:** Utilize different LLMs (Gemini, Ollama, OpenAI) for code analysis and documentation generation, allowing for comparative studies of their effectiveness.
*   **Interactive Exploration:** Use the Streamlit frontend to input repositories, view generated documentation, and manage API keys and chat history.

**Primary Commands/Interactions:**
*   **Run the Frontend:** Start the Streamlit application to access the user interface. (e.g., `streamlit run frontend/Frontend.py`)
*   **Input Repository URL:** Provide a GitHub repository URL within the frontend to initiate the analysis and documentation process.
*   **Configure LLM API Keys:** Set up API keys for Gemini, OpenAI, or Ollama models through the frontend's settings.
*   **Generate Documentation:** Trigger the documentation generation workflow via the frontend after providing a repository URL.
*   **View Reports:** Browse the generated Markdown reports and associated metrics directly within the application.

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

## 5. Code Analysis
### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath: str, project_root: str)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles edge cases where the file path is not within the project root by falling back to the basename of the file. If the resulting path ends with '.__init__', it removes the trailing part to correctly represent the module name.
*   **Parameters:**
    *   **filepath** (`str`): The absolute or relative path to a Python file.
    *   **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    *   **module_path** (`str`): A dot-separated module path derived from the given file path.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the __init__ method in AST_Schema.py at line 31.

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It collects information about imports, classes, and functions, organizing them into a structured schema. The visitor maintains context about the current class being processed and builds metadata for each function or method encountered, including their identifiers, source segments, and line numbers. It leverages the standard library's `ast.NodeVisitor` base class to perform depth-first traversal of the AST nodes.
*   **Instantiation:** The ASTVisitor class is instantiated within the analyze_repository function located in AST_Schema.py at line 182.
*   **Dependencies:** This class depends on standard libraries like ast, os, and potentially networkx and callgraph.build_filtered_callgraph as indicated in the imports list.
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It computes the module path based on these inputs and initializes an empty schema dictionary to store collected information about imports, functions, and classes. A private attribute `_current_class` is also initialized to track the currently visited class during traversal.
    *   *Parameters:*
        *   **source_code** (`str`): The full source code string of the file being analyzed.
        *   **file_path** (`str`): The absolute or relative path to the source file.
        *   **project_root** (`str`): The root directory of the project.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `visit_Import(node: ast.Import)`
        *   *Description:* Handles the processing of import statements in the AST. For each imported alias, it appends the import name to the schema's imports list. After collecting the imports, it continues visiting child nodes using generic_visit.
        *   *Parameters:*
            *   **node** (`ast.Import`): An AST node representing an import statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the AST traversal mechanism when an import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `visit_ImportFrom(node: ast.ImportFrom)`
        *   *Description:* Processes import-from statements in the AST. For each imported alias, it constructs a qualified name combining the module and alias, then appends it to the schema's imports list. It subsequently continues traversal using generic_visit.
        *   *Parameters:*
            *   **node** (`ast.ImportFrom`): An AST node representing an import-from statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the AST traversal mechanism when an import-from node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `visit_ClassDef(node: ast.ClassDef)`
        *   *Description:* Handles class definitions in the AST. It generates a unique identifier for the class using the module path and class name. It creates a detailed class info dictionary containing metadata such as docstring, source segment, and line numbers. This dictionary is appended to the schema's classes list. It tracks the current class being processed and ensures proper cleanup after traversal.
        *   *Parameters:*
            *   **node** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the AST traversal mechanism when a class definition node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `visit_FunctionDef(node: ast.FunctionDef)`
        *   *Description:* Processes function definitions in the AST. If a class is currently being visited, it adds method metadata to the current class's context. Otherwise, it adds standalone function metadata to the schema's functions list. In both cases, it extracts arguments, docstrings, and source segments, and stores them along with line number information. Finally, it continues traversal using generic_visit.
        *   *Parameters:*
            *   **node** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the AST traversal mechanism when a function definition node is encountered.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `visit_AsyncFunctionDef(node: ast.AsyncFunctionDef)`
        *   *Description:* Handles asynchronous function definitions in the AST. It delegates the processing to the regular visit_FunctionDef method, allowing shared logic for handling function metadata regardless of whether it's synchronous or asynchronous.
        *   *Parameters:*
            *   **node** (`ast.AsyncFunctionDef`): An AST node representing an async function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls visit_FunctionDef to handle the common logic for function definitions.
            *   **Called By:** This method is called by the AST traversal mechanism when an async function definition node is encountered.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information. It merges relationship data into the schema and supports the construction of a comprehensive view of the codebase including functions, classes, and their interdependencies. The class primarily operates on a collection of file objects and a GitRepository to extract and process AST nodes.
*   **Instantiation:** This class is instantiated by the evaluation function in HelperLLM_evaluation.py at line 128 and by the main_workflow function in main.py at line 187.
*   **Dependencies:** This class depends on the ast, networkx, os modules, and the build_filtered_callgraph function from callgraph and GitRepository from getRepo.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any operations and simply passes.
    *   *Parameters:*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `_enrich_schema_with_callgraph(schema: dict, call_graph: nx.DiGraph, filename: str)`
        *   *Description:* This static method enriches a given schema with call graph information by updating function and method contexts with details about which functions they call and which functions call them. It iterates through functions and class methods in the schema and updates their context fields based on the provided call graph.
        *   *Parameters:*
            *   **schema** (`dict`): A dictionary representing the schema to be enriched with call graph data.
            *   **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions.
            *   **filename** (`str`): The filename associated with the schema being processed.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is not directly called by any other method in the provided context.
    *   **`merge_relationship_data`**
        *   *Signature:* `merge_relationship_data(self, full_schema: dict, relationship_data: list)`
        *   *Description:* This method merges relationship data into a full schema by mapping identifiers from the relationship data to corresponding entries in the schema. It updates function and class contexts with 'called_by' information and class contexts with 'instantiated_by' information based on the provided relationship data.
        *   *Parameters:*
            *   **full_schema** (`dict`): The complete schema into which relationship data will be merged.
            *   **relationship_data** (`list`): A list of dictionaries containing relationship information with identifiers and called_by lists.
        *   *Returns:*
            *   **full_schema** (`dict`): The updated schema with merged relationship data.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the evaluation function in HelperLLM_evaluation.py at line 137 and by the main_workflow function in main.py at line 197.
    *   **`analyze_repository`**
        *   *Signature:* `analyze_repository(self, files: list, repo: GitRepository)`
        *   *Description:* This method analyzes a repository by processing a list of file objects and building a schema representation of the code. It parses each Python file's content into an AST, uses an ASTVisitor to extract schema nodes, enriches these nodes with call graph data, and aggregates the results into a full schema structure.
        *   *Parameters:*
            *   **files** (`list`): A list of file objects to be analyzed.
            *   **repo** (`GitRepository`): The GitRepository object representing the repository to be analyzed.
        *   *Returns:*
            *   **full_schema** (`dict`): A dictionary containing the aggregated schema of all processed files.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called by the evaluation function in HelperLLM_evaluation.py at line 129 and by the main_workflow function in main.py at line 188.

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes an AST representation of a file and uses a custom visitor to extract import dependencies. The resulting graph maps each file to its imported files, forming a dependency structure suitable for analysis or visualization.
*   **Parameters:**
    *   **filename** (`str`): The name of the file being analyzed for dependencies.
    *   **tree** (`AST`): The abstract syntax tree of the file, used to traverse and identify import statements.
    *   **repo_root** (`str`): The root directory of the repository, used to resolve relative paths for imports.
*   **Returns:**
    *   **graph** (`nx.DiGraph`): A directed graph where nodes represent files and edges represent import relationships.
*   **Usage:**
    *   **Calls:** The function internally utilizes a FileDependencyGraph visitor to process the AST and extract import dependencies.
    *   **Called By:** This function is called by the 'build_repository_graph' function in the 'File_Dependency.py' file.

#### Function: `build_repository_graph`
*   **Signature:** `def build_repository_graph(repository: GitRepository)`
*   **Description:** This function constructs a dependency graph for all Python files within a given Git repository. It iterates through each Python file, parses its content into an abstract syntax tree (AST), and builds a file-level dependency graph. These individual graphs are then merged into a single global directed graph that represents dependencies across the entire repository. The resulting graph captures relationships between modules based on their import statements.
*   **Parameters:**
    *   **repository** (`GitRepository`): The GitRepository object representing the repository whose files' dependencies are to be analyzed.
*   **Returns:**
    *   **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the combined dependency graph of all Python files in the repository.
*   **Usage:**
    *   **Calls:** This function internally uses several AST parsing and graph-building utilities including parse(), build_file_dependency_graph(), and various NetworkX functions.
    *   **Called By:** This function is called by the backend.File_Dependency module at line 200.

#### Function: `get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory: str)`
*   **Description:** This function retrieves all Python files (.py) from a specified directory and its subdirectories, returning them as relative paths from the given directory. It resolves the input directory to an absolute path before performing the search. The function uses the `pathlib` module for path manipulation and recursive globbing.
*   **Parameters:**
    *   **directory** (`str`): The path to the directory from which to find all .py files.
*   **Returns:**
    *   **all_files** (`list[pathlib.Path]`): A list of Path objects representing the relative paths of all .py files found in the directory and its subdirectories.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the _resolve_module_name method in File_Dependency.py at line 43.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze and resolve file-level import dependencies within a Python project. It extends NodeVisitor to traverse AST nodes representing imports and builds a mapping of file dependencies. The class handles both absolute and relative imports, resolving relative paths by examining the repository structure and checking for module existence or symbol exports in __init__.py files.
*   **Instantiation:** This class is instantiated by the function 'build_file_dependency_graph' located in 'File_Dependency.py' at line 156.
*   **Dependencies:** This class does not explicitly depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up the instance variables to track the current file being analyzed and the root directory of the repository.
    *   *Parameters:*
        *   **filename** (`str`): The name of the file being analyzed for dependencies.
        *   **repo_root** (`Any`): The root directory path of the repository containing the file.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `_resolve_module_name(self, node: ImportFrom)`
        *   *Description:* Resolves relative import statements by analyzing the import node and determining the actual module or symbol names. It checks for matching files or symbols in the repository structure, handling cases where imports use relative paths like '..'. The method raises ImportError if no valid resolution can be found.
        *   *Parameters:*
            *   **node** (`ImportFrom`): The AST node representing the import statement to resolve.
        *   *Returns:*
            *   **resolved_names** (`list[str]`): A list of resolved module or symbol names.
        *   **Usage:**
            *   **Calls:** This method internally calls helper functions 'module_file_exists' and 'init_exports_symbol' to check for file existence and symbol exports respectively.
            *   **Called By:** This method is called by 'visit_ImportFrom' when resolving relative imports.
    *   **`visit_Import`**
        *   *Signature:* `visit_Import(self, node: Import | ImportFrom, base_name: str | None)`
        *   *Description:* Handles import statements by adding the imported module names to the dependency mapping for the current file. It ensures that the import dependencies dictionary is initialized for the current file before adding entries.
        *   *Parameters:*
            *   **node** (`Import | ImportFrom`): The AST node representing the import statement.
            *   **base_name** (`str | None`): Optional base name for the import, used in certain cases like from ... import statements.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls 'generic_visit' to continue traversal of the AST.
            *   **Called By:** This method is called by 'visit_ImportFrom' and directly during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `visit_ImportFrom(self, node: ImportFrom)`
        *   *Description:* Processes 'from ... import ...' style import statements. It extracts the module name and either adds it directly or resolves relative imports using '_resolve_module_name'. If resolution fails, it prints an error message but continues processing.
        *   *Parameters:*
            *   **node** (`ImportFrom`): The AST node representing the from-import statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls 'visit_Import' and '_resolve_module_name' to handle different aspects of import processing.
            *   **Called By:** This method is called during AST traversal when encountering 'from ... import ...' statements.

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** This function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analysis for three example functions ('add_item', 'check_stock', and 'generate_report') and simulates the documentation generation process for these functions using an LLMHelper instance. It also includes a mock class definition for 'InventoryManager' and demonstrates how the LLMHelper would process both individual function inputs and class definitions.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it uses the LLMHelper class to process inputs.
    *   **Called By:** Called by backend.HelperLLM (line 419 in HelperLLM.py)

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a centralized interface for interacting with various language models, including Google Gemini, OpenAI, and custom APIs, to generate validated documentation for functions and classes. It handles API configuration, prompt loading, batching logic, and error management while supporting different model types through conditional instantiation. The class provides two main methods: one for generating documentation for functions and another for classes, both utilizing structured output from the underlying LLMs.
*   **Instantiation:** The LLMHelper class is instantiated by the main_orchestrator function in HelperLLM.py, the evaluation function in HelperLLM_evaluation.py, and the main_workflow function in main.py.
*   **Dependencies:** No external dependencies are explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API credentials, prompt files, and model configuration. It loads system prompts from specified files, configures batch settings based on the model name, and sets up appropriate LLM clients depending on the model type. It also prepares structured output configurations for function and class analysis.
    *   *Parameters:*
        *   **api_key** (`str`): API key for accessing the language model service.
        *   **function_prompt_path** (`str`): File path to the system prompt used for function documentation generation.
        *   **class_prompt_path** (`str`): File path to the system prompt used for class documentation generation.
        *   **model_name** (`str`): Name of the language model to use. Defaults to 'gemini-2.0-flash-lite'.
        *   **base_url** (`str`): Base URL for custom API endpoints. Optional.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `_configure_batch_settings(self, model_name: str)`
        *   *Description:* Configures the batch size for processing requests based on the specified model name. It assigns predefined batch sizes for known models and falls back to a default value for unknown models. This method ensures efficient resource utilization by adjusting batch sizes according to model capabilities and limitations.
        *   *Parameters:*
            *   **model_name** (`str`): Name of the language model being used.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** This method is called during initialization of the LLMHelper class.
    *   **`generate_for_functions`**
        *   *Signature:* `generate_for_functions(self, function_inputs: List[FunctionAnalysisInput])`
        *   *Description:* Generates and validates documentation for a batch of functions using the configured LLM. It processes inputs in batches, converts them into JSON payloads, and sends them to the LLM for structured output. The method includes error handling to maintain order in results even when individual requests fail, and respects rate limits by waiting between batches.
        *   *Parameters:*
            *   **function_inputs** (`List[FunctionAnalysisInput]`): A list of function input models to document.
        *   *Returns:*
            *   **result** (`List[Optional[FunctionAnalysis]]`): A list of validated function analysis outputs or None for failed items.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** Called by evaluation in HelperLLM_evaluation.py and main_workflow in main.py.
    *   **`generate_for_classes`**
        *   *Signature:* `generate_for_classes(self, class_inputs: List[ClassAnalysisInput])`
        *   *Description:* Generates and validates documentation for a batch of classes using the configured LLM. Similar to the function generation method, it processes inputs in batches, converts them into JSON payloads, and sends them to the LLM for structured output. It also includes error handling and respects rate limits by waiting between batches.
        *   *Parameters:*
            *   **class_inputs** (`List[ClassAnalysisInput]`): A list of class input models to document.
        *   *Returns:*
            *   **result** (`List[Optional[ClassAnalysis]]`): A list of validated class analysis outputs or None for failed items.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions directly.
            *   **Called By:** Called by evaluation in HelperLLM_evaluation.py and main_workflow in main.py.

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** The MainLLM class serves as the central interface for interacting with various language learning models (LLMs). It supports multiple LLM providers including Google Generative AI, OpenAI-compatible APIs, and Ollama-based models. The class initializes with configuration parameters such as API keys, prompt file paths, and model specifications, and provides two core functionalities: synchronous LLM invocation and streaming responses. It handles different model types by dynamically selecting appropriate LLM clients based on the model name and environment settings.
*   **Instantiation:** The class is instantiated by the main_workflow function in main.py at line 398.
*   **Dependencies:** No external dependencies identified.
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading the system prompt from a specified file, and setting up the appropriate LLM client based on the model name. It supports multiple LLM backends including Google Generative AI, custom OpenAI-compatible APIs, and Ollama models.
    *   *Parameters:*
        *   **api_key** (`str`): The API key required for authenticating with the LLM provider.
        *   **prompt_file_path** (`str`): The file path to the system prompt that will be used for LLM interactions.
        *   **model_name** (`str`): The name of the model to use, which determines the backend LLM client to instantiate.
        *   **base_url** (`str`): Optional base URL for connecting to a custom LLM endpoint.
*   **Methods:**
    *   **`call_llm`**
        *   *Signature:* `call_llm(self, user_input: str)`
        *   *Description:* Executes a synchronous call to the configured LLM with the provided user input. It constructs a message sequence including the system prompt and user input, sends it to the LLM, and returns the content of the response. If an error occurs during the call, it logs the error and returns None.
        *   *Parameters:*
            *   **user_input** (`str`): The input text provided by the user to be processed by the LLM.
        *   *Returns:*
            *   **response_content** (`str`): The content of the LLM's response, or None if an error occurred.
        *   **Usage:**
            *   **Calls:** No internal method calls detected.
            *   **Called By:** Called by main_workflow function in main.py at line 417.
    *   **`stream_llm`**
        *   *Signature:* `stream_llm(self, user_input: str)`
        *   *Description:* Initiates a streaming call to the configured LLM with the provided user input. It yields content chunks from the LLM response one at a time, allowing for real-time processing of the output. If an error occurs during the streaming process, it logs the error and yields an error message.
        *   *Parameters:*
            *   **user_input** (`str`): The input text provided by the user to be processed by the LLM.
        *   *Returns:*
            *   **chunk_content** (`str`): Content chunks yielded from the LLM response, or an error message if an exception occurred.
        *   **Usage:**
            *   **Calls:** No internal method calls detected.
            *   **Called By:** No external callers detected.

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** The ProjektInfoExtractor class is designed to extract basic project information from common project files such as README.md, pyproject.toml, and requirements.txt. It initializes with a predefined structure for storing extracted data and provides methods to parse different file types. The class prioritizes information extraction from pyproject.toml, followed by requirements.txt, and finally README files, ensuring metadata is collected systematically. It also handles formatting of dependency lists and sets a default project title based on the repository URL.
*   **Instantiation:** This class is instantiated in HelperLLM_evaluation.py at line 104 and in main.py at line 160.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported.
*   **Constructor:**
    *   *Description:* Initializes the ProjektInfoExtractor with a predefined dictionary structure to hold project information. It sets up placeholders for various project details including overview and installation sections, and defines a constant for indicating missing information.
    *   *Parameters:*
*   **Methods:**
    *   **`_finde_datei`**
        *   *Signature:* `_finde_datei(self, patterns: List[str], dateien: List[Any])`
        *   *Description:* This private method searches for a file among a list of files that matches any of the given patterns, ignoring case. It iterates through the list of files and checks if the file path ends with one of the specified patterns. If a match is found, it returns the matching file object; otherwise, it returns None.
        *   *Parameters:*
            *   **patterns** (`List[str]`): A list of file extension patterns to search for.
            *   **dateien** (`List[Any]`): A list of file objects to search through.
        *   *Returns:*
            *   **result** (`Optional[Any]`): The matched file object or None if no match is found.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other methods in the provided context.
    *   **`_extrahiere_sektion_aus_markdown`**
        *   *Signature:* `_extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])`
        *   *Description:* This private method extracts text content from a markdown document under a specific section header identified by keywords. It uses regular expressions to find the section header and captures all content until the next header or end of the document. It supports multiple alternative keywords for identifying the section.
        *   *Parameters:*
            *   **inhalt** (`str`): The full markdown text to process.
            *   **keywords** (`List[str]`): A list of alternative keywords to identify the target section.
        *   *Returns:*
            *   **extracted_text** (`Optional[str]`): The extracted text from the section or None if no match is found.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other methods in the provided context.
    *   **`_parse_readme`**
        *   *Signature:* `_parse_readme(self, inhalt: str)`
        *   *Description:* This private method parses the content of a README file to extract various project details such as title, description, key features, tech stack, current status, setup instructions, and quick start guide. It uses regex patterns to locate these elements and updates the internal info dictionary accordingly, prioritizing existing values over new ones.
        *   *Parameters:*
            *   **inhalt** (`str`): The content of the README file to parse.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other methods in the provided context.
    *   **`_parse_toml`**
        *   *Signature:* `_parse_toml(self, inhalt: str)`
        *   *Description:* This private method parses the content of a pyproject.toml file to extract project metadata such as name, description, and dependencies. It uses the tomllib library to load the TOML content and updates the internal info dictionary with the parsed data. If tomllib is not available, it prints a warning message.
        *   *Parameters:*
            *   **inhalt** (`str`): The content of the pyproject.toml file to parse.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other methods in the provided context.
    *   **`_parse_requirements`**
        *   *Signature:* `_parse_requirements(self, inhalt: str)`
        *   *Description:* This private method parses the content of a requirements.txt file to extract dependency information. It filters out comments and empty lines to build a list of dependencies. If no dependencies have been previously set in the info dictionary, it populates the dependencies field with the parsed list.
        *   *Parameters:*
            *   **inhalt** (`str`): The content of the requirements.txt file to parse.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other methods in the provided context.
    *   **`extrahiere_info`**
        *   *Signature:* `extrahiere_info(self, dateien: List[Any], repo_url: str)`
        *   *Description:* This public method orchestrates the extraction of project information from a list of repository files. It identifies relevant files (README, pyproject.toml, requirements.txt) using the _finde_datei helper method. It processes the files in priority order: pyproject.toml, requirements.txt, and README. Finally, it formats the dependencies list and sets the project title based on the repository URL.
        *   *Parameters:*
            *   **dateien** (`List[Any]`): A list of repository file objects to extract information from.
            *   **repo_url** (`str`): The URL of the repository used to derive the project title.
        *   *Returns:*
            *   **info** (`Dict[str, Any]`): A dictionary containing the extracted project information.
        *   **Usage:**
            *   **Calls:** This method calls the following helper methods: _finde_datei, _parse_toml, _parse_requirements, and _parse_readme.
            *   **Called By:** This method is called by the evaluation function in HelperLLM_evaluation.py and the main_workflow function in main.py.

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
*   **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
*   **Description:** The function 'make_safe_dot' takes a NetworkX directed graph and a file path as inputs. It creates a copy of the graph and generates a safe node naming scheme by replacing original node names with 'n0', 'n1', etc. It then relabels the nodes in the copied graph according to this mapping and assigns the original node names as labels to the new nodes. Finally, it writes the modified graph to a DOT file at the specified output path.
*   **Parameters:**
    *   **graph** (`nx.DiGraph`): A NetworkX directed graph object to be processed and saved as a DOT file.
    *   **out_path** (`str`): The file path where the DOT representation of the graph will be written.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it uses NetworkX functions like 'copy', 'relabel_nodes', and 'write_dot'.
    *   **Called By:** This function is called by 'backend.callgraph' in the file 'callgraph.py' at line 244.

#### Function: `build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo: GitRepository)`
*   **Description:** Die Funktion erstellt einen globalen Call-Graphen basierend auf allen Python-Dateien eines Git-Repositories und filtert diesen anschließend auf Funktionen, die vom Benutzer selbst geschrieben wurden. Sie durchläuft alle Dateien, parst deren Inhalt mit dem Abstract Syntax Tree (AST), extrahiert Funktionsaufrufe und baut einen gerichteten Graphen auf, wobei nur Kanten zwischen eigenen Funktionen erhalten bleiben.
*   **Parameters:**
    *   **repo** (`GitRepository`): Ein Objekt, das Informationen über ein Git-Repository enthält, insbesondere Zugriff auf alle darin enthaltenen Dateien.
*   **Returns:**
    *   **global_graph** (`nx.DiGraph`): Ein gerichteter Graph (DiGraph) von NetworkX, der die Aufrufbeziehungen zwischen Funktionen des Repositories darstellt, gefiltert auf selbst geschriebene Funktionen.
*   **Usage:**
    *   **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes direkt auf.
    *   **Called By:** Diese Funktion wird von 'analyze_repository' in der Datei 'AST_Schema.py' auf Zeile 167 und von 'backend.callgraph' in der Datei 'callgraph.py' auf Zeile 243 aufgerufen.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is designed to construct a call graph representation of Python code by traversing the Abstract Syntax Tree (AST). It tracks function and class definitions, resolves function calls, and maintains a directed graph of these relationships. The class uses AST visitor methods to process imports, class definitions, function definitions, and function calls, mapping local and imported names to fully qualified identifiers. It supports both synchronous and asynchronous function definitions and handles conditional blocks related to main execution scope.
*   **Instantiation:** This class is instantiated by the build_filtered_callgraph function in callgraph.py at lines 199 and 206.
*   **Dependencies:** This class does not depend on any external libraries beyond standard Python modules and networkx.
*   **Constructor:**
    *   *Description:* Initializes the CallGraph with a filename and sets up internal tracking structures including local definitions, a graph representation, import mappings, and function sets. It also initializes tracking variables for current function and class scopes.
    *   *Parameters:*
        *   **filename** (`str`): The name of the file being processed for call graph construction.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `_recursive_call(self, node)`
        *   *Description:* Recursively extracts the dotted name components from an AST node representing a function call or attribute access. It traverses the AST to build a list of name components, which can represent a fully qualified name such as 'package.module.Class.method'.
        *   *Parameters:*
            *   **node** (`ast.AST`): An AST node representing a function call or attribute access.
        *   *Returns:*
            *   **parts** (`list[str]`): A list of string components forming a dotted name.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the _resolve_all_callee_names method.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `_resolve_all_callee_names(self, callee_nodes: list[list[str]])`
        *   *Description:* Resolves a list of dotted name components into fully qualified names by checking local definitions, import mappings, and constructing appropriate names based on the current class context. It prioritizes local definitions over imports and constructs names with appropriate namespace prefixes.
        *   *Parameters:*
            *   **callee_nodes** (`list[list[str]]`): A list of lists representing dotted name components for potential callees.
        *   *Returns:*
            *   **resolved** (`list[str]`): A list of resolved fully qualified names.
        *   **Usage:**
            *   **Calls:** This method calls the _recursive_call method to extract name components.
            *   **Called By:** This method is called by the visit_Call method.
    *   **`_make_full_name`**
        *   *Signature:* `_make_full_name(self, basename: str, class_name: str | None)`
        *   *Description:* Constructs a fully qualified name for a function or method by combining the filename, optional class name, and base name. This helps in uniquely identifying functions within the context of a file and potentially within a class.
        *   *Parameters:*
            *   **basename** (`str`): The base name of the function or method.
            *   **class_name** (`Optional[str]`): The name of the class if the function belongs to one.
        *   *Returns:*
            *   **full_name** (`str`): A fully qualified name constructed from the filename, class name (if provided), and base name.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the visit_FunctionDef method.
    *   **`_current_caller`**
        *   *Signature:* `_current_caller(self)`
        *   *Description:* Determines the current caller's name based on whether a function is currently being visited. If a function is active, it returns the function name; otherwise, it returns a generic identifier for global scope.
        *   *Parameters:*
        *   *Returns:*
            *   **caller** (`str`): The name of the current caller or a placeholder for global scope.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods.
            *   **Called By:** This method is called by the visit_Call method.
    *   **`visit_Import`**
        *   *Signature:* `visit_Import(self, node)`
        *   *Description:* Processes import statements in the AST by mapping aliases to their actual module names. This allows for proper resolution of imported names when building the call graph.
        *   *Parameters:*
            *   **node** (`ast.Import`): An AST node representing an import statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversal.
            *   **Called By:** This method is called during AST traversal.
    *   **`visit_ImportFrom`**
        *   *Signature:* `visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements by mapping imported names to their originating modules. It processes aliases and constructs appropriate module paths for later resolution.
        *   *Parameters:*
            *   **node** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversal.
            *   **Called By:** This method is called during AST traversal.
    *   **`visit_ClassDef`**
        *   *Signature:* `visit_ClassDef(self, node: ast.ClassDef)`
        *   *Description:* Visits class definitions in the AST, temporarily setting the current class name to track nested function definitions within the class. After processing the class body, it restores the previous class name.
        *   *Parameters:*
            *   **node** (`ast.ClassDef`): An AST node representing a class definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversal.
            *   **Called By:** This method is called during AST traversal.
    *   **`visit_FunctionDef`**
        *   *Signature:* `visit_FunctionDef(self, node)`
        *   *Description:* Processes function definitions by creating a fully qualified name for the function, updating local definitions, and adding the function to the call graph. It also manages the current function context during traversal.
        *   *Parameters:*
            *   **node** (`ast.FunctionDef`): An AST node representing a function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the _make_full_name and generic_visit methods.
            *   **Called By:** This method is called during AST traversal.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating to the visit_FunctionDef method, ensuring that async functions are treated similarly to regular functions in terms of call graph construction.
        *   *Parameters:*
            *   **node** (`ast.AsyncFunctionDef`): An AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the visit_FunctionDef method.
            *   **Called By:** This method is called during AST traversal.
    *   **`visit_Call`**
        *   *Signature:* `visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST by determining the caller, resolving the callee names, and recording edges in the call graph. It updates the internal edges dictionary to reflect the call relationships.
        *   *Parameters:*
            *   **node** (`ast.Call`): An AST node representing a function call.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the _current_caller, _recursive_call, and _resolve_all_callee_names methods.
            *   **Called By:** This method is called during AST traversal.
    *   **`visit_If`**
        *   *Signature:* `visit_If(self, node)`
        *   *Description:* Handles conditional statements that check for '__name__ == \"__main__\"'. In such cases, it temporarily changes the current function context to '<main_block>' before visiting the conditional body, allowing for special handling of main execution blocks.
        *   *Parameters:*
            *   **node** (`ast.If`): An AST node representing an if statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the generic_visit method to continue traversal.
            *   **Called By:** This method is called during AST traversal.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It implements lazy loading for file metadata such as the blob object, content, and size to optimize performance by only loading data when explicitly accessed. The class provides properties to access these lazily-loaded attributes and includes utility methods like word count analysis and conversion to dictionary format.
*   **Instantiation:** This class is instantiated by the get_all_files method in the getRepo.py file.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object with a file path and a commit tree. Sets up internal attributes for lazy loading including blob, content, and size.
    *   *Parameters:*
        *   **file_path** (`str`): The path to the file within the repository.
        *   **commit_tree** (`git.Tree`): The tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `blob(self)`
        *   *Description:* A property that lazily loads and returns the Git blob object associated with the file. If the blob hasn't been loaded yet, it attempts to retrieve it from the commit tree using the stored file path. Raises a FileNotFoundError if the file is not found in the tree.
        *   *Parameters:*
        *   *Returns:*
            *   **blob** (`git.Blob`): The Git blob object representing the file.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other functions according to the provided context.
    *   **`content`**
        *   *Signature:* `content(self)`
        *   *Description:* A property that lazily loads and returns the decoded UTF-8 content of the file. If the content hasn't been loaded yet, it reads the data stream from the blob and decodes it, ignoring encoding errors. Returns the decoded string content.
        *   *Parameters:*
        *   *Returns:*
            *   **content** (`str`): The decoded content of the file.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other functions according to the provided context.
    *   **`size`**
        *   *Signature:* `size(self)`
        *   *Description:* A property that lazily loads and returns the size of the file in bytes. If the size hasn't been determined yet, it retrieves the size directly from the blob object. Returns the integer size value.
        *   *Parameters:*
        *   *Returns:*
            *   **size** (`int`): The size of the file in bytes.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other functions according to the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `analyze_word_count(self)`
        *   *Description:* An example analysis method that counts the number of words in the file's content by splitting the content on whitespace and returning the length of the resulting list. This method relies on the content property to ensure the file content is loaded before counting.
        *   *Parameters:*
        *   *Returns:*
            *   **word_count** (`int`): The total number of words in the file content.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other functions according to the provided context.
    *   **`__repr__`**
        *   *Signature:* `__repr__(self)`
        *   *Description:* Returns a string representation of the RepoFile object, useful for debugging and logging purposes. Displays the file path in a formatted string.
        *   *Parameters:*
        *   *Returns:*
            *   **repr_string** (`str`): A string representation of the RepoFile object showing the file path.
        *   **Usage:**
            *   **Calls:** This method does not call any other functions.
            *   **Called By:** This method is not called by any other functions according to the provided context.
    *   **`to_dict`**
        *   *Signature:* `to_dict(self, include_content: bool)`
        *   *Description:* Converts the RepoFile object into a dictionary format, including basic file information such as path, name, size, and type. Optionally includes the full content if specified. Uses the os.path.basename function to extract the filename from the path.
        *   *Parameters:*
            *   **include_content** (`bool`): Flag indicating whether to include the file content in the returned dictionary.
        *   *Returns:*
            *   **data** (`dict`): A dictionary containing file metadata and optionally the content.
        *   **Usage:**
            *   **Calls:** This method calls os.path.basename to extract the filename from the path.
            *   **Called By:** This method is not called by any other functions according to the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory and providing functionality to retrieve file information and construct a hierarchical file tree. It supports initialization with a repository URL, fetching all files as RepoFile objects, closing the repository by cleaning up the temporary directory, and constructing a structured file tree representation. The class implements context manager protocols (__enter__ and __exit__) to facilitate automatic resource cleanup.
*   **Instantiation:** The GitRepository class is instantiated in the evaluation function in HelperLLM_evaluation.py at line 86 and in the main_workflow function in main.py at line 141.
*   **Dependencies:** This class depends on the git module (specifically git.Repo and git.GitCommandError), tempfile, shutil, logging, and os modules.
*   **Constructor:**
    *   *Description:* Initializes a GitRepository instance by cloning the specified repository URL into a temporary directory. It sets up necessary attributes such as the repository URL, temporary directory path, and references to the cloned repository and its latest commit. If cloning fails, it raises a RuntimeError after cleaning up resources.
    *   *Parameters:*
        *   **repo_url** (`str`): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `get_all_files(self)`
        *   *Description:* Retrieves a list of all files in the repository and converts them into RepoFile objects. It uses Git's ls-files command to obtain file paths and constructs RepoFile instances for each path, storing them in the instance's files attribute.
        *   *Parameters:*
        *   *Returns:*
            *   **files** (`list[RepoFile]`): A list of RepoFile instances representing all files in the repository.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods internally.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`close`**
        *   *Signature:* `close(self)`
        *   *Description:* Deletes the temporary directory used for the repository clone, effectively cleaning up resources associated with the GitRepository instance.
        *   *Parameters:*
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other methods internally.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`__enter__`**
        *   *Signature:* `__enter__(self)`
        *   *Description:* Enables the use of the GitRepository instance in a context manager (with statement). It simply returns the instance itself.
        *   *Parameters:*
        *   *Returns:*
            *   **""** (`GitRepository`): The GitRepository instance.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods internally.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`__exit__`**
        *   *Signature:* `__exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* Implements the context manager's exit protocol. It ensures that the close() method is called when exiting the context, thereby cleaning up the temporary directory.
        *   *Parameters:*
            *   **exc_type** (`Any`): Exception type, if an exception occurred in the with block.
            *   **exc_val** (`Any`): Exception value, if an exception occurred in the with block.
            *   **exc_tb** (`Any`): Exception traceback, if an exception occurred in the with block.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the close() method internally.
            *   **Called By:** This method is not called by any other methods according to the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `get_file_tree(self, include_content: bool)`
        *   *Description:* Constructs a hierarchical file tree representation of the repository. If no files have been retrieved yet, it fetches them first. Then, it iterates through the files and builds a nested dictionary structure reflecting the directory hierarchy.
        *   *Parameters:*
            *   **include_content** (`bool`): Flag indicating whether to include file content in the returned dictionary.
        *   *Returns:*
            *   **tree** (`dict`): A dictionary representing the hierarchical file tree structure.
        *   **Usage:**
            *   **Calls:** This method calls the get_all_files() method internally if no files are already loaded.
            *   **Called By:** This method is not called by any other methods according to the provided context.

### File: `backend/main.py`

#### Function: `create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
*   **Description:** Die Funktion erstellt ein Balkendiagramm zur Visualisierung des Token-Vergleichs zwischen JSON und TOON-Formaten und speichert das Diagramm in einer Datei. Sie verwendet matplotlib zur Erstellung des Diagramms und zeigt die Anzahl der Tokens für beide Formate sowie den prozentualen Einsparungswert an. Die Funktion nimmt die Token-Anzahlen, den Einsparungsprozentsatz und den Ausgabepfad als Parameter entgegen.
*   **Parameters:**
    *   **json_tokens** (`int`): Die Anzahl der Tokens im JSON-Format.
    *   **toon_tokens** (`int`): Die Anzahl der Tokens im TOON-Format.
    *   **savings_percent** (`float`): Der prozentuale Einsparungswert zwischen den beiden Format-Token-Anzahlen.
    *   **output_path** (`str`): Der Dateipfad, unter dem das generierte Diagramm gespeichert wird.
*   **Returns:**
*   **Usage:**
    *   **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.
    *   **Called By:** Die Funktion wird von der Funktion 'main_workflow' in der Datei 'main.py' aufgerufen.

#### Function: `calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items: int, batch_size: int, model_name: str)`
*   **Description:** The function calculates the net time duration by subtracting sleep times related to rate limits from the total time elapsed between a start and end timestamp. It specifically handles cases where the model name starts with 'gemini-' and adjusts the calculation based on the number of batches and item count. If the model is not a gemini model, it returns the total duration directly. If there are no items, it returns zero. Otherwise, it computes the net time after accounting for sleep periods.
*   **Parameters:**
    *   **start_time** (`float or datetime`): The starting timestamp of the operation.
    *   **end_time** (`float or datetime`): The ending timestamp of the operation.
    *   **total_items** (`int`): The total number of items processed during the operation.
    *   **batch_size** (`int`): The size of each batch used for processing items.
    *   **model_name** (`str`): The name of the model being used, which determines whether rate limit adjustments apply.
*   **Returns:**
    *   **net_time** (`float or int`): The calculated net time after subtracting sleep durations from the total duration.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the evaluation function in HelperLLM_evaluation.py at lines 249 and 275, and by the main_workflow function in main.py at lines 311 and 342.

#### Function: `main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive code analysis pipeline for a given repository URL. It begins by extracting API keys and model names, then clones the repository and retrieves all files. It proceeds to extract basic project information, construct a file tree, perform relationship analysis, and build an abstract syntax tree (AST). The function prepares inputs for a helper LLM to analyze functions and classes, then calls the helper LLM to generate documentation. Afterward, it prepares inputs for a main LLM to produce a final report. Finally, it saves the report and generates statistics on token usage.
*   **Parameters:**
    *   **input** (`Any`): The input data, typically a URL pointing to a repository.
    *   **api_keys** (`dict`): A dictionary containing API keys for various services such as Gemini, OpenAI, and SCADsLLM.
    *   **model_names** (`dict`): A dictionary specifying the names of models to be used for helper and main LLMs.
    *   **status_callback** (`Callable[[str], None] | None`): An optional callback function to report status updates during execution.
*   **Returns:**
    *   **report** (`str`): The final markdown report generated by the main LLM.
    *   **metrics** (`dict`): A dictionary containing timing metrics for helper and main LLM operations.
*   **Usage:**
    *   **Calls:** This function internally calls several components including GitRepository for cloning repositories, ProjektInfoExtractor for extracting project information, ProjectAnalyzer for analyzing relationships, ASTAnalyzer for building AST schemas, LLMHelper for function and class analysis, and MainLLM for generating the final report.
    *   **Called By:** This function is called by the frontend module in 'Frontend.py' at line 489 and by the backend main module in 'main.py' at line 533.

#### Function: `update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The function 'update_status' is designed to handle status updates by invoking an optional callback function if one is defined, followed by logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages throughout the application.
*   **Parameters:**
    *   **msg** (`Any`): A message to be passed to the status callback and logged.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function internally calls the 'status_callback' function if it is defined, and also logs the message using 'logging.info'.
    *   **Called By:** This function is called by 'main_workflow' in 'main.py' at multiple locations across different lines.

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles cases where the filepath is not within the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure.
*   **Parameters:**
    *   **filepath** (`str`): The absolute or relative path to a Python file.
    *   **project_root** (`str`): The root directory of the project used to compute the relative path.
*   **Returns:**
    *   **module_path** (`str`): A dot-separated module path derived from the given file path.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by _collect_definitions and __init__ methods in relationship_analyzer.py.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is designed to analyze Python projects by examining their source code structure and identifying relationships between functions, classes, and methods. It walks through the project directory to find Python files, parses them into Abstract Syntax Trees (ASTs), collects definitions such as functions and classes along with their locations, and resolves call relationships between these definitions. The analyzer maintains internal state including definitions, call graphs, and ASTs for processing. After analysis, it formats and returns results showing which elements are called by others.
*   **Instantiation:** This class is instantiated by the functions `evaluation` in `HelperLLM_evaluation.py` at line 119 and `main_workflow` in `main.py` at line 177.
*   **Dependencies:** This class does not depend on any external modules beyond standard library imports like ast, os, logging, and collections.defaultdict.
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including dictionaries for storing definitions and call graphs, and defines a set of directories to ignore during traversal.
    *   *Parameters:*
        *   **project_root** (`str`): The absolute path to the root directory of the project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `analyze(self)`
        *   *Description:* The main entry point for performing the analysis of the project. It finds all Python files in the project, collects definitions from those files, resolves calls between definitions, clears temporary AST storage, and returns formatted results.
        *   *Parameters:*
        *   *Returns:*
            *   **output_list** (`list`): A list of dictionaries describing each definition and the callers associated with it.
        *   **Usage:**
            *   **Calls:** This method internally calls `_find_py_files`, `_collect_definitions`, and `_resolve_calls` for each Python file, and finally calls `get_formatted_results`.
            *   **Called By:** This method is called by the functions `evaluation` in `HelperLLM_evaluation.py` at line 120 and `main_workflow` in `main.py` at line 178.
    *   **`_find_py_files`**
        *   *Signature:* `_find_py_files(self)`
        *   *Description:* Traverses the project root directory recursively to find all Python (.py) files, excluding certain directories like .git, venv, etc., and returns a list of their full paths.
        *   *Parameters:*
        *   *Returns:*
            *   **py_files** (`list`): List of absolute paths to Python files in the project.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods directly.
            *   **Called By:** This method is called by the `analyze` method.
    *   **`_collect_definitions`**
        *   *Signature:* `_collect_definitions(self, filepath)`
        *   *Description:* Parses a given Python file into an AST and extracts information about function and class definitions, including their location and type. It maps these definitions to their fully qualified names and stores them in the internal definitions dictionary.
        *   *Parameters:*
            *   **filepath** (`str`): The absolute path to the Python file to analyze.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not call any other methods directly.
            *   **Called By:** This method is called by the `analyze` method.
    *   **`_get_parent`**
        *   *Signature:* `_get_parent(self, tree, node)`
        *   *Description:* Given an AST node and a tree, this helper method attempts to find the parent node of the specified node within the tree by walking the AST.
        *   *Parameters:*
            *   **tree** (`ast.AST`): The AST tree to search within.
            *   **node** (`ast.AST`): The AST node whose parent needs to be found.
        *   *Returns:*
            *   **parent** (`ast.AST or None`): The parent AST node if found, otherwise None.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods directly.
            *   **Called By:** This method is called by the `_collect_definitions` method.
    *   **`_resolve_calls`**
        *   *Signature:* `_resolve_calls(self, filepath)`
        *   *Description:* Resolves call relationships in a given Python file by using a CallResolverVisitor to traverse the AST and collect call information. It updates the internal call graph based on the resolved calls.
        *   *Parameters:*
            *   **filepath** (`str`): The absolute path to the Python file to resolve calls for.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method creates a CallResolverVisitor and calls its visit method, then iterates over the collected calls to update the call graph.
            *   **Called By:** This method is called by the `analyze` method.
    *   **`get_formatted_results`**
        *   *Signature:* `get_formatted_results(self)`
        *   *Description:* Formats the collected call graph and definitions into a structured list of dictionaries. Each dictionary represents a definition and includes details about its origin and the callers that reference it.
        *   *Parameters:*
        *   *Returns:*
            *   **output_list** (`list`): A list of dictionaries containing formatted information about definitions and their callers.
        *   **Usage:**
            *   **Calls:** This method does not call any other methods directly.
            *   **Called By:** This method is called by the `analyze` method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to analyze Python code and resolve call relationships between functions, methods, and modules. It tracks the current execution context (such as class and function names) to determine the caller of each function call. It also maintains mappings of imported names and instance types to resolve qualified names and track which functions are called from where. This class is primarily used in the context of static code analysis to understand inter-module and intra-module dependencies.
*   **Instantiation:** This class is instantiated by the `_resolve_calls` function in the `relationship_analyzer.py` file at line 92.
*   **Dependencies:** This class does not depend on any external libraries beyond standard Python modules like ast, os, logging, and collections.defaultdict.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and a set of definitions. It sets up internal tracking structures such as scope, instance types, and call records. It also determines the module path based on the file path and project root.
    *   *Parameters:*
        *   **filepath** (`str`): The absolute path to the Python file being analyzed.
        *   **project_root** (`str`): The root directory of the project, used to compute relative module paths.
        *   **definitions** (`set`): A collection of known fully qualified names (e.g., module.function) that can be referenced during analysis.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `visit_ClassDef(self, node)`
        *   *Description:* Handles the visitation of class definitions in the AST. It updates the current class name context to track which class is currently being visited, allowing accurate resolution of method calls within the class. After visiting the class body, it restores the previous class name.
        *   *Parameters:*
            *   **node** (`ast.ClassDef`): The AST node representing the class definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is invoked by the AST visitor framework when encountering a class definition in the source code.
    *   **`visit_FunctionDef`**
        *   *Signature:* `visit_FunctionDef(self, node)`
        *   *Description:* Handles the visitation of function definitions in the AST. It updates the current caller name to reflect the function being visited, enabling accurate tracking of which function is making a call. After visiting the function body, it restores the previous caller name.
        *   *Parameters:*
            *   **node** (`ast.FunctionDef`): The AST node representing the function definition.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is invoked by the AST visitor framework when encountering a function definition in the source code.
    *   **`visit_Call`**
        *   *Signature:* `visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST. It resolves the qualified name of the called function using the internal scope and instance types. If the resolved name exists in the definitions, it records the call with metadata about the caller, including the file, line number, and caller type (module, method, or function).
        *   *Parameters:*
            *   **node** (`ast.Call`): The AST node representing the function call.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method calls the private helper method `_resolve_call_qname` to resolve the qualified name of the function being called.
            *   **Called By:** This method is invoked by the AST visitor framework when encountering a function call in the source code.
    *   **`visit_Import`**
        *   *Signature:* `visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST. It maps the imported names to their actual module paths in the internal scope dictionary, allowing for later resolution of qualified names. It supports both regular imports and star imports.
        *   *Parameters:*
            *   **node** (`ast.Import`): The AST node representing the import statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is invoked by the AST visitor framework when encountering an import statement in the source code.
    *   **`visit_ImportFrom`**
        *   *Signature:* `visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST. It resolves the full module path for the imported names, considering relative imports (using the level attribute). It stores these mappings in the internal scope dictionary for use in resolving qualified names.
        *   *Parameters:*
            *   **node** (`ast.ImportFrom`): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is invoked by the AST visitor framework when encountering a 'from ... import ...' statement in the source code.
    *   **`visit_Assign`**
        *   *Signature:* `visit_Assign(self, node)`
        *   *Description:* Processes assignment statements in the AST. Specifically, it looks for assignments where the right-hand side is a function call that creates an instance of a known class. It tracks the type of the assigned variable to enable correct resolution of method calls made on that instance.
        *   *Parameters:*
            *   **node** (`ast.Assign`): The AST node representing the assignment statement.
        *   *Returns:*
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is invoked by the AST visitor framework when encountering an assignment statement in the source code.
    *   **`_resolve_call_qname`**
        *   *Signature:* `_resolve_call_qname(self, func_node)`
        *   *Description:* A helper method that resolves the qualified name of a function call. It handles both direct function names and attribute-based calls (like obj.method). It checks the internal scope and instance types to determine the fully qualified name of the function being called.
        *   *Parameters:*
            *   **func_node** (`ast.expr`): The AST node representing the function being called.
        *   *Returns:*
            *   **resolved_name** (`str or None`): The fully qualified name of the function if resolved, otherwise None.
        *   **Usage:**
            *   **Calls:** This method does not explicitly call any other methods.
            *   **Called By:** This method is called by the `visit_Call` method to resolve the qualified name of the function being called.

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str)`
*   **Description:** The function encrypts a given text string using a Fernet cipher suite. It first checks if the input text is empty or if the cipher suite is not initialized, returning the text as-is in such cases. Otherwise, it encodes the stripped text to bytes, encrypts it using the cipher suite, and returns the decrypted result as a string.
*   **Parameters:**
    *   **text** (`str`): The text string to be encrypted.
*   **Returns:**
    *   **encrypted_text** (`str`): The encrypted version of the input text, returned as a string.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the update_gemini_key function in the db.py file.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str)`
*   **Description:** The function decrypts a given text using a cipher suite if both the text and cipher suite are valid. It handles potential decryption errors gracefully by returning the original text in case of failure. The function performs basic validation on the input text and cipher suite before attempting decryption.
*   **Parameters:**
    *   **text** (`str`): The encrypted text to be decrypted.
*   **Returns:**
    *   **result** (`str`): The decrypted text if successful; otherwise, the original input text.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by get_decrypted_api_keys in db.py at line 93.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** The function inserts a new user into the database by creating a user document with the provided username, name, and password. It hashes the password using a hasher utility before storing the user data. The function returns the ID of the inserted document.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user, used as the '_id' field in the database.
    *   **name** (`str`): The full name of the user to be stored in the database.
    *   **password** (`str`): The plain text password of the user, which gets hashed before storage.
*   **Returns:**
    *   **inserted_id** (`ObjectId`): The unique identifier of the newly inserted user document in the database.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the frontend.Frontend class in Frontend.py at line 294.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user records from a MongoDB collection named 'dbusers'. It performs a database query to find all documents in the collection and returns them as a list. The function does not take any parameters and directly accesses the global 'dbusers' variable, which is expected to be initialized elsewhere in the codebase.
*   **Parameters:**
*   **Returns:**
    *   **result** (`list`): A list containing all user documents retrieved from the 'dbusers' collection.
*   **Usage:**
    *   **Calls:** The function does not call any other functions directly.
    *   **Called By:** This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 244.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The function 'fetch_user' retrieves a user document from a MongoDB collection named 'dbusers' based on the provided username. It uses the 'find_one' method to query the database with a filter that matches the '_id' field to the given username. The function assumes that the 'dbusers' collection and the 'find_one' method are properly initialized and accessible within the scope of the function.
*   **Parameters:**
    *   **username** (`str`): The unique identifier (username) used to locate the specific user document in the MongoDB collection.
*   **Returns:**
    *   **result** (`Any`): The user document retrieved from the MongoDB collection, or None if no matching document is found.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is not called by any other functions within the provided context.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the name field of a user document in a MongoDB collection identified by the username. It uses the MongoDB update_one method to modify only the name field, leaving other fields unchanged. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    *   **username** (`str`): The unique identifier of the user whose name needs to be updated.
    *   **new_name** (`str`): The new name value to be set for the specified user.
*   **Returns:**
    *   **result.modified_count** (`int`): The number of documents that were successfully modified by the update operation.
*   **Usage:**
    *   **Calls:** The function internally calls the MongoDB update_one method to perform the database update operation.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database after encrypting it. It takes a username and an unencrypted API key as inputs, encrypts the key using a helper function, and then updates the corresponding document in the 'dbusers' collection with the encrypted key. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
    *   **gemini_api_key** (`str`): The unencrypted Gemini API key to be stored in the database.
*   **Returns:**
    *   **modified_count** (`int`): The number of documents that were successfully modified in the database. Typically 1 if the update succeeded.
*   **Usage:**
    *   **Calls:** This function internally calls 'encrypt_text' to encrypt the provided API key before storing it.
    *   **Called By:** This function is called by 'save_gemini_cb' in 'Frontend.py' at line 35 and by 'frontend.Frontend' in 'Frontend.py' at line 393.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and performs an update operation on the user document. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    *   **username** (`str`): The unique identifier of the user whose Ollama base URL needs to be updated.
    *   **ollama_base_url** (`str`): The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped.
*   **Returns:**
    *   **modified_count** (`int`): The number of documents that were successfully modified by the update operation. Typically 1 if the user exists and the update was applied.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on the pymongo library's update_one method.
    *   **Called By:** This function is called by save_ollama_cb in Frontend.py at line 42 and by frontend.Frontend in Frontend.py at line 407.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** The function retrieves a Gemini API key associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'gemini_api_key' field. If no matching user is found, it returns None.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose Gemini API key is to be retrieved.
*   **Returns:**
    *   **gemini_api_key** (`str or None`): The retrieved Gemini API key if a matching user is found; otherwise, None.
*   **Usage:**
    *   **Calls:** This function internally uses the 'dbusers.find_one' method to query a MongoDB collection.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** The function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose Ollama base URL is to be retrieved.
*   **Returns:**
    *   **ollama_base_url** (`Optional[str]`): The Ollama base URL associated with the user, or None if the user is not found.
*   **Usage:**
    *   **Calls:** This function internally uses the 'dbusers.find_one' method to query a MongoDB collection.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** The function 'delete_user' removes a user document from a MongoDB collection identified by the provided username. It performs a deletion operation using the 'delete_one' method and returns the count of deleted documents. The function assumes the existence of a global 'dbusers' variable representing the MongoDB collection.
*   **Parameters:**
    *   **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    *   **deleted_count** (`int`): The number of documents deleted as a result of the operation. Typically 0 or 1.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user is not found, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function and retrieves the 'ollama_base_url' directly. It then returns both the decrypted Gemini API key and the Ollama base URL.
*   **Parameters:**
    *   **username** (`str`): The unique identifier for the user whose API keys are to be retrieved.
*   **Returns:**
    *   **gemini_plain** (`str`): The decrypted Gemini API key for the user, or an empty string if not present.
    *   **ollama_plain** (`str`): The Ollama base URL for the user, or an empty string if not present.
*   **Usage:**
    *   **Calls:** The function internally uses dbusers.find_one to retrieve user data and decrypt_text to decrypt the API key.
    *   **Called By:** This function is called by the frontend.Frontend class in Frontend.py at lines 380 and 479.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** The function 'insert_chat' creates a new chat entry in a database with a unique identifier, associated username, chat name, and timestamp. It generates a UUID for the chat ID, captures the current datetime, and inserts the chat document into a MongoDB collection named 'dbchats'. The function returns the ID of the newly inserted document.
*   **Parameters:**
    *   **username** (`str`): The username associated with the chat.
    *   **chat_name** (`str`): The name of the chat to be created.
*   **Returns:**
    *   **result.inserted_id** (`str`): The unique identifier of the newly inserted chat document in the database.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by load_data_from_db in Frontend.py at line 81, handle_delete_chat in Frontend.py at line 122, and frontend.Frontend in Frontend.py at line 344.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** Die Funktion fetch_chats_by_user ruft alle Chats eines bestimmten Benutzers aus einer MongoDB-Datenbank ab. Sie verwendet den Benutzernamen als Filterkriterium und sortiert die Ergebnisse nach dem Erstellungsdatum in aufsteigender Reihenfolge. Das Ergebnis ist eine Liste der gefundenen Chat-Dokumente.
*   **Parameters:**
    *   **username** (`str`): Der Benutzername, dessen Chats abgerufen werden sollen.
*   **Returns:**
    *   **chats** (`list`): Eine Liste aller Chat-Dokumente des angegebenen Benutzers, sortiert nach Erstellungsdatum.
*   **Usage:**
    *   **Calls:** Die Funktion ruft keine anderen Funktionen innerhalb ihres Codes auf.
    *   **Called By:** Die Funktion wird von der Funktion load_data_from_db in der Datei Frontend.py aufgerufen.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a query using MongoDB's find_one method to locate a matching document. If a document is found, the function returns True; otherwise, it returns False.
*   **Parameters:**
    *   **username** (`str`): The username associated with the chat.
    *   **chat_name** (`str`): The name of the chat to check for existence.
*   **Returns:**
    *   **exists** (`bool`): True if a chat with the specified username and chat_name exists in the database, False otherwise.
*   **Usage:**
    *   **Calls:** The function internally uses the dbchats.find_one method to query the database.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and updates all associated exchanges in the database. It first updates the chat entry in the chats collection, then updates all related exchange records in the exchanges collection. The function returns the number of modified chat documents.
*   **Parameters:**
    *   **username** (`str`): The username associated with the chat to be renamed.
    *   **old_name** (`str`): The current name of the chat to be renamed.
    *   **new_name** (`str`): The new name to assign to the chat.
*   **Returns:**
    *   **modified_count** (`int`): The number of chat documents that were successfully modified during the renaming operation.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the frontend.Frontend function in Frontend.py at line 462.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str, main_used: str, total_time: str, helper_time: str, main_time: str)`
*   **Description:** This function inserts a new exchange record into a MongoDB collection. It generates a unique identifier for the exchange, constructs a dictionary with all the provided details including optional fields with default empty strings, and attempts to insert this data into the database. If the insertion fails, it catches the exception, prints an error message, and returns None.
*   **Parameters:**
    *   **question** (`str`): The question asked in the exchange.
    *   **answer** (`str`): The answer provided in response to the question.
    *   **feedback** (`str`): Feedback associated with the exchange.
    *   **username** (`str`): The username of the user involved in the exchange.
    *   **chat_name** (`str`): The name of the chat session.
    *   **helper_used** (`str`): Optional field indicating which helper was used. Defaults to an empty string.
    *   **main_used** (`str`): Optional field indicating which main component was used. Defaults to an empty string.
    *   **total_time** (`str`): Optional field indicating the total time taken. Defaults to an empty string.
    *   **helper_time** (`str`): Optional field indicating the time taken by the helper. Defaults to an empty string.
    *   **main_time** (`str`): Optional field indicating the time taken by the main component. Defaults to an empty string.
*   **Returns:**
    *   **new_id** (`str`): The unique ID generated for the inserted exchange record, or None if insertion failed.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the frontend.Frontend class in Frontend.py at line 530.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses a database query to find documents matching the username and sorts them by the 'created_at' field. The result is returned as a list of exchange records.
*   **Parameters:**
    *   **username** (`str`): The username to filter exchange records by.
*   **Returns:**
    *   **exchanges** (`list`): A list of exchange records retrieved from the database, sorted by creation timestamp.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the load_data_from_db function in Frontend.py at line 64.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched exchanges as a list.
*   **Parameters:**
    *   **username** (`str`): The username associated with the exchanges to be retrieved.
    *   **chat_name** (`str`): The name of the chat associated with the exchanges to be retrieved.
*   **Returns:**
    *   **exchanges** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order.
*   **Usage:**
    *   **Calls:** The function internally uses the 'dbexchanges.find' method to query the database and 'sort' to order the results.
    *   **Called By:** This function is not called by any other functions according to the provided context.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** This function updates the feedback value for a specific exchange document in a MongoDB collection. It takes an exchange ID and a feedback integer, then attempts to update the corresponding document by setting its 'feedback' field to the provided value. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    *   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    *   **feedback** (`int`): The new feedback value to be set for the exchange document.
*   **Returns:**
    *   **result.modified_count** (`int`): The number of documents that were successfully modified by the update operation.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the handle_feedback_change function in Frontend.py at line 98.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** This function updates the feedback message associated with a specific exchange document in a MongoDB collection. It takes an exchange ID and a new feedback message as inputs, then performs an update operation on the database to set the feedback_message field. The function returns the count of modified documents, which should be 1 if the update was successful.
*   **Parameters:**
    *   **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
    *   **feedback_message** (`str`): The new feedback message to be stored in the exchange document.
*   **Returns:**
    *   **modified_count** (`int`): The number of documents that were modified by the update operation.
*   **Usage:**
    *   **Calls:** The function internally calls dbexchanges.update_one to perform the database update operation.
    *   **Called By:** This function is called by the render_exchange function in Frontend.py at line 211.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a given exchange ID. It performs a delete operation using the 'delete_one' method and returns the count of deleted documents. The function takes a single string parameter representing the exchange ID and relies on a pre-configured MongoDB client connection.
*   **Parameters:**
    *   **exchange_id** (`str`): A unique identifier for the exchange document to be deleted.
*   **Returns:**
    *   **deleted_count** (`int`): The number of documents successfully deleted from the collection. Typically 0 or 1.
*   **Usage:**
    *   **Calls:** The function does not call any other functions directly.
    *   **Called By:** This function is called by the 'handle_delete_exchange' function in 'Frontend.py' at line 102.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** The function deletes all exchanges and the chat entry associated with a given username and chat name from the database. It first removes all exchange records matching the criteria, then deletes the corresponding chat record. The function returns the count of deleted chat entries, which should be 1 if the operation was successful.
*   **Parameters:**
    *   **username** (`str`): The username associated with the chat to be deleted.
    *   **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
    *   **deleted_count** (`int`): The number of chat entries that were deleted from the database.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on external database operations via dbexchanges and dbchats.
    *   **Called By:** This function is called by the handle_delete_chat function in Frontend.py at line 110.

### File: `frontend/Frontend.py`

#### Function: `save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** This function handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key for the current user, clears the input field, and displays a success message to the user. The function does not take any parameters and does not return any value.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    *   **Calls:** The function internally uses streamlit session state operations and calls a database update function.
    *   **Called By:** This function is not called by any other function according to the provided context.

#### Function: `save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** This function handles the callback for saving an Ollama URL entered by the user in a Streamlit frontend. It retrieves the URL from the session state, updates the database with the new URL associated with the user's username, and displays a success toast message. The function does not take any parameters and does not return any value.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    *   **Calls:** The function internally uses `st.session_state.get` to retrieve the Ollama URL and `db.update_ollama_url` to update the database.
    *   **Called By:** This function is not called by any other function according to the provided context.

#### Function: `load_data_from_db`
*   **Signature:** `def load_data_from_db(username: str)`
*   **Description:** Die Funktion 'load_data_from_db' lädt Chats und Exchanges konsistent aus einer Datenbank für einen bestimmten Benutzer. Sie prüft zunächst, ob der Benutzer bereits geladen wurde, und lädt nur dann neue Daten, wenn dies erforderlich ist. Zunächst werden Chats aus der Datenbank abgerufen und in den Session-State eingefügt. Anschließend werden Exchanges abgerufen und den entsprechenden Chats zugeordnet. Bei Bedarf wird ein Standard-Chat erstellt und als aktiv markiert.
*   **Parameters:**
    *   **username** (`str`): Der Name des Benutzers, für den die Daten aus der Datenbank geladen werden sollen.
*   **Returns:**
*   **Usage:**
    *   **Calls:** Die Funktion ruft keine anderen internen Funktionen auf.
    *   **Called By:** Die Funktion wird von der Methode 'frontend.Frontend' in der Datei 'Frontend.py' auf Zeile 310 aufgerufen.

#### Function: `handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** This function updates the feedback value for a given exchange object in the database and triggers a re-render of the Streamlit application. It takes an exchange dictionary and a new feedback value, updates the feedback field in the dictionary, saves the updated feedback to the database using the exchange ID, and then reruns the Streamlit app to reflect the changes.
*   **Parameters:**
    *   **ex** (`dict`): A dictionary representing an exchange object, expected to contain keys like 'feedback' and '_id'.
    *   **val** (`Any`): The new feedback value to be assigned to the exchange object.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function internally calls 'db.update_exchange_feedback' to update the feedback in the database and 'st.rerun()' to refresh the Streamlit UI.
    *   **Called By:** This function is called by the 'render_exchange' function in 'Frontend.py' at lines 199 and 204.

#### Function: `handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** This function handles the deletion of an exchange from the database and updates the session state accordingly. It first deletes the exchange by its ID from the database, then checks if the exchange exists in the session state for a given chat and removes it if found. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    *   **chat_name** (`str`): The name of the chat from which the exchange is to be deleted.
    *   **ex** (`dict`): A dictionary representing the exchange to be deleted, expected to contain an '_id' key.
*   **Returns:**
*   **Usage:**
    *   **Calls:** The function internally calls `db.delete_exchange_by_id()` to delete the exchange from the database and `st.rerun()` to refresh the Streamlit UI.
    *   **Called By:** This function is called by the `render_exchange` function in `Frontend.py` at lines 228 and 234.

#### Function: `handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** The function handles the deletion of a chat by first removing the chat from the database and then cleaning up the session state. It ensures that the active chat is updated appropriately, either to another existing chat or by creating a new default chat if none remain. Finally, it triggers a rerun of the Streamlit app to reflect the changes.
*   **Parameters:**
    *   **username** (`str`): The username associated with the chat to be deleted.
    *   **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on external modules like 'db' and 'st' for database operations and Streamlit session management.
    *   **Called By:** This function is called by the frontend.Frontend class in Frontend.py at line 367.

#### Function: `extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** The function 'extract_repo_name' takes a text input and attempts to extract a repository name from any URL present in that text. It uses regular expressions to find a URL, parses it using urllib.parse.urlparse, extracts the path component, and then derives the repository name from the last segment of the path. If the repository name ends with '.git', it removes the extension. If no URL is found or the path is empty, the function returns None.
*   **Parameters:**
    *   **text** (`str`): A string that may contain a URL from which to extract the repository name.
*   **Returns:**
    *   **repo_name** (`str`): The extracted repository name from the URL, with '.git' suffix removed if present.
    *   **None** (`NoneType`): Returned when no valid URL is found in the input text or when the URL path is empty.
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on imported modules like 're' and 'urllib.parse.urlparse'.
    *   **Called By:** This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 442.

#### Function: `stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** The function 'stream_text_generator' takes a string of text as input and yields each word in the text followed by a space, with a small delay between each word. This creates a streaming effect where words are produced one at a time. It uses the 'time.sleep' function to introduce a brief pause between yielding each word.
*   **Parameters:**
    *   **text** (`str`): A string of text to be processed and streamed word by word.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly.
    *   **Called By:** This function is called by the 'render_text_with_mermaid' function in 'Frontend.py' at line 160.

#### Function: `render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream: bool)`
*   **Description:** This function processes a markdown text string to identify and render Mermaid diagrams embedded within code blocks. It splits the input text by Mermaid code blocks, rendering regular markdown content using Streamlit's markdown functionality and Mermaid diagrams using the st_mermaid component. If rendering fails, it falls back to displaying the Mermaid code as a code block. The function supports streaming output when enabled.
*   **Parameters:**
    *   **markdown_text** (`str`): The markdown text that may contain Mermaid code blocks enclosed in triple backticks with 'mermaid' language identifier.
    *   **should_stream** (`bool`): A flag indicating whether to stream the rendered markdown text instead of rendering it all at once.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any other functions directly; it relies on external components like st_mermaid, st.write_stream, st.markdown, and st.code.
    *   **Called By:** This function is called by the render_exchange function in Frontend.py at line 238 and by the frontend.Frontend module at line 524.

#### Function: `render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name: str)`
*   **Description:** The function `render_exchange` renders a chat exchange in a Streamlit interface, displaying a user question and an assistant's response. It handles both regular responses and error cases, providing interactive feedback mechanisms such as like/dislike buttons, comment popups, download options, and deletion capabilities. The assistant's response includes a toolbar with various actions and a content area for rendering the actual answer text with Mermaid support.
*   **Parameters:**
    *   **ex** (`dict`): A dictionary containing the exchange data, including the question, answer, feedback status, and other metadata.
    *   **current_chat_name** (`str`): The name of the current chat session, used for handling exchange deletions.
*   **Returns:**
*   **Usage:**
    *   **Calls:** This function does not call any external functions directly; it relies on Streamlit components and helper functions like `handle_feedback_change` and `handle_delete_exchange`.
    *   **Called By:** This function is called by the `frontend.Frontend` class in the `Frontend.py` file at line 429.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the structure of a single parameter within a function. It enforces that each parameter has a name, a type, and a descriptive string, making it suitable for use in API schemas or documentation systems where parameter metadata needs to be consistently structured and validated.
*   **Instantiation:** This class is not explicitly instantiated by any other component listed in the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* The class is initialized with three required fields: 'name', 'type', and 'description'. These fields define the essential characteristics of a function parameter and are enforced by the Pydantic BaseModel framework.
    *   *Parameters:*
        *   **name** (`str`): The name of the function parameter.
        *   **type** (`str`): The data type of the function parameter.
        *   **description** (`str`): A textual description of the function parameter's purpose or usage.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model designed to represent and validate the description of a function's return value. It encapsulates three essential attributes: the name of the return value, its type, and a textual description. This class ensures that return value metadata is consistently structured and validated, making it suitable for use in API schemas, documentation systems, or any application requiring standardized return value definitions.
*   **Instantiation:** This class is not instantiated by any other component as per the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ReturnDescription instance with a name, type, and description. These fields are required and must be provided during instantiation to create a valid instance of the model.
    *   *Parameters:*
        *   **name** (`str`): The name of the return value.
        *   **type** (`str`): The type of the return value.
        *   **description** (`str`): A textual description of the return value.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function. It captures two key pieces of information: the functions or methods that are called by the function in question, and the functions or methods that call the function in question. This class serves as a structured way to document and enforce the usage relationships between different parts of a codebase.
*   **Instantiation:** This class is not instantiated by any other components mentioned in the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes the UsageContext model with two string fields: 'calls' and 'called_by'. These fields are used to store information about the calling context of a function.
    *   *Parameters:*
        *   **calls** (`str`): A string describing the functions or methods that are called by the function.
        *   **called_by** (`str`): A string describing the functions or methods that call the function.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate detailed metadata about a function, including its overall purpose, parameter descriptions, return value details, and usage context. It serves as a structured representation for documenting function signatures and behaviors, likely used in automated documentation systems or API schema generation.
*   **Instantiation:** This class is not instantiated by any other components as per the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The constructor initializes a FunctionDescription instance with four required fields: 'overall', 'parameters', 'returns', and 'usage_context'. These fields collectively describe the function's behavior, inputs, outputs, and contextual usage information.
    *   *Parameters:*
        *   **overall** (`str`): A string describing the overall purpose and functionality of the function.
        *   **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing each parameter accepted by the function.
        *   **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects detailing the return values of the function.
        *   **usage_context** (`UsageContext`): An object describing the usage context of the function, such as where and how it is called.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic model designed to represent the complete JSON schema for a function. It serves as a structured data container that holds essential information about a function, including its identifier, a detailed description, and an optional error field. This class ensures type safety and validation for function metadata, making it suitable for use in systems that require consistent and reliable function schema representations.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The constructor initializes the FunctionAnalysis model with required fields: 'identifier' as a string and 'description' as a FunctionDescription object. An optional 'error' field is also included, defaulting to None.
    *   *Parameters:*
        *   **identifier** (`str`): A unique identifier for the function.
        *   **description** (`FunctionDescription`): A detailed description of the function's purpose and behavior.
        *   **error** (`Optional[str]`): An optional error message related to the function, defaulting to None.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to describe the initialization method (__init__) of a class. It captures two key aspects of a constructor: a textual description of its purpose and a list of parameter descriptions that define its interface. This class serves as a structured representation for documenting constructor details, likely used in automated documentation systems or API schema generation.
*   **Instantiation:** This class is not instantiated by any other component according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription instance with a description of the constructor and a list of parameter descriptions.
    *   *Parameters:*
        *   **description** (`str`): A textual description of the constructor's purpose.
        *   **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects detailing each parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to describe a class's external dependencies and its primary points of instantiation. It serves as a structured representation of metadata related to a class, capturing information about what external components it relies on and where it is instantiated within the system.
*   **Instantiation:** This class is not instantiated by any other component according to the provided context.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields store information about the class's external dependencies and the entities that instantiate it, respectively.
    *   *Parameters:*
        *   **dependencies** (`str`): A string describing the external dependencies of the class.
        *   **instantiated_by** (`str`): A string describing the entities or locations where the class is instantiated.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information.
*   **Instantiation:** This class is not instantiated by any other component as indicated in the context.
*   **Dependencies:** This class does not depend on any external modules beyond those imported in the file.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ClassDescription model with specified attributes for overall purpose, constructor description, methods analysis, and usage context.
    *   *Parameters:*
        *   **overall** (`str`): A string describing the overall purpose of the class being analyzed.
        *   **init_method** (`ConstructorDescription`): An instance of ConstructorDescription detailing the constructor of the analyzed class.
        *   **methods** (`List[FunctionAnalysis]`): A list of FunctionAnalysis objects representing the methods of the analyzed class.
        *   **usage_context** (`ClassContext`): An instance of ClassContext providing contextual information about how the class is used.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential information about a class including its identifier, a detailed description, and an optional error message. This class is designed to provide a standardized structure for documenting class metadata and associated descriptions.
*   **Instantiation:** This class is not instantiated by any other classes or functions as indicated in the context.
*   **Dependencies:** This class does not depend on any external modules or libraries beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* Initializes a new instance of the ClassAnalysis class with the required identifier and description, and an optional error field.
    *   *Parameters:*
        *   **identifier** (`str`): A string identifier for the class being analyzed.
        *   **description** (`ClassDescription`): An instance of ClassDescription containing detailed information about the class.
        *   **error** (`Optional[str]`): An optional string field to store any error messages related to the class analysis.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for capturing metadata related to calls within the system.
*   **Instantiation:** This class is not instantiated by any other components according to the provided context.
*   **Dependencies:** No external dependencies were identified for this class.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo instance with file, function, mode, and line attributes to represent a call event.
    *   *Parameters:*
        *   **file** (`str`): The file path where the call occurred.
        *   **function** (`str`): The name of the function that made the call.
        *   **mode** (`str`): The mode of the call, such as 'method', 'function', or 'module'.
        *   **line** (`int`): The line number in the file where the call occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing a function. It encapsulates two key pieces of information: a list of function names that the analyzed function calls, and a list of CallInfo objects representing the functions that call the analyzed function.
*   **Instantiation:** This class is instantiated in the evaluation function in HelperLLM_evaluation.py at line 162 and in the main_workflow function in main.py at line 223.
*   **Dependencies:** This class does not depend on any external modules beyond those specified in the imports.
*   **Constructor:**
    *   *Description:* The class is initialized with two fields: 'calls', which is a list of strings representing the names of functions called by the analyzed function, and 'called_by', which is a list of CallInfo objects indicating the callers of the analyzed function.
    *   *Parameters:*
        *   **calls** (`List[str]`): A list of string identifiers for functions called by the analyzed function.
        *   **called_by** (`List[CallInfo]`): A list of CallInfo objects describing the functions that call the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for analyzing a function, including its mode, identifier, source code, imports, and associated context.
*   **Instantiation:** The class is instantiated by the evaluation function in HelperLLM_evaluation.py at line 167 and by the main_workflow function in main.py at line 228.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput instance with fields representing the mode, identifier, source code, imports, and context required for function analysis.
    *   *Parameters:*
        *   **mode** (`Literal[\"function_analysis\"]`): A literal string indicating the mode of operation, specifically set to \"function_analysis\".
        *   **identifier** (`str`): A string identifier for the function being analyzed.
        *   **source_code** (`str`): The raw source code of the function under analysis.
        *   **imports** (`List[str]`): A list of import statements used within the function's source code.
        *   **context** (`FunctionContextInput`): An object containing contextual information about the function, such as its dependencies and call relationships.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent and exchange metadata about method usage and dependencies in a structured format.
*   **Instantiation:** This class is instantiated in the evaluation function in HelperLLM_evaluation.py at line 187 and in the main_workflow function in main.py at line 248.
*   **Dependencies:** This class does not explicitly depend on any external libraries beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* The class is initialized with a set of predefined fields that define the structure of the method context. It inherits from BaseModel, which provides validation and serialization capabilities.
    *   *Parameters:*
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to structure contextual information about a class being analyzed. It encapsulates three key pieces of information: a list of dependencies, a list of call information for where the class is instantiated, and a list of method contexts for the methods within the class.
*   **Instantiation:** The class is instantiated by the main_orchestrator function in HelperLLM.py at line 369, the evaluation function in HelperLLM_evaluation.py at line 199, and the main_workflow function in main.py at line 260.
*   **Dependencies:** This class does not depend on any external modules beyond those already imported in the file.
*   **Constructor:**
    *   *Description:* The constructor initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are intended to hold lists of strings, CallInfo objects, and MethodContextInput objects respectively.
    *   *Parameters:*
        *   **dependencies** (`List[str]`): A list of string identifiers representing the dependencies of the class.
        *   **instantiated_by** (`List[CallInfo]`): A list of CallInfo objects indicating where and how the class is instantiated.
        *   **method_context** (`List[MethodContextInput]`): A list of MethodContextInput objects describing the context of each method within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class serves as a data structure for encapsulating the necessary inputs required to generate a ClassAnalysis object. It defines the expected fields including the mode of operation, a unique identifier, the source code of the class being analyzed, a list of import statements, and contextual information about how the class is used within the system.
*   **Instantiation:** The class is instantiated by the main_orchestrator function in HelperLLM.py at line 338, the evaluation function in HelperLLM_evaluation.py at line 205, and the main_workflow function in main.py at line 266.
*   **Dependencies:** This class does not depend on any external modules beyond standard typing and pydantic components.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysisInput instance with the required fields: mode, identifier, source_code, imports, and context. The mode is constrained to the literal value 'class_analysis', ensuring that only class analysis operations can instantiate this object.
    *   *Parameters:*
        *   **mode** (`Literal['class_analysis']`): A literal string value that specifies the mode of operation as 'class_analysis'.
        *   **identifier** (`str`): A string identifier for the class being analyzed.
        *   **source_code** (`str`): The raw source code of the class to be analyzed.
        *   **imports** (`List[str]`): A list of import statements associated with the class.
        *   **context** (`ClassContextInput`): An object containing contextual information about the class usage.
*   **Methods:**

---
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview  
- **Description:** *Could not be determined due to a missing README file and insufficient context.*  
- **Key Features:**  
  - None identified (information not found)  
- **Tech Stack:**  
  - None identified (information not found)  

*Repository Structure*  
```mermaid
graph LR
    root --> SystemPrompts[SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt]
    root --> backend[backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
    root --> database[database<br/>db.py]
    root --> frontend[frontend<br/>__init__.py<br/>frontend.py]
    root --> ".streamlit"[frontend/.streamlit<br/>config.toml]
    root --> gifs[frontend/gifs<br/>4j.gif]
    root --> notizen[notizen<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md]
    root --> grafiken[notizen/grafiken<br/>1<br/>2<br/>Flask-Repo<br/>Repo-onboarding]
    root --> result[result<br/>... (files omitted for brevity)]
    root --> schemas[schemas<br/>types.py]
    root --> statistics[statistics<br/>... (files omitted for brevity)]
    root --> test.json[test.json]
    root --> output.json[output.json]
    root --> output.toon[output.toon]
    root --> readme.md[readme.md]
    root --> requirements.txt[requirements.txt]
    root --> .env.example[.env.example]
    root --> .gitignore[.gitignore]
    root --> analysis_output.json[analysis_output.json]
```

---

## 2. Installation  

### Dependencies  
- The project relies on a large number of Python packages (see `requirements.txt`).  
- To install all required dependencies, run:  

```bash
pip install -r requirements.txt
```  

### Setup Guide  
*Information not found.*

### Quick Startup  
*Information not found.*

---

## 3. Use Cases & Commands  

| Use‑Case | Description | Primary Command / API |
|----------|-------------|-----------------------|
| Analyze a remote GitHub repository and generate a full onboarding report | Clones the repository, extracts project metadata, builds AST and call‑graph schemas, runs Helper‑LLM and Main‑LLM to produce a markdown report with token‑usage statistics. | `python -m backend.main "https://github.com/owner/repo"` |
| Generate documentation for a single Python function or class | Supplies a `FunctionAnalysisInput` or `ClassAnalysisInput` to `HelperLLM.generate_for_functions` / `generate_for_classes`. | Use the `backend.HelperLLM.LLMHelper` class programmatically. |
| Visualise file‑level import dependencies | Builds a directed graph of Python file imports. | Call `backend.File_Dependency.build_repository_graph(repo)` and optionally export with `backend.callgraph.make_safe_dot`. |
| Analyse Jupyter notebooks in a repository | Converts notebooks to an XML‑like representation, then uses a Gemini‑based LLM to produce per‑notebook reports. | `backend.main.notebook_workflow(...)`. |
| Store and retrieve user API keys / chat history (Streamlit UI) | Database utilities for CRUD operations on users, chats, exchanges. | Functions in `database.db` (e.g., `insert_user`, `fetch_chats_by_user`). |

---

## 4. Architecture  
*No Mermaid diagrams were supplied in the input data.*  

---

## 5. Code Analysis  

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`  
* **Signature:** `def path_to_module(filepath, project_root)`  
* **Description:** Converts a given file path into its corresponding Python module path, handling relative paths, stripping the `.py` extension, and normalising `__init__.py`.  
* **Parameters:**  
  - **filepath** (`str`): The absolute or relative path to the Python file.  
  - **project_root** (`str`): The root directory of the project, used to calculate the relative path.  
* **Returns:**  
  - **module_path** (`str`): The converted Python module path string.  
* **Usage:** No explicit calls recorded in the provided context.

#### Class: `ASTVisitor`  
* **Summary:** Traverses a Python AST to collect imports, functions, and class definitions, building a structured schema.  
* **Instantiation:** Called by `backend.AST_Schema.ASTAnalyzer.analyze_repository`.  
* **Dependencies:** Depends on `backend.AST_Schema.path_to_module`.  
* **Constructor:**  
  - *Description:* Initializes with source code, file path, and project root; computes module path and prepares an empty schema.  
  - *Parameters:* `source_code` (`str`), `file_path` (`str`), `project_root` (`str`).  
* **Methods:**  
  - **`visit_Import`** – Records simple import statements.  
  - **`visit_ImportFrom`** – Records `from X import Y` statements.  
  - **`visit_ClassDef`** – Creates class metadata, stores it, and sets the current class context.  
  - **`visit_FunctionDef`** – Distinguishes between top‑level functions and methods; records their metadata.  
  - **`visit_AsyncFunctionDef`** – Delegates to `visit_FunctionDef`.  

#### Class: `ASTAnalyzer`  
* **Summary:** Provides high‑level analysis of a repository: parses files, builds per‑file AST schemas, and merges relationship data.  
* **Instantiation:** Not explicitly shown; used in `backend.main.main_workflow`.  
* **Methods:**  
  - **`analyze_repository`** – Parses Python files, builds AST schemas via `ASTVisitor`.  
  - **`merge_relationship_data`** – Enriches the AST schema with call‑graph relationships (calls, called_by, dependencies).  

---

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`  
* **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`  
* **Description:** Constructs a directed graph of file‑level import dependencies for a single Python file using `FileDependencyGraph`.  
* **Parameters:**  
  - **filename** (`str`) – Path to the file being analysed.  
  - **tree** (`AST`) – Parsed abstract syntax tree of the file.  
  - **repo_root** (`str`) – Root directory of the repository (for relative import resolution).  
* **Returns:** `graph` (`networkx.DiGraph`) – Nodes are files; edges represent import relationships.  
* **Calls:** `backend.File_Dependency.FileDependencyGraph`.  

#### Function: `build_repository_graph`  
* **Signature:** `def build_repository_graph(repository)`  
* **Description:** Aggregates per‑file dependency graphs into a global repository‑wide graph.  
* **Parameters:** `repository` (`GitRepository`).  
* **Returns:** `global_graph` (`nx.DiGraph`).  
* **Calls:** `backend.File_Dependency.build_file_dependency_graph`.  

#### Function: `get_all_temp_files`  
* **Signature:** `def get_all_temp_files(directory)`  
* **Description:** Recursively finds all `.py` files under a directory, returning a list of `Path` objects.  
* **Parameters:** `directory` (`str`).  
* **Returns:** `all_files` (`list[Path]`).  

#### Class: `FileDependencyGraph`  
* **Summary:** AST visitor that records import dependencies of a single file, handling both absolute and relative imports.  
* **Instantiation:** Called by `build_file_dependency_graph`.  
* **Constructor:** Stores `filename` and `repo_root`.  
* **Key Methods:**  
  - **`_resolve_module_name`** – Resolves relative imports (`from .. import X`).  
  - **`visit_Import`** – Records simple imports.  
  - **`visit_ImportFrom`** – Handles `from X import Y` and delegates to `_resolve_module_name` for relative cases.  

---

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`  
* **Signature:** `def main_orchestrator()`  
* **Description:** Dummy driver that creates example `FunctionAnalysisInput`/`ClassAnalysisInput` objects, runs the `LLMHelper` to generate documentation, and prints the aggregated JSON result.  
* **Calls:** `backend.HelperLLM.LLMHelper`, `schemas.types.ClassAnalysisInput`, `schemas.types.ClassContextInput`.  

#### Class: `LLMHelper`  
* **Summary:** Centralises interaction with various LLM providers (Gemini, OpenAI, Ollama, custom APIs) for generating structured documentation of functions and classes. Handles batch processing, rate‑limit waiting, and schema validation via Pydantic models.  
* **Constructor Parameters:** `api_key`, `function_prompt_path`, `class_prompt_path`, optional `model_name`, optional `base_url`.  
* **Key Methods:**  
  - **`_configure_batch_settings`** – Sets `batch_size` based on model name.  
  - **`generate_for_functions`** – Sends a batch of function inputs to the LLM and returns `FunctionAnalysis` objects (or `None` on error).  
  - **`generate_for_classes`** – Same as above but for classes (`ClassAnalysis`).  

---

### File: `backend/MainLLM.py`

#### Class: `MainLLM`  
* **Summary:** Provides a thin wrapper around a chosen LLM (Gemini, OpenAI, Ollama, or custom) for single‑shot or streaming interactions using a system prompt loaded from a file.  
* **Constructor Parameters:** `api_key`, `prompt_file_path`, optional `model_name`, optional `base_url`.  
* **Methods:**  
  - **`call_llm`** – Sends a user message and returns the complete response content.  
  - **`stream_llm`** – Returns a generator yielding streamed response chunks.  

---

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`  
* **Summary:** Extracts high‑level project metadata (title, description, status, key features, tech stack, dependencies, setup instructions, quick‑start guide) from common files (`README`, `pyproject.toml`, `requirements.txt`).  
* **Key Private Helpers:** `_clean_content`, `_finde_datei`, `_extrahiere_sektion_aus_markdown`, `_parse_readme`, `_parse_toml`, `_parse_requirements`.  
* **Public Method:** `extrahiere_info(dateien, repo_url)` – Orchestrates detection and parsing of relevant files, returns a dictionary with the extracted info.  

---

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`  
* **Signature:** `def make_safe_dot(graph, out_path)`  
* **Description:** Relabels graph nodes with safe identifiers (`n0`, `n1`, …) and writes a DOT file preserving original labels.  

#### Function: `build_filtered_callgraph`  
* **Signature:** `def build_filtered_callgraph(repo)`  
* **Description:** Generates a call‑graph limited to functions defined inside the repository (excluding external library calls).  
* **Calls:** `backend.callgraph.CallGraph`.  

#### Class: `CallGraph`  
* **Summary:** Visits an AST to build a call‑graph (`networkx.DiGraph`). Tracks imports, class context, and resolves call targets to fully‑qualified identifiers.  
* **Key Methods:** `_recursive_call`, `_resolve_all_callee_names`, `_make_full_name`, `_current_caller`, `visit_Import`, `visit_ImportFrom`, `visit_ClassDef`, `visit_FunctionDef`, `visit_Call`, `visit_If`.  

---

### File: `backend/converter.py`

#### Function: `wrap_cdata` – Wraps text inside CDATA tags.  
#### Function: `extract_output_content` – Extracts textual and image data from notebook cell outputs, inserting placeholders for images.  
#### Function: `process_image` – Helper used by `extract_output_content` (implementation shown inside).  
#### Function: `convert_notebook_to_xml` – Turns a Jupyter notebook into an XML‑like representation, handling markdown, code, and output cells.  
#### Function: `process_repo_notebooks` – Finds all `.ipynb` files in a repo, converts each via `convert_notebook_to_xml`, returns a dict of `{path: {"xml": ..., "images": [...]}}`.  

---

### File: `backend/getRepo.py`

#### Class: `RepoFile`  
* **Summary:** Represents a single file in a Git repository with lazy loading of its blob, content, and size. Provides utility methods such as `analyze_word_count`.  

#### Class: `GitRepository`  
* **Summary:** Manages cloning of a remote repository into a temporary directory, provides access to `RepoFile` objects, and can produce a hierarchical file‑tree dictionary. Implements context‑manager protocol (`__enter__`, `__exit__`).  

---

### File: `backend/main.py`

#### Function: `create_savings_chart` – Generates a bar chart comparing JSON vs TOON token counts.  
#### Function: `calculate_net_time` – Computes net execution time after subtracting rate‑limit sleep intervals (for Gemini models).  
#### Function: `update_status` – Helper for logging and optional UI callbacks.  
#### Function: `main_workflow` – Orchestrates the full onboarding pipeline:  
  1. Parses user input for repo URL and API keys.  
  2. Clones the repo, extracts basic info, builds file tree.  
  3. Runs relationship analysis (`ProjectAnalyzer`).  
  4. Generates AST schema (`ASTAnalyzer`).  
  5. Enriches AST with relationship data.  
  6. Prepares inputs for Helper LLM (functions & classes).  
  7. Calls `LLMHelper` to obtain documentation for each component.  
  8. Calls `MainLLM` to synthesize the final markdown report.  
  9. Calculates token‑savings and creates a chart.  
  10. Saves the report and statistics.  

#### Function: `notebook_workflow` – Similar to `main_workflow` but focuses on Jupyter notebooks, converting them to XML, building a Gemini multimodal payload, and generating per‑notebook reports via `MainLLM`.  

#### Function: `gemini_payload` – Builds a multimodal (text + image) payload for Gemini from notebook XML and extracted images.  

---

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module` – Same functionality as in `AST_Schema`.  

#### Class: `ProjectAnalyzer`  
* **Summary:** Performs static analysis to discover function/class definitions and resolve call relationships across the entire project.  
* **Key Methods:** `analyze`, `get_raw_relationships`, `_find_py_files`, `_collect_definitions`, `_resolve_calls`, `_get_parent`.  

#### Class: `CallResolverVisitor`  
* **Summary:** AST visitor that records calls, resolves imports, and tracks instance types to resolve method calls on objects.  

---

### File: `database/db.py`

*(Only a selection shown – all functions follow the same pattern of interacting with a MongoDB collection `dbusers`, `dbchats`, or `dbexchanges`.)*  

#### Function: `encrypt_text` – Encrypts a string using a preset `cipher_suite`.  
#### Function: `decrypt_text` – Decrypts a string, handling errors gracefully.  
#### Function: `insert_user` – Inserts a new user document with hashed password.  
#### Function: `fetch_all_users` – Returns a list of all user documents.  
#### Function: `fetch_user` – Retrieves a single user by username.  
#### Function: `update_user_name` – Updates the `name` field of a user.  
#### Function: `update_gemini_key` – Encrypts & stores a user's Gemini API key.  
#### Function: `update_gpt_key` – Encrypts & stores a user's GPT API key.  
#### Function: `update_ollama_url` – Stores a user's Ollama base URL.  
#### Function: `update_opensrc_key` / `update_opensrc_url` – Similar for Open‑Source API keys/URLs.  
#### Function: `fetch_gemini_key`, `fetch_gpt_key`, `fetch_ollama_url`, `fetch_opensrc_key`, `fetch_opensrc_url` – Retrieve stored credentials.  
#### Function: `get_decrypted_api_keys` – Returns decrypted keys for a user (calls `decrypt_text`).  
#### Function: `insert_chat`, `fetch_chats_by_user`, `check_chat_exists`, `rename_chat_fully`, `delete_full_chat` – Manage chat metadata.  
#### Function: `insert_exchange`, `fetch_exchanges_by_user`, `fetch_exchanges_by_chat`, `update_exchange_feedback`, `update_exchange_feedback_message`, `delete_exchange_by_id`, `delete_full_chat` – Manage chat exchanges.  

---

### File: `frontend/frontend.py`

#### Functions (selected):  
- `clean_names(model_list)` – Returns list with only the final component of each model name.  
- `get_filtered_models(source_list, category_name)` – Filters model list based on keywords or a standard list.  
- `save_gemini_cb`, `save_ollama_cb` – Callback to store API keys/URL from Streamlit UI.  
- `load_data_from_db(username)` – Populates Streamlit session state with chats and exchanges.  
- `handle_feedback_change`, `handle_delete_exchange`, `handle_delete_chat` – UI callbacks for feedback, deletion.  
- `extract_repo_name(text)` – Extracts repo name from a URL.  
- `stream_text_generator(text)` – Yields words with a short delay for streaming effect.  
- `render_text_with_mermaid(markdown_text, should_stream=False)` – Renders markdown, extracting and displaying Mermaid diagrams.  
- `render_exchange(ex, current_chat_name)` – Renders a chat exchange with feedback buttons, download, and delete actions.  

---

### File: `schemas/types.py`

*(All classes are Pydantic models defining the JSON schema for analysis results.)*  

- `ParameterDescription` – `{name, type, description}`.  
- `ReturnDescription` – `{name, type, description}`.  
- `UsageContext` – `{calls, called_by}`.  
- `FunctionDescription` – `{overall, parameters, returns, usage_context}`.  
- `FunctionAnalysis` – `{identifier, description, error?}`.  
- `ConstructorDescription` – `{description, parameters}`.  
- `ClassContext` – `{dependencies, instantiated_by}`.  
- `ClassDescription` – `{overall, init_method, methods, usage_context}`.  
- `ClassAnalysis` – `{identifier, description, error?}`.  
- `CallInfo` – `{file, function, mode, line}`.  
- `FunctionContextInput` – `{calls, called_by}`.  
- `FunctionAnalysisInput` – `{mode="function_analysis", identifier, source_code, imports, context}`.  
- `MethodContextInput` – `{identifier, calls, called_by, args, docstring?}`.  
- `ClassContextInput` – `{dependencies, instantiated_by, method_context}`.  
- `ClassAnalysisInput` – `{mode="class_analysis", identifier, source_code, imports, context}`.  

---  

*End of generated documentation.*
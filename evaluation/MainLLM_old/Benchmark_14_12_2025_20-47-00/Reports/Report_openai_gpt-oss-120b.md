# Project Documentation: repo‑onboarding‑agent documentation

## 1. Project Overview
- **Description:**  
  *Description could not be determined due to a missing README file and insufficient context.*

- **Key Features:**  
  - Information not found  
  - Information not found  
  - Information not found  
  - Information not found  
  - Information not found  

- **Tech Stack:**  
  Information not found  

*Repository Structure*

```mermaid
graph LR
    root --> SystemPrompts[SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt]
    root --> backend[backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
    root --> database[database<br/>db.py]
    root --> frontend[frontend<br/>Frontend.py<br/>__init__.py<br/>gifs (directory)<br/>.streamlit (directory)]
    root --> notizen[notizen<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken (directory)<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md]
    root --> result[result<br/>ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>… (other report files) ]
    root --> schemas[schemas<br/>types.py]
    root --> statistics[statistics<br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>… (other png files) ]
```

## 2. Installation
### Dependencies
*Information not found.*  
If a `requirements.txt` is present, install with:

```bash
pip install -r requirements.txt
```

### Setup Guide
*Information not found.*

### Quick Startup
*Information not found.*

## 3. Use Cases & Commands
The repository implements an **automated code‑analysis and documentation generation pipeline** for any GitHub Python project. Typical workflow:

1. **Provide a GitHub URL** (via Streamlit UI or API).  
2. The system **clones the repository**, extracts basic project metadata, builds an AST schema, and analyses call relationships.  
3. **Helper LLM** (`LLMHelper`) generates detailed function‑ and class‑level documentation.  
4. **Main LLM** (`MainLLM`) assembles a final Markdown report.  
5. Token‑saving statistics are visualised and stored.

Primary commands (invoked internally by the pipeline):

- `backend.main.main_workflow(input, api_keys, model_names)` – orchestrates the whole analysis.  
- `backend.HelperLLM.main_orchestrator()` – dummy entry used for LLMHelper testing.  
- `backend.MainLLM.call_llm(user_input)` – low‑level LLM query.  

The Streamlit front‑end (`frontend.Frontend`) offers UI controls to trigger the workflow, save API keys, and view generated reports.

## 4. Architecture
*(No Mermaid diagrams were supplied in the input data.)*

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
* **Summary:** Traverses an AST to collect imports, functions, and classes, building a structured schema.  
* **Instantiation:** Instantiated in `ASTAnalyzer.analyze_repository` (line 182).  
* **Dependencies:** Uses `ast`, `networkx`, `os`, `callgraph.build_filtered_callgraph`, `getRepo.GitRepository`.  
* **Constructor:**  
  ```python
  def __init__(self, source_code: str, file_path: str, project_root: str)
  ```
  *Parameters*  
  - `source_code` (`str`): source of the file.  
  - `file_path` (`str`): path to the file.  
  - `project_root` (`str`): repository root.  

* **Methods**
  * **`visit_Import`** – records imported module names.  
  * **`visit_ImportFrom`** – records `from X import Y` imports.  
  * **`visit_ClassDef`** – creates a class entry in the schema; sets current class context.  
  * **`visit_FunctionDef`** – records functions; if inside a class, registers as a method (see method context).  
  * **`visit_AsyncFunctionDef`** – forwards to `visit_FunctionDef`.  

* **Usage**  
  *Calls*: none (operates on AST nodes).  
  *Called by*: `ASTAnalyzer.analyze_repository` (line 182).

#### Class: `ASTAnalyzer`
* **Summary:** Provides high‑level repository analysis: parses files into ASTs, builds per‑file schemas, enriches them with call‑graph data, and merges relationship information.  
* **Instantiation:** Created in several evaluation scripts (e.g., `HelperLLM_evaluation.py` line 128).  
* **Dependencies:** `ast`, `networkx`, `os`, `callgraph.build_filtered_callgraph`, `getRepo.GitRepository`.  
* **Constructor:** No arguments.  

* **Methods**
  * **`_enrich_schema_with_callgraph(schema, call_graph, filename)`** – adds `calls`/`called_by` to functions & methods from a global call graph.  
  * **`merge_relationship_data(full_schema, relationship_data)`** – inserts `called_by` information from the relationship analyzer into the schema.  
  * **`analyze_repository(files, repo)`** – core routine that iterates over repository files, builds ASTs, collects schemas, enriches with call‑graph, and returns a full schema.

* **Usage**  
  *Calls*: internal utilities and `build_filtered_callgraph`.  
  *Called by*: `main.main_workflow` (line 187) and evaluation helpers.

---

### File: `backend/File_Dependency.py`

#### Function: `build_file_dependency_graph`
* **Overall:** Builds a `networkx.DiGraph` representing import‑level dependencies for a single Python file.  
* **Signature:**  
  ```python
  def build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph
  ```
* **Parameters**  
  - `filename` (`str`): name of the file (without extension).  
  - `tree` (`AST`): abstract syntax tree of the file.  
  - `repo_root` (`str`): repository root directory.  
* **Returns** – `graph` (`nx.DiGraph`).  
* **Usage** – Called by `build_repository_graph` (line 156).

#### Function: `build_repository_graph`
* **Overall:** Aggregates file‑level dependency graphs into a global repository‑wide directed graph.  
* **Signature:**  
  ```python
  def build_repository_graph(repository: GitRepository) -> nx.DiGraph
  ```
* **Parameters** – `repository` (`GitRepository`).  
* **Returns** – `global_graph` (`nx.DiGraph`).  
* **Usage** – Called internally by repository‑level scripts (line 177).

#### Function: `get_all_temp_files`
* **Overall:** Recursively collects all `.py` files below a directory, returning `pathlib.Path` objects relative to that directory.  
* **Signature:**  
  ```python
  def get_all_temp_files(directory: str) -> list[Path]
  ```
* **Parameters** – `directory` (`str`).  
* **Returns** – `all_files` (`list[pathlib.Path]`).  
* **Usage** – Used inside `FileDependencyGraph._resolve_module_name` (line 43).

#### Class: `FileDependencyGraph`
* **Summary:** AST visitor that extracts import dependencies for a single file, handling both absolute and relative imports.  
* **Instantiation:** Created inside `build_file_dependency_graph` (line 156).  
* **Dependencies:** `ast`, `os`, `pathlib.Path`, project‑wide helper `get_all_temp_files`.  

* **Constructor:**  
  ```python
  def __init__(self, filename: str, repo_root)
  ```
  *Parameters* – `filename` (`str`), `repo_root` (any).  

* **Methods**
  * **`_resolve_module_name(self, node: ImportFrom) -> list[str]`** – resolves relative imports to actual module or symbol names; may raise `ImportError`.  
  * **`visit_Import(self, node, base_name=None)`** – records simple imports.  
  * **`visit_ImportFrom(self, node)`** – handles `from … import …`; uses `_resolve_module_name` for relative imports.

* **Usage** – Invoked by `build_file_dependency_graph`.

---

### File: `backend/HelperLLM.py`

#### Function: `main_orchestrator`
* **Overall:** Demonstrates a dummy data flow for testing `LLMHelper`. Constructs mock `FunctionAnalysisInput` objects for three sample functions, creates a `LLMHelper`, and runs documentation generation.  
* **Signature:**  
  ```python
  def main_orchestrator()
  ```
* **Parameters:** none.  
* **Returns:** none (prints final JSON).  
* **Usage:** Called at the end of `HelperLLM.py` (line 419) and by evaluation scripts.

#### Class: `LLMHelper`
* **Summary:** Wrapper around various LLM back‑ends (Gemini, OpenAI, custom APIs, Ollama) that batches requests for function and class documentation generation, handling rate‑limits and structured output via Pydantic models.  
* **Instantiation:** Used throughout the pipeline (`main_workflow`, evaluation scripts).  
* **Dependencies:** `langchain_*` libraries, `pydantic` models from `schemas.types`, `json`, `logging`, `time`.  

* **Constructor:**  
  ```python
  def __init__(self, api_key: str, function_prompt_path: str,
               class_prompt_path: str, model_name: str = "gemini-2.0-flash-lite",
               base_url: str = None)
  ```
  *Parameters* – API credentials, prompt file paths, optional model name & base URL.  

* **Methods**
  * **`_configure_batch_settings(self, model_name)`** – sets `self.batch_size` according to model.  
  * **`generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]`** – batches function inputs, sends them to the LLM, respects rate‑limits, and returns validated `FunctionAnalysis` objects (or `None` on error).  
  * **`generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]`** – analogous to the function method but for classes.

* **Usage** – Called by `backend.main.main_workflow` to produce documentation for every discovered function and class.

---

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
* **Summary:** High‑level interface to the *main* LLM that produces the final documentation report. Supports synchronous (`call_llm`) and streaming (`stream_llm`) interactions.  
* **Dependencies:** `langchain_google_genai`, `langchain_openai`, `langchain_ollama`, `langchain.messages`.  

* **Constructor:**  
  ```python
  def __init__(self, api_key: str, prompt_file_path: str,
               model_name: str = "gemini-2.5-pro", base_url: str = None)
  ```
* **Methods**
  * **`call_llm(self, user_input: str) -> str | None`** – sends a single prompt and returns the LLM’s response content.  
  * **`stream_llm(self, user_input: str) -> Iterator[str]`** – streams the response chunk‑by‑chunk.

* **Usage** – Invoked at the end of `backend.main.main_workflow` to turn the enriched AST schema into a human‑readable Markdown report.

---

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
* **Summary:** Extracts high‑level project metadata (title, description, features, tech stack, dependencies, setup instructions) from common repo files (`README`, `pyproject.toml`, `requirements.txt`).  
* **Dependencies:** Standard library (`re`, `os`, `tomllib`, typing).  

* **Constructor:** Initializes placeholder values (`Information not found`).  

* **Key Methods**
  * **`_finde_datei(self, patterns, dateien)`** – case‑insensitive search for a file matching one of the patterns.  
  * **`_extrahiere_sektion_aus_markdown(self, inhalt, keywords)`** – regex‑based extraction of a markdown section under a heading.  
  * **`_parse_readme(self, inhalt)`**, **`_parse_toml(self, inhalt)`**, **`_parse_requirements(self, inhalt)`** – parse respective files and fill the internal `info` dict.  
  * **`extrahiere_info(self, dateien, repo_url)`** – orchestrates the whole extraction process, applies priority (toml > requirements > README), formats dependencies list, and derives a title from the repository URL.

* **Usage** – Called by `backend.main.main_workflow` to obtain `basic_project_info`.

---

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
* **Overall:** Writes a DOT file with sanitized node identifiers (`n0`, `n1`, …) while preserving original labels as node attributes.  
* **Signature:**  
  ```python
  def make_safe_dot(graph: nx.DiGraph, out_path: str)
  ```
* **Parameters** – `graph` (`nx.DiGraph`), `out_path` (`str`).  
* **Usage:** Called by `callgraph` module (line 244) for visualisation.

#### Function: `build_filtered_callgraph`
* **Overall:** Constructs a global call‑graph from all repository Python files, then filters to retain only calls between *own* functions.  
* **Signature:**  
  ```python
  def build_filtered_callgraph(repo: GitRepository) -> nx.DiGraph
  ```
* **Parameters** – `repo` (`GitRepository`).  
* **Returns** – `global_graph` (`nx.DiGraph`).  
* **Usage:** Invoked by `ASTAnalyzer.analyze_repository` (line 167) and directly by `callgraph` (line 243).

#### Class: `CallGraph`
* **Summary:** Visitor that walks a Python AST and records function/method definitions and call relationships, producing a directed graph of internal calls.  
* **Dependencies:** `ast`, `networkx`.  

* **Constructor:** `def __init__(self, filename: str)` – stores filename and initialises structures.  

* **Important Methods**
  * `_recursive_call(self, node)` – extracts dotted name parts from a call node.  
  * `_resolve_all_callee_names(self, callee_nodes)` – resolves names against local definitions and imports.  
  * `_make_full_name(self, basename, class_name=None)` – builds fully‑qualified identifiers.  
  * `_current_caller(self)` – determines the current caller context.  
  * Visitor callbacks (`visit_Import`, `visit_ImportFrom`, `visit_ClassDef`, `visit_FunctionDef`, `visit_AsyncFunctionDef`, `visit_Call`, `visit_If`) – populate `self.graph`, `self.import_mapping`, `self.local_defs`, and `self.edges`.

* **Usage:** Instantiated by `build_filtered_callgraph` for each file (lines 199, 206).

---

### File: `backend/getRepo.py`

#### Class: `RepoFile`
* **Summary:** Lazy‑loading wrapper for a single file in a cloned Git repository. Provides `blob`, `content`, `size`, plus a simple word‑count analysis.  
* **Constructor:** `def __init__(self, file_path, commit_tree)`.  

* **Properties** – `blob`, `content`, `size` (all lazily loaded).  

* **Methods** – `analyze_word_count`, `__repr__`, `to_dict(include_content=False)`.

* **Usage:** Created by `GitRepository.get_all_files` (line 111).

#### Class: `GitRepository`
* **Summary:** Clones a remote Git repository into a temporary directory and offers utilities to list files and build a hierarchical file‑tree. Implements the context‑manager protocol for automatic cleanup.  
* **Constructor:** `def __init__(self, repo_url)`.  
* **Key Methods**
  * `get_all_files()` – returns `RepoFile` objects for every repository file.  
  * `close()` – deletes temporary directory.  
  * `__enter__` / `__exit__` – enable `with GitRepository(url) as repo:` usage.  
  * `get_file_tree(include_content=False)` – builds a nested dict representing the repository’s directory structure.

* **Usage:** Employed throughout the pipeline (`backend.main.main_workflow`, evaluation scripts) to obtain repository contents.

---

### File: `backend/main.py`

#### Function: `create_savings_chart`
* **Overall:** Generates a Matplotlib bar chart comparing token counts of JSON vs. TOON formats and saves it as an image.  
* **Signature:**  
  ```python
  def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)
  ```
* **Parameters** – `json_tokens` (`int`), `toon_tokens` (`int`), `savings_percent` (`float`), `output_path` (`str`).  
* **Usage:** Called from `main_workflow` after token‑savings evaluation (line 503).

#### Function: `calculate_net_time`
* **Overall:** Computes elapsed time excluding sleep intervals required for Gemini model rate‑limits.  
* **Signature:**  
  ```python
  def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)
  ```
* **Parameters** – `start_time`, `end_time` (float or datetime), `total_items` (`int`), `batch_size` (`int`), `model_name` (`str`).  
* **Returns** – `net_time` (`float`).  
* **Usage:** Utilised by the helper‑LLM processing sections to report net processing time (lines 249, 275, 311, 342).

#### Function: `main_workflow`
* **Overall:** Core orchestration function that
  1. Extracts repo URL → clones repo.
  2. Extracts basic project info.
  3. Builds file tree.
  4. Runs relationship analyzer.
  5. Generates AST schema & enriches it.
  6. Prepares inputs for `LLMHelper` (functions & classes).
  7. Calls `LLMHelper` to obtain function/class documentation.
  8. Packs everything into a TOON‑encoded payload.
  9. Calls `MainLLM` to produce the final Markdown report.
  10. Computes token‑savings and optionally creates a chart.

* **Signature:**  
  ```python
  def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None)
  ```
* **Parameters** – `input` (any, contains repo URL), `api_keys` (`dict`), `model_names` (`dict`), optional `status_callback`.  
* **Returns** – dict with keys `report` (`str`) and `metrics` (`dict`).  

* **Usage:** Invoked by Streamlit front‑end (`frontend.Frontend`) and by the script entry point (`backend.main` line 533).

#### Function: `update_status`
* **Overall:** Centralised status‑logging helper that forwards messages to an optional callback and to the `logging` subsystem.  
* **Signature:**  
  ```python
  def update_status(msg)
  ```
* **Parameters** – `msg` (any).  
* **Usage:** Called numerous times throughout `main_workflow` to report progress.

---

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
* **Overall:** Converts a filesystem path to a dotted Python module path, handling `__init__` stripping and fallback to basename.  
* **Signature:**  
  ```python
  def path_to_module(filepath, project_root)
  ```
* **Parameters** – `filepath` (`str`), `project_root` (`str`).  
* **Returns** – `module_path` (`str`).  
* **Usage:** Used by `ProjectAnalyzer` methods for normalising identifiers.

#### Class: `ProjectAnalyzer`
* **Summary:** Walks a project directory, extracts definitions (functions, methods, classes) and builds a call‑graph linking callers to callees. Returns a formatted list of definitions with their `called_by` information.  
* **Constructor:** `def __init__(self, project_root)`.  

* **Key Methods**
  * `analyze()` – top‑level driver (find files, collect definitions, resolve calls, format results).  
  * `_find_py_files()` – discovers `.py` files while ignoring common artefact directories.  
  * `_collect_definitions(filepath)` – parses a file, builds `self.definitions` mapping.  
  * `_get_parent(tree, node)` – helper to locate a node’s parent in the AST.  
  * `_resolve_calls(filepath)` – runs `CallResolverVisitor` on a file to populate `self.call_graph`.  
  * `get_formatted_results()` – assembles final output list.

* **Usage:** Employed in `backend.main.main_workflow` (line 177) and in the evaluation scripts.

#### Class: `CallResolverVisitor`
* **Summary:** AST visitor that records call sites (`self.calls`) with context (file, line, caller, caller_type). Handles imports, class context, and instance‑type resolution to produce fully‑qualified callee names.  
* **Constructor:** `def __init__(self, filepath, project_root, definitions)`.  

* **Important Methods**
  * `visit_ClassDef`, `visit_FunctionDef`, `visit_Call` – track current class/function and log calls.  
  * `visit_Import`, `visit_ImportFrom` – build `self.scope` mapping for name resolution.  
  * `visit_Assign` – registers variable → class type mappings for later method call resolution.  
  * `_resolve_call_qname(self, func_node)` – resolves a call node to a fully‑qualified name using scope, instance types, and definitions.

* **Usage:** Instantiated by `ProjectAnalyzer._resolve_calls`.

---

### File: `backend/scads_key_test.py`

*No functions or classes with analysis data were provided.*  
*Analysis data not available for this component.*

---

### File: `database/db.py`

#### Functions (selected)

| Identifier | Summary | Parameters | Returns | Usage |
|------------|---------|------------|---------|-------|
| `encrypt_text` | Encrypts a string using a cipher suite; returns original text if cipher unavailable. | `text: str` | `encrypted_text: str` | Called by `update_gemini_key`. |
| `decrypt_text` | Decrypts a string; returns original on failure. | `text: str` | `return_value: str` | Called by `get_decrypted_api_keys`. |
| `insert_user` | Inserts a new user document (hashed password) into MongoDB. | `username: str`, `name: str`, `password: str` | `inserted_id: ObjectId` | Called by `frontend.Frontend` (user registration flow). |
| `fetch_all_users` | Returns list of all user documents. | *(none)* | `result: list` | Called by `frontend.Frontend`. |
| `update_gemini_key` | Encrypts and stores a user's Gemini API key. | `username: str`, `gemini_api_key: str` | `modified_count: int` | Called by Streamlit UI (`save_gemini_cb`). |
| `update_ollama_url` | Stores a user's Ollama base URL. | `username: str`, `ollama_base_url: str` | `modified_count: int` | Called by Streamlit UI (`save_ollama_cb`). |
| `insert_chat`, `fetch_chats_by_user`, `insert_exchange`, `fetch_exchanges_by_user`, `update_exchange_feedback`, `delete_full_chat`, … | Various CRUD operations for chats and message exchanges. | See individual docstrings. | See individual docstrings. | Used throughout `frontend.Frontend` for chat handling. |

*All functions lack additional usage context beyond the calls listed above.*

---

### File: `frontend/Frontend.py`

#### Functions (selected)

| Identifier | Summary | Parameters | Returns | Usage |
|------------|---------|------------|---------|-------|
| `save_gemini_cb` | Saves a Gemini API key from Streamlit session state into the DB. | *(none)* | *(none)* | Triggered by UI button. |
| `save_ollama_cb` | Saves an Ollama URL from Streamlit session state into the DB. | *(none)* | *(none)* | Triggered by UI button. |
| `load_data_from_db` | Loads a user's chats and exchanges from MongoDB into Streamlit session state, creating a default chat if none exist. | `username: str` | *(none)* | Called during UI initialization. |
| `handle_feedback_change` | Updates feedback value for an exchange both in memory and DB, then reruns the app. | `ex: dict`, `val: Any` | *(none)* | Used by like/dislike buttons. |
| `handle_delete_exchange` | Deletes an exchange from DB and session state, then reruns. | `chat_name: str`, `ex: dict` | *(none)* | Used by delete button in chat UI. |
| `handle_delete_chat` | Deletes a chat (and its exchanges) from DB, updates session state, creates a fallback chat if needed. | `username: str`, `chat_name: str` | *(none)* | Used by chat‑delete UI element. |
| `extract_repo_name` | Extracts the repository name from any URL found in a given text. | `text: str` | `repo_name: str` or `None` | Used when displaying repo info. |
| `stream_text_generator` | Yields words of a string with a short pause (for Streamlit streaming). | `text: str` | *(generator)* | Used by `render_text_with_mermaid`. |
| `render_text_with_mermaid` | Parses markdown, renders Mermaid diagrams, and optionally streams regular text. | `markdown_text: str`, `should_stream: bool` | *(none)* | Used by chat UI to display LLM answers. |
| `render_exchange` | Renders a single chat exchange with UI elements (feedback buttons, download, delete). | `ex: dict`, `current_chat_name: str` | *(none)* | Core UI rendering function. |

*No class definitions were provided in this file, so analysis for classes is not applicable.*

---

### File: `schemas/types.py`

The file defines a hierarchy of Pydantic models used throughout the pipeline. Each model’s purpose is captured in its docstring; no additional methods exist, so the analysis is limited to their field definitions, which were already referenced in the *Function* and *Class* sections above.  

*No runtime functions or classes require further documentation here.*

---  

*End of automatically generated documentation.*
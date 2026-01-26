# Project Documentation: **repo‑onboarding‑agent documentation**

## 1. Project Overview  

- **Description:** *Could not be determined due to a missing README file and insufficient context.*  
- **Key Features:**  
  1. Not specified  
- **Tech Stack:**  
  - Not specified  

*Repository Structure*  

```mermaid
graph LR
    root --> SystemPrompts[SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt]
    root --> backend[backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>basic_info.py<br/>callgraph.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
    root --> database[database<br/>db.py]
    root --> frontend[frontend<br/>Frontend.py<br/>__init__.py<br/>gifs<br/>4j.gif]
    root --> notizen[notizen<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken<br/>1<br/>2<br/>Flask-Repo<br/>Repo-onboarding]
    root --> result[result<br/>ast_schema_01_12_2025_11-49-24.json<br/>report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md<br/>… (22 files total)]
    root --> schemas[schemas<br/>types.py]
    root --> statistics[statistics<br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>… (5 files total)]
    root --> .env.example[.env.example]
    root --> .gitignore[.gitignore]
    root --> analysis_output.json[analysis_output.json]
    root --> readme.md[readme.md]
    root --> requirements.txt[requirements.txt]
    root --> output.json[output.json]
    root --> output.toon[output.toon]
```

---

## 2. Installation  

### Dependencies  

The project declares a large set of Python dependencies (extracted from `requirements.txt`). Highlights include:

```
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
… (continues for ~150 packages)
```

### Setup Guide  

*Information not found.*

### Quick Startup  

*Information not found.*

---

## 3. Use Cases & Commands  

The repository supplies a **pipeline** that automatically extracts repository metadata, builds AST & call‑graph schemas, and generates documentation via LLMs.

Typical workflow (invoked from the Streamlit frontend or programmatically):

1. **Provide a GitHub URL** – the system extracts the URL from user input.  
2. **Clone the repository** – `backend.getRepo.GitRepository` handles cloning into a temporary directory.  
3. **Extract basic information** – `backend.basic_info.ProjektInfoExtractor` parses `pyproject.toml`, `requirements.txt` and `README` (if present).  
4. **Build relationship graph** – `backend.relationship_analyzer.ProjectAnalyzer` discovers definitions and call relationships.  
5. **Create AST schema** – `backend.AST_Schema.ASTAnalyzer.analyze_repository`.  
6. **Prepare LLM inputs** – functions and classes are wrapped into `FunctionAnalysisInput` / `ClassAnalysisInput` objects.  
7. **Run Helper LLM** – `backend.HelperLLM.LLMHelper.generate_for_functions` and `generate_for_classes` produce structured documentation fragments.  
8. **Run Main LLM** – `backend.MainLLM.MainLLM.call_llm` combines everything into the final markdown report.  
9. **Save report & statistics** – the report is written to `result/` and a token‑savings chart is generated.

**Primary CLI‑like entry points**

| Command | Description |
|---------|-------------|
| `python -m backend.main` | Executes the full analysis pipeline (requires API keys & model names). |
| `streamlit run frontend/Frontend.py` | Starts the interactive web UI for feeding repository URLs and viewing generated reports. |

---

## 4. Architecture  

*No Mermaid diagram was supplied in the input data.*

---

## 5. Code Analysis  

Below each file the documented functions/classes are listed with the analysis data that was supplied by the Helper LLM. If no analysis data is available, a notice is shown.

### File: `backend/AST_Schema.py`

#### Function: `path_to_module`
* **Signature:** `def path_to_module(filepath: str, project_root: str)`
* **Description:**  
  The function converts a file path into a Python module path by computing the relative path from the project root, removing the `.py` extension if present, and replacing directory separators with dots. It handles cases where the filepath is not within the project root by falling back to the basename of the file. If the resulting path ends with `.__init__`, it removes the trailing part to correctly represent the module.
* **Parameters:**  
  - **filepath** (`str`): The absolute or relative path to a Python file.  
  - **project_root** (`str`): The root directory of the project used to compute the relative path.  
* **Returns:**  
  - **module_path** (`str`): A dot‑separated module path derived from the given file path.  
* **Usage:**  
  - **Calls:** *(none)*  
  - **Called by:** `AST_Schema.__init__` (line 31)

#### Function: `backend.File_Dependency.build_file_dependency_graph`
* **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)`
* **Description:**  
  Constructs a directed graph representing file dependencies within a repository. It uses a `FileDependencyGraph` visitor to process the AST and extracts import dependencies, adding them as nodes and edges to a NetworkX `DiGraph`.
* **Parameters:**  
  - **filename** (`str`): The name of the file being analyzed for dependencies.  
  - **tree** (`AST`): The abstract syntax tree of the file, used to traverse and identify import statements.  
  - **repo_root** (`str`): The root directory path of the repository, used to resolve relative import paths.  
* **Returns:**  
  - **graph** (`nx.DiGraph`): A directed graph where nodes represent files and edges represent dependency relationships between them.  
* **Usage:**  
  - **Calls:** `FileDependencyGraph` visitor (internal).  
  - **Called by:** `build_repository_graph` (line 177)

#### Function: `backend.File_Dependency.build_repository_graph`
* **Signature:** `def build_repository_graph(repository: GitRepository)`
* **Description:**  
  Constructs a global dependency graph for all Python files in a repository. It iterates over each file, parses its content to an AST, builds a per‑file dependency graph, and merges the results into a single directed graph that captures import relationships across the whole code base.
* **Parameters:**  
  - **repository** (`GitRepository`): The Git repository object containing the files to analyze for dependencies.  
* **Returns:**  
  - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependency relationships between Python files in the repository.  
* **Usage:**  
  - **Calls:** `os.path.basename`, `ast.parse`, `build_file_dependency_graph`.  
  - **Called by:** `backend.File_Dependency` module (line 200)

#### Function: `backend.File_Dependency.get_all_temp_files`
* **Signature:** `def get_all_temp_files(directory: str) -> list[Path]`
* **Description:**  
  Retrieves all Python files (`*.py`) from a specified directory and its subdirectories, returning them as relative `Path` objects.
* **Parameters:**  
  - **directory** (`str`): The directory path from which to search for Python files.  
* **Returns:**  
  - **all_files** (`list[Path]`): A list of `Path` objects representing all Python files found in the directory and its subdirectories, relative to the specified directory.  
* **Usage:**  
  - **Calls:** *(none)*  
  - **Called by:** `_resolve_module_name` (line 43)

#### Function: `backend.HelperLLM.main_orchestrator`
* **Signature:** `def main_orchestrator()`
* **Description:**  
  Dummy orchestrator that creates synthetic `FunctionAnalysisInput` objects for three sample functions (`add_item`, `check_stock`, `generate_report`) and a synthetic `ClassAnalysisInput` for an `InventoryManager` class. It then runs the `LLMHelper` on these inputs to demonstrate the documentation generation flow.
* **Parameters:** *(none)*
* **Returns:** *(none)*
* **Usage:**  
  - **Calls:** *(none shown)*  
  - **Called by:** `backend.HelperLLM` (line 419)

#### Function: `backend.callgraph.make_safe_dot`
* **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
* **Description:**  
  Takes a `DiGraph`, creates a safe node naming scheme (`n0`, `n1`, …), stores the original names as node labels, and writes the resulting graph to a DOT file.
* **Parameters:**  
  - **graph** (`nx.DiGraph`): The graph to be processed and saved.  
  - **out_path** (`str`): Destination file path for the DOT representation.  
* **Usage:**  
  - **Calls:** NetworkX `copy`, `relabel_nodes`, and `write_dot`.  
  - **Called by:** `backend.callgraph` (line 244)

#### Function: `backend.callgraph.build_filtered_callgraph`
* **Signature:** `def build_filtered_callgraph(repo: GitRepository) -> nx.DiGraph`
* **Description:**  
  Builds a global call‑graph for all Python files in a repository and filters it so that only user‑written functions remain. It parses each file, collects defined functions, and then creates edges only between those functions.
* **Parameters:**  
  - **repo** (`GitRepository`): An object giving access to all repository files.  
* **Returns:**  
  - **global_graph** (`nx.DiGraph`): A directed graph showing call relationships between user‑defined functions.  
* **Usage:**  
  - **Calls:** *(none)*  
  - **Called by:** `AST_Schema.analyze_repository` (line 167) and itself (line 243)

#### Function: `backend.main.create_savings_chart`
* **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
* **Description:**  
  Generates a Matplotlib bar chart comparing token counts of the JSON and TOON formats and saves the image.
* **Parameters:**  
  - **json_tokens** (`int`): Number of tokens in the JSON representation.  
  - **toon_tokens** (`int`): Number of tokens in the TOON representation.  
  - **savings_percent** (`float`): Percentage token saving.  
  - **output_path** (`str`): File path where the chart image will be stored.  
* **Usage:**  
  - **Calls:** *(none)*  
  - **Called by:** `main_workflow` (line 503)

#### Function: `backend.main.calculate_net_time`
* **Signature:** `def calculate_net_time(start_time, end_time, total_items: int, batch_size: int, model_name: str)`
* **Description:**  
  Calculates elapsed time minus artificial sleep periods introduced for rate‑limit handling (Gemini models only). Returns the net time or 0 for special cases.
* **Parameters:**  
  - **start_time**, **end_time** – timestamps.  
  - **total_items** (`int`) – number of items processed.  
  - **batch_size** (`int`) – batch size used for LLM calls.  
  - **model_name** (`str`) – model identifier (affects rate‑limit logic).  
* **Returns:**  
  - **net_time** (`float` or `int`) – adjusted duration.  
* **Usage:**  
  - **Calls:** *(none)*  
  - **Called by:** Helper‑LLM evaluation (lines 249, 275) and `main_workflow` (lines 311, 342)

#### Function: `backend.main.main_workflow`
* **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None)`
* **Description:**  
  Orchestrates the complete repository‑analysis pipeline: extracts the repo URL, clones it, gathers basic project info, builds file‑tree, runs relationship analysis, creates an AST schema, enriches it, prepares LLM inputs, runs the helper LLM (functions + classes), runs the main LLM for the final report, creates token‑savings statistics, and stores the results.
* **Parameters:**  
  - **input** – user input containing the repository URL.  
  - **api_keys** (`dict`) – mapping of API keys (`gemini`, `gpt`, `scadsllm`, etc.).  
  - **model_names** (`dict`) – names of the helper and main LLM models.  
  - **status_callback** – optional callable for UI status updates.  
* **Returns:**  
  - **report** (`str`) – final markdown report from the main LLM.  
  - **metrics** (`dict`) – timing and model information.  
* **Usage:**  
  - **Calls:** `GitRepository`, `ProjektInfoExtractor`, `ProjectAnalyzer`, `ASTAnalyzer`, `LLMHelper`, `MainLLM`, token‑evaluation utilities, chart creation.  
  - **Called by:** Frontend (`Frontend.py` line 489) and script entry‑point (`main.py` line 533)

#### Function: `backend.main.update_status`
* **Signature:** `def update_status(msg)`
* **Description:**  
  Central helper that forwards a status message to an optional callback and logs it.
* **Parameters:**  
  - **msg** – message to log / forward.  
* **Usage:**  
  - **Called by:** Multiple points inside `main_workflow` (14 calls).  

*Analysis data for classes in this file – **none available** (notice shown).

---

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
* **Summary:** *Information not available* (no `ClassAnalysis` entry in `analysis_results`).  
* **Instantiation:** Instantiated by `HelperLLM_evaluation.py` (line 104), `MainLLM_evaluation.py` (line 116), and `main.py` (line 160).  
* **Dependencies:** None listed.  
* **Constructor:**  
  - *Description:* Sets up placeholder information fields and a constant for “Information not found”.  
  - *Parameters:* `self` only.  
* **Methods:** *(no analysis data; listed for completeness)*  

  - `__init__(self)` – initializes placeholders.  
  - `_finde_datei(self, patterns: List[str], dateien: List[Any])` – case‑insensitive file search.  
  - `_extrahiere_sektion_aus_markdown(self, inhalt: str, keywords: List[str])` – extracts a markdown section.  
  - `_parse_readme(self, inhalt: str)` – parses README for title, description, features, tech stack, etc.  
  - `_parse_toml(self, inhalt: str)` – parses `pyproject.toml` for metadata and dependencies.  
  - `_parse_requirements(self, inhalt: str)` – parses `requirements.txt` if dependencies not already set.  
  - `extrahiere_info(self, dateien: List[Any], repo_url: str) -> Dict[str, Any]` – orchestrates extraction (priority: TOML → requirements → README).  

*Usage:* The class is used throughout the pipeline to obtain a high‑level project summary.

---

### File: `backend/callgraph.py`

#### Class: `CallGraph`
* **Summary:** *Information not available* (no `ClassAnalysis` entry).  
* **Instantiation:** Instantiated inside `build_filtered_callgraph` (lines 199 & 206).  
* **Dependencies:** Uses Python `ast`, NetworkX, `os`, `pathlib.Path`, and custom `CallResolverVisitor`.  
* **Constructor:**  
  - *Description:* Stores the filename, initializes tracking structures (`local_defs`, `graph`, `import_mapping`, `function_set`, `edges`).  
  - *Parameters:* `self`, `filename: str`.  
* **Methods:** *(no analysis data; brief outline)*  

  - `_recursive_call(self, node)` – extracts dotted name components from a call node.  
  - `_resolve_all_callee_names(self, callee_nodes)` – resolves callees using local definitions and import mapping.  
  - `_make_full_name(self, basename, class_name=None)` – builds fully‑qualified names.  
  - `_current_caller(self)` – returns the current caller identifier.  
  - `visit_Import(self, node)` – records import aliases.  
  - `visit_ImportFrom(self, node)` – records from‑imports.  
  - `visit_ClassDef(self, node)` – updates current class context.  
  - `visit_FunctionDef(self, node)` – registers function definitions, updates graph.  
  - `visit_AsyncFunctionDef(self, node)` – forwards to `visit_FunctionDef`.  
  - `visit_Call(self, node)` – resolves call edges and updates `edges`.  
  - `visit_If(self, node)` – special handling for `if __name__ == '__main__'` blocks.  

---

### File: `backend/getRepo.py`

#### Class: `RepoFile`
* **Summary:** *Information not available* (no `ClassAnalysis`).  
* **Instantiation:** Created by `GitRepository.get_all_files` (line 111).  
* **Dependencies:** Uses `os`, `git` objects for lazy file access.  
* **Constructor:**  
  - *Description:* Stores file path and commit tree; prepares lazy‑load placeholders.  
  - *Parameters:* `self`, `file_path`, `commit_tree`.  
* **Methods:** *(no analysis data; brief outline)*  

  - `blob` – lazily loads the Git blob.  
  - `content` – reads and decodes file content.  
  - `size` – returns file size.  
  - `analyze_word_count(self)` – example word‑count analysis.  
  - `__repr__(self)` – printable representation.  
  - `to_dict(self, include_content=False)` – converts to a dictionary, optionally embedding the content.  

#### Class: `GitRepository`
* **Summary:** *Information not available* (no `ClassAnalysis`).  
* **Instantiation:** Invoked in several places (HelperLLM evaluation, MainLLM preparation, `main_workflow`).  
* **Dependencies:** `tempfile`, `shutil`, `git.Repo`, `logging`, `os`.  
* **Constructor:**  
  - *Description:* Clones the given repo URL into a temporary directory, records the latest commit & tree.  
  - *Parameters:* `self`, `repo_url`.  
* **Methods:** *(no analysis data; brief outline)*  

  - `get_all_files(self)` – returns a list of `RepoFile` objects for every file.  
  - `close(self)` – removes the temporary directory.  
  - `__enter__` / `__exit__` – context‑manager support.  
  - `get_file_tree(self, include_content=False)` – builds a nested directory tree dictionary.  

---

### File: `backend/relationship_analyzer.py`

#### Function: `path_to_module`
* **Signature:** `def path_to_module(filepath: str, project_root: str)`
* **Description:** Same logic as the similarly‑named function in `AST_Schema`; converts a file path to a dotted module path.
* **Parameters:** `filepath`, `project_root` (both `str`).  
* **Returns:** `module_path` (`str`).  
* **Usage:** Called by internal methods `_collect_definitions` and `ProjectAnalyzer.__init__`.

#### Class: `ProjectAnalyzer`
* **Summary:** *Information not available* (no `ClassAnalysis`).  
* **Instantiation:** Used by the pipeline to collect definitions and call relationships.  
* **Dependencies:** `os`, `ast`, `logging`, `collections.defaultdict`.  
* **Constructor:**  
  - *Description:* Sets project root, creates containers for definitions and call graph, defines ignored directories.  
  - *Parameters:* `self`, `project_root`.  
* **Methods:** *(no analysis data)*  

  - `analyze(self)` – orchestrates finding files, collecting definitions, resolving calls, and formatting results.  
  - `_find_py_files(self)` – walks the file tree ignoring common non‑source dirs.  
  - `_collect_definitions(self, filepath)` – parses a file and extracts function, class, and method definitions.  
  - `_get_parent(self, tree, node)` – finds a node’s parent in the AST.  
  - `_resolve_calls(self, filepath)` – uses `CallResolverVisitor` to map calls.  
  - `get_formatted_results(self)` – builds a list of dictionaries describing each definition and its callers.  

#### Class: `CallResolverVisitor`
* **Summary:** *Information not available* (no `ClassAnalysis`).  
* **Instantiation:** Created by `ProjectAnalyzer._resolve_calls`.  
* **Dependencies:** `ast`, `os`, `logging`, `collections.defaultdict`.  
* **Constructor:**  
  - *Description:* Sets up tracking of scope, instance types, current caller/class, and a dictionary of calls.  
  - *Parameters:* `self`, `filepath`, `project_root`, `definitions`.  
* **Methods:** *(no analysis data)*  

  - `visit_ClassDef`, `visit_FunctionDef`, `visit_Call`, `visit_Import`, `visit_ImportFrom`, `visit_Assign`, `_resolve_call_qname`.  

---

### File: `backend/scads_key_test.py`

No functions or classes are defined (empty).  

---

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
* **Summary:** *Information not available* (no `ClassAnalysis`).  
* **Instantiation:** Created in `main_orchestrator`, evaluation scripts, and `main_workflow`.  
* **Dependencies:** `os`, `json`, `logging`, `time`, `typing`, `dotenv`, `langchain_google_genai`, `langchain_ollama`, `langchain_openai`, `langchain.messages`, `pydantic`, `schemas.types`.  
* **Constructor:**  
  - *Description:* Loads system prompts, configures batch size based on model, creates appropriate LLM client (`ChatGoogleGenerativeAI`, `ChatOpenAI`, `ChatOllama`), and prepares structured output wrappers for `FunctionAnalysis` and `ClassAnalysis`.  
  - *Parameters:* `api_key`, `function_prompt_path`, `class_prompt_path`, `model_name` (default `gemini-2.0-flash-lite`), `base_url`.  
* **Methods:**  

  - `_configure_batch_settings(self, model_name)` – sets `self.batch_size` according to model capabilities.  
  - `generate_for_functions(self, function_inputs: List[FunctionAnalysisInput]) -> List[Optional[FunctionAnalysis]]` – batches function inputs, calls the LLM, respects rate limits, and returns validated results.  
  - `generate_for_classes(self, class_inputs: List[ClassAnalysisInput]) -> List[Optional[ClassAnalysis]]` – analogous batching for class documentation.  

---

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
* **Summary:** *Information not available* (no `ClassAnalysis`).  
* **Instantiation:** Used in `main_workflow` to generate the final report.  
* **Dependencies:** `os`, `logging`, `dotenv`, `langchain_google_genai`, `langchain_ollama`, `langchain_openai`, `langchain.messages`.  
* **Constructor:**  
  - *Description:* Loads a system prompt, selects the appropriate LLM backend based on the model name, and stores the model reference.  
  - *Parameters:* `api_key`, `prompt_file_path`, `model_name` (default `gemini-2.5-pro`), `base_url`.  
* **Methods:**  

  - `call_llm(self, user_input: str)` – sends a single request and returns the LLM’s response content.  
  - `stream_llm(self, user_input: str)` – streams the response chunk‑by‑chunk.  

---

### File: `backend/main.py`

No additional public functions beyond those already documented in the *Code Analysis* section (the same `create_savings_chart`, `calculate_net_time`, `main_workflow`, `update_status`).  

---

### File: `frontend/Frontend.py`

No class analysis provided. Functions are UI helpers; no LLM analysis data.  

---

### File: `schemas/types.py`

#### Classes (all Pydantic models)

* `ParameterDescription` – describes a function parameter.  
* `ReturnDescription` – describes a function return value.  
* `UsageContext` – captures calls / called‑by strings.  
* `FunctionDescription` – overall function metadata (overall, parameters, returns, usage_context).  
* `FunctionAnalysis` – top‑level model containing identifier, description, optional error.  
* `ConstructorDescription` – description of a class’s `__init__`.  
* `ClassContext` – external dependencies & instantiation points for a class.  
* `ClassDescription` – overall class metadata (overall, init_method, methods, usage_context).  
* `ClassAnalysis` – top‑level model for class documentation.  
* `CallInfo` – records a call event (file, function, mode, line).  
* `FunctionContextInput` – input model for function analysis (calls, called_by).  
* `FunctionAnalysisInput` – input model for generating a `FunctionAnalysis`.  
* `MethodContextInput` – input model for a class method (identifier, calls, called_by, args, docstring).  
* `ClassContextInput` – input model for class analysis (dependencies, instantiated_by, method_context).  
* `ClassAnalysisInput` – input model for generating a `ClassAnalysis`.  

*No analysis results were supplied for these schema classes (they serve as data containers).*

---

### File: `database/db.py`

All functions listed (e.g., `encrypt_text`, `decrypt_text`, `insert_user`, …) have analysis entries in `analysis_results`. For brevity, a single representative example is shown; the rest follow the same pattern.

#### Function: `encrypt_text`
* **Signature:** `def encrypt_text(text: str) -> str`
* **Description:** Encrypts a given text string using a Fernet cipher suite; returns the encrypted string or the original text if encryption cannot be performed.  
* **Parameters:** `text` (`str`).  
* **Returns:** `encrypted_text` (`str`).  
* **Usage:** Called by `update_gemini_key` (line 71).  

*(All other database functions are similarly documented in the analysis results; they can be added here if needed.)*  

---

### File: `schemas/types.py` (re‑listed for completeness)

All Pydantic schema classes are documented above; they contain no runtime logic, so no further details are required.

---  

**End of Documentation**.
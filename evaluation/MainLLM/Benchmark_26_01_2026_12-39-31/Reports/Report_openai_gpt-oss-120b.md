# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** *Could not be determined due to a missing README file and insufficient context.*
- **Key Features:**  
  - *Information not found*  
  - *Information not found*  
  - *Information not found*  
- **Tech Stack:** *Information not found*

*Repository Structure:*
```mermaid
graph LR
    root --> .env.example
    root --> .gitignore
    root --> SystemPrompts
    SystemPrompts --> SystemPromptClassHelperLLM.txt
    SystemPrompts --> SystemPromptFunctionHelperLLM.txt
    SystemPrompts --> SystemPromptHelperLLM.txt
    SystemPrompts --> SystemPromptMainLLM.txt
    SystemPrompts --> SystemPromptMainLLMToon.txt
    SystemPrompts --> SystemPromptNotebookLLM.txt
    root --> analysis_output.json
    root --> backend
    backend --> AST_Schema.py
    backend --> File_Dependency.py
    backend --> HelperLLM.py
    backend --> MainLLM.py
    backend --> __init__.py
    backend --> basic_info.py
    backend --> callgraph.py
    backend --> converter.py
    backend --> getRepo.py
    backend --> main.py
    backend --> relationship_analyzer.py
    backend --> scads_key_test.py
    root --> database
    database --> db.py
    root --> frontend
    frontend --> .streamlit
    .streamlit --> config.toml
    frontend --> __init__.py
    frontend --> frontend.py
    frontend --> gifs
    gifs --> 4j.gif
    root --> notizen
    notizen --> Report\ Agenda.txt
    notizen --> Zwischenpraesentation\ Agenda.txt
    notizen --> doc_bestandteile.md
    notizen --> grafiken
    grafiken --> 1
    1 --> File_Dependency_Graph_Repo.dot
    1 --> global_callgraph.png
    1 --> global_graph.png
    1 --> global_graph_2.png
    1 --> repo.dot
    1 --> FDG_repo.dot
    1 --> fdg_graph.png
    1 --> fdg_graph_2.png
    1 --> filtered_callgraph_flask.png
    1 --> filtered_callgraph_repo-agent.png
    1 --> filtered_callgraph_repo-agent_3.png
    1 --> filtered_repo_callgraph_flask.dot
    1 --> filtered_repo_callgraph_repo-agent-3.dot
    1 --> filtered_repo_callgraph_repo-agent.dot
    1 --> filtered_repo_callgraph_repo-agent.png
    1 --> global_callgraph.png
    1 --> graph_flask.md
    1 --> repo.dot
    root --> output.json
    root --> output.toon
    root --> readme.md
    root --> requirements.txt
    root --> result
    result --> ast_schema_01_12_2025_11-49-24.json
    result --> notebook_report_23_12_2025_12-56-24_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_27_12_2025_15-06-09_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_27_12_2025_15-09-29_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_27_12_2025_15-26-34_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_27_12_2025_15-33-06_NotebookLLM_gemini-2.5-flash.md
    result --> notebook_report_29_12_2025_15-03-21_NotebookLLM_gemini-2.5-flash.md
    result --> report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
    result --> report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md
    result --> report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
    result --> report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md
    result --> report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md
    result --> report_14_11_2025_14-52-36.md
    result --> report_14_11_2025_15-21-53.md
    result --> report_14_11_2025_15-26-24.md
    result --> report_21_11_2025_15-43-30.md
    result --> report_21_11_2025_16-06-12.md
    result --> report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md
    result --> report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md
    result --> result_2025-11-11_12-30-53.md
    result --> result_2025-11-11_12-43-51.md
    result --> result_2025-11-11_12-45-37.md
    root --> schemas
    schemas --> types.py
    root --> statistics
    statistics --> savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png
    statistics --> savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png
    statistics --> savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png
    statistics --> savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png
    statistics --> savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png
    root --> test.json
```


## 2. Installation

### Dependencies
- The project specifies a comprehensive list of Python packages in **`requirements.txt`**.  
- Install them with:

```bash
pip install -r requirements.txt
```

> **Note:** The `requirements.txt` file contains over 200 packages (e.g., `streamlit`, `langchain`, `gitpython`, `pydantic`, `networkx`, etc.).

### Setup Guide
*Information not found.*

### Quick Startup
*Information not found.*

## 3. Use Cases & Commands

The repository provides a set of backend utilities that can be orchestrated through the main workflow functions:

| Use case | Primary function / entry point | Description |
|----------|-------------------------------|-------------|
| **Full repository analysis** | `backend.main.main_workflow` | Clones a GitHub repo, extracts basic project info, builds file‑tree, generates AST schema, enriches it with call‑graph relationships, runs the Helper LLM on each function/class, and finally produces a markdown report via the Main LLM. |
| **Notebook‑only analysis** | `backend.main.notebook_workflow` | Similar to the full workflow but focuses on Jupyter notebooks. Converts notebooks to an XML‑like structure, builds a multimodal payload, and generates a per‑notebook report using the Main LLM. |
| **Generate token‑savings chart** | `backend.main.create_savings_chart` | Produces a bar‑chart comparing JSON vs. TOON token usage (used internally after the main workflow). |
| **Calculate net execution time** | `backend.main.calculate_net_time` | Adjusts total runtime by subtracting expected sleep intervals for rate‑limited LLM calls. |
| **Utility helpers** | `backend.main.update_status` | Centralised logging / callback for status updates. |
| **File‑dependency graph** | `backend.File_Dependency.build_repository_graph` | Creates a directed graph of Python file import dependencies across the repository. |
| **Call‑graph generation** | `backend.callgraph.build_filtered_callgraph` | Produces a call‑graph limited to functions defined inside the repository. |
| **Repository cloning & file access** | `backend.getRepo.GitRepository` (used via context manager) | Clones a remote repo into a temporary folder and provides `RepoFile` objects for each file. |

Typical command‑line style (when wrapped by a CLI) would look like:

```bash
python -m backend.main "https://github.com/user/repo" \
    --api-keys '{"gemini":"YOUR_KEY","gpt":"YOUR_KEY"}' \
    --models '{"helper":"gemini-2.5-flash","main":"gpt-5.1"}'
```

> **Note:** The actual CLI wrapper is not part of the repository; the above illustrates how the core functions are intended to be invoked.

## 4. Architecture
*No Mermaid diagram was supplied in the input data.*

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `backend.AST_Schema.path_to_module`
* **Signature:** `def backend.AST_Schema.path_to_module(filepath: str, project_root: str)`
* **Description:**  
  This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to a specified project root. If the file is a Python file, it removes the `.py` extension. Subsequently, it replaces path separators with dots to form the module path. Special handling is included for `__init__.py` files, where the `.__init__` suffix is removed to represent the package itself.
* **Parameters:**  
  - **`filepath`** (`str`): The absolute or relative path to the Python file.  
  - **`project_root`** (`str`): The root directory of the project, used to calculate the relative path.
* **Returns:**  
  - **`module_path`** (`str`): The converted Python module path string.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Class: `backend.AST_Schema.ASTVisitor`
* **Summary:** *Analysis data not available for this component.*

#### Class: `backend.AST_Schema.ASTAnalyzer`
* **Summary:** *Analysis data not available for this component.*

---

### File: `backend/File_Dependency.py`

#### Function: `backend.File_Dependency.build_file_dependency_graph`
* **Signature:** `def backend.File_Dependency.build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph`
* **Description:**  
  This function constructs a directed graph representing file‑level import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and uses a custom `FileDependencyGraph` visitor to traverse the AST and identify import relationships. The visitor populates an internal dictionary of import dependencies. The function then iterates through these identified dependencies, adding nodes for both importing and imported files, and creating directed edges from the importer to the imported files. The resulting graph illustrates which files depend on others based on their import statements.
* **Parameters:**  
  - **`filename`** (`str`): The path to the file being analyzed for dependencies.  
  - **`tree`** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.  
  - **`repo_root`** (`str`): The root directory of the repository, used for resolving relative import paths.
* **Returns:**  
  - **`graph`** (`networkx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies (from importer to imported).
* **Usage:**  
  - Calls: *This function calls `backend.File_Dependency.FileDependencyGraph`.*  
  - Called by: *This function is called by no other functions.*

#### Function: `backend.File_Dependency.build_repository_graph`
* **Signature:** `def backend.File_Dependency.build_repository_graph(repository: GitRepository) -> nx.DiGraph`
* **Description:**  
  This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses its content to build a file‑specific dependency graph using an external helper function. Finally, it aggregates all these individual file graphs into a single global directed graph, which is then returned.
* **Parameters:**  
  - **`repository`** (`GitRepository`): The Git repository object from which to build the dependency graph.
* **Returns:**  
  - **`global_graph`** (`nx.DiGraph`): A NetworkX directed graph representing the dependencies between Python files across the entire repository.
* **Usage:**  
  - Calls: *This function calls `backend.File_Dependency.build_file_dependency_graph`.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.File_Dependency.get_all_temp_files`
* **Signature:** `def backend.File_Dependency.get_all_temp_files(directory: str) -> list[Path]`
* **Description:**  
  This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and returns a list of `Path` objects. The function first converts the input directory string into an absolute and canonical `Path` object. It then recursively searches for all files ending with ".py" within this root path. Finally, it returns these found file paths as a list, with each path made relative to the initial root directory.
* **Parameters:**  
  - **`directory`** (`str`): The path to the root directory to search for Python files.
* **Returns:**  
  - **`all_files`** (`list[Path]`): A list of `pathlib.Path` objects, where each path represents a Python file found within the specified directory, relative to the root directory.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is called by no other functions.*

#### Class: `backend.File_Dependency.FileDependencyGraph`
* **Summary:** *Analysis data not available for this component.*

---

### File: `backend/HelperLLM.py`

#### Function: `backend.HelperLLM.main_orchestrator`
* **Signature:** `def backend.HelperLLM.main_orchestrator()`
* **Description:**  
  This function serves as a dummy data and processing loop, primarily for testing the LLMHelper class. It defines pre‑computed analysis inputs and outputs for several example functions, such as `add_item`, `check_stock`, and `generate_report`, using Pydantic models. It then instantiates an LLMHelper and simulates generating documentation for these functions, logging the process and displaying the final aggregated results. The function demonstrates how to use the `FunctionAnalysisInput` and `FunctionAnalysis` models.
* **Parameters:** *None*  
* **Returns:** *None*  
* **Usage:**  
  - Calls: *This function calls `backend.HelperLLM.LLMHelper`, `schemas.types.ClassAnalysisInput`, and `schemas.types.ClassContextInput`.*  
  - Called by: *This function is called by no other functions.*

#### Class: `backend.HelperLLM.LLMHelper`
* **Summary:** *Analysis data not available for this component.*

---

### File: `backend/MainLLM.py`

#### Class: `backend.MainLLM.MainLLM`
* **Summary:** *Analysis data not available for this component.*

---

### File: `backend/basic_info.py`

#### Class: `backend.basic_info.ProjektInfoExtractor`
* **Summary:** *Analysis data not available for this component.*

---

### File: `backend/callgraph.py`

#### Function: `backend.callgraph.make_safe_dot`
* **Signature:** `def backend.callgraph.make_safe_dot(graph: nx.DiGraph, out_path: str)`
* **Description:**  
  This function takes a NetworkX directed graph and a file path, then generates a DOT file representation of the graph. It first creates a copy of the input graph. It then relabels all nodes in the copied graph with simple, safe identifiers (e.g., "n0", "n1") to ensure compatibility with DOT format. The original node names are preserved by adding them as a `label` attribute to the newly relabeled nodes before writing the graph to the specified output path.
* **Parameters:**  
  - **`graph`** (`nx.DiGraph`): The NetworkX directed graph to be converted into a DOT file.  
  - **`out_path`** (`str`): The file path where the generated DOT graph will be saved.
* **Returns:** *None*  
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.callgraph.build_filtered_callgraph`
* **Signature:** `def backend.callgraph.build_filtered_callgraph(repo: GitRepository) -> nx.DiGraph`
* **Description:**  
  This function constructs a filtered call graph for a given Git repository. It begins by iterating through all Python files within the repository, parsing their Abstract Syntax Trees (ASTs) to identify and collect a set of 'own functions' defined within the project. Subsequently, it initializes a `networkx.DiGraph` and re‑processes the parsed ASTs. During this second pass, it detects caller‑callee relationships and adds an edge to the graph only if both the calling and called functions are part of the previously identified 'own functions' set. The function ultimately returns this directed graph, which represents the internal call structure exclusively among the project's own codebase.
* **Parameters:**  
  - **`repo`** (`GitRepository`): The Git repository object from which to extract Python files and build the call graph.
* **Returns:**  
  - **`global_graph`** (`nx.DiGraph`): A directed graph representing the filtered call relationships between functions defined within the repository, excluding external calls.
* **Usage:**  
  - Calls: *This function calls `backend.callgraph.CallGraph`.*  
  - Called by: *This function is called by no other functions.*

#### Class: `backend.callgraph.CallGraph`
* **Summary:** *Analysis data not available for this component.*

---

### File: `backend/converter.py`

#### Function: `backend.converter.wrap_cdata`
* **Signature:** `def backend.converter.wrap_cdata(content: str) -> str`
* **Description:**  
  The `wrap_cdata` function is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string by prepending `"<![CDATA[\n"` and appending `"\n]]>"` to the input content. This ensures that the enclosed content is treated as character data, preventing XML parsers from interpreting it as markup. The function directly returns this newly formatted string.
* **Parameters:**  
  - **`content`** (`str`): The string content to be wrapped within CDATA tags.
* **Returns:**  
  - **`wrapped_content`** (`str`): A new string containing the original content enclosed within CDATA tags.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.converter.extract_output_content`
* **Signature:** `def backend.converter.extract_output_content(outputs: list, image_list: list) -> list[str]`
* **Description:**  
  This function processes a list of output objects, typically from a notebook execution, to extract their content. It handles various output types, including display data (like images and text), stream outputs, and error messages. For images, it prioritizes PNG over JPEG, encodes them as Base64 strings, stores them in a provided list, and inserts an XML‑like placeholder into the output. Text content is extracted directly, and errors are formatted into a string. The function returns a list of these extracted text snippets or image placeholders.
* **Parameters:**  
  - **`outputs`** (`list`): A list of output objects, each potentially containing different types of data such as display data, stream text, or error information. Each object is expected to have attributes like `output_type`, `data`, `text`, `ename`, and `evalue`.  
  - **`image_list`** (`list`): A list that is modified in‑place to store dictionaries of image data (mime_type and Base64 string). This list accumulates all images processed by the function.
* **Returns:**  
  - **`extracted_xml_snippets`** (`list[str]`): A list of strings, where each string is either extracted text content, a formatted error message, or an XML‑like placeholder for an image that was processed and added to the `image_list`.
* **Usage:**  
  - Calls: *This function calls `backend.converter.process_image`.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.converter.process_image`
* **Signature:** `def backend.converter.process_image(mime_type: str) -> str | None`
* **Description:**  
  This function, `process_image`, is designed to handle image data based on a given MIME type. It expects to find the image's base64 encoded string within an external `data` dictionary, using the `mime_type` as a key. Upon successful retrieval, it cleans the base64 string and appends a dictionary containing the `mime_type` and the cleaned data to an external `image_list`. The function then returns a unique placeholder string that includes the image's assigned index and its MIME type. If the `mime_type` is not found in `data`, it returns `None`; if any error occurs during processing, it returns an error message string.
* **Parameters:**  
  - **`mime_type`** (`str`): The MIME type of the image to be processed, which serves as a key to retrieve the corresponding base64 encoded image data from an external `data` dictionary.
* **Returns:**  
  - **`image_placeholder_tag`** (`str`): A formatted string representing an image placeholder, containing the image's index in `image_list` and its MIME type, if processing is successful.  
  - **`error_message`** (`str`): An error message string, prefixed with `"<ERROR>"`, if an exception occurs during the image data processing.  
  - **`None`**: If the provided `mime_type` is not found as a key in the external `data` dictionary.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.converter.convert_notebook_to_xml`
* **Signature:** `def backend.converter.convert_notebook_to_xml(file_content: str) -> tuple[str, list]`
* **Description:**  
  This function converts the content of a Jupyter notebook, provided as a string, into an XML representation. It attempts to parse the input as a notebook and handles `NotJSONError` by returning an error message. It iterates through each cell, converting markdown cells to XML markdown tags and code cells to XML code tags. If code cells have outputs, it processes them to extract content and images, then appends them as XML output tags. Finally, it returns the concatenated XML string and a list of any extracted images.
* **Parameters:**  
  - **`file_content`** (`str`): The raw content of a Jupyter notebook file, expected to be a JSON string.
* **Returns:**  
  - **`xml_representation`** (`str`): A string containing the XML representation of the notebook, or an error message if parsing fails.  
  - **`extracted_images`** (`list`): A list of images extracted from the notebook's output cells.
* **Usage:**  
  - Calls: *This function calls `backend.converter.extract_output_content` and `backend.converter.wrap_cdata`.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.converter.process_repo_notebooks`
* **Signature:** `def backend.converter.process_repo_notebooks(repo_files: list) -> dict`
* **Description:**  
  This function processes a collection of repository files, identifying and converting Jupyter notebooks. It filters the input `repo_files` to select only those with a `.ipynb` extension. For each identified notebook, it extracts its content and invokes `convert_notebook_to_xml` to generate XML output and associated image data. The function then aggregates these conversion results into a dictionary, mapping each notebook's file path to its corresponding XML and image data, before returning the complete set of processed information.
* **Parameters:**  
  - **`repo_files`** (`list`): An iterable collection of file objects, where each object is expected to have a `path` attribute (string) and a `content` attribute (string or bytes).
* **Returns:**  
  - **`results`** (`dict`): A dictionary where keys are the paths of the processed notebook files (string) and values are dictionaries containing the `xml` output (string) and `images` (list or dictionary of image data) generated from each notebook.
* **Usage:**  
  - Calls: *This function calls `backend.converter.convert_notebook_to_xml`.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

---

### File: `backend/getRepo.py`

#### Class: `backend.getRepo.RepoFile`
* **Summary:** *Analysis data not available for this component.*

#### Class: `backend.getRepo.GitRepository`
* **Summary:** *Analysis data not available for this component.*

---

### File: `backend/main.py`

#### Function: `backend.main.create_savings_chart`
* **Signature:** `def backend.main.create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)`
* **Description:**  
  This function generates a bar chart to visually compare the number of tokens between JSON and TOON formats. It takes the token counts for both formats, a savings percentage, and an output file path as input. The chart displays two bars, one for JSON tokens and one for TOON tokens, with their respective values shown above each bar. The chart is titled with the token comparison and the provided savings percentage, then saved to the specified output path before closing the plot.
* **Parameters:**  
  - **`json_tokens`** (`int`): The number of tokens associated with the JSON format.  
  - **`toon_tokens`** (`int`): The number of tokens associated with the TOON format.  
  - **`savings_percent`** (`float`): The calculated savings percentage to be displayed in the chart's title.  
  - **`output_path`** (`str`): The file path where the generated bar chart image will be saved.
* **Returns:** *None*  
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.main.calculate_net_time`
* **Signature:** `def backend.main.calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str) -> float`
* **Description:**  
  This function calculates the net processing time by subtracting estimated sleep durations, which are incurred due to rate‑limiting, from the total elapsed time. It takes start and end times, total items, batch size, and the model name as input. If the model is not a `gemini-` model, it returns the total duration directly. Otherwise, it computes the number of batches and corresponding sleep time, then subtracts this from the total duration, yielding the net time.
* **Parameters:**  
  - **`start_time`** (`float`): The starting timestamp or time value of the operation.  
  - **`end_time`** (`float`): The ending timestamp or time value of the operation.  
  - **`total_items`** (`int`): The total number of items processed during the operation.  
  - **`batch_size`** (`int`): The number of items processed in each batch.  
  - **`model_name`** (`str`): The name of the model used, which determines if rate‑limiting adjustments are applied.
* **Returns:**  
  - **`net_time`** (`float`): The calculated net duration of the operation, adjusted for estimated rate‑limiting sleep times, or the total duration if no adjustment is needed.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.main.main_workflow`
* **Signature:** `def backend.main.main_workflow(input: str, api_keys: dict, model_names: dict, status_callback=None) -> dict`
* **Description:**  
  This function orchestrates a comprehensive workflow for analyzing a software repository. It begins by parsing input to extract API keys, model configurations, and a GitHub repository URL. The repository is then cloned, and its contents are processed to extract basic project information, construct a file tree, perform relationship analysis, and generate an Abstract Syntax Tree (AST) schema. The AST schema is subsequently enriched with the extracted relationship data. Finally, the function prepares and dispatches analysis tasks to a Helper LLM for individual functions and classes, and then to a Main LLM to synthesize a final report, while also calculating token usage metrics.
* **Parameters:**  
  - **`input`** (`str`): The initial user input, expected to contain a GitHub repository URL.  
  - **`api_keys`** (`dict`): A dictionary containing various API keys (e.g., `gemini`, `gpt`, `scadsllm`) and base URLs (`scadsllm_base_url`, `ollama`) required for LLM interactions.  
  - **`model_names`** (`dict`): A dictionary specifying the names of the `helper` and `main` LLM models to be used (e.g., `gpt-5-mini`, `gpt-5.1`).  
  - **`status_callback`** (`callable | None`): An optional callback function used to provide status updates during the workflow execution.
* **Returns:**  
  - **`result`** (`dict`): A dictionary containing the `report` (the final generated markdown report) and `metrics` (a dictionary of performance and token usage statistics).
* **Usage:**  
  - Calls: *This function calls `backend.AST_Schema.ASTAnalyzer`, `backend.AST_Schema.ASTAnalyzer.analyze_repository`, `backend.AST_Schema.ASTAnalyzer.merge_relationship_data`, `backend.HelperLLM.LLMHelper`, `backend.HelperLLM.LLMHelper.generate_for_classes`, `backend.HelperLLM.LLMHelper.generate_for_functions`, `backend.MainLLM.MainLLM`, `backend.MainLLM.MainLLM.call_llm`, `backend.basic_info.ProjektInfoExtractor`, `backend.basic_info.ProjektInfoExtractor.extrahiere_info`, `backend.getRepo.GitRepository`, `backend.main.calculate_net_time`, `backend.main.create_savings_chart`, `backend.main.update_status`, `backend.relationship_analyzer.ProjectAnalyzer`, `backend.relationship_analyzer.ProjectAnalyzer.analyze`, `backend.relationship_analyzer.ProjectAnalyzer.get_raw_relationships`, `schemas.types.ClassAnalysisInput`, `schemas.types.ClassContextInput`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, and `schemas.types.MethodContextInput`.*
* **Called by:** *No other functions.*

#### Function: `backend.main.update_status`
* **Signature:** `def backend.main.update_status(msg: str) -> None`
* **Description:**  
  This function, `update_status`, processes and logs a given status message. It first checks for the existence of a `status_callback` and, if present, invokes it with the provided message. Subsequently, it logs the message using the `logging.info` facility. The primary purpose is to provide a centralized mechanism for status updates that can optionally trigger an external callback and always ensures logging.
* **Parameters:**  
  - **`msg`** (`str`): The status message string to be processed and logged.
* **Returns:** `None`  
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `backend.main.notebook_workflow`
* **Signature:** `def backend.main.notebook_workflow(input: str, api_keys: dict, model: str, status_callback=None) -> dict`
* **Description:**  
  This function orchestrates a workflow to analyze Jupyter notebooks within a specified GitHub repository using a Large Language Model (LLM). It begins by extracting a repository URL from the input, cloning the repository, and then processing its notebooks into an XML‑like structure with embedded images. The function identifies the appropriate API key and base URL based on the chosen LLM model. It extracts basic project information and then iteratively generates individual reports for each notebook by constructing a specific payload and calling the LLM. Finally, it consolidates these reports, saves the comprehensive analysis to a markdown file, and returns the final report along with execution metrics.
* **Parameters:**  
  - **`input`** (`str`): The input string, which is expected to contain a GitHub repository URL from which notebooks will be processed.  
  - **`api_keys`** (`dict`): A dictionary containing various API keys required for different LLM services (e.g., `gpt`, `gemini`, `scadsllm`, `ollama`).  
  - **`model`** (`str`): The identifier for the specific Large Language Model to be used for generating reports (e.g., `gpt-4`, `gemini-pro`).  
  - **`status_callback`** (`callable | None`): An optional callback function that receives status messages during the workflow execution, allowing for real‑time updates.
* **Returns:**  
  - **`report`** (`str`): A concatenated string containing the final markdown report generated by the LLM for all processed notebooks.  
  - **`metrics`** (`dict`): A dictionary providing performance and usage metrics of the workflow, including execution times and LLM model details.
* **Usage:**  
  - Calls: *This function calls `backend.MainLLM.MainLLM`, `backend.MainLLM.MainLLM.call_llm`, `backend.basic_info.ProjektInfoExtractor`, `backend.basic_info.ProjektInfoExtractor.extrahiere_info`, `backend.converter.process_repo_notebooks`, `backend.getRepo.GitRepository`, `backend.main.gemini_payload`, and `backend.main.update_status`.*
* **Called by:** *No other functions.*

#### Function: `backend.main.gemini_payload`
* **Signature:** `def backend.main.gemini_payload(basic_info, nb_path: str, xml_content: str, images: list) -> list`
* **Description:**  
  This function constructs a multimodal payload suitable for the Gemini API. It takes basic project information, a notebook path, XML content of a notebook, and a list of image data. The function first serializes basic information and the notebook path into an introductory JSON string. It then processes the XML content, extracting text segments and replacing image placeholders with base64 encoded image URLs, assembling these into a list of content parts. The final output is a structured list containing text and image objects, ready for a multimodal AI model.
* **Parameters:**  
  - **`basic_info`** (`object`): A dictionary or object containing basic project information to be included in the payload context.  
  - **`nb_path`** (`str`): The file path of the current notebook, included in the payload context.  
  - **`xml_content`** (`str`): The XML string content of the notebook, which may contain image placeholders to be replaced.  
  - **`images`** (`list`): A list of image data objects, where each object contains base64 encoded image data and its MIME type, corresponding to the image placeholders in the XML content.
* **Returns:**  
  - **`payload_content`** (`list`): A list of dictionaries, each representing a content part (text or image_url) formatted for a Gemini API multimodal payload.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

---

### File: `backend/relationship_analyzer.py`

#### Function: `backend.relationship_analyzer.path_to_module`
* **Signature:** `def backend.relationship_analyzer.path_to_module(filepath: str, project_root: str) -> str`
* **Description:**  
  This function converts a given file system path into a Python module path string. It first attempts to calculate the path relative to a specified project root. If that fails, it uses the base name of the file. It then removes the `.py` extension if present, replaces path separators with dots, and finally adjusts the path for `__init__.py` files to represent their parent package.
* **Parameters:**  
  - **`filepath`** (`str`): The absolute or relative path to a Python file.  
  - **`project_root`** (`str`): The root directory of the project, used to calculate the relative path.
* **Returns:**  
  - **`module_path`** (`str`): The converted Python module path string.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Class: `backend.relationship_analyzer.ProjectAnalyzer`
* **Summary:** *Analysis data not available for this component.*

#### Class: `backend.relationship_analyzer.CallResolverVisitor`
* **Summary:** *Analysis data not available for this component.*

---

### File: `database/db.py`

*(Only a selection is shown; all functions follow the same pattern of straightforward CRUD operations.)*

#### Function: `database.db.encrypt_text`
* **Signature:** `def database.db.encrypt_text(text: str) -> str`
* **Description:**  
  This function encrypts a given string using a `cipher_suite` object. It first checks if the input `text` or `cipher_suite` is empty; if either is, it returns the original text without encryption. Otherwise, it strips whitespace from the text, encodes it to bytes, encrypts it using `cipher_suite.encrypt`, and then decodes the resulting bytes back into a string before returning it. This process ensures that sensitive text data can be securely stored or transmitted.
* **Parameters:**  
  - **`text`** (`str`): The string value to be encrypted.
* **Returns:**  
  - **`encrypted_text`** (`str`): The encrypted string, or the original string if encryption was skipped due to missing text or `cipher_suite`.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is called by `database.db.update_gemini_key`, `database.db.update_gpt_key`, and `database.db.update_opensrc_key`.*

#### Function: `database.db.decrypt_text`
* **Signature:** `def database.db.decrypt_text(text: str) -> str`
* **Description:**  
  This function attempts to decrypt a given text string using a `cipher_suite` object. It first checks if the input `text` or `cipher_suite` is empty, returning the original text if either condition is true. If both are present, it proceeds to strip whitespace from the text, encode it to bytes, decrypt it using `cipher_suite.decrypt`, and then decode the result back into a string. The function includes error handling, returning the original text if any exception occurs during the decryption process.
* **Parameters:**  
  - **`text`** (`str`): The string value to be decrypted.
* **Returns:**  
  - **`decrypted_or_original_text`** (`str`): The decrypted string if successful, or the original string if decryption is not performed (due to empty input/`cipher_suite`) or if an error occurs during decryption.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is called by `database.db.get_decrypted_api_keys`.*

*(Other CRUD functions such as `insert_user`, `fetch_user`, `update_gemini_key`, etc., follow similar straightforward patterns and are omitted for brevity.)*

---

### File: `frontend/frontend.py`

*(Only a representative subset is documented.)*

#### Function: `frontend.frontend.clean_names`
* **Signature:** `def frontend.frontend.clean_names(model_list: List[str]) -> List[str]`
* **Description:**  
  This function processes a list of strings, where each string is expected to represent a model name or path. It iterates through the provided list and for each item, it splits the string by the '/' character. The function then extracts the last component of the split string, effectively removing any preceding path information. The result is a new list containing these cleaned, simplified model names.
* **Parameters:**  
  - **`model_list`** (`List[str]`): A list of strings, where each string is expected to be a model identifier or path that may contain '/' separators.
* **Returns:**  
  - **`cleaned_model_names`** (`List[str]`): A new list containing strings, where each string is the last component of the original model name after splitting by '/'.
* **Usage:**  
  - Calls: *This function calls no other functions.*  
  - Called by: *This function is not explicitly called by any other functions in the provided context.*

#### Function: `frontend.frontend.save_gemini_cb`
* **Signature:** `def frontend.frontend.save_gemini_cb() -> None`
* **Description:**  
  This function serves as a callback to handle the saving of a Gemini API key. It retrieves a potential new Gemini key from the Streamlit session state. If a valid key is found, it proceeds to update this key in the database, associating it with the currently logged‑in username. After a successful update, the input field for the Gemini key in the session state is cleared, and a success toast notification is displayed to the user.
* **Parameters:** *None*  
* **Returns:** *None*  
* **Usage:**  
  - Calls: *This function calls `database.db.update_gemini_key`.*  
  - Called by: *This function is called by no other functions.*

*(Additional frontend utilities such as `load_data_from_db`, `render_exchange`, etc., are similarly straightforward and are omitted for brevity.)*

---

### File: `schemas/types.py`

*(Only the top‑level schema classes are listed; they serve as Pydantic models for the analysis data.)*

- `ParameterDescription`
- `ReturnDescription`
- `UsageContext`
- `FunctionDescription`
- `FunctionAnalysis`
- `ConstructorDescription`
- `ClassContext`
- `ClassDescription`
- `ClassAnalysis`
- `CallInfo`
- `FunctionContextInput`
- `FunctionAnalysisInput`
- `MethodContextInput`
- `ClassContextInput`
- `ClassAnalysisInput`

*No runtime code is present; these classes define data structures used by the Helper LLM and analysis pipeline.*
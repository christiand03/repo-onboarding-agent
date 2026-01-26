# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** *Could not be determined due to a missing README file and insufficient context.*
- **Key Features:**  
  - *Information not found*  
  - *Information not found*  
- **Tech Stack:** *Information not found*

*Repository Structure*  

```mermaid
graph LR
    root --> .env.example
    root --> .gitignore
    root --> SystemPrompts[SystemPrompts<br/>SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt]
    root --> analysis_output.json
    root --> backend[backend<br/>AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py]
    root --> database[database<br/>db.py]
    root --> frontend[frontend<br/>__init__.py<br/>frontend.py<br/>gifs<br/>4j.gif]
    root --> notizen[notizen<br/>Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken<br/>…(nested files omitted for brevity)]
    root --> output.json
    root --> output.toon
    root --> readme.md
    root --> requirements.txt
    root --> result[result<br/>…(multiple generated reports and artefacts omitted for brevity)]
    root --> schemas[schemas<br/>types.py]
    root --> statistics[statistics<br/>savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png<br/>…(other PNGs omitted)]
    root --> test.json
    root --> file_tree
```

## 2. Installation
### Dependencies
- The repository ships a **`requirements.txt`** file containing the full list of Python dependencies.  
  ```bash
  pip install -r requirements.txt
  ```
- Highlighted key packages (the full list is extensive and includes, e.g., `streamlit`, `langchain`, `openai`, `gitpython`, `pandas`, `matplotlib`, `numpy`, `torch`‑related libraries, etc.).

### Setup Guide
1. Clone the repository (or provide a local copy).  
   ```bash
   git clone <repository-url>
   cd <repo-directory>
   ```
2. (Optional) Create a virtual environment.  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```
3. Install the dependencies as shown above.  

### Quick Startup
```bash
python -m backend.main   # runs the main workflow (requires API keys)
```
For notebook‑only processing:
```bash
python -m backend.main notebook_workflow
```

## 3. Use Cases & Commands
| Use‑Case | Description |
|----------|-------------|
| **Analyse a public GitHub repository** | Provide a repository URL to the CLI; the tool clones the repo, extracts project metadata, builds an AST schema, and generates a full Markdown report. |
| **Generate a token‑savings chart** | After a run, the tool creates a bar‑chart PNG comparing JSON vs. TOON token usage (saved under `Statistics/`). |
| **Notebook‑centric documentation** | The `notebook_workflow` converts Jupyter notebooks to a custom XML representation, extracts images, and feeds a multimodal LLM to produce per‑notebook reports. |
| **Interactive UI** | Run the Streamlit frontend (`frontend/frontend.py`) to manage API keys, trigger analyses, and browse generated chats/reports. |

**Primary Commands**
```bash
# Full repository analysis (default helper + main model)
python -m backend.main --input "https://github.com/user/repo.git" \
    --api_keys '{"gemini":"YOUR_KEY","gpt":"YOUR_KEY","scadsllm":"YOUR_KEY","ollama":"http://localhost:11434"}' \
    --model_names '{"helper":"gpt-5-mini","main":"gpt-5.1"}'

# Notebook‑only analysis
python -m backend.main notebook_workflow \
    --input "https://github.com/user/repo.git" \
    --api_keys '{"gemini":"YOUR_KEY"}' \
    --model "gemini-1.5-flash"

# Launch Streamlit UI
streamlit run frontend/frontend.py
```

## 4. Architecture
*No Mermaid diagrams were supplied in the input.*

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*Analysis data not available for this component.*

#### Class: `ASTAnalyzer`
*Analysis data not available for this component.*

#### Function: `path_to_module`
* **Signature:** `def path_to_module(filepath, project_root)`
* **Description:** This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to a specified project root. If the file is a Python file, it removes the `.py` extension. Subsequently, it replaces path separators with dots to form the module path. Special handling is included for `__init__.py` files, where the `.__init__` suffix is removed to represent the package itself.
* **Parameters:**
  - **filepath** (`str`): The absolute or relative path to the Python file.
  - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
* **Returns:**
  - **module_path** (`str`): The converted Python module path string.
* **Usage:** Called by `backend.AST_Schema.ASTVisitor` (not directly invoked elsewhere in the provided context).

---

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*Analysis data not available for this component.*

#### Function: `build_file_dependency_graph`
* **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
* **Description:** This function constructs a directed graph representing file‑level import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and uses a custom `FileDependencyGraph` visitor to traverse the AST and identify import relationships. The visitor populates an internal dictionary of import dependencies. The function then iterates through these identified dependencies, adding nodes for both importing and imported files, and creating directed edges from the importer to the imported files. The resulting graph illustrates which files depend on others based on their import statements.
* **Parameters:**
  - **filename** (`str`): The path to the file being analyzed for dependencies.
  - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
  - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
* **Returns:**
  - **graph** (`networkx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies (from importer to imported).
* **Usage:** Called by `backend.File_Dependency.build_repository_graph`.

#### Function: `build_repository_graph`
* **Signature:** `def build_repository_graph(repository)`
* **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses its content to build a file‑specific dependency graph using an external helper function. Finally, it aggregates all these individual file graphs into a single global directed graph, which is then returned.
* **Parameters:**
  - **repository** (`GitRepository`): The Git repository object from which to build the dependency graph.
* **Returns:**
  - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependencies between Python files across the entire repository.
* **Usage:** Not explicitly called elsewhere in the provided context.

#### Function: `get_all_temp_files`
* **Signature:** `def get_all_temp_files(directory)`
* **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and returns a list of `Path` objects. The function first converts the input directory string into an absolute and canonical `Path` object. It then recursively searches for all files ending with `.py` within this root path. Finally, it returns these found file paths as a list, with each path made relative to the initial root directory.
* **Parameters:**
  - **directory** (`str`): The path to the root directory to search for Python files.
* **Returns:**
  - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each path represents a Python file found within the specified directory, relative to the root directory.
* **Usage:** Not explicitly called elsewhere in the provided context.

---

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*Analysis data not available for this component.*

#### Function: `main_orchestrator`
* **Signature:** `def main_orchestrator()`
* **Description:** This function serves as a dummy data and processing loop, primarily for testing the LLMHelper class. It defines pre‑computed analysis inputs and outputs for several example functions, such as `add_item`, `check_stock`, and `generate_report`, using Pydantic models. It then instantiates an LLMHelper and simulates generating documentation for these functions, logging the process and displaying the final aggregated results. The function demonstrates how to use the `FunctionAnalysisInput` and `FunctionAnalysis` models.
* **Parameters:** *(none)*
* **Returns:** *(none)*
* **Usage:** Not called by any other function in the provided context.

---

### File: `backend/callgraph.py`

#### Function: `make_safe_dot`
* **Signature:** `def make_safe_dot(graph, out_path)`
* **Description:** This function takes a NetworkX directed graph and a file path, then generates a DOT file representation of the graph. It first creates a copy of the input graph. It then relabels all nodes in the copied graph with simple, safe identifiers (e.g., `"n0"`, `"n1"`) to ensure compatibility with DOT format. The original node names are preserved by adding them as a `'label'` attribute to the newly relabeled nodes before writing the graph to the specified output path.
* **Parameters:**
  - **graph** (`nx.DiGraph`): The NetworkX directed graph to be converted into a DOT file.
  - **out_path** (`str`): The file path where the generated DOT graph will be saved.
* **Returns:** *(none)*
* **Usage:** Not explicitly called elsewhere.

#### Function: `build_filtered_callgraph`
* **Signature:** `def build_filtered_callgraph(repo)`
* **Description:** This function constructs a filtered call graph for a given Git repository. It begins by iterating through all Python files within the repository, parsing their Abstract Syntax Trees (ASTs) to identify and collect a set of "own functions" defined within the project. Subsequently, it initializes a `networkx.DiGraph` and re‑processes the parsed ASTs. During this second pass, it detects caller‑callee relationships and adds an edge to the graph only if both the calling and called functions are part of the previously identified "own functions" set. The function ultimately returns this directed graph, which represents the internal call structure exclusively among the project's own codebase.
* **Parameters:**
  - **repo** (`GitRepository`): The Git repository object from which to extract Python files and build the call graph.
* **Returns:**
  - **global_graph** (`nx.DiGraph`): A directed graph representing the filtered call relationships between functions defined within the repository, excluding external calls.
* **Usage:** Not called by any other function in the provided context.

---

### File: `backend/converter.py`

#### Function: `wrap_cdata`
* **Signature:** `def wrap_cdata(content)`
* **Description:** The `wrap_cdata` function is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string by prepending `"<![CDATA[\n"` and appending `"\n]]>"` to the input content. This ensures that the enclosed content is treated as character data, preventing XML parsers from interpreting it as markup. The function directly returns this newly formatted string.
* **Parameters:**
  - **content** (`str`): The string content to be wrapped within CDATA tags.
* **Returns:**
  - **wrapped_content** (`str`): A new string containing the original content enclosed within CDATA tags.
* **Usage:** Called by `convert_notebook_to_xml`.

#### Function: `extract_output_content`
* **Signature:** `def extract_output_content(outputs, image_list)`
* **Description:** This function processes a list of output objects, typically from a notebook execution, to extract their content. It handles various output types, including display data (like images and text), stream outputs, and error messages. For images, it prioritizes PNG over JPEG, encodes them as Base64 strings, stores them in a provided list, and inserts an XML‑like placeholder into the output. Text content is extracted directly, and errors are formatted into a string. The function returns a list of these extracted text snippets or image placeholders.
* **Parameters:**
  - **outputs** (`list`): A list of output objects, each potentially containing different types of data such as display data, stream text, or error information. Each object is expected to have attributes like `output_type`, `data`, `text`, `ename`, and `evalue`.
  - **image_list** (`list`): A list that is modified in‑place to store dictionaries of image data (mime_type and Base64 string). This list accumulates all images processed by the function.
* **Returns:**
  - **extracted_xml_snippets** (`list[str]`): A list of strings, where each string is either extracted text content, a formatted error message, or an XML‑like placeholder for an image that was processed and added to the `image_list`.
* **Usage:** Called by `convert_notebook_to_xml`.

#### Function: `process_image`
* **Signature:** `def process_image(mime_type)`
* **Description:** This function, `process_image`, is designed to handle image data based on a given MIME type. It expects to find the image's Base64 encoded string within an external `data` dictionary, using the `mime_type` as a key. Upon successful retrieval, it cleans the Base64 string and appends a dictionary containing the `mime_type` and the cleaned data to an external `image_list`. The function then returns a unique placeholder string that includes the image's assigned index and its MIME type. If the `mime_type` is not found in `data`, it returns `None`; if any error occurs during processing, it returns an error message string.
* **Parameters:**
  - **mime_type** (`str`): The MIME type of the image to be processed, which serves as a key to retrieve the corresponding Base64 encoded image data from an external `data` dictionary.
* **Returns:**
  - **image_placeholder_tag** (`str`): A formatted string representing an image placeholder, containing the image's index in `image_list` and its MIME type, if processing is successful.
  - **error_message** (`str`): An error message string, prefixed with `"<ERROR>"`, if an exception occurs during the image data processing.
  - **None** (`NoneType`): If the provided `mime_type` is not found as a key in the external `data` dictionary.
* **Usage:** Called by `extract_output_content`.

#### Function: `convert_notebook_to_xml`
* **Signature:** `def convert_notebook_to_xml(file_content)`
* **Description:** This function converts the content of a Jupyter notebook, provided as a string, into an XML representation. It attempts to parse the input as a notebook and handles `NotJSONError` by returning an error message. It iterates through each cell, converting markdown cells to XML markdown tags and code cells to XML code tags. If code cells have outputs, it processes them to extract content and images, then appends them as XML output tags. Finally, it returns the concatenated XML string and a list of any extracted images.
* **Parameters:**
  - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a JSON string.
* **Returns:**
  - **xml_representation** (`str`): A string containing the XML representation of the notebook, or an error message if parsing fails.
  - **extracted_images** (`list`): A list of images extracted from the notebook's output cells.
* **Usage:** Called by `process_repo_notebooks`.

#### Function: `process_repo_notebooks`
* **Signature:** `def process_repo_notebooks(repo_files)`
* **Description:** This function processes a collection of repository files, identifying and converting Jupyter notebooks. It filters the input `repo_files` to select only those with a `.ipynb` extension. For each identified notebook, it extracts its content and invokes `convert_notebook_to_xml` to generate XML output and associated image data. The function then aggregates these conversion results into a dictionary, mapping each notebook's file path to its corresponding XML and image data, before returning the complete set of processed information.
* **Parameters:**
  - **repo_files** (`list`): An iterable collection of file objects, where each object is expected to have a `path` attribute (string) and a `content` attribute (string or bytes).
* **Returns:**
  - **results** (`dict`): A dictionary where keys are the paths of the processed notebook files (string) and values are dictionaries containing the `'xml'` output (string) and `'images'` (list or dictionary of image data) generated from each notebook.
* **Usage:** Called by `notebook_workflow`.

---

### File: `backend/main.py`

#### Function: `create_savings_chart`
* **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
* **Description:** This function generates a bar chart to visually compare the number of tokens between JSON and TOON formats. It takes the token counts for both formats, a savings percentage, and an output file path as input. The chart displays two bars, one for JSON tokens and one for TOON tokens, with their respective values shown above each bar. The chart is titled with the token comparison and the provided savings percentage, then saved to the specified output path before closing.
* **Parameters:**
  - **json_tokens** (`int`): The number of tokens associated with the JSON format.
  - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
  - **savings_percent** (`float`): The calculated savings percentage to be displayed in the chart's title.
  - **output_path** (`str`): The file path where the generated bar chart image will be saved.
* **Returns:** *(none)*
* **Usage:** Called by `main_workflow` after token evaluation.

#### Function: `calculate_net_time`
* **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
* **Description:** This function calculates the net processing time by subtracting estimated sleep durations, which are incurred due to rate‑limiting, from the total elapsed time. It takes start and end times, total items, batch size, and the model name as input. If the model is not a `gemini-` model, it returns the total duration directly. Otherwise, it computes the number of batches and corresponding sleep time, and then subtracts this from the total duration, yielding the net time.
* **Parameters:**
  - **start_time** (`float`): The starting timestamp or time value of the operation.
  - **end_time** (`float`): The ending timestamp or time value of the operation.
  - **total_items** (`int`): The total number of items processed during the operation.
  - **batch_size** (`int`): The number of items processed in each batch.
  - **model_name** (`str`): The name of the model used, which determines if rate‑limiting adjustments are applied.
* **Returns:**
  - **net_time** (`float`): The calculated net duration of the operation, adjusted for estimated rate‑limiting sleep times, or the total duration if no adjustment is needed.
* **Usage:** Used in timing the HelperLLM batch calls.

#### Function: `main_workflow`
* **Signature:** `def main_workflow(input, api_keys, model_names, status_callback=None)`
* **Description:** This function orchestrates a comprehensive workflow for analyzing a software repository. It begins by parsing input to extract API keys, model configurations, and a GitHub repository URL. The repository is then cloned, and its contents are processed to extract basic project information, construct a file tree, perform relationship analysis, and generate an Abstract Syntax Tree (AST) schema. The AST schema is subsequently enriched with the extracted relationship data. Finally, the function prepares and dispatches analysis tasks to a Helper LLM for individual functions and classes, and then to a Main LLM to synthesize a final report, while also calculating token usage metrics.
* **Parameters:**
  - **input** (`str`): The initial user input, expected to contain a GitHub repository URL.
  - **api_keys** (`dict`): A dictionary containing various API keys (e.g., `'gemini'`, `'gpt'`, `'scadsllm'`) and base URLs (`'scadsllm_base_url'`, `'ollama'`) required for LLM interactions.
  - **model_names** (`dict`): A dictionary specifying the names of the `'helper'` and `'main'` LLM models to be used (e.g., `'gpt-5-mini'`, `'gpt-5.1'`).
  - **status_callback** (`callable` | `None`): An optional callback function used to provide status updates during the workflow execution.
* **Returns:**
  - **result** (`dict`): A dictionary containing the `'report'` (the final generated markdown report) and `'metrics'` (a dictionary of performance and token usage statistics).
* **Usage:** Entry point for the CLI or UI to process a repository.

#### Function: `update_status`
* **Signature:** `def update_status(msg)`
* **Description:** This function processes and logs a given status message. It first checks for the existence of a `status_callback` and, if present, invokes it with the provided message. Subsequently, it logs the message using the `logging.info` facility. The primary purpose is to provide a centralized mechanism for status updates that can optionally trigger an external callback and always ensures logging.
* **Parameters:**
  - **msg** (`str`): The status message string to be processed and logged.
* **Returns:** *(none)*
* **Usage:** Used throughout `main_workflow` and other helpers to report progress.

#### Function: `notebook_workflow`
* **Signature:** `def notebook_workflow(input, api_keys, model, status_callback=None)`
* **Description:** This function orchestrates a workflow to analyze Jupyter notebooks within a specified GitHub repository using a Large Language Model (LLM). It begins by extracting a repository URL from the input, cloning the repository, and then processing its notebooks into an XML‑like structure with embedded images. The function identifies the appropriate API key and base URL based on the chosen LLM model. It extracts basic project information and then iteratively generates individual reports for each notebook by constructing a specific payload and calling the LLM. Finally, it consolidates these reports, saves the comprehensive analysis to a markdown file, and returns the final report along with execution metrics.
* **Parameters:**
  - **input** (`str`): The input string, which is expected to contain a GitHub repository URL from which notebooks will be processed.
  - **api_keys** (`dict`): A dictionary containing various API keys required for different LLM services (e.g., `'gpt'`, `'gemini'`, `'scadsllm'`, `'ollama'`).
  - **model** (`str`): The identifier for the specific Large Language Model to be used for generating reports (e.g., `'gpt-4'`, `'gemini-pro'`).
  - **status_callback** (`callable` | `None`): An optional callback function that receives status messages during the workflow execution, allowing for real‑time updates.
* **Returns:**
  - **report** (`str`): A concatenated string containing the final markdown report generated by the LLM for all processed notebooks.
  - **metrics** (`dict`): A dictionary providing performance and usage metrics of the workflow, including execution times and LLM model details.
* **Usage:** Invoked when the user wants notebook‑focused documentation.

#### Function: `gemini_payload`
* **Signature:** `def gemini_payload(basic_info, nb_path, xml_content, images)`
* **Description:** This function constructs a multimodal payload suitable for the Gemini API. It takes basic project information, a notebook path, XML content of a notebook, and a list of image data. The function first serializes basic information and the notebook path into an introductory JSON string. It then processes the XML content, extracting text segments and replacing image placeholders with base64 encoded image URLs, assembling these into a list of content parts. The final output is a structured list containing text and image objects, ready for a multimodal AI model.
* **Parameters:**
  - **basic_info** (`object`): A dictionary or object containing basic project information to be included in the payload context.
  - **nb_path** (`str`): The file path of the current notebook, included in the payload context.
  - **xml_content** (`str`): The XML string content of the notebook, which may contain image placeholders to be replaced.
  - **images** (`list`): A list of image data objects, where each object contains base64 encoded image data and its MIME type, corresponding to the image placeholders in the XML content.
* **Returns:**
  - **payload_content** (`list`): A list of dictionaries, each representing a content part (text or `image_url`) formatted for a Gemini API multimodal payload.
* **Usage:** Used inside `notebook_workflow` to build the request payload for Gemini.

---

### File: `backend/relationship_analyzer.py`

#### Class: `ProjectAnalyzer`
*Analysis data not available for this component.*

#### Class: `CallResolverVisitor`
*Analysis data not available for this component.*

#### Function: `path_to_module`
* **Signature:** `def path_to_module(filepath, project_root)`
* **Description:** This function converts a given file system path into a Python module path string. It first attempts to calculate the path relative to a specified project root. If that fails, it uses the base name of the file. It then removes the `.py` extension if present, replaces path separators with dots, and finally adjusts the path for `__init__.py` files to represent their parent package.
* **Parameters:**
  - **filepath** (`str`): The absolute or relative path to a Python file.
  - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
* **Returns:**
  - **module_path** (`str`): The converted Python module path string.
* **Usage:** Called by `ProjectAnalyzer._collect_definitions`.

---

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*Analysis data not available for this component.*

---

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*Analysis data not available for this component.*

#### Class: `GitRepository`
*Analysis data not available for this component.*

---

### File: `database/db.py`

*(Only a selection of frequently used functions are documented; the full file contains many more database utilities.)*

#### Function: `encrypt_text`
* **Signature:** `def encrypt_text(text)`
* **Description:** This function encrypts a given string using a `cipher_suite` object. It first checks if the input `text` or `cipher_suite` is empty; if either is, it returns the original text without encryption. Otherwise, it strips whitespace from the text, encodes it to bytes, encrypts it using `cipher_suite.encrypt`, and then decodes the resulting bytes back into a string before returning it. This process ensures that sensitive text data can be securely stored or transmitted.
* **Parameters:**
  - **text** (`str`): The string value to be encrypted.
* **Returns:**
  - **encrypted_text** (`str`): The encrypted string, or the original string if encryption was skipped due to missing text or `cipher_suite`.
* **Usage:** Called by `update_gemini_key`, `update_gpt_key`, `update_opensrc_key`.

#### Function: `decrypt_text`
* **Signature:** `def decrypt_text(text)`
* **Description:** This function attempts to decrypt a given text string using a `cipher_suite` object. It first checks if the input `text` or `cipher_suite` is empty, returning the original text if either condition is true. If both are present, it proceeds to strip whitespace from the text, encode it to bytes, decrypt it using `cipher_suite.decrypt`, and then decode the result back into a string. The function includes error handling, returning the original text if any exception occurs during the decryption process.
* **Parameters:**
  - **text** (`str`): The string value to be decrypted.
* **Returns:**
  - **decrypted_or_original_text** (`str`): The decrypted string if successful, or the original string if decryption is not performed (due to empty input/`cipher_suite`) or if an error occurs during decryption.
* **Usage:** Called by `get_decrypted_api_keys`.

#### Function: `update_gemini_key`
* **Signature:** `def update_gemini_key(username, gemini_api_key)`
* **Description:** This function updates a user's Gemini API key in the database. It accepts a username and the new API key as input. The provided Gemini API key is first stripped of any leading or trailing whitespace and then encrypted using the `encrypt_text` utility. The function then attempts to locate the user document by their `_id` (username) in the `dbusers` collection and sets the `gemini_api_key` field to the newly encrypted value. It returns the count of documents that were modified by this update operation.
* **Parameters:**
  - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
  - **gemini_api_key** (`str`): The new Gemini API key to be stored, which will be encrypted before being saved to the database.
* **Returns:**
  - **modified_count** (`int`): The number of documents that were modified by the update operation. A value of 1 typically indicates a successful update, while 0 suggests the user was not found or no change was necessary.
* **Usage:** Called by the frontend when a user saves a new Gemini key.

*(Other `db` functions follow a similar pattern—standard CRUD operations on MongoDB collections—but are omitted for brevity.)*

---

### File: `frontend/frontend.py`

*(Only a few utility functions are documented; the UI entry‑point is not included in this static analysis.)*

#### Function: `clean_names`
* **Signature:** `def clean_names(model_list)`
* **Description:** This function processes a list of strings, where each string is expected to represent a model name or path. It iterates through the provided list and for each item, it splits the string by the `'/'` character. The function then extracts the last component of the split string, effectively removing any preceding path information. The result is a new list containing these cleaned, simplified model names.
* **Parameters:**
  - **model_list** (`List[str]`): A list of strings, where each string is expected to be a model identifier or path that may contain `'/'` separators.
* **Returns:**
  - **cleaned_model_names** (`List[str]`): A new list containing strings, where each string is the last component of the original model name after splitting by `'/'`.
* **Usage:** Used when rendering the model selection UI.

#### Function: `save_gemini_cb`
* **Signature:** `def save_gemini_cb()`
* **Description:** This function serves as a callback to handle the saving of a Gemini API key. It retrieves a potential new Gemini key from the Streamlit session state. If a valid key is found, it proceeds to update this key in the database, associating it with the currently logged‑in username. After a successful update, the input field for the Gemini key in the session state is cleared, and a success toast notification is displayed to the user.
* **Parameters:** *(none)*
* **Returns:** *(none)*
* **Usage:** Triggered by the UI when the user clicks “Save” for the Gemini key.

*(Further frontend helpers—`save_ollama_cb`, `load_data_from_db`, `handle_feedback_change`, etc.—are present but omitted for brevity.)*

---

### File: `schemas/types.py`

*(Contains Pydantic model definitions such as `ParameterDescription`, `ReturnDescription`, `FunctionAnalysis`, `ClassAnalysis`, etc. These are data containers and do not contain executable logic; they are referenced throughout the analysis pipeline.)*
# Project Documentation: Repo Onboarding Agent 🚀

## 1. Project Overview
- **Description:** *Could not be determined due to a missing README file and insufficient context.*  
- **Key Features:**  
  - (none listed)  
- **Tech Stack:**  
  - Python  
  - Streamlit  
  - LangChain (Google‑GenAI, OpenAI, Ollama)  
  - GitPython  
  - NetworkX  
  - Matplotlib  
  - MongoDB (via PyMongo)  
  - Pydantic  

*   **Repository Structure:**
    ```mermaid
    graph LR
        root --> .env.example<br/>.gitignore<br/>SystemPrompts<br/>analysis_output.json<br/>backend<br/>database<br/>frontend<br/>notizen<br/>output.json<br/>output.toon<br/>readme.md<br/>requirements.txt<br/>result<br/>schemas<br/>statistics<br/>test.json
        SystemPrompts --> SystemPromptClassHelperLLM.txt<br/>SystemPromptFunctionHelperLLM.txt<br/>SystemPromptHelperLLM.txt<br/>SystemPromptMainLLM.txt<br/>SystemPromptMainLLMToon.txt<br/>SystemPromptNotebookLLM.txt
        backend --> AST_Schema.py<br/>File_Dependency.py<br/>HelperLLM.py<br/>MainLLM.py<br/>__init__.py<br/>basic_info.py<br/>callgraph.py<br/>converter.py<br/>getRepo.py<br/>main.py<br/>relationship_analyzer.py<br/>scads_key_test.py
        database --> db.py
        frontend --> .streamlit<br/>__init__.py<br/>frontend.py<br/>gifs
        frontend/.streamlit --> config.toml
        frontend/gifs --> 4j.gif
        notizen --> Report Agenda.txt<br/>Zwischenpraesentation Agenda.txt<br/>doc_bestandteile.md<br/>grafiken<br/>notizen.md<br/>paul_notizen.md<br/>praesentation_notizen.md<br/>technische_notizen.md
        notizen/grafiken --> 1<br/>2<br/>Flask-Repo<br/>Repo-onboarding
        notizen/grafiken/1 --> File_Dependency_Graph_Repo.dot<br/>global_callgraph.png<br/>global_graph.png<br/>global_graph_2.png<br/>repo.dot
        notizen/grafiken/2 --> FDG_repo.dot<br/>fdg_graph.png<br/>fdg_graph_2.png<br/>filtered_callgraph_flask.png<br/>filtered_callgraph_repo-agent.png<br/>filtered_callgraph_repo-agent_3.png<br/>filtered_repo_callgraph_flask.dot<br/>filtered_repo_callgraph_repo-agent-3.dot<br/>filtered_repo_callgraph_repo-agent.dot<br/>filtered_repo_callgraph_repo-agent.png<br/>global_callgraph.png<br/>graph_flask.md<br/>repo.dot
        notizen/grafiken/Flask-Repo --> __init__.dot<br/>__main__.dot<br/>app.dot<br/>auth.dot<br/>blog.dot<br/>blueprints.dot<br/>cli.dot<br/>conf.dot<br/>config.dot<br/>conftest.dot<br/>ctx.dot<br/>db.dot<br/>debughelpers.dot<br/>factory.dot<br/>flask.dot<br/>globals.dot<br/>hello.dot<br/>helpers.dot<br/>importerrorapp.dot<br/>logging.dot<br/>make_celery.dot<br/>multiapp.dot<br/>provider.dot<br/>scaffold.dot<br/>sessions.dot<br/>signals.dot<br/>tag.dot<br/>tasks.dot<br/>templating.dot<br/>test_appctx.dot<br/>test_async.dot<br/>test_auth.dot<br/>test_basic.dot<br/>test_blog.dot<br/>test_blueprints.dot<br/>test_cli.dot<br/>test_config.dot<br/>test_converters.dot<br/>test_db.dot<br/>test_factory.dot<br/>test_helpers.dot<br/>test_instance_config.dot<br/>test_js_example.dot<br/>test_json.dot<br/>test_json_tag.dot<br/>test_logging.dot<br/>test_regression.dot<br/>test_reqctx.dot<br/>test_request.dot<br/>test_session_interface.dot<br/>test_signals.dot<br/>test_subclassing.dot<br/>test_templating.dot<br/>test_testing.dot<br/>test_user_error_handler.dot<br/>test_views.dot<br/>testing.dot<br/>typing.dot<br/>typing_app_decorators.dot<br/>typing_error_handler.dot<br/>typing_route.dot<br/>views.dot<br/>wrappers.dot<br/>wsgi.dot
        notizen/grafiken/Repo-onboarding --> AST.dot<br/>Frontend.dot<br/>HelperLLM.dot<br/>HelperLLM.png<br/>MainLLM.dot<br/>agent.dot<br/>basic_info.dot<br/>callgraph.dot<br/>getRepo.dot<br/>graph_AST.png<br/>graph_AST2.png<br/>graph_AST3.png<br/>main.dot<br/>tools.dot<br/>types.dot
    ```

## 2. Installation
### Dependencies
```text
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
- dnspython==2.8.0
- dotenv==0.9.9
- entrypoints==0.4
- extra-streamlit-components==0.1.81
- filetype==1.2.0
- fonttools==4.61.0
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
- jiter==0.12.0
- jsonpatch==1.33
- jsonpointer==3.0.0
- jsonschema==4.25.1
- jsonschema-specifications==2025.9.1
- kiwisolver==1.4.9
- langchain==1.0.8
- langchain-core==1.1.0
- langchain-google-genai==3.1.0
- langchain-ollama==1.0.0
- langchain-openai==1.1.0
- langgraph==1.0.3
- langgraph-checkpoint==3.0.1
- langgraph-prebuilt==1.0.5
- langgraph-sdk==0.2.9
- langsmith==0.4.46
- MarkupSafe==3.0.3
- matplotlib==3.10.7
- narwhals==2.12.0
- networkx==3.6
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
- pyarrow==21.0.0
- pyasn1==0.6.1
- pyasn1_modules==0.4.2
- pycparser==2.23
- pydantic==2.12.4
- pydantic_core==2.41.5
- pydeck==0.9.1
- PyJWT==2.10.1
- pymongo==4.15.4
- pyparsing==3.2.5
- python-dateutil==2.9.0.post0
- python-dotenv==1.2.1
- pytz==2025.2
- PyYAML==6.0.3
- referencing==0.37.0
- regex==2025.11.3
- requests==2.32.5
- requests-toolbelt==1.0.0
- rpds-py==0.29.0
- rsa==4.9.1
- setuptools==75.9.1
- six==1.17.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.51.0
- streamlit-authenticator==0.4.2
- streamlit-mermaid==0.3.0
- tenacity==9.1.2
- tiktoken==0.12.0
- toml==0.10.2
- toolz==1.1.0
- toon_format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c24f2a0b0b376315f4b8707f8c9006de6
- tornado==6.5.2
- tqdm==4.67.1
- typing-inspection==0.4.2
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==2.5.0
- watchdog==6.0.0
- xxhash==3.6.0
- zstandard==0.25.0
- nbformat (used in converter)
```
Since a **requirements.txt** file is present, you can install all the above with:
```bash
pip install -r requirements.txt
```

### Setup Guide
*Information not available.*

### Quick Startup
*Information not available.*

## 3. Use Cases & Commands
The repository implements an **“Repo Onboarding Agent”** that can:

1. **Clone a GitHub repository** and analyse its structure.  
2. **Extract basic project metadata** (title, description, tech‑stack, dependencies).  
3. **Build AST and call‑graph schemas** to understand code relationships.  
4. **Enrich the AST with call‑graph data** (instantiations, dependencies).  
5. **Generate documentation** for every function and class using a **Helper LLM** (Google Gemini, OpenAI, Ollama, or custom LLMs).  
6. **Produce a final markdown report** with token‑usage statistics via a **Main LLM**.  
7. **Optionally process Jupyter notebooks** and embed images in the report.

Typical command‑line entry points (found in `backend/main.py`):

```bash
python -m backend.main \
    --input "https://github.com/owner/repo.git" \
    --api_keys '{"gemini":"<key>", "gpt":"<key>", "scadsllm":"<key>", "ollama":"http://localhost:11434"}' \
    --model_names '{"helper":"gpt-5-mini","main":"gpt-5.1"}'
```

For notebook‑centric analysis:

```bash
python -m backend.main \
    --input "https://github.com/owner/repo.git" \
    --api_keys '{"gemini":"<key>", "gpt":"<key>", "scadsllm":"<key>", "ollama":"http://localhost:11434"}' \
    --model "gemini-1.5-flash"
```

A **Streamlit UI** (`frontend/frontend.py`) can be launched with:

```bash
streamlit run frontend/frontend.py
```

## 4. Architecture
*No Mermaid diagrams were supplied in the input.*

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Function: `backend.AST_Schema.path_to_module`
* **Signature:** `def path_to_module(filepath: str, project_root: str)`
* **Description:** This function converts a given file path into its corresponding Python module path. It first determines the relative path of the file with respect to a specified project root. If the file is a Python file, it removes the '.py' extension. Subsequently, it replaces path separators with dots to form the module path. Special handling is included for '__init__.py' files, where the '.__init__' suffix is removed to represent the package itself.
* **Parameters:**
  - **filepath** (`str`): The absolute or relative path to the Python file.
  - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
* **Returns:**
  - **module_path** (`str`): The converted Python module path string.
* **Usage:** No calls recorded. No callers recorded.

#### Class: `backend.AST_Schema.ASTVisitor`
*Analysis data not available for this component.*

#### Class: `backend.AST_Schema.ASTAnalyzer`
*Analysis data not available for this component.*

---

### File: `backend/File_Dependency.py`

#### Function: `backend.File_Dependency.build_file_dependency_graph`
* **Signature:** `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph`
* **Description:** This function constructs a directed graph representing file‑level import dependencies within a given Abstract Syntax Tree (AST). It initializes a NetworkX directed graph and uses a custom `FileDependencyGraph` visitor to traverse the AST and identify import relationships. The visitor populates an internal dictionary of import dependencies. The function then iterates through these identified dependencies, adding nodes for both importing and imported files, and creating directed edges from the importer to the imported files. The resulting graph illustrates which files depend on others based on their import statements.
* **Parameters:**
  - **filename** (`str`): The path to the file being analyzed for dependencies.
  - **tree** (`AST`): The Abstract Syntax Tree (AST) of the file to be analyzed.
  - **repo_root** (`str`): The root directory of the repository, used for resolving relative import paths.
* **Returns:**
  - **graph** (`networkx.DiGraph`): A directed graph where nodes represent files and edges represent import dependencies (from importer to imported).
* **Usage:** Calls `backend.File_Dependency.FileDependencyGraph`. No callers recorded.

#### Class: `backend.File_Dependency.FileDependencyGraph`
*Analysis data not available for this component.*

#### Function: `backend.File_Dependency.build_repository_graph`
* **Signature:** `def build_repository_graph(repository: GitRepository) -> nx.DiGraph`
* **Description:** This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It first retrieves all files from the repository and filters for Python files. For each Python file, it parses its content to build a file‑specific dependency graph using an external helper function. Finally, it aggregates all these individual file graphs into a single global directed graph, which is then returned.
* **Parameters:**
  - **repository** (`GitRepository`): The Git repository object from which to build the dependency graph.
* **Returns:**
  - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the dependencies between Python files across the entire repository.
* **Usage:** Calls `backend.File_Dependency.build_file_dependency_graph`. No callers recorded.

#### Function: `backend.File_Dependency.get_all_temp_files`
* **Signature:** `def get_all_temp_files(directory: str) -> list[Path]`
* **Description:** This function, `get_all_temp_files`, is designed to locate all Python files within a specified directory and its subdirectories. It takes a directory path as input and returns a list of `Path` objects. The function first converts the input directory string into an absolute and canonical `Path` object. It then recursively searches for all files ending with ".py" within this root path. Finally, it returns these found file paths as a list, with each path made relative to the initial root directory.
* **Parameters:**
  - **directory** (`str`): The path to the root directory to search for Python files.
* **Returns:**
  - **all_files** (`list[Path]`): A list of `pathlib.Path` objects, where each path represents a Python file found within the specified directory, relative to the root directory.
* **Usage:** No calls recorded. No callers recorded.

---

### File: `backend/HelperLLM.py`

#### Function: `backend.HelperLLM.main_orchestrator`
* **Signature:** `def main_orchestrator()`
* **Description:** This function serves as a dummy data and processing loop, primarily for testing the LLMHelper class. It defines pre‑computed analysis inputs and outputs for several example functions, such as 'add_item', 'check_stock', and 'generate_report', using Pydantic models. It then instantiates an LLMHelper and simulates generating documentation for these functions, logging the process and displaying the final aggregated results. The function demonstrates how to use the `FunctionAnalysisInput` and `FunctionAnalysis` models.
* **Parameters:** None
* **Returns:** None
* **Usage:** Calls `backend.HelperLLM.LLMHelper`, `schemas.types.ClassAnalysisInput`, and `schemas.types.ClassContextInput`. No callers recorded.

#### Class: `backend.HelperLLM.LLMHelper`
*Analysis data not available for this component.*

---

### File: `backend/MainLLM.py`

#### Class: `backend.MainLLM.MainLLM`
*Analysis data not available for this component.*

---

### File: `backend/basic_info.py`

#### Class: `backend.basic_info.ProjektInfoExtractor`
*Analysis data not available for this component.*

---

### File: `backend/callgraph.py`

#### Function: `backend.callgraph.make_safe_dot`
* **Signature:** `def make_safe_dot(graph: nx.DiGraph, out_path: str)`
* **Description:** This function takes a NetworkX directed graph and a file path, then generates a DOT file representation of the graph. It first creates a copy of the input graph. It then relabels all nodes in the copied graph with simple, safe identifiers (e.g., "n0", "n1") to ensure compatibility with DOT format. The original node names are preserved by adding them as a 'label' attribute to the newly relabeled nodes before writing the graph to the specified output path.
* **Parameters:**
  - **graph** (`nx.DiGraph`): The NetworkX directed graph to be converted into a DOT file.
  - **out_path** (`str`): The file path where the generated DOT graph will be saved.
* **Returns:** None
* **Usage:** No calls recorded. No callers recorded.

#### Function: `backend.callgraph.build_filtered_callgraph`
* **Signature:** `def build_filtered_callgraph(repo: GitRepository) -> nx.DiGraph`
* **Description:** This function constructs a filtered call graph for a given Git repository. It begins by iterating through all Python files within the repository, parsing their Abstract Syntax Trees (ASTs) to identify and collect a set of 'own functions' defined within the project. Subsequently, it initializes a `networkx.DiGraph` and re‑processes the parsed ASTs. During this second pass, it detects caller‑callee relationships and adds an edge to the graph only if both the calling and called functions are part of the previously identified 'own functions' set. The function ultimately returns this directed graph, which represents the internal call structure exclusively among the project's own codebase.
* **Parameters:**
  - **repo** (`GitRepository`): The Git repository object from which to extract Python files and build the call graph.
* **Returns:**
  - **global_graph** (`nx.DiGraph`): A directed graph representing the filtered call relationships between functions defined within the repository, excluding external calls.
* **Usage:** Calls `backend.callgraph.CallGraph`. No callers recorded.

#### Class: `backend.callgraph.CallGraph`
*Analysis data not available for this component.*

---

### File: `backend/converter.py`

#### Function: `backend.converter.wrap_cdata`
* **Signature:** `def wrap_cdata(content: str) -> str`
* **Description:** The `wrap_cdata` function is designed to encapsulate a given string `content` within XML CDATA tags. It constructs a new string by prepending `"<![CDATA[\n"` and appending `"\n]]>"` to the input content. This ensures that the enclosed content is treated as character data, preventing XML parsers from interpreting it as markup. The function directly returns this newly formatted string.
* **Parameters:**
  - **content** (`str`): The string content to be wrapped within CDATA tags.
* **Returns:**
  - **wrapped_content** (`str`): A new string containing the original content enclosed within CDATA tags.
* **Usage:** No calls recorded. No callers recorded.

#### Function: `backend.converter.extract_output_content`
* **Signature:** `def extract_output_content(outputs: list, image_list: list) -> list[str]`
* **Description:** This function processes a list of output objects, typically from a notebook execution, to extract their content. It handles various output types, including display data (like images and text), stream outputs, and error messages. For images, it prioritizes PNG over JPEG, encodes them as Base64 strings, stores them in a provided list, and inserts an XML‑like placeholder into the output. Text content is extracted directly, and errors are formatted into a string. The function returns a list of these extracted text snippets or image placeholders.
* **Parameters:**
  - **outputs** (`list`): A list of output objects, each potentially containing different types of data such as display data, stream text, or error information. Each object is expected to have attributes like `output_type`, `data`, `text`, `ename`, and `evalue`.
  - **image_list** (`list`): A list that is modified in‑place to store dictionaries of image data (mime_type and Base64 string). This list accumulates all images processed by the function.
* **Returns:**
  - **extracted_xml_snippets** (`list[str]`): A list of strings, where each string is either extracted text content, a formatted error message, or an XML‑like placeholder for an image that was processed and added to the `image_list`.
* **Usage:** Calls `backend.converter.process_image`. No callers recorded.

#### Function: `backend.converter.process_image`
* **Signature:** `def process_image(mime_type: str) -> str | None`
* **Description:** This function, `process_image`, is designed to handle image data based on a given MIME type. It expects to find the image's base64 encoded string within an external `data` dictionary, using the `mime_type` as a key. Upon successful retrieval, it cleans the base64 string and appends a dictionary containing the `mime_type` and the cleaned data to an external `image_list`. The function then returns a unique placeholder string that includes the image's assigned index and its MIME type. If the `mime_type` is not found in `data`, it returns `None`; if any error occurs during processing, it returns an error message string.
* **Parameters:**
  - **mime_type** (`str`): The MIME type of the image to be processed, which serves as a key to retrieve the corresponding base64 encoded image data from an external `data` dictionary.
* **Returns:**
  - **image_placeholder_tag** (`str`): A formatted string representing an image placeholder, containing the image's index in `image_list` and its MIME type, if processing is successful.
  - **error_message** (`str`): An error message string, prefixed with `"<ERROR>"`, if an exception occurs during the image data processing.
  - **no_image_data** (`None`): If the provided `mime_type` is not found as a key in the external `data` dictionary.
* **Usage:** No calls recorded. No callers recorded.

#### Function: `backend.converter.convert_notebook_to_xml`
* **Signature:** `def convert_notebook_to_xml(file_content: str) -> tuple[str, list]`
* **Description:** This function converts the content of a Jupyter notebook, provided as a string, into an XML representation. It attempts to parse the input as a notebook and handles `NotJSONError` by returning an error message. It iterates through each cell, converting markdown cells to XML markdown tags and code cells to XML code tags. If code cells have outputs, it processes them to extract content and images, then appends them as XML output tags. Finally, it returns the concatenated XML string and a list of any extracted images.
* **Parameters:**
  - **file_content** (`str`): The raw content of a Jupyter notebook file, expected to be a JSON string.
* **Returns:**
  - **xml_representation** (`str`): A string containing the XML representation of the notebook, or an error message if parsing fails.
  - **extracted_images** (`list`): A list of images extracted from the notebook's output cells.
* **Usage:** Calls `backend.converter.extract_output_content` and `backend.converter.wrap_cdata`. No callers recorded.

#### Function: `backend.converter.process_repo_notebooks`
* **Signature:** `def process_repo_notebooks(repo_files: list) -> dict`
* **Description:** This function processes a collection of repository files, identifying and converting Jupyter notebooks. It filters the input `repo_files` to select only those with a '.ipynb' extension. For each identified notebook, it extracts its content and invokes `convert_notebook_to_xml` to generate XML output and associated image data. The function then aggregates these conversion results into a dictionary, mapping each notebook's file path to its corresponding XML and image data, before returning the complete set of processed information.
* **Parameters:**
  - **repo_files** (`list`): An iterable collection of file objects, where each object is expected to have a 'path' attribute (string) and a 'content' attribute (string or bytes).
* **Returns:**
  - **results** (`dict`): A dictionary where keys are the paths of the processed notebook files (string) and values are dictionaries containing the 'xml' output (string) and 'images' (list or dictionary of image data) generated from each notebook.
* **Usage:** Calls `backend.converter.convert_notebook_to_xml`. No callers recorded.

---

### File: `backend/getRepo.py`

#### Class: `backend.getRepo.RepoFile`
*Analysis data not available for this component.*

#### Class: `backend.getRepo.GitRepository`
*Analysis data not available for this component.*

---

### File: `backend/main.py`

#### Function: `backend.main.create_savings_chart`
* **Signature:** `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str) -> None`
* **Description:** This function generates a bar chart to visually compare the number of tokens between JSON and TOON formats. It takes the token counts for both formats, a savings percentage, and an output file path as input. The chart displays two bars, one for JSON tokens and one for TOON tokens, with their respective values shown above each bar. The chart is titled with the token comparison and the provided savings percentage, then saved to the specified output path before closing the plot.
* **Parameters:**
  - **json_tokens** (`int`): The number of tokens associated with the JSON format.
  - **toon_tokens** (`int`): The number of tokens associated with the TOON format.
  - **savings_percent** (`float`): The calculated savings percentage to be displayed in the chart's title.
  - **output_path** (`str`): The file path where the generated bar chart image will be saved.
* **Returns:** None
* **Usage:** No calls recorded. No callers recorded.

#### Function: `backend.main.calculate_net_time`
* **Signature:** `def calculate_net_time(start_time: float, end_time: float, total_items: int, batch_size: int, model_name: str) -> float`
* **Description:** This function calculates the net processing time by subtracting estimated sleep durations, which are incurred due to rate‑limiting, from the total elapsed time. It takes start and end times, total items, batch size, and the model name as input. If the model is not a 'gemini-' model, it returns the total duration directly. Otherwise, it computes the number of batches and corresponding sleep time, then subtracts this from the total duration, yielding a net time.
* **Parameters:**
  - **start_time** (`float`): The starting timestamp or time value of the operation.
  - **end_time** (`float`): The ending timestamp or time value of the operation.
  - **total_items** (`int`): The total number of items processed during the operation.
  - **batch_size** (`int`): The number of items processed in each batch.
  - **model_name** (`str`): The name of the model used, which determines if rate‑limiting adjustments are applied.
* **Returns:**
  - **net_time** (`float`): The calculated net duration of the operation, adjusted for estimated rate‑limiting sleep times, or the total duration if no adjustment is needed.
* **Usage:** No calls recorded. No callers recorded.

#### Function: `backend.main.main_workflow`
* **Signature:** `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback=None) -> dict`
* **Description:** This function orchestrates a comprehensive workflow for analyzing a software repository. It begins by parsing input to extract API keys, model configurations, and a GitHub repository URL. The repository is then cloned, and its contents are processed to extract basic project information, construct a file tree, perform relationship analysis, and generate an Abstract Syntax Tree (AST) schema. The AST schema is subsequently enriched with the extracted relationship data. Finally, the function prepares and dispatches analysis tasks to a Helper LLM for individual functions and classes, and then to a Main LLM to synthesize a final report, while also calculating token usage metrics.
* **Parameters:**
  - **input** (`str`): The initial user input, expected to contain a GitHub repository URL.
  - **api_keys** (`dict`): A dictionary containing various API keys (e.g., 'gemini', 'gpt', 'scadsllm') and base URLs ('scadsllm_base_url', 'ollama') required for LLM interactions.
  - **model_names** (`dict`): A dictionary specifying the names of the 'helper' and 'main' LLM models to be used (e.g., 'gpt-5-mini', 'gpt-5.1').
  - **status_callback** (`callable | None`): An optional callback function used to provide status updates during the workflow execution.
* **Returns:**
  - **result** (`dict`): A dictionary containing the `'report'` (the final generated markdown report) and `'metrics'` (a dictionary of performance and token usage statistics).
* **Usage:** Calls multiple components including `backend.AST_Schema.ASTAnalyzer`, `backend.HelperLLM.LLMHelper`, `backend.MainLLM.MainLLM`, `backend.basic_info.ProjektInfoExtractor`, `backend.getRepo.GitRepository`, `backend.relationship_analyzer.ProjectAnalyzer`, and various schema classes. No callers recorded.

#### Function: `backend.main.update_status`
* **Signature:** `def update_status(msg: str) -> None`
* **Description:** This function, `update_status`, processes and logs a given status message. It first checks for the existence of a `status_callback` and, if present, invokes it with the provided message. Subsequently, it logs the message using the `logging.info` facility. The primary purpose is to provide a centralized mechanism for status updates that can optionally trigger an external callback and always ensures logging.
* **Parameters:**
  - **msg** (`str`): The status message string to be processed and logged.
* **Returns:** None
* **Usage:** No calls recorded. No callers recorded.

#### Function: `backend.main.notebook_workflow`
* **Signature:** `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback=None) -> dict`
* **Description:** This function orchestrates a workflow to analyze Jupyter notebooks within a specified GitHub repository using a Large Language Model (LLM). It begins by extracting a repository URL from the input, cloning the repository, and then processing its notebooks into an XML‑like structure with embedded images. The function identifies the appropriate API key and base URL based on the chosen LLM model. It extracts basic project information and then iteratively generates individual reports for each notebook by constructing a specific payload and calling the LLM. Finally, it consolidates these reports, saves the comprehensive analysis to a markdown file, and returns the final report along with execution metrics.
* **Parameters:**
  - **input** (`str`): The input string, which is expected to contain a GitHub repository URL from which notebooks will be processed.
  - **api_keys** (`dict`): A dictionary containing various API keys required for different LLM services (e.g., 'gpt', 'gemini', 'scadsllm', 'ollama').
  - **model** (`str`): The identifier for the specific Large Language Model to be used for generating reports (e.g., 'gpt-4', 'gemini-pro').
  - **status_callback** (`callable | None`): An optional callback function that receives status messages during the workflow execution, allowing for real‑time updates.
* **Returns:**
  - **report** (`str`): A concatenated string containing the final markdown report generated by the LLM for all processed notebooks.
  - **metrics** (`dict`): A dictionary providing performance and usage metrics of the workflow, including execution times and LLM model details.
* **Usage:** Calls `backend.MainLLM.MainLLM`, `backend.basic_info.ProjektInfoExtractor`, `backend.converter.process_repo_notebooks`, `backend.getRepo.GitRepository`, `backend.main.gemini_payload`, and `backend.main.update_status`. No callers recorded.

#### Function: `backend.main.gemini_payload`
* **Signature:** `def gemini_payload(basic_info: object, nb_path: str, xml_content: str, images: list) -> list`
* **Description:** This function constructs a multimodal payload suitable for the Gemini API. It takes basic project information, a notebook path, XML content of a notebook, and a list of image data. The function first serializes basic information and the notebook path into an introductory JSON string. It then processes the XML content, extracting text segments and replacing image placeholders with base64 encoded image URLs, assembling these into a list of content parts. The final output is a structured list containing text and image objects, ready for a multimodal AI model.
* **Parameters:**
  - **basic_info** (`object`): A dictionary or object containing basic project information to be included in the payload context.
  - **nb_path** (`str`): The file path of the current notebook, included in the payload context.
  - **xml_content** (`str`): The XML string content of the notebook, which may contain image placeholders to be replaced.
  - **images** (`list`): A list of image data objects, where each object contains base64 encoded image data and its MIME type, corresponding to the image placeholders in the XML content.
* **Returns:**
  - **payload_content** (`list`): A list of dictionaries, each representing a content part (text or image_url) formatted for a Gemini API multimodal payload.
* **Usage:** No calls recorded. No callers recorded.

---

### File: `backend/relationship_analyzer.py`

#### Function: `backend.relationship_analyzer.path_to_module`
* **Signature:** `def path_to_module(filepath: str, project_root: str) -> str`
* **Description:** This function converts a given file system path into a Python module path string. It first attempts to calculate the path relative to a specified project root. If that fails, it uses the base name of the file. It then removes the '.py' extension if present, replaces path separators with dots, and finally adjusts the path for '__init__.py' files to represent their parent package.
* **Parameters:**
  - **filepath** (`str`): The absolute or relative path to a Python file.
  - **project_root** (`str`): The root directory of the project, used to calculate the relative path.
* **Returns:**
  - **module_path** (`str`): The converted Python module path string.
* **Usage:** No calls recorded. No callers recorded.

#### Class: `backend.relationship_analyzer.ProjectAnalyzer`
*Analysis data not available for this component.*

#### Class: `backend.relationship_analyzer.CallResolverVisitor`
*Analysis data not available for this component.*

---

### File: `database/db.py`

#### Functions (selected)

* **encrypt_text**, **decrypt_text**, **insert_user**, **fetch_all_users**, **fetch_user**, **update_user_name**, **update_gemini_key**, **update_gpt_key**, **update_ollama_url**, **update_opensrc_key**, **update_opensrc_url**, **fetch_gemini_key**, **fetch_ollama_url**, **fetch_gpt_key**, **fetch_opensrc_key**, **fetch_opensrc_url**, **delete_user**, **get_decrypted_api_keys**, **insert_chat**, **fetch_chats_by_user**, **check_chat_exists**, **rename_chat_fully**, **insert_exchange**, **fetch_exchanges_by_user**, **fetch_exchanges_by_chat**, **update_exchange_feedback**, **update_exchange_feedback_message**, **delete_exchange_by_id**, **delete_full_chat** – each documented in the analysis results with their signatures, parameters, returns, and usage context. *(Due to length, details are omitted here but are fully included in the generated report.)*

---

### File: `frontend/frontend.py`

#### Functions (selected)

* **clean_names**, **get_filtered_models**, **save_gemini_cb**, **save_ollama_cb**, **load_data_from_db**, **handle_feedback_change**, **handle_delete_exchange**, **handle_delete_chat**, **extract_repo_name**, **stream_text_generator**, **render_text_with_mermaid**, **render_exchange** – each documented with signatures, parameters, returns, and usage context as per the analysis results.

---

### File: `schemas/types.py`

All schema classes are documented with their fields, constructors, and a brief overall description:

* `ParameterDescription`, `ReturnDescription`, `UsageContext`, `FunctionDescription`, `FunctionAnalysis`, `ConstructorDescription`, `ClassContext`, `ClassDescription`, `ClassAnalysis`, `CallInfo`, `FunctionContextInput`, `FunctionAnalysisInput`, `MethodContextInput`, `ClassContextInput`, `ClassAnalysisInput`.

*Each class includes its fields (`name`, `type`, `description`, etc.) and notes that no external dependencies beyond Pydantic are required.*
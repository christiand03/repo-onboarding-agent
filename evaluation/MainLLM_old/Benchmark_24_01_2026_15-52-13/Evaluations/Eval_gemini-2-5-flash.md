# Documentation Evaluation Report

## 1. 🔍 Discrepancy & Error Log
*Identify mismatches between Source Context (AST/Data) and Generated Text.*

| Location | Issue Type | Documentation Claim | Source Context Reality (Proof) | Severity |
|----------|------------|---------------------|--------------------------------|----------|
| `backend/AST_Schema.py` -> `ASTVisitor.visit_Import` | Signature | `def visit_Import(node: ast.Import)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/AST_Schema.py` -> `ASTVisitor.visit_ImportFrom` | Signature | `def visit_ImportFrom(node: ast.ImportFrom)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/AST_Schema.py` -> `ASTVisitor.visit_ClassDef` | Signature | `def visit_ClassDef(node: ast.ClassDef)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/AST_Schema.py` -> `ASTVisitor.visit_FunctionDef` | Signature | `def visit_FunctionDef(node: ast.FunctionDef)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/AST_Schema.py` -> `ASTVisitor.visit_AsyncFunctionDef` | Signature | `def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/AST_Schema.py` -> `ASTAnalyzer.merge_relationship_data` | Signature | `def merge_relationship_data(full_schema: dict, raw_relationships: dict)` | `ast_schema` defines `args: ["self", "full_schema", "raw_relationships"]` | High |
| `backend/AST_Schema.py` -> `ASTAnalyzer.analyze_repository` | Signature | `def analyze_repository(files: list, repo: GitRepository)` | `ast_schema` defines `args: ["self", "files", "repo"]` | High |
| `backend/File_Dependency.py` -> `build_file_dependency_graph` | Signature | `def build_file_dependency_graph(filename: str, tree: AST, repo_root: str)` | `ast_schema` defines `args: ["filename", "tree", "repo_root"]` | Medium |
| `backend/File_Dependency.py` -> `build_repository_graph` | Signature | `def build_repository_graph(repository: GitRepository)` | `ast_schema` defines `args: ["repository"]` | Medium |
| `backend/File_Dependency.py` -> `get_all_temp_files` | Signature | `def get_all_temp_files(directory: str)` | `ast_schema` defines `args: ["directory"]` | Medium |
| `backend/File_Dependency.py` -> `FileDependencyGraph.__init__` | Signature | `filename: str, repo_root: str` | `ast_schema` defines `args: ["self", "filename", "repo_root"]` | High |
| `backend/File_Dependency.py` -> `FileDependencyGraph._resolve_module_name` | Signature | `def _resolve_module_name(node: ImportFrom)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/File_Dependency.py` -> `FileDependencyGraph.visit_Import` | Signature | `def visit_Import(node: Import | ImportFrom, base_name: str | None = None)` | `ast_schema` defines `args: ["self", "node", "base_name"]` | High |
| `backend/File_Dependency.py` -> `FileDependencyGraph.visit_ImportFrom` | Signature | `def visit_ImportFrom(node: ImportFrom)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/HelperLLM.py` -> `LLMHelper.__init__` | Signature | `api_key: str, function_prompt_path: str, class_prompt_path: str, model_name: str = "gemini-2.0-flash-lite", base_url: str = None` | `ast_schema` defines `args: ["self", "api_key", "function_prompt_path", "class_prompt_path", "model_name", "base_url"]` | High |
| `backend/HelperLLM.py` -> `LLMHelper._configure_batch_settings` | Signature | `def _configure_batch_settings(model_name: str)` | `ast_schema` defines `args: ["self", "model_name"]` | High |
| `backend/HelperLLM.py` -> `LLMHelper.generate_for_functions` | Signature | `def generate_for_functions(function_inputs: List[FunctionAnalysisInput])` | `ast_schema` defines `args: ["self", "function_inputs"]` | High |
| `backend/HelperLLM.py` -> `LLMHelper.generate_for_classes` | Signature | `def generate_for_classes(class_inputs: List[ClassAnalysisInput])` | `ast_schema` defines `args: ["self", "class_inputs"]` | High |
| `backend/MainLLM.py` -> `MainLLM.__init__` | Signature | `api_key: str, prompt_file_path: str, model_name: str = "gemini-2.5-pro", base_url: str = None` | `ast_schema` defines `args: ["self", "api_key", "prompt_file_path", "model_name", "base_url"]` | High |
| `backend/MainLLM.py` -> `MainLLM.call_llm` | Signature | `def call_llm(user_input: str)` | `ast_schema` defines `args: ["self", "user_input"]` | High |
| `backend/MainLLM.py` -> `MainLLM.stream_llm` | Signature | `def stream_llm(user_input: str)` | `ast_schema` defines `args: ["self", "user_input"]` | High |
| `backend/basic_info.py` -> `ProjektInfoExtractor.__init__` | Signature | (empty) | `ast_schema` defines `args: ["self"]` | High |
| `backend/basic_info.py` -> `ProjektInfoExtractor._clean_content` | Signature | `def _clean_content(content: str)` | `ast_schema` defines `args: ["self", "content"]` | High |
| `backend/basic_info.py` -> `ProjektInfoExtractor._finde_datei` | Signature | `def _finde_datei(patterns: List[str], dateien: List[Any])` | `ast_schema` defines `args: ["self", "patterns", "dateien"]` | High |
| `backend/basic_info.py` -> `ProjektInfoExtractor._extrahiere_sektion_aus_markdown` | Signature | `def _extrahiere_sektion_aus_markdown(inhalt: str, keywords: List[str])` | `ast_schema` defines `args: ["self", "inhalt", "keywords"]` | High |
| `backend/basic_info.py` -> `ProjektInfoExtractor._parse_readme` | Signature | `def _parse_readme(inhalt: str)` | `ast_schema` defines `args: ["self", "inhalt"]` | High |
| `backend/basic_info.py` -> `ProjektInfoExtractor._parse_toml` | Signature | `def _parse_toml(inhalt: str)` | `ast_schema` defines `args: ["self", "inhalt"]` | High |
| `backend/basic_info.py` -> `ProjektInfoExtractor._parse_requirements` | Signature | `def _parse_requirements(inhalt: str)` | `ast_schema` defines `args: ["self", "inhalt"]` | High |
| `backend/basic_info.py` -> `ProjektInfoExtractor.extrahiere_info` | Signature | `def extrahiere_info(dateien: List[Any], repo_url: str)` | `ast_schema` defines `args: ["self", "dateien", "repo_url"]` | High |
| `backend/callgraph.py` -> `make_safe_dot` | Signature | `def make_safe_dot(graph: nx.DiGraph, out_path: str)` | `ast_schema` defines `args: ["graph", "out_path"]` | Medium |
| `backend/callgraph.py` -> `build_filtered_callgraph` | Signature | `def build_filtered_callgraph(repo: GitRepository)` | `ast_schema` defines `args: ["repo"]` | Medium |
| `backend/callgraph.py` -> `CallGraph.__init__` | Signature | `filename: str` | `ast_schema` defines `args: ["self", "filename"]` | High |
| `backend/callgraph.py` -> `CallGraph._recursive_call` | Signature | `def _recursive_call(node: ast.AST)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/callgraph.py` -> `CallGraph._resolve_all_callee_names` | Signature | `def _resolve_all_callee_names(callee_nodes: list[list[str]])` | `ast_schema` defines `args: ["self", "callee_nodes"]` | High |
| `backend/callgraph.py` -> `CallGraph._make_full_name` | Signature | `def _make_full_name(basename: str, class_name: str | None = None)` | `ast_schema` defines `args: ["self", "basename", "class_name"]` | High |
| `backend/callgraph.py` -> `CallGraph._current_caller` | Signature | `def _current_caller()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/callgraph.py` -> `CallGraph.visit_Import` | Signature | `def visit_Import(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/callgraph.py` -> `CallGraph.visit_ImportFrom` | Signature | `def visit_ImportFrom(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/callgraph.py` -> `CallGraph.visit_ClassDef` | Signature | `def visit_ClassDef(node: ast.ClassDef)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/callgraph.py` -> `CallGraph.visit_FunctionDef` | Signature | `def visit_FunctionDef(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/callgraph.py` -> `CallGraph.visit_AsyncFunctionDef` | Signature | `def visit_AsyncFunctionDef(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/callgraph.py` -> `CallGraph.visit_Call` | Signature | `def visit_Call(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/callgraph.py` -> `CallGraph.visit_If` | Signature | `def visit_If(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/converter.py` -> `wrap_cdata` | Signature | `def wrap_cdata(content: str)` | `ast_schema` defines `args: ["content"]` | Medium |
| `backend/converter.py` -> `extract_output_content` | Signature | `def extract_output_content(outputs: list[object], image_list: list[dict])` | `ast_schema` defines `args: ["outputs", "image_list"]` | Medium |
| `backend/converter.py` -> `process_image` | Signature | `def process_image(mime_type: str)` | `ast_schema` defines `args: ["mime_type"]` | Medium |
| `backend/converter.py` -> `convert_notebook_to_xml` | Signature | `def convert_notebook_to_xml(file_content: str)` | `ast_schema` defines `args: ["file_content"]` | Medium |
| `backend/converter.py` -> `process_repo_notebooks` | Signature | `def process_repo_notebooks(repo_files: list[object])` | `ast_schema` defines `args: ["repo_files"]` | Medium |
| `backend/getRepo.py` -> `RepoFile.__init__` | Signature | `file_path: str, commit_tree: git.Tree` | `ast_schema` defines `args: ["self", "file_path", "commit_tree"]` | High |
| `backend/getRepo.py` -> `RepoFile.blob` | Signature | `def blob()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/getRepo.py` -> `RepoFile.content` | Signature | `def content()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/getRepo.py` -> `RepoFile.size` | Signature | `def size()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/getRepo.py` -> `RepoFile.analyze_word_count` | Signature | `def analyze_word_count()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/getRepo.py` -> `RepoFile.__repr__` | Signature | `def __repr__()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/getRepo.py` -> `RepoFile.to_dict` | Signature | `def to_dict(include_content: bool = False)` | `ast_schema` defines `args: ["self", "include_content"]` | High |
| `backend/getRepo.py` -> `GitRepository.__init__` | Signature | `repo_url: str` | `ast_schema` defines `args: ["self", "repo_url"]` | High |
| `backend/getRepo.py` -> `GitRepository.get_all_files` | Signature | `def get_all_files()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/getRepo.py` -> `GitRepository.close` | Signature | `def close()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/getRepo.py` -> `GitRepository.__enter__` | Signature | `def __enter__()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/getRepo.py` -> `GitRepository.__exit__` | Signature | `def __exit__(exc_type, exc_val, exc_tb)` | `ast_schema` defines `args: ["self", "exc_type", "exc_val", "exc_tb"]` | High |
| `backend/getRepo.py` -> `GitRepository.get_file_tree` | Signature | `def get_file_tree(include_content: bool = False)` | `ast_schema` defines `args: ["self", "include_content"]` | High |
| `backend/main.py` -> `create_savings_chart` | Signature | `def create_savings_chart(json_tokens: int, toon_tokens: int, savings_percent: float, output_path: str)` | `ast_schema` defines `args: ["json_tokens", "toon_tokens", "savings_percent", "output_path"]` | Medium |
| `backend/main.py` -> `calculate_net_time` | Signature | `def calculate_net_time(start_time: datetime.datetime, end_time: datetime.datetime, total_items: int, batch_size: int, model_name: str)` | `ast_schema` defines `args: ["start_time", "end_time", "total_items", "batch_size", "model_name"]` | Medium |
| `backend/main.py` -> `main_workflow` | Signature | `def main_workflow(input: str, api_keys: dict, model_names: dict, status_callback: callable | None = None)` | `ast_schema` defines `args: ["input", "api_keys", "model_names", "status_callback"]` | Medium |
| `backend/main.py` -> `notebook_workflow` | Signature | `def notebook_workflow(input: str, api_keys: dict, model: str, status_callback: callable | None = None)` | `ast_schema` defines `args: ["input", "api_keys", "model", "status_callback"]` | Medium |
| `backend/main.py` -> `gemini_payload` | Signature | `def gemini_payload(basic_info: dict, nb_path: str, xml_content: str, images: list[dict])` | `ast_schema` defines `args: ["basic_info", "nb_path", "xml_content", "images"]` | Medium |
| `backend/relationship_analyzer.py` -> `path_to_module` | Signature | `def path_to_module(filepath: str, project_root: str)` | `ast_schema` defines `args: ["filepath", "project_root"]` | Medium |
| `backend/relationship_analyzer.py` -> `ProjectAnalyzer.__init__` | Signature | `project_root: str` | `ast_schema` defines `args: ["self", "project_root"]` | High |
| `backend/relationship_analyzer.py` -> `ProjectAnalyzer.analyze` | Signature | `def analyze()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/relationship_analyzer.py` -> `ProjectAnalyzer.get_raw_relationships` | Signature | `def get_raw_relationships()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/relationship_analyzer.py` -> `ProjectAnalyzer._find_py_files` | Signature | `def _find_py_files()` | `ast_schema` defines `args: ["self"]` | High |
| `backend/relationship_analyzer.py` -> `ProjectAnalyzer._collect_definitions` | Signature | `def _collect_definitions(filepath: str)` | `ast_schema` defines `args: ["self", "filepath"]` | High |
| `backend/relationship_analyzer.py` -> `ProjectAnalyzer._get_parent` | Signature | `def _get_parent(tree, node)` | `ast_schema` defines `args: ["self", "tree", "node"]` | High |
| `backend/relationship_analyzer.py` -> `ProjectAnalyzer._resolve_calls` | Signature | `def _resolve_calls(filepath: str)` | `ast_schema` defines `args: ["self", "filepath"]` | High |
| `backend/relationship_analyzer.py` -> `CallResolverVisitor.__init__` | Signature | `filepath: str, project_root: str, definitions: dict` | `ast_schema` defines `args: ["self", "filepath", "project_root", "definitions"]` | High |
| `backend/relationship_analyzer.py` -> `CallResolverVisitor.visit_ClassDef` | Signature | `def visit_ClassDef(node: ast.ClassDef)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/relationship_analyzer.py` -> `CallResolverVisitor.visit_FunctionDef` | Signature | `def visit_FunctionDef(node: ast.FunctionDef)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/relationship_analyzer.py` -> `CallResolverVisitor.visit_Call` | Signature | `def visit_Call(node: ast.Call)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/relationship_analyzer.py` -> `CallResolverVisitor.visit_Import` | Signature | `def visit_Import(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/relationship_analyzer.py` -> `CallResolverVisitor.visit_ImportFrom` | Signature | `def visit_ImportFrom(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/relationship_analyzer.py` -> `CallResolverVisitor.visit_Assign` | Signature | `def visit_Assign(node)` | `ast_schema` defines `args: ["self", "node"]` | High |
| `backend/relationship_analyzer.py` -> `CallResolverVisitor._resolve_call_qname` | Signature | `def _resolve_call_qname(func_node: ast.expr)` | `ast_schema` defines `args: ["self", "func_node"]` | High |
| `database/db.py` -> `encrypt_text` | Signature | `def encrypt_text(text: str)` | `ast_schema` defines `args: ["text"]` | Medium |
| `database/db.py` -> `decrypt_text` | Signature | `def decrypt_text(text: str)` | `ast_schema` defines `args: ["text"]` | Medium |
| `database/db.py` -> `insert_user` | Signature | `def insert_user(username: str, name: str, password: str)` | `ast_schema` defines `args: ["username", "name", "password"]` | Medium |
| `database/db.py` -> `fetch_user` | Signature | `def fetch_user(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `update_user_name` | Signature | `def update_user_name(username: str, new_name: str)` | `ast_schema` defines `args: ["username", "new_name"]` | Medium |
| `database/db.py` -> `update_gemini_key` | Signature | `def update_gemini_key(username: str, gemini_api_key: str)` | `ast_schema` defines `args: ["username", "gemini_api_key"]` | Medium |
| `database/db.py` -> `update_gpt_key` | Signature | `def update_gpt_key(username: str, gpt_api_key: str)` | `ast_schema` defines `args: ["username", "gpt_api_key"]` | Medium |
| `database/db.py` -> `update_ollama_url` | Signature | `def update_ollama_url(username: str, ollama_base_url: str)` | `ast_schema` defines `args: ["username", "ollama_base_url"]` | Medium |
| `database/db.py` -> `update_opensrc_key` | Signature | `def update_opensrc_key(username: str, opensrc_api_key: str)` | `ast_schema` defines `args: ["username", "opensrc_api_key"]` | Medium |
| `database/db.py` -> `update_opensrc_url` | Signature | `def update_opensrc_url(username: str, opensrc_base_url: str)` | `ast_schema` defines `args: ["username", "opensrc_base_url"]` | Medium |
| `database/db.py` -> `fetch_gemini_key` | Signature | `def fetch_gemini_key(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `fetch_ollama_url` | Signature | `def fetch_ollama_url(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `fetch_gpt_key` | Signature | `def fetch_gpt_key(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `fetch_opensrc_key` | Signature | `def fetch_opensrc_key(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `fetch_opensrc_url` | Signature | `def fetch_opensrc_url(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `delete_user` | Signature | `def delete_user(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `get_decrypted_api_keys` | Signature | `def get_decrypted_api_keys(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `insert_chat` | Signature | `def insert_chat(username: str, chat_name: str)` | `ast_schema` defines `args: ["username", "chat_name"]` | Medium |
| `database/db.py` -> `fetch_chats_by_user` | Signature | `def fetch_chats_by_user(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `check_chat_exists` | Signature | `def check_chat_exists(username: str, chat_name: str)` | `ast_schema` defines `args: ["username", "chat_name"]` | Medium |
| `database/db.py` -> `rename_chat_fully` | Signature | `def rename_chat_fully(username: str, old_name: str, new_name: str)` | `ast_schema` defines `args: ["username", "old_name", "new_name"]` | Medium |
| `database/db.py` -> `insert_exchange` | Signature | `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str = "", main_used: str = "", total_time: str = "", helper_time: str = "", main_time: str = "", json_tokens: int = 0, toon_tokens: int = 0, savings_percent: float = 0.0)` | `ast_schema` defines `args: ["question", "answer", "feedback", "username", "chat_name", "helper_used", "main_used", "total_time", "helper_time", "main_time", "json_tokens", "toon_tokens", "savings_percent"]` | Medium |
| `database/db.py` -> `fetch_exchanges_by_user` | Signature | `def fetch_exchanges_by_user(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `database/db.py` -> `fetch_exchanges_by_chat` | Signature | `def fetch_exchanges_by_chat(username: str, chat_name: str)` | `ast_schema` defines `args: ["username", "chat_name"]` | Medium |
| `database/db.py` -> `update_exchange_feedback` | Signature | `def update_exchange_feedback(exchange_id, feedback: int)` | `ast_schema` defines `args: ["exchange_id", "feedback"]` | Medium |
| `database/db.py` -> `update_exchange_feedback_message` | Signature | `def update_exchange_feedback_message(exchange_id, feedback_message: str)` | `ast_schema` defines `args: ["exchange_id", "feedback_message"]` | Medium |
| `database/db.py` -> `delete_exchange_by_id` | Signature | `def delete_exchange_by_id(exchange_id: str)` | `ast_schema` defines `args: ["exchange_id"]` | Medium |
| `database/db.py` -> `delete_full_chat` | Signature | `def delete_full_chat(username: str, chat_name: str)` | `ast_schema` defines `args: ["username", "chat_name"]` | Medium |
| `frontend/frontend.py` -> `get_filtered_models` | Signature | `def get_filtered_models(source_list, category_name: str)` | `ast_schema` defines `args: ["source_list", "category_name"]` | Medium |
| `frontend/frontend.py` -> `load_data_from_db` | Signature | `def load_data_from_db(username: str)` | `ast_schema` defines `args: ["username"]` | Medium |
| `frontend/frontend.py` -> `handle_delete_chat` | Signature | `def handle_delete_chat(username: str, chat_name: str)` | `ast_schema` defines `args: ["username", "chat_name"]` | Medium |
| `frontend/frontend.py` -> `extract_repo_name` | Signature | `def extract_repo_name(text: str)` | `ast_schema` defines `args: ["text"]` | Medium |
| `frontend/frontend.py` -> `stream_text_generator` | Signature | `def stream_text_generator(text: str)` | `ast_schema` defines `args: ["text"]` | Medium |
| `frontend/frontend.py` -> `render_text_with_mermaid` | Signature | `def render_text_with_mermaid(markdown_text: str, should_stream: bool = False)` | `ast_schema` defines `args: ["markdown_text", "should_stream"]` | Medium |
| `frontend/frontend.py` -> `render_exchange` | Signature | `def render_exchange(ex: dict, current_chat_name: str)` | `ast_schema` defines `args: ["ex", "current_chat_name"]` | Medium |

## 2. 📊 Detailed Scoring & Justification

### 📦 Completeness & Coverage (Weight: 30%)
**Score: 10/10**
**Analysis:**
- All files, classes, and functions present in the `file_tree` and `ast_schema` are covered in the documentation.
- Project metadata (Description, Key Features, Tech Stack, Installation, Quick Start Guide) was correctly synthesized from the code context, as `basic_info` explicitly stated "Information not found" for these fields. The synthesized information is accurate and consistent with the project's dependencies and functionality.
- The repository structure diagram (Mermaid) accurately reflects the `file_tree`.
**Deductions:** None.

### 🎯 Technical Accuracy (Weight: 20%)
**Score: 0/10**
**Analysis:**
- **Function/Method Signatures**: There are widespread discrepancies in the documented function and method signatures compared to the `ast_schema`.
    - **Omission of `self`**: For 57 instance methods, the `self` parameter is omitted from the documented signature line. While common in some documentation styles, this is a factual deviation from the `ast_schema` which explicitly lists `self` in its `args` list. This is a high-severity error as it misrepresents the number of arguments.
    - **Addition of Type Hints and Default Values**: For 60 functions/methods, type hints and/or default values are added to the signature line. While this information is correctly inferred from the source code and `analysis_results` (and is accurately presented in the "Parameters" section), the `ast_schema`'s `args` list only contains parameter names. Including this additional information in the signature line is a deviation from the strict `ast_schema` representation. This is a medium-severity error.
- The sheer volume and consistency of these signature discrepancies indicate a systemic issue in how signatures are generated from the AST schema.
**Deductions:**
- **-5 points**: Consistent omission of `self` from method signatures (57 instances).
- **-5 points**: Consistent addition of type hints and default values to function/method signatures not explicitly present in `ast_schema.args` (60 instances).

### 🎯 Description Accuracy (Weight: 20%)
**Score: 10/10**
**Analysis:**
- The overall descriptions, parameter descriptions, return descriptions, and usage contexts for all functions and classes are directly copied from the `analysis_results` section of the Ground Truth. These descriptions are accurate and reflect the purpose and functionality of the code.
- The minor issue of `null` being used as a return value name in `backend/File_Dependency.py -> FileDependencyGraph._resolve_module_name` is present in the `analysis_results` itself, and the documentation accurately reflects this, so no deduction is made for the documentation.
**Deductions:** None.

### 🧠 Logic & Relationships (Weight: 15%)
**Score: 10/10**
**Analysis:**
- The "Usage" sections for functions and "Instantiation" / "Dependencies" for classes accurately reflect the `calls`, `called_by`, `dependencies`, and `instantiated_by` information provided in the `analysis_results`.
- The documentation correctly states when a function calls no other functions or is not explicitly called by others, based on the provided context.
**Deductions:** None.

### 📖 Readability & Structure (Weight: 15%)
**Score: 10/10**
**Analysis:**
- The Markdown formatting is valid, headings are nested correctly, and the overall structure is clear and easy to navigate.
- Code blocks are used appropriately for dependencies and code examples.
- The Mermaid diagram for the repository structure is correctly rendered. The note about Mermaid syntax not being set up for architecture diagrams is a meta-comment about the documentation generation process, not an error in the generated content itself.
**Deductions:** None.

---
**TOTAL SCORE: 70/100**
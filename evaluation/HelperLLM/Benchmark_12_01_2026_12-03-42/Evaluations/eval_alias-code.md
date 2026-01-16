# Helper LLM Analysis Report

## 1. 🔍 Error Log
*Identify mismatches between Source Code and Generated JSON.*

| Identifier | Issue Type | Input Data (Ground Truth) | LLM Output | Severity |
|---|---|---|---|---|
| `frontend.frontend.stream_text_generator` | Type Error | Returns `generator` | Returns `[]` | Medium |
| `backend.MainLLM.MainLLM.call_llm` | Type Error | Returns `str` or `None` | Returns `str` | Medium |
| `backend.MainLLM.MainLLM.stream_llm` | Type Error | Returns `generator` | Returns `str` | Medium |
| `frontend.frontend.extract_repo_name` | Type Error | Returns `str` or `None` | Returns `str` | Minor |
| `backend.AST_Schema.ASTVisitor.__init__` | Hallucination | `context.method_context[0].calls`: `["backend.AST_Schema.path_to_module"]` | `usage_context.calls`: "This method does not call any other functions directly." | High |
| `backend.AST_Schema.ASTVisitor.visit_AsyncFunctionDef` | Hallucination | `context.method_context[5].calls`: `[]` (but source calls `self.visit_FunctionDef`) | `usage_context.calls`: "This method does not call any other functions directly." | High |
| `backend.AST_Schema.ASTAnalyzer.__init__` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.AST_Schema.ASTAnalyzer.merge_relationship_data` | Parameter Accuracy | `args`: `["self", "full_schema", "raw_relationships"]` | `parameters`: `full_schema: dict`, `raw_relationships: dict` | Medium |
| `backend.AST_Schema.ASTAnalyzer.analyze_repository` | Parameter Accuracy | `args`: `["self", "files", "repo"]` | `parameters`: `files: list`, `repo: GitRepository` | Medium |
| `backend.File_Dependency.FileDependencyGraph._resolve_module_name` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ImportFrom` | Medium |
| `backend.File_Dependency.FileDependencyGraph.module_file_exists` | Type Error | Returns `bool` | Returns `[]` | Medium |
| `backend.File_Dependency.FileDependencyGraph.init_exports_symbol` | Type Error | Returns `bool` | Returns `[]` | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_Import` | Parameter Accuracy | `args`: `["self", "node", "base_name"]` | `parameters`: `node: Import | ImportFrom`, `base_name: str | None` | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ImportFrom` | Medium |
| `backend.HelperLLM.LLMHelper` | Hallucination | `context.dependencies`: `[]` | `dependencies`: "This class depends on several external libraries..." | High |
| `backend.HelperLLM.LLMHelper` | Hallucination | `context.instantiated_by`: `[]` | `instantiated_by`: "This class is instantiated by components within the backend.HelperLLM module..." | High |
| `backend.HelperLLM.LLMHelper.__init__` | Hallucination | `context.method_context[0].calls`: `[]` (but source calls `_configure_batch_settings`, `ChatGoogleGenerativeAI` etc.) | `usage_context.calls`: "This method does not call any other functions." | High |
| `backend.HelperLLM.LLMHelper._configure_batch_settings` | Hallucination | `context.method_context[1].called_by`: `[]` (but source is called by `__init__`) | `usage_context.called_by`: "Called by the __init__ method of the LLMHelper class." | High |
| `backend.HelperLLM.LLMHelper.generate_for_functions` | Hallucination | `context.method_context[2].calls`: `[]` (but source calls `json.dumps`, `self.function_llm.batch` etc.) | `usage_context.calls`: "This method uses the self.function_llm client..." | High |
| `backend.HelperLLM.LLMHelper.generate_for_functions` | Hallucination | `context.method_context[2].called_by`: `[]` | `usage_context.called_by`: "This method is invoked externally to generate documentation for functions." | High |
| `backend.HelperLLM.LLMHelper.generate_for_classes` | Hallucination | `context.method_context[3].calls`: `[]` (but source calls `json.dumps`, `self.class_llm.batch` etc.) | `usage_context.calls`: "This method uses the self.class_llm client..." | High |
| `backend.HelperLLM.LLMHelper.generate_for_classes` | Hallucination | `context.method_context[3].called_by`: `[]` | `usage_context.called_by`: "This method is invoked externally to generate documentation for classes." | High |
| `backend.basic_info.ProjektInfoExtractor.__init__` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.basic_info.ProjektInfoExtractor._clean_content` | Parameter Accuracy | `args`: `["self", "content"]` | `parameters`: `content: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor._clean_content` | Hallucination | `context.method_context[1].called_by`: `[]` | `usage_context.called_by`: "Called by _parse_readme, _parse_toml, and _parse_requirements." | High |
| `backend.basic_info.ProjektInfoExtractor._finde_datei` | Parameter Accuracy | `args`: `["self", "patterns", "dateien"]` | `parameters`: `patterns: List[str]`, `dateien: List[Any]` | Medium |
| `backend.basic_info.ProjektInfoExtractor._finde_datei` | Hallucination | `context.method_context[2].called_by`: `[]` | `usage_context.called_by`: "Called by extrahiere_info." | High |
| `backend.basic_info.ProjektInfoExtractor._extrahiere_sektion_aus_markdown` | Parameter Accuracy | `args`: `["self", "inhalt", "keywords"]` | `parameters`: `inhalt: str`, `keywords: List[str]` | Medium |
| `backend.basic_info.ProjektInfoExtractor._extrahiere_sektion_aus_markdown` | Hallucination | `context.method_context[3].called_by`: `[]` | `usage_context.called_by`: "Called by _parse_readme." | High |
| `backend.basic_info.ProjektInfoExtractor._parse_readme` | Parameter Accuracy | `args`: `["self", "inhalt"]` | `parameters`: `inhalt: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_readme` | Hallucination | `context.method_context[4].calls`: `[]` (but source calls `_clean_content`, `_extrahiere_sektion_aus_markdown`) | `usage_context.calls`: "_clean_content, _extrahiere_sektion_aus_markdown" | High |
| `backend.basic_info.ProjektInfoExtractor._parse_readme` | Hallucination | `context.method_context[4].called_by`: `[]` | `usage_context.called_by`: "Called by extrahiere_info." | High |
| `backend.basic_info.ProjektInfoExtractor._parse_toml` | Parameter Accuracy | `args`: `["self", "inhalt"]` | `parameters`: `inhalt: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_toml` | Hallucination | `context.method_context[5].calls`: `[]` (but source calls `_clean_content`) | `usage_context.calls`: "_clean_content" | High |
| `backend.basic_info.ProjektInfoExtractor._parse_toml` | Hallucination | `context.method_context[5].called_by`: `[]` | `usage_context.called_by`: "Called by extrahiere_info." | High |
| `backend.basic_info.ProjektInfoExtractor._parse_requirements` | Parameter Accuracy | `args`: `["self", "inhalt"]` | `parameters`: `inhalt: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_requirements` | Hallucination | `context.method_context[6].calls`: `[]` (but source calls `_clean_content`) | `usage_context.calls`: "_clean_content" | High |
| `backend.basic_info.ProjektInfoExtractor._parse_requirements` | Hallucination | `context.method_context[6].called_by`: `[]` | `usage_context.called_by`: "Called by extrahiere_info." | High |
| `backend.basic_info.ProjektInfoExtractor.extrahiere_info` | Parameter Accuracy | `args`: `["self", "dateien", "repo_url"]` | `parameters`: `dateien: List[Any]`, `repo_url: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor.extrahiere_info` | Hallucination | `context.method_context[7].calls`: `[]` (but source calls `_finde_datei`, `_parse_toml` etc.) | `usage_context.calls`: "_finde_datei, _parse_toml, _parse_requirements, _parse_readme" | High |
| `backend.callgraph.CallGraph` | Hallucination | `context.dependencies`: `[]` | `dependencies`: "This class depends on the ast module..." | High |
| `backend.callgraph.CallGraph` | Hallucination | `context.instantiated_by`: `[]` | `instantiated_by`: "This class is instantiated by the getRepo.GitRepository and basic_info.ProjektInfoExtractor classes." | High |
| `backend.callgraph.CallGraph._recursive_call` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.AST` | Medium |
| `backend.callgraph.CallGraph._recursive_call` | Hallucination | `context.method_context[1].calls`: `[]` (but source calls `self._recursive_call`) | `usage_context.calls`: "This method does not call any other functions." | High |
| `backend.callgraph.CallGraph._recursive_call` | Hallucination | `context.method_context[1].called_by`: `[]` | `usage_context.called_by`: "This method is called by the _resolve_all_callee_names method." | High |
| `backend.callgraph.CallGraph._resolve_all_callee_names` | Parameter Accuracy | `args`: `["self", "callee_nodes"]` | `parameters`: `callee_nodes: list[list[str]]` | Medium |
| `backend.callgraph.CallGraph._resolve_all_callee_names` | Hallucination | `context.method_context[2].calls`: `[]` (but source calls `self._recursive_call`) | `usage_context.calls`: "This method calls the _recursive_call method..." | High |
| `backend.callgraph.CallGraph._resolve_all_callee_names` | Hallucination | `context.method_context[2].called_by`: `[]` | `usage_context.called_by`: "This method is called by the visit_Call method." | High |
| `backend.callgraph.CallGraph._make_full_name` | Parameter Accuracy | `args`: `["self", "basename", "class_name"]` | `parameters`: `basename: str`, `class_name: Optional[str]` | Medium |
| `backend.callgraph.CallGraph._make_full_name` | Hallucination | `context.method_context[3].called_by`: `[]` | `usage_context.called_by`: "This method is called by the visit_FunctionDef method." | High |
| `backend.callgraph.CallGraph._current_caller` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.callgraph.CallGraph._current_caller` | Hallucination | `context.method_context[4].called_by`: `[]` | `usage_context.called_by`: "This method is called by the visit_Call method." | High |
| `backend.callgraph.CallGraph.visit_Import` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.Import` | Medium |
| `backend.callgraph.CallGraph.visit_Import` | Hallucination | `context.method_context[5].calls`: `[]` (but source calls `self.generic_visit`) | `usage_context.calls`: "This method calls the generic_visit method..." | High |
| `backend.callgraph.CallGraph.visit_Import` | Hallucination | `context.method_context[5].called_by`: `[]` | `usage_context.called_by`: "This method is called during AST traversal." | High |
| `backend.callgraph.CallGraph.visit_ImportFrom` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.ImportFrom` | Medium |
| `backend.callgraph.CallGraph.visit_ImportFrom` | Hallucination | `context.method_context[6].calls`: `[]` (but source calls `self.generic_visit`) | `usage_context.calls`: "This method calls the generic_visit method..." | High |
| `backend.callgraph.CallGraph.visit_ImportFrom` | Hallucination | `context.method_context[6].called_by`: `[]` | `usage_context.called_by`: "This method is called during AST traversal." | High |
| `backend.callgraph.CallGraph.visit_ClassDef` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.ClassDef` | Medium |
| `backend.callgraph.CallGraph.visit_ClassDef` | Hallucination | `context.method_context[7].calls`: `[]` (but source calls `self.generic_visit`) | `usage_context.calls`: "This method calls the generic_visit method..." | High |
| `backend.callgraph.CallGraph.visit_ClassDef` | Hallucination | `context.method_context[7].called_by`: `[]` | `usage_context.called_by`: "This method is called during AST traversal." | High |
| `backend.callgraph.CallGraph.visit_FunctionDef` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.FunctionDef` | Medium |
| `backend.callgraph.CallGraph.visit_FunctionDef` | Hallucination | `context.method_context[8].calls`: `[]` (but source calls `self._make_full_name`, `self.generic_visit`) | `usage_context.calls`: "This method calls the _make_full_name and generic_visit methods." | High |
| `backend.callgraph.CallGraph.visit_FunctionDef` | Hallucination | `context.method_context[8].called_by`: `[]` | `usage_context.called_by`: "This method is called during AST traversal." | High |
| `backend.callgraph.CallGraph.visit_AsyncFunctionDef` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.AsyncFunctionDef` | Medium |
| `backend.callgraph.CallGraph.visit_AsyncFunctionDef` | Hallucination | `context.method_context[9].calls`: `[]` (but source calls `self.visit_FunctionDef`) | `usage_context.calls`: "This method calls the visit_FunctionDef method." | High |
| `backend.callgraph.CallGraph.visit_AsyncFunctionDef` | Hallucination | `context.method_context[9].called_by`: `[]` | `usage_context.called_by`: "This method is called during AST traversal." | High |
| `backend.callgraph.CallGraph.visit_Call` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.Call` | Medium |
| `backend.callgraph.CallGraph.visit_Call` | Hallucination | `context.method_context[10].calls`: `[]` (but source calls `self._current_caller`, `self._recursive_call`, `self._resolve_all_callee_names`) | `usage_context.calls`: "This method calls the _current_caller, _recursive_call, and _resolve_all_callee_names methods." | High |
| `backend.callgraph.CallGraph.visit_Call` | Hallucination | `context.method_context[10].called_by`: `[]` | `usage_context.called_by`: "This method is called during AST traversal." | High |
| `backend.callgraph.CallGraph.visit_If` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.If` | Medium |
| `backend.callgraph.CallGraph.visit_If` | Hallucination | `context.method_context[11].calls`: `[]` (but source calls `self.generic_visit`) | `usage_context.calls`: "This method calls the generic_visit method..." | High |
| `backend.callgraph.CallGraph.visit_If` | Hallucination | `context.method_context[11].called_by`: `[]` | `usage_context.called_by`: "This method is called during AST traversal." | High |
| `backend.getRepo.RepoFile` | Hallucination | `context.dependencies`: `[]` | `dependencies`: "This class does not depend on any external modules..." | High |
| `backend.getRepo.RepoFile.blob` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.getRepo.RepoFile.content` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.getRepo.RepoFile.content` | Hallucination | `context.method_context[2].calls`: `[]` (but source calls `self.blob.data_stream.read().decode`) | `usage_context.calls`: "This method does not call any other functions." | High |
| `backend.getRepo.RepoFile.size` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.getRepo.RepoFile.size` | Hallucination | `context.method_context[3].calls`: `[]` (but source calls `self.blob.size`) | `usage_context.calls`: "This method does not call any other functions." | High |
| `backend.getRepo.RepoFile.analyze_word_count` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.getRepo.RepoFile.analyze_word_count` | Hallucination | `context.method_context[4].calls`: `[]` (but source calls `self.content.split()`) | `usage_context.calls`: "This method does not call any other functions." | High |
| `backend.getRepo.RepoFile.__repr__` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.getRepo.RepoFile.to_dict` | Parameter Accuracy | `args`: `["self", "include_content"]` | `parameters`: `include_content: bool` | Medium |
| `backend.getRepo.RepoFile.to_dict` | Hallucination | `context.method_context[6].calls`: `[]` (but source calls `self.size`, `self.content`) | `usage_context.calls`: "This method does not call any other functions." | High |
| `backend.getRepo.GitRepository.__init__` | Hallucination | `context.method_context[0].calls`: `[]` (but source calls `tempfile.mkdtemp`, `Repo.clone_from`, `self.close`) | `usage_context.calls`: "This method does not call any other functions." | High |
| `backend.getRepo.GitRepository.__exit__` | Hallucination | `context.method_context[4].calls`: `[]` (but source calls `self.close()`) | `usage_context.calls`: "This method does not call any other functions." | High |
| `backend.getRepo.GitRepository.get_file_tree` | Hallucination | `context.method_context[5].calls`: `[]` (but source calls `self.get_all_files`, `file_obj.to_dict`) | `usage_context.calls`: "This method does not call any other functions directly." | High |
| `backend.relationship_analyzer.ProjectAnalyzer.analyze` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer.analyze` | Hallucination | `context.method_context[1].calls`: `[]` (but source calls `_find_py_files`, `_collect_definitions`, `_resolve_calls`) | `usage_context.calls`: "This method does not explicitly call any other methods defined within the class itself." | High |
| `backend.relationship_analyzer.ProjectAnalyzer.get_raw_relationships` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._find_py_files` | Parameter Accuracy | `args`: `["self"]` | `parameters`: `[]` | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._collect_definitions` | Parameter Accuracy | `args`: `["self", "filepath"]` | `parameters`: `filepath: str` | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._get_parent` | Parameter Accuracy | `args`: `["self", "tree", "node"]` | `parameters`: `tree: ast.AST`, `node: ast.AST` | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._resolve_calls` | Parameter Accuracy | `args`: `["self", "filepath"]` | `parameters`: `filepath: str` | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_ClassDef` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.ClassDef` | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_FunctionDef` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.FunctionDef` | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Call` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.Call` | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Call` | Hallucination | `context.method_context[3].calls`: `[]` (but source calls `self._resolve_call_qname`) | `usage_context.calls`: "This method calls the private helper method `_resolve_call_qname`..." | High |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Import` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.Import` | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_ImportFrom` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.ImportFrom` | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Assign` | Parameter Accuracy | `args`: `["self", "node"]` | `parameters`: `node: ast.Assign` | Medium |
| `backend.relationship_analyzer.CallResolverVisitor._resolve_call_qname` | Parameter Accuracy | `args`: `["self", "func_node"]` | `parameters`: `func_node: ast.expr` | Medium |
| `backend.relationship_analyzer.CallResolverVisitor._resolve_call_qname` | Hallucination | `context.method_context[7].called_by`: `[]` | `usage_context.called_by`: "This method is called by the `visit_Call` method..." | High |
| `schemas.types.ParameterDescription` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.ReturnDescription` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.UsageContext` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.FunctionDescription` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.FunctionDescription.__init__` | Parameter Accuracy | Pydantic fields: `overall`, `parameters`, `returns`, `usage_context` | `parameters`: `[]` | Medium |
| `schemas.types.FunctionAnalysis` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.ConstructorDescription` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.ClassContext` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.ClassDescription` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.ClassAnalysis` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.CallInfo` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.FunctionContextInput` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.FunctionContextInput.__init__` | Parameter Accuracy | Pydantic fields: `calls`, `called_by` | `parameters`: `[]` | Medium |
| `schemas.types.FunctionContextInput.calls` | Hallucination | `context.method_context`: `[]` (This is a field, not a method) | `methods` entry exists | High |
| `schemas.types.FunctionContextInput.called_by` | Hallucination | `context.method_context`: `[]` (This is a field, not a method) | `methods` entry exists | High |
| `schemas.types.FunctionAnalysisInput` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.MethodContextInput` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.ClassContextInput` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |
| `schemas.types.ClassAnalysisInput` | Hallucination | `context.method_context`: `[]` | `init_method` entry exists | High |

## 2. 📊 Scoring

### 🎯 Signature & Type Accuracy (Weight: 30%)
**Score: 0/10**
**Analysis:** The model frequently failed to correctly identify the `self` parameter in method signatures, omitting it from the `parameters` list. It also made several incorrect inferences for return types (e.g., `[]` for `generator` or `bool`, `str` for `str or None`). For Pydantic models, it incorrectly generated `init_method` entries with empty parameter lists or incorrect parameter lists, despite the ground truth `method_context` being empty.

### 🧠 Logic Description (Weight: 40%)
**Score: 10/10**
**Analysis:** The `overall` descriptions for functions and classes were generally accurate and provided a good summary of the code's functionality. No significant vagueness or factual errors were detected in the descriptive text itself.

### 🔗 Context Integration (Weight: 30%)
**Score: 0/10**
**Analysis:** The model exhibited severe hallucination issues regarding `calls`, `called_by`, `dependencies`, and `instantiated_by` within classes and methods. It frequently ignored the explicit empty lists provided in the `context` object of the ground truth, instead inferring calls from the source code or making up descriptive sentences about usage. This directly violates the critical rule to "TRUST ONLY THE 'context' OBJECT IN PART 1". Additionally, it hallucinated `init_method` entries for Pydantic `BaseModel` classes where no such method was explicitly defined in the ground truth `method_context`.

---
**TOTAL SCORE: 40/100**
---
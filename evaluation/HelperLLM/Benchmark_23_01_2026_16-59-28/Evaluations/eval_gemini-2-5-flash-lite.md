# Helper LLM Analysis Report

## 1. 🔍 Error Log
*Identify mismatches between Source Code and Generated JSON.*

| Identifier | Issue Type | Input Data (Ground Truth) | LLM Output | Severity |
|---|---|---|---|---|
| `backend.converter.process_image` | Type Error (Return) | Returns `str | None` | Returns `str` | Medium |
| `backend.main.calculate_net_time` | Type Error (Return) | Returns `float` | Returns `int` | Medium |
| `backend.main.main_workflow` | Description Vagueness (Return) | Returns `dict` with `report: str`, `metrics: dict` | Returns `report: str`, `metrics: dict` | Minor |
| `backend.main.notebook_workflow` | Description Vagueness (Return) | Returns `dict` with `report: str`, `metrics: dict` | Returns `report: str`, `metrics: dict` | Minor |
| `database.db.get_decrypted_api_keys` | Type Error (Return) | Returns `Tuple[str, ..., str] | Tuple[None, ..., None]` | Returns `str, ..., str` | Medium |
| `database.db.insert_exchange` | Type Error (Return) | Returns `str | None` | Returns `str` | Medium |
| `backend.File_Dependency.FileDependencyGraph.module_file_exists` | Type Error (Return) | Returns `bool` | Returns `[]` | High |
| `backend.File_Dependency.FileDependencyGraph.init_exports_symbol` | Type Error (Return) | Returns `bool` | Returns `[]` | High |
| `backend.File_Dependency.FileDependencyGraph.module_file_exists` | Logic Extraction (Missing Description) | Docstring is `null` | Description is missing | Medium |
| `backend.File_Dependency.FileDependencyGraph.init_exports_symbol` | Logic Extraction (Missing Description) | Docstring is `null` | Description is missing | Medium |
| `backend.MainLLM.MainLLM.call_llm` | Type Error (Return) | Returns `str | None` | Returns `str` | Medium |
| `backend.MainLLM.MainLLM.stream_llm` | Type Error (Return) | Returns `Iterator[str]` | Returns `str` | Medium |
| `backend.File_Dependency.FileDependencyGraph._resolve_module_name` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.File_Dependency.FileDependencyGraph.visit_Import` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.File_Dependency.FileDependencyGraph.visit_Import` | Type Error (Parameter) | `self: FileDependencyGraph` | `self: ASTVisitor` | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Type Error (Parameter) | `self: FileDependencyGraph` | `self: ASTVisitor` | Medium |
| `backend.HelperLLM.LLMHelper.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.HelperLLM.LLMHelper._configure_batch_settings` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.HelperLLM.LLMHelper.generate_for_functions` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.HelperLLM.LLMHelper.generate_for_classes` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.MainLLM.MainLLM.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.MainLLM.MainLLM.call_llm` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.MainLLM.MainLLM.stream_llm` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph._recursive_call` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph._resolve_all_callee_names` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph._make_full_name` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph._current_caller` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph.visit_Import` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph.visit_ImportFrom` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph.visit_ClassDef` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph.visit_FunctionDef` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph.visit_AsyncFunctionDef` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph.visit_Call` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.callgraph.CallGraph.visit_If` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.RepoFile.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.RepoFile.blob` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.RepoFile.content` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.RepoFile.size` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.RepoFile.analyze_word_count` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.RepoFile.__repr__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.RepoFile.to_dict` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.GitRepository.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.getRepo.GitRepository.get_file_tree` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.ProjectAnalyzer.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.ProjectAnalyzer.analyze` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.ProjectAnalyzer.get_raw_relationships` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.ProjectAnalyzer._find_py_files` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.ProjectAnalyzer._collect_definitions` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.ProjectAnalyzer._get_parent` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.ProjectAnalyzer._resolve_calls` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.CallResolverVisitor.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.CallResolverVisitor.visit_ClassDef` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.CallResolverVisitor.visit_FunctionDef` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Call` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Import` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.CallResolverVisitor.visit_ImportFrom` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Assign` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.relationship_analyzer.CallResolverVisitor._resolve_call_qname` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.ParameterDescription.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.ReturnDescription.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.UsageContext.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.FunctionDescription.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.FunctionDescription.__init__` | Parameter Accuracy | Pydantic attributes as params | `[]` | Medium |
| `schemas.types.FunctionAnalysis.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.ConstructorDescription.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.ClassContext.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.ClassContext.__init__` | Parameter Accuracy | Pydantic attributes as params | `[]` | Medium |
| `schemas.types.ClassDescription.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.ClassAnalysis.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.CallInfo.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.FunctionContextInput.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.FunctionAnalysisInput.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.MethodContextInput.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.ClassContextInput.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `schemas.types.ClassAnalysisInput.__init__` | Parameter Accuracy | `self` parameter present | `self` parameter missing | High |
| `backend.AST_Schema.ASTVisitor.visit_Import` | Hallucination (Calls) | `[]` | `generic_visit` | High |
| `backend.AST_Schema.ASTVisitor.visit_ImportFrom` | Hallucination (Calls) | `[]` | `generic_visit` | High |
| `backend.AST_Schema.ASTVisitor.visit_ClassDef` | Hallucination (Calls) | `[]` | `ast.get_docstring`, `ast.get_source_segment`, `generic_visit` | High |
| `backend.AST_Schema.ASTVisitor.visit_FunctionDef` | Hallucination (Calls) | `[]` | `ast.get_docstring`, `ast.get_source_segment`, `generic_visit` | High |
| `backend.AST_Schema.ASTVisitor.visit_AsyncFunctionDef` | Hallucination (Calls) | `[]` | `visit_FunctionDef` | High |
| `backend.AST_Schema.ASTAnalyzer.merge_relationship_data` | Hallucination (Calls) | `[]` | Internal operations | High |
| `backend.AST_Schema.ASTAnalyzer.analyze_repository` | Hallucination (Calls) | `["backend.AST_Schema.ASTVisitor"]` | `ast.parse`, `os.path` functions, `visit` method call | High |
| `backend.File_Dependency.FileDependencyGraph._resolve_module_name` | Hallucination (Called By) | `[]` | `visit_ImportFrom` | High |
| `backend.File_Dependency.FileDependencyGraph.module_file_exists` | Hallucination (Called By) | `[]` | `content` and `size` properties | High |
| `backend.File_Dependency.FileDependencyGraph.init_exports_symbol` | Hallucination (Called By) | `[]` | `content` and `size` properties | High |
| `backend.File_Dependency.FileDependencyGraph.visit_Import` | Hallucination (Calls) | `[]` |
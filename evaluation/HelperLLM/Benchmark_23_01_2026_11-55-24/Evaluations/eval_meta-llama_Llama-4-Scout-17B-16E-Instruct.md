# Helper LLM Analysis Report

## 1. 🔍 Error Log
*Identify mismatches between Source Code and Generated JSON.*

| Identifier | Issue Type | Input Data (Ground Truth) | LLM Output | Severity |
|---|---|---|---|---|
| `backend.HelperLLM.main_orchestrator` | Context Omission | `calls`: `["schemas.types.ClassContextInput"]` | `calls`: Missing `schemas.types.ClassContextInput` | High |
| `backend.HelperLLM.main_orchestrator` | Context Hallucination | `calls`: `[]` (for `FunctionAnalysisInput.model_validate`) | `calls`: `FunctionAnalysisInput.model_validate` | High |
| `backend.HelperLLM.main_orchestrator` | Context Formatting | `called_by`: `[]` | `called_by`: `""` | Minor |
| `backend.main.calculate_net_time` | Parameter Type Error | `start_time`, `end_time`: `float` | `start_time`, `end_time`: `datetime` | Medium |
| `backend.main.calculate_net_time` | Return Type Error | Returns `float` | Returns `int` | Medium |
| `backend.main.main_workflow` | Context Omission | `calls`: `["schemas.types.ClassAnalysisInput", "schemas.types.ClassContextInput", "schemas.types.FunctionAnalysisInput", "schemas.types.FunctionContextInput", "schemas.types.MethodContextInput"]` | `calls`: Missing 5 schema type calls | High |
| `database.db.update_exchange_feedback_message` | Parameter Type Error | `exchange_id`: `str` | `exchange_id`: `objectId` | Medium |
| `frontend.frontend.stream_text_generator` | Return Type Error | Returns `Generator[str, None, None]` | Returns `[]` | Medium |
| `frontend.frontend.handle_feedback_change` | Parameter Type Error | `val`: `int` | `val`: `str` | Medium |
| `backend.AST_Schema.ASTVisitor.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.AST_Schema.ASTVisitor.visit_Import` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.AST_Schema.ASTVisitor.visit_ImportFrom` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.AST_Schema.ASTVisitor.visit_ClassDef` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.AST_Schema.ASTVisitor.visit_FunctionDef` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.AST_Schema.ASTVisitor.visit_AsyncFunctionDef` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.AST_Schema.ASTAnalyzer.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.AST_Schema.ASTAnalyzer.merge_relationship_data` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.AST_Schema.ASTAnalyzer.analyze_repository` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.File_Dependency.FileDependencyGraph.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.File_Dependency.FileDependencyGraph.__init__` | Description Inaccuracy | Description implies call to `path_to_module` | `usage_context.calls` is empty (correct per context, but description is misleading) | Minor |
| `backend.File_Dependency.FileDependencyGraph._resolve_module_name` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_Import` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Context Hallucination | `calls`: `[]` | `calls`: `_resolve_module_name` | High |
| `backend.File_Dependency.FileDependencyGraph.module_file_exists` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.File_Dependency.FileDependencyGraph.init_exports_symbol` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.HelperLLM.LLMHelper.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.HelperLLM.LLMHelper._configure_batch_settings` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.HelperLLM.LLMHelper.generate_for_functions` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.HelperLLM.LLMHelper.generate_for_functions` | Context Hallucination | `calls`: `[]` | `calls`: "language model API" | High |
| `backend.HelperLLM.LLMHelper.generate_for_classes` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.HelperLLM.LLMHelper.generate_for_classes` | Context Hallucination | `calls`: `[]` | `calls`: "language model API" | High |
| `backend.MainLLM.MainLLM.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.MainLLM.MainLLM.call_llm` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.MainLLM.MainLLM.stream_llm` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.MainLLM.MainLLM.stream_llm` | Return Type Error | Returns `Generator[str, None, None]` | Returns `[]` | Medium |
| `backend.basic_info.ProjektInfoExtractor.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.basic_info.ProjektInfoExtractor._clean_content` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.basic_info.ProjektInfoExtractor._finde_datei` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.basic_info.ProjektInfoExtractor._extrahiere_sektion_aus_markdown` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_readme` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_toml` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_requirements` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.basic_info.ProjektInfoExtractor.extrahiere_info` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph._recursive_call` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph._resolve_all_callee_names` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph._make_full_name` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph._current_caller` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph.visit_Import` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph.visit_ImportFrom` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph.visit_ClassDef` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph.visit_FunctionDef` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph.visit_AsyncFunctionDef` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph.visit_Call` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.callgraph.CallGraph.visit_If` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.RepoFile.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.RepoFile.blob` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.RepoFile.content` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.RepoFile.size` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.RepoFile.analyze_word_count` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.RepoFile.__repr__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.RepoFile.to_dict` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.GitRepository.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.GitRepository.get_all_files` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.GitRepository.close` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.GitRepository.__enter__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.GitRepository.__exit__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.GitRepository.__exit__` | Context Hallucination | `calls`: `[]` | `calls`: `close` method | High |
| `backend.getRepo.GitRepository.get_file_tree` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.getRepo.GitRepository.get_file_tree` | Context Hallucination | `calls`: `[]` | `calls`: `get_all_files` method | High |
| `backend.relationship_analyzer.ProjectAnalyzer.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer.analyze` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer.analyze` | Context Hallucination | `calls`: `[]` | `calls`: `_find_py_files`, `_collect_definitions`, `_resolve_calls` | High |
| `backend.relationship_analyzer.ProjectAnalyzer.get_raw_relationships` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._find_py_files` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._collect_definitions` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._get_parent` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._resolve_calls` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.__init__` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.__init__` | Context Omission | `calls`: `["backend.relationship_analyzer.path_to_module"]` | `calls`: `""` | High |
| `backend.relationship_analyzer.CallResolverVisitor.visit_ClassDef` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_FunctionDef` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Call` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Import` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_ImportFrom` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Assign` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |
| `backend.relationship_analyzer.CallResolverVisitor._resolve_call_qname` | Parameter Omission | `self` parameter present | `self` parameter missing | Medium |

## 2. 📊 Scoring

### 🎯 Signature & Type Accuracy (Weight: 30%)
**Score: 1/10**
**Analysis:** The model consistently omits the `self` parameter from method signatures in classes, which is a critical error for Python methods. This accounts for 40 instances of missing parameters. Additionally, there are several incorrect type inferences for function parameters and return values (e.g., `datetime` instead of `float`, `int` instead of `float`, `objectId` instead of `str`, `[]` instead of `Generator`).

### 🧠 Logic Description (Weight: 40%)
**Score: 9/10**
**Analysis:** The `overall` descriptions are generally accurate and capture the core functionality of the functions and classes. There are a couple of minor instances where the description is slightly vague or implies a call that isn't explicitly listed in the `usage_context` (due to the strict interpretation of the `context` object), but these are not major logical errors in the description text itself.

### 🔗 Context Integration (Weight: 30%)
**Score: 4/10**
**Analysis:** This section shows significant discrepancies. The model frequently hallucinates calls that are not present in the `context` object provided in PART 1 (e.g., internal method calls that the `context` object explicitly marks as empty). Conversely, it also omits calls that *are* explicitly listed in the `context` object (e.g., `schemas.types.*Input` calls in `main_workflow`, `path_to_module` in `CallResolverVisitor.__init__`). The formatting for empty `called_by` lists is also inconsistent. The strict instruction to "TRUST ONLY THE 'context' OBJECT IN PART 1" highlights these as critical errors.

---
**TOTAL SCORE: 50/100**
---
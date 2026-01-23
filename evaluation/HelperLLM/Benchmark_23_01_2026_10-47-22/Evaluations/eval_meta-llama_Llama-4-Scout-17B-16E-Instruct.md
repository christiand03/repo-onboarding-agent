# Helper LLM Analysis Report

## 1. 🔍 Error Log
*Identify mismatches between Source Code and Generated JSON.*

| Identifier | Issue Type | Input Data (Ground Truth) | LLM Output | Severity |
|---|---|---|---|---|
| `backend.HelperLLM.main_orchestrator` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.HelperLLM.main_orchestrator` | Context Synthesis (calls) | `["backend.HelperLLM.LLMHelper", "schemas.types.ClassAnalysisInput", "schemas.types.ClassContextInput"]` | `LLMHelper, FunctionAnalysisInput.model_validate, ClassAnalysisInput` | Medium |
| `backend.HelperLLM.main_orchestrator` | Context Synthesis (called_by) | `[]` (empty list) | `""` (empty string) | Minor |
| `backend.callgraph.make_safe_dot` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.main.create_savings_chart` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.main.calculate_net_time` | Return Type Error | Returns `float` | Returns `int` | Medium |
| `backend.main.main_workflow` | Context Synthesis (calls) | `["backend.AST_Schema.ASTAnalyzer", ..., "schemas.types.MethodContextInput"]` (20 calls) | `ASTAnalyzer, ..., ProjectAnalyzer.get_raw_relationships` (15 calls) | High |
| `backend.main.update_status` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `database.db.update_exchange_feedback` | Parameter Type Error | `exchange_id` (implied `str`) | `exchange_id: objectId` | Medium |
| `database.db.update_exchange_feedback_message` | Parameter Type Error | `exchange_id` (implied `str`) | `exchange_id: objectId` | Medium |
| `frontend.frontend.save_gemini_cb` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `frontend.frontend.save_ollama_cb` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `frontend.frontend.load_data_from_db` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `frontend.frontend.handle_feedback_change` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `frontend.frontend.handle_delete_exchange` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `frontend.frontend.handle_delete_chat` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `frontend.frontend.stream_text_generator` | Return Type Error | Returns `Generator` | Returns `[]` | Medium |
| `frontend.frontend.render_text_with_mermaid` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `frontend.frontend.render_exchange` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.AST_Schema.ASTVisitor.__init__` | Context Synthesis (calls) | `["backend.AST_Schema.path_to_module"]` | `The constructor also calls the path_to_module function...` (missing identifier) | Medium |
| `backend.AST_Schema.ASTAnalyzer.analyze_repository` | Context Synthesis (calls) | `["backend.AST_Schema.ASTVisitor"]` | `The method calls the ASTVisitor class...` (missing identifier) | Medium |
| `backend.File_Dependency.FileDependencyGraph.__init__` | Parameter Type Error | `repo_root: str` | `repo_root: object` | Medium |
| `backend.File_Dependency.FileDependencyGraph._resolve_module_name` | Return Type Error | Returns `list[str]` | Returns `[]` | Minor |
| `backend.File_Dependency.FileDependencyGraph._resolve_module_name` | Context Synthesis (calls) | `["backend.File_Dependency.get_all_temp_files", ...]` (3 calls) | `This method calls get_all_temp_files, init_exports_symbol, and module_file_exists...` (missing identifiers) | High |
| `backend.File_Dependency.FileDependencyGraph.module_file_exists` | Return Type Error | Returns `bool` | Returns `[]` | Minor |
| `backend.File_Dependency.FileDependencyGraph.init_exports_symbol` | Return Type Error | Returns `bool` | Returns `[]` | Minor |
| `backend.File_Dependency.FileDependencyGraph.visit_Import` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Context Synthesis (calls) | `["backend.File_Dependency.FileDependencyGraph._resolve_module_name", ...]` (2 calls) | `""` (empty string) | High |
| `backend.HelperLLM.LLMHelper._configure_batch_settings` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.MainLLM.MainLLM.stream_llm` | Return Type Error | Returns `Generator` | Returns `[]` | Medium |
| `backend.basic_info.ProjektInfoExtractor._clean_content` | Return Type Error | Returns `str` | Returns `[]` | Minor |
| `backend.basic_info.ProjektInfoExtractor._parse_readme` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.basic_info.ProjektInfoExtractor._parse_readme` | Context Synthesis (calls) | `["backend.basic_info.ProjektInfoExtractor._clean_content", ...]` (2 calls) | `""` (empty string) | High |
| `backend.basic_info.ProjektInfoExtractor._parse_toml` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.basic_info.ProjektInfoExtractor._parse_toml` | Context Synthesis (calls) | `["backend.basic_info.ProjektInfoExtractor._clean_content"]` | `""` (empty string) | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_requirements` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.basic_info.ProjektInfoExtractor._parse_requirements` | Context Synthesis (calls) | `["backend.basic_info.ProjektInfoExtractor._clean_content"]` | `""` (empty string) | Medium |
| `backend.basic_info.ProjektInfoExtractor.extrahiere_info` | Context Synthesis (calls) | `["backend.basic_info.ProjektInfoExtractor._finde_datei", ...]` (4 calls) | `""` (empty string) | High |
| `backend.callgraph.CallGraph._recursive_call` | Return Type Error | Returns `list[str]` | Returns `[]` | Minor |
| `backend.callgraph.CallGraph.visit_Import` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.callgraph.CallGraph.visit_ImportFrom` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.callgraph.CallGraph.visit_ClassDef` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.callgraph.CallGraph.visit_FunctionDef` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.callgraph.CallGraph.visit_FunctionDef` | Context Synthesis (calls) | `["backend.callgraph.CallGraph._make_full_name"]` | `""` (empty string) | Medium |
| `backend.callgraph.CallGraph.visit_AsyncFunctionDef` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.callgraph.CallGraph.visit_AsyncFunctionDef` | Context Synthesis (calls) | `["backend.callgraph.CallGraph.visit_FunctionDef"]` | `""` (empty string) | Medium |
| `backend.callgraph.CallGraph.visit_Call` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.callgraph.CallGraph.visit_Call` | Context Synthesis (calls) | `["backend.callgraph.CallGraph._current_caller", ...]` (3 calls) | `""` (empty string) | High |
| `backend.callgraph.CallGraph.visit_If` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.getRepo.RepoFile.blob` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.getRepo.RepoFile.content` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.getRepo.RepoFile.size` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.getRepo.RepoFile.analyze_word_count` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.getRepo.RepoFile.__repr__` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.getRepo.GitRepository.get_all_files` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.getRepo.GitRepository.get_all_files` | Context Synthesis (calls) | `["backend.getRepo.RepoFile"]` | `This method calls the RepoFile class...` (missing identifier) | Medium |
| `backend.getRepo.GitRepository.close` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.getRepo.GitRepository.close` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.getRepo.GitRepository.__enter__` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.getRepo.GitRepository.__exit__` | Parameter Accuracy | `self, exc_type, exc_val, exc_tb` parameters present | `[]` (missing all parameters) | High |
| `backend.getRepo.GitRepository.__exit__` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.getRepo.GitRepository.__exit__` | Context Synthesis (calls) | `["backend.getRepo.GitRepository.close"]` | `This method calls the close method...` (missing identifier) | Medium |
| `backend.getRepo.GitRepository.get_file_tree` | Context Synthesis (calls) | `["backend.getRepo.GitRepository.get_all_files", "backend.getRepo.RepoFile.to_dict"]` | `This method calls the get_all_files method...` (missing identifiers) | High |
| `backend.relationship_analyzer.ProjectAnalyzer.analyze` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer.analyze` | Context Synthesis (calls) | `["backend.relationship_analyzer.ProjectAnalyzer._find_py_files", ...]` (3 calls) | `This method calls _find_py_files, _collect_definitions, and _resolve_calls...` (missing identifiers) | High |
| `backend.relationship_analyzer.ProjectAnalyzer.get_raw_relationships` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._find_py_files` | Parameter Accuracy | `self` parameter present | `[]` (missing `self`) | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._collect_definitions` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.relationship_analyzer.ProjectAnalyzer._collect_definitions` | Context Synthesis (calls) | `["backend.relationship_analyzer.path_to_module"]` | `This method calls path_to_module.` (missing identifier) | Medium |
| `backend.relationship_analyzer.ProjectAnalyzer._resolve_calls` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.relationship_analyzer.ProjectAnalyzer._resolve_calls` | Context Synthesis (calls) | `["backend.relationship_analyzer.CallResolverVisitor"]` | `This method calls CallResolverVisitor.` (missing identifier) | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.__init__` | Context Synthesis (calls) | `["backend.relationship_analyzer.path_to_module"]` | `""` (empty string) | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_ClassDef` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.relationship_analyzer.CallResolverVisitor.visit_FunctionDef` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Call` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Call` | Context Synthesis (calls) | `["backend.relationship_analyzer.CallResolverVisitor._resolve_call_qname"]` | `""` (empty string) | Medium |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Import` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.relationship_analyzer.CallResolverVisitor.visit_ImportFrom` | Return Type Error | Returns `None` | Returns `[]` | Minor |
| `backend.relationship_analyzer.CallResolverVisitor.visit_Assign` | Return Type Error | Returns `None` | Returns `[]` | Minor |

## 2. 📊 Scoring

### 🎯 Signature & Type Accuracy (Weight: 30%)
**Score: 0/10**
**Analysis:** The Helper LLM made numerous errors in identifying return types, frequently reporting `[]` (empty list) for functions that implicitly return `None` or explicitly return a specific type like `list[str]` or `Generator`. It also incorrectly inferred parameter types (e.g., `objectId` for `str`, `object` for `str`) and, critically, failed to include the `self` parameter for many instance methods, which is a fundamental aspect of Python method signatures.

### 🧠 Logic Description (Weight: 40%)
**Score: 10/10**
**Analysis:** The `overall` descriptions for all functions and classes were consistently accurate and well-summarized, reflecting the core functionality of the code snippets. No deductions were made in this category.

### 🔗 Context Integration (Weight: 30%)
**Score: 0/10**
**Analysis:** The model struggled significantly with context integration, particularly in the `usage_context.calls` field. It frequently omitted specific identifiers for called functions/classes, instead providing a descriptive sentence about the call without listing the actual identifiers from the ground truth `context` object. For several methods, it completely missed all `calls` listed in the ground truth. Minor issues included incorrect phrasing for `called_by` when no callers existed.

---
**TOTAL SCORE: 40/100**
---
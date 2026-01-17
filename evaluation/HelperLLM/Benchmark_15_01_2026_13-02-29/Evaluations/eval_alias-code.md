# Helper LLM Analysis Report

## 1. 🔍 Error Log
*Identify mismatches between Source Code and Generated JSON.*

| Identifier | Issue Type | Input Data (Ground Truth) | LLM Output | Severity |
|------------|------------|------------|----------------|----------|
| `backend.diagram_generation.generator.analyze_project` | Return Type Error | `resolved_calls: dict[str, list[ResolvedCall]]` | `resolved_calls: ResolvedCall` | Medium |
| `backend.AST_Schema.ASTAnalyzer.__init__` | Parameter Error | `self` | `[]` | Medium |
| `backend.AST_Schema.ASTAnalyzer.merge_relationship_data` | Parameter Error | `self, full_schema: dict, raw_relationships: dict` | `full_schema: dict, raw_relationships: dict` | Medium |
| `backend.AST_Schema.ASTAnalyzer.analyze_repository` | Parameter Error | `self, files: list, repo: GitRepository` | `files: list, repo: GitRepository` | Medium |
| `backend.File_Dependency.FileDependencyGraph.__init__` | Parameter Error | `self, filename: str, repo_root` | `filename: str, repo_root: Any` | Medium |
| `backend.File_Dependency.FileDependencyGraph._resolve_module_name` | Parameter Error | `self, node: ImportFrom` | `node: ImportFrom` | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_Import` | Parameter Error | `self, node: Import | ImportFrom, base_name: str | None = None` | `node: Import | ImportFrom, base_name: str | None` | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Parameter Error | `self, node: ImportFrom` | `node: ImportFrom` | Medium |
| `backend.File_Dependency.FileDependencyGraph.visit_ImportFrom` | Context Error (Calls) | `calls: ["backend.File_Dependency.FileDependencyGraph._resolve_module_name", "backend.File_Dependency.FileDependencyGraph.visit_Import"]` | `calls: "This method does not call any other functions directly."` | Medium |
| `backend.HelperLLM.LLMHelper.__init__` | Context Error (Calls) | `calls: ["backend.HelperLLM.LLMHelper._configure_batch_settings"]` | `calls: []` | Medium |
| `backend.MainLLM.MainLLM.call_llm` | Context Error (Calls) | `calls: []` | `calls: ""` | Minor |
| `backend.MainLLM.MainLLM.stream_llm` | Context Error (Calls) | `calls: []` | `calls: ""` | Minor |
| `backend.basic_info.ProjektInfoExtractor.__init__` | Parameter Error | `self` | `[]` | Medium |
| `backend.basic_info.ProjektInfoExtractor._clean_content` | Parameter Error | `self, content: str` | `content: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor._finde_datei` | Parameter Error | `self, patterns: List[str], dateien: List[Any]` | `patterns: List[str], dateien: List[Any]` | Medium |
| `backend.basic_info.ProjektInfoExtractor._extrahiere_sektion_aus_markdown` | Parameter Error | `self, inhalt: str, keywords: List[str]` | `inhalt: str, keywords: List[str]` | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_readme` | Parameter Error | `self, inhalt: str` | `inhalt: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_toml` | Parameter Error | `self, inhalt: str` | `inhalt: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor._parse_requirements` | Parameter Error | `self, inhalt: str` | `inhalt: str` | Medium |
| `backend.basic_info.ProjektInfoExtractor.extrahiere_info` | Parameter Error | `self, dateien: List[Any], repo_url: str` | `dateien: List[Any], repo_url: str` | Medium |
| `backend.callgraph.CallGraph.__init__` | Parameter Error | `self, filename: str` | `filename: str` | Medium |
| `backend.callgraph.CallGraph._recursive_call` | Parameter Error | `self, node` | `node: ast.AST` | Medium |
| `backend.callgraph.CallGraph._resolve_all_callee_names` | Parameter Error | `self, callee_nodes: list[list[str]]` | `callee_nodes: list[list[str]]` | Medium |
| `backend.callgraph.CallGraph._make_full_name` | Parameter Error | `self, basename: str, class_name: str | None = None` | `basename: str, class_name: Optional[str]` | Medium |
| `backend.callgraph.CallGraph._current_caller` | Parameter Error | `self` | `[]` | Medium |
| `backend.callgraph.CallGraph.visit_Import` | Parameter Error | `self, node` | `node: ast.Import` | Medium |
| `backend.callgraph.CallGraph.visit_ImportFrom` | Parameter Error | `self, node` | `node: ast.ImportFrom` | Medium |
| `backend.callgraph.CallGraph.visit_ClassDef` | Parameter Error | `self, node: ast.ClassDef` | `node: ast.ClassDef` | Medium |
| `backend.callgraph.CallGraph.visit_FunctionDef` | Parameter Error | `self, node` | `node: ast.FunctionDef` | Medium |
| `backend.callgraph.CallGraph.visit_AsyncFunctionDef` | Parameter Error | `self, node` | `node: ast.AsyncFunctionDef` | Medium |
| `backend.callgraph.CallGraph.visit_Call` | Parameter Error | `self, node` | `node: ast.Call` | Medium |
| `backend.callgraph.CallGraph.visit_If` | Parameter Error | `self, node` | `node: ast.If` | Medium |
| `backend.diagram_generation.call_resolver.CallResolver.__init__` | Parameter Error | `self, project: ProjectIndex` | `project: ProjectIndex` | Medium |
| `backend.diagram_generation.call_resolver.CallResolver.resolve_all` | Parameter Error | `self, calls: dict[str, list[RawCall]]` | `calls: dict[str, list[RawCall]]` | Medium |
| `backend.diagram_generation.call_resolver.CallResolver.resolved` | Parameter Error | `self, call: RawCall` | `call: RawCall` | Medium |
| `backend.diagram_generation.call_resolver.CallResolver._resolve_name` | Parameter Error | `self, call: RawCall, node: ast.Name` | `call: RawCall, node: ast.Name` | Medium |
| `backend.diagram_generation.call_resolver.CallResolver._resolve_attribute` | Parameter Error | `self, call: RawCall, node: ast.Attribute` | `call: RawCall, node: ast.Attribute` | Medium |
| `backend.diagram_generation.callgraph.TreeVisitor.__init__` | Parameter Error | `self, module: ModuleSymbol, project: ProjectIndex` | `module: ModuleSymbol, project: ProjectIndex` | Medium |
| `backend.diagram_generation.callgraph.TreeVisitor.visit_ClassDef` | Parameter Error | `self, node: ClassDef` | `node: ClassDef` | Medium |
| `backend.diagram_generation.callgraph.TreeVisitor.visit_FunctionDef` | Parameter Error | `self, node: FunctionDef` | `node: FunctionDef` | Medium |
| `backend.diagram_generation.callgraph.TreeVisitor.visit_Call` | Parameter Error | `self, node` | `node: Call` | Medium |
| `backend.diagram_generation.data_types.ProjectIndex.all_classes` | Parameter Error | `self` | `[]` | Medium |
| `backend.diagram_generation.emitter.MermaidSequenceEmitter.emit` | Parameter Error | `self, calls: list[ResolvedCall]` | `calls: list[ResolvedCall]` | Medium |
| `backend.diagram_generation.emitter.MermaidSequenceEmitter._collect_participants` | Parameter Error | `self, calls: list[ResolvedCall]` | `calls: list[ResolvedCall]` | Medium |
| `backend.diagram_generation.emitter.MermaidSequenceEmitter._emit_response` | Parameter Error | `self, call:ResolvedCall` | `call: ResolvedCall` | Medium |
| `backend.diagram_generation.emitter.MermaidSequenceEmitter._emit_call` | Parameter Error | `self, call: ResolvedCall` | `call: ResolvedCall` | Medium |
| `backend.diagram_generation.emitter.MermaidOverviewArchitectureEmitter.emit` | Parameter Error | `self, modules: dict[str, ModuleSymbol]` | `modules: dict[str, ModuleSymbol]` | Medium |
| `backend.diagram_generation.emitter.MermaidClassDiagramEmitter.emit` | Parameter Error | `self, modules: dict[str, ModuleSymbol]` | `modules: dict[str, ModuleSymbol]` | Medium |
| `backend.diagram_generation.symbol_collector.SymbolCollector.__init__` | Parameter Error | `self, module_name: str, packages: list[str]` | `module_name: str, packages: list[str]` | Medium |
| `backend.diagram_generation.symbol_collector.SymbolCollector._has_return` | Parameter Error | `self, node: FunctionDef` | `node: FunctionDef` | Medium |
| `backend.diagram_generation.symbol_collector.SymbolCollector._declare_input_parameters` | Parameter Error | `self, node: FunctionDef` | `node: FunctionDef` | Medium |
| `backend.diagram_generation.symbol_collector.SymbolCollector.visit_Import` | Parameter Error | `self, node: Import` | `node: Import` | Medium |
| `backend.diagram_generation.symbol_collector.SymbolCollector.visit_ImportFrom` | Parameter Error | `self, node: ImportFrom` | `node: ImportFrom` | Medium |
| `backend.diagram_generation.symbol_collector.SymbolCollector.visit_ClassDef` | Parameter Error | `self, node` | `node: ClassDef` | Medium |
| `backend.diagram_generation.symbol_collector.SymbolCollector.visit_AsyncFunctionDef` | Parameter Error | `self, node` | `node: AsyncFunctionDef` | Medium |
| `backend.diagram_generation.symbol_collector.SymbolCollector.visit_FunctionDef` | Parameter Error | `self, node: FunctionDef` | `node: FunctionDef` | Medium |
| `backend.getRepo.RepoFile.__init__` | Parameter Error | `self, file_path, commit_tree` | `file_path: str, commit_tree: git.Tree` | Medium |
| `backend.getRepo.RepoFile.blob` | Parameter Error | `self` | `[]` | Medium |
| `backend.getRepo.RepoFile.content` | Parameter Error | `self`
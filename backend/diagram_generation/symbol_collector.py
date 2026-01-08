from ast import (
    AST,
    AsyncFunctionDef,
    ClassDef,
    FunctionDef,
    Import,
    ImportFrom,
    NodeVisitor,
    iter_child_nodes,
    parse,
    walk
    )

from data_types import ModuleSymbol, FunctionSymbol, ClassSymbol
from callgraph import TreeVisitor


#TODO: Callstruktur über mehrere Funktionen/Methoden nachvollziehen für konkrete Prozesse nicht nur File
class SymbolCollector(NodeVisitor):

    def __init__(self, module_name: str, packages: list[str]):
        self.module = ModuleSymbol(
            name=module_name,
            overlying_packages=packages,
            functions={},
            classes={},
            imports={}
        )


    def visit_Import(self, node: Import) -> None:
        for alias in node.names:
            self.module.imports[alias.asname or alias.name] = alias.name
        self.generic_visit(node)


    def visit_ImportFrom(self, node: ImportFrom) -> None:
        if node.module is None:
            return
        
        module_base = node.module.split(".")[-1]
        for alias in node.names:
            self.module.imports[alias.asname or alias.name] = f"{module_base}.{alias.name}"
        self.generic_visit(node)


    def visit_ClassDef(self, node) -> None:
        cls = ClassSymbol(
            name=node.name,
            module=self.module.name,
            methods={}
        )

        self.module.classes[node.name] = cls

        for stmt in node.body:
            if isinstance(stmt, FunctionDef):
                curr_meth = FunctionSymbol(
                    name = stmt.name,
                    module = self.module.name,
                    qualname=f"{self.module.name}.{stmt.name}",
                    asynchron=True if isinstance(stmt, AsyncFunctionDef) else False,
                    return_symb=stmt.returns if stmt.returns else None,
                    lineno=stmt.lineno
                )
                cls.methods[stmt.name] = curr_meth
        self.generic_visit(node)


    def visit_AsyncFunctionDef(self, node) -> None:
        if isinstance(getattr(node, "parent", None), ClassDef):
            return
        
        curr_func = FunctionSymbol(
            name=node.name,
            module=self.module.name,
            qualname= f"{self.module.name}.{node.name}",
            asynchron=True if isinstance(node, AsyncFunctionDef) else False,
            return_symb=node.returns,
            lineno=node.lineno

        )
        self.module.functions[node.name] = curr_func
        self.generic_visit(node)

    
    def visit_FunctionDef(self, node: FunctionDef) -> None:
        self.visit_AsyncFunctionDef(node)
    

def attach_with_parents(tree: AST) -> None:
    for parent in walk(tree):
        for child in iter_child_nodes(parent):
            child.parent = parent


if __name__=="__main__":
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent.parent))
    from getRepo import GitRepository
    import os
    repo_url = "https://github.com/pallets/flask"    

    with GitRepository(repo_url) as repository:
        print(f"Repository von {repository.repo_url} erfolgreich geklont. Es liegt im Ornder {repository.temp_dir}")
        
        # Die Dateiliste wird jetzt am Anfang geholt, damit sie für alle Analysen verfügbar ist
        all_file_objects = repository.get_all_files()
    
    filtered_file_obj = [file for file in all_file_objects if file.path.endswith(".py")]
    for file in filtered_file_obj:
        module_path: str = file.path
        # if not module_path.endswith(".py"):
        #     continue
        module_name = module_path.replace("/", ".").removesuffix(".py")
        tree = parse(file.content)
        attach_with_parents(tree)
        symbol_collector = SymbolCollector(module_name)
        symbol_collector.visit(tree)
        module_symbol = symbol_collector.module

        callgraph = TreeVisitor(module_symbol)
        callgraph.visit(tree)

        print(callgraph.calls)
            
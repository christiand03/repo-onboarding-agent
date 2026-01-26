import sys

from ast import (
    AST,
    AsyncFunctionDef,
    ClassDef,
    FunctionDef,
    Import,
    ImportFrom,
    NodeVisitor,
    Return,
    iter_child_nodes,
    unparse,
    walk
    )
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from diagram_generation.data_types import (
    ModuleSymbol, 
    FunctionSymbol, 
    ClassSymbol
)


class SymbolCollector(NodeVisitor):
    def __init__(self, module_name: str, packages: list[str], filtered_file_obj: list):
        self.module = ModuleSymbol(
            name=module_name,
            overlying_packages=packages,
            functions={},
            classes={},
            imports={}
        )

        self.filtered_file_stem = self._filtered_file_stems(filtered_file_obj)

               
    def _filtered_file_stems(self, file_objects):
        all_last_parts = []
        for file in file_objects:
            last_parts = file.path.split("/")[-2:]
            joined_parts = ".".join(last_parts).removesuffix(".py")
            all_last_parts.append(joined_parts)
        
        return all_last_parts
    

    def _return_value(self, node: FunctionDef) -> str:
        """Returns the return value of a function."""
        return_values = []
        for stmt in node.body:
            if isinstance(stmt, Return):
                return_values.append(stmt.value)
        
        if len(return_values) == 1:
            return unparse(return_values[0]) if return_values[0] else "None"
        return "<return values>"


    def _resolve_import(self, node: ImportFrom):
        """Resolve relative Imports."""
        parts = self.module.overlying_packages
        parent = parts[:-node.level]
        
        for alias in node.names:
            if node.module is None:
                mod = parent + [alias.name] if alias.name in self.filtered_file_stem else parent
            else:
                mod = parent + node.module.split(".")
                if alias.name in self.filtered_file_stem:
                    mod = mod + [alias.name]

            import_path = ".".join(mod)
            self.module.imports[alias.asname or alias.name] = import_path
            self.generic_visit(node)

    def _declare_input_parameters(self, node: FunctionDef) -> list[str]:
        input_parameters: list[str] = []
        for argument in node.args.args:
            input_param = argument.arg
            input_parameters.append(input_param)

        return input_parameters
            

    def visit_Import(self, node: Import) -> None:
        for alias in node.names:
            self.module.imports[alias.asname or alias.name] = alias.name
        self.generic_visit(node)


    def visit_ImportFrom(self, node: ImportFrom) -> None:
        if node.level > 0:
            self._resolve_import(node)
        else:
            import_module = node.module
            for alias in node.names:
                self.module.imports[alias.asname or alias.name] = f"{import_module}.{alias.name}"
        self.generic_visit(node)


    def visit_ClassDef(self, node) -> None:
        cls = ClassSymbol(
            name=node.name,
            module=self.module.name,
            methods={},
            lineno=node.lineno,
            end_lineno=node.end_lineno,
            inheritance=[unparse(base) for base in node.bases]
        )

        self.module.classes[node.name] = cls

        for stmt in node.body:
            if isinstance(stmt, FunctionDef):
                return_value = self._return_value(node)
                input_parameters = self._declare_input_parameters(stmt)
                curr_meth = FunctionSymbol(
                    name = stmt.name,
                    module = self.module.name,
                    cls = node.name,
                    qualname=f"{self.module.name}.{node.name}.{stmt.name}",
                    asynchron=True if isinstance(stmt, AsyncFunctionDef) else False,
                    input_params=input_parameters,
                    return_symb=return_value,
                    lineno=stmt.lineno,
                    end_lineno=stmt.end_lineno
                )
                cls.methods[stmt.name] = curr_meth
        self.generic_visit(node)


    def visit_AsyncFunctionDef(self, node) -> None:
        if isinstance(getattr(node, "parent", None), ClassDef):
            return
        
        return_value = self._return_value(node)
        input_paramters = self._declare_input_parameters(node)
        curr_func = FunctionSymbol(
            name=node.name,
            module=self.module.name,
            cls = None,
            qualname= f"{self.module.name}.{node.name}",
            asynchron=True if isinstance(node, AsyncFunctionDef) else False,
            input_params=input_paramters,
            return_symb=return_value,
            lineno=node.lineno,
            end_lineno=node.end_lineno

        )
        self.module.functions[node.name] = curr_func
        self.generic_visit(node)

    
    def visit_FunctionDef(self, node: FunctionDef) -> None:
        self.visit_AsyncFunctionDef(node)
    

def attach_with_parents(tree: AST) -> None:
    for parent in walk(tree):
        for child in iter_child_nodes(parent):
            child.parent = parent


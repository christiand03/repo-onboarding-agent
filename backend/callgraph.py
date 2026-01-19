import ast
import networkx as nx


class CallGraph(ast.NodeVisitor):
    def __init__(self, filename: str):
        self.filename = filename
        self.current_function = None
        self.current_class = None
        
        self.local_defs: dict[str, str] = {}
        self.graph = nx.DiGraph()
        self.import_mapping: dict[str, str] = {}
        self.function_set: set[str] = set()
        self.edges: dict[str, set[str]] = {}

    def _recursive_call(self, node):
        """
        Liefert eine Liste der Namenskomponenten als dotted string z.B. ['pkg', 'mod', 'Class', 'method']
        """
        if isinstance(node, ast.Call):
            return self._recursive_call(node.func)
        if isinstance(node, ast.Name):
            return [node.id]
        if isinstance(node, ast.Attribute):
            parts = self._recursive_call(node.value)
            parts.append(node.attr)
            return parts
        return []

    def _resolve_all_callee_names(self, callee_nodes: list[list[str]]) -> list[str]:
        """
        callee_nodes ist jetzt eine Liste von Listen (Name-Steps).
        Wir prüfen zuerst lokale Definitionen, dann import_mapping.
        """
        resolved = []
        for parts in callee_nodes:
            if not parts:
                continue
            simple = parts[-1]
            dotted = ".".join(parts[-2:]) if len(parts) >= 2 else simple

            if simple in self.local_defs:
                resolved.append(self.local_defs[simple])
                continue
            if dotted in self.local_defs:
                resolved.append(self.local_defs[dotted])
                continue

            first = parts[0]
            if first in self.import_mapping:
                mod = self.import_mapping[first]
                rest = "::".join(parts[1:]) if len(parts) > 1 else simple
                resolved.append(f"{mod}::{rest}")
                continue

            if self.current_class:
                resolved.append(f"{self.filename}::{parts[0]}::{simple}" if len(parts)==1 else f"{self.filename}::{'::'.join(parts)}")
            else:
                resolved.append(f"{self.filename}::{ '::'.join(parts)}")
        return resolved

    def _make_full_name(self, basename: str, class_name: str | None = None) -> str:
        if class_name:
            return f"{self.filename}::{class_name}::{basename}"
        return f"{self.filename}::{basename}"
    
    def _current_caller(self) -> str:
        if self.current_function:
            return self.current_function
        return f"<{self.filename}>" if self.filename else "<global-scope>"

    def visit_Import(self, node):
        for alias in node.names:
            module_name = alias.name
            module_asname = alias.asname if alias.asname else module_name
            self.import_mapping[module_asname] = module_name
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module_name = node.module.split(".")[-1] if node.module else ""
        for alias in node.names:
            self.import_mapping[alias.asname or alias.name] = f"{module_name}" if module_name else alias.name

    def visit_ClassDef(self, node: ast.ClassDef):
        prev_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = prev_class
        
    def visit_FunctionDef(self, node):
        prev_function = self.current_function
        full_name = self._make_full_name(node.name, self.current_class)
        self.local_defs[node.name] = full_name
        if self.current_class:
            self.local_defs[f"{self.current_class}.{node.name}"] = full_name

        self.current_function = full_name
        self.graph.add_node(self.current_function)
        self.generic_visit(node)
        self.function_set.add(self.current_function)
        self.current_function = prev_function

    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)

    def visit_Call(self, node):
        caller = self._current_caller()
        parts = self._recursive_call(node)
        resolved_callees = self._resolve_all_callee_names([parts])

        if caller not in self.edges:
            self.edges[caller] = set()

        for callee in resolved_callees:
            if callee:
                self.edges[caller].add(callee)
        self.generic_visit(node)

    def visit_If(self, node):
        if (isinstance(node.test, ast.Compare) and
            isinstance(node.test.left, ast.Name) and 
            node.test.left.id == "__name__"):
            caller_backup = self.current_function
            self.current_function = "<main_block>"
            self.generic_visit(node)
            self.current_function = caller_backup
        else:
            self.generic_visit(node)


def build_callGraph(tree: ast.AST, filename: str) -> nx.DiGraph:
    visitor = CallGraph(filename)
    visitor.visit(tree)
    graph = visitor.graph
    own_functions = visitor.function_set

    for caller, callees in visitor.edges.items():
        if caller in own_functions:
            graph.add_node(caller)
        for callee in callees:
            if callee in own_functions:
                graph.add_node(callee)
                graph.add_edge(caller, callee)

    return graph

def make_safe_dot(graph: nx.DiGraph, out_path: str):
    mapping = {}
    H = graph.copy()
    for i, n in enumerate(list(graph.nodes())):
        safe = f"n{i}"           
        mapping[n] = safe
    H = nx.relabel_nodes(H, mapping)
    for orig, safe in mapping.items():
        H.nodes[safe]["label"] = orig
    nx.drawing.nx_pydot.write_dot(H, out_path)

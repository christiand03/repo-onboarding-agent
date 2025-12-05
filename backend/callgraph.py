import ast
import networkx as nx
import os 

from pathlib import Path
from typing import Dict

from .getRepo import GitRepository

import ast
import networkx as nx
import os
from pathlib import Path
from typing import Dict

from .getRepo import GitRepository

class CallGraph(ast.NodeVisitor):
    def __init__(self, filename: str):
        self.filename = filename
        self.current_function = None
        self.current_class = None
        
        self.local_defs: dict[str, str] = {}
        self.graph = nx.DiGraph()
        self.import_mapping: dict[str, str] = {}
        self.function_set: set[str] = set()
        self.edges: Dict[str, set[str]] = {}

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

# def build_callGraph(tree: ast.AST, filename: str, repo_root) -> nx.DiGraph:
#     visitor = CallGraph(filename, repo_root)
#     visitor.visit(tree)
#     graph = visitor.graph

#     for caller, callees in visitor.edges.items():
#         for callee in callees:
#             graph.add_node(callee)
#             graph.add_edge(caller, callee)

#     return graph

# def build_global_callgraph(repo: GitRepository, repo_root) -> nx.DiGraph:
#     all_files = repo.get_all_files()
#     global_graph = nx.DiGraph()

#     # Zunächst alle Funktionen aller Dateien erfassen
#     file_function_mapping = {}
#     for file in all_files:
#         if not file.path.endswith(".py"):
#             continue
#         filename = Path(file.path).stem
#         tree = ast.parse(file.content)
#         visitor = CallGraph(filename, repo_root)
#         visitor.visit(tree)
#         file_function_mapping[filename] = visitor.function_set
#         for node in visitor.graph.nodes:
#             global_graph.add_node(node)
#         for caller, callees in visitor.edges.items():
#             if caller not in global_graph:
#                 global_graph.add_node(caller)
#             for callee in callees:
#                 global_graph.add_node(callee)
#                 global_graph.add_edge(caller, callee)

#     return global_graph

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


def build_filtered_callgraph(repo: GitRepository) -> nx.DiGraph:
    """
    Baut den globalen Call-Graphen und filtert ihn auf selbst geschriebene Funktionen.
    """
    all_file_objects = repo.get_all_files()
    own_functions = set()
    file_trees = {}

    for file in all_file_objects:
        if not file.path.endswith(".py"):
            continue
        filename = Path(file.path).stem
        tree = ast.parse(file.content)
        file_trees[filename] = tree
        visitor = CallGraph(filename)
        visitor.visit(tree)
        own_functions.update(visitor.function_set)

    # Globalen Call-Graph bauen
    global_graph = nx.DiGraph()
    for filename, tree in file_trees.items():
        visitor = CallGraph(filename)
        visitor.visit(tree)
        for caller, callees in visitor.edges.items():
            if caller not in own_functions:
                continue 
            for callee in callees:
                if callee in own_functions:
                    global_graph.add_edge(caller, callee)
                    global_graph.add_node(caller)
                    global_graph.add_node(callee)
    return global_graph


if __name__ == "__main__":
    from getRepo import GitRepository
    from basic_info import ProjektInfoExtractor
    import os

    # repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    repo_url = "https://github.com/pallets/flask"    

    with GitRepository(repo_url) as repository:
        print(f"Repository von {repository.repo_url} erfolgreich geklont. Es liegt im Ornder {repository.temp_dir}")
        
        # Die Dateiliste wird jetzt am Anfang geholt, damit sie für alle Analysen verfügbar ist
        all_file_objects = repository.get_all_files()

        info_extractor = ProjektInfoExtractor()
        basic_project_info = info_extractor.extrahiere_info(all_file_objects, repo_url)

        print("\n--- Verzeichnisstruktur (Tree View) ---")
        file_tree_structure = repository.get_file_tree()
        repo_name = os.path.basename(repo_url.removesuffix('.git'))
        print(f"📁 {repo_name}/")

        print("\n--- Starte nun die detaillierte Code-Analyse... ---")
        print(f"Insgesamt {len(all_file_objects)} Dateien im Repository für die Analyse gefunden.")               
        filtered_graph = build_filtered_callgraph(repository)
        make_safe_dot(filtered_graph, f"filtered_repo_callgraph_repo-agent-3.dot")

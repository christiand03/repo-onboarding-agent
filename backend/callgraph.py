import ast
import networkx as nx
import os 

from typing import Dict
from .getRepo import RepoFile

class CallGraph(ast.NodeVisitor):
    """
    Visitor, der Funktionsaufrufe im AST sammelt und Kanten für den Call-Graph erstellt.
    """
    def __init__(self, filename: str):
        """
        Initialisiert den Visitor mit einem Platzhalter für die aktuelle Funktion.
        """
        self.filename = filename
        self.current_function = None
        self.current_class = None

        self.graph = nx.DiGraph()
        self.import_mapping: dict[str, str] = {}
        self.function_set: set[str] = ()
        self.edges: Dict[str, set[str]] = {}

    def _recursive_call(self, node) -> list[str]:
        all_calls = []
        if isinstance(node, ast.Call):
            return self._recursive_call(node.func)
        elif isinstance(node, ast.Name):
            all_calls.append(node.id)
            return all_calls
        elif isinstance(node, ast.Attribute):
            all_calls.append(node.attr)
            return all_calls
        return all_calls
            
    def _resolve_all_callee_names(self, callee_nodes: list[str]) -> list[str]:
        resolved_callees = []
        for raw_callee in callee_nodes:
            if not self.current_class:
                resolved_callee = f"{self.filename}::{raw_callee}"
            else:
                resolved_callee = f"{self.filename}::{self.current_class}::{raw_callee}"
            resolved_callees.append(resolved_callee)
        return resolved_callees

    def _make_full_name(self, basename: str, class_name: str | None = None)-> str:
        if class_name:
            return f"{self.filename}::{class_name}::{basename}"
        return f"{self.filename}::{basename}"
    
    def _current_caller(self)-> str:
        if self.current_function:
            return self.current_function
        return f"<{self.filename}>" if self.filename else"<global-scope>"

    # def visit_Import(self, node):
    #     for alias in node.names:
    #         module_name = alias.name
    #         module_asname = (alias.asname if alias.asname else module_name)
    #         self.import_mapping[module_asname] = module_name
    #     self.generic_visit(node)

    # def visit_ImportFrom(self, node):
    #     module_name = node.module
    #     level_depth = node.level
        
    #     module_base = module_name.split(".")[0]
    #     for alias in node.names:
    #         import_name = (alias.asname if alias.asname else alias.name)
    #         self.import_mapping[import_name] = module_base
    #     # TODO: level depth und relative import From resolven

    def visit_ClassDef(self, node: ast.ClassDef):
        prev_class = self.current_class
        self.current_class = node.name
        for function in node.body:
            self.visit(function)
        self.current_class = prev_class
        
    def visit_FunctionDef(self, node):
        """ 
        Besucht eine normale Funktionsdefinition.

        Setzt `self.current_function`, erstellt den Knoten im Graphen und 
        traversiert rekursiv den Funktionskörper.
        """
        if self.current_class:
            self.current_function = self._make_full_name(node.name, class_name=self.current_class)
        else:
            self.current_function = self._make_full_name(node.name) 
        self.graph.add_node(self.current_function)
        self.generic_visit(node)
        self.function_set.add(self.current_function)
        self.current_function = None

    def visit_AsyncFunctionDef(self, node):
        """
        Besucht eine asynchrone Funktionsdefinition (`async def`).

        Funktioniert analog zu `visit_FunctionDef`.
        """
        self.visit_FunctionDef(node)

    def visit_Call(self, node):
        """
        Besucht einen Funktions- oder Methodenaufruf und behandelt komplexe Fälle
        mit einer detaillierten Warnung, anstatt abzustürzen.
        """             
        caller = self._current_caller()
        raw_callees: list[str] = []
        try:
            # benutze die Helferfunktion, um Namen zu extrahieren
            raw_callees = self._recursive_call(node)
            # falls _recursive_call ein leeres array oder None zurückgibt, sicherstellen, dass es list ist
            if raw_callees is None:
                raw_callees = []

            resolved_callees = self._resolve_all_callee_names(raw_callees)

            # sicherstellen, dass caller als Key existiert und ein Set ist
            if caller not in self.edges:
                self.edges[caller] = set()

            for resolved_callee in resolved_callees:
                if resolved_callee:
                    self.edges[caller].add(resolved_callee)
        except Exception as e:
            print(f"Unerwarteter Fehler bei der Verarbeitung eines Funktionsaufrufs: {e} in Datei {self.filename}")
        self.generic_visit(node)

    def visit_If(self, node):
        """
        Prüft auf `if __name__ == "__main__"`-Blöcke, um globale Aufrufe innerhalb
        dieses Blocks separat als <main_block> im Call-Graphen darzustellen.

        Alle Funktionsaufrufe innerhalb des Blocks werden dann von <main_block> aus
        als Caller-Knoten erfasst.
        """
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
    """ 
    Erstellt einen Call-Graphen aus einem gegebenen Python-AST.

    Der Graph ist ein gerichteter Graph (networkx.DiGraph), in dem:
      - Knoten: Funktionen, Methoden und der globale Scope (<module>) bzw. <main_block> für `if __name__ == "__main__"`-Code
      - Kanten: Funktions-/Methodenaufrufe zwischen diesen Knoten

    Args:
        tree (ast.AST): Der AST der zu analysierenden Python-Datei.
        filename (str, optional): Der Name der analysierten Datei, z. B. `"main.py"` oder `"src/utils.py"`.

    Returns:
        nx.DiGraph: Der vollständige Call-Graph.
    """
    visitor = CallGraph(filename)
    visitor.visit(tree)
    graph = visitor.graph

# add all edges from dictionary to the graph at once
    for caller, callees in visitor.edges.items():
        for callee in callees:
            # if callee in visitor.function_set:
                graph.add_edge(caller, callee)

    return graph

# --- NEUE FUNKTION HINZUGEFÜGT ---
def graph_to_adj_list(graph: nx.DiGraph) -> Dict[str, list[str]]:
    """
    Konvertiert einen networkx.DiGraph in eine Adjazenzliste (Dict),
    die JSON-serialisierbar ist.

    Args:
        graph (nx.DiGraph): Der zu konvertierende Call-Graph.

    Returns:
        Dict[str, List[str]]: Eine Adjazenzliste, bei der jeder Schlüssel
                              ein aufrufender Knoten (caller) und der Wert
                              eine Liste der aufgerufenen Knoten (callees) ist.
    """
    adj_list = {}
    # Wir sortieren die Knoten für eine konsistente Ausgabe
    for node in sorted(list(graph.nodes())):
        # Wir holen alle Nachfolger (aufgerufene Funktionen) und sortieren sie ebenfalls
        successors = sorted(list(graph.successors(node)))
        if successors:  # Nur Knoten aufnehmen, die auch wirklich andere aufrufen
            adj_list[node] = successors
    return adj_list

# Globale Darstellung des Callgraphen

def build_global_callgraph(repo: GitRepository)-> nx.DiGraph:
    all_files = repository.get_all_files()
    global_graph = nx.DiGraph()

    for file in all_files: 
        if not file.path.endswith(".py"):
            continue
        filename = str(os.path.basename(file.path)).removesuffix(".py")
        tree = ast.parse(file.content)
        graph = build_callGraph(tree, filename)
        
        for node in graph.nodes:
            global_graph.add_node(node)
            
        for caller, callee in graph.edges:
            if callee:
                global_graph.add_node(callee)
                global_graph.add_edge(caller, callee)
    
    return global_graph


   
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

if __name__ == "__main__":
    from getRepo import GitRepository
    from basic_info import ProjektInfoExtractor
    import os

    repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    #repo_url = "https://github.com/pallets/flask"    

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
        global_graph = build_global_callgraph(repository)
        make_safe_dot(global_graph, f"repo.dot")

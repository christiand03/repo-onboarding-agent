import ast
import networkx as nx
from typing import Dict

def build_callGraph(tree: ast.AST, filename: str | None = None) -> nx.DiGraph:
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

    graph = nx.DiGraph()
    edges: Dict[str, set[str]] = {}

    class CallGraph(ast.NodeVisitor):
        """
        Visitor, der Funktionsaufrufe im AST sammelt und Kanten für den Call-Graph erstellt.
        """

        def __init__(self):
            """
            Initialisiert den Visitor mit einem Platzhalter für die aktuelle Funktion.
            """
            self.current_function = None

        def visit_FunctionDef(self, node):
            """ 
            Besucht eine normale Funktionsdefinition.

            Setzt `self.current_function`, erstellt den Knoten im Graphen und 
            traversiert rekursiv den Funktionskörper.
            """
            self.current_function = node.name
            graph.add_node(self.current_function)
            self.generic_visit(node)
            self.current_function = None

        def visit_AsyncFunctionDef(self, node):
            """
            Besucht eine asynchrone Funktionsdefinition (`async def`).

            Funktioniert analog zu `visit_FunctionDef`.
            """
            self.current_function = node.name
            graph.add_node(self.current_function)
            self.generic_visit(node)
            self.current_function = None

        def visit_Call(self, node):
            """
            Besucht einen Funktions- oder Methodenaufruf.

            Fügt eine Kante im Call-Graphen von `self.current_function` (oder
            <module>/<main_block> für globalen Scope) zum aufgerufenen Funktionsnamen hinzu.
            """             
            caller = self.current_function or (f"<{filename}>" if filename else "<global-scope>")
            try:
                if isinstance(node.func, ast.Name):
                    # ast.Name sind einfache Funktionsausdrücke, wie z.B. print()
                    # die "id" wäre dann print
                    call_name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    # ast.Attribute sind Methodenaufrufe oder Attributzugriffe, wie z.B. obj.method()
                    # das "attr" wäre dann method
                    call_name = node.func.attr
                else:
                    raise TypeError(f"Unerwarteter Funktionsaufruf-Typ: {type(node.func).__name__}"
                                    f"in Zeile {getattr(node, 'lineno', '?')}")
                # graph.add_edge(self.current_function, call_name)
            
                if caller not in edges:
                    edges[caller] = {call_name}
                else:
                    edges[caller].add(call_name)
            
            except Exception as e:
                raise RuntimeError(f"Fehler bei der Verarbeitung eines Funktionsaufrufs: {e}")
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

    visitor = CallGraph()
    visitor.visit(tree)

    # add all edges from dictionary to the graph at once
    for caller, callees in edges.items():
        for callee in callees:
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
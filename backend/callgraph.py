import ast
import networkx as nx
from typing import Dict

def build_callGraph(tree: ast.AST, filename: str | None = None, file_content: str | None = None) -> nx.DiGraph:
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
            Besucht einen Funktions- oder Methodenaufruf und behandelt komplexe Fälle
            mit einer detaillierten Warnung, anstatt abzustürzen.
            """             
            caller = self.current_function or (f"<{filename}>" if filename else "<global-scope>")
            try:
                # Iterativ durch verschachtelte Calls navigieren, um den Basis-Namen zu finden
                callee_node = node.func
                while isinstance(callee_node, ast.Call):
                    callee_node = callee_node.func

                call_name = None
                if isinstance(callee_node, ast.Name):
                    call_name = callee_node.id
                elif isinstance(callee_node, ast.Attribute):
                    call_name = callee_node.attr
                else:
                    # --- NEUE, VERBESSERTE WARNUNG ---
                    
                    # 1. Versuche, das exakte Code-Snippet zu extrahieren
                    source_segment = "N/A (benötigt Python 3.8+ und file_content)"
                    # ast.get_source_segment ist die "magische" Funktion dafür
                    if file_content and hasattr(ast, 'get_source_segment'):
                        try:
                            source_segment = ast.get_source_segment(file_content, node)
                        except Exception:
                            source_segment = "(Konnte Quellcode-Segment nicht extrahieren)"
                    
                    # 2. Gib eine strukturierte, mehrzeilige Warnung aus
                    print(
                        f"\n--- WARNUNG: Komplexer Funktionsaufruf übersprungen ---\n"
                        f"| Problem:  Der Typ des aufgerufenen Objekts ('{type(callee_node).__name__}') wird nicht unterstützt.\n"
                        f"| Ort:      Datei '{filename}', Zeile {getattr(node, 'lineno', '?')}\n"
                        f"| Code:     {source_segment}\n"
                        f"| AST-Dump: {ast.dump(callee_node)}\n"
                        f"----------------------------------------------------------"
                    )
                    # Der Aufruf wird bewusst übersprungen, anstatt das Programm abstürzen zu lassen.

                if call_name:
                    if caller not in edges:
                        edges[caller] = {call_name}
                    else:
                        edges[caller].add(call_name)
            
            except Exception as e:
                print(f"Unerwarteter Fehler bei der Verarbeitung eines Funktionsaufrufs: {e} in Datei {filename}")
            
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
import networkx as nx
import os

from ast import (
    Assign,
    AST,
    ClassDef,
    FunctionDef,
    Import,
    ImportFrom,
    Name,
    NodeVisitor,
    literal_eval,
    parse,
    walk
)
from keyword import iskeyword
from pathlib import Path

from getRepo import GitRepository
from callgraph import make_safe_dot
class FileDependencyGraph(NodeVisitor):

    import_dependencies: dict[str, set[str]] = {}
    def __init__(self, filename: str, repo_root):
        """
        Initialisiert den File Dependency Graphen

        Args:

        """
        self.filename = filename
        self.repo_root = repo_root

    def _resolve_module_name(self, node: ImportFrom) -> list[str]:
        """
        Löst relative Imports der Form `from .. import name1, name2` auf.
        Liefert die Liste der tatsächlich existierenden Modul-/Symbolnamen (z.B. ["foo","bar"]).
        Wirft ImportError, wenn nichts aufgelöst werden konnte.
        """
        level_depth = node.level
        names = [alias.name for alias in node.names]  
        all_files = get_all_temp_files(self.repo_root)  

        candidates = [p for p in all_files if p.stem == Path(self.filename).stem or p.name == f"{self.filename}.py"]

        if not candidates:
            raise ImportError(f"Kann aktuelle Datei '{self.filename}' im Repo nicht finden.")


        candidates.sort(key=lambda p: len(p.parts))
        current_rel_path = candidates[0]
        base_dir = current_rel_path.parent
        if level_depth <= 0:
            raise ImportError("Erwarteter relativer Import (level >= 1).")
        for _ in range(level_depth - 1):
            if base_dir == base_dir.parent and len(base_dir.parts) == 0:
                raise ImportError(f"Relative Import-Ebene ({level_depth}) zu groß für Datei '{current_rel_path}'.")
            base_dir = base_dir.parent

        repo_root_path = Path(self.repo_root).resolve()
        resolved: list[str] = []

        def module_file_exists(rel_base: Path, name: str) -> bool:
            file_path = repo_root_path / rel_base / f"{name}.py"
            pkg_init = repo_root_path / rel_base / name / "__init__.py"
            return file_path.exists() or pkg_init.exists()

        def init_exports_symbol(rel_base: Path, symbol: str) -> bool:
            """
            Prüft, ob rel_base/__init__.py existiert und symbol entweder in __all__ ist
            oder als Name (funktion/klasse/assign) definiert ist.
            """
            init_path = repo_root_path / rel_base / "__init__.py"
            if not init_path.exists():
                return False
            try:
                src = init_path.read_text(encoding="utf-8")
                mod = parse(src, filename=str(init_path))
            except Exception:
                return False

            for node_ in walk(mod):
                if isinstance(node_, Assign):
                    for target in node_.targets:
                        if isinstance(target, Name) and target.id == "__all__":
                            try:
                                value = literal_eval(node_.value)
                                if isinstance(value, (list, tuple)) and symbol in value:
                                    return True
                            except Exception:
                                pass
                if isinstance(node_, (FunctionDef, ClassDef)) and node_.name == symbol:
                    return True
                if isinstance(node_, Assign):
                    for target in node_.targets:
                        if isinstance(target, Name) and target.id == symbol:
                            return True
            return False

        for name in names:
            if not name.isidentifier() or iskeyword(name):
                continue

            if module_file_exists(base_dir, name):
                resolved.append(name)
                continue
            if init_exports_symbol(base_dir, name):
                resolved.append(name)
                continue

        resolved = sorted(set(resolved))

        if not resolved:
            raise ImportError(
                f"Kein passendes Modul/Symbol für relative Import-Auflösung gefunden "
                f"(level={level_depth}, names={names}, base_dir={base_dir})"
            )

        return resolved
    
    def visit_Import(self, node: Import | ImportFrom, base_name: str | None = None):
        for alias in node.names:
        
            if self.filename not in self.import_dependencies:
                self.import_dependencies[self.filename] = set()

            if base_name:
                self.import_dependencies[self.filename].add(base_name)
            else:
                self.import_dependencies[self.filename].add(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ImportFrom):
        """
        Wenn der Import die Form from a.b.c import d besitzt, wird der letzte Teil des Moduls genommen,
        also c, und dieser wird als callee für den caller, das File, gesetzt.
        """
        module_name = node.module
        if module_name:
            module_base = module_name.split(".")[-1]
            self.visit_Import(node, module_base)
        else:
            try:
                resolved = self._resolve_module_name(node)
                for base in resolved:
                    self.visit_Import(node, base)
            except ImportError as e:
                print(f"Auflösung eines relativen Imports fehlgeschlagen: {e}")

        self.generic_visit(node)

def build_file_dependency_graph(filename: str, tree: AST, repo_root: str) -> nx.DiGraph:
    graph = nx.DiGraph()

    tree_visitor = FileDependencyGraph(filename, repo_root)
    tree_visitor.visit(tree)

    for caller, callees in tree_visitor.import_dependencies.items():
        graph.add_node(caller)
        graph.add_nodes_from(callees)
        for callee in callees:
            graph.add_edge(caller, callee)
    
    return graph

def build_repository_graph(repository: GitRepository) -> nx.DiGraph:
    all_files = repository.get_all_files()
    repo_root = repository.temp_dir
    global_graph = nx.DiGraph()

    for file in all_files: 
        if not file.path.endswith(".py"):
            continue
        filename = str(os.path.basename(file.path)).removesuffix(".py")
        tree = parse(file.content)
        graph = build_file_dependency_graph(filename, tree, repo_root)
        
        for node in graph.nodes:
            global_graph.add_node(node)

        for caller, callee in graph.edges:
            if callee:
                global_graph.add_node(callee)
                global_graph.add_edge(caller, callee)
    
    return global_graph

def get_all_temp_files(directory: str) -> list[Path]:
    root_path = Path(directory).resolve()
    all_files = [file.relative_to(root_path) for file in root_path.rglob("*.py")]

    return all_files

from collections import defaultdict

def nx_to_mermaid_with_folders(G: nx.DiGraph):
    # Ordner → Liste der Dateien
    folder_map = defaultdict(list)
    for node in G.nodes:
        parts = node.split("/")
        folder = "/".join(parts[:-1])  # alles außer Datei = Ordner
        folder_map[folder].append(parts[-1])  # nur der Dateiname als Knoten

    lines = ["graph TD"]

    # Subgraphs erstellen
    for folder, files in folder_map.items():
        if folder:  # nur wenn es einen Ordner gibt
            lines.append(f"    subgraph {folder.replace('/', '_')}")
            for f in files:
                node_id = f"{folder}/{f}".replace('/', '_')
                lines.append(f'        {node_id}["{f}"]')
            lines.append("    end")
        else:
            # Dateien im Root
            for f in files:
                node_id = f.replace('/', '_')
                lines.append(f'    {node_id}["{f}"]')

    # Kanten
    for caller, callee in G.edges:
        caller_id = caller.replace('/', '_')
        callee_id = callee.replace('/', '_')
        lines.append(f'    {caller_id} --> {callee_id}')

    return "\n".join(lines)

if __name__ == "__main__":
    # repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    repo_url = "https://github.com/pallets/flask"
    with GitRepository(repo_url) as repo:
        global_graph = build_repository_graph(repo)
        make_safe_dot(global_graph, f"FDG_repo.dot")
        # mermaid_code = nx_to_mermaid_with_folders(global_graph)
        # with open("dependency_graph.md", "w") as f:
        #     f.write(mermaid_code)
        
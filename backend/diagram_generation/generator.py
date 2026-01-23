import ast
from pathlib import Path
import sys
import re


sys.path.append(str(Path(__file__).parent.parent))
from getRepo import RepoFile
from diagram_generation.call_resolver import CallResolver
from diagram_generation.callgraph import TreeVisitor
from diagram_generation.data_types import ProjectIndex, ResolvedCall
from diagram_generation.emitter import (
    MermaidSequenceEmitter,
    MermaidClassDiagramEmitter,
    MermaidOverviewEmitter
)
from diagram_generation.symbol_collector import SymbolCollector, attach_with_parents


def analyze_project(all_files: list[RepoFile]):
    project = ProjectIndex(modules={})
    trees: dict[str, ast.AST] = {}

    py_files: list[RepoFile] = []
    for file in all_files:
        if file.path.endswith(".py"):
            py_files.append(file)


    for file in py_files:
        module_name = file.path.split("/")[-1].removesuffix(".py")
        packages: list[str] = file.path.split("/")[:-1]
        tree = ast.parse(file.content)
        attach_with_parents(tree)

        collector = SymbolCollector(module_name, packages, py_files)
        collector.visit(tree)

        project.modules[module_name] = collector.module
        trees[module_name] = tree

    raw_calls = {}

    for module_name, tree in trees.items():
        module = project.modules[module_name]
        visitor = TreeVisitor(module, project)
        visitor.visit(tree)
        raw_calls[module_name] = (visitor.calls)

    resolver = CallResolver(project)
    resolved_calls = resolver.resolve_all(raw_calls)

    return project, resolved_calls


def main_diagram_generation(py_files: list[str]) -> tuple:
    project, resolved_calls = analyze_project(py_files)
    call_from_same_function: dict[str, list[ResolvedCall]] = {}

    for res_calls in resolved_calls.values():
        if len(res_calls) == 0:
            continue
        for res_call in res_calls:
            caller_name = res_call.caller.name
            if caller_name not in call_from_same_function:
                call_from_same_function[caller_name] = []
            call_from_same_function[caller_name].append(res_call)

    class_diagrams = MermaidClassDiagramEmitter().emit(project.modules)
    component_diagram = MermaidOverviewEmitter().emit(project.modules)

    seqs: dict[str, tuple[str, str]] = {}
    for function, calls in call_from_same_function.items():
        seq, metadata = MermaidSequenceEmitter().emit(calls)
        seqs[function] = (seq, metadata)
    return seqs, class_diagrams, component_diagram


def enrich_report_with_diagrams(placeholder_doc: list[str], diagrams: dict, component_diagram: str, class_diagrams: dict) -> str:
    """Fügt Diagramme aus dem `diagrams`-Dictionary in den `final_report` ein."""
    enriched_report = []

    current_name = ""
    for line in placeholder_doc:
        if "<Placeholder for Diagram>" in line: 
            for filename, seq_diagram in diagrams.items():
                    if filename in current_name:
                        enriched_report.append(f"*    **Sequence diagram for {filename}**")
                        enriched_report.append(seq_diagram[0])
                        enriched_report.append(seq_diagram[1])
                        break
            
            for class_name, class_diagram in class_diagrams.items():
                if re.search(rf"\b{re.escape(class_name)}\b", current_name):
                    enriched_report.append(f"*    **Class visualization for {class_name}**")
                    enriched_report.append(class_diagram[0])
                    enriched_report.append(class_diagram[1])
                    break
            current_name = ""
            continue
        enriched_report.append(line)
        if "#### Function:" in line or "#### Class:" in line:
            current_name = line
        
        if r"## [0-9\.]? Architecture" in line:
            enriched_report.append(component_diagram)

        # new logic for placeholder        
    return "\n".join(enriched_report)


def create_placeholders(final_doc: str) -> list[str]:
    """Insert Placeholders for diagrams."""

    lines_doc: list[str] = final_doc.splitlines()

    n = len(lines_doc)
    new_doc = []
    for i in range(n):
        new_doc.append(lines_doc[i])
        # edge cases for last diagram
        if i == n - 2:
            new_doc.append("<Placeholder for Diagram>")
            break
        next_line = lines_doc[i + 1]
        # normal iteration for the rest
        if ("#### Function" in next_line or 
            "#### Class" in next_line or 
            "### File" in next_line):
            new_doc.append("<Placeholder for Diagram>")
    
    return new_doc


if __name__ == "__main__":
    from getRepo import GitRepository, RepoFile
    from pathlib import Path

    repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    # repo_url = "https://github.com/pallets/flask"
    repo = GitRepository(repo_url)
    all_files = repo.get_all_files()
    py_files: list[RepoFile] = []
    for file in all_files:
        if file.path.endswith(".py"):
            py_files.append(file)
    diagrams_per_function, class_diagram, component_diagram = main_diagram_generation(py_files)

    for d in diagrams_per_function.values():
        with open("Flask Diagrams_seq.md", "a", encoding="utf-8") as file:
            file.write(f"{d[0]}\n")
        
    for cd in class_diagram.values():
        with open("Flask Diagrams_class.md", "a", encoding="utf-8") as file:
            file.write(f"{cd[0]}\n")
    
    with open("Flask Diagrams_overview.md", "a", encoding="utf-8") as file:
        file.write(component_diagram)    

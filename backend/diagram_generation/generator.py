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

        collector = SymbolCollector(module_name, packages)
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


def main_diagram_generation(py_files: list[str]) -> tuple[dict, dict, str]:
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

    seqs: dict[str, str] = {}
    for function, calls in call_from_same_function.items():
        seq = MermaidSequenceEmitter().emit(calls)
        seqs[function] = seq

    return seqs, class_diagrams, component_diagram


def enrich_report_with_diagrams(final_report: str, diagrams: dict, component_diagram: str, class_diagrams: dict) -> str:
    """Fügt Diagramme aus dem `diagrams`-Dictionary in den `final_report` ein."""
    report_lines = final_report.splitlines()
    enriched_report = []

    for line in report_lines:
        enriched_report.append(line)
        if "#### Function:" in line:
            for filename, seq_diagram in diagrams.items():
                    if filename in line:
                        enriched_report.append(f"   **Sequence diagram for {filename}**")
                        enriched_report.append(seq_diagram)
        
        if r"## [0-9\.]? Architecture" in line:
            enriched_report.append(component_diagram)
        
        
        if "#### Class:" in line:
            for class_name, class_diagram in class_diagrams.items():
                if re.search(rf"\b{re.escape(class_name)}\b", line):
                    enriched_report.append(class_diagram)

        
    return "\n".join(enriched_report)


if __name__ == "__main__":
    from getRepo import GitRepository, RepoFile
    from pathlib import Path

    repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    repo = GitRepository(repo_url)
    all_files = repo.get_all_files()
    py_files: list[RepoFile] = []
    for file in all_files:
        if file.path.endswith(".py"):
            py_files.append(file)
    diagrams_per_function, class_diagram, component_diagram = main_diagram_generation(py_files)

    with open(Path(__file__).parent.parent.parent / "result" / "report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md", "r") as file:
        report = file.read()
    
    enriched_report = enrich_report_with_diagrams(report, diagrams_per_function, component_diagram, class_diagram)
    with open("Test_enriched_report_2.md", "w") as file:
        file.write(enriched_report)

    

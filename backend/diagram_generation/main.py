import ast
from pathlib import Path
import sys


sys.path.append(str(Path(__file__).parent.parent))
from getRepo import GitRepository, RepoFile
from call_resolver import CallResolver
from callgraph import TreeVisitor
from data_types import ProjectIndex, ResolvedCall, FunctionSymbol
from emitter import (
    MermaidClassDiagramEmitter, 
    MermaidSequenceEmitter
)
from symbol_collector import SymbolCollector, attach_with_parents


def analyze_project(py_files: list[RepoFile]):
    project = ProjectIndex(modules={})
    trees: dict[str, ast.AST] = {}

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
        visitor = TreeVisitor(module)
        visitor.visit(tree)
        raw_calls[module_name] = (visitor.calls)

    resolver = CallResolver(project)
    resolved_calls = resolver.resolve_all(raw_calls)

    return project, resolved_calls

def construct_overview_diagram(project: ProjectIndex) -> list[list[str]]:
    packages = []
    for mod in project.modules.values():
        packages.extend([mod.overlying_packages])

    overlying_packages: set[str] = set(p[0] for p in packages)

    module_imports = [{m: m.imports.keys() } for m in project.modules.values()]
                      
    
    # sorted_packages = sorted(packages, key=lambda x: len(x), reverse=True)
    
    # for idx, p in enumerate(sorted_packages[:]):
    #     if len(packages[idx + 1]) < len(p):
    #         packages = packages[:idx + 1]

    return packages
def main_diagram_generation():
    # repo_url = "https://github.com/christiand03/repo-onboarding-agent"
    # repo_url = "https://github.com/brkahmed/taskly"
    repo_url = "https://github.com/pallets/flask"
    repo = GitRepository(repo_url)
    all_files = repo.get_all_files()
    py_files = [f for f in all_files if f.path.endswith(".py")]


    project, resolved_calls = analyze_project(py_files)
        
    # packages = construct_overview_diagram(project)

    # print(packages)
    call_from_same_function: dict[FunctionSymbol, list[ResolvedCall]] = {}

    for res_calls in resolved_calls.values():
        if len(res_calls) == 0:
            continue
        for res_call in res_calls:
            caller_name = res_call.caller.qualname
            if caller_name not in call_from_same_function:
                call_from_same_function[caller_name] = []
            call_from_same_function[caller_name].append(res_call)

    seqs: list[str] = []
    for calls in call_from_same_function.values():
        seq = MermaidSequenceEmitter().emit(calls)
        seqs.append(seq)
    # cls = MermaidClassDiagramEmitter().emit(project.modules)

    print("\n=== SEQUENCE DIAGRAMS ===\n")
    for s in seqs:
        with open("SequenceDiagrams_Flask_3.md", "a") as f:
            f.write(f"{s}\n")
    # print("\n=== CLASS DIAGRAM ===\n")
    # with open("ClassDiagram.md", "w") as f:
    #     f.write(cls)

if __name__ == "__main__":
    main_diagram_generation()

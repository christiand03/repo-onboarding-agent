from ast import (
    Attribute,
    ClassDef,
    FunctionDef,  
    Name, 
    NodeVisitor,
)
from typing import(
    Optional
)

from diagram_generation.data_types import (
    CallContext,
    ClassSymbol,
    FunctionSymbol,
    ModuleSymbol,
    RawCall,
    ProjectIndex
)
class TreeVisitor(NodeVisitor):

    def __init__(self, module: ModuleSymbol, project: ProjectIndex):
        self.module = module
        self.project = project
        self.current_function: Optional[FunctionSymbol] = None
        self.current_class: Optional[ClassSymbol] = None
        self.calls: list[RawCall] = []

    
    def visit_ClassDef(self, node: ClassDef) -> None:
        prev_class = self.current_class
        self.current_class = self.module.classes.get(node.name)
        self.generic_visit(node)
        self.current_class = prev_class

    
    def visit_FunctionDef(self, node: FunctionDef) -> None:
        prev_function = self.current_function
        if self.current_class:
            self.current_function = self.current_class.methods.get(node.name)
        else:
            self.current_function = self.module.functions.get(node.name)

        self.generic_visit(node)
        self.current_function = prev_function


    def visit_Call(self, node) -> None:
        if not self.current_function:
            return
        
        if isinstance(node.func, Name):
            if node.func.id not in self.module.functions:
                return
        elif isinstance(node.func, Attribute):
            
            if node.func not in self.project.modules.values():
                return
        self.calls.append(
            RawCall(
                caller=self.current_function,
                func_node=node.func,
                lineno=node.lineno,
                context=CallContext(
                    module=self.module,
                    function=self.current_function,
                    classes=self.current_class
                )
            )
        )
        self.generic_visit(node)
   
from ast import expr
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

   
@dataclass
class FunctionSymbol:
    name: str
    module: str
    cls: Optional[str]
    qualname: str
    asynchron: False
    input_params: list[str]
    return_symb: str
    lineno: int
    end_lineno: int


@dataclass
class ClassSymbol:
    name: str
    module: str
    methods: dict[str, FunctionSymbol]
    lineno: int
    end_lineno: int
    inheritance: list[str]


@dataclass
class ModuleSymbol:
    name: str
    overlying_packages: list[str]
    functions: dict[str, FunctionSymbol]
    classes: dict[str, ClassSymbol]
    imports: dict[str, str]


@dataclass
class CallContext:
    module: ModuleSymbol
    function: FunctionSymbol
    classes: Optional[ClassSymbol]


@dataclass
class RawCall:
    caller: FunctionSymbol
    func_node: expr
    lineno: int
    context: CallContext


class CallType(Enum):
    DIRECT = "direct"
    METHOD = "method"
    IMPORTED = "imported"
    DYNAMIC = "dynamic"
    UNKNOWN = "unknown"


@dataclass
class ResolvedCall:
    caller: FunctionSymbol
    callee: Union[ClassSymbol, FunctionSymbol, None]
    call_type: CallType
    lineno: int

@dataclass
class ProjectIndex:
    modules: dict[str, ModuleSymbol]

    def all_classes(self) -> list[ClassSymbol]:
        return [
            clss 
            for module in self.modules.values()
            for clss in module.classes.values()
        ]
    

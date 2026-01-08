import ast
import sys

from pathlib import Path


sys.path.append(Path(__file__).parent.parent)
from data_types import (
    CallType,
    RawCall,
    ResolvedCall,
    ProjectIndex
)

class CallResolver:

    def __init__(self, project: ProjectIndex):
        self.project = project

    
    def resolve_all(self, calls: dict[str, list[RawCall]]) -> dict[str, list[ResolvedCall]]:
        resolved: dict[str, list[ResolvedCall]] = {}

        for mod, call in calls.items():
            if mod not in resolved:
                resolved[mod] = []
            for c in call:
                resolved[mod].extend(self.resolved(c))
        return resolved
    

    def resolved(self, call: RawCall) -> list[ResolvedCall]:
        node = call.func_node

        if isinstance(node, ast.Name):
            return self._resolve_name(call, node)
        
        if isinstance(node, ast.Attribute):
            return self._resolve_attribute(call, node)
        
        return [
            ResolvedCall(
                caller=call.caller,
                callee=None,
                call_type=CallType.UNKNOWN,
                lineno=call.lineno
            )
        ]

    def _resolve_name(self, call: RawCall, node: ast.Name) -> list[ResolvedCall]:
        name = node.id
        module = self.project.modules[call.context.module.name]

        if name in module.functions:
            return [
                ResolvedCall(
                    caller=call.caller,
                    callee = module.functions[name],
                    call_type = CallType.DIRECT,
                    lineno = call.lineno
                )
            ]
        
        if name in module.imports:
            target = module.imports[name]
            mod_name, _, attr = target.rpartition(".")
            target_module = self.project.modules.get(mod_name)
            if target_module in target_module.functions:
                return [
                    ResolvedCall(
                        caller = call.caller,
                        callee = module.functions[attr],
                        call_type = CallType.IMPORTED,
                        lineno = call.lineno
                    )
                ]
            return [
                ResolvedCall(
                    caller=call.caller, 
                    callee=None,
                    call_type=CallType.UNKNOWN,
                    lineno=call.lineno
                )
            ]
    

    def _resolve_attribute(self, call: RawCall, node: ast.Attribute) -> list[ResolvedCall]:
        attr = node.attr

        if isinstance(node.value, ast.Name) and node.value.id == "self":
            cls = call.context.classes
            if cls and attr in cls.methods:
                return [
                    ResolvedCall(
                        caller=call.caller,
                        callee=cls.methods[attr],
                        call_type=CallType.METHOD,
                        lineno=call.lineno
                    )
                ]
        
        if isinstance(node.value, ast.Name):
            mod_alias = node.value.id
            module = self.project.modules[call.context.module.name]

            if mod_alias in module.imports:
                target_module = self.project.modules.get(module.imports[mod_alias])
            
                if target_module and attr in target_module.functions:
                    return [
                        ResolvedCall(
                            caller=call.caller,
                            callee=target_module.functions[attr],
                            call_type=CallType.IMPORTED,
                            lineno=call.lineno
                        )
                    ]
        

        candidates = []
        for cls in self.project.all_classes():
            if attr in cls.methods:
                candidates.append(
                    ResolvedCall(
                        caller=call.caller,
                        callee=cls.methods[attr],
                        call_type=CallType.DYNAMIC,
                        lineno=call.lineno,
                    )
                )

        if candidates:
            return candidates

        return [
            ResolvedCall(
                caller=call.caller, 
                callee=None, 
                call_type=CallType.UNKNOWN, 
                lineno=call.lineno
            )
        ]        


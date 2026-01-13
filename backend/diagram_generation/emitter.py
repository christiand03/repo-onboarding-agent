from diagram_generation.data_types import (
    ModuleSymbol,
    ResolvedCall
)


class MermaidSequenceEmitter:
    def emit(self, calls: list[ResolvedCall]) -> str:
        lines: list[str] = ["```mermaid"]
        lines.append("sequenceDiagram")

        participants = self._collect_participants(calls)
        for p in participants:
            lines.append(f"    participant {p}")

        for call in sorted(calls, key=lambda c: c.lineno):
            lines.append(self._emit_call(call))
            if call.callee.return_symb:
                lines.append(self._emit_response(call))
        lines.append("```")
        return "\n".join(lines)


    def _collect_participants(self, calls: list[ResolvedCall]) -> list[str]:
        participants: list[str] = []
        for call in calls:
            participants.append(mermaid_id(call.caller.qualname))
            if call.callee and call.callee not in participants:
                participants.append(
                    mermaid_id(call.callee.qualname)
                )
            else:
                participants.append("?")
        return participants


    def _emit_response(self, call:ResolvedCall) -> str:
        resolved_callee = mermaid_id(call.callee.qualname)
        resolved_caller = mermaid_id(call.caller.qualname)
        
        return f"    {resolved_callee} ->> {resolved_caller}: return"
    
    
    def _emit_call(self, call: ResolvedCall) -> str:
        caller = mermaid_id(call.caller.qualname)
        if call.callee:
            callee = mermaid_id(call.callee.qualname)
            label= call.callee.input_params
        else:
            callee = "?"
            label = "unknown"
        return f"    {caller} ->> {callee}: {label}"


class MermaidOverviewArchitectureEmitter:
    def emit(self, modules: dict[str, ModuleSymbol]) -> str:
        lines = ["graph TD"]
        
        for module in modules.values():
            src = module.name.split(".")[-1]

            for target in module.imports.values():
                if target in modules:
                    dst = target.split(".")[-1]
                    lines.append(f"    {src} --> {dst}")

        return "\n".join(lines)


class MermaidClassDiagramEmitter:
    def emit(self, modules: dict[str, ModuleSymbol]) -> str:
        lines: list[str] = ["classDiagram"]

        for module in modules.values():
            for cls in module.classes.values():
                class_id = mermaid_id(cls.name)
                lines.append(f"    class {class_id} {{")

                for method in cls.methods.values():
                    if method.name.startswith(r"_[a-Z]+"):
                        lines.append(f"        -{method.name}()")
                    lines.append(f"        +{method.name}()")

                lines.append("    }")

        for module in modules.values():
            src = mermaid_id(module.name)
            for imported in module.imports.values():
                dst = mermaid_id(imported)
                lines.append(f"    {src} ..> {dst} : imports")

        return "\n".join(lines)


def mermaid_id(name: str) -> str:
    """Mermaid identifier dürfen keine Punkte im Namen enthalten."""
    return name.replace(".", "_")
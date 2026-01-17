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
        lines = ["```mermaid"]
        lines.append("graph LR")
        import_list: list[str] = [ key for module in modules.values() for key in module.imports.keys()]
        filtered_list: list[str] = []

        for import_name in import_list:
            if import_name in filtered_list:
                continue
            filtered_list.append(import_name)


        for module in modules.values():
            src = module.name.split(".")[-1]
            for target in filtered_list:
                if target in modules:
                    dst = target.split(".")[-1]
                    lines.append(f"    {src} --> {dst}")
        lines.append("```")
        return "\n".join(lines)


class MermaidClassDiagramEmitter:
    def emit(self, modules: dict[str, ModuleSymbol]) -> dict[str, str]:

        class_diagrams: dict[str, str] = {}
        for module in modules.values():
            for name, cls in module.classes.items():
                lines: list[str] = ["```mermaid"]
                lines.append("classDiagram")
                class_id = mermaid_id(cls.name)
                lines.append(f"    class {class_id} {{")

                for method in cls.methods.values():
                    if method.name.startswith("_") and method.name != "__init__":
                        lines.append(f"        -{method.name}()")
                        continue
                    lines.append(f"        +{method.name}()")

                lines.append("    }")
                lines.append("```")
                class_diagrams[name] = "\n".join(lines)
                lines = []


        # for module in modules.values():
        #     src = mermaid_id(module.name)
        #     for imported in module.imports.values():
        #         dst = mermaid_id(imported)
        #         lines.append(f"    {src} ..> {dst} : imports")
        # lines.append("```")
        return class_diagrams


def mermaid_id(name: str) -> str:
    """Mermaid identifier dürfen keine Punkte im Namen enthalten."""
    return name.replace(".", "_")
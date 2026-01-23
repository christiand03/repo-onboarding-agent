from diagram_generation.data_types import (
    ModuleSymbol,
    ResolvedCall
)


class MermaidSequenceEmitter:
    def emit(self, calls: list[ResolvedCall]) -> tuple[str, str]:
        lines: list[str] = ["```mermaid"]
        lines.append("sequenceDiagram")
        metadata: list[str] = ["*    **Metadata for Diagram:**"]
        participants = self._collect_participants(calls)
        for p in participants:
            lines.append(f"    participant {p}")

        for call in calls:
            metadata.append(f"`{call.caller.name}: {call.caller.lineno}-{call.caller.end_lineno}`")
            break

        for call in sorted(calls, key=lambda c: c.lineno):
            lines.append(self._emit_call(call))
            if call.callee:

                lines.append(self._emit_response(call))
                metadata_for_callee = f"`{call.callee.name}: {call.callee.lineno}-{call.callee.end_lineno}`"
                if metadata_for_callee not in metadata:
                    metadata.append(metadata_for_callee)
        lines.append("```")
        return "\n".join(lines), " ".join(metadata)


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
        return f"    {resolved_callee} ->> {resolved_caller}: {call.callee.return_symb}"
    
    
    def _emit_call(self, call: ResolvedCall) -> str:
        caller = mermaid_id(call.caller.qualname)
        if call.callee:
            callee = mermaid_id(call.callee.qualname)
            label= call.callee.input_params
        else:
            callee = "?"
            label = "unknown"
        return f"    {caller} ->> {callee}: {label}"


class MermaidOverviewEmitter:
    def emit(self, modules: dict[str, ModuleSymbol]) -> str:
        """
        Erstellt ein High-Level Architektur-Diagramm mit nur den Top-Level Verzeichnissen.
        """
        lines = ["```mermaid"]
        lines.append("graph TD")
        
        # Extrahiere Top-Level Verzeichnisse
        top_level_dirs = self._extract_top_level_directories(modules)
        
        if not top_level_dirs:
            lines.append('    root["📦 root"]')
            lines.append("```")
            return "\n".join(lines)
        
        # Erstelle Knoten für jedes Top-Level-Verzeichnis
        dir_nodes = {}
        for dir_name in sorted(top_level_dirs):
            node_id = self._sanitize_id(dir_name)
            dir_nodes[dir_name] = node_id
            module_count = self._count_modules_in_directory(modules, dir_name)
            lines.append(f'    {node_id}["📦 {dir_name}<br/>({module_count} Module)"]')
        
        # Extrahiere Abhängigkeiten zwischen Verzeichnissen
        relationships = self._extract_directory_dependencies(modules, top_level_dirs)
        
        # Füge eindeutige Beziehungen hinzu
        for src_dir, target_dir in sorted(relationships):
            src_id = dir_nodes.get(src_dir)
            target_id = dir_nodes.get(target_dir)
            if src_id and target_id:
                lines.append(f"    {src_id} --> {target_id}")
        
        lines.append("```")
        return "\n".join(lines)

    def _extract_top_level_directories(self, modules: dict[str, ModuleSymbol]) -> set[str]:
        """Extrahiert die obersten Verzeichnisse."""
        top_level = set()
        
        for module in modules.values():
            if module.overlying_packages:
                top_level.add(module.overlying_packages[0])
            else:
                top_level.add("root")
        
        return top_level

    def _count_modules_in_directory(self, modules: dict[str, ModuleSymbol], top_dir: str) -> int:
        """Zählt Module in einem Top-Level-Verzeichnis."""
        count = 0
        for module in modules.values():
            if module.overlying_packages and module.overlying_packages[0] == top_dir:
                count += 1
            elif not module.overlying_packages and top_dir == "root":
                count += 1
        return count

    def _extract_directory_dependencies(
        self,
        modules: dict[str, ModuleSymbol],
        top_level_dirs: set[str]
    ) -> set[tuple[str, str]]:
        """
        Findet Abhängigkeiten zwischen Top-Level-Verzeichnissen.
        Für jedes Modul: schaue den obersten Ordner an,
        dann check alle Imports auf andere oberste Ordner.
        """
        relationships = set()
        
        for module in modules.values():
            # Bestimme den obersten Ordner des aktuellen Moduls
            source_top_dir = module.overlying_packages[0] if module.overlying_packages else "root"
            
            # Gehe durch alle Imports dieses Moduls
            for import_path in module.imports.values():
                # Extrahiere den ersten Segment des Import-Pfads
                first_segment = import_path.split(".")[0]
                
                # Prüfe, ob dieser erste Segment ein bekannter Top-Level-Dir ist
                if first_segment in top_level_dirs and first_segment != source_top_dir:
                    relationships.add((source_top_dir, first_segment))
        
        return relationships

    def _sanitize_id(self, name: str) -> str:
        """Konvertiert Namen in valide Mermaid-IDs."""
        return name.replace("-", "_").replace(" ", "_").replace(".", "_")
        
       
class MermaidClassDiagramEmitter:
    def emit(self, modules: dict[str, ModuleSymbol]) -> dict[str, tuple[str, str]]:

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
                metadata = f"*    **Metadata for Class diagram:** `{cls.name}: {cls.lineno}-{cls.end_lineno}`"
                class_diagrams[name] = ("\n".join(lines), metadata)
                lines = []
        return class_diagrams


def mermaid_id(name: str) -> str:
    """Mermaid identifier dürfen keine Punkte im Namen enthalten."""
    return name.replace(".", "/")
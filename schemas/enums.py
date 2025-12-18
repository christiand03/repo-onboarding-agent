from enum import Enum

class AnalysisMode(str, Enum):
    "Detailgrad der Analyse"
    OVERVIEW = "overview"
    STANDARD = "standard"
    DETAILED = "detailed"
    DEEP_DIVE = "deep_dive"


class DiagramFocus(str, Enum):
    """Schwerpunkt der Visualisierung im Diagramm."""
    ARCHITECTURE = "architecture"
    DATA_FLOW = "data_flow"
    DEPENDENCIES = "dependencies"
    CALL_GRAPH = "call_graph"


class DiagramType(str, Enum):
    """Mermaid Diagramm-Typen"""
    CLASS_DIAGRAM = "classDiagram"
    SEQUENCE_DIAGRAM = "sequenceDiagram"
    FLOWCHART = "flowchart"
    STATE_DIAGRAM = "stateDiagram"
    GRAPH = "graph"
    CALL_GRAPH = "callgraph"
    FILE_DEPENCY = "fileDependencyGraph"


class GraphType(str, Enum):
    """Typ des Input-Graphen"""
    CALLGRAPH = "callgraph"
    DEPENDENCY = "dependency"
    COMBINED = "combined"
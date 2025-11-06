from typing import TypedDict, List, Optional, Literal

# --------- Helper LLM FUNCTION OUTPUT Schema ----------
class ParameterDescription(TypedDict):
    """Describes a single parameter of a function."""
    name: str
    type: str
    description: str

class ReturnDescription(TypedDict):
    """Describes the return value of a function."""
    name: str
    type: str
    description: str

class UsageContext(TypedDict):
    """Describes the calling context of a function."""
    calls: List[str]
    called_by: List[str]

class FunctionDescription(TypedDict):
    """Contains the detailed analysis of a function's purpose and signature."""
    overall: str
    parameters: List[ParameterDescription]
    returns: List[ReturnDescription]
    usage_context: UsageContext

class FunctionAnalysis(TypedDict):
    """The main TypedDict representing the entire JSON schema for a function."""
    identifier: str
    description: FunctionDescription
    error: Optional[str]


# -------- Helper LLM CLASS OUTPUT Schema ----------
class ConstructorDescription(TypedDict):
    """Describes the __init__ method of a class."""
    description: str
    parameters: List[ParameterDescription]

class ClassContext(TypedDict):
    """Describes the class's external dependencies and primary points of instantiation."""
    dependencies: str    
    instantiated_by: str   

class ClassDescription(TypedDict):
    """Contains the detailed analysis of a class's purpose, constructor, and methods."""
    overall: str
    init_method: ConstructorDescription
    methods: List[FunctionAnalysis]
    usage_context: ClassContext

class ClassAnalysis(TypedDict):
    """The main TypedDict for the entire JSON schema for a class."""
    identifier: str
    description: ClassDescription
    error: Optional[str]


# -------- Helper LLM FUNCTION INPUT Schema --------
class FunctionContextInput(TypedDict):
    """Structured context for analyzing a function."""
    calls: List[str]      
    called_by: List[str]  

class FunctionAnalysisInput(TypedDict):
    """The required input to generate a FunctionAnalysis object."""
    mode: Literal["function_analysis"]
    source_code: str
    imports: List[str]
    context: FunctionContextInput


# --- Helper LLM CLASS INPUT Schema ---
class ClassContextInput(TypedDict):
    """Structured context for analyzing a class."""
    dependencies: List[str]      
    instantiated_by: List[str]   
    methods_analysis: List[FunctionAnalysis] 

class ClassAnalysisInput(TypedDict):
    """The required input to generate a ClassAnalysis object."""
    mode: Literal["class_analysis"]
    source_code: str
    imports: List[str]
    context: ClassContextInput






# How to access a Schema in another File
"""
from your_project.schemas.types import FunctionAnalysis # Clear and explicit import

def process_analysis_data(data: dict) -> None:
    # Cast the incoming dict to your TypedDict for static analysis
    analysis_result: FunctionAnalysis = data
    
    # Now your IDE and type checkers know the structure
    print(f"Analyzing function: {analysis_result['identifier']}")
    if analysis_result['error']:
        print(f"An error occurred: {analysis_result['error']}")
"""
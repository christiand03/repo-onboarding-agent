from typing import List, Optional, Literal
from pydantic import BaseModel, ValidationError

from schemas.enums import (
    AnalysisMode,
    DiagramFocus,
    DiagramType
)
# --------- Helper LLM FUNCTION OUTPUT Schema ----------

class ParameterDescription(BaseModel):
    """Describes a single parameter of a function."""
    name: str
    type: str
    description: str

class ReturnDescription(BaseModel):
    """Describes the return value of a function."""
    name: str
    type: str
    description: str

class UsageContext(BaseModel):
    """Describes the calling context of a function."""
    calls: str
    called_by: str

class FunctionDescription(BaseModel):
    """Contains the detailed analysis of a function's purpose and signature."""
    overall: str
    parameters: List[ParameterDescription]
    returns: List[ReturnDescription]
    usage_context: UsageContext

class FunctionAnalysis(BaseModel):
    """The main model representing the entire JSON schema for a function."""
    identifier: str
    description: FunctionDescription
    error: Optional[str] = None


# -------- Helper LLM CLASS OUTPUT Schema ----------

class ConstructorDescription(BaseModel):
    """Describes the __init__ method of a class."""
    description: str
    parameters: List[ParameterDescription]

class ClassContext(BaseModel):
    """Describes the class's external dependencies and primary points of instantiation."""
    dependencies: str
    instantiated_by: str

class ClassDescription(BaseModel):
    """Contains the detailed analysis of a class's purpose, constructor, and methods."""
    overall: str
    init_method: ConstructorDescription
    methods: List[FunctionAnalysis]
    usage_context: ClassContext

class ClassAnalysis(BaseModel):
    """The main model for the entire JSON schema for a class."""
    identifier: str
    description: ClassDescription
    error: Optional[str] = None


# CALL INFO MODEL

class CallInfo(BaseModel):
    """
    Represents a specific call event from the relationship analyzer.
    Used in 'called_by' and 'instantiated_by' lists.
    """
    file: str
    function: str  # Name des Aufrufers
    mode: str      # z.B. 'method', 'function', 'module'
    line: int


# -------- Helper LLM FUNCTION INPUT Schema --------

class FunctionContextInput(BaseModel):
    """Structured context for analyzing a function."""
    calls: List[str]
    called_by: List[CallInfo]

class FunctionAnalysisInput(BaseModel):
    """The required input to generate a FunctionAnalysis object."""
    mode: Literal["function_analysis"]
    identifier: str
    source_code: str
    imports: List[str]
    context: FunctionContextInput


# ------ Helper LLM CLASS INPUT Schema  ------

class MethodContextInput(BaseModel):
    """Structured context for a classes methods"""
    identifier: str
    calls: List[str]
    called_by: List[CallInfo]
    args: List[str]
    docstring: Optional[str]
    
class ClassContextInput(BaseModel):
    """Structured context for analyzing a class."""
    dependencies: List[str]
    instantiated_by: List[CallInfo]
    method_context: List[MethodContextInput]

class ClassAnalysisInput(BaseModel):
    """The required input to generate a ClassAnalysis object."""
    mode: Literal["class_analysis"]
    identifier: str
    source_code: str
    imports: List[str]
    context: ClassContextInput

# --------- Diagram Request Schema ----------
class DiagramRequest(BaseModel):
    """Input schema for requesting a diagram generation."""
    nodes: list[dict]
    edges: list[tuple]

    mode: AnalysisMode = AnalysisMode.STANDARD
    focus: DiagramFocus = DiagramFocus.ARCHITECTURE


class GraphInput(BaseModel):
    """Repräsentiert deinen CallGraph in serialisierbarer Form"""
    
    nodes: list[dict]
    edges: list[tuple]
    graph_type: str
    metadata: dict = {}

class DiagramOutput(BaseModel):
    """Output schema for generated diagram information."""
    diagramtype: DiagramType
    mermaid_code: str
    explanation: str


# ----------------------- Example Dictionaries --------------------------
if __name__ == "__main__":
    # Example Dictionary Structure FunctionAnalysis Output
    valid_function_output = {
        "identifier": "my_module.utils.calculate_sum",
        "description": {
            "overall": "This function takes two integers and returns their sum.",
        
            "parameters": [
                {
                    "name": "x",
                    "type": "int",
                    "description": "The first integer operand."
                },
                {
                    "name": "y",
                    "type": "int",
                    "description": "The second integer operand."
                }
            ],
        
            "returns": [
                {
                    "name": "total",
                    "type": "int",
                    "description": "The sum of x and y."
                }
            ],
        
            "usage_context": {
                "calls": " bla bla logging.info",
                "called_by": "bla bla api.v1.endpoints.add_numbers and scripts.run_daily_job"
            }
        },
        # The 'error' field is optional. We can omit it, and it will default to None.
        # Or we can explicitly set it to None.
        "error": None 
    }

    # How to Validate and Access Dictionary
    try:
        # Pydantic will recursively parse the nested dictionaries into the correct model instances.
        function_analysis_output = FunctionAnalysis.model_validate(valid_function_output)
        print("Function Analysis validated.")
        print(f"Overall Description: {function_analysis_output.description.overall}")

    except ValidationError as e:
        print("Validation failed!")
        print(e)

    valid_class_output = {
        "identifier": "AST_Analyser",
        "description": {
            "overall": "Class to create the AST",
            "init_method": {
                "description": "Bla",
                "parameters": [
                    {
                        "name": "Parameter 1",
                        "type": "I dont know",
                        "description": "Here to do stuff"
                    },
                    {
                        "name": "Parameter 2",
                        "type": "still dont know",
                        "description": "doesnt do stuff"
                    }
                ]
            },
            "methods": [
                function_analysis_output,
                function_analysis_output
            ],
            "usage_context": {
                "dependencies": "bla bla A and B",
                "instantiated_by": "bla bla A and B"
            }
        },
        "error": "None"
    }

    try:
        # Pydantic will recursively parse the nested dictionaries into the correct model instances.
        class_analysis_output = ClassAnalysis.model_validate(valid_class_output)
        print("Class Analysis validated.")

    except ValidationError as e:
        print("Validation failed!")
        print(e)


    valid_function_input = {
        "mode": "function_analysis",
        "identifier": "A",
        "source_code": "ABC",
        "imports": ["pandas", "numpy"],
        "context": {
            "calls": ["function1", "function2"],
            "called_by": ["functionA", "functionB"]
        }
    }

    try:
        function_analysis_input = FunctionAnalysisInput.model_validate(valid_function_input)
        print("Function Input validated.")

    except ValidationError as e:
        print("Validation failed!")
        print(e)

    valid_class_input = {
        "mode": "class_analysis",
        "identifier": "A",
        "source_code": "ABC",
        "imports": ["pandas", "numpy"],
        "context": {
            "dependencies": ["function1", "function2"],
            "instantiated_by": ["functionA", "functionB"],
            "methods_analysis": [
                valid_function_output,
                valid_function_output
            ]
        }    
    }

    try:
        class_analysis_input = ClassAnalysisInput.model_validate(valid_class_input)
        print("Class Input validated.")

    except ValidationError as e:
        print("Validation failed!")
        print(e)
from typing import List, Optional, Literal
from pydantic import BaseModel, ValidationError

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
    calls: List[str]
    called_by: List[str]

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


# -------- Helper LLM FUNCTION INPUT Schema --------

class FunctionContextInput(BaseModel):
    """Structured context for analyzing a function."""
    calls: List[str]
    called_by: List[str]

class FunctionAnalysisInput(BaseModel):
    """The required input to generate a FunctionAnalysis object."""
    mode: Literal["function_analysis"]
    identifier: str
    source_code: str
    imports: List[str]
    context: FunctionContextInput


# ------ Helper LLM CLASS INPUT Schema  ------

class ClassContextInput(BaseModel):
    """Structured context for analyzing a class."""
    dependencies: List[str]
    instantiated_by: List[str]
    methods_analysis: List[FunctionAnalysis]

class ClassAnalysisInput(BaseModel):
    """The required input to generate a ClassAnalysis object."""
    mode: Literal["class_analysis"]
    identifier: str
    source_code: str
    imports: List[str]
    context: ClassContextInput


# Example Dictionary Structure FunctionAnalysis Output
valid_function_data = {
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
            "calls": ["logging.info"],
            "called_by": ["api.v1.endpoints.add_numbers", "scripts.run_daily_job"]
        }
    },
    # The 'error' field is optional. We can omit it, and it will default to None.
    # Or we can explicitly set it to None.
    "error": None 
}

# How to Validate and Access Dictionary
try:
    # Pydantic will recursively parse the nested dictionaries into the correct model instances.
    function_analysis_instance = FunctionAnalysis.model_validate(valid_function_data)
    print(f"Overall Description: {function_analysis_instance.description.overall}")

except ValidationError as e:
    print("Validation failed!")
    print(e)
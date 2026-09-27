from typing import Callable, Dict, Any, Type, List
from pydantic import BaseModel

class ToolRegistry:
    """
    Dynamically loads and validates registered tools.
    """
    def __init__(self):
        self._tools: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, func: Callable, input_model: Type[BaseModel], output_model: Type[BaseModel]):
        """
        Registers a tool with its validation models.
        """
        self._tools[name] = {
            "func": func,
            "input_model": input_model,
            "output_model": output_model
        }

    def execute(self, name: str, **kwargs) -> BaseModel:
        """
        Executes a registered tool, enforcing input and output contracts.
        """
        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found in registry.")
        
        tool = self._tools[name]
        
        # Validate Input
        validated_input = tool["input_model"](**kwargs)
        
        # Execute Domain Logic
        result = tool["func"](validated_input)
        
        # Validate Output
        if not isinstance(result, tool["output_model"]):
            raise TypeError(f"Tool '{name}' returned {type(result)}, expected {tool['output_model']}")
            
        return result

    def list_tools(self) -> List[str]:
        """Returns a list of registered tool names."""
        return list(self._tools.keys())

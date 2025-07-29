from pydantic import BaseModel
from pydantic import Field
from typing import Literal

class ToolParameters(BaseModel):
    cutting_diameter: float = Field(..., gt=0, example=6.8)
    overall_length: float = Field(..., gt=0, example=80)
    cutting_length: float = Field(..., gt=0, example=29.8)
    point_angle: float = Field(..., gt=0, lt=180, example=118)
    shank_diameter: float = Field(..., gt=0, example=6.8)
    shank_length: float = Field(..., gt=0, example=37.6)

class ToolRequest(BaseModel):
    tool_type: Literal["drill"]
    parameters: ToolParameters

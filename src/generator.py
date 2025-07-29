import cadquery as cq
import math
import uuid

from cadquery import Vector
from cadquery.cq import CQ
from models import ToolRequest
from fastapi import HTTPException

def generate_model(req: ToolRequest, out_path = f"/tmp/{uuid.uuid4()}.step"):
    dc = req.parameters.cutting_diameter
    pa = req.parameters.point_angle
    lc = req.parameters.cutting_length
    l = req.parameters.overall_length
    ls = req.parameters.shank_length
    ds = req.parameters.shank_diameter    
    if req.tool_type == "drill":
        tip_height = (dc / 2) / math.tan(math.radians(pa / 2))
        cutting_part = (
            cq.Workplane("XY")
            .circle(0.001)
            .workplane(offset = tip_height)
            .circle(dc/2)
            .loft(combine = True)
            .faces(">Z")
            .workplane()
            .circle(dc/2)
            .extrude(lc - tip_height)
            )

        non_cutting_part = (
            cq.Workplane("XY")
            .workplane(offset = lc)
            .circle(dc/2)
            .extrude(l - (lc + ls))
            .faces(">Z")
            .workplane()
            .circle(ds/2)
            .extrude(ls)
            )
        asm = cq.Assembly()
        asm.add(cutting_part, name="cut", color=cq.Color(0.627, 0.627, 0.627))
        asm.add(non_cutting_part, name="no-cut", color=cq.Color(0.392, 0.392, 0.392))
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported tool_type: {req.tool_type}")
    asm.save(out_path)
    return out_path

import cadquery as cq

def generate_model(diameter: float, length: float, out_path: str = "../models/tool.step"):
    model = cq.Workplane("XY").circle(diameter / 2).extrude(length)
    cq.exporters.export(model, out_path)
    return out_path

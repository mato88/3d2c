from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from generator import generate_model

app = FastAPI()

@app.get("/generate")
def generate_tool(
    diameter: float = Query(10.0, gt=0, lt=100, description="Диаметр инструмента (мм)"),
    length: float = Query(50.0, gt=0, lt=300, description="Длина инструмента (мм)")
):
    path = generate_model(diameter, length)
    return FileResponse(path, media_type='application/step', filename='tool.step')

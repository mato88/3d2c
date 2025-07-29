from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from models import ToolRequest
from generator import generate_model

app = FastAPI()

@app.post("/generate")
def generate_tool(req: ToolRequest):
    path = generate_model(req)
    return FileResponse(path, media_type='application/step', filename='tool.step')

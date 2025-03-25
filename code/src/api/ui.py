import os
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from llm import classify_email
from llm.models import all_models

routes = APIRouter()

static_dir = os.path.join(os.path.dirname(__file__), "static")

# Serve static files (like the HTML page)
routes.mount("/static", StaticFiles(directory=static_dir), name="static")

@routes.get("/", response_class=HTMLResponse)
def serve_html():
    with open(f"{static_dir}/index.html", "r") as file:
        return HTMLResponse(content=file.read())

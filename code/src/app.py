from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api import controllers
from api import ui

app = FastAPI(
    title="Demo API"
)
app.include_router(controllers.routes, prefix='/api')
app.include_router(ui.routes)

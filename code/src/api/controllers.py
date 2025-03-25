from io import BytesIO
from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel

from api.extract_email_content import extract_eml_content
from llm import classify_email
from llm.models import all_models

routes = APIRouter()

@routes.get('/')
async def index():
    return 'Welcome to the api'

class EmailText(BaseModel):
    text: str

@routes.post('/analyzeEmail')
def analyze_email(email_text: EmailText):
    data = None
    error = None
    
    try:
        data = {name: classify_email(email_text.text, model) for name, model in all_models}
    except Exception as err:
        error = f"An error occurred: {err}"
        print(err)
    
    return {
        "data": data,
        "error": error
    }

@routes.post("/analyze")
async def upload_eml(file: UploadFile = File(...)):

    data = None
    error = None
    
    try:
        eml_bytes = await file.read()  # Read file content
        eml_data = extract_eml_content(BytesIO(eml_bytes))  # Extract content
        data = {name: classify_email(eml_data['text'], model) for name, model in all_models}
    except Exception as err:
        error = f"An error occurred: {err}"
        print(err)
    
    return {
        "data": data,
        "error": error
    }
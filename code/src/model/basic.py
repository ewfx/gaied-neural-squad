from json import JSONDecodeError, loads
import os
import re

from langchain_community.llms import HuggingFaceEndpoint
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from huggingface_hub import login

from model.types import request_types_str ,alternate_request_types

HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACE_TOKEN')

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

login(HUGGINGFACEHUB_API_TOKEN)
llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_length=1024, temperature=0.001, token=HUGGINGFACEHUB_API_TOKEN,
)

def classify_email(text: str):
    ai_role_prompt = 'Remember that you are a banker working on email classification'
    
    goal_prompt = """
    You are given an email. Extract the main intent of the email.

    Email:""" + text + """

    Imagine you are a banker and working on these emails the bank has received. Your answers must be with respect to the bank. Identify the request type, sub request type, and intent of the email. The list of request types are given in the below json file - the subrequest is inside the request.
    Ensure that the request and sub request you are returning is found in the list.
    """ + request_types_str + """
    """
    conversation_history = [
        SystemMessage(ai_role_prompt),
        HumanMessage(goal_prompt),
    ]
    
    print(f'## Prompting LLM ##')
    first_response = llm.invoke(conversation_history)
    conversation_history.append(AIMessage(first_response))
    print(f'## LLM RESPONSE #1: {first_response} ##')
    
    follow_up_question = """
        give the final output as a json file with the fields "requestType", "subRequestType", "intent".
        For example: 
        {
            "requestType":  "Au",
            "subRequestType": "None",
            "intent": "To change loan from branch Maine to Branch Oakland" 
        }
        Return only the json file, nothing else
    """
    conversation_history.append(HumanMessage(follow_up_question))
    
    print(f'## Prompting LLM ##')
    second_response: str = llm.invoke(conversation_history)
    print(f'## LLM RESPONSE #2 (type: {type(second_response)}): {second_response} ##')
    
    # formatted_response = second_response.removeprefix('AI\n```json\n').removesuffix('```')
    
    
    formatted_response = extract_json_from_string(second_response)
    
    return formatted_response

def extract_json_from_string(text):
    """
    Extracts the first valid JSON object found in a given string.
    :param text: The input string containing JSON.
    :return: Extracted JSON as a dictionary or None if not found.
    """
    # Regex pattern to match a JSON object
    json_pattern = re.compile(r'\{.*?\}', re.DOTALL)
    
    match = json_pattern.search(text)
    if match:
        try:
            return loads(match.group())  # Convert to dictionary
        except JSONDecodeError:
            return None  # Return None if the extraction fails
    
    return None  # No JSON found


from json import JSONDecodeError, loads
import re


def compare_string_fuzzy(str1: str, str2: str):
    return str1.replace(' ', '').lower() == str2.replace(' ', '').lower()

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

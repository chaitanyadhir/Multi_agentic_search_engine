import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_response(prompt: str) -> str:
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text

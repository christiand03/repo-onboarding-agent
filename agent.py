import os

from dotenv import load_dotenv
import google.generativeai as genai

#load .env file
load_dotenv()

# Config Gemini API
# get API-Key from .env file
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    # if Key not found.
    raise ValueError("GOOGLE_API_KEY is not found in .env-file! Please create a .env-file with the key.")
genai.configure(api_key=GEMINI_API_KEY)
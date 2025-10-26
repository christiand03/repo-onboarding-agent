import logging
import os
# import sys
# from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langfuse import Langfuse

load_dotenv()
app = FastAPI()

allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
langfuse = Langfuse(
    public_key=os.getenv('LANGFUSE_PUBLIC_KEY'),
    secret_key=os.getenv('LANGFUSE_SECRET_KEY'),
    host=os.getenv('LANGFUSE_HOST'),
)

# Beispiel, wie man mit fastAPI Endpunkte für ein Programm setzen kann
# @app.post("/prompt")
# def register_prompt(Objekt : Klasse):
#     return method(prompt)
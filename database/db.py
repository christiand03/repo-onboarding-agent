from pymongo import MongoClient
from dotenv import load_dotenv  
import streamlit_authenticator as stauth

import os

load_dotenv()

MONGO_KEY = os.getenv("MONGO_KEY")
client=MongoClient(MONGO_KEY)

dbusers = client.AI4AA.users

def insert_user(username: str, name: str,  password: str):
    # Insert a new user into the database
    user = {"_id": username,"name":name, "hashed_password": stauth.hasher.hash(password), "gemini_api_key": "", "ollama_base_url": ""}
    result = dbusers.insert_one(user)
    return result.inserted_id


def fetch_all_users():
    # Fetch all users from the database
    users = list(dbusers.find())
    return users

def fetch_user(username: str):
    # Fetch a single user by username
    user = dbusers.find_one({"_id": username})
    return user

def update_gemini_key(username: str, gemini_api_key: str ):
    # Update the Gemini API key for a user
    result = dbusers.update_one({"_id": username}, {"$set": {"gemini_api_key": gemini_api_key}})
    return result.modified_count

def update_ollama_url(username: str, ollama_base_url: str ):
    # Update the Ollama Base URL for a user
    result = dbusers.update_one({"_id": username}, {"$set": {"ollama_base_url": ollama_base_url}})
    return result.modified_count

def fetch_gemini_key(username: str):
    # Fetch the Gemini API key for a user
    user = dbusers.find_one({"_id": username}, {"gemini_api_key": 1, "_id": 0})
    return user.get("gemini_api_key")

def fetch_ollama_url(username: str):
    # Fetch the Ollama Base URL for a user
    user = dbusers.find_one({"_id": username}, {"ollama_base_url": 1, "_id": 0})
    return user.get("ollama_base_url")

def delete_user(username: str):
    # Delete a user from the database
    result = dbusers.delete_one({"_id": username})
    return result.deleted_count


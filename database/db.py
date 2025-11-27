from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv  
import streamlit_authenticator as stauth
from cryptography.fernet import Fernet

import os

if "MONGO_KEY" in st.secrets and "ENCRYPTION_KEY" in st.secrets:
    MONGO_KEY = st.secrets["MONGO_KEY"]
    ENCRYPTION_KEY = st.secrets["ENCRYPTION_KEY"]
else:
    load_dotenv()
    MONGO_KEY = os.getenv("MONGO_KEY")
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

if not MONGO_KEY or not ENCRYPTION_KEY:
    raise ValueError("Database configuration is missing! Check Secrets or .env")

client=MongoClient(MONGO_KEY)

if ENCRYPTION_KEY:
    cipher_suite = Fernet(ENCRYPTION_KEY)
else:
    # Fallback, falls Key vergessen wurde (nur Warnung, aber wichtig)
    print("ACHTUNG: ENCRYPTION_KEY fehlt in .env! Verschlüsselung deaktiviert.")
    cipher_suite = None

# --- Helper Functions ---
def encrypt_text(text: str) -> str:
    if not text or not cipher_suite: return text
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt_text(text: str) -> str:
    if not text or not cipher_suite: return text
    try:
        return cipher_suite.decrypt(text.encode()).decode()
    except Exception:
        
        return text


# --- users ---
dbusers = client.AI4AA.users

def insert_user(username: str, name: str,  password: str):
    # Insert a new user into the database
    user = {
            "_id": username,
            "name":name, "hashed_password": stauth.hasher.hash(password),
            "gemini_api_key": "", 
            "ollama_base_url": ""
    }
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
    encrypted_key = encrypt_text(gemini_api_key)
    result = dbusers.update_one({"_id": username}, {"$set": {"gemini_api_key": encrypted_key}})
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

def get_decrypted_api_keys(username: str):
    """Holt User und entschlüsselt die Keys direkt"""
    user = dbusers.find_one({"_id": username})
    if not user: return None, None
    
    gemini_plain = decrypt_text(user.get("gemini_api_key", ""))
    ollama_plain = user.get("ollama_base_url", "")
    return gemini_plain, ollama_plain


# --- exchanges ---
dbexchanges = client.AI4AA.exchanges

def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str="", main_used: str="", total_time: str="", helper_time: str="", main_time: str=""):
    # Insert a new exchange into the database
    exchange = {
        "question": question,
        "answer": answer,
        "feedback": feedback,
        "feedback_message": "",
        "chat_name": chat_name,
        "username": username,
        "helper_used": helper_used,
        "main_used": main_used,
        "total_time": total_time,
        "helper_time": helper_time,
        "main_time": main_time,
        "created_at":  datetime.now()
    }
    result = dbexchanges.insert_one(exchange)
    return result.inserted_id

def fetch_exchanges_by_user(username: str):
    exchanges = list(dbexchanges.find({"username": username}))
    return exchanges

def fetch_exchanges_by_chat(username: str, chat_name: str):
    exchanges = list(dbexchanges.find({"username": username, "chat_name": chat_name}))
    return exchanges

def update_exchange_feedback(exchange_id, feedback: int):
    # Update the feedback for a specific exchange
    result = dbexchanges.update_one({"_id": exchange_id}, {"$set": {"feedback": feedback}})
    return result.modified_count

def update_exchange_feedback_message(exchange_id, feedback_message: str):
    # Update the feedback message for a specific exchange
    result = dbexchanges.update_one({"_id": exchange_id}, {"$set": {"feedback_message": feedback_message}})
    return result.modified_count

def delete_chats_by_user(username: str, chat_name: str):
    # Delete all exchanges for a specific user and chat
    result = dbexchanges.delete_many({"username": username, "chat_name": chat_name})
    return result.deleted_count

def delete_exchange_by_id(exchange_id: str):
    # Delete a specific exchange by its ID
    result = dbexchanges.delete_one({"_id": exchange_id})
    return result.deleted_count

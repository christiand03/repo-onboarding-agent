from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import streamlit_authenticator as stauth
from cryptography.fernet import Fernet

import uuid
import os


load_dotenv()
MONGO_KEY = os.getenv("MONGO_KEY")
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

if not MONGO_KEY or not ENCRYPTION_KEY:
    raise ValueError("Database configuration is missing! Check Secrets or .env")

client = MongoClient(MONGO_KEY)

if ENCRYPTION_KEY:
    cipher_suite = Fernet(ENCRYPTION_KEY)
else:
    print("ACHTUNG: ENCRYPTION_KEY fehlt in .env! Verschlüsselung deaktiviert.")
    cipher_suite = None

# --- Helper Functions ---

def encrypt_text(text: str) -> str:
    if not text or not cipher_suite: return text
    return cipher_suite.encrypt(text.strip().encode()).decode()

def decrypt_text(text: str) -> str:
    if not text or not cipher_suite: return text
    try:
        return cipher_suite.decrypt(text.strip().encode()).decode()
    except Exception:
        return text

# --- users ---

dbusers = client.AI4AA.users

def insert_user(username: str, name: str, password: str):
    user = {
        "_id": username,
        "name": name, 
        "hashed_password": stauth.Hasher.hash(password),
        "gemini_api_key": "",
        "ollama_base_url": "",
        "gpt_api_key": ""
    }
    result = dbusers.insert_one(user)
    return result.inserted_id

def fetch_all_users():
    return list(dbusers.find())

def fetch_user(username: str):
    return dbusers.find_one({"_id": username})

def update_user_name(username: str, new_name: str):
    # Achtung: _id kann in Mongo nicht einfach so geändert werden. 
    # Hier wird nur das Name-Feld geupdated.
    result = dbusers.update_one({"_id": username}, {"$set": {"name": new_name}})
    return result.modified_count

def update_gemini_key(username: str, gemini_api_key: str):
    encrypted_key = encrypt_text(gemini_api_key.strip())
    result = dbusers.update_one({"_id": username}, {"$set": {"gemini_api_key": encrypted_key}})
    return result.modified_count

def update_gpt_key(username: str, gpt_api_key: str):
    encrypted_key = encrypt_text(gpt_api_key.strip())
    result = dbusers.update_one({"_id": username}, {"$set": {"gpt_api_key": encrypted_key}})
    return result.modified_count

def update_ollama_url(username: str, ollama_base_url: str):
    result = dbusers.update_one({"_id": username}, {"$set": {"ollama_base_url": ollama_base_url.strip()}})
    return result.modified_count

def fetch_gemini_key(username: str):
    user = dbusers.find_one({"_id": username}, {"gemini_api_key": 1, "_id": 0})
    return user.get("gemini_api_key") if user else None

def fetch_ollama_url(username: str):
    user = dbusers.find_one({"_id": username}, {"ollama_base_url": 1, "_id": 0})
    return user.get("ollama_base_url") if user else None

def delete_user(username: str):
    return dbusers.delete_one({"_id": username}).deleted_count

def get_decrypted_api_keys(username: str):
    user = dbusers.find_one({"_id": username})
    if not user: return None, None
    gemini_plain = decrypt_text(user.get("gemini_api_key", ""))
    ollama_plain = user.get("ollama_base_url", "")
    gpt_plain = decrypt_text(user.get("gpt_api_key", ""))
    return gemini_plain, ollama_plain, gpt_plain

# --- chats ---

dbchats = client.AI4AA.chats

def insert_chat(username: str, chat_name: str):
    """Erstellt einen neuen Chat-Eintrag."""
    chat = {
        "_id": str(uuid.uuid4()),
        "username": username,
        "chat_name": chat_name,
        "created_at": datetime.now()
    }
    result = dbchats.insert_one(chat)
    return result.inserted_id

def fetch_chats_by_user(username: str):
    """Holt alle definierten Chats eines Users."""
    # Sortieren nach Erstellung macht Sinn
    chats = list(dbchats.find({"username": username}).sort("created_at", 1))
    return chats

def check_chat_exists(username: str, chat_name: str):
    return dbchats.find_one({"username": username, "chat_name": chat_name}) is not None


def rename_chat_fully(username: str, old_name: str, new_name: str):
    """
    Benennt einen Chat und alle zugehörigen Exchanges um.
    """
    # 1. Chat-Eintrag umbenennen
    result = dbchats.update_one(
        {"username": username, "chat_name": old_name}, 
        {"$set": {"chat_name": new_name}}
    )
    
    # 2. Alle Messages (Exchanges) umhängen
    dbexchanges.update_many(
        {"username": username, "chat_name": old_name},
        {"$set": {"chat_name": new_name}}
    )
    return result.modified_count

# --- exchanges ---

dbexchanges = client.AI4AA.exchanges

def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, 
                    helper_used: str="", main_used: str="", total_time: str="", helper_time: str="", main_time: str="",
                    json_tokens=0, toon_tokens=0, savings_percent=0.0):
    new_id = str(uuid.uuid4())
    exchange = {
        "_id": new_id,
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
        "json_tokens": json_tokens,
        "toon_tokens": toon_tokens,
        "savings_percent": savings_percent,
        "created_at": datetime.now()
    }
    try:
        dbexchanges.insert_one(exchange)
        return new_id
    except Exception as e:
        print(f"DB Error: {e}")
        return None

def fetch_exchanges_by_user(username: str):
    # Sortieren nach Zeitstempel wichtig für die Anzeige
    exchanges = list(dbexchanges.find({"username": username}).sort("created_at", 1))
    return exchanges

def fetch_exchanges_by_chat(username: str, chat_name: str):
    exchanges = list(dbexchanges.find({"username": username, "chat_name": chat_name}).sort("created_at", 1))
    return exchanges

def update_exchange_feedback(exchange_id, feedback: int):
    result = dbexchanges.update_one({"_id": exchange_id}, {"$set": {"feedback": feedback}})
    return result.modified_count

def update_exchange_feedback_message(exchange_id, feedback_message: str):
    result = dbexchanges.update_one({"_id": exchange_id}, {"$set": {"feedback_message": feedback_message}})
    return result.modified_count

def delete_exchange_by_id(exchange_id: str):
    result = dbexchanges.delete_one({"_id": exchange_id})
    return result.deleted_count

# --- CONSISTENT DELETE FUNCTIONS ---

def delete_full_chat(username: str, chat_name: str):
    """
    Löscht den Chat UND alle zugehörigen Exchanges.
    Das sorgt für Konsistenz zwischen Frontend und Backend.
    """
    # 1. Alle Nachrichten in diesem Chat löschen
    del_exchanges = dbexchanges.delete_many({"username": username, "chat_name": chat_name})
    
    # 2. Den Chat selbst aus der Chat-Liste löschen
    del_chat = dbchats.delete_one({"username": username, "chat_name": chat_name})
    
    return del_chat.deleted_count
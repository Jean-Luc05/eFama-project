# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = FastAPI()

# --- CORS Middleware Setup ---
# This allows your frontend (running on a different port) to talk to this backend
origins = [
    "http://localhost:5173", # Default Vue.js dev server port
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Supabase Client Setup ---
# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
# supabase: Client = create_client(url, key)

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the eFama-project API! 🚀"}

@app.get("/api/v1/test")
def test_endpoint():
    # Example of how you might fetch data from Supabase
    # response = supabase.table('your_table_name').select("*").execute()
    return {"data": "This is a test endpoint"}
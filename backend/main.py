# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = FastAPI()

# --- CORS Middleware Setup ---
# This allows your frontend (running on a different port) to talk to this backend
origins = [
    "http://localhost:3000",   # <-- UPDATE THIS for Nuxt.js
    "http://127.0.0.1:3000",  # <-- UPDATE THIS for Nuxt.js
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include the Auth Router from routers/auth.py ---
app.include_router(auth.router)

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome!"}
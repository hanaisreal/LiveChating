from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from pydantic import BaseModel

app = FastAPI()

# Allow CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for messages
chat_messages: List[Dict[str, str]] = []

# Message model
class Message(BaseModel):
    role: str
    content: str

@app.post("/messages/send")
def send_message(message: Message):
    chat_messages.append(message.dict())
    return {"status": "Message sent"}

@app.get("/messages/fetch")
def fetch_messages():
    return chat_messages

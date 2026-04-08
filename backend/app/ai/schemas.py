from pydantic import BaseModel          # ← AJOUTER cette ligne
from typing import List

class ChatMessage(BaseModel):
    role: str       # "user" ou "assistant"
    content: str

class ChatRequest(BaseModel):
    message: str
    history: List[ChatMessage] = []

class ChatResponse(BaseModel):
    response: str

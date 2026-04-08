import anthropic
import os
from app.config import settings
from fastapi import HTTPException

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """You are Velura's personal AI stylist. 
Velura is a luxury fashion rental service in Morocco.
You help users choose outfits from our catalog: dresses, blazers, and luxury pieces.
Be elegant, concise, and fashion-forward in your responses.
Always suggest items that could be rented from Velura's catalog."""

def get_ai_response(user_message: str, conversation_history: list) -> str:
    if not settings.ANTHROPIC_API_KEY:                     # ← AJOUTER
        raise HTTPException(status_code=503, detail="AI service non configuré")
    
    VALID_ROLES = {"user", "assistant"}
    clean_history = [m for m in conversation_history if m.get("role") in VALID_ROLES]
    messages = clean_history + [{"role": "user", "content": user_message}]

    try:                                                   # ← AJOUTER
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",                     # ← voir note ci-dessous
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=messages
        )
        return response.content[0].text
    except Exception as e:
        print(f"AI ERROR: {str(e)}")                                  # ← AJOUTER
        raise HTTPException(status_code=503, detail=f"Erreur AI : {str(e)}")
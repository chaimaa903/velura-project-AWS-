from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from app.ai.service import get_ai_response
from app.auth.service import get_current_user
from app.users.models import User
from app.ai.schemas import ChatMessage, ChatRequest, ChatResponse

router = APIRouter(prefix="/ai", tags=["ai"])


# POST /api/ai/chat
# → ai-stylist/page.tsx envoie le message ici
@router.post("/chat", response_model=ChatResponse)
def chat_with_stylist(
    data: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    history = [{"role": m.role, "content": m.content} for m in data.history]
    response = get_ai_response(data.message, history)
    return {"response": response}
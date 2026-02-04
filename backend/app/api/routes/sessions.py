from __future__ import annotations
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.schemas.session import CookingSession, SessionView

router = APIRouter()

class CreateSessionRequest(BaseModel):
    recipe_id: str = Field(..., min_length=1)

@router.post("", response_model= CookingSession)
def create_session(req: CreateSessionRequest):
    from app.state import RECIPE_STORE, SESSION_STORE, new_id, now_iso

    if req.recipe_id not in RECIPE_STORE:
        raise HTTPException(status_code= 404, detail="recipe_id not found")
    
    session_id = new_id("ses")
    session = CookingSession(
        session_id=session_id,
        recipe_id=req.recipe_id,
        current_step_index=0,
        status="NOT_STARTED",
        created_at=now_iso(),
        updated_at=now_iso(),
    )

    SESSION_STORE[session_id]=session

    return session

@router.get("/{session_id}", response_model=SessionView)
def get_session(session_id: str):
    from app.state import RECIPE_STORE, SESSION_STORE

    session = SESSION_STORE(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="session not found")
    
    recipe = RECIPE_STORE.get(session.recipe_id)
    if not recipe:
        raise HTTPException(status_code=500, detail="recipe missing for session")
    

    idx = min(session.current_step_index, len(recipe.steps)-1)
    instruction = recipe.steps[idx].instruction

    return SessionView(
        session=session,
        current_step_instruction= instruction,
        total_steps=len(recipe.steps),
    )
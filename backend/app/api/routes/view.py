from __future__ import annotations
from fastapi import APIRouter, HTTPException

from app.schemas.cook_mode import CookModeView
from app.services.cook_mode.builder import build_cook_mode_view

router = APIRouter()

@router.get("/{session_id}/view", response_model=CookModeView)
def get_session_view(session_id: str):
    from app.state import SESSION_STORE, RECIPE_STORE, TIMER_STORE

    session = SESSION_STORE.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="session not found")
    
    recipe = RECIPE_STORE.get(session.recipe_id)
    if not recipe:
        return HTTPException(status_code=500, detail=" recipe missing for session")
    
    timers = [t for t in TIMER_STORE.values() if t.session_id == session_id]
    return build_cook_mode_view(session=session, recipe= recipe, timers=timers)
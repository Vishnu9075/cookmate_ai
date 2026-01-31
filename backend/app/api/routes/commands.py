from __future__ import annotations
from fastapi import APIRouter, HTTPException

from app.schemas.commands import SessionCommand
from app.schemas.session import SessionView
from app.services.session_engine.engine import apply_command

router = APIRouter()


@router.post("/{session_id}/command", response_model=SessionView)
def command_session(session_id: str, cmd: SessionCommand):
    from app.main import RECIPE_STORE, SESSION_STORE

    session = SESSION_STORE.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="session not found")
    
    recipe = RECIPE_STORE.get(session.recipe_id)
    if not recipe:
        raise HTTPException(status_code=500, detail="recipe missing for session")
    

    out = apply_command(session=session, recipe=recipe ,cmd = cmd)
    SESSION_STORE[session_id] = out.session

    idx = min(out.session.current_step_index, len(recipe.steps)-1)
    instruction = recipe.steps[idx].instruction

    return SessionView(
        session=out.session,
        current_step_instruction=instruction,
        total_steps=len(recipe.steps),
    )
from __future__ import annotations
from fastapi import APIRouter, HTTPException

from app.schemas.commands import SessionCommand
from app.schemas.session import SessionView
from app.services.session_engine.engine import apply_command
from app.services.timers.step_timer import maybe_start_timer_for_step

router = APIRouter()

@router.post("/{session_id}/command", response_model=SessionView)
def command_session(session_id: str, cmd: SessionCommand):
    from app.state import RECIPE_STORE, SESSION_STORE, TIMER_STORE, new_id

    session = SESSION_STORE.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="session not found")

    recipe = RECIPE_STORE.get(session.recipe_id)
    if not recipe:
        raise HTTPException(status_code=500, detail="recipe missing for session")

    out = apply_command(session=session, recipe=recipe, cmd=cmd)
    SESSION_STORE[session_id] = out.session

    # current step
    idx = min(out.session.current_step_index, len(recipe.steps) - 1)
    step = recipe.steps[idx]

    # AUTO start step timer (if step has duration or parsable duration)
    maybe_start_timer_for_step(
        session_id=session_id,
        step_index=idx,
        step=step,
        timer_store=TIMER_STORE,
        new_id_func=new_id,
    )

    # return timers for this session
    timers = [t for t in TIMER_STORE.values() if t.session_id == session_id]

    return SessionView(
        session=out.session,
        current_step_instruction=step.instruction,
        total_steps=len(recipe.steps),
        timers=timers,
    )

from __future__ import annotations
from fastapi import APIRouter, HTTPException
from app.schemas.timer import StartTimerRequest, CancelTimerRequest, Timer
from app.services.timers.service import start_timer
from app.state import SESSION_STORE, TIMER_STORE, new_id


router = APIRouter()

@router.get("/{session_id}/timers", response_model= list[Timer])
def list_timers(session_id:str):
	from app.state import SESSION_STORE, TIMER_STORE
	if session_id not in SESSION_STORE:
		raise HTTPException(status_code=404, detail="session not found")
	
	return [t for t in TIMER_STORE.values() if t.session_id == session_id]


@router.post("/{session_id}/timers/start", response_model = Timer)
def start_session_timer(session_id:str, req: StartTimerRequest):
	if session_id not in SESSION_STORE:
		raise HTTPException(status_code=404, detail="session not found")
	
	label = req.label or f"{req.seconds}s timer"
	t = start_timer(session_id=session_id, seconds=req.seconds, label=label, new_id_func= new_id)
	TIMER_STORE[t.timer_id] = t
	return t

@router.post("/{session_id}/timers/cancel", response_model=Timer)
def cancel_timer(session_id: str, req: CancelTimerRequest):
    from app.state import SESSION_STORE, TIMER_STORE

    if session_id not in SESSION_STORE:
        raise HTTPException(status_code=404, detail="session not found")

    t = TIMER_STORE.get(req.timer_id)
    if (t is None) or (t.session_id != session_id):
        raise HTTPException(status_code=404, detail="timer not found")

    tt = t.model_copy(deep=True)
    tt.status = "CANCELED"
    TIMER_STORE[req.timer_id] = tt
    return tt

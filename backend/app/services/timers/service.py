from __future__ import annotations
from datetime import datetime, timezone, timedelta
from app.schemas.timer import Timer

def now_utc():
    return datetime.now(timezone.utc)

def iso(dt: datetime) -> str:
    return dt.isoformat()

def start_timer(session_id:str, seconds: int, label:str, new_id_func) -> Timer:
    start = now_utc()
    end = start + timedelta(seconds=seconds)
    return Timer(
        timer_id=new_id_func("tmr"),
        session_id= session_id,
        label= label or "Timer",
        duration_seconds=seconds,
        started_at=iso(start),
        ends_at= iso(end),
        status="RUNNING",
    )

def mark_done_if_expired(timer: Timer) -> Timer:
    if timer.status != "RUNNING":
        return timer
    
    now = now_utc()
    ends = datetime.fromisoformat(timer.ends_at)
    if now>= ends:
        t = timer.model_copy(deep=True)
        t.status = "DONE"
        return t
    return timer

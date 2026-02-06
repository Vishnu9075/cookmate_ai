from __future__ import annotations

from app.db.models import SessionRow, TimerRow
from app.schemas.session import CookingSession
from app.schemas.timer import Timer


def session_to_row(s: CookingSession) -> SessionRow:
    return SessionRow(
        session_id= s.session_id,
        recipe_id= s.recipe_id,
        current_step_index=s.current_step_index,
        status=s.status,
        created_at=s.created_at,
        updated_at=s.updated_at,
    )

def row_to_session(r: SessionRow) -> CookingSession:
    return CookingSession(
        session_id=r.session_id,
        recipe_id=r.recipe_id,
        current_step_index=r.current_step_index,
        status=r.status,
        created_at=r.created_at,
        updated_at=r.updated_at,
    )

def timer_to_timer(t:Timer) -> TimerRow:
    return TimerRow(
        timer_id=t.timer_id,
        session_id=t.session_id,
        label=t.label,
        duration_seconds=t.duration_seconds,
        started_at=t.started_at,
        ends_at=t.ends_at,
        status=t.status,
        paused_at=getattr(t, "paused_at", None),
        remaining_seconds= getattr(t, "remaining_seconds", None),
    )

def row_to_timer(r: TimerRow) -> Timer:
    return Timer(
        timer_id=r.timer_id,
        session_id=r.session_id,
        label=r.label,
        duration_seconds=r.duration_seconds,
        started_at=r.started_at,
        ends_at=r.ends_at,
        status=r.status,
        paused_at=r.paused_at,
        remaining_seconds=r.remaining_seconds,
    )
from __future__ import annotations
from datetime import datetime, timezone, timedelta
from typing import Optional

from app.schemas.timer import Timer

def now_utc() -> datetime:
    return datetime.now(timezone.utc)

def iso(dt: datetime) -> str:
    return dt.isoformat()

def parse_iso(s: str) -> datetime:
    return datetime.fromisoformat(s)


def remaining_seconds(timer: Timer) -> int:
    #prefer stored ramaining seconds if present
    if timer.remaining_seconds is not None:
        return max(0, int(timer.remaining_seconds))
    
    end = parse_iso(timer.ends_at)
    return max(0, int((end-now_utc()).total_seconds()))


def pause_timer(timer: Timer) -> Timer:
    if timer.status != "RUNNING":
        return timer
    
    t= timer.model_copy(deep=True)
    t.remaining_seconds = remaining_seconds(timer)
    t.paused_at = iso(now_utc())
    t.status = "PAUSED"
    return t

def resume_timer(timer: Timer) -> Timer:
    if timer.status != "PAUSED":
        return timer
    
    rem = remaining_seconds(timer)
    start = now_utc()
    end = start + timedelta(seconds=rem)

    t = timer.model_copy(deep=True)
    t.started_at = iso(start)
    t.ends_at = iso(end)
    t.paused_at = None
    t.remaining_seconds = None
    t.status = "RUNNING"
    return t
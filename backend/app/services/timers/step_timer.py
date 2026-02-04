from __future__ import annotations
from typing import Optional

from app.schemas.recipie_spec import Step
from app.schemas.timer import Timer
from app.services.timers.service import start_timer
from app.services.steps.duration_parser import parse_duration_seconds

def _step_timer_label(step_index: int) -> str:
    return f"Step {step_index + 1} timer"

def maybe_start_timer_for_step(*,session_id: str, step_index: str,step:Step, timer_store: dict, new_id_func,) -> Optional[Timer]:
    """
    Starts a timer if:
    - step.duration_seconds is set, OR
    - duration can be parsed from step.instruction

    Idempotent-ish:
    - If there is already a RUNNING timer for this step label in this session, do nothing.
    """

    label = _step_timer_label(step_index)

    # If a timer is already running for this step, don't start another

    for t in timer_store.values():
        if t.session_id == session_id and t.label == label and t.status == "RUNNING":
            return None
        
    seconds = step.duration_seconds
    if seconds is None:
        seconds = parse_duration_seconds(step.instruction)

    if not seconds or seconds <=0:
        return None
    
    timer = start_timer(session_id=session_id,
                        seconds=int(seconds),
                        label=label,
                        new_id_func=new_id_func,
                        )
    
    timer_store[timer.timer_id] = timer
    return timer
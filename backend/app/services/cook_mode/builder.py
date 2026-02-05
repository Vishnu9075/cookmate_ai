from __future__ import annotations

from app.schemas.cook_mode import CookModeView
from app.schemas.recipie_spec import RecipeSpec
from app.schemas.session import CookingSession
from app.schemas.timer import Timer


def _phase_from_status(status: str) -> str:
    # map your session.status into cook-mode phases
    if status == "IDLE":
        return "IDLE"
    if status == "PAUSED":
        return "PAUSED"
    if status == ("DONE", "FINISHED"):
        return "DONE"
    if status in ("COOKING",):
        return "COOKING"
    return "IDLE"

def _make_speak_text(step_index: int, total_steps: int, instruction: str, active_timers: list[Timer]) -> str:
    base = f"{step_index + 1} of {total_steps}. {instruction}"

    if not active_timers:
        return base
    
    t= active_timers[0]
    return f"{base}. Timer running :{t.label} for {t.duration_seconds} seconds."


def build_cook_mode_view(
        *, 
        session: CookingSession,
        recipe: RecipeSpec,
        timers: list[Timer],) -> CookModeView:
    
    total = len(recipe.steps)
    idx = min(max(session.current_step_index,0), max(total-1, 0))
    step = recipe.steps[idx]

    current_label = f"Step {idx + 1} timer"
    active = [t for t in timers if t.status == "RUNNING"]
    active_for_step = [t for t in active if t.label == current_label]


    return CookModeView(
        session=session,
        phase= _phase_from_status(session.status),
        step_index=idx,
        total_steps= total,
        current_step_instruction= step.instruction,
        speak_text= _make_speak_text(idx, total, step.instruction, active_for_step),
        timers= timers,
        active_timers=active
    )
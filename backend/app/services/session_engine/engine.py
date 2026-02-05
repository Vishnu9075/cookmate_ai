from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone

from app.schemas.session import CookingSession
from app.schemas.recipie_spec import RecipeSpec
from app.schemas.commands import SessionCommand
from app.schemas.commands import CommandResult



def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class EngineOutput:
    session: CookingSession
    result: CommandResult


def apply_command(session: CookingSession, recipe: RecipeSpec, cmd: SessionCommand) -> EngineOutput:
    total = len(recipe.steps)
    if total <= 0:
        # Should never happen due to schema min_length=1
        return EngineOutput(session=session, result=CommandResult(message="Recipe has no steps."))
    
    s= session.model_copy(deep=True)
    s.updated_at = _now_iso()

    if cmd.type == "START":
        s.status == "COOKING"
        s.current_step_index = 0
        step = recipe.steps[s.current_step_index].instruction
        return EngineOutput(
            session=s,
            result = CommandResult(message= "session started", speak=f"step 1. {step}")
        )
    
    if s.status == "NOT_STARTED":
        #force a sane ux
        s.status = "COOKING"

    if cmd.type == "NEXT_STEP":
        if s.current_step_index + 1 >= total:
            s.status = "FINISHED"
            return EngineOutput(session=s, result= CommandResult(message="Recipe finished.", speak="You are done."))
        s.current_step_index +=1
        step = recipe.steps[s.current_step_index].instruction
        return EngineOutput(session=s, result=CommandResult(message="Moved to next step.", speak=step))
    
    if cmd.type == "PREV_STEP":
        if s.current_step_index == 0:
            step = recipe.steps[0].instruction
            return EngineOutput(session=s, result=CommandResult(message="Already at first step.", speak=step))
        s.current_step_index -= 1
        step = recipe.steps[s.current_step_index].instruction
        return EngineOutput(session=s, result=CommandResult(message="Moved to previous step.", speak = step))
    
    if cmd.type == "PAUSE":
        s = session.model_copy(deep=True)
        s.status = "PAUSED"
        s.updated_at = _now_iso()
        return EngineOutput(session=s, result="PAUSED")

    if cmd.type == "RESUME":
        s = session.model_copy(deep=True)
        s.status = "COOKING"
        s.updated_at = _now_iso()
        return EngineOutput(session=s, result="RESUMED")


    if cmd.type == "REPEAT_STEP":
        step = recipe.steps[s.current_step_index].instruction
        return EngineOutput(session=s, result = CommandResult(message="Repeated current step.", speak=step))
    
    if cmd.type == "GO_TO_STEP":
        if cmd.step_index is None:
            return EngineOutput(session=s, result=CommandResult(message="step_index is required."))
        
        if cmd.step_index >= total:
            return EngineOutput(session=s, result= CommandResult(message=f"step_index out of range (0..{total-1})."))
        
        s.current_step_index = cmd.step_index
        step = recipe.steps[s.current_step_index].instruction
        return EngineOutput(session=s, result= CommandResult(message="Jumped to step.", speak=step))
    
    return EngineOutput(session=s, result=CommandResult(message=f"Unsupported command: {cmd.type}"))

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

from app.schemas.session import CookingSession
from app.schemas.timer import Timer


CookModePhase = Literal["IDLE","COOKING","PAUSED","DONE"]

class CookModeView(BaseModel):
    model_config = ConfigDict( extra="forbid")

    #core state

    session: CookingSession
    phase: CookModePhase

    #what to show
    step_index: int
    total_steps: int
    current_step_instruction: str

    #voice output
    speak_text: str

    #timers(full + active convenience)
    timers: list[Timer] = Field(default_factory=list)
    active_timers: list[Timer] = Field(default_factory=list)
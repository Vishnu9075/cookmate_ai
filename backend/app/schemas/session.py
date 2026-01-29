from __future__ import annotations
from typing import Literal, Optional
from pydantic import BaseModel, Field, ConfigDict


SessionStatus = Literal["NOT_STARTED", "COOKING", "PAUSED","FINISHED"]

class CookingSession(BaseModel):
    model_config = ConfigDict(extra="forbid")
    session_id : str
    recipe_id : str
    current_step_index: int = Field(default=0, ge=0)
    status: SessionStatus= "NOT_STARTED"
    created_at:str
    updated_at: str


class SessionView(BaseModel):
    model_config = ConfigDict(extra = "forbid")
    session: CookingSession
    current_step_instruction:str
    total_steps:int
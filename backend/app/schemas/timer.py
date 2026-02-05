from __future__ import annotations
from typing import Literal, Optional
from pydantic import BaseModel, Field, ConfigDict


TimerStatus = Literal["RUNNING", "DONE", "CANCELED"]

class Timer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    timer_id:str
    session_id: str
    label: str = Field(default="True")
    duration_seconds: int = Field(..., ge=1)
    started_at: str
    ends_at: str
    status: TimerStatus = "RUNNING"
    paused_at: Optional[str] = None
    remaining_seconds: Optional[int] = None

class StartTimerRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    seconds: int = Field(..., ge=1)
    label: Optional[str] = None

class CancelTimerRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    timer_id: str
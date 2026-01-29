from __future__ import annotations
from typing import Literal, Optional
from pydantic import BaseModel, Field, ConfigDict


CommandType = Literal["START", "NEXT_STEP", "PREV_STEP","REPEAT_STEP","GO_TO_STEP",]


class SessionCommand(BaseModel):
    """
    request_id enables idempotency later. For MVP we keep it but do not persist.
    """
    model_config = ConfigDict(extra="forbid")
    type: CommandType
    request_id: Optional[str] = None
    step_index : Optional[int] = Field(default=None, ge= 0)


class CommandResult(BaseModel):
    model_config = ConfigDict(extra="forbid")
    message: str
    speak:Optional[str] = None
    
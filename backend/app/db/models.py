from __future__ import annotations
from typing import Optional
from sqlmodel import SQLModel, Field


class RecipeRow(SQLModel, table= True):
    recipe_id: str = Field(primary_key=True)
    raw_text: str

class SessionRow(SQLModel, Table= True):
    session_id: str = Field(primary_key= True)
    recipe_id: str = Field(index= True)
    current_step_index: int
    status: str
    created_at: str
    updated_at: str

class TimerRow(SQLModel, table=True):
    timer_id: str = Field(primary_key=True)
    session_id: str = Field(index=True)
    label: str
    duration_seconds:int
    ends_at: str
    started_at:str
    status: str

    paused_at: Optional[str] = None
    remaining_seconds : Optional[int] = None
from __future__ import annotations
from typing import Optional, List
from sqlmodel import Session, select

from app.db.models import RecipeRow, SessionRow, TimerRow

#--recipes--

def save_recipe(db: Session, recipe_id: str, raw_text:str) -> str:
    db.add(RecipeRow(recipe_id=recipe_id, raw_text=raw_text))
    db.commit()

def get_recipe(db: Session, recipe_id: str) -> Optional[RecipeRow]:
    return db.get(RecipeRow, recipe_id)


#-- sessions --

def save_session(db: Session, row: SessionRow) -> None:
    db.add(row)
    db.commit()

def get_session(db:Session, session_id: str) -> Optional[SessionRow]:
    return db.get(SessionRow, session_id)

def update_session(db: Session, row: SessionRow) ->None:
    db.add(row)
    db.commit()

# ---- Timers ----

def upsert_timer(db: Session, row: TimerRow) -> None:
    db.add(row)
    db.commit() 

def get_timer(db:Session, timer_id: str) ->Optional[TimerRow]:
    return db.get(TimerRow, timer_id)

def list_timers(db:Session, session_id : str) -> List[TimerRow]:
    stmt = select(TimerRow).where(TimerRow.session_id == session_id)
    return list(db.exec(stmt).all())
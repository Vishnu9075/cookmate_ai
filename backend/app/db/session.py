from __future__ import annotations

from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

engine = create_engine(settings.database_url, echo= False)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as db:
        yield db


from __future__ import annotations
from datetime import datetime, timezone
from typing import Dict

from app.schemas.recipie_spec import RecipeSpec
from app.schemas.session import CookingSession
from app.schemas.timer import Timer

RECIPE_STORE: Dict[str, RecipeSpec] = {}
SESSION_STORE: Dict[str, CookingSession] = {}
TIMER_STORE: Dict[str, Timer] = {}

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def new_id(prefix: str) -> str:
    t = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
    return f"{prefix}_{t}"

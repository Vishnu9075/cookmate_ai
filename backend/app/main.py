from __future__ import annotations
from datetime import datetime, timezone
from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import api_router
from app.schemas.recipie_spec import RecipeSpec
from app.schemas.session import CookingSession

RECIPE_STORE: Dict[str, RecipeSpec] = {}
SESSION_STORE:Dict[str, CookingSession]={}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def new_id(prefix:str) -> str:
    t = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
    return f"{prefix}_{t}"

app = FastAPI(title="Cookmate MVP API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_allow_origins.split(",") if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api")
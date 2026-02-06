from __future__ import annotations
from datetime import datetime, timezone
from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from contextlib import asynccontextmanager
from app.state import TIMER_STORE

from app.core.config import settings
from app.api.routes import api_router
from app.schemas.recipie_spec import RecipeSpec
from app.schemas.session import CookingSession
from app.schemas.timer import Timer
from app.services.timers.scheduler import timer_scheduler_loop
from app.db.session import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    task = asyncio.create_task(timer_scheduler_loop(TIMER_STORE, interval_seconds=2))
    yield
    # shutdown
    task.cancel()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db
    yield

app = FastAPI(title="Cookmate MVP API")



app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_allow_origins.split(",") if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api")
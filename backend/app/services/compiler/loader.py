from __future__ import annotations
from sqlmodel import Session
from fastapi import HTTPException

from app.db.repo import get_recipe
from app.schemas.recipie_spec import RecipeSpec
from app.services.compiler import compile_recipe


def load_recipe_spec(db:Session, recipe_id: str) -> RecipeSpec:
    row = get_recipe(db, recipe_id)
    if not row:
        raise HTTPException(status_code=404, detail="recipe not found")
    
    # compile from raw_text deterministically
    return compile_recipe(row.raw_text)
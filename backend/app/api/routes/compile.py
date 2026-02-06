from __future__ import annotations
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.compiler.compile_recipe import Compile_recipe_from_text, CompileError
from app.schemas.recipie_spec import RecipeSpec
from app.services.compiler import compile_recipe

router = APIRouter()

class CompileRequest(BaseModel):
    raw_text: str = Field(..., min_length=1)
    source_type: str = "text"
    source_url: str | None = None

class CompilerResponse(BaseModel):
    recipe_id: str
    recipe: RecipeSpec

@router.post("/recipe", response_model= CompilerResponse)
def compile_recipe(req: CompileRequest):
    try:
        recipe = Compile_recipe_from_text(
            req.raw_text,
            source_type= req.source_type,
            source_url=req.source_type,   
        )
    except CompileError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Store is in app.main global for MVP

    from app.state import RECIPE_STORE, new_id

    recipe_id = new_id("rcp")
    RECIPE_STORE[recipe_id] = recipe
    return CompilerResponse(recipe_id= recipe_id, recipe=recipe)
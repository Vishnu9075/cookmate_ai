from __future__ import annotations
from typing import Literal, Optional, List
from pydantic import BaseModel, Field, ConfigDict


class Ingredient(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(..., min_length=1)
    quantity: Optional[float] = None
    unit: Optional[str] = None
    notes: Optional[str] = None


class Step(BaseModel):
    model_config = ConfigDict(extra="forbid")
    index: int = Field(..., ge=0)
    instruction: str = Field(..., min_length=1)
    duration_seconds: Optional[int]= Field(default=None, ge=0)
    temperature: Optional[str]=None
    tools: List[str] = Field(default_factory=list)
    ingredients_used: List[str] = Field(default_factory=list)


class RecipeSource(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Literal["youtube","text"]
    url: Optional[str] = None
    raw_text_id: Optional[str]= None

class RecipeSpec(BaseModel):
    """
    Compiled artifact. This is what your compiler (LLM later) must output.
    Keep this stable.
    """

    model_config = ConfigDict(extra = "forbid")
    title: str = Field(..., min_length=1)
    servings: Optional[str]= None
    ingredients: List[Ingredient] = Field(default_factory=list)
    steps: List[Step] = Field(..., min_length=1)
    warnings: List[str]= Field(default_factory=list)
    source: RecipeSource


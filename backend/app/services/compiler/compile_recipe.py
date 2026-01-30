from __future__ import annotations
from typing import Optional
from app.schemas.recipie_spec import RecipeSource, RecipeSpec, Step


class CompileError(ValueError):
    pass

def Compile_recipe_from_text(raw_text: str,
                             *, 
                             source_type: str= "text", 
                             source_url: Optional[str]= None, 
                             raw_text_id: Optional[str]= None,) -> RecipeSpec:
    """
    MVP compiler: deterministic fallback.
    - Splits text into steps by lines.
    - If text is a paragraph, splits by sentences.
    Replace this with LLM-backed strict JSON generation later.
    """
    cleaned = (raw_text or "").strip()
    if not cleaned:
        raise CompileError("raw text is empty")
    
    # Step extraction heuristic

    lines = [ln.strip() for ln in cleaned.splitlines() if ln.strip()]
    if len(lines) >= 2:
        step_texts = lines
    else:

         # fallback: split by period

        parts = [p.strip() for p in cleaned.split(".") if p.strip()]
        step_text = parts if parts else [cleaned]

    steps = [Step(index=i, instruction=txt) for i , txt in enumerate(step_texts)]

    #very basic title heuristic

    title = "CookMate Recipe"
    if lines and len(lines[0])<=80:
        title = lines[0][:80]


    return RecipeSpec(
        title= title,
        servings=None,
        ingredients=[],
        steps=steps,
        warnings=[],
        source= RecipeSource(type= source_type, url= source_url, raw_text_id=raw_text_id),
    )
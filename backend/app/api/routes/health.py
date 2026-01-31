from fastapi import APIRouter

router = APIRouter()

@router.get(path="/health")
def health():
    return {"ok": True}
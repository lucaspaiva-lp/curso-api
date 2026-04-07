from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
def health():
    return {
        "status": "ok",
        "database": "ok",
        "service": "running"
    }

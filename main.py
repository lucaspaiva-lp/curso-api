from fastapi import FastAPI
from src.api.routes.health import router as health_router
from src.api.routes.aluno import router as aluno_router
from src.api.routes.curso import router as curso_router

app = FastAPI()

app.include_router(health_router)
app.include_router(aluno_router)
app.include_router(curso_router)
from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.aluno import AlunoCreate, AlunoOut
from src.services.aluno_service import AlunoService

router = APIRouter(tags=["alunos"])
service = AlunoService()

@router.post("/alunos", response_model=AlunoOut)
def create_aluno(aluno: AlunoCreate):
    try:
        new_aluno = service.criar_aluno(aluno.nome, aluno.email)
        return new_aluno
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/alunos", response_model=List[AlunoOut])
def list_alunos():
    return service.listar_alunos()
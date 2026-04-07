from fastapi import APIRouter, HTTPException
from src.schemas.curso import CursoCreate, CursoOut, CursoUpdatePreco, CursoDetalhadoOut
from src.services.curso_service import CursoService

router = APIRouter(tags=["cursos"])
service = CursoService()

@router.post("/cursos", response_model=CursoOut)
def criar(curso: CursoCreate):
    try:
        return service.criar_curso(curso.codigo, curso.titulo, curso.preco, curso.tipo, curso.desconto_percentual)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/cursos", response_model=list[CursoOut])
def listar():
    return service.listar_cursos()

@router.get("/cursos/{codigo}", response_model=CursoOut)
def buscar(codigo: int):
    curso = service.buscar_curso(codigo)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@router.get("/cursos/{codigo}/preco-final")
def ver_preco_final(codigo: int):
    curso = service.buscar_curso(codigo)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return {"preco_final": curso.preco_final()}

@router.put("/cursos/{codigo}/preco")
def atualizar_preco(codigo: int, body: CursoUpdatePreco):
    try:
        service.atualizar_preco(codigo, body.novo_preco)
        return {"message": "Preço atualizado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
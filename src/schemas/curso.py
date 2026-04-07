from pydantic import BaseModel
from typing import Optional

class CursoCreate(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: Optional[float] = 0

class CursoUpdatePreco(BaseModel):
    novo_preco: float

class CursoOut(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float
    
class CursoDetalhadoOut(CursoOut):
    preco_final: float
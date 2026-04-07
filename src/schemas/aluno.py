from pydantic import BaseModel, EmailStr

class AlunoCreate(BaseModel):
    nome: str
    email: EmailStr

class AlunoOut(BaseModel):
    id: int
    nome: str
    email: str
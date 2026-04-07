from src.domain.curso import Curso
from src.repositories.curso_repository import CursoRepository

class CursoService:
    def __init__(self):
        self.repository = CursoRepository()

    def criar_curso(self, codigo: int, titulo: str, preco: float, tipo: int, desconto: float = 0) -> Curso:
        if self.repository.existe(codigo):
            raise ValueError("Já existe um curso com este código")
        
        novo_curso = Curso(codigo, titulo, preco, tipo, desconto)
        self.repository.salvar(novo_curso)
        return novo_curso

    def listar_cursos(self):
        return self.repository.listar_todos()

    def buscar_curso(self, codigo: int):
        return self.repository.buscar_por_codigo(codigo)

    def atualizar_preco(self, codigo: int, novo_preco: float):
        curso = self.repository.buscar_por_codigo(codigo)
        if not curso:
            raise ValueError("Curso não encontrado")
        curso.preco = novo_preco
        self.repository.salvar(curso)
        return curso
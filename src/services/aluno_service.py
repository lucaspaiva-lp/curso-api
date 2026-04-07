from src.domain.aluno import Aluno
from src.repositories.aluno_repository import AlunoRepository

class AlunoService:
    def __init__(self):
        self.aluno_repository = AlunoRepository()

    def criar_aluno(self, nome: str, email: str) -> Aluno:
        novo_id = self.aluno_repository.gerar_novo_id()
        
        aluno = Aluno(id=novo_id, nome=nome, email=email)
        
        self.aluno_repository.salvar(aluno)
        return aluno

    def buscar_aluno(self, id: int) -> Aluno | None:
        return self.aluno_repository.buscar_por_id(id)
        
    def listar_alunos(self) -> list[Aluno]:
        return self.aluno_repository.listar_todos()
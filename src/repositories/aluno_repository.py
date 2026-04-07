from src.domain.aluno import Aluno
from src.database.memory import db


class AlunoRepository:
    def gerar_novo_id(self) -> int:
        novo_id = db.proximo_id_aluno
        db.proximo_id_aluno += 1
        return novo_id

    def salvar(self, aluno: Aluno) -> None:
        db.aluno_por_id[aluno.id] = aluno

    def buscar_por_id(self, id: int) -> Aluno | None:
        return db.aluno_por_id.get(id)

    def existe(self, id: int) -> bool:
        return id in db.aluno_por_id

    def listar_todos(self) -> list[Aluno]:
        return list(db.aluno_por_id.values())
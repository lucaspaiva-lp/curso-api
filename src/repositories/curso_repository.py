from src.database.memory import db
from src.domain.curso import Curso

class CursoRepository:
    def salvar(self, curso: Curso) -> None:
        db.curso_por_codigo[curso.codigo] = curso

    def buscar_por_codigo(self, codigo: int) -> Curso | None:
        return db.curso_por_codigo.get(codigo)

    def listar_todos(self) -> list[Curso]:
        return list(db.curso_por_codigo.values())

    def existe(self, codigo: int) -> bool:
        return codigo in db.curso_por_codigo
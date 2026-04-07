from typing import Dict
from src.domain.aluno import Aluno
from src.domain.curso import Curso

class MemoryDB:
    def __init__(self):
        self.aluno_por_id: Dict[int, Aluno] = {}
        self.curso_por_codigo: Dict[int, Curso] = {}
        self.proximo_id_aluno = 1

db = MemoryDB()
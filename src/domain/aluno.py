from dataclasses import dataclass


@dataclass(frozen=True)
class Aluno:
    id: int
    name: str = ""
    email: str = ""
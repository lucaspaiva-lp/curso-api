class Curso:
    def __init__(self, codigo: int, titulo: str, preco: float, tipo: int, desconto_percentual: float = 0):
        self.codigo = codigo
        self.titulo = titulo
        self.preco = preco
        self.tipo = tipo
        self.desconto_percentual = desconto_percentual

    def preco_final(self) -> float:
        if self.tipo == 1:
            return 0.0
        
        valor_desconto = self.preco * (self.desconto_percentual / 100)
        resultado = self.preco - valor_desconto
        
        return max(0.0, resultado)
from enum import Enum

class TipoConta(Enum):
    POUPANCA = 1
    CORRENTE = 2

class Conta:
    def __init__(self, titular, tipo):
        self.titular = titular
        self.tipo = tipo

    def __str__(self):
        return f"Conta de {self.titular} do tipo {self.tipo.name}"

c1 = Conta("Ana", TipoConta.CORRENTE)
print(c1.tipo.name)
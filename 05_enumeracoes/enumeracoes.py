from enum import Enum, auto

class Cor(Enum):
    VERMELHO = 1
    VERDE = 2
    AZUL = 3

class Dia(Enum):
    SEGUNDA = "segunda-feira"
    TERCA = "terça-feira"
    QUARTA = "quarta-feira"

class Nivel(Enum):
    BAIXO = auto()
    MEDIO = auto()
    ALTO = auto()

print(Cor.VERMELHO)
print(Cor.VERMELHO.name)   # nome
print(Cor.VERMELHO.value)  # valor

print(Dia.SEGUNDA)
print(Dia.SEGUNDA.name)   # nome
print(Dia.SEGUNDA.value)  # valor

print(Nivel.BAIXO)
print(Nivel.BAIXO.name)   # nome
print(Nivel.BAIXO.value)  # valor
print(Nivel.MEDIO.value)  # valor
print(Nivel.ALTO.value)   # valor


from enum import Enum

class DiaSemana(Enum):
    DOMINGO = "domingo"
    SEGUNDA = "segunda-feira"
    TERCA = "terça-feira"
    QUARTA = "quarta-feira"
    QUINTA = "quinta-feira"
    SEXTA = "sexta-feira"
    SABADO = "sábado"

for d in DiaSemana:
    print(d.value, "-", d.name)
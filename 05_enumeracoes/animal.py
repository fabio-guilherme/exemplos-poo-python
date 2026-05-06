from enum import Enum

class Animal(Enum):
    CAO = 1
    GATO = 2
    LEAO = 3

sons = {
    Animal.CAO: "latir",
    Animal.GATO: "miar",
    Animal.LEAO: "rugir"
}

print(sons[Animal.CAO])
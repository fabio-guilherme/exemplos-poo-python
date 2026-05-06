from enum import Enum

class Fruta(Enum):
    MACA = 1
    BANANA = 2
    LARANJA = 3

print(Fruta.MACA is Fruta.BANANA)
print(Fruta.LARANJA == Fruta.BANANA)
print(Fruta.LARANJA is Fruta.LARANJA)
print(Fruta.LARANJA == Fruta.LARANJA)

l1 = Fruta.LARANJA
l2 = Fruta.LARANJA
print(l1 is l2) 
print(l1 == l2)

a = [1,2]
b = [1,2]
print(a is b)
print(a == b)
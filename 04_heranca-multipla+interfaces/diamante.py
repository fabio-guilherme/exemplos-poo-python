class A:
    def ml(self):
        print('metodo de A')

class B(A):
    def m2(self):
        print('metodo de B')

class C(A):
    def m2(self):
        print('metodo de C')

class D(B, C):
    pass

if __name__ == '__main__':
    print(D.mro())

    # A ordem de resolução de métodos é dada pela ordem das classes na declaração da classe D
    d = D()
    d.ml()
    d.m2()
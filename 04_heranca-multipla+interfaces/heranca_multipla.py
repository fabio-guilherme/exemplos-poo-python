import abc

class Funcionario(abc.ABC):

    def __init__(self, nome, nif, salario):
        self._nome = nome
        self._nif = nif
        self._salario = salario
        
class Autenticavel:
    def autentica (self, senha):
        pass
        # verifica se a senha confere

class Gerente (Funcionario, Autenticavel):
    def __init__(self, nome, nif, salario, senha, qtd_funcionarios):
        super().__init__(nome, nif, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

class Diretor (Funcionario, Autenticavel):
    def __init__(self, nome, nif, salario, senha):
        super().__init__(nome, nif, salario)
        self._senha = senha

class Cliente (Autenticavel):
    def __init__(self, nome, nif, senha):
        self._nome = nome
        self._nif = nif
        self._senha = senha

class SistemaInterno:

    def login(self, obj):
        if (hasattr(obj, 'autentica')):
            obj.autentica(obj._senha)
            return True
        else:
            print('{} não é autenticável' .format(obj.__class__.__name__))
            return False

class Desenvolvedor (Funcionario):
    def __init__(self, nome, nif, salario):
        super().__init__(nome, nif, salario)

if __name__ == '__main__':
    diretor = Diretor('João', '111111111-11', 3000.0, '1234')
    gerente = Gerente('José', '222222222-22', 2000.0, '1235', 10)
    cliente = Cliente('Maria', '333333333-33', '1236')
    desenvolvedor = Desenvolvedor('Carlos', '444444444-44', 1500.0)
    sistema = SistemaInterno()
    print("Resultado para diretor {}: {}".format(diretor._nome, sistema.login(diretor)))
    print("Resultado para gerente {}: {}".format(gerente._nome, sistema.login(gerente)))
    print("Resultado para cliente {}: {}".format(cliente._nome, sistema.login(cliente)))
    print("Resultado para desenvolvedor {}: {}".format(desenvolvedor._nome, sistema.login(desenvolvedor)))
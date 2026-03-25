from unicodedata import name


class Funcionario:
    pass
    def __init__(self, nome, nif, salario):
        self._nome = nome
        self._nif = nif
        self._salario = salario

    # outros metodos e properties

    def get_bonificacao(self):
        return self._salario * 0.10

class Gerente (Funcionario):
    def __init__(self, nome, nif, salario, senha, qtd_funcionarios):
        super().__init__(nome, nif, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        #return self._salario * 0.15
        #return self._salario * 0.10 + 1000
        return super().get_bonificacao() + 1000

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0): 
        self._total_bonificacoes = total_bonificacoes

    def regista(self, obj): 
        #if(hasattr(obj, 'get_bonificacao')):
        if(isinstance(obj, Funcionario)):
            self._total_bonificacoes += obj.get_bonificacao() 
        else:
            #print('Instância de {} não implementa o método get_bonificacao()'.format(obj.__class__.__name__))
            print('{} não é uma instância de Funcionario'.format(obj.__class__.__name__))

    @property
    def total_bonificacoes(self): 
        return self._total_bonificacoes

class Cliente:

    def __init__(self, nome, nif, senha):
        self._nome = nome
        self._nif = nif
        self._senha = senha

    # métodos e properties
    '''
    def get_bonificacao(self):
        return 300
    '''

if __name__  == '__main__':
    '''
    funcionario = Funcionario('João', '111111111-11', 2000.0) 
    print("Bonificação funcionário: {}".format(funcionario.get_bonificacao()))

    gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0) 
    print("Bonificação gerente: {}".format(gerente.get_bonificacao()))

    controle = ControleDeBonificacoes() 
    controle.regista(funcionario) 
    controle.regista(gerente)

    print("Total: {}".format(controle.total_bonificacoes))
    #
    cliente = Cliente('Maria', '333333333-33', '1234')
    #controle = ControleDeBonificacoes()
    controle.regista(cliente)
    '''

class Conta :
    __slots__= [ '_numero' , '_titular' , '_saldo' , '_limite' ]

    def __init__(self, numero , titular , saldo, limite=1000.0) :
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

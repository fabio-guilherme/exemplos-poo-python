import abc

class Funcionario(abc.ABC):

    def __init__(self, nome, nif, salario):
        self._nome = nome
        self._nif = nif
        self._salario = salario
    
    @abc.abstractmethod
    def get_bonificacao(self):
        pass
        
class Gerente(Funcionario):
    # outros métodos e propriedades

    def __init__(self, nome, nif, salario, senha, qtd_funcionarios):
        super().__init__(nome, nif, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        return self._salario * 0.15

# Classe Diretor que herda de Funcionario sem o método get_bonificacao() :
class Diretor(Funcionario):
    def __init__(self, nome, nif, salario):
        super().__init__(nome, nif, salario)

if __name__ == '__main__':
    # Tentativa de instanciar a classe Funcionario (que é abstrata) - isso causará um erro
    #f = Funcionario()

    # Instanciando a classe Gerente e chamando o método get_bonificacao()
    #gerente = Gerente('jose', '222222222-22', 5000.0, '1234', 0)
    #print(gerente.get_bonificacao())

    # Instanciando a classe Diretor - isso causará um erro porque o método get_bonificacao() não foi implementado
    diretor = Diretor('joao', '111111111-11', 4000.0)
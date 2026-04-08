import abc

class Autenticavel(abc.ABC) :
    """
    Classe abstrata que contém operações de um objeto autenticável.
    As subclasses concretas devem sobrescrever o método autentica.
    """

    @abc . abstractmethod
    def autentica (self, senha):
        """
        Método abstrato que faz verificação da senha.
        Devolve True se a senha confere, e False caso contrário.
        """

class Funcionario(abc.ABC):
    def __init__(self, nome, nif, salario):
        self._nome = nome
        self._nif = nif
        self._salario = salario

class Gerente (Funcionario, Autenticavel):
    def __init__(self, nome, nif, salario):
        super().__init__(nome, nif, salario)

    def autentica(self, senha):
        return senha == '1234'
    
if __name__ == '__main__':
    Autenticavel.register(Gerente)
    gerente = Gerente( 'Jolo', '111111111-11', 3000.0)
    
    # Verifica se o objeto é uma instância de Autenticavel
    print(isinstance(gerente, Autenticavel))
    print(issubclass(Gerente, Autenticavel))
    
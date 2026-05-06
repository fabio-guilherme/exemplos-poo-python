class Singleton:
    __instance = None

    #'''
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    #'''

    def __init__(self):
        # Código de inicialização, se necessário
        pass

    @classmethod
    def get_instance(cls):
        return cls()
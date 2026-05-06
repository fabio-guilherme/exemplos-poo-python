class Evento:
    def __init__(self, descricao: str, data: str):
        self.descricao = descricao
        self.data = data

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self.__descricao = descricao

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str) -> None:
        self.__data = data

    def __str__(self) -> str:
        return (
            "Evento{"
            f"descricao='{self.__descricao}', "
            f"data='{self.__data}'"
            "}"
        '''
        return (
            f"{self.__descricao} - {self.__data}"
        '''
        )
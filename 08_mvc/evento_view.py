from evento import Evento


class EventoView:
    def __init__(self):
        self.__azul = "\033[34m"
        self.__reset = "\033[0m"

    def get_descricao(self) -> str:
        print("Digite a descrição do evento: ", end="")
        return input()

    def get_data(self) -> str:
        print("Digite a data do evento (dd/mm/yyyy): ", end="")
        return input()

    def display_evento(self, evento: Evento) -> None:
        print(self.__azul)
        print(f"Evento: {evento.descricao} | Data: {evento.data}")
        #print(f"Evento adicionado: {evento}")
        print(self.__reset)
        print()

    def display_all_eventos(self, eventos: list[Evento]) -> None:
        print(self.__azul)
        print("Lista de Eventos:")

        for evento in eventos:
            print(evento)

        print(self.__reset)
        print()
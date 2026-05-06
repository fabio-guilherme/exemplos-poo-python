from evento import Evento
from evento_view import EventoView


class EventoController:
    def __init__(self, view: EventoView):
        self.__eventos: list[Evento] = []
        self.__view = view

    def adicionar_evento(self) -> None:
        descricao = self.__view.get_descricao()
        data = self.__view.get_data()

        evento = Evento(descricao, data)
        self.__eventos.append(evento)

        self.__view.display_evento(evento)

    def listar_eventos(self) -> None:
        self.__view.display_all_eventos(self.__eventos)
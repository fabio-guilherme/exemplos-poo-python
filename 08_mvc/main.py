from evento_view import EventoView
from evento_controller import EventoController

def main() -> None:
    view = EventoView()
    controller = EventoController(view)

    continuar = True

    while continuar:
        print("1. Adicionar Evento")
        print("2. Listar Eventos")
        print("3. Sair")
        print("Escolha uma opção: ", end="")

        escolha = input()

        if escolha == "1":
            controller.adicionar_evento()
        elif escolha == "2":
            controller.listar_eventos()
        elif escolha == "3":
            print("Encerrando o programa. Adeus!")
            continuar = False
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
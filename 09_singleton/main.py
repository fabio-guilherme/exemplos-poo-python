from singleton import Singleton

def main() -> None:
    singleton1 = Singleton.get_instance()
    singleton2 = Singleton.get_instance()

    print(singleton1)
    print(singleton2)

    if singleton1 is singleton2:
        print("As duas variáveis referem-se à mesma instância.")
    else:
        print("As duas variáveis referem-se a instâncias diferentes.")


if __name__ == "__main__":
    main()
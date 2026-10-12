"""TaskTracker - gerenciador de tarefas em linha de comando.

Bootcamp II (CEUB EAD) - Fase 2: Entrega Intermediária.
"""

tarefas = []


def exibir_menu():
    print("\n===== TaskTracker =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def cadastrar_tarefa():
    print("\n[Cadastro de tarefa - em desenvolvimento]")


def listar_tarefas():
    print("\n[Listagem de tarefas - em desenvolvimento]")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()

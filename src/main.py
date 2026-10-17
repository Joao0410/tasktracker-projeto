"""TaskTracker - gerenciador de tarefas em linha de comando.

Bootcamp II (CEUB EAD) - Fase 2: Entrega Intermediária.
"""

tarefas = []


def exibir_menu():
    print("\n===== TaskTracker =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def validar_titulo(texto):
    """Título é válido apenas se não for vazio nem só espaços em branco."""
    return len(texto.strip()) > 0


def normalizar_prioridade(texto):
    """Retorna a prioridade no formato padrão ou None se for inválida.

    Aceita exclusivamente Alta, Média (ou Media) e Baixa, sem diferenciar
    maiúsculas de minúsculas.
    """
    opcoes = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
    return opcoes.get(texto.strip().lower())


def pedir_titulo():
    while True:
        titulo = input("Título: ")
        if validar_titulo(titulo):
            return titulo.strip()
        print("Erro: o título é obrigatório e não pode ficar vazio. Tente novamente.")


def pedir_prioridade():
    while True:
        prioridade = normalizar_prioridade(input("Prioridade (Alta/Média/Baixa): "))
        if prioridade is not None:
            return prioridade
        print("Erro: prioridade inválida. Use Alta, Média ou Baixa.")


def cadastrar_tarefa():
    print("\n--- Cadastro de nova tarefa ---")
    titulo = pedir_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = pedir_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas():
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status:      {tarefa['status']}")
    print(f"\nTotal de tarefas: {len(tarefas)}")


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

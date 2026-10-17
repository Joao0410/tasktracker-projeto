# TaskTracker

Sistema de gerenciamento de tarefas em linha de comando (CLI), desenvolvido em Python 3 como parte do **Bootcamp II** (CEUB EAD) — Fase 2: Entrega Intermediária.

## Descrição funcional

O TaskTracker ajuda uma pessoa a organizar suas tarefas do dia a dia em um único lugar. Pelo menu do terminal é possível:

1. **Cadastrar nova tarefa** — informando título, descrição, prioridade e data limite;
2. **Visualizar tarefas cadastradas** — com todas as informações organizadas na tela;
3. **Sair da aplicação**.

### Regras de negócio

| Campo | Regra |
|---|---|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o sistema pede nova digitação. |
| Descrição | Texto livre. |
| Prioridade | Apenas `Alta`, `Média` (ou `Media`) e `Baixa`, sem diferenciar maiúsculas/minúsculas. Outro valor gera erro e repete a pergunta. |
| Data limite | Texto livre (sugestão: `DD/MM/AAAA`). |
| Status | Definido automaticamente como `Pendente` no cadastro. |

Se não houver tarefas, a listagem informa que não existem registros.

## Tecnologias

- Python 3 (somente biblioteca padrão, sem dependências externas)
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                    # Documentação principal e instruções de uso
├── .gitignore                   # Ignora arquivos temporários do Python e ambiente virtual
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico e arquitetural (Fase 1)
└── src/
    └── main.py                  # Código-fonte principal da aplicação
```

## Instalação e execução

Pré-requisito: Python 3.8 ou superior instalado.

```bash
git clone https://github.com/Joao0410/tasktracker-projeto.git
cd tasktracker-projeto
python3 src/main.py
```

No Windows, use `python src/main.py`.

## Exemplo de uso

```
===== TaskTracker =====
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
Escolha uma opção: 1
Título: Estudar Git
Descrição: Revisar commit, branch e push
Prioridade (Alta/Média/Baixa): alta
Data limite (DD/MM/AAAA): 20/10/2026
Tarefa cadastrada com sucesso!
```

## Roadmap do Bootcamp II

- **Fase 1** — Planejamento lógico (concluída)
- **Fase 2** — Repositório, Git/GitHub e implementação em Python (esta entrega)
- **Fase 3** — Containerização com Docker

## Autor

João Luiz Verissimo Falcão Rodrigues — Ciência da Computação, CEUB.

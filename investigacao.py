from registros import registros


def exibir_relatorio(operador):
    """Exibe as informações iniciais do caso de desaparecimento."""
    print("=" * 50)
    print("                  ARQUIVO 017-A")
    print("=" * 50)
    print()
    print("TIPO: RELATÓRIO FINAL")
    print("CASO: DESAPARECIMENTO")
    print("STATUS: INCOMPLETO")
    print()
    print("FUNCIONÁRIO:")
    print("ID 017")
    print()
    print("STATUS DO FUNCIONÁRIO:")
    print("DESAPARECIDO")
    print()
    print("LOCAL:")
    print("Unidade Central de Arquivos")
    print()
    print("DATA DO DESAPARECIMENTO:")
    print("17/04/2017")
    print()
    print("ÚLTIMO REGISTRO:")
    print("23:24")
    print()
    print("-" * 50)
    print()
    print("O funcionário ID 017 trabalhava no turno noturno")
    print("quando desapareceu dentro da unidade.")
    print()
    print("Nenhuma saída do prédio foi registrada.")
    print()
    print("O caso possui 16 registros relacionados.")
    print()
    print(f"Operador responsável pela revisão: {operador}")
    print()
    print("Após analisar os registros, o Arquivo 017-A")
    print("deverá receber uma conclusão.")
    print()
    print("-" * 50)
    print()
    print(f"REGISTROS DISPONÍVEIS: {len(registros)}/16")
    print()


def revisar_registros():
    """Apresenta os registros disponíveis em ordem."""
    input("Pressione Enter para iniciar a revisão...")
    print()

    for registro in registros:
        print("=" * 50)
        print(f"                  ARQUIVO {registro['codigo']}")
        print("=" * 50)
        print()
        print(f"TIPO: {registro['tipo']}")
        print(f"HORÁRIO: {registro['horario']}")
        print()
        print(registro["descricao"])
        print()

        detalhes = registro.get("detalhes")

        if detalhes:
            print("DETALHES:")

            for detalhe in detalhes:
                print(f"- {detalhe}")

            print()

        observacao = registro.get("observacao")

        if observacao:
            print("OBSERVAÇÃO:")
            print(observacao)
            print()

        input("Pressione Enter para concluir este registro...")
        print()

    print("-" * 50)
    print(f"REGISTROS REVISADOS: {len(registros)}/16")
    print()
    print("Todos os registros relacionados foram revisados.")
    print()

def solicitar_conclusao():
    """Solicita ao operador uma conclusão para o Arquivo 017-A."""
    print("=" * 50)
    print("              CONCLUSÃO DO ARQUIVO 017-A")
    print("=" * 50)
    print()
    print("Todos os registros foram analisados.")
    print()
    print("Selecione a conclusão que será registrada:")
    print()
    print("[1] Desaparecimento com causa indeterminada")
    print("[2] Possível envolvimento de uma segunda pessoa")
    print("[3] Manter a investigação aberta")
    print()

    opcao = ""

    while opcao not in ["1", "2", "3"]:
        opcao = input("> ")
        print()

        if opcao not in ["1", "2", "3"]:
            print("Opção inválida.")
            print()

    if opcao == "1":
        conclusao = "DESAPARECIMENTO COM CAUSA INDETERMINADA"

    elif opcao == "2":
        conclusao = "POSSÍVEL ENVOLVIMENTO DE UMA SEGUNDA PESSOA"

    else:
        conclusao = "INVESTIGAÇÃO MANTIDA EM ABERTO"

    return conclusao

def exibir_conclusao(operador, conclusao):
    """Exibe a conclusão escolhida pelo operador."""
    print("-" * 50)
    print("CONCLUSÃO REGISTRADA")
    print("-" * 50)
    print()
    print(f"OPERADOR: {operador}")
    print(f"ARQUIVO: 017-A")
    print(f"CONCLUSÃO: {conclusao}")
    print()
    print("O relatório foi atualizado.")
    print()

def iniciar_investigacao(operador):
    """Inicia a apresentação, revisão e conclusão do caso."""
    exibir_relatorio(operador)
    revisar_registros()

    conclusao = solicitar_conclusao()
    exibir_conclusao(operador, conclusao)
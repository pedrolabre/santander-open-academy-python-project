def exibir_cabecalho():
    """Exibe o cabeçalho inicial do sistema."""
    print("=" * 50)
    print("        SISTEMA CENTRAL DE ARQUIVAMENTO")
    print("                  VERSÃO 4.17")
    print("=" * 50)
    print()


def identificar_operador():
    """Solicita e valida a identificação do operador."""
    operador = input("Identificação do operador: ")

    while operador == "":
        print("Identificação obrigatória.")
        operador = input("Identificação do operador: ")

    return operador


def iniciar_sessao(operador):
    """Apresenta a sessão e o arquivo pendente do operador."""
    print()
    print("Credenciais aceitas.")
    print(f"Bem-vindo, {operador}.")
    print()
    print("Verificando registros pendentes...")
    print()
    print("1 arquivo associado ao operador encontrado.")
    print()
    print("-" * 50)
    print("ARQUIVO: 017-A")
    print("CLASSIFICAÇÃO: RESTRITO")
    print("STATUS: INCOMPLETO")
    print(f"OPERADOR ASSOCIADO: {operador}")
    print("-" * 50)
    print()


def solicitar_abertura():
    """Mantém a sessão ativa até o arquivo pendente ser aberto."""
    opcao = ""

    while opcao != "1":
        print("[1] Abrir Arquivo 017-A")
        print("[2] Encerrar sessão")
        print()

        opcao = input("> ")
        print()

        if opcao == "2":
            print("Existe um arquivo pendente.")
            print("A sessão não pode ser encerrada antes da revisão.")
            print()

        elif opcao != "1":
            print("Opção inválida.")
            print()


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
    print("REGISTROS DISPONÍVEIS: 0/16")
    print()
    print("Os registros relacionados ainda não foram carregados.")
    print()
    input("Pressione Enter para encerrar a consulta...")


exibir_cabecalho()

operador = identificar_operador()

iniciar_sessao(operador)
solicitar_abertura()
exibir_relatorio(operador)
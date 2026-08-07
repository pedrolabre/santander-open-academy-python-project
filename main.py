from investigacao import iniciar_investigacao

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


exibir_cabecalho()

operador = identificar_operador()

iniciar_sessao(operador)
solicitar_abertura()
iniciar_investigacao(operador)
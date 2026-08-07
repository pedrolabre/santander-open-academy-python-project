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


def exibir_relatorio(operador, quantidade_registros):
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
    print(f"REGISTROS DISPONÍVEIS: {quantidade_registros}/16")
    print()


def revisar_registros(registros):
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
    print("Os demais registros ainda não estão disponíveis.")
    print()
    input("Pressione Enter para encerrar a consulta...")


registros = [
    {
        "codigo": "001-A",
        "tipo": "CONTROLE DE ACESSO",
        "horario": "22:04",
        "descricao": (
            "O crachá do funcionário ID 017 foi registrado\n"
            "na entrada principal da unidade.\n\n"
            "Não houve nenhuma irregularidade no acesso."
        )
    },
    {
        "codigo": "002-A",
        "tipo": "ESCALA DE TRABALHO",
        "horario": "22:10",
        "descricao": (
            "A escala confirma que o funcionário ID 017\n"
            "era o único funcionário designado para o turno.\n\n"
            "Nenhuma outra pessoa deveria estar na unidade."
        )
    },
    {
        "codigo": "003-A",
        "tipo": "CÂMERA DE SEGURANÇA",
        "horario": "22:41",
        "descricao": (
            "A câmera do corredor principal registrou\n"
            "o funcionário ID 017 seguindo para o setor de arquivos.\n\n"
            "Uma segunda pessoa aparece alguns metros atrás dele."
        ),
        "observacao": (
            "A identidade da segunda pessoa não pôde ser confirmada."
        )
    },
    {
        "codigo": "004-A",
        "tipo": "CONTROLE DE ACESSO",
        "horario": "22:43",
        "descricao": (
            "Os registros de entrada foram verificados após\n"
            "a identificação da segunda pessoa nas câmeras.\n\n"
            "Nenhum outro acesso foi registrado naquela noite."
        ),
        "observacao": (
            "O funcionário ID 017 continua sendo a única pessoa\n"
            "com entrada registrada na unidade."
        )
    },
    {
        "codigo": "005-A",
        "tipo": "REGISTRO DE TELEFONIA",
        "horario": "22:48",
        "descricao": (
            "O funcionário ID 017 utilizou o telefone interno\n"
            "para ligar para o supervisor de plantão."
        ),
        "detalhes": [
            "Origem: ramal do setor de arquivos",
            "Destino: supervisor de plantão",
            "Status: chamada atendida"
        ]
    },
    {
        "codigo": "006-A",
        "tipo": "REGISTRO DE TELEFONIA",
        "horario": "22:49",
        "descricao": (
            "A ligação foi encerrada após poucos segundos.\n\n"
            "Não houve outra tentativa de contato."
        ),
        "detalhes": [
            "Duração: 12 segundos",
            "Encerramento: ramal do funcionário ID 017"
        ],
        "observacao": (
            "O conteúdo da ligação não foi registrado."
        )
    }
]


exibir_cabecalho()

operador = identificar_operador()

iniciar_sessao(operador)
solicitar_abertura()
exibir_relatorio(operador, len(registros))
revisar_registros(registros)
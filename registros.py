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
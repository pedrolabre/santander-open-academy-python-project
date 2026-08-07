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
    },
    {
        "codigo": "007-A",
        "tipo": "CÂMERA DE SEGURANÇA",
        "horario": "22:52",
        "descricao": (
            "Após encerrar a ligação, o funcionário ID 017\n"
            "foi registrado caminhando em direção à sala de arquivos.\n\n"
            "Esta foi a última imagem clara do funcionário antes\n"
            "da interrupção das câmeras."
        ),
        "observacao": (
            "A segunda pessoa identificada anteriormente\n"
            "não aparece nesta gravação."
        )
    },
    {
        "codigo": "008-A",
        "tipo": "REGISTRO DO SISTEMA",
        "horario": "23:17",
        "descricao": (
            "O sistema registrou uma interrupção no fornecimento\n"
            "de energia da Unidade Central de Arquivos."
        ),
        "detalhes": [
            "Horário da interrupção: 23:17",
            "Sistemas afetados: iluminação e câmeras de segurança"
        ],
        "observacao": (
            "O sistema de controle de acesso permaneceu ativo."
        )
    },
    {
        "codigo": "009-A",
        "tipo": "CÂMERA DE SEGURANÇA",
        "horario": "23:17",
        "descricao": (
            "As câmeras de segurança deixaram de transmitir\n"
            "durante a interrupção de energia.\n\n"
            "Nenhuma imagem foi registrada nesse período."
        ),
        "detalhes": [
            "Início da interrupção: 23:17",
            "Retorno das câmeras: 23:24",
            "Tempo sem gravação: 7 minutos"
        ]
    },
    {
        "codigo": "010-A",
        "tipo": "CONTROLE DE ACESSO",
        "horario": "23:21",
        "descricao": (
            "Durante o período sem imagens, o sistema registrou\n"
            "a abertura de uma porta no setor restrito de arquivos."
        ),
        "observacao": (
            "A porta permaneceu aberta por menos de um minuto."
        )
    },
    {
        "codigo": "011-A",
        "tipo": "CONTROLE DE ACESSO",
        "horario": "23:21",
        "descricao": (
            "A abertura da porta restrita foi autorizada\n"
            "por um crachá válido do sistema."
        ),
        "detalhes": [
            "Crachá utilizado: ID 017",
            "Acesso: autorizado",
            "Local: setor restrito de arquivos"
        ],
        "observacao": (
            "O crachá pertencia ao funcionário desaparecido."
        )
    },
    {
        "codigo": "012-A",
        "tipo": "CÂMERA DE SEGURANÇA",
        "horario": "23:24",
        "descricao": (
            "As câmeras voltaram a funcionar após sete minutos.\n\n"
            "O funcionário ID 017 não aparece nas imagens\n"
            "registradas depois do restabelecimento."
        ),
        "observacao": (
            "Nenhuma imagem mostra o funcionário deixando\n"
            "o setor de arquivos."
        )
    },
    {
        "codigo": "013-A",
        "tipo": "CONTROLE DE ACESSO",
        "horario": "06:00",
        "descricao": (
            "Os registros de saída da unidade foram verificados\n"
            "após o encerramento do turno noturno.\n\n"
            "Não existe registro de saída do funcionário ID 017."
        ),
        "detalhes": [
            "Entrada registrada: 22:04",
            "Saída registrada: nenhuma"
        ]
    },
    {
        "codigo": "014-A",
        "tipo": "REGISTRO DO TERMINAL",
        "horario": "06:18",
        "descricao": (
            "Durante a análise do computador utilizado pelo\n"
            "funcionário ID 017, um novo arquivo foi encontrado."
        ),
        "detalhes": [
            "Local: terminal do setor de arquivos",
            "Arquivo criado durante o turno do desaparecimento"
        ],
        "observacao": (
            "O arquivo não constava nos registros anteriores do terminal."
        )
    },
    {
        "codigo": "015-A",
        "tipo": "ARQUIVO RECUPERADO",
        "horario": "23:22",
        "descricao": (
            "Os dados do arquivo encontrado no terminal indicam\n"
            "que ele foi criado durante a interrupção das câmeras.\n\n"
            "O arquivo contém apenas uma mensagem."
        ),
        "observacao": (
            "O registro de criação ocorreu dois minutos antes\n"
            "do retorno das câmeras."
        )
    },
    {
        "codigo": "016-A",
        "tipo": "MENSAGEM RECUPERADA",
        "horario": "23:22",
        "descricao": (
            "Conteúdo integral do arquivo encontrado no terminal:\n\n"
            "\"Eu não estou sozinho aqui. Não arquivem o caso.\""
        ),
        "observacao": (
            "Nenhuma alteração posterior foi registrada no arquivo."
        )
    }
]
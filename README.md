# Arquivo 17

Microconto interativo de suspense desenvolvido em Python para execução no terminal.

O projeto foi criado como aplicação prática dos fundamentos estudados no curso de Python da Santander Open Academy. Em vez de reproduzir exercícios isolados, a proposta foi reunir diferentes conceitos da linguagem em uma pequena experiência interativa.

## Sobre o projeto

Em **Arquivo 17**, o usuário assume o papel de um operador de um antigo sistema de arquivamento.

Após iniciar a sessão, o sistema identifica um relatório incompleto relacionado ao desaparecimento do funcionário ID 017, ocorrido durante um turno noturno na Unidade Central de Arquivos.

O operador deve revisar 16 registros relacionados ao caso, reconstruir os acontecimentos daquela noite e escolher qual conclusão será registrada no relatório.

A decisão tomada interfere no desfecho apresentado pelo sistema.

## Execução

É necessário ter Python 3 instalado.

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/pedrolabre/santander-open-academy-python-project.git
cd santander-open-academy-python-project
```

Execute:

```bash
python main.py
```

No Windows, dependendo da instalação do Python, também pode ser utilizado:

```bash
py main.py
```

## Estrutura

```text
santander-open-academy-python-project/
├── main.py
├── investigacao.py
├── registros.py
└── README.md
```

### `main.py`

Responsável pela entrada no sistema, identificação do operador e início do fluxo principal.

### `investigacao.py`

Controla a apresentação do caso, revisão dos registros, escolha da conclusão e os diferentes desfechos.

### `registros.py`

Armazena os 16 registros utilizados para construir a narrativa da investigação.

## Fundamentos aplicados

Durante o desenvolvimento foram utilizados conceitos abordados no curso, entre eles:

- variáveis e strings;
- entrada e saída com `input()` e `print()`;
- f-strings;
- estruturas condicionais com `if`, `elif` e `else`;
- estruturas de repetição com `while` e `for`;
- listas e dicionários;
- acesso a valores opcionais em dicionários;
- funções, parâmetros e valores de retorno;
- escopo local;
- docstrings;
- funções nativas como `len()`;
- métodos de strings como `strip()`;
- organização do código em módulos;
- importação de módulos próprios.

## Desenvolvimento

O projeto foi construído de forma incremental.

A primeira versão continha apenas a identificação do operador e a apresentação do Arquivo 017-A. Ao longo do desenvolvimento, foram adicionados o caso de desaparecimento, os registros da investigação, a organização dos dados em módulos, as decisões do operador, diferentes desfechos e melhorias na validação das entradas.

Essa evolução também está registrada no histórico de commits do repositório.

## Contexto

Projeto desenvolvido após a conclusão do curso de Python da Santander Open Academy, como forma de transformar os fundamentos apresentados durante a formação em uma aplicação pequena, completa e autoral.
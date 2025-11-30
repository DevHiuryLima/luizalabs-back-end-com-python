# Dicionários Aninhados em Python
# Dicionários aninhados são dicionários que contêm outros dicionários como valores
# Eles são úteis para representar estruturas de dados mais complexas


# Declarando um dicionário aninhado para armazenar contatos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}


# Acessando dados em um dicionário aninhado
telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)
# Saída: 3443-2121

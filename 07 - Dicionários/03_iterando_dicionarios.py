# Declarando um dicionário aninhado para armazenar contatos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}


# Iterando sobre as chaves do dicionário
for chave in contatos:
    print(chave, contatos[chave])


# Separador para melhor visualização
print("=" * 100)


# Iterando sobre os valores do dicionário usando o método items()
# O método items() retorna uma lista de tuplas, onde cada tupla contém um par chave-valor
for chave, valor in contatos.items():
    print(chave, valor)

# Método clear() em dicionários


# Declarando um dicionário aninhado para armazenar contatos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}


# O método clear() remove todos os itens do dicionário in-place.
# Não retorna um novo dicionário; retorna None.
# Modifica o objeto existente: todas as referências ao mesmo dicionário verão o dicionário vazio após o clear().
contatos.clear()


# Após clear(), o dicionário continua sendo o mesmo objeto, mas agora vazio.
print(contatos)
# Saída: {}

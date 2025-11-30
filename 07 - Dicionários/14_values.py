# Método values() em dicionários


# Declarando um dicionário aninhado para armazenar vários contatos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}


# O método values() retorna uma visão dos valores no dicionário.
# Essa visão é dinâmica e reflete as mudanças feitas no dicionário original.
resultado = (
    contatos.values()
)
print(resultado)
# Saída: dict_values(
#   [
#       {'nome': 'Guilherme', 'telefone': '3333-2221'},
#       {'nome': 'Giovanna', 'telefone': '3443-2121'},
#       {'nome': 'Chappie', 'telefone': '3344-9871'},
#       {'nome': 'Melaine', 'telefone': '3333-7766'}
#   ]
# )

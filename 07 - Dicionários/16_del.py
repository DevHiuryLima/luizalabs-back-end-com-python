# Método del em dicionários


# Declarando um dicionário aninhado para armazenar vários contatos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}


# A instrução del remove um par chave-valor do dicionário.
# Também pode ser usada para remover uma chave específica dentro de um dicionário aninhado
del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]


print(contatos)
# Saída: 
# {
#   'guilherme@gmail.com': {'nome': 'Guilherme'},
#   'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
#   'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}
# }

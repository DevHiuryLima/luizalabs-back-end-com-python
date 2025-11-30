# Método items() em dicionários


# Declarando um dicionário aninhado para armazenar um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


# O método items() retorna uma visão (view) dos pares chave-valor do dicionário como tuplas dentro de um objeto dict_items.
# Essa visão é dinâmica e reflete as mudanças feitas no dicionário original.
resultado = contatos.items()
print(resultado)
# Saída: dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

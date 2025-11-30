# Método keys() em dicionários


# Declarando um dicionário aninhado para armazenar um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


# O método keys() retorna uma visão (view) das chaves do dicionário.
# Essa visão é dinâmica e reflete as mudanças feitas no dicionário original.
resultado = contatos.keys()
print(resultado)
# Saída: dict_keys(['guilherme@gmail.com'])

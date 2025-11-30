# Método update() em dicionários


# Declarando um dicionário aninhado para armazenar um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


# O método update() atualiza o dicionário com os pares chave-valor de outro dicionário ou de um iterável de pares chave-valor.
# Se a chave já existir, o valor será atualizado; caso contrário, a chave-valor será adicionada.
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)
# Saída: {'guilherme@gmail.com': {'nome': 'Gui'}}


# Nesse caso, uma nova chave-valor será adicionada ao dicionário
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos)
# Saída: {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

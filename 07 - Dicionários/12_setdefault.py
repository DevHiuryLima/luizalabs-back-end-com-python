# Método setdefault() em dicionários


# Declarando um dicionário para armazenar um contato
contato = {"nome": "Guilherme", "telefone": "3333-2221"}


# O método setdefault() retorna o valor da chave especificada.
# Se a chave não existir, insere a chave com o valor padrão fornecido.
contato.setdefault("nome", "Giovanna")
print(contato)
# Saída: {'nome': 'Guilherme', 'telefone': '3333-2221'}


# A chave "idade" não existe, então ela será adicionada com o valor padrão 28
contato.setdefault("idade", 28)
print(contato)
# Saída: {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

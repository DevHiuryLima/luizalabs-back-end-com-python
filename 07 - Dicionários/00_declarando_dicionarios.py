# Declarando dicionários em Python
# Dicionários são coleções não ordenadas, mutáveis e indexadas por chaves
# São definidos usando chaves {}


# Exemplo de declaração de dicionários:
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)
# Saída: {'nome': 'Guilherme', 'idade': 28}


# Outra forma de declarar um dicionário usando a função dict()
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)
# Saída: {'nome': 'Guilherme', 'idade': 28}


# Adicionando novos pares chave-valor ao dicionário
pessoa["telefone"] = "3333-1234"
print(pessoa)
# Saída: {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'}

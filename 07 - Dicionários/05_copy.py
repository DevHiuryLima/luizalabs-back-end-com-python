# Método copy() em dicionários


# Declarando um dicionário com dados de uma pessoa
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


# O método copy() cria uma cópia rasa (shallow copy) do dicionário.
# Retorna um novo dicionário com os mesmos pares chave-valor do original.
copia = contatos.copy()


# Modificando a cópia não afeta o dicionário original
copia["guilherme@gmail.com"] = {"nome": "Gui"}


print(contatos["guilherme@gmail.com"])
# Saída: {"nome": "Guilherme", "telefone": "3333-2221"}


print(copia["guilherme@gmail.com"])
# Saída: {"nome": "Gui"}

# Declarando um dicionário com dados de uma pessoa
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}


# Acessando valores no dicionário usando suas chaves
print(dados["nome"])
# Sáida: "Guilherme"


print(dados["idade"])
# Saída: 28


print(dados["telefone"])
# Saída "3333-1234"


# Modificando valores no dicionário
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"


print(dados)
# Saída: {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

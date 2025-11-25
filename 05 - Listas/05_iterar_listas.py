# Declarando uma lista de carros
carros = ["gol", "celta", "palio"]


# Iterando sobre a lista de carros usando um loop for
# O loop percorre cada elemento da lista e o atribui à variável 'carro'
for carro in carros:
    print(carro)
# Saída:
# gol
# celta
# palio

# Usando enumerate para obter o índice e o valor ao mesmo tempo
# enumerate() gera pares de índice e valor, facilitando a iteração com acesso ao índice
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
# Saída:
# 0: gol
# 1: celta
# 2: palio

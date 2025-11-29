# Declarando uma tupla de carros
carros = ("gol", "celta", "palio",)


# Iterando sobre a tupla de carros usando um loop for
# O loop percorre cada elemento da tupla e o atribui à variável 'carro'
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

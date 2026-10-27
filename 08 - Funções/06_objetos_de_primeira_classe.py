# Funções como objetos de primeira classe
# Em Python, funções são objetos de primeira classe. Isso significa que elas podem ser:
# - Atribuídas a variáveis, passadas como argumentos para outras funções e retornadas por outras funções.


# variáveis, passadas como argumentos e chamadas dentro de outras funções.
def somar(a, b):
    # Retorna a soma dos dois valores recebidos.
    return a + b


# Recebe dois números e uma função como argumentos.
def exibir_resultado(a, b, funcao):
    # Chama a função recebida, passando a e b, e guarda o valor retornado.
    resultado = funcao(a, b)
    # Exibe os valores usados e o resultado da operação.
    print(f"O resultado da operação {a} + {b} = {resultado}")


# Passa somar sem parênteses: assim, enviamos a própria função como argumento,
# em vez de executá-la imediatamente. exibir_resultado chama somar internamente.
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
# Saída: O resultado da operação 10 + 10 = 20

op = somar # Atribui a função somar à variável op.

print(op(1, 23))
# Saída: 24

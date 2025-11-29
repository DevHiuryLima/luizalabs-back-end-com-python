## Criando uma matriz usando tuplas aninhadas
# Uma matriz é uma coleção de elementos organizados em linhas e colunas
# Aqui, usamos tuplas para criar uma matriz imutável
# Estrutura visual:
#     coluna 0  coluna 1  coluna 2
# linha 0: [1,      "a",      2]
# linha 1: ["b",     3,       4]
# linha 2: [6,       5,      "c"]


matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

# Acessando uma linha inteira
# matriz[0] acessa a primeira linha (índice 0)
print(matriz[0])
# Saída: (1, "a", 2)


# Acessando um elemento específico usando dois índices
# matriz[0][0] acessa a primeira linha, primeira coluna
print(matriz[0][0])
# Saída: 1


# Acessando o último elemento da primeira linha
# matriz[0][-1] acessa a primeira linha, último elemento
print(matriz[0][-1])
# Saída: 2


# Acessando o último elemento da última linha
# matriz[-1][-1] acessa a última linha, último elemento
print(matriz[-1][-1])
# Saída: c

# Declarando uma tupla com elementos de frutas
# Os índices negativos começam do -1 (último elemento) e vão para trás
frutas = ("maçã", "laranja", "uva", "pera",)
#          [0]      [1]       [2]    [3]    (índices positivos)
#          [-4]     [-3]      [-2]   [-1]   (índices negativos)


# Acessando o último elemento usando índice negativo
# frutas[-1] acessa o último elemento da tupla
print(frutas[-1])  # pera


# Acessando o terceiro elemento a partir do final
# frutas[-3] acessa o terceiro elemento contando de trás para frente
print(frutas[-3])  # laranja

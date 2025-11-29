# Declarando uma tupla de caracteres
tupla = ("p", "y", "t", "h", "o", "n",)

# Fatiamento (slicing) permite acessar partes da tupla
# A sintaxe é tupla[início:fim:passo]


# Acessando elementos a partir do índice 2 até o final
print(tupla[2:])
# Saída: ['t', 'h', 'o', 'n'] (começa no índice 2 e vai até o final)


# Acessando elementos do início até o índice 2 (exclui o 2)
print(tupla[:2])
# Saída: ['p', 'y'] (pega do início até antes do índice 2)


# Acessando elementos do índice 1 até o índice 3 (exclui o 3)
print(tupla[1:3])
# Saída: ['y', 't'] (pega os elementos nos índices 1 e 2)


# Acessando elementos do índice 0 até o índice 3, pulando de 2 em 2
print(tupla[0:3:2])
# Saída: ['p', 't'] (pega o índice 0 e depois o índice 2)


# Acessando todos os elementos da tupla
print(tupla[::])
# Saída: ['p', 'y', 't', 'h', 'o', 'n'] (copia a tupla inteira)


# Revertendo a tupla usando fatiamento
print(tupla[::-1])
# Saída: ['n', 'o', 'h', 't', 'y', 'p'] (passo -1 inverte a tupla)

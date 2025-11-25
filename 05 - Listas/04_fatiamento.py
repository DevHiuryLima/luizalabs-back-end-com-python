# Declarando uma lista de caracteres
lista = ["p", "y", "t", "h", "o", "n"]

# Fatiamento (slicing) permite acessar partes da lista
# A sintaxe é lista[início:fim:passo]



# Acessando elementos a partir do índice 2 até o final
print(lista[2:])
# Saída: ['t', 'h', 'o', 'n'] (começa no índice 2 e vai até o final)

# Acessando elementos do início até o índice 2 (exclui o 2)
print(lista[:2])
# Saída: ['p', 'y'] (pega do início até antes do índice 2)


# Acessando elementos do índice 1 até o índice 3 (exclui o 3)
print(lista[1:3])
# Saída: ['y', 't'] (pega os elementos nos índices 1 e 2)


# Acessando elementos do índice 0 até o índice 3, pulando de 2 em 2
print(lista[0:3:2])
# Saída: ['p', 't'] (pega o índice 0 e depois o índice 2)


# Acessando todos os elementos da lista
print(lista[::])
# Saída: ['p', 'y', 't', 'h', 'o', 'n'] (copia a lista inteira)


# Revertendo a lista usando fatiamento
print(lista[::-1])
# Saída: ['n', 'o', 'h', 't', 'y', 'p'] (passo -1 inverte a lista)

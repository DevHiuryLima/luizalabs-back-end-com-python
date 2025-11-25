# Método append() em listas

# Cria uma lista vazia para começar a armazenar elementos
lista = []

# append() adiciona UM elemento ao final da lista.
# Observação: append modifica a lista in-place (não retorna nova lista).

# Adiciona um inteiro -> lista passa a ser [1]
lista.append(1)

# Adiciona uma string -> lista passa a ser [1, "Python"]
lista.append("Python")


# Se você passar uma lista para append(), essa lista é adicionada como UM único elemento
# (ou seja, cria-se uma lista aninhada). Para concatenar elementos de outra lista,

# Adiciona a lista como um elemento -> [1, "Python", [40,30,20]]
lista.append([40, 30, 20])


print(lista)  
# Saída: [1, 'Python', [40, 30, 20]]
 
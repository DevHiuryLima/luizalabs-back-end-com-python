# Declarando Tuplas em Pytho
# Tuplas são coleções ordenadas e imutáveis de itens
# Podem conter elementos de diferentes tipos de dados
# São definidas usando parênteses ()


# Exemplo de declaração de tuplas:
frutas = ("laranja", "pera", "uva",)
print(frutas)
# Saída: ('laranja', 'pera', 'uva')


# Tuplas podem ser declaradas sem parênteses
# Isso é chamado de "packing"
letras = tuple("python")
print(letras)
# Saída: ('p', 'y', 't', 'h', 'o', 'n')


# Criando uma tupla com números usando a função tuple()
numeros = tuple([1, 2, 3, 4])
print(numeros)
# Saída: (1, 2, 3, 4)


# Tupla com um único elemento
# Note a vírgula após o elemento
# Sem a vírgula, o Python interpreta como uma string comum
pais = ("Brasil",)
print(pais)
# Saída: ('Brasil',)

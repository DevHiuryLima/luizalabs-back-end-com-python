# Filtrar lista
# Cria uma nova lista apenas com os números pares.
# Compreensão de lista tem a forma: [expressão for item in iterável if condição]
# - A expressão (a esquerda) define o que vai para a nova lista.
# - O for itera sobre o iterável.
# - O if (opcional) filtra elementos.
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
# Saída esperada: [30, 2, 34] — somente números pares


# Modificar valores
# Aplica uma transformação a cada elemento da lista original.
# Aqui calculamos o quadrado de cada número
# A expressão numero**2 é avaliada para cada elemento 'numero' do iterável.
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros] 
print(quadrado)
# Saída esperada: [1, 900, 441, 4, 81, 4225, 1156]

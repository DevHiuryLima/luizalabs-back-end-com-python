# Método clear() em listas



lista = [1, "Python", [40, 30, 20]]


# Exibe a lista original
print(lista) 


# clear() remove todos os elementos da lista in-place.
# Não retorna uma nova lista; retorna None.
# Modifica o objeto existente: todas as referências à mesma lista verão a lista vazia após o clear().
lista.clear()


# Após clear(), a lista continua sendo o mesmo objeto, mas agora vazio.
print(lista)
# Saída: []

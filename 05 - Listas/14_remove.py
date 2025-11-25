# Método remove() - Remove o primeiro item em listas 


# Cria uma lista com algumas linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]


# remove() remove a primeira ocorrência de um elemento específico na lista.
# Se o elemento não for encontrado, gera um ValueError.
linguagens.remove("c")


print(linguagens)
# Saída: ["python", "js", "java", "csharp"]

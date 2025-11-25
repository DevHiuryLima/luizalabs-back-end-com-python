# Método extend() em listas


# Cria uma lista com algumas linguagens de programação
linguagens = ["python", "js", "c"]


print(linguagens)
# Saída: ["python", "js", "c"]

# extend() adiciona os elementos de um iterável (como outra lista) ao final da lista original.
# Modifica a lista in-place e não retorna uma nova lista.
linguagens.extend(["java", "csharp"])


print(linguagens)
# Saída: ["python", "js", "c", "java", "csharp"]

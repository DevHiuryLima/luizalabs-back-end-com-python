# Método sorted() em listas


# Cria uma lista com algumas linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]


# sorted() retorna uma nova lista ordenada, sem modificar a lista original.
print(sorted(linguagens, key=lambda x: len(x)))
# Saída: ["c", "js", "java", "python", "csharp"]

# sorted() com o parâmetro reverse=True ordena em ordem decrescente.
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
# Saída: ["python", "csharp", "java", "js", "c"]

# Método sort() em listas


# Cria uma lista com algumas linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]


# sort() ordena os elementos da lista in-place.
# Por padrão, ordena em ordem crescente (alfabética para strings).
linguagens.sort()
print(linguagens)
# Saída: ["c", "csharp", "java", "js", "python"]


# Cria novamente uma lista com algumas linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]
# sort() com o parâmetro reverse=True ordena em ordem decrescente.
linguagens.sort(reverse=True)
print(linguagens)
# Saída: ["python", "js", "java", "csharp", "c"]


# Cria novamente uma lista com algumas linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]
# sort() com o parâmetro key permite definir uma função personalizada para determinar a ordem.
# Aqui, ordenamos pelas strings com base em seu comprimento.
linguagens.sort(key=lambda x: len(x))
print(linguagens)
# Saída: ["c", "js", "java", "python", "csharp"]


# Cria novamente uma lista com algumas linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]
# Ordena pelas strings com base em seu comprimento em ordem decrescente.
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)
# Saída: ["python", "csharp", "java", "js", "c"]

# Definindo uma variável com o nome
nome = "hIUrY"


# Exibindo o nome em diferentes formatos:
print(nome.upper())  # Converte todas as letras para maiúsculas: "HIURY"
print(nome.lower())  # Converte todas as letras para minúsculas: "hiury"
print(nome.title())  # Converte a primeira letra de cada palavra para maiúscula: "Hiury"


# Definindo uma variável com texto que contém espaços em branco
texto = "  Olá mundo    "

# Exibindo o texto original com espaços
print(texto + "!")  # Exibe o texto original seguido de um ponto de exclamação

# Exibindo o texto sem espaços em branco no início e no fim
print(texto.strip() + "!")  # Exibe o texto original seguido de um ponto de exclamação

print(texto.rstrip() + "!")  # Exibe o texto original seguido de um ponto de exclamação e sem espaços no final

print(texto.lstrip() + "!")  # Exibe o texto original seguido de um ponto de exclamação e sem espaços no início


# Definindo uma variável para o menu
menu = "Python"


print("####" + menu + "####")  # Exibe o texto com caracteres antes e depois da string

print(menu.center(14))  # Centraliza o texto em 14 caracteres, preenchendo com espaços em branco

print(menu.center(14, "#"))  # Centraliza o texto em 14 caracteres, preenchendo com "#"

print("-".join(menu))  # Exibe o texto com um hífen entre cada caractere da string

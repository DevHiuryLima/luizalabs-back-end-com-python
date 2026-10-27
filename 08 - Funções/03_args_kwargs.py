# Funções com *args e **kwargs
# *args e **kwargs são usados para receber uma quantidade variável de argumentos em funções.


# Define uma função que aceita um texto inicial, vários argumentos posicionais
# e vários argumentos nomeados.
def exibir_poema(data_extenso, *args, **kwargs):
    # *args reúne os argumentos posicionais extras em uma tupla.
    # join() combina as linhas usando uma quebra de linha como separador.
    texto = "\n".join(args)

    # **kwargs reúne os argumentos nomeados extras em um dicionário.
    # items() permite percorrer cada par de chave e valor.
    # title() deixa a primeira letra de cada palavra da chave em maiúscula.
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])

    # Monta a mensagem com o título, o texto do poema e os metadados,
    # separando essas partes com linhas em branco.
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    # Exibe a mensagem montada; a função não retorna esse texto.
    print(mensagem)


# O primeiro argumento é atribuído a data_extenso.
# As strings seguintes são reunidas em args, na ordem em que foram passadas.
# autor e ano são argumentos nomeados reunidos em kwargs.
exibir_poema(
    "Sexta-feira, 19 de fevereiro de 1999",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)
# Saída: título, linhas do poema separadas por quebras de linha e, ao final:
# Autor: Tim Peters
# Ano: 1999

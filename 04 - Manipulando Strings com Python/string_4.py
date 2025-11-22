# Variável com um nome simples
nome = "Hiury"


# String multilinha com triple quotes (""")
# As aspas triplas permitem quebras de linha dentro da string
# f"""...""" = f-string multilinha (permite interpolação de variáveis)
# Observe que os espaços em branco (indentação) fazem parte da string
mensagem = f"""

   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""


# Exibe a mensagem completa com todas as quebras de linha e espaços
print(mensagem)


# String multilinha sem interpolação (sem o f)
# Também usa triple quotes para permitir múltiplas linhas
# Útil para criar menus, cabeçalhos e outras estruturas de texto formatado
print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)

# Funções em Python
# Uma função agrupa instruções que podem ser executadas quando ela é chamada.
# O código indentado forma o corpo da função e não roda durante a definição.
# É xecutado quando ela é chamada. Ex: funcao()


# Define uma função sem parâmetros: ela não precisa receber dados para executar.
def exibir_mensagem():
    print("Olá mundo!")


# Define uma função com um parâmetro obrigatório chamado nome.
# O valor recebido pode ser usado dentro do corpo da função.
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


# Define uma função com parâmetro opcional: "Anônimo" é o valor padrão.
# Se a chamada não fornecer nome, a função usará esse valor.
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


# Chama a função sem parâmetros.
exibir_mensagem()
# Saída: Olá mundo!

# Passa "Guilherme" para o parâmetro nome usando o nome do parâmetro.
# Esse formato é chamado de argumento nomeado.
exibir_mensagem_2(nome="Guilherme")
# Saída: Seja bem vindo Guilherme!

# Como nenhum argumento foi informado, nome recebe o valor padrão "Anônimo".
exibir_mensagem_3()
# Saída: Seja bem vindo Anônimo!

# O argumento informado substitui o valor padrão nessa chamada.
exibir_mensagem_3(nome="Chappie")
# Saída: Seja bem vindo Chappie!

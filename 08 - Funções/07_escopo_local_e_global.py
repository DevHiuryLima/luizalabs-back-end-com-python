# Objetos de escopo local e global
# Variáveis definidas dentro de uma função são locais a ela e não podem ser acessadas


# Variável definida no escopo global: pode ser acessada fora e dentro das funções.
salario = 2000


# O parâmetro bonus é local à função e recebe o valor passado na chamada.
def salario_bonus(bonus):
    # A declaração global permite alterar aqui a variável salario definida fora da função.
    # Sem global, uma atribuição a salario dentro da função criaria uma variável local.
    global salario
    # Soma o bônus ao salário global e atualiza seu valor.
    salario += bonus
    # Devolve o salário atualizado para quem chamou a função.
    return salario


# Chama a função com um bônus de 500; o retorno é 2500.
# Como o retorno não é passado para print() nem armazenado, nada é exibido no terminal.
salario_bonus(500)

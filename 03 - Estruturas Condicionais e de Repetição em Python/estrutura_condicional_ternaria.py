saldo = 2000
saque = 2500


# Estrutura condicional ternária
# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso
# É uma forma concisa de escrever um if-else em uma única linha
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

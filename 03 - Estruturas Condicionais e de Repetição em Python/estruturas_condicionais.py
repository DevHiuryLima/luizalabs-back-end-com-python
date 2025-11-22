# Definindo constantes para idade
MAIOR_IDADE = 18        # Idade mínima para tirar CNH
IDADE_ESPECIAL = 17     # Idade que permite apenas aulas teóricas


# Recebe a idade do usuário e converte para inteiro
idade = int(input("Informe sua idade: "))


# Exemplo 1: Estrutura IF simples
# Verifica apenas uma condição, sem alternativa
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


# Exemplo 2: Estrutura IF-ELSE
# Verifica uma condição e fornece uma alternativa caso seja falsa
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")


# Exemplo 3: Estrutura IF-ELIF-ELSE
# Permite verificar múltiplas condições em sequência
# O ELIF só é verificado se o IF for falso
# O ELSE só é executado se todas as condições anteriores forem falsas
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")

# Função com retorno: recebe uma coleção de números e calcula a soma deles.


# O parâmetro numeros é uma lista (ou outro iterável aceito por sum()).
# sum() soma os valores do iterável e return envia o resultado de volta
def calcular_total(numeros):
    return sum(numeros)


# Função que calcula dois valores. O antecessor é o número imediatamente anterior.
# O sucessor é o número imediatamente posterior.
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    # Ao separar os valores por vírgula, Python os retorna em uma tupla.
    return antecessor, sucessor


# Chama a função com uma lista e exibe o valor retornado por ela.
print(calcular_total([10, 20, 34]))  # 64
# Saída: 64

# Chama a função com 10 e exibe a tupla com antecessor e sucessor.
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
# Saída: (9, 11)

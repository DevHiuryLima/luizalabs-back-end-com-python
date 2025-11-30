# Método in em dicionários


# Declarando um dicionário aninhado para armazenar vários contatos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}


# O operador in verifica se uma chave existe no dicionário.
# Retorna True se a chave existir; caso contrário, retorna False.
resultado = "guilherme@gmail.com" in contatos
print(resultado)
# Saída: True


# Verificando uma chave que não existe
resultado = "megui@gmail.com" in contatos
print(resultado)
# Saída: False


# Verificando chaves dentro dos dicionários aninhados
resultado = "idade" in contatos["guilherme@gmail.com"]
print(resultado)
# Saída: False


# Verificando uma chave existente dentro do dicionário aninhado
resultado = "telefone" in contatos["giovanna@gmail.com"]
print(resultado)
# Saída: True

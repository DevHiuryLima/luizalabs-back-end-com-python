# Método fromkeys() em dicionários


# fromkeys() cria um novo dicionário a partir de uma lista de chaves, todas com o mesmo valor inicial (padrão é None).
# Retorna um novo dicionário sem modificar o original.
resultado = dict.fromkeys(["nome", "telefone"])
print(resultado)
# Saída: {'nome': None, 'telefone': None}


# Definindo um valor padrão diferente de None
resultado = dict.fromkeys(["nome", "telefone"], "vazio")
print(resultado)
# Saída: {'nome': 'vazio', 'telefone': 'vazio'}

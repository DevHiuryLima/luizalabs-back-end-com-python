# Método popitem() em dicionários


# Declarando um dicionário aninhado para armazenar um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


# O método popitem() remove e retorna um par chave-valor arbitrário do dicionário.
# Não é possível especificar qual item será removido.
# Se o dicionário estiver vazio, gera um KeyError.
resultado = contatos.popitem()
print(resultado)
# Sáida: ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})


# Tentando remover um item de um dicionário vazio vai gerar um KeyError
# contatos.popitem()
# Saída: KeyError

# Método pop() em dicionários


# Declarando um dicionário aninhado para armazenar um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


# O método pop() remove o par chave-valor associado à chave especificada e retorna o valor removido.
# Se a chave não existir, retorna um valor padrão se fornecido; caso contrário, gera um KeyError.
resultado = contatos.pop("guilherme@gmail.com")
print(resultado)
# Saída: {'nome': 'Guilherme', 'telefone': '3333-2221'}


# Tentando remover uma chave inexistente sem valor padrão
# Como a chave não existe mais, isso poeria gerar um KeyError. 
# Mas aqui usamos o valor padrão para evitar o erro.
resultado = contatos.pop("guilherme@gmail.com", {})
print(resultado)
# Saída: {}

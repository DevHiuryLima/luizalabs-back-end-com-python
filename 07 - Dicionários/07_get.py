# Método get() em dicionários


# Declarando um dicionário aninhado para armazenar um contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


# O método get() acessa o valor associado a uma chave, retornando None ou um valor padrão se a chave não existir.
# Evita o erro KeyError que ocorre ao acessar uma chave inexistente diretamente.
# Exemplo:
# contatos["chave"]
# Saída: KeyError


# Usando get() para acessar chaves, caso a chave não exista retorna None sem gerar erro
resultado = contatos.get("chave")
print(resultado)
# Saída: None


# Usando get() com valor padrão para chave caso não exista
resultado = contatos.get("chave", {})
print(resultado)
# Saída: {}


# Usando get() para acessar uma chave existente
resultado = contatos.get(
    "guilherme@gmail.com", {}
)
print(resultado)
# Saída: {'nome': 'Guilherme', 'telefone': '3333-2221'}

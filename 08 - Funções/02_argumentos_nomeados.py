# Argumentos Nomeados em Funções
# Argumentos nomeados permitem passar valores para parâmetros de uma função usando o nome do parâmetro


# Define uma função com quatro parâmetros obrigatórios para receber os dados do carro.
# A mensagem simula uma confirmação; nenhum banco de dados é usado.
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# Argumentos posicionais: cada valor é associado ao parâmetro pela ordem em que aparece.
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# Saída: Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234

# Argumentos nomeados: cada valor é associado explicitamente pelo nome do parâmetro.
# A ordem pode ser alterada quando todos os argumentos são nomeados.
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# Saída: Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234

# O operador ** desempacota o dicionário em argumentos nomeados.
# Para funcionar, as chaves devem corresponder aos nomes dos parâmetros da função.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
# Saída: Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234

# Função que combina parâmetros somente posicionais e somente nomeados.
# Os parâmetros antes de / só aceitam argumentos posicionais.
# Os parâmetros depois de * só aceitam argumentos nomeados.


def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    # Exibe os valores recebidos na ordem indicada.
    print(modelo, ano, placa, marca, motor, combustivel)


# Chamada válida: os três primeiros valores são posicionais e os demais nomeados.
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# Saída da chamada válida: Palio 1999 ABC-1234 Fiat 1.0 Gasolina

# Chamada inválida: modelo, ano e placa estão antes de /, portanto não podem
# ser informados por nome. Ao executar, Python levanta TypeError.
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Funções com parâmetros somente por posição
# Parâmetros declarados antes da barra (/) só podem receber argumentos posicionais.
# Parâmetros declarados depois da barra podem receber argumentos posicionais ou nomeados.


# modelo, ano e placa são somente posicionais por estarem antes da barra.
# marca, motor e combustivel também podem ser passados pelo nome.
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    # Exibe os valores recebidos, na ordem indicada.
    print(modelo, ano, placa, marca, motor, combustivel)


# Argumentos posicionais são associados aos parâmetros pela ordem.
# Os parâmetros após / são passados como argumentos nomeados.
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# Saída: Palio 1999 ABC-1234 Fiat 1.0 Gasolina

# Esta chamada é inválida: modelo, ano e placa estão antes de / e não podem
# ser fornecidos com seus nomes. Ao executá-la, Python levanta TypeError.
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

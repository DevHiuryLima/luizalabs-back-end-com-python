conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450


# Estrutura condicional principal - verifica o tipo de conta
if conta_normal:

    # Se for conta normal, temos 3 possibilidades:
    if saldo >= saque: # 1. Saldo suficiente para o saque
        print("Saque realizado com sucesso!")

    elif saque <= (saldo + cheque_especial): # 2. Saldo + cheque especial suficiente
        print("Saque realizado com uso do cheque especial!")

    else: # 3. Nem saldo nem cheque especial são suficientes
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria: # Se for conta universitária, só verifica o saldo

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial: # Se for conta especial, apenas confirma o tipo
    print("Conta especial selecionada!")

else: # Se nenhum tipo de conta foi reconhecido
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")

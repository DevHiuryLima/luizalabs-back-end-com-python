opcao = -1


# Estrutura while: repete um bloco enquanto a condição for True
while opcao != 0: # Enquanto a opção for diferente de 0, o loop continua executando
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

# O bloco else do while é executado quando o loop termina normalmente
# (ou seja, quando a condição do while ficou False). NÃO é executado se o loop
# for interrompido por um break.
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

# Loop infinito controlado por condições internas
# while True cria um laço que só termina quando encontra um break
while True:
    # Lê um número do usuário
    numero = int(input("Informe um número: "))

    # Se o usuário digitar 10, saímos do while sem executar mais nada.
    # pois o break interrompe o loop imediatamente.
    if numero == 10:
        break

    # Se o número for par (resto 0), não queremos imprimir; pulamos direto para a próxima entrada.
    # o 'continue' pula para a próxima iteração do loop sem executar o código que vem depois.
    if numero % 2 == 0:
        continue

    # Este print só é alcançado para números ímpares diferentes de 10
    print(numero)

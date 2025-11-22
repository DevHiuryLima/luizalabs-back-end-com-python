# Exemplos simples de operadores lógicos
# AND (e) -> só é True se todos os operandos forem True
# OR  (ou) -> é True se pelo menos um operando for True
print(True and True and True)    # True  (todos True)
print(True and False and True)   # False (existe um False)
print(False and False and False)  # False (todos False)

print(True or True or True)      # True  (pelo menos um True)
print(True or False or False)    # True  (existe um True)
print(False or False or False)   # False (nenhum True)

# Exemplo prático: saque bancário
saldo = 1000          # saldo na conta
saque = 250           # valor que queremos sacar
limite = 200          # limite da conta normal
conta_especial = True # indica se a conta tem cheque especial

# Sem parênteses explícitos — atenção à precedência:
# em Python, "and" tem prioridade sobre "or".
# A expressão é avaliada como:
# (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)  # True — porque, mesmo que saque > limite, conta_especial permite (e saldo é suficiente)

# Mesma expressão com parênteses para deixar a intenção clara.
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)  # True (idêntico a exp, mas mais legível)

# Quebramos a lógica em variáveis booleanas com nomes descritivos
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

# União das duas condições — se qualquer uma for True, o saque é permitido
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)  # True

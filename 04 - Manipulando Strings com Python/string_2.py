# Definindo variáveis com diferentes tipos de dados
nome = "Hiury"
idade = 25
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435


# Definindo um dicionário com dados
dados = {"nome": "Hiury", "idade": 25}


# ===== MÉTODO 1: Formatação com operador % (Estilo antigo) =====
# %s = substitui por string
# %d = substitui por inteiro
print("Nome: %s Idade: %d" % (nome, idade))
# Saída: Nome: Hiury Idade: 25


# ===== MÉTODO 2: Formatação com .format() (Estilo intermediário) =====
# {} = placeholder (posição genérica)
print("Nome: {} Idade: {}".format(nome, idade))
# Saída: Nome: Hiury Idade: 25


# Usando índices numéricos para reordenar os argumentos
# {1} = segundo argumento (nome)
# {0} = primeiro argumento (idade)
print("Nome: {1} Idade: {0}".format(idade, nome))
# Saída: Nome: Hiury Idade: 25


# Reutilizando o mesmo argumento múltiplas vezes
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
# Saída: Nome: Hiury Idade: 25 Nome: Hiury Hiury


# Usando nomes descritivos (argumentos nomeados)
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
# Saída: Nome: Hiury Idade: 25


# Usando nomes diferentes dos parâmetros originais
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
# Saída: Nome: Hiury Idade: 25 Hiury Hiury 25


# Desempacotando um dicionário com ** para usar suas chaves como argumentos nomeados
print("Nome: {nome} Idade: {idade}".format(**dados))
# Saída: Nome: Hiury Idade: 25


# ===== MÉTODO 3: Formatação com f-strings (Estilo moderno - Python 3.6+) =====
# f"..." = f-string (a forma mais legível e recomendada atualmente)
# Permite inserir variáveis diretamente entre chaves
print(f"Nome: {nome} Idade: {idade}")
# Saída: Nome: Hiury Idade: 25


# Formatando números com casas decimais
# {saldo:.2f} = exibe saldo com 2 casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
# Saída: Nome: Hiury Idade: 25 Saldo: 45.43

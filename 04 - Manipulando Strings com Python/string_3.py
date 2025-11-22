# Variável com o nome completo
nome = "Hiury Lima Oliveira"


# Acessando caracteres por índice:
# nome[0] -> primeiro caractere (índice inicia em 0)
print(nome[0])   # 'H'


# Índices negativos contam a partir do final:
# nome[-2] -> penúltimo caractere da string
print(nome[-2])  # 'r' ("Oliveira")


# Slices (fatiamento): nome[início:fim]
# Pega caracteres do início (0) até o índice 9
print(nome[:9])  # 'Hiury Lim'  (até o caractere no índice 9)


# Pega a partir do índice 11 até o final
print(nome[10:]) # ' Oliveira'  (depois do índice 10 até o fim)


# Pega do índice 11 (inclusivo) até o 16 (16 é incluído)
print(nome[10:16])  # ' Olive' 


# Slice com passo: nome[início:fim:passo]
# Aqui pega do 11 ao 16, pulando 2 em 2 caracteres
print(nome[10:16:2])  # seleciona cada 2º caractere: 'lv'


# nome[:] copia a string inteira (início/fim padrão)
print(nome[:])   # 'Hiury Lima Oliveira' (cópia completa)


# Revertendo a string com slice: passo negativo
# nome[::-1] -> começa no fim, vai até o início, passo -1 (inverte)
print(nome[::-1])  # 'arievelO amiL yriuH'


# Observação:
# - Slices vai incluir o espaço em branco se estiver dentro do intervalo.

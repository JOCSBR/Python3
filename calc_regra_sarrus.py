# Calculo de matriz de ordem 3 (3 linhas vs 3 colunas)
# Regra de Sarrus
# Jose Carlos - 24/10/2019

# apresentacao do cenario de teste
print('Para validar o calculo insira os dados abaixo e o resultado sera -59')
print('         ','Col 1','Col 2','Col 3')
print('Linha 1  ','5    ','0    ','1')
print('Linha 2  ','-2   ','3    ','4')
print('Linha 3  ','0    ','2    ','-1')
print('\n')

# definicao das variaveis
matriz = {}
lista = []
linha = 0
coluna = 0

# preenchimento da matriz
while linha < 3:
    linha += 1
    coluna = 1
    for coluna in range(1,4):
        valor = int(input('Linha: '+str(linha)+' - Insira o valor da coluna '+str(coluna)+' (somente inteiros): '))
        lista.append(valor)
    matriz[linha] = lista
    lista = []

# representacao como determinante (insere copia das 2 primeiras colunas)
linha = 0
coluna = 0
while linha < 3:
    linha += 1
    for i in matriz[linha]:
        coluna += 1
        matriz[linha].append(i)
        if coluna == 2:
            coluna = 0
            break

# calculo do produto da diagonal principal vs diagonal secundária
linha = 0
coluna = 0
DP1 = 0
for i in matriz:
    c = matriz[i]
    if i == 1:
        DP1 = c[0] * 1
        DP2 = c[1] * 1
        DP3 = c[2] * 1 
        DS1 = c[2] * 1
        DS2 = c[3] * 1
        DS3 = c[4] * 1
    if i == 2:
        DP1 = c[1] * DP1
        DP2 = c[2] * DP2
        DP3 = c[3] * DP3
        DS1 = c[1] * DS1
        DS2 = c[2] * DS2
        DS3 = c[3] * DS3
    if i == 3:
        DP1 = c[2] * DP1
        DP2 = c[3] * DP2
        DP3 = c[4] * DP3
        DS1 = c[0] * DS1
        DS2 = c[1] * DS2
        DS3 = c[2] * DS3

# inversao do sinal do produto das secundarias
DS1 = DS1 * -1
DS2 = DS2 * -1
DS3 = DS3 * -1

# calculo do resultado
r = DS1 + DS2 + DS3 + DP1 + DP2 + DP3
print('\n')
print('Matriz de ordem 3 com os valores:', DS1, DS2, DS3, DP1, DP2, DP3, 'resulta em:', r)
print('\n')
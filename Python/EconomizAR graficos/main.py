import matplotlib.pyplot as plt
# Lê todas as linhas e armazena em uma lista na qual cada linha compõe uma string
with open("EconomizAR projeto ligado.txt", 'r') as arquivo:
    dados = arquivo.readlines()
    # Remove os \n de cada linha
    for i in range(len(dados)):
        dados[i] = dados[i].replace("\n", "")

datas = []
watts = []
# Divide a string em substrings para uma manipulação mais fácil
for i in range(len(dados)):
    dia = dados[i].split(",")
    datas.append(dia[0])
    watts.append(float(dia[3]))

print(sum(watts)/len(watts))
WATTS1 = []
DATAS1 = []

# Pega a primeira posição da lista e remove todas as ocorrências de mesmo valor, salvando os valores correspondentes em
# Watts em uma lista separada para futura manipulação
while len(datas) > 0:
    dataAtual = datas[0]
    Watual = []
    while dataAtual in datas:
        posicao = datas.index(dataAtual)
        Watual.append(watts[posicao])

        watts.pop(posicao)
        datas.pop(posicao)

# Salva os valores em uma lista principal
    WATTS1.append(sum(Watual) / len(Watual))
    DATAS1.append(dataAtual)

# Cria o gráfico com os dados manipulados

# Lê todas as linhas e armazena em uma lista na qual cada linha compõe uma string
with open("EconomizAR projeto desligado.txt", 'r') as arquivo:
    dados = arquivo.readlines()
    # Remove os \n de cada linha
    for i in range(len(dados)):
        dados[i] = dados[i].replace("\n", "")

datas = []
watts = []
# Divide a string em substrings para uma manipulação mais fácil
for i in range(len(dados)):
    dia = dados[i].split(",")
    datas.append(dia[0])
    watts.append(float(dia[3]))
print(sum(watts)/len(watts))
WATTS = []
DATAS = []

# Pega a primeira posição da lista e remove todas as ocorrências de mesmo valor, salvando os valores correspondentes em
# Watts em uma lista separada para futura manipulação
while len(datas) > 0:
    dataAtual = datas[0]
    Watual = []
    while dataAtual in datas:
        posicao = datas.index(dataAtual)
        Watual.append(watts[posicao])

        watts.pop(posicao)
        datas.pop(posicao)

    # Salva os valores em uma lista principal
    WATTS.append(sum(Watual) / len(Watual))
    DATAS.append(dataAtual)

# Cria o gráfico com os dados manipulados
plt.plot(DATAS1, WATTS1)
plt.ylim(1500, 5000)
plt.show()



import matplotlib.pyplot as plt
def novo():


    with open("EconomizAR projeto ligado.txt", 'r') as arquivo:
        dados = arquivo.readlines()
        # Remove os \n de cada linha
        for i in range(len(dados)):
            dados[i] = dados[i].replace("\n", "")

    datas = []
    watts = []
    for i in range(len(dados)):
        dia = dados[i].split(",")
        datas.append(dia[0])
        watts.append(float(dia[3]))

    WATTS = []
    DATAS = []

    inicio = False
    while len(datas) > 0:
        dataAtual = datas[0]
        Watual = []
        while dataAtual in datas:
            posicao = datas.index(dataAtual)
            Watual.append(watts[posicao])

            watts.pop(posicao)
            datas.pop(posicao)

        WATTS.append(sum(Watual) / len(Watual))
        DATAS.append(dataAtual)

    print(DATAS)
    print(WATTS)
    print("###############")
    print(datas, watts)

    plt.plot(DATAS, WATTS)
    plt.ylim(1500, 5000)
    plt.show()

def velho():

    with open("EcomizAR Projeto desligado.txt", 'r') as arquivo:
        dados = arquivo.readlines()
        # Remove os \n de cada linha
        for i in range(len(dados)):
            dados[i] = dados[i].replace("\n", "")

    datas = []
    watts = []
    for i in range(len(dados)):
        dia = dados[i].split(",")
        datas.append(dia[0])
        watts.append(float(dia[3]))

    WATTS = []
    DATAS = []

    inicio = False
    while len(datas) > 0:
        dataAtual = datas[0]
        Watual = []
        while dataAtual in datas:
            posicao = datas.index(dataAtual)
            Watual.append(watts[posicao])

            watts.pop(posicao)
            datas.pop(posicao)

        WATTS.append(sum(Watual) / len(Watual))
        DATAS.append(dataAtual)

    print(DATAS)
    print(WATTS)
    print("###############")
    print(datas, watts)

    plt.plot(DATAS, WATTS)
    plt.ylim(1500, 5000)
    plt.show()
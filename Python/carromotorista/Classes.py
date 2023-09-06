class carro:
    def __init__(self,cor,modelo,marca,ano):
        self.__cor = cor
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__velocidade = 0

    def setCor(self, cor):
        self.__cor = cor
    def getCor(self):
        return self.__cor
    cor = property(getCor, setCor)

    def setModelo(self, modelo):
        self.__modelo = modelo
    def getModelo(self):
        return self.__modelo
    modelo = property(getModelo, setModelo)

    def setMarca(self, marca):
        self.__marca = marca
    def getMarca(self):
        return self.__marca
    marca = property(getMarca, setMarca)

    def setAno(self, ano):
        self.__ano = ano
    def getAno(self):
        return self.__ano
    ano = property(getAno, setAno)

    def setVelocidade(self, velocidade):
        self.__velocidade = velocidade
    def getVelocidade(self):
        return self.__velocidade
    velocidade = property(getVelocidade, setVelocidade)

    ### Métodos ###
    def Acelerar(self):
        acelerar = float(input("Quantos Km/h você deseja acelerar?"))
        velocidadet = self.getVelocidade() + acelerar
        self.setVelocidade(velocidadet)
        return velocidadet
    def Ligar(self):
        print("O carro ligou")

    def Freiar(self):
        acelerar = float(input("Quantos Km/h você deseja freiar?"))
        velocidadet = self.getVelocidade() - acelerar
        self.setVelocidade(velocidadet)
        return velocidadet

class motorista:
    def __init__(self,nome, RG, CPF, CNH,Carro):
        self.__nome= nome
        self.__RG =RG
        self.__CPF=CPF
        self.__CNH=CNH
        self.__Carro = Carro

    def setRg(self, RG):
        self.__RG = RG
    def getRg(self):
        return self.__RG
    RG = property(getRg, setRg)

    def setCpf(self, CPF):
        self.__CPF = CPF
    def getCpf(self):
        return self.__CPF
    CPF = property(getCpf, setCpf)

    def setCnh(self, CNH):
        self.__CNH = CNH
    def getCnh(self):
        return self.__CNH
    CNH = property(getCnh, setCnh)

    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    nome = property(getNome, setNome)

    def getCarro(self):
        return self.__Carro
    def setCarro(self,Carro):
        self.__Carro = Carro
    Carro = property(getCarro,setCarro)


    ### Métodos ###
    def dirigir(self):
        print("Velocidade do carro: {} ".format(self.getCarro().getVelocidade()))
        acao = int(input("Oque deseja fazer?\n "
              "1-Ligar 2- Acelerar 3- Freiar"))
        if acao == 1:
            V = self.getCarro().Ligar()
        elif acao == 2:
            V = self.getCarro().Acelerar()
            self.CalcMulta(V)
        elif acao == 3:
            V = self.getCarro().Freiar()
            self.CalcMulta(V)
    def CalcMulta(self,V):
        if V >= 120.0:
            print("Motorista multado no valor de 200R$")
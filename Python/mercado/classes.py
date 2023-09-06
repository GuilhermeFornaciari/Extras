### Classes ###

from datetime import *

class Pessoa:

    def __init__(self,nome,datanasc,nacio,altura,peso):
        self.__nome = nome
        self.__datanasc = datanasc
        self.__nacio = nacio
        self.__altura = altura
        self.__peso = peso

    def getnome(self):
        return self.__nome
    def setnome(self,nome):
        self.__nome = nome

    def getdatanasc(self):
        return self.__datanasc
    def setdatanasc(self,datanasc):
        self.__datanasc = datanasc

    def getnacio(self):
        return self.__nacio
    def setnacio(self,nacio):
        self.__nacio = nacio

    def getaltura(self):
        return self.__altura
    def setaltura(self,altura):
        self.__altura = altura

    def getpeso(self):
        return self.__peso
    def setpeso(self,peso):
        self.__peso = peso

    nome = property(getnome,setnome)
    datanasc = property(getdatanasc,setdatanasc)
    nacio = property(getnacio,setnacio)
    altura = property(getaltura,setaltura)
    peso = property(getpeso,setpeso)


class JogadorFutebol(Pessoa):
    def __init__(self,nome,datanasc,nacio,altura,peso,posicao):
        super().__init__(nome,datanasc,nacio,altura,peso)
        self.__posicao = posicao

    def getposicao(self):
        return self.__posicao
    def setposicao(self,posicao):
        self.__posicao = posicao
    posicao = property(getposicao,setposicao)
    ### Métodos ###
    def printtudo(self):
        print("Nome: {} \n"
              "Data de nascimento: {} \n"
              "Nacionalidade: {} \n"
              "Altura: {} \n"
              "Peso: {} \n"
              "Posição: {} \n"
              .format(self.getnome(),self.getdatanasc(),self.getnacio(),self.getaltura(),self.getpeso(),self.getposicao())
              )
    def idade_atual(self):
        idade = date.today() - self.getdatanasc()
        return idade


    def restante_para_aposentar(self):
        tempo = 0
        if self.getposicao() == "Defesa":
            tempo = timedelta(days=14610)  # 40 * 365.25 = 14610
        elif self.getposicao() == "Meio-Campo":
            tempo = timedelta(days=13879.5)  # 38 * 365.25 = 13879.5
        elif self.getposicao() == "Atacante":
            tempo = timedelta(days= 12783.75) #35 * 365.25 = 12783.75
        print(tempo)
        aposentar = (tempo -self.idade_atual())
        return aposentar // timedelta(365.25) + 1

class Uniforme:
    def __init__(self,Cor_Calcao,Cor_Camisa,Cor_Meiao,Numero,Jogador):
        self.__Cor_Calcao = Cor_Calcao
        self.__Cor_Camisa = Cor_Camisa
        self.__Cor_Meiao = Cor_Meiao
        self.__Numero = Numero
        self.__Jogador = Jogador

    def getCor_Calcao(self):
        return self.__Cor_Calcao
    def setCor_Calcao(self, Cor_Calcao):
        self.__Cor_Calcao = Cor_Calcao

    def getCor_Camisa(self):
        return self.__Cor_Camisa
    def setCor_Camisa(self, Cor_Camisa ):
        self.__Cor_Camisa = Cor_Camisa

    def getCor_Meiao(self):
        return self.__Cor_Meiao
    def setCor_Meiao(self, Cor_Meiao ):
        self.__Cor_Meiao = Cor_Meiao

    def getNumero(self):
        return self.__Numero
    def setNumero(self, Numero):
        self.__Numero = Numero

    Cor_Calcao = property(getCor_Calcao,setCor_Calcao)
    Cor_Camisa = property(getCor_Camisa,setCor_Camisa)
    Cor_Meiao  = property(getCor_Meiao,setCor_Meiao)
    Numero     = property(getNumero,setNumero)

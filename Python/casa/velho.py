from imovel import *
class Velho(Imovel):
    def __init__(self,areaTotal,nComodos,tipoImovel,endereco,valor,valorAdicional):
        super().__init__(areaTotal,nComodos,tipoImovel,endereco,valor)
        self.__valorAdicional = valorAdicional

    def setValoradicional(self, valorAdicional):
        self.__valorAdicional = valorAdicional
    def getValoradicional(self):
        return self.__valorAdicional
    valorAdicional = property(getValoradicional, setValoradicional)

    ### MÉTODOS ###

    def printValores(self):
        print("Valor da casa:   {} \n"
              "Valor descontado: {} \n"
              "Valor Total:     {}".format(self.getValor(),self.getValoradicional(),self.getValor() - self.getValoradicional()))
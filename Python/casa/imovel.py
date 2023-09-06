class Imovel:
    def __init__(self,areaTotal,nComodos,tipoImovel,endereco,valor):
        self.__areaTotal = areaTotal
        self.__nComodos = nComodos
        self.__tipoImovel = tipoImovel
        self.__endereco = endereco
        self.__valor = valor


    def setAreatotal(self, areaTotal):
        self.__areaTotal = areaTotal
    def getAreatotal(self):
        return self.__areaTotal
    areaTotal = property(getAreatotal, setAreatotal)


    def setNcomodos(self, nComodos):
        self.__nComodos = nComodos
    def getNcomodos(self):
        return self.__nComodos
    nComodos = property(getNcomodos, setNcomodos)


    def setTipoimovel(self, tipoImovel):
        self.__tipoImovel = tipoImovel
    def getTipoimovel(self):
        return self.__tipoImovel
    tipoImovel = property(getTipoimovel, setTipoimovel)


    def setEndereco(self, endereco):
        self.__endereco = endereco
    def getEndereco(self):
        return self.__endereco
    endereco = property(getEndereco, setEndereco)


    def setValor(self, valor):
        self.__valor = valor
    def getValor(self):
        return self.__valor
    valor = property(getValor, setValor)




class Endereco:
    def __init__(self,cidade,bairro,rua,cep):
        self.__rua = rua
        self.__cep = cep
        self.__bairro = bairro
        self.__cidade = cidade

    def setRua(self, rua):
        self.__rua = rua
    def getRua(self):
        return self.__rua

    def setCep(self, cep):
        self.__cep = cep
    def getCep(self):
        return self.__cep

    def setBairro(self, bairro):
        self.__bairro = bairro
    def getBairro(self):
        return self.__bairro

    def setCidade(self, cidade):
        self.__cidade = cidade
    def getCidade(self):
        return self.__cidade

    cidade = property(getCidade, setCidade)
    rua = property(getRua, setRua)
    cep = property(getCep, setCep)
    bairro = property(getBairro, setBairro)

    def retornastring(self):
        string = "Cidade: {} ; Bairro: {} ; Rua: {} ; CEP: {} ".format(self.getCidade(),self.getBairro(),self.getRua(),self.getCep())
        return string
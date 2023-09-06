class zoologico:
    def __init__(self):
        self.__animais = []

    def getAnimais(self):
        return self.__animais
    def setAnimais(self, animais):
        for i in animais:
            self.appendAnimais(i)
    def appendAnimais(self,novos):
        self.getAnimais().append(novos)
    property(getAnimais,setAnimais)

    def mostrar(self):
        cont = 1
        for i in self.getAnimais():
            print("Jaula {} : ".format(cont))
            print("".format(i.som_que_emite()))
            cont += 1
class animal:
    def __init__(self, idade, sexo, cor, peso, alimentacao, habitat):
        self.__idade = idade
        self.__sexo = sexo
        self.__cor = cor
        self.__peso = peso
        self.__alimentacao = alimentacao
        self.__habitat = habitat

    def setIdade(self, idade):
        self.__idade = idade
    def getIdade(self):
        return self.__idade
    idade = property(getIdade, setIdade)


    def setSexo(self, sexo):
        self.__sexo = sexo
    def getSexo(self):
        return self.__sexo
    sexo = property(getSexo, setSexo)


    def setCor(self, cor):
        self.__cor = cor
    def getCor(self):
        return self.__cor
    cor = property(getCor, setCor)


    def setPeso(self, peso):
        self.__peso = peso
    def getPeso(self):
        return self.__peso
    peso = property(getPeso, setPeso)


    def setAlimentacao(self, alimentacao):
        self.__alimentacao = alimentacao
    def getAlimentacao(self):
        return self.__alimentacao
    alimentacao = property(getAlimentacao, setAlimentacao)


    def setHabitat(self, habitat):
        self.__habitat = habitat
    def getHabitat(self):
        return self.__habitat
    habitat = property(getHabitat, setHabitat)

    def locomocao(self):
        print("andou 3 passos")
    def som_que_emite(self):
        print("muahaaha")

class cachorro(animal):
    def __init__(self,idade, sexo, cor, peso, alimentacao, habitat,raca,tamanho,adestrado):
        super().__init__(idade, sexo, cor, peso, alimentacao, habitat)
        self.__raca = raca
        self.__tamanho = tamanho
        self.__adestrado = adestrado

    def setRaca(self, raca):
        self.__raca = raca
    def getRaca(self):
        return self.__raca
    raca = property(getRaca, setRaca)


    def setTamanho(self, tamanho):
        self.__tamanho = tamanho
    def getTamanho(self):
        return self.__tamanho
    tamanho = property(getTamanho, setTamanho)


    def setAdestrado(self, adestrado):
        self.__adestrado = adestrado
    def getAdestrado(self):
        return self.__adestrado
    adestrado = property(getAdestrado, setAdestrado)

    def locomocao(self):
        print("Corri 3 passos")
    def som_que_emite(self):
        print("Au Au Au")

class Cavalo(animal):
    def __init__(self,idade, sexo, cor, peso, alimentacao, habitat,raca,competicao):
        super().__init__(idade, sexo, cor, peso, alimentacao, habitat)
        self.__raca = raca
        self.__competicao = competicao

    def setRaca(self, raca):
        self.__raca = raca
    def getRaca(self):
        return self.__raca
    raca = property(getRaca, setRaca)

    def setCompeticao(self, competicao):
        self.__competicao = competicao
    def getCompeticao(self):
        return self.__competicao
    competicao = property(getCompeticao, setCompeticao)

    def locomocao(self):
        print("Galopei")
    def som_que_emite(self):
        print("Hiin in in")

class Preguica(animal):
    def __init__(self,idade, sexo, cor, peso, alimentacao, habitat):
        super().__init__(idade, sexo, cor, peso, alimentacao, habitat)
    ### Métodos ###

    def locomocao(self):
        print("escalei")
    def som_que_emite(self):
        print("IIIIIIIII")

class veterinario:
    def __init__(self,CRMV,nome):
        self.__CRMV = CRMV
        self.__nome = nome

    def setCrmv(self, CRMV):
        self.__CRMV = CRMV
    def getCrmv(self):
        return self.__CRMV
    CRMV = property(getCrmv, setCrmv)


    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    nome = property(getNome, setNome)
    ### Métodos ###
    def examinar(self,animal):
        animal.som_que_emite()
        print("Animal examinado")
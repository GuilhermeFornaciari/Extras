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
    def muda_endereco(self,nome):
        print(self.retornastring())
        opcao = int(input("Oque você deseja alterar?"))
        if opcao == 1:
            X = input("Qual é o nome da cidade em que o {} mora? \n".format(nome))
            self.setCidade(X)

        if opcao <= 2:
            X = input("Qual é o nome do bairro em que o {} mora? \n".format(nome))
            self.setBairro(X)
        if opcao <= 3:
            X = input("Qual é o nome da rua em que o {} mora? \n".format(nome))
            self.setRua(X)
        if opcao <= 4:
            X = input("Qual é o CEP em que o {} mora? \n".format(nome))
            self.setCep(X)

class datanasc:
    def __init__(self,dia,mes,ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def setDia(self, dia):
        self.__dia = dia
    def getDia(self):
        return self.__dia

    def setMes(self, mes):
        self.__mes = mes
    def getMes(self):
        return self.__mes

    def setAno(self, ano):
        self.__ano = ano
    def getAno(self):
        return self.__ano

    ano = property(getAno, setAno)
    mes = property(getMes, setMes)
    dia = property(getDia, setDia)

    ### MÉTODOS ###
    def retornastring(self):
        string = str(self.getDia()) +"/"+ str(self.getMes()) +"/"+ str(self.getAno())
        return string

    def muda_data(self,Nome):
        print(self.retornastring())
        X = int(input("Qual é o dia em que o {} nasceu? \n".format(Nome)))
        self.setDia(X)
        X = int(input("Qual é o mês em que o {} nasceu? \n".format(Nome)))
        self.setMes(X)
        X = int(input("Qual é o ano em que o {} nasceu? \n".format(Nome)))
        self.setAno(X)


class contato:
    def __init__(self,nome,nascimento,email,telefone,endereco):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco

    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome

    def setNascimento(self, nascimento):
        self.__nascimento = nascimento
    def getNascimento(self):
        return self.__nascimento

    def setEmail(self, email):
        self.__email = email
    def getEmail(self):
        return self.__email

    def setTelefone(self, telefone):
        self.__telefone = telefone
    def getTelefone(self):
        return self.__telefone

    def setEndereco(self, endereco):
        self.__endereco = endereco
    def getEndereco(self):
        return self.__endereco

    endereco = property(getEndereco, setEndereco)
    telefone = property(getTelefone, setTelefone)
    email = property(getEmail, setEmail)
    nascimento = property(getNascimento, setNascimento)
    nome = property(getNome, setNome)
    ### MÉTODOS ###

    def Print_Tudo(self):
        nasc = self.getNascimento()
        print("1-Nome: {}\n"
              "2-Nascimento: {}\n"
              "3-Email: {}\n"
              "4-Telefone {}\n"
              "5-Endereco: {}\n"
              .format(self.getNome(),self.getNascimento().retornastring(),
                      self.getEmail(),self.getTelefone(),self.getEndereco().retornastring()))

    def mudar_Atributo(self):
        print("\n")
        self.Print_Tudo()
        opcao =int(input("Selecione uma opção para alterar: \n"
                         "Caso deseje cancelar, digite um numero não citado."))
        if opcao == 1:
            X = input("Qual é o nome para qual você deseja alterar?")
            self.setNome(X)
        if opcao == 2:
            self.getNascimento().muda_data(self.getNome())
        if opcao == 3:
            X = input("Digite o novo Email: ")
            self.setEndereco(X)
        if opcao == 4:
            X = input("Digite o novo numero do telefone: ")
        if opcao == 5:
            self.getEndereco().muda_endereco(self.getNome())

class agenda:
    def __init__(self):
        self.__contatos = {}

    def getcontatos(self):
        return self.__contatos

    def appendcontato(self,contato):
        self.__contatos[contato.getNome()] =  contato
    def deletecontato(self,contato):
        self.__contatos.pop(contato.getNome())

    def printcontatos(self):
        print(self.__contatos)

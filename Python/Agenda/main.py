from Classes import *
End = Endereco("Santa Luzia Doeste","Centro","Vanderlei Dalla Costa",76950000)
Data = datanasc(23,8,2005)
Pessoa = contato("Guilherme",Data,"Fornaciari049@gmail.com",984696665,End)

Age = agenda()
Age.appendcontato(Pessoa)

cont = ""
while cont == "":
    Contato = Age.getcontatos().get(
    input("Qual contato você deseja acessar? \n {} ".format((Age.getcontatos()).keys()))
    )

    opcao = int(input("Oque você deseja fazer neste contato? \n"
                  "1- Atualizar alguma informação dele \n"
                  "2- Exclui-lo \n"
                  "3- Imprimir todos os seus dados\n"))

    if opcao == 1:
        Contato.mudar_Atributo()
    if opcao == 2:
        Age.deletecontato(Contato)
    if opcao == 3:
        Contato.Print_Tudo()
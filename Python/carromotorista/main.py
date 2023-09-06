from Classes import *
C = carro("Azul","HB20","Tesla","2020")
M = motorista("Guilherme", "1551035","70116562277","________",C)
cont = ''
while cont == '':
    M.dirigir()
    cont = input("Deseja continuar? digite qualquer coisa para sair")

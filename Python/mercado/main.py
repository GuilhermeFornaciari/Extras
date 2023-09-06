#### Main ###
from classes import *

Jog = JogadorFutebol("Guilherme de Souza Fornaciari",date(2005,8,23),"Brasileiro",1.75,65.7,"Defesa")
Jog.printtudo()
print("\nIdade atual: {} ".format(Jog.idade_atual()))
print("Tempo para aposentar: {} anos".format(Jog.restante_para_aposentar()))

Uni = Uniforme("Amarelo","Rosa","Preto",42,Jog)
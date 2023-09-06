from classes import *
from Zoologico import *
dog = cachorro(5,"F","Preto",10.0,"Ração","Casa","Buldog","grande",True)
horse = Cavalo(10,"M","Preto",300.0,"Grama","Pasto","Pônei brasileiro","Nacional")
sloth = Preguica(2,"F","Branca",30.0,"Folhas de Arvores","florestas")

print("Cachorro:")
dog.som_que_emite()
dog.locomocao()

print()
print("Cavalo:")
horse.som_que_emite()
horse.locomocao()

print()
print("Preguiça:")
sloth.som_que_emite()
sloth.locomocao()

opcao = int(input("\n Qual animal você deseja examinar? 1 para preguiça, 2 para cachorro, 3 para cavalo "))
if opcao == 1:
    sloth.som_que_emite()
elif opcao == 2:
    dog.som_que_emite()
elif opcao == 3:
    horse.som_que_emite()
print("Animal examinado")

zoo = zoologico()
zoo.setAnimais([sloth,dog,horse,sloth,dog,horse,dog,sloth,dog,horse])
zoo.mostrar()
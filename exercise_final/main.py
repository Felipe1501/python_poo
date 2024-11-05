from exercise_final import *

jogador1 = Jogador("Felipe")
jogador2 = Jogador("Teto")
print(jogador1)
print(jogador2)


soco = Soco()
chute = Chute()
revolver = Revolver()

jogador1.bater(soco, jogador2)
jogador2.bater(chute, jogador1)
jogador1.atirar(revolver, jogador2)
jogador1.atirar(revolver, jogador2)
jogador1.atirar(revolver, jogador2)
jogador1.atirar(revolver, jogador2)
jogador1.atirar(revolver, jogador2)
jogador1.atirar(revolver, jogador2)
jogador1.atirar(revolver, jogador2)

revolver.recarregar()

print(jogador2)

print(jogador2)
print(jogador1)
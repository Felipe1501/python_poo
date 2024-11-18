from fps import *
from armas import *
from golpe import *

if __name__ == '__main__':
    j1 = Jogador()
    print(j1)

    s1 = Soco()
    c1 = Chute()
    f1 = Faca(2)

    for x in range(1, 13):
     print (x)
     f1.agredir(j1)
     print(j1)

    jogador2 = Jogador()
    print (j1)
    print (jogador2)
    r1 = Lanca_Chamas()
    j1.armas.append(r1)
    j1.atirar(j1.armas[0], jogador2)
    print (j1)
    print (jogador2)

    j1.bater(jogador2,arma=j1.armas[0])
    print (j1)
    print (jogador2)
from armas import Arma, Disparavel
from golpe import Golpe
from typing import List

class Jogador:
    energia: float
    armas: List[Arma] = []

    def __init__(self):
        self.energia = 150.0

    def __str__(self):
        return f"Energia {self.energia}"

    def atirar(self, X: Disparavel, CHAR):
        X.disparar(CHAR)

    def bater(self,CHAR, golpe: Golpe = None, arma: Arma = None ):
        if golpe != None and arma == None:
            golpe.golpear(CHAR)
        elif golpe == None and arma != None:
            arma.agredir(CHAR)



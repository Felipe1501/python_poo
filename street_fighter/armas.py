from abc import ABC, abstractmethod
from golpe import Soco


class Arma(ABC):
    destruicao: float

    def __init__(self, X):
        self.destruicao = X

    def agredir(self, CHAR):
        CHAR.energia -= 5

    def __str__(self):
        return f"Destruicao: {self.destruicao}"

class Faca(ABC):
    lamina: int

    def __init__(self, X):
        super().__init__(15)
        self.lamina = 10

    def agredir(self, CHAR):
        if self.lamina > 0:
           self.lamina -= 1
           CHAR.energia -= self.destruicao
        else:
            super().agredir()


class Soco_Ingles(Faca, Soco):
    def agredir(self, CHAR):
        super().agredir(CHAR)
        self.golpear(CHAR)



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

class Faca(Arma):
    lamina: int

    def __init__(self, X):
        super().__init__(15)
        self.lamina = 10

    def agredir(self, CHAR):
        if self.lamina > 0:
           self.lamina -= 1
           CHAR.energia -= self.destruicao
        else:
            super().agredir(CHAR)


class Soco_Ingles(Faca, Soco):
    def agredir(self, CHAR):
        super().agredir(CHAR)
        self.golpear(CHAR)


class Disparavel(ABC):
    @abstractmethod
    def disparar(self, CHAR):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma, Disparavel):
    cartuchos: int

    def __init__(self):
        self.cartuchos = 6
        self.destruicao = 20


    def disparar(self, CHAR):
        if self.cartuchos > 0:
            self.cartuchos -= 1
            CHAR.energia -= self.destruicao

    def recarregar(self):
        self.cartuchos = 6


class Lanca_Chamas(Arma, Disparavel):
    gas: float

    def __init__(self):
        self.destruicao = 30
        self.gas = 100


    def disparar(self, CHAR):
        if self.gas > 0:
            self.gas -= 5.5
            CHAR.energia -= self.destruicao

    def recarregar(self):
        self.gas = 100


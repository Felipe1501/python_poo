from abc import ABC, abstractmethod
from socket import send_fds


class Jogador():
    nome: str
    energia: float

    def __init__(self, nome):
        self.nome = nome
        self.energia = 150.0

    def atirar(self, disparavel, jogador):
        disparavel.disparar(jogador)

    def bater(self, golpe, jogador):
        golpe.golpear(jogador)

    def __str__(self):
        info = f"Jogador {self.nome} tem {self.energia}% de energia"

        return info


class Golpe(ABC):
    @abstractmethod
    def golpear(self, jogador):
        pass

class Soco(Golpe):
    def golpear(self, jogador):
        jogador.energia -= 1

class Chute(Golpe):
    def golpear(self, jogador):
        jogador.energia -= 2


class Arma(ABC):
    destruicao: float

    def __init__(self, destruicao):
        self.destruicao = destruicao

    @abstractmethod
    def agredir(self, jogador):
        pass

    def disparar(self, jogador):
        pass

    def __str__(self):
        info = f"Arma com poder poder de destruição {self.destruicao}"



class Revolver(Arma):

    cartuchos: int

    def __init__(self):
        super().__init__(destruicao=20)
        self.cartuchos = 6

    def disparar(self, jogador):
        if self.cartuchos > 0:
            jogador.energia -= self.destruicao
            self.cartuchos -= 1
            print(f"{jogador.nome} foi atingido por um tiro "
                  f"e perdeu {self.destruicao} de energia! "
                  f"Restam {self.cartuchos} cartuchos.")
        else:
            print("sem municao!!!! recarregue o revolver")

    def agredir(self, jogador):
        print("revolver não pode ser usado para agredir diretamente!!!!")

    def recarregar(self):
        self.cartuchos = 6



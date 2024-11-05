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

    def bater(self, golpe, arma, jogador):
        if isinstance(arma, Arma):
            arma.agredir(jogador)
        elif isinstance(golpe, Golpe):
            golpe.golpear(jogador)

    def municiar(self, disparavel):
        disparavel.recarregar()

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
        print(f"{jogador.nome} foi golpeado com um soco "
              f"e perdeu 1 de energia. "
              f"Energia atual: {jogador.energia}%")

class Chute(Golpe):
    def golpear(self, jogador):
        jogador.energia -= 2
        print(f"{jogador.nome} foi golpeado com um chute "
              f"e perdeu 2 de energia. "
              f"Energia atual: {jogador.energia}%")

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
        print(f"o revolver foi recarregado e tem {self.cartuchos} cartuchos")

class Lanca_Chamas(Arma):
    gas: float

    def __init__(self):
        super().__init__(destruicao=30)
        self.gas = 100.0

    def disparar(self, jogador):
        if self.gas > 0:
            jogador.energia -= self.destruicao
            self.gas -= 5.5
            print(f"{jogador.nome} foi atingido pelo lancha-chamas "
                  f"e perdeu {self.destruicao} de energia! "
                  f"Gás restante: {self.gas}%")
        else:
            print("acabou o gás! agora recarregue o lancha-chamas!!!!!")

    def agredir(self, jogador):
        print("o lancha-chamas não deve ser usado diretamente para agredir!!!")

    def recarregar(self):
        self.gas = 100
        print(f"o lança-chamas foi recarregado e tem {self.gas}% de gás!!")

class Faca(Arma):
    lamina: int
    
    def __init__(self):
        super().__init__(destruicao=15)
        self.lamina = 10


    def disparar(self, jogador):
        print("a faca não pode disparar!!!")


    def agredir(self, jogador):
        if self.lamina > 0:
            jogador.energia -= self.destruicao
            self.lamina -= 1
            print(f"{self.nome} foi cortado por uma faca "
                  f"e perdeu {self.destruicao} de energia!! "
                  f"A lâmina está com {self.lamina} afiação de 10.")
        else:
            print("a lâmina está cega, não é possível agredir usá-la!!!!")

    def recarregar(self):
        print("a faca não precisa ser recarregada")


class Soco_Ingles(Arma, Golpe):
    def __init__(self):
        super().__init__(destruicao=15)

    def golpear(self, jogador):
        jogador.energia -= 1
        print(f"{jogador.nome} foi golpeado com um soco-inglês "
              f"e perdeu 5 de energia. "
              f"Energia atual: {jogador.energia}%")

    def agredir(self, jogador):
        self.golpear(jogador)
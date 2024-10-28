from abc import ABC

class Atleta(ABC):
    nome: str
    idade: int
    peso: float

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso



    def aquecer(self):
        return 'vai correr fi'

    def __str__(self):
        info = (f"nome: {self.nome}\n"
                f"idade: {self.idade}\n"
                f"peso: {self.peso}")

        return info

class Corredor(Atleta):
    def correr(self):
        return 'é o corredor \n'

class Nadador(Atleta):

    def nadar(self):
        return 'nada ai fi \n'

class Ciclista(Atleta):
    def pedalar(self):
        return 'pedala ai fi \n'


class Triatleta(Nadador, Ciclista, Corredor):
    def realizar_maratona(self):
        info = self.nadar()
        info += self.pedalar()
        info += self.correr()

        return info
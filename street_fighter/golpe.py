from abc import ABC, abstractmethod


class Golpe(ABC):
    @abstractmethod
    def golpear(self, CHAR):
        pass

class Soco(Golpe):
    def golpear(self, CHAR):
        CHAR.energia -= 1

class Chute(Golpe):
    def golpear(self, CHAR):
        CHAR.energia -= 2


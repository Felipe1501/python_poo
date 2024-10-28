from atleta import *

if __name__ == "__main__":
    c1 = Corredor('Mbappe', 24, 80.8)
    print(c1)
    print(c1.aquecer())
    print(c1.correr())

    n1 = Nadador('Michael Phelps', 34, 90.8)
    print(n1)
    print(n1.aquecer())
    print(n1.nadar())

    p1 = Ciclista('Pablo', 20, 70.8)
    print(p1)
    print(p1.aquecer())
    print(p1.pedalar())

    triatleta = Triatleta("Vini JR BALLON DOR", 24, 76.4)
    print(triatleta)
    print(triatleta.aquecer())
    print(triatleta.realizar_maratona())
    print((Triatleta.__mro__))
import random

from fight import *

##
# if __name__ == '__main__':
#     cara1 = input("digite o nome do primeiro desafiante.....")
#     op1 = input("digite seu estilo de luta: \n"
#                 "1 - Boxeador \n"
#                 "2 - Muay Thai \n"
#                 "3 - Normalzin \n"
#                 "4 - JiuJitsu \n"
#                 "5 - MMA")
#     if op1 == 1:
#         Boxeador(cara1)
#     elif op1 == 2:
#         Muay_Thai(cara1)
#     elif op1 == 3:
#         Lutador(cara1)
#     elif op1 == 4:
#         Jujitsu(cara1)
#     elif op1 == 5:
#         MMA(cara1)
#     else:
#         print("Opção Errada, tente novamente mais tarde")
#
#
#
#     cara2 = input("digite o nome do segundo desafiante......")
#     op2 = input("digite seu estilo de luta: \n"
#                 "1 - Boxeador \n"
#                 "2 - Muay Thai \n"
#                 "3 - Normalzin \n"
#                 "4 - JiuJitsu \n"
#                 "5 - MMA")
#     if op2 == 1:
#         Boxeador(cara2)
#     elif op2 == 2:
#         Muay_Thai(cara2)
#     elif op1 == 3:
#         Lutador(cara2)
#     elif op1 == 4:
#         Jujitsu(cara2)
#     elif op1 == 5:
#         MMA(cara2)
#     else:
#         print("Opção Errada, tente novamente mais tarde")
#
#
#     print(f"pela ordem de sorteio da máquina, quem começa o combate é o {cara2}")
#     while Lutador.energia > 0:
#         print(cara1)
#         print(cara2)
#
#         if op1 == 1:
#             tipo_golpe = input(f"digite o tipo de golpe que voce quer aplicar: \n"
#                                f"1 - Cruzado \n"
#                                f"2 - Gancho \n")
#             if tipo_golpe == 1:
#                 print(cara2.cruzado(cara1))
#             elif tipo_golpe == 2:
#                 print(cara2.gancho(cara1))
#
# ###

def golpe(cara1: MMA, cara2: MMA):
    golpe = random.randrange(1, 7)
    if golpe == 1:
        cara1.soco(cara2)
    elif golpe == 2:
        cara1.cruzado(cara2)
    elif golpe == 3:
        cara1.gancho(cara2)
    elif golpe == 4:
        cara1.cruzado(cara2)
    elif golpe == 5:
        cara1.chave_braco(cara2)
    elif golpe == 6:
        cara1.superman_puch(cara2)


if __name__ == '__main__':
    Jair = Boxeador('Bolsonaro')
    Inacio = MMA('Lula')

    while Jair.energia > 0 and Inacio.energia > 0:
        print(Jair)
        print(Inacio)
        lutador = random.randrange(1, 3)
        if lutador == 1:
            golpe(Jair, Inacio)
        else:
            golpe(Inacio, Jair)


    if Jair.energia <= 0:
        print("Bolsonaro ganhou.")
    else:
        print("Lula Ganhou!!!!!!!!")








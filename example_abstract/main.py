from funcionary import *

if __name__ == '__main__':

    g1 = Gerente("Felipe", "313131313", 31141414)
    if g1.autenticar("313131313", 31141414):
        print(g1.cancelar_operacao())
    else:
        print("Erro!!")

    op1 = Operador_Caixa("Jao", "1431414", 314141441414, 2)
    if op1.autenticar("2", 233):
        print(op1.registrar_produto())
    else:
        print("Erro! Tente Novamente!")

    seguranca = Seguranca("MC Kung SP", "2222", 1234, 90)
    if seguranca.autenticar("90", 12234):
        print(seguranca.acionar_alarme())
    else:
        print("Negativo capita!")
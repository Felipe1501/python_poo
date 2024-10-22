import pickle
from typing import List
from common import *
from interface_election import Transparencia
import csv

class Urna(Transparencia):
    mesario: Pessoa
    __secao: int
    __zona: int
    __eleitores_presentes: List[Eleitor] = []
    __eleitores: List[Eleitor] = []
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor: Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def to_csv(self):
        with open(f'{self.__zona}_{self.__secao}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Seção', 'Zona', 'Título'])

            for eleitores in self.__eleitores:
                writer.writerow([eleitores.get_secao().get_zona(), eleitores.get_titulo()])

    def to_txt(self):
        with open(f'{self.__zona}_{self.__secao}.txt', mode='w') as file:
            for eleitores in self.__eleitores_presentes:
                file.write(eleitores.__str__())

    def __str__(self):
        info =  f'Urna da seção {self.__secao}, zona {self.__zona}\n'
        info += f'Mesario {self.mesario}\n'
        return info

if __name__ == '__main__':
    cand1 = Candidato("Yuri Aberto", "19102024-2", "19102024-2", 9)
    cand2 = Candidato("Jair Bolsoneiro", "19102024-2", "19102024-2", 13)

    eleitor = Eleitor("Lula JR", "1213134-3", "1213134-3", 1, 132, 9)
    eleitor1 = Eleitor("Chico Coins", "1214434-3", "1214434-3", 1, 162, 9)
    eleitor2 = Eleitor("Japa NK", "111111-3", "111111-3", 1, 162, 13)

    urna = Urna(eleitor2, 54, 272, [cand1, cand2], [eleitor, eleitor1, eleitor2])
    urna.registrar_voto(eleitor1, 99)
    urna.to_csv()
    urna.to_txt()
    print(urna)
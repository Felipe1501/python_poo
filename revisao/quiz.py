
from typing import List

class Quiz:
    disciplina : str
    aluno: str
    __acertos: int
    __erros: int

    def __init__(self, disciplina: str, aluno: str, acertos: int, erros: int):
        self.disciplina = disciplina
        self.aluno = aluno
        self.__acertos = acertos
        self.__erros = erros

    def calcular_pontos(self):
        pontos = max(0,self.get_acertos() - self.get_erros())

        return pontos


    def get_acertos(self):
       return self.__acertos

    def get_erros(self):
        return self.__erros

    def __str__(self):
        resultado_quiz = (f'Disciplina: {self.disciplina}\n'
                          f'Aluno: {self.aluno}\n'
                          f'Acertos: {self.get_acertos()}\n'
                          f'Erros: {self.get_erros()}\n'
                          f'Resultado Final: {self.calcular_pontos()}')
        return resultado_quiz

class Quiz2A(Quiz):
    def __init__(self, disciplina, aluno, acertos, erros):
        super().__init__(disciplina, aluno, acertos, erros)

    def calcular_pontos(self):
        return max(0, self.get_acertos() - (4 * self.get_erros()))

class Quiz3A(Quiz):
    def __init__(self, disciplina, aluno, acertos, erros):
        super().__init__(disciplina, aluno, acertos, erros)

    def calcular_pontos(self):
        return max(0, self.get_acertos() - (2 * self.get_erros()))

class Aluno:
    __matricula: int
    __nome: str
    __quizes: Quiz

    def __init__(self, matricula: int, nome: str, quizes: Quiz):
        self.__quizes = quizes
        self.__matricula = matricula
        self.__nome = nome

    def __str__(self):
        info = (f'Matricula: {self.__matricula}\n'
                f'Nome: {self.__nome}\n'
                f'Quiz: {self.__quizes}')

class Disciplina:
    __nome: str
    __professor: str
    __ano: int
    __semestre: int
    __alunos: List[Aluno] = []

    def __init__(self, nome: str, professor: str, ano:int, semestre: int, alunos: List[Aluno]):
        self.__nome = nome
        self.__ano = ano
        self.__professor = professor
        self.__semestre = semestre
        self.__alunos = []

    def add_alunos(self, aluno: Aluno):
        for a in self.__alunos:
            if a.__matricula == aluno.__matricula:
                raise Exception("Aluno já existe")
        self.__alunos.append(aluno)

    def __str__(self):
        alunos_info = "\n".join([str(aluno) for aluno in self.__alunos])
        return (f'Disciplina: {self.__nome}\n'
                f'Professor: {self.__professor}\n'
                f'Ano: {self.__ano}, Semestre: {self.__semestre}\n'
                f'Alunos:\n{alunos_info}')
class Quiz:
    disciplina : str
    aluno : str
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
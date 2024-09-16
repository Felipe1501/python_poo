from quiz import *

def main():

    aluno1 = Aluno(123, "João Silva")
    aluno2 = Aluno(456, "Maria Souza")

    # Criando quizzes para os alunos
    quiz1_aluno1 = Quiz2A("Matemática", "João Silva", 10, 2)  # Cada erro anula 4 acertos
    quiz2_aluno1 = Quiz3A("História", "João Silva", 8, 1)     # Cada erro anula 2 acertos
    quiz1_aluno2 = Quiz3A("Matemática", "Maria Souza", 7, 3)


    aluno1.adicionar_quiz(quiz1_aluno1)
    aluno1.adicionar_quiz(quiz2_aluno1)
    aluno2.adicionar_quiz(quiz1_aluno2)


    disciplina = Disciplina("Ciências Exatas", "Professor Carlos", 2024, 1)
    try:
        disciplina.add_aluno(aluno1)
        disciplina.add_aluno(aluno2)
    except Exception as e:
        print(e)


    print(disciplina)

if __name__ == "__main__":
    main()

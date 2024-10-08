from abc import ABC, abstractmethod
class Funcionario(ABC):
    nome: str
    cpf: str
    __senha: int

    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    def __str__(self):
        informacoes = (f'Nome: {self.nome}\n'
                       f'CPF: {self.cpf}')
        return informacoes

    def get_senha(self):
        return self.__senha

    @abstractmethod
    def autenticar(self, user: str, senha: int):
        pass

class Gerente(Funcionario):

    def autenticar(self, user: str, senha: int):
        if user == self.cpf and senha == self.get_senha():
            return True
        return False

    def cancelar_operacao(self):
        return "Operação Cancelada!!!"

class Operador_Caixa(Funcionario):
    numero_int: int

    def __init__(self, nome: str, cpf: str, senha: int, num_caixa: int):
        super().__init__(nome, cpf, senha)
        self.numero_int = num_caixa
    def __str__(self):
        super().__str__()
        informacoes = f'Código do caixa: {self.numero_int}'
        return informacoes
    def autenticar(self, user: str, senha: int):
        if int(user) == self.numero_int and senha == self.get_senha():
            return True
        return False

    def registrar_produto(self):
        return "Produto Registrado com Sucesso!!!!!"

class Seguranca(Funcionario):
    posto: int

    def __init__(self, nome: str, cpf: str, senha: int, posto: int):
        super().__init__(nome, cpf, senha)
        self.posto = posto

    def __str__(self):
        super.__str__()
        informacoes = f'Posto: {self.posto}'
        return informacoes

    def autenticar(self, user: str, senha: int):
        if int(user) == self.posto and senha == self.get_senha():
            return True
        return False

    def acionar_alarme(self):
        return "Uooooooooouuuuooooouuuoouuuu!"
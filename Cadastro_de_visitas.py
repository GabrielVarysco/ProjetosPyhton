import enum

lista_visita = []
lista_visitantes = []
lista_profissionais = []


class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def get_nome(self):
        return self.__nome

    def get_especialidade(self):
        return self.__especialidade

    def get_sala(self):
        return self.__sala


class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def get_nome(self):
        return self.__nome

    def get_documento(self):
        return self.__documento


class Visita:
    def __init__(self, visitante, profissional, data_visita):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_visita = data_visita

    def get_visitante(self):
        return self.__visitante

    def get_profissional(self):
        return self.__profissional

    def get_data(self):
        return self.__data_visita

    def __str__(self):
        return f"Visitante: {self.__visitante}, Profissional: {self.__profissional}, Data: {self.__data_visita}"


def cadastrar_profissional():
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    sala = int(input("sala: "))

    objProfissional = Profissional(nome, especialidade, sala)
    lista_profissionais.append(objProfissional)


def cadastrar_visitante():
    nome = input("Nome: ")
    documento = int(input("CPF: "))

    objVisitante = Visitante(nome, documento)
    lista_visitantes.append(objVisitante)


def localizar_profissional():
    for ind, objProfissional in enumerate(lista_profissionais):
        print(f"{ind} - {objProfissional.get_nome()}, {objProfissional.get_especialidade()}, sala: {objProfissional.get_sala()}")


def registrar_visita():
    for ind, objVisitante in enumerate(lista_visitantes):
        print(f"{ind} - {objVisitante.get_nome()}")
    visitante = int(input("Escolha pelo índice: "))

    for ind, objProfissional in enumerate(lista_profissionais):
        print(f"{ind} - {objProfissional.get_nome()}")
    profissional = int(input("Escolha pelo índice: "))

    data = input("Data da visita: ")

    objVisita = Visita(visitante, profissional, data)
    lista_visita.append(objVisita)


def relatorio():
    for ind, objProfissional in enumerate(lista_profissionais):
        print(f"{ind} - {objProfissional.get_nome()}, {objProfissional.get_especialidade()}, sala: {objProfissional.get_sala()}")
    try:
        selecionado = input('Escolha um dos ids acima: ')
        # escolhido = lista_profissionais[int(selecionado)].get_nome() Aqui e para caso salve o nome
        for indice, visita in enumerate(lista_visita):
            if visita.get_profissional() == int(selecionado):
                print(
                    indice, lista_visitantes[visita.get_visitante()].get_nome())
    except:
        print(f'Opção Invalida')
        relatorio()


def menu():
    while True:
        escolha = input(
            """
            MENU
1- Cadastrar Profissional.
2- Localizar Profissional.
3- Cadastrar Visitante.
4- Registrar Visita.
5- Relatório de Conferência.
6- Sair.
Escolha: """)
        if escolha == "1":
            cadastrar_profissional()

        if escolha == "2":
            localizar_profissional()

        if escolha == "3":
            cadastrar_visitante()

        if escolha == "4":
            registrar_visita()

        if escolha == "5":
            relatorio()

        if escolha == "6":
            break


if __name__ == '__main__':
    menu()

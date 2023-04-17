lista_jogadores = []
lista_escalados = []
lista_reserva = []


class Jogador:
    def __init__(self, numero, nome, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao
        self.__situacao = "NORMAL"
        self.__participou_partida = False

    def __str__(self):
        return f"Jogador: {self.__nome_jogador} - Camisa: {self.__numero} - Posição: {self.__posicao} - Situação: {self.__situacao}"

    def get_nome(self):
        return self.__nome_jogador

    def get_numero(self):
        return self.__numero

    def get_posicao(self):
        return self.__posicao

    def get_situacao(self):
        return self.__situacao

    def set_situacao(self):
        self.__situacao = "EXPULSO"

    def get_participou_partida(self):
        return self.__participou_partida

    def set_participou_partida(self):
        self.__participou_partida = True


def ler_arquivo():
    arquivo = open("convocados.txt", "r")

    for pessoa in arquivo:
        numero, nome, posicao = pessoa[0:-1].split(":")
        objJogadores = Jogador(numero, nome, posicao)
        lista_jogadores.append(objJogadores)

    print("\n=-=-=\nJogadores adicionados ao projeto com sucesso.\n=-=-=")

    arquivo.close()


def escalar_jogadores():
    for numero in range(11):
        numero_escolhido = "inválido"
        lista_numeros = list(map(lambda e: e.get_numero(), lista_jogadores))
        lista_numeros_escalados = list(map(lambda e: e.get_numero(), lista_escalados))

        while numero_escolhido not in lista_numeros or numero_escolhido in lista_numeros_escalados:
            nomes_jogadores = ""
            for jogador in lista_jogadores:
                nomes_jogadores += f"{jogador.get_numero()} - {jogador.get_nome()}\n"
            print(f"Jogadores restantes: \n{nomes_jogadores}")

            numero_escolhido = input(f"Jogador {numero+1}, escolha pelo numero da camisa: ")

            if numero_escolhido in lista_numeros_escalados:
                print("Jogador já escalado")
            elif numero_escolhido not in lista_numeros:
                print("Número do jogador não existente")

        objEscalado = [e for e in lista_jogadores if e.get_numero() == numero_escolhido][0]
        objEscalado.set_participou_partida()
        lista_escalados.append(objEscalado)
        lista_jogadores.remove(objEscalado)
        print(f"Jogador {objEscalado.get_nome()}, camisa {objEscalado.get_numero()}, posicao {objEscalado.get_posicao()} escalado")

    for jogador in lista_jogadores:
        if not jogador.get_participou_partida():
            lista_reserva.append(jogador)

    print("\n=-=-=\nOs jogadores restantes foram adicionados ao banco de reservas.\n=-=-=")


def substituicao():
    while True:
        for js in lista_escalados:
            print(js)

        numero_substituido = input(f"\nSelecione pelo número da camisa o jogador do seu time que você deseja retirar de campo: ")
        objSubstituicao = [e for e in lista_escalados if e.get_numero() == numero_substituido][0]
        lista_reserva.append(objSubstituicao)
        lista_escalados.remove(objSubstituicao)

        for je in lista_reserva:
            print(je)

        numero_escalado = input(f"\nSelecione pelo numero da camisa o jogador que irá entrar em campo: ")
        objSubstituicao = [e for e in lista_reserva if e.get_numero() == numero_escalado][0]
        objSubstituicao.set_participou_partida()
        lista_escalados.append(objSubstituicao)
        lista_reserva.remove(objSubstituicao)

        escolha_parar = int(input(
"""Você deseja fazer mais alguma substituição?
1- Continuar a substituir
2- Voltar
Escolha pelo indice: """))
        if escolha_parar == 1:
            pass
        if escolha_parar == 2:
            break


def expulsao():
    while True:
        for je in lista_escalados:
            print(je)

        numero_expulso = input(f"\nSelecione pelo numero da camisa o jogador que será expulso: ")
        objExpulso = [e for e in lista_escalados if e.get_numero() == numero_expulso][0]
        objExpulso.set_situacao()
        lista_reserva.append(objExpulso)
        lista_escalados.remove(objExpulso)

        escolha_parar = int(input(
"""Você deseja fazer mais alguma expulsão?
1- Continuar a expulsar
2- Voltar
Escolha pelo índice: """))
        if escolha_parar == 1:
            pass
        if escolha_parar == 2:
            break


def imprimir_jogadores():
    arquivo = open("todosJogadores.txt", "w")
    for je in lista_escalados:
        arquivo.write(str(je)+"\n")

    for jr in lista_reserva:
        if jr.get_participou_partida() == True:
            arquivo.write(str(jr)+"\n")

    arquivo.close()


while True:
    escolha = int(input(
"""
---------- MENU -----------
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
6- Sair
Escolha: """))
    if escolha == 1:
        ler_arquivo()
    if escolha == 2:
        escalar_jogadores()
    if escolha == 3:
        substituicao()
    if escolha == 4:
        expulsao()
    if escolha == 5:
        imprimir_jogadores()
    if escolha == 6:
        break

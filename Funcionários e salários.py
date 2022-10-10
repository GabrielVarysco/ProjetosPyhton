funcionarios = ['Maria Clara', 'João Antonio', 'Carlos', 'Pedro', 'Ana']
salarios = [7450.23, 5677.33, 3970.34, 3470.00, 2200.00]

media_salarios = sum(salarios) / len(salarios)

login = []
senha = []

while True:
    escolha = input('''
    MENU
    1- Cadastrar Login e Senha
    2- Aumento de 10%
    3- Relatório
    4- Cadastrar Funcionário
    Escolha: ''')

    if escolha == '1':
        nome = input("Digite o seu nome: ")

        if nome in funcionarios:
            login.append(nome)

            digite_senha = input("Digite a senha: ")
            senha.append(digite_senha)

        else:
            print("Seu nome não está cadastrado.")
            continue

    if escolha == '2':
        login2 = input("Login: ")
        senha2 = input("senha: ")

        if login2 in login and senha2 in senha:
            if salarios[0] < media_salarios:
                aumento = salarios[0] * 0.1 + salarios[0]
                salarios[0] = aumento
            if salarios[1] < media_salarios:
                aumento = salarios[1] * 0.1 + salarios[1]
                salarios[1] = aumento
            if salarios[2] < media_salarios:
                aumento = salarios[2] * 0.1 + salarios[2]
                salarios[2] = aumento
            if salarios[3] < media_salarios:
                aumento = salarios[3] * 0.1 + salarios[3]
                salarios[3] = aumento
            if salarios[4] < media_salarios:
                aumento = salarios[4] * 0.1 + salarios[4]
                salarios[4] = aumento

        else:
            print("Você não está cadastrado.")
            continue

    if escolha == '3':
        for i in range(len(funcionarios)):
            print(str(funcionarios[i]) + '\t ' + str(salarios[i]))

    if escolha == '4':
        nome2 = input("Digite o nome do novo funcionário: ")
        funcionarios.append(nome2)
        salarios2 = input("Digite o salário do novo funcionário: ")
        salarios.append(salarios2)

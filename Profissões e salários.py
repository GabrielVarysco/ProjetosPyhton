lst_nomes = []
lst_profissoes = []
lst_salarios = []

lst_menores_profissoes = []
lst_menores_salarios = []

profissoes_repetidas = 0

while True:
    nome = input("Digite o nome: ")
    if nome == "fim":
        break
    else:
        lst_nomes.append(nome)

    profissao = input("Digite a profissão: ")
    if profissao in lst_profissoes:
        profissoes_repetidas = profissoes_repetidas + 1
        print(profissoes_repetidas)
    lst_profissoes.append(profissao)

    salario = int(input("Digite o salário sem casas decimais: "))
    if salario >= 1:
        lst_salarios.append(salario)
    else:
        while True:
            salario = int(input("O salário deve ser maior que zero. Digite novamente: "))
            if salario >= 1:
                lst_salarios.append(salario)
                break
            else:
                continue

    if salario <= 2700:
        lst_menores_salarios.append(salario)
        lst_menores_profissoes.append(profissao)

media_salarios = sum(lst_salarios) / len(lst_salarios)

print("Nomes    - Profissões     - Salários")
for i in range(len(lst_nomes)):
   print(f"{lst_nomes[i]}    - {lst_profissoes[i]}    - {lst_salarios[i]}")

print(f'''Resultados após a digitação:\n
--> Número de pessoas cadastradas: {len(lst_nomes)}\n
--> Número de profissões informadas: {len(lst_profissoes) - profissoes_repetidas}\n
--> Média salarial: {media_salarios}\n
--> Profissões que possuem salário de 2700 ou menos: {lst_menores_profissoes}''')


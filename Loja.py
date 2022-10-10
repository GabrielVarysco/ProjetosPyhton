lista_produtos = ['1001', '1324', '6548', '2987', '7623']
lista_precos   = [ 5.32 ,  6.45 ,  2.37 ,  5.32 ,  6.45 ]

lista_produtos_cliente = []
lista_quantidade = []
lista_precos_cliente = []

conta0 = 0
conta1 = 0
conta2 = 0
conta3 = 0
conta4 = 0

nome = input("Seu nome: ")
while True:
    produto = input("Código do produto: ")
    if produto in lista_produtos:
        lista_produtos_cliente.append(produto)
        quantidade = int(input("Quantidade de produtos: "))
        lista_quantidade.append(quantidade)
    elif produto == 'fim':
        break
    else:
        print("Esse código de produto é inexistente, tente novamente.")


if '1001' in lista_produtos_cliente:
     numero0 = lista_produtos_cliente.index('1001')
     conta0 = lista_quantidade[numero0] * 5.32
     lista_precos_cliente.append(conta0)

if '1324' in lista_produtos_cliente:
    numero1 = lista_produtos_cliente.index('1324')
    conta1 = lista_quantidade[numero1] * 6.45
    lista_precos_cliente.append(conta1)

if '6548' in lista_produtos_cliente:
    numero2 = lista_produtos_cliente.index('6548')
    conta2 = lista_quantidade[numero2] * 2.37
    lista_precos_cliente.append(conta2)

if '2987' in lista_produtos_cliente:
     numero3 = lista_produtos_cliente.index('2987')
     conta3 = lista_quantidade[numero3] * 5.32
     lista_precos_cliente.append(conta3)

if '7623' in lista_produtos_cliente:
     numero4 = lista_produtos_cliente.index('7623')
     conta4 = lista_quantidade[numero4] * 6.45
     lista_precos_cliente.append(conta4)


total = conta0 + conta1 + conta2 + conta3 + conta4

print(lista_quantidade)
print(lista_precos_cliente)
print(lista_produtos_cliente)

print(f"Nome: {nome}\nProduto - Qtd.  - Preço")
for i in range(len(lista_produtos_cliente)):
   print(f"{lista_produtos_cliente[i]}    - {lista_quantidade[i]}    - {lista_precos_cliente[i]}")
print(f"Total:            {total}")

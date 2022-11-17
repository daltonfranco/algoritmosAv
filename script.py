from rich import print

lista = []

while True:
    perg = int(input("Escolher um valor (Valor negativo para cancelar): "))
    if perg >= 0:
        lista.append(perg)
    elif perg < 0:
        break

lista_crescente = []

def crescente():
    while lista != []:
        maior_numero = min(lista, key=int)
        lista_crescente.append(maior_numero)
        lista.remove(maior_numero)
    return lista_crescente

lista_decrescente = []

def decrescente():
    while lista != []:
        menor_numero = max(lista, key=int)
        lista_decrescente.append(menor_numero)
        lista.remove(menor_numero)
    return lista_decrescente

escolha = input("Quer a lista decrescente ou crescente: [d/c]: ")

if escolha == "c":
    print(crescente())
elif escolha == "d":
    print(decrescente())

    


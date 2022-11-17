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

lista_true = []

if escolha == "c":
    lista_true = crescente()
    print(crescente())

elif escolha == "d":
    lista_true = decrescente()
    print(decrescente())

qtt_element = len(lista_true)

print(f'Existem {qtt_element} elementos na sua lista!!!!!!')

while True:
    pilha = int(input("Voce quer remover o valor de qual posição: [valor negativo para cancelar] "))
    if pilha > qtt_element:
        input("Não existe essa posicao na lista!!! Aperte enter para continuar!!!!  ")
        print(lista_true)
        print(f'Existem {qtt_element} elementos na sua lista!!!!!!')
    elif pilha >= 0:
        pilha -= 1
        lista_true.pop(pilha)
        print(lista_true)
        qtt_element -= 1
        print(f'Existem {qtt_element} elementos na sua lista!!!!!!')
    elif pilha < 0:
        break

while True:
    for y in reversed(lista_true)
        print(x)


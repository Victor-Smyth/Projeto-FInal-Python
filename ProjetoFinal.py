#Tabuada
def op1():
    print('Bem Vindo a Tabuada')
    print('Digite 1-Adição, 2-Multiplicação, 3-Subtração, 4-Divisão, 5-Exponeciação')
    def adic():
        valor = int(input('Digite um valor: '))
        aux = 0
        while (aux <= 10):
            print('{} + {} = {}'.format(valor, aux, (valor + aux)))
            aux = aux + 1

    def mult():
        valor = int(input('Digite um valor: '))
        aux = 0
        while (aux <= 10):
            print('{} X {} = {}'.format(valor, aux, (valor * aux)))
            aux = aux + 1

    def sub():
        valor = int(input('Digite um valor: '))
        aux = 0
        while (aux <= 10):
            print('{} - {} = {}'.format(valor, aux, (valor - aux)))
            aux = aux + 1

    def div():
        valor = int(input('Digite um valor: '))
        aux = 0
        while (aux <= 10):
            print('{} / {} = {}'.format(valor, aux, (valor / aux)))
            aux = aux + 1

    def expo():
        valor = int(input('Digite um valor: '))
        aux = 0
        while (aux <= 10):
            print('{} ** {} = {}'.format(valor, aux, (valor ** aux)))
            aux = aux + 1

    y = input('Escolha sua opção')
    if y == '1':
        adic()
    elif y == '2':
        mult()
    elif y == '3':
        sub()
    elif y == '4':
        div()
    elif y == '5':
        expo()
    else:
        print('COMANDO ERRADO')

#While
def op2():
    x = 10
    while (x > 1):
        print(x)
        x = x - 2

#For
def op3():
    b = ['sem ar']
    lista = [1, 2, 3, 4, 5, 'a', 'b']
    for number in lista:
        print(number)
#Lista
def op4():
    lista = [1,2,3,4,5,6,7]
    print(lista)

#Range
def op5():
    for rodada in range(1, 11):
        print(rodada)

#If
def op6():
    numero = 42
    chute = input('Digite um número: ')
    if chute == numero:
        print('Você acertou')
    else:
        print('Você errou')

while True:
    print()
    print('Swith Case')
    print()
    print('Tabuada - (1)\n')
    print('While - (2)\n')
    print('For - (3)\n')
    print('Lista - (4)\n')
    print('Range - (5)\n')
    print('If - (6)\n')

    escolha=int(input('Escolha o Progama Desejado:'))

    match escolha:
        case 1:
            op1()
            break
        case 2:
            op2()
            break
        case 3:
            op3()
            break
        case 4:
            op4()
            break
        case 5:
            op5()
            break
        case 6:
            op6()
            break
        case _:
            print('Inválido')
            break

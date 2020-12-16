# calculadora simples.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('''Escolha uma das opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa ''' )
    escolha = int(input('Dentre as opções, qual a sua escolha? '))
    if escolha == 1:
        somar = n1 + n2
        print(f'A soma entre {n1} + {n2} = {somar}')
    elif escolha == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} = {multiplicar}')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
            print(f'Entre {n1} e {n2} o maior número é {maior}')
    elif escolha == 4:
        print('Informe novos números: ')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    else:
        print('Você saiu do programa')

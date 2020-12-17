# Par ou Ímpar.
from random import randint
conta = 0
while True:
    jogador = int(input('Digite um número inteiro: '))
    pc = randint(0, 10)
    tot = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolhe par ou ímpar? [P / I] ')).strip().upper() [0]
    print(f'Você escolheu {jogador} e o seu oponente escolheu {pc}. O total foi de {tot}')
    print('Par' if tot % 2 == 0 else 'Ímpar')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você ganhou')
            conta += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if tot % 2 == 0:
            print('Você ganhou')
            conta += 1
        else:
            print('Você perdeu')
            break
    print('Você quer jogar novamente?')

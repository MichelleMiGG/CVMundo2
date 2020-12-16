# jogo da adivinhação
from random import randint
pc = randint(0, 10)
print('Vou pensar em un número de 0 a 10, tente adivinhar:')
acerto = False
palpite = 0
while not acerto:
    escolha = int(input('Em que número o computador pensou? '))
    palpite += 1
    if escolha == pc:
        acerto = True
    else:
        if escolha < pc:
            print('Mais... tente novamente.')
        elif escolha > pc:
            print('Menos... tente novamente.')
print(f'Você acertou com {palpite} palpites')

# número primo.
n = int(input('Digite um número:'))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
print(f'O número {n} foi divisível {cont} vezes')
if cont == 2:
    print('O número é primo')
else:
    print('O número não é primo')

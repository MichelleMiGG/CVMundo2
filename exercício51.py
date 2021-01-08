# Progressão Aritmética.
termo = int(input('Informe o primeiro termo:'))
r = int(input('Informe qual é a razão: '))
dec = termo + (10 - 1) * r
for c in range (termo, dec + r, r):
    print(f'{c}')

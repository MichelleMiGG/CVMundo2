# maioridade
from datetime import date
anoa = date.today().year
totm = 0
totmen = 0
for c in range(1, 8):
    anon = int(input(f'Informe o ano de nascimento da {c}° pessoa: '))
    idade = anoa - anon
    print(idade)
    if idade >= 21:
        totm += 1
    else:
        totmen += 1
print(f'Ao todo {totm} pessoas são maiores de idade e {totmen} pessoas são menores de idade')

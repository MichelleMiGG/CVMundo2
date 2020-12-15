# Analisador de média das idades, nome do homem mais velho e quantas mulheres são menores de 20 anos.
sidade = 0
medidade = 0
mhomem = 0
nvelho = ''
tm20 = 0
for c in range(1, 5):
    nome = str(input(f'Nome da {c}° pesssoa: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sidade += idade
    if c == 1 and sexo in 'Mm':
        mhomem = idade
        nvelho = nome 
    if sexo in 'Mm' and idade > mhomem:
        mhomem = idade
        nvelho = nome
    if sexo in 'Ff' and idade < 20:
        tm20 += 1

medidade = sidade / 4
print(f'A média da idade das pessoas no grupo é de {medidade}')
print(f'O homem mais velho tem {mhomem} anos e se chama {nvelho}')
print(f'Ao todo são {tm20} mulheres com menos de 20 anos')

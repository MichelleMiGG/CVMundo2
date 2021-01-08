# categorias
from datetime import date
anoa = date.today().year
anon = int(input('Informe o ano de nascimento: '))
idade = anoa - anon
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Categoria mirim')
elif idade <= 14:
    print('Categoria infantil')
elif idade <= 19:
    print('Categoria júnior')
elif idade <= 25:
    print('Categoria master')
else:
    print('Categoria sênior')

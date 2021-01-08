# tipos de triângulo.
a = float(input('Digite um número: '))
b = float(input('Digite outro númeor: '))
c = float(input('Digite mais um número: '))
if a < b + c and b < a + c and c < a + b:
    print('Pode formar um triângulo')
    if a == b == c:
        print('Forma um triângulo equilátero')
    elif a != b != c != a:
        print('Forma um triângulo escaleno')
    else:
         print('Forma um triângulo isócels')
else:
    print('Não pode formar um triângulo')

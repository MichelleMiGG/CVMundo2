# conversão de bases.
num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das opções para a basse de conversão
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal ''')
escolha = int(input('Informe qual foi a sua escolha: '))
print(escolha)
if escolha == 1:
    print(f'O número {num} convertido para Binário é {bin(num)[2:]}')
elif escolha == 2:
    print(f'O número {num} convertido para Octal é {oct(num)[2:]}')
elif escolha == 3:
    print(f'O número {num} convertido para Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente')

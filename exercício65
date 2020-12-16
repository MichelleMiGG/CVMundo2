# Média, maior e menor valores.
resposta = 'S'
soma = qtd = med = maior = menor =  0
while resposta in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resposta = str(input('Você quer continuar? [S/N]' )).upper().strip()[0]
med = soma / qtd
print(f'Você digitou {qtd} e média foi {med:.2}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

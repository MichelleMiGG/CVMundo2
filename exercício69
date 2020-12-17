# Dados de um grupo.
soma18 = qsm = qm20 = 0
while True:
    idade = int(input('Qual a idade da pessoa? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o sexo da pessoa? [F / M] ')).strip().upper() [0]
    if idade >= 18:
        soma18 += 1
    elif sexo == 'M':
        qsm += 1
    elif sexo == 'F' and idade < 20:
        qm20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar? [S / N] ')).strip().upper() [0]
    if resposta == 'N':
        break
print(f'{soma18} pessoas tem mais de 18 anos, {qsm} homens foram cadastrados e {qm20} mulheres tem menos de 20 anos')

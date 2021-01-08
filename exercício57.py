# validando dados
sexo = str(input('Qual é o seu sexo? [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, tente novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')

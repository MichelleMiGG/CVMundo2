# Caixa Eletrônico
vc = float(input('Qual valor você quer sacar? R$'))
totv = vc
cd = 50
totcd = 0
while True:
    if totv >= cd:
        totv -= cd
        totcd += 1
    else: 
        if totcd > 0:
            print(f'Total de {totcd} cédulas de R$ {cd}')
        elif cd == 50:
            cd = 20
        elif cd == 20:
            cd = 10
        elif cd == 10:
            cd = 1
        totcd = 0
        if totv == 0:
            break
  

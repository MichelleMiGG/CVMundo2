# valor a ser pago.
vp = float(input('Qual o valor do produto? R$'))
print(''' Escolha uma das formas de pagamento:
[ 1 ] à vista dinheiro/cheque: 10 por cento de desconto;
[ 2 ] à vista no cartão: 5 por cento de desconto;
[ 3 ] em até 2x no cartão;
[ 4 ] 3x ou mais no cartão: 20 por cento de juros. ''')
fp = int(input('Qual será a forma de pagamento? '))
if fp == 1:
    desc1 = vp - (vp * 0.10)
    print(f'Você pagará R$ {desc1}')
elif fp == 2:
    desc2 = vp - (vp * 0.05)
    print(f'Você pagará {desc2}')
elif fp == 3:
    sj = vp / 2
    print(f'Você pagará duas parcelas de R$ {sj}')
elif fp == 4:
    qp = int(input('Em quantas vezes você gostaria de parcelar? '))
    cj = (vp * 1.20) / qp
    print(f'Você pagará R${cj} de {qp} parcelas')
else:
    print('Opção inválida')

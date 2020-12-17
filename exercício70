# Anilasando produtos.
totc = pp1000 = ct = mp = 0
while True:
    np = str(input('Produto: '))
    pp = float(input('Preço: R$'))
    ct += 1
    totc += pp
    if pp > 1000:
        pp1000 += 1
    if ct == 1:
        mp = pp
    else:
        if pp < mp:
            mp = pp
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S / N] '))
    if resp == 'N':
        break
print(f'Foi gasto R${totc:.2f}, {pp1000} produtos custam mais de R$1000,00 e o produto mais barato custa {mp:.2f}')

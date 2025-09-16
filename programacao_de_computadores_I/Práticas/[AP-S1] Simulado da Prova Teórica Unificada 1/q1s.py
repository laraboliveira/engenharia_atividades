valorCompra=float(input('Defina o valor total da compra: R$'))

if valorCompra<=0:
    print('Erro: Valor total inválido.')
else:
    if valorCompra<=250:
        valorDesc=valorCompra-valorCompra*0.03
        print('Desconto de 3%.')
    elif valorCompra<=550:
        valorDesc=valorCompra-valorCompra*0.06
        print(f'Desconto de 6%.')
    elif valorCompra<=750:
        valorDesc=valorCompra-valorCompra*0.08
        print(f'Desconto de 8%.')
    else:
        valorDesc=valorCompra-valorCompra*0.1
        print(f'Desconto de 10%.')
    print(f'Valor com desconto: R${valorDesc:.2f}')
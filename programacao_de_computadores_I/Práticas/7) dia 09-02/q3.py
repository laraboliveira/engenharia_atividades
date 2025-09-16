resp='não'
cont=0;somaT=0

print('Caixa aberto!')
while resp!='sim':
    quant=int(input('\nDefina a quantidade de itens do pedido: '))
    somaP=0
    for i in range (1,quant+1):
        preço=float(input(f'. Defina o preço do item {i}: '))
        somaP+=preço
    respT=input('. CDefina a cobrança do delivery: ')
    if respT=='sim':
        somaP+=15
    somaT+=somaP
    cont+=1
    print(f'. Valor do pedido: R$ {somaP:.2f}.')
    resp=input('Defina o fechamento do caixa: ')
    
print(f'\nCaixa fechado!\nNúmero de pedidos: {cont}.\nValor total vendido: R$ {somaT:.2f}.')
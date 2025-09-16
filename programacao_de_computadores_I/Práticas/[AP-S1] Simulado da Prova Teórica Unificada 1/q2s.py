produto=input('Informe o nome do produto: ')

while produto!='fim':
    valorPedido=float(input('Informe o valor do pedido: R$'))
    if produto=='Pão de queijo':
        if valorPedido<=50:
            print('Percentual de desconto: 10.00%')
            valorDesconto=valorPedido-valorPedido*0.1
        elif valorPedido<=100:
            print('Percentual de desconto: 12.00%')
            valorDesconto=valorPedido-valorPedido*0.12
        else:
            print('Percentual de desconto: 15.00%')
            valorDesconto=valorPedido-valorPedido*0.15
    else:
        if valorPedido<=50:
            print('Percentual de desconto: 9.00%')
            valorDesconto=valorPedido-valorPedido*0.09
        elif valorPedido<=100:
            print('Percentual de desconto: 10.00%')
            valorDesconto=valorPedido-valorPedido*0.1
        else:
            print('Percentual de desconto: 11.00%')
            valorDesconto=valorPedido-valorPedido*0.11
    print(f'Valor com desconto: R$ {valorDesconto:.2f}')
    produto=input('Informe o nome do produto: ')
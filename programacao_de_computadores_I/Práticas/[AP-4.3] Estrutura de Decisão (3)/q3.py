quant_Mo = float(input('Digite a quantidade de Morangos (em kg): '))
quant_Ma = float(input('Digite a quantidade de Maçãs (em kg): '))

if quant_Mo < 0 or quant_Ma < 0:
    print('Entrada inválida')
else:
    if quant_Mo<=5:
        val_Mo = quant_Mo * 2.5
    else:
        val_Mo = quant_Mo * 2.2
        
    if quant_Ma<=5:
        val_Ma = quant_Ma * 1.8
    else:
        val_Ma = quant_Ma * 1.5
    total = val_Mo + val_Ma
    print(f'O valor total da sua compra é R$ {total:.2f}')
#FUNÇÕES
def Calculos(salMinimo,quantKW):
    valorKW=(salMinimo/7)/100
    preço= quantKW*valorKW
    preço_des=preço-preço*0.1
    return valorKW, preço, preço_des
    
    
#PROGRAMA PRINCIPAL
print('Cálculo do Custo da Energia Elétrica\n')
salMinimo=float(input('Informe o valor do Salário Mínimo (R$): '))
quantKW=float(input('Informe a quantidade gasta de quilowatts (kW): '))

valorKW, preço, preço_desc=Calculos(salMinimo,quantKW)

print(f'\nValor de cada quilowatt (R$): {valorKW:.2f}\nCusto da energia elétrica sem o desconto (R$): {preço:.2f}')
print(f'Custo da energia elétrica (desconto de 10%) (R$): {preço_desc:.2f}')
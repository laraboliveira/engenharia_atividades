import math

q = int(input('Digite a quantidade de lados: '))
if q<3:
    print('Não é um polígono')
elif q>6:
    print('Polígono não identificado')
else:
    l = float(input('Digite a medida do lado: '))
    if q==3:
        pol='triângulo'
        a=(pow(l,2)* math.sqrt(3))/4
    elif q==4:
        pol='quadrado'
        a=l**2
    elif q==5:
        pol='pentágono'
        a=(5*l**2)/(4*math.tan(0.6283))
    else:
        pol='hexágono'
        a=(3*pow(l,2)* math.sqrt(3))/2
    print(f'O polígono é um {pol} com área: {a:.2f}')


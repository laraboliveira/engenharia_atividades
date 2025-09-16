import math

def Potencia(a,b):
    x=10**(b*math.log10(a))
    return x

print('Cálculo da Potência\n')

a=int(input('Valor da base     (A): '))
b=int(input('Valor do expoente (B): '))

resut=Potencia(a,b)

print(f'\nA**B: {resut:.0f}')
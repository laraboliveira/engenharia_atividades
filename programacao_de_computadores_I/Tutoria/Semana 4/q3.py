import math

t=float(input('Informe a temperatura (em Kelvin): '))
#auxiliares
i0=2*10**-6
q=1.602*10**-19
print(f'Tensão | Corrente', end='')
print()

k=1.38*10**-23
resp='n'

while resp=='n':
    vd=-1
    while vd<=0.6:
        id=i0*((math.e)**((q*vd)/(k*t))-1)
        print(f'{vd:5.1f} | {id:5.1f}')
        vd+=0.1
    resp=input('Deseja sair? (s/S/n/n):')
    if resp=='n' or resp=='N':
        t=float(input('Informe a temperatura (em Kelvin): '))
     
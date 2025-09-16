import math

#CABEÇALHO
print(f'  x\y |', end='')
cont=7
for g in range(3,25,3):
        print(f'{g:5.0f}',end='')
        cont+=5
print()
print('-'*cont)

for x in range(2,31,2):
    print(f'{x:5d} |',end='') #CABEÇAÇHO DE COLUNA
    for y in range(3,25,3):
        op1=x+y
        resto1=op1%2
        op2=x*y
        resto2=op2%2
        if resto1==0:
            rp=(1/(x*y)) + math.sin(x+y)
        elif resto2!=0:
            rp=((y**x)-(4*x))**(1/2)
        else:
            rp=(x+y)**(1/3)
        print(f'{rp:5.2f}',end='')
        x+=3
    print()
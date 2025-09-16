import math
#CRIANDO VARIÁVEL
ini=int(input('Digite o valor inicial:'))
while -150>ini or ini>50:
    ini=int(input('Digite o valor inicial:'))
    
fim=int(input('Digite o valor final:'))
while ini>=fim:
    fim=int(input('Digite o valor final: '))
    
passo=int(input('Digite o passo: '))
while passo<=0:
    passo=int(input('Digite o passo: '))
    
#CABEÇALHO
l=ini
print(f'  x\y |', end='')
for g in range(ini,fim+1, passo):
    if l<=fim:
        print(f'{l:10.0f}',end='       ')
        l+=passo
print('\n-------------------------------------------------------------------------------------')

#CRIANDO TABELA
for x in range(ini,fim+1, passo):
    print(f'{x:5d} |',end='') #CABEÇAÇHO DE COLUNA
    for y in range(ini,fim+1, passo):
        if x<=30:
            resp=(x**2)+(2*y)-3
        elif x<=60:
            resp=math.sin(0.0175*x)*math.cos(0.0175*y)
        elif x<=90:
            resp=1/x**(-2)+y
        else:
            resp=math.pi
        print(f'{resp:10.2f}',end='       ')
    print('\n')
    
        
        
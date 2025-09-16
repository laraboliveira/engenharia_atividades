import math
crp=float(input('Valor padrão da carga de compressão (kg/cm2):'))
n= float(input('Número de amostras: '))
i=1
c=0
menor=math.inf

while i<=n:
    a=float(input(f'Área da amostra {i} (cm2):'))
    p=float(input(f'Peso da amostra {i} (cm2):'))
    c=p/a
    if c<menor:
        menor=c
    i=i+1
    
print(f'CARGA DE RUPTURA MÍNIMA = {menor:.2f}')

if crp>c:
    print('CIMENTO REPROVADO.')
else:
    print('CIMENTO APROVADO.')

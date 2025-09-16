import math

tipo=int(input('Forneça o tipo de ladrilho (1 ou 2): '))
area=float(input('Forneça a área da sala: '))

if tipo==1:
    quant=math.ceil(area/80)
else:
    quant=math.ceil(area/60)

print(f'Quantidade de ladrilhos: {quant}')
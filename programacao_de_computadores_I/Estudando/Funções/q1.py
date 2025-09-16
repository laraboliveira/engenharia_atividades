def Distancia(x1,x2,y1,y2):
    dis=((x1-x2)**2 + (y1-y2)**2)**0.5
    return dis

x1=float(input('Digite o valor da coordenada X1: '))
x2=float(input('Digite o valor da coordenada X2: '))
y1=float(input('Digite o valor da coordenada Y1: '))
y2=float(input('Digite o valor da coordenada Y2: '))

dis=Distancia(x1,x2,y1,y2)

print(f'A distância entre os pontos é {dis:.2f}')



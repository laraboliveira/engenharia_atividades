def Distancia (v,t):
    d=v*t
    return d

def Litros (d):
    l=d/12
    return l

print('Consumo na Viagem\n')

v=float(input('Velocidade Média (km/h): '))
t=float(input('Tempo da Viagem (h): '))

d=Distancia(v,t)
l=Litros(d)

print(f'\nDistância percorrida (km): {d:.0f}\nCombustível gasto (l): {l:.2f}')
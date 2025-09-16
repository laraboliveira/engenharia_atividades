p = float(input('Informe a posição inicial (Si): '))
while p<0:
    p = float(input('Informe a posição inicial (Si): '))

v = float(input('Informe a velocidade (v): '))
while v<=0:
    v = float(input('Informe a velocidade (v):'))

t = float(input('Informe o instante de tempo (t): '))
while t<=0:
    t = float(input('Informe o instante de tempo (t): '))

s=p+v*t

print(f'A posição final no tempo t = {t:.2f} será S = {s:.2f}')
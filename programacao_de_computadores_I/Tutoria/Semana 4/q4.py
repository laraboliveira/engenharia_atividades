cont=8
print(f'  x\y |', end='')
for g in range(1,9):
    print(f'{g:7.0f}',end='')
    cont+=7
print()
print('-'*cont)

for x in range(1,9,1):
    print(f'{x:6d}|',end='') #CABEÇAÇHO DE COLUNA
    for y in range(1,x+1):
        resto=(x+y)%2
        if x==y:
            rp=(x * y) / (x + y)
        elif resto!=0:
            rp=(x**2) + (y**2)
        else:
            rp=x+y
        print(f'{rp:7.1f}',end='')
    print()
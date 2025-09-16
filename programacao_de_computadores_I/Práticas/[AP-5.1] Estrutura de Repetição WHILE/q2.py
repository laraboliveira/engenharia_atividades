n=float(input('Informe o número que deseja calcular o Fatorial: '))
while n<=0:
    n=int(input('Número inválido, defina outro: '))
c=1
f=1

while c<=n:
    f=f*c
    c=c+1
print(f'O Fatorial de {n} é: {f}')
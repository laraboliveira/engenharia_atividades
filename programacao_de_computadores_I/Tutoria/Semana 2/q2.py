q=float(input('Quantidade de Números:'))
i=1
s=0
m=1
while i<=q:
    print(f'Iteração: {i}')
    n=float(input('Digite um número real (x > 0): '))
    while n<=0:
        print('ERRO: Número inválido !')
        n=float(input('Digite um número real (x > 0): '))
    s=s+n
    m=m*n
    i=i+1
ma=s/q
print(ma)
mg=m**(f'Média Aritmética: {1/q}')
print(f'{Média Geométrica: {mg:.2f}')


        
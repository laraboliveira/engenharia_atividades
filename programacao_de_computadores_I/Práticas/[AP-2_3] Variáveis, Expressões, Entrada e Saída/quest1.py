a1 = float(input('Informe o primeiro termo: '))
q = float(input('Informe a razão: '))
n = float(input('Informe o número do termo: '))


an=a1*q**(n-1)

print(f'O termo a({n:.0f}) é {an:.2f}')
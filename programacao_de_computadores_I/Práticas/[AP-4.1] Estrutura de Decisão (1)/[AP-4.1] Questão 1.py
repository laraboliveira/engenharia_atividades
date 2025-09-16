a=float(input('Informe o cateto 1 (a): '))
b=float(input('Informe o cateto 2 (b): '))
c=float(input('Informe a hipotenusa (c): '))

if c**2==b**2+a**2:
    print(f'{a:.0f}, {b:.0f}, {c:.0f} representam um terno pitagórico')
else:
    print(f'{a:.0f}, {b:.0f}, {c:.0f} NÃO representam um terno pitagórico')
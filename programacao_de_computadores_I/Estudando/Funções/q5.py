def comprimento1(l,p):
    h=p*l/100
    c1=(l**2+h**2)**0.5
    return c1

def comprimento2(l,p):
    h=(p*l/2)/100
    c2=2*((l/2)**2 + h**2)**0.5
    return c2

l=float(input('Digite a largura do telhado: '))
p=float(input('Digite a inclinação percentual: '))

c1,c2=comprimento1(l,p),comprimento2(l,p)

print(f'O comprimento do telhado de uma água é {c1:.2f}')
print(f'O comprimento do telhado de duas águas é {c2:.2f}')
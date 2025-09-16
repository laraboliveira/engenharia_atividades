def extensaoMola(m,k,g):
    fg=m*g
    x=fg/k
    return x
    

m=float(input('Digite a massa do objeto: '))
k=float(input('Digite a constante da mola: '))
g=9.807

x=extensaoMola(m,k,g)
print(f'A extensão da mola é {x:.2f} m')
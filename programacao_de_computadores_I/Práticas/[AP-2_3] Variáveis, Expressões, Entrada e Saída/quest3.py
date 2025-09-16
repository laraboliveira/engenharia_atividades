l = float(input('Forneça o comprimento do fio: '))
p = float(input('Forneça a força peso: '))
m = float(input('Forneça a massa: '))

g=p/m

t=2*3.14*(l/g)**0.5

print(f'A aceleração da gravidade é {g:.3f}')
print(f'O período do pêndulo é  {t:.3f}')
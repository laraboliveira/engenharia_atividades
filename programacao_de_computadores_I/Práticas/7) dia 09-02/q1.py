rp=input('Informe se deseja imprimir um retângulo (s/n): ')

while rp == 's':
    a=int(input('Informe a altura do retângulo: '))
    l=int(input('Informe a largura do retângulo: '))
    while a>l or a<0 or l<0:
        print('Entrada Inválida')
        a=int(input('Altura do retângulo: '))
        l=int(input('Largura do retângulo: '))
    for i in range(1,a+1,1):
        print('')
        for j in range(1,l+1,1):
            print('*',end='')
    rp=input('\nInforme se deseja imprimir outro retângulo (s/n):')
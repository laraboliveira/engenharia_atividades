name=input('Informe o nome do juiz: ')
n=int(input('Informe a quantidade de partidas: '))
contIm=0;contFal=0;contCar=0;contAcr=0
somaImp=0;somaFalt=0;somaCar=0;somaAcr=0

for i in range(1,n+1,1):
    print(f'\nPartida {i}:')
    imp=int(input('. Informe Impedimentos.......: '))
    somaImp+=imp
    contIm+=1
    falt=int(input('. Informe faltas.............: '))
    somaFalt+=falt
    contFal+=1
    cart=int(input('. Informe cartões............: '))
    somaCar+=cart
    contCar+=1
    acr=float(input('. Informe tempo de acréscimo.: '))
    somaAcr+=acr
    contAcr+=1
mediaIm=somaImp/contIm;mediaFalt=somaFalt/contFal
mediaCart=somaCar/contCar;mediaAcr=somaAcr/contAcr

print(f'\nEstatísticas do juiz {name}:\n. Impedimentos.......: {mediaIm:.2f}.\n. Faltas.............: {mediaFalt:.2f}.\n. Cartões............: {mediaCart:.2f}.\n. Tempo de acréscimo.: {mediaAcr:.2f}.')
    
    
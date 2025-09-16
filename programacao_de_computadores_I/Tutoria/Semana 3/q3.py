n=int(input('Quantidade de pacientes: '))
contM=0;contO=0

for i in range(1,n+1):
    peso=float(input('Peso: '))
    alt=float(input('Altura: '))
    imc=peso/alt**2
    if imc<16:
        print(f'O IMC é {imc:.2f} ==> Magreza grave')
        contM+=1
    elif imc<18.5:
        print(f'O IMC é {imc:.2f} ==> Abaixo do peso')
    elif imc<25:
        print(f'O IMC é {imc:.2f} ==> Saudável')
    elif imc<30:
        print(f'O IMC é {imc:.2f} ==> Sobrepeso')
    elif imc<40:
        print(f'O IMC é {imc:.2f} ==> Obesidade')
    else:
        print(f'O IMC é {imc:.2f} ==> Obesidade extrema')
        contO+=1

percM=contM*100/n
percO=contO*100/n
print(f'Percentual para Magreza grave: {percM:.2f}%\nPercentual para Obesidade extrema: {percO:.2f}%')
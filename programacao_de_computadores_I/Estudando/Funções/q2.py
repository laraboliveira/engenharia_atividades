def converteTemp(temC):
    tempF=tempC*9/5+32
    return tempF

tempC=float(input('Digite uma temperatura em Celsius: '))

tempF=converteTemp(tempC)

print(f'A temperatura em Fahrenheit é {tempF:.1f}')
def converteTemp(temF):
    tempC=(tempF-32)*5/9
    return tempC

tempF=float(input('Digite a temperatura em Fahrenheit:'))

tempC=converteTemp(tempF)

print(f'A temperatura em Celsius é {tempC:.1f}')
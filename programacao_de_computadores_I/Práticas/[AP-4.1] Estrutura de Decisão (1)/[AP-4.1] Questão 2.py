alt = float(input('Digite a altura: '))
sexo = input('Digite o sexo (m ou f): ')

if sexo=='m':
    peso=72.7*alt-58
else:
    peso=62.1*alt-44.7

print(f'O peso ideal é {peso:.2f}')
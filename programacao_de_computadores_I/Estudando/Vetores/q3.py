from biblioteca import*


vec=inputVetor('Informe o vetor: ',float)
print(f'\nDimensão do vetor: {len(vec)}')

print('\nElementos do Vetor:')
for i in range(len(vec)):
    print(round(vec[i],1))
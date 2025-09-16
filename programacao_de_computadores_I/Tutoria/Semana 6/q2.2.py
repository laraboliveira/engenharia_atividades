from biblioteca import*

print('Exercício 2')
vec1=[];vec2=[];vec3=[]

print('Leitura do primeiro vetor...')
vec1=inputVetor('Elementos: ',float)
print('Leitura do segundo vetor...')
vec2=inputVetor('Elementos: ',float)

for g in range(len(vec1)):
    result=2*(vec1[g]+vec2[g])
    vec3.append(result)

print(f'Impressões dos resultados:\nVetor 1\n{vec1}\nVetor 2\n{vec2}\nVetor 3\n{vec3}')
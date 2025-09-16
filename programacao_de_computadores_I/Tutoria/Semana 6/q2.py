from biblioteca import*

print('Exercício 2')
n=int(input('\nQual a dimensão dos vetores ? '))
vec1=[];vec2=[];vec3=[]

print('Leitura do primeiro vetor...')
for j in range(0,n):
    result1=float(input(f'Elemento na posição {j}: '))
    vec1.append(result1)
    
print('Leitura do segundo vetor...')
for i in range(0,n):
    result2=float(input(f'Elemento na posição {i}: '))
    vec2.append(result2)

for g in range(0,n):
    result3=2*(vec1[g]+vec2[g])
    vec3.append(result3)

print(f'Impressões dos resultados:\nVetor 1\n{vec1}\nVetor 2\n{vec2}\nVetor 3\n{vec3}')
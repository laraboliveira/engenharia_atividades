from biblioteca import*
import math

maior=-math.inf;menor=math.inf
vetorIND=[];vetorind=[]

mat=inputMatriz('Matriz de notas: ',float)

for i in range(len(mat)):
    for g in range(len(mat[0])):
        if mat[i][g]>maior:
            maior= mat[i][g]
        if mat[i][g]<menor:
            menor=mat[i][g]

for h in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[h][j]==maior:
            vetorIND.append(h)
        if mat[h][j]==menor:
            vetorind.append(h)
            
print(f'\nMenor nota: {menor}\nAlunos com a menor nota:')
for k in range(len(vetorind)):
    print(f'. {vetorind[k]}')
    
print(f'\nMaior nota: {maior}\nAlunos com a maior nota:')
for l in range(len(vetorIND)):
    print(f'. {vetorIND[l]}')

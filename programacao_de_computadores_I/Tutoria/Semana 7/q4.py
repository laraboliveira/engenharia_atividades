from biblioteca import*

mat=inputMatriz('Digite a matriz imagem, todos os elementos\n>>>', int)

print('Imagem:')
for j in range(len(mat)):
    print(mat[j])

for i in range(len(mat)):
    for g in range(len(mat[0])):
        if mat[i][g]==1:
            mat[i][g]=0
        else:
            mat[i][g]=1

print('Negativo:')
for h in range(len(mat)):
    print(mat[h])

#0,0,0,0,1,0,0,0,0; 0,0,0,1,0,1,0,0,0; 0,0,1,0,0,0,1,0,0; 0,1,0,0,0,0,0,1,0; 1,1,1,1,1,1,1,1,1
from biblioteca import*

mat=inputMatriz('Digite toda a matriz de inteiros: \n>>> ',int)
k=int(input('Digite uma constante: '))
col=int(input('Índice de uma coluna: '))

print('Resultados')

for i in range(len(mat)):
    for g in range(len(mat[0])):
        if g==col:
            mat[i][g]=mat[i][g]*k

for j in range(len(mat)):
    print(mat[j])
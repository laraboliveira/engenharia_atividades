from biblioteca import*

def somaMatriz(mat1,mat2):
    mat3=[]
    for i in range(len(mat1)):
        vec=[]
        for g in range(len(mat1[0])):
            val=mat1[i][g]+mat2[i][g]
            vec.append(val)
        mat3.append(vec)
    return mat3



mat1=inputMatriz('Digite a primeira matriz: ', int)
mat2=inputMatriz('Digite a segunda matriz: ', int)

if len(mat1)!=len(mat2):
    print('\nNão é possível somar as matrizes')
else:
    mat3=somaMatriz(mat1,mat2)
    print('Matriz resultante: ')
    for i in range(len(mat3)):
        print(mat3[i])
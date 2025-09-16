from biblioteca import*

mat1=inputMatriz('Informe os resultados do atleta 1: ', int)
mat2=inputMatriz('Informe os resultados do atleta 2: ', int)


if len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0]):
    print('Matrizes incompatíveis.')
else:
    cont1V=0;cont2V=0;contE=0
    for i in range(len(mat1)):
        for g in range(len(mat1[0])):
            if mat1[i][g]>mat2[i][g]:
                cont1V+=1
            elif mat2[i][g]>mat1[i][g]:
                cont2V+=1
            else:
                contE+=1
    print(f'Quantidade de vitórias do atleta 1: {cont1V}\nQuantidade de vitórias do atleta 2: {cont2V}\nQuantidade de empates: {contE}')
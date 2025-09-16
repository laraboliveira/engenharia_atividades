from biblioteca import*

mat=inputMatriz('Digite os elementos da matriz: ',int)
v=[]
if len(mat)!=len(mat[0]):
    print('\A matriz não é quadrada.')
else:
    print('Elementos da diagonal principal:')
    for i in range(len(mat)):
        for g in range(len(mat[0])):
            if i == g:
                val=mat[i][g]
                v.append(val)
    for j in range(len(v)):
        if j+1!=len(v):
            print(f'{v[j]},', end=' ')
        else:
            print(f'{v[j]}')
                
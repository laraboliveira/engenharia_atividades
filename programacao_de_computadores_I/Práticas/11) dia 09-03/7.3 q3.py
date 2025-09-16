from biblioteca import*

mat=inputMatriz('Digite os elementos da matriz: ',int)

resp=0
for i in range(len(mat)):
    for g in range(len(mat[0])):
        if i==g:
            if mat[i][g]!=1:
                resp=1
        else:
            if mat[i][g]==1:
                resp=1
        
if resp==1:
    print('A matriz não é identidade.')
else:
    print('A matriz é identidade.')
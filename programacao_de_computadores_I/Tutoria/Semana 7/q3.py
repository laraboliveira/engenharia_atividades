from biblioteca import*

print('Exercício 3 - Análise das Linhas da Matriz')
M = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
vec=[];prod=1;soma=0

print('\nResultados:\n\nMatriz:')
for i in range(len(M)):
    prod=1;soma=0
    print(M[i])
    for g in range(len(M[0])):
        if i%2==0:
            prod*=M[i][g]
        else:
            soma+=M[i][g]
    if prod>1:
        vec.append(prod)
    if soma>0:
        vec.append(soma)
print(f'\nVetor Resultante:\n{vec}')
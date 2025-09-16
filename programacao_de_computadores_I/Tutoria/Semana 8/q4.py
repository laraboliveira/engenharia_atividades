from biblioteca import*

mat1=inputMatriz('Matriz Original (inteiros):\n>>> ',int)

print('Matriz Original:')
for i in range(len(mat1)):
    print(mat1[i])

lin1=int(input('Primeira Linha: '))
lin2=int(input('Segunda Linha: '))

print('Matriz Resultante:')
for j in range(len(mat1)):
    if j==lin1:
        print(mat1[lin2])
    elif j==lin2:
        print(mat1[lin1])
    else:
        print(mat1[j])
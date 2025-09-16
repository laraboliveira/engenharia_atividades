from biblioteca import*

mat1=inputMatriz('Matriz Original (inteiros):\n>>> ',int)

print('Matriz Original:')
for i in range(len(mat1)):
    print(mat1[i])

lin1=int(input('Primeira Linha: '))
vec1=mat1[lin1]
lin2=int(input('Segunda Linha: '))
vec2=mat1[lin2]

print('Matriz Resultante:')
for j in range(len(mat1)):
    if j==lin1:
        print(vec2)
    elif j==lin2:
        print(vec1)
    else:
        print(mat1[j])
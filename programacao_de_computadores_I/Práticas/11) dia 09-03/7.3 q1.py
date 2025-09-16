from biblioteca import*

mat=inputMatriz('Digite os elementos da matriz: ',int)
col=int(input('\nDigite a coluna que será alterada: '))

while col<0 or col>len(mat[0])-1:
    col=int(input('Digite uma coluna válida: '))

print('\nMatriz alterada:')
for i in range(len(mat)):
    mat[i][col]*=2

for j in range(len(mat)):
    print(mat[j])
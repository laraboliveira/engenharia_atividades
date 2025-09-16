from biblioteca import*

dim=int(input('Digite a dimensão da matriz: '))
val=int(input('Digite o valor para preencher os campos: '))

mat=criarMatriz(dim,dim,val)

for i in range(len(mat)):
    print(mat[i])
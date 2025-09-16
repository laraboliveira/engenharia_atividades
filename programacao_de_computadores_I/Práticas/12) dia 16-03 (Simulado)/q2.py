from biblioteca import*
import math

print('Loja da tia Maria')
mat=inputMatriz('Matriz de estoque: ',int)
num=int(input('Numero de atualizações: '))

for i in range(num):
    indL=int(input('Índice da loja: '))
    indP=int(input('Índice do produto: '))
    est=int(input('Novo estoque: '))
    mat[indL][indP]=est
    for j in range(len(mat)):
        print(mat[j])
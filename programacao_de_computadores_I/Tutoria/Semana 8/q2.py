from biblioteca import*

print('Média das Notas dos Alunos:')

vec= inputVetor('Nomes dos alunos:\n>>>', str)
mat= inputMatriz('Matriz de notas:\n>>>', float)

vecNota=[]
vecInd=[]

for i in range(len(mat)):
    media=0
    for j in range(len(mat[0])):
        media+=mat[i][j]
    media/=len(mat[0])
    if media>=7:
        vecNota.append(media)
        vecInd.append(i)

if vecNota!=[]:
    for g in range(len(vecNota)):
        print(f'{vec[vecInd[g]]}, média={vecNota[g]:.2f}')
else:
    print('Não há alunos com média >= que 7.0 !')
    
    
#7.2,7.5,7.8,7.9; 6.8,6.9,5.8,5.2; 8.2,8.8,7.9,7.8;6.8,6.5,6.4,6.2
        
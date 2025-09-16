from biblioteca import*

print('Ministério do Meio Ambiente')
vec=inputVetor('Metas dos estados: ',int)
mat=inputMatriz('Plantio de árvores: ',int)
ind=[];plant=[]

for i in range(len(mat[0])):
    soma=0
    for g in range(len(mat)):
        soma+=mat[g][i]
    if soma<vec[i]:
        ind.append(i)
        plant.append(soma)

for j in range(len(ind)):
    print(f'Estado {ind[j]+1}, meta = {vec[ind[j]]}, plantio = {plant[j]}')
    


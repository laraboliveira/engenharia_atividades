from biblioteca import*

vec=inputVetor('Leitura das notas dos alunos\n>>', int)
F=[0,0,0,0,0,0,0,0,0,0,0]
A=[0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(vec)):
    F[vec[i]]+=1
for j in range(len(F)):
    A[j]=round(F[j]/len(vec),2)
print('Notas...F. Absoluta...F. Relativa')
v=0
for g in range(len(F)):
    print(f'{v:4d}',end='')
    print(f'{F[g]:10d}',end='')
    print(f'{A[g]:14.2f}')
    v+=1
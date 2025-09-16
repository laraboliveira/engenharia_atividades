from biblioteca import*

mat=[]
vec=['v','D(t)']

val=int(input('Digite o tempo final: '))
print(vec)


for i in range(0,val):
    for j in range(2):
        g=9.807
        d=round((g*i**2)/2)
        mat[i][j]=d

for k in range(len(mat)):
    print(mat[k])
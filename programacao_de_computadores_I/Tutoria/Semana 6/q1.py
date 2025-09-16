from biblioteca import*

print('Exercício 1')

n=int(input('\nQual a dimensão do vetor? '))
soma=0;mult=1
result=[]

for i in range(0,n):
    vec=float(input(f'Elemento [{i}]: '))
    result.append(round(vec,1))
    soma+=vec
    mult*=vec

medA=soma/n
medG=mult**(1/n)

print(f'\nResultados:\n{result}')
print(f'Média Aritmética: {medA:.4f}\nMédia Geométrica: {medG:.4f}')  
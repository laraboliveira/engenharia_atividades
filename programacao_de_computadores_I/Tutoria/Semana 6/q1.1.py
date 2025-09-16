from biblioteca import*

print('Exercício 1.1')
soma=0;mult=1
result=[]
result= inputVetor('Elementos: ', float)

for i in range(0,len(result)):
    soma+=result[i]
    mult*=result[i]

medA=soma/len(result)
medG=mult**(1/len(result))

print(f'\nResultados:\n{result}')
print(f'Média Aritmética: {medA:.4f}\nMédia Geométrica: {medG:.4f}')  
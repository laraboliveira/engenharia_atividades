from biblioteca import*

print('Exercício 1 - Operações com Matriz')

n=inputMatriz('Digite a matriz: ',int)

print('Leitura dos elementos da matriz:')

somaDP=0;prodDS=1;prodDP=1;contN=0

for i in range(len(n)):
    for g in range(len(n[0])):
        if g==i:
            somaDP+=n[i][g]
        if i+g==len(n)-1:
            prodDS*=n[i][g]
        if g>i:
            prodDP*=n[i][g]
        if g<i and n[i][g]==0:
            contN+=1
print(f'Resultados:')
print(f'Somatório (diagonal principal): {somaDP}\nProdutório (diagonal secundária): {prodDS}\nProdutório (acima da diagonal principal): {prodDP}\nNulos (abaixo da diagonal principal): {contN}')

#1, 1, 1, 2; 0, 2, 1, 3; 7, 6, 3, 4; 9, 0, 0, 4
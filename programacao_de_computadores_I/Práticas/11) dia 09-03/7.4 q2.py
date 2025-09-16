from biblioteca import*
import math

vecProduto=inputVetor('Informe os nomes dos produtos: ', str)
matVenda=inputMatriz('Informe as quantidades de vendas: ', float)

        
maior=-math.inf
for g in range(len(matVenda)):
    soma=0
    for j in range(len(matVenda[0])):
        soma+=matVenda[g][j]
        if soma>maior:
            maior=soma
            ind=g
            
print(f'Produto selecionado: {vecProduto[ind]}\nTotal de vendas de {vecProduto[ind]}: {maior:.0f}')
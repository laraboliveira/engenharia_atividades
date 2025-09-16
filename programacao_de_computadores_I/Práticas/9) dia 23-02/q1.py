from biblioteca import *

listaNome= inputVetor('Digite os nomes dos candidatos: ', str)
listaQuant= inputVetor('Digite as quantidades de votos: ', int)

if len(listaNome)!=len(listaQuant):
    print('\nVetores com tamanhos diferentes')
elif len(listaNome)<3:
    print('\nQuantidade de candidatos insuficiente')
else:
    maior = -1
    ind = 0
    for i in range(len(listaQuant)):
        if listaQuant[i] > maior:
            maior = listaQuant[i]
            ind = i
    print(f'\nVencedor das eleições: {listaNome[ind]}')

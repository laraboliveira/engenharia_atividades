from biblioteca import*
import math

def acimaMedia(nota,media):
    nVetor=[]
    for i in range(len(nota)):
        if nota[i]>media:
            nVetor.append(i)
    return nVetor
        

def estatNotas(nota):
    maior=-math.inf
    menor=math.inf
    soma=0
    for i in range(len(nota)):
        soma+=nota[i]
        if nota[i]>maior:
            maior=round(nota[i],1)
        if nota[i]<menor:
            menor=round(nota[i],1)
    media=round(soma/len(nota),1)
    return maior, menor, media

def exameEspecial(nota):
    exameVetor=[]
    for i in range(len(nota)):
        if nota[i]>=3 and nota[i]<6:
            exameVetor.append(i)
    return exameVetor
    
nota=[];nome=[]
nota=inputVetor('Notas: ', float)
nome=inputVetor('Nomes: ',str)

maior, menor, media=estatNotas(nota)
print(f'Maior nota: {maior:.1f}\nMenor nota: {menor:.1f}\nNota média: {media:.1f}')

print('Notas acima da média:')
nVetor=acimaMedia(nota,media)
for i in range(len(nVetor)):
    print(f'- [{nVetor[i]}] = {nota[nVetor[i]]} ({nome[nVetor[i]]})')
    
print('Notas em Exame Especial:')
exameVetor=exameEspecial(nota)
for j in range(len(exameVetor)):
    print(f'- [{exameVetor[j]}] = {round(nota[exameVetor[j]],1)} ({nome[exameVetor[j]]})')







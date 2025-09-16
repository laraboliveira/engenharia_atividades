from biblioteca import*
import math

def calculosVetor(x):
    soma=0;maior=-math.inf;menor=math.inf
    for i in range(len(x)):
        if x[i]>maior:
            maior=round(x[i],2)
        if x[i]<menor:
            menor=round(x[i],2)
        soma+=x[i]
    media=round(soma/len(x),2)
    
    num=len(x)
    return(num,menor, maior, media)

print('Manipulações de valores de Vetor')
vec=inputVetor('Vetor X: ', float)
num,menor, maior, media=calculosVetor(vec)
print('Propriedades do vetor X:')
print(f'. Possui {num:.2f} elementos\n. {menor:.2f} é o menor valor\n. {maior:.2f} é o maior valor\n. A média dos valores é {media:.2f}')

#59.19, 76.0, 88.27, 47.06, 70.41, 71.0, 86.0, 17.9, 91.0
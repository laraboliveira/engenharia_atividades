from biblioteca import *
import math
def calculaLucros(qCoxinha, qQuibe, lCoxinha,lQuibe):
    lucro=[]
    for i in range(len(qCoxinha)):
        coxinha=qCoxinha[i]
        quibe=qQuibe[i]
        total=coxinha*lCoxinha+quibe*lQuibe
        lucro.append(round(total,2))
    return lucro

quantCoxinhas= inputVetor('Informe as vendas de coxinhas: ', float)
quantQuibes = inputVetor('Informe as vendas de quibes: ', float)
if len(quantCoxinhas)!=len(quantQuibes):
    print('Dados de vendas inválidos')
else:
    lucroCoxinha=float(input('Informe o lucro por unidade de coxinha: R$ '))
    lucroQuibe=float(input('Informe o lucro por unidade de quibe: R$ '))
    lucro=calculaLucros(quantCoxinhas,quantQuibes,lucroCoxinha,lucroQuibe)
    maior=-math.inf;indM=0
    menor=math.inf;indm=0
    for i in range(len(lucro)):
        if lucro[i]>maior:
            maior=lucro[i]
            indM=i
        if lucro[i]<menor:
            menor=lucro[i]
            indm=i   
    print(f'Lucros: {lucro}\nMaior lucro: R$ {lucro[indM]:.2f}\nMenor lucro: R$ {lucro[indm]:.2f}')
    
from biblioteca import *
import math

def getDivisores(num):
    div=[]
    d=num
    while d!=0:
        if num%d==0:
            result=num/d
            result=int(result)
            div.append(result)
        d-=1
    return div


num= inputVetor('Digite os números: ', int)

if num==[]:
    print('\nNenhum número informado')
else:
    for i in range(len(num)):
        div=getDivisores(num[i])
        if len(div)>2:
            print(f'\n{num[i]} não é um número primo.\nSeus divisores são:')
            print(div)
        else:
            print(f'\n{num[i]} é um número primo.')
        
            
    
    
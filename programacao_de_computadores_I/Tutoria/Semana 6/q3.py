from biblioteca import*

n=float(input('Digite um valor --> '))
vec=[]; vecS=[]; soma=0

while n>=0:
    vec.append(n)
    soma+=n
    vecS.append(soma)
    n=float(input('Digite um valor --> '))
    
print(f'Impressão dos Vetores Resultantes:\nVetor lido:\n{vec}\nVetor soma acumulada:\n{vecS}')
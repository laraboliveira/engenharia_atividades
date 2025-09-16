def Somatorio(x):
    soma=0
    for i in range(1,x+1):
        soma+=(1/i)
    return round(soma,5)
    
def Produtorio(p):
    prod=1
    for i in range(1,p+1):
        prod*=2**(1/i)
    return round(prod,5)

n=int(input('Quantidade de termos (N): '))
while n>0:
    print(f'. O valor de S é {Somatorio(n):.3f}\n. O valor de P é {Produtorio(n):.3f}')
    n=int(input('Quantidade de termos (N): '))
    
    
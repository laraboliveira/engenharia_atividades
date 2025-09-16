n=int(input('Informe o número de parcelas: '))                 #Entrada das parcelas
x=50;y=-80                                                     #Valores do enunciado
a=1;b=1                                                        #Constantes dos valores de x e y da fórmula
i=1                                                            #Auxiliar do fatorial
f=1                                                            #Variável do fatorial
soma=0                                                         #Auxiliar da fórmula

while n<=0:                                                    #Validação da entrada
    n=int(input('Valor inválido para n: '))
 
while i<=n:                                                   
    f*=i                                                       #Cálculo do fatorial
    soma+=((a*x)+(b*y))/f
    a=a+2                                                      #Mudança da constante de x
    b=(b+6)*-1                                                 #Mudança da constante de y
    i=i+1                                                      #Auxiliar do cálculo do fatorial
print(f'Valor do somatório com {n} parcelas: {soma:.2f}')


resp=input('Deseja calcular a Sequência de Collatz (s/S/n/N)? ')
if resp=='s' or resp=='S':
    n=int(input('Digite um número inteiro positivo: '))

while resp=='s' or resp=='S':
    print(f'{n}',end='  ')
    while n!=1:
        op1=n%3
        if op1==0:
            n=n/3
        elif op1==1:
            n=(n*4+2)/3
        elif op1==2:
            n=(2*n-1)/3
        print(f'{n:.0f}',end='  ')
        
    resp=input('\nDeseja calcular a Sequência de Collatz (s/S/n/N)? ')
    while resp!='s' and resp!='S' and resp!='n' and resp!='N':
        resp=input('ERRO: Resposta inválida: ')
    if resp=='s':
        n=int(input('Digite um número inteiro positivo: '))
print('Fim do Programa')
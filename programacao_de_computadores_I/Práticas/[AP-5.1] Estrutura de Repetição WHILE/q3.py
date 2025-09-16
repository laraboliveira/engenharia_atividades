T=float(input('Forneça o capital Total para empréstimo: '))
c=float(input('Forneça o capital emprestado: '))

while T>c:
    m=int(input('Forneça a quantidade de meses para quitação: '))
    if c<=10000:
        t=0.1
    else:
        t=0.07
    j=c*t*m
    jd=c+j
    print(f'Taxa de juros aplicada: {t*100:.0f}%.')
    print(f'Juros devido: {j:.2f}.')
    print(f'Valor total: {jd:.2f}.')
    T=T-c
    c=float(input('Forneça o capital emprestado: '))
        
print(f'Empréstimo negado, capital total é de R$ {T:.2f}.')
c=float(input('Informe o capital emprestado: '))
m = int(input('Informe a quantidade de meses para quitação: '))

if c<=10000:
    t=0.1
else:
    t=0.07

j=c*t*m

print(f'Taxa de juros aplicada: {t*100:.0f}%')
print(f'Juros devido: {j:.2f}')
print(f'Valor total: {j+c:.2f}')

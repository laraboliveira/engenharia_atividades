def impostoRenda (x):
    if x<=1500:
        d=0
    elif x<=2500:
        d=x*0.05
    elif x<=4500:
        d=x*0.1
    else:
        d=x*0.2
    return round(d,2)

   
b=float(input('Digite o salário bruto: '))
inss=b*0.1
fgts=b*0.11
desc= inss+impostoRenda(b)
salL=b-desc

print(f'(-)IR: R$ {impostoRenda(b):.2f}\n(-)INSS: R$ {inss:.2f}\nFGTS: R$ {fgts:.2f}\nTotal de descontos: R$ {desc:.2f}\nSalário Líquido: R$ {salL:.2f}')
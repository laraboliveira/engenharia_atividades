p = float(input('Digite seu peso (em kg): '))
a = float(input('Digite sua altura (em metros): '))
s = input('Seu sexo é masculino (M) ou feminino (F)? ')

imc=p/a**2

if s=='M':
    if imc>25:
        peso=25*a**2
        print(f'Você deve perder {p-peso:.2f}kg para ter IMC = 25')        
    else:
        print('Você não precisa perder peso para ter IMC <= 25')
elif s=='F':
    if imc>24:
        peso=24*a**2
        print(f'Você deve perder {(p-peso):.2f}kg para ter IMC = 24')
    else:
        print('Você não precisa perder peso para ter IMC <= 24')
else:
    print('A entrada contém dados não reconhecidos')
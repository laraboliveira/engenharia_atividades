m14 = float(input('Informe a média móvel dos últimos 14 dias: '))
a6 = int(input('Informe o somatório dos casos dos últimos 6 dias: '))
h = int(input('Informe a quantidade de casos de hoje: '))

m7=(a6+h)/7

d=m7-m14

taxa=d/m14*100

if d<=0:
    print(f'Casos diminuindo em {taxa*-1:.2f}%')
elif d<=15:
    print(f'Casos estáveis em {taxa:.2f}%')
else:
    print(f'Casos aumentando em {taxa:.2f}%')
nota = float(input('Forneça a média no semestre: '))
freq = int(input('Forneça a frequência no semestre: '))

if freq>=75 and nota>=6:
    print('Conceito: aprovado')
elif freq>=75 and nota<6:
    print('Conceito: exame especial')
    val = 6 - nota
    print(f'Justificativa: média {val:.2f} abaixo da mínima')
else:
    print('Conceito: reprovado por faltas')
    val = 75 - freq
    print(f'Justificativa: frequência {val:.0f}% abaixo da mínima')
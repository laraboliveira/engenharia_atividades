def converteMedidas (x):
    ft=0.3048*x
    yd=0.9144*x
    return round(ft,3), round(yd,3)

quant=int(input('Quantidade de percursos: '))
for i in range(1,quant+1):
    print(f'Percurso {i}')
    met=float(input(' - Tamanho em metros: '))
    pe,jardas=converteMedidas(met)
    print(f'  - Tamanho em pés...: {pe:.2f}\n  - Tamanho em jardas: {jardas:.2f}')
import math

i=5;contLinAp=0;somaMassa=0; maior=-math.inf

for i in range (1,i+1,1):
    massaLingote=float(input(f'Digite a massa do lingote {i}: '))
    if massaLingote>24.9:
        contLinAp+=1
        somaMassa+=massaLingote
        if massaLingote>maior:
            maior=massaLingote
        
mediaMassa=somaMassa/contLinAp
print(f'Número de lingotes aproveitados: {contLinAp}\nPeso médio dos lingotes aproveitados: {mediaMassa:.1f} kg\nMaior peso de um lingote aproveitado: {maior} kg')
cand1=input('Forneça o nome do candidato 1: ')
num1=int(input('Forneça o número do candidato 1: '))
cand2=input('Forneça o nome do candidato 2: ')
num2=int(input('Forneça o número do candidato 2: '))
quantElei=int(input('Forneça a quantidade de eleitores: '))
cont1=0;cont2=0;contVal=0;contIn=0

while quantElei<3:
    quantElei=int(input('Forneça a quantidade de eleitores é inferior a 3\nQuantidade de eleitores: '))
print('\n## Votação Iniciada')

for i in range (1,quantElei+1,1):
    vot=int(input('Forneça o número do candidato que deseja votar: '))
    if vot==num1 or vot==num2:
        contVal+=1
        if vot==num1:
            cont1+=1
        else:
            cont2+=1
    else:
        contIn+=1
print('## Votação Encerrada')

if contVal!=0:
    perc1=cont1*100/contVal;perc2=cont2*100/contVal
else:
    perc1=0;perc2=0

percVal=contVal*100/quantElei;percIn=contIn*100/quantElei

print(f'\nVotos válidos: {percVal:.2f}% ({contVal} votos)\nVotos inválidos: {percIn:.2f}% ({contIn} votos)\nVotos para {cand1}: {perc1:.2f}% ({cont1} votos)\nVotos para {cand2}: {perc2:.2f}% ({cont2} votos)')


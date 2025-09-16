numCompet=int(input('Defina a quantidade de apresentações: '))
numJuiz=int(input('Defina a quantidade de juízes: '))

for i in range(1,numCompet+1,1):
    soma=0
    grauDificul=float(input(f' . Apresentação {i}:\n . Defina o grau de dificuldade: '))
    for g in range(1,numJuiz+1,1):
        nota=float(input(f'. Defina a nota do juíz {g}: '))
        soma+=nota
    pont=grauDificul*soma
    print(f'  . Pontuação da apresentação: {pont:.2f}')
n=int(input('Digite o número de alunos: '))
somaMedia=0

for i in range(1,n+1):
    name=input('Digite o nome do aluno 1: ')
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    n3=float(input('Nota 3: '))
    m=(n1*2+n2*3+n3*5)/10
    somaMedia+=m
    print(f'Média Ponderada das notas de Bart: {m:.3f}')
mTurma=somaMedia/n
print(f'Média da turma: {mTurma:.3f}')
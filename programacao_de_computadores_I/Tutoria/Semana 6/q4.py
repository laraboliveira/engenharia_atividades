from biblioteca import*

aluno = [ "Peny", "Rajesh Koothrappali", "Sheldon Cooper", "Howard Wolowitz", "Leonard Hofstadter" ]
notasBCC701 = [ 6.0, 8.5, 10.0, 9.0, 9.5 ]

nota=0

print('Buscando a nota de um aluno...')
nome=input('Digite o nome do(a) aluno(a): ')

for i in range(len(aluno)):
    if nome==aluno[i]:
        nota=notasBCC701[i]

if nota==0:
    print('Erro na busca, aluno(a) não encontrado(a) !')
else:
    print(f'Resultados:\nNome do(a) aluno(a) buscado(a): {nome}\nNota: {nota}')
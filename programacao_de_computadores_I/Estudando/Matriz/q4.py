from biblioteca import*

mat=inputMatriz('Informe a matriz: ', str)

lin=int(input('Informe uma linha: '))
while lin>len(mat)-1:
    lin=int(input('Informe uma linha válida: '))
        
col=int(input('Informe uma coluna: '))
while col>len(mat[0])-1:
    col=int(input('Informe uma coluna válida: '))

print(f'O valor armazenado em [{lin},{col}] é {mat[lin][col]}')




#Sardinha,Salame,Picanha;Coca-cola,Guaraná,Pipoca
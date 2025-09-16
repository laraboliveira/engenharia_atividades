#FUNÇÃO
def Custo(v,t,rg,pg,pa):
    cg=((v*t)/rg)*pg
    ra=rg*0.7
    ca=((v*t)/ra)*pa
    return cg,ca

#PROGRAMA PRINCIPAL
print('Custo do combustível em uma viagem\n')
v=float(input('Velocidade média (km/h): '))
t= float(input('Tempo previsto (h): '))
rg=float(input('Rendimento com gasolina (km/litro): '))
pg=float(input('Preço do litro de gasolina (R$): '))
pa=float(input('Preço do litro do álcool (R$): '))

cg,ca=Custo(v,t,rg,pg,pa)

print(f'\nCusto usando gasolina (R$): {cg:.2f}\nCusto usando álcool (R$): {ca:.2f}')
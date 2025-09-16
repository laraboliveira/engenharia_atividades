n=int(input('Digite o número de termos: '))
pi=0
for i in range(0,n,1):
    pi+=((-1)**i)*(4/(2*i+1))
r=float(input('Digite o raio da esfera: '))
v=4/3*pi*r**3
print(f'pi = {pi:.5f}.\nVolume da esfera = {v:.5f}.')
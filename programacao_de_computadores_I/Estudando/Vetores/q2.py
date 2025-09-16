a=float(input('Digite o valor de "a": '))
b=float(input('Digite o valor de "b": '))
c=float(input('Digite o valor de "c":'))

xi=int(input('Digite o valor inicial de x: '))
xf=int(input('Digite o valor final de x: '))

print(' x   f(x)')
for i in range(xi,xf+1):
    fun=[]
    fun.append(i)
    y=a*i**2+b*i+c
    y=int(y)
    fun.append(y)
    print(fun) 
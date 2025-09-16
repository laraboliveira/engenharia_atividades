import math
t=int(input('Digite o tempo final: '))

print('t   D(t)')
for i in range(0,t+1):
    dis=[]
    dis.append(i)
    g=9.807
    d=(g*i**2)/2
    #d=math.trunc(d)
    dis.append(d)
    print(dis)
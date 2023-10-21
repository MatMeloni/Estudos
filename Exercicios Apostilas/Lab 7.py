import math as m
n=int(input('Valor de n: '))
while n<=0:
    print('Valor invalido')
    n=int(input('Valor de n: '))
s=0
for i in range(1,n+1,1):
    s= s + i/(i*2-1)
print('Somatorio igual a : ',s)
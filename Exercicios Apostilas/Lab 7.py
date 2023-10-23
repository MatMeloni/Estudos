import math as m
n=int(input('Valor de n: '))
while n<=0:
    print('Valor invalido')
    n=int(input('Valor de n: '))
s=0
for i in range(1,n+1,1):
    s= s + i/(i*2-1)
print('Somatorio igual a : ',s)

#Sequencia Lab 7 - Algoritmos e Programação I
import math as m
n=int(input('Valor de n: '))
while n<=0:
    print('Valor invalido')
    n=int(input('Valor de n: '))
x=float(input('Valo de x: '))
while x==0:
    print('Valor Invalido')
    x=float(input('Valor de x:'))
s=0
for i in range(1,n+1,1):
    s= s + ((3*i-1)*(x*i)/(i+2))
print('Somatorio igual a : ',s)
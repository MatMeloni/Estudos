#Aula Laboratorio 8 - 05.10.2023
#Exercicio 1
import math as m

n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
x=float(input('Valor do valor de X: '))  
while x==0:
    print('Valor de X invalid: ')
    x=float(input('Informe o valor de X: '))
s=0
for i in range (1,n+1,1):
    p=(3*i)*m.pow(x,2*i-1)
    s=s+p
print('O valor da Soma é: ',s)

#Exercicio 2
import math as m

n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
x=float(input('Valor do valor de X: '))  
while x==0:
    print('Valor de X invalid: ')
    x=float(input('Informe o valor de X: '))
s=0
c=1
for i in range (1,n+1,1):
    c=-c
    s= s+c*(3*i)*m.pow(x,2*i-1)
print('O valor da Soma é: ',s)

#Exercicio 3
import math as m

n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
x=float(input('Valor do valor de X: '))  
while x==0:
    print('Valor de X invalid: ')
    x=float(input('Informe o valor de X: '))
s=0
c=-1
for i in range (1,n+1,1):
    c=-c
    s= s+c*(3*i)*m.pow(x,2*i-1)
print('O valor da Soma é: ',s)

#materia Nova - Estatisticas
''' Soma, Quantidade, Média, Porcentagem
import random as r
randint(n,m)- aleatórias inteiras entre n e m
random()- aleatorios reais ente 0 e 1 
uniform(n,m) - aleatorios reais entre n e m 
'''
#exercicio 4-

import math as m

n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
sp=0
for i in range(1,n+1):
    x=float(input('Informe o valor de X'))
    if x>0:
        sp=sp+x
print('O valor da Soma dos positivos é: ',sp)

#exercicio 5-
#quantidade de pares
import math as m

n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
qp=0
for i in range(1,n+1):
    x=float(input('Informe o valor de X'))
    if x%2==0:
        qp=qp+1
print('O valor da quantidade de pares é: ',qp)

#exercicio 6-
#Numeros inteiros - % de impares
import math as m

n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
qi=0
for i in range(1,n+1):
    x=float(input('Informe o valor de X'))
    if x%2!=0:
        qi=qi+1
pi=(qi/n)*100
print('O valor da porcentagem de impares é: ', pi, '%')

#Exercicio 7-
#Média dos numeros negativos- numeros reais
import math as m

n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
qneg=0
sneg=0
for i in range(1,n+1):
    x=float(input('Informe o valor de X'))
    if x<0:
        sneg=sneg+x
        qneg=qneg+1
if qneg==0:
    mneg=0
else:
    mneg=sneg/qneg
(print('A média dos negativos é: ', mneg))

#Tarefa Minima -
#Exercicio 1 -
n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
s=0
for i in range(1,n+1,1):
    x=int(input('Valor do X: '))
    if x>0 and x%2==0:
        s=s+x
print('Valor da Soma é: ')

#Exercicio 2 - 
n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
q=0
for i in range(1,n+1,1):
    x=int(input('Valor do X: '))
    if x>0 and x%7==0:
        q=q+1
print('Valor da Quantidade de multiplos de 7 é: ')

#Exercicio 3- 
n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
s=0
q=0
for i in range(1,n+1,1):
    x=int(input('Valor do X: '))
    s=s+x
m=s/n
print('Valor da média é: ',m)

#Exercicio 4- 
import random as r
n=int(input('Informe o valor de n: '))
while n<=0:
    print('Valor de n invalido')
    n=int(input('Informe o valor de n: '))
q=0
for i in range(1,n+1,1):
    x=r.randint(1,100)
    if x%10==0:
        q=q+1
p=(q/n)*100
print('Valor da porcentagem de multiplos de 10: ',p)

#exercicio 5-
n=(input(' informe o valor de n: '))
while n <= 0:
  print(' valor de n invalido!! ')
  n = int(input(' informe o valor de n: '))
qp = 0
qi = 0
for i in range(1, n+1):
  x = float(input(' informe o valor de x: '))
  if x % 2 == 0:
    qp = qp + 1
  else:
    x % 2 != 0
    qi = qi + 1
print('Quantidade pares: ', qp, '\n Quantidade de Impares:', qi)



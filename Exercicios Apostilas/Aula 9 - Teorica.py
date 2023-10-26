#Aula 9 - Teorica 25/10/2023
#Definição da Função
#Exemplo 1

def Area (b1,h1):
    A1=b1*h1
    return A1
#ou podemos fazer 'return b1*h1
def Perimetro (b2,h2):
    P2=(b2+h2)*2
    return P2
def ExibeMsg():
    print('Area e Perimetro de um retangulo: ')

ExibeMsg()
b=float(input('Informe o valor da base: '))
h=float(input('Informe o valor do altura: '))
A=Area(b,h)#Chamada da Função
P=Perimetro(b,h)
print('O Valor da Área é: ',A)#podemos colocar tambem Area(b,h), é necessario apagar ali em cima
print(f'O Valor do perimetro é {P}')

#Exercicio 6.28

import math as m

def Area(A):
  A=((m.pow(a,2)*m.sqrt(3))/2)+3*a*h
  return A
def Volume(V):
  V=(m.pow(a,2)*h*m.sqrt(3))/4
  return V

a=float(input('Informe o valor da Aresta: '))
h=float(input('Informe o valor da Altura: '))
V=Volume
A=Area
print('Valor da Area:',A,'/n Valor da Volume:',V)

#Exercicio 7.23
import math as m

def Função(x):
    y=m.sqrt((m.pow(x,2)+3/2))
    return y

n=int(input('Quantos valores serão calculados: '))
while n<=0:
    print('Valor Invalido de N')
    n=int(input('Digite novamente a quantidade de valores: '))

for i in range (1,n+1):
    x=float(input('Informe o valor de X: '))
    y=Função(x)
    print(f'Para o valor de X = {x}, o resultado é {y}')

#Exercicio 6.30
def Geratriz(G):
  hipotenusa=m.pow(h,2)+m.pow(r,2)
  G=m.pow(hipotenusa,2)
  return G
def Area(A):
  A=m.pi*r*(g+r)
  return A
def Volume(V):
  V=(m.pi*m.pow(r,2)*h)/3
  return V

r=float(input('Informe o valor do raio:'))
h=float(input('Informe o valor da altura:'))

Area=A
Volume=V

print('Valor da area:',A,'/n Valor do volume:',V)

#exercicio 9.24
import math as m
def Serie(n):
    c=1
    s=0
    for i in range (1,n+1):
        s=s+c*i/(2*i-1)
        c=-c
    return c

n=int(input('Quanto valores serão calculados: '))
while n<=0:
    print('Valor Invalido de N')
    n=int(input('Digite novamente a quantidade de valores: '))
s=Serie(n)#chamada da Função
print('O valor da Serie é: ',s)

#Exercicio 9.25
import math as m
def Serie(n,x):
    c=0
    s=0
    for i in range (1,n+1):
        s=s+c*(x/(i+1))
        c=-c
    return s

n=int(input('Quantos valores serão calculados: '))
while n<=0:
    print('Valor Invalido de N')
    n=int(input('Quantos valores serão calculados: '))

x=float(input('Qual o valor da variavel x: '))
while x==0:
    print('Valor de X Invalido')
    x=float(input('Qual o valor da variavel x: '))

s=Serie(n,x)#Chamar a função
print('Valor da Soma da serie é: ',s)


#Exercicio 9.26
import math as m
def Serie(n,x):
    c=-1
    s=0
    for i in range (1,n+1):
        s=s+c*((i+1)*m.pow(x,i))/(2*i+1)
        c=-c
    return s

n=int(input('Quantos valores serão calculados: '))
while n<=0:
    print('Valor Invalido de N')
    n=int(input('Quantos valores serão calculados: '))

x=float(input('Qual o valor da variavel x: '))
while x==0:
    print('Valor de X Invalido')
    x=float(input('Qual o valor da variavel x: '))
s=Serie(n,x)#Chamar a função
print('Valor da Soma da serie é: ',s)

#Exemplo 9.32

def Serie(n,x):
    c=1
    s=0
    for i in range (1,n+1):
        s=s+c*Duvida 
        c=-c
    return s

n=int(input('Quantos valores serão calculados: '))
while n<=0:
    print('Valor Invalido de N')
    n=int(input('Quantos valores serão calculados: '))

x=float(input('Qual o valor da variavel x: '))
while x==0:
    print('Valor de X Invalido')
    x=float(input('Qual o valor da variavel x: '))

s=Serie(n,x)#Chamar a função
print('Valor da Soma da serie é: ',s)

#Exercicio 9.33

def Serie(n,x):
    c=-1
    s=0
    for i in range (1,n+1):
        s=s+c* Duvida de como fazer
        c=-c
    return s

n=int(input('Quantos valores serão calculados: '))
while n<=0:
    print('Valor Invalido de N')
    n=int(input('Quantos valores serão calculados: '))

x=float(input('Qual o valor da variavel x: '))
while x==0:
    print('Valor de X Invalido')
    x=float(input('Qual o valor da variavel x: '))
s=Serie(n,x)#Chamar a função
print('Valor da Soma da serie é: ',s)

#Exercicio 9.37
#Exercicio 9.38
#Exercicio 9.39
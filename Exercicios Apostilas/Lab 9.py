""" Laboratório 8 - Funções - 19/10/2023"""
#Exemplo 1

def mediap (n1, n2, n3):
  m = (2*n1+3*n2+5*n3)/10
  return m

n1 = float(input('Informe o valor de n1: '))
n2 = float(input('Informe o valor de n2: '))
n3 = float(input('Informe o valor de n3; '))

m = mediap (n1, n2, n3)

print ('O valor da média é:', m)
print ('O valor da média é %.2f'%m)
print (f'O valor da média é {m}')



#Exemplo 2

def mediap (a, b, c):
  mp = (2*a + 3*b + 5*c)/10
  return mp

n1 = float(input(" Informe o valor de n1: "))
n2 = float(input(" Informe o valor de n2: "))
n3 = float(input(" Informe o valor de n3: "))
m = mediap(n1, n2, n3) # chamada da função

print("O valor da média é: ", m)
print("O valor da média é: %.2f" %m)
print(f"O valor da média é {m}")

#Exemplo 3

def mediap (a, b, c):
  return (2*a + 3*b + 5*c)/10

n1 = float(input(" Informe o valor de n1: "))
n2 = float(input(" Informe o valor de n2: "))
n3 = float(input(" Informe o valor de n3: "))
m = mediap(n1, n2, n3) # chamada da função

print("O valor da média é: ", m)
print("O valor da média é: %.2f" %m)
print(f"O valor da média é {m}")

#Exemplo 4 
# Definição de uma função

def mediap (a, b, c):
  return (2*a + 3*b + 5*c)/10

def ExibeMensagem():
  print("Este programa exibe a média ponderada de três valores reais\n")

ExibeMensagem()
n1 = float(input(" Informe o valor de n1: "))
n2 = float(input(" Informe o valor de n2: "))
n3 = float(input(" Informe o valor de n3: "))
m = mediap(n1, n2, n3) # chamada da função

print("O valor da média é: ", m)
print("O valor da média é: %.2f" %m)
print(f"O valor da média é {m}")


#Exercicio-1

def CelFar (c):
  f = 9/5 * c + 32
  return f 

c = float(input('Informe a temperatura em Celsius: '))
f = CelFar (c)
print (f' A temperatura em fahrenheit é {f}°')

#Exercicio-2

import math as m 

def  area (r):
  a = 4* m.pi* r **2
  return a

r = float(input('Informe o valor do raio (r):'))
a = area (r)
print ('O valor da área é %.2f'%a)

#Exercicio-3

import math as m 

def volume (r):
  v = (4/3)* m.pi*r**3
  return v

r = float(input('Informe o valor do raio (r):'))
v = volume (r)
print ('O valor do volume da esfera é %.2f'%v)

#Exercicio-4

def maior (n1, n2, n3):
  m=n1
  if n2> m:
    m=n2
  if n3 > m:
    m=n3
  return m   

n1 = float(input('Informe o valor de n1: '))
n2 =float(input('Informe o valor de n2: '))
n3 =float(input('Informe o valor de n3: '))
m = maior (n1, n2, n3)
print ('O maior valor é: ', m)

#Exercicio-5
import math as m

def modulo(x):
  if x<0:
    return -x
  else:
    return x
  
x=float(input('Qual o valor de X: '))
y=modulo(x)
print('Para x=',x,' O valor do modulo é: ',y)

#Exercicio-6
import math as m

def Area (A):
  A=2*m.sqrt(3*m.pow(a,2))
  return A
def Volume (V):
  V=1/3*m.sqrt(2*m.pow(a,3))
  return V

a=float(input('Qual o valor da aresta: '))
V=Volume
A=Area

print('O valor do Volume é de :',V, 'O valor da Area é de: ',A)

#Exercicio-7
import math as m

def Altura(h):
  h=(a*m.sqrt(6))/3
  return h
def Area(A):
  A=m.pow(a,2)*m.sqrt(3)
  return A
def Volume(V):
  V=m.pow(a,3)*m.sqrt(2)/12
  return V

a=float(input('Qual o valor da Aresta:'))
V=volume
A=Area
h=Altura
print('Valor da Area:',A,' Valor da Altura',h,'Valor do Volume:',V)

#Exercicio-8 
import math as m

def Função(f):
  if x<0:
    f=m.sqrt(m.fabs(x))
  elif x>=0 or x<=1:
    f=m.pow(x,2)
  else:
    f=m.log(x,5)

x=float(input('Informe o valor de x: '))
f=Função
print('Valor da função: ',f)

#Lista Complementar
#Exercicio 1
def Distancia(d):
  d=m.sqrt(m.pow(xfinal-xinicial,2)+m.pow(yfinal-yinicial,2)+m.pow(zfinal-zinicial,2))
xinicial=float(input('Valor inicial de x:'))
xfinal=float(input('Valor final de x:'))
yinicial=float(input('Valor inicial de y:'))
yfinal=float(input('Valor final de y:'))
zinicial=float(input('Valor inicial de z:'))
zfinal=float(input('Valor final de z:'))

D=Distancia

print('Valor da função da distancia é de: ',D)

#Exercicio 2
import math as m

def Area(A):
  A=((m.pow(a,2)*m.sqrt(3))/2)+3*a*h
def Volume(V):
  V=(m.pow(a,2)*h*m.sqrt(3))/4

a=float(input('Informe o valor da Aresta: '))
h=float(input('Informe o valor da Altura: '))
Volume=V
Area=A
print('Valor da Area:',A,'/n Valor da Volume:',V)

#Exercicio 3
import math as m

def Geratriz(G):
  hipotenusa=m.pow(h,2)+m.pow(r,2)
  G=m.pow(hipotenusa,2)
def Area(A):
  A=m.pi*r*(g+r)
def Volume(V):
  V=(m.pi*m.pow(r,2)*h)/3
r=float(input('Informe o valor do raio:'))
h=float(input('Informe o valor da altura:'))
Area=A
Volume=V
print('Valor da area:',A,'/n Valor do volume:',V)

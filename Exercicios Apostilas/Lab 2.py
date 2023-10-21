#Lab 2 - Tarefa Complementar

#Exercício 3.25

import math

S=float(input("Qual a medida da largura: "))
a=2/math.sqrt(3)*S
D=2*a
S=(math.sqrt(3)/2)*D
A=3/2*math.pow(a,2)*math.sqrt(3)
print("A area do hexagono é de: ",A)
print("A Aresta do hexagono mede: ",a)
print("A Diagonal deste hexagono tem a medida de: ",D)

#Exercício 2.49

import math

r=float(input("Qual o raio da esferas: "))
a=float(input("Qual o valor da dimensao A:"))
b=float(input("Qual o valor da dimensao B:"))
h=float(input("Qual o valor da dimensao H:"))
Am=2*math.pi*r*h
Ao=math.pi*(2*r*h+math.pow(a,2)+math.pow(b,2))
V=1/6*math.pi*h*(3*math.pow(a,2)+3*math.pow(b,2)+math.pow(h,2))
print("A Área Lateral Am é de:",Am)
print("A Área Exterior Ao é de :",Ao)
print("O Volume é de: ",V)

#Exercicio 2

import math

a=float(input("Lado A:"))
b=float(input("Lado B:"))
area=a*b
per=2*(a+b)
print("valor a area:",area)
print("valor do perimetro",per)

#Exercicio 3

import math

r=float(input("valor do raio:"))
a=math.pi*math.pow(r,2)
c=2*math.pi*r
print("valor da area",a)
print("valor da circunferencia",c)
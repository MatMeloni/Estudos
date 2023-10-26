'''Lab 10 - Algoritmos e Programação I

Exercicio que nao estao na lista, são para fixação da materia

Exemplo 1A
Dado o valor do raio da circunferência, defina duas funções em Python, uma para calcular a área do circulo e outra para calcular o perímetro da circunferência.'''

import math as m
def Area(r):
    A=m.pi*r*r
    return A

def Perimetro(r):
    P=2*m.pi*r
    return r

r=float(input('Informe o valor do raio: '))
A=Area
P=Perimetro #Chamar a função
print (f'O perimetro é: {P}, A Area é: {A}')
print ('Os valores da área e do perimetro sao: %.4f e %.2f'%(A,P))

''' Exemplo 1B
-Dado o valor do raio da circunferência, defina UMA únaca função em Python, uma para calcular a área do circulo e o perímetro da circunferência.'''

import math as m

def Circulo(r):
    global A,P
    A = m.pi*r*r
    P=2*m.pi*r

r=float(input('Informe o valor do raio: '))
Circulo(r)
print('O Valor da Area: ',A)
print('O Valor do perimetro: ',P)

'''Exemplo 2A
Dado um valor de x real, pede=se definir 3 funções. A primeira deverá calcular e retornar o dobro deste numero, a segunda o triplo e a terceira função a metade'''

import math as m
def dobro(x):
    return 2*x 

def triplo(x):
    return 3*x

def metade(x):
    return x/2

x=float(input(' Informe o valor de x:'))
d=dobro(x)
t=triplo(x)
m=metade(x)
print(f'O dobro do numer {x} é {d}, o triplo é {t} e a metade é {m}')

'''Exemplo 2B
Dado um valor de x real, pede-se definir 1 função que deverá calcular e retornar o dobro deste numero, o triplo e a metade'''

import math as m
def Calculo(x):
    global d,t,m
    d=2*x
    t=3*x
    m=x/2

x=float(input(' Informe o valor de x:'))
Calculo(x)
print(f'O dobro do numer {x} é {d}, o triplo é {t} e a metade é {m}')

'''Exemplo 3A
-Elaborar um programa python que realize a troca do conteudo entre duas variaveis
'''

a=float(input('Informe o valor de A: '))
b=float(input('Informe o valor de B: '))
aux=b
b=a
a=aux
print(f'Os valores de A e B após a troca são: {a} e {b}')

'''Exemplo 3B
-Elaborar um programa python, que chame uma função que troque o conteúdo de duas variáveis reais.
'''
def Troca():
    global a, b
    aux=a
    a=b
    b=aux

a=float(input('Informe o valor de A: '))
b=float(input('Informe o valor de B: '))
Troca()
print(f'Os valores de A e B após a troca são: {a} e {b}')

'''            Inicio da Atividade Minima
Exercicio 1 -  Faça  um  programa,  utilizando  funções,  que  receba  três  números  inteiros  e  positivos,  e  que  forneça  a 
soma desses três números.

Para este exercício crie três funções: 

• entrada() - retorna um número digitado (fazer a verificação se é positivo);  
• calculaSoma(a, b, c) - recebe 3 números inteiros e positivos e retorna a soma deles; 
• main() - chamada das funções criadas (chama 3 vezes a entrada, sendo uma para cada número e a 
função para somar) e depois mostre o resultado.  '''

def entrada():
    x=int(input('Valor do X:'))
    while x<1:
        print('Digite um numero positivo!')
        x=int(input('Valor do X:'))
    return x
def calculaSoma(a,b,c):
    s=(a+b+c)
    return s

def main():
    a=entrada()
    b=entrada()
    c=entrada()
    s=calculaSoma(a,b,c)
print(f'{a}+{b}+{c}={s}')

'''Exercicio 2 - Faça um programa, utilizando funções, que terá um número inteiro como entrada  e a função retornará o caractere "P", se o número for positivo (> 0),  "N", se o número for negativo (< 0) e "Zero" se o número for igual a zero.  
Para este exercício crie duas funções: 
• verifica(a) - recebe o número e retorna "P" (> 0), "N" (< 0) ou "Zero" (igual a 0). 
• main() - digita um número, faz a chamada à função verifica e depois mostra o resultado..  '''

def main():
    x=int(input('Valor do X:'))
    a=verificar(x)
    print('O numero é: ',a)

def verificar(a):
    if a>0:
        resp='P' 
    elif a==0:
        resp='z'
    else:
        resp='n'
    return resp
main()

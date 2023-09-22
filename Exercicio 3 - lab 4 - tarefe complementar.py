'''
Elabore um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:

1- Telefonou para a vítimia?
2- Esteve no local do crime?
3- Mora perto da vítima?
4- Devia para a vítima?
5- Ja trabalhou com a vitima?

O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder Sim a 2 questões ela deve ser classificada 
como 'suspeita', entre 3 e 4 "cumplice" e 5 como "Assasino". Caso Contrário, ela sera classificada como "inocente" '''
n=0
a=int(input('Telefonou para a vitima?\n'
            '(1)Sim\n'
            '(2)Não\n'))
while a<1 or a>3:
    print('Valor errado')
    a=int(input('Telefonou para a vitima?\n'
            '(1)Sim\n'
            '(2)Não\n'))
if a==1:
    n=n+1
else:
    n=n+0
b=int(input('Esteve no local do crime?\n'
            '(1)Sim\n'
            '(2)Não\n'))
while b<1 or b>3:
    print('Valor errado')
    b=int(input('Esteve no local do crime?\n'
            '(1)Sim\n'
            '(2)Não\n'))
if b==1:
    n=n+1
else:
    n=n+0
c=int(input('Mora peto da vitima?\n'
            '(1)Sim\n'
            '(2)Não\n'))
while c<1 or c>3:
    print('Valor errado')
    c=int(input('Mora peto da vitima?\n'
            '(1)Sim\n'
            '(2)Não\n'))
if c==1:
    n=n+1
else:
    n=n+0
d=int(input('Devia para a vitima?\n'
            '(1)Sim\n'
            '(2)Não\n'))
while d<1 or d>3:
    print('Valor errado')
    d=int(input('Devia para a vitima?\n'
            '(1)Sim\n'
            '(2)Não\n'))
if d==1:
    n=n+1
else:
    n=n+0
e=int(input('Ja trabalhou com a vitima?\n'
            '(1)Sim\n'
            '(2)Não\n'))
while e<1 or e>3:
    print('Valor errado')
    e=int(input('Ja trabalhou com a vitima?\n'
            '(1)Sim\n'
            '(2)Não\n'))
if e==1:
    n=n+1
else:
    n=n+0

while n<0 or n>5:
    print('Contagem Errada')

print('A pessoa tem um total de: ',n,'\n')
if n==2:
    print('Suspeita')
elif n==3 or n==4:
    print('Cumplice')
elif n==5:
    print('Assasino')
else:
    print('Inocente')
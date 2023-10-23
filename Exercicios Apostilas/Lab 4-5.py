#Lab 4-5
'''Exercicio 1 

Um hospital precisa de um programa para calcular e imprimir os gastos de um paciente.

Escreva um programa que leia:
- o Número de dias gastos do hospital:
- o tipo de quarto:
- se usou ou não o WIFI (Sim Ou Não):
- Se usou ou não a TV a CaBO (Sim ou Não):

Ao final, emita um relatório:

'''

print('  Quartos: \n\n'
      '- (1) Particular -       R$ 360,00\n'
      '- (2) Semi-Particular -  R$ 210,00\n'
      '- (3) Coletivo -         R$ 185,00\n\n' 
      '  WiFi - R$3,00\n'
      '  TV a cabo - R$4,00\n\n'
      '(Valores referentes a diaria)\n'
      '***************************************\n')

n=int(input('Quantos dias o paciente ficou no hospital? \n'))
while n<1:
    print('Valor invalido\n')
    n=int(input('Quantos dias o paciente ficou no hosptal? \n'))

tipo=int(input('Qual o tipo do quarto?\n'))
while tipo<0 or tipo>3:
    print('Tipo de quarto invalido\n')
    tipo=int(input('Qual o tipo do quarto?\n'))


if tipo==1:
    tipo=('Particular')
    soma=360*n
elif tipo==2:
    tipo=('Semi-Particular')
    soma=210*n
else:
    tipo=('Coletivo')
    soma=185*n

wifi=int(input('O paciente usou o Wifi? \n'
         '(1)Sim: \n'
         '(2)Não: \n'))
while wifi<1 or wifi>3:
    print('Valor invalido')
    wifi=int('O paciente usou o Wifi? \n'
         '(1)Sim: \n'
         '(2)Não: \n')
    
if wifi==1:
    wifi1=3*n
else:
    wifi1=0

tv=int(input('O paciente usou o Tv a cabo? \n'
         '(1)Sim: \n'
         '(2)Não: \n'))
while tv<0 or tv>3:
    print('Valor invalido')
    tv=int('O paciente usou a Tv a cabo? \n'
         '(1)Sim: \n'
         '(2)Não: \n')
if tv==1:
    tv1=4*n
else:
    tv1=0


Total=soma+wifi1+tv1
print('Conta do Paciente: \n'
      'Número de dias no hospital:.R$',n,'\n'
      'Tipo de quarto:.............R$',tipo,'\n'
      'Diárias:....................R$',soma,'\n'
      'Wifi:.......................R$',wifi1,'\n'
      'TV a cabo:..................R$',tv1,'\n'
      'Total:......................R$',Total)

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

'''Elabora um programa para a partir de uma medida em metros, criar um menu de opções para converte-lo em outroaas unidades internacionais de medida
Fazer validação com mensagem de erro personalizada;

'''
print('  Conversão: \n\n'
      '- (1) Metros - Jardas       \n'
      '- (2) Quilometro - Milhas   \n'
      '- (3) Milimitro - Pes       \n'
      '- (4) Milimetro - Polegadas \n') 

metros=float(input('Qual a medida de metros deseja converter? \n'))
while metros<0:
    print('Valor invalido, é necessário um valor positivo para fazer a conversão')
    metros=float(input('Qual a medida de metros deseja converter? \n'))
op=int(input('Qual a opção de conversão: \n'))
while op<0 or op>4:
    print('Valor invalido, é necessario um valo de 1 a 4: ')
    op=int(input('Qual a opção de conversão: \n'))
if op==1:
    jardas=metros*1.09361
    print('Valor do conversão: ',jardas,'\n')
elif op==2:
    milhas=metros*0.000621371
    print('valor de conversão: ',milhas,'\n')
elif op==3:
    pes=(metros*1000)/304.8
    print('valor de conversão: ',pes,'\n')
elif op==4:
    Polegadas=(metros*1000)/25.4
    print('valor de conversão: ',Polegadas,'\n')
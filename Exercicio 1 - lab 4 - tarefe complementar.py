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






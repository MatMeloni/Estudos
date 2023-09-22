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


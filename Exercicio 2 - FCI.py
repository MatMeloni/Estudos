preco=float(input('Qual o preço do produto: \n'))
print('\n condições de pagamento:'
      '\n 1- A vista em dinheiro ou cheque, recebe %10 de desconto'
      '\n 2- A vista em cartão de crédito, recebe %5 de desconto'
      '\n 3- Em 2 vezes, preço normal de etiqueta sem juros'
      '\n 4- Em 3 vezes, preço normal de etiqueta mais juros de %10 \n')
condicao=int(input('Digite o codigo da condição de pagamento: '))
print('preço da etiqueta:R$',preco)
if condicao==1:
    preco=preco*0.9
elif condicao==2:
    preco=preco*0.95
elif condicao==3:
    preco=preco
elif condicao==4:
    preco=preco*1.1
else:
    print('Condição de pagamento invalida:')
print('Preço a pagar: R$',preco)
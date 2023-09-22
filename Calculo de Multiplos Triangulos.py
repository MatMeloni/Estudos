n = int(input(' Informe o valor de n: '))
while n <= 0:
  print(' Valor de n invalido!!!')
i = 1
while i <= n:
  print(' \n Triangulo ', i)
  b = float(input(' Informe o valor da base b: '))
  while b <= 0:
    print(' Valor de base invalido!!!')
    b = float(input(' Informe o valor da base b: '))
  h = float(input(' Informe o valor da altura h: '))
  while h <= 0:
    print(' Valor da altura invalido!!!')
    h = float(input(' Informe o valor da altura h: '))
  A = b*h/2
  print(' O valor da área é: ' , A)
  print(' O valor da área é: %.2f ' %A)
  i = i + 1

import math as m

n=int(input('Informe o valor de cilindros - valor de n: '))
while n<=0:
    print('Quantidade de cilindros invalida!!')
    n=int(input('Informe o valor de cilindros - valor de n: '))
i=1
while i<=n:
    print('\n\n Cilindro',i)    

    r=float(input('Informe o valor do raio: '))
    while r<=0:
        print('Valor do raio invalido')
        r=float(input('Infome o valor do raio: '))
    h1=float(input('Informe o valor da Altura 1: ')) 
    while h1<=0:
        print('Valor da Altura 1 invalida')
        h1=float(input('Informe o valor da Altra 1: '))
    h2=float(input('Informe o valor da Altura 2: '))
    while h2<=0 or h2<=h1:
        print('Valor da Altura 2 invalda')
        h2=float(input('Informe o valor da Altura 2:'))
    a=m.pi*r*(h1+h2)
    v=m.pi*r**2*(h1+h2)/2
    print('Os valores da área e do volume são %.2f e %.2f' %(a,v))
    i=i+1

#Lab 1 - Tarefa Complementar
#Exercicio 1

c= float(input('informe a temperatura em graus celsius'))
F= c*1,8+32
K= c+273,15
print('O valor da temperatura em kelvin é : ',K, 'e em farenheit é: ',F)

#Exercicio 2

r1= float(input('informe a primeira resistencia'))
r2= float(input('informe a segunda resistencia'))
r3= float(input('informe a terceira resistencia'))
rs= r1+r2+r3
rp=1/((1/r1)+(1/r2)+(1/r3))
print('O valor das resistencia em paralelo é:', rp , 'e das resistencias em série:',rs)
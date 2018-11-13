a=float(input('Entre com a reta A:'))
b=float(input('Entre com a reta B:'))
c=float(input('Entre com a reta C:'))

if(a+b>c and b+c>a and c+a>b):
    print('O triângulo PODE ser formado')
else:
    print('O triângulo, NÃO PODE ser formado')



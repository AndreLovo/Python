a=float(input('Entre com a reta A:'))
b=float(input('Entre com a reta B:'))
c=float(input('Entre com a reta C:'))
#Condição aninhada
if(a+b>c and b+c>a and c+a>b):
    print('Os segmentos acima PODEM FORMAR um triângulo ',end=' ')
    if a==b==c:
        print('EQUILÁTERO!')
    elif a!=b!=c!=a:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('O triângulo, NÃO PODE ser formado')

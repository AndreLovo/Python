num=int(input('Entre com um número inteiro qualquer: '))
c=num
f=1
print('CALCULANDO {}!= '.format(num), end='')
while c>0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    f*=c
    c-=1
print('O fatorial de {}! é: {}'.format(num,f))
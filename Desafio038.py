n1=int(input('Entre com o 1º número:'))
n2=int(input('Entre com o 2º número:'))

if(n1==n2):
    print('Não existe valor maior. Os valores {} e {} são iguais'.format(n1,n2))
elif(n1>n2):
    print('O primeiro valor {} é maior'.format(n1))
else:
    print('O segundo valor {} é maior'.format(n2))

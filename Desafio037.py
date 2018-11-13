x=int(input('Entre com um número inteiro:'))
print(""""
Escolha uma das bases de conversão:
[1] Conversão para BINÁRIO
[2] Conversão para OCTAL
[3] Conersão para HEXADECIMAL
""")
c=int(input('Escolha uma opção:'))
if c==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(x, bin(x)))
elif c==2:
    print('{} convertido para OCTAL é igual a {}'.format(x, oct(x)))
elif c==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(x, hex(x)))
else:
    print('Opção invalida!!Tente novamente!!')



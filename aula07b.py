n1 = int(input('Entre com um valor: '))
n2 = int(input('Entre com um outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}, o produto vale {} e a divisão é {:.3f}'.format(s, m, d), end='')
print(' divisão inteira {} e a potência {}'.format(di, e))
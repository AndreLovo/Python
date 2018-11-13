n1= float(input('Entre com a primeira nota: '))
n2= float (input('Entre com a segunda nota:'))
n= (n1+n2)/2
print('A sua media foi {:.2f}'.format(n))
#if n>= 6.0:
#    print('Sua media foi boa. PARABÉNS!')
#else:
#    print('Sua media foi ruim. ESTUDE MAIS!')
print('PARABENS!' if n>=6 else 'ESTUDE MAIS!')

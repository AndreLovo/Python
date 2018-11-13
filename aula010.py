tempo=int(input('Quantos anos tem seu carro?'))
if tempo<=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

#ou

tempo=int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo<=3 else'carro velho')
print('--FIM--')
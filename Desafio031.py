d=float(input('Entre com a distância da viagem:'))
print(d)
if(d<=200):
    print('O valor da passagem é de: R${}'.format(d*0.50))
else:
    print('O valor da passagem é de: R${}'.format(d * 0.45))

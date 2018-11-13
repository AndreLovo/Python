v=float(input('Entre com a velocidade do carro:'))
if(v <=80.0):
    print('Você está com a velocidade de:{} Km/h'.format(v))
else:
    print('Você esta acima da velocidade, e está à:{} Km/h e sua multa será de R${:.3f}'.format(v,((v-80)*7)))


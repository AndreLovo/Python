preçotot=0
dist=float(input('Quantos Km foram percorridos? '))
dias=float(input('Quantos dias o carro ficou alugado?'))
preçotot=((dist*0.15)+(dias*60))
print('O preço total a pagar é de R${:.2f}'.format(preçotot))


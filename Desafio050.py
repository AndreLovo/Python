s=0
cont=0
for c in range(1,7):
    n=int(input('Entre com um número inteiro qualquer: '.format(c)))
    if n%2==0:
        s+=n
        cont+=1
print('A soma dos VALORES PARES dos {} números digitados é: {}'.format(cont,s))

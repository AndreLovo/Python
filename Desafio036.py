#Aprovação empréstimo bancário
casa=float(input('Entre com o preço da casa:'))
sal=float(input('Entre com o salário comprador: '))
anos=float(input('Número de anos que ele vai levar pagar a casa: '))

print('O valor da casa é de:R${:.2f}'.format(casa))
print('O salário do trabalhador é de:R${:.2f}'.format(sal))
print('O número de anos é de:R${:.2f}'.format(anos))

print('O valor da Prestação Mensal é de:R${}'.format(casa/anos))
if((casa/anos)>=(sal*0.3)):
    print('O finaciamento NÃO pode ocorrer!')
else:
    print('O financiamento está APROVADO!')



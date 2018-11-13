s=float(input('Entre com o valor do salário: R$ '))
if(s>1250.00):
    print('O novo salário será de: R${:.2f}'.format(s*1.10))
else:
    print('O novo salário será de: R$ {:.2f}'.format(s*1.15))
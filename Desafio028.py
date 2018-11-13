import random
num= random.randint(0,5)
x =int(input('Entre com um valor inteiro entre 0 e 5:'))
print('Você entro com o valor:{}'.format(x))
print('O sistema entrou com o valor:{}'.format(num))
if(num==x):
    print('Você acertou o número: PARABÉNS!!')
else:
    print('Você ERROU o número. TENTE OUTRA VEZ!')




#https://www.youtube.com/watch?v=ei2Kr3ccfO0&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=2

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont=('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
   num=int(input('Entre com o numero entre 0 e 20: '))
   if  0<=num<=20:
        break
   print('Tente novamente. ', end='')
print('Voce digitou o numero {cont[num]}.')
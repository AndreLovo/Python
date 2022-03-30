# 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print('==' * 30)

num = (int(input('Digite um número: ')),
       int(input('Digite um outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print('==' * 30)

print(f'Você digitou os valores {num}')

print('==' * 30)

#A)
print(f'O valor 9 apareceu {num.count(9)} vezes!')

print('==' * 30)

#B)
if 3 in num:
     print(f'O valor 3 apareceu nas seguintes posições: {num.index(3)+1} !')
else:
     print(f'O valor 3 não foi digitado!') 

print('==' * 30)

#C)
print(f'Os valores pares digitados foram: ', end='')
for n in num:
 if n % 2==0:
    print(n, end=' ')
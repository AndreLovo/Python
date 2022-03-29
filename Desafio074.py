#  074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10))

print('\nOs valores sorteados foram: -', end='')
for n in numeros:
    print(f'{n}', end='')

print(f'\n O maior valor foi: {max(numeros)}')
print(f'\nO menor valor foi: {min(numeros)}')
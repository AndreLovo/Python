v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite mais um valor: '))
v4 = int(input('Digite o último valor: '))
num = (v1, v2, v3, v4)
print(f'Os valores digitados foram: {num}')
if num.count(9) == 1:
    print(f'O número 9 apareceu {num.count(9)} vez')
elif num.count(9) == 0:
    print('O número 9 não foi digitado')
else:
    print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro número 3 foi digitado na {num.index(3) + 1}ª posição')
else:
    print('Não tem nenhum número 3 nos valores digitados')
print('Os valores pares digitados foram: ', end = '')
for p in num:
    if p % 2 == 0:
        print(p, end=' ')

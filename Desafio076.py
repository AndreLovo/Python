# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-' * 40)
listagem = ('lapis', 1.75,
           'borracha', 2,
           'caderno', 15.90,
           'estojo', 4.20,
           'transferidor', 9.99,
           'mochila', 120.32,
           'canetas', 22.30,
           'livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2==0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

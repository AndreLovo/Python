#  Crie um programa que tenha uma tupla com várias palavras. Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
print('-' * 80)

palavras=('aprender','programar','linguagem','python','curso','grátis','estudar','praticar',
          'trabalhar','mercado')

print('-' * 80)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ')
    for letra in p:
     if letra.lower() in 'aáàãeéioóuú':
        print(letra, end=' ')
        
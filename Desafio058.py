from random import randint
computador=randint(0,10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Tente adivinhar! Qual foi?')
acertou=False
palpites=0
while not acertou:
    jogador =int (input('Qual é o seu palpite?'))
    palpites+=1
    if jogador == computador:
        acertou = True
    else:
        if jogador<computador:
            print('Mais...tente mais uma vez.')
        elif jogador>computador:
            print('Menos...tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
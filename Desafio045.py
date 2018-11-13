from random import randint
from time import sleep
itens=('Pedra','Papel','Tesoura')
# itens nas posicoes 0,1,2
computador= randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador= int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador==0: #computador jogou pedra
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCEU')
    elif jogador ==2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif computador==1: #computador jogou papel
    if jogador ==0:
        print('COMPUTADOR VENCEU')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif computador==2: #computador jogou tesoura
    if jogador ==0:
        print('JOGADOR VENCEU')
    elif jogador ==1:
        print('COMPUTADOR VENCEU')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

from random import randint
V=0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    jogador = int(input('Diga um valor: '))
    computador=randint(0,10)
    total= jogador+computador
    tipo=' '
    while tipo not in 'PpIi':
        tipo=str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total deu : {total}', end=' ')
    print('O resultado é PAR' if total % 2 ==0 else 'O resultado é ÍMPAR')
    if tipo=='P':
        if total % 2 == 0:
           print('VOCÊ VENCEU!!')
           v=+1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo =='I':
        if total % 2 == 1:
           print('VOCÊ VENCEU!!')
           v=+1
        else:
            print('VOCÊ PERDEU!')
            break
        print('VAMOS JOGAR NOVAMENTE...')
print(f'GAME OVER! Você venceu {v} vez(es).')



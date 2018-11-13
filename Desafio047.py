#QUANTIDADE DE RETIÇÕES DO LAÇO
for n in range(1,51):
    print('.', end='')
    if n%2==0:
        print(n, end=' ')
print('ACABOU')

#FAÇO METADE DOS LAÇOS PARA O MESMO RESULTADO
for n in range(2,51,2):
    print(n, end=' ')
print('ACABOU')
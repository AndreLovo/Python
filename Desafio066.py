s=cont=0
while True:
    n=int(input('Entre com um número inteiro qualquer [999 para PARAR]: '))
    if n==999:
        break
    cont+=1
    s+=n
print('Foram digitados {} números e a soma deles é {}.'.format(cont,s))




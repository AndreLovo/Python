num= int(input('Digite eum número para ver a sua tabuada: '))
for c in range(1,11):
    print('{} X {:2} = {}'.format(num,c,num*c))
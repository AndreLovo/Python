s=0
c=0
#CONTANDO OS VALORES IMPARES:
for n in range (1,501,2):
#SOMANDO OS VALORES QUE SÃO MULTIPLOS DE 3:
    if n%3==0:
        c+=1
        s+=n
print('A soma dos {} números impares entre 1 e 500 é: {}'.format(c,s))
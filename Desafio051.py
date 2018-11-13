p= int(input('Primeiro termo: '))
r= int(input('Razão desta PA: '))
d = p+(10-1)*r
print('O primeiro termo, a razão e o décimo termos desta P.A.são: {},{},{}'.format(p,r,d))
for c in range(p,d+r,r):
    print(c, end=' ')
print('->ACABOU')
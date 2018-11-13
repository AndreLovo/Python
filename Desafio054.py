#Análise de Dados
s=0
m=0
from datetime import date
atual= date.today().year
for c in range(0,3,1):
    a= int(input('Entre com o ano de nascimento:'.format(c)))
    if (atual-a>=21):
        s+=c
        print('Temos {} pessoas maiores de idade'.format(s))
    elif(atual-a<21):
        m+=c
        print('Temos {} pessoas menores de idade'.format(m))


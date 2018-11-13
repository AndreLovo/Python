from datetime import date
atual= date.today().year
d=int(input('Entre com o ano de seu nascimento: '))
idade= atual-d

print('Quem nasceu em {} tem {} anos em {}'.format(d, idade, atual))
if(idade==18):
    print('Você tem que se alistar AGORA!!')
elif(idade>18):

    print('Você está com {} anos e você está atrasado {} anos para você se alistar'.format(idade,(idade-18)))
else:
    print('Você ainda vai se alistar e estão faltando {} anos'.format(18-idade))
from datetime import date
atual= date.today().year
ano= int(input('Entre com o ano de nascimento:'))
print('O ano que você nasceu é:{}'.format(ano))
idade=atual-ano
if(idade==18):
    print('Está na hora de você se alistar')
elif(idade>18):
    print('Você está com {} anos e você está atrasado {} para você se alistar'.format(idade,(idade-18)))
else:
    print('Você está com {} e ainda vai se alistar e estão faltando {} anos'.format(idade,(idade+18)))
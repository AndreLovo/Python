from datetime import date
ano= int(input('Entre com o ano de nascimento:'))
atual= date.today().year
idade=(atual-ano)
print('Você tem {} anos'.format(idade))

if(idade<=9):
    print('Você nasceu em {} e sua categoria é a MIRIM'.format(ano))
elif(idade<=14):
    print('Você nasceu em {} e sua categoria é a INFANTIL'.format(ano))
elif (idade<=19):
    print('Você nasceu em {} e sua categoria é a JÚNIOR'.format(ano))
elif(idade<=25):
    print('Você nasceu em {} e sua categoria é a SENIOR'.format(ano))
else:
    print('Você tem acima de 20 anos e sua categoria é MASTER.')

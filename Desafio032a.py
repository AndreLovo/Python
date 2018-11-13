ano= int(input('Que ano quer analisar? '))
if ano%4 ==0 and ano%100!=0 or ano%400==0 :
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} NÃO é Bissexto'.format(ano))

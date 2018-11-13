
sexo=str(input('Entre com o sexo da pessoa [M/F]:')).strip().upper()[0]
while sexo!='M' and sexo!='F':
    print('Entre novamente com o soxo da pessoa!')

    print('Você entrou com o sexo: {}'.format(sexo))
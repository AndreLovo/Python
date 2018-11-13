n1= float(input('Entre com a nota 1: '))
n2= float(input('Entre com a nota 2: '))
m= float((n1+n2)/2)
print('A nota 1 é:{:.1f}'.format(n1))
print('A nota 2 é:{:.1f}'.format(n2))
print('A media é:{:.1f}'.format(m))
if m<5.0:
    print('A média é de {:.1f}, e o aluno está REPROVADO!'.format(m))
elif 6.9> m >=5:
#elif m>=5.0 and m<=6.9:
    print('A media do aluno é {:.1f}, e o aluno está em RECUPERAÇÃO'.format(m))
else:
    print('A media do aluno é {:.1f}, e o aluno está APROVADO'.format(m))





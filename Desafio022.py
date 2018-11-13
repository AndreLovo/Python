#Trabalho com stringues:
#strip REMOVE OS ESPAÇOS DA FRASE.

nome= str(input('Entre com o nome completo:')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
print(nome.find(' '))


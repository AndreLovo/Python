import random
n1= str(input('Primeiro aluno: '))
n2= str(input('Segundo aluno: '))
n3= str(input('Terceiro aluno: '))
n4= str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]#crio uma lista para guardar os elementos
escolhido= random.choice(lista)
print('O escolhido foi:{}'.format(escolhido))

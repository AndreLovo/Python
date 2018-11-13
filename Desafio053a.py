#Entro com a frase e já deixo tudo em maiúsculo
frase= str(input('Digite uma frase: ')).strip().upper()
#Aula Mundo 1 - Tratamento de Strings
#Separei as palavras
palavras= frase.split()
junto= ''.join(palavras)
#FATIAMENTO DE PYTHON
inverso=junto[::-1]
print(junto, inverso)
if inverso==junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!!')

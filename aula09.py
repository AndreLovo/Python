# Operações

# Função de Fatiamento:
frase= 'Curso em Video Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Função de Análise:
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase) #operador lógico

#Funcionalidades Transformação:
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

#Elimina os espaços - strip
frase1= '   Aprenda Python  '
print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())

#Função de Divisão:
print(frase.split())

#Funçaõ de Juntar (Junção)
print('-'.join(frase))


a= int(input('Primeiro valor: '))
b= int(input('Segundo valor: '))
c= int(input('Terceiro valor: '))
#Verificando quem é menor: Já sei que "a" é menor então testo a
# condição de "a" ser maior que b e ...
menor=a
if b < a and b < c:
    menor=b
if c < a and c < b:
    menor=c
#Verificando quem é maior
maior=a
if b > a and b > c:
    maior=b
if c > a and c > b:
    maior=c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

"""
No geral é o mesmo mostrado no vídeo, porém eu não vi a necessidade 
de realizar b<a e b<c, ou o inverso para o maior, se já estamos comparando 
todos os 3 números em sequência começando pelo a. 

Para exemplificar vou pegar o resultado do maior, o maior começa com o valor A,
em seguida já testamos se o valor B é maior que o A, caso seja, o atributo 
maior irá receber B, caso contrário continuará com A.

Passando para a próxima condição, se o valor C for maior que o valor que 
estiver em maior, o atributo maior irá receber o valor C,caso contrário irá 
continuar com o valor anterior.

Não há necessidade de testar novamente se o C é maior que o A ou não. 
Pois se o B foi maior que o A, e o C for maior que o B, pela lógica o C 
também será maior que A, sem haver necessidade de testar isso novamente.
"""
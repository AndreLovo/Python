#https://www.youtube.com/watch?v=0LB3FSfjvao&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH
lanche=('hamburguer', 'suco', 'pizza', 'pudim', 'batata_frita')#variavel composta

print('---------------------------')

for cont in range(0, len(lanche)):
   print(f'Eu vou comer {lanche[cont]}')
print('comi pra caramba!')

print('---------------------------')

for comida in lanche:
   print(f'Eu vou comer{comida}')

print('---------------------------')

for pos, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {pos}')

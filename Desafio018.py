import math
ângulo=float(input('Entre com o angulo que você deseja:'))
seno= math.sin(math.radians(ângulo))
print('O ângulo de {} tem o seno de {:.3f}'.format(ângulo,seno))
cosseno= math.cos(math.radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.3f}'.format(ângulo,cosseno))
tangente= math.tan(math.radians(ângulo))
print('O ângulo de {} tem a tangente de {:.3f}'.format(ângulo,tangente))

from math import radians, sin, cos, tan
ângulo=float(input('Entre com o angulo que você deseja:'))
seno= sin(radians(ângulo))
print('O ângulo de {} tem o seno de {:.3f}'.format(ângulo,seno))
cosseno= cos(radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.3f}'.format(ângulo,cosseno))
tangente= tan(radians(ângulo))
print('O ângulo de {} tem a tangente de {:.3f}'.format(ângulo,tangente))
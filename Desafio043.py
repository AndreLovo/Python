peso=float(input('Qual é o seu peso? (Kg)'))
altura=float(input('Qual é a sua altura? (m)'))
imc= peso/(altura**2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do PESO normal')
elif 18.5 <= imc < 25:
    print('PARAÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA!')
preco = float(input('Qual Preço Normal do Produto ?: R$'))
resultado = 0
print('Qual condição de pagamento ?')
print('1 - A vista Dinheiro/Cheque: 10% de desconto')
print('2 - A vista no cartão: 5% de desconto')
print('3 - Em até 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')
condicao = int(input('Condição [1,2,3,4]: '))

if condicao == 1:
    resultado = preco - (10/100)*preco
elif condicao == 2:
    resultado = preco - (5/100)*preco
elif condicao == 3:
    resultado = preco
    parcelas = resultado/2
    print('Com parcela de 2x de R${:.2f} no cartão (SEM JUROS),'.format(parcelas), end='')
elif condicao == 4:
    quantparcelas = int(input('Quantas parcelas ?'))
    resultado = preco + (20/100)*preco
    parcelas = resultado/quantparcelas
    print('Parcelado em {}x de R${:.2f} (COM JUROS)'.format(quantparcelas, parcelas), end=' ')
else:
    resultado = preco
    print('Opção Inválida.Tente Novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, resultado))
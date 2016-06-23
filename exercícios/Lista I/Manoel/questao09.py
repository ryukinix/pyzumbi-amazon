s = int(input('Distância percorrida: '))
days = int(input('Dias pelo qual o carro foi alugado: '))
price = 60 * days + 0.15 * s
print('O preço a ser pago é: R$%.2f' %price)

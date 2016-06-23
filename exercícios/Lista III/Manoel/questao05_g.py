'''
	Dados dois números inteiros positivos, determinar o máximo divisor
	comum entre eles usando o algoritmo de Euclides.
	Exemplo: mdc(21, 15) = 3
	 a b 	a % b
	21 15	  6
	15 6 	  3
     6 3	  0
     		  ^ --> isso prova, portanto, que o mdc desses números é 3.
'''
a = int(input('a: '))
b = int(input('b: '))
while a % b != 0:
	a, b = b, a %b
print('mdc = %d' %b)
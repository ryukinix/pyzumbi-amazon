'''
	A sequência de Fibonacci é a seguinte:
		1, 1, 2, 3, 5, 8, 13, 21, 34, 55 (...)
	Sua regra de formação é simples: os dois primeiros elementos são 1;
	a partir de então, cada elemento é a soma de dois anteriores.
	Faça um algoritmo que leia um número inteiro calcule o seu número
	de Fibonacci. F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, etc.
'''
x = int(input("Insira o termo Fibonacci: "))
a, b = 1, 1
k = 0
while k < (x - 2):
	a, b = b, (a + b)
	k = k + 1
print('F(%d)=%d' %(x, b))

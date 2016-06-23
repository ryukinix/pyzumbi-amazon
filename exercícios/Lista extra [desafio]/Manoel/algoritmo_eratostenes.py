#Implementação do crivo de eratóstenes
from math import *
from time import clock

def primesIterable(n):
	primes = []
	for i in range(2, n):
		p = True
		for j in range(2, i):
			if i % j == 0:
				p = False
				break
		if p:
			primes.append(i)
	return primes

def primesEratostenes(n):
	primesRange = int(sqrt(n)) + 1
	primes = primesIterable(primesRange)
	lista = list(range(2, n + 1))
	for p in primes:
		for num in lista:
			if num % p == 0:
				lista.remove(num)
	return lista

def main():
	n = int(input('Calcular números primos até: '))
	time1 = clock()
	#calculando pelo algoritmo de eratostenes
	print('~Eratostenes Algorithm~')
	lista = primesEratostenes(n)
	time1 = clock() - time1
	print('Tempo de cálculo usando crivo de eratostenes %4.5fs' %time1)

	print('~Calculo Iterativo~')
	time2 = clock()
	lista = primesIterable(n)
	time2 = clock() - time2
	
	print('Tempo de cálculo usando calculo iterativo %4.5fs' %time2)

	print('Diferença de tempo: %4.5f' %abs(time2 - time))
	x = input('Pressione enter para sair...')

if __name__ == '__main__':
	main()

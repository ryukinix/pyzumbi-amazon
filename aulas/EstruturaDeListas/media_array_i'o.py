#leia 4 números positivos, então imprima eles e sua média!
array = []
n = 1
while n <= 4:
	i = int(input('Digite um número positivo: '))
	array.append(i)
	n += 1
n, sum_array = 3, 0
while n >= 0:
	sum_array += array[n]
	n -= 1
print(array, 'em que sua média é: ', sum_array / 4)
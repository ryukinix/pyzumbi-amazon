#leia 4 números positivos, então imprima eles e sua média!
#versão mais concisa
array, n, sum_array = [], 0, 0
while n <= 3:
	i = int(input('Digite um número positivo: '))
	array.append(i)
	sum_array += array[n]
	n += 1
print(array, 'em que sua média é: ', sum_array / 4)
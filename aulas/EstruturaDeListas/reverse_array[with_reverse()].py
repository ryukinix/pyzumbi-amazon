#Invertendo um array com 10 elementos que foram inseridos pelo usuário
array = []
n = 1
while n <=10:
	x = input('Insira um número real: ')
	array.append(x)
	n += 1
array.reverse()
print('O inverso dessa lista é:', array)
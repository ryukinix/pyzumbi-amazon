#encoding=utf-8
def check_repeat(x):	#verifica se há dois números iguais consecutivos
	s = ''
	for char in x:
		s = s + char
		if len(s) > 1 and s[-2] == char:
			return True
	return False
def sumnums(x):		#soma os algarismos entre si de um número
	c = 0
	for n in x:
		c += int(n)
	return c 
def check(x):		#verifica todas as condições
	if check_repeat(x) == False:
		if sumnums(x) % 2 == 0:
			if x[-1] != x[0]:
				return True
	return False
	
k = 0
numbers_clean = ''

with open('numbers.txt') as numbers:
	numbers = numbers.read()
	for char in numbers:
		if char == '\n':
			numbers_clean = numbers_clean + ' '
		else:
			numbers_clean = numbers_clean + char
	print(numbers_clean)
	array = numbers_clean.split()
	print(array)
	for phone in array:
		if check(phone) == True:
			k += 1
print('A quantidade de números válidos é: %d' %k)

			


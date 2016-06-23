#sortear 10 números aleatórios entre 1 a 100, então elecionar entre eles o maior e menor sem usar as funções max() e min().
from random import randint
array = []
big = 1
small = 100
while len(array) < 10:
	array.append(randint(1, 100))
for x in array:
	if x >= big:
		big = x
	if x <= small:
		small = x
print('A lista aleatória é: ', array, '\nO maior e menor são: %d e %d' %(big, small))

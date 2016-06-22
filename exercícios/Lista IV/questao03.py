'''
Crie dois vetores com 10 elementos aleatorios entre 1 e 100. Então gere
um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.
'''      
from random import randint

def generate(x): #gera_uma_lista_com_10_números_aleatórios.
	array = []
	while len(array) < x:
		array.append(randint(1, 100))
	return array

array = []
while len(array) < 2: #insere duas sublistas com 10 elementos aleatórios no 'array'.
	array.append(generate(10))
array.append([])
for k in range(0, 10): #intercala as duas ultimas sublistas em uma nova sublista dentro de 'array'.
	array[2].append(array[0][k])
	array[2].append(array[1][k])

print(array[0])
print(array[1])
print(array[2])

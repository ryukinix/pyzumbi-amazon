'''
Sortei 20 inteiros entre 1 e 100 num array. A partir desse array então colete dados e crie mais 2 arrays com respectivos conteúdos:
PAR, ÍMPAR
Imprima as três listas
'''
from random import randint
x, array, par, impar = 0, [], [], []
while x < 20:
        array.append(randint(1, 100))
        x = len(array)	 #contador
        y = x - 1 		#index
        if array[y] % 2 == 0:
                par.append(array[y])
        else:
                impar.append(array[y])

print('Array: ', array, '\nPar: ', par, '\nImpar: ', impar)

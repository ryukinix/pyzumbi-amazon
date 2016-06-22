#Invertendo um array com 10 elementos que foram inseridos pelo usuário (sem métood reverse())
array = [] #Variáveis
n = 0
m = 0
while n <=9:	#escopo de entrada
	x = input('Insira um número real: ')
	array.append(x)
	n += 1

print('Normal: ', array) #impressão da lista

while n >= 5 and m <= 5:	#inversão da lista
        n -= 1
        array[n], array[m] = array[m], array[n]
        m += 1
print('Invertida: ', array)

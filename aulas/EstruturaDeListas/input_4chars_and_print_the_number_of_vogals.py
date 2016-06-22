#ler 10 letras minusculas e dizer quantas são consoantes
array = []
n = 1
vogals = ['a', 'e', 'i', 'o', 'u']
consoantes = 0
while n <= 10:
	i = input('Digite uma letra minúscula: ')
	if i not in vogals:
		consoantes += 1
	n += 1
print('O número de consoantes que foi informado é igual a %d' %consoantes)
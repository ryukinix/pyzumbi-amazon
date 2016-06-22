#trocando vogais por '*' numa palavra com letras minúsculas e sem acentos.
vogals = ['a', 'e', 'i', 'o', 'u' ]
x = input('Escreva uma palavra com letras minúsculas e sem acentos: ')
y = len(x)
n = 0
while n < y:
	if x[n] in vogals:
		z = x[0:n]
		x = '*' + x[(n +1):y]
		x = z + x 
	n += 1
print("Trocando as vogais por '*' temos a seguinte string: ", x)  
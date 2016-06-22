#trocar vogais por * na string.
x = input("Digite uma palavra com letras minúsculas e sem acentos: ")
vogals = ['a', 'e', 'i', 'o', 'u']
string = ''
n = 0
while n < len(x):
	if x[n] in vogals:
		string = string + '*'
	else:
		string = string + x[n]
	n += 1
print("A nova palavra com '*' em vez de vogais é: %s" %string)
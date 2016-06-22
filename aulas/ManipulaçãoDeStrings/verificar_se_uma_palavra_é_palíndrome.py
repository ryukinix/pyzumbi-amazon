#manipulação com strings
#verificar se um número é palíndrome
x = input('Insira uma palavra com letras minúsculas sem acento: ')
if x == x[::-1]:
	print('Essa palavra é palíndrome!')
else:
	print('Essa palavra não é palíndrome!')

'''
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo.
A própria palavra leet admite muitas variações, como l33t ou 1337. 
O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet,
sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak. 
'''
k = {'a':'4', 'e':'3', 'i':'1', 'o':'0','s':'5', 't':'7','b':'8'}
text = input('Escreva uma frase ou texto: ')

new_text = ''
for c in text:
	c = c.lower()
	if c in k:
		new_text += k[c]
	else:
		new_text += c

print(new_text.upper())



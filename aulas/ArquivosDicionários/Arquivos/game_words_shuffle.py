'''
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. 
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''
import random, string
from time import sleep
archive = open('words.txt')		#banco de palavras
words = archive.read()  
for c in string.punctuation:	#limpa caracteres estranhos
	words.replace(c, ' ')

words = words.split()			#cria uma lista com todas as palavras do bancos

a = random.choice(words)		#escolhe uma palavra qualquer

word = list()
for char in a:					#insire cada uma das letras separadas em uma lista(word)
	word.append(char)	
	
random.shuffle(word)			#embaralha as letras

word = ''.join(word)			#converte a lista em uma 'palavra'



k = int()
while k < 7:					#lógica do game
	print('%s' %word)
	x = input('Que palavra é essa? %d-life(s)' %(6 - k))
	if x.lower() == a.lower():
		print("Parabéns! A palavra certa era %s mesmo! Seu safado!" %a.capitalize())
		sleep(10)
		quit()
	elif k < 6 :
		print('Você errou, tente novamente')
	k += 1
print('Suas chances acabaram. A palavra correta era: %s' %a.capitalize())
sleep(10)


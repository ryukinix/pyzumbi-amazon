#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os
from aux_functions import readWords, cleanWords, reporthook
from random import * 
from string import ascii_lowercase as lowerLetters

url = 'http://www.ime.usp.br/~pf/algoritmos/dicios/br'
forca = ["        +------+\n",
		 "        !      !\n",
		 "        O      !\n",
		 "       /|\\     !\n",
		 "       / \     !\n",
		 "               !\n",
		 "               !\n"
		 "================\n"]
messages = [["     LoSER!    !\n", "SAD. YoU LoST. !\n", "     STUPID!   !\n", "     STUPID!   !\n"], \
			["     MASTER!   !\n", " YES!  I WIN!  !\n", "     SAVED!    !\n", "    GAMEoVER!  !\n"]]

pices = "O/|\\"

def drawForca(forca, pices, erros):
	count = 0;
	for part in forca:
		for c in part:
			if count >=  erros:
				if c in pices:
					c = ' '
			elif c in pices:
				count += 1
			print(c, end ='')

def drawWord(word, corrects):
	print("Word: ", end = '')
	for i in word:
		if i in corrects:
			print(i, end = ' ')
		else:
			print('_', end = ' ')
	print()

def drawGame(word, corrects, wrongs, mensagem = False):
	global forca, pices
	if mensagem != False:
		before = forca[5]
		forca[5] = mensagem
		corrects = word
	##forca
	drawForca(forca, pices, len(wrongs))
	#word
	drawWord(word, corrects)
	
	if mensagem != False:
		forca[5] = before

def sortedWord(words):
	return choice(words)

def chute(letras):
	new = input("Chute uma letra: ").lower()
	if len(new) > 1:
		print("Eu disse uma... vamos tentar novamente.")
		return chute(letras)
	elif new not in lowerLetters or len(new) == 0:
		print("Desde quando isso é uma letra? Tente outra vez.")
		return chute(letras)
	elif new in letras:
		print("Essa já foi tentada.")
		return chute(letras)
	return new

def winOrLost(word, correctLetters, wrongLetters):
	global deadMessage, person, messages
	if len(wrongLetters) >= 6:
		drawGame(word, correctLetters, wrongLetters, mensagem = choice(messages[0]))
		return False
	elif win(word, correctLetters):
		drawGame(word, correctLetters, wrongLetters, mensagem = choice(messages[1]))
		print('Parabéns! Você se salvou!')
		return False
	return True

def win(word, correctLetters):
	for c in word:
		if c not in correctLetters:
			return False
	return True

def again():
	question = input('Jogar novamente?[s][n]: ')
	if question.lower() in 'sim':
		return True
	elif question.lower() in 'nao':
		return False
	else:
		print("Reposta Inválida!")
		return again()
def game(words):
	if os.name == 'nt':
		clear_command = 'cls'
	else:
		clear_command = 'clear'
	word = sortedWord(words)
	correctLetters = ''
	wrongLetters =  ''
	running = True
	while running:
		os.system(clear_command)
		print("Corretas: %s | Erradas: %s" %(correctLetters, wrongLetters))
		drawGame(word, correctLetters, wrongLetters)
		new = chute(correctLetters + wrongLetters)

		if new in word:
			correctLetters += new
		else:
			wrongLetters += new

		running = winOrLost(word, correctLetters, wrongLetters)

	if again():
		game(words)
if __name__ == '__main__':
	words = cleanWords(readWords(url))
	print("\rJogo da forca! By Neto")
	game(words)

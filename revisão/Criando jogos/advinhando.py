#coding=utf-8
#advinhando
from random import randint
n = randint(1, 100)
k, i = 0, 0
while True:
	x = int(input("Chute um número: "))
	if x == n:
		print('Você venceu! A resposta era realmente %d' %n)
		break
	else:
		print("Maior" if x > n else "Menor")
	i += 1

print('Fim de jogo! Tentativa necessarias para ganhar o jogo: %d' %i)

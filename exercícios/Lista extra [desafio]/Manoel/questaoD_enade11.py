# Questão D. (Enade 2011) No livro “O Homem que Calculava”, de Malba Tahan, um personagem desejava
# ganhar os grãos de trigos que fossem distribuídos sobre um tabuleiro de xadrez do seguinte modo: um
# grão na primeira casa do tabuleiro, o dobro (2) na segunda, novamente o dobro (4) na terceira, outra vez o
# dobro (8) na quarta, e assim por diante, até a sexagésima quarta casa do tabuleiro. Faça um algoritmo que
# calcule a quantidade total de grãos de trigos necessários para realizar esta distribuição.

# sum n = (q^n - 1)/q - 1

def progressGeometric(n, r):
	for i in range(n):		
		yield r
		r = r * 2
def pointsNumber(n):
	n = str(n)
	if len(n) > 3:
		n = n[::-1]
		newString = ''
		for i in range(len(n)):
			if i % 3 == 0 and i != 0:
				newString += '.'
			newString += n[i]
		return newString[::-1]
	return n

seeds = 0
for i in progressGeometric(64, 1):
	seeds += i

print('Sum of seeds: ',  pointsNumber(seeds), '! D:')



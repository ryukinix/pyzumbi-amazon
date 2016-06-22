# Questão E (OBI ensino médio). São dados N azulejos de dimensões 10cm × 10cm. Com eles, você deve
# montar um conjunto de quadrados (com espessura de um azulejo) de modo a utilizar TODOS os azulejos
# dados. Inicialmente você deve montar o maior quadrado possível com os azulejos dados; então, com os
# azulejos que sobraram, você deve montar o maior quadrado possível, e assim sucessivamente. Por
# exemplo, se forem dados 31 azulejos, o conjunto montado terá quatro quadrados, conforme ilustra a
# figura abaixo. Faça uma função que recebe o número de azulejos e calcule quais quadrados são montados.
# Suponha que não teremos mais que 400 azulejos e teste para 76, 290 e 347 azulejos. No exemplo abaixo a
# resposta seria:
from math import sqrt


def squares(n, lista = []):
	s = int(sqrt(n)) 
	n = n - (s * s)
	lista.append(s)
	if n > 0:
		squares(n, lista)
	return lista
def count(sqrs):
	dic = dict()
	for i in sqrs:
		if i not in dic:
			dic[i] = 1
		else:
			dic[i] += 1
	return dic
def tests():
	for teste in [76, 290, 347]:
		sqrs = count(squares(teste))
		print('\nTeste para %d azulejos' %teste)
		for i in sorted(sqrs, reverse = True):
			print('%d quadrado(s) de %d lado(s)' %(sqrs[i], i))

if __name__ == '__main__':
	tests()
	input('Pressione enter para sair...')

# Seletiva Facebook Hackaton 2013
# Dados dois inteiros positivos n e k, gerar todos os binários entre os inteiros 0 e 

# 2**n-1, inclusive. Estes binários serão sorteados em ordem descrescente segundo o 

# números de 1s existentes. Caso haja empate escolhemos o menor valor númerico. 

# Retorne o k-ésimo elemento da lista sorteada. Dicas: use count, bin e uma função 

# para sortear por outra chave.
 
# Ex.: n = 3 e k = 5
# ['0b111', '0b11', '0b101', '0b110', '0b1', '0b10', '0b100', '0b0']

# quinto elemento '0b1'

# n = 4 
# ['0b1111', '0b111', '0b1011', '0b1101', '0b1110', '0b11', '0b101', '0b110', 

# '0b1001', '0b1010', '0b1100', '0b1', '0b10', '0b100', '0b1000', '0b0']

# n = 5 
# ['0b11111', '0b1111', '0b10111', '0b11011', '0b11101', '0b11110', '0b111', '0b1011', 

# '0b1101', '0b1110', '0b10011', '0b10101', '0b10110', '0b11001', '0b11010', 

# '0b11100', '0b11', '0b101', '0b110', '0b1001', '0b1010', '0b1100', '0b10001', 


# '0b10010', '0b10100', '0b11000', '0b1', '0b10', '0b100', '0b1000', '0b10000', '0b0']



def existInDic(dic, n, acrescimo):
	if n in dic:
		div = 10 ** len(str(acrescimo)) 
		print(acrescimo, div, acrescimo / div)
		n += acrescimo / div
		return existInDic(dic, n, acrescimo)
	return n
def lenghtBin(n):
	lenght = 0
	for i in range(n):
		lenght += 2 ** i
	return lenght
def binGenerator(n):
	lenght = lenghtBin(n)
	for i in range(lenght + 1):
		yield bin(i)
def dicBins(n):
	bins = binGenerator(n)
	dic = {}
	for b in bins:
		n = b.count('1')
		acres = int(b, 2)
		n = existInDic(dic, n, -acres)
		dic[n] = b
	return dic
def sortedBins(dic):
	lista = []
	for b in sorted(dic, reverse = True):
		lista.append(dic[b])
	return lista

n = int(input("Insira o número n binário: "))
p = int(input("Qual indice pesquisar?"))

dic = dicBins(n)
sortedBins = sortedBins(dic) 
print(dic)

for i in sortedBins:
	print(i)
print('K:', sortedBins[p])

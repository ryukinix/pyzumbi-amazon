arq = open('alice.txt', encoding='utf-8')
alice = arq.read()
alice = alice.lower()
import string 
for c in string.punctuation:
	alice.replace(c, ' ')
alice = alice.split()

x = input('Qual palavra deseja buscar e contar?').capitalize()
dic = {}

for word in alice:
	if word.lower() not in dic:
		dic[word] = 1
	else:
		dic[word] += 1
print('%s aparece %s vezes' %(x, dic[x.lower()]))
arq.close()

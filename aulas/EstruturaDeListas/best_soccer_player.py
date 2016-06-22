'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos.
Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++.
Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. 
Um número de jogador igual zero, indica que a votação foi encerrada. 
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:

   1.O total de votos computados;
   2.Os números e respectivos votos de todos os jogadores que receberam votos;
   3.O percentual de votos de cada um destes jogadores;
   4.O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.


Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. 
O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. 
Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco,
obedecendo a mesma disposição apresentada na tela. 
'''
array, votes, k = [], [], 0
def percent(x):
	global k
	percent = x*100/k
	return percent
while True:
	try: 
		x = int(input('Digite o número do jogador: '))
		if x == 0:
			break
		if x > 0 and x <= 23:
			if x not in array:
				array.append(x)
				votes.append(1)
			else:
				i = array.index(x)
				votes[i] += 1
		else:
			print('Número de jogador inválido! Tente novamente.')
		k += 1
	except ValueError:
		print('Tipo de dado incorreto, tente novamente.')
print(array, votes, k)

n = 0
results = ['Total de votos: %d' %k]
while n < len(array):
	y = percent(votes[n])
	string = 'O jogador %d teve %d votos, na qual corresponde a %d%% em relação ao total.' %(array[n], votes[n], y)
	results.append(string)
	n +=1

best_player_votes = max(votes)
best_player = array[votes.index(best_player_votes)]
string = 'Um dos jogadores mais votado é o %d, com %d votos ( %d%% )' %(best_player, best_player_votes, percent(best_player_votes))
results.append(string)
 
arq = open('best_player_soccer.txt', 'w')
for c in results:
	print(c)
	arq.writelines('%s\n' %c)
arq.close()






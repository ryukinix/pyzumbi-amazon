# Questão A (Vestibular FATEC 2008). Uma escola do Ensino Fundamental ofereceu a alguns de seus alunos um passeio ao zoológico.
# Para tanto, a escola pretende gastar EXATAMENTE 93 reais e sabe que o ingresso do zoológico custa 5 reais para os menores de 12 anos
# e 7 reais os que têm 12 anos ou mais. 
# Elabore um algoritmo que retorne o número máximo de alunos que a escola pode levar ao zoológico
# considerando todos os valores como inteiros. 
# O seu programa deve ter uma abordagem genérica e não levar em conta peculiaridades nos dados fornecidos.  
def maxStudents(n):
	students, n = n // 5, n % 5
	students += n // 7
	return students

# Questão B. Conversor de decimal para romano. 
# Você deverá programar um algoritmo em Python que traduza um número lido no sistema arábico para romano. 
# Evite fazer muitos “ifs”.
# A idéia é usar um comando while para analisar cada casa decimal e gerar os caracteres romanos diferentemente para cada iteração.
# Exemplo 2011 = MMXI em romano. Não precisa testar até o infinito, basta de 1 até 2013.  
def dec_rom(decimal, romano = '', i = 0):
	dic = { 1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
	lenght = len(str(decimal))
	while i < lenght:
		n_dec = str(decimal)[i]
		value =  int(n_dec) * 10 ** (lenght -(i + 1))
		if value > 0:
			for m in [1, 2, 3, 4, 5]:
				if value / m in dic:
					romano += dic[value / m ] * m
					return dec_rom(decimal, romano,  i + 1)	
			for romValue  in sorted(dic, reverse = True):
				if romValue  > value:
					resto = romValue  % value
					if resto in dic and romValue  == value + resto:
						romano += dic[resto] + dic[romValue]
						return dec_rom(decimal, romano, i + 1)
				elif value > romValue:
					resto = value % romValue
					for m in [1, 2, 3]:
						if resto / m in dic:
							romano += dic[romValue] + dic[resto / m] * m
							return dec_rom(decimal, romano,  i + 1)
		i += 1
	return romano

# Questão C. Faça um programa que calcule o valor aproximado de pi com n termos, segundo a fórmula abaixo. 
# No exemplo são visíveis 4 termos. 4/1 - 4/3 + 4/5 - 4/7 ... 4/n
def piaprox(n):
	i = 0
	div = 1; sinal = 4; termos = 0
	pi = 0
	while termos < n:
		if i % 2 != 0:
			div = i
			x = sinal / div
			pi += x
			sinal = - sinal
			termos += 1
		i += 1

	return pi

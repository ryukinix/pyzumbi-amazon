#Autor: Manoel Vilela | Criado às 08:48 em 07/05/2014
t = 0
a = 80000
b = 200000
while a <= b:
	a = a + 0.03*a
	b = b + 0.015*b
	t = t + 1
print("O tempo necessário para que A ultrapasse B é de %d anos" %t)


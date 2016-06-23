x = 1067
y = 3627
k = 0
for n in range(x, y + 1):
	if n % 2 == 0 and n % 7 == 0:
		k += 1
print('A quantidade de números entre %d e %d que completam tal sentença é: %d' %(x, y, k))

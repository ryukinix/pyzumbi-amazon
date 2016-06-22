x = 18644
y = 33087
k = 0
for n in range(x, y +1):
	if '2' in str(n):
		if '7' not in str(n):
			k += 1
print(k)

a = open('chars.txt', 'w')
for x in range(300, 10000):
    s = chr(x)
    a.write('%s = %s \n' %(x, s))
a.close()
	

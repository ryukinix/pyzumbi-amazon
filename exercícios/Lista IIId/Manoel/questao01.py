#Python!
#Verificando se um número é triangular | Manoel Vilela | 10:06 24/05/2014

a = int(input("Digite um número:"))
x, y, z = 1, 2, 3
produto = 1

while produto < a:
    produto = x * y * z
    if produto == a:
        print("O número %d é triangular, pois %d*%d*%d = %d" %(a, x, y, z, produto))
        break
    z = z + 1
    y = y + 1
    x = x + 1
if produto != a:
    print("%d não é triangular" %a)

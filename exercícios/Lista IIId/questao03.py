#Python!
#Verificar se um número é primo ou não.
x = int(input("Digite um número:"))
n = 2

while n < x:
    r1 = x % n
    if r1 == 0 and x != 2:
        print("%d não é primo e é múltiplo de %d." %(x, n))
        break
    n = n + 1
if r1 != 0:
    print("%d é um número primo." %x)

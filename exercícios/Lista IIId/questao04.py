#Python
#Decompor em números primos!
x = int(input("Digite um número a ser decomposto: "))
entry = x
n = 2
lista = []
while n <= x:
    while x % n == 0:
        m = str(n)
        lista.append(m)
        x = x / n
    n = n + 1
string = '*'.join(lista)
if len(lista) is 1:
    print("%d é um número primo!" %(entry))
else:
    print("A decomposição é: %d=%s" %(entry, string))

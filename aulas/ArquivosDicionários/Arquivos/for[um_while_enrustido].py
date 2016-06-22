#relação entre while e for.
a = 'Iteração For: '
b = 'Iteração While: '

#Exemplo_1

print(a)
#for
for letra in 'aeiou':
	print(letra)

print(b)
#while
k = 0
n = 'aeiou'
while k < len(n):
	letra = n[k]
	print(letra)
	k = k + 1

#Exemplo_2 [with range()]

print(a)
#for
for x in range(0, 11):
	print(x)
print(b)
#while
k = 0
array = list(range(0, 11))
while k < len(array):
	valor = array[k]
	print(valor)
	k = k + 1

#Exemplo_3 [vários tipos em uma só lista]

lista = [42, 3.14, 'Limbo']

print(a)
#for
for i in lista:
	print(i)

print(b)
#while
k = 0
while k < len(lista):
	valor = lista[k]
	print(valor)
	k = k + 1

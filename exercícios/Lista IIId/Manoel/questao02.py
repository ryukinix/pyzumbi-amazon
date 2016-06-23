#Python
#Verificando troco em cédulas
bill = int(input("Conta:"))
money = int(input("Pagamento:"))

troco = money - bill

notas = []
while troco >= 50:
    troco = troco - 50
    notas.append(50)
while troco >= 20:
    troco = troco - 20
    notas.append(20)
while troco >= 10:
    troco = troco - 10
    notas.append(10)
while troco >= 5:
    troco = troco - 5
    notas.append(5)
while troco >= 2:
    troco = troco - 2
    notas.append(2)
while troco >= 1:
    troco = troco - 1
    notas.append(1)

print("Para que seja usado um número mínimo de notas, o troco deve ser dado da seguinte forma:")
print(notas)

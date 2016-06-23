#Python!
#Criado por Manoel Vilela | 01/05/2014 às 07:00 AM | Corrigido em 13/05/2014
x, y, z = [int(input("Digite um número:")), int(input("Digite um número:")), int(input("Digite um número:"))]
if x >= y and x >= z:
    print(x, "é o maior")
elif y >= z:
    print(y, "é o maior")
else:
    print(z, "é o maior")
if x  <= y and x <= z:
    print(x, "é o menor")
elif y <= z:
    print(y, "é o menor")
else:
    print(z, "é o menor")
    

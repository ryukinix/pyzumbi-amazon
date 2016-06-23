#Python!
#Criado por Manoel Vilela | 01/05/2014 às 06:30 AM
x, y, z = [int(input("Digite um número:")), int(input("Digite um número:")), int(input("Digite um número:"))]
if x > y and x > z:
    print(x, "é o maior")
    if y < z:
        print(y, "é o menor")
    else:
        print(z, "é o menor")
elif y > x and y > z:
    print(y, "é o maior")
    if x < z:
        print(x, "é o menor")
    else:
        print(z, "é o menor")
else:
    print(z, "é o maior")
    if y < x:
        print(y, "é o menor")
    else:
        print(x, "é o menor")
                                               

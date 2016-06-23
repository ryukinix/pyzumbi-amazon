#Python!
#Criado por Manoel Vilela | 01/05/2014 às 05:17 AM
#A condição de existência de um triângulo:"A medida de qualquer um dos lados deverá ser menor que a soma das medidas dos outros dois."
a, b, c = [int(input("1ª lado: ")), int(input("2ª lado: ")), int(input("3ª lado: "))]
if a > b + c or b > a + c or c > a + b or 0 in [a, b, c]:
    print("Esses lados não podem formar um triângulo.")
elif [a, b, a] != [b, c, c]:
    print("Esses lados formam um triângulo escaleno.")
elif a == b == c:
    print("Esses lados formam um triângulo equilátero.")
else:
    print("Esses lados formam um triângulo isósceles.")

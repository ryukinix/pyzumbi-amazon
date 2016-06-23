#Autor: Manoel Vilela | 11/05/2014 às 02:22 
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
if a > b:
    r1 = a % b
    if r1 == 0:
        print("O máximo divisor comum entre %d e %d é %d" %(a, b, b))
    else:
        while r1 > 0:
            r2 = a % r1
            r3 = b % r1
            if r2 == 0 and r3 == 0:
                print("O máximo divisor comum entre %d e %d é %d." %(a, b, r1))
                break
            r1 = r1 - 1
else:
    r1 = b % a
    if r1 == 0:
        print("O máximo divisor comum entre %d e %d é %d" %(a, b, a))
    else:
        while r1 > 0:
            r2 = b % r1
            r3 = a % r1
            if r2 == 0 and r3 ==0:
                print("O máximo divisor comum entre %d e %d é %d" %(a, b, r1))
                break
            r1 = r1 - 1
if r1 != 0 and r2 != 0:
    print("Os números %d e %d não possuem divisor comum." %(a, b)) 

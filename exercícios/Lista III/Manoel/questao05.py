#Python!
#Autor: Manoel Vilela | Criado às 06:52 em 12/05/2014
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
if a > b:  #atribuindo variáveis fixas para as entradas a e b. x = maior;y = menor
    x, y = a, b
else:
    y, x = a, b

r1 = x % y
r2 = 2   

if r1 == 0:
    print("O maior divisor comum entre %d e %d é o próprio %d" %(a, b, y))
else:
    while r2 > 1 and r1 > 1:        
        r2 = y % r1
        if r2 == 0:
            print("O maior divisor comum entre %d e %d é %d" %(a, b, r1))
            break
        y, r1 = r1, r2      #próximo dividendo será o resto da penúltima divisão(r1); próximo divisor será o resto da última divisão(r2).
if r2 != 0:
    print("%d e %d não possuem divisores comuns" %(a, b))

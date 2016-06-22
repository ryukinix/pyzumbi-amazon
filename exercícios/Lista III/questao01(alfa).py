x = -1 
while 1 > x or x > 10:
    x = int(input("Digite um número entre 0 a 10: "))
    if 1 > x or x > 10:
        print("Valor ínvalido, tente novamente")
    else:
        print("Valor aceito. Você digitou %d" %(x))

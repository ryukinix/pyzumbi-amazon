while True:
    x = int(input("Digite um número entre 0 a 10: "))
    if 0 <= x <= 10:
        print("Você digitou %d. Valor aceito." %x)
        break
    print("Tente novamente, %d é um valor inválido." %x)

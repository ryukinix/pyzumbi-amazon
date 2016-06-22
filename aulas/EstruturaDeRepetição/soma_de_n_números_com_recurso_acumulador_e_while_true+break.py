soma = 0
while True:
    x = int(input("Digite um número inteiro a ser somado e 0 pra parar: "))
    if x == 0:
        break
    soma = soma + x
print("A soma é igual a: %d " %soma)

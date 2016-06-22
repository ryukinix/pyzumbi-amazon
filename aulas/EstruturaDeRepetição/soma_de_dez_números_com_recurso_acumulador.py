#Acumuladores
n = 1
soma = 0
while n <= 10: #usar while dessa forma, e n = n + 1 ao final do códgio, faz com que a execução passe por esse bloco 10 vezes.
    x = int(input("Insira o %dº número:" %n))
    soma = soma + x
    n = n + 1
print("Soma: %d"%soma)

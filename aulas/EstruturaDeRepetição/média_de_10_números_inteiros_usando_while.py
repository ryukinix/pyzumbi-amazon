#Cálculo da média de 10 números inteiros!
soma = 0
n = 1
while n <= 10:
    x = int(input("Insira o %dº número: " %n))
    soma = soma + x
    n = n + 1
media = soma/10
print("Média: %5.2f" %media)
    

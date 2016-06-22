#fatorial
#Autor: Manoel Vilela | Criado em 30/04/2014 às 18:54.
fat = 1
print("~Cálculo Fatorial~")
n = int(input("Digite um número: "))
number_entry = n
while n > 1:
    fat = fat * n  #corrigido entrada (n - 1) por n -- estava errado pois a multiplicação não começava do número n inicial| Fix it in 01/05/2014 às 02:03
    n = n - 1
length = len(str(fat))
if length < 5:
    print("O fatorial de %d! vale %d"%(number_entry, fat))
else:
    print("O fatorial de %d! Tem %s dígitos e vale essa porra aqui: %d"%(number_entry, length, fat))
my_min = int(input("Quantos minutos você usou durante esse mês?"))
if my_min < 200:
    count = my_min * 0.20
elif my_min <= 400:
    count = my_min * 0.18
elif my_min <= 800:
    count = my_min * 0.15
else:
    count = my_min  * 0.08
print ("O valor da sua conta é R$%5.2f" %count)



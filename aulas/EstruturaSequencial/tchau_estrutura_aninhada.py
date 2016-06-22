my_min = int(input("Minutos utilizados:"))
if my_min < 200:
    price = 0.20
else:
    if my_min <= 400:
        price = 0.18
    else:
        if my_min <= 800:
            price = 0.15
        else:
            price = 0.08
print ("Conta telefônica: R$%2.2f" %(my_min*price))

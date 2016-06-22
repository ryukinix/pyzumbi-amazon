#excess_velocity
from time import sleep
v = int(input("Qual a velocidade do carro?"))
if v > 110:
    exc = v - 110
    m = 5 * exc
    print ('Seu safado! Andando rápido, hein? A multa é de R$%d!' %m)
else:
    print ('Você é bem comportado!')
sleep(15)

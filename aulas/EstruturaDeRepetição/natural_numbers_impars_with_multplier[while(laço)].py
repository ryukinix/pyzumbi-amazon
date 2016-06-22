#While_Impars
#Com opção de insirir um multiplicador
from time import sleep
y = 1
x = int(input("Imprima números até: "))
z = int(input("Insira o multiplicador: "))
while y * z <= x:
    print(y * z)
    y = y + 2
sleep(10)

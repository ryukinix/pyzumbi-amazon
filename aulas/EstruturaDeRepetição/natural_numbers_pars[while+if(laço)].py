from time import sleep
y = 1
x = int(input("Imprima os números naturais até:"))
while y <= x:
    if (y % 2) == 0:
        print(y)
    y = y + 1
sleep(10)

tabuada = int(input("Começar a impressão em qual tabuada?"))
finish = int(input("E imprimir até que tabuada?"))
produto = int(input("Qual o produto máximo a se fazer em cada multplicação?"))
while tabuada <= finish:
    n = 1
    print("Tabuada do número %d"%tabuada)
    while n <= produto:
        valor = n * tabuada
        print("%d x %d = %d"%(tabuada, n, valor))
        n = n + 1
    tabuada = tabuada + 1

#Verificação se um número é primo ou não
#Recebe um número inteiro e como retorno, diz se tal número é primo ou múltiplo do número y.
#Autor: Manoel Vilela
#30/04/2014 às 01:49
x = int(input("Digite um número: "))
y = 2
while y <= x:
    if x % y == 0 and x != y:
        print("O menor múltiplo de %d é %d." %(x, y))
        break
    elif x == y or x == 2:
        print("%d é um número primo!" %(x))
    y = y + 1
        
    

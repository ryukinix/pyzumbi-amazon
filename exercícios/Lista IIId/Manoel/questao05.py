#Python!
#Pedir um número positivo e mostrá-lo invertido.
n=0
lista = []
while True:   #laço para tratamento de erro.
    try:
        x = input('Digite um número positivo: ')
        if int(x) > 0:
            break
        print('Valor não é positivo, tente novamente!')
    except ValueError:
        print('Tipo errado, tente novamente')

        
while n < len(x): #quebra de string em caracteres em uma lista
    lista.append(x[n])
    n += 1
invertido = lista.reverse()
string = ''.join(lista)
while string[0] == '0': #apagando zeros a esquerda
    string = string[1:]
print('Se tal número fosse invertido ficaria deste modo:', string)
    

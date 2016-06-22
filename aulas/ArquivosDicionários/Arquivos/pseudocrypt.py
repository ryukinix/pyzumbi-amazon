#leia um arquivo mensagem.txt e substitua todas as vogais por '*' escrevendo o resultado final em crypt.txt
'''
mensagem = open('mensagem.txt', 'w')
x = input("Escreva uma mensagem a ser gravada no arquivo 'temp': ")
mensagem.write(x)
mensagem.close()
'''
mensagem = open('mensagem.txt')
crypt = open('crypt.txt', 'w')
vogals = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'ã', 'é', 'í', 'ó', 'õ', 'ú']
s = ''
for i in mensagem.read():
    if i.lower() in vogals:
        s = s + '*'
    else:
        s = s + i
mensagem.close()
crypt.write(s)
crypt.close()
